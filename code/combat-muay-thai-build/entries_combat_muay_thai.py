#!/usr/bin/env python3
"""Entries for the Muay Thai Combat databases (combat batch 1, 2026-10-17).

Scope verified before authoring 2026-10-17: RAW check over the full manifest
plus every shard index title in jah-databases-data-1: zero 'combat-muay*'
slugs/names; zero Muay Thai combat technique catalog databases of this kind.
Dedupe gate check of all 68 planned titles (34 public + 34 Signature) vs the
whole exact index: zero collisions, zero refusals. ID prefixes JAH-CBMT- and
JAH-CBMTS- verified free in the manifest id_prefix values and every shard
index file (zero hits).

This build creates two NEW databases, 34 ladder-ordered records each:

  combat-muay-thai              - The Muay Thai Combat Database
                                  (public-harvest: real, fact-checked Muay
                                  Thai technique knowledge - the art of eight
                                  limbs: punches (mat), elbows (sok), knees
                                  (khao), kicks (tae, thip), clinch work
                                  (chap kho), sweeps and dumps (tad kha,
                                  thum), and conditioning methods - every
                                  record carrying the Thai name with
                                  translation, step-by-step body mechanics,
                                  key points, requirements, standards, and
                                  citations; standard references Delp C.
                                  Muay Thai Basics 2004; Delp C. Muay Thai:
                                  Advanced Thai Kickboxing Techniques 2006;
                                  Kraitus P, Kraitus P. Muay Thai: The Most
                                  Distinguished Art of Fighting 1988; IFMA
                                  rules; WMC rules)
  combat-muay-thai-signature    - The Muay Thai Combat Signature Database
                                  (his original Signature Eight-Limb Method:
                                  every limb a covenant of mechanics, the
                                  stance the oath of the feet, the guard
                                  the walls of the temple, the clinch the
                                  handshake of warriors; src signature,
                                  titles suffixed " (Signature Edition)",
                                  never presented as authentic public
                                  record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced): stance, footwork, guard,
basic punches, kicks, defense, bag work, and conditioning (foundations)
-> hooks, uppercuts, elbows, knees, clinch entry and control, low and
switch kicks, catches and counters (compounded) -> spinning techniques,
flying knee, clinch throws, sweeps, counter-timing, combination systems,
ringcraft, and the full fight camp (advanced).

ID prefixes: JAH-CBMT- (public) and JAH-CBMTS- (signature), verified free
in the manifest and in every shard index (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_muay_thai.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos before commit.

Civilian martial-arts sport instruction only. Nothing on neutralizing or
defeating military or defense-grade systems. Never the words "bat belt"
anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Eight-Limb Method: "
            "every limb a covenant of mechanics, the stance the oath of the "
            "feet, the guard the walls of the temple, the clinch the "
            "handshake of warriors. Clearly labeled Signature-made, never "
            "presented as authentic public record.")

CIT_DELP_BASICS = ("Delp C. Muay Thai Basics: Introductory Thai Boxing "
                   "Techniques. North Atlantic Books; 2004.")
CIT_DELP_ADV = ("Delp C. Muay Thai: Advanced Thai Kickboxing Techniques. "
                "Blue Snake Books; 2006.")
CIT_KRAITUS = ("Kraitus P, Kraitus P. Muay Thai: The Most Distinguished Art "
               "of Fighting. Soma Publishing; 1988.")
CIT_IFMA = ("International Federation of Muaythai Associations (IFMA). "
            "Rules of Muaythai Competition; current edition.")
CIT_WMC = ("World Muaythai Council (WMC). Muaythai Rules and Regulations; "
           "current edition.")
CIT_TRAD = ("Traditional Muay Thai gym lineage: techniques as taught in "
            "Thai training camps in the Bangkok stadium tradition.")

ENTRIES = [
    # ------------------------------------------------------- FOUNDATIONS
    {
        "key": "stance",
        "name": "Muay Thai Fighting Stance",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The fighting stance (thaa muay) is the home base of every Muay "
            "Thai technique. Feet sit roughly shoulder-width apart with the "
            "lead foot forward at about 45 degrees and the rear foot planted "
            "with the heel slightly raised so the fighter can pivot and "
            "push off. Weight rests close to even between the feet, knees "
            "soft, hips square enough to check kicks yet angled enough to "
            "hide the body. Hands ride at cheek level with the chin tucked "
            "behind the lead shoulder and the elbows tucked tight to the "
            "ribs. Nothing in Muay Thai works without this stance: every "
            "punch, kick, elbow, knee, and clinch entry starts here and "
            "returns here."
        ),
        "how_it_works": (
            "Stand with feet shoulder-width apart, then step your dominant "
            "side foot back about one shoulder width so the lead foot points "
            "roughly 45 degrees outward and the rear foot points forward. "
            "Raise the rear heel an inch off the floor so your weight can "
            "shift instantly. Bend the knees slightly and drop the hips so "
            "your center of gravity sits low and between your feet. Bring "
            "both hands to cheek level, knuckles facing forward, and tuck "
            "the chin down behind the lead shoulder. Pull the elbows in to "
            "guard the ribs and float the lead shoulder slightly forward. "
            "From here you bounce lightly on the balls of the feet, never "
            "crossing the feet and never standing flat-footed. The mechanics "
            "work because the staggered base gives two planes of movement: "
            "forward pressure for punches and teeps, and hip clearance for "
            "the roundhouse kick. A stance that is too square leaves the "
            "body open to kicks; a stance that is too sideways traps the "
            "hips and kills the kick."
        ),
        "key_points": [
            "The stance is the first technique and the last correction: when anything breaks down, the fix almost always starts at the feet.",
            "Lead foot at 45 degrees and a raised rear heel make the stance mobile in every direction instead of rooted in place.",
            "Weight close to 50-50 keeps both the jab and the rear kick honest - a fighter leaning on the front foot cannot check or teep.",
            "Hands at cheek level, chin tucked, elbows in: the guard lives inside the stance, not bolted on afterward.",
            "A low center of gravity between the feet is what lets a fighter absorb a kick and stay upright instead of being bowled over.",
        ],
        "requirements": [
            "Feet roughly shoulder-width apart, lead foot at about 45 degrees, rear heel slightly raised.",
            "Knees soft and hips dropped so the center of gravity sits low between the feet.",
            "Hands at cheek level with the chin tucked behind the lead shoulder.",
            "Elbows tucked to the ribs, guarding the body without squeezing the arms dead.",
            "Light bounce on the balls of the feet with the feet never crossing and never planted flat.",
        ],
        "standards": [
            "Orthodox (left foot forward) and southpaw (right foot forward) are both standard; fighters pick the lead that matches their dominant rear power side.",
            "IFMA and WMC competition rules require the bout to open from a standing guard - the stance is the legal fighting base.",
            "Traditional Thai camps teach the stance before any strike: weeks of stance and footwork precede pad work for beginners.",
        ],
        "citations": [CIT_DELP_BASICS, CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the stance is the oath of the feet - a promise "
            "the body makes to the ground before a single strike is thrown. "
            "In the Signature Eight-Limb Method, the stance is graded first "
            "and corrected last."
        ),
    },
    {
        "key": "footwork",
        "name": "Muay Thai Footwork Basics",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Footwork is how the stance travels. Muay Thai footwork moves in "
            "short, gliding steps that keep the fighting base intact: the "
            "lead foot moves first when advancing, the rear foot moves first "
            "when retreating, and the feet never cross and never come "
            "together. A standard ring is about six meters square, and a "
            "fighter crosses it in controlled steps rather than leaps, "
            "staying balanced enough to strike or defend at any instant. "
            "Good footwork decides range - the distance at which each of the "
            "eight limbs can reach - and range decides everything in Muay "
            "Thai."
        ),
        "how_it_works": (
            "From the fighting stance, advance by sliding the lead foot "
            "forward six to ten inches and then bringing the rear foot the "
            "same distance so the stance width is restored. Retreat by "
            "moving the rear foot first, then the lead foot. Sidestep by "
            "moving the foot on the side you are going to, then closing the "
            "other foot back into stance. Pivot by turning on the ball of "
            "the lead foot to change angle without giving up base. Every "
            "step is a glide, not a hop: the feet stay low, the head stays "
            "level, and the guard stays up. The mechanics work because the "
            "base never narrows or crosses, so the hips stay loaded for a "
            "kick and the weight stays centered for a check. Common faults "
            "are crossing the feet (which kills balance), stepping too "
            "wide (which freezes the hips), and bouncing the head (which "
            "telegraphs movement)."
        ),
        "key_points": [
            "Footwork is the delivery system for all eight limbs - a great punch with bad feet never lands.",
            "Lead foot leads when going forward, rear foot leads when going back; the stance shape survives every step.",
            "Feet that cross or come together delete the base and the fighter is defenseless for a full beat.",
            "Small gliding steps beat big leaps: the head stays level and the guard stays honest.",
            "Controlling range with the feet is safer than controlling it with the face.",
        ],
        "requirements": [
            "Maintain the stance width through every step - feet never cross, never touch.",
            "Glide low with the head level; no hopping and no bouncing the chin up and down.",
            "Keep the guard up and the weight centered while moving in any direction.",
            "Practice the four moves: advance, retreat, sidestep, and pivot on the lead foot.",
            "Stay able to throw or check at any point in the step - if you cannot, the step was too big.",
        ],
        "standards": [
            "Competition rings are approximately 6.1 meters square; footwork must function in that bounded space.",
            "Traditional camps drill footwork on the spot and across the ring before any combination work.",
            "IFMA rules penalize passivity - footwork must drive engagement, not runaway.",
        ],
        "citations": [CIT_DELP_BASICS, CIT_KRAITUS, CIT_IFMA],
        "sig_lens": (
            "Signature lens: footwork is the silent limb - the ninth limb "
            "that carries the other eight. In the Signature Eight-Limb "
            "Method, the fighter who owns the floor owns the fight."
        ),
    },
    {
        "key": "guard",
        "name": "The Muay Thai High Guard",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The high guard is the defensive shell of Muay Thai: both gloves "
            "held at cheek or temple level, forearms vertical in front of "
            "the face, chin tucked behind the lead shoulder, and elbows "
            "tucked tight to the ribs. Unlike a boxing guard it sits "
            "slightly higher and more forward, because it must also catch "
            "elbows and high kicks and collapse quickly into a clinch. The "
            "guard is active, not a wall: it parries, catches, and redirects "
            "while the eyes stay open and watching over the top of the "
            "gloves."
        ),
        "how_it_works": (
            "Raise both gloves to cheek level with the knuckles pointing "
            "forward and the palms facing each other. Stack the forearms "
            "vertically so they form a shield in front of the nose and "
            "mouth, leaving the eyes a clear lane over the top of the "
            "gloves. Drop the chin and roll the lead shoulder forward so "
            "the jaw hides behind the shoulder and glove. Pin the elbows "
            "against the floating ribs so a body kick meets bone and "
            "muscle, not open space. Keep a fist-width gap between the "
            "gloves and the face - the guard absorbs by giving slightly, "
            "not by pressing into your own nose. The mechanics work "
            "because the forearms and gloves present hard, bony surfaces "
            "at the exact heights where punches, elbows, and high kicks "
            "arrive, while the tucked chin shortens the knockout lever of "
            "the jaw."
        ),
        "key_points": [
            "The high guard defends the head, the tucked elbows defend the body - the two halves work as one shell.",
            "Eyes stay open over the top of the gloves; a guard you hide behind is a blindfold.",
            "A fist-width gap between gloves and face turns the guard into a shock absorber instead of a second impact.",
            "The Muay Thai guard sits higher and more forward than a boxing guard because elbows and high kicks must be caught too.",
            "A dropping guard is the first sign of fatigue, which is why conditioning and the guard are taught together.",
        ],
        "requirements": [
            "Gloves at cheek or temple level, forearms vertical, knuckles forward.",
            "Chin tucked behind the lead shoulder with eyes watching over the gloves.",
            "Elbows pinned to the ribs, sealing the body against kicks and knees.",
            "Fist-width space between gloves and face to absorb impact.",
            "Guard returns to position after every single strike - no admiring your work.",
        ],
        "standards": [
            "Gloves in competition are 10 oz for most weight classes; the guard is built around gloved forearms.",
            "IFMA and WMC rules prohibit holding the ropes for defense - the guard must work in open space.",
            "Traditional instruction pairs the guard with chin-tuck drills from the first week of training.",
        ],
        "citations": [CIT_DELP_BASICS, CIT_KRAITUS, CIT_WMC],
        "sig_lens": (
            "Signature lens: the guard is the walls of the temple - built "
            "before the treasures inside are ever shown. In the Signature "
            "Eight-Limb Method, the guard is inspected every round like a "
            "fortress wall."
        ),
    },
    {
        "key": "jab",
        "name": "The Jab (Mat Trong)",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The jab (mat trong, the straight lead punch) is the most thrown "
            "punch in Muay Thai. Fired straight from the lead shoulder to "
            "the target, it measures distance, sets up power strikes, "
            "interrupts the opponent's rhythm, and scores. A proper jab "
            "snaps out along the centerline and snaps straight back to the "
            "guard, with the shoulder rolling forward to protect the chin "
            "and the rear hand glued to the cheek. It is a range-finder, a "
            "blinder, and a setup tool before it is ever a knockout punch."
        ),
        "how_it_works": (
            "From the stance, extend the lead hand straight toward the "
            "target, rotating the fist a quarter turn so the knuckles land "
            "flat. Step or shift the weight slightly forward as the punch "
            "extends, keeping the rear hand tight to the cheek. Roll the "
            "lead shoulder up to shield the chin at full extension. Snap "
            "the punch back along the same line the instant it lands - the "
            "return is half the technique. The mechanics work because the "
            "shortest path between two points is a straight line: the jab "
            "arrives faster than any other strike and costs the least "
            "energy, while the shoulder roll and fast return keep the "
            "puncher covered. Common faults are dropping the rear hand, "
            "leaning the head past the lead knee, and pushing the punch "
            "instead of snapping it."
        ),
        "key_points": [
            "The jab is the measuring stick of the fight - every combination and every kick starts with knowing the range.",
            "Speed and return beat power: a jab that comes back slow gets countered.",
            "The lead shoulder rolls up to guard the chin at full extension, making the jab its own defense.",
            "Doubling and tripling the jab (two or three in a row) breaks an opponent's timing and opens the cross.",
            "A jab thrown without footwork is an arm punch - the step gives it weight.",
        ],
        "requirements": [
            "Straight line from shoulder to target along the centerline, fist rotating to land flat.",
            "Rear hand stays glued to the cheek for the entire punch.",
            "Lead shoulder rolls forward to shield the chin at extension.",
            "Immediate snap-back to the guard along the same line.",
            "Small forward weight shift or step with the punch, never a lean past the lead knee.",
        ],
        "standards": [
            "Mat trong (straight punch) is the first punch taught in every traditional Thai camp.",
            "Judges score clean jabs; IFMA scoring rewards effective striking including clean lead punches.",
            "Hand wraps and 10 oz gloves are the standard striking surface for the jab in training and bouts.",
        ],
        "citations": [CIT_DELP_BASICS, CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the jab is the scout of the eight limbs - it "
            "goes ahead, reports the distance, and returns alive. In the "
            "Signature Eight-Limb Method, no army advances without its "
            "scout."
        ),
    },
    {
        "key": "parry_slip",
        "name": "Parry and Slip Defense in Muay Thai",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Parrying and slipping are the two head-movement defenses of Muay "
            "Thai. A parry redirects an incoming punch with a short, sharp "
            "tap of the glove, knocking it off the centerline by inches. A "
            "slip moves the head itself just off the line of the punch, "
            "letting it pass through empty air. Both keep the fighter in "
            "range to counter instead of backing away, and both cost far "
            "less energy than blocking with the arms. In Muay Thai they are "
            "used more sparingly than in boxing, because slipping into a "
            "knee or elbow is a real risk - so the movements stay small, "
            "tight, and always back to guard."
        ),
        "how_it_works": (
            "To parry a jab, tap the outside of the incoming glove with "
            "your rear glove using a short downward-outward motion of two "
            "to three inches, then snap the hand home. To parry a cross, "
            "use the lead hand the same way. To slip a jab, bend slightly "
            "at the knees and shift the head six inches to the outside, "
            "keeping the eyes on the opponent and the hands up. To slip a "
            "cross, move the head to the inside the same small amount. The "
            "mechanics work because a punch needs the centerline: moving "
            "the head or the punch just a few inches off that line deletes "
            "the impact while keeping you in countering range. The golden "
            "rule in Muay Thai is small: big slips and wild parries open "
            "you to the elbows and knees that boxing never has to fear."
        ),
        "key_points": [
            "Inches beat feet: a parry or slip moves the minimum distance that deletes the punch.",
            "Both defenses keep you in range to answer back, which is the whole point of not retreating.",
            "Hands stay up through the slip - the head moves, the guard does not drop.",
            "In Muay Thai, slips stay shallow because the head is also a target for knees and elbows.",
            "Every parry and slip ends with the guard rebuilt; a defense that leaves you open is a failed defense.",
        ],
        "requirements": [
            "Parry with a short 2-3 inch tap that redirects the punch off the centerline.",
            "Slip the head about six inches off line with bent knees, never bending at the waist.",
            "Keep eyes on the opponent through the entire defensive motion.",
            "Keep both hands in guard position while the head moves.",
            "Return to stance and guard immediately, ready to counter.",
        ],
        "standards": [
            "Parrying is legal and scored as effective defense under IFMA and WMC judging criteria.",
            "Traditional camps drill parry-and-return on the pads: every defensive rep ends with a counter.",
            "Head movement is taught only after the guard is solid - defense layers on defense.",
        ],
        "citations": [CIT_DELP_BASICS, CIT_DELP_ADV, CIT_IFMA],
        "sig_lens": (
            "Signature lens: the parry is the diplomat and the slip is the "
            "ghost - one negotiates the punch aside, the other was never "
            "there. In the Signature Eight-Limb Method, the smallest move "
            "that works is the best move."
        ),
    },
    {
        "key": "shadowboxing",
        "name": "Shadowboxing (Lom Muay)",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Shadowboxing (lom muay, literally boxing the wind) is solo "
            "practice of Muay Thai technique against an imaginary opponent. "
            "Fighters throw full combinations - punches, elbows, knees, "
            "kicks, and defensive moves - at full speed with full form but "
            "without contact, usually in three-minute rounds with one-minute "
            "rests to mirror a bout. It is the laboratory of Muay Thai: the "
            "place where new techniques are installed, footwork is drilled, "
            "and fighters visualize real opponents. Every Thai camp opens "
            "training with shadowboxing, and it never stops being useful, "
            "from the first week to the championship camp."
        ),
        "how_it_works": (
            "Set a timer for three-minute rounds with one-minute rests. "
            "Round one is slow and technical: stance, footwork, and single "
            "strikes thrown with perfect form at half speed. Round two "
            "builds combinations at increasing speed, adding head movement "
            "and checks as if answering an opponent. Round three is fight "
            "speed: full combinations, level changes, clinch entries, and "
            "defensive reactions, all thrown with intent but zero contact. "
            "Watch your form in a mirror or record it - shadowboxing only "
            "works if the technique is honest, because there is no bag or "
            "pad to give feedback. The mechanics work because thousands of "
            "perfect repetitions wire the movement patterns into muscle "
            "memory, and the visualization trains the eyes and timing "
            "without the damage of sparring."
        ),
        "key_points": [
            "Shadowboxing is where technique is installed before it is ever tested on equipment or partners.",
            "Three-minute rounds with one-minute rests condition the exact energy system a fight uses.",
            "The mirror is the coach: form must be honest because nothing pushes back.",
            "Visualization matters - picture a real opponent answering, and your defense sharpens with your offense.",
            "It is the safest high-volume training in Muay Thai: full speed, full intent, zero impact.",
        ],
        "requirements": [
            "Three-minute rounds with one-minute rests, matching bout structure.",
            "Full technique at real speed - no lazy arm punches or half kicks.",
            "Include defense in every round: slips, parries, checks, and clinch entries.",
            "Use a mirror or recording to audit form; fix what you see.",
            "Warm up into it: technical slow rounds before fight-speed rounds.",
        ],
        "standards": [
            "Lom muay is the traditional opening of every Thai camp training session.",
            "Bouts run 3-minute rounds (5 rounds professional, 3 amateur); shadowboxing mirrors this exactly.",
            "IFMA amateur competition uses 3 rounds; training rounds match the competition format.",
        ],
        "citations": [CIT_DELP_BASICS, CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: shadowboxing is the fighter rehearsing before "
            "an audience of one - the mirror. In the Signature Eight-Limb "
            "Method, the invisible opponent is the strictest teacher."
        ),
    },
    {
        "key": "cross",
        "name": "The Cross (Mat Wiang San)",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The cross (mat wiang san, the straight rear punch) is the power "
            "punch of the hands in Muay Thai. Thrown straight down the "
            "centerline from the rear shoulder, it carries the rotation of "
            "the hips and the drive of the rear leg, making it the hardest "
            "punch in the basic arsenal. It almost never travels alone: the "
            "jab-cross (one-two) is the most drilled combination in the "
            "sport, with the jab opening the guard and the cross punishing "
            "through the opening. A proper cross pivots the rear foot, turns "
            "the hips fully, and snaps back to guard as fast as it left."
        ),
        "how_it_works": (
            "From the stance, pivot the rear foot inward on the ball of the "
            "foot as the rear hip drives forward. Extend the rear hand "
            "straight along the centerline, rotating the fist to land flat, "
            "while the lead hand stays glued to the cheek and the chin "
            "tucks behind the lead shoulder. Turn the hips and shoulders "
            "fully so the rear shoulder finishes where the lead shoulder "
            "started. Snap the hand straight back to the guard along the "
            "same line. The mechanics work because the punch is the end of "
            "a kinetic chain: rear foot pivot drives the hip, the hip "
            "rotates the torso, and the torso whips the arm, stacking "
            "bodyweight behind the fist. Common faults are arm-punching "
            "without the hip, dropping the lead hand, and leaning forward "
            "past the lead knee instead of rotating."
        ),
        "key_points": [
            "The cross is a hip punch that happens to use the hand - power comes from rotation, not the arm.",
            "The rear-foot pivot is the ignition: no pivot, no hip, no power.",
            "It pairs with the jab as the one-two, the most fundamental combination in striking.",
            "The lead hand must stay home - the classic knockout in gyms is a cross landing while the lead hand drops.",
            "Snap-back is mandatory: a cross left hanging is an invitation to be countered.",
        ],
        "requirements": [
            "Rear foot pivots on the ball, driving the rear hip forward with the punch.",
            "Full hip and shoulder rotation finishing with the rear shoulder forward.",
            "Straight centerline path, fist rotating to land flat on the knuckles.",
            "Lead hand glued to the cheek and chin tucked for the entire punch.",
            "Immediate return to guard along the same line the punch traveled.",
        ],
        "standards": [
            "Mat wiang (swinging/straight rear punch family) is core curriculum in traditional Thai instruction.",
            "Clean crosses score heavily under IFMA/WMC judging as effective power punching.",
            "Pad holders call the one-two as the default beginner combination in every Thai camp.",
        ],
        "citations": [CIT_DELP_BASICS, CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the cross is the thunder after the jab's "
            "lightning - the scout reports, the heavy artillery answers. "
            "In the Signature Eight-Limb Method, the one-two is the first "
            "sentence every fighter learns to speak."
        ),
    },
    {
        "key": "roundhouse",
        "name": "Roundhouse Kick Mechanics (Tae Tad)",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The roundhouse kick (tae tad) is the signature weapon of Muay "
            "Thai and the highest-scoring strike in the sport. Thrown with "
            "the shin - never the foot - it swings in a horizontal arc "
            "powered by a full pivot of the support foot and a violent "
            "rotation of the hips, landing on the ribs, arms, legs, or head. "
            "Judges reward it above all other strikes: a clean roundhouse "
            "that moves the opponent visibly can decide a round by itself. "
            "The kick is thrown in three beats - step, pivot, whip - and the "
            "supporting leg's pivot is what unlocks the hips."
        ),
        "how_it_works": (
            "From the stance, take a small step outward with the lead foot "
            "at about 45 degrees to open the hips. Pivot hard on the ball "
            "of the support foot, turning it 90 degrees or more so the heel "
            "points at the target, while the kicking hip rolls over and "
            "drives through. Swing the leg in a horizontal arc with the knee "
            "slightly bent, striking with the lower shin, and whip the "
            "same-side arm down past the hip for counterbalance as the "
            "opposite hand guards the face. Follow through the target - the "
            "kick lands through, not at - then rechamber by reversing the "
            "motion and returning to stance. The mechanics work because the "
            "support-foot pivot frees the hip to rotate fully, turning the "
            "whole body into a swinging bat with the shin as the barrel. "
            "Kicking with the foot instead of the shin, failing to pivot, "
            "and dropping both hands are the three classic beginner faults."
        ),
        "key_points": [
            "The shin is the weapon, not the foot: shin-on-body is the defining impact of Muay Thai.",
            "The support-foot pivot is the whole kick - without it the hips lock and the kick becomes an arm-less slap.",
            "Judges score the roundhouse highest: visible effect on the opponent wins rounds.",
            "The same-side arm swings down for balance while the other hand stays glued to the face.",
            "Follow through the target: the kick is thrown through the opponent, not at the surface.",
        ],
        "requirements": [
            "Small 45-degree step to open the hips before the kick fires.",
            "Full pivot on the ball of the support foot, heel turning toward the target.",
            "Hip rolls over completely with the leg swinging in a horizontal arc.",
            "Contact with the lower shin, knee slightly bent at impact.",
            "Same-side arm swings down, opposite hand guards the face, then rechamber to stance.",
        ],
        "standards": [
            "Tae tad is the highest-scoring strike under traditional Thai judging criteria and IFMA scoring.",
            "Contact must be with the shin or foot; strikes with the knee to a grounded opponent are fouls.",
            "Thai camps drill the pivot separately - hundreds of pivots - before full kicks are allowed.",
        ],
        "citations": [CIT_DELP_BASICS, CIT_KRAITUS, CIT_IFMA],
        "sig_lens": (
            "Signature lens: the roundhouse is the broadsword of the eight "
            "limbs - the weapon the art is known by. In the Signature "
            "Eight-Limb Method, the pivot is the oath and the shin is the "
            "signature."
        ),
    },
    {
        "key": "teep",
        "name": "The Teep Front Push Kick (Thip Trong)",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The teep (thip trong, the straight front push kick) is Muay "
            "Thai's long-range stop sign. Thrust straight from the rear or "
            "lead leg with the ball of the foot into the opponent's hips, "
            "thigh, or torso, it halts forward pressure, breaks rhythm, "
            "manages distance, and scores. Fighters call it the jab of the "
            "legs: fast, cheap, and constantly in the opponent's face - or "
            "rather, in their stomach. A sharp teep can knock a rushing "
            "opponent backward off their feet, and a steady diet of teeps "
            "makes every other weapon land easier."
        ),
        "how_it_works": (
            "From the stance, lift the knee of the kicking leg straight up "
            "toward the chest, keeping the support leg slightly bent. Thrust "
            "the foot forward and slightly downward by extending the hip "
            "and knee together, striking with the ball of the foot while "
            "the toes pull back. Lean the torso slightly back and push the "
            "same-side hand down past the hip for balance as the opposite "
            "hand guards. Drive through the target with the hips, then snap "
            "the foot straight back to the ground and reset the stance. The "
            "mechanics work because the teep is a piston, not a swing: the "
            "knee lift chambers the leg and the hip extension fires it "
            "straight, transferring bodyweight forward into the push. "
            "Common faults are leaning forward into the kick (which kills "
            "the push), striking with flat toes, and dropping both hands."
        ),
        "key_points": [
            "The teep is distance management made physical: it puts the opponent exactly where you want them.",
            "It is the cheapest high-value strike in the sport - low energy, low risk, constant reward.",
            "The ball of the foot is the striking surface; toes pulled back, ankle locked.",
            "A rear teep stops a rush; a lead teep (the jab of the legs) sets up everything.",
            "Like the jab, it must snap back instantly - a teep left hanging gets caught and swept.",
        ],
        "requirements": [
            "Knee lifts straight to the chest to chamber before the thrust.",
            "Hip and knee extend together, striking with the ball of the foot.",
            "Torso leans slightly back with the same-side hand swinging down for balance.",
            "Opposite hand stays at the guard throughout the kick.",
            "Foot snaps straight back to stance the instant the push lands.",
        ],
        "standards": [
            "Thip is a core scoring technique; teeps to the body score under IFMA and WMC rules.",
            "Pushing with an extended leg to off-balance is legal; holding the leg and striking is a separate technique with its own rules.",
            "Traditional camps drill the teep against a partner's advance to teach timing over power.",
        ],
        "citations": [CIT_DELP_BASICS, CIT_KRAITUS, CIT_IFMA],
        "sig_lens": (
            "Signature lens: the teep is the gatekeeper of the temple - no "
            "one enters without answering. In the Signature Eight-Limb "
            "Method, the fighter who controls the gate controls the fight."
        ),
    },
    {
        "key": "check",
        "name": "Checking Kicks (Bang)",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Checking (bang) is the primary defense against low kicks in "
            "Muay Thai: the defender lifts the lead leg, knee bent and "
            "pointed at the incoming kick, so the attacker's shin crashes "
            "into the defender's raised shin instead of the thigh. A clean "
            "check turns the attacker's own weapon against them - kicking a "
            "checked shin hurts the kicker more than the defender. Because "
            "low kicks are thrown in volume in Muay Thai, the check is as "
            "fundamental as the guard: no fighter survives a bout without "
            "it, and the raised shin is often the first thing an opponent "
            "tests."
        ),
        "how_it_works": (
            "As the low kick comes, shift the weight to the rear leg and "
            "lift the lead knee up and slightly outward, shin vertical, "
            "knee pointed toward the incoming kick. Turn the hip slightly "
            "so the hard outer edge of the shin faces the impact. Keep the "
            "guard up and the eyes on the opponent - the check is a leg "
            "move, not a flinch. Meet the kick with the upper half of your "
            "shin, then drop the leg straight back to stance. The mechanics "
            "work because bone meets bone at an angle: the raised shin "
            "presents its hardest edge while the attacker's shin lands on "
            "its flat, and the attacker's momentum does the damage to "
            "themselves. Common faults are lifting the leg too late, "
            "turning the shin flat to the kick, and hopping backward "
            "instead of checking."
        ),
        "key_points": [
            "A good check punishes the kicker: their shin takes the worst of a bone-on-bone collision.",
            "Timing beats speed - the check must be up before the kick arrives, so reading the hip is everything.",
            "The outer edge of the raised shin is the shield; a flat shin is a target.",
            "Weight shifts to the rear leg first; a check thrown off a loaded lead leg is slow and weak.",
            "Checking is a scoring defense: judges notice a fighter whose kicks keep dying on a raised shin.",
        ],
        "requirements": [
            "Shift weight to the rear leg and lift the lead knee with the shin vertical.",
            "Point the knee at the incoming kick with the hip turned to present the shin's outer edge.",
            "Keep the guard up and eyes on the opponent through the check.",
            "Meet the kick with the upper half of the shin, then drop straight back to stance.",
            "Check early by reading the hip - waiting for the shin means waiting too long.",
        ],
        "standards": [
            "Bang (blocking with the shin) is the standard low-kick defense taught in all Thai camps.",
            "IFMA/WMC scoring credits effective defense; repeated checked kicks score for no one.",
            "Conditioning the shins (see Shin and Core Conditioning Basics) is paired with check drills.",
        ],
        "citations": [CIT_DELP_BASICS, CIT_DELP_ADV, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the check is the shield wall raising its edge "
            "to meet the axe. In the Signature Eight-Limb Method, the best "
            "defense wounds the attack."
        ),
    },
    {
        "key": "heavy_bag",
        "name": "Heavy Bag Training for Muay Thai",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Heavy bag training is where Muay Thai technique becomes power. "
            "Fighters work the bag in three-minute rounds, throwing full "
            "combinations of punches, elbows, knees, and kicks at a heavy "
            "suspended bag, building striking power, conditioning the shins "
            "and knuckles, and drilling the cardio to fight hard for every "
            "round. The bag gives honest feedback: a punch thrown with the "
            "arm barely moves it, while a punch thrown with the hips makes "
            "it jump. Bag rounds also teach the fighter to keep the guard "
            "up and keep moving when tired, which is exactly what a fight "
            "demands."
        ),
        "how_it_works": (
            "Wrap the hands, glove up, and set three-minute rounds with "
            "one-minute rests. Round one is technical: single strikes and "
            "basic combinations at moderate power, focusing on form - "
            "pivots, hip turn, guard return. Rounds two and three build "
            "power and volume: full combinations, kicks with full hip "
            "commitment, and clinch knees against the bag. Final rounds are "
            "conditioning: nonstop output, 10-second sprint bursts, and "
            "working while tired. Move around the bag as you strike, never "
            "standing flat in front of it, and keep the guard up between "
            "combinations. The mechanics work because the bag's mass "
            "resists the strike, forcing the body to recruit the full "
            "kinetic chain; over weeks the shins, knuckles, and core adapt "
            "to real impact. Common faults are arm-punching, standing "
            "still, and dropping the hands when fatigued."
        ),
        "key_points": [
            "The bag is the truth-teller: only hip-driven strikes move it, so it grades every punch and kick.",
            "Three-minute rounds with one-minute rests train the exact work-rest cycle of a bout.",
            "Power comes from form at speed; swinging wildly at the bag builds bad habits, not knockouts.",
            "Move around the bag constantly - footwork and angles are trained here, not just impact.",
            "Bag work conditions the weapons: shins, knuckles, and core harden against real resistance.",
        ],
        "requirements": [
            "Hands wrapped and gloved before touching the bag, every session.",
            "Three-minute rounds with one-minute rests, technical early rounds before power rounds.",
            "Full combinations of all eight limbs, not just punches.",
            "Constant movement around the bag with the guard up between strikes.",
            "Sprint bursts in late rounds to train output under fatigue.",
        ],
        "standards": [
            "Bag rounds mirror bout structure: 3-minute rounds, 5 rounds professional, 3 amateur.",
            "Thai camps typically program 3-5 bag rounds daily inside a two-session training day.",
            "Wraps are mandatory under gloves in training; bare-knuckle bag work is not standard practice.",
        ],
        "citations": [CIT_DELP_BASICS, CIT_TRAD, CIT_IFMA],
        "sig_lens": (
            "Signature lens: the heavy bag is the anvil and the fighter is "
            "the hammer - every round forges the weapons harder. In the "
            "Signature Eight-Limb Method, the bag never lies and never "
            "forgives."
        ),
    },
    {
        "key": "conditioning",
        "name": "Shin and Core Conditioning Basics",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Shin and core conditioning is the body-hardening foundation of "
            "Muay Thai. Fighters condition the shins by kicking pads and "
            "the heavy bag in gradually increasing volume, so the bone "
            "densifies and the nerves desensitize over months of honest "
            "work; there are no shortcuts, only progressive overload. Core "
            "conditioning - sit-ups, leg raises, planks, and medicine-ball "
            "work - builds the armor that absorbs body kicks, knees, and "
            "the clinch grind. A fighter with unconditioned shins cannot "
            "throw or check kicks at full power, and a fighter with a soft "
            "core folds under body attack."
        ),
        "how_it_works": (
            "Condition the shins by kicking the heavy bag and Thai pads "
            "with the shin, starting at moderate volume (for example three "
            "rounds of kicks) and adding roughly ten percent more kicks "
            "per week. Kick through the target with full hip turn - "
            "conditioning only works with real technique. Between sessions, "
            "rest the shins; microdamage needs recovery to remodel into "
            "denser bone. Condition the core daily: sets of sit-ups, "
            "hanging leg raises, planks, and rotational work, plus taking "
            "controlled body shots on the pads to learn to brace. The "
            "mechanics work through progressive adaptation: repeated "
            "sub-maximal impact stimulates bone remodeling and nerve "
            "desensitization, while core training builds the muscular "
            "corset that protects the organs. Never kick trees, bottles, "
            "or other absurdly hard objects - that is how shins break, not "
            "how they harden."
        ),
        "key_points": [
            "Shin conditioning is measured in months, not days - progressive overload with real technique is the only method.",
            "Bone remodels under repeated sub-maximal impact; rest days are when the hardening actually happens.",
            "The core is the body's armor: body kicks and knees are survived by muscle, not by willpower.",
            "Conditioning without technique is just damage; kick correctly and the bag does the teaching.",
            "There are no shortcuts - anyone selling instant shin hardening is selling injury.",
        ],
        "requirements": [
            "Kick pads and heavy bag with the shin in progressively increasing weekly volume (about +10% per week).",
            "Full technique on every conditioning kick - hip turn, pivot, follow-through.",
            "Rest days between hard shin sessions to allow bone remodeling.",
            "Daily core work: sit-ups, leg raises, planks, and rotational exercises.",
            "Never condition on trees, bottles, or concrete - use proper equipment only.",
        ],
        "standards": [
            "Traditional Thai camps build shin conditioning over years, starting in childhood for career fighters.",
            "Progressive overload is the standard sports-science principle; sudden jumps in impact volume cause stress fractures.",
            "Core conditioning is standard in every fight camp worldwide, typically 15-30 minutes daily.",
        ],
        "citations": [CIT_DELP_BASICS, CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: conditioning is the slow forging of the "
            "weapons before battle - the Signature Eight-Limb Method "
            "tempers steel over months, never quenched in a day."
        ),
    },
    {
        "key": "hook",
        "name": "The Hook Punch (Mat Wiang Kwat)",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The hook (mat wiang kwat, the short swinging punch) travels in "
            "a horizontal arc to attack from the side, where the guard is "
            "weakest. Thrown with a bent arm - elbow at roughly 90 degrees - "
            "and driven by violent torso rotation, the hook lands on the "
            "jaw, temple, or ribs with the knuckles, palm facing the "
            "puncher. It is the great guard-breaker: where straight punches "
            "are caught on the gloves, the hook comes around them. Thrown "
            "short and tight it is one of the most reliable knockout "
            "punches in striking, and the lead hook off the jab is a "
            "classic Muay Thai combination."
        ),
        "how_it_works": (
            "From the stance, pivot the lead foot inward and rotate the "
            "hips and torso sharply as the lead elbow lifts to shoulder "
            "height with the arm bent at about 90 degrees. Swing the fist "
            "in a tight horizontal arc, landing with the knuckles while "
            "the palm faces you, and keep the rear hand glued to the "
            "cheek. The elbow stays bent and the punch stays short - a "
            "wide looping hook is slow and gets countered. Snap the hand "
            "back to guard along the arc it traveled. The mechanics work "
            "because the bent arm turns the torso's rotation into a "
            "centrifugal whip: the shorter the arc, the faster the fist "
            "and the harder the transfer. Common faults are swinging the "
            "arm wide like a haymaker, dropping the rear hand, and "
            "standing upright instead of rotating."
        ),
        "key_points": [
            "The hook attacks the side door: it goes around the guard that stops straight punches.",
            "Short and tight beats long and loopy - the 90-degree elbow is the whole technique.",
            "Torso rotation, not the arm, powers the hook; the arm is just the delivery vehicle.",
            "The lead hook off the jab is a money combination: the jab lifts the guard, the hook goes around it.",
            "A hook to the body (digging to the ribs or liver) folds opponents who guard high.",
        ],
        "requirements": [
            "Elbow bent at roughly 90 degrees, lifted to shoulder height for head hooks.",
            "Violent hip and torso rotation with the lead foot pivoting inward.",
            "Fist travels a tight horizontal arc, landing on the knuckles.",
            "Rear hand stays glued to the cheek for the entire punch.",
            "Snap back to guard along the same arc; never leave the hook hanging.",
        ],
        "standards": [
            "The hook family (mat wiang) is core traditional curriculum, drilled on pads and bag.",
            "Hooks to the head and body both score under IFMA/WMC rules; kidney strikes from behind are fouls.",
            "Pad holders call hook combinations (jab-hook, hook-cross-hook) as standard intermediate work.",
        ],
        "citations": [CIT_DELP_BASICS, CIT_DELP_ADV, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the hook is the curved blade that finds the "
            "seam in the armor. In the Signature Eight-Limb Method, the "
            "straight road is guarded - so the wise fighter takes the "
            "curved path."
        ),
    },
    {
        "key": "uppercut",
        "name": "The Uppercut (Mat Soi Dao)",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The uppercut (mat soi dao, the scooping punch) rises vertically "
            "from below, traveling up the centerline to strike the chin, "
            "solar plexus, or ribs from underneath the guard. Thrown by "
            "dropping the hips slightly and driving upward with the legs "
            "and torso, it is the punch that punishes a fighter who leans "
            "forward or drops their hands. In Muay Thai it is thrown "
            "shorter and tighter than in boxing, because a long uppercut "
            "invites the clinch and the knee that comes with it. The "
            "uppercut-cross and the jab-uppercut-hook are classic "
            "guard-splitting combinations."
        ),
        "how_it_works": (
            "From the stance, bend the knees slightly to load the legs, "
            "keeping the guard tight. Drive upward with the legs as the "
            "punching arm extends upward along the centerline, rotating the "
            "fist so the palm faces you at impact, with the elbow staying "
            "bent until extension. The opposite hand stays glued to the "
            "cheek and the chin stays tucked - never look up at the punch. "
            "Snap the hand back down to guard along the same vertical "
            "line. The mechanics work because the legs and torso drive "
            "bodyweight straight up into the target: it is a squat that "
            "ends in a fist. Common faults are dropping the punch low and "
            "looping it (which telegraphs), lifting the chin to watch it "
            "land, and overextending upward off balance."
        ),
        "key_points": [
            "The uppercut is the answer to a high guard: it travels where the gloves are not.",
            "Leg drive powers it - the punch is the top of a squat, not an arm lift.",
            "Short and vertical beats long and loopy; a tight uppercut is invisible until it lands.",
            "Never admire it: the chin stays tucked and the hand snaps straight back down.",
            "It pairs brutally with the hook - uppercut lifts the chin, hook turns it.",
        ],
        "requirements": [
            "Bend the knees to load the legs before the punch fires.",
            "Drive upward with legs and torso, arm extending vertically along the centerline.",
            "Fist rotates palm-inward at impact; elbow bent until extension.",
            "Chin tucked and opposite hand glued to the cheek throughout.",
            "Snap the hand back down to guard along the same line.",
        ],
        "standards": [
            "Mat soi dao is taught as the vertical punch of the traditional four-punch curriculum.",
            "Uppercuts to the chin and body score under IFMA/WMC rules.",
            "Pad work for uppercuts emphasizes the leg drive - holders watch the knees, not the hands.",
        ],
        "citations": [CIT_DELP_BASICS, CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the uppercut is the geyser - pressure from "
            "below that the walls cannot hold. In the Signature Eight-Limb "
            "Method, the low road rises to meet the high guard."
        ),
    },
    {
        "key": "elbow_horizontal",
        "name": "Horizontal Elbow Strike (Sok Tad)",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The horizontal elbow (sok tad) is the signature close-range "
            "weapon of Muay Thai: the arm bent tight, the elbow driven "
            "sideways across the target like a blade. The elbow is bone "
            "with almost no padding over it, so even a short sok tad cuts "
            "skin open - elbow cuts stop fights. Thrown from the clinch "
            "break, the pocket, or as a counter to a missed punch, it "
            "travels only inches but lands with the full rotation of the "
            "torso behind it. Fighters fear the elbow more than the punch "
            "because the damage is immediate and visible."
        ),
        "how_it_works": (
            "From close range, bend the striking arm tightly so the fist "
            "nearly touches the shoulder, with the elbow pointing outward "
            "at about shoulder height. Rotate the hips and torso sharply, "
            "driving the point of the elbow horizontally across the "
            "target - the brow, cheek, or temple. Keep the opposite hand "
            "guarding the face and the chin tucked; the elbow strike is "
            "thrown with the body, not swung with the shoulder. Snap the "
            "arm back to guard immediately. The mechanics work because "
            "the bent arm is a rigid lever: torso rotation whips the bony "
            "point of the elbow through a short arc at high speed, and the "
            "small contact area concentrates all the force into a cut. "
            "Common faults are swinging the arm wide, dropping the guard "
            "hand, and throwing elbows from too far away where they cannot "
            "reach."
        ),
        "key_points": [
            "The elbow cuts: a short sok tad can open a fight-ending cut, which is why it is the most feared close weapon.",
            "Range is inches, not feet - the elbow only works in the pocket or the clinch.",
            "Torso rotation drives it; the arm stays bent and rigid like a blade handle.",
            "It is the classic counter: slip a punch and the elbow is already in range.",
            "Guard discipline is critical - throwing elbows with both hands down is how you get knocked out mid-technique.",
        ],
        "requirements": [
            "Arm bent tight with the fist near the shoulder, elbow at shoulder height.",
            "Sharp hip and torso rotation driving the elbow point horizontally across the target.",
            "Target the brow, cheek, or temple - the cutting zones.",
            "Opposite hand guards the face with the chin tucked throughout.",
            "Immediate return to guard; elbows are thrown from close range only.",
        ],
        "standards": [
            "Elbow strikes (sok) are legal and characteristic under IFMA and WMC Muaythai rules.",
            "Cuts from elbows are a leading cause of referee and doctor stoppages in the sport.",
            "Traditional instruction introduces elbows only after punches are solid - they are intermediate weapons.",
        ],
        "citations": [CIT_DELP_ADV, CIT_KRAITUS, CIT_WMC],
        "sig_lens": (
            "Signature lens: the elbow is the hidden dagger - short, "
            "sharp, and always closer than it looks. In the Signature "
            "Eight-Limb Method, the blade is drawn only at arm's length."
        ),
    },
    {
        "key": "knee_straight",
        "name": "Straight Knee Strike (Khao Trong)",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The straight knee (khao trong) drives the point of the knee "
            "straight up into the opponent's torso - the solar plexus, "
            "ribs, or thighs. It is the workhorse of the clinch and one of "
            "the highest-scoring strikes in Muay Thai: a visible knee that "
            "lifts the opponent is worth more than three blocked punches. "
            "The technique chambers the knee high toward the chest, then "
            "thrusts the hips forward so the knee spears upward into the "
            "target while the hands pull the opponent down into it. Fighters "
            "win championships on the strength of their khao trong."
        ),
        "how_it_works": (
            "From the clinch or close range, grip the opponent's neck or "
            "shoulders and pull downward as you lift your knee sharply "
            "toward your own chest. Thrust the hips forward and up, driving "
            "the point of the knee into the target while the arms drag the "
            "opponent's weight down onto the strike - the pull and the "
            "thrust meet at the point of impact. Stay tall on the support "
            "leg with the foot planted, then drop the knee straight back "
            "to the ground. The mechanics work because two forces collide: "
            "the hip thrust drives the knee up while the arm pull drags "
            "the target down, doubling the effective impact. Common faults "
            "are leaning back away from the knee, failing to pull with the "
            "arms, and hopping instead of driving from a planted base."
        ),
        "key_points": [
            "The knee is a collision of two forces: hips thrust up, arms pull down, target caught between.",
            "It is among the highest-scoring strikes - judges reward knees that visibly move the opponent.",
            "Chamber the knee to the chest first; a knee thrown from the floor has no travel and no power.",
            "Stay tall on the planted support leg - hopping knees sacrifice balance for spectacle.",
            "The clinch and the knee are one system: control the neck and the knees are free.",
        ],
        "requirements": [
            "Grip the neck or shoulders and pull the opponent downward into the strike.",
            "Chamber the knee high toward the chest before thrusting.",
            "Drive the hips forward and up, spearing with the point of the knee.",
            "Stay tall and planted on the support leg throughout the strike.",
            "Drop the knee straight back to stance after impact; reset the grip.",
        ],
        "standards": [
            "Knee strikes (khao) to the body and legs are legal and heavily scored under IFMA/WMC rules.",
            "Knees to the head of a standing opponent are restricted by ruleset and weight class - know your rules.",
            "The long clinch with active knees is the classic Thai stadium style, rewarded by traditional judges.",
        ],
        "citations": [CIT_DELP_BASICS, CIT_DELP_ADV, CIT_IFMA],
        "sig_lens": (
            "Signature lens: the knee is the battering ram - the gate "
            "falls when the ram swings true. In the Signature Eight-Limb "
            "Method, the clinch builds the gate and the knee breaks it."
        ),
    },
    {
        "key": "elbow_updiag",
        "name": "Upward and Diagonal Elbow Strikes (Sok Ngat and Sok Chieng)",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The upward elbow (sok ngat) and the diagonal elbow (sok "
            "chieng) attack on rising and slashing lines that the "
            "horizontal elbow cannot reach. Sok ngat drives straight up "
            "under the chin or into the solar plexus, splitting a high "
            "guard from below. Sok chieng slashes diagonally downward "
            "across the brow and scalp, the classic cutting angle that "
            "opens the forehead. Together with the horizontal elbow they "
            "complete the elbow arsenal: every angle of the head can be "
            "cut from the pocket. These are advanced elbows because they "
            "demand precise range and timing - thrown wrong, they miss and "
            "expose the thrower."
        ),
        "how_it_works": (
            "For sok ngat, bend the arm tight with the elbow pointing "
            "down, drop the hips slightly, then drive the elbow straight "
            "up under the chin, rotating the torso into the strike. For "
            "sok chieng, raise the bent arm so the elbow points up and "
            "outward, then slash it diagonally down across the brow, "
            "rotating the torso and dropping the weight into the cut. In "
            "both, the opposite hand guards, the chin stays tucked, and "
            "the arm snaps back to guard instantly. The mechanics work "
            "because the elbow's bony point concentrates torso rotation "
            "onto a tiny area: the upward line attacks under the guard "
            "while the diagonal line shears across the skin to cut. "
            "Common faults are reaching with the arm instead of rotating "
            "the body, and throwing the diagonal elbow too flat so it "
            "pushes instead of cuts."
        ),
        "key_points": [
            "Sok ngat is the uppercut of elbows: it rises under the guard to find the chin.",
            "Sok chieng is the cutting diagonal: brow and scalp split along the slash line.",
            "Both demand pocket range - a half-step too far and the elbow waves at air.",
            "The body rotates into every elbow; the arm is a rigid blade, never a swinging limb.",
            "These are counter and clinch-break weapons, thrown when the opponent's head is presented, not chased.",
        ],
        "requirements": [
            "Sok ngat: elbow down, hips drop, drive straight up under the chin with torso rotation.",
            "Sok chieng: elbow high, slash diagonally down across the brow with weight dropping in.",
            "Arm stays bent and rigid; power comes from the torso, not the shoulder.",
            "Opposite hand guards the face and the chin stays tucked on every rep.",
            "Thrown only at true elbow range, then snapped straight back to guard.",
        ],
        "standards": [
            "All elbow angles are legal under IFMA/WMC rules; the diagonal cut is a classic stoppage producer.",
            "Elbow knockouts and cuts are recorded as KO/TKO results in professional Muay Thai.",
            "Advanced elbow work is pad-drilled with a holder presenting head targets at pocket range.",
        ],
        "citations": [CIT_DELP_ADV, CIT_KRAITUS, CIT_WMC],
        "sig_lens": (
            "Signature lens: the upward elbow is the stalagmite and the "
            "diagonal is the falling star - one rises from the earth, one "
            "falls from the sky. In the Signature Eight-Limb Method, the "
            "blade learns every angle."
        ),
    },
    {
        "key": "knee_curved",
        "name": "Curved Knee Strike (Khao Kong)",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The curved knee (khao kong) swings the knee in an arc to "
            "attack the ribs and thighs from the side, where the straight "
            "knee cannot reach. Thrown from the clinch or the pocket, it "
            "combines the upward drive of the knee with a sideways sweep "
            "of the hip, landing the point of the knee on the floating "
            "ribs or the outer thigh. Fighters use it to punish opponents "
            "who shell up against straight knees: the guard stops the "
            "centerline, so the curved knee goes around it. Like all "
            "knees, it is amplified when the arms pull the opponent into "
            "the strike."
        ),
        "how_it_works": (
            "From the clinch grip, swing the hip outward and drive the "
            "knee in a curved path, the point of the knee arcing into the "
            "ribs or thigh from the side. Pull with the arms to drag the "
            "target into the arc as the hip turns over, the same hip "
            "rotation that powers the roundhouse kick. Keep the support "
            "leg planted and the torso upright - the curve comes from the "
            "hip, not from leaning. Return the knee along its arc to the "
            "ground. The mechanics work because the arc lets the knee "
            "travel around a high guard while the hip rotation adds "
            "lateral force to the upward drive, striking the ribs at an "
            "angle they are not braced for. Common faults are leaning "
            "away from the strike, throwing it without the arm pull, and "
            "letting it become a weak leg swing instead of a hip-driven "
            "spear."
        ),
        "key_points": [
            "The curved knee is the hook of the knees: it goes around the guard that stops straight lines.",
            "Hip rotation powers the arc - the same engine as the roundhouse kick, at closer range.",
            "The arm pull is half the strike; without it the target simply rides the curve.",
            "Ribs and outer thigh are the targets; both fold a fighter who is braced only for the centerline.",
            "It flows naturally from the straight knee: when the centerline closes, curve around it.",
        ],
        "requirements": [
            "Swing the hip outward and drive the knee in an arc into the ribs or thigh.",
            "Pull with the arms to drag the target into the strike's path.",
            "Rotate the hip fully over, support leg planted, torso upright.",
            "Strike with the point of the knee, not the thigh.",
            "Return along the arc to the ground and reset the clinch grip.",
        ],
        "standards": [
            "Curved knees score as effective knee strikes under IFMA/WMC judging.",
            "Knees to the ribs are a classic body-attack strategy in stadium Muay Thai.",
            "Clinch-knee rounds on the pads drill straight and curved knees in alternation.",
        ],
        "citations": [CIT_DELP_ADV, CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the curved knee is the scythe - it reaps "
            "where the straight spear cannot reach. In the Signature "
            "Eight-Limb Method, when the gate holds, the warrior goes "
            "around the wall."
        ),
    },
    {
        "key": "clinch_entry",
        "name": "Clinch Entry and Inside Position (Chap Kho)",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The clinch (chap kho, seizing the neck) is Muay Thai's "
            "standing grappling: both fighters grip the neck, head, and "
            "arms, fighting for the inside position from which knees, "
            "elbows, and throws are launched. Entering the clinch safely - "
            "closing distance without walking into a knee or elbow - is a "
            "technique in itself. The fighter who wins the inside position, "
            "with both hands controlling the opponent's neck and the "
            "opponent's arms trapped outside, controls the fight's most "
            "damaging phase. Stadium Muay Thai is often decided in the "
            "clinch: the better clinch fighter drags the bout into deep "
            "water and drowns the opponent there."
        ),
        "how_it_works": (
            "Enter behind a strike - typically a jab, teep, or kick - "
            "stepping deep to collapse the distance as the opponent "
            "reacts. Swim the hands inside: both palms cup the back of "
            "the opponent's neck and head, pulling the head down while "
            "your forearms frame against their collarbone. Fight for the "
            "inside by pummeling - alternating your arms inside theirs - "
            "until both of your hands control the neck and their arms are "
            "outside yours. Keep the hips close, the head positioned to "
            "the side of theirs, and the weight heavy on them. The "
            "mechanics work because inside control gives leverage: hands "
            "on the neck steer the head, and where the head goes the body "
            "follows, opening the torso for knees. Common faults are "
            "entering without a setup strike, reaching with the arms "
            "instead of stepping in, and standing upright where you can "
            "be thrown."
        ),
        "key_points": [
            "Never enter the clinch naked - a setup strike (jab, teep, kick) buys the step inside.",
            "Inside position is everything: both hands on the neck wins, one hand in is a fight.",
            "Pummeling - swimming the arms inside - is the continuous battle for that position.",
            "Heavy hips and head position to the side make you hard to throw and easy to throw with.",
            "The clinch is scored: dominant clinch work with knees wins rounds in stadium judging.",
        ],
        "requirements": [
            "Enter behind a setup strike, stepping deep to collapse distance.",
            "Swim both hands inside to cup the neck, forearms framing the collarbone.",
            "Pummel continuously to keep both hands inside the opponent's arms.",
            "Keep hips close, head to the side, weight heavy on the opponent.",
            "Eyes open and posture broken down - never stand tall in the clinch.",
        ],
        "standards": [
            "The clinch is a defining legal phase of Muaythai under IFMA/WMC rules; prolonged passive clinching is broken by the referee.",
            "Neck wrestling with active knees is the classic stadium style, scored highly by traditional judges.",
            "Gripping the opponent's head with both hands (the plum) is the fundamental clinch control taught first.",
        ],
        "citations": [CIT_DELP_BASICS, CIT_DELP_ADV, CIT_IFMA],
        "sig_lens": (
            "Signature lens: the clinch is the handshake of warriors - "
            "grip for grip, will against will. In the Signature Eight-Limb "
            "Method, the fighter who owns the neck owns the storm."
        ),
    },
    {
        "key": "low_kick",
        "name": "The Low Cut Kick (Tae Kod)",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The low kick (tae kod, the cutting kick) chops the shin "
            "horizontally into the opponent's thigh or calf, usually the "
            "lead leg. It is the great equalizer of Muay Thai: a few clean "
            "low kicks deaden the lead leg, killing the opponent's "
            "footwork, their kicks, and eventually their ability to stand. "
            "Thrown with the same mechanics as the roundhouse but aimed "
            "low, it is faster, safer, and harder to check than the body "
            "kick. Fighters who cannot check low kicks lose the leg by the "
            "third round - and with it, the fight."
        ),
        "how_it_works": (
            "From the stance, step slightly outward with the lead foot and "
            "pivot hard on the support foot as the hips roll over. Swing "
            "the leg in a low horizontal arc, striking with the lower shin "
            "across the opponent's thigh or calf, and chop downward "
            "through the target as if cutting it. Keep the guard up and "
            "the same-side arm swinging for balance. Return to stance "
            "immediately - a low kick left hanging is begging to be "
            "caught. The mechanics work because the thigh's nerves and "
            "muscle cannot condition against repeated shin impacts: each "
            "kick deadens the leg a little more, and the chopping angle "
            "drives through the muscle instead of glancing off. Common "
            "faults are kicking with the foot (which breaks toes), "
            "standing too upright (which telegraphs), and admiring the "
            "kick instead of resetting."
        ),
        "key_points": [
            "The low kick is an investment: each one pays off in a slower, weaker opponent leg.",
            "Three unchecked low kicks change a fight; ten end the leg's usefulness.",
            "The shin is the weapon - kicking with the foot risks broken toes and metatarsals.",
            "The chopping angle matters: cut down through the thigh, do not slap at it.",
            "Set it up: the low kick lands cleanest behind a jab, cross, or feint that lifts the guard.",
        ],
        "requirements": [
            "Step outward and pivot fully on the support foot with the hips rolling over.",
            "Swing a low horizontal arc, striking with the lower shin across thigh or calf.",
            "Chop downward through the target rather than slapping at the surface.",
            "Guard stays up with the same-side arm swinging for balance.",
            "Immediate return to stance; never leave the leg hanging to be caught.",
        ],
        "standards": [
            "Low kicks are legal and scored under IFMA/WMC rules; they are a staple of stadium strategy.",
            "Kicking a downed or grounded opponent is a foul - low kicks target the standing leg only.",
            "Thai camps drill low-kick setups (jab-low kick, cross-low kick) as core intermediate combinations.",
        ],
        "citations": [CIT_DELP_BASICS, CIT_DELP_ADV, CIT_WMC],
        "sig_lens": (
            "Signature lens: the low kick is the woodsman's axe - it does "
            "not fell the tree in one swing, but the tree always falls. "
            "In the Signature Eight-Limb Method, patience is a weapon."
        ),
    },
    {
        "key": "switch_kick",
        "name": "The Switch Kick (Tae Salap)",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The switch kick (tae salap) is a lead-leg roundhouse kick "
            "thrown after a quick switch of the feet: the fighter hops the "
            "feet into opposite stance and fires the new rear leg - which "
            "was the lead leg a heartbeat ago - as a full-power roundhouse. "
            "The switch disguises the kick: the opponent reads a stance "
            "change and eats a kick instead. Faster than stepping into a "
            "rear kick and more powerful than a static lead-leg kick, the "
            "switch kick is the great deceiver of Muay Thai kicking, "
            "capable of landing to the body, legs, or head."
        ),
        "how_it_works": (
            "From the stance, hop lightly and switch the feet: the lead "
            "foot jumps back and the rear foot jumps forward, landing "
            "momentarily in opposite stance. The instant the feet land, "
            "pivot on the new support foot and throw a full roundhouse "
            "with the new rear leg - hip over, shin horizontal, guard "
            "tight. The switch and the kick blend into one motion: hop, "
            "land, pivot, kick. The mechanics work because the switch "
            "loads the lead leg like a rear leg, giving it rear-leg power "
            "with lead-leg speed, while the footwork disguises the attack "
            "as a stance shift. Common faults are switching too high "
            "(which telegraphs), pausing between the switch and the kick, "
            "and landing flat-footed so the pivot dies."
        ),
        "key_points": [
            "The switch turns the fast lead leg into a power leg - speed of the jab, force of the cross.",
            "Disguise is the weapon: the opponent sees footwork and reacts too late to the kick.",
            "The switch must be low and quick - a hopping switch is a telegraphed switch.",
            "No pause between switch and kick: one motion, four beats - hop, land, pivot, kick.",
            "It is the entry to head kicks: the switch kick to the head is a classic highlight finish.",
        ],
        "requirements": [
            "Low, quick foot switch with the feet landing in opposite stance.",
            "Immediate pivot on the new support foot - no pause after the switch.",
            "Full roundhouse mechanics: hip over, shin horizontal, arm swinging.",
            "Guard stays tight through the switch and the kick.",
            "Land back in a balanced stance ready to follow up or defend.",
        ],
        "standards": [
            "Tae salap is standard intermediate curriculum in Thai camps, drilled on pads and bag.",
            "Switch kicks to all legal targets score under IFMA/WMC rules.",
            "The switch step is also a defensive footwork tool - stance switching is legal and common.",
        ],
        "citations": [CIT_DELP_ADV, CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the switch kick is the masquerade - the "
            "lead leg wears the rear leg's mask for a heartbeat. In the "
            "Signature Eight-Limb Method, deception is the ninth limb."
        ),
    },
    {
        "key": "clinch_control",
        "name": "Clinch Control: Pummeling and Hip Position",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Once the clinch is entered, the fight becomes a continuous "
            "battle for control: pummeling - swimming the arms inside the "
            "opponent's to win the neck - and hip position, the leverage "
            "that decides who throws knees and who gets thrown. The "
            "fighter with inside control and heavy hips dictates the "
            "clinch: their knees land, their opponent's knees are smothered, "
            "and the throws go their way. Clinch control is exhausting, "
            "technical, grinding work - and in stadium Muay Thai it is "
            "often the phase that decides championships, round after round "
            "of neck wrestling won by the stronger, smarter clinch fighter."
        ),
        "how_it_works": (
            "From the clinch, pummel by alternating your arms inside the "
            "opponent's: swim one hand over their arm and under yours, "
            "then the other, in a continuous cycle, always fighting to "
            "keep both hands on the neck. Drop your hips lower than "
            "theirs and keep your weight heavy on them, head to the side "
            "of theirs, so your center of gravity sits under theirs. When "
            "you have inside control, pull the head down and fire knees; "
            "when you lose it, pummel back inside or frame the arms away "
            "to break. The mechanics work because the neck is the "
            "steering wheel: inside hands control the head, the head "
            "controls the posture, and broken posture cannot throw knees "
            "or resist throws. Lower hips win the leverage battle every "
            "time. Common faults are standing upright, letting both hands "
            "drift outside, and pulling with the arms instead of dropping "
            "the weight."
        ),
        "key_points": [
            "Pummeling never stops: inside position is rented by the second, never owned.",
            "Lower hips beat higher hips - the leverage battle is won at the waistline.",
            "Inside hands on the neck mean your knees land and theirs are smothered.",
            "Head position to the side protects you from headbutts and sets up the throw.",
            "Clinch dominance is scored: judges reward the fighter visibly controlling the tie-up.",
        ],
        "requirements": [
            "Continuous pummeling to keep both hands inside on the neck.",
            "Hips lower than the opponent's with weight heavy on them.",
            "Head positioned to the side of the opponent's head.",
            "Pull the head down to fire knees when in control; frame and break when losing.",
            "Never stand upright or let both hands drift outside without fighting back inside.",
        ],
        "standards": [
            "Active clinch work with knees and positional dominance scores under IFMA/WMC judging.",
            "Referees break passive clinches; control must produce offense to be rewarded.",
            "Neck-wrestling rounds are standard in Thai camps - dedicated clinch sparring days are traditional.",
        ],
        "citations": [CIT_DELP_ADV, CIT_KRAITUS, CIT_IFMA],
        "sig_lens": (
            "Signature lens: clinch control is the wrestling of wills - "
            "two storms gripping the same rope. In the Signature "
            "Eight-Limb Method, the lower storm always wins."
        ),
    },
    {
        "key": "catch_dump",
        "name": "Catching Kicks and Basic Dumps (Jap Kha)",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Catching a kick (jap kha) turns the opponent's offense into "
            "your opening: as the roundhouse arrives, you trap the leg "
            "against your body with your arms, leaving the kicker balanced "
            "on one leg and wide open. From the catch, the basic dump "
            "sweeps or pushes the standing leg while pulling the caught "
            "leg, toppling the opponent to the canvas for a scored knockdown "
            "effect. The catch is high-risk - mistime it and you eat the "
            "kick with your arms down - but it is one of the most "
            "demoralizing techniques in Muay Thai: nothing deflates a "
            "kicker like being dumped on their own weapon."
        ),
        "how_it_works": (
            "As the kick comes, step slightly into it and wrap both arms "
            "around the kicking leg, pinning the shin tight against your "
            "ribs and hip - never catch it out at arm's length. Clamp the "
            "leg, take one step to off-balance the kicker, then sweep or "
            "kick their standing leg while pulling the caught leg upward "
            "and across. They fall; you stay standing over the catch. The "
            "mechanics work because a kicker on one leg has no base: the "
            "catch removes their balance point and the sweep removes the "
            "remaining one, so gravity does the rest. Rules limit what "
            "follows: you must release or sweep quickly, and you cannot "
            "hold the leg and strike repeatedly. Common faults are "
            "reaching for the kick (which gets your arms kicked), catching "
            "too low on the ankle, and holding the leg too long."
        ),
        "key_points": [
            "The catch converts the opponent's best weapon into their worst moment - but only if timed.",
            "Pin the leg to your body, never at arm's length: the catch is a hug, not a reach.",
            "Step in as you catch; retreating while catching gets you kicked through your own arms.",
            "The dump is immediate: sweep the standing leg while pulling the caught leg - hesitation loses it.",
            "A clean dump scores like a knockdown in the eyes of the judges.",
        ],
        "requirements": [
            "Time the catch to the kick's arrival; step slightly into the kick.",
            "Trap the shin tight against the ribs and hip with both arms.",
            "Off-balance with one step, then sweep the standing leg while pulling the caught leg.",
            "Release or complete the technique quickly - no prolonged holding and hitting.",
            "Return to stance immediately after the dump; never chase a falling opponent.",
        ],
        "standards": [
            "Catching the kick is legal; IFMA/WMC rules limit holding the leg and require prompt release or technique.",
            "Sweeps and dumps from the catch score as effective technique under Thai judging.",
            "Striking a caught-leg opponent is regulated - know the holding-and-hitting rules of your ruleset.",
        ],
        "citations": [CIT_DELP_ADV, CIT_KRAITUS, CIT_WMC],
        "sig_lens": (
            "Signature lens: the catch is the trapdoor - the attacker's "
            "bridge becomes their cliff. In the Signature Eight-Limb "
            "Method, the boldest weapon makes the boldest opening."
        ),
    },
    {
        "key": "shell_counter",
        "name": "Defensive Shell and Counter Basics",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The defensive shell is the tight, compact guard a fighter "
            "assumes under heavy fire: gloves high and tight, elbows "
            "pinned, chin buried, forearms absorbing punches while the "
            "body weathers the storm. But a shell that only absorbs is a "
            "losing shell - the technique pairs the shell with the "
            "counter, the immediate answer thrown through the gaps the "
            "attacker's offense opens. Block the combination, then fire "
            "back before the attacker resets: the counter is the profit "
            "on the defense's investment. Fighters who shell and counter "
            "well turn aggressive opponents into their own worst enemies."
        ),
        "how_it_works": (
            "Under fire, tighten the high guard: gloves to the temples, "
            "elbows welded to the ribs, chin tucked, knees slightly bent "
            "to ride the impact. Absorb on the gloves and forearms, "
            "watching through the guard for the end of the opponent's "
            "combination - the moment their hands return or their weight "
            "shifts. Fire the counter in that window: the cross down the "
            "middle, the hook around the returning guard, or the low kick "
            "as they plant. The mechanics work because every attack opens "
            "a line: punches extended cannot guard, weight committed "
            "cannot move, and the counter travels into the space the "
            "attack just vacated. Common faults are shelling without "
            "watching (which makes counters impossible), countering too "
            "late after the window closes, and dropping the shell to "
            "throw - the counter must fire from behind the guard."
        ),
        "key_points": [
            "The shell buys time; the counter spends it - defense without an answer is just delay.",
            "Watch through the guard: the counter is aimed at the opening, and only the eyes find it.",
            "Every combination ends: the window between their last punch and their reset is your punch.",
            "Counter from the shell, not instead of it - the guard stays up while the answer fires.",
            "The best counters are simple: cross, hook, or low kick, thrown the instant the window opens.",
        ],
        "requirements": [
            "Tighten to a compact shell under fire: gloves high, elbows pinned, chin buried.",
            "Keep the eyes open and watching through the guard for the combination's end.",
            "Identify the window: hands returning, weight shifting, guard opening.",
            "Fire a simple counter - cross, hook, or low kick - in that window.",
            "Rebuild the guard immediately after the counter lands.",
        ],
        "standards": [
            "Effective counter-striking is scored highly under IFMA/WMC judging criteria.",
            "Blocking with the gloves and forearms is legal defense; turning the back is not.",
            "Pad holders drill shell-and-counter as a core intermediate defensive combination.",
        ],
        "citations": [CIT_DELP_BASICS, CIT_DELP_ADV, CIT_IFMA],
        "sig_lens": (
            "Signature lens: the shell is the fortress gate and the "
            "counter is the arrow slit - the enemy batters the wall while "
            "the answer flies through the slit. In the Signature "
            "Eight-Limb Method, every wall has a window."
        ),
    },
    {
        "key": "spin_elbow",
        "name": "Spinning Elbow (Sok Klap)",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The spinning elbow (sok klap) is Muay Thai's most spectacular "
            "close weapon: the fighter turns fully, whipping the elbow "
            "around in a 360-degree arc to blindside the opponent. Thrown "
            "when the opponent crowds or after a missed strike spins you "
            "naturally, it lands the bony point of the elbow on the temple "
            "or brow with the full momentum of the body's rotation - and "
            "it cuts like a scalpel. It is high-risk: a missed spinning "
            "elbow turns your back to the opponent. But landed clean, it "
            "is among the most devastating and celebrated techniques in "
            "the sport."
        ),
        "how_it_works": (
            "From close range, step the lead foot across and begin turning "
            "the body, spotting the target over the shoulder as long as "
            "possible. Whip the bent arm around with the elbow leading, "
            "the point of the elbow traveling the full circle to meet the "
            "temple or brow, driven by the hips and the planted pivot "
            "foot. Keep the opposite hand guarding through the turn and "
            "re-face the opponent the instant the elbow lands or misses. "
            "The mechanics work because the full-body spin loads enormous "
            "angular momentum into a tiny striking surface: rotational "
            "energy concentrates at the elbow's point like a hammer swung "
            "in a circle. Common faults are telegraphing with a big "
            "windup, throwing it from too far away, and failing to "
            "re-face after the miss."
        ),
        "key_points": [
            "The spinning elbow weaponizes the full turn: 360 degrees of rotation behind a single bony point.",
            "It is a counter and pocket weapon - thrown when the opponent crowds, not chased across the ring.",
            "Spot the target over the shoulder as long as possible; blind spins miss.",
            "A miss must re-face instantly: the technique's price is a moment with your back turned.",
            "Elbow cuts end fights - the spinning elbow is a stoppage machine when it lands.",
        ],
        "requirements": [
            "Thrown from true pocket range after crowding or a natural turn.",
            "Full 360-degree body rotation with the elbow leading and the arm bent tight.",
            "Pivot foot planted, hips driving the rotation, opposite hand guarding.",
            "Spot the target over the shoulder through the turn.",
            "Re-face the opponent immediately whether it lands or misses.",
        ],
        "standards": [
            "Spinning elbows are legal under IFMA/WMC rules and are recorded in professional highlight knockouts.",
            "Turning the back momentarily during a spin is legal; deliberately turning away to avoid fighting is not.",
            "Advanced spinning techniques are drilled on pads with a holder calling the entry.",
        ],
        "citations": [CIT_DELP_ADV, CIT_KRAITUS, CIT_WMC],
        "sig_lens": (
            "Signature lens: the spinning elbow is the cyclone - the "
            "warrior becomes the storm and the storm carries a blade. In "
            "the Signature Eight-Limb Method, the full turn is the full "
            "commitment."
        ),
    },
    {
        "key": "flying_knee",
        "name": "Flying Knee (Khao Loi)",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The flying knee (khao loi, the floating knee) launches the "
            "fighter airborne, driving the knee upward into the opponent's "
            "head or torso at the peak of the jump. It is the most "
            "dramatic technique in Muay Thai: the fighter takes a running "
            "or hopping step, springs off one leg, and spears the knee "
            "into the target while the hands pull the opponent down into "
            "it. Landed clean it is a knockout blow and an instant "
            "highlight. It is also the highest-commitment strike in the "
            "art - a missed flying knee leaves the fighter airborne, "
            "off-balance, and exhausted."
        ),
        "how_it_works": (
            "Take one or two driving steps toward the opponent, plant the "
            "support foot, and spring upward off it as the striking knee "
            "chambers to the chest. At the peak of the jump, thrust the "
            "hips and drive the point of the knee into the target - chin, "
            "face, or torso - while the hands grip and pull the opponent "
            "down into the strike. Land on the support foot first, "
            "absorbing with a bent knee, and reset the stance instantly. "
            "The mechanics work because the jump adds the body's upward "
            "momentum to the hip thrust: mass times the combined velocity "
            "meets the target at the knee's point, and the downward pull "
            "of the arms doubles the collision. Common faults are jumping "
            "without a setup (which gets you met with an elbow), failing "
            "to pull with the hands, and landing stiff-legged."
        ),
        "key_points": [
            "The flying knee is maximum commitment: the whole body leaves the ground behind one strike.",
            "It must be set up - off a combination, a broken rhythm, or a hurt opponent - never thrown naked.",
            "Hands pull down as the knee drives up; the collision of the two is the knockout.",
            "The jump's peak is the impact point: mistime it and the knee arrives weak or not at all.",
            "Land ready: bent knee, stance reset, guard up - the technique ends on the ground, not in the air.",
        ],
        "requirements": [
            "One or two driving steps into a planted, springing takeoff - never flat-footed.",
            "Knee chambered to the chest at takeoff, thrust at the jump's peak.",
            "Hands gripping and pulling the opponent down into the strike.",
            "Target the chin, face, or torso with the point of the knee.",
            "Land on the support leg with a bent knee and reset the stance immediately.",
        ],
        "standards": [
            "Flying knees are legal under IFMA/WMC rules; knees to the head follow the ruleset's head-knee regulations.",
            "Jumping knee knockouts are among the most recorded highlight finishes in professional Muay Thai.",
            "Advanced jump techniques are drilled on crash pads before live pad work.",
        ],
        "citations": [CIT_DELP_ADV, CIT_KRAITUS, CIT_WMC],
        "sig_lens": (
            "Signature lens: the flying knee is the thunderbolt - the "
            "warrior leaves the earth to strike from the sky. In the "
            "Signature Eight-Limb Method, the sky is just another range."
        ),
    },
    {
        "key": "spin_heel",
        "name": "Spinning Heel Kick (Tae Klap)",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The spinning heel kick (tae klap) turns the fighter a full "
            "360 degrees, whipping the heel around in a horizontal arc to "
            "strike the head or body from the blind side. The longest "
            "weapon in the spinning arsenal, it carries the full rotation "
            "of the body into the hard bone of the heel - a landed spinning "
            "heel kick is a knockout blow. Fighters throw it as a counter "
            "when the opponent overcommits, or as a surprise behind a "
            "combination that has the opponent's eyes low. Like all spins, "
            "it demands total commitment and punishes hesitation."
        ),
        "how_it_works": (
            "From stance, step the lead foot across the body and begin the "
            "turn, spotting the target over the shoulder. As the body "
            "rotates, chamber the kicking leg and whip it around "
            "horizontally, extending at the last instant so the heel - not "
            "the foot - strikes the target at the end of the rotation. "
            "Pivot hard on the support foot through the full turn, keep "
            "the guard hand up as long as possible, and follow through "
            "the target before re-facing. The mechanics work because the "
            "leg is the longest lever in the body: a full-speed 360-degree "
            "rotation whips the heel through the longest possible arc, "
            "and the heel's small hard surface concentrates the force. "
            "Common faults are chambering too early (which kills the "
            "whip), striking with the flat foot, and stopping the "
            "rotation at impact instead of following through."
        ),
        "key_points": [
            "The heel is the hammer head: hard bone at the end of the body's longest lever.",
            "Spotting over the shoulder keeps the kick aimed; blind spins are lottery tickets.",
            "It is a counter and surprise weapon - thrown when the opponent's eyes are busy elsewhere.",
            "Full commitment or nothing: a half-spun heel kick is a slow turn with your back exposed.",
            "Follow through the target; the kick's power lives in the last 90 degrees of the turn.",
        ],
        "requirements": [
            "Lead foot steps across to start the turn; spot the target over the shoulder.",
            "Full 360-degree rotation with a hard pivot on the support foot.",
            "Leg chambers then whips out horizontally, striking with the heel at full extension.",
            "Guard hand stays up through the turn as long as possible.",
            "Follow through the target and re-face immediately.",
        ],
        "standards": [
            "Spinning heel kicks are legal under IFMA/WMC rules; heel knockouts are recorded KO results.",
            "Spinning techniques are advanced curriculum, drilled on pads after the fundamentals are mastered.",
            "Head kicks must be controlled in amateur rulesets - know the contact rules of your competition.",
        ],
        "citations": [CIT_DELP_ADV, CIT_KRAITUS, CIT_IFMA],
        "sig_lens": (
            "Signature lens: the spinning heel is the scythe of the "
            "whirlwind - the longest blade the storm carries. In the "
            "Signature Eight-Limb Method, the full circle is the full "
            "word."
        ),
    },
    {
        "key": "pocket_elbows",
        "name": "Elbow-Range Fighting in the Pocket",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Pocket fighting is combat at elbow range - the phone-booth "
            "distance where punches are smothered, kicks cannot chamber, "
            "and elbows rule. The advanced pocket fighter lives "
            "comfortably in this chaos: slipping inside the opponent's "
            "power, framing with the forearms, and carving with short "
            "elbows in every direction while staying defensively tight. "
            "It is the most dangerous range in Muay Thai and the most "
            "lucrative: fighters who master the pocket cut opponents to "
            "ribbons while taking little in return. The pocket is not "
            "brawling - it is surgery at conversational distance."
        ),
        "how_it_works": (
            "Slip or step inside the opponent's punching range, closing to "
            "forearm distance with the guard tight and the chin buried. "
            "Frame with the forearms against their shoulders and arms to "
            "control their posture, then work short elbows - horizontal, "
            "upward, diagonal - in combination, turning the hips into "
            "each one while the non-striking hand guards or frames. Move "
            "the head constantly off the centerline between elbows; a "
            "stationary head in the pocket gets elbowed back. Exit on an "
            "angle after the combination, never straight back. The "
            "mechanics work because at this range the opponent's long "
            "weapons are jammed while your short weapons have full "
            "travel: geometry favors the elbows. Common faults are "
            "standing still in the pocket, dropping the hands to brawl, "
            "and backing straight out into a knee."
        ),
        "key_points": [
            "The pocket is elbow country: at forearm distance, long weapons jam and short blades rule.",
            "Framing with the forearms controls the opponent's posture and creates the elbow lanes.",
            "Head movement never stops in the pocket - a still head is a cut waiting to happen.",
            "Elbows are thrown in combination with hip turn behind each one, not as single swings.",
            "Exit on an angle after the exchange; straight back is where the knee is waiting.",
        ],
        "requirements": [
            "Close to forearm distance with the guard tight and chin buried.",
            "Frame the opponent's shoulders and arms with the forearms to control posture.",
            "Throw short elbows in combination - horizontal, upward, diagonal - with hip turn each time.",
            "Keep the head moving off the centerline between strikes.",
            "Exit the pocket on an angle, guard rebuilt, never backing straight out.",
        ],
        "standards": [
            "Close-range elbow exchanges are the classic stadium infighting, heavily scored when effective.",
            "Framing with the forearm is legal; extending the arm to stiff-arm the face is regulated.",
            "Pocket sparring with controlled elbows is standard advanced training in Thai camps.",
        ],
        "citations": [CIT_DELP_ADV, CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the pocket is the forge - the hottest fire "
            "makes the sharpest blade. In the Signature Eight-Limb "
            "Method, the warrior who is comfortable in the fire owns it."
        ),
    },
    {
        "key": "clinch_throws",
        "name": "Clinch Throws (Thum)",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Clinch throws (thum) dump the opponent to the canvas from the "
            "tie-up: off-balancing the opponent's posture, then reaping, "
            "tripping, or twisting them to the ground. A clean throw scores "
            "like a knockdown in Thai judging and breaks the opponent's "
            "will - being ragdolled in the clinch is humiliating and "
            "exhausting. The technique begins with kuzushi, the breaking "
            "of balance: pulling, pushing, and turning the opponent until "
            "their weight commits past their base, then removing the "
            "support. Advanced clinch fighters chain throws off failed "
            "knees: every defended knee is a chance to change levels and "
            "dump."
        ),
        "how_it_works": (
            "From inside clinch control, break the opponent's posture by "
            "pulling the head down and to one side while stepping your "
            "hips across their centerline. As their weight commits past "
            "their feet, reap their near leg with your leg, or hook behind "
            "their knee and twist their upper body the opposite way, "
            "driving them to the canvas. Keep your own base wide and your "
            "weight back so you stay standing as they fall. The mechanics "
            "work through off-balancing: a human stays upright only while "
            "their center of mass sits over their base of support, so the "
            "throw first moves the mass past the base and then removes the "
            "base itself. Common faults are muscling the throw without "
            "breaking balance first, standing too upright, and falling "
            "with the opponent instead of staying on the feet."
        ),
        "key_points": [
            "Balance breaks before the body falls: the throw is won in the off-balancing, not the lift.",
            "Inside control is the launchpad - you cannot throw well from outside the clinch.",
            "Reap the leg, twist the body: remove the base while turning the mass past it.",
            "Stay standing: a throw where both fighters fall scores for no one.",
            "Chain throws off defended knees - every blocked knee is a level-change opportunity.",
        ],
        "requirements": [
            "Win inside clinch control before attempting any throw.",
            "Break posture by pulling the head down and to the side, stepping hips across.",
            "Off-balance the opponent until their weight commits past their base.",
            "Reap or hook the near leg while twisting the upper body the opposite way.",
            "Keep a wide base and stay on your feet as the opponent falls.",
        ],
        "standards": [
            "Clean throws score as effective technique, comparable to knockdowns, under Thai judging.",
            "Suplex-style spikes and throws designed to land the opponent on the head or neck are fouls.",
            "Clinch-throw drills are standard advanced work in Thai camps, practiced on mats.",
        ],
        "citations": [CIT_DELP_ADV, CIT_KRAITUS, CIT_IFMA],
        "sig_lens": (
            "Signature lens: the throw is the harvest - the stalk is cut "
            "when it leans past standing. In the Signature Eight-Limb "
            "Method, the earth is the final opponent and gravity always "
            "wins."
        ),
    },
    {
        "key": "sweeps",
        "name": "Sweeping the Supporting Leg (Tad Kha)",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The sweep (tad kha) removes the opponent's supporting leg at "
            "the exact moment their weight commits to it, toppling them "
            "with leverage rather than force. Thrown from the clinch, off "
            "a caught kick, or as a counter to a step, the sweep hooks the "
            "ankle or calf and pulls or pushes it out from under the "
            "opponent while the upper body is turned the other way. It is "
            "the most economical takedown in Muay Thai: a few inches of "
            "well-timed footwork defeats a fully braced fighter. Judges "
            "score clean sweeps highly, and a fighter who is swept "
            "repeatedly loses confidence in their base."
        ),
        "how_it_works": (
            "Time the sweep to the opponent's weight transfer: as they "
            "step or plant onto the leg, hook your foot behind their ankle "
            "or across their calf. Simultaneously push or pull their upper "
            "body the opposite direction - with a clinch grip, a forearm "
            "frame, or a pull on the caught leg. The leg sweeps out as the "
            "body tips over it, and the opponent falls. Keep your own "
            "weight back and your base wide so you remain standing. The "
            "mechanics work through leverage and timing: the ankle is the "
            "longest lever from the hip, so a small force at the ankle "
            "moves the whole body, and striking at the weight-transfer "
            "moment means there is no second leg to catch them. Common "
            "faults are sweeping a leg with no weight on it, muscling with "
            "the leg instead of timing, and leaning in so far you fall "
            "together."
        ),
        "key_points": [
            "Timing is the technique: sweep the leg at the weight-transfer moment, not before or after.",
            "The ankle is the longest lever - a small, well-timed hook moves the whole fighter.",
            "Upper body goes one way, leg goes the other: the twist is what topples.",
            "Sweeps are leverage, not strength - the smallest fighter can sweep the largest with timing.",
            "Stay standing: your base stays wide and back while their base disappears.",
        ],
        "requirements": [
            "Read the weight transfer and time the sweep to the plant or step.",
            "Hook the ankle or calf with your foot at the moment of commitment.",
            "Turn or push the upper body opposite to the sweep direction.",
            "Keep your own weight back on a wide base throughout.",
            "Remain standing over the fallen opponent; reset to stance immediately.",
        ],
        "standards": [
            "Sweeps (tad kha) are legal and scored as effective technique under IFMA/WMC rules.",
            "Sweeping a supporting leg during a kick attempt is classic Muay Thai counter-fighting.",
            "Sweep drills are practiced on mats with partners, emphasizing timing over force.",
        ],
        "citations": [CIT_DELP_ADV, CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the sweep is the tide under the cliff - the "
            "rock stands until the ground is gone. In the Signature "
            "Eight-Limb Method, the smallest wave topples the tallest "
            "tower."
        ),
    },
    {
        "key": "counter_timing",
        "name": "Counter-Fighting: Timing and Interception",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Counter-fighting is the art of answering: reading the "
            "opponent's attack and landing your strike in the gap it "
            "leaves. The advanced counter-fighter does not just block and "
            "return - they intercept, meeting the attack mid-flight with a "
            "teep to the hip, a cross down the middle, or an elbow on the "
            "entry. Timing beats speed: the counter lands because it starts "
            "later and arrives first, traveling the shorter line into the "
            "space the attack vacated. The great stadium counter-fighters "
            "make aggressive opponents look foolish, turning every "
            "offense into an opening."
        ),
        "how_it_works": (
            "Study the opponent's rhythm for a round: which strikes they "
            "lead with, how they step in, where their hands go. As they "
            "commit, fire the interception into the opening line - the "
            "teep into a stepping opponent's hip, the cross over a lazy "
            "jab, the elbow as they lean into the clinch. The counter "
            "starts after their attack starts but lands first because it "
            "travels the inside line while theirs travels the outside. "
            "Drill the core counters until they are reflex: jab-cross over "
            "the jab, low kick on the plant, teep on the step-in, elbow "
            "on the clinch entry. The mechanics work because commitment "
            "is a loan: the attacker spends their balance and guard to "
            "attack, and the counter collects the debt in the exact moment "
            "of spending. Common faults are guessing instead of reading, "
            "countering too late after the window closes, and reaching so "
            "far the counter becomes its own overcommitment."
        ),
        "key_points": [
            "Timing beats speed: the counter starts later and lands first by traveling the shorter line.",
            "Read first, answer second - counters thrown on guesses are just late attacks.",
            "Every attack spends balance and guard; the counter collects the debt at the moment of spending.",
            "The core four interceptions - cross over the jab, low kick on the plant, teep on the step, elbow on the entry - cover most offenses.",
            "Patience is the weapon: the counter-fighter lets the opponent build the opening, then walks through it.",
        ],
        "requirements": [
            "Study the opponent's rhythm, leads, and habits before committing to counters.",
            "Fire the interception into the opening line as the attack commits.",
            "Travel the inside line: shorter path, earlier arrival.",
            "Keep the guard intact - the counter fires from defense, not instead of it.",
            "Drill the core four interceptions until they fire on reflex.",
        ],
        "standards": [
            "Clean counter-striking is among the highest-scored skills under IFMA/WMC judging.",
            "Interception timing is the hallmark of elite stadium fighters (muay femur stylists).",
            "Counter drills - partner attacks, fighter answers - are standard advanced pad and sparring work.",
        ],
        "citations": [CIT_DELP_ADV, CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the counter is the echo that arrives before "
            "the shout - the answer written before the question is "
            "finished. In the Signature Eight-Limb Method, the patient "
            "blade cuts deepest."
        ),
    },
    {
        "key": "combinations",
        "name": "Combination Systems: Multi-Strike Flow",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Combination systems chain strikes into flowing sequences - "
            "three, four, five weapons deep - where each strike sets up the "
            "next and the defense cannot reset between them. The classic "
            "Thai combinations mix levels and limbs: jab-cross-low kick, "
            "hook-cross-hook-body kick, teep-jab-cross-knee. Advanced "
            "systems add branching: the fighter reads the opponent's "
            "reaction mid-combination and takes the open path, so the "
            "combination is a decision tree, not a script. The fighter with "
            "the deeper combination system lands in volume, breaks guards "
            "by accumulation, and never throws a single strike alone."
        ),
        "how_it_works": (
            "Build from two-strike pairs: jab-cross, jab-low kick, "
            "cross-hook. Extend to threes by adding a level change or a "
            "limb change: jab-cross-low kick, hook-cross-body kick. Then "
            "add the branch: if the opponent shells high after the "
            "one-two, the third strike goes low; if they drop the hands "
            "to check, the third strike goes high. Drill each combination "
            "slow on the pads until the transitions are seamless, then "
            "bring it to speed, then to the bag with full power, then to "
            "sparring with control. The mechanics work because defense is "
            "sequential: the guard can only answer one line at a time, so "
            "each strike in the sequence occupies the defense while the "
            "next one lands where the guard just left. Common faults are "
            "throwing combinations as memorized scripts, pausing between "
            "strikes, and dropping the guard to admire the last strike."
        ),
        "key_points": [
            "Combinations are decision trees, not scripts: read the reaction mid-flow and take the open branch.",
            "Mix levels and limbs - high-low, hand-foot, punch-kick - so the defense can never settle.",
            "Each strike occupies the guard so the next one lands where the guard just left.",
            "Build slowly: pairs, then threes, then branches - speed comes after seamlessness.",
            "Never throw one strike alone at the advanced level; every weapon travels with an escort.",
        ],
        "requirements": [
            "Master two-strike pairs before building threes and fours.",
            "Change levels and limbs within every combination.",
            "Branch on the opponent's reaction: high shell means go low, low check means go high.",
            "Drill slow to seamless, then fast, then full power on the bag, then controlled sparring.",
            "Guard stays up between strikes; no pausing and no admiring.",
        ],
        "standards": [
            "Multi-strike combinations are the primary scoring offense in professional Muay Thai.",
            "Pad holders call numbered combinations; fighters must execute 3-5 strike flows on command.",
            "Traditional training builds combinations from the basic pairs upward - no skipping levels.",
        ],
        "citations": [CIT_DELP_BASICS, CIT_DELP_ADV, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the combination is the river - each strike "
            "a bend, and the defense drowns trying to dam it. In the "
            "Signature Eight-Limb Method, one strike is a word and a "
            "combination is the sentence."
        ),
    },
    {
        "key": "ringcraft",
        "name": "Ringcraft: Ring Control and Angles",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Ringcraft is the strategic layer of Muay Thai: controlling "
            "where the fight happens, cutting off the ring to trap mobile "
            "opponents, creating angles that multiply your offense while "
            "halving theirs, and managing the clock and the score. The "
            "advanced fighter does not chase - they herd, stepping to cut "
            "the escape routes so the opponent backs into the ropes or the "
            "corner where the combinations land heaviest. Angles are the "
            "geometry of advantage: stepping 45 degrees off the centerline "
            "after a combination puts you beside the opponent's guard "
            "instead of in front of it. Ringcraft wins fights that "
            "technique alone cannot."
        ),
        "how_it_works": (
            "Cut the ring by stepping toward the opponent's escape side, "
            "not at the opponent: if they circle left, step to your right "
            "to close the exit, herding them toward the ropes. Once they "
            "are near the ropes, increase pressure with combinations "
            "rather than single strikes - the ropes limit their retreat, "
            "so volume lands. Create angles by pivoting 45 degrees after "
            "your combination: the pivot moves you off the centerline so "
            "their return fire travels through empty space while your next "
            "attack comes from their blind side. Manage distance with the "
            "teep and the jab when ahead, and press with the clinch and "
            "combinations when behind. The mechanics work because the ring "
            "is finite: every step that denies space compounds, and angles "
            "turn a head-on exchange into a flanking attack. Common faults "
            "are following the opponent in a straight line, squaring up "
            "after combinations, and fighting the whole bout in the "
            "center without a plan."
        ),
        "key_points": [
            "Do not chase - herd: cut the escape route and let the ropes do the trapping.",
            "The 45-degree pivot after a combination turns defense into a blind-side attack.",
            "Ropes and corners are force multipliers: volume lands heaviest where retreat is impossible.",
            "Control the real estate and you control the terms - every step should deny space or create angle.",
            "Ringcraft includes the clock: press when behind, manage when ahead, finish when hurt.",
        ],
        "requirements": [
            "Step to cut the escape side, herding the opponent toward ropes and corners.",
            "Increase combination volume when the opponent is trapped; do not let them out for free.",
            "Pivot 45 degrees off the centerline after combinations to create the angle.",
            "Use the teep and jab to manage distance; use the clinch to press.",
            "Fight with a round-by-round plan tied to the score, not just the moment.",
        ],
        "standards": [
            "Ring control and effective aggression are formal judging criteria under IFMA/WMC rules.",
            "The standard ring is approximately 6.1 meters square - ringcraft is the tactics of that space.",
            "Corner and ropes work is drilled with partners in positional sparring rounds.",
        ],
        "citations": [CIT_DELP_ADV, CIT_KRAITUS, CIT_IFMA],
        "sig_lens": (
            "Signature lens: ringcraft is the general's map - the battle "
            "is won in the maneuver before the first blow. In the "
            "Signature Eight-Limb Method, the wise fighter moves the "
            "mountain one step at a time."
        ),
    },
    {
        "key": "fight_camp",
        "name": "Full Fight Camp Conditioning",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The full fight camp is the complete training system that "
            "builds a Muay Thai fighter: typically six to eight weeks of "
            "two daily sessions, six days a week, progressing from base "
            "conditioning to peak sharpness. Mornings bring the roadwork - "
            "5 to 10 kilometer runs - followed by bag rounds, pad rounds, "
            "clinch sparring, and hundreds of kicks. Evenings add "
            "technique, sparring, and strength work. The camp is "
            "periodized: early weeks build volume and the aerobic base, "
            "middle weeks sharpen technique and power, the final week "
            "tapers so the fighter arrives fresh. Everything in this "
            "database funnels into the camp - the camp is where the eight "
            "limbs are forged into a fighter."
        ),
        "how_it_works": (
            "Structure the week as six training days with one full rest "
            "day. Each training day holds two sessions: morning roadwork "
            "(5-10 km run) plus 5 rounds of bag work, 5 rounds of pads, "
            "and 30 minutes of clinch; evening technique drilling, "
            "controlled sparring, and core/strength work. Count the "
            "volume: a camp week delivers roughly 120 rounds of work and "
            "thousands of strikes. Progress the load across the camp: "
            "weeks 1-2 build volume at moderate intensity, weeks 3-5 "
            "raise intensity and sparring, week 6+ tapers volume while "
            "keeping sharpness. Sleep eight or more hours, eat to fuel "
            "two-a-days, and cut weight gradually - never in a crash. The "
            "mechanics work through progressive overload and "
            "supercompensation: the body adapts to the two-a-day stress "
            "during rest, arriving at fight night stronger than the sum "
            "of the sessions. Common faults are skipping the rest day, "
            "sparring hard too often, and cutting weight so aggressively "
            "that the camp's fitness is wasted."
        ),
        "key_points": [
            "The camp is periodized: build volume, sharpen intensity, taper to freshness - in that order.",
            "Two sessions a day, six days a week is the traditional Thai camp rhythm; the rest day is sacred.",
            "Roadwork builds the aerobic engine that powers five championship rounds.",
            "Weight is cut gradually across the camp - a crash cut throws away weeks of fitness.",
            "Everything compounds: technique, conditioning, timing, and toughness are built together, never separately.",
        ],
        "requirements": [
            "Six to eight week camp: two sessions daily, six days on, one full rest day.",
            "Morning: 5-10 km roadwork plus bag rounds, pad rounds, and clinch work.",
            "Evening: technique drilling, controlled sparring, core and strength work.",
            "Periodize: volume early, intensity middle, taper late - arrive fresh, not broken.",
            "Fuel and sleep for two-a-days; cut weight gradually across the camp.",
        ],
        "standards": [
            "The two-session training day is the traditional Thai camp standard, practiced for generations.",
            "Professional bouts run 5 three-minute rounds; the camp's conditioning targets that demand plus margin.",
            "Weight classes and weigh-in rules are set by IFMA/WMC; cuts must land the fighter in class safely.",
        ],
        "citations": [CIT_DELP_BASICS, CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the fight camp is the forge where the eight "
            "limbs become one weapon - weeks of fire, one night of "
            "truth. In the Signature Eight-Limb Method, the camp is the "
            "covenant the fighter signs with themselves."
        ),
    },
]
