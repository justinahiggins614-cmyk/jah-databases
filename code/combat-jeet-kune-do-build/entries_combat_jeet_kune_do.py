#!/usr/bin/env python3
"""Entries for the Jeet Kune Do Combat databases (combat batch 2, 2026-10-17).

Two NEW databases, 34 ladder-ordered records each:

  combat-jeet-kune-do              - The Jeet Kune Do Combat Database
                                      (public-harvest: real, fact-checked
                                      jeet kune do knowledge - Bruce Lee's
                                      way of the intercepting fist: the
                                      bai-jong on-guard stance, the push-step
                                      footwork, the straight lead, the five
                                      ways of attack, pak sao / lop sao /
                                      jut sao trapping, stop hits and stop
                                      kicks, broken rhythm and economy of
                                      motion - every technique taught as a
                                      full record with step-by-step body
                                      mechanics; standard references Lee
                                      Tao of Jeet Kune Do 1975, Bruce Lee's
                                      Fighting Method Complete Edition 2008,
                                      Inosanto Jeet Kune Do: The Art and
                                      Philosophy of Bruce Lee 1980, and
                                      Little The Warrior Within 1996)
  combat-jeet-kune-do-signature    - The Jeet Kune Do Combat Signature
                                      Database
                                      (his original Signature combat method:
                                      every technique a covenant of body and
                                      breath, the stance the oath of the
                                      ground, the intercepting fist the
                                      signature of the reader of motion;
                                      src signature, titles suffixed
                                      " (Signature Edition)", never
                                      presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBJKD- (public) and JAH-CBJKDS- (signature), verified free
in the manifest id_prefix values and zero hits in every shard index file.

Dedupe: all 68 titles (34 public + 34 Signature Edition) run through the
whole-system dedupe gate before authoring - zero refusals, zero collisions.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_jeet_kune_do.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos. Demo
numbers cross-check the entry text they accompany.

Screening: civilian martial-arts instruction only. Nothing hate-adjacent,
profane, or inappropriate; no religious talk. Nothing on neutralizing or
defeating military or defense-grade systems - the standing exclusion holds.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature combat method: every "
            "technique a covenant of body and breath, the stance the oath of "
            "the ground, the intercepting fist the signature of the reader of "
            "motion, trapping the handshake that never lets go. Clearly "
            "labeled Signature-made, never presented as authentic public "
            "record.")

CIT_TAO = ("Lee B. Tao of Jeet Kune Do. Santa Clarita: Ohara Publications; "
           "1975.")
CIT_FIGHTING_METHOD = ("Lee B. Bruce Lee's Fighting Method: The Complete "
                       "Edition. Valencia: Black Belt Communications; 2008.")
CIT_INOSANTO = ("Inosanto D. Jeet Kune Do: The Art and Philosophy of Bruce "
                "Lee. Los Angeles: Know Now Publishing; 1980.")
CIT_WARRIOR_WITHIN = ("Little J, ed. The Warrior Within: The Philosophies of "
                      "Bruce Lee. Chicago: Contemporary Books; 1996.")

ENTRIES = [
    {
        "key": "baijong",
        "name": "Bai-Jong Stance - The On-Guard Position",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description":
            "Bai-jong, the ready stance, is the on-guard position of jeet kune "
            "do and the platform every technique in the system launches from. "
            "The strong side leads: a right-handed practitioner stands with the "
            "right foot forward, because the lead side carries the system's "
            "primary weapons - the straight lead and the lead leg kicks - and "
            "keeping them closest to the opponent shortens every attack. The "
            "feet sit about a shoulder-width apart, the lead toe points at the "
            "opponent and the rear foot angles about forty-five degrees, the "
            "rear heel lifted just enough to stay spring-loaded. Weight rests "
            "evenly, about fifty percent on each leg, the knees softly bent, "
            "the chin tucked behind the lead shoulder. From this coil the "
            "practitioner can advance, retreat, angle, or intercept without "
            "first shifting weight - that readiness is the whole point of the "
            "stance.",
        "how_it_works":
            "Stand with the strong-side foot forward and the weak-side foot "
            "back, the feet about one shoulder-width apart front to back and "
            "side to side. Point the lead toe directly at the opponent and "
            "angle the rear foot about forty-five degrees outward, lifting the "
            "rear heel roughly two finger-widths off the floor. Bend both "
            "knees softly and settle the weight evenly, about fifty percent on "
            "each leg - a partner pushing your shoulders should not topple "
            "you in any direction. Raise the lead hand to chin height, "
            "extended toward the opponent, and hold the rear hand at the chin "
            "with the elbows tucked. Tuck the chin behind the lead shoulder "
            "and keep the eyes level. Bounce lightly in place: the stance is "
            "alive, never frozen, and from it you should be able to step in "
            "any direction without a preparatory shift.",
        "key_points": [
            "Category: stance - the platform every JKD technique launches from.",
            "Strong side forward: the lead carries the straight lead and lead kicks.",
            "Feet about one shoulder-width apart, lead toe at the opponent.",
            "Rear foot angled about forty-five degrees, rear heel slightly lifted.",
            "Weight even, about fifty percent on each leg; knees softly bent.",
            "Lead hand at chin height and extended; rear hand at the chin; elbows tucked.",
            "Chin tucked behind the lead shoulder; eyes level; stance alive, never frozen.",
        ],
        "requirements": [
            "Flat, non-slippery training surface with room to move in all directions.",
            "Bare feet or flat training shoes; loose clothing that does not bind the hips.",
            "A mirror or partner to check foot angles, heel lift, and hand positions.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): the on-guard position and strong-side-forward structure.",
            "Bruce Lee's Fighting Method: Basic Training (Complete Edition, 2008): bai-jong mechanics.",
        ],
        "citations": [CIT_TAO, CIT_FIGHTING_METHOD],
        "sig_lens":
            "In the Signature reading, bai-jong is the oath of the ground: the "
            "body signs a covenant with the floor - even weight, live heels, "
            "hands already halfway to their targets - so that no technique "
            "ever begins from stillness. The strong side forward is the "
            "signature of intent: your best weapons live closest to the work.",
    },
    {
        "key": "footwork_advance",
        "name": "Footwork Fundamentals: Advance and Retreat",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description":
            "The advance and the retreat are the first footwork every jeet kune "
            "do student drills, because range is decided by the feet long "
            "before the hands arrive. Advancing, the lead foot moves first and "
            "the rear foot follows, covering roughly thirty centimeters per "
            "step; retreating, the rear foot moves first and the lead foot "
            "follows, preserving the bai-jong structure exactly. Four such "
            "steps close a gap of about one point two meters - a full fighting "
            "range - in about one second, which is why JKD treats footwork as "
            "the delivery system for every weapon. The feet never cross and "
            "never hop; the stance glides, low and level, so the hands are "
            "free to work at every instant of the movement.",
        "how_it_works":
            "Begin in bai-jong at a comfortable sparring distance from a "
            "partner. To advance: slide the lead foot forward about thirty "
            "centimeters, keeping it low to the floor, then bring the rear "
            "foot forward the same distance so the stance is restored exactly. "
            "To retreat: slide the rear foot back about thirty centimeters "
            "first, then bring the lead foot back to restore the stance. Keep "
            "the knees bent and the head level - no bobbing up and down - and "
            "never let the feet cross or come together. Drill ten advances "
            "and ten retreats in a slow rhythm, then have the partner advance "
            "while you retreat to hold the distance constant. When the "
            "movement is smooth at slow speed, raise the pace until four "
            "steps close the full range in about one second.",
        "key_points": [
            "Category: footwork - the delivery system for every weapon.",
            "Advance: lead foot moves first, rear foot follows.",
            "Retreat: rear foot moves first, lead foot follows.",
            "Each step covers roughly thirty centimeters; stance structure is preserved.",
            "Four steps close about one point two meters in about one second.",
            "Feet never cross, never hop; the stance glides low and level.",
            "Head stays level - no bobbing - so the hands can work at every instant.",
        ],
        "requirements": [
            "Open floor with at least three meters of clear linear space.",
            "A partner or a floor marker to practice holding and closing distance.",
            "Flat footwear with grip; no thick soles that hide the push from the floor.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): footwork as the base of all movement.",
            "Bruce Lee's Fighting Method: Basic Training (Complete Edition, 2008): the advance and retreat.",
        ],
        "citations": [CIT_TAO, CIT_FIGHTING_METHOD],
        "sig_lens":
            "In the Signature reading, the advance and retreat are the "
            "signature of range: the feet write the distance contract and the "
            "hands only sign it. Four gliding steps in one second is the oath "
            "kept - the stance never breaks its shape, so the fighter never "
            "pays for his own movement.",
    },
    {
        "key": "guard_parry",
        "name": "The Guard: Parry and Cover Positions",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description":
            "The guard is the shield wall of jeet kune do: the lead hand held "
            "at chin height and extended toward the opponent, the rear hand at "
            "the chin, the elbows tucked and the chin dropped behind the lead "
            "shoulder. The parry is the guard in motion - a short, sharp tap "
            "that deflects an incoming straight punch about ten centimeters "
            "off the centerline, just enough to miss, using the smallest "
            "movement that does the job. The cover is the guard under fire: "
            "chin tucked, elbows drawn in, forearms forming a wall while the "
            "practitioner rides out a flurry or prepares the counter. Both "
            "positions share one law: the hands return to guard after every "
            "action, because a hand that wanders is a door left open.",
        "how_it_works":
            "From bai-jong, extend the lead hand to chin height, roughly a "
            "forearm's length ahead of the face, palm angled slightly inward. "
            "Hold the rear fist at the chin, elbow tucked against the ribs, "
            "and drop the chin behind the lead shoulder. To parry a straight "
            "punch: as the punch arrives, tap it with the lead hand just "
            "enough to slide it about ten centimeters off the centerline - a "
            "wrist-flick, not a swing - and snap the hand back to guard. To "
            "cover: tuck the chin, draw both elbows tight, and let the "
            "forearms form a wall in front of the head and body while keeping "
            "the eyes on the opponent. Drill with a partner throwing slow "
            "straight punches: parry five, cover through a five-punch flurry, "
            "and check that both hands are home in guard after every action.",
        "key_points": [
            "Category: defense - the shield wall every attack launches behind.",
            "Lead hand at chin height, extended; rear hand at the chin; elbows tucked.",
            "Parry: a short tap deflecting the punch about ten centimeters off line.",
            "The parry is a wrist-flick, not a swing - smallest movement that works.",
            "Cover: chin tucked, forearms a wall, eyes on the opponent.",
            "Hands return to guard after every action - no wandering hands.",
            "Chin stays behind the lead shoulder throughout.",
        ],
        "requirements": [
            "A partner with focus mitts or gloves for slow, controlled straight punches.",
            "Headgear optional for early cover drills; mouthguard recommended.",
            "Clear floor space; no hard obstacles at head height.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): the guard and parrying principles.",
            "Inosanto, Jeet Kune Do: The Art and Philosophy of Bruce Lee (1980): guard structure.",
        ],
        "citations": [CIT_TAO, CIT_INOSANTO],
        "sig_lens":
            "In the Signature reading, the guard is the covenant of the hands: "
            "each hand swears to return home after every errand. The parry is "
            "the signature of economy - ten centimeters of deflection bought "
            "with a flick, never a swing - because the Signature fighter "
            "spends nothing he cannot afford.",
    },
    {
        "key": "straight_lead",
        "name": "The Straight Lead",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description":
            "The straight lead is the signature punch of jeet kune do and the "
            "fastest hand weapon in the system: a straight punch thrown from "
            "the lead hand, already halfway to the target by virtue of the "
            "strong-side-forward stance. A seventy-kilogram practitioner "
            "drives it at roughly nine meters per second across about "
            "three-quarters of a meter of reach, so it lands in under a tenth "
            "of a second - faster than the eye can fully track. The fist "
            "travels vertically, corkscrewing only at the very end, and the "
            "rear hand stays home at the chin while the shoulder snaps the "
            "punch out and back along the same line. Because the lead hand "
            "starts closest to the opponent and needs no chamber, the straight "
            "lead is both the primary probe and the primary interception "
            "tool of the art.",
        "how_it_works":
            "From bai-jong with the lead hand extended at chin height, snap "
            "the lead fist straight to the target along the shortest line - "
            "no pull-back, no shoulder dip, no telegraph. Rotate the fist to "
            "vertical as it extends and drive from the floor: push off the "
            "rear foot, let the hip turn a fraction, and let the shoulder "
            "whip the arm out. Keep the rear hand glued to the chin and the "
            "chin tucked behind the lead shoulder throughout. The instant the "
            "punch lands, snap it back along the exact same line to guard - "
            "the return is as fast as the delivery. Drill on a heavy bag: ten "
            "leads at half speed feeling the floor push, then ten at full "
            "speed, checking that the rear hand never leaves the chin.",
        "key_points": [
            "Category: hand strikes - the fastest weapon in the system.",
            "Thrown from the lead hand, already halfway to the target.",
            "About three-quarters of a meter of reach, roughly nine meters per second.",
            "Lands in under a tenth of a second - no chamber, no telegraph.",
            "Vertical fist, corkscrewing only at the very end.",
            "Rear hand stays at the chin; chin tucked behind the lead shoulder.",
            "Snaps back along the same line - the return is as fast as the delivery.",
        ],
        "requirements": [
            "Heavy bag or focus mitts and hand wraps plus gloves.",
            "Mirror to check for pull-back or shoulder dip before the punch.",
            "Clear space behind the bag for the follow-through line.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): the straight lead as the core weapon.",
            "Bruce Lee's Fighting Method: Skill in Techniques (Complete Edition, 2008): lead mechanics.",
        ],
        "citations": [CIT_TAO, CIT_FIGHTING_METHOD],
        "sig_lens":
            "In the Signature reading, the straight lead is the purest "
            "signature in the system: the shortest line between intent and "
            "impact, signed in under a tenth of a second. The Signature "
            "fighter treats the lead hand as a pen already touching the "
            "paper - no wind-up, no announcement, only the stroke.",
    },
    {
        "key": "cross",
        "name": "The Cross",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description":
            "The cross is the rear straight punch of jeet kune do, the "
            "system's heavy hand: thrown from the rear hand across the "
            "centerline, it travels farther than the lead - about eighty-five "
            "centimeters of reach - and arrives in roughly eleven hundredths "
            "of a second at about eight meters per second. What it loses in "
            "speed to the straight lead it repays in mass: the punch rides a "
            "forty-five-degree rotation of the hips and a drive from the rear "
            "leg, stacking the body's weight behind the fist. The cross is "
            "most often thrown behind the straight lead, the lead opening the "
            "line and the cross finishing through it, and the rear shoulder "
            "must cover the chin as the punch extends so the exchange never "
            "costs more than it earns.",
        "how_it_works":
            "From bai-jong, turn the rear hip forward about forty-five degrees "
            "while driving off the ball of the rear foot, and shoot the rear "
            "fist straight down the centerline to the target. Let the rear "
            "shoulder roll forward to cover the chin as the arm extends, and "
            "keep the lead hand up - it guards while the cross travels. Do "
            "not lean past the front knee; the power comes from the hip turn "
            "and the floor push, not from reaching. Snap the fist back to the "
            "chin along the same line the moment it lands. Drill the "
            "one-two: straight lead, then cross, feeling the hip turn hand the "
            "baton from the lead shoulder to the rear shoulder without a pause "
            "between them.",
        "key_points": [
            "Category: hand strikes - the heavy hand of the system.",
            "Rear straight punch across the centerline.",
            "About eighty-five centimeters of reach at roughly eight meters per second.",
            "Lands in about eleven hundredths of a second.",
            "Power from a forty-five-degree hip rotation and the rear-leg drive.",
            "Rear shoulder covers the chin as the punch extends.",
            "Lead hand stays up guarding; snap the cross straight back to the chin.",
        ],
        "requirements": [
            "Heavy bag or focus mitts; hand wraps and gloves.",
            "Mirror to check the hip turn and that the head does not lean past the front knee.",
            "Partner holding mitts for one-two timing work.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): the rear straight and hip rotation.",
            "Bruce Lee's Fighting Method: Skill in Techniques (Complete Edition, 2008).",
        ],
        "citations": [CIT_TAO, CIT_FIGHTING_METHOD],
        "sig_lens":
            "In the Signature reading, the cross is the signature of the "
            "whole body: the lead opens the line and the rear hand signs it "
            "with the weight of the hips behind it. The forty-five-degree "
            "turn is the covenant - the body rotates as one piece, and the "
            "chin stays covered because the Signature fighter never spends "
            "his safety to buy power.",
    },
    {
        "key": "lead_hook",
        "name": "The Lead Hook",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description":
            "The lead hook is the curved punch of the lead hand, the weapon "
            "that goes around the guard when the straight line is closed. The "
            "fist travels a horizontal arc of about ninety degrees on a "
            "radius of roughly sixty centimeters - an arc length of about "
            "ninety-four centimeters - with the elbow bent and the forearm "
            "level, arriving in roughly thirteen hundredths of a second. Power "
            "comes from the pivot of the lead foot and the snap of the hip, "
            "not from swinging the arm; the arm is the end of the whip, not "
            "the whip itself. Thrown tight, the lead hook is nearly as fast "
            "as the straight lead and lands where straight punches cannot "
            "reach - the side of the jaw around a high guard.",
        "how_it_works":
            "From bai-jong, pivot on the ball of the lead foot and snap the "
            "lead hip around, whipping the bent lead arm on a tight "
            "horizontal arc toward the side of the target. Keep the elbow "
            "bent at about ninety degrees and the forearm level - the fist, "
            "elbow, and shoulder stay on one plane. Do not wind the hand back "
            "or drop it first; the arc starts from the guard and returns to "
            "the guard. Keep the rear hand at the chin and the chin tucked. "
            "Drill on the heavy bag: ten slow hooks feeling the foot pivot "
            "start the motion, then ten at speed, checking in the mirror that "
            "the arc stays tight and the elbow never drops below the fist.",
        "key_points": [
            "Category: hand strikes - the curved punch around the guard.",
            "Horizontal arc of about ninety degrees on roughly a sixty-centimeter radius.",
            "Arc length about ninety-four centimeters; lands in about thirteen hundredths of a second.",
            "Elbow bent about ninety degrees; forearm level; fist, elbow, shoulder on one plane.",
            "Power from the lead-foot pivot and hip snap, not the arm swing.",
            "No wind-up, no dropped hand before the punch; starts and ends at the guard.",
            "Rear hand stays at the chin; chin tucked throughout.",
        ],
        "requirements": [
            "Heavy bag for arc work; hand wraps and gloves.",
            "Mirror to verify the tight arc and level forearm.",
            "Partner with mitts held at the side of the head for target practice.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): the hook and the pivot principle.",
            "Bruce Lee's Fighting Method: Skill in Techniques (Complete Edition, 2008).",
        ],
        "citations": [CIT_TAO, CIT_FIGHTING_METHOD],
        "sig_lens":
            "In the Signature reading, the lead hook is the signature of the "
            "turn: the foot pivots, the hip signs, and the fist is only the "
            "ink at the end of the stroke. The Signature fighter keeps the "
            "arc tight because a wide signature is a slow one - ninety "
            "degrees, no more, and home again.",
    },
    {
        "key": "uppercut",
        "name": "The Uppercut - Lead and Rear",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description":
            "The uppercut is the rising punch of jeet kune do, thrown on a "
            "vertical line from below the opponent's sight into the chin or "
            "the body. Dipping the knees slightly, the practitioner drives up "
            "from the legs and sends the fist rising about half a meter at "
            "roughly seven meters per second, landing in about seven "
            "hundredths of a second - the shortest-traveling power punch in "
            "the arsenal. The lead uppercut slips inside a high guard; the "
            "rear uppercut follows the cross's hip rotation with even more "
            "body behind it. Because it rises from below, the uppercut is the "
            "natural answer to an opponent who leans forward or drops his "
            "hands after punching.",
        "how_it_works":
            "From bai-jong, dip both knees a few centimeters to load the legs, "
            "keeping the back straight and the chin tucked. Drive up from the "
            "floor and whip the fist upward along the centerline, palm facing "
            "you, to the target - chin or solar plexus. For the lead "
            "uppercut, use the lead hand with a small hip turn; for the rear "
            "uppercut, rotate the rear hip through as with the cross. Do not "
            "drop the punching hand to the waist first - the rise starts from "
            "the guard. Snap the fist back down to guard along the same line. "
            "Drill on the bag: ten lead uppercuts feeling the leg drive, ten "
            "rear, checking that the non-punching hand never leaves the chin.",
        "key_points": [
            "Category: hand strikes - the rising punch from below the sight line.",
            "Fist rises about half a meter at roughly seven meters per second.",
            "Lands in about seven hundredths of a second - the shortest power-punch travel.",
            "Power from the leg drive, not from dropping the hand first.",
            "Lead uppercut slips inside a high guard; rear uppercut carries the hip rotation.",
            "Palm faces the practitioner; punch rises along the centerline.",
            "Snaps back to guard along the same line; the other hand never leaves the chin.",
        ],
        "requirements": [
            "Heavy bag or uppercut bag; hand wraps and gloves.",
            "Mirror to check the knee dip stays small and the hand does not drop first.",
            "Clear space below the target line for the rising path.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): the uppercut and leg-driven power.",
            "Bruce Lee's Fighting Method: Skill in Techniques (Complete Edition, 2008).",
        ],
        "citations": [CIT_TAO, CIT_FIGHTING_METHOD],
        "sig_lens":
            "In the Signature reading, the uppercut is the signature of the "
            "earth: the legs sign first and the fist only delivers the "
            "message. Rising half a meter in seven hundredths of a second, "
            "it is the Signature proof that the shortest line can also be "
            "the heaviest - when the floor does the writing.",
    },
    {
        "key": "lateral_footwork",
        "name": "Lateral Footwork: Side-Step and Circle Step",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description":
            "The side-step and the circle step are the lateral footwork of "
            "jeet kune do, the movements that change the angle instead of the "
            "range. A forty-five-degree angle step of about thirty centimeters "
            "displaces the practitioner roughly twenty-one centimeters "
            "sideways and twenty-one centimeters forward - off the opponent's "
            "centerline while staying in range to strike. The circle step "
            "walks the practitioner around the opponent's lead side, forcing "
            "the opponent to turn and resetting his offense to zero. Lateral "
            "footwork is how JKD answers pressure: rather than trading in a "
            "straight line, the fighter steps off the tracks and makes the "
            "opponent's straight weapons miss by geometry instead of by "
            "speed.",
        "how_it_works":
            "From bai-jong, to side-step right: push off the left foot and "
            "slide the right foot about thirty centimeters to the right, "
            "then bring the left foot along to restore the stance - the feet "
            "never cross. For the forty-five-degree angle step: step the lead "
            "foot forward and outward at forty-five degrees about thirty "
            "centimeters, then bring the rear foot up to restore bai-jong; "
            "you should now stand off the centerline with the opponent's lead "
            "shoulder open to you. For the circle step: take two or three "
            "small angle steps in the same rotational direction, walking "
            "around the opponent's lead side while keeping the guard up. "
            "Drill with a partner walking you down: angle-step off his line "
            "and touch his shoulder with the lead hand to prove the new "
            "angle.",
        "key_points": [
            "Category: footwork - changing the angle instead of the range.",
            "Side-step: push off the far foot, slide about thirty centimeters, restore stance.",
            "Forty-five-degree angle step displaces about twenty-one centimeters sideways and forward.",
            "Angle step takes the practitioner off the opponent's centerline while staying in range.",
            "Circle step walks around the opponent's lead side, forcing him to turn.",
            "Feet never cross; the guard stays up through every step.",
            "Straight weapons miss by geometry, not by speed.",
        ],
        "requirements": [
            "Open floor with room to move in a circle of about two meters radius.",
            "A partner to provide forward pressure for angle-step drills.",
            "Flat grippy footwear for the push-off.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): angling and lateral movement.",
            "Inosanto, Jeet Kune Do: The Art and Philosophy of Bruce Lee (1980): circle stepping.",
        ],
        "citations": [CIT_TAO, CIT_INOSANTO],
        "sig_lens":
            "In the Signature reading, lateral footwork is the signature of "
            "the angle: the Signature fighter does not outrun the punch, he "
            "rewrites the geometry it travels through. Twenty-one "
            "centimeters off the line is a full signature - the opponent's "
            "straight weapon arrives at an empty address.",
    },
    {
        "key": "paksao_intro",
        "name": "Basic Trapping Touch: Pak Sao Introduction",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description":
            "The basic trapping touch is the first lesson in the hand "
            "immobilization that makes jeet kune do's close range famous: a "
            "light pak sao - a slapping touch - that meets the partner's lead "
            "hand and pins it for a fraction of a second. The contact lasts "
            "only about five hundredths of a second, a tap rather than a "
            "grab, and its whole purpose is to teach the student that the "
            "opponent's guard is not a wall but a door with a handle. From "
            "this first touch grows the entire trapping curriculum - the lop "
            "sao pull, the jut sao jerk, and the hand immobilization attacks - "
            "because every trap begins with the same lesson: touch the guard, "
            "move it, and hit through the opening before it returns.",
        "how_it_works":
            "Face a partner in bai-jong at arm's length, both in guard. The "
            "partner holds his lead hand up as a passive target. Slap the "
            "back of his lead hand lightly with your lead hand - a crisp tap "
            "lasting about five hundredths of a second - pressing his hand "
            "a few centimeters off the centerline, and immediately extend "
            "your rear hand in a straight punch to his chest guard, stopping "
            "short of contact. Withdraw both hands to guard. The partner "
            "then does the same to you. Keep the tap light: the goal is "
            "sensitivity and timing, not force. Drill ten touches each, "
            "alternating, until the slap-and-punch flows as one beat instead "
            "of two separate motions.",
        "key_points": [
            "Category: trapping - the first lesson in hand immobilization.",
            "Pak sao: a light slapping touch, not a grab.",
            "Contact lasts about five hundredths of a second - a tap.",
            "Presses the guard a few centimeters off the centerline.",
            "The straight punch follows through the opening in the same beat.",
            "Teaches that the guard is a door with a handle, not a wall.",
            "Foundation of the lop sao, the jut sao, and hand immobilization attacks.",
        ],
        "requirements": [
            "A cooperative partner; both in guard at arm's length.",
            "Light gloves or bare hands with controlled contact.",
            "Chest guard or focus mitt as the punch target for safety.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): trapping hands and the pak sao.",
            "Bruce Lee's Fighting Method: Self-Defense Techniques (Complete Edition, 2008): trapping entries.",
        ],
        "citations": [CIT_TAO, CIT_FIGHTING_METHOD],
        "sig_lens":
            "In the Signature reading, the first trapping touch is the "
            "signature of the handshake that never lets go: five hundredths "
            "of a second of contact that teaches the hand to read the "
            "opponent's guard like a page. The Signature student learns that "
            "every wall in fighting has a handle - and he is learning to "
            "find it by touch.",
    },
    {
        "key": "slip_duck",
        "name": "Defensive Timing: The Slip and the Duck",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description":
            "The slip and the duck are the head-movement defenses of jeet kune "
            "do: the slip shifts the head about fifteen centimeters off the "
            "centerline to let a straight punch pass, and the duck drops the "
            "whole body under a hook. A trained slip moves the head those "
            "fifteen centimeters in about fifteen hundredths of a second - "
            "against a punch that needs about twenty-five hundredths of a "
            "second to arrive, that leaves a full tenth of a second of "
            "margin, which is why head movement beats blocking for economy. "
            "Both defenses keep the eyes on the opponent and the hands up, "
            "because the slip that blinds you or the duck that drops your "
            "hands trades one danger for another.",
        "how_it_works":
            "From bai-jong with the guard up, to slip a straight punch: rotate "
            "the torso slightly and shift the head about fifteen centimeters "
            "to the outside of the incoming punch, keeping the eyes fixed on "
            "the opponent and both hands in guard. Let the punch pass and "
            "return the head to center at once - the slip is a visit, not a "
            "move. To duck a hook: bend both knees and drop the body straight "
            "down under the arc of the hook, keeping the back straight and "
            "the hands up, then rise back to stance. Have a partner throw slow "
            "straight punches: slip five to the outside, five to the inside. "
            "Then slow hooks: duck five. Speed up only when the eyes stay open "
            "and the hands stay home on every repetition.",
        "key_points": [
            "Category: defense - head movement that beats blocking for economy.",
            "Slip: head shifts about fifteen centimeters off the centerline.",
            "A trained slip takes about fifteen hundredths of a second.",
            "Against a punch arriving in twenty-five hundredths of a second, the margin is a tenth of a second.",
            "Duck: knees bend, body drops straight under the hook's arc.",
            "Eyes stay on the opponent; hands stay in guard throughout.",
            "The slip is a visit, not a move - the head returns to center at once.",
        ],
        "requirements": [
            "A partner throwing slow, controlled straight punches and hooks with gloves.",
            "Headgear and mouthguard recommended as speed increases.",
            "Mirror for solo shadow work on the slip line.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): evasion and head movement.",
            "Bruce Lee's Fighting Method: Self-Defense Techniques (Complete Edition, 2008).",
        ],
        "citations": [CIT_TAO, CIT_FIGHTING_METHOD],
        "sig_lens":
            "In the Signature reading, the slip is the signature of the "
            "absent target: fifteen centimeters of absence, delivered in "
            "fifteen hundredths of a second, signed with the eyes still open. "
            "The Signature fighter is not where the punch was addressed - "
            "and he never pays the postage of a block to get there.",
    },
    {
        "key": "sda",
        "name": "Single Direct Attack - First Way of Attack",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description":
            "The single direct attack is the first of the five ways of attack "
            "in jeet kune do: one weapon, one beat, straight to the target "
            "with no preparation. Typically the straight lead fired behind a "
            "single advancing step, it covers a full fighting gap of about "
            "one point two meters - step plus punch - in roughly four tenths "
            "of a second, landing before the opponent's defense can organize. "
            "The single direct attack is the purest expression of the JKD "
            "creed of simplicity: when the line is open, take it at once, "
            "with the fastest tool, and be gone. Every other way of attack is "
            "a variation for the days when the line is not open.",
        "how_it_works":
            "From bai-jong at the edge of range, wait for - or create - the "
            "instant the opponent's guard opens or his weight shifts. In one "
            "beat, advance with the lead foot and fire the straight lead down "
            "the open line, the step and the punch landing together. Do not "
            "chamber, feint, or double-step: the attack is a single decision "
            "executed once. Snap the lead back to guard and either follow "
            "with the cross or angle-step out. Drill with a partner holding a "
            "focus mitt at the edge of your range: on his nod, close the one "
            "point two meter gap with step-plus-lead in about four tenths of "
            "a second. Ten repetitions, then switch roles.",
        "key_points": [
            "Category: the five ways of attack - the first way, one weapon one beat.",
            "Usually the straight lead behind a single advancing step.",
            "Covers about one point two meters - step plus punch - in about four tenths of a second.",
            "No chamber, no feint, no double-step: a single decision executed once.",
            "Step and punch land together as one beat.",
            "Fired when the line is open - the purest expression of simplicity.",
            "Snap back to guard; follow with the cross or angle-step out.",
        ],
        "requirements": [
            "Open floor with at least three meters of linear space.",
            "Partner with focus mitt at the edge of range for timing.",
            "Hand wraps and gloves; the mitt holder wears a chest guard.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): the five ways of attack - single direct attack.",
            "Little, The Warrior Within (1996): simplicity and directness in JKD offense.",
        ],
        "citations": [CIT_TAO, CIT_WARRIOR_WITHIN],
        "sig_lens":
            "In the Signature reading, the single direct attack is the "
            "signature in its simplest form: one stroke, no draft, no "
            "erasures. Four tenths of a second from decision to delivery is "
            "the Signature oath - when the line is open, the Signature "
            "fighter does not knock; he enters.",
    },
    {
        "key": "abc",
        "name": "Attack by Combination - Second Way of Attack",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description":
            "Attack by combination is the second way of attack: a volley of "
            "strikes in which each punch covers the recovery of the last. A "
            "classic three-strike combination - straight lead, cross, lead "
            "hook - delivers all three blows in about nine tenths of a "
            "second, roughly three tenths per strike, giving the opponent's "
            "guard no quiet beat in which to reset. The combination is not "
            "three separate punches but one continuous motion: the hip turn "
            "of the cross begins as the lead returns, and the pivot of the "
            "hook begins as the cross returns. JKD combinations are short by "
            "design - two to four strikes - because every strike past the "
            "fourth is thrown at an opponent who has already had time to "
            "answer.",
        "how_it_works":
            "From bai-jong, fire the straight lead and, as it returns, let "
            "the hip turn carry straight into the cross - no pause between "
            "them. As the cross returns, pivot the lead foot into the lead "
            "hook. The three strikes should flow in about nine tenths of a "
            "second, each covering the last one's withdrawal. Keep the "
            "non-punching hand at the chin at all times and the chin tucked; "
            "never admire the combination - snap the hook back and reset. "
            "Drill on the heavy bag: ten slow volleys feeling the hip hand "
            "the baton from punch to punch, then ten at speed, then the same "
            "on focus mitts with a partner calling the combination.",
        "key_points": [
            "Category: the five ways of attack - the second way, the volley.",
            "Each strike covers the recovery of the last - one continuous motion.",
            "Three strikes (lead, cross, hook) in about nine tenths of a second.",
            "Roughly three tenths of a second per strike; no quiet beat for the guard to reset.",
            "Hip turn hands the baton from punch to punch without pause.",
            "JKD combinations run two to four strikes - short by design.",
            "Non-punching hand at the chin; snap the last punch back and reset.",
        ],
        "requirements": [
            "Heavy bag and focus mitts; hand wraps and gloves.",
            "Partner to call combinations and hold mitts.",
            "Timer to check the nine-tenths-of-a-second volley pace.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): the five ways of attack - attack by combination.",
            "Bruce Lee's Fighting Method: Skill in Techniques (Complete Edition, 2008).",
        ],
        "citations": [CIT_TAO, CIT_FIGHTING_METHOD],
        "sig_lens":
            "In the Signature reading, the combination is a single signature "
            "written with three strokes: the hip never lifts the pen between "
            "them. Nine tenths of a second, three blows, no quiet beat - the "
            "Signature fighter signs so quickly the guard never finds a "
            "moment to read what hit it.",
    },
    {
        "key": "pia",
        "name": "Progressive Indirect Attack - Third Way of Attack",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description":
            "The progressive indirect attack is the third way of attack: a "
            "feint that draws the opponent's defense, followed by the real "
            "strike into the line the feint opened. The feint commits the "
            "opponent's guard for about twenty-five hundredths of a second - "
            "the time his reaction needs to travel - and the true attack "
            "lands inside the window from twenty-five to fifty hundredths of "
            "a second, while his defense is still answering the lie. The "
            "classic form is the low feint with the lead hand, then the "
            "straight lead to the head as his guard drops. The feint must be "
            "believable - thrown with real speed and intent - because a "
            "defense only moves for a threat it respects.",
        "how_it_works":
            "From bai-jong, throw a sharp feint with the lead hand toward the "
            "opponent's low line - fast and committed, as if it were real. "
            "As his guard drops to answer it, redirect: fire the straight "
            "lead to the head in the same motion, landing inside the "
            "twenty-five to fifty hundredths of a second window while his "
            "hands are still low. The feint and the strike are one continuous "
            "action, not two separate decisions. Drill with a partner: he "
            "holds a low mitt and a high mitt; you feint low, and when his "
            "low hand moves, you strike the high mitt. Ten repetitions, then "
            "reverse the lines - feint high, strike low.",
        "key_points": [
            "Category: the five ways of attack - the third way, the feint and the truth.",
            "Feint draws the defense; the real strike takes the opened line.",
            "The feint commits the guard for about twenty-five hundredths of a second.",
            "The true attack lands in the twenty-five to fifty hundredths of a second window.",
            "The feint must be believable - defenses only move for respected threats.",
            "Feint and strike are one continuous action, not two decisions.",
            "Classic form: low feint, straight lead to the head.",
        ],
        "requirements": [
            "Partner with two focus mitts (high and low targets).",
            "Hand wraps and gloves; controlled contact on the mitts.",
            "Mirror work first to make the feint indistinguishable from the real strike.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): the five ways of attack - progressive indirect attack.",
            "Inosanto, Jeet Kune Do: The Art and Philosophy of Bruce Lee (1980): feinting structure.",
        ],
        "citations": [CIT_TAO, CIT_INOSANTO],
        "sig_lens":
            "In the Signature reading, the progressive indirect attack is the "
            "signature with a decoy stroke: the feint signs a false name and "
            "the true strike signs the real one before the ink dries. The "
            "Signature fighter lies with his hands the way a master forges "
            "with a pen - so well the defense itself authenticates the lie.",
    },
    {
        "key": "hia",
        "name": "Hand Immobilization Attack - Fourth Way of Attack",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description":
            "The hand immobilization attack is the fourth way of attack: trap "
            "the opponent's guarding hand so it cannot defend, then strike "
            "through the opening the trap creates. The trap - a pak sao slap, "
            "a lop sao pull, a jut sao jerk - pins the guard for about two "
            "tenths of a second, and the strike must land inside that window, "
            "arriving as the trap is still holding. This is the close-range "
            "heart of jeet kune do, the reason the art's trapping hands are "
            "famous: at trapping range the guard is not evaded or overpowered, "
            "it is simply switched off for the fifth of a second the punch "
            "needs. The trap and the hit are one beat, never two.",
        "how_it_works":
            "Close to trapping range with a partner in guard. Slap his lead "
            "hand off the centerline with a pak sao - a crisp tap - and in "
            "the same beat drive your rear straight punch through the opening "
            "to his chest guard, stopping short of full contact. The trap "
            "holds about two tenths of a second; the punch must be landing "
            "as the trap lands, not after it. Withdraw to guard. Alternate "
            "the traps: pak sao slap, then lop sao pull (drag his hand down "
            "and across), then jut sao jerk (sharp downward yank). Drill ten "
            "of each, then let the partner vary his guard so you must choose "
            "the trap that fits what he gives you.",
        "key_points": [
            "Category: the five ways of attack - the fourth way, trap then hit.",
            "The trap pins the guard for about two tenths of a second.",
            "The strike lands inside that window - trap and hit are one beat.",
            "Pak sao slap, lop sao pull, or jut sao jerk - the trap fits the guard offered.",
            "At trapping range the guard is switched off, not evaded or overpowered.",
            "The close-range heart of jeet kune do.",
            "Withdraw to guard after every trap-and-hit.",
        ],
        "requirements": [
            "A cooperative partner in guard at trapping range.",
            "Chest guard for the punch target; light gloves.",
            "Control first: speed only after the one-beat timing is clean.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): the five ways of attack - hand immobilization attack.",
            "Bruce Lee's Fighting Method: Self-Defense Techniques (Complete Edition, 2008): trapping applications.",
        ],
        "citations": [CIT_TAO, CIT_FIGHTING_METHOD],
        "sig_lens":
            "In the Signature reading, the hand immobilization attack is the "
            "signature of the held door: the trap hand holds the guard's "
            "handle for two tenths of a second while the striking hand walks "
            "through. The Signature fighter does not knock the wall down - "
            "he simply holds it open for the fifth of a second the truth "
            "needs.",
    },
    {
        "key": "abd",
        "name": "Attack by Drawing - Fifth Way of Attack",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description":
            "Attack by drawing is the fifth way of attack: invite the "
            "opponent's attack by offering an apparent opening, then punish "
            "the commitment. The practitioner baits - dropping the lead hand "
            "a few centimeters, or retreating about twenty centimeters to "
            "suggest vulnerability - and when the opponent commits, the "
            "counter is already moving, landing about three tenths of a "
            "second after his attack begins, while he is extended and "
            "cannot defend. Drawing is the most psychological of the five "
            "ways: it requires reading the opponent's habits, offering the "
            "exact bait he cannot resist, and having the counter chambered "
            "before he moves. The trap is set with the body; it is sprung "
            "with the hands.",
        "how_it_works":
            "From bai-jong, offer the bait: lower the lead hand a few "
            "centimeters or take a short retreat of about twenty centimeters, "
            "suggesting the low line or the distance is open - but keep the "
            "rear hand cocked and the weight ready. The instant the partner "
            "commits to the opening, fire the prepared counter - usually the "
            "straight lead or the stop hit - down the line he has vacated, "
            "landing about three tenths of a second after his attack begins. "
            "Do not chase his attack; let it come to the counter. Drill with "
            "a partner: he attacks the offered opening on your cue at first, "
            "then freely, and you score only counters that land while he is "
            "still extended.",
        "key_points": [
            "Category: the five ways of attack - the fifth way, the invitation.",
            "Bait: drop the lead hand slightly or retreat about twenty centimeters.",
            "The counter is chambered before the opponent moves.",
            "Counter lands about three tenths of a second after his attack begins.",
            "Punish the commitment while he is extended and cannot defend.",
            "Requires reading habits and offering the bait he cannot resist.",
            "The trap is set with the body; it is sprung with the hands.",
        ],
        "requirements": [
            "A partner willing to attack committedly on the bait.",
            "Headgear, mouthguard, and gloves for counter-contact drills.",
            "Clear agreement on the bait and the allowed counters before free practice.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): the five ways of attack - attack by drawing.",
            "Little, The Warrior Within (1996): the psychology of the drawn attack.",
        ],
        "citations": [CIT_TAO, CIT_WARRIOR_WITHIN],
        "sig_lens":
            "In the Signature reading, attack by drawing is the signature of "
            "the patient hunter: the Signature fighter writes an invitation "
            "with his own apparent weakness and lets the opponent sign his "
            "name to it. Three tenths of a second after the commitment, the "
            "counter arrives - the bait was never the target; the target was "
            "the hunger.",
    },
    {
        "key": "paksao",
        "name": "Pak Sao - The Slapping Hand",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description":
            "Pak sao, the slapping hand, is the signature trap of jeet kune "
            "do: an open-hand slap that knocks the opponent's guarding hand "
            "about twenty centimeters off the centerline and pins it there "
            "for fifteen to twenty-five hundredths of a second while the "
            "other hand strikes. Unlike a grab, the slap needs no grip and "
            "cannot be stripped; unlike a parry, it does not merely deflect "
            "but captures, riding the opponent's hand down and holding it "
            "out of the fight. The pak sao is thrown with the whole body "
            "behind it - a short step and a hip turn drive the slap - so the "
            "twenty-centimeter displacement is authoritative, not tentative. "
            "It is the trap students drill ten thousand times, because at "
            "close range it is the key that opens every door.",
        "how_it_works":
            "At trapping range, step in slightly and slap the back of the "
            "partner's lead hand with your lead palm, driving it about twenty "
            "centimeters down and off the centerline - the power comes from "
            "the step and the hip turn, not the arm alone. Keep your slapping "
            "hand on his hand, pinning it for fifteen to twenty-five "
            "hundredths of a second, while your rear hand fires the straight "
            "punch through the opened line to his chest guard. Withdraw both "
            "hands to guard together. The slap is crisp and committed; a "
            "tentative tap gets brushed aside. Drill ten pak sao and hits, "
            "then have the partner resist lightly so you learn to drive "
            "through a live guard.",
        "key_points": [
            "Category: trapping - the signature trap of the art.",
            "Open-hand slap displacing the guard about twenty centimeters off line.",
            "Pins the hand for fifteen to twenty-five hundredths of a second.",
            "No grip needed - cannot be stripped like a grab.",
            "Captures and rides the hand down, not merely deflecting it.",
            "Power from the step and hip turn, not the arm alone.",
            "The other hand strikes through the opening in the same beat.",
        ],
        "requirements": [
            "Partner at trapping range in guard; chest guard for the punch.",
            "Light gloves or bare hands with controlled slap contact.",
            "Ten thousand repetitions begin with ten clean ones - patience required.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): the pak sao and trapping hands.",
            "Inosanto, Jeet Kune Do: The Art and Philosophy of Bruce Lee (1980): pak sao mechanics.",
        ],
        "citations": [CIT_TAO, CIT_INOSANTO],
        "sig_lens":
            "In the Signature reading, pak sao is the signature of the "
            "authoritative hand: twenty centimeters of displacement, signed "
            "with the hip, held for the fifth of a second the other hand "
            "needs. The Signature fighter does not ask the guard to move - "
            "he moves it, pins it, and writes through the space it leaves.",
    },
    {
        "key": "lopsao",
        "name": "Lop Sao - The Pulling Hand",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description":
            "Lop sao, the pulling hand, is the trap that drags the "
            "opponent's guard down and across his own body: the practitioner "
            "grabs or hooks the opponent's lead hand and pulls it about "
            "twenty-five centimeters down and inward, dragging the "
            "opponent's structure with it and opening the high line. The pull "
            "unbalances as well as clears - the opponent's weight follows "
            "his hand, and for the three tenths of a second he spends "
            "recovering, his head is unguarded and his balance is borrowed. "
            "Lop sao pairs naturally with the straight lead or the cross to "
            "the head, the pull and the punch leaving together like two "
            "hands of the same motion.",
        "how_it_works":
            "At trapping range, hook or grab the partner's lead hand with "
            "your lead hand and pull it sharply about twenty-five centimeters "
            "down and across his centerline, turning your hip into the pull "
            "so his structure follows his hand. As the pull lands, fire your "
            "rear straight punch to the head line - controlled, stopping at "
            "his headgear - in the same beat. The pull must be committed: a "
            "half-hearted tug only warns him. Release and withdraw to guard "
            "together. Drill ten pulls and punches, then have the partner "
            "offer different guard positions so you learn to find the pulling "
            "angle on a live arm.",
        "key_points": [
            "Category: trapping - the trap that drags the guard across the body.",
            "Hooks the lead hand and pulls about twenty-five centimeters down and inward.",
            "Unbalances as well as clears - the opponent's weight follows his hand.",
            "Opens the high line for about three tenths of a second.",
            "Pairs with the straight lead or cross to the head.",
            "Pull and punch leave together - two hands of one motion.",
            "Power from the hip turn into the pull, not the arm alone.",
        ],
        "requirements": [
            "Partner at trapping range; headgear and mouthguard for the head-line punch.",
            "Chest guard; gloves with controlled contact.",
            "Agreement on pull intensity before drilling - the pull must be committed but safe.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): the lop sao and pulling traps.",
            "Inosanto, Jeet Kune Do: The Art and Philosophy of Bruce Lee (1980).",
        ],
        "citations": [CIT_TAO, CIT_INOSANTO],
        "sig_lens":
            "In the Signature reading, lop sao is the signature of the "
            "borrowed balance: the Signature fighter takes the opponent's "
            "hand on a twenty-five-centimeter journey and the opponent's "
            "weight insists on coming along. For three tenths of a second "
            "the head stands unguarded - and the Signature punch signs it.",
    },
    {
        "key": "jutsao",
        "name": "Jut Sao - The Jerking Hand",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description":
            "Jut sao, the jerking hand, is the sharp downward yank that "
            "clears a high guard: the practitioner chops or jerks the "
            "opponent's lead hand downward about fifteen centimeters in a "
            "violent, short motion, snapping the high line open for the "
            "straight lead or the hook that follows. Where pak sao slaps "
            "aside and lop sao drags across, jut sao drops straight down - "
            "the fastest of the three traps, a sudden yank that the "
            "opponent's arm cannot follow in time. The jerk is all suddenness: "
            "relaxed arm, explosive drop, the body weight falling into it for "
            "a single violent instant. It is the trap for the opponent who "
            "holds his hands high and dares you to come through.",
        "how_it_works":
            "At trapping range against a partner holding a high guard, chop "
            "downward onto his lead forearm with your lead hand - or hook and "
            "yank - driving his hand down about fifteen centimeters in one "
            "explosive motion, letting your body weight drop into the jerk. "
            "The instant his hand falls, fire your straight lead or lead hook "
            "to the head line, controlled, in the same beat. Withdraw to "
            "guard. The jerk must be sudden, not strong: speed of the drop is "
            "what beats his recovery. Drill ten jerks and strikes, then have "
            "the partner hold the high guard firmly so you learn to put your "
            "weight into the drop without leaning.",
        "key_points": [
            "Category: trapping - the sharp downward yank that clears a high guard.",
            "Drives the opponent's lead hand down about fifteen centimeters.",
            "The fastest of the three traps - suddenness beats strength.",
            "Opens the high line for the straight lead or hook.",
            "Relaxed arm, explosive drop, body weight falling into the jerk.",
            "Trap and strike are one beat, never two.",
            "The answer to the opponent who holds his hands high.",
        ],
        "requirements": [
            "Partner holding a committed high guard at trapping range.",
            "Headgear and mouthguard; gloves with controlled contact.",
            "Wrist wraps recommended - the jerk loads the wrist sharply.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): the jut sao and jerking traps.",
            "Bruce Lee's Fighting Method: Self-Defense Techniques (Complete Edition, 2008).",
        ],
        "citations": [CIT_TAO, CIT_FIGHTING_METHOD],
        "sig_lens":
            "In the Signature reading, jut sao is the signature of suddenness: "
            "fifteen centimeters straight down, signed in a single violent "
            "instant with the body's weight as the ink. The Signature fighter "
            "does not argue with a high guard - he drops it like a curtain "
            "and strikes before it can rise.",
    },
    {
        "key": "lead_side_kick",
        "name": "The Lead Side Kick",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description":
            "The lead side kick is the signature kick of jeet kune do: thrown "
            "from the lead leg, it chambers the knee high and then extends "
            "the leg straight into the target with the heel or the edge of "
            "the foot, reaching about one point two meters. The foot travels "
            "at roughly ten meters per second, so the kick lands in about "
            "twelve hundredths of a second - and because the lead leg is "
            "already closest to the opponent, there is almost no telegraph. "
            "It is both a stop kick, spearing into an advancing opponent, and "
            "a power kick to the body or knee, and its chamber makes it "
            "nearly unreadable until the extension fires.",
        "how_it_works":
            "From bai-jong, lift the lead knee high across the body, chambering "
            "tight with the foot cocked - heel exposed, toes pulled back. "
            "Pivot on the supporting foot and drive the hips forward, "
            "extending the lead leg straight into the target: the knee, the "
            "body, or the head line on a bag. Strike with the heel or the "
            "knife-edge of the foot, never the toes. Rechamber the knee at "
            "once and set the foot back down into bai-jong - the kick returns "
            "the way it came. Drill on the heavy bag: ten slow kicks feeling "
            "the chamber hide the intent, then ten at speed, checking that "
            "the supporting foot pivots fully and the hips drive through.",
        "key_points": [
            "Category: kicking - the signature kick of the system.",
            "Thrown from the lead leg - already closest, almost no telegraph.",
            "Chamber the knee high, then extend straight with heel or foot edge.",
            "Reach about one point two meters at roughly ten meters per second.",
            "Lands in about twelve hundredths of a second.",
            "Serves as stop kick against advances and power kick to body or knee.",
            "Rechamber at once and return to bai-jong along the same path.",
        ],
        "requirements": [
            "Heavy bag rated for kicking; shin and foot protection for partner drills.",
            "Open floor with room for the full one point two meter extension.",
            "Hip flexor warm-up - the high chamber demands it.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): the side kick and lead-leg kicking.",
            "Bruce Lee's Fighting Method: Skill in Techniques (Complete Edition, 2008): kicking mechanics.",
        ],
        "citations": [CIT_TAO, CIT_FIGHTING_METHOD],
        "sig_lens":
            "In the Signature reading, the lead side kick is the signature of "
            "the hidden spear: chambered tight and unreadable, then extended "
            "one point two meters in twelve hundredths of a second. The "
            "Signature fighter keeps his longest weapon closest and fires it "
            "like a signature - no draft, no warning, only the stroke.",
    },
    {
        "key": "hook_kick",
        "name": "The Hook Kick",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description":
            "The hook kick is the arcing kick of jeet kune do, the leg's "
            "answer to the lead hook: the foot travels a circular path of "
            "about one hundred twenty degrees on a radius of roughly ninety "
            "centimeters - a path length near one point nine meters - and "
            "whips around the opponent's guard into the side of the head or "
            "body. At a foot speed near nine meters per second the kick "
            "lands in about twenty-one hundredths of a second, slower than "
            "the side kick but arriving from an angle straight kicks cannot "
            "take. The hip turns over fully and the supporting foot pivots, "
            "so the kick's power comes from rotation rather than a swing of "
            "the leg. It is the kick for the opponent whose front is "
            "fortified and whose side is open.",
        "how_it_works":
            "From bai-jong, pivot the supporting foot and turn the hip over, "
            "swinging the lead leg on a tight circular path - knee slightly "
            "bent at first, extending through the target - with the foot "
            "traveling about one hundred twenty degrees of arc. Strike with "
            "the heel or the sole of the foot to the side of the target, "
            "keeping the hands up in guard throughout; the kick must not cost "
            "you your defense. Rechamber along the arc and set the foot back "
            "into bai-jong. Drill on the heavy bag: ten slow arcs feeling the "
            "hip turn over completely, then ten at speed, checking in the "
            "mirror that the path stays tight and the hands never drop.",
        "key_points": [
            "Category: kicking - the arcing kick around the guard.",
            "Foot travels about one hundred twenty degrees on roughly a ninety-centimeter radius.",
            "Path length near one point nine meters; lands in about twenty-one hundredths of a second.",
            "Whips around straight defenses into the side of the head or body.",
            "Hip turns over fully; supporting foot pivots; power from rotation.",
            "Hands stay in guard throughout - the kick must not cost the defense.",
            "Rechamber along the arc and return to bai-jong.",
        ],
        "requirements": [
            "Heavy bag; shin guards for partner drills.",
            "Open floor with clearance for the full circular path.",
            "Hip and groin warm-up - the arc demands rotational mobility.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): the hook kick and circular kicking.",
            "Bruce Lee's Fighting Method: Skill in Techniques (Complete Edition, 2008).",
        ],
        "citations": [CIT_TAO, CIT_FIGHTING_METHOD],
        "sig_lens":
            "In the Signature reading, the hook kick is the signature of the "
            "long way around: one point nine meters of arc signed in "
            "twenty-one hundredths of a second, arriving where straight "
            "lines cannot go. The Signature fighter turns the hip over "
            "completely - a half-turned signature is a forgery, and his "
            "kicks are never forged.",
    },
    {
        "key": "low_lead_kick",
        "name": "The Low Lead Kick",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description":
            "The low lead kick is the quiet destroyer of jeet kune do: a "
            "short, sharp kick from the lead leg to the opponent's shin or "
            "thigh, about half a meter off the floor, thrown with almost no "
            "chamber and therefore almost no warning. The foot travels only "
            "about sixty centimeters at roughly eight meters per second, "
            "landing in under eight hundredths of a second - faster than the "
            "opponent can lift his leg to check it. Repeated low kicks deaden "
            "the lead leg, slow the footwork, and force the opponent to think "
            "about his base instead of his attack. It is the least spectacular "
            "kick in the system and one of the most effective, because it "
            "attacks the foundation the whole fight stands on.",
        "how_it_works":
            "From bai-jong, snap the lead shin into the partner's lead shin "
            "or thigh - about half a meter high - with a short chopping "
            "motion, pivoting slightly on the supporting foot. There is "
            "almost no chamber: the kick fires from where the foot already "
            "stands, which is why it cannot be read in time. Strike with the "
            "shin, not the foot, and set the foot straight back down into "
            "bai-jong. Keep the hands up - the low kick must not trade the "
            "guard for the leg. Drill with a partner wearing shin guards: ten "
            "light kicks each, then increase to medium contact, checking that "
            "every kick returns to stance faster than it left.",
        "key_points": [
            "Category: kicking - the quiet destroyer aimed at the foundation.",
            "Lead leg to the shin or thigh, about half a meter off the floor.",
            "Almost no chamber - fires from where the foot stands.",
            "Travels about sixty centimeters at roughly eight meters per second.",
            "Lands in under eight hundredths of a second - too fast to check.",
            "Repeated kicks deaden the leg and slow the opponent's footwork.",
            "Strike with the shin; hands stay up; foot returns to stance at once.",
        ],
        "requirements": [
            "Partner with shin guards and thigh pads; agreed contact level.",
            "Open floor; the drill needs lateral room for stance recovery.",
            "Shin conditioning built gradually - never full power on day one.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): low-line kicking and the lead leg.",
            "Inosanto, Jeet Kune Do: The Art and Philosophy of Bruce Lee (1980): low kicks.",
        ],
        "citations": [CIT_TAO, CIT_INOSANTO],
        "sig_lens":
            "In the Signature reading, the low lead kick is the signature of "
            "the foundation attacked: half a meter high, eight hundredths of "
            "a second, signed on the shin the whole fight stands on. The "
            "Signature fighter writes small and often - and the opponent's "
            "base slowly forgets how to stand.",
    },
    {
        "key": "stop_hit",
        "name": "Stop Hit - The Jeet Interception",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description":
            "The stop hit is the technique that gives jeet kune do its name - "
            "jeet, to intercept: as the opponent begins his attack, you "
            "strike into it, landing your blow while his is still traveling. "
            "The arithmetic is the art: his punch needs about twenty-five "
            "hundredths of a second to arrive, your straight-lead stop hit "
            "needs only about fifteen hundredths, so striking the instant you "
            "read his preparation lands your punch a full tenth of a second "
            "before his - his attack dies unborn. The stop hit is usually the "
            "straight lead, sometimes the lead side kick, thrown not at his "
            "guard but into the line of his attack. It demands the reading of "
            "intention - the shoulder twitch, the weight shift - because the "
            "interception must start as his does, not after.",
        "how_it_works":
            "Face a partner in bai-jong at sparring range. Have him begin a "
            "slow straight punch on your cue. The instant you see his "
            "shoulder move - the preparation, not the punch - fire your "
            "straight lead directly into his attacking line, aiming to land "
            "as his punch is half extended. Your fifteen-hundredths-of-a-second "
            "lead against his twenty-five-hundredths arrival is the tenth of "
            "a second that decides it. Start with his punch at half speed so "
            "you can practice reading the shoulder twitch; only increase his "
            "speed as your interception starts landing first. Drill ten "
            "interceptions, then let him vary the timing so you must read, "
            "not anticipate.",
        "key_points": [
            "Category: interception - the technique the art is named for.",
            "Jeet: to intercept - strike into his attack as it begins.",
            "His punch needs about twenty-five hundredths of a second; your stop hit about fifteen.",
            "The tenth-of-a-second margin is the whole technique.",
            "Usually the straight lead, sometimes the lead side kick.",
            "Thrown into the line of his attack, not at his guard.",
            "Read the preparation - shoulder twitch, weight shift - and start as he starts.",
        ],
        "requirements": [
            "A partner throwing committed but controlled straight punches.",
            "Headgear, mouthguard, gloves; chest guard for body interceptions.",
            "Patience: the reading of intention is trained slowly, then sped up.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): jeet - the stop hit and interception.",
            "Little, The Warrior Within (1996): interception as the core of JKD.",
        ],
        "citations": [CIT_TAO, CIT_WARRIOR_WITHIN],
        "sig_lens":
            "In the Signature reading, the stop hit is the signature the art "
            "is named for: the Signature fighter reads the first letter of "
            "the opponent's intention and finishes the sentence before him. "
            "A tenth of a second is the margin, and the margin is everything "
            "- his attack dies unborn, and the Signature lead signs its "
            "place.",
    },
    {
        "key": "stop_kick",
        "name": "Stop Kick - Intercepting the Kicker",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description":
            "The stop kick applies interception to the opponent's legs: as he "
            "chambers to kick, you spear your lead side kick into his hip, "
            "thigh, or supporting leg, killing the kick before it extends. "
            "The kicker needs about thirty-five hundredths of a second to "
            "chamber and extend; your stop kick, already chambered in "
            "bai-jong's lead leg, needs only about twenty hundredths - a "
            "fifteen-hundredths-of-a-second margin that lands your heel while "
            "his foot is still rising. The stop kick punishes the very idea "
            "of kicking: after two or three interceptions, most opponents "
            "stop offering their legs at all, which is itself a victory. It "
            "is thrown from the lead leg precisely because the lead is "
            "already halfway there.",
        "how_it_works":
            "Face a partner at kicking range. Have him begin a slow round kick "
            "with his lead leg on your cue. The instant his knee starts to "
            "chamber - the preparation - fire your lead side kick into his "
            "hip or the thigh of his kicking leg, extending straight through "
            "the line his kick wanted. Land and rechamber at once, back to "
            "bai-jong. Your twenty-hundredths-of-a-second kick against his "
            "thirty-five-hundredths chamber-and-extend is the margin. Start "
            "with his kick at half speed, practicing the read of the chamber; "
            "increase speed only as your interceptions start landing first. "
            "Drill ten stop kicks, then let him choose when to kick.",
        "key_points": [
            "Category: interception - killing the kick before it extends.",
            "Spear the lead side kick into his hip, thigh, or supporting leg.",
            "His chamber-and-extend needs about thirty-five hundredths of a second.",
            "Your stop kick needs about twenty hundredths - a fifteen-hundredths margin.",
            "Thrown from the lead leg, already halfway there.",
            "Read the chamber - the knee rising - not the extended kick.",
            "Two or three interceptions teach most opponents to stop kicking.",
        ],
        "requirements": [
            "Partner throwing controlled kicks; thigh pads and chest guard.",
            "Shin guards for both; mouthguard recommended.",
            "Start at half speed - the read of the chamber is trained slowly.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): the stop kick and kicking interceptions.",
            "Bruce Lee's Fighting Method: Self-Defense Techniques (Complete Edition, 2008).",
        ],
        "citations": [CIT_TAO, CIT_FIGHTING_METHOD],
        "sig_lens":
            "In the Signature reading, the stop kick is the signature of the "
            "unborn kick: the Signature fighter's heel signs the kicker's "
            "hip while the kick is still a thought in the knee. Fifteen "
            "hundredths of a second is the margin - and after a few such "
            "signatures, the opponent stops writing kicks altogether.",
    },
    {
        "key": "broken_rhythm",
        "name": "Broken Rhythm - Timing and Cadence",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description":
            "Broken rhythm is the deliberate disruption of timing: instead of "
            "attacking on a steady beat the opponent can measure - half a "
            "second, half a second, half a second - the practitioner varies "
            "the cadence, perhaps half a second, then three tenths, then seven "
            "tenths, so the opponent's defensive timing is always answering "
            "the last beat instead of the next one. Human reaction needs a "
            "pattern to predict; broken rhythm denies the pattern, and a "
            "defense timed for a beat that never comes is a defense spent. "
            "The broken cadence applies to footwork, feints, and strikes "
            "alike - the whole fighter becomes unreadable in time, not just "
            "in technique. It is the temporal equivalent of the feint: a lie "
            "told in rhythm.",
        "how_it_works":
            "On the heavy bag, establish a steady striking rhythm: strike "
            "every half second for ten beats, letting the body learn the "
            "metronome. Then break it deliberately: strike, pause three "
            "tenths, strike, pause seven tenths, strike - varying the gaps "
            "while keeping the strikes themselves crisp. Have a partner hold "
            "mitts and try to catch your rhythm: when he starts moving the "
            "mitt early to meet your expected beat, you will feel the "
            "broken rhythm working - his defense is spending itself on "
            "phantoms. Drill broken footwork the same way: advance on an "
            "irregular cadence so a partner mirroring you is always a step "
            "behind your actual timing.",
        "key_points": [
            "Category: timing - the deliberate disruption of cadence.",
            "Steady beat (half second, half second) lets the defense predict.",
            "Broken cadence (half, three-tenths, seven-tenths) denies the pattern.",
            "A defense timed for a beat that never comes is a defense spent.",
            "Applies to footwork, feints, and strikes - the whole fighter in time.",
            "The temporal equivalent of the feint: a lie told in rhythm.",
            "Reaction needs a pattern to predict; broken rhythm gives it none.",
        ],
        "requirements": [
            "Heavy bag and a timer or metronome for cadence work.",
            "Partner with mitts to test whether your rhythm can be read.",
            "Patience: irregularity must stay deliberate, not become sloppiness.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): broken rhythm and timing.",
            "Little, The Warrior Within (1996): rhythm in JKD.",
        ],
        "citations": [CIT_TAO, CIT_WARRIOR_WITHIN],
        "sig_lens":
            "In the Signature reading, broken rhythm is the signature of the "
            "unreadable clock: the Signature fighter signs his strikes on a "
            "metronome only he can hear, and changes the tempo mid-signature. "
            "The opponent's defense keeps excellent time - to music that is "
            "no longer playing.",
    },
    {
        "key": "economy_motion",
        "name": "Economy of Motion - Non-Telegraphic Movement",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description":
            "Economy of motion is the discipline of the non-telegraphic "
            "strike: no pull-back of the fist, no dip of the shoulder, no "
            "flare of the elbow before the punch - nothing that warns the "
            "opponent before the weapon moves. A telegraphed straight lead "
            "wastes about fifteen hundredths of a second and fifteen "
            "centimeters of elbow flare on preparation; the direct lead "
            "travels its three-quarter-meter line with none of that tax, "
            "arriving roughly a third sooner than the looping punch that "
            "covers one point one meters to reach the same target. The "
            "practitioner trains economy by watching for his own tells in the "
            "mirror and deleting them one by one: the shoulder that rises, "
            "the fist that cocks, the breath that catches. What remains is "
            "the punch that simply appears.",
        "how_it_works":
            "Stand before a mirror in bai-jong and throw slow straight leads, "
            "watching for every preparatory motion: does the fist pull back "
            "first? does the shoulder dip? does the elbow flare those fifteen "
            "centimeters? Freeze at each tell and rehearse the punch without "
            "it, until the fist leaves the guard with no warning at all. "
            "Have a partner watch your shadow drills and call out every "
            "telegraph he sees - the outside eye catches what yours forgives. "
            "Then drill the comparison on the bag: ten deliberately "
            "telegraphed leads (pull back, then punch) against ten direct "
            "leads, feeling the roughly one-third time saving of the honest "
            "line. Economy is deletion: remove everything that is not the "
            "strike.",
        "key_points": [
            "Category: advanced principle - the strike that gives no warning.",
            "No pull-back, no shoulder dip, no elbow flare before the punch.",
            "A telegraph wastes about fifteen hundredths of a second and fifteen centimeters.",
            "The direct lead covers three-quarters of a meter; the looping punch one point one.",
            "The honest line arrives roughly a third sooner.",
            "Train by mirror: find each tell and delete it one by one.",
            "Economy is deletion - remove everything that is not the strike.",
        ],
        "requirements": [
            "A full-length mirror for tell-hunting shadow work.",
            "An honest partner to call out telegraphs the mirror misses.",
            "Heavy bag for the telegraphed-versus-direct comparison drill.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): economy of motion and non-telegraphic striking.",
            "Little, The Warrior Within (1996): simplicity and directness.",
        ],
        "citations": [CIT_TAO, CIT_WARRIOR_WITHIN],
        "sig_lens":
            "In the Signature reading, economy of motion is the signature "
            "with nothing wasted: no flourish before the stroke, no ink "
            "spent on the margin. The Signature fighter deletes his tells "
            "one by one until what remains is the punch that simply appears "
            "- a third sooner, fifteen centimeters truer, signed before the "
            "eye can object.",
    },
    {
        "key": "time_hit",
        "name": "The Intercepting Fist - Time Hit and Counter Timing",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description":
            "The time hit is interception refined to its purest timing: not "
            "meeting the opponent's attack with a block, but landing your own "
            "strike in the exact instant his begins - the counter that is "
            "also an interception. The window is brutally narrow: his attack "
            "commits in about twenty-five hundredths of a second, your "
            "counter needs about twenty hundredths to land, so you must begin "
            "within five hundredths of a second of reading his cue - the "
            "shoulder twitch, the breath, the shift of weight. There is no "
            "time to decide; the time hit is trained until the cue and the "
            "counter are one reflex. It is the difference between the fighter "
            "who reacts to attacks and the fighter for whom the opponent's "
            "attack is the trigger of his own.",
        "how_it_works":
            "With a partner in bai-jong, agree on his attack: a slow straight "
            "punch on his own timing, unknown to you. Your task is to fire "
            "your straight lead the instant you detect his preparation - not "
            "his punch, his preparation - so the two strikes cross and yours "
            "lands first. At half speed the five-hundredths-of-a-second "
            "window is generous enough to learn; as his speed rises, you "
            "will feel the window shrink to its true size. Drill ten time "
            "hits, resting between each - this is nervous-system work, and "
            "fatigue destroys timing. When you can land the counter-first "
            "exchange eight times in ten at three-quarter speed, the reflex "
            "is installed.",
        "key_points": [
            "Category: interception - the counter that is also an interception.",
            "Land your strike in the exact instant his begins - no block, only the hit.",
            "His commitment: about twenty-five hundredths of a second.",
            "Your counter: about twenty hundredths - begin within five hundredths of the cue.",
            "The cue is the preparation: shoulder twitch, breath, weight shift.",
            "No time to decide - cue and counter must be one reflex.",
            "Train at half speed, then three-quarter; rest between reps - fatigue kills timing.",
        ],
        "requirements": [
            "A partner with a consistent, readable straight punch.",
            "Headgear, mouthguard, gloves; controlled contact.",
            "Fresh nervous system: drill this early in the session, not tired.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): the time hit and counter-attack timing.",
            "Inosanto, Jeet Kune Do: The Art and Philosophy of Bruce Lee (1980).",
        ],
        "citations": [CIT_TAO, CIT_INOSANTO],
        "sig_lens":
            "In the Signature reading, the time hit is the signature of the "
            "single reflex: the opponent's preparation is the pen lifting, "
            "and the Signature counter is already writing. Five hundredths "
            "of a second is the whole margin - trained until cue and counter "
            "are one stroke, and the opponent's attack becomes the trigger "
            "of his own defeat.",
    },
    {
        "key": "flow_drills",
        "name": "Trapping Flow Drills - Chi Sao and Hubud Basics",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description":
            "Trapping flow drills are the sensitivity training of jeet kune "
            "do's close range: chi sao, the sticking hands, keeps the "
            "forearms in constant rolling contact so each partner feels the "
            "other's intention through touch, and hubud, the tie-and-untie "
            "drill, cycles both partners through pak sao, lop sao, and "
            "strikes in a continuous loop. At a training pace of about sixty "
            "cycles per minute, a three-minute round delivers one hundred "
            "eighty repetitions of trap-and-hit - sensitivity and timing "
            "installed by volume. The drills teach the hands to answer "
            "pressure without the eyes: when the partner pushes, you yield "
            "and trap; when he yields, you enter and hit. Flow first, "
            "speed later, resistance last - the sensitivity must be built "
            "before it is tested.",
        "how_it_works":
            "Face a partner in bai-jong at trapping range. For hubud basics: "
            "partner A feeds a slow straight punch; partner B pak saos it "
            "aside and returns a slow punch; A lop saos the return and punches; "
            "B jut saos and punches - the loop continues, each trap answering "
            "the last punch. Keep the pace at about sixty cycles per minute, "
            "light contact, both partners flowing rather than forcing. For "
            "chi sao basics: press forearms together and roll them in small "
            "circles, each partner maintaining light forward pressure; when "
            "you feel a gap in his structure, enter with a slow trap and "
            "punch. Drill three-minute rounds - one hundred eighty cycles - "
            "resting one minute between, for three rounds.",
        "key_points": [
            "Category: sensitivity - the hands learn to answer pressure by touch.",
            "Chi sao: sticking hands, forearms in constant rolling contact.",
            "Hubud: the tie-and-untie loop cycling pak, lop, jut, and strikes.",
            "Training pace about sixty cycles per minute.",
            "A three-minute round delivers one hundred eighty trap-and-hit repetitions.",
            "When he pushes, yield and trap; when he yields, enter and hit.",
            "Flow first, speed later, resistance last.",
        ],
        "requirements": [
            "A patient partner at trapping range; light gloves.",
            "A timer for the three-minute rounds and one-minute rests.",
            "Mats or open floor - close-range footwork still needs room.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): chi sao and sensitivity training.",
            "Inosanto, Jeet Kune Do: The Art and Philosophy of Bruce Lee (1980): hubud and flow drills.",
        ],
        "citations": [CIT_TAO, CIT_INOSANTO],
        "sig_lens":
            "In the Signature reading, the flow drills are the signature of "
            "the listening hand: one hundred eighty repetitions per round "
            "until the forearms can read intention the way fingers read "
            "braille. The Signature fighter's hands answer pressure without "
            "consulting the eyes - the touch itself becomes the signature.",
    },
    {
        "key": "stop_thrust",
        "name": "The Stop-Thrust - Offensive Interception",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description":
            "The stop-thrust is interception turned offensive: instead of "
            "waiting for the opponent's attack and meeting it, the "
            "practitioner advances into the opponent's preparation, spearing "
            "the straight lead or the lead side kick into him as he begins to "
            "move. The advance covers about sixty centimeters in three tenths "
            "of a second - two meters per second of forward pressure - while "
            "the strike extends, so the opponent's preparation is met by an "
            "attack that started before his did. The stop-thrust collapses "
            "the distinction between offense and defense: it is an attack "
            "thrown at the moment of his vulnerability and a defense that "
            "needs no block, because the best answer to his beginning is your "
            "already arriving.",
        "how_it_works":
            "Face a partner at sparring range. Have him begin to advance on "
            "his own timing. The instant his weight shifts forward - his "
            "preparation - drive forward yourself: advance about sixty "
            "centimeters in three tenths of a second while spearing the "
            "straight lead into his chest guard, or the lead side kick into "
            "his lead thigh. Your forward motion plus his forward motion "
            "close the distance together; your strike, started first, lands "
            "first. Do not wait for his attack to develop - the stop-thrust "
            "meets the preparation, not the punch. Drill ten stop-thrusts at "
            "half speed, then let him vary his advance timing so you must "
            "read the weight shift, not anticipate it.",
        "key_points": [
            "Category: interception - the offensive stop, meeting preparation with attack.",
            "Advance about sixty centimeters in three tenths of a second - two meters per second.",
            "Spear the straight lead or lead side kick into his beginning.",
            "Your strike starts before his - offense and defense collapse into one.",
            "Meets the preparation (weight shift), not the developed punch.",
            "Both fighters' forward motion closes the distance together.",
            "Read the weight shift; never anticipate the timing.",
        ],
        "requirements": [
            "Partner advancing with committed but controlled intent.",
            "Chest guard, thigh pads, headgear, mouthguard, gloves.",
            "Open floor with room for the sixty-centimeter drive.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): the stop-thrust and offensive interception.",
            "Bruce Lee's Fighting Method: Advanced Techniques (Complete Edition, 2008).",
        ],
        "citations": [CIT_TAO, CIT_FIGHTING_METHOD],
        "sig_lens":
            "In the Signature reading, the stop-thrust is the signature of "
            "the already-arriving: two meters per second of forward intent "
            "that meets the opponent's preparation before it becomes an "
            "attack. The Signature fighter does not defend against beginnings "
            "- he out-begins them, and his strike signs the space where the "
            "opponent's plan used to be.",
    },
    {
        "key": "lowline_stop",
        "name": "Kicking Interception - The Low Line Stop",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description":
            "The low line stop is the shin-on-shin answer to the low kick: as "
            "the opponent's low kick travels, the practitioner raises his own "
            "lead shin to meet it, the two shins colliding at roughly a "
            "forty-five-degree angle about forty centimeters from the hip. "
            "The interception works because the raised shin is braced by the "
            "body's structure while the kicking leg is extended and "
            "unsupported - the kicker absorbs his own force plus the stop. "
            "Timing is everything: the shin must rise as the kick is "
            "chambering, not after it extends, which means reading the hip "
            "rather than watching the foot. One good low line stop often ends "
            "the opponent's kicking game for the round.",
        "how_it_works":
            "Face a partner at kicking range wearing shin guards. Have him "
            "throw slow low kicks to your lead leg. As his hip turns to "
            "chamber - read the hip, not the foot - lift your lead knee and "
            "angle your shin outward about forty-five degrees, bracing it "
            "with your structure, so his shin meets yours about forty "
            "centimeters from your hip. Keep your hands up; the stop is a "
            "leg action, not an excuse to drop the guard. Absorb the contact "
            "with the outer shin and set the foot back down into bai-jong at "
            "once. Drill ten stops at half speed, then increase his kick "
            "speed gradually - the read of the hip is the whole technique.",
        "key_points": [
            "Category: interception - the shin-on-shin answer to the low kick.",
            "Shins meet at roughly a forty-five-degree angle, about forty centimeters from the hip.",
            "The raised shin is braced by structure; the kicking leg is extended and unsupported.",
            "The kicker absorbs his own force plus the stop.",
            "Rise the shin as he chambers - read the hip, not the foot.",
            "Hands stay up; the stop is a leg action.",
            "One good stop often ends his kicking game for the round.",
        ],
        "requirements": [
            "Shin guards for both partners - mandatory, no exceptions.",
            "Partner throwing committed low kicks at controlled speed.",
            "Mats or open floor; the stop needs stable footing.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): low-line defense and shin interceptions.",
            "Inosanto, Jeet Kune Do: The Art and Philosophy of Bruce Lee (1980).",
        ],
        "citations": [CIT_TAO, CIT_INOSANTO],
        "sig_lens":
            "In the Signature reading, the low line stop is the signature of "
            "the braced answer: forty-five degrees of structure meeting an "
            "unsupported kick forty centimeters from the hip. The Signature "
            "fighter reads the hip, not the foot - the foot is the rumor, "
            "the hip is the signature, and he answers the signature.",
    },
    {
        "key": "attack_prep",
        "name": "The Counter-Offensive - Attack on Preparation",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description":
            "Attack on preparation is the counter-offensive principle: strike "
            "not after the opponent's attack, but during its preparation - "
            "the shoulder rising, the weight shifting, the breath catching - "
            "which broadcasts his intention about fifteen hundredths of a "
            "second before his weapon moves. The practitioner's attack, "
            "launched inside that fifteen-hundredths-of-a-second broadcast "
            "window, lands as the opponent's attack is being born: he cannot "
            "defend because his body is committed to attacking, and he cannot "
            "attack because your strike is already arriving. This is the "
            "highest form of the stop hit - not intercepting the punch but "
            "intercepting the decision to punch. It requires studying the "
            "opponent until his tells are as readable as large print.",
        "how_it_works":
            "Spar lightly with a partner and study him: every fighter "
            "broadcasts - a shoulder that lifts before the jab, a breath "
            "that catches before the kick, a weight shift before the advance. "
            "Identify one reliable tell in your partner. Then, the instant "
            "you see the tell - inside its fifteen-hundredths-of-a-second "
            "broadcast window - launch your straight lead or stop kick into "
            "him, landing as his attack begins. You are not reacting to his "
            "weapon; you are answering his intention. Drill in light sparring "
            "only, with full protective gear, and trade roles so each partner "
            "learns both to read tells and to hide his own.",
        "key_points": [
            "Category: interception - striking the preparation, not the attack.",
            "Preparation broadcasts intention about fifteen hundredths of a second early.",
            "Launch inside that window; land as his attack is being born.",
            "He cannot defend - his body is committed to attacking.",
            "The highest form of the stop hit: intercepting the decision.",
            "Requires studying the opponent until his tells read like large print.",
            "Drill in light sparring; trade roles to learn to hide your own tells.",
        ],
        "requirements": [
            "Light sparring partner with readable, consistent tells.",
            "Full protective gear: headgear, mouthguard, gloves, shin guards.",
            "A coach or observer to confirm the tell you think you see is real.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): attack on preparation.",
            "Little, The Warrior Within (1996): reading intention.",
        ],
        "citations": [CIT_TAO, CIT_WARRIOR_WITHIN],
        "sig_lens":
            "In the Signature reading, attack on preparation is the signature "
            "of the mind reader: fifteen hundredths of a second of broadcast "
            "is all the Signature fighter needs to answer the intention "
            "instead of the weapon. He studies his opponent until the tells "
            "read like large print - and then he signs his answer before the "
            "question is finished.",
    },
    {
        "key": "cadence_traps",
        "name": "Cadence Traps - Broken Rhythm in Sparring",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description":
            "Cadence traps apply broken rhythm directly to sparring: the "
            "practitioner establishes a readable striking cadence - three "
            "beats at half-second intervals - and the moment the opponent's "
            "defense starts timing itself to the fourth beat, the beat never "
            "comes; instead the real attack lands about twenty-five "
            "hundredths of a second after the expected beat, inside the "
            "defense's recovery. The trap exploits the opponent's own timing "
            "instinct: his body, having learned the pattern in three "
            "repetitions, commits to the prediction, and the broken fourth "
            "beat punishes the commitment. Three beats to teach, one broken "
            "beat to collect - that is the whole economy of the cadence trap.",
        "how_it_works":
            "In light sparring, establish the pattern: throw three light "
            "straight leads on a steady half-second cadence, letting the "
            "partner's guard start rising to meet the rhythm. On the fourth "
            "beat, hesitate - let his defense commit to the expected timing - "
            "then fire the real straight lead about twenty-five hundredths "
            "of a second after the beat he expected, landing inside his "
            "recovery. Vary the trap: sometimes break on the third beat, "
            "sometimes extend to five steady beats before breaking. Drill "
            "with a partner in light sparring with full gear, alternating "
            "roles, and count aloud at first so both partners can feel the "
            "cadence being set and broken.",
        "key_points": [
            "Category: timing - the sparring application of broken rhythm.",
            "Establish three beats at half-second intervals to teach the pattern.",
            "Break the fourth beat: hesitate, let his defense commit to the phantom.",
            "Real attack lands about twenty-five hundredths of a second after the expected beat.",
            "Exploits his timing instinct - his body commits to the prediction.",
            "Three beats to teach, one broken beat to collect.",
            "Vary the break point: third beat, fourth, sometimes fifth.",
        ],
        "requirements": [
            "Light sparring partner with full protective gear.",
            "Agreed contact level - the trap is about timing, not power.",
            "A count-aloud phase first so both partners feel the cadence.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): broken rhythm applied in sparring.",
            "Little, The Warrior Within (1996): timing and cadence.",
        ],
        "citations": [CIT_TAO, CIT_WARRIOR_WITHIN],
        "sig_lens":
            "In the Signature reading, the cadence trap is the signature of "
            "the broken promise: three honest beats to earn the opponent's "
            "trust, then a fourth beat that never arrives - only the strike, "
            "twenty-five hundredths of a second late and exactly on time. "
            "The Signature fighter teaches the rhythm, then collects on the "
            "lesson.",
    },
    {
        "key": "centerline",
        "name": "Centerline Theory in Combat",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description":
            "Centerline theory is the geometric heart of jeet kune do: the "
            "imaginary line running down the middle of each fighter's body "
            "carries the most direct paths to the vital targets, so the "
            "fighter who controls the centerline controls the fight. "
            "Controlling it means occupying it with your weapons while denying "
            "it to his - your straight lead owns the line; his straight "
            "punches must travel around your presence. In practice the "
            "centerline is a cone about thirty degrees wide: inside the cone "
            "your short weapons dominate, and angling even slightly outside "
            "his cone while staying inside your own is the positional victory "
            "the whole art pursues. Every trap, every interception, every "
            "angle step is ultimately a negotiation over this one line.",
        "how_it_works":
            "Face a partner in bai-jong. Extend your lead hand down the "
            "centerline between you - feel how it both threatens him and "
            "blocks his straight path to you. Have him throw slow straight "
            "punches: note how each must detour around your occupying hand, "
            "losing the shortest line. Now angle-step forty-five degrees to "
            "his outside: your centerline cone - about thirty degrees wide - "
            "still covers him, while his cone now points at empty space. "
            "Drill the negotiation: he tries to reclaim the line with "
            "footwork while you maintain it with lead-hand presence and small "
            "angle steps, each of you scoring when your straight lead can "
            "travel the true centerline unobstructed.",
        "key_points": [
            "Category: advanced principle - the geometric heart of the art.",
            "The centerline carries the most direct paths to vital targets.",
            "Control it: occupy it with your weapons, deny it to his.",
            "Your straight lead owns the line; his straights must detour.",
            "The centerline is a cone about thirty degrees wide.",
            "Angle outside his cone while staying inside your own - the positional victory.",
            "Every trap, interception, and angle step negotiates this one line.",
        ],
        "requirements": [
            "A partner for the centerline negotiation drill.",
            "Open floor for the angle-step repositioning.",
            "Light gloves; the drill is positional, not full contact.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): the centerline and economy of line.",
            "Inosanto, Jeet Kune Do: The Art and Philosophy of Bruce Lee (1980): centerline control.",
        ],
        "citations": [CIT_TAO, CIT_INOSANTO],
        "sig_lens":
            "In the Signature reading, the centerline is the signature line "
            "itself: thirty degrees of owned geometry down the middle of the "
            "fight, and every technique in the system is a negotiation over "
            "who gets to write on it. The Signature fighter occupies the "
            "line with his lead hand the way a signer occupies the bottom of "
            "the page - and dares the opponent to write around him.",
    },
    {
        "key": "simul_parry_hit",
        "name": "Simultaneous Parry and Hit",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description":
            "Simultaneous parry and hit is the two-handed expression of jeet "
            "kune do's economy: as the opponent's punch arrives, one hand "
            "parries it aside while the other hand strikes - both actions in "
            "a single beat. The parry takes about ten hundredths of a second "
            "and the counter-punch about twenty; overlapped, the whole "
            "defense-offense completes in about twenty hundredths of a second "
            "- the time of the punch alone. There is no block-then-hit "
            "sequence for the opponent to exploit, because the parry and the "
            "hit are not sequential: the defending hand clears the line the "
            "striking hand is already traveling. It is the standing proof of "
            "the JKD law that the best defense is a counter-offense sharing "
            "its beat.",
        "how_it_works":
            "Face a partner throwing slow straight punches. As his punch "
            "arrives, parry it about ten centimeters off the centerline with "
            "your lead hand - a ten-hundredths-of-a-second tap - while your "
            "rear hand fires the cross down the cleared line in the same "
            "instant. The two hands move together: the parry does not finish "
            "before the punch starts. Land the cross on his chest guard, then "
            "withdraw both hands to guard. Start at half speed until the "
            "overlap feels like one motion rather than two; increase speed "
            "only when the parry and the hit truly share their beat. Drill "
            "ten simultaneous parry-and-hits, then let him vary which hand "
            "he punches with so you must parry with either hand.",
        "key_points": [
            "Category: advanced principle - defense and offense sharing one beat.",
            "One hand parries while the other strikes - both in a single beat.",
            "Parry about ten hundredths of a second; counter-punch about twenty.",
            "Overlapped, the whole action completes in about twenty hundredths of a second.",
            "No block-then-hit sequence - the parry clears the line the punch already travels.",
            "The standing proof that the best defense is a counter-offense.",
            "Drill at half speed until the overlap feels like one motion.",
        ],
        "requirements": [
            "Partner throwing committed straight punches at controlled speed.",
            "Chest guard for the cross target; headgear, mouthguard, gloves.",
            "Patience: the overlap is a coordination skill built slowly.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): simultaneous parry and counter.",
            "Bruce Lee's Fighting Method: Advanced Techniques (Complete Edition, 2008).",
        ],
        "citations": [CIT_TAO, CIT_FIGHTING_METHOD],
        "sig_lens":
            "In the Signature reading, the simultaneous parry and hit is the "
            "signature in stereo: two hands writing at once, the parry "
            "clearing the line the punch is already traveling. Twenty "
            "hundredths of a second, one beat, no sequence - the Signature "
            "fighter defends and signs in the same stroke.",
    },
    {
        "key": "sparring_synthesis",
        "name": "Jeet Kune Do Sparring Synthesis - The Interception Game",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description":
            "The interception game is the sparring synthesis of jeet kune do: "
            "a full three-minute round in which the practitioner's sole "
            "scoring objective is the interception - stop hits, stop kicks, "
            "and attacks on preparation - rather than volume of strikes. A "
            "typical round produces about twenty exchanges, of which roughly "
            "six present genuine interception opportunities; converting three "
            "of the six is excellent work. The game forces everything the "
            "ladder taught into one alive test: the bai-jong stance must hold "
            "under pressure, the footwork must maintain the range, the five "
            "ways must appear as answers rather than plans, and the reading "
            "of intention must function at full speed. It is the final exam "
            "of the system - and, passed repeatedly, the beginning of a "
            "personal jeet kune do.",
        "how_it_works":
            "Gear up fully - headgear, mouthguard, gloves, shin guards, chest "
            "guard - and spar a three-minute round with a partner under one "
            "special rule: only interceptions score - stop hits, stop kicks, "
            "attacks on preparation, and simultaneous parry-and-hits. Volume "
            "striking earns nothing. Count the exchanges afterward: about "
            "twenty per round is typical, with roughly six true interception "
            "opportunities, and converting three is excellent. Between rounds, "
            "review: which interceptions did you see but not take? which "
            "tells did you miss? Spar three rounds with one-minute rests, "
            "trading the initiative each round so both partners practice "
            "reading and being read. The game never ends - it only gets "
            "faster.",
        "key_points": [
            "Category: synthesis - the full system alive in one sparring game.",
            "Three-minute round; only interceptions score.",
            "About twenty exchanges per round; roughly six interception opportunities.",
            "Converting three of six is excellent work.",
            "Forces stance, footwork, the five ways, and reading into one alive test.",
            "Between rounds review the interceptions seen but not taken.",
            "Three rounds, one-minute rests; trade initiative so both partners read and are read.",
        ],
        "requirements": [
            "Full protective gear for both partners: headgear, mouthguard, gloves, shin guards, chest guard.",
            "A timer for three-minute rounds and one-minute rests.",
            "A coach or observer to count exchanges and score interceptions.",
        ],
        "standards": [
            "Tao of Jeet Kune Do (1975): sparring and the alive test of interception.",
            "Little, The Warrior Within (1996): the personal expression of JKD.",
        ],
        "citations": [CIT_TAO, CIT_WARRIOR_WITHIN],
        "sig_lens":
            "In the Signature reading, the interception game is the final "
            "signature and the first: three minutes, twenty exchanges, six "
            "chances to read intention and answer it first. The Signature "
            "fighter treats every round as an exam he sets for himself - and "
            "every passed exam as the beginning of a personal jeet kune do, "
            "signed in his own hand.",
    },
]
