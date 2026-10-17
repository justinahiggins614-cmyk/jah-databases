#!/usr/bin/env python3
"""Entries for the Sambo Combat databases (Manon combat orders 2026-10-17, combat batch 2).

Two NEW databases, 34 ladder-ordered records each:

  combat-sambo               - The Sambo Combat Database
                               (public-harvest: real, fact-checked martial-arts
                               knowledge - Russian sambo, sport and combat
                               sambo: throws, leg locks, ground control, and
                               the strikes of combat sambo; every record a
                               technique carrying HOW TO DO IT step-by-step
                               body mechanics, ladder-ordered from
                               fundamentals to advanced; civilian training
                               scope only)
  combat-sambo-signature     - The Sambo Combat Signature Database
                               (his original Signature Sambo Method: the same
                               ladder through the Signature lens, every
                               technique reframed as Signature science; src
                               signature, titles suffixed " (Signature
                               Edition)", never presented as authentic public
                               record)

34 records each, teaching ladder ranks 1-10 non-decreasing:
foundations -> compounded -> advanced.

ID prefixes: JAH-CBSAM- (public) and JAH-CBSAMS- (signature), verified free
in data/manifest.json id_prefix values and in all 819 shard index files in
jah-databases-data-1 (zero hits, 2026-10-17).

Civilian training scope only. No hate-adjacent, profane, or inappropriate
content; no religious talk. Nothing on neutralizing or defeating military
or defense-grade systems (standing exclusion).

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Sambo Method: the "
            "same ladder through the Signature lens, every technique reframed "
            "as Signature science. Clearly labeled Signature-made, never "
            "presented as authentic public record.")

CIT_FIAS = ("FIAS (International Sambo Federation). Official Sambo Rules. "
            "Lausanne; 2024.")
CIT_CHUMAKOV = ("Chumakov EM. 100 Lessons of Sambo. Fizkultura i sport; "
                "Moscow; 1977.")
CIT_KHARLAMPIEV = ("Kharlampiev AA. Sambo: the foundational manuals of the "
                   "system developed from Oshchepkov and Spiridonov; "
                   "1930s-1940s.")
CIT_JACQUES = ("Jacques B, Anderson S. The Sambo Encyclopedia. Black Belt "
               "Communications; 2016.")
CIT_KODOKAN = ("Kano J. Kodokan Judo: The Essential Guide to Judo by Its "
               "Founder. Kodansha; 1986.")
CIT_COMBAT_RULES = ("FIAS. Official Combat Sambo Rules: permitted strikes, "
                    "chokes, and match conduct. Lausanne; 2024.")
CIT_USA_SAMBO = ("USA Sambo. Coaching curriculum and rank requirements; "
                 "2023.")

ENTRIES = [
    {
        "key": "stance_base",
        "name": "Sambo Stance and Base",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The sambo stance is the ready position every technique stands "
            "on: feet roughly shoulder-width apart, knees bent, weight "
            "distributed evenly or slightly forward, back straight and head "
            "up, hands raised to guard. It keeps the center of mass low and "
            "inside the base of support so the fighter can move, grip, and "
            "throw in any direction without being pushed over. A good stance "
            "is the first safety device in sambo and the foundation of every "
            "throw, sweep, and defense that follows."),
        "how_it_works": (
            "Step 1: stand with feet shoulder-width apart, toes pointing "
            "slightly outward. Step 2: bend the knees until the thighs are "
            "roughly at a half-squat, keeping the back straight and the "
            "chest open, never leaning on the front foot. Step 3: lower the "
            "hips so the center of mass sits between the feet, weight "
            "balanced heel to toe. Step 4: raise both hands to chest height, "
            "elbows tucked, palms ready to grip the jacket. Step 5: keep the "
            "head up and eyes on the partner. Step 6: practice shifting "
            "weight foot to foot without rising up or crossing the feet, "
            "so the base stays wide and low under motion."),
        "key_points": [
            "Feet shoulder-width apart, knees bent, back straight",
            "Weight balanced, center of mass inside the base of support",
            "Hands raised to guard, elbows tucked to the body",
            "Head up, eyes on the partner at all times",
            "Never cross the feet while moving",
            "A low stance multiplies balance against pushes and pulls",
        ],
        "requirements": [
            "Flat grippy mat surface with room to move",
            "Sambo boots or bare feet with ankle support",
            "A partner or mirror for posture checks",
            "Warm-up of ankles, knees, and hips before drilling",
        ],
        "standards": [
            "FIAS mat and uniform regulations for sport sambo",
            "Civilian training safety: controlled movement, no live resistance at this stage",
        ],
        "citations": [CIT_CHUMAKOV, CIT_JACQUES, CIT_FIAS],
        "sig_lens": (
            "Signature lens: in the Signature system the stance is the oath "
            "the feet swear to the ground - low, wide, and unhurried. The "
            "fighter plants the Signature base before the first grip, so "
            "balance becomes a promise kept rather than a reaction chased."),
    },
    {
        "key": "breakfalls",
        "name": "Breakfalls: Sambo Ukemi",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Breakfalls (ukemi) are the first technique taught in sambo: how "
            "to land safely when thrown. The fighter tucks the chin, rounds "
            "the back, exhales on impact, and slaps the mat with a straight "
            "arm to spread the landing force across a wide surface instead "
            "of concentrating it in the head, shoulder, or hip. Every "
            "subsequent throwing technique in this database depends on both "
            "partners knowing how to fall. No throwing is practiced until "
            "breakfalls are reliable."),
        "how_it_works": (
            "Backward fall, step 1: squat down close to the mat to start "
            "low. Step 2: tuck the chin hard to the chest so the head never "
            "strikes. Step 3: round the back and roll onto the shoulder "
            "blades. Step 4: exhale sharply on impact. Step 5: slap the mat "
            "with both arms at 45 degrees from the body, palms down, arms "
            "straight. Step 6: keep the legs slightly bent and together. "
            "Side fall: fall to one side, slap with the lower arm, tuck the "
            "upper leg's knee toward the chest, and keep the chin tucked. "
            "Forward fall: from the knees first, then standing, slap with "
            "forearms, forehead never touching."),
        "key_points": [
            "Chin tucked to the chest on every fall, no exceptions",
            "Exhale on impact to protect the ribs and lungs",
            "Slap with a straight arm to spread the landing force",
            "Round the back; never land flat on the spine",
            "Learn from the ground up: squat, then kneel, then stand",
            "Both partners must breakfall before any throwing begins",
        ],
        "requirements": [
            "Thick training mats with no gaps",
            "A qualified instructor supervising first falls",
            "Partner or crash pad for progressive height",
            "No jewelry, watches, or hard objects on the body",
        ],
        "standards": [
            "FIAS mat safety regulations for falls and landings",
            "Civilian training safety: progressive height, supervised practice",
        ],
        "citations": [CIT_CHUMAKOV, CIT_KODOKAN, CIT_FIAS],
        "sig_lens": (
            "Signature lens: in the Signature system the fall is the first "
            "technique and the last insurance - the Signature fighter learns "
            "the ground before the throw. The slap is the covenant with the "
            "mat: force given a wide road never finds the narrow one to "
            "injury."),
    },
    {
        "key": "jacket_grips",
        "name": "The Sambo Jacket Grips",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Sambo is fought in the kurtka, the short sambo jacket with a "
            "belt, and the grips on it are the steering wheel of every "
            "throw. The standard grip is one hand on the sleeve at the "
            "elbow and the other on the lapel at chest height; the belt "
            "grip, the over-the-back grip, and the double-sleeve grip each "
            "open different throwing lanes. Grip fighting - winning the "
            "grip exchange - decides who throws first, so sambo athletes "
            "drill grip acquisition, grip breaking, and re-gripping as a "
            "core skill."),
        "how_it_works": (
            "Step 1: from the stance, step in and secure the sleeve grip "
            "with the fingers wrapped deep past the elbow, thumb on top. "
            "Step 2: take the lapel grip at chest height, knuckles into the "
            "chest, elbow down. Step 3: keep the arms bent and the elbows "
            "close - straight arms get broken. Step 4: to break an "
            "opponent's sleeve grip, circle the hand sharply against their "
            "thumb, the weak point of the grip. Step 5: re-grip instantly "
            "after breaking; the grip exchange never pauses. Step 6: drill "
            "two-on-one grip strips and pummeling to win inside position."),
        "key_points": [
            "Sleeve plus lapel is the standard throwing grip",
            "Fingers deep on the sleeve; knuckles into the lapel",
            "Elbows bent and close - straight arms invite grip breaks",
            "Attack the thumb to break a grip",
            "Re-grip instantly; the exchange never pauses",
            "Grip fighting decides who throws first",
        ],
        "requirements": [
            "A proper sambo kurtka with belt for both partners",
            "Trimmed fingernails to protect hands in grip fighting",
            "A partner for live grip-exchange drills",
            "Wrist mobility warm-up before grip work",
        ],
        "standards": [
            "FIAS uniform regulations: kurtka, belt, shorts, boots",
            "Civilian training safety: no finger locks or grip cranks",
        ],
        "citations": [CIT_CHUMAKOV, CIT_JACQUES, CIT_FIAS],
        "sig_lens": (
            "Signature lens: in the Signature system the grip is the "
            "handshake before the throw - firm, deep, and honest. The "
            "Signature fighter grips the jacket the way a builder grips a "
            "tool: to direct force, never to cling."),
    },
    {
        "key": "footwork",
        "name": "Sambo Footwork",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Sambo footwork moves the stance without breaking it: short "
            "sliding steps, never crossing the feet, circling to change the "
            "attack angle, and the tsugi-ashi follow step that keeps the "
            "base under the hips. Good footwork creates the entries for "
            "throws, keeps the fighter balanced against counters, and lets "
            "the hips arrive where the hands already grip. It is drilled "
            "every session, solo and with a partner."),
        "how_it_works": (
            "Step 1: from the stance, slide the lead foot a short step in "
            "the desired direction without lifting it high. Step 2: bring "
            "the rear foot the same distance with the follow step, so the "
            "stance width never changes. Step 3: circle by stepping the "
            "lead foot around and following, keeping the chest toward the "
            "partner. Step 4: retreat the same way - rear foot first, lead "
            "foot follows. Step 5: never cross the feet and never let the "
            "feet come together. Step 6: drill shadow movement, then "
            "partner mirroring, then grip-and-move entries."),
        "key_points": [
            "Slide, do not step high - stay low and connected to the mat",
            "Follow step keeps stance width constant",
            "Never cross the feet",
            "Circle to change the attack angle",
            "Feet move the hips to where the hands grip",
            "Drill footwork every session, solo and partnered",
        ],
        "requirements": [
            "Open mat space for sliding and circling drills",
            "Sambo boots with mat grip",
            "A partner for mirroring drills",
            "Ankle and calf warm-up",
        ],
        "standards": [
            "FIAS mat regulations",
            "Civilian training safety: controlled speed until patterns are clean",
        ],
        "citations": [CIT_CHUMAKOV, CIT_KODOKAN, CIT_JACQUES],
        "sig_lens": (
            "Signature lens: in the Signature system the feet write the "
            "first draft of every throw. The Signature fighter slides "
            "rather than stamps, so the hips arrive under the grip like a "
            "key arriving at its lock."),
    },
    {
        "key": "kuzushi",
        "name": "Kuzushi: Breaking Balance",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Kuzushi is the art of breaking the opponent's balance before "
            "the throw: pulling, pushing, or turning them so their center "
            "of mass moves outside their base of support. A throw attempted "
            "on a balanced opponent is a strength contest; the same throw "
            "after kuzushi is a redirection of a falling body. Sambo "
            "teaches eight directions of unbalancing and the timing to "
            "exploit the instant the opponent's weight commits."),
        "how_it_works": (
            "Step 1: grip and feel the opponent's weight - where it sits "
            "foot to foot. Step 2: pull or push sharply in the direction "
            "their weight is already drifting, adding to their motion "
            "rather than fighting it. Step 3: time the pull to their step, "
            "when one foot is lifting and the base narrows. Step 4: keep "
            "your own balance low and centered while you unbalance them. "
            "Step 5: the instant their weight commits past their base, "
            "enter the throw. Step 6: drill with a partner rocking "
            "forward, back, and side to side, feeling each direction of "
            "fall."),
        "key_points": [
            "Unbalance first, throw second - never wrestle a balanced opponent",
            "Add to their motion; do not fight it",
            "Attack during their step, when the base narrows",
            "Eight directions: forward, back, left, right, and the diagonals",
            "Keep your own balance while taking theirs",
            "Kuzushi makes technique beat strength",
        ],
        "requirements": [
            "A cooperative partner for balance-feeling drills",
            "Grips already learned and comfortable",
            "Mat space for rocking and stepping drills",
            "Patience: kuzushi is felt, not forced",
        ],
        "standards": [
            "FIAS competition conduct rules",
            "Civilian training safety: no full throws during kuzushi drills",
        ],
        "citations": [CIT_KODOKAN, CIT_CHUMAKOV, CIT_JACQUES],
        "sig_lens": (
            "Signature lens: in the Signature system kuzushi is the quiet "
            "question asked of the opponent's feet - and the throw is the "
            "answer they give by falling. The Signature fighter never "
            "pushes a wall; he waits for the lean and walks it over."),
    },
    {
        "key": "tieup",
        "name": "The Sambo Tie-Up and Clinch Entry",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The tie-up is how sambo fighters close distance and take "
            "control: stepping into the pocket, securing grips, and "
            "establishing the clinch where throws begin. The entry is made "
            "with the head up and the hips low, hands winning inside "
            "position, because whoever controls the tie-up controls the "
            "throwing exchange. Pummeling - fighting for underhooks and "
            "overhooks - is the clinch-entry drill every sambo athlete "
            "repeats."),
        "how_it_works": (
            "Step 1: from footwork range, step in with the lead foot, "
            "staying low. Step 2: raise the hands and swim for inside "
            "position - underhooks or the standard sleeve-lapel grip. "
            "Step 3: bring the hips close, chest to chest, head positioned "
            "to the side, never forehead to forehead. Step 4: secure the "
            "grips tight, elbows in. Step 5: establish kuzushi immediately "
            "with a pull or turn - never stand still in the clinch. Step 6: "
            "drill pummeling: partners alternate swimming for underhooks "
            "without throwing."),
        "key_points": [
            "Enter low, with the head up and eyes forward",
            "Win inside position: underhooks or sleeve-lapel grips",
            "Head to the side, never forehead to forehead",
            "Hips close, chest to chest",
            "Move immediately - a static clinch is a stalled attack",
            "Pummeling drills build clinch entries safely",
        ],
        "requirements": [
            "Comfortable stance, footwork, and grips",
            "A partner for pummeling drills",
            "Mouthguard when clinch work gets live",
            "Mat space for entries without obstacles",
        ],
        "standards": [
            "FIAS rules on gripping and clinch conduct",
            "Civilian training safety: no strikes in sport-sambo clinch drills",
        ],
        "citations": [CIT_CHUMAKOV, CIT_JACQUES, CIT_FIAS],
        "sig_lens": (
            "Signature lens: in the Signature system the tie-up is the "
            "doorway, and the Signature fighter never barges through it - "
            "he steps in low, takes the inside, and makes the clinch his "
            "room before the throw begins."),
    },
    {
        "key": "posture_frame",
        "name": "Posture and Frame in the Clinch",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Posture and framing keep a fighter safe inside the clinch: an "
            "upright spine, a strong neck, and arms used as structural "
            "frames that hold the opponent's weight off the body. A broken "
            "posture - head down, back rounded - is the invitation every "
            "throw accepts. Sambo teaches framing with the forearms and "
            "hands to create space, redirect pressure, and buy the instant "
            "needed to attack or escape."),
        "how_it_works": (
            "Step 1: in the clinch, keep the spine tall and the chin "
            "tucked, neck strong. Step 2: place the forearms as frames "
            "against the opponent's chest and shoulders, elbows bent. "
            "Step 3: when they pressure in, extend the frames to hold their "
            "weight on your skeleton, not your muscles. Step 4: never let "
            "the head drop below their shoulder line. Step 5: use the "
            "frames to steer - push one side to create an angle. Step 6: "
            "drill frame-and-pummel: one partner pressures, the other "
            "frames and re-establishes posture."),
        "key_points": [
            "Spine tall, chin tucked, neck strong",
            "Forearms are structural frames, not pushing muscles",
            "Hold their weight on the skeleton",
            "Head never drops below their shoulder line",
            "Frames create the angle for the attack",
            "Lost posture is lost position",
        ],
        "requirements": [
            "Tie-up and clinch familiarity",
            "Neck strengthening in the warm-up",
            "A partner for pressure drills",
            "Controlled pressure - build intensity gradually",
        ],
        "standards": [
            "FIAS conduct rules for the clinch",
            "Civilian training safety: tap early in pressure drills",
        ],
        "citations": [CIT_CHUMAKOV, CIT_JACQUES, CIT_KODOKAN],
        "sig_lens": (
            "Signature lens: in the Signature system the frame is the "
            "architecture of the clinch - bone, not muscle, carries the "
            "load. The Signature fighter builds his posture like a "
            "doorframe: square, upright, and unmoved by the shoulder "
            "against it."),
    },
    {
        "key": "hip_escape",
        "name": "Hip Escape and Shrimping",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The hip escape - shrimping - is the fundamental ground "
            "movement of sambo: lying on the side, the fighter pushes with "
            "the feet and slides the hips away to create space from a "
            "pinning opponent. Every guard recovery, every escape from "
            "side control and mount, begins with a hip escape. It is "
            "drilled as a warm-up movement until it is automatic, because "
            "on the ground the hips are the engine of survival."),
        "how_it_works": (
            "Step 1: lie on your back, then turn onto one side, knees bent, "
            "feet flat. Step 2: push hard with the feet against the mat. "
            "Step 3: slide the hips backward and away, keeping the "
            "shoulders on the ground - the body moves like a shrimp "
            "curling. Step 4: bring the knees back in and re-square. "
            "Step 5: alternate sides down the length of the mat. Step 6: "
            "drill with a partner holding light side control: shrimp, "
            "insert the knee, and recover guard."),
        "key_points": [
            "Move the hips, not the shoulders - shoulders stay down",
            "Push with the feet, slide the hips",
            "Stay on your side; flat on the back is stuck",
            "The hip escape is the first move of every ground escape",
            "Drill it until it needs no thought",
            "On the ground the hips are the engine",
        ],
        "requirements": [
            "Open mat for shrimping lanes",
            "Comfortable ground clothing, no hard objects",
            "A partner for progressive escape drills",
            "Hip mobility warm-up",
        ],
        "standards": [
            "FIAS mat safety",
            "Civilian training safety: escapes drilled cooperatively first",
        ],
        "citations": [CIT_JACQUES, CIT_CHUMAKOV, CIT_USA_SAMBO],
        "sig_lens": (
            "Signature lens: in the Signature system the shrimp is the "
            "smallest complete escape - hips fleeing danger while the "
            "shoulders hold the line. The Signature fighter moves his "
            "center before he moves his limbs, and space appears."),
    },
    {
        "key": "bridging",
        "name": "Bridging and Rolling Escapes",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Bridging is the explosive upward thrust of the hips from the "
            "back - the power move that unseats a mounted or side-control "
            "opponent. Combined with a roll, it becomes the classic "
            "bridge-and-roll escape from the mount. Sambo teaches bridging "
            "as a full-body lift driven by the legs and glutes, timed to "
            "the opponent's weight shifts, because a bridge thrown into "
            "settled weight fails and a bridge timed to motion succeeds."),
        "how_it_works": (
            "Step 1: lie on your back, feet flat near the hips, arms "
            "protecting. Step 2: drive through the heels and thrust the "
            "hips straight up as high as possible, head and shoulders "
            "staying on the mat. Step 3: hold the top briefly to feel the "
            "full extension. Step 4: for the bridge-and-roll from mount, "
            "trap one of their arms and one of their legs, bridge hard "
            "toward the trapped side, and roll over them as they tip. "
            "Step 5: come up on top in their guard or side control. Step 6: "
            "drill with a cooperative partner, increasing resistance "
            "gradually."),
        "key_points": [
            "Drive through the heels; hips go straight up",
            "Head and shoulders stay on the mat during the lift",
            "Trap an arm and a leg before the bridge-and-roll",
            "Bridge toward the trapped side and roll with the momentum",
            "Time the bridge to their movement, not their settled weight",
            "Legs and glutes drive; the back is a bridge, not a crane",
        ],
        "requirements": [
            "Mat space and a cooperative partner",
            "Hip escape already comfortable",
            "Leg and glute warm-up",
            "Mouthguard for live escape rounds",
        ],
        "standards": [
            "FIAS rules for ground position conduct",
            "Civilian training safety: no slamming, controlled rolls",
        ],
        "citations": [CIT_CHUMAKOV, CIT_JACQUES, CIT_FIAS],
        "sig_lens": (
            "Signature lens: in the Signature system the bridge is the "
            "body's declaration that it will not be held down - the hips "
            "rising like a drawbridge lifting the siege. The Signature "
            "fighter bridges into motion, never into stone."),
    },
    {
        "key": "rules_scoring",
        "name": "Sambo Rules and Scoring Basics",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Sambo is contested under FIAS rules: sport sambo allows throws, "
            "hold-downs, and painful joint locks but bans chokes and "
            "strikes; combat sambo adds punches, kicks, knees, elbows, "
            "ground striking, and chokes. Throws score 1, 2, or 4 points "
            "by amplitude and landing; hold-downs score 2 or 4 by duration; "
            "a painful hold that forces submission, an 8-point lead, or a "
            "knockout in combat sambo ends the bout with total victory. "
            "Knowing the rules shapes every technique choice on the mat."),
        "how_it_works": (
            "Step 1: learn the two disciplines - sport (no chokes, no "
            "strikes) and combat (strikes and chokes added). Step 2: learn "
            "throw scoring: 4 points for a big throw with the opponent "
            "landing flat while the thrower stays standing, 2 for a "
            "side-landing throw, 1 for a low-amplitude landing. Step 3: "
            "learn hold-down scoring: 2 points for a 10-second hold, 4 for "
            "a 20-second hold. Step 4: learn total victory: submission by "
            "painful hold, an 8-point lead, or knockout. Step 5: learn "
            "warnings - three warnings disqualify. Step 6: watch or "
            "referee practice bouts and call the scores."),
        "key_points": [
            "Sport sambo: throws, hold-downs, joint locks - no chokes, no strikes",
            "Combat sambo: strikes, chokes, and ground striking added",
            "Throws score 4, 2, or 1 by amplitude and landing",
            "Hold-downs score 2 (10 seconds) or 4 (20 seconds)",
            "Total victory: submission, 8-point lead, or knockout",
            "Three warnings mean disqualification",
        ],
        "requirements": [
            "Access to the current FIAS rulebook",
            "A coach or referee to explain edge cases",
            "Observation of live or recorded bouts",
            "A rules quiz before first competition",
        ],
        "standards": [
            "FIAS Official Sambo Rules 2024",
            "FIAS Official Combat Sambo Rules 2024",
        ],
        "citations": [CIT_FIAS, CIT_COMBAT_RULES, CIT_USA_SAMBO],
        "sig_lens": (
            "Signature lens: in the Signature system the rules are the "
            "borders of the arena the Signature fighter agrees to honor - "
            "they do not limit the art, they give it a field to play on. "
            "The Signature competitor studies scoring like a ledger, "
            "because points are the currency of victory."),
    },
]

# ---------------------------------------------------------------- compounded
ENTRIES += [
    {
        "key": "osoto_gari",
        "name": "O Soto Gari: Major Outer Reap",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "O soto gari, the major outer reap, is a signature sambo throw: "
            "the attacker steps past the opponent's leg, hooks the leg "
            "from the outside with their own, and drives the opponent "
            "backward over the reaped leg while pulling them down with the "
            "grips. It is one of the highest-percentage throws in sambo "
            "because the mechanics are simple - a lever at the ankle with "
            "the push at the chest - and it chains naturally into follow-up "
            "attacks when defended."),
        "how_it_works": (
            "Step 1: from the standard grip, pull the opponent toward you "
            "and slightly to their right, loading their weight onto their "
            "right leg. Step 2: step your left foot deep beside their right "
            "foot, staying low. Step 3: swing your right leg back and hook "
            "it behind their right leg at the calf, toes pointed, leg "
            "straight. Step 4: drive your chest into them, pushing at "
            "shoulder height while your leg reaps their leg forward and "
            "up. Step 5: keep pulling down with the grips through the "
            "throw so they land on their back. Step 6: follow them down "
            "into side control for the hold-down."),
        "key_points": [
            "Kuzushi first: load their weight onto the leg you will reap",
            "Step deep beside their foot before the reap",
            "Reap with a straight leg, toes pointed, at the calf",
            "Push at the chest while the leg sweeps - lever and force together",
            "Pull down through the throw for the back landing",
            "Follow into side control",
        ],
        "requirements": [
            "Reliable breakfalls from both partners",
            "Standard sleeve-lapel grips",
            "Mat space for the driving step",
            "Crash-pad repetitions before full throws",
        ],
        "standards": [
            "FIAS throw scoring: amplitude and landing quality",
            "Civilian training safety: controlled reap, no kicking the leg",
        ],
        "citations": [CIT_CHUMAKOV, CIT_KODOKAN, CIT_JACQUES],
        "sig_lens": (
            "Signature lens: in the Signature system o soto gari is the "
            "scythe of the ladder - the leg swings like a blade through "
            "wheat while the hands harvest the fall. The Signature fighter "
            "reaps the leg the opponent stands on, and the ground does the "
            "rest."),
    },
    {
        "key": "de_ashi_harai",
        "name": "De Ashi Harai: Advancing Foot Sweep",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "De ashi harai, the advancing foot sweep, catches the "
            "opponent's foot the instant it moves: as they step forward, "
            "the attacker sweeps the advancing foot sideways with the sole "
            "of their own foot, removing the landing the step needed. It "
            "is a timing throw rather than a strength throw - the sweep "
            "lands in the split second the foot is light. Sambo athletes "
            "use it as an opening probe and as a counter to aggressive "
            "forward pressure."),
        "how_it_works": (
            "Step 1: grip and move with the opponent, matching their "
            "rhythm. Step 2: watch their feet, not their hands - the sweep "
            "targets the stepping foot. Step 3: as their foot begins to "
            "advance, sweep your foot low across the mat into the side of "
            "their advancing foot. Step 4: contact with the sole of your "
            "foot at their ankle, sweeping through, not kicking. Step 5: "
            "simultaneously pull their upper body in the direction of the "
            "step to complete the unbalancing. Step 6: the instant they "
            "fall, step back into base - never chase a failed sweep."),
        "key_points": [
            "Sweep the foot that is moving, while it is light",
            "Sole of the foot to their ankle - sweep, never kick",
            "Stay low; the sweep travels across the mat",
            "Pull the upper body with the sweep",
            "Timing beats strength on every foot sweep",
            "If the sweep misses, reset - do not chase",
        ],
        "requirements": [
            "Footwork and rhythm drills already comfortable",
            "Light, flexible sambo boots",
            "A moving partner for timing practice",
            "Patience - this throw is learned slowly",
        ],
        "standards": [
            "FIAS rules on foot sweeps and contact",
            "Civilian training safety: sweep the foot, never the shin or knee",
        ],
        "citations": [CIT_KODOKAN, CIT_CHUMAKOV, CIT_JACQUES],
        "sig_lens": (
            "Signature lens: in the Signature system de ashi harai is the "
            "thief of the step - it steals the ground the foot was "
            "traveling to. The Signature fighter watches the feet the way "
            "a reader watches the next word, and sweeps the sentence away."),
    },
    {
        "key": "ko_uchi_gari",
        "name": "Ko Uchi Gari: Minor Inner Reap",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Ko uchi gari, the minor inner reap, attacks the inside of the "
            "opponent's far-side foot: the attacker hooks their foot behind "
            "the opponent's heel from the inside and reaps it forward "
            "while driving the upper body backward. It is the close-range "
            "cousin of o soto gari, thrown from chest-to-chest distance, "
            "and it is the classic follow-up when an opponent steps back "
            "to avoid the outer reap."),
        "how_it_works": (
            "Step 1: from the clinch, pull the opponent forward onto their "
            "toes. Step 2: step your foot between their legs, close to "
            "their lead foot. Step 3: hook your foot behind their heel "
            "from the inside, ankle to ankle. Step 4: reap their foot "
            "forward and up while driving your chest into them and pulling "
            "down with the grips. Step 5: keep your weight on them through "
            "the fall. Step 6: land in side control, ready for the "
            "hold-down."),
        "key_points": [
            "Hook ankle to ankle from the inside",
            "Pull them forward onto their toes first",
            "Chest-to-chest distance - this is a close throw",
            "Reap forward and up while driving the body back",
            "The classic answer to the o soto gari defense",
            "Stay heavy through the landing",
        ],
        "requirements": [
            "Clinch entries and posture comfortable",
            "Breakfalls reliable from close throws",
            "A partner for slow technical repetitions",
            "Ankle mobility for the hooking foot",
        ],
        "standards": [
            "FIAS throw scoring",
            "Civilian training safety: no stomping the reap",
        ],
        "citations": [CIT_KODOKAN, CIT_CHUMAKOV, CIT_JACQUES],
        "sig_lens": (
            "Signature lens: in the Signature system ko uchi gari is the "
            "inside answer to the outside question - when the opponent "
            "flees the outer reap, the inner reap is already waiting. The "
            "Signature fighter sets traps in pairs."),
    },
    {
        "key": "seoi_nage",
        "name": "Seoi Nage: Shoulder Throw",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Seoi nage, the shoulder throw, turns the back to the opponent, "
            "loads their body across the shoulders and hips, and throws "
            "them forward over the top. In sambo the drop-knee and standing "
            "variants are both staples, thrown off the sleeve-lapel grip. "
            "It is a committed turning throw - the entry must be deep and "
            "the hips must get below the opponent's - and it scores big "
            "when the landing is clean."),
        "how_it_works": (
            "Step 1: pull the opponent forward hard, breaking their balance "
            "to their front. Step 2: pivot 180 degrees on the lead foot, "
            "turning your back to them, and step deep so your hips are "
            "below theirs. Step 3: pull their sleeve arm tight across your "
            "chest and trap it. Step 4: straighten the legs explosively, "
            "lifting with the hips, not the back. Step 5: continue the "
            "rotation, throwing them forward over your shoulder. Step 6: "
            "keep the grip through the landing and follow into the "
            "hold-down."),
        "key_points": [
            "Pull them forward before you turn - no kuzushi, no throw",
            "Hips must finish below their hips",
            "Trap the sleeve arm across your chest",
            "Lift with the legs, never with the back",
            "Commit fully; a half turn is a counter invitation",
            "Follow the throw into the pin",
        ],
        "requirements": [
            "Strong legs and a conditioned lower back",
            "Reliable breakfalls - this is a big-amplitude throw",
            "Crash pad for first full-power repetitions",
            "A partner matched in size for learning",
        ],
        "standards": [
            "FIAS scoring for high-amplitude throws",
            "Civilian training safety: knees bent on entry, no back lifting",
        ],
        "citations": [CIT_KODOKAN, CIT_CHUMAKOV, CIT_JACQUES],
        "sig_lens": (
            "Signature lens: in the Signature system seoi nage is the "
            "wheel - the fighter becomes the axle and the opponent the "
            "rim. The Signature thrower turns completely, because a half "
            "turn is a promise half kept."),
    },
    {
        "key": "harai_goshi",
        "name": "Harai Goshi: Sweeping Hip Throw",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Harai goshi, the sweeping hip throw, loads the opponent onto "
            "the hip and sweeps their leg out with the attacker's leg in "
            "one motion. The hip is the fulcrum and the sweeping leg the "
            "lever - the opponent rotates over the hip while their support "
            "leg is removed. It is a powerful sambo throw against a stiff, "
            "upright opponent, and it transitions smoothly into side "
            "control."),
        "how_it_works": (
            "Step 1: pull the opponent forward and step in, turning the "
            "hips across their front. Step 2: load their weight onto your "
            "hip - your backside contacts their thighs. Step 3: swing your "
            "rear leg up and through, sweeping their leg at thigh or knee "
            "height. Step 4: bend forward at the waist, driving your upper "
            "body down while the leg sweeps. Step 5: keep pulling with the "
            "grips to rotate them over your hip. Step 6: stay on your feet "
            "through the landing for the maximum score, then take side "
            "control."),
        "key_points": [
            "The hip is the fulcrum - load them onto it fully",
            "Sweep at thigh or knee height, not at the ankle",
            "Bend at the waist as the leg sweeps",
            "Upper body pulls while the leg sweeps - two forces, one rotation",
            "Best against a stiff, upright opponent",
            "Stay standing through the landing",
        ],
        "requirements": [
            "Hip mobility and hamstring flexibility",
            "Seoi nage entries already comfortable",
            "A partner for loading drills",
            "Core strength for the forward bend under load",
        ],
        "standards": [
            "FIAS throw scoring",
            "Civilian training safety: sweep the leg, never kick the knee joint",
        ],
        "citations": [CIT_KODOKAN, CIT_CHUMAKOV, CIT_JACQUES],
        "sig_lens": (
            "Signature lens: in the Signature system harai goshi is the "
            "gate swinging on its hinge - the hip the post, the leg the "
            "gate, the opponent carried through the opening. The Signature "
            "fighter sweeps the support and the body follows."),
    },
    {
        "key": "uchi_mata",
        "name": "Uchi Mata: Inner Thigh Throw",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Uchi mata, the inner thigh throw, drives the attacker's leg up "
            "between the opponent's legs, lifting their inner thigh while "
            "the upper body pulls them forward over the top. It is one of "
            "the most dynamic throws in sambo, capable of huge amplitude "
            "from a single-leg lift, and it doubles as a setup: the threat "
            "of uchi mata opens the opponent for the outer reaps."),
        "how_it_works": (
            "Step 1: pull the opponent forward onto their toes with the "
            "grips. Step 2: step in deep and turn, bringing your hips "
            "across their front like a hip throw entry. Step 3: drive your "
            "rear leg up hard between their legs, thigh contacting their "
            "inner thigh. Step 4: hop or pivot on your support foot to "
            "stay balanced as you lift. Step 5: pull down and around with "
            "the grips, rotating them over your lifting leg. Step 6: "
            "control the landing and move to the hold-down."),
        "key_points": [
            "Drive the lifting leg up between their legs, thigh to inner thigh",
            "Pull them forward onto their toes first",
            "The support foot pivots to keep balance during the lift",
            "Upper body rotates them over the lifting leg",
            "Huge amplitude - commit fully",
            "Doubles as a setup for the outer reap family",
        ],
        "requirements": [
            "Hip flexor and adductor flexibility",
            "Single-leg balance on the support foot",
            "Breakfalls solid for high-amplitude landings",
            "A partner for lift-and-carry drills before throwing",
        ],
        "standards": [
            "FIAS scoring for high-amplitude throws",
            "Civilian training safety: lift with the thigh, never kick upward into the groin",
        ],
        "citations": [CIT_KODOKAN, CIT_CHUMAKOV, CIT_JACQUES],
        "sig_lens": (
            "Signature lens: in the Signature system uchi mata is the "
            "rising tide - the leg comes up between, the body goes over, "
            "and the mat receives what the tide carried. The Signature "
            "fighter lifts the inside and the outside has nowhere to go."),
    },
    {
        "key": "morote_gari",
        "name": "Morote Gari: Double Leg Takedown",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Morote gari, the double leg takedown, shoots in low, wraps "
            "both arms around the opponent's legs, and drives through them "
            "to lift and dump. It is the fundamental wrestling-style shot "
            "adapted to the sambo jacket: the grips convert to a leg "
            "clamp, the head stays tight to the hip, and the drive comes "
            "from the legs. Combat sambo fighters use it to take strikers "
            "down; sport sambo athletes use it against upright throwers."),
        "how_it_works": (
            "Step 1: from just outside gripping range, lower your level - "
            "hips drop, back straight. Step 2: step the lead foot between "
            "their feet and drop the rear knee to the mat. Step 3: wrap "
            "both arms around their legs above the knees, head tight to "
            "their hip, ear to their side. Step 4: drive forward off the "
            "rear leg, lifting their hips with your shoulder. Step 5: cut "
            "the corner - circle your feet as they fall to land in side "
            "control. Step 6: keep the head up throughout; a dropped head "
            "invites the counter."),
        "key_points": [
            "Level change first: hips drop, back stays straight",
            "Rear knee drops to the mat on the penetration step",
            "Head tight to the hip, never under their center",
            "Drive through them with the legs, lift with the shoulder",
            "Cut the corner as they fall to land in control",
            "Head up - a dropped head invites the sprawl and choke",
        ],
        "requirements": [
            "Knee pads or soft mats for the penetration step",
            "Explosive leg drive from the stance",
            "A partner for level-change drills",
            "Neck strength to keep the head positioned",
        ],
        "standards": [
            "FIAS rules on leg attacks and takedown scoring",
            "Civilian training safety: no driving the head into the mat",
        ],
        "citations": [CIT_CHUMAKOV, CIT_JACQUES, CIT_COMBAT_RULES],
        "sig_lens": (
            "Signature lens: in the Signature system morote gari is the "
            "tide coming in low - the level drops, the arms close like a "
            "gate, and the drive carries everything forward. The Signature "
            "fighter shoots under the storm and stands up with the sky."),
    },
    {
        "key": "sprawl",
        "name": "Sprawl and Takedown Defense",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The sprawl is the universal takedown defense: as the opponent "
            "shoots, the defender throws the hips and legs back, lands the "
            "chest heavy on the opponent's back and head, and circles to "
            "take the back or re-establish the stance. It converts the "
            "attacker's forward drive into a face-down sprawl under the "
            "defender's weight. Every sambo athlete drills the sprawl until "
            "it fires on reflex, because the shot always comes."),
        "how_it_works": (
            "Step 1: read the level change - the instant their hips drop, "
            "fire the sprawl. Step 2: throw both legs straight back, hips "
            "driving down to the mat, toes driving. Step 3: land your "
            "chest and hips heavy on their upper back and head, arms "
            "wrapping to control. Step 4: keep your weight on them - a "
            "light sprawl gets run through. Step 5: circle toward their "
            "back as they stall, or push the head down and stand back up. "
            "Step 6: drill with a partner shooting at increasing speed."),
        "key_points": [
            "Fire on the level change, not on contact",
            "Hips and legs go back and down in one motion",
            "Land heavy on their back and head",
            "Control with the arms; keep the weight on",
            "Circle to the back or stand back up - do not stay flat",
            "Drill until the sprawl is reflex",
        ],
        "requirements": [
            "Hip flexor explosiveness and core strength",
            "A partner to shoot progressively faster",
            "Mat space for full-extension sprawls",
            "Mouthguard for live takedown rounds",
        ],
        "standards": [
            "FIAS defensive conduct rules",
            "Civilian training safety: controlled shots in drills",
        ],
        "citations": [CIT_CHUMAKOV, CIT_JACQUES, CIT_COMBAT_RULES],
        "sig_lens": (
            "Signature lens: in the Signature system the sprawl is the "
            "mat itself rising up - the hips become ground, and the "
            "shooter discovers he has tackled the floor. The Signature "
            "fighter answers the drive with weight, not with wrestling."),
    },
    {
        "key": "kesa_gatame",
        "name": "Side Control: Kesa Gatame",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Kesa gatame, the scarf hold, is sambo's classic side-control "
            "pin: the attacker sits beside the opponent, wraps one arm "
            "around their head and grips their own body or the far arm, "
            "and pins the near arm with the chest. Under FIAS rules a "
            "20-second hold scores 4 points and ends the ground exchange "
            "in the attacker's favor. It is the first pin every sambo "
            "athlete learns because most throws land the fight exactly "
            "here."),
        "how_it_works": (
            "Step 1: from the throw, settle beside the opponent's torso, "
            "knees wide for base. Step 2: wrap your near arm around their "
            "head, hand gripping your own thigh or their far lapel. Step 3: "
            "pin their near arm against your chest with your body weight. "
            "Step 4: sit your hips low and heavy, chest expanded, weight "
            "driving through them into the mat. Step 5: keep your head up "
            "and watch their hips - the escape always starts there. Step 6: "
            "hold and ride their bridges; when they push, settle heavier."),
        "key_points": [
            "Arm around the head, near arm pinned to your chest",
            "Hips low and heavy, knees wide for base",
            "Weight drives through them into the mat",
            "Watch their hips - escapes start there",
            "Ride the bridge; settle heavier when they push",
            "20 seconds scores 4 points under FIAS rules",
        ],
        "requirements": [
            "Throw follow-ups already practiced",
            "A partner for hold-down timing drills",
            "A stopwatch for 10 and 20 second holds",
            "Chest and shoulder mobility for the wrap",
        ],
        "standards": [
            "FIAS hold-down scoring: 2 points at 10 seconds, 4 at 20",
            "Civilian training safety: no neck cranks from the hold",
        ],
        "citations": [CIT_KODOKAN, CIT_CHUMAKOV, CIT_FIAS],
        "sig_lens": (
            "Signature lens: in the Signature system kesa gatame is the "
            "scarf the Signature fighter wraps around the struggle - snug, "
            "heavy, and patient. The pin does not chase the escape; it "
            "waits, and the waiting is the technique."),
    },
    {
        "key": "mount",
        "name": "Mount Control: Tate Shiho Gatame",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The mount - tate shiho gatame, the vertical four-quarter hold "
            "is the dominant top position: the attacker sits on the "
            "opponent's torso, knees pinching their sides, weight settled "
            "through the hips. From the mount the attacker controls with "
            "gravity, and in combat sambo it is the platform for ground "
            "striking. Sambo teaches the mount as a riding position: low "
            "hips, wide knees, hands free, moving with the opponent's "
            "bridges instead of fighting them."),
        "how_it_works": (
            "Step 1: slide the knees up both sides of their torso and sit "
            "on their hips-to-chest, not high on the chest. Step 2: pinch "
            "the knees tight to their ribs and drop your weight through "
            "your hips. Step 3: keep your hands free - post on their chest "
            "or head when they bridge. Step 4: when they bridge, ride it: "
            "lift slightly and resettle, never stiffen. Step 5: grapevine "
            "the legs or cross the feet under their back to kill the "
            "bridge. Step 6: from the stabilized mount, attack the arms "
            "for submissions or hold for the pin points."),
        "key_points": [
            "Sit on the hips-to-chest, knees pinching the ribs",
            "Weight settles through the hips, not the hands",
            "Ride the bridge; never stiffen against it",
            "Grapevine the legs to kill bridging power",
            "Hands stay free for control and attacks",
            "The mount is a riding position, not a sitting one",
        ],
        "requirements": [
            "Hip escape and bridging already learned",
            "A partner for bridge-riding drills",
            "Knee and ankle mobility",
            "Core stability for the riding posture",
        ],
        "standards": [
            "FIAS hold-down and position rules",
            "Civilian training safety: no dropping weight onto the ribs",
        ],
        "citations": [CIT_KODOKAN, CIT_CHUMAKOV, CIT_JACQUES],
        "sig_lens": (
            "Signature lens: in the Signature system the mount is the "
            "rider and the storm - the Signature fighter sits the "
            "bridging like a horseman sits a bucking ride, loose where "
            "they heave and heavy where they settle."),
    },
    {
        "key": "back_control",
        "name": "Back Control and the Rear Choke",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Back control - both hooks in, seatbelt grip across the chest - "
            "is the most dominant position in grappling, and in combat "
            "sambo it is finished with the rear naked choke: the forearm "
            "across the throat, the other hand behind the head, squeezing "
            "the carotid arteries until the opponent submits. Note the "
            "rules boundary: chokes are banned in sport sambo and legal in "
            "combat sambo, so this technique is trained for combat sambo "
            "and self-defense contexts only. Control must be absolute "
            "before the choke is ever applied."),
        "how_it_works": (
            "Step 1: take the back during a scramble or from the turtle, "
            "sliding both hooks (feet) inside their thighs. Step 2: secure "
            "the seatbelt grip - one arm over their shoulder, one under "
            "their armpit, hands clasped at their chest. Step 3: keep your "
            "chest glued to their back, head behind their shoulder. Step 4: "
            "slide the choking arm under their chin, forearm across the "
            "throat, and grip your own biceps. Step 5: place the other hand "
            "behind their head and expand the chest, squeezing the sides of "
            "the neck - never crank the windpipe. Step 6: release instantly "
            "on the tap or at the first sign of distress."),
        "key_points": [
            "Both hooks in and seatbelt secured before any finish",
            "Chest to back, head behind their shoulder",
            "Forearm across the throat, grip your own biceps",
            "Squeeze the sides of the neck with chest expansion",
            "Chokes are combat-sambo legal, sport-sambo banned - know the rules",
            "Release instantly on the tap",
        ],
        "requirements": [
            "A trusted, experienced partner",
            "Explicit tap-out protocol agreed before drilling",
            "Instructor supervision for first choke applications",
            "Calm control - never apply a choke in anger or haste",
        ],
        "standards": [
            "FIAS Combat Sambo Rules: chokes permitted in combat sambo",
            "FIAS Sport Sambo Rules: chokes prohibited",
            "Civilian training safety: tap early, release instantly",
        ],
        "citations": [CIT_COMBAT_RULES, CIT_FIAS, CIT_JACQUES],
        "sig_lens": (
            "Signature lens: in the Signature system the back is the "
            "throne the Signature fighter earns, never steals - hooks and "
            "seatbelt first, the finish only when the kingdom is secure. "
            "The choke is applied with the gravity of a signature on a "
            "treaty: final, controlled, and released the moment it is "
            "acknowledged."),
    },
]

# ------------------------------------------------------------------ advanced
ENTRIES += [
    {
        "key": "armbar",
        "name": "Juji Gatame: Straight Armbar",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "Juji gatame, the straight armbar, hyperextends the elbow by "
            "trapping the arm between the legs, pinching the knees, and "
            "bridging the hips upward against the elbow joint. It is "
            "sambo's most versatile submission - attacked from the mount, "
            "side control, guard, and as a counter to the sprawl. The "
            "mechanics are pure leverage: the hips are the fulcrum, the "
            "legs the vise, and even a small bridge generates joint-"
            "breaking force, so control and the tap are everything."),
        "how_it_works": (
            "From the mount, step 1: trap their arm by pinning it to your "
            "chest as they push. Step 2: swing the leg over their head, "
            "sitting back so their arm is between your legs, thumb up. "
            "Step 3: pinch your knees tight together around their arm and "
            "pull their wrist to your chest. Step 4: keep their thumb "
            "pointing up - the elbow must face the ceiling. Step 5: bridge "
            "your hips slowly upward, raising their elbow with your hips, "
            "not yanking with your arms. Step 6: stop at the first "
            "resistance; in training the tap comes before pressure, and "
            "you release the instant it comes."),
        "key_points": [
            "Arm between the legs, thumb up, elbow facing the ceiling",
            "Knees pinched tight - the legs are the vise",
            "Pull the wrist to your chest before bridging",
            "Bridge the hips upward; never yank with the arms",
            "Attackable from mount, side control, guard, and counters",
            "In training the tap comes before pressure",
        ],
        "requirements": [
            "Mount and side control already solid",
            "A trusted partner with a clear tap protocol",
            "Slow, controlled application - speed kills joints",
            "Instructor supervision for first live applications",
        ],
        "standards": [
            "FIAS rules: painful holds on the elbow are legal submissions",
            "Civilian training safety: apply slowly, release on the tap",
        ],
        "citations": [CIT_KODOKAN, CIT_CHUMAKOV, CIT_JACQUES],
        "sig_lens": (
            "Signature lens: in the Signature system the armbar is the "
            "Signature lever - the whole body becomes a machine with one "
            "moving part, the hips. The Signature fighter does not break "
            "the arm; he demonstrates, with geometry, that it is already "
            "broken, and the tap is the opponent signing the proof."),
    },
    {
        "key": "kimura",
        "name": "Ude Garami: Kimura",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "Ude garami, the kimura, is a bent-arm shoulder lock: the "
            "attacker figures-fours their own hands around the opponent's "
            "wrist, pins the elbow to the body, and rotates the arm behind "
            "the back to attack the shoulder. Named in the West for "
            "Masahiko Kimura, it is a sambo staple from side control, the "
            "guard, and the standing clinch. The figure-four grip is the "
            "lock's engine - once it is set, the shoulder has nowhere to "
            "go."),
        "how_it_works": (
            "From side control, step 1: isolate their near arm as they "
            "push or reach. Step 2: thread your arm under theirs and grip "
            "your own wrist, forming the figure-four with their wrist "
            "trapped. Step 3: pin their elbow to your body so the shoulder "
            "cannot rotate free. Step 4: keeping the figure-four tight, "
            "rotate their hand toward their own back, lifting the elbow. "
            "Step 5: use your whole torso to turn, not just the arms. "
            "Step 6: apply slowly and release the instant they tap - the "
            "shoulder is a fragile joint."),
        "key_points": [
            "Figure-four grip: one hand grips your own wrist",
            "Pin their elbow to your body",
            "Rotate the hand behind their back with torso rotation",
            "The shoulder is fragile - apply slowly",
            "Works from side control, guard, and standing",
            "Once the figure-four is set, the escape window is tiny",
        ],
        "requirements": [
            "Side control and guard positions comfortable",
            "A trusted partner with tap protocol",
            "Shoulder mobility in the warm-up",
            "Slow application discipline",
        ],
        "standards": [
            "FIAS rules: painful holds on the shoulder are legal",
            "Civilian training safety: no cranking, release on tap",
        ],
        "citations": [CIT_KODOKAN, CIT_CHUMAKOV, CIT_JACQUES],
        "sig_lens": (
            "Signature lens: in the Signature system the kimura is the "
            "knot the Signature fighter ties in the opponent's own arm - "
            "the figure-four a signature looped twice. The shoulder, that "
            "proud ball in its socket, learns the geometry of the fold."),
    },
    {
        "key": "achilles",
        "name": "Achilles Lock: Straight Ankle Lock",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "The Achilles lock is sambo's signature leg lock: the attacker "
            "traps the opponent's foot in the armpit, wraps the forearm "
            "across the Achilles tendon, grips their own body, and bridges "
            "the hips to compress the tendon against the forearm bone. "
            "Sambo permits leg locks where many grappling arts restrict "
            "them, so the Achilles lock is the art's calling card - taught "
            "early in sambo groundwork, finished with control, and "
            "respected for how fast it injures when cranked."),
        "how_it_works": (
            "Step 1: from a leg entanglement, trap their foot deep in your "
            "armpit, toes pointed, their heel at your ribs. Step 2: wrap "
            "your forearm across their Achilles tendon, the bony edge of "
            "the forearm on the tendon. Step 3: grip your own lapel, "
            "biceps, or body to close the vise. Step 4: pinch your elbows, "
            "tuck their foot tight, and bridge your hips upward slowly to "
            "apply pressure. Step 5: keep their knee controlled so the "
            "force goes to the ankle, not the knee. Step 6: release the "
            "instant they tap - this lock damages quickly."),
        "key_points": [
            "Foot deep in the armpit, heel at the ribs",
            "Forearm bone across the Achilles tendon",
            "Bridge the hips slowly - pressure, not a yank",
            "Control their knee so force stays on the ankle",
            "Sambo's calling card: legal here, restricted elsewhere",
            "Releases instantly - this lock injures fast",
        ],
        "requirements": [
            "Leg entanglement entries already drilled",
            "A trusted, experienced partner",
            "Explicit tap protocol - verbal taps allowed",
            "Slow application discipline above all",
        ],
        "standards": [
            "FIAS rules: straight ankle locks are legal painful holds",
            "Civilian training safety: slowest application of any lock",
        ],
        "citations": [CIT_CHUMAKOV, CIT_JACQUES, CIT_FIAS],
        "sig_lens": (
            "Signature lens: in the Signature system the Achilles lock is "
            "the Signature seal pressed into the heel - the forearm a "
            "stamp, the tendon the wax. The Signature fighter finishes "
            "leg locks the way he signs his name: deliberately, once, and "
            "never twice on the same joint."),
    },
    {
        "key": "knee_bar",
        "name": "Knee Bar: Leg Bar Submission",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The knee bar hyperextends the knee: the attacker traps the "
            "opponent's leg between their own legs, hugs the thigh tight "
            "to the chest, and bridges the hips to straighten the knee "
            "past its limit. It is the leg-lock counterpart of the "
            "armbar - same lever logic, larger joint, higher stakes. Sambo "
            "competition allows it, so sambo athletes learn both the "
            "attack and the defense: the knee bar punishes anyone who "
            "leaves a leg extended in the scramble."),
        "how_it_works": (
            "Step 1: from a leg entanglement, thread your legs so their "
            "leg is trapped between yours, their knee at your hip line. "
            "Step 2: hug their thigh tight to your chest, hands clasped. "
            "Step 3: pinch your knees together and fall back slightly, "
            "keeping their foot controlled. Step 4: bridge your hips "
            "upward slowly, extending their knee with your whole body. "
            "Step 5: keep their toes pointed away so the force stays on "
            "the knee. Step 6: release instantly on the tap - knee "
            "injuries are career-ending."),
        "key_points": [
            "Their leg trapped between yours, knee at your hip line",
            "Hug the thigh to your chest, hands clasped",
            "Bridge the hips to extend the knee - whole-body leverage",
            "The armbar's logic applied to the larger knee joint",
            "Punishes extended legs in the scramble",
            "Release instantly - knee injuries end careers",
        ],
        "requirements": [
            "Achilles lock control already demonstrated",
            "An experienced, trusted partner",
            "Instructor supervision required",
            "Tap protocol with verbal taps",
        ],
        "standards": [
            "FIAS rules: knee bars are legal painful holds",
            "Civilian training safety: slowest possible application",
        ],
        "citations": [CIT_CHUMAKOV, CIT_JACQUES, CIT_FIAS],
        "sig_lens": (
            "Signature lens: in the Signature system the knee bar is the "
            "long lever of the ladder - the body's largest hinge met by "
            "the body's full bridge. The Signature fighter treats it with "
            "the gravity it demands: demonstrated, never detonated."),
    },
    {
        "key": "toe_hold",
        "name": "Toe Hold: Foot Lock",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The toe hold twists the foot: the attacker grips the "
            "opponent's toes, figures the hands around the foot and "
            "ankle, and rotates the foot outward while controlling the "
            "leg, torquing the ankle and the small joints of the foot. "
            "It is a rotational lock rather than a straight lever, which "
            "makes it subtle and dangerous - the damage arrives with "
            "little warning. Sambo teaches it as an advanced weapon, "
            "applied with extreme control."),
        "how_it_works": (
            "Step 1: control their leg fully - hip and knee pinned so only "
            "the foot can move. Step 2: grip their toes with one hand, "
            "palm over the top of the foot. Step 3: wrap the other arm "
            "around to complete the figure grip on the foot and ankle. "
            "Step 4: keeping their leg immobilized, rotate their toes "
            "outward and upward slowly, torquing the ankle. Step 5: use "
            "small, incremental pressure - the lock tightens fast. Step 6: "
            "release at the first tap or grimace; never chase a resisting "
            "toe hold."),
        "key_points": [
            "Control the whole leg - only the foot may move",
            "Grip the toes, figure the hands around foot and ankle",
            "Rotate outward slowly - rotational locks tighten fast",
            "Small incremental pressure, never a yank",
            "Subtle and dangerous: damage arrives with little warning",
            "Never chase a resisting toe hold",
        ],
        "requirements": [
            "All straight leg locks already controlled",
            "A highly trusted, experienced partner",
            "Instructor supervision required",
            "Verbal tap protocol",
        ],
        "standards": [
            "FIAS rules on foot locks in competition",
            "Civilian training safety: minimal pressure, instant release",
        ],
        "citations": [CIT_JACQUES, CIT_CHUMAKOV, CIT_FIAS],
        "sig_lens": (
            "Signature lens: in the Signature system the toe hold is the "
            "corkscrew of the ladder - rotation where the other locks "
            "are levers. The Signature fighter turns it the way he turns "
            "a key: a quarter turn tells him everything; he never needs "
            "the full twist."),
    },
    {
        "key": "combinations",
        "name": "Throwing Combinations: Renzoku Waza",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Renzoku waza is combination throwing: chaining two or three "
            "throws so the defense against the first becomes the setup for "
            "the second. The classic sambo chain is o soto gari to ko uchi "
            "gari to seoi nage - each attack herds the opponent's weight "
            "onto the leg the next attack reaps. Combinations are how "
            "advanced sambo is actually fought: single committed throws "
            "are rare at high level, but chains are constant."),
        "how_it_works": (
            "Step 1: attack with the first throw at full commitment - o "
            "soto gari, driving them back. Step 2: read their defense: "
            "when they step the leg back to avoid the reap, their weight "
            "shifts. Step 3: without pausing, switch to the second throw "
            "that attacks the new position - ko uchi gari on the retreating "
            "foot. Step 4: if they hop away from that, turn in for seoi "
            "nage as they land light. Step 5: keep the grips alive through "
            "every transition - dead grips kill chains. Step 6: drill the "
            "chain slowly with a cooperative partner, then at speed."),
        "key_points": [
            "The defense to the first throw sets up the second",
            "Classic chain: o soto gari to ko uchi gari to seoi nage",
            "Attack the leg their defense just moved",
            "Grips stay alive through every transition",
            "Each attack is full commitment, not a feint",
            "High-level sambo is fought in chains, not single shots",
        ],
        "requirements": [
            "All component throws already reliable",
            "A partner who defends realistically but safely",
            "Breakfalls solid for chained landings",
            "Mat space for multi-directional chains",
        ],
        "standards": [
            "FIAS competition conduct",
            "Civilian training safety: controlled defense, no counters at full speed yet",
        ],
        "citations": [CIT_CHUMAKOV, CIT_KODOKAN, CIT_JACQUES],
        "sig_lens": (
            "Signature lens: in the Signature system the combination is "
            "the sentence and each throw a word - the Signature fighter "
            "speaks in chains, and the opponent's defense is merely the "
            "punctuation that tells him where the next word goes."),
    },
    {
        "key": "counters",
        "name": "Counter Throwing: Kaeshi Waza",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Kaeshi waza is counter throwing: using the opponent's own "
            "attack as the kuzushi for your throw. When they drive in for "
            "o soto gari, you reap their reaping leg; when they turn for "
            "seoi nage, you ride the turn into ura nage. Counters demand "
            "the deepest timing in sambo - you must feel their commitment "
            "before it lands and add your technique to their momentum. "
            "The counter is the art's answer to aggression."),
        "how_it_works": (
            "Step 1: feel their attack developing - the grip pull, the "
            "step, the hip turn. Step 2: do not resist the direction of "
            "their force; yield just enough to let them commit. Step 3: at "
            "the instant of their commitment, apply your counter to their "
            "exposed structure - reap the reaping leg, ride the turning "
            "hips. Step 4: add your kuzushi to their momentum; the two "
            "forces sum. Step 5: follow through completely - a half "
            "counter becomes their throw. Step 6: drill with a partner "
            "attacking at increasing commitment, starting cooperative."),
        "key_points": [
            "Feel the attack before it lands",
            "Yield to their direction; add your force to theirs",
            "Counter their exposed structure, not their strength",
            "Timing is everything - a late counter is their throw",
            "Follow through completely",
            "The counter is the art's answer to aggression",
        ],
        "requirements": [
            "All major throws learned as attacks first",
            "A partner who attacks with real commitment",
            "Excellent breakfalls - counters are big throws",
            "A coach to referee timing at speed",
        ],
        "standards": [
            "FIAS rules on counter techniques and scoring",
            "Civilian training safety: cooperative commitment first",
        ],
        "citations": [CIT_KODOKAN, CIT_CHUMAKOV, CIT_JACQUES],
        "sig_lens": (
            "Signature lens: in the Signature system the counter is the "
            "echo that arrives before the shout - the Signature fighter "
            "does not block the wave, he surfs its crest and throws the "
            "ocean back at the swimmer."),
    },
    {
        "key": "striking_entries",
        "name": "Combat Sambo Striking Entries",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Combat sambo adds strikes, and the striking entry is how the "
            "combat sambist closes distance: a jab-cross or a low kick "
            "thrown not to finish but to occupy the guard and create the "
            "clinch or the shot. The strikes are the key that unlocks the "
            "grappling - thrown with the hands returning to guard and the "
            "hips ready to level-change the instant the opponent reacts. "
            "This is trained for combat sambo and self-defense contexts."),
        "how_it_works": (
            "Step 1: from striking range, step in behind a stiff jab, "
            "hand returning to guard. Step 2: follow with the cross as "
            "you continue stepping, closing the distance. Step 3: as the "
            "opponent covers up or retreats, level-change and secure the "
            "tie-up or shoot the double leg. Step 4: never admire the "
            "strikes - the entry is a bridge, not a destination. Step 5: "
            "keep the chin tucked and the off-hand guarding during the "
            "whole entry. Step 6: drill with a partner holding pads, then "
            "with a partner defending the entry."),
        "key_points": [
            "Strikes are the key; grappling is the door",
            "Hands return to guard after every strike",
            "Step in behind the strikes, closing distance continuously",
            "Level-change the instant they react",
            "Chin tucked, off-hand guarding throughout",
            "The entry is a bridge, not a destination",
        ],
        "requirements": [
            "Boxing fundamentals: jab, cross, guard",
            "Tie-up and morote gari already learned",
            "Focus mitts and a pad holder",
            "Mouthguard, headgear for live entries",
        ],
        "standards": [
            "FIAS Combat Sambo Rules: permitted strikes and entries",
            "Civilian training safety: controlled contact, protective gear",
        ],
        "citations": [CIT_COMBAT_RULES, CIT_JACQUES, CIT_CHUMAKOV],
        "sig_lens": (
            "Signature lens: in the Signature system the striking entry "
            "is the knock on the door before the Signature fighter walks "
            "in - the jab a polite announcement, the clinch the arrival. "
            "He strikes to enter, never to linger."),
    },
    {
        "key": "clinch_striking",
        "name": "Combat Sambo Clinch Striking",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Clinch striking is combat sambo's close-range artillery: "
            "knees to the body and thighs, short elbows, and uppercuts "
            "thrown from the tie-up while controlling the opponent's "
            "posture. The strikes and the throws feed each other - the "
            "knee makes them drop their hands and the throw follows, or "
            "the throw threat makes them posture up into the knee. It is "
            "trained with control on pads and in the clinch, for combat "
            "sambo contexts."),
        "how_it_works": (
            "Step 1: secure the clinch with head position and underhooks. "
            "Step 2: pull their posture down with the grip on the neck "
            "or jacket. Step 3: drive the knee straight up into the body "
            "or thigh, hips thrusting forward, standing tall on the "
            "support leg. Step 4: return the knee to the ground without "
            "losing the clinch - balance first. Step 5: mix short elbows "
            "and uppercuts when they posture up to stop the knees. Step 6: "
            "the instant they react to the strikes, hit the throw they "
            "opened."),
        "key_points": [
            "Control posture first; strikes second",
            "Knees driven up with hip thrust, standing tall",
            "Return the foot to base - never fall after the knee",
            "Elbows and uppercuts punish the upright posture",
            "Strikes and throws feed each other",
            "The throw follows the strike's reaction",
        ],
        "requirements": [
            "Tie-up and posture control already solid",
            "Thai pads and a holder for knee repetitions",
            "Mouthguard and headgear for clinch rounds",
            "Hip mobility for high knees",
        ],
        "standards": [
            "FIAS Combat Sambo Rules: permitted clinch strikes",
            "Civilian training safety: pads for power, control for partners",
        ],
        "citations": [CIT_COMBAT_RULES, CIT_JACQUES, CIT_CHUMAKOV],
        "sig_lens": (
            "Signature lens: in the Signature system the clinch is the "
            "forge and the knee the hammer - the Signature fighter holds "
            "the posture in the tongs and strikes the shape he wants. "
            "Every knee is a question; the throw is the answer."),
    },
    {
        "key": "kick_defense",
        "name": "Combat Sambo Kick Defense and Counters",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Kick defense in combat sambo blends the check, the catch, and "
            "the takedown: low kicks are checked with the shin or caught "
            "and converted to a dump, body kicks are absorbed on the arms "
            "while stepping in, and every caught kick is an invitation to "
            "the clinch or the double leg. The sambo answer to a kicker "
            "is to make the kick cost a takedown - after two catches, "
            "kickers stop kicking."),
        "how_it_works": (
            "Step 1: read the hip - the kick telegraphs at the hip "
            "before the leg moves. Step 2: for the low kick, lift the "
            "lead leg and check with the shin, turning the shin into the "
            "kick. Step 3: for the body kick, step in deep and catch it "
            "under the arm, pinning it to your ribs. Step 4: the instant "
            "the kick is caught, drive forward - dump them or run the "
            "double leg while they stand on one leg. Step 5: never back "
            "straight up from kicks; circle or step in. Step 6: drill "
            "with a partner kicking at increasing speed on pads first, "
            "then light contact."),
        "key_points": [
            "Read the hip - the kick telegraphs there first",
            "Check low kicks with the shin",
            "Catch body kicks and pin them to the ribs",
            "Every caught kick becomes a takedown",
            "Step in or circle - never back straight up",
            "Make the kick cost a takedown",
        ],
        "requirements": [
            "Sprawl and morote gari already learned",
            "Shin conditioning built gradually",
            "A partner for controlled kicking drills",
            "Mouthguard, shin guards for live rounds",
        ],
        "standards": [
            "FIAS Combat Sambo Rules: permitted kicks and defenses",
            "Civilian training safety: shin guards, controlled contact",
        ],
        "citations": [CIT_COMBAT_RULES, CIT_JACQUES, CIT_CHUMAKOV],
        "sig_lens": (
            "Signature lens: in the Signature system the caught kick is "
            "a gift the Signature fighter accepts with both hands - and "
            "returns as a takedown. The kicker learns the Signature "
            "arithmetic: every kick thrown is a throw owed."),
    },
    {
        "key": "ground_striking_defense",
        "name": "Ground Striking Defense in Combat Sambo",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Ground striking defense keeps a fighter safe when combat "
            "sambo goes to the mat with punches allowed: the guard "
            "becomes a shell - forearms shielding the face, hips active, "
            "constantly working to stand up, sweep, or submit rather than "
            "accepting punishment. The rule of the bottom is movement: a "
            "still guard gets hit, a moving guard creates escapes. This "
            "is trained for combat sambo and self-defense contexts with "
            "strict control."),
        "how_it_works": (
            "Step 1: from the bottom, build the shell - forearms vertical "
            "in front of the face, elbows tight, chin tucked. Step 2: keep "
            "the hips moving - shrimp, bridge, and re-guard constantly. "
            "Step 3: control one of their arms to limit the striking "
            "hand. Step 4: the instant they posture up to strike, "
            "attack - sweep, submit, or technical stand-up. Step 5: never "
            "lie flat and cover; flat is where strikes land. Step 6: "
            "drill with a partner throwing controlled strikes from the "
            "top while you work escapes."),
        "key_points": [
            "Build the shell: forearms up, elbows tight, chin tucked",
            "Hips never stop moving",
            "Control an arm to take away a striking hand",
            "Their posture-up is your attack window",
            "Sweep, submit, or stand - never just survive",
            "Flat on the back is where strikes land",
        ],
        "requirements": [
            "Guard, hip escape, and bridging already solid",
            "A controlled partner for strike-and-escape drills",
            "Mouthguard and headgear",
            "Strict no-power agreement in drills",
        ],
        "standards": [
            "FIAS Combat Sambo Rules: ground striking conduct",
            "Civilian training safety: light contact only in defense drills",
        ],
        "citations": [CIT_COMBAT_RULES, CIT_JACQUES, CIT_CHUMAKOV],
        "sig_lens": (
            "Signature lens: in the Signature system the bottom is not "
            "a grave but a workshop - the Signature fighter shells the "
            "storm and builds the escape inside it. Movement is the roof "
            "over his head; stillness is the rain coming through."),
    },
    {
        "key": "ura_nage",
        "name": "Ura Nage: Rear Throw",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Ura nage, the rear throw, is sambo's suplex: the attacker "
            "wraps the opponent's waist from the front, lifts them clean "
            "off the mat, arches backward, and throws them over the top "
            "to land on their back. It is the ultimate counter to the "
            "forward throw - when they turn in for seoi nage, the ura "
            "nage wraps the turn and reverses it. It demands real "
            "lifting strength and is drilled with crash pads before any "
            "live attempt."),
        "how_it_works": (
            "Step 1: as they turn in for their forward throw, wrap both "
            "arms tight around their waist, chest to their back, hips "
            "close. Step 2: drop your hips below theirs and lock your "
            "hands. Step 3: lift with the legs - deadlift them off the "
            "mat, keeping your back straight. Step 4: arch backward, "
            "throwing them up and over your own body. Step 5: turn with "
            "the throw so you land on top in side control. Step 6: this "
            "is a high-amplitude throw - crash pads and expert "
            "supervision until it is clean."),
        "key_points": [
            "Wrap the waist tight, chest to their back",
            "Hips below theirs before the lift",
            "Lift with the legs like a deadlift - back straight",
            "Arch back and throw them over the top",
            "The ultimate counter to the forward throw",
            "Crash pads and supervision until clean",
        ],
        "requirements": [
            "Deadlift-level leg and back strength",
            "Counter-throwing timing already developed",
            "Crash pads for all early repetitions",
            "Expert supervision - no solo learning",
        ],
        "standards": [
            "FIAS scoring for maximum-amplitude throws",
            "Civilian training safety: pads mandatory, controlled arch",
        ],
        "citations": [CIT_KODOKAN, CIT_CHUMAKOV, CIT_JACQUES],
        "sig_lens": (
            "Signature lens: in the Signature system ura nage is the "
            "Signature reversal - the opponent's own turn, borrowed and "
            "returned with interest. The Signature fighter lifts the "
            "storm and sets it down behind him, then stands where it "
            "stood."),
    },
    {
        "key": "fight_strategy",
        "name": "Sambo Fight Strategy: Game Planning",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Fight strategy is the capstone of the ladder: planning the "
            "bout around your best throws, your opponent's habits, the "
            "score, and the clock. The sambo strategist opens with "
            "probing combinations, attacks the opponent's weakest "
            "direction, manages the 8-point total-victory threshold, and "
            "knows when to chase the submission and when to ride the "
            "lead. Technique wins exchanges; strategy wins tournaments."),
        "how_it_works": (
            "Step 1: scout - identify the opponent's favorite throw and "
            "their weak side. Step 2: choose your two highest-percentage "
            "throws and the combination that links them. Step 3: open the "
            "bout with foot sweeps and grip fighting to read their "
            "reactions. Step 4: attack their weak direction relentlessly "
            "once it is confirmed. Step 5: manage the score - ahead by 6, "
            "protect the lead and hunt the 8-point total victory; behind, "
            "open up and chase the big throw or the lock. Step 6: drill "
            "the plan in situational rounds: down by 4 with a minute "
            "left, up by 6, tied in the last thirty seconds."),
        "key_points": [
            "Scout the opponent's favorite throw and weak side",
            "Two best throws plus the combination that links them",
            "Probe with sweeps and grips before committing",
            "Attack the confirmed weak direction",
            "Manage the score and the clock - 8 points ends it",
            "Technique wins exchanges; strategy wins tournaments",
        ],
        "requirements": [
            "Full technical ladder already learned",
            "Competition or hard-round experience",
            "A coach for scouting and cornering",
            "Video review of your own bouts",
        ],
        "standards": [
            "FIAS competition rules and scoring",
            "Civilian conduct: respect for opponents and officials",
        ],
        "citations": [CIT_FIAS, CIT_COMBAT_RULES, CIT_USA_SAMBO],
        "sig_lens": (
            "Signature lens: in the Signature system strategy is the "
            "Signature written across the whole bout - every exchange a "
            "letter, every round a word. The Signature fighter does not "
            "chase the fight; he authors it, and the scoreboard reads it "
            "back."),
    },
]
