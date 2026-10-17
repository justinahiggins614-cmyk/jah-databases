#!/usr/bin/env python3
"""Entries for the Savate Combat databases (combat batch 1, 2026-10-17).

Scope verified 2026-10-17: RAW SWEEP over the full manifest (2,386+
databases) plus every shard index title in jah-databases-data-1 (809 index
files): zero 'combat-savate*' slugs; zero savate-specific title collisions.
Whole-system dedupe pre-check (dedupe_gate vs the exact-title index): all
68 titles (34 public + 34 Signature-suffixed) checked, zero cross-database
refusals. ID prefixes JAH-CBSAV- / JAH-CBSAVS-: zero hits in manifest
id_prefix values and zero hits in all 809 shard index files.

So this build creates two NEW databases, 34 ladder-ordered records each:

  combat-savate             - The Savate Combat Database (public-harvest:
                              real, fact-checked French savate / boxe
                              francaise knowledge - shoe-based kicking, hand
                              strikes, the four kick families (fouette,
                              chasse, revers, coup de pied bas),
                              combinations - every record a technique with
                              HOW TO DO IT step-by-step body mechanics,
                              ladder-ordered from stance to advanced ring
                              tactics; standard references Charlemont
                              1878/1899, Baruzy, FISav, FFBFSDA)
  combat-savate-signature   - The Savate Combat Signature Database (his
                              original Signature Savate Method: the same
                              ladder through the Signature lens - every
                              kick a signed line, the guard a covenant of
                              balance, the combination an oath kept in
                              rhythm; src signature, titles suffixed
                              " (Signature Edition)", clearly labeled
                              Signature-made, never presented as authentic
                              public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_savate.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos before the pages
are written.

Screening: civilian martial-arts instruction only. No neutralizing of
military or defense-grade systems; no hate-adjacent, profane, or
inappropriate content; no religious talk. Never the words "bat belt"
anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Savate Method: the "
            "same ladder through the Signature lens, every kick a signed "
            "line, the guard a covenant of balance, the combination an oath "
            "kept in rhythm. Clearly labeled Signature-made, never presented "
            "as authentic public record.")

CIT_CHARLEMONT_1899 = ("Charlemont J. L'Art de la boxe francaise et du baton. "
                       "Paris; 1899. (Foundational French manual of savate "
                       "technique.)")
CIT_CHARLEMONT_1878 = ("Charlemont J. La Boxe francaise: traite theorique et "
                       "pratique. Paris; 1878.")
CIT_BARUZY = ("Baruzy P. Modern codification of boxe francaise; Academie de "
              "Boxe Francaise. (Standardization of the four kick families "
              "and competitive rules.)")
CIT_FISAV = ("Federation Internationale de Savate. Reglement sportif et "
             "technique. (International competition rules: assaut and "
             "combat formats, scoring, legal techniques.)")
CIT_FFBFSDA = ("Federation Francaise de Boxe Francaise, Savate et Disciplines "
               "Associees. Technical program: grades (gants), tireur "
               "curriculum.")

ENTRIES = ([
    {
        "key": "stance",
        "name": "La Garde: The Savate Stance",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "La garde is the savate stance, the platform every kick and punch "
            "launches from and returns to. Stand with feet about one and a "
            "half shoulder-widths apart: the lead foot points toward the "
            "opponent, the rear foot turns out about forty-five degrees, and "
            "the weight settles roughly sixty percent on the front leg and "
            "forty on the back. The knees stay soft and springy, never "
            "locked, so the body can rise, sink, and pivot without "
            "telegraphing. The torso turns slightly sideways to narrow the "
            "target, the chin tucks behind the lead shoulder, and both hands "
            "come up: lead hand at cheek height, rear hand at chin height, "
            "elbows tucked to shield the ribs. The rear heel lifts a finger's "
            "width off the floor so the back leg can drive and the foot can "
            "pivot on kicks. This is not a pose struck for a photograph; it "
            "is a loaded spring. Every savate technique begins by checking "
            "the guard, and every combination ends by snapping back to it, "
            "because a tireur out of guard is a tireur open to the fouette."
        ),
        "how_it_works": (
            "Build the stance from the ground up. Step one: place the feet. "
            "Set the lead foot pointing at the opponent and the rear foot "
            "angled forty-five degrees out, with about forty-five "
            "centimeters between them for a 1.75-meter tireur - wide enough "
            "to resist a push, narrow enough to move. Step two: bend the "
            "knees until they sit over the toes, which drops the center of "
            "mass to about ninety-five centimeters and puts the legs under "
            "spring tension. Step three: distribute the weight sixty "
            "percent front, forty percent back - press the front foot into "
            "the floor and feel the rear calf engage. Step four: lift the "
            "rear heel slightly and turn the torso a quarter-turn sideways. "
            "Step five: raise the hands - lead hand high at cheek level, "
            "rear hand guarding the chin, elbows pinned to the ribs. Step "
            "six: tuck the chin and set the eyes on the opponent's chest, "
            "which lets you see shoulders, hips, and feet move at once. Test "
            "it: have a partner push your shoulder; if the stance holds "
            "without a step, the base is wide enough. Rock forward and back "
            "on the balls of the feet - if you can shift without the head "
            "bobbing, the knees are doing their job. Return to this exact "
            "shape after every single technique; the demo computes the "
            "weight split, base width, and stability margin."
        ),
        "key_points": [
            "Feet: lead foot forward, rear foot at forty-five degrees, base about forty-five centimeters wide - the tripod the whole art stands on.",
            "Weight sixty percent front, forty percent back, knees soft over the toes, rear heel lifted a finger's width.",
            "Torso quarter-turned to narrow the target, chin tucked behind the lead shoulder, eyes on the opponent's chest.",
            "Hands: lead at cheek height, rear at chin, elbows tucked to the ribs - the wall every attack must cross.",
            "The guard is a round trip, not a pose: leave it for a technique, snap back to it the instant the technique lands.",
        ],
        "requirements": [
            "Flat training shoes with grip - savate kicks land with the shoe, so learn the stance in the footwear you will kick in.",
            "A clear floor space of at least two meters square, free of obstacles, for stance and partner-push testing.",
            "A mirror or a training partner to check the three sight-lines: foot angle, knee-over-toe, chin tucked.",
            "Three practice blocks of five minutes holding the stance, resting one minute between, before any kick is thrown.",
            "A coach or experienced tireur to verify the rear-heel lift and the sixty-forty weight split in the first week.",
        ],
        "standards": [
            "The stance follows the classical French school described by Charlemont: sideways body, high guard, springy legs.",
            "Weight distribution and base width scale with the tireur's height - the demo proportions hold for heights 1.60 to 1.90 meters.",
            "Guard position is checked at the start and end of every technique in assaut judging; drifting hands cost touches.",
        ],
        "citations": [CIT_CHARLEMONT_1899, CIT_CHARLEMONT_1878, CIT_FFBFSDA],
        "sig_lens": (
            "The Signature read: the guard is the covenant of balance - the "
            "tireur signs a contract with the floor before signing anything "
            "with the opponent. Sixty-forty is the signature split, the "
            "loaded spring the ink. Where public savate files a stance, the "
            "Signature Savate Method files a promise: I am rooted, I am "
            "ready, I return here after every line I write."
        ),
    },
    {
        "key": "footwork",
        "name": "Deplacement de Base: Basic Footwork",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Deplacement is how the tireur travels without breaking the "
            "guard. Savate footwork is built on the pas chasse - the "
            "shuffling step where the feet never cross and never come "
            "together: to advance, the lead foot steps forward and the rear "
            "foot follows the same distance; to retreat, the rear foot steps "
            "back and the lead foot follows. Lateral movement works the same "
            "way sideways, and the pivot turns the whole stance on the ball "
            "of the lead foot to change the angle. The head stays level - "
            "bobbing telegraphs every move - and the weight split never "
            "leaves sixty-forty for more than a heartbeat. Good footwork "
            "does three jobs: it carries the tireur into kicking range, it "
            "carries the tireur out of danger, and it sets the angle so a "
            "kick lands while the opponent's guard faces the wrong way. "
            "Champions are often just tireurs whose feet arrive half a "
            "second before their opponent's do, and the drills here build "
            "exactly that: quiet, level, economical travel in all four "
            "directions plus the pivot."
        ),
        "how_it_works": (
            "Learn the pas chasse in four directions. Step one: from la "
            "garde, advance - slide the lead foot forward about forty "
            "centimeters, then pull the rear foot the same forty "
            "centimeters, landing in the identical stance you started from. "
            "Step two: retreat - reverse the order, rear foot first, same "
            "forty centimeters. Step three: move laterally - to the lead "
            "side, lead foot steps and rear follows; to the rear side, rear "
            "foot steps and lead follows; the feet never cross, because "
            "crossed feet cannot kick or absorb. Step four: the pivot - on "
            "the ball of the lead foot, swing the rear foot ninety degrees "
            "to change the angle while the guard faces the opponent. Step "
            "five: drill the square - advance, lateral right, retreat, "
            "lateral left, returning to the start mark, keeping the head "
            "level and the stance intact at every corner. Step six: add the "
            "coach's clap - move on the clap, freeze on the second clap, and "
            "check that the guard is perfect in the freeze. Speed comes from "
            "short, frequent steps, not long lunges: the demo computes step "
            "distance, step time, and travel speed so the tireur can measure "
            "economy instead of guessing it."
        ),
        "key_points": [
            "The pas chasse rule: the feet never cross and never touch - lead foot leads forward, rear foot leads back.",
            "Advance, retreat, and both laterals use the same shuffle; the pivot turns ninety degrees on the ball of the lead foot.",
            "The head stays level through every step; bobbing is a telegram to the opponent.",
            "Short frequent steps beat long lunges - economy of travel is what arrives half a second early.",
            "Every drill ends in a freeze-check: the guard must be perfect in the freeze, or the step was wasted.",
        ],
        "requirements": [
            "The la garde stance held solidly for five minutes - footwork on a broken stance teaches broken footwork.",
            "A marked square of one meter per side on the floor for the square drill, plus a start mark.",
            "A partner or coach to call directions and clap the move-freeze rhythm.",
            "Ten minutes of directional shuffles per session, guard checked in the mirror after each set.",
            "Patience: the pivot is drilled alone for a full week before it is used in combinations.",
        ],
        "standards": [
            "Pas chasse mechanics follow the classical French school; crossed feet are a fault in assaut judging.",
            "Step distance scales with leg length - the demo uses forty centimeters for a 1.75-meter tireur.",
            "Footwork drills precede all kicking drills in the FFBFSDA tireur curriculum.",
        ],
        "citations": [CIT_CHARLEMONT_1899, CIT_FFBFSDA],
        "sig_lens": (
            "The Signature read: footwork is the signature in motion - every "
            "step a stroke of the pen that never lifts from the page. The "
            "feet that never cross are lines that never smudge. The "
            "Signature Savate Method teaches travel as handwriting: quiet, "
            "level, legible only to the writer, arriving before the reader "
            "knows the sentence began."
        ),
    },
    {
        "key": "fouette_median",
        "name": "Le Fouette Median: The Mid-Level Whip Kick",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The fouette is the signature kick of savate and its most thrown "
            "weapon: a whipping round kick that strikes with the top of the "
            "foot - le dessus du pied, the laced part of the shoe. The "
            "median version targets the ribs and the floating ribs at "
            "mid-torso height. The mechanics are a two-stage snap: the knee "
            "chambers up and across the body like a loaded hinge, then the "
            "lower leg whips out horizontally, the foot extending through "
            "the target as the hip turns over. The supporting foot pivots on "
            "the ball so the hip can open fully, and the guard hand on the "
            "kicking side swings down to counterbalance while the opposite "
            "hand stays glued to the chin. Because savate is fought in "
            "shoes, the top-of-foot strike lands with the rigid laces and "
            "toe box behind it - this is why the fouette is thrown with the "
            "foot pointed and extended, never flexed. Thrown correctly it is "
            "fast enough to beat a parry and heavy enough to fold a tireur "
            "around his own ribs; thrown with a dead hip it is an arm-punch "
            "with the leg, and the drills here make sure the hip does the "
            "work."
        ),
        "how_it_works": (
            "Throw the median fouette in six beats. Step one: from la garde, "
            "shift the weight onto the lead leg and lift the rear knee up "
            "and across until the thigh is horizontal and the knee points "
            "past the target line - this chamber is the hinge being loaded. "
            "Step two: pivot the supporting foot on its ball about ninety "
            "degrees so the hip opens toward the target. Step three: snap "
            "the lower leg out by extending the knee, whipping the top of "
            "the foot through the ribs at mid-torso height while the hip "
            "rolls over - the power comes from the hip turn plus the knee "
            "snap, not from swinging the whole leg. Step four: point the "
            "foot hard at extension, striking with the laces; the instant "
            "after contact, the knee re-chambers along the same path it came "
            "out. Step five: set the foot back down into la garde - never "
            "drop it in front of the stance. Step six: breathe out sharply "
            "on the snap. Drill it on the heavy bag in sets of ten per leg, "
            "checking that the bag swings from hip torque rather than "
            "pushing from a stiff leg. The demo computes the foot's tip "
            "speed and the strike's kinetic energy from leg length, arc, "
            "and snap time."
        ),
        "key_points": [
            "Striking surface is the top of the foot - the laces - with the foot pointed and extended at impact.",
            "Two-stage snap: knee chambers across the body, then the lower leg whips out as the hip turns over.",
            "The supporting foot pivots on the ball about ninety degrees so the hip opens fully into the kick.",
            "Target is the ribs at mid-torso height; the kicking-side hand drops to counterbalance while the other guards the chin.",
            "Re-chamber along the same path and return to la garde - the kick is a round trip, never a dropped leg.",
        ],
        "requirements": [
            "Solid la garde and forty-centimeter pas chasse - the kick is built on the stance and the step.",
            "Savate shoes or firm training shoes: the top-of-foot strike needs the rigid laced upper.",
            "A heavy bag at torso height and ten minutes of chamber drills (knee up, hold, snap, re-chamber) per leg.",
            "Hip mobility to chamber the thigh horizontal - daily hip openers until the chamber needs no effort.",
            "A partner holding a pad at rib height to confirm the laces, not the toes, are landing.",
        ],
        "standards": [
            "The fouette is one of the four canonical kick families codified by Baruzy; median height is the competition workhorse.",
            "Legal striking surface in assaut and combat: the shoe's upper - toe strikes are a fault.",
            "Median target zone is the torso between belt and shoulder; the demo's energy figure assumes a 4.5-kilogram leg-plus-shoe mass.",
        ],
        "citations": [CIT_CHARLEMONT_1899, CIT_BARUZY, CIT_FISAV],
        "sig_lens": (
            "The Signature read: the fouette is the signed line itself - "
            "the pen-stroke of the Signature Savate Method, flicked from the "
            "wrist of the hip. The chamber is the pen lifted, the snap the "
            "ink laid down, the re-chamber the pen returned to rest. "
            "Signature tireurs do not throw fouettes; they sign them, and "
            "the ribs keep the autograph."
        ),
    },
    {
        "key": "chasse_frontal",
        "name": "Le Chasse Frontal: The Front Push Kick",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The chasse is savate's push kick, and the frontal version "
            "drives straight ahead into the opponent's torso or thigh with "
            "the sole of the shoe - la plante du pied. Where the fouette "
            "whips, the chasse shoves: the knee chambers straight up in "
            "front of the chest, then the leg extends like a piston as the "
            "hip thrusts forward, the whole body leaning back a hand's "
            "width to put the weight behind the push. The supporting leg "
            "bends slightly to absorb the recoil, and both hands stay up "
            "because the chasse, for all its stopping power, leaves the "
            "head in place for the half-second the leg is extended. It is "
            "the tireur's fence and battering ram in one tool: thrown at "
            "the thigh it stops an advance cold, thrown at the torso it "
            "knocks a tireur backward out of punching range, and thrown as "
            "a counter it meets an incoming attacker with a wall of sole. "
            "Because the strike lands with the flat sole rather than a "
            "small point, it is forgiving to learn and brutally effective "
            "once the hip thrust is committed."
        ),
        "how_it_works": (
            "Throw the frontal chasse in five beats. Step one: from la "
            "garde, lift the rear knee straight up in front of the chest, "
            "thigh parallel to the floor - the chamber points the sole at "
            "the target like a loaded piston. Step two: lean the torso back "
            "a hand's width while driving the hip forward; this "
            "counter-lean puts the body mass behind the sole instead of "
            "behind the kick's starting line. Step three: extend the leg "
            "explosively, striking with the flat sole of the shoe into the "
            "opponent's thigh or torso, the foot flexed so the sole presents "
            "fully. Step four: the instant the push lands, re-chamber the "
            "knee back to the chest - do not leave the leg hanging in the "
            "air, where it can be caught or swept. Step five: set the foot "
            "down back into la garde and re-square the guard hands, which "
            "never dropped. Drill it against a partner holding a body pad: "
            "ten pushes per leg, and the pad holder should be moved, not "
            "stung - the chasse displaces, it does not snap. The demo "
            "computes the push force, the work done on an eighty-kilogram "
            "opponent, and the distance that work moves him."
        ),
        "key_points": [
            "Striking surface is the flat sole of the shoe, foot flexed to present the whole sole.",
            "The knee chambers straight up before the chest, then the leg extends like a piston with the hip thrusting forward.",
            "The torso leans back a hand's width to put body mass behind the push.",
            "Re-chamber immediately after contact - a hanging leg is a caught leg.",
            "The chasse displaces rather than snaps: the pad holder should be moved backward, not stung.",
        ],
        "requirements": [
            "La garde with the sixty-forty split - the push needs the rear leg loaded to drive from.",
            "Shoes with a flat grippy sole; the technique is named for the sole and needs it.",
            "A body pad and a willing holder, or a heavy bag, for ten-push sets per leg.",
            "Core strength for the counter-lean: planks and dead-bugs until the lean needs no arm waving.",
            "Guard discipline: both hands stay up through the whole piston stroke, checked in the mirror.",
        ],
        "standards": [
            "The chasse is the second of the four canonical kick families; frontal is its primary line.",
            "Legal target zones: torso and thigh; the sole must land flat - edge strikes are the revers's business.",
            "In assaut, a clean chasse that visibly displaces the opponent scores as a controlled, effective touch.",
        ],
        "citations": [CIT_CHARLEMONT_1899, CIT_BARUZY, CIT_FISAV],
        "sig_lens": (
            "The Signature read: the chasse is the stamped seal - where the "
            "fouette signs, the chasse embosses. The piston leg is the press, "
            "the sole the die, the opponent's torso the wax. The Signature "
            "Savate Method teaches the push as authentication: one flat "
            "impression, unmistakable, moving the reader back a full step."
        ),
    },
    {
        "key": "direct_avant",
        "name": "Le Direct du Bras Avant: The Lead Punch",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The direct du bras avant is savate's jab: a straight punch "
            "thrown with the lead hand, the fastest strike in the tireur's "
            "arsenal and the tool that does the most jobs. It measures "
            "distance, it probes the guard, it sets up every kick, it "
            "interrupts the opponent's rhythm, and in assaut it scores "
            "clean controlled touches. The punch travels straight from the "
            "cheek to the target and straight back, the fist rotating a "
            "quarter-turn so the knuckles land flat, the elbow staying "
            "under the fist rather than flaring. The shoulder snaps forward "
            "to add the last centimeters of reach, and the rear hand stays "
            "glued to the chin because the lead punch's only real risk is "
            "the counter it invites. In savate the jab is thrown from the "
            "sideways guard, so it carries a little more shoulder and a "
            "little less hip than a boxing jab - it is a fencer's touch "
            "more than a slugger's ram, and its speed is its power."
        ),
        "how_it_works": (
            "Throw the lead direct in five beats. Step one: from la garde, "
            "fix the eyes on the target - the opponent's nose or lead "
            "shoulder - without moving the head. Step two: extend the lead "
            "arm straight along the line from cheek to target, rotating the "
            "fist a quarter-turn so the knuckles face forward at impact; the "
            "elbow tracks under the fist, never winging out. Step three: "
            "snap the lead shoulder forward at full extension to steal the "
            "last few centimeters - the shoulder, not a lunge, because the "
            "feet stay planted in la garde. Step four: the instant the "
            "knuckles touch, pull the fist straight back along the same "
            "line to the cheek; the punch is a piston, and the return is "
            "half the technique. Step five: exhale sharply through the "
            "strike. Drill it on the focus mitts: the coach calls single "
            "jabs, then double jabs, and the tireur's rear hand must not "
            "drift from the chin - tape a coin to the chin and keep it "
            "there with the rear glove if needed. The demo computes the "
            "fist's travel time and speed over the standard sixty-centimeter "
            "line, and the reach the shoulder snap adds."
        ),
        "key_points": [
            "Straight line out from the cheek and straight back - the shortest path is the fastest punch.",
            "Fist rotates a quarter-turn; knuckles land flat, elbow tracks under the fist.",
            "The lead shoulder snaps forward for extra reach; the feet stay planted in la garde.",
            "The rear hand never leaves the chin - the jab's risk is the counter it invites.",
            "The return is half the technique: pull back along the same line the instant the knuckles touch.",
        ],
        "requirements": [
            "La garde with the lead hand at cheek height - the punch starts where the guard lives.",
            "Hand wraps and 10-ounce gloves for mitt and bag work; bare-knuckle drilling is never done.",
            "Focus mitts and a coach or partner calling single and double jabs.",
            "Shoulder mobility for the snap - arm circles and band pull-aparts in the warm-up.",
            "One hundred return-to-guard repetitions before the jab is used in any combination.",
        ],
        "standards": [
            "Hand strikes in savate: direct (straight), crochet (hook), remontant (uppercut) - the jab is the direct du bras avant.",
            "Legal hand targets: the head and torso front; strikes must land with the gloved knuckles.",
            "In assaut, the jab scores on clean controlled contact; wild swinging is penalized.",
        ],
        "citations": [CIT_CHARLEMONT_1878, CIT_FISAV],
        "sig_lens": (
            "The Signature read: the lead direct is the dotted line - the "
            "lightest stroke that still counts as writing. It measures the "
            "page, tests the ink, and tells the hand where the real "
            "sentence will go. The Signature Savate Method throws the jab "
            "as a question; the kicks are the answer."
        ),
    },
    {
        "key": "direct_arriere",
        "name": "Le Direct du Bras Arriere: The Rear Cross",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The direct du bras arriere is savate's cross: the straight "
            "punch of the rear hand, thrown with the full rotation of the "
            "hips and shoulders behind it. If the jab is the question, the "
            "cross is the exclamation - it carries roughly forty percent "
            "more speed at the knuckles than the lead punch because the hip "
            "turn whips the shoulder through a longer arc. The mechanics "
            "start at the floor: the rear foot pivots, the rear hip drives "
            "forward, the torso unwinds, and the fist travels straight from "
            "the chin to the target, rotating to land flat. The lead hand "
            "pulls back to the cheek as the cross extends, so the guard "
            "trades rather than drops. Thrown after the jab, it is the "
            "classic one-two that every tireur learns first; thrown alone "
            "it is a committed power shot that must land or be answered. "
            "The cross teaches the central lesson of savate punching: power "
            "comes from the floor through the hip, never from the arm."
        ),
        "how_it_works": (
            "Throw the rear cross in six beats. Step one: from la garde, "
            "plant the lead foot - it is the anchor the hip will rotate "
            "around. Step two: pivot the rear foot on its ball, driving the "
            "rear knee inward and the rear hip forward; the belt line should "
            "turn nearly square to the target. Step three: unwind the torso "
            "behind the hip, letting the rear shoulder whip forward through "
            "the arc the hip opened. Step four: extend the rear arm straight "
            "from chin to target along the center line, fist rotating to "
            "flat knuckles at impact. Step five: simultaneously retract the "
            "lead hand to the cheek - the guard trades hands, it never "
            "opens. Step six: snap everything back to la garde on the "
            "exhale; the cross that stays extended is a gift to the "
            "opponent's counter. Drill the one-two on the mitts: jab, then "
            "cross, with the coach checking that the rear heel lifted and "
            "the hip turned - no hip turn, no cross, just an arm punch. The "
            "demo computes the cross's knuckle speed with the hip "
            "contribution, the momentum of the gloved fist, and the "
            "percentage gain over the jab."
        ),
        "key_points": [
            "Power starts at the floor: rear foot pivots, rear hip drives, torso unwinds, fist travels last.",
            "The hip turn adds roughly forty percent to knuckle speed over the jab - that is the whole technique.",
            "The lead hand retracts to the cheek as the cross extends; the guard trades, never drops.",
            "The fist travels straight from chin to target on the center line, rotating to flat knuckles.",
            "Snap back to la garde on the exhale - an extended cross invites the counter.",
        ],
        "requirements": [
            "A reliable lead jab - the cross is drilled as the second half of the one-two, never alone at first.",
            "Hand wraps and gloves; a heavy bag for the hip-turn check (the bag should jump, not sway).",
            "Ankle and hip mobility for the rear-foot pivot - the pivot, not the arm, is the usual beginner failure.",
            "Fifty slow one-twos in the mirror, watching the belt line turn square, before any speed is added.",
            "A coach to confirm the rear heel lifts on every cross for the first month.",
        ],
        "standards": [
            "The direct du bras arriere is the power straight of the savate hand arsenal, per the classical school.",
            "Legal targets and glove-contact rules match the jab; the cross scores on clean penetration of the guard.",
            "Hip-driven punching is the graded standard in FFBFSDA technical examinations.",
        ],
        "citations": [CIT_CHARLEMONT_1878, CIT_FFBFSDA, CIT_FISAV],
        "sig_lens": (
            "The Signature read: the cross is the bold underline - the "
            "stroke that gives the sentence its weight. The floor signs "
            "first, the hip countersigns, the fist delivers the document. "
            "The Signature Savate Method treats the cross as the seal of "
            "the one-two: the jab proposes, the cross disposes."
        ),
    },
    {
        "key": "pied_bas",
        "name": "Le Coup de Pied Bas: The Low Shin Kick",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The coup de pied bas is savate's low kick: a short, chopping "
            "strike to the opponent's shin, delivered with the inner edge "
            "of the shoe - le tranchant interne. It is the fourth of the "
            "canonical kick families and the great equalizer of the "
            "tireur's game, because the shin is always in range and a dead "
            "leg cannot dance. The kick is thrown with a compact swing of "
            "the lower leg from a barely-lifted knee, the foot turned so "
            "the inner edge leads, chopping down and through the shin about "
            "twenty-five centimeters off the floor. There is no big chamber "
            "and no flourish: the bas is economical by design, landing "
            "before the opponent's guard can react and returning before it "
            "can be caught. Three clean bas kicks to the same shin change "
            "the whole fight - the opponent's footwork slows, his weight "
            "shifts to protect the leg, and his kicks lose their spring. "
            "Savate's shoes make this kick uniquely punishing: the rigid "
            "inner edge of the shoe concentrates the chop where a bare foot "
            "would spread it."
        ),
        "how_it_works": (
            "Throw the coup de pied bas in five beats. Step one: from la "
            "garde, lift the kicking knee only slightly - about fifteen "
            "centimeters - keeping the motion small and unreadable. Step "
            "two: turn the foot so the inner edge of the shoe leads, toes "
            "pointing slightly outward. Step three: swing the lower leg in "
            "a short downward arc, chopping the inner edge through the "
            "opponent's shin at about twenty-five centimeters of height, "
            "the hip adding a small inward turn at contact. Step four: let "
            "the leg follow through only a few centimeters past contact, "
            "then pull it straight back to la garde - the bas lives and "
            "dies on its speed of return. Step five: keep the hands high "
            "through the whole chop; the kick is low, the guard stays high. "
            "Drill it on the low pad or the bag's lower third: ten chops "
            "per leg, and the sound should be a crack, not a thud - the "
            "crack means the edge landed, the thud means the flat of the "
            "foot slapped. The demo computes the swing time, the contact "
            "window at forty centimeters of range, and the accumulated "
            "effect model across three landed kicks."
        ),
        "key_points": [
            "Striking surface is the inner edge of the shoe - le tranchant interne - toes turned slightly out.",
            "Target is the shin at about twenty-five centimeters; the knee lifts only fifteen centimeters to stay unreadable.",
            "Short downward chop with a small hip turn; follow-through is a few centimeters, then instant return.",
            "The crack of the edge, not the thud of the flat foot, is the sound of a correct bas.",
            "Hands stay high the whole time - the kick goes low, the guard never does.",
        ],
        "requirements": [
            "Firm shoes with a defined inner edge - the technique is built on the shoe's architecture.",
            "A low pad or a bag marked at twenty-five centimeters; ten chops per leg per session.",
            "La garde stable on one leg - single-leg balance drills until the support leg never wobbles.",
            "A partner to call random lead/rear bas so the kick is thrown on cue, not on rhythm.",
            "Shin conditioning is the receiver's business; the thrower needs only the edge and the timing.",
        ],
        "standards": [
            "The coup de pied bas is the fourth canonical kick family; the shin is its primary legal target.",
            "The inner edge must lead - flat-foot slaps are a technical fault in grading.",
            "In combat, repeated bas kicks are a legitimate attrition strategy; in assaut they score as controlled low touches.",
        ],
        "citations": [CIT_CHARLEMONT_1899, CIT_BARUZY, CIT_FISAV],
        "sig_lens": (
            "The Signature read: the bas is the footnote - small type at "
            "the bottom of the page that changes the meaning of everything "
            "above it. Three footnotes and the opponent's whole argument "
            "limps. The Signature Savate Method writes its footnotes with "
            "the inner edge, cites the shin, and lets the limp do the "
            "arguing."
        ),
    },
    {
        "key": "revers_lateral",
        "name": "Le Revers Lateral: The Side Reverse Kick",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The revers is savate's backhand kick: the leg swings outward "
            "and the strike lands with the outer edge or the sole of the "
            "shoe, the body turning away from the target as the kick "
            "extends. The lateral version drives sideways into the "
            "opponent's torso or thigh - imagine a backhand slap performed "
            "with the whole leg. The chamber brings the knee up across the "
            "body, then the leg unfolds outward as the supporting foot "
            "pivots and the hip opens away, the striking edge traveling on "
            "a wide arc that is hard to parry because it arrives from "
            "outside the guard's frame. It is the kick that punishes "
            "opponents who crowd the center line: where the fouette whips "
            "across the front, the revers comes around the side, and the "
            "two together bracket the guard like closing doors. Beginners "
            "learn it at torso height against the pad, feeling the hip "
            "open fully - a revers thrown with a closed hip is just an "
            "awkward fouette, and the pivot is what tells them apart."
        ),
        "how_it_works": (
            "Throw the lateral revers in six beats. Step one: from la garde, "
            "chamber the rear knee up and across the body, thigh rising "
            "toward horizontal - the same doorway the fouette uses, which "
            "is why the two kicks pair so well as feints for each other. "
            "Step two: pivot hard on the ball of the supporting foot, "
            "turning the body away from the target so the hip opens outward; "
            "the shoulders should finish nearly sideways-on. Step three: "
            "unfold the leg outward along the arc, extending through the "
            "target at torso height with the outer edge of the shoe leading "
            "- le tranchant externe. Step four: let the hip's opening carry "
            "the power; the leg is the edge of a swinging door, and the "
            "hinge is the hip. Step five: re-chamber the knee back across "
            "the body along the same arc - never let the leg drop across in "
            "front, which tangles the stance. Step six: plant back into la "
            "garde with the guard hands untouched throughout. Drill it on "
            "the bag's side: ten revers per leg, checking that the bag "
            "swings sideways from hip opening rather than being pushed. The "
            "demo computes the heel's arc length and tip speed from leg "
            "length and swing time, and the lateral range the kick covers."
        ),
        "key_points": [
            "Striking surface is the outer edge of the shoe, the leg unfolding outward as the body turns away.",
            "The supporting foot pivots hard so the hip opens fully - the pivot is what separates the revers from the fouette.",
            "The chamber crosses the body like the fouette's, which makes the two kicks natural feints for each other.",
            "The leg is the edge of a swinging door and the hip is the hinge; power comes from the opening, not the leg muscle.",
            "Re-chamber along the same arc and plant back into la garde - never drop the leg across the stance.",
        ],
        "requirements": [
            "A reliable median fouette - the revers is learned as its mirror image, sharing the chamber.",
            "Hip mobility for the full opening: lateral leg swings and pigeon stretches in every warm-up.",
            "Shoes with a defined outer edge; the strike must land edge-first, not with the toes.",
            "A heavy bag approached from the side, ten revers per leg, guard hands verified in the mirror.",
            "A partner holding a side pad to confirm the edge lands flat at torso height.",
        ],
        "standards": [
            "The revers is the third canonical kick family; lateral is its foundational line.",
            "Legal striking surfaces: outer edge and sole; the target zone is the torso and thigh.",
            "The full hip opening is the graded criterion - a closed-hip revers is marked as a fouette error.",
        ],
        "citations": [CIT_CHARLEMONT_1899, CIT_BARUZY, CIT_FISAV],
        "sig_lens": (
            "The Signature read: the revers is the backhand signature - "
            "the flourish written with the pen turned around. It arrives "
            "from outside the frame, where the reader is not looking. The "
            "Signature Savate Method keeps the revers as the second "
            "signature on the document: unexpected, outward-bound, "
            "impossible to forge without the hip's full opening."
        ),
    },
    {
        "key": "crochets",
        "name": "Les Crochets: The Hook Punches",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The crochet is savate's hook: a punch that travels on an arc "
            "rather than a straight line, landing with the knuckles on the "
            "side of the target. Thrown with the lead hand it is a short, "
            "tight arc around the opponent's guard; thrown with the rear "
            "hand it is a wider, heavier swing powered by the full hip "
            "rotation. The elbow stays bent at roughly ninety degrees and "
            "the fist travels on the horizontal plane at chin height, the "
            "forearm parallel to the floor at impact - a hook thrown with a "
            "dropped elbow is an arm slap, and a hook thrown with a "
            "straightening arm is a failed cross. The crochet is the punch "
            "that finishes combinations: the straight punches open the "
            "guard down the middle, and the hook comes around the side "
            "where the guard just left. In the sideways savate stance the "
            "lead hook is especially natural, snapping around with a short "
            "pivot of the lead foot, while the rear hook demands the same "
            "committed hip turn as the cross."
        ),
        "how_it_works": (
            "Throw the lead crochet in five beats. Step one: from la garde, "
            "shift a breath of weight onto the lead foot and pivot it "
            "slightly inward - this pivot is the hook's engine. Step two: "
            "raise the lead elbow to shoulder height, forearm horizontal, "
            "fist at the same height as the target's chin. Step three: "
            "whip the fist along a tight horizontal arc, rotating the hip "
            "and shoulder into the punch, landing with the knuckles as the "
            "elbow stays bent at ninety degrees - the power is the pivot "
            "plus the hip, never the arm swinging wide. Step four: snap the "
            "fist straight back to the cheek along the arc's return; the "
            "hook that hangs out is answered by a cross. Step five: keep "
            "the rear hand glued to the chin throughout. For the rear "
            "crochet, add the full rear-foot pivot and hip drive of the "
            "cross, and let the arc run wider - it is the heavy artillery. "
            "Drill both on the mitts: the coach holds for jab-cross-lead "
            "hook, checking the elbow never drops below the fist. The demo "
            "computes the fist's arc speed from radius and swing time for "
            "both the tight lead hook and the wide rear hook."
        ),
        "key_points": [
            "The fist travels on a horizontal arc at chin height, elbow bent at ninety degrees, forearm parallel to the floor.",
            "The lead hook runs on a short lead-foot pivot; the rear hook runs on the full hip drive of the cross.",
            "Power comes from the pivot and the hip - a hook swung with the arm alone is a slap.",
            "The elbow never drops below the fist; a dropped elbow turns the hook into an arm punch.",
            "Snap back along the arc's return - a hanging hook invites the straight counter down the middle.",
        ],
        "requirements": [
            "Reliable jab and cross - the hook is the third punch, learned after the straights are automatic.",
            "Hand wraps and gloves; the hook's arc stresses the wrist, so wrap the wrist with extra support.",
            "Focus mitts and a coach to hold the jab-cross-hook sequence and check elbow height.",
            "Wrist and shoulder conditioning: knuckle push-ups and band rotations before hook sessions.",
            "One hundred slow hooks per hand in the mirror, elbow pinned at ninety degrees, before speed work.",
        ],
        "standards": [
            "The crochet is the hook of the savate hand arsenal, thrown lead or rear, per the classical school.",
            "Legal targets: the side of the head and the torso; the knuckles must land with the glove closed.",
            "Elbow height is the graded criterion - hooks thrown with a dropped elbow are marked down in examinations.",
        ],
        "citations": [CIT_CHARLEMONT_1878, CIT_FFBFSDA],
        "sig_lens": (
            "The Signature read: the crochet is the parenthetical - the "
            "curve that closes around the opponent's guard like brackets "
            "around a phrase. The straights write the line; the hook "
            "punctuates it from the side. The Signature Savate Method "
            "throws the hook as the closing bracket: everything inside it "
            "belongs to the combination."
        ),
    },
])
ENTRIES.extend([
    {
        "key": "defenses",
        "name": "Parades et Esquives: Basic Defenses",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Parades et esquives are the two families of savate defense: "
            "the parade meets the attack with a deflecting surface, and the "
            "esquive moves the target out of the attack's path. The basic "
            "parades use the gloves and forearms: the lead hand catches or "
            "slaps aside the jab, the rear glove blocks the cross, the "
            "elbows pin to the ribs against hooks, and the forearm or shin "
            "checks the low kicks. The basic esquives move the head or body: "
            "a slip of the head inside or outside the straight punch, a bob "
            "under the hook, a step back out of the kick's range. The "
            "golden rule of savate defense is economy - the smallest "
            "movement that makes the attack miss. A parade moves the glove "
            "centimeters, not the arm a foot; an esquive moves the head "
            "inches, not the body a yard. Big defensive movements are just "
            "attacks on your own balance, and they leave you too far away "
            "to answer. Defense is drilled as a question-and-answer: the "
            "partner throws the single attack, the tireur answers with the "
            "smallest working defense, and the guard is whole again before "
            "the partner's hand returns."
        ),
        "how_it_works": (
            "Drill the six basic answers. One: against the jab, slap the "
            "lead glove a few centimeters outward across the punch's line - "
            "the parade deflects, it never catches force head-on. Two: "
            "against the cross, raise the rear glove to the cheek and let "
            "the punch land on the glove, the elbow tucked so the ribs stay "
            "covered. Three: against the hook, pin the elbow to the ribs on "
            "that side and turn slightly into the punch so it slides off "
            "the forearm. Four: against the fouette, lift the knee and "
            "present the shin, or step back just out of range - never reach "
            "for a kick with the hands. Five: the slip - against the "
            "straight punches, move the head a hand's width inside or "
            "outside the line, the knees bending, the guard intact. Six: "
            "the step-back - one pas chasse rearward timed to the "
            "opponent's step, leaving the kick to land on empty floor. "
            "Practice each as a call-and-response: the partner announces "
            "the attack, throws it at half speed, and the tireur answers "
            "with the smallest defense that works, freezing to check the "
            "guard afterward. The demo computes the reaction budget - "
            "visual detection plus motor response - against the flight time "
            "of a jab, showing why the smallest defense is the only one "
            "that fits inside the window."
        ),
        "key_points": [
            "Two families: the parade deflects with glove or forearm, the esquive moves the target off the line.",
            "Economy is the law: the smallest movement that makes the attack miss - centimeters, not feet.",
            "Never reach for a kick with the hands; check kicks with the shin or step out of range.",
            "The slip moves the head a hand's width off the line, knees bending, guard intact.",
            "Every defense ends in a freeze-check: the guard must be whole before the partner's hand returns.",
        ],
        "requirements": [
            "All four basic strikes readable at half speed - defense is drilled against known attacks first.",
            "Gloves and headgear for partner drills; even half-speed punches need the gear.",
            "A patient partner who announces attacks and throws at controlled speed.",
            "Ten call-and-response repetitions per defense per session, guard checked in the freeze.",
            "The discipline to keep defenses small: a coach watching for the flinch that becomes a leap.",
        ],
        "standards": [
            "Parade and esquive are the classical defensive families of the French school, per Charlemont.",
            "In assaut, clean defense followed by an immediate answer is the highest-valued exchange.",
            "Excessive retreat is penalized in competition - defense must stay in the fighting space.",
        ],
        "citations": [CIT_CHARLEMONT_1899, CIT_FISAV],
        "sig_lens": (
            "The Signature read: defense is the eraser used sparingly - "
            "one small stroke removes the opponent's line without smudging "
            "your own. The parade is a comma, the esquive a line break: "
            "tiny marks that change the whole sentence. The Signature "
            "Savate Method defends like an editor - cut the least, keep "
            "the most, and the page stays clean."
        ),
    },
    {
        "key": "fouette_figure",
        "name": "Le Fouette Figure: The High Whip Kick",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The fouette figure is the high whip kick, the same two-stage "
            "snap as the median fouette delivered at head height - and the "
            "most spectacular weapon in savate. The chamber is identical: "
            "knee up and across, thigh horizontal. The difference is the "
            "hip: it must open further and the supporting leg must sit "
            "deeper, because the foot has to travel another forty "
            "centimeters upward to reach the head. The striking surface "
            "remains the top of the foot, and the head target makes the "
            "guard discipline non-negotiable - a high kick thrown with "
            "dropped hands is a trade the tireur will lose. In assaut the "
            "figure scores beautifully when it lands clean, but experienced "
            "tireurs throw it sparingly: it is slower than the median, it "
            "telegraphs more, and a caught high kick ends the exchange "
            "badly. The figure is best understood as a finishing tool and "
            "a threat that keeps the opponent's guard high - which is "
            "exactly what opens the median and the bas underneath it."
        ),
        "how_it_works": (
            "Throw the figure in the same six beats as the median, with "
            "three adjustments. Step one: chamber the knee fully - thigh "
            "horizontal is the minimum; the figure forgives no lazy "
            "chamber. Step two: sink the supporting knee deeper, dropping "
            "the hips about ten centimeters, which buys the striking leg "
            "the height it needs without leaning the torso. Step three: "
            "pivot the support foot a full ninety degrees and open the hip "
            "completely - the figure lives or dies on hip openness. Step "
            "four: snap the lower leg up and through at head height, "
            "striking with the laces, the opposite hand nailed to the chin "
            "because the head is now the counter-target. Step five: "
            "re-chamber fast along the same path; the high kick's return is "
            "longer, so it must start sooner. Step six: plant into la garde "
            "and check the guard before anything else. Build it "
            "progressively: first throw at shoulder height for two weeks, "
            "then add ten centimeters a week until head height is "
            "comfortable - never chase height with a leaning torso. The "
            "demo computes the hip-flexion angle the figure demands, the "
            "extra travel distance over the median, and the snap time that "
            "keeps the kick ahead of the parry."
        ),
        "key_points": [
            "Same two-stage snap as the median fouette, delivered at head height with the top of the foot.",
            "The supporting leg sinks about ten centimeters and the hip opens fully - height comes from the base, not from leaning.",
            "The chamber must be complete; a lazy chamber makes the figure slow, telegraphed, and catchable.",
            "Guard discipline is non-negotiable: the opposite hand stays nailed to the chin while the kick is high.",
            "Build height progressively - shoulder height for two weeks, then ten centimeters a week, never chasing with a lean.",
        ],
        "requirements": [
            "A reliable median fouette - the figure is the same kick ten centimeters higher, learned only after the median is automatic.",
            "Hip flexor and hamstring mobility: daily splits progressions and hip openers.",
            "A tall bag or a partner holding a high pad; ten figures per leg, guard checked after each.",
            "Core strength for the deep support-leg sink: squats and lunges in the conditioning program.",
            "The honesty to throw it sparingly in sparring until the return is as fast as the median's.",
        ],
        "standards": [
            "The figure is the high line of the fouette family; head-height kicks are legal in combat and controlled in assaut.",
            "Clean head contact with the laces is the highest-valued single kick in assaut scoring.",
            "A caught or blocked high kick that unbalances the thrower is scored against the thrower.",
        ],
        "citations": [CIT_CHARLEMONT_1899, CIT_BARUZY, CIT_FISAV],
        "sig_lens": (
            "The Signature read: the figure is the exclamation point - "
            "the tallest mark on the page, used sparingly because a page "
            "of exclamations is noise. It keeps the reader's eyes up, "
            "which is exactly where the Signature Savate Method wants "
            "them while the real sentence lands underneath."
        ),
    },
    {
        "key": "chasse_lateral",
        "name": "Le Chasse Lateral: The Side Push Kick",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The chasse lateral is the side push kick: the same piston "
            "mechanics as the frontal chasse, redirected sideways into the "
            "opponent's torso or thigh. The knee chambers up and across, the "
            "body turns a quarter away, and the sole drives out along the "
            "side line as the hip opens - it is the revers's chamber with "
            "the chasse's piston finish. Tireurs use it to punish "
            "opponents who circle toward the kicking side, to stop a "
            "lateral advance cold, and to shove an opponent sideways out "
            "of position when the frontal line is blocked. Because the "
            "body turns, the lateral chasse covers the head with the "
            "shoulder naturally, and because the sole is broad, it is as "
            "forgiving as its frontal brother. The key checkpoint is the "
            "support foot: it must pivot fully, or the hip cannot open and "
            "the kick becomes a weak sideways stab. Thrown with the pivot "
            "and the hip thrust together, it moves an eighty-kilogram "
            "opponent a full step sideways."
        ),
        "how_it_works": (
            "Throw the lateral chasse in six beats. Step one: from la garde, "
            "chamber the rear knee up and across the body, thigh toward "
            "horizontal. Step two: pivot on the ball of the supporting foot, "
            "turning the body a quarter-turn away from the target so the hip "
            "can open sideways - this is the beat beginners skip, and the "
            "kick fails without it. Step three: drive the hip sideways and "
            "extend the leg like a piston, the sole of the shoe striking "
            "flat into the opponent's torso or thigh along the side line. "
            "Step four: lean the torso slightly away from the kick to put "
            "the mass behind the sole, the shoulder covering the chin. Step "
            "five: re-chamber the knee immediately - the sideways extended "
            "leg is the easiest leg in savate to catch. Step six: plant back "
            "into la garde, guard hands verified high. Drill it against the "
            "bag's side and against a partner's lateral advance: the partner "
            "steps sideways, the tireur meets him with the lateral piston "
            "and stops him. Ten per leg, checking the pivot on every rep. "
            "The demo computes the sideways displacement of an "
            "eighty-kilogram opponent, the pivot angle required, and the "
            "balance margin of the supporting leg."
        ),
        "key_points": [
            "The revers's chamber with the chasse's piston finish: knee up and across, then the sole drives sideways.",
            "The support foot must pivot fully - without the pivot the hip cannot open and the kick is a weak stab.",
            "The torso leans slightly away, the shoulder covering the chin; the body turn is natural head protection.",
            "Re-chamber immediately: the sideways extended leg is the easiest leg in savate to catch.",
            "It punishes lateral movement and shoves the opponent sideways out of position when the frontal line is blocked.",
        ],
        "requirements": [
            "Reliable frontal chasse and lateral revers - the lateral chasse borrows the chamber of one and the piston of the other.",
            "Hip mobility for the quarter-turn opening; lateral leg swings in the warm-up.",
            "A bag approachable from the side, or a partner drilling lateral advances into the kick.",
            "Shoes with a flat sole; ten lateral pistons per leg with the pivot checked on every rep.",
            "Single-leg balance on the support leg through the pivot - wobble means the pivot was rushed.",
        ],
        "standards": [
            "The chasse lateral is the side line of the chasse family, per the classical codification.",
            "Legal targets: torso and thigh; the sole must land flat along the side line.",
            "The full pivot is the graded criterion in technical examinations.",
        ],
        "citations": [CIT_CHARLEMONT_1899, CIT_BARUZY, CIT_FFBFSDA],
        "sig_lens": (
            "The Signature read: the lateral chasse is the margin note - "
            "written in the side space where the main text cannot reach. "
            "It shoves the reader's argument sideways off the page. The "
            "Signature Savate Method keeps a broad sole for the margins: "
            "flat, undeniable, and impossible to argue with."
        ),
    },
    {
        "key": "distance",
        "name": "La Distance de Combat: Managing Range",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "La distance de combat is range management: knowing which "
            "weapons reach at which distance and living at the range where "
            "your weapons work and the opponent's do not. Savate recognizes "
            "three ranges. The longue is kicking range, about one hundred "
            "eighty centimeters - the fouette, chasse, and revers all land "
            "here, and the punches fall short. The moyenne is punching "
            "range, about one hundred twenty centimeters - the jab, cross, "
            "and hooks land here, and the kicks are smothered. The courte "
            "is clinch and infighting range, about sixty centimeters - "
            "short hooks, uppercuts, and knees of the body, where long "
            "limbs are liabilities. The tireur's job is to surf these "
            "ranges: enter the longue to kick, cross the moyenne with "
            "punches covered, never stand still in the opponent's favorite "
            "range, and always know the distance in centimeters, not in "
            "feelings. Range is measured with the jab - extend it, and "
            "where the glove falls tells you which range you are in."
        ),
        "how_it_works": (
            "Learn the three ranges by measurement. Step one: face a partner "
            "in la garde and extend the jab - mark where the glove falls; "
            "that is the edge of the moyenne, about one hundred twenty "
            "centimeters. Step two: step back until the jab falls ten "
            "centimeters short, then throw the median fouette - if it lands "
            "clean, you are at the longue, about one hundred eighty "
            "centimeters. Step three: step in until the jab cannot extend "
            "without bending the elbow - that is the courte, about sixty "
            "centimeters. Step four: drill the surf - the partner calls a "
            "range, and the tireur moves to it with the pas chasse and "
            "throws only the weapons of that range: kicks at longue, "
            "punches at moyenne, short hooks at courte. Step five: learn "
            "the exit - after every attack, one pas chasse carries you back "
            "to the longue, out of the opponent's moyenne. Step six: spar "
            "the range game - one round where only kicks score, one where "
            "only punches score, feeling how the feet must serve the "
            "weapons. The demo computes the three range bands in "
            "centimeters, the step count to cross between them, and the "
            "time a pas chasse needs to exit the moyenne."
        ),
        "key_points": [
            "Three ranges: longue at about 180 cm for kicks, moyenne at about 120 cm for punches, courte at about 60 cm for infighting.",
            "Measure range with the jab - where the extended glove falls tells you which range you are in.",
            "Surf the ranges: enter the longue to kick, cross the moyenne with punches covered, exit with one pas chasse.",
            "Never stand still in the opponent's favorite range; the feet must serve the weapons.",
            "Range is known in centimeters, not in feelings - measure it in every drill until it is automatic.",
        ],
        "requirements": [
            "A working jab, median fouette, and the pas chasse in all four directions - range means nothing without the tools.",
            "A partner and a tape measure: mark the three ranges on the floor for the first month.",
            "Ten minutes of the range-surf drill per session, weapons restricted to the called range.",
            "The discipline to exit after every attack - one pas chasse back to the longue, every time.",
            "Sparring rounds with restricted weapons to feel each range in isolation.",
        ],
        "standards": [
            "Range bands follow the classical French pedagogy: each weapon family has its measured distance.",
            "Excessive holding at courte is broken up by the referee; the ranges are for striking, not stalling.",
            "Assaut judging rewards the tireur who controls the range the exchange is fought at.",
        ],
        "citations": [CIT_CHARLEMONT_1899, CIT_FFBFSDA, CIT_FISAV],
        "sig_lens": (
            "The Signature read: distance is the margin of the page - the "
            "tireur writes at longue, edits at moyenne, and never lets the "
            "opponent hold the pen at courte. The Signature Savate Method "
            "measures every margin in centimeters and signs only from the "
            "range where the signature cannot be smudged."
        ),
    },
    {
        "key": "combos_simples",
        "name": "Combinaisons Simples: The First Chains",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Combinaisons simples are the first two-strike chains: the "
            "moment savate stops being single techniques and becomes "
            "sentences. The foundation chains pair the tools the tireur "
            "already owns: jab-cross, jab-median fouette, cross-bas, "
            "fouette-chasse. The logic of every chain is the same - the "
            "first strike occupies the guard or the eyes, and the second "
            "strike lands where the defense just left. The jab-cross is the "
            "alphabet: jab down the middle, cross following through the "
            "opening. The jab-fouette is the first true pieds-poings "
            "sentence: the jab lifts the opponent's eyes and guard, and the "
            "median fouette arrives underneath at the ribs. Chains are "
            "drilled slowly until the transition disappears - there must be "
            "no pause, no re-chamber visible, no weight shift that "
            "announces strike two. A combination is one technique with two "
            "impacts, not two techniques standing next to each other, and "
            "the guard must be intact at the end of the chain exactly as it "
            "was at the start."
        ),
        "how_it_works": (
            "Build the four foundation chains. Chain one, jab-cross: throw "
            "the jab, and as the lead fist returns, the rear hip is already "
            "turning - the cross launches off the jab's return, not after "
            "it. Chain two, jab-median fouette: jab to lift the guard, then "
            "shift the weight to the lead leg as the jab returns and snap "
            "the fouette to the ribs underneath the lifted guard. Chain "
            "three, cross-bas: the cross turns the hip inward, and the "
            "hip's return swing feeds directly into the low chop of the "
            "bas. Chain four, fouette-chasse: the fouette's re-chamber "
            "becomes the chasse's chamber - the knee never fully drops "
            "between the two kicks. Drill each chain in three speeds: slow "
            "for mechanics, half speed for the disappearing transition, "
            "then full speed on the mitts or pads with the guard checked "
            "after every rep. Count the beats: each two-strike chain should "
            "fit inside half a second at full speed. The demo computes the "
            "permutation count of two-strike chains from the four "
            "foundation tools, the beat timing of each chain, and the total "
            "duration that keeps the chain ahead of the counter."
        ),
        "key_points": [
            "Every chain follows one logic: the first strike occupies the guard or the eyes, the second lands where the defense left.",
            "The four foundation chains: jab-cross, jab-median fouette, cross-bas, fouette-chasse.",
            "Strike two launches off strike one's return - there is no pause and no visible re-chamber between them.",
            "A combination is one technique with two impacts, and the guard must be intact at the end exactly as at the start.",
            "Each two-strike chain fits inside half a second at full speed; slower than that, it is two singles.",
        ],
        "requirements": [
            "Automatic jab, cross, median fouette, frontal chasse, and bas - chains are built from owned tools, not wished-for ones.",
            "Focus mitts and pads: the chains are drilled on equipment, never first on a live partner.",
            "Three-speed drilling: slow for mechanics, half for the transition, full for timing - in that order.",
            "A coach or mirror to verify the guard is whole at the end of every chain.",
            "One hundred repetitions of each chain before it is used in sparring.",
        ],
        "standards": [
            "Two-strike chains are the first graded combination level in the FFBFSDA tireur curriculum.",
            "In assaut, a clean two-touch chain outscores two isolated touches - continuity is judged.",
            "The guard-intact finish is the examination criterion for every graded chain.",
        ],
        "citations": [CIT_FFBFSDA, CIT_CHARLEMONT_1899],
        "sig_lens": (
            "The Signature read: the simple combination is the first "
            "compound signature - two strokes, one flourish, no lifting "
            "the pen. The jab signs the first name, the kick the family "
            "name. The Signature Savate Method teaches chains as "
            "calligraphy: the transition invisible, the guard unbroken, "
            "the whole thing unmistakably yours."
        ),
    },
])
ENTRIES.extend([
    {
        "key": "fouette_balance",
        "name": "Le Fouette Balance: The Swinging Whip Kick",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The fouette balance is the swinging version of the whip kick: "
            "instead of chambering the knee across the body, the whole leg "
            "swings up and through on a wide arc, like a pendulum with the "
            "hip as its pivot. It trades the chambered fouette's speed and "
            "subtlety for raw momentum - the full mass of the leg, some "
            "twelve kilograms with the shoe, arrives at the target on the "
            "longest possible lever. Thrown at the median or figure height "
            "with the top of the foot, it is the kick that ends exchanges: "
            "opponents respect it, guards brace for it, and a clean one "
            "folds the torso sideways. The cost is telegraphing and "
            "recovery - the swing is visible from the first degrees of the "
            "arc, and the leg's momentum must be ridden back down under "
            "control. Tireurs earn the balance by first owning the "
            "chambered fouette, then learning when the situation pays for "
            "the swing: against a retreating opponent, as the heavy second "
            "half of a combination, or when the opponent's guard has been "
            "pulled low by the bas."
        ),
        "how_it_works": (
            "Throw the swinging fouette in five beats. Step one: from la "
            "garde, begin the swing by lifting the leg on its wide arc - "
            "the knee stays relatively extended compared to the chambered "
            "version, the arc running from the floor through the target "
            "line. Step two: pivot the supporting foot fully and turn the "
            "hip over early, because the swing's power is the hip's "
            "rotation multiplied by the long lever, not a late snap. Step "
            "three: extend through the target at median or figure height, "
            "striking with the laces as the leg reaches the top of its "
            "pendulum - contact should happen just before the arc's peak, "
            "while the foot is still accelerating. Step four: ride the "
            "momentum through a short follow and then pull the leg back "
            "along a controlled return - the swing's recovery is a skill in "
            "itself, drilled separately. Step five: plant into la garde and "
            "re-square, the guard hands having stayed up through the whole "
            "arc. Drill it on the heavy bag: five swings per leg, and the "
            "bag should wrap around the kick from momentum, distinctly "
            "different from the chambered fouette's sharp crack. The demo "
            "computes the swinging leg's momentum and kinetic energy from "
            "leg mass, arc, and swing time, and compares it to the "
            "chambered version."
        ),
        "key_points": [
            "The whole leg swings on a wide arc with the hip as pivot - momentum replaces the chamber's snap.",
            "The hip turns over early; the swing's power is hip rotation times the long lever.",
            "Contact happens just before the arc's peak, while the foot is still accelerating.",
            "The recovery is a separate skill: ride the momentum through a short follow, then pull back under control.",
            "Best used against retreat, as a combination's heavy second half, or when the bas has pulled the guard low.",
        ],
        "requirements": [
            "An automatic chambered median fouette - the swing is learned as its heavy sibling, never before it.",
            "Heavy bag work: five swings per leg, feeling the bag wrap from momentum versus the chambered crack.",
            "Hip and hamstring mobility for the wide arc; groin stretches in every warm-up.",
            "Recovery drilling: ten controlled returns per leg before the swing is used in sparring.",
            "The judgment to throw it in the right situations - the coach calls the situation, the tireur throws the swing.",
        ],
        "standards": [
            "The fouette balance is the swinging line of the fouette family in the classical codification.",
            "In combat, a clean swinging fouette is a fight-changing strike; in assaut it must stay controlled.",
            "Telegraphing is the graded fault - the swing must launch from the guard without a wind-up tell.",
        ],
        "citations": [CIT_CHARLEMONT_1899, CIT_BARUZY, CIT_FISAV],
        "sig_lens": (
            "The Signature read: the balance is the sweeping underline - "
            "the broad stroke that rules the whole page beneath the text. "
            "Where the chambered fouette signs precisely, the swing "
            "authenticates with weight. The Signature Savate Method keeps "
            "the pendulum as the heavy seal: impressive, expensive, and "
            "spent only where the document demands it."
        ),
    },
    {
        "key": "revers_balance",
        "name": "Le Revers Balance: The Swinging Reverse Kick",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The revers balance is the swinging version of the reverse kick: "
            "the leg sweeps up and around on a full outward arc, the body "
            "turning away as the outer edge of the shoe travels the longest "
            "path of any savate kick. It is the mirror of the fouette "
            "balance - same pendulum logic, opposite direction - and the "
            "two swinging kicks together form the heavy artillery of the "
            "leg arsenal. The revers balance arrives from outside the "
            "opponent's vision, which makes it the kick most likely to land "
            "unseen, and its arc carries it naturally into the blind side "
            "after a fouette has pulled the guard across. The demands are "
            "steep: the supporting pivot must be total, the hip must open "
            "completely, and the balance on one leg through a wide swinging "
            "arc must be drilled until it is boring. Tireurs who rush the "
            "revers balance fall over; tireurs who drill it own the "
            "outside line of every exchange."
        ),
        "how_it_works": (
            "Throw the swinging revers in five beats. Step one: from la "
            "garde, start the leg on its outward arc - the knee opens away "
            "from the body rather than chambering across it, the first "
            "degrees of the swing already turning the body. Step two: pivot "
            "the supporting foot completely, a full ninety degrees or more, "
            "so the hip can open to its limit - the pivot is even more "
            "critical here than in the lateral revers. Step three: let the "
            "outer edge of the shoe travel the full arc, turning the body "
            "away as the leg comes around, striking at torso height with le "
            "tranchant externe at the moment the arc crosses the target "
            "line. Step four: the body will have turned substantially - "
            "ride it, spot the opponent over the shoulder, and pull the leg "
            "back along the return arc under control. Step five: plant into "
            "la garde facing the opponent again, guard verified. Drill it "
            "slowly first: walk the arc in three counts - swing, contact, "
            "return - until the balance is unshakeable, then add speed in "
            "small steps. The demo computes the full arc length, the tip "
            "speed, and the time the kick spends in the opponent's blind "
            "sector."
        ),
        "key_points": [
            "The leg sweeps the full outward arc with the body turning away - the longest path of any savate kick.",
            "The supporting pivot must be total, ninety degrees or more; the hip opens to its absolute limit.",
            "It arrives from outside the opponent's vision - the kick most likely to land unseen.",
            "Ride the body's turn, spot the opponent over the shoulder, and pull back along the return arc.",
            "Drill the arc in three slow counts until balance is unshakeable, then add speed in small steps.",
        ],
        "requirements": [
            "An automatic lateral revers - the swing is its heavy sibling, learned after the pivot is perfect.",
            "Exceptional single-leg balance: eyes-closed single-leg stands until thirty seconds is easy.",
            "Hip openers and lateral swings in every warm-up; the full opening is non-negotiable.",
            "A patient drilling progression: three-count walks for two weeks before any speed.",
            "A coach watching the pivot - the number-one fault is the pivot that stops at forty-five degrees.",
        ],
        "standards": [
            "The revers balance is the swinging line of the revers family, per the classical codification.",
            "Blind-side arrival is its tactical purpose; in assaut the control standard still applies.",
            "Loss of balance on the return is scored against the thrower in competition.",
        ],
        "citations": [CIT_CHARLEMONT_1899, CIT_BARUZY, CIT_FISAV],
        "sig_lens": (
            "The Signature read: the revers balance is the signature "
            "written backward - legible only in the mirror, arriving where "
            "no one is reading. It is the Signature Savate Method's hidden "
            "clause: the term the other party never saw, binding the "
            "moment the outer edge crosses the line."
        ),
    },
    {
        "key": "chasse_bas",
        "name": "Le Chasse Bas: The Low Push Kick",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The chasse bas is the low push kick: the chasse's piston "
            "driven into the opponent's thigh or knee line with the sole, "
            "stopping an advance the way a doorstop stops a door. Where the "
            "frontal chasse displaces the torso, the bas version attacks "
            "the foundation - a hard sole into the lead thigh deadens the "
            "leg, breaks the opponent's rhythm, and makes every subsequent "
            "kick he throws a negotiation with pain. It is thrown with a "
            "shorter chamber than the frontal chasse, the knee lifting only "
            "enough to line the sole up with the thigh, and the hip thrust "
            "is downward-angled rather than level. Tireurs use it as the "
            "answer to pressure: when the opponent marches forward behind "
            "his guard, the chasse bas meets the lead leg and the march "
            "stops. Combined with the coup de pied bas, it gives the "
            "tireur a complete low game - the chop stings the shin, the "
            "push kills the thigh, and together they dismantle the "
            "opponent's base."
        ),
        "how_it_works": (
            "Throw the low chasse in five beats. Step one: from la garde, "
            "lift the knee to about waist height - a shorter chamber than "
            "the frontal, because the target is the thigh, not the torso. "
            "Step two: angle the hip thrust slightly downward, driving the "
            "body's mass down and through the sole rather than level. Step "
            "three: extend the leg and plant the flat sole into the "
            "opponent's lead thigh, about forty centimeters above the "
            "knee, the foot flexed to present the whole sole. Step four: "
            "push through - this is a displacing kick, so the leg extends "
            "fully and the opponent's leg is driven back and down, not "
            "snapped at. Step five: re-chamber fast and plant into la garde; "
            "the low extended leg is as catchable as the lateral's. Drill "
            "it against a partner's advance: the partner walks forward "
            "behind his guard, and the tireur stops him with the bas piston "
            "to the thigh - the partner should halt, not hop. Ten stops "
            "per leg. The demo computes the stopping impulse against an "
            "eighty-kilogram opponent advancing at two meters per second, "
            "and the thigh-contact height that maximizes the deadening "
            "effect."
        ),
        "key_points": [
            "The chasse's piston driven downward-angled into the lead thigh with the flat sole.",
            "Shorter chamber than the frontal - the knee lifts only to waist height for a thigh target.",
            "It is a displacing kick: the leg extends fully and drives the opponent's leg back and down.",
            "The answer to pressure - when the opponent marches forward, the bas piston stops the march.",
            "Pair it with the coup de pied bas: the chop stings the shin, the push kills the thigh.",
        ],
        "requirements": [
            "A reliable frontal chasse - the bas is the same piston angled down, learned after the level version.",
            "A partner willing to advance into the kick for stop-drills, with thigh protection.",
            "Sole conditioning: the flat sole must land confidently - pad work until the placement is automatic.",
            "Hip flexor strength for the downward-angled thrust: hanging knee raises in conditioning.",
            "Ten stops per leg per session, the partner's advance actually halted, not merely touched.",
        ],
        "standards": [
            "The chasse bas is the low line of the chasse family; the thigh is its primary target.",
            "The knee joint itself is never the target - the strike lands on the thigh above it.",
            "In combat, visible deadening of the lead leg is legitimate attrition; in assaut, control applies.",
        ],
        "citations": [CIT_CHARLEMONT_1899, CIT_BARUZY, CIT_FISAV],
        "sig_lens": (
            "The Signature read: the chasse bas is the redaction bar - a "
            "thick black line drawn across the opponent's advance, "
            "removing his forward motion from the record. The Signature "
            "Savate Method redacts with the sole: one flat impression, and "
            "the march is struck from the minutes."
        ),
    },
    {
        "key": "remontant",
        "name": "Le Remontant: The Uppercut Punch",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The remontant is savate's uppercut: a punch that travels "
            "upward, landing with the knuckles under the chin or into the "
            "torso from below. Thrown with either hand, it is the punch "
            "that exploits the guard's vertical gaps - when the opponent's "
            "gloves rise to catch the jab and cross, the space under the "
            "elbows opens, and the remontant climbs through it. The "
            "mechanics dip the knees slightly, then drive upward as the "
            "legs extend, the fist traveling on a tight vertical arc with "
            "the elbow bent and tucked - a wide looping uppercut is a hook "
            "that missed its plane and is easily seen. The rear-hand "
            "remontant, powered by the same hip drive as the cross, is one "
            "of the heaviest single punches in the arsenal; the lead-hand "
            "version is a short, sharp tool for the infighting range. In "
            "the courte, where straight punches have no room, the remontant "
            "and the short crochet are the entire hand game."
        ),
        "how_it_works": (
            "Throw the rear remontant in six beats. Step one: from la garde, "
            "dip the knees about ten centimeters - the punch's power is "
            "loaded in the legs, not wound up in the arm. Step two: pivot "
            "the rear foot and drive the rear hip forward exactly as for "
            "the cross; the uppercut is a cross that changed planes. Step "
            "three: as the legs extend, drive the rear fist upward on a "
            "tight vertical arc, elbow bent and tucked to the body, the "
            "fist rotating so the knuckles face up at impact. Step four: "
            "land under the chin or into the solar plexus from below - the "
            "punch climbs through the gap under the opponent's elbows. Step "
            "five: the lead hand stays at the cheek throughout; the "
            "uppercut's dip is the moment counters are born, and the guard "
            "must not dip with the knees. Step six: snap the fist back down "
            "the same vertical line to the chin. Drill it on the mitts "
            "held low: the coach drops the mitt to the body line and the "
            "tireur climbs into it - ten per hand, the arc tight every "
            "time. The demo computes the upward fist speed from leg drive "
            "and arc, and the chin-height target the punch must reach."
        ),
        "key_points": [
            "The fist travels upward on a tight vertical arc, elbow bent and tucked - a wide loop is a failed punch.",
            "Power is loaded in the leg dip and delivered by the extension; the arm merely guides the fist.",
            "The rear remontant uses the cross's hip drive on a vertical plane - it is among the heaviest single punches.",
            "It exploits the guard's vertical gaps: when gloves rise, the space under the elbows opens.",
            "The guard must not dip with the knees - the dip is the moment counters are born.",
        ],
        "requirements": [
            "Reliable cross with full hip drive - the remontant is the cross changed to the vertical plane.",
            "Leg strength for the dip-and-drive: squats and box jumps in the conditioning program.",
            "Mitts held at body line by a coach; ten tight uppercuts per hand per session.",
            "Wrist support in the wraps - the upward impact angle stresses the wrist more than straight punches.",
            "Mirror work to verify the arc stays tight and the lead hand never leaves the cheek.",
        ],
        "standards": [
            "The remontant is the uppercut of the savate hand arsenal, thrown lead or rear, per the classical school.",
            "Legal targets: chin from below and the torso; the knuckles must land with the glove closed.",
            "In the courte, the remontant and short crochet are the sanctioned hand tools; straights need room.",
        ],
        "citations": [CIT_CHARLEMONT_1878, CIT_FFBFSDA],
        "sig_lens": (
            "The Signature read: the remontant is the caret - the little "
            "mark that inserts meaning from below, lifting the whole line "
            "upward. It finds the gap the guard left open and writes in "
            "it. The Signature Savate Method keeps the caret tight and "
            "vertical: small mark, large revision."
        ),
    },
    {
        "key": "enchainements",
        "name": "Enchainements Pieds-Poings: Kick-Punch Chains",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Enchainements pieds-poings are the kick-punch chains that make "
            "savate savate: three-strike sequences mixing the hands and the "
            "feet, the art's native language. The classic chains - "
            "jab-cross-median fouette, jab-bas-cross, fouette-chasse-cross "
            "- work because each strike's recovery feeds the next strike's "
            "launch: the cross's hip turn loads the fouette, the fouette's "
            "re-chamber chambers the chasse, the jab's return covers the "
            "bas's entry. The tireur learns to think in threes, feeling the "
            "rhythm - fast-fast-slow for power finishes, or even beats for "
            "volume - and to end every chain in la garde with the guard "
            "whole. The great leap from the simple combinations is the "
            "weight transfer: in a two-strike chain the weight barely moves, "
            "but in a three-strike chain the tireur's mass must surf from "
            "leg to leg without ever being caught between. Chains are where "
            "savate's shoe-and-glove duality becomes one weapon, and the "
            "drills here build the surfing until it is silent."
        ),
        "how_it_works": (
            "Build the three classic chains. Chain one, jab-cross-fouette: "
            "throw the one-two, and as the cross's hip finishes turning, "
            "let the weight settle onto the lead leg - the rear knee is "
            "already lifting, and the fouette snaps to the ribs before the "
            "opponent's guard resets. Chain two, jab-bas-cross: jab to lift "
            "the eyes, chop the bas to the shin as the jab returns, and let "
            "the chop's hip swing feed the rear cross over the top. Chain "
            "three, fouette-chasse-cross: the fouette's re-chamber becomes "
            "the chasse's chamber mid-air, the piston lands, and the plant "
            "of the kicking foot drives the cross. Drill each chain in the "
            "three speeds - slow for the weight surfing, half for the "
            "rhythm, full on the pads - and count the beats aloud until the "
            "rhythm is internal: ONE-two-THREE for the power finish, or "
            "one-two-three even for volume. The guard check after every rep "
            "is mandatory; a chain that ends open is a chain that failed. "
            "The demo computes each chain's total duration at full speed, "
            "the beat gaps, and the weight-transfer path across the three "
            "strikes."
        ),
        "key_points": [
            "Three-strike chains mixing hands and feet: jab-cross-fouette, jab-bas-cross, fouette-chasse-cross.",
            "Each strike's recovery feeds the next strike's launch - the cross's hip loads the fouette, the re-chamber chambers the chasse.",
            "The leap from two-strike chains is the weight transfer: the mass must surf leg to leg, never caught between.",
            "Rhythm is a tool: fast-fast-slow for power finishes, even beats for volume.",
            "Every chain ends in la garde with the guard whole - a chain that ends open failed.",
        ],
        "requirements": [
            "All four simple combinations automatic - the three-strike chains extend them, they do not replace them.",
            "Pads and mitts for full-speed chain work; chains are never first learned on a live partner.",
            "Three-speed drilling with the beats counted aloud until the rhythm is internal.",
            "A coach to watch the weight surfing - the caught-between moment is the chain's failure point.",
            "Fifty repetitions of each classic chain before any improvisation is allowed.",
        ],
        "standards": [
            "Three-strike pieds-poings chains are the intermediate graded combination level in the FFBFSDA curriculum.",
            "In assaut, a flowing three-touch chain is the premier scoring exchange; broken chains score as singles.",
            "Weight transfer without loss of balance is the examination criterion.",
        ],
        "citations": [CIT_FFBFSDA, CIT_BARUZY, CIT_FISAV],
        "sig_lens": (
            "The Signature read: the enchainement is the full signature - "
            "first name, family name, and flourish in one unbroken motion. "
            "The weight surfing is the pen never lifting; the rhythm is "
            "the hand's natural cadence. The Signature Savate Method "
            "writes in threes because two strokes are a mark and three are "
            "a name."
        ),
    },
    {
        "key": "feintes",
        "name": "Les Feintes: The Art of the Feint",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Les feintes are feints: attacks begun and not finished, thrown "
            "to steal the opponent's reaction and then punish it. The "
            "tireur shows the beginning of the median fouette - the knee "
            "lifts, the hip starts to turn - and when the opponent's guard "
            "drops to answer the kick, the real attack goes elsewhere: the "
            "figure over the lowered hands, the cross through the opened "
            "center, the bas under the shifted weight. A feint works "
            "because the human reaction to a chambered kick is faster than "
            "the decision to ignore it; the opponent's body answers before "
            "his mind catches up, and for three-tenths of a second he is "
            "defending a kick that will never come. The craft has two "
            "rules: the feint must look exactly like the real attack's "
            "first half - a lazy feint fools no one - and the real attack "
            "must already be launching as the feint peaks. Feinting is "
            "savate's chess: the tireur who feints well fights the "
            "opponent's reactions instead of his guard."
        ),
        "how_it_works": (
            "Build the three core feints. Feint one, fouette-to-figure: "
            "begin the median fouette exactly - knee chamber, hip starting "
            "to turn - and as the opponent's hands drop toward the ribs, "
            "extend the snap upward to the head instead. Feint two, "
            "fouette-to-cross: show the knee lift, and when the opponent "
            "shifts weight to check the kick, plant the foot and drive the "
            "rear cross through the center his guard just opened. Feint "
            "three, jab-to-bas: throw the jab short, deliberately falling a "
            "hand's width short, and as the opponent parries the phantom "
            "punch, chop the bas to the unweighted shin. Drill each as a "
            "two-beat: the partner is told to react to the feint honestly, "
            "and the tireur's real attack must land inside the "
            "three-tenths-of-a-second window the reaction opens. Start with "
            "the partner cooperating, then let him choose whether to bite - "
            "the feint must earn the reaction. The demo computes the "
            "reaction window, the timing overlap between feint peak and real "
            "attack launch, and the success model across ten attempts."
        ),
        "key_points": [
            "A feint is an attack begun and not finished, thrown to steal the reaction and punish it.",
            "The feint must look exactly like the real attack's first half - a lazy feint fools no one.",
            "The real attack launches as the feint peaks, landing inside the 0.3-second window the reaction opens.",
            "Three core feints: fouette-to-figure, fouette-to-cross, jab-to-bas.",
            "Feinting fights the opponent's reactions instead of his guard - it is savate's chess.",
        ],
        "requirements": [
            "Convincing real attacks - a feint of a kick you cannot throw is pantomime, not tactics.",
            "A partner trained to react honestly to the feint, then progressively to read and not bite.",
            "Ten feint-and-punish repetitions per pattern, the real attack timed inside the reaction window.",
            "Video review: the feint's first half must be indistinguishable from the real attack's.",
            "The discipline to feint sparingly - a tireur who feints constantly teaches the opponent to ignore him.",
        ],
        "standards": [
            "Feinting is a classical tactical element of the French school; Charlemont treats it as essential ringcraft.",
            "In assaut, touches set up by clean feints are valued for their technical merit.",
            "Excessive feinting without attacking is penalized as passivity in competition.",
        ],
        "citations": [CIT_CHARLEMONT_1899, CIT_FISAV],
        "sig_lens": (
            "The Signature read: the feint is the draft - the visible "
            "sketch that makes the reader brace for one document while the "
            "real one is already being signed underneath. The Signature "
            "Savate Method drafts in the open and signs in the gap: the "
            "opponent proofreads the feint, and the real attack is "
            "published before he finishes."
        ),
    },
    {
        "key": "contre",
        "name": "Le Contre: Counter-Striking",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Le contre is the counter: striking not after the opponent's "
            "attack, but into it - meeting his advance with your own "
            "technique so that his commitment becomes your opening. The "
            "classic savate counters are the chasse into the advancing "
            "opponent, the cross over the lazy jab, and the fouette into "
            "the step of the kicking leg. Countering works on a brutal "
            "arithmetic: the attacker has spent his balance and his guard "
            "on the attack, so for the fraction of a second his technique "
            "is extended, he is both open and unable to change direction. "
            "The counter-striker's skill is reading the tell - the dip of "
            "the shoulder before the cross, the weight shift before the "
            "fouette - and launching the answer into the attack's path "
            "rather than waiting for it to finish. This is the most "
            "advanced timing in the compounded tier, and it is drilled "
            "only after defense is reflexive, because a failed counter is "
            "simply being hit while trying to be clever."
        ),
        "how_it_works": (
            "Build the three classic counters. Counter one, the chasse stop: "
            "as the opponent steps in behind his guard, drive the frontal "
            "chasse piston into his advance - his forward momentum adds to "
            "your push, and he meets a wall. Counter two, the cross over "
            "the jab: slip the opponent's lazy jab a hand's width outside "
            "and drive your rear cross down the line his jab just vacated - "
            "his lead hand is extended and cannot guard. Counter three, the "
            "fouette into the step: as the opponent lifts his knee for his "
            "own kick, snap your median fouette to his ribs - his weight is "
            "on one leg and his guard is moving. Drill each as a "
            "stimulus-response: the partner throws the committed attack at "
            "increasing speed, and the tireur's counter must launch within "
            "six-hundredths of a second of the tell - the demo shows why "
            "this window is the whole technique. Start with the partner "
            "announcing the attack, then unannounced, then in free sparring "
            "with counters as the only scoring strikes. The demo computes "
            "the attack's flight time, the counter's launch window, and the "
            "combined-momentum effect of the chasse stop."
        ),
        "key_points": [
            "The counter strikes into the attack, not after it - the attacker's commitment becomes your opening.",
            "Three classics: the chasse stop into the advance, the cross over the lazy jab, the fouette into the kicking step.",
            "Read the tell - the shoulder dip, the weight shift - and launch into the attack's path.",
            "The counter must launch within 0.06 seconds of the tell; later than that, it is just being hit cleverly.",
            "Drilled only after defense is reflexive; a failed counter is the most expensive mistake in the tier.",
        ],
        "requirements": [
            "Reflexive parades and esquives - countering without defense is gambling, not technique.",
            "A partner who can throw committed, readable attacks at increasing speed.",
            "Stimulus-response drilling: announced, then unannounced, then free sparring with counters only.",
            "Headgear and full sparring gear - counters are drilled at real speed against real attacks.",
            "A coach to identify each tireur's tells-reading: some read shoulders, some read hips, some read feet.",
        ],
        "standards": [
            "Counter-striking is the advanced timing element of the classical French school.",
            "In assaut and combat, a clean counter outscores the attack it defeats - timing is prized.",
            "Meeting force with force head-on is discouraged; the counter deflects the line while striking.",
        ],
        "citations": [CIT_CHARLEMONT_1899, CIT_FISAV],
        "sig_lens": (
            "The Signature read: the contre is the countersignature - "
            "written across the opponent's document while his pen is still "
            "moving. His commitment is the ink; your timing is the seal "
            "over it. The Signature Savate Method countersigns in the "
            "six-hundredths of a second where his signature is wet and "
            "yours makes it yours."
        ),
    },
    {
        "key": "corps_corps",
        "name": "Le Corps a Corps: Close-Quarter Work",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Le corps a corps is the close-quarter game: fighting at the "
            "courte, sixty centimeters and under, where long kicks are "
            "smothered and the short weapons rule. The toolkit shrinks to "
            "the short crochet, the remontant, the bas, and the shoulder "
            "and hip bumps that make space - but the intensity rises, "
            "because at this distance every strike lands and there is no "
            "room to miss. The stance shortens and lowers, the guard "
            "tightens to the face, and the tireur learns to punch inside "
            "the opponent's arms rather than around them. The key skill is "
            "the exit: at the courte you are always one beat from being "
            "tied up, so every close exchange ends with a push, a pivot, or "
            "a short combination that buys the step back to the moyenne. "
            "Tireurs who fear the inside lose there; tireurs who drill it "
            "discover that the courte is where the remontant - the most "
            "underused punch in beginner savate - becomes the best punch "
            "in the building."
        ),
        "how_it_works": (
            "Work the close quarter in four drills. Drill one, the phone "
            "booth: both tireurs stand at courte with a rope tied loosely "
            "between their belts - if the rope goes taut, someone retreated, "
            "and the drill resets; trade only short crochets and remontants "
            "for thirty-second rounds. Drill two, the bump and punch: from "
            "the clinch-ish tie, bump with the shoulder to make six inches "
            "of space, then throw the short hook into the space - the bump "
            "is the punch's chamber. Drill three, the bas at close range: "
            "the low chop needs no distance, so practice chopping the shin "
            "while chest-to-chest, the hands glued high. Drill four, the "
            "exit: after every close exchange, one pas chasse back to the "
            "moyenne - drill the exit as its own technique, because the "
            "tireur who cannot leave the courte will be held there. Keep "
            "the headgear on and the power at sixty percent; the courte is "
            "for volume and positioning, not for knockouts. The demo "
            "computes the short-hook output rate at the courte, the space "
            "the shoulder bump creates, and the step count of the exit."
        ),
        "key_points": [
            "At the courte the toolkit shrinks to the short crochet, the remontant, the bas, and the bump - but every strike lands.",
            "The stance shortens and lowers, the guard tightens to the face; punch inside the opponent's arms, not around them.",
            "The shoulder bump is the close punch's chamber - make six inches of space, then fill it with the hook.",
            "The exit is its own technique: every close exchange ends with the pas chasse back to the moyenne.",
            "Drill at sixty percent power - the courte is for volume and positioning, not knockouts.",
        ],
        "requirements": [
            "Short crochet and remontant already reliable - the courte is fought with owned tools only.",
            "Headgear, gloves, and mouthguard; the courte lands everything, so the gear is mandatory.",
            "A rope or belt for the phone-booth drill, and a partner comfortable at close range.",
            "Thirty-second rounds to start - the courte is exhausting, and fatigue destroys technique first.",
            "A coach to enforce the exit drill; beginners fall in love with brawling and forget to leave.",
        ],
        "standards": [
            "Corps-a-corps work is part of the classical curriculum; excessive holding is separated by the referee.",
            "Short punches must remain punches - open-glove pushing is a fault.",
            "In assaut, clean short combinations at the courte score fully; wild swinging does not.",
        ],
        "citations": [CIT_CHARLEMONT_1899, CIT_FFBFSDA, CIT_FISAV],
        "sig_lens": (
            "The Signature read: the corps a corps is the fine print - "
            "the dense clause at the bottom where the real terms live. "
            "No room for flourishes; every word lands. The Signature "
            "Savate Method reads the fine print with short hooks and "
            "signs it with the remontant, then exits before the other "
            "party can renegotiate."
        ),
    },
    {
        "key": "pied_saute",
        "name": "Le Coup de Pied Saute: The Jumping Kick",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The coup de pied saute is the jumping kick: the tireur leaves "
            "the floor and delivers a kick mid-air, most often a fouette or "
            "a chasse thrown from the jump's peak. It is savate's most "
            "athletic technique and its most situational - the jump adds "
            "the body's falling mass to the strike, but it also commits the "
            "tireur to a ballistic path he cannot change. Used well, the "
            "saut punishes a retreating opponent, clears the distance in a "
            "single beat, and lands the rare spectacular touch that breaks "
            "an opponent's confidence. Used poorly, it is a gift: a missed "
            "jumping kick lands the tireur off-balance and open. The "
            "technique demands real leg power - a thirty-five-centimeter "
            "vertical jump just to have time for the chamber and extension "
            "- and it is drilled on the crash mat long before it is thrown "
            "at a partner. In assaut the saut is a spice, not a staple; in "
            "combat it is the strike that ends highlight reels."
        ),
        "how_it_works": (
            "Build the jumping fouette in stages. Stage one, the jump alone: "
            "from la garde, dip and drive straight up, tucking the knees - "
            "measure the vertical until thirty-five centimeters is "
            "reliable, because the kick needs that airtime. Stage two, the "
            "air chamber: at the jump's peak, chamber the kicking knee "
            "exactly as for the standing fouette - the peak is the only "
            "moment the body is stable enough to kick from. Stage three, "
            "the air snap: extend the fouette at the peak, striking with "
            "the laces, then re-chamber before gravity reclaims the legs. "
            "Stage four, the landing: come down into la garde, knees soft, "
            "guard up - the landing is half the technique, and a stumbling "
            "landing voids the kick's value. Drill it on the crash mat for "
            "a month: jump, chamber, snap, land, freeze, check the guard. "
            "Only then take it to the bag, and only then to a retreating "
            "partner at half speed. The demo computes the airtime from jump "
            "height, the kick window inside that airtime, and the added "
            "impact mass the falling body contributes."
        ),
        "key_points": [
            "The kick is thrown at the jump's peak - the only moment the airborne body is stable enough.",
            "Thirty-five centimeters of vertical jump is the entry ticket; the kick needs that airtime.",
            "Jump, chamber, snap, re-chamber, land in la garde - the landing is half the technique.",
            "The jump adds the falling body's mass to the strike but commits the tireur to an unchangeable path.",
            "A spice, not a staple: best against retreat, worst as an opening gamble.",
        ],
        "requirements": [
            "A thirty-five-centimeter vertical jump, measured - no jump, no saut.",
            "An automatic standing fouette; the air version is the same kick with the floor removed.",
            "A crash mat for the first month; the landing is drilled before the kick is.",
            "Leg power conditioning: box jumps and depth jumps twice weekly.",
            "A coach's clearance before the saut is used against any partner - the risk is real.",
        ],
        "standards": [
            "Jumping kicks are legal in combat and permitted controlled in assaut.",
            "The landing in guard is the safety criterion; stumbling landings are a fault.",
            "A missed jumping kick that leaves the thrower defenseless is scored for the opponent's answer.",
        ],
        "citations": [CIT_BARUZY, CIT_FISAV],
        "sig_lens": (
            "The Signature read: the saut is the seal pressed mid-air - "
            "the signature written while jumping over the desk. It commits "
            "everything to one airborne flourish. The Signature Savate "
            "Method jumps only when the document is worth the risk, lands "
            "in guard, and lets the thud of the landing punctuate the "
            "sentence."
        ),
    },
    {
        "key": "riposte",
        "name": "La Riposte: Answering Under Fire",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "La riposte is the immediate answer: the strike thrown in the "
            "instant after a successful defense, while the opponent's "
            "attack is still extended and his guard still open. It is the "
            "highest-value exchange in savate - the parade that becomes a "
            "cross, the slip that becomes a hook, the shin-check that "
            "becomes a bas - because it punishes the exact moment of "
            "maximum vulnerability. The riposte window is brutally short: "
            "about four-tenths of a second from the parry's contact to the "
            "opponent's guard recovery, and the answer must be chosen "
            "before the defense is even finished. Tireurs drill ripostes "
            "as fixed pairs - this parade always answers with that cross - "
            "until the pair is a single reflex, because there is no time "
            "to decide in the window. The riposte is what separates the "
            "defensive tireur from the complete one: the first survives "
            "the attack, the second makes the attacker pay for throwing it."
        ),
        "how_it_works": (
            "Drill the four fixed pairs. Pair one: parry the jab with the "
            "lead glove, and as the glove deflects, the rear cross is "
            "already launching down the opened line - the parry's outward "
            "motion becomes the cross's chamber. Pair two: slip the cross "
            "outside, and the lead hook is already traveling - the slip's "
            "head movement loads the hook's pivot. Pair three: check the "
            "fouette with the shin, and the bas chops the now-weighted "
            "support leg before it can reset. Pair four: parry the jab and "
            "answer with the median fouette to the ribs the parry exposed. "
            "Practice each pair as one word, not two: the partner throws at "
            "half speed, and the tireur's defense-answer must land inside "
            "the four-tenths window - the coach counts it aloud until the "
            "timing is felt. Then randomize the attack and let the tireur "
            "choose the pair; then spar with the rule that only ripostes "
            "score. The demo computes the riposte window from parry contact "
            "to guard recovery, the launch deadline, and the scoring value "
            "of each fixed pair."
        ),
        "key_points": [
            "The riposte is the strike thrown in the instant after a successful defense, into the attacker's open guard.",
            "The window is about 0.4 seconds from parry contact to guard recovery - the answer must be pre-chosen.",
            "Drill fixed pairs until each is one reflex: parry-cross, slip-hook, check-bas, parry-fouette.",
            "The defense's motion becomes the answer's chamber - the parry loads the cross, the slip loads the hook.",
            "It separates the defensive tireur from the complete one: the first survives, the second makes the attacker pay.",
        ],
        "requirements": [
            "Reflexive basic defenses - the riposte is built on parries and slips that need no thought.",
            "A partner throwing honest attacks at increasing speed, and a coach counting the 0.4-second window aloud.",
            "The four fixed pairs drilled to reflex before any free choice is allowed.",
            "Sparring rounds where only ripostes score, to force the answer habit.",
            "Full gear - ripostes are thrown at real speed into real openings.",
        ],
        "standards": [
            "The riposte is the classical crown of defensive technique in the French school.",
            "In assaut, the defense-answer exchange is the highest-valued scoring unit.",
            "The answer must follow the defense immediately; a delayed strike is scored as a separate exchange.",
        ],
        "citations": [CIT_CHARLEMONT_1899, CIT_FISAV],
        "sig_lens": (
            "The Signature read: the riposte is the annotation - the note "
            "written in the margin the instant the opponent's line is "
            "read. His attack is the text; your parry is the finding; the "
            "riposte is the correction published before he finishes the "
            "paragraph. The Signature Savate Method annotates in four "
            "tenths of a second, in ink."
        ),
    },
    {
        "key": "balayage",
        "name": "Le Balayage: The Sweep",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Le balayage is the sweep: a low, hooking kick that catches "
            "the opponent's supporting foot or ankle and removes it, "
            "toppling his structure rather than striking it. The foot "
            "travels just above the floor - about ten centimeters - and "
            "hooks inward with the inner edge or the sole, contacting the "
            "ankle as the opponent's weight commits to it. The physics are "
            "leverage, not impact: the ankle is the far end of a "
            "ninety-five-centimeter lever (the opponent's leg), and a small "
            "force applied there, timed to his weight transfer, rotates the "
            "whole body. The sweep is savate's quietest takedown and its "
            "most timing-dependent technique - thrown a tenth of a second "
            "early it pushes a planted foot, thrown a tenth late it meets "
            "empty air. It is drilled as a complement to the kicking game: "
            "when the opponent starts checking the bas, the sweep takes "
            "the leg he lifts to check with."
        ),
        "how_it_works": (
            "Throw the sweep in five beats. Step one: from la garde, drop "
            "the level slightly and swing the kicking foot low, no higher "
            "than ten centimeters off the floor - the sweep travels under "
            "the opponent's attention. Step two: time it to his step - the "
            "contact must land as his weight transfers onto the target "
            "foot, the moment the foot is loaded but not yet planted. Step "
            "three: hook the inner edge or sole against his ankle and pull "
            "through in the direction his weight is moving - the sweep "
            "assists his motion, it never fights it. Step four: keep your "
            "own guard high and your weight centered; the sweeper who leans "
            "into the sweep falls with the swept. Step five: as he "
            "stumbles, be already back in la garde - the sweep's value is "
            "the follow-up it creates, and you must be balanced to take "
            "it. Drill it with a walking partner: he walks the pas chasse "
            "back and forth, and you sweep the ankle on his weight "
            "transfer - ten clean timing hits per leg before any speed. "
            "The demo computes the lever mechanics, the timing window "
            "around the weight transfer, and the toppling torque from a "
            "small applied force."
        ),
        "key_points": [
            "The foot travels about ten centimeters off the floor and hooks the ankle with the inner edge or sole.",
            "Contact lands as the opponent's weight transfers onto the foot - loaded but not yet planted.",
            "The sweep assists his motion, never fights it; leverage topples him, not impact.",
            "A tenth of a second early pushes a planted foot; a tenth late meets empty air - timing is the technique.",
            "Stay centered and back in la garde instantly; the sweep's value is the follow-up it creates.",
        ],
        "requirements": [
            "A reliable coup de pied bas - the sweep is its timing-obsessed cousin, learned after the chop is automatic.",
            "A walking partner for timing drills; ten clean hits per leg before any speed is added.",
            "Mats for the drilling area - partners will fall, and the fall is part of the drill.",
            "Ankle mobility and low-line control: the foot must travel flat and low without scraping.",
            "A coach to call the weight-transfer moment aloud until the tireur feels it.",
        ],
        "standards": [
            "Sweeps are permitted in savate competition within the technical regulations.",
            "The ankle is the target; sweeping above the ankle is a fault.",
            "A clean sweep that off-balances the opponent scores; the follow-up must remain controlled in assaut.",
        ],
        "citations": [CIT_CHARLEMONT_1899, CIT_FISAV],
        "sig_lens": (
            "The Signature read: the balayage is the pulled rug - the "
            "footnote that removes the floor the argument stood on. No "
            "force, only timing; no impact, only leverage. The Signature "
            "Savate Method pulls rugs at ten centimeters: the smallest "
            "stroke with the largest consequence."
        ),
    },
    {
        "key": "esquive_totale",
        "name": "Les Esquives Totales: Full-Body Evasion",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Les esquives totales are the full-body evasions: moving the "
            "entire torso out of the attack's path - the lean-back from "
            "the high fouette, the deep side-step from the swinging kick, "
            "the full duck under the figure. Where the basic esquive moves "
            "the head inches, the totale moves the body feet, and it is "
            "reserved for the attacks that cannot be parried: the committed "
            "swinging kicks, the jumping attacks, the combinations whose "
            "second half is already coming. The lean-back is the signature "
            "move - the torso hinges at the hips, the head traveling back "
            "half a meter as the high kick passes through the space the "
            "face just left, and the hands stay up to catch the follow. "
            "The risk is the recovery: a full evasion leaves the tireur "
            "extended and must be drilled with an immediate return - the "
            "lean becomes a spring that fires the counter. Evasion without "
            "the return is just retreat with style."
        ),
        "how_it_works": (
            "Drill the three totales. One, the lean-back: as the high "
            "fouette comes, hinge at the hips and lay the torso back, the "
            "head traveling half a meter rearward while the feet stay "
            "planted - the kick passes through empty air where the face "
            "was, and the hands remain up to parry the follow. Two, the "
            "deep side-step: against the swinging kick, take a full pas "
            "chasse laterally as the kick launches, letting the arc pass "
            "across the vacated line, then step back in with the counter. "
            "Three, the full duck: bend the knees deeply and drop the whole "
            "body under the figure's line, the guard shelling the head, "
            "then rise with the remontant into the exposed torso. Each "
            "totale is drilled as evade-and-return: the partner throws the "
            "committed attack at increasing speed, the tireur evades fully "
            "and must land the scripted counter before the partner resets - "
            "evasion without the return fails the drill. The demo computes "
            "the head displacement of the lean-back, the clearance margin "
            "against the kick's arc, and the return time that keeps the "
            "counter inside the window."
        ),
        "key_points": [
            "Full-body evasions are reserved for unparryable attacks: swinging kicks, jumping attacks, committed combinations.",
            "The lean-back hinges at the hips, moving the head half a meter as the high kick passes through empty air.",
            "Hands stay up through every evasion to catch the follow-up attack.",
            "Every totale is drilled as evade-and-return; evasion without the counter fails the drill.",
            "Evasion without the return is just retreat with style.",
        ],
        "requirements": [
            "Reflexive basic esquives - the totales are the big siblings, learned after the small ones are automatic.",
            "Core and hip-hinge strength: deadlifts and good-mornings for the lean-back's hinge.",
            "A partner throwing committed attacks at increasing speed, with full gear on both sides.",
            "The scripted counter for each evasion, drilled as one word: evade-RETURN.",
            "A coach to verify the feet stay planted in the lean-back - stepping back turns it into mere retreat.",
        ],
        "standards": [
            "Full-body evasion is a classical advanced defensive element of the French school.",
            "In assaut, a clean totale followed by a counter is among the highest-valued exchanges.",
            "Evasion that leaves the fighting space is penalized; the totale stays in range to answer.",
        ],
        "citations": [CIT_CHARLEMONT_1899, CIT_FISAV],
        "sig_lens": (
            "The Signature read: the esquive totale is the page turned - "
            "the whole sheet moved aside so the opponent's ink lands on "
            "the desk, and then the page turns back with your own line "
            "already written. The Signature Savate Method turns pages at "
            "the hips: half a meter of absence, then the annotation."
        ),
    },
])
ENTRIES.extend([
    {
        "key": "combos_avancees",
        "name": "Les Combinaisons Avancees: Four-Move Chains",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Les combinaisons avancees are the four- and five-move chains: "
            "the point where savate becomes composition. Where the "
            "three-strike chains have fixed classic forms, the advanced "
            "chains are built by the tireur for the opponent in front of "
            "him - jab, bas, cross, figure against the guard that drops; "
            "fouette, chasse, hook, remontant against the tireur who "
            "retreats straight back. The construction principles are the "
            "advanced curriculum: alternate the levels (high-low-high) so "
            "the guard cannot settle, alternate the sides (lead-rear-lead) "
            "so the weight keeps surfing, and always finish with the "
            "heaviest weapon the chain's rhythm has earned - the fourth "
            "strike lands hardest because the first three bought its "
            "opening. The great danger of long chains is the fourth "
            "strike's telegraphing: by strike three the opponent has the "
            "rhythm, so the advanced tireur learns to break it - "
            "fast-fast-SLOW, or the stutter step that turns a four into a "
            "three-and-a-half. Chains are drilled on the pads until the "
            "coach cannot hear the seams, then pressure-tested in sparring "
            "where only completed chains score."
        ),
        "how_it_works": (
            "Compose chains by the three principles. Principle one, "
            "alternate levels: build jab (high), bas (low), cross (high), "
            "figure (high) - the guard chases the level changes and is "
            "always one beat behind. Principle two, alternate sides: lead "
            "fouette, rear chasse, lead hook, rear remontant - the weight "
            "surfs continuously and no strike starts from a dead stance. "
            "Principle three, the earned finish: the first three strikes "
            "are investments, the fourth is the withdrawal - make it the "
            "swinging fouette or the rear remontant, the heaviest tool the "
            "rhythm allows. Then learn the break: drill the chain "
            "fast-fast-fast, then drill it fast-fast-SLOW, the pause a "
            "fraction of a beat that makes the opponent's counter arrive "
            "early and miss. Practice on the pads in sets of five per "
            "chain, the coach calling the chain number and checking that "
            "the guard is whole at the end and the rhythm has no seams. "
            "Spar with the completed-chain rule: only chains of four that "
            "finish in guard score. The demo computes the permutation "
            "space of four-move chains from eight tools, the duration of "
            "each composed chain, and the timing of the rhythm break."
        ),
        "key_points": [
            "Four- and five-move chains composed for the opponent in front of you, not recited from a list.",
            "Alternate levels (high-low-high) so the guard cannot settle; alternate sides so the weight keeps surfing.",
            "The fourth strike is the earned finish - the heaviest weapon the first three strikes bought.",
            "Break the rhythm: fast-fast-SLOW, or the stutter step, so the opponent's timed counter arrives early and misses.",
            "Drill until the coach cannot hear the seams; spar with the rule that only completed chains score.",
        ],
        "requirements": [
            "All three classic three-strike chains at full speed - the advanced chains extend them.",
            "Pads and a coach who can hear seams: the rhythm must be continuous, the guard whole at the end.",
            "A notebook: write each composed chain down, with its opponent-type and its rhythm pattern.",
            "Sparring rounds with the completed-chain scoring rule, full gear.",
            "The honesty to abandon a composed chain that the opponent has solved - composition is ongoing.",
        ],
        "standards": [
            "Four-plus-strike composed chains are the advanced graded combination level in the FFBFSDA curriculum.",
            "In assaut, a completed composed chain is the premier technical demonstration.",
            "Chains must remain controlled; the fourth strike thrown wild voids the chain's value.",
        ],
        "citations": [CIT_FFBFSDA, CIT_CHARLEMONT_1899, CIT_FISAV],
        "sig_lens": (
            "The Signature read: the advanced combination is the "
            "illuminated manuscript - levels alternating like decorated "
            "capitals, sides alternating like margins, the fourth strike "
            "the gilded initial. The Signature Savate Method composes for "
            "the reader in front of it, breaks the rhythm like a "
            "watermark, and signs the whole page in under a second."
        ),
    },
    {
        "key": "jeu_jambes",
        "name": "Le Jeu de Jambes Avance: Advanced Footwork and Angles",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Le jeu de jambes avance is advanced footwork: the angled "
            "steps, pivots, and lateral shifts that put the tireur beside "
            "the opponent's guard instead of in front of it. The core move "
            "is the forty-five-degree cut - stepping diagonally forward "
            "and outward so the tireur's center line clears the opponent's "
            "shoulder, leaving him facing empty space while the tireur's "
            "weapons face his flank. Built on the pivot and the lateral pas "
            "chasse, the advanced game adds the switch-step (changing lead "
            "leg mid-motion to attack from the unexpected side), the "
            "pendulum step (rocking in to draw the counter, then rocking "
            "out as it misses), and the angle-after-attack (every strike "
            "ends with a step to the side, so the tireur is never where "
            "the return fire is aimed). Advanced footwork is invisible "
            "work: the audience watches the kicks, but the tireur knows "
            "the angle won the exchange before the kick was thrown. It is "
            "drilled with cones, with chalk angles on the floor, and "
            "finally against the live opponent who punishes straight-line "
            "movement."
        ),
        "how_it_works": (
            "Drill the four advanced steps. One, the forty-five-degree cut: "
            "from la garde, step the lead foot diagonally forward-outward "
            "about fifty-seven centimeters for every eighty centimeters of "
            "forward travel, the rear foot following - you should finish "
            "beside the opponent's lead shoulder, your center line clear "
            "of his. Two, the switch-step: mid-advance, hop-switch the "
            "feet so the rear leg becomes the lead, then attack immediately "
            "from the new side - the opponent's guard is set for the old "
            "lead. Three, the pendulum: rock forward into range to draw the "
            "jab, then rock back out on its beat - the second rock is the "
            "real entry, timed to his recovery. Four, the angle-after-"
            "attack: after every kick or combination, take one lateral pas "
            "chasse before resetting - never stand where you just attacked "
            "from. Practice with floor chalk: draw the forty-five-degree "
            "lines and hit the marks for ten minutes, then remove the "
            "chalk and keep the angles. Spar with the straight-line "
            "penalty: every exchange fought on the center line is lost. "
            "The demo computes the cut geometry, the lateral displacement "
            "per step, and the angle advantage of the flank position."
        ),
        "key_points": [
            "The forty-five-degree cut puts you beside the opponent's guard instead of in front of it.",
            "The switch-step changes the lead leg mid-motion and attacks from the unexpected side.",
            "The pendulum draws the counter with a false entry, then makes the real entry on its beat.",
            "Every attack ends with an angle step - never stand where you just attacked from.",
            "Advanced footwork is invisible: the angle wins the exchange before the kick is thrown.",
        ],
        "requirements": [
            "Automatic pas chasse, pivot, and lateral movement - the advanced steps are built on them.",
            "Floor chalk or cones to mark the forty-five-degree lines for the first month.",
            "Ten minutes of angle drills per session, then chalk removed - the angles must live in the feet.",
            "A sparring partner who punishes straight-line movement, enforcing the angle habit.",
            "Video review: the tireur should be visibly off the center line after every exchange.",
        ],
        "standards": [
            "Angled footwork is the advanced movement element of the classical French school.",
            "In assaut, the tireur who consistently takes the angle is judged the technical superior.",
            "Straight-line retreat under pressure is the fault the advanced game exists to cure.",
        ],
        "citations": [CIT_CHARLEMONT_1899, CIT_FFBFSDA],
        "sig_lens": (
            "The Signature read: advanced footwork is the watermark - "
            "visible only when the page is held to the light, decisive "
            "all the same. The forty-five-degree cut is the signature "
            "slanting across the corner of the document. The Signature "
            "Savate Method never stands where it just wrote; it is always "
            "already beside the reader."
        ),
    },
    {
        "key": "coups_retournes",
        "name": "Les Coups de Pied Retournes: Turning Kicks",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Les coups de pied retournes are the turning kicks: techniques "
            "in which the tireur rotates fully - a half or full turn - and "
            "delivers the kick from the rotation, usually a revers or a "
            "fouette thrown as the body completes its spin. The turning "
            "fouette and the turning chasse are the common forms: the "
            "tireur pivots on the lead foot, the body rotates three hundred "
            "sixty degrees, and the kick extends during the final hundred "
            "twenty degrees of the turn, arriving with the rotation's full "
            "momentum behind it. They are the highest-risk, highest-reward "
            "kicks in savate: the turn blinds the tireur for a fraction of "
            "a second, and a mistimed turn presents the back - but a clean "
            "turning kick lands with a force no standing kick can match, "
            "and its arrival angle defeats guards set for linear attacks. "
            "Tireurs earn the turn only after the swinging kicks are "
            "automatic, and they throw it in competition only in the "
            "situations the turn favors: against the ropes, after a "
            "combination that has the opponent covered, or as the "
            "punishment for a missed attack."
        ),
        "how_it_works": (
            "Build the turning revers in stages. Stage one, the turn alone: "
            "from la garde, pivot on the lead foot and rotate the full "
            "three hundred sixty degrees, spotting the opponent over the "
            "shoulder at the end - drill until the turn takes under "
            "fifty-five hundredths of a second and ends in perfect guard. "
            "Stage two, the kick insertion: during the final hundred twenty "
            "degrees of the turn, extend the revers with the outer edge, "
            "timing the extension so contact happens as the rotation "
            "completes - the kick is the turn's punctuation, not a separate "
            "event. Stage three, the spot: pick the target before the turn "
            "starts, because mid-turn vision is unreliable; the kick goes "
            "where the eyes last saw the target. Stage four, the recovery: "
            "the rotation's momentum must be braked into la garde - drill "
            "the stop as its own skill, because the turn that cannot stop "
            "is a fall. Practice on the bag for a month before any partner "
            "work, and throw it in sparring only on the coach's call. The "
            "demo computes the turn time, the kick's arrival speed with "
            "rotational momentum, and the blind fraction of the rotation."
        ),
        "key_points": [
            "The body rotates fully and the kick extends during the final 120 degrees - the kick is the turn's punctuation.",
            "Pick the target before the turn starts; mid-turn vision is unreliable.",
            "The turn must complete in under 0.55 seconds and end in perfect guard.",
            "The rotation's momentum must be braked into la garde - the turn that cannot stop is a fall.",
            "Thrown only in favored situations: against the ropes, after covering combinations, or punishing a miss.",
        ],
        "requirements": [
            "Automatic swinging revers and fouette - the turn multiplies owned kicks, it does not create them.",
            "A 0.55-second full turn ending in guard, timed - the turn is the prerequisite, not the kick.",
            "Crash mats for the first month; mistimed turns end on the floor.",
            "Exceptional core strength for the rotational braking: Russian twists and Pallof presses.",
            "A coach's explicit clearance before the turning kick is used against any partner.",
        ],
        "standards": [
            "Turning kicks are legal in combat; in assaut they must remain controlled despite the momentum.",
            "Presenting the back without attacking is a fault - the turn must deliver the kick.",
            "The guarded landing is the safety criterion in technical examinations.",
        ],
        "citations": [CIT_BARUZY, CIT_FISAV],
        "sig_lens": (
            "The Signature read: the turning kick is the signature with a "
            "flourish that circles the whole page - the pen leaves the "
            "paper, loops the air, and lands the final stroke with "
            "everything behind it. The Signature Savate Method turns only "
            "when the document deserves the ceremony, and brakes the "
            "flourish into a perfect guard."
        ),
    },
    {
        "key": "strategie_ring",
        "name": "La Strategie de Ring: Ringcraft",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "La strategie de ring is ringcraft: the management of space, "
            "position, and pace across the rounds. The ring is six point "
            "one meters square, and the tireur who controls its geography "
            "controls the fight. The principles are positional: own the "
            "center, because the center offers exits in every direction "
            "while the ropes offer none; cut the ring with angled steps "
            "rather than chasing, so the retreating opponent runs out of "
            "space instead of out of danger; and never follow a retreating "
            "opponent in a straight line - the straight chase walks into "
            "the counter. The principles are also temporal: win the first "
            "round with volume to bank the judges' impression, control the "
            "middle with ring geography, and spend the last round's energy "
            "only where it changes the score. Ringcraft includes the dark "
            "arts of pace - clinching to rest without stalling, circling "
            "to recover without retreating - and the discipline to execute "
            "the corner's plan when the blood is up. Technique wins "
            "exchanges; ringcraft wins fights."
        ),
        "how_it_works": (
            "Install ringcraft in four habits. Habit one, center ownership: "
            "in every sparring round, the tireur's default position is the "
            "center meter of the ring - after every exchange, the feet "
            "return there, and the opponent is the one maneuvered toward "
            "the ropes. Habit two, the cut: when the opponent retreats, "
            "step at forty-five degrees to intercept his path rather than "
            "following it - two angled steps close more space than four "
            "straight ones, and they keep you off his counter line. Habit "
            "three, the trap: once the opponent's back is near the ropes, "
            "take the lateral angle and work the body - the ropes remove "
            "his retreat, and the angle removes his lateral escape. Habit "
            "four, the clock: divide each round into thirds in your head - "
            "first third establishes volume, second third establishes "
            "position, final third spends energy only on scoring "
            "exchanges. Drill the cut-and-trap with a retreating partner "
            "for entire rounds; the only scoring strikes are those thrown "
            "after a successful angle cut. The demo computes the ring's "
            "geometry, the step savings of the angled cut, and the "
            "corner-trap's escape denial."
        ),
        "key_points": [
            "Own the center: it offers exits in every direction while the ropes offer none.",
            "Cut the ring with forty-five-degree steps - two angled steps close more space than four straight ones.",
            "Never chase in a straight line; the straight chase walks into the counter.",
            "Trap at the ropes: take the lateral angle, work the body, remove the retreat and the lateral escape.",
            "Divide each round into thirds: volume, position, then spend energy only where it changes the score.",
        ],
        "requirements": [
            "Advanced footwork automatic - ringcraft is angles applied to geography, not a separate subject.",
            "A full-size ring or marked 6.1-meter square for cut-and-trap drilling.",
            "Sparring rounds scored only on post-cut strikes, to install the cutting habit.",
            "A corner team or coach who calls the round-thirds plan between rounds.",
            "Fight video review: map your positions round by round until center ownership is visible.",
        ],
        "standards": [
            "Ringcraft is the strategic element of competition savate under FISav regulations.",
            "Excessive holding to rest is penalized; circling and angling are legitimate recovery.",
            "Judges score ring control as a criterion in close rounds.",
        ],
        "citations": [CIT_FISAV, CIT_FFBFSDA],
        "sig_lens": (
            "The Signature read: ringcraft is the document layout - "
            "margins, columns, and whitespace arranged so the reader goes "
            "where you want. The center is the headline position; the "
            "ropes are the fine print at the edge. The Signature Savate "
            "Method lays out every round like a page: own the headline, "
            "trap the reader in the margins, and sign at the bottom."
        ),
    },
    {
        "key": "specialites",
        "name": "Les Specialites de Pied: Signature Foot Techniques",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Les specialites de pied are the tireur's personal specialties: "
            "the one or two kicks, refined over years, that become his "
            "trademark - the double fouette that lands twice from one "
            "chamber, the chassé that stops everything, the figure that "
            "never misses. Every elite tireur has them, and they are built "
            "deliberately: choose the kick whose mechanics suit your body - "
            "long legs favor the swinging kicks, fast hips favor the "
            "chambered snap - then drill it ten thousand times across every "
            "situation until it is available tired, hurt, and behind on "
            "points. The double fouette is the classic specialty: the knee "
            "chambers once, the lower leg snaps to the ribs, re-chambers "
            "without dropping, and snaps again to the head - two impacts, "
            "one plant, thirty-five hundredths of a second apart, defeating "
            "the guard that answered the first kick. Specialties are also "
            "strategic: the opponent prepares for your ordinary game, and "
            "the specialty is the deviation he cannot prepare for. Build "
            "two, keep one secret until it matters."
        ),
        "how_it_works": (
            "Build the double fouette specialty. Step one: throw the median "
            "fouette, but instead of planting after the re-chamber, hold "
            "the chamber - the knee stays up, the guard stays set, and the "
            "opponent's hands stay down where the first kick put them. Step "
            "two: within thirty-five hundredths of a second, snap the "
            "second fouette upward to the figure line - the guard is still "
            "answering kick one when kick two arrives. Step three: plant "
            "into la garde only after the second impact; the single plant "
            "is what makes it a specialty rather than two kicks. Drill it "
            "in layers: first the chamber-hold for balance (thirty seconds "
            "per leg), then the double snap on the bag (the bag should "
            "take two distinct hits), then the timing - the partner holds "
            "the pad low for kick one and high for kick two, and the gap "
            "must stay under 0.35 seconds. Choose your second specialty by "
            "body type and drill it the same way: ten thousand "
            "repetitions, every situation, until it is the technique you "
            "trust when nothing else works. The demo computes the double "
            "kick's timing gap, the guard-recovery deficit it exploits, and "
            "the repetition count of the specialty program."
        ),
        "key_points": [
            "A specialty is one kick refined over years until it is available tired, hurt, and behind on points.",
            "Choose by body type: long legs favor swinging kicks, fast hips favor the chambered snap.",
            "The double fouette: one chamber, two snaps - ribs then head, 0.35 seconds apart, one plant.",
            "The second kick defeats the guard that answered the first; the single plant makes it one technique.",
            "Build two specialties and keep one secret until it matters.",
        ],
        "requirements": [
            "Mastery of the base kick - the specialty is a refinement, and refinement needs something to refine.",
            "Ten thousand repetitions across every situation: fresh, tired, pressured, behind on points.",
            "The chamber-hold balance drill: thirty seconds per leg before the double snap is attempted.",
            "A pad holder who can present low-then-high targets with the 0.35-second gap enforced.",
            "A coach's eye on the body-type match - the wrong specialty for your build is a wasted year.",
        ],
        "standards": [
            "Specialty techniques must remain within the legal techniques of the FISav regulations.",
            "In assaut, the double kick's both impacts must be controlled to score.",
            "The specialty is demonstrated in advanced FFBFSDA gradings as the tireur's personal technique.",
        ],
        "citations": [CIT_FFBFSDA, CIT_FISAV, CIT_BARUZY],
        "sig_lens": (
            "The Signature read: the specialty is the personal seal - the "
            "unique stamp no other hand can replicate, pressed ten "
            "thousand times until the die is perfect. The double fouette "
            "is the seal struck twice in one motion. The Signature Savate "
            "Method issues each tireur exactly one seal, and it is "
            "recognized across every ring it touches."
        ),
    },
    {
        "key": "preparation",
        "name": "La Preparation du Tireur: Fighter Conditioning",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "La preparation du tireur is the fighter's conditioning: the "
            "physical program that lets technique survive the third round. "
            "Savate fitness has four pillars. The engine: roadwork and "
            "interval running, because a savate bout is three to five "
            "rounds of three minutes with one-minute rests, and the "
            "aerobic base decides who is still kicking in the last minute. "
            "The weapons: leg power for the kicks - squats, lunges, box "
            "jumps - and rotational core power for the hip turn behind "
            "every strike. The armor: neck, shoulder, and shin conditioning "
            "to absorb the contact the sport guarantees. The recovery: "
            "sleep, nutrition, and the discipline to rest, because "
            "overtraining breaks more tireurs than opponents do. The "
            "program is periodized across the fight camp: base building "
            "eight weeks out, intensity peaking four weeks out, taper in "
            "the final ten days. Conditioning is the least glamorous "
            "record in this database and the one that decides the most "
            "fights - technique chooses the winner only when both tireurs "
            "can still execute it."
        ),
        "how_it_works": (
            "Run the eight-week camp. Weeks one to three, the base: five "
            "kilometer runs three times weekly at conversational pace, "
            "three strength sessions (squat, lunge, press, row, core), and "
            "daily mobility - the aerobic engine is built slow. Weeks four "
            "to six, the intensity: replace one run with round intervals - "
            "three minutes hard, one minute easy, five repetitions, "
            "mirroring the bout's work-rest ratio - and add pad rounds at "
            "fight pace. Week seven, the peak: full sparring rounds in "
            "number, intensity dropping ten percent to stay sharp without "
            "breaking. Week eight, the taper: volume halves, intensity "
            "stays, sleep goes to nine hours, and the weight cut - if any - "
            "finishes three days before the bout. Track three numbers "
            "weekly: resting heart rate (it should fall), round output "
            "(strikes per round, it should rise), and body weight. Eat for "
            "the work: the camp burns roughly thirteen kilocalories per "
            "minute of hard rounds, and the tireur who under-eats "
            "under-recovers. The demo computes the camp's weekly volumes, "
            "the work-rest energetics of a three-minute round, and the "
            "caloric cost across the full bout."
        ),
        "key_points": [
            "Four pillars: the aerobic engine, leg and rotational power, contact armor, and recovery discipline.",
            "Eight-week camp: base building, then intensity, then peak sparring, then a ten-day taper.",
            "Round intervals mirror the bout: three minutes hard, one minute easy, five repetitions.",
            "Track resting heart rate, strikes per round, and body weight weekly - the numbers tell the truth.",
            "Overtraining breaks more tireurs than opponents do; sleep and nutrition are training.",
        ],
        "requirements": [
            "A training log: every run, session, and sparring round recorded - the camp is managed by numbers.",
            "Access to road or track, a strength setup (squat, lunge, press, row), and pads for round work.",
            "A heart-rate monitor for the interval sessions and the resting-rate trend.",
            "Nine hours of sleep in the taper weeks; the camp fails without recovery.",
            "A coach to call the taper - tired tireurs always want one more hard week, and it is always wrong.",
        ],
        "standards": [
            "Bout format under FISav: three to five rounds of three minutes with one-minute rests (assaut typically shorter).",
            "Weight management follows the federation's weigh-in regulations; dangerous cuts are prohibited.",
            "Medical clearance is required for competition; the conditioning program assumes a healthy tireur.",
        ],
        "citations": [CIT_FISAV, CIT_FFBFSDA],
        "sig_lens": (
            "The Signature read: conditioning is the paper - nobody "
            "applauds the paper, but no signature survives bad stock. The "
            "engine, the power, the armor, the recovery: four fibers in "
            "the sheet. The Signature Savate Method mills its paper over "
            "eight weeks, and the signature it carries into the third "
            "round is still legible."
        ),
    },
    {
        "key": "assaut_combat",
        "name": "L'Assaut et le Combat: Rules and Competition",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "L'assaut et le combat are the two competition formats of "
            "savate, and understanding them is what turns training into "
            "sport. In l'assaut, the tireurs fence with controlled contact: "
            "techniques must touch cleanly but without force intended to "
            "harm, and the judges score technical merit - precision, "
            "variety, defense, and ring control. It is often called "
            "fencing with the feet, and it is where most tireurs compete "
            "for most of their careers. In le combat, full contact is "
            "allowed and knockouts decide: the same techniques, the same "
            "ring, but the strikes carry fight-ending intent and the "
            "judging values effective damage alongside technique. Both "
            "formats use the glove grading system - gant bleu, vert, "
            "rouge, blanc, jaune - marking the tireur's technical rank, "
            "and both are fought in the savate uniform: the long pantalon "
            "and the special chaussures. Competition teaches what the gym "
            "cannot: the weight cut, the waiting room, the walk to the "
            "ring, and the first exchange against a stranger who has "
            "trained to beat you."
        ),
        "how_it_works": (
            "Prepare for competition in stages. Stage one, choose the "
            "format: begin in assaut, where controlled contact lets "
            "technique be judged without the knockout risk - most "
            "federations require assaut experience before combat "
            "clearance. Stage two, learn the scoring: in assaut, each clean "
            "controlled touch scores, with variety, effective defense, and "
            "ring control as the tiebreakers the judges actually use; in "
            "combat, effective strikes and damage decide, with knockdowns "
            "weighing heavily. Stage three, the camp: eight weeks of "
            "preparation (see the conditioning record), with the final "
            "sparring sessions fought under the format's rules - assaut "
            "sparring penalizes hard contact, combat sparring allows it. "
            "Stage four, the logistics: weigh-in procedures, equipment "
            "check (gloves, chaussures, pantalon, groin and mouth guards), "
            "and the corner team - one coach, one second, one plan. Stage "
            "five, the bout: three rounds minimum, the corner calling the "
            "round-thirds plan, the tireur executing technique rather than "
            "chasing the knockout. The demo computes a sample scorecard "
            "across three rounds under both formats, showing how the same "
            "exchanges score differently."
        ),
        "key_points": [
            "L'assaut: controlled contact, fencing with the feet, judged on technical merit - where most careers are built.",
            "Le combat: full contact, knockouts decide, effective damage weighed alongside technique.",
            "The glove grades - bleu, vert, rouge, blanc, jaune - mark technical rank in both formats.",
            "Begin in assaut; federations require assaut experience before combat clearance.",
            "Competition teaches what the gym cannot: the cut, the wait, the walk, and the stranger across the ring.",
        ],
        "requirements": [
            "A federation license and medical clearance - no bout without both.",
            "The full uniform: pantalon, chaussures de savate, gloves, groin guard, mouthguard, headgear per format.",
            "An eight-week camp under the format's rules, with format-specific sparring.",
            "A corner team: one coach, one second, one plan - never compete alone.",
            "Assaut experience before any combat bout; the progression is mandatory, not suggested.",
        ],
        "standards": [
            "Competition is governed by the FISav reglement sportif et technique and national federation rules.",
            "Legal techniques, target zones, and contact levels differ by format and are defined in the regulations.",
            "Glove grades (gants) follow the FFBFSDA technical program.",
        ],
        "citations": [CIT_FISAV, CIT_FFBFSDA, CIT_BARUZY],
        "sig_lens": (
            "The Signature read: competition is the publication - the "
            "private training manuscript submitted for peer review under "
            "lights. Assaut is the journal article, judged on rigor; "
            "combat is the public defense, judged on consequence. The "
            "Signature Savate Method publishes only when the manuscript "
            "is ready, in the right journal, with the corner team as "
            "co-authors."
        ),
    },
    {
        "key": "tactiques_elite",
        "name": "Les Tactiques du Tireur d'Elite: Advanced Ring Tactics",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Les tactiques du tireur d'elite are the advanced ring tactics: "
            "the strategic layer above technique, where the tireur fights "
            "the opponent's mind. The elite game has five weapons. Pattern "
            "breaking: every tireur falls into rhythms, and the elite "
            "tireur deliberately establishes a pattern - jab, jab, fouette "
            "- then breaks it at the moment the opponent times it, "
            "punishing the anticipation. Weapon denial: identify the "
            "opponent's best strike in the first round and take it away - "
            "crowd the kicker, outrange the puncher, check the low-kick "
            "artist's every bas until he abandons it. False tempo: fight a "
            "round at half speed to teach the opponent the pace, then "
            "double it in the second when his reactions are calibrated "
            "wrong. Target programming: touch the same spot - the lead "
            "thigh, the ribs - until the opponent guards it reflexively, "
            "then attack where the guard went. And the championship "
            "rounds: the explicit plan for winning the last round when "
            "behind - the high-variance techniques, the sustained pressure, "
            "the refusal to coast. Elite tactics are honest: they are "
            "applied psychology with gloves on, and they decide the fights "
            "where both tireurs have the technique."
        ),
        "how_it_works": (
            "Install the five tactical weapons one per camp. Weapon one, "
            "pattern breaking: in sparring, deliberately throw the same "
            "three-strike sequence four times, then on the fifth, break it "
            "after strike two with the unscripted finish - the partner's "
            "anticipated defense becomes the opening. Weapon two, weapon "
            "denial: spend round one identifying the opponent's money "
            "strike, then spend round two removing it - step inside the "
            "kicker's range, extend past the puncher's, check every bas. "
            "Weapon three, false tempo: spar a full round at sixty percent "
            "pace, then open round two at full pace without warning - the "
            "calibration gap is worth a dozen clean strikes. Weapon four, "
            "target programming: land six touches on the lead thigh across "
            "two rounds, then throw the figure over the guard that now "
            "drops reflexively. Weapon five, the championship plan: write "
            "it before the bout - behind on points, final round, the plan "
            "is sustained pressure with high-variance techniques, no "
            "coasting, the corner calling the score gap between rounds. "
            "Review every bout on video and grade each weapon's use. The "
            "demo computes the unpredictability (entropy) of a four-weapon "
            "mix, the calibration gap of the false tempo, and the "
            "programmed-target payoff model."
        ),
        "key_points": [
            "Pattern breaking: establish the rhythm deliberately, then break it when the opponent times it.",
            "Weapon denial: identify the opponent's best strike in round one, take it away in round two.",
            "False tempo: teach the opponent a slow pace for a round, then double it when his reactions are miscalibrated.",
            "Target programming: touch one spot until it is guarded reflexively, then attack where the guard went.",
            "The championship plan is written before the bout: behind on points, final round, pressure and variance, no coasting.",
        ],
        "requirements": [
            "Complete technical arsenal - tactics multiply technique; they cannot replace it.",
            "A video review habit: every bout watched, every tactical weapon graded.",
            "Sparring partners of varied styles: the tactics must work against kickers, punchers, and counter-fighters.",
            "A written championship plan before every bout, and a corner that calls the score gap honestly.",
            "One camp per weapon: install the five tactics sequentially, not simultaneously.",
        ],
        "standards": [
            "Advanced tactics are the strategic layer of competition savate under FISav regulations.",
            "All tactical weapons must remain within legal techniques; gamesmanship outside the rules is penalized.",
            "Elite competition expects assaut mastery before combat; tactics are layered on that foundation.",
        ],
        "citations": [CIT_FISAV, CIT_CHARLEMONT_1899],
        "sig_lens": (
            "The Signature read: elite tactics are the cipher - the "
            "message written so the opponent reads the wrong plaintext. "
            "Pattern breaking is the key change, weapon denial the "
            "redacted passage, false tempo the misleading preface. The "
            "Signature Savate Method encrypts in the ring and decrypts "
            "only for the judges: by the final bell, the plaintext is "
            "yours."
        ),
    },
])
