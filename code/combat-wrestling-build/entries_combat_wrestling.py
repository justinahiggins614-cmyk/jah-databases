#!/usr/bin/env python3
"""Entries for the Wrestling Combat Database (combat batch 2, wrestling).

Verified 2026-10-17 (combat batch 2): RAW SWEEP over the full manifest
(2,410 databases) PLUS every shard index in jah-databases-data-1 PLUS the
main-repo data dir: zero 'combat-wrestling' slugs/names; zero wrestling
title collisions across all 68 titles (34 public + 34 Signature Edition,
whole-system dedupe_gate check, 0 refusals). ID prefixes JAH-CBWR- (public)
and JAH-CBWRS- (signature) verified free in the manifest id_prefix values
and in every shard index file.

Two NEW databases, 34 ladder-ordered records each:

  combat-wrestling             - The Wrestling Combat Database
                                 (public-harvest: real, fact-checked
                                 freestyle and Greco-Roman wrestling
                                 technique - stance and motion, clinch ties,
                                 takedown defense and escapes, shots
                                 (single and double leg), clinch attacks,
                                 throws, par terre turns, reversals, and
                                 combination systems - every record a full
                                 technique with step-by-step body mechanics,
                                 taught along the teaching ladder; standard
                                 references United World Wrestling
                                 International Wrestling Rules; NCAA
                                 Wrestling Rules; Gable Coaching Wrestling
                                 Successfully 1999)
  combat-wrestling-signature   - The Wrestling Combat Signature Database
                                 (his original Signature Combat Method: the
                                 mat the proving ground, stance the oath,
                                 every technique a Signature discipline of
                                 leverage and will, the chain the creed;
                                 src signature, titles suffixed
                                 " (Signature Edition)", never presented as
                                 authentic public record)

34 records each, teaching ladder (ladder_rank 1-10, ladder_tier
foundations/compounded/advanced), shard index written in ladder order:
simple -> compounded -> complex.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_wrestling.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
Civilian martial-arts instruction only.
"""

SIG_TAIL = ("Signature original - his original Signature Combat Method: the "
            "mat the proving ground, stance the oath, every technique a "
            "Signature discipline of leverage and will, the chain the "
            "creed. Clearly labeled Signature-made, never presented as "
            "authentic public record.")

CIT_UWW = ("United World Wrestling. International Wrestling Rules. "
           "Corsier-sur-Vevey: UWW; 2024 (freestyle and Greco-Roman scoring, "
           "par terre, passivity, falls).")
CIT_NCAA = ("National Collegiate Athletic Association. NCAA Wrestling Rules "
            "Book. Indianapolis: NCAA; 2024-25 season.")
CIT_GABLE = ("Gable D. Coaching Wrestling Successfully. Champaign: Human "
             "Kinetics; 1999.")

ENTRIES = [
    # ------------------------------------------------------- FOUNDATIONS
    {
        "key": "stance",
        "name": "The Wrestling Stance",
        "group": "Stance and Motion",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The wrestling stance is the foundation position from which every "
            "attack, defense, and motion in freestyle and Greco-Roman "
            "wrestling begins. The wrestler stands with feet a little wider "
            "than shoulder width, one foot forward of the other, knees bent "
            "deeply, back straight with the chest up, head up with eyes "
            "forward, elbows tucked tight to the body, and hands open in "
            "front like claws ready to tie up or strike. The staggered feet "
            "split the base front to back so the wrestler cannot be pushed "
            "straight over, the bent knees lower the center of gravity so "
            "shots can launch and sprawls can fire, and the upright head "
            "keeps the spine safe and the eyes on the opponent. A good stance "
            "is low enough that a broom handle laid across the thighs would "
            "rest level, relaxed enough to move in any direction on the first "
            "step, and balanced enough to absorb a shove without stepping. "
            "Every other technique in this database is built on this "
            "position; a wrestler out of stance is a wrestler already "
            "beaten."
        ),
        "how_it_works": (
            "Step 1: set the feet. Place the feet a little wider than "
            "shoulder width, with the lead foot (usually the same side as the "
            "dominant hand) about one foot-length ahead of the trail foot. "
            "Step 2: bend the knees. Sink until the thighs are near parallel "
            "to the mat and the knees sit over the toes, never caving "
            "inward. Step 3: set the back. Keep the back straight and the "
            "chest up, hinging at the hips rather than rounding the spine. "
            "Step 4: set the head. Lift the head so the eyes look forward at "
            "the opponent's chest; the head stays up through every shot and "
            "every sprawl. Step 5: set the arms. Tuck the elbows tight "
            "against the ribs and hold the hands open in front of the knees, "
            "fingers together, ready to collar-tie, underhook, or post. "
            "Step 6: check the base. Have a partner shove you lightly from "
            "each side; if you must step to stay up, widen or re-stagger the "
            "feet. Step 7: hold and breathe. Stay in stance for timed "
            "rounds, keeping motion in the feet so the position is alive, "
            "not frozen."
        ),
        "key_points": [
            "Feet staggered front to back and wider than the shoulders; the split base resists straight pushes.",
            "Knees bent deeply with the chest up and the head up; low hips, safe spine, eyes on the opponent.",
            "Elbows tucked and hands open in front; the arms are ready to tie, post, or shoot.",
            "The stance is a living position - feet always moving, weight centered, ready in every direction.",
            "Every attack and every defense starts here; stance discipline decides matches before contact.",
        ],
        "requirements": [
            "A flat mat surface and enough room to step in every direction without obstruction.",
            "Wrestling shoes for grip; the stance cannot be held on a slick surface.",
            "A partner or coach to check the base with light shoves from each side.",
            "Timed stance-hold rounds to build the leg endurance the position demands.",
            "A mirror or video check so the athlete can see knee tracking, back angle, and head position.",
        ],
        "standards": [
            "Stance and motion fundamentals follow standard coaching practice (Gable 1999).",
            "Head-up, spine-safe posture is required before any live takedown drilling.",
            "Mat safety: clear space and proper footwear per UWW competition-area practice.",
        ],
        "citations": [CIT_GABLE, CIT_UWW],
        "sig_lens": (
            "The Signature read: the stance is the oath taken before battle "
            "is joined. Feet planted as the foundation stones, knees bent as "
            "the bow drawn, head high as the banner - the Signature wrestler "
            "does not stand, he declares. Every later discipline in this "
            "archive is a verse built on this first line."
        ),
    },
    {
        "key": "motion_footwork",
        "name": "Circling and Motion Footwork",
        "group": "Stance and Motion",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Circling and motion footwork is how a wrestler stays in stance "
            "while moving - the constant small steps that keep the base "
            "under the body, control the angle to the opponent, and set up "
            "every attack. From the stance the wrestler moves with short "
            "choppy steps, never crossing the feet, keeping the same "
            "staggered lead and the same knee bend through the whole motion, "
            "circling the opponent to probe for an opening and to deny the "
            "opponent a straight line of attack. Good motion is quiet, "
            "level, and endless: the head stays at the same height, the feet "
            "never leave the mat for long, and the wrestler can stop, shoot, "
            "or sprawl from any step. Poor motion - crossing the feet, "
            "standing up tall, bouncing, or moving in straight lines - hands "
            "the opponent a takedown. Footwork is drilled as shadow motion, "
            "as circle drills with a partner, and as penetration-step "
            "repetitions until the feet move without thought."
        ),
        "how_it_works": (
            "Step 1: start in stance. Set the full stance - staggered feet, "
            "bent knees, chest and head up, elbows in. Step 2: take short "
            "steps. Move with small quick steps, the lead foot stepping "
            "first in the direction of travel and the trail foot following; "
            "never let the feet cross. Step 3: stay level. Keep the head at "
            "one height through the motion - no bouncing up between steps, "
            "which telegraphs and unloads the legs. Step 4: circle with "
            "purpose. Move laterally around the partner, cutting the angle "
            "so the lead foot steps toward the opponent's lead foot, "
            "forcing them to turn. Step 5: change direction sharply. Plant "
            "the outside foot and redirect without standing up; the "
            "direction change is what opens shot windows. Step 6: penetrate "
            "from motion. From a circling step, drop the level and fire the "
            "penetration step without pausing - the shot grows out of the "
            "feet, not out of a standstill. Step 7: drill to exhaustion. "
            "Run timed circle rounds, switching direction on the whistle, "
            "until the feet stay correct when the lungs are empty."
        ),
        "key_points": [
            "Short choppy steps with the feet never crossing; the stance survives the motion.",
            "The head stays level - bouncing unloads the legs and telegraphs attacks.",
            "Circle to cut angles toward the opponent's lead foot, denying straight attacks.",
            "Direction changes plant the outside foot and redirect without standing up.",
            "Shots launch from live feet; still feet make still wrestlers, and still wrestlers get taken down.",
        ],
        "requirements": [
            "A full mat with room to circle a partner at wrestling distance.",
            "Wrestling shoes with grip; footwork drills fail on slick floors.",
            "A partner to circle against, or a marked center circle for shadow motion.",
            "A whistle or timer for direction-change intervals and timed motion rounds.",
            "Video review to catch crossing feet, bouncing, and stance decay under fatigue.",
        ],
        "standards": [
            "Footwork fundamentals follow standard coaching practice (Gable 1999).",
            "Live-motion drilling requires the same mat safety as stance work.",
            "Direction-change drills keep the head up and the spine safe at all times.",
        ],
        "citations": [CIT_GABLE, CIT_UWW],
        "sig_lens": (
            "The Signature read: motion is the tide and the wrestler the "
            "moon that moves it. The Signature wrestler never stands still "
            "to be measured - he circles, he cuts, he vanishes from one "
            "angle and appears at another. Stillness is surrender; motion is "
            "the first weapon."
        ),
    },
    {
        "key": "penetration_step",
        "name": "The Penetration Step",
        "group": "Stance and Motion",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The penetration step is the explosive lunge that carries the "
            "wrestler from stance into the opponent's legs - the engine of "
            "the double leg, the single leg, the low single, and the ankle "
            "pick. From circling motion the wrestler drops the level, steps "
            "the lead foot deep between the opponent's feet, drives the "
            "trail knee to the mat beside the lead foot, and keeps the head "
            "up and tight to the opponent's body as the arms wrap the target. "
            "The power comes from the legs and hips driving forward, not "
            "from reaching with the arms; the arms only finish what the step "
            "started. A correct penetration step lands the lead foot flat "
            "between the opponent's feet, the trail knee down, the chest "
            "against the opponent's thigh or hip, and the back straight. "
            "Done slowly it is a drill; done at full speed it is the "
            "fastest motion in wrestling, closing more than a meter of "
            "distance before the opponent's sprawl can fire."
        ),
        "how_it_works": (
            "Step 1: move first. Circle or step in stance until the distance "
            "is right - roughly one long step from the opponent's lead foot. "
            "Step 2: drop the level. Bend deeper at the knees, lowering the "
            "hips without leaning the head forward. Step 3: step deep. Drive "
            "the lead foot forward and plant it flat between the opponent's "
            "feet, toes pointed slightly out. Step 4: bring the trail knee "
            "down. Let the trail knee drop to the mat right beside the lead "
            "foot as the hips drive forward - the knee landing is the sound "
            "of a committed shot. Step 5: keep the head up. Tuck the head "
            "tight against the opponent's ribs or hip, eyes forward; the "
            "head never drops to the mat. Step 6: wrap with the arms. As the "
            "knee lands, the arms encircle the target - both legs for the "
            "double, one leg for the single - elbows tight, hands locked. "
            "Step 7: drive through. Push off the trail toes and drive the "
            "hips forward and up, finishing the takedown with leg drive, "
            "not arm pulling."
        ),
        "key_points": [
            "The step is a leg-and-hip lunge, not an arm reach; the arms finish what the step started.",
            "Lead foot lands flat between the opponent's feet; trail knee drops to the mat beside it.",
            "Head stays up and tight to the body; a dropped head is a sprawled-on head.",
            "Level drops before the step fires - change level, then penetrate, never reach first.",
            "Drive through the finish with the legs; pulling with the arms stalls the shot.",
        ],
        "requirements": [
            "A mat with space for full-speed penetration repetitions.",
            "A partner or a heavy bag / shot dummy to penetrate against.",
            "Knee protection or a mat clean enough for repeated trail-knee drops.",
            "A coach's eye on head position - the most common and most punished error.",
            "Timed repetition sets to build the step until it fires without thought.",
        ],
        "standards": [
            "Penetration mechanics follow standard coaching practice (Gable 1999).",
            "Head-up position is mandatory in all live shot drilling.",
            "Trail-knee drops require a clean mat to avoid mat burns and knee injury.",
        ],
        "citations": [CIT_GABLE, CIT_UWW],
        "sig_lens": (
            "The Signature read: the penetration step is the Signature "
            "arrow loosed. The bow is the stance, the draw is the level "
            "change, and the release is total commitment - the knee strikes "
            "the mat like a seal on the attack. Half-drawn bows do not "
            "strike; the Signature step is never half."
        ),
    },
    {
        "key": "level_change",
        "name": "The Level Change",
        "group": "Stance and Motion",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The level change is the sudden drop of the hips that precedes "
            "every leg attack and much of wrestling's deception - the "
            "wrestler sinks several inches in a heartbeat, loading the legs "
            "like a spring, so the penetration step can fire underneath the "
            "opponent's hands and the shot arrives below the sprawl. It is "
            "also a fake in its own right: a sharp level change freezes the "
            "opponent, whose hands drop to block a shot that never comes, "
            "opening the head and upper body for snap-downs, arm drags, and "
            "throws. The mechanics are a pure knee bend - the back stays "
            "straight, the chest stays up, the head stays up, and only the "
            "hips descend, as if sitting into a short squat. The most common "
            "failure is bending at the waist instead of the knees, which "
            "drops the head into the opponent's front headlock and surrenders "
            "the spine. Drilled as a standalone motion - drop and recover, "
            "drop and recover - the level change becomes the metronome of "
            "the wrestler's offense."
        ),
        "how_it_works": (
            "Step 1: start in motion. Circle in stance so the level change "
            "grows out of live feet. Step 2: bend the knees sharply. Drop "
            "the hips straight down several inches by bending the knees, "
            "keeping the back straight and the chest up. Step 3: keep the "
            "head up. The eyes stay on the opponent's chest; the head never "
            "follows the hips down. Step 4: load, don't lean. Feel the "
            "weight settle into the balls of the feet with the knees over "
            "the toes - coiled, not collapsed. Step 5: explode or recover. "
            "Either fire the penetration step from the loaded position, or "
            "rise back to stance if it was a fake - both at full speed. "
            "Step 6: chain the fake. Drop the level, watch the opponent's "
            "hands drop, then attack high with a snap-down or arm drag while "
            "their guard is low. Step 7: drill the rhythm. Alternate real "
            "shots and level-change fakes so the opponent can never tell "
            "which drop is loaded."
        ),
        "key_points": [
            "The drop is a knee bend, not a waist bend; the back and head stay up.",
            "A sharp level change is itself a fake - it drags the opponent's hands down.",
            "Load the legs like a spring; the penetration step fires from the loaded position.",
            "Bending at the waist feeds the head to the front headlock - the cardinal error.",
            "Rhythm matters: alternate real drops and fake drops so none can be read.",
        ],
        "requirements": [
            "Open mat for drop-and-recover repetitions and drop-to-shot chains.",
            "A partner to read the fakes - the drill only works against live reactions.",
            "A mirror or coach checking that the back stays straight on every drop.",
            "Timed sets: ten level changes alternating with full shots per round.",
            "Leg conditioning - the drill is a squat workout disguised as technique.",
        ],
        "standards": [
            "Level-change mechanics follow standard coaching practice (Gable 1999).",
            "Spine-safe posture (no waist bending) is enforced in all drilling.",
            "Fake-to-shot chains are drilled at controlled speed before full speed.",
        ],
        "citations": [CIT_GABLE, CIT_UWW],
        "sig_lens": (
            "The Signature read: the level change is the Signature tide "
            "going out before the wave. The wrestler sinks and the opponent "
            "reads the sea wrong - hands drop to meet a flood that is only a "
            "feint, or fail to drop before the true wave arrives. To master "
            "the level is to master deception itself."
        ),
    },
    {
        "key": "collar_tie",
        "name": "The Collar Tie",
        "group": "Clinch Ties",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The collar tie is the fundamental head-and-neck control tie of "
            "wrestling: the wrestler cups the back of the opponent's neck or "
            "the trapezius with the palm, elbow high and tight, and uses the "
            "tie to pull, push, snap, and steer the opponent's head - and "
            "where the head goes, the body follows. From the collar tie come "
            "snap-downs, go-behinds, front headlocks, and the pressure that "
            "sets up every other tie. The mechanics demand the elbow stay "
            "high (a low elbow is an invitation to the duck-under) and the "
            "grip stay on the neck meat, never the throat; control comes "
            "from the whole arm and shoulder, not from squeezing the hand. "
            "The collar tie is a two-way weapon - both wrestlers usually "
            "hold one - so the battle of the tie is a battle of position: "
            "inside position, higher elbow, better head position. Wrestlers "
            "drill pummeling in and out of the collar tie until the tie "
            "feels like an extension of the arm."
        ),
        "how_it_works": (
            "Step 1: reach with the lead hand. From stance, extend the lead "
            "hand and cup the back of the opponent's neck, palm on the "
            "trapezius, fingers together. Step 2: raise the elbow. Lift the "
            "elbow high and keep it tight to your own head - the elbow is "
            "the shield of the tie. Step 3: set the head position. Tuck your "
            "forehead against the side of the opponent's head, staying "
            "forehead-to-temple so their head cannot turn into you. Step 4: "
            "pull and push. Use the tie to pull the opponent's head down "
            "and push it side to side, breaking their posture and reading "
            "their reactions. Step 5: snap from the tie. When the opponent "
            "pushes back into the tie, snap the head down sharply and "
            "circle behind (the snap-down and go-behind). Step 6: defend "
            "the tie. If the opponent gets the deeper tie, pummel the free "
            "hand inside, raise your elbow, and reclaim head position. "
            "Step 7: drill the battle. Pummel continuously with a partner, "
            "fighting for inside position and high elbows for timed rounds."
        ),
        "key_points": [
            "Cup the neck/trapezius with the palm; the grip is on muscle, never the throat.",
            "Elbow high and tight - a low elbow invites the duck-under.",
            "Head position wins ties: forehead to temple, never letting the opponent turn in.",
            "The tie is a steering wheel: pull, push, and snap the head to move the body.",
            "Both wrestlers hold ties, so pummeling for inside position is constant war.",
        ],
        "requirements": [
            "A partner for tie-up drilling and pummeling rounds.",
            "Mat space for tie battles that move across the mat.",
            "Instruction on legal tie areas - the grip stays off the throat.",
            "Timed pummeling rounds to build the shoulder and grip endurance ties demand.",
            "A coach watching elbow height and head position - the two deciding details.",
        ],
        "standards": [
            "Tie-up practice follows standard coaching practice (Gable 1999).",
            "Grips on the throat are illegal; control is applied to the neck and trapezius.",
            "UWW rules govern legal holds from the tie in competition.",
        ],
        "citations": [CIT_GABLE, CIT_UWW],
        "sig_lens": (
            "The Signature read: the collar tie is the Signature hand upon "
            "the helm. To hold the neck is to hold the rudder of the ship - "
            "pull and the vessel heels, push and it turns, snap and it "
            "dives. The Signature wrestler steers opponents the way "
            "captains steer storms: with a firm hand and a high elbow."
        ),
    },
    {
        "key": "underhook",
        "name": "The Underhook",
        "group": "Clinch Ties",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The underhook is the dominant clinch tie of wrestling: the "
            "wrestler threads the arm deep under the opponent's armpit, "
            "palm on the far shoulder blade or lat, elbow tight to the "
            "ribs, and uses the position to lift, turn, and throw the "
            "opponent while denying them any offense on that side. From the "
            "underhook come the hip toss, the throw-by, the high single "
            "when the opponent whizzers, and the body lock; in Greco-Roman, "
            "where leg attacks are forbidden, the underhook is the throne "
            "of offense. The tie must be deep - a shallow underhook is just "
            "an arm the opponent can whizzer - with the shoulder driven "
            "into the opponent's armpit and the head positioned on the "
            "underhook side to block the counter. Wrestlers pummel "
            "relentlessly for the underhook because the wrestler with two "
            "underhooks controls the match, and the wrestler with none is "
            "being controlled."
        ),
        "how_it_works": (
            "Step 1: pummel inside. From the tie-up, swim the hand inside "
            "the opponent's arm and thread it deep under the armpit. Step 2: "
            "go deep. Drive the shoulder into the armpit and reach the palm "
            "to the far shoulder blade; depth is everything. Step 3: close "
            "the elbow. Pin your elbow tight to your own ribs so the tie "
            "cannot be whizzered over. Step 4: set the head. Place your head "
            "on the underhook side, forehead against the opponent's temple "
            "or jaw, blocking their turn-in. Step 5: lift and turn. Use the "
            "underhook to lift the opponent's near side and turn them - "
            "step across for the hip toss, or throw by as they push back. "
            "Step 6: defend the counter. If the opponent overhooks your "
            "underhook (the whizzer), keep the elbow tight, circle toward "
            "the whizzer, and attack the far leg. Step 7: drill the pummel. "
            "Fight for underhooks continuously, scoring each deep entry, "
            "until the pummel is instinct."
        ),
        "key_points": [
            "Depth decides the tie: shoulder in the armpit, palm on the far shoulder blade.",
            "Elbow pinned to the ribs; a loose elbow gets whizzered.",
            "Head on the underhook side blocks the opponent's turn-in and counters.",
            "The underhook is Greco-Roman's throne - lift, turn, throw, or body lock from it.",
            "Two underhooks control the match; pummeling for them never stops.",
        ],
        "requirements": [
            "A partner for pummeling and underhook-entry drilling.",
            "Mat space for throws and throw-bys launched from the tie.",
            "Instruction distinguishing the deep underhook from the shallow, whizzerable arm.",
            "Timed pummel rounds with scoring for deep entries.",
            "Crash-mat practice for the throws before live entries.",
        ],
        "standards": [
            "Underhook entries follow standard coaching practice (Gable 1999).",
            "Throw finishes from the underhook are drilled on crash mats first.",
            "UWW Greco-Roman rules: the underhook is a legal upper-body tie; no holds below the waist.",
        ],
        "citations": [CIT_GABLE, CIT_UWW],
        "sig_lens": (
            "The Signature read: the underhook is the Signature key turned "
            "in the lock of the opponent's body. Deep it goes, past the "
            "armpit gate, and the door swings - lift, turn, throw. The "
            "Signature wrestler does not reach for the underhook; he takes "
            "up residence inside it."
        ),
    },
    {
        "key": "overhook",
        "name": "The Overhook",
        "group": "Clinch Ties",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The overhook is the defensive answer to the underhook: the "
            "wrestler drapes the arm over the opponent's underhooking arm, "
            "clamping it tight to the body with downward pressure, and uses "
            "the position to kill the opponent's offense, set up the "
            "whizzer, and launch counters like the throw-by and the lateral "
            "drop. The overhook must clamp down hard - a lazy overhook is "
            "simply carried by the underhook - with the elbow tight, the "
            "hand controlling the opponent's far wrist or tricep, and the "
            "hips back so the underhook cannot lift. From the overhook the "
            "wrestler can whizzer to stop shots, throw by when the opponent "
            "pushes, and drop laterally when the opponent overcommits. The "
            "tie is a constant negotiation: the underhook wants depth and "
            "lift, the overhook wants clamp and downward pressure, and the "
            "wrestler who wins the negotiation wins the position."
        ),
        "how_it_works": (
            "Step 1: clamp over. As the opponent threads the underhook, "
            "drape your arm over their arm and clamp it tight against your "
            "body. Step 2: pressure down. Drive the overhooking arm downward "
            "with your shoulder and lat, killing the lift of the underhook. "
            "Step 3: control the wrist. Grab the opponent's far wrist or "
            "tricep with the overhooking hand to limit their motion. "
            "Step 4: hips back. Keep your hips away so the underhook cannot "
            "get under your center and lift. Step 5: whizzer on shots. When "
            "the opponent shoots on the overhook side, lock the overhook "
            "into a whizzer - straighten the arm and drive down through "
            "their shoulder. Step 6: throw by on pressure. When the "
            "opponent pushes hard into the overhook, pull the arm across "
            "your body and step behind (the throw-by). Step 7: drill the "
            "negotiation. Pummel with a partner alternating underhook and "
            "overhook, feeling the clamp-versus-lift battle from both sides."
        ),
        "key_points": [
            "Clamp the opponent's arm tight to your body with heavy downward pressure.",
            "Hips back denies the underhook the lift it needs to throw.",
            "Wrist or tricep control with the overhooking hand limits the opponent's motion.",
            "The overhook becomes the whizzer the instant a shot comes on that side.",
            "Push pressure into the overhook opens the throw-by; it is a counter tie.",
        ],
        "requirements": [
            "A partner drilling underhook-versus-overhook exchanges.",
            "Mat space for throw-by and lateral-drop counters from the tie.",
            "Instruction on the whizzer transition - the overhook's emergency form.",
            "Timed clamp rounds: hold the overhook against a partner trying to lift.",
            "Video review of elbow tightness and hip distance - the two failure points.",
        ],
        "standards": [
            "Overhook mechanics follow standard coaching practice (Gable 1999).",
            "Counter throws from the overhook are drilled on crash mats first.",
            "UWW rules govern legal upper-body ties and counters in competition.",
        ],
        "citations": [CIT_GABLE, CIT_UWW],
        "sig_lens": (
            "The Signature read: the overhook is the Signature lid upon the "
            "boiling pot. The opponent's underhook rises like steam and the "
            "overhook presses it down, down, until the pressure finds its "
            "own escape - and the escape is the throw. To overhook is to "
            "govern another's ambition."
        ),
    },
    {
        "key": "russian_tie",
        "name": "The Two-on-One (Russian Tie)",
        "group": "Clinch Ties",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The two-on-one, called the Russian tie, is the control tie in "
            "which the wrestler grips the opponent's arm with both hands - "
            "one at the wrist, one above the elbow - and uses the two-against-"
            "one leverage to drag, post, and steer the opponent wherever the "
            "attack needs them. Two arms against one arm is the simplest "
            "arithmetic in wrestling, and it wins: the controlled arm "
            "cannot post, cannot tie, and cannot defend the far side. From "
            "the Russian tie come arm drags, single legs on the far side, "
            "foot sweeps, and throw-bys; the tie also drags the opponent "
            "into front headlocks when they resist the pull. The grip must "
            "stay active - the wrist hand pulls while the elbow hand pushes, "
            "creating a steering wheel on the opponent's arm - and the "
            "wrestler's stance must stay low, because a tall Russian tie is "
            "a duck-under waiting to happen. It is the great equalizer tie, "
            "letting a smaller wrestler boss a stronger arm."
        ),
        "how_it_works": (
            "Step 1: catch the wrist. From the tie-up, catch the opponent's "
            "wrist with your near hand. Step 2: add the second hand. Bring "
            "your other hand above their elbow, so both hands control the "
            "one arm - wrist hand and elbow hand. Step 3: create the wheel. "
            "Pull with the wrist hand and push with the elbow hand, bending "
            "their arm into a lever you can steer. Step 4: stay low. Drop "
            "your level so the tie is anchored to your hips, not held up in "
            "the air where it can be ducked under. Step 5: drag and circle. "
            "Drag the controlled arm across their body while circling to the "
            "controlled side, pulling them off balance. Step 6: attack the "
            "far side. With their arm tied up, shoot the far-side single leg "
            "or arm-drag past the controlled arm to the back. Step 7: "
            "defend the duck. If the opponent ducks under the tie, keep the "
            "wrist grip, follow with the hips, and re-drag before they "
            "clear."
        ),
        "key_points": [
            "Two hands on one arm: wrist hand pulls, elbow hand pushes - a steering wheel.",
            "The controlled arm cannot post or defend the far side; the far side is always open.",
            "Stay low and anchor the tie to the hips; a high tie gets ducked under.",
            "Drag across the body while circling to the controlled side to break balance.",
            "The great equalizer: leverage beats strength when the arithmetic is two on one.",
        ],
        "requirements": [
            "A partner for Russian-tie entry and drag drilling.",
            "Mat space for far-side shots and arm drags launched from the tie.",
            "Instruction on keeping the tie low and the stance intact.",
            "Timed control rounds: maintain the two-on-one against a partner trying to strip it.",
            "Review of duck-under defense - the tie's built-in risk.",
        ],
        "standards": [
            "Two-on-one mechanics follow standard coaching practice (Gable 1999).",
            "Grip fighting from the tie stays within UWW legal-hold rules.",
            "Far-side attacks from the tie are drilled at controlled speed first.",
        ],
        "citations": [CIT_GABLE, CIT_UWW],
        "sig_lens": (
            "The Signature read: the Russian tie is Signature arithmetic - "
            "two against one, and the one always loses. The Signature "
            "wrestler does not fight the strong arm; he outvotes it. Grip "
            "the wrist, command the elbow, and the opponent's strongest "
            "limb becomes your steering oar."
        ),
    },
    {
        "key": "sprawl",
        "name": "The Sprawl",
        "group": "Defense and Escapes",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The sprawl is the primary defense against leg attacks in "
            "freestyle wrestling: the instant the opponent shoots, the "
            "defender throws the legs back, drives the hips hard to the "
            "mat, and lands heavy chest pressure on the shooter's head and "
            "shoulders, killing the penetration and leaving the attacker "
            "flattened underneath. A correct sprawl lands the hips on the "
            "mat behind the sprawling legs, the chest on the back of the "
            "opponent's head and neck, and the arms wrapping the head or "
            "posting on the mat - the defender's weight becomes a blanket "
            "the shot cannot lift. From the sprawl come the go-behind "
            "(circling to the back for the takedown), the front headlock, "
            "and the crossface series. The sprawl must be violent and "
            "total; a half sprawl - hips high, legs only half back - is "
            "simply a single leg waiting to be finished. Wrestlers drill "
            "sprawls by the hundred until the hips hit the mat before "
            "thought arrives."
        ),
        "how_it_works": (
            "Step 1: read the shot. Watch the opponent's level change - the "
            "drop of the hips is the starting gun. Step 2: throw the legs "
            "back. Kick both legs straight back as if doing a falling "
            "push-up, landing on the tops of the feet with the legs wide. "
            "Step 3: drive the hips down. Slam the hips to the mat, aiming "
            "to land the hips behind where the shooter's head is. Step 4: "
            "land heavy on the head. Drop the chest onto the back of the "
            "opponent's head and neck, driving their face toward the mat. "
            "Step 5: wrap or post. Wrap the arms around the head for the "
            "front headlock, or post the hands on the mat to keep the "
            "weight forward. Step 6: circle to the back. With the shooter "
            "flattened, circle the hips behind and take the go-behind for "
            "the takedown. Step 7: drill the reaction. Have a partner shoot "
            "at random intervals; sprawl every time, full violence, until "
            "the reaction is faster than the thought."
        ),
        "key_points": [
            "Legs back, hips to the mat, chest heavy on the shooter's head - all three, every time.",
            "The hips must land behind the shooter's head; hips high is a half sprawl and a lost takedown.",
            "Read the level change - the hips dropping is the starting gun for the sprawl.",
            "From the sprawl: go-behind, front headlock, or crossface - the sprawl is offense begun.",
            "Drill by the hundred; the sprawl must fire before thought arrives.",
        ],
        "requirements": [
            "A mat and a partner shooting live shots at varied intervals.",
            "Hip and core conditioning - the sprawl is an explosive whole-body motion.",
            "Instruction on landing position: hips down, chest on the head, never the knees first.",
            "Repetition volume: sprawl drills are counted in hundreds per week.",
            "A coach timing the reaction from level change to hip contact.",
        ],
        "standards": [
            "Sprawl mechanics follow standard coaching practice (Gable 1999).",
            "Full-speed sprawl drilling requires a clean, burn-free mat.",
            "Go-behind finishes from the sprawl follow UWW takedown scoring (2 points freestyle).",
        ],
        "citations": [CIT_GABLE, CIT_UWW],
        "sig_lens": (
            "The Signature read: the sprawl is the Signature mountain "
            "falling upon the plain. The shot comes like a river and the "
            "mountain drops into its path - hips the bedrock, chest the "
            "avalanche upon the head. The Signature wrestler does not "
            "retreat from the shot; he buries it."
        ),
    },
    {
        "key": "whizzer",
        "name": "The Whizzer",
        "group": "Defense and Escapes",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The whizzer is the overhook hardened into a weapon: when the "
            "opponent shoots or drives in on the whizzer side, the defender "
            "locks the overhook deep, straightens the arm, and drives "
            "downward through the opponent's shoulder with the full weight "
            "of the upper body, using the arm as a lever to stuff the head, "
            "break the attacker's posture, and set up the go-behind. It is "
            "the great eraser of single legs - the shooter wraps the leg "
            "and the whizzer drives their head to the mat, turning their "
            "attack into the defender's takedown. The mechanics require the "
            "arm locked straight (a bent whizzer is just an overhook being "
            "carried), the shoulder dropped into the lever, and the hips "
            "back and heavy. Combined with a sprawl of the far leg, the "
            "whizzer is nearly impenetrable; used alone against a committed "
            "double leg it can be run through, which is why the whizzer is "
            "always paired with hip position. Every wrestler's defense "
            "carries one."
        ),
        "how_it_works": (
            "Step 1: lock the overhook. As the shot comes on your overhook "
            "side, clamp the overhook deep and tight. Step 2: straighten the "
            "arm. Lock the whizzering arm straight, turning it into a rigid "
            "lever over their shoulder. Step 3: drop the shoulder. Drive "
            "your shoulder down into the lever, putting your upper-body "
            "weight through their shoulder toward the mat. Step 4: hips "
            "back. Keep the hips away so the shooter cannot run through the "
            "whizzer to finish. Step 5: sprawl the far leg. Kick the far leg "
            "back into a partial sprawl so the shooter has no second leg to "
            "convert to. Step 6: stuff the head. Keep driving until their "
            "head is on the mat and their attack is broken. Step 7: circle "
            "behind. With the head stuffed, circle to the back for the "
            "go-behind takedown, keeping the whizzer until the back is "
            "taken."
        ),
        "key_points": [
            "The whizzer is a locked-straight overhook driven down through the shoulder.",
            "Drop the shoulder into the lever; upper-body weight does the work, not the arm alone.",
            "Hips back and far leg sprawled - the whizzer alone can be run through.",
            "It erases single legs: the shooter's head goes to the mat and the attack becomes your takedown.",
            "Keep the whizzer until the back is taken; releasing early resurrects the shot.",
        ],
        "requirements": [
            "A partner shooting single legs on the whizzer side.",
            "Shoulder and upper-back strength work - the whizzer is a heavy lever.",
            "Instruction on the straight-arm lock; bent-arm whizzers fail.",
            "Mat space for the stuff-and-circle go-behind finish.",
            "Drilling against both high singles and low singles to learn the whizzer's limits.",
        ],
        "standards": [
            "Whizzer mechanics follow standard coaching practice (Gable 1999).",
            "Go-behind finishes from the whizzer follow UWW takedown scoring.",
            "Shoulder safety: the lever drives the opponent's shoulder, never cranks the joint past range.",
        ],
        "citations": [CIT_GABLE, CIT_UWW],
        "sig_lens": (
            "The Signature read: the whizzer is the Signature lever that "
            "moves the world of the shot. The opponent wraps your leg and "
            "you lay the iron bar across his shoulder and lean the mountain "
            "upon it. His attack becomes your elevation - the Signature "
            "defense that counterattacks."
        ),
    },
    {
        "key": "standup",
        "name": "The Stand-Up Escape",
        "group": "Defense and Escapes",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The stand-up is the fundamental escape from the bottom of "
            "referee's position: the bottom wrestler clears the top "
            "wrestler's hands, stands to the feet in one explosive motion, "
            "and separates to neutral - scoring the escape point in "
            "collegiate wrestling and denying the top wrestler any turn in "
            "freestyle and Greco-Roman. The technique is a sequence, not a "
            "scramble: control the top wrestler's hands, post the outside "
            "foot, stand up tall while peeling the hands, and step away "
            "with hand control so the top wrestler cannot re-attack. The "
            "fatal errors are standing straight up into the top wrestler's "
            "chest (a mat return waiting to happen) and forgetting the "
            "hands (the top wrestler simply re-wraps and breaks you back "
            "down). Drilled as a five-count motion - hand control, foot "
            "post, stand, peel, separate - the stand-up is the bottom "
            "wrestler's declaration of independence."
        ),
        "how_it_works": (
            "Step 1: control the hands. From referee's position, grip the "
            "top wrestler's hands or wrists so they cannot lock around your "
            "waist. Step 2: post the foot. Step the outside foot up flat "
            "beside your knee, loading the leg to stand. Step 3: explode "
            "up. Drive off the posted foot and stand tall in one motion, "
            "keeping your head up and back straight. Step 4: peel the "
            "hands. As you rise, peel the top wrestler's hands off your "
            "body - strip the grip while standing, not before. Step 5: "
            "create separation. Step away with hand control, keeping your "
            "hands on theirs until the distance is safe. Step 6: face and "
            "reset. Turn to face the opponent in stance; the escape is only "
            "complete when you are neutral and safe. Step 7: drill the "
            "chain. Have the top wrestler ride and return; stand up, get "
            "returned, stand up again - the bottom wrestler never accepts "
            "the mat."
        ),
        "key_points": [
            "Hand control first: the top wrestler's hands must be managed before the body rises.",
            "One explosive stand - posting the outside foot and driving tall, head up.",
            "Peel the hands while rising; stripping early lets them re-lock.",
            "Separate with hand control; the escape ends at safe neutral distance, not at standing.",
            "Never stand up into the top wrestler's chest - rise away from the pressure.",
        ],
        "requirements": [
            "A partner to ride top and apply realistic breakdown pressure.",
            "Mat space for stand-and-separate repetitions.",
            "Instruction on hand-fighting from the bottom - the escape's first battle.",
            "Leg power work: the stand-up is a loaded single-leg squat against resistance.",
            "Timed escape rounds: bottom wrestler must escape within the period.",
        ],
        "standards": [
            "Stand-up mechanics follow standard coaching practice (Gable 1999).",
            "NCAA rules award 1 point for the escape; UWW freestyle awards no escape point - the value is positional.",
            "Bottom-wrestler hand-fighting must stay within legal-hold rules.",
        ],
        "citations": [CIT_GABLE, CIT_NCAA, CIT_UWW],
        "sig_lens": (
            "The Signature read: the stand-up is the Signature rising. "
            "Held down by hands and weight, the Signature wrestler does not "
            "wriggle or beg - he stands, in one motion, peeling the "
            "oppressor's grip like old paint. To stand up is to refuse the "
            "mat's verdict."
        ),
    },
    {
        "key": "referee_position",
        "name": "The Referee Position and Par Terre Defense",
        "group": "Defense and Escapes",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Referee's position is the ordered start for top and bottom "
            "wrestling: the bottom wrestler on hands and knees with hands "
            "on the mat, the top wrestler kneeling beside with one hand on "
            "the opponent's near elbow and one on the near back. In "
            "freestyle the position follows takedowns; in Greco-Roman the "
            "referee orders par terre - the bottom wrestler flat with arms "
            "folded - after passivity calls. Par terre defense is the art of "
            "surviving the top wrestler's turns: the bottom wrestler stays "
            "heavy, keeps the hips down and the base wide, hand-fights "
            "every lock attempt, and never lets the top wrestler get under "
            "the body. The gut wrench and leg lace - each worth 2 points "
            "per turn in UWW scoring - are the weapons par terre defense "
            "must defeat. The bottom wrestler who survives par terre "
            "without conceding turns has won the period's hidden battle."
        ),
        "how_it_works": (
            "Step 1: set the base. From referee's position, spread the "
            "knees wide, keep the hips low and heavy, and post the hands "
            "firmly - a wide heavy base. Step 2: hand-fight everything. "
            "The moment the top wrestler's hands move to lock, fight them: "
            "strip grips, keep elbows in, never let a lock close. Step 3: "
            "stay flat in par terre. When ordered to par terre, go flat "
            "with arms folded tight, hips heavy, making no space under the "
            "body. Step 4: hip pressure down. If the top wrestler gets a "
            "gut-wrench lock, drive the hips to the mat and arch slightly "
            "away, killing the lift. Step 5: follow the lace. If a leg lace "
            "locks, keep the laced leg heavy and straight, and turn with "
            "the pressure rather than fighting it rigidly. Step 6: explode "
            "on the whistle. When the referee restarts or the top wrestler "
            "resets, use the instant to improve the base or stand up. "
            "Step 7: drill the survival. Timed par terre rounds against a "
            "top wrestler hunting turns; the bottom wrestler's only job is "
            "zero points conceded."
        ),
        "key_points": [
            "Wide heavy base with low hips; the top wrestler must never get under the body.",
            "Hand-fight every lock attempt - no lock may close uncontested.",
            "In ordered par terre, go flat with folded arms and make no space underneath.",
            "Against the gut wrench: hips to the mat, arch away, kill the lift.",
            "Surviving par terre with zero points conceded wins the period's hidden battle.",
        ],
        "requirements": [
            "A partner drilling top turns (gut wrench, leg lace) at increasing intensity.",
            "Understanding of UWW par terre and passivity rules for Greco-Roman.",
            "Hip and core strength work - par terre defense is a strength position.",
            "Timed survival rounds scored on points conceded.",
            "A coach enforcing legal lock defense - no illegal holds to stop turns.",
        ],
        "standards": [
            "Par terre procedure follows UWW International Wrestling Rules (ordered par terre, passivity).",
            "UWW scoring: gut wrench and leg lace turns score 2 points each.",
            "NCAA referee's-position procedure follows the NCAA Wrestling Rules Book.",
        ],
        "citations": [CIT_UWW, CIT_NCAA, CIT_GABLE],
        "sig_lens": (
            "The Signature read: par terre defense is the Signature siege "
            "wall. Ordered to the ground, the Signature wrestler becomes the "
            "fortress - wide base the ramparts, heavy hips the gate barred, "
            "hand-fighting the archers on the walls. Let them bring their "
            "wrenches and laces; the wall does not open."
        ),
    },
    {
        "key": "double_leg",
        "name": "The Double Leg Takedown",
        "group": "Shots and Takedowns",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The double leg takedown is the signature leg attack of freestyle "
            "wrestling: the wrestler changes level, penetration-steps deep "
            "between the opponent's legs, wraps both legs with the arms, and "
            "drives through to bring the opponent to the mat - scoring 2 "
            "points under United World Wrestling rules (3 points under NCAA "
            "rules). It is the highest-percentage takedown in the sport "
            "because it attacks both legs at once, leaving the defender no "
            "base to post on. The finish has flavors: the drive-through "
            "(run the opponent over), the lift (elevate and return), and "
            "the cutback (change direction as the defender sprawls). All "
            "share the same entries - level change, deep penetration step, "
            "head tight to the ribs, trail knee down - and all demand the "
            "leg drive that separates committed shots from reaches. The "
            "double leg is drilled from every setup: the collar tie, the "
            "underhook, the arm drag, and the snap-down fake."
        ),
        "how_it_works": (
            "Step 1: set it up. From the tie or motion, change level and "
            "draw the opponent's hands up or freeze their feet. Step 2: "
            "penetration step. Step the lead foot deep between the "
            "opponent's feet and drop the trail knee to the mat beside it. "
            "Step 3: head position. Tuck the head tight against the "
            "opponent's ribs on the outside, ear to the body, eyes forward - "
            "never between the legs. Step 4: wrap both legs. Encircle both "
            "thighs with the arms, hands locked or elbows tight, cheek to "
            "the hip. Step 5: drive. Push off the trail toes and drive the "
            "hips forward and up into the opponent, running through the "
            "finish. Step 6: choose the finish. If the opponent stays "
            "upright, drive through and run them over; if they sprawl hard, "
            "cut back the other way or lift the trapped legs. Step 7: land "
            "in control. Come up on top with chest pressure, ready to work "
            "for the turn - the takedown is only the down payment."
        ),
        "key_points": [
            "Both legs wrapped at once; the defender has no base left to post on.",
            "Head tight to the outside ribs, never between the legs where the sprawl lands.",
            "The penetration step and trail knee create the entry; leg drive creates the finish.",
            "Finishes: drive-through, lift-and-return, or cutback against the hard sprawl.",
            "UWW: 2 points; NCAA: 3 points - the highest-percentage takedown in wrestling.",
        ],
        "requirements": [
            "Mastery of the penetration step and level change - the double leg is built on them.",
            "A partner drilling entries at increasing speed and resistance.",
            "Crash-mat or full-mat space for drive-through finishes.",
            "Leg drive conditioning: sled pushes and shot repetitions build the finish.",
            "A coach checking head position on every entry - the head decides safety.",
        ],
        "standards": [
            "Takedown scoring: 2 points UWW freestyle; 3 points NCAA (2023-24 rules change).",
            "Entry mechanics follow standard coaching practice (Gable 1999).",
            "Head-outside position is mandatory; head-inside double legs are coached as unsafe.",
        ],
        "citations": [CIT_UWW, CIT_NCAA, CIT_GABLE],
        "sig_lens": (
            "The Signature read: the double leg is the Signature battering "
            "ram. Two legs, one gate, and the ram does not knock - it "
            "removes the gate from its hinges. The Signature wrestler "
            "attacks both pillars at once because a fortress with no "
            "foundation is just a pile of stones."
        ),
    },
    {
        "key": "high_single",
        "name": "The High Single Leg",
        "group": "Shots and Takedowns",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The high single leg is the freestyle leg attack on one leg, "
            "taken high around the thigh: the wrestler penetration-steps to "
            "the opponent's lead leg, wraps it high with both arms - head "
            "inside (head on the inside of the thigh, the classic position) "
            "or head outside - and finishes by running the pipe, tripping, "
            "or elevating the trapped leg while driving the opponent down. "
            "It scores the same 2 points (UWW) or 3 points (NCAA) as any "
            "takedown, and it is the great counter-attacking shot: when the "
            "opponent reaches or oversteps, the high single is there. The "
            "head-inside finish - head tight to the inner thigh, driving "
            "forward - is the position of control; the head-outside finish "
            "demands the whizzer be beaten with motion and elevation. "
            "Finishes include the run-the-pipe (circle while pulling the "
            "leg through), the trip (reap the far leg), and the crackdown "
            "(drop the trapped leg and drive over). The high single rewards "
            "the wrestler who shoots to the leg the opponent leaves "
            "forward."
        ),
        "how_it_works": (
            "Step 1: read the lead leg. Watch which leg the opponent steps "
            "forward; the high single hunts the lead leg. Step 2: penetrate "
            "to the leg. Change level and penetration-step so the lead "
            "shoulder meets the opponent's thigh. Step 3: wrap high. Enclose "
            "the thigh with both arms, hands locked, the leg high on your "
            "body. Step 4: head inside. Tuck the head to the inside of the "
            "thigh, ear against the leg, driving forward - this is the "
            "control position. Step 5: finish run-the-pipe. Circle toward "
            "the trapped leg while pulling it across and through, running "
            "the opponent down. Step 6: or finish with the trip. If the "
            "opponent hops to stay up, reap the far leg with your leg while "
            "driving the trapped thigh. Step 7: land heavy. Come down on "
            "top with the leg still controlled, ready to work the turn."
        ),
        "key_points": [
            "Attacks the lead leg high on the thigh; head inside is the control position.",
            "The great counter shot - it punishes every reach and overstep.",
            "Finishes: run-the-pipe, far-leg trip, or crackdown over the trapped leg.",
            "Head-outside singles must beat the whizzer with motion and elevation.",
            "Same scoring as any takedown: 2 points UWW, 3 points NCAA.",
        ],
        "requirements": [
            "Penetration-step mastery - the single leg entry is a shortened double-leg step.",
            "A partner giving varied lead-leg looks and live whizzer defense.",
            "Mat space for run-the-pipe and trip finishes at speed.",
            "Grip and arm endurance for holding the high wrap through the finish.",
            "Coaching on head-inside versus head-outside risk and reward.",
        ],
        "standards": [
            "Takedown scoring: 2 points UWW freestyle; 3 points NCAA.",
            "Single-leg mechanics follow standard coaching practice (Gable 1999).",
            "Finishes are drilled at controlled speed before live resistance.",
        ],
        "citations": [CIT_GABLE, CIT_UWW, CIT_NCAA],
        "sig_lens": (
            "The Signature read: the high single is the Signature snare. "
            "One leg lifted high and the mighty oak has one root - pull the "
            "root and the oak must fall. The Signature wrestler does not "
            "wrestle the whole opponent; he removes one pillar and lets "
            "gravity argue the rest."
        ),
    },
    {
        "key": "ankle_pick",
        "name": "The Ankle Pick",
        "group": "Shots and Takedowns",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The ankle pick is the timing takedown: as the opponent steps "
            "the lead foot forward, the wrestler reaches down, cups the "
            "ankle or heel, and pulls it while driving into the opponent's "
            "upper body - sweeping the stepping foot out from under them "
            "for the takedown. It looks effortless and it is the opposite: "
            "the technique is pure timing, reading the opponent's step "
            "rhythm and striking in the fraction of a second the foot is "
            "committed but not yet planted. The mechanics pair the low "
            "pull with high pressure - the hand takes the ankle while the "
            "shoulder or head drives the chest - so the opponent falls over "
            "the picked foot. Setups include the collar tie pull (drag the "
            "opponent forward so they step), the fake shot (hands drop, "
            "feet step), and the circle (the opponent steps to follow). "
            "The ankle pick scores like any takedown and costs almost no "
            "energy, which is why veterans love it."
        ),
        "how_it_works": (
            "Step 1: read the step. Circle with the opponent and learn the "
            "rhythm of their lead-foot steps. Step 2: draw the step. Pull "
            "on the collar tie or fake a level change so the opponent steps "
            "the lead foot forward. Step 3: drop with it. As the foot "
            "commits forward, drop your level and reach for the ankle. "
            "Step 4: cup the heel. Wrap the hand around the ankle or heel, "
            "fingers firm - catch the foot, not the air above it. Step 5: "
            "drive high. Simultaneously drive your shoulder or head into "
            "the opponent's chest or far shoulder. Step 6: pull and lift. "
            "Pull the ankle up and toward you while driving forward, "
            "sweeping the foot out from under them. Step 7: follow to the "
            "mat. Stay with the fall, landing on top in control for the "
            "takedown points."
        ),
        "key_points": [
            "Pure timing: strike in the instant the lead foot is committed but unplanted.",
            "Low pull plus high drive - the ankle goes one way, the chest goes the other.",
            "Setups draw the step: collar-tie pull, fake shot, or circling pressure.",
            "Cup the heel firmly; reaching at air is how ankle picks become sprawls.",
            "Low energy cost, high veteran value - the efficient takedown.",
        ],
        "requirements": [
            "A partner stepping at varied rhythms for timing reads.",
            "Drilling the collar-tie pull setup that manufactures the step.",
            "Knee and back flexibility for the deep low reach.",
            "Reaction training: the window is a fraction of a second.",
            "Mat awareness - the follow-through must land controlled, not reckless.",
        ],
        "standards": [
            "Takedown scoring: 2 points UWW freestyle; 3 points NCAA.",
            "Timing-based attacks follow standard coaching practice (Gable 1999).",
            "The pick targets the ankle/heel; holds must remain UWW-legal.",
        ],
        "citations": [CIT_GABLE, CIT_UWW],
        "sig_lens": (
            "The Signature read: the ankle pick is the Signature thief in "
            "the night. No crash, no drive, no warning - the foot simply "
            "ceases to be where the opponent left it, and the mighty "
            "stance becomes a stumble. The Signature wrestler steals the "
            "ground from under giants."
        ),
    },
    {
        "key": "low_single",
        "name": "The Low Single",
        "group": "Shots and Takedowns",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The low single is the ankle-level leg attack: the wrestler "
            "drops almost to the mat, shoots low along the ground to the "
            "opponent's lead ankle, wraps it with both hands, and finishes "
            "by elevating the foot, driving forward, or switching to a "
            "high single as the opponent reacts. It is the safest shot in "
            "wrestling - the attacker's head and body stay below the "
            "defender's sprawl, so the classic sprawl defense cannot reach "
            "it - and the signature weapon of technicians who win on "
            "timing rather than power. The entry is a long low penetration "
            "that skims the mat; the finish is a lift-and-drive or a "
            "switch-off to the far leg when the opponent pulls the ankle "
            "back. John Smith's low single made the technique legendary in "
            "American freestyle, and it remains the great equalizer for "
            "wrestlers giving up size and strength."
        ),
        "how_it_works": (
            "Step 1: stay low. Drop the level until the hips are near the "
            "mat - the low single starts lower than any other shot. Step 2: "
            "skim the entry. Shoot low along the mat to the opponent's lead "
            "ankle, head up, back straight, body nearly horizontal. Step 3: "
            "wrap the ankle. Enclose the ankle with both hands, head tight "
            "to the leg, cheek on the shin. Step 4: elevate. Lift the ankle "
            "while driving your shoulder into the leg, taking the foot off "
            "the mat. Step 5: drive or switch. Drive forward to run the "
            "opponent down, or - if they yank the leg back - switch off to "
            "the far leg or come up to the high single. Step 6: keep the "
            "head up. Through every finish the head stays up and the back "
            "stays straight; the low position never means a dropped head. "
            "Step 7: land in control. Finish on top with the leg secured, "
            "already working toward the turn."
        ),
        "key_points": [
            "The safest shot: the body stays below the sprawl's reach.",
            "Entry skims the mat; the hips start near the ground.",
            "Finish by elevating the ankle or switching off as the opponent reacts.",
            "The technician's weapon - timing and position beat size and power.",
            "Head up and back straight even at full extension; low never means collapsed.",
        ],
        "requirements": [
            "Exceptional level-change depth and hip flexibility.",
            "A partner drilling ankle reactions - pull-back, hop, and whizzer attempts.",
            "Mat space for the long low entry at full speed.",
            "Core strength to hold the near-horizontal body position.",
            "Study of switch-off finishes - the low single's second and third options.",
        ],
        "standards": [
            "Takedown scoring: 2 points UWW freestyle; 3 points NCAA.",
            "Low-single mechanics follow standard coaching practice (Gable 1999).",
            "Spine-safe posture is maintained through the full low extension.",
        ],
        "citations": [CIT_GABLE, CIT_UWW],
        "sig_lens": (
            "The Signature read: the low single is the Signature root "
            "cutter. While giants watch the sky for attacks, the Signature "
            "wrestler travels beneath their gaze along the mat and takes "
            "the ankle - the smallest handle on the largest body. Great "
            "oaks fall to the patient saw."
        ),
    },
    {
        "key": "arm_drag",
        "name": "The Arm Drag",
        "group": "Clinch Attacks",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The arm drag is the tie-up's great redirect: the wrestler "
            "catches the opponent's wrist, pulls it across the opponent's "
            "body while stepping to the side, and takes the back as the "
            "opponent's arm is dragged past - arriving behind for the "
            "go-behind takedown. It punishes every overcommitted tie: the "
            "harder the opponent pushes into the collar tie or the Russian "
            "tie, the faster the drag spins them. The mechanics are a pull "
            "and a step, not a pull alone - the wrist is dragged across "
            "while the feet circle hard to the dragged side, so the "
            "wrestler's hips clear the opponent's hips and the back is "
            "taken cleanly. From the back come the takedown, the leg "
            "attacks on a turned opponent, and in folkstyle the ride. The "
            "arm drag is also the setup king: drag to a single leg, drag "
            "to a double, drag to a throw-by - the back-take threatens "
            "everything."
        ),
        "how_it_works": (
            "Step 1: catch the wrist. From the tie, grip the opponent's "
            "near wrist with your near hand. Step 2: pull across. Drag the "
            "wrist firmly across the opponent's body toward your far side. "
            "Step 3: step and circle. As you pull, step hard to the dragged "
            "side, circling your hips past their hips. Step 4: clear the "
            "hips. Keep stepping until your chest is behind their shoulder "
            "and your hips are past theirs - the back is taken. Step 5: "
            "secure the waist. Wrap the far arm around the waist and lock "
            "on; the near hand keeps the dragged wrist. Step 6: finish the "
            "takedown. Drive forward for the go-behind, or drop to the "
            "single or double on the turned opponent. Step 7: drill the "
            "timing. Have the partner push into the tie; drag the instant "
            "their pressure commits - the drag feeds on their push."
        ),
        "key_points": [
            "Pull the wrist across while the feet circle hard - drag is pull plus step.",
            "Clear the hips: the back is only taken when your hips pass theirs.",
            "It feeds on pressure - the harder they push the tie, the faster the drag.",
            "From the back: go-behind, leg attacks, or the ride - everything is open.",
            "The setup king: drag to single, drag to double, drag to throw-by.",
        ],
        "requirements": [
            "A partner pushing into ties so the drag can be timed against pressure.",
            "Footwork drilling: the circle step must be as fast as the pull.",
            "Mat space for back-take finishes at speed.",
            "Wrist grip strength for the initial catch against resistance.",
            "Defense review: the failed drag gives up the tie, so commit fully.",
        ],
        "standards": [
            "Takedown scoring: 2 points UWW freestyle; 3 points NCAA.",
            "Arm-drag mechanics follow standard coaching practice (Gable 1999).",
            "Back-take finishes must control the opponent to the mat for the score.",
        ],
        "citations": [CIT_GABLE, CIT_UWW],
        "sig_lens": (
            "The Signature read: the arm drag is the Signature revolving "
            "door. The opponent pushes through it and finds himself "
            "outside his own attack, staring at your back where his "
            "victory was. The Signature wrestler does not meet force - he "
            "gives it a door to exit through, and charges admission in "
            "takedown points."
        ),
    },
    {
        "key": "snap_down",
        "name": "The Snap Down and Go-Behind",
        "group": "Clinch Attacks",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The snap-down is the collar tie's payoff: the wrestler snaps "
            "the opponent's head sharply toward the mat and, as the "
            "opponent's hands hit the mat and their hips rise, circles "
            "behind for the go-behind takedown. It is the highest-percentage "
            "front-headlock entry in wrestling because it manufactures the "
            "exact position - head down, hands on the mat, hips high - from "
            "which the go-behind is nearly free. The snap must be violent "
            "and committed, driven by the whole upper body with the elbow "
            "high; a weak snap just annoys the opponent. Timing sells it: "
            "snap when the opponent pushes into the tie or steps forward, "
            "so their own momentum carries their head down. The go-behind "
            "finish - circle, secure the waist, drive through - scores the "
            "takedown, and the snapped-down opponent who posts a hand "
            "offers the front headlock instead. Snap, circle, score."
        ),
        "how_it_works": (
            "Step 1: own the tie. Establish the collar tie with a high "
            "elbow and good head position. Step 2: feel the pressure. Wait "
            "for the opponent to push into the tie or step forward - their "
            "momentum is your fuel. Step 3: snap violently. Drive the "
            "opponent's head straight down toward the mat with the whole "
            "upper body, elbow high, in one explosive motion. Step 4: keep "
            "the grip. Maintain the collar-tie grip through the snap so "
            "you control the falling head. Step 5: circle immediately. The "
            "instant their hands touch the mat, circle hard behind, keeping "
            "contact on the head. Step 6: secure the waist. Wrap the waist "
            "as you arrive behind and lock on. Step 7: drive through. Finish "
            "the go-behind takedown, or - if they post - lock the front "
            "headlock and work the turn."
        ),
        "key_points": [
            "Snap on their pressure: their push into the tie becomes your snap's fuel.",
            "The snap must be violent - a weak snap only warns the opponent.",
            "Keep the collar-tie grip through the snap to steer the falling head.",
            "Circle the instant hands touch the mat; hesitation lets them recover.",
            "The snapped opponent offers two gifts: the go-behind or the front headlock.",
        ],
        "requirements": [
            "A committed collar tie with high elbow - the snap's launch pad.",
            "A partner drilling realistic tie pressure and forward steps.",
            "Neck and upper-back strength for the explosive snap.",
            "Mat space for the snap-and-circle finish at full speed.",
            "Timing work: snapping early (no pressure) and late (sprawled on) both fail.",
        ],
        "standards": [
            "Takedown scoring: 2 points UWW freestyle; 3 points NCAA.",
            "Snap-down mechanics follow standard coaching practice (Gable 1999).",
            "The snap controls the head and neck within legal-hold limits - no throat grips.",
        ],
        "citations": [CIT_GABLE, CIT_UWW],
        "sig_lens": (
            "The Signature read: the snap-down is the Signature thunderclap. "
            "The tie holds the sky, and in one motion the sky falls - head "
            "driven to the earth, hands slapping the mat in surrender. The "
            "Signature wrestler does not push opponents down; he convinces "
            "the ground to call them."
        ),
    },
    {
        "key": "front_headlock",
        "name": "The Front Headlock",
        "group": "Clinch Attacks",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The front headlock is the control position captured when the "
            "opponent's head goes down - off the snap-down, the sprawl, or "
            "the failed shot: the wrestler encircles the head and an arm "
            "with both arms, locks the hands, and uses the position to "
            "control, turn, and pin. From the front headlock come the "
            "go-behind (circle and release into the back), the cement "
            "mixer (roll through for the turn), the cradle entries, and the "
            "pinning combinations that end matches. The lock must be tight "
            "and the hips heavy - the headlocker's chest on the opponent's "
            "back, weight driving down, so the trapped wrestler carries "
            "the headlocker's weight with every breath. It is both a "
            "scoring position and a resting position: the wrestler in the "
            "front headlock can control the pace while hunting the turn. "
            "Every snap-down drill ends here, which is why the front "
            "headlock is wrestling's busiest intersection."
        ),
        "how_it_works": (
            "Step 1: capture the head. As the opponent's head drops (snap, "
            "sprawl, or failed shot), encircle the head and one arm with "
            "both of your arms. Step 2: lock tight. Lock your hands - "
            "palm to palm or S-grip - with the chin strap tight under their "
            "chin, never on the throat. Step 3: get heavy. Drive your chest "
            "onto their back and make your hips heavy; they carry your "
            "weight now. Step 4: control the motion. Keep the lock tight "
            "and circle with them, denying any attempt to stand or turn in. "
            "Step 5: choose the finish. Circle hard and release into the "
            "go-behind, or sit through for the cement mixer roll, or work "
            "toward the cradle. Step 6: watch the counters. If they start "
            "to peek out the back, tighten the lock and re-circle; never "
            "let the head slip. Step 7: drill the entries. Snap-down to "
            "headlock, sprawl to headlock, failed-shot to headlock - every "
            "road leads here."
        ),
        "key_points": [
            "Capture head and arm together; lock the hands with the chin strap under the chin.",
            "Get heavy: chest on their back, hips heavy - they carry your weight.",
            "The position is a crossroads: go-behind, cement mixer, cradle, or pin - all open.",
            "Circle with their motion; a static headlock is an escapable headlock.",
            "Never grip the throat; control the chin and head within legal holds.",
        ],
        "requirements": [
            "Reliable snap-down and sprawl entries - the headlock must be caught, not chased.",
            "A partner drilling headlock escapes so the lock is tested.",
            "Upper-body endurance: the position is held and worked for long stretches.",
            "Instruction on legal chin-strap placement versus throat pressure.",
            "Mat space for the roll-through finishes (cement mixer) at speed.",
        ],
        "standards": [
            "Front-headlock control follows standard coaching practice (Gable 1999).",
            "Chin-strap pressure must stay off the throat per UWW legal-hold rules.",
            "Turns and pins from the headlock follow UWW and NCAA scoring.",
        ],
        "citations": [CIT_GABLE, CIT_UWW],
        "sig_lens": (
            "The Signature read: the front headlock is the Signature yoke. "
            "The head bowed, the arm bound, the weight of the Signature "
            "wrestler settled upon the back like a judgment - the opponent "
            "plows the mat carrying a burden he did not choose. From the "
            "yoke, every road leads to the fall."
        ),
    },
    {
        "key": "duck_under",
        "name": "The Duck Under",
        "group": "Clinch Attacks",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The duck under is the tie-up's disappearing act: when the "
            "opponent reaches deep with the collar tie or pushes hard with "
            "a high elbow, the wrestler drops the level, ducks the head "
            "under the opponent's arm, and emerges behind for the takedown. "
            "It is the definitive answer to the overcommitted tie - the "
            "farther the opponent reaches, the cleaner the duck. The "
            "mechanics demand a true level change (the head must go under "
            "the arm, not into it), a hard step to the ducking side, and "
            "an immediate waist lock on emergence; a slow duck is simply a "
            "gifted front headlock. The duck under punishes tall ties, lazy "
            "elbows, and every wrestler who reaches instead of wrestling. "
            "Setups include inviting the tie (offer the collar tie and "
            "wait), the elbow raise (lift their elbow with your tie hand "
            "and go), and the pressure draw (push so they push back, then "
            "vanish). Duck, emerge, lock the waist, score."
        ),
        "how_it_works": (
            "Step 1: invite the reach. Tie up and let the opponent get "
            "comfortable reaching with the collar tie. Step 2: change "
            "level. Drop the hips sharply - the head must travel under the "
            "arm, which requires real depth. Step 3: duck the head. Slip "
            "the head under the opponent's armpit on the ducking side, "
            "keeping the head up and eyes forward. Step 4: step through. "
            "Step hard to the ducking side as the head clears, driving past "
            "their hip. Step 5: emerge behind. Come up behind the opponent "
            "with your chest to their back. Step 6: lock the waist. Wrap "
            "both arms around the waist immediately - the takedown is only "
            "scored when the back is controlled. Step 7: finish. Drive "
            "through for the go-behind takedown, lifting if they resist."
        ),
        "key_points": [
            "The duck punishes the reaching tie - the deeper they reach, the cleaner the duck.",
            "Real level change first; the head goes under the arm, never into it.",
            "Step hard to the ducking side as the head clears; speed is the technique.",
            "Emerge and instantly lock the waist - the back must be controlled to score.",
            "A slow duck becomes their front headlock; commit at full speed or not at all.",
        ],
        "requirements": [
            "A partner giving committed collar ties to duck under.",
            "Level-change depth sufficient to clear the armpit.",
            "Mat space for full-speed duck-and-emerge repetitions.",
            "A coach checking head clearance - ducking into the arm is the common failure.",
            "Drilling the waist-lock finish so the emergence always ends in control.",
        ],
        "standards": [
            "Takedown scoring: 2 points UWW freestyle; 3 points NCAA.",
            "Duck-under mechanics follow standard coaching practice (Gable 1999).",
            "The maneuver is legal in freestyle and Greco-Roman (upper-body entry).",
        ],
        "citations": [CIT_GABLE, CIT_UWW],
        "sig_lens": (
            "The Signature read: the duck under is the Signature vanishing. "
            "The opponent reaches for you and grasps the place you were; "
            "you are already behind him, hands upon his waist like fate. "
            "The Signature wrestler is never where the grasp falls - he is "
            "always one step beyond it, collecting the toll."
        ),
    },
    {
        "key": "hip_toss",
        "name": "The Hip Toss",
        "group": "Throws and Turns",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The hip toss is the fundamental upper-body throw: from the "
            "underhook (or the over-under clinch), the wrestler steps across "
            "the opponent's body, loads them onto the hip, and rotates the "
            "hips to throw them over - a clean, high-percentage throw that "
            "works in both freestyle and Greco-Roman. The hip becomes the "
            "fulcrum and the opponent's body the lever; the throw is "
            "powered by hip rotation and leg drive, not by arm strength. "
            "In Greco-Roman, where leg attacks are forbidden, the hip toss "
            "is core offense; in freestyle it punishes the wrestler who "
            "overhooks lazily or stands too tall in the clinch. Scoring "
            "rewards amplitude: a clean hip toss with the opponent's feet "
            "over their head and direct back exposure earns grand-amplitude "
            "points (4 points, 5 with direct danger under UWW rules). The "
            "entry must be deep - hip to hip, chest to chest - because a "
            "shallow hip toss is a counter waiting to happen."
        ),
        "how_it_works": (
            "Step 1: secure the underhook. Pummel to the deep underhook "
            "with the head on the underhook side. Step 2: step across. "
            "Step your underhook-side foot across the opponent's body, "
            "placing it beyond their far foot. Step 3: load the hip. Turn "
            "your hips in so your hip sits below their hip, back to chest, "
            "knees bent - they are loaded on the fulcrum. Step 4: pull "
            "with the underhook. Pull their upper body tight across your "
            "back with the underhook arm. Step 5: rotate and extend. Rotate "
            "the hips violently while straightening the legs, throwing the "
            "opponent over the hip fulcrum. Step 6: follow through. Stay "
            "with the throw, landing in control on top. Step 7: drill the "
            "load. Practice the step-across and hip load slowly until the "
            "fulcrum position is exact, then add speed - the throw is "
            "position first, power second."
        ),
        "key_points": [
            "The hip is the fulcrum, the opponent's body the lever; rotation throws, arms only guide.",
            "Step deep across and load hip-to-hip - a shallow entry gets countered.",
            "Core Greco-Roman offense and the freestyle answer to the lazy overhook.",
            "Amplitude scores: feet over head with back exposure earns grand-amplitude points.",
            "Position first, power second - the load decides the throw before the rotation starts.",
        ],
        "requirements": [
            "A deep underhook - the throw cannot launch from a shallow tie.",
            "A partner drilling the step-across load at increasing speed.",
            "Crash mats for learning the rotation before live throws.",
            "Hip flexibility and leg drive for the loaded rotation.",
            "A coach verifying hip-to-hip depth on every entry.",
        ],
        "standards": [
            "UWW scoring: grand-amplitude throws 4 points, 5 with direct danger position.",
            "Throw mechanics follow standard coaching practice (Gable 1999).",
            "Throws are drilled on crash mats before live execution.",
        ],
        "citations": [CIT_UWW, CIT_GABLE],
        "sig_lens": (
            "The Signature read: the hip toss is the Signature fulcrum of "
            "the world. Load the opponent upon the hip and the smallest "
            "rotation moves the largest mass - Archimedes with a singlet. "
            "The Signature wrestler does not lift giants; he gives them a "
            "hip to pivot on and lets geometry do the lifting."
        ),
    },
    {
        "key": "headlock_throw",
        "name": "The Headlock Throw",
        "group": "Throws and Turns",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The headlock throw is the clinch's thunderbolt: from the "
            "headlock position (head and arm controlled), the wrestler "
            "steps in front, arches the back, and throws the opponent over "
            "in a high-amplitude arc - the classic Greco-Roman "
            "match-ender. It is the highest-risk, highest-reward throw in "
            "the foundational arsenal: a clean headlock throw scores "
            "grand-amplitude points and often the fall, but a failed "
            "headlock throw gives up position badly, and the thrower must "
            "commit the hips fully or be counter-thrown. The mechanics are "
            "a deep step-in, a tight head-and-arm lock, and a full back "
            "arch with the hips driving under - the throw is a bridge "
            "thrown backward, not an arm pull. Wrestlers learn it on crash "
            "mats with patient partners because the arch demands trust and "
            "the landing demands control. Thrown cleanly, it is the most "
            "spectacular technique in wrestling."
        ),
        "how_it_works": (
            "Step 1: lock the head and arm. Secure the headlock with the "
            "head-and-arm grip tight, chin strap under the chin. Step 2: "
            "step deep in front. Step your near foot deep in front of the "
            "opponent's near foot, hips below theirs. Step 3: commit the "
            "hips. Drive your hips under and in, back to their chest, "
            "loading them on your body. Step 4: arch. Throw your head back "
            "and arch the back fully, lifting with the hips and legs - the "
            "body becomes the bridge they travel over. Step 5: guide, "
            "don't pull. Keep the head-and-arm lock tight and let the arch "
            "carry them over; the arms steer, the back throws. Step 6: "
            "land in control. Follow the throw to the mat, staying tight "
            "for the pin or the exposure points. Step 7: drill with trust. "
            "Learn the arch on crash mats with a cooperative partner "
            "before any live attempt - commitment without control is a "
            "counter."
        ),
        "key_points": [
            "Head-and-arm lock, deep step-in, full back arch - the throw is a bridge, not a pull.",
            "Highest risk, highest reward: clean throws end matches, failed ones give up position.",
            "Hips must go fully under; a half-committed headlock gets counter-thrown.",
            "Grand-amplitude scoring rewards the clean arc with back exposure.",
            "Learn on crash mats with trusted partners - the arch demands commitment and control.",
        ],
        "requirements": [
            "A tight head-and-arm lock - the throw cannot launch from a loose grip.",
            "Crash mats and a cooperative partner for learning the arch.",
            "Back and hip flexibility for the full bridge arch.",
            "A coach supervising every early attempt - the counter risk is real.",
            "Neck strength work: the arch loads the neck and upper back.",
        ],
        "standards": [
            "UWW scoring: grand-amplitude throws 4 points, 5 with direct danger position.",
            "Throw mechanics follow standard coaching practice (Gable 1999).",
            "Head-and-arm locks must stay within legal-hold limits - no throat pressure.",
        ],
        "citations": [CIT_UWW, CIT_GABLE],
        "sig_lens": (
            "The Signature read: the headlock throw is the Signature "
            "lightning. The clinch darkens, the hips gather the charge, "
            "and the back arches - the bolt strikes and the opponent "
            "travels the sky. The Signature wrestler throws lightning only "
            "when the storm is fully gathered; half-storms strike the "
            "thrower."
        ),
    },
    {
        "key": "gut_wrench",
        "name": "The Gut Wrench",
        "group": "Throws and Turns",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The gut wrench is the par terre turn that wins Greco-Roman "
            "matches: from the top position, the wrestler locks around the "
            "opponent's waist (hands locked, chest to back), and rolls the "
            "opponent over - lifting and turning them through back exposure "
            "for 2 points per turn under UWW rules. Chained gut wrenches - "
            "roll, re-lock, roll again - can pile up double-digit points in "
            "a single par terre period, which is why the gut wrench is the "
            "most drilled turn in Greco-Roman wrestling. The mechanics are "
            "a tight waist lock, the chest driving into the back, and a "
            "rolling lift powered by the hips and legs rather than the "
            "arms; the turn exposes the opponent's back to the mat on every "
            "rotation. Defense - hips heavy, arching away, hand-fighting "
            "the lock - is covered in par terre defense, but the best gut "
            "wrenchers lock so tight and roll so fast that defense arrives "
            "too late. It is also legal and effective in freestyle par "
            "terre."
        ),
        "how_it_works": (
            "Step 1: lock the waist. From top par terre, wrap both arms "
            "around the opponent's waist and lock the hands tight, chest "
            "to their back. Step 2: get perpendicular. Position your body "
            "across theirs, hips loaded to lift. Step 3: lift with the "
            "legs. Drive up with the legs and hips, elevating their waist "
            "off the mat - the lift starts the turn. Step 4: roll through. "
            "Roll across, carrying them over through back exposure, keeping "
            "the lock unbroken. Step 5: land in the lock. Finish the roll "
            "still locked around the waist, chest to back, ready to go "
            "again. Step 6: chain it. Without pausing, lift and roll again "
            "- each clean turn through danger is 2 more points. Step 7: "
            "drill the chain. Timed par terre periods: top wrestler chains "
            "wrenches, bottom wrestler defends; count the turns."
        ),
        "key_points": [
            "Waist lock, chest to back, lift with the legs - the arms hold, the hips turn.",
            "Each clean turn through back exposure scores 2 points (UWW).",
            "The chain is the weapon: roll, re-lock, roll - points compound per turn.",
            "Keep the lock unbroken through the roll; the chain dies when the hands open.",
            "Greco-Roman's match-winner and a freestyle par terre staple.",
        ],
        "requirements": [
            "A partner drilling par terre top and bottom at increasing resistance.",
            "A tight, practiced waist lock - the turn fails on a loose lock.",
            "Hip and leg power for the repeated lifts of the chain.",
            "Understanding of UWW exposure scoring to know when each turn counts.",
            "A coach counting clean turns versus sloppy rolls in drilling.",
        ],
        "standards": [
            "UWW scoring: 2 points per gut-wrench turn through danger position.",
            "Par terre procedure follows UWW International Wrestling Rules.",
            "The waist lock must remain a legal hold - no illegal grips.",
        ],
        "citations": [CIT_UWW, CIT_GABLE],
        "sig_lens": (
            "The Signature read: the gut wrench is the Signature millwheel. "
            "Locked around the waist, the Signature wrestler turns and the "
            "river of the match flows through the wheel - each rotation "
            "grinding two points of flour. Turn, and turn again; the mill "
            "does not tire, and neither does the Signature turn."
        ),
    },
    {
        "key": "leg_lace",
        "name": "The Leg Lace",
        "group": "Throws and Turns",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The leg lace is the freestyle par terre turn built on leg "
            "control: the top wrestler traps the opponent's leg - typically "
            "in a figure-four or lace lock around the thigh and ankle - and "
            "uses the trapped leg as a lever to turn the opponent through "
            "back exposure, scoring 2 points per turn under UWW rules. Like "
            "the gut wrench it chains - lace, turn, re-lace, turn - and a "
            "wrestler caught in a deep lace can concede a cascade of points "
            "before the period ends. The lock must capture the leg "
            "completely, with the top wrestler's body positioned to drive "
            "the turn; the lever is long (the whole leg) so the force "
            "multiplies, which is why even strong defenders get turned "
            "once the lace is deep. Entries come from the top position "
            "after takedowns, from the turk (leg ride), and from scrambles "
            "where a leg is momentarily isolated. The leg lace is freestyle "
            "ground wrestling at its most systematic."
        ),
        "how_it_works": (
            "Step 1: isolate the leg. From top, capture the opponent's "
            "near leg as they move - the lace hunts isolated legs. Step 2: "
            "lock the lace. Weave your legs around theirs in the lace "
            "lock, trapping thigh and ankle so the leg cannot straighten. "
            "Step 3: position to drive. Set your hips to drive across, "
            "chest over their hips, the trapped leg levered. Step 4: turn "
            "through exposure. Drive and roll the opponent through back "
            "exposure, keeping the lace locked. Step 5: hold the lock. "
            "Finish the turn with the lace still secured, ready to chain. "
            "Step 6: re-lace and repeat. Adjust the lock and turn again - "
            "each clean exposure is 2 points. Step 7: drill the entries. "
            "Practice lacing from the turk, from scrambles, and from the "
            "takedown landing; the turn is easy once the lace is deep."
        ),
        "key_points": [
            "The whole trapped leg is the lever; depth of the lace decides everything.",
            "Each turn through back exposure scores 2 points (UWW) - and the lace chains.",
            "Entries: the turk ride, scrambles, and takedown landings that isolate a leg.",
            "Keep the lace locked through the turn; the chain dies when the legs open.",
            "Freestyle ground wrestling at its most systematic - position, lock, turn, repeat.",
        ],
        "requirements": [
            "A partner drilling leg isolation and lace defense.",
            "Leg dexterity work: the lace is tied with the legs, not the hands.",
            "Understanding of UWW exposure criteria for counting turns.",
            "Mat space for chained turns at drilling speed.",
            "A coach checking lock depth - shallow laces get kicked out of.",
        ],
        "standards": [
            "UWW scoring: 2 points per leg-lace turn through danger position.",
            "Leg lace mechanics follow standard coaching practice (Gable 1999).",
            "The lock must remain a legal leg hold under UWW freestyle rules.",
        ],
        "citations": [CIT_UWW, CIT_GABLE],
        "sig_lens": (
            "The Signature read: the leg lace is the Signature snare of "
            "the long lever. One leg caught in the weave and the whole "
            "body must follow where the lever leads - turn, and turn "
            "again. The Signature wrestler ties the knot once and lets "
            "geometry collect the debt, two points at a time."
        ),
    },
    {
        "key": "half_nelson",
        "name": "The Half Nelson",
        "group": "Throws and Turns",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The half nelson is the classic pinning combination: from the "
            "top position, the wrestler threads one arm under the "
            "opponent's near armpit, places the hand on the back of the "
            "opponent's head or neck, and drives forward - turning the "
            "opponent to their back and holding them in danger for the "
            "fall. It is the first pinning hold most wrestlers learn and "
            "still one of the most reliable: the mechanics attack the "
            "head-neck-shoulder triangle, and once the opponent's shoulders "
            "go flat with the half nelson locked, the pin is a matter of "
            "pressure and patience. The power half nelson - driving with "
            "the legs while the arm levers the head - can turn even "
            "resistant opponents. Setups include the crossface series, the "
            "spiral ride breakdown, and the far-side cradle transition. A "
            "half nelson held with chest pressure and hip control ends "
            "matches; a loose one gets reversed, which is why the lock, "
            "the drive, and the patience are drilled as one motion."
        ),
        "how_it_works": (
            "Step 1: break them down. From top, flatten the opponent "
            "with a breakdown (spiral ride or crossface) so the base is "
            "gone. Step 2: thread the arm. Slide your near arm under their "
            "near armpit, deep. Step 3: set the hand. Place your hand on "
            "the back of their head or neck - on the head, never the "
            "throat. Step 4: drive forward. Drive with your legs, pressing "
            "their head toward the mat and turning their shoulders over. "
            "Step 5: stay chest to back. Keep your chest on their back and "
            "your hips heavy as they go to danger. Step 6: hold the pin. "
            "Once shoulders are flat, settle your weight, keep the half "
            "nelson locked, and hold through the referee's count. Step 7: "
            "drill the patience. Practice holding the pin against a "
            "bridging partner - the fall comes to the wrestler who does "
            "not rush."
        ),
        "key_points": [
            "Thread under the armpit, hand on the back of the head - the head-neck-shoulder triangle.",
            "Break them down first; the half nelson finishes flat opponents, it does not flatten them.",
            "Drive with the legs (power half) - the turn is leg-powered, not arm-yanked.",
            "Chest to back and hips heavy through the pin; patience finishes what pressure starts.",
            "The first pin learned and still one of the most reliable in wrestling.",
        ],
        "requirements": [
            "A reliable breakdown (spiral ride or crossface) to set up the pin.",
            "A partner drilling bridging escapes to test the hold.",
            "Instruction on legal hand placement - back of the head, never the throat.",
            "Leg drive conditioning for the power finish.",
            "Timed pin-hold rounds to build the patience the fall requires.",
        ],
        "standards": [
            "Pin/fall criteria follow UWW rules (shoulders held in danger) and NCAA rules.",
            "Half-nelson mechanics follow standard coaching practice (Gable 1999).",
            "Hand placement must stay legal - pressure on the back of the head, not the throat.",
        ],
        "citations": [CIT_UWW, CIT_NCAA, CIT_GABLE],
        "sig_lens": (
            "The Signature read: the half nelson is the Signature seal. "
            "The arm threads beneath, the hand settles upon the head, and "
            "the decree is pressed into the mat - shoulders flat, the wax "
            "cooling. The Signature wrestler does not chase the fall; he "
            "applies the seal and lets the count confirm it."
        ),
    },
    {
        "key": "switch_reversal",
        "name": "The Switch Reversal",
        "group": "Reversals and Escapes",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The switch is the bottom wrestler's reversal from referee's "
            "position: as the top wrestler applies pressure, the bottom "
            "wrestler sits through toward the top wrestler's far side, "
            "swings the near leg through, and comes up behind - reversing "
            "the position and scoring 2 points (1 point in some folkstyle "
            "contexts; the reversal is universally the bottom wrestler's "
            "counter-offense). The technique exploits the top wrestler's "
            "forward pressure: the harder they drive in, the more energy "
            "the switch borrows. Mechanics are a sit-through (hips swing "
            "under and past), a tight grip on the top wrestler's arm or "
            "waist, and a climb to the back as the top wrestler's momentum "
            "carries them forward into the trap. The switch must be "
            "explosive and complete - a half switch leaves the bottom "
            "wrestler flattened under a re-attack. Drilled against live "
            "top pressure, it becomes the bottom wrestler's favorite "
            "sentence: your pressure is my points."
        ),
        "how_it_works": (
            "Step 1: feel the pressure. From bottom referee's position, "
            "wait for the top wrestler to drive forward pressure. Step 2: "
            "sit through. Swing your hips under and toward the top "
            "wrestler's far side, sitting through their pressure. Step 3: "
            "swing the leg. Bring the near leg through hard, clearing it "
            "past their body. Step 4: grip the arm. Catch the top "
            "wrestler's near arm or waist as you come through, controlling "
            "their fall. Step 5: climb the back. Rise up behind them as "
            "their forward momentum carries them over - you are suddenly "
            "the top wrestler. Step 6: secure control. Lock around the "
            "waist and settle your weight; the reversal must end in "
            "control to score. Step 7: drill against pressure. Have the "
            "top wrestler drive harder each round; the switch feeds on "
            "exactly that."
        ),
        "key_points": [
            "The switch borrows the top wrestler's pressure - harder pressure, easier reversal.",
            "Sit through completely; a half switch is a flattened bottom wrestler.",
            "Grip the arm or waist through the motion to control their fall.",
            "Climb to the back as their momentum carries them over the trap.",
            "The reversal must end in control - position without control scores nothing.",
        ],
        "requirements": [
            "A partner applying realistic forward top pressure.",
            "Hip mobility for the full sit-through motion.",
            "Mat space for the climb-to-the-back finish.",
            "Timing work: switching on pressure, not on stillness.",
            "A coach confirming control at the finish - the reversal's scoring requirement.",
        ],
        "standards": [
            "Reversal scoring: 2 points UWW; 2 points NCAA (reversal).",
            "Switch mechanics follow standard coaching practice (Gable 1999).",
            "Control must be established for the reversal to score.",
        ],
        "citations": [CIT_UWW, CIT_NCAA, CIT_GABLE],
        "sig_lens": (
            "The Signature read: the switch is the Signature judo of the "
            "mat - the opponent's pressure becomes the Signature "
            "wrestler's propulsion. Push, and you are already behind him, "
            "hands upon the waist of your own momentum returned. To switch "
            "is to prove that every force carries its own reversal."
        ),
    },
    {
        "key": "sitout_turnin",
        "name": "The Sit-Out and Turn-In",
        "group": "Reversals and Escapes",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The sit-out and turn-in is the advanced bottom technique for "
            "the wrestler trapped under a tight top ride: the bottom "
            "wrestler sits out away from the top wrestler - hips to the "
            "mat, legs extended - creating space, then turns in to face "
            "the top wrestler, converting a breakdown into a neutral "
            "scramble or a reversal. It is the escape hatch when the "
            "stand-up is smothered: rather than rising into the top "
            "wrestler's chest, the bottom wrestler goes under and out, "
            "using hip movement to defeat the ride's pressure. The sit-out "
            "must be explosive - a slow sit-out is a turk (leg ride) "
            "waiting to happen - and the turn-in must keep the elbows in "
            "and the head up, because turning in carelessly offers the "
            "cement mixer. Chained with the switch and the stand-up, the "
            "sit-out completes the bottom wrestler's triple threat: up, "
            "through, or out - the top wrestler cannot cover all three."
        ),
        "how_it_works": (
            "Step 1: recognize the smother. When the top ride kills the "
            "stand-up, choose the sit-out - go under the pressure, not "
            "into it. Step 2: sit out explosively. Shoot the hips to the "
            "mat away from the top wrestler, legs extending, in one burst. "
            "Step 3: clear the grip. As the hips hit the mat, strip or "
            "slip the top wrestler's controlling grips. Step 4: turn in. "
            "Rotate to face the top wrestler, elbows tight, head up - "
            "never turn in with the head down. Step 5: win the scramble. "
            "From the facing position, attack: come up for the reversal, "
            "or separate to neutral. Step 6: chain the threat. Show the "
            "stand-up, then sit out when they cover it; show the sit-out, "
            "then switch when they follow. Step 7: drill the triple "
            "threat. Bottom rounds where the top wrestler doesn't know "
            "which escape is coming - up, through, or out."
        ),
        "key_points": [
            "The escape hatch when the stand-up is smothered: go under the pressure, not into it.",
            "Explosive sit-out; a slow one invites the turk leg ride.",
            "Turn in with elbows tight and head up - careless turn-ins feed the cement mixer.",
            "Converts breakdowns into scrambles the bottom wrestler can win.",
            "Completes the triple threat with the stand-up and switch: up, through, or out.",
        ],
        "requirements": [
            "Mastery of the stand-up and switch first - the sit-out is the third option.",
            "A partner riding tight top pressure that smothers basic escapes.",
            "Hip explosiveness for the sit-out burst.",
            "Scramble training: the turn-in leads to live positions, not set pieces.",
            "A coach policing head position on the turn-in.",
        ],
        "standards": [
            "Escape and reversal scoring per UWW and NCAA rules.",
            "Sit-out mechanics follow standard coaching practice (Gable 1999).",
            "Turn-in head position is coached as a safety fundamental.",
        ],
        "citations": [CIT_GABLE, CIT_UWW, CIT_NCAA],
        "sig_lens": (
            "The Signature read: the sit-out is the Signature trapdoor. "
            "Smothered beneath the ride, the Signature wrestler does not "
            "push against the ceiling - he opens the floor. Down and out, "
            "turn and face: the prisoner's cell becomes the duelist's "
            "ground. Escape is not always upward."
        ),
    },
    {
        "key": "suplex",
        "name": "The Suplex",
        "group": "Greco-Roman Throws",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The suplex is Greco-Roman wrestling's crown throw: from the "
            "clinch - typically the body lock or the reverse body lock - "
            "the wrestler arches backward and launches the opponent clean "
            "over in a grand-amplitude arc, scoring 5 points for a direct "
            "back-exposure throw under UWW rules and often ending the "
            "match by fall. It is the most spectacular and most demanding "
            "technique in wrestling, requiring a deep lock, total hip "
            "commitment, and a fearless back arch; the thrower literally "
            "throws themselves backward, trusting the arch to carry the "
            "opponent over. Entries include the body lock (both arms around "
            "the waist), the reverse body lock, and the front body lock off "
            "a defended attack. The suplex is drilled exhaustively on crash "
            "mats with expert partners before any live attempt, because a "
            "failed suplex surrenders the back and a mistimed one risks "
            "both wrestlers. Thrown correctly, it is the single most "
            "decisive motion in the sport."
        ),
        "how_it_works": (
            "Step 1: lock the body. Secure the body lock - both arms around "
            "the opponent's waist, hands locked, chest to chest, hips in. "
            "Step 2: load the hips. Get your hips below theirs, knees bent, "
            "the opponent's weight settled onto your body. Step 3: commit "
            "totally. There is no half suplex - decide and go. Step 4: "
            "arch back. Throw your head and shoulders backward, arching the "
            "whole back while extending the legs violently. Step 5: lift "
            "with the lock. The body lock lifts and guides as the arch "
            "carries the opponent up and over in the grand arc. Step 6: "
            "land in control. Come down maintaining the lock, chest to "
            "chest, ready for the fall. Step 7: earn it on the mats. Drill "
            "hundreds of arches on crash mats with a trusted partner "
            "before the first live attempt - the suplex is never improvised."
        ),
        "key_points": [
            "Body lock, hips below theirs, total commitment - there is no half suplex.",
            "The back arch launches the throw; the lock guides what the arch throws.",
            "5 points for the direct back-exposure grand amplitude (UWW) - the match decider.",
            "The most spectacular and most demanding technique in wrestling.",
            "Hundreds of crash-mat repetitions before any live attempt; never improvised.",
        ],
        "requirements": [
            "An expert partner and crash mats - non-negotiable for suplex training.",
            "A deep, practiced body lock; the throw cannot launch from a loose lock.",
            "Back, hip, and leg explosiveness for the loaded arch.",
            "A coach supervising all suplex drilling - the failure modes are severe.",
            "Neck and spinal conditioning; the arch loads the whole posterior chain.",
        ],
        "standards": [
            "UWW scoring: 5 points for grand-amplitude throws with direct danger position.",
            "Suplex training follows supervised crash-mat progression per coaching practice.",
            "Body-lock throws must remain within UWW legal-hold rules.",
        ],
        "citations": [CIT_UWW, CIT_GABLE],
        "sig_lens": (
            "The Signature read: the suplex is the Signature cataclysm. "
            "The clinch becomes the fault line, the arch the earthquake, "
            "and the opponent the mountain range rearranged. The Signature "
            "wrestler does not throw opponents; he renames the landscape "
            "they land in. Five points, and the map is redrawn."
        ),
    },
    {
        "key": "lateral_drop",
        "name": "The Lateral Drop",
        "group": "Greco-Roman Throws",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The lateral drop is the overhook's masterpiece throw: when the "
            "opponent drives hard into your overhook, you drop your weight "
            "laterally, block their near leg or hip with your body, and "
            "throw them sideways over your falling body - converting their "
            "forward pressure into a high-amplitude throw. It is the "
            "purest counter-throw in wrestling: you supply no force of "
            "your own, only the pivot, and the opponent's aggression does "
            "the throwing. The mechanics require exquisite timing - drop as "
            "their pressure peaks, not before - a tight overhook that "
            "steers their upper body, and a committed lateral fall that "
            "takes your own body out as the fulcrum. In Greco-Roman it is a "
            "staple counter; in freestyle it punishes the wrestler who "
            "bull-rushes the clinch. The lateral drop teaches wrestling's "
            "deepest lesson: the best throw is the one your opponent throws "
            "himself."
        ),
        "how_it_works": (
            "Step 1: own the overhook. Establish the tight overhook with "
            "downward pressure and wrist control. Step 2: invite the "
            "drive. Let the opponent push hard into the overhook - their "
            "pressure is the throw's engine. Step 3: time the peak. Wait "
            "for the instant their drive commits fully forward. Step 4: "
            "drop laterally. Drop your body weight sideways and down, "
            "blocking their near hip/leg with your body as the fulcrum. "
            "Step 5: steer with the overhook. Keep the overhook tight and "
            "guide their upper body over the fulcrum as you fall. Step 6: "
            "land in control. Come down maintaining the overhook, ready "
            "for the pin or exposure points. Step 7: drill the timing. "
            "Practice against partners driving at varied rhythms; the drop "
            "must match the pressure peak, never anticipate it."
        ),
        "key_points": [
            "The purest counter-throw: their pressure is the engine, you supply only the pivot.",
            "Drop as their drive peaks - early drops get sprawled on, late drops get run over.",
            "The tight overhook steers their upper body over your falling-body fulcrum.",
            "Greco-Roman staple and the freestyle answer to the clinch bull-rush.",
            "Wrestling's deepest lesson: the best throw is the one the opponent throws himself.",
        ],
        "requirements": [
            "A committed overhook - the throw cannot launch from a loose tie.",
            "Partners drilling varied-pressure drives into the overhook.",
            "Crash mats for learning the lateral fall before live counters.",
            "Timing training against unpredictable drive rhythms.",
            "A coach verifying the fulcrum position - body blocking hip, not just falling.",
        ],
        "standards": [
            "UWW scoring: amplitude and exposure decide 4 vs 5 points.",
            "Counter-throw mechanics follow standard coaching practice (Gable 1999).",
            "Lateral falls are drilled on crash mats before live execution.",
        ],
        "citations": [CIT_UWW, CIT_GABLE],
        "sig_lens": (
            "The Signature read: the lateral drop is the Signature mirror. "
            "The opponent charges and meets himself coming back - his "
            "fury, reflected and amplified, becomes his flight. The "
            "Signature wrestler lays the mirror at the exact angle of the "
            "charge and steps aside. Force, properly framed, defeats "
            "itself."
        ),
    },
    {
        "key": "firemans_carry",
        "name": "The Fireman Carry",
        "group": "Advanced Combinations",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The fireman's carry is the spectacular shoulder throw of "
            "freestyle wrestling: the wrestler drops to a knee, threads an "
            "arm between the opponent's legs to grip the far thigh, pulls "
            "the opponent's upper body across the shoulders, and dumps them "
            "over - carrying them like a fireman carries a rescued "
            "victim, hence the name. It is the definitive answer to the "
            "opponent who overhooks hard or leans heavy on the tie: their "
            "upper-body pressure becomes the load you carry and dump. The "
            "mechanics demand a deep knee drop (the carry launches from the "
            "mat), a tight grip on the far thigh, and a violent pull-down "
            "of the opponent's head and arm across the shoulders. Variations "
            "include the high fireman's (standing entry) and the crackdown "
            "finish. The fireman's carry scores big - grand amplitude when "
            "thrown clean - and it breaks opponents psychologically: being "
            "carried and dumped is humbling. Drill it on crash mats until "
            "the knee drop is fearless."
        ),
        "how_it_works": (
            "Step 1: read the pressure. Wait for the opponent to lean or "
            "overhook hard into the tie - their weight is your load. Step 2: "
            "drop the knee. Drop your near knee hard to the mat beside "
            "their foot, changing level completely. Step 3: thread the arm. "
            "Shoot your near arm between their legs and grip the far thigh "
            "tight. Step 4: pull across. With your other arm, pull their "
            "head and near arm down across your shoulders. Step 5: load "
            "and dump. Pop your hips up, loading them across your shoulders, "
            "then dump them over to the mat. Step 6: stay tight. Keep the "
            "thigh grip and the head pull through the dump so they cannot "
            "roll out. Step 7: drill fearlessly. Practice the knee drop on "
            "crash mats until dropping hard is instinct - hesitation kills "
            "the carry."
        ),
        "key_points": [
            "Their upper-body pressure becomes the load you carry and dump.",
            "Deep knee drop launches the carry; the entry starts at the mat.",
            "Thread between the legs to the far thigh - the grip is the steering.",
            "Pull the head and arm across the shoulders as the hips pop the load over.",
            "Grand amplitude when thrown clean; psychologically devastating when landed.",
        ],
        "requirements": [
            "A partner giving committed tie pressure to carry.",
            "Crash mats for learning the knee drop and dump.",
            "Knee protection and mat cleanliness for the hard knee drop.",
            "Hip explosiveness for the pop that loads the opponent.",
            "A coach checking the far-thigh grip depth - shallow grips lose the load.",
        ],
        "standards": [
            "UWW scoring: amplitude and exposure decide the throw's points.",
            "Fireman's carry mechanics follow standard coaching practice (Gable 1999).",
            "Knee-drop entries require clean mats to protect the dropping knee.",
        ],
        "citations": [CIT_UWW, CIT_GABLE],
        "sig_lens": (
            "The Signature read: the fireman's carry is the Signature "
            "rescue in reverse. The opponent leans in like a burning "
            "building leans on the fireman - and the Signature wrestler "
            "shoulders the whole structure and lays it gently, violently, "
            "on the mat. To be carried is to be conquered completely."
        ),
    },
    {
        "key": "cradle_series",
        "name": "The Cradle Series",
        "group": "Advanced Combinations",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The cradle is the pinning combination that folds the opponent "
            "like a pocketknife: the wrestler locks one arm around the "
            "opponent's head and the other around the near knee, joining "
            "the hands to form a closed loop - and squeezes, rocking the "
            "opponent onto their shoulders for the fall. The near-side "
            "cradle (head and near knee on the same side) and the far-side "
            "cradle (reaching across) are the two families, and the series "
            "chains them: near-side fails, switch to far-side; far-side "
            "stalls, rock back to near-side; the opponent sits up, take the "
            "crossface cradle. The cradle's genius is its completeness - "
            "head and knee locked together means the body cannot bridge, "
            "cannot turn, cannot breathe comfortably. Entries come from the "
            "front headlock, the crossface, the stand-up attempt, and the "
            "cement mixer roll. A locked cradle with rocking pressure ends "
            "matches at every level of the sport."
        ),
        "how_it_works": (
            "Step 1: capture head and knee. From the breakdown or headlock, "
            "wrap one arm around the opponent's head and the other around "
            "the near knee. Step 2: lock the hands. Join your hands - "
            "palm to palm - closing the loop around head and knee. Step 3: "
            "squeeze and rock. Squeeze the loop tight and rock the opponent "
            "onto their shoulders, driving with your legs. Step 4: stay "
            "tight. Keep your chest on them and the loop closed; the cradle "
            "pins by completeness, not by weight alone. Step 5: switch "
            "sides. If they fight the near-side, release and re-lock the "
            "far-side cradle without giving them space to recover. Step 6: "
            "chain the series. Near-side to far-side to crossface cradle - "
            "each failed lock becomes the next lock's entry. Step 7: drill "
            "the rock. Practice the squeeze-and-rock finish against "
            "bridging partners until the fall is a foregone conclusion."
        ),
        "key_points": [
            "Head and knee locked in one loop - the folded body cannot bridge or turn.",
            "Near-side and far-side are the two families; the series chains them without pause.",
            "Squeeze and rock with leg drive; completeness pins, not weight alone.",
            "Entries everywhere: front headlock, crossface, stand-up attempts, cement mixer.",
            "A locked cradle with rocking pressure ends matches at every level.",
        ],
        "requirements": [
            "Reliable breakdowns and front-headlock entries to start the series.",
            "A partner drilling bridging and sitting-up escapes from the lock.",
            "Arm and grip endurance for holding the closed loop.",
            "Instruction on the squeeze mechanics - pressure without panic.",
            "Timed pin-hold rounds from the locked cradle.",
        ],
        "standards": [
            "Pin/fall criteria follow UWW rules (shoulders held in danger) and NCAA rules.",
            "Cradle mechanics follow standard coaching practice (Gable 1999).",
            "The lock must remain a legal hold - no illegal pressure on joints.",
        ],
        "citations": [CIT_UWW, CIT_NCAA, CIT_GABLE],
        "sig_lens": (
            "The Signature read: the cradle is the Signature knot. Head "
            "to knee, the loop closed, the opponent folded into the "
            "smallest possible version of himself - the Signature wrestler "
            "ties the knot and the match is bound. Some knots are for "
            "sailing; this one is for finishing."
        ),
    },
    {
        "key": "ankle_lace",
        "name": "The Ankle Lace Turn",
        "group": "Advanced Combinations",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The ankle lace turn is the freestyle par terre turn built on "
            "the ankle: the top wrestler captures the opponent's foot, "
            "laces it with the legs in a tight figure-four around the "
            "ankle and shin, and uses the trapped foot as a short, brutal "
            "lever to turn the opponent through back exposure - 2 points "
            "per turn under UWW rules. Shorter than the leg lace's "
            "full-leg lever, the ankle lace is faster to lock and harder "
            "to feel coming; the turn is a sharp crank of the trapped "
            "ankle that rolls the whole body. It chains viciously - lace, "
            "turn, re-lace, turn - and specialists can end par terre "
            "periods with cascades of exposure points. The defense must "
            "keep the feet moving and never let the top wrestler isolate a "
            "foot; once the lace is locked deep, the turn is nearly "
            "automatic. The ankle lace is the par terre turn for the "
            "wrestler who hunts feet."
        ),
        "how_it_works": (
            "Step 1: hunt the foot. From top par terre, watch for the "
            "bottom wrestler's foot to isolate as they move. Step 2: "
            "capture fast. Seize the ankle before they can withdraw it - "
            "speed is the entry. Step 3: lace the figure-four. Weave your "
            "legs around their ankle and shin in the tight lace lock. "
            "Step 4: lever the turn. Crank the trapped ankle as a short "
            "lever, rolling their body through back exposure. Step 5: "
            "hold the lace. Finish the turn with the figure-four still "
            "locked, ready to chain. Step 6: re-lace and repeat. Adjust "
            "and turn again - each clean exposure is 2 points. Step 7: "
            "drill the hunt. Foot-isolation rounds: top wrestler may only "
            "score via the ankle lace, bottom wrestler keeps feet alive."
        ),
        "key_points": [
            "The trapped ankle is a short, brutal lever - faster to lock than the full leg lace.",
            "Speed is the entry: seize the foot before it withdraws.",
            "Each turn through back exposure scores 2 points (UWW); the lace chains.",
            "Defense is foot discipline - never let the top wrestler isolate a foot.",
            "The par terre turn for the wrestler who hunts feet.",
        ],
        "requirements": [
            "A partner drilling foot isolation and ankle-lace defense.",
            "Leg dexterity for the fast figure-four lace lock.",
            "Understanding of UWW exposure criteria for counting turns.",
            "Ankle and leg conditioning for the repeated levering.",
            "A coach enforcing legal lace mechanics - leverage, never joint cranks past range.",
        ],
        "standards": [
            "UWW scoring: 2 points per ankle-lace turn through danger position.",
            "Ankle lace mechanics follow standard coaching practice (Gable 1999).",
            "The lever must stay within legal-hold limits - no illegal joint manipulation.",
        ],
        "citations": [CIT_UWW, CIT_GABLE],
        "sig_lens": (
            "The Signature read: the ankle lace is the Signature trap for "
            "the careless foot. The smallest lever, the fastest knot - the "
            "foot strays once and the whole body pays the toll, turned and "
            "turned again. The Signature wrestler watches feet the way "
            "hawks watch fields."
        ),
    },
    {
        "key": "peterson_roll",
        "name": "The Peterson Roll",
        "group": "Advanced Combinations",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The Peterson roll is the bottom wrestler's granby-style "
            "reversal: trapped underneath, the bottom wrestler rolls "
            "shoulder-over-shoulder, threading the far arm through, and "
            "comes up on top - turning a breakdown into a reversal in one "
            "continuous rotation. Named for the Peterson wrestling family, "
            "it is the most athletic escape in the sport: the bottom "
            "wrestler somersaults under and through the top wrestler's "
            "pressure, emerging behind for the reversal points. The "
            "mechanics demand a committed shoulder roll (hesitation gets "
            "you flattened), a tight arm thread that captures the top "
            "wrestler's arm, and a finish that lands on top in control. "
            "It is the ultimate answer to the tight ride: when the top "
            "wrestler has everything covered, the Peterson goes underneath "
            "it all. Drilled on crash mats until the roll is fearless, it "
            "is the bottom technique that makes crowds gasp."
        ),
        "how_it_works": (
            "Step 1: recognize the trap. When the ride has your stand-up "
            "and switch covered, choose the roll - go under everything. "
            "Step 2: commit the shoulder. Drive one shoulder to the mat "
            "and initiate the shoulder-over-shoulder roll with total "
            "commitment. Step 3: thread the arm. As you roll, thread your "
            "far arm through, capturing the top wrestler's arm in the "
            "rotation. Step 4: stay tight. Keep your body compact through "
            "the roll - a loose roll is a flattened roll. Step 5: emerge "
            "on top. Complete the rotation and come up on top of the "
            "captured opponent. Step 6: secure control. Land in control "
            "with the arm captured; the reversal must end controlled to "
            "score. Step 7: drill fearlessly. Practice the roll on crash "
            "mats until commitment is total - the Peterson punishes "
            "hesitation and rewards courage."
        ),
        "key_points": [
            "The shoulder-over-shoulder roll goes under the entire ride - the ultimate trapdoor.",
            "Total commitment: a hesitant roll gets flattened; a committed one reverses.",
            "Thread the far arm through the roll to capture the top wrestler.",
            "Stay compact; looseness in the roll is position lost.",
            "The reversal must land in control - athleticism without control scores nothing.",
        ],
        "requirements": [
            "Crash mats for learning the roll before live attempts.",
            "A partner applying the tight ride the roll is designed to beat.",
            "Shoulder and neck conditioning for the repeated rolls.",
            "Mastery of basic bottom escapes first - the Peterson is the advanced answer.",
            "A coach confirming control at the landing - the reversal's scoring requirement.",
        ],
        "standards": [
            "Reversal scoring: 2 points UWW; 2 points NCAA.",
            "Peterson roll mechanics follow standard coaching practice (Gable 1999).",
            "Rolls are drilled on crash mats before live execution.",
        ],
        "citations": [CIT_GABLE, CIT_UWW, CIT_NCAA],
        "sig_lens": (
            "The Signature read: the Peterson roll is the Signature "
            "phoenix. Buried beneath the ride, the Signature wrestler "
            "does not dig upward - he rolls through the underworld and "
            "rises on the far side, on top, the trap become the triumph. "
            "From beneath everything, to above everything, in one "
            "rotation."
        ),
    },
    {
        "key": "chain_wrestling",
        "name": "Chain Wrestling: Setup Systems and Combination Attacks",
        "group": "Advanced Combinations",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Chain wrestling is the master system: no single technique "
            "thrown alone, but attacks linked in combinations where each "
            "move's most likely defense opens the next move's entry. The "
            "double leg's sprawl opens the cutback; the snap-down's posted "
            "hand opens the front headlock; the arm drag's turn opens the "
            "single leg; the underhook's whizzer opens the far-side attack. "
            "Elite wrestlers drill chains, not moves - double-to-single, "
            "snap-to-go-behind-to-headlock, tie-to-drag-to-double - until "
            "the second attack fires before the first one finishes. The "
            "system has three layers: setups (fakes, ties, and motion that "
            "manufacture reactions), primary attacks (the highest-"
            "percentage shot for the manufactured opening), and re-attacks "
            "(the pre-planned answer to each likely defense). Chain "
            "wrestling is why advanced wrestlers seem to score at will: "
            "they are not throwing techniques, they are running programs "
            "with branches for every defense. This record is the capstone "
            "of the ladder - the system that organizes all thirty-three "
            "techniques before it."
        ),
        "how_it_works": (
            "Step 1: pick the chain. Choose a primary attack and map its "
            "two most likely defenses (e.g., double leg: sprawl, whizzer). "
            "Step 2: build the setup. Design the fake, tie, or motion that "
            "manufactures the primary's opening. Step 3: drill the "
            "primary. Rep the first attack until it fires at full speed. "
            "Step 4: drill the branches. For each likely defense, drill "
            "the pre-planned re-attack: sprawl becomes cutback, posted "
            "hand becomes headlock, whizzer becomes far-side single. "
            "Step 5: run the chain live. Drill with a defending partner "
            "who chooses defenses randomly; fire the correct branch "
            "without pausing. Step 6: add the third link. Extend chains to "
            "three techniques: setup to primary to re-attack to counter-"
            "re-attack. Step 7: systematize the arsenal. Build chains for "
            "every position - neutral, top, bottom - until the whole "
            "match is programmed responses, not improvisation."
        ),
        "key_points": [
            "Every defense opens an entry: the chain converts the opponent's defense into your next attack.",
            "Three layers: setups manufacture reactions, primaries exploit them, re-attacks answer defenses.",
            "The second attack fires before the first finishes - chains are drilled, not improvised.",
            "Elite wrestlers run programs with branches; beginners throw single techniques.",
            "The capstone system: it organizes all thirty-three techniques in this database.",
        ],
        "requirements": [
            "Mastery of the individual techniques - chains are built from reliable links.",
            "A partner giving varied, realistic defenses for branch drilling.",
            "A written chain map: primary, likely defenses, and each branch's re-attack.",
            "Live chain rounds: the partner defends randomly, the wrestler branches correctly.",
            "Video review to verify the second attack truly fires without pause.",
        ],
        "standards": [
            "Combination systems follow standard coaching practice (Gable 1999).",
            "Chain drilling progresses from cooperative to fully live resistance.",
            "All linked techniques remain within UWW and NCAA legal-hold rules.",
        ],
        "citations": [CIT_GABLE, CIT_UWW, CIT_NCAA],
        "sig_lens": (
            "The Signature read: chain wrestling is the Signature grand "
            "strategy. Single techniques are battles; the chain is the "
            "campaign - every engagement planned, every retreat of the "
            "enemy mapped to the next advance. The Signature wrestler does "
            "not hope for openings; he manufactures them, harvests them, "
            "and has the next harvest already planted. This is the creed "
            "entire: no wasted motion, no isolated attack, everything "
            "connected."
        ),
    },
]
