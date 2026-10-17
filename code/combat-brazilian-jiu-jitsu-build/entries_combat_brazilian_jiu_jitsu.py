#!/usr/bin/env python3
"""Entries for the Brazilian Jiu-Jitsu Combat databases (combat batch 1).

Verified 2026-10-17 (combat batch 1): RAW SWEEP over the full manifest
plus every shard index title in jah-databases-data-1 plus the main-repo
data dir: zero 'combat-brazilian-jiu-jitsu*' slugs; zero title collisions
for 68 planned titles. One refusal: "Mount" collided with the dictionary
word entry "mount" - the record is titled "Mount Position" (CLEAR).
The paste's rule was applied by name/purpose/record schema/capabilities:
a ladder-ordered technique archive with step-by-step body mechanics,
drill timers, and training calculators is a distinct capability, so
BUILD NEW is the verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  combat-brazilian-jiu-jitsu            - The Brazilian Jiu-Jitsu Combat
                                         Database
                                         (public-harvest: real, fact-checked
                                         Brazilian jiu-jitsu technique -
                                         positions, escapes, guard passes,
                                         sweeps, joint locks, chokes,
                                         takedowns - every record carrying
                                         step-by-step how-to body mechanics;
                                         standard references Gracie R and
                                         Gracie R Brazilian Jiu-Jitsu:
                                         Theory and Technique 2001; Helio
                                         Gracie self-defense curriculum
                                         (Gracie University); Ribeiro S
                                         Jiu-Jitsu University 2008; the
                                         International Brazilian Jiu-Jitsu
                                         Federation Rule Book; and the
                                         classic Danaher/Renzo instructional
                                         lineage cited per record)
  combat-brazilian-jiu-jitsu-signature  - The Brazilian Jiu-Jitsu Combat
                                         Signature Database
                                         (his original Signature Combat
                                         Method: every position a covenant
                                         of balance, every escape an oath of
                                         return, every submission the
                                         handshake of control; src
                                         signature, titles suffixed
                                         " (Signature Edition)", never
                                         presented as authentic public
                                         record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBBJJ- (public) and JAH-CBBJJS- (signature), verified free
in the manifest id_prefix values and in every shard index file (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_brazilian_jiu_jitsu.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos before
commit.

Civilian martial-arts instruction only. Nothing hate-adjacent, profane, or
inappropriate; no religious talk. Standing exclusion honored: nothing on
neutralizing or defeating military or defense-grade systems.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Combat Method: "
            "every position a covenant of balance, every escape an oath of "
            "return, every submission the handshake of control. Clearly "
            "labeled Signature-made, never presented as authentic public "
            "record.")

CIT_GRACIE = ("Gracie R, Gracie R. Brazilian Jiu-Jitsu: Theory and Technique. "
              "Invisible Cities Press; 2001.")
CIT_HELIO = ("Gracie H. Gracie Jiu-Jitsu self-defense curriculum. "
             "Gracie University; Torrance, California.")
CIT_SAULO = ("Ribeiro S. Jiu-Jitsu University. Victory Belt Publishing; 2008.")
CIT_IBJJF = ("International Brazilian Jiu-Jitsu Federation. IBJJF Rule Book. "
             "v6.1; 2025.")
CIT_RENZO = ("Gracie R. Mastering Jiu-Jitsu. Human Kinetics; 2003.")
CIT_DANAHER = ("Danaher J. Go Further Faster instructional series. "
               "BJJ Fanatics; 2018-2021.")

ENTRIES = [
    {
        "key": "breakfall",
        "name": "Breakfall",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The breakfall is the first skill of Brazilian jiu-jitsu: how to hit "
            "the ground without injury. Every throw, sweep, and takedown ends "
            "with a fall, so the breakfall is drilled before anything else. The "
            "body spreads the impact across the forearm, the lat, and the leg, "
            "the chin tucks to protect the head, and the breath leaves the body "
            "on impact so the ribs stay loose. Done right, a hard throw lands "
            "with a loud slap and no pain."
        ),
        "how_it_works": (
            "Step 1: tuck the chin hard to the chest and never let the head touch "
            "the mat. Step 2: cross the arms over the chest and, as you fall, "
            "slap the whole arm - palm, forearm, and lat - flat against the mat "
            "at about 30 degrees from the body. Step 3: exhale sharply the instant "
            "you land so the diaphragm releases. Step 4: let the leg on the "
            "landing side absorb through the calf and thigh, never the knee or "
            "elbow. Step 5: drill forward rolls and side falls from kneeling, "
            "then standing, until the slap is automatic. The slap spreads force "
            "over a wide surface instead of one point."
        ),
        "key_points": [
            "Chin tucked to the chest on every fall, no exceptions",
            "Slap with the whole arm and lat, not the elbow or hand alone",
            "Exhale on impact to keep the ribs and diaphragm loose",
            "Never post with a straight arm or the wrist takes the fall",
            "Drill from kneeling before standing, standing before throws",
        ],
        "requirements": [
            "A matted surface with at least 1.5 inches of foam",
            "A partner or coach to check chin tuck and slap timing",
            "Loose clothing with nothing hard in the pockets",
        ],
        "standards": [
            "IBJJF: breakfalls are assumed fundamentals; no contest scoring applies",
            "Gracie curriculum: breakfalls are lesson one before any throw",
        ],
        "citations": [CIT_GRACIE, CIT_HELIO],
        "sig_lens": (
            "Signature lens: the fall is a covenant with the ground - the arm "
            "slaps the oath, the chin seals it, the breath releases it."
        ),
    },
    {
        "key": "hip_escape",
        "name": "Hip Escape",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The hip escape, called shrimping, is the engine of Brazilian "
            "jiu-jitsu. Nearly every escape on the ground is a hip escape in "
            "disguise: the hips slide away to make space while the frames hold "
            "the opponent back. The student lies on the side, posts the far "
            "hand, and drives the hips backward like a shrimp flicking its "
            "tail. Ten minutes of shrimping per class builds the movement that "
            "saves every bad position."
        ),
        "how_it_works": (
            "Step 1: turn onto your side, never flat on your back, and post the "
            "top hand flat on the mat to make a frame. Step 2: plant the top "
            "foot and the bottom knee, then push hard through the feet while "
            "pulling the hips backward. Step 3: the body slides away in an "
            "arc, creating a pocket of space between you and the opponent. "
            "Step 4: immediately replace the guard or insert the knee as a "
            "shield in the new space - never shrimp without filling the space "
            "behind it. Step 5: chain three to five shrimps in a row down the "
            "mat, keeping the frames up the whole way. The power comes from "
            "the legs, not the arms."
        ),
        "key_points": [
            "Always shrimp onto the side, never flat on the back",
            "Drive with the legs; the arms only frame and guard",
            "Fill the created space with a knee, foot, or guard instantly",
            "Keep the chin tucked and the far hand posted as a frame",
            "Chain shrimps continuously - one escape is rarely enough",
        ],
        "requirements": [
            "Open mat space of at least 10 meters for shrimping lines",
            "A partner providing light top pressure for resistance drills",
        ],
        "standards": [
            "IBJJF: no restriction; hip escapes are universal fundamentals",
            "Gracie curriculum: shrimping is the first movement drill taught",
        ],
        "citations": [CIT_GRACIE, CIT_SAULO],
        "sig_lens": (
            "Signature lens: the shrimp is the oath of return - the hips "
            "withdraw the covenant of space, the frames keep the promise."
        ),
    },
    {
        "key": "closed_guard",
        "name": "Closed Guard",
        "group": "Positions",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The closed guard is the home position of Brazilian jiu-jitsu: the "
            "bottom player wraps the legs around the opponent's waist and "
            "locks the ankles, controlling the posture with grips. From here "
            "the guard player attacks with sweeps and submissions while the "
            "top player must first break the guard. It is the position that "
            "proves leverage beats size - a smaller player can control a "
            "larger one entirely from the closed guard."
        ),
        "how_it_works": (
            "Step 1: wrap both legs around the opponent's waist, crossing the "
            "ankles behind their back or locking a figure-four. Step 2: pull "
            "the opponent's posture down with a cross-collar grip and a sleeve "
            "grip, keeping their head below your chest. Step 3: keep the hips "
            "angled slightly to one side so you can attack, never square and "
            "flat. Step 4: control one arm at a time - the arm you do not "
            "control is the arm that passes your guard. Step 5: attack in "
            "combination: threaten a sweep, and when they posture up, take "
            "the submission; threaten the submission, and when they defend, "
            "take the sweep."
        ),
        "key_points": [
            "Ankles locked tight; an open ankle is an invitation to pass",
            "Break the posture first - a postured opponent is safe from attacks",
            "Stay on a hip, angled, never flat on the back",
            "Control one arm; the free arm is the danger arm",
            "Attack in combinations: sweep threat opens submissions",
        ],
        "requirements": [
            "A training partner willing to work guard passing rounds",
            "Grips conditioned by regular sleeve and collar gripping",
        ],
        "standards": [
            "IBJJF: guard is a neutral position; sweeps from guard score 2 points",
            "Gracie curriculum: closed guard is the first guard taught",
        ],
        "citations": [CIT_GRACIE, CIT_SAULO],
        "sig_lens": (
            "Signature lens: the closed guard is the first covenant of "
            "control - the legs seal the agreement, the grips enforce it."
        ),
    },
    {
        "key": "mount_position",
        "name": "Mount Position",
        "group": "Positions",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The mount is the most dominant position in Brazilian jiu-jitsu: "
            "sitting on the opponent's torso with knees pinching their sides "
            "and feet hooked under their legs. From the mount the top player "
            "controls all the weapons - strikes in a real fight, submissions "
            "in sport - while the bottom player can only defend and escape. "
            "It scores 4 points in IBJJF competition and is the position "
            "every beginner learns to hold before learning to attack from it."
        ),
        "how_it_works": (
            "Step 1: settle the hips low on the opponent's torso, below the "
            "chest, with the knees pinched tight against their ribs. Step 2: "
            "hook the feet under their legs or grapevine to kill the hip "
            "escape. Step 3: keep the hands posted wide on the mat or on their "
            "biceps, staying heavy through the hips. Step 4: when they bridge, "
            "ride it like a wave - post the hands and let the hips float, "
            "never stiffen. Step 5: when they turn to a side, take the "
            "technical mount, sliding the knee up by their head and keeping "
            "the other foot hooked. Attack only when the position is stable."
        ),
        "key_points": [
            "Hips low and heavy; high hips get bucked off",
            "Knees pinched, feet hooked - no space at the hips",
            "Ride the bridge, do not fight it with stiffness",
            "Switch to technical mount when they turn to a side",
            "Position before submission: secure the mount first",
        ],
        "requirements": [
            "Hip mobility for low, heavy mount posture",
            "A partner for bridge-and-roll escape drilling",
        ],
        "standards": [
            "IBJJF: mount held 3 seconds scores 4 points",
            "Gracie curriculum: mount is taught as the primary dominant position",
        ],
        "citations": [CIT_GRACIE, CIT_IBJJF],
        "sig_lens": (
            "Signature lens: the mount is the covenant of weight - the hips "
            "sign it, the hooks witness it, the patience collects it."
        ),
    },
    {
        "key": "side_control",
        "name": "Side Control",
        "group": "Positions",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Side control is chest-to-chest dominance from the side: the top "
            "player pins the opponent's torso with the chest, blocks the near "
            "hip with a knee, and controls the far arm and head. It is the "
            "great transition position - submissions flow from it, the mount "
            "and back are one step away, and the bottom player burns energy "
            "just surviving. Holding side control for 3 seconds scores points "
            "in IBJJF competition."
        ),
        "how_it_works": (
            "Step 1: drop the chest onto the opponent's chest, driving the "
            "shoulder into their jawline to turn their head away. Step 2: "
            "block the near hip with the knee and sprawl the far leg wide for "
            "base. Step 3: control the far arm - underhook it, pin the wrist, "
            "or trap it with the head. Step 4: stay heavy through the chest, "
            "not the arms; let gravity do the pinning. Step 5: when they turn "
            "in, take the mount; when they turn away, take the back; when they "
            "push, take the far-side armbar or americana. Move with their "
            "escape attempts instead of clamping down."
        ),
        "key_points": [
            "Chest to chest, shoulder in the jaw to kill their frames",
            "Near hip blocked, far leg sprawled for an immovable base",
            "Control the far arm - it is their best escape tool",
            "Stay heavy through the chest, relaxed through the arms",
            "Follow their turn: in means mount, away means back",
        ],
        "requirements": [
            "Chest and shoulder pressure conditioning",
            "A partner drilling bridge, shrimp, and turn escapes",
        ],
        "standards": [
            "IBJJF: side control held 3 seconds scores 3 points",
            "Gracie curriculum: side control is the core pinning position",
        ],
        "citations": [CIT_GRACIE, CIT_SAULO, CIT_IBJJF],
        "sig_lens": (
            "Signature lens: side control is the covenant of pressure - the "
            "chest signs in weight, the shoulder seals the jaw."
        ),
    },
    {
        "key": "bridge_roll",
        "name": "Bridge and Roll Escape",
        "group": "Escapes",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The bridge and roll, called the upa, is the first mount escape: "
            "the bottom player traps one arm and one leg of the mounted "
            "opponent, bridges the hips high, and rolls them over. It uses "
            "the strongest muscles in the body - the glutes and hips - against "
            "the opponent's balance, not their strength. Every beginner "
            "learns it in the first week because the mount is where beginners "
            "end up most."
        ),
        "how_it_works": (
            "Step 1: trap one of their arms against your chest with both of "
            "your arms, and trap the foot on the same side by stepping your "
            "foot over it. Step 2: bridge your hips as high as possible, "
            "driving through the trapped-side foot. Step 3: at the top of the "
            "bridge, turn your head to look toward the trapped side and roll "
            "over your shoulder. Step 4: keep the arm trapped tight through "
            "the whole roll - if it escapes, they post and you fail. Step 5: "
            "land in their guard or in mount yourself, and immediately "
            "establish posture. Timing beats strength: bridge when they are "
            "settling or reaching, not when they are braced."
        ),
        "key_points": [
            "Trap the arm AND the leg on the same side before bridging",
            "Bridge straight up first, then roll - never roll without height",
            "Look toward the trapped side to steer the roll",
            "Keep the trapped arm pinned through the entire motion",
            "Bridge when they settle or reach, not when they are braced",
        ],
        "requirements": [
            "Hip and glute strength for a high bridge",
            "A partner giving honest mount pressure",
        ],
        "standards": [
            "IBJJF: escapes score nothing, but the reversal can earn sweep points",
            "Gracie curriculum: the upa is the first escape taught",
        ],
        "citations": [CIT_GRACIE, CIT_HELIO],
        "sig_lens": (
            "Signature lens: the upa is the oath of return - the hips rise "
            "to collect what the mount borrowed."
        ),
    },
    {
        "key": "standup_base",
        "name": "Stand Up in Base",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Standing up in base is the safe way to rise from the ground in "
            "Brazilian jiu-jitsu: one hand posts behind, one foot plants, the "
            "free hand guards the face, and the fighter stands without ever "
            "turning the back or dropping the hands. It is the Gracie "
            "self-defense stand-up, drilled so that getting off the floor "
            "never means getting knocked down again. Every sparring round "
            "ends with both partners standing in base."
        ),
        "how_it_works": (
            "Step 1: from a seated position, post one hand on the mat behind "
            "you and plant the same-side foot flat. Step 2: bring the other "
            "hand up to guard the face, elbow tucked. Step 3: push through "
            "the posted hand and the planted foot to lift the hips. Step 4: "
            "swing the back leg through to standing in one motion, keeping "
            "the guard hand up the whole time. Step 5: finish in a staggered "
            "fighting stance, hands up, never having turned your back. Drill "
            "it at speed until the hands never drop."
        ),
        "key_points": [
            "One hand posts, one hand guards the face at all times",
            "Never turn the back or look away while standing",
            "Push through the posted hand and planted foot together",
            "Finish in a staggered stance, ready to move",
            "Drill to speed until dropping the hands feels wrong",
        ],
        "requirements": [
            "Open mat space to stand without hitting anyone",
            "A partner to add light pressure in later drills",
        ],
        "standards": [
            "Gracie curriculum: the technical stand-up is core self-defense",
            "IBJJF: no scoring; it is a transition skill",
        ],
        "citations": [CIT_HELIO, CIT_GRACIE],
        "sig_lens": (
            "Signature lens: standing in base is the covenant of readiness - "
            "the ground releases you only when the guard is up."
        ),
    },
    {
        "key": "posture_guard",
        "name": "Posture in Closed Guard",
        "group": "Positions",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Posture in the closed guard is the top player's survival skill: "
            "sitting up tall with a straight spine, head up, hands controlling "
            "the opponent's hips or biceps, so the guard player cannot break "
            "you down to attack. Good posture makes the closed guard a "
            "stalemate the top player can eventually pass; bad posture makes "
            "it a submission waiting to happen. Beginners lose from the top "
            "of the guard more than from anywhere else."
        ),
        "how_it_works": (
            "Step 1: sit tall with the spine straight and the head up, like a "
            "string pulling the crown of the head to the ceiling. Step 2: "
            "place both hands on the opponent's hips or biceps to manage "
            "distance - never let both hands get controlled at once. Step 3: "
            "keep the knees wide and the weight back so the hips stay heavy. "
            "Step 4: if they pull you down, post one hand on the mat and "
            "drive the hips back to rebuild posture - never fight the pull "
            "with the neck. Step 5: once posture is stable, begin the guard "
            "break: stand, or open the knees against their legs."
        ),
        "key_points": [
            "Spine tall, head up - posture is a straight line, not a lean",
            "Hands manage distance on hips or biceps, never both trapped",
            "Knees wide, weight back, hips heavy",
            "Rebuild posture with a post and hip drive, not neck strength",
            "Stable posture first, guard break second",
        ],
        "requirements": [
            "Core and hip flexor conditioning for tall sitting",
            "A partner actively trying to break posture down",
        ],
        "standards": [
            "Gracie curriculum: posture is the first lesson inside the guard",
            "IBJJF: posture itself scores nothing; it enables the pass",
        ],
        "citations": [CIT_GRACIE, CIT_SAULO],
        "sig_lens": (
            "Signature lens: posture is the covenant of the spine - tall and "
            "unbroken, it holds the guard at bay."
        ),
    },
    {
        "key": "guard_break_standing",
        "name": "Guard Break from Standing",
        "group": "Guard Passes",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The standing guard break is the simplest reliable way out of the "
            "closed guard: the top player gets tall posture, controls the "
            "hips, stands up, and pries the guard open with the knee and "
            "hands. Gravity and leg strength do the work the arms cannot. It "
            "is the first guard pass taught because it works against almost "
            "everyone and teaches the principle that passes start with "
            "posture, not speed."
        ),
        "how_it_works": (
            "Step 1: establish tall posture with both hands controlling the "
            "opponent's hips. Step 2: bring one foot up to stand, keeping the "
            "other knee down for base, hands still pinning the hips. Step 3: "
            "stand fully, driving the hips forward so the opponent's weight "
            "hangs on your legs. Step 4: wedge one knee into the tailbone "
            "area and press down with both hands on their knees, prying the "
            "ankles apart. Step 5: the instant the guard opens, step back "
            "and establish a passing position - combat base or standing - "
            "before they re-guard. Never let the hands get stuck inside."
        ),
        "key_points": [
            "Posture first: never stand while broken down",
            "Control the hips with both hands through the whole stand",
            "Wedge the knee and pry with the hands, not the arms alone",
            "The moment the guard opens, disengage to a passing stance",
            "Keep the elbows tight so they cannot trap an arm",
        ],
        "requirements": [
            "Leg strength to stand with the opponent's weight on you",
            "A partner with an active, attacking closed guard",
        ],
        "standards": [
            "IBJJF: opening the guard scores nothing; the pass scores 3 points",
            "Gracie curriculum: the standing break is the first guard break",
        ],
        "citations": [CIT_GRACIE, CIT_HELIO],
        "sig_lens": (
            "Signature lens: the standing break is the covenant of height - "
            "rise tall and the guard must let go."
        ),
    },
    {
        "key": "scissor_sweep",
        "name": "Scissor Sweep",
        "group": "Sweeps",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The scissor sweep is the classic first sweep of Brazilian "
            "jiu-jitsu: from the closed guard, the legs open like scissors "
            "while the grips pull the opponent across, tipping them over "
            "into mount. It teaches the sweep formula - off-balance, then "
            "redirect - that every later sweep follows. In IBJJF competition "
            "a sweep from the guard scores 2 points."
        ),
        "how_it_works": (
            "Step 1: from closed guard, grip the same-side sleeve and the "
            "opposite collar, and open the guard. Step 2: place the top foot "
            "on the mat by their hip as a block and swing the bottom leg "
            "across their far hip like a scissor blade. Step 3: pull hard "
            "with both grips to load their weight onto the blocking foot's "
            "side. Step 4: scissor the legs - top leg chops down, bottom leg "
            "sweeps across - while driving with the grips. Step 5: follow "
            "them over and settle into the mount, establishing posture "
            "before they can scramble. The sweep fails if the grips do not "
            "off-balance them first."
        ),
        "key_points": [
            "Off-balance with the grips before the legs ever move",
            "Block the near hip with the top foot planted on the mat",
            "Scissor the legs in opposite directions with commitment",
            "Follow through to the mount and stabilize immediately",
            "Keep the collar grip deep so they cannot posture out",
        ],
        "requirements": [
            "Sleeve and collar grips strong enough to off-balance a partner",
            "Hip mobility to swing the bottom leg across cleanly",
        ],
        "standards": [
            "IBJJF: sweeps from guard to top position score 2 points",
            "Gracie curriculum: the scissor sweep is the first sweep taught",
        ],
        "citations": [CIT_GRACIE, CIT_SAULO, CIT_IBJJF],
        "sig_lens": (
            "Signature lens: the scissor sweep is the covenant of the blades "
            "- two legs sign the fall, the grips deliver it."
        ),
    },
    {
        "key": "hip_bump_sweep",
        "name": "Hip Bump Sweep",
        "group": "Sweeps",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The hip bump sweep punishes the opponent who postures up too "
            "tall in your guard: you sit up, block their far arm, and drive "
            "your hips into them like a battering ram, tipping them backward "
            "into the mount. It is the fundamental answer to good posture - "
            "the better they posture, the harder they fall. Every guard "
            "player pairs it with the triangle and kimura in the classic "
            "beginner combination."
        ),
        "how_it_works": (
            "Step 1: from closed guard, wait for or force them to posture up "
            "tall. Step 2: sit up sharply, sliding your hips under their "
            "chest and blocking their far arm with your hand. Step 3: wrap "
            "your near arm around their back or far lat for control. Step 4: "
            "drive the hips forward and up in one explosive bump, tipping "
            "them over backward. Step 5: follow to the mount and base out "
            "wide. If they post the free hand to stop the sweep, that hand "
            "is now the kimura or the triangle setup - the combination is "
            "the technique."
        ),
        "key_points": [
            "Their tall posture is the trigger - posture up means sweep",
            "Sit the hips deep under their chest before bumping",
            "Block the far arm so they cannot base out",
            "Explode once, fully committed - half bumps get stuffed",
            "The posted hand they save themselves with becomes the kimura",
        ],
        "requirements": [
            "Explosive hip drive from the seated position",
            "A partner who postures realistically in the guard",
        ],
        "standards": [
            "IBJJF: sweeps from guard score 2 points",
            "Gracie curriculum: hip bump pairs with kimura and guillotine basics",
        ],
        "citations": [CIT_GRACIE, CIT_SAULO],
        "sig_lens": (
            "Signature lens: the hip bump is the covenant of the tall - rise "
            "too proud and the hips collect the debt."
        ),
    },
    {
        "key": "americana",
        "name": "Americana",
        "group": "Joint Locks",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The americana is the first joint lock most students learn: from "
            "side control or mount, the opponent's arm is bent in an L, the "
            "wrist is pinned, and the elbow is lifted like a paintbrush to "
            "pressure the shoulder. It attacks the shoulder joint with a "
            "slow, controllable pressure that gives the partner plenty of "
            "time to tap. It is the classic demonstration that technique, "
            "not strength, finishes joint locks."
        ),
        "how_it_works": (
            "Step 1: from side control, isolate the far arm and fold it so "
            "the hand points toward their own hip, elbow bent at 90 degrees. "
            "Step 2: pin their wrist to the mat with your hand, keeping your "
            "elbow tight to your ribs. Step 3: slide your other hand under "
            "their elbow and grip your own wrist, making a figure of control. "
            "Step 4: lift their elbow toward the ceiling like a paintbrush "
            "while keeping the wrist pinned - the shoulder rotates under "
            "pressure. Step 5: apply slowly and release the instant they tap. "
            "Never yank; the lock works with steady pressure."
        ),
        "key_points": [
            "Wrist pinned flat, elbow at 90 degrees before pressure",
            "Keep your elbows tight to your own ribs for control",
            "Lift the elbow like a paintbrush - slow and steady",
            "Control the body first so they cannot roll out",
            "Release instantly on the tap, every time",
        ],
        "requirements": [
            "A partner who taps early and honestly",
            "Shoulder mobility awareness - never force past resistance",
        ],
        "standards": [
            "IBJJF: legal at all belt levels, gi and no-gi",
            "Gracie curriculum: the americana is the first shoulder lock",
        ],
        "citations": [CIT_GRACIE, CIT_SAULO, CIT_IBJJF],
        "sig_lens": (
            "Signature lens: the americana is the covenant of the brush - "
            "painted slow, the shoulder signs its surrender."
        ),
    },
    {
        "key": "kimura",
        "name": "Kimura",
        "group": "Joint Locks",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The kimura is the figure-four shoulder lock named after Masahiko "
            "Kimura, who used it to defeat Helio Gracie in 1951: the "
            "attacker's arms form a figure-four around the opponent's bent "
            "arm, rotating the shoulder behind the back. It works from the "
            "guard, side control, mount, and the back, making it one of the "
            "most versatile submissions in the art. Control the grip and you "
            "control the person."
        ),
        "how_it_works": (
            "Step 1: isolate the arm and thread your arm through, gripping "
            "your own wrist to form the figure-four, their bent arm trapped "
            "inside. Step 2: keep their elbow pinned to your body - the lock "
            "dies if the elbow floats free. Step 3: rotate their hand toward "
            "their own back, cranking the shoulder with your whole torso, "
            "not just the arms. Step 4: step over or adjust your hips to keep "
            "their body from following the rotation. Step 5: finish with slow, "
            "heavy pressure and release on the tap. The power is in the hip "
            "rotation and the tight figure-four, never in yanking the wrist."
        ),
        "key_points": [
            "Figure-four locked tight before any rotation starts",
            "Pin their elbow to your body - a free elbow escapes",
            "Rotate with the torso and hips, not the arms alone",
            "Keep their body from turning with the crank",
            "Slow pressure, instant release on the tap",
        ],
        "requirements": [
            "Grip strength to maintain the figure-four under resistance",
            "A partner who taps to shoulder pressure early",
        ],
        "standards": [
            "IBJJF: legal at all belt levels, gi and no-gi",
            "Gracie curriculum: named for the 1951 Kimura vs Helio Gracie match",
        ],
        "citations": [CIT_GRACIE, CIT_RENZO, CIT_IBJJF],
        "sig_lens": (
            "Signature lens: the kimura is the covenant of the figure-four - "
            "four limbs sign one agreement the shoulder cannot refuse."
        ),
    },
    {
        "key": "rear_naked_choke",
        "name": "Rear Naked Choke",
        "group": "Chokes",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The rear naked choke is the most reliable submission in "
            "Brazilian jiu-jitsu and the definitive back attack: from behind, "
            "one arm slides under the chin, the hand grips the opposite "
            "biceps, the other hand locks behind the head, and the elbows "
            "pinch to compress both carotid arteries. Unconsciousness follows "
            "in seconds when it is locked correctly. The back is the safest "
            "place to attack from because the opponent cannot see the choke "
            "coming."
        ),
        "how_it_works": (
            "Step 1: from back control with both hooks in, slide the choking "
            "arm under the chin, palm facing you. Step 2: grip your own "
            "opposite biceps with the choking hand. Step 3: place the free "
            "hand behind their head, locking the triangle of arms around the "
            "neck. Step 4: expand the chest, pull the elbows down and pinch "
            "them together, and drive the head-side shoulder forward. Step 5: "
            "hold steady pressure - do not crank the neck - and release the "
            "instant they tap or go limp, then lay them on their side. The "
            "choke compresses the carotids on the sides of the neck, not the "
            "windpipe."
        ),
        "key_points": [
            "Choking arm deep under the chin, biceps grip locked",
            "Free hand behind the head completes the triangle",
            "Pinch the elbows and expand the chest - squeeze, do not crank",
            "It is a blood choke on the carotids, not a windpipe crush",
            "Release instantly on tap or limpness; lay them on their side",
        ],
        "requirements": [
            "Back control with hooks or a body triangle established first",
            "A partner who taps early to chokes without fail",
        ],
        "standards": [
            "IBJJF: legal at all belt levels, gi and no-gi",
            "Gracie curriculum: the rear naked choke is the primary back submission",
        ],
        "citations": [CIT_GRACIE, CIT_HELIO, CIT_IBJJF],
        "sig_lens": (
            "Signature lens: the rear naked choke is the covenant of the "
            "unseen - signed behind the back, collected in seconds."
        ),
    },
    {
        "key": "cross_collar_choke",
        "name": "Cross-Collar Choke",
        "group": "Chokes",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The cross-collar choke is the signature submission of the gi: "
            "from the closed guard or mount, both hands grip deep in opposite "
            "collars and the wrists scissor against the carotids. It is one "
            "of the first submissions Helio Gracie taught because it proves "
            "the gi itself is a weapon. The choke works with almost no "
            "strength once the grips are deep - the cloth does the work."
        ),
        "how_it_works": (
            "Step 1: from closed guard, open the opponent's collar with one "
            "hand and feed it deep to the other hand, gripping four fingers "
            "inside at the ear level. Step 2: the second hand grips the "
            "opposite collar the same way, thumbs inside, wrists straight. "
            "Step 3: pull the elbows down to the ribs and flare them out, "
            "scissoring the wrists against the sides of the neck. Step 4: "
            "close the guard tight and crunch forward, driving the chest "
            "into them as the wrists cut. Step 5: hold the scissor - the "
            "carotids compress under the crossed cloth - and release on the "
            "tap. Deep grips at the start decide everything."
        ),
        "key_points": [
            "Grips four fingers deep at ear level, thumbs inside",
            "Elbows drop to the ribs and flare to scissor the wrists",
            "Break their posture down before finishing",
            "The gi cloth compresses the carotids - strength is secondary",
            "Release on the tap; never hold a finished choke",
        ],
        "requirements": [
            "A gi with a sturdy collar for realistic grip training",
            "Grip endurance for deep collar control",
        ],
        "standards": [
            "IBJJF: legal at all belt levels in the gi",
            "Gracie curriculum: the cross-collar choke is the first gi choke",
        ],
        "citations": [CIT_GRACIE, CIT_HELIO, CIT_IBJJF],
        "sig_lens": (
            "Signature lens: the cross-collar choke is the covenant of the "
            "cloth - the gi itself witnesses and enforces."
        ),
    },
    {
        "key": "armbar_mount",
        "name": "Armbar from Mount",
        "group": "Joint Locks",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The armbar from mount is the classic finishing sequence of "
            "Brazilian jiu-jitsu: the mounted attacker traps an arm, swings "
            "the leg over the head, and falls back to hyperextend the elbow "
            "over the hips. It is the submission most associated with the "
            "art - a smaller person breaking the arm of a larger one with "
            "pure leverage. The hips are the fulcrum; the whole body is the "
            "lever."
        ),
        "how_it_works": (
            "Step 1: from mount, trap one arm against your chest when they "
            "push on you, pinning it tight. Step 2: slide the knee of the "
            "trapping side up by their head and swing the other leg over "
            "their face, sitting back to the mat. Step 3: pinch the knees "
            "tight around their shoulder and arm, keeping their thumb pointed "
            "up. Step 4: pull their wrist to your chest and bridge the hips "
            "up into the elbow - the joint extends over your hips as the "
            "fulcrum. Step 5: apply pressure slowly with the hips, never the "
            "arms, and release the instant they tap. Keep the arm controlled "
            "through the whole fall so they cannot stack you."
        ),
        "key_points": [
            "Pin the arm to your chest before the leg ever swings",
            "Knees pinched tight on the shoulder - no space",
            "Thumb up, wrist pulled to your chest",
            "Hips bridge into the elbow; the arms only hold",
            "Slow hip pressure, instant release on the tap",
        ],
        "requirements": [
            "Hip mobility to swing the leg over cleanly",
            "A partner who taps to elbow pressure immediately",
        ],
        "standards": [
            "IBJJF: legal at all belt levels, gi and no-gi",
            "Gracie curriculum: the armbar is the core elbow attack",
        ],
        "citations": [CIT_GRACIE, CIT_SAULO, CIT_IBJJF],
        "sig_lens": (
            "Signature lens: the armbar is the covenant of the lever - the "
            "hips sign as fulcrum, the body as the bar."
        ),
    },
    {
        "key": "triangle_choke",
        "name": "Triangle Choke",
        "group": "Chokes",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The triangle choke is the most iconic guard submission: the legs "
            "form a triangle around the opponent's neck and one arm, and the "
            "squeeze compresses a carotid against their own shoulder. It "
            "turns the guard player's legs - the strongest limbs on the body "
            "- into a finishing weapon. Beginners drill it endlessly because "
            "the setup teaches angle, timing, and hip movement all at once."
        ),
        "how_it_works": (
            "Step 1: from closed guard, control one arm and pull it across "
            "as they posture up, opening the angle by sliding your hips out "
            "to the side. Step 2: throw the leg over their shoulder, shin "
            "across the back of the neck. Step 3: lock the triangle by "
            "tucking the foot under the opposite knee, ankle locked tight. "
            "Step 4: pull down on the head and lift the hips, adjusting the "
            "angle so the choking leg's calf presses their carotid against "
            "their own trapped shoulder. Step 5: squeeze the knees together "
            "and hold - release on the tap. The angle makes the choke; "
            "straight-on triangles rarely finish."
        ),
        "key_points": [
            "Create the angle by sliding the hips out - never triangle straight on",
            "One arm in, one arm out; two arms in means re-adjust",
            "Lock the ankle under the knee, shin across the neck",
            "Pull the head down and lift the hips to finish",
            "The trapped shoulder becomes part of the choke",
        ],
        "requirements": [
            "Hip flexibility to lock the triangle comfortably",
            "A partner who taps to chokes early and reliably",
        ],
        "standards": [
            "IBJJF: legal at all belt levels, gi and no-gi",
            "Gracie curriculum: the triangle is the core guard submission",
        ],
        "citations": [CIT_GRACIE, CIT_SAULO, CIT_IBJJF],
        "sig_lens": (
            "Signature lens: the triangle is the covenant of three sides - "
            "leg, leg, and shoulder sign together."
        ),
    },
    {
        "key": "elbow_escape_mount",
        "name": "Elbow Escape from Mount",
        "group": "Escapes",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The elbow escape is the technical answer to the mount when the "
            "bridge and roll fails: the bottom player bridges to unweight "
            "one side, shrimps the hips out, and walks the elbows back to "
            "feed a knee through, recovering the guard inch by inch. It is "
            "the escape that works against good mount riders who cannot be "
            "thrown. Patience is the technique - each cycle gains a few "
            "inches until the guard is back."
        ),
        "how_it_works": (
            "Step 1: bridge hard to one side to unweight their hip, then "
            "immediately shrimp the hips away on that side. Step 2: walk "
            "your elbows back toward your hips, keeping frames on their "
            "chest so they cannot follow. Step 3: feed the knee of the "
            "shrimped side through the gap onto their hip. Step 4: repeat "
            "bridge, shrimp, elbow-walk on the other side if needed, then "
            "push the knee through to recover closed or half guard. Step 5: "
            "never reach both arms up at once - one frame always stays. "
            "Each cycle is small; chain them without pausing."
        ),
        "key_points": [
            "Bridge first to unweight, then shrimp - order matters",
            "One frame always stays on their chest",
            "Feed the knee through the gap the shrimp creates",
            "Small gains chained together beat one big attempt",
            "Recover guard fully before resting",
        ],
        "requirements": [
            "Shrimping endurance for repeated cycles",
            "A partner with a stable, heavy mount",
        ],
        "standards": [
            "IBJJF: escapes score nothing; guard recovery resets the position",
            "Gracie curriculum: the elbow escape is the technical mount escape",
        ],
        "citations": [CIT_GRACIE, CIT_SAULO],
        "sig_lens": (
            "Signature lens: the elbow escape is the covenant of inches - "
            "signed small, collected whole."
        ),
    },
    {
        "key": "bullfighter_pass",
        "name": "Bullfighter Pass",
        "group": "Guard Passes",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The bullfighter pass is the speed pass of Brazilian jiu-jitsu: "
            "from standing, the passer grips both knees or ankles and sprints "
            "to the side like a matador dodging the bull, throwing the legs "
            "aside and sliding into side control. It punishes open guards "
            "that reach too far and teaches the passing principle that speed "
            "around the legs beats strength through them."
        ),
        "how_it_works": (
            "Step 1: stand in the open guard with posture, gripping both of "
            "their knees or ankles. Step 2: shove one leg down and across "
            "while exploding laterally to the opposite side. Step 3: keep "
            "the grips driving their legs away as you sprint around, chest "
            "low. Step 4: the moment your hips clear their legs, drop the "
            "chest onto theirs and release the grips into side control. "
            "Step 5: stabilize for three seconds - the pass only scores when "
            "control is held. If they re-guard mid-sprint, reset and go the "
            "other way; bullfighters hunt in both directions."
        ),
        "key_points": [
            "Grip the knees or ankles before moving - control first",
            "Explode laterally, not forward into their guard",
            "Drive their legs away with the grips the whole sprint",
            "Drop into side control the instant the hips clear",
            "Hold three seconds to make the pass count",
        ],
        "requirements": [
            "Sprint agility and lateral quickness",
            "A partner playing a committed open guard",
        ],
        "standards": [
            "IBJJF: guard passes held 3 seconds score 3 points",
            "Gracie curriculum: the bullfighter is the first speed pass",
        ],
        "citations": [CIT_GRACIE, CIT_SAULO, CIT_IBJJF],
        "sig_lens": (
            "Signature lens: the bullfighter is the covenant of the sidestep "
            "- the matador never meets the horns head on."
        ),
    },
    {
        "key": "knee_slice_pass",
        "name": "Knee Slice Pass",
        "group": "Guard Passes",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The knee slice pass is the pressure pass of Brazilian jiu-jitsu: "
            "from combat base, the passer pins one of the opponent's legs "
            "with the knee and slices it across the thigh, driving the "
            "weight through into side control. It is the highest-percentage "
            "pass in modern competition because it combines control with "
            "forward pressure - the opponent carries your weight the whole "
            "way through."
        ),
        "how_it_works": (
            "Step 1: from combat base inside their half or open guard, "
            "control the far collar or underhook the far arm. Step 2: pin "
            "their near leg by placing your knee on their thigh and driving "
            "your weight onto it. Step 3: slice the knee across their thigh "
            "toward the far side, keeping your head low and heavy on their "
            "chest. Step 4: as the knee clears, sprawl the back leg and drop "
            "the hips, sliding into side control. Step 5: lock the position "
            "for three seconds. If they turn in, follow to the mount; if "
            "they frame, switch to the underhook and finish the slice."
        ),
        "key_points": [
            "Pin the near leg with the knee before slicing",
            "Drive weight through the knee, not around it",
            "Head low and heavy on their chest during the slice",
            "Control the far arm so they cannot frame you off",
            "Sprawl the back leg as the knee clears to kill the re-guard",
        ],
        "requirements": [
            "Knee and shin conditioning for pressure passing",
            "A partner playing half guard with frames",
        ],
        "standards": [
            "IBJJF: guard passes held 3 seconds score 3 points",
            "Danaher lineage: the knee slice is the core pressure pass",
        ],
        "citations": [CIT_SAULO, CIT_DANAHER, CIT_IBJJF],
        "sig_lens": (
            "Signature lens: the knee slice is the covenant of the blade - "
            "one knee parts the guard like still water."
        ),
    },
    {
        "key": "half_guard",
        "name": "Half Guard",
        "group": "Positions",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The half guard is the in-between position where the bottom "
            "player traps one of the opponent's legs between their own: not "
            "fully guarded, not fully passed. Modern jiu-jitsu turned it "
            "from a stalling spot into an attacking system - the underhook "
            "battle decides everything. Win the underhook and you sweep; "
            "lose it and you get flattened. It is where scrambles are born."
        ),
        "how_it_works": (
            "Step 1: from the bottom, trap their near leg between yours, "
            "locking your legs around their shin and keeping your knee as a "
            "shield. Step 2: fight for the underhook on the trapped-leg "
            "side - swim your arm under theirs and lock your hands. Step 3: "
            "stay on your side, never flat, with your head tight to their "
            "chest. Step 4: with the underhook, come up to your elbow, then "
            "your hand, then drive forward for the old-school sweep or take "
            "the back as they whizzer. Step 5: if they get the underhook "
            "instead, frame hard and shrimp back to full guard - never let "
            "them flatten you. The underhook is the whole position."
        ),
        "key_points": [
            "The underhook battle decides the half guard",
            "Stay on your side with a knee shield, never flat",
            "Lock your legs around their trapped shin",
            "Come up in stages: elbow, hand, drive",
            "Losing the underhook means framing and recovering guard",
        ],
        "requirements": [
            "Underhook pummeling endurance",
            "A partner who fights honestly for the underhook",
        ],
        "standards": [
            "IBJJF: half guard is a neutral position; sweeps score 2 points",
            "Ribeiro lineage: half guard is a complete attacking system",
        ],
        "citations": [CIT_SAULO, CIT_RENZO, CIT_IBJJF],
        "sig_lens": (
            "Signature lens: the half guard is the covenant of the half-kept "
            "promise - one leg held, the underhook decides the rest."
        ),
    },
    {
        "key": "double_leg",
        "name": "Double Leg Takedown",
        "group": "Takedowns",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The double leg takedown is the most fundamental takedown in "
            "grappling: the attacker changes levels, penetrates deep between "
            "the opponent's legs, wraps both legs, and drives through to put "
            "them on the mat. Brazilian jiu-jitsu borrowed it from wrestling "
            "and made it the standard way to start standing. A good double "
            "leg lands the attacker already past the guard."
        ),
        "how_it_works": (
            "Step 1: change levels by bending the knees, not the back, "
            "keeping the head up and the back straight. Step 2: take a deep "
            "penetration step so your lead knee lands between their feet. "
            "Step 3: wrap both arms around their legs, cheek tight to their "
            "hip, hands clasped behind the knees. Step 4: drive forward off "
            "the back foot, lifting and turning the corner as they fall. "
            "Step 5: follow them down, keeping the head up and the arms "
            "wrapped until you land in side control or their guard. Never "
            "drop the head below their hips - that is the guillotine's home."
        ),
        "key_points": [
            "Change levels with the knees, back straight, head up",
            "Penetration step lands deep between their feet",
            "Cheek to hip, arms wrapped tight behind the knees",
            "Drive through with the legs, turning the corner",
            "Head stays up - a dropped head feeds the guillotine",
        ],
        "requirements": [
            "Matted space with room for a driving finish",
            "A partner trained to sprawl and to breakfall",
        ],
        "standards": [
            "IBJJF: takedowns that land past the guard score 2 points",
            "Gracie curriculum: the double leg is the core standing takedown",
        ],
        "citations": [CIT_GRACIE, CIT_HELIO, CIT_IBJJF],
        "sig_lens": (
            "Signature lens: the double leg is the covenant of the level "
            "change - drop low, drive true, and the ground signs."
        ),
    },
    {
        "key": "delariva_guard",
        "name": "De la Riva Guard",
        "group": "Positions",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "The de la Riva guard, named for Ricardo de la Riva, is the "
            "open guard where the bottom player's leg wraps behind the "
            "standing opponent's leg like a hook, with a sleeve grip and a "
            "collar or ankle grip for control. It revolutionized guard play "
            "in the 1980s by making the standing passer constantly "
            "off-balanced. From it come sweeps, back takes, and the "
            "berimbolo - it is the gateway to modern guard systems."
        ),
        "how_it_works": (
            "Step 1: from open guard against a standing opponent, wrap your "
            "leg behind their lead leg, hooking the ankle with your instep. "
            "Step 2: grip their same-side sleeve and their far collar or "
            "ankle to control posture and distance. Step 3: keep your hips "
            "mobile and your free foot on their far hip as a frame. Step 4: "
            "pull with the grips and push with the hook to off-balance them "
            "forward, then kick the hook through for the classic de la Riva "
            "sweep. Step 5: when they step back to avoid the sweep, follow "
            "underneath for the berimbolo to the back. The hook is the "
            "engine; the grips are the steering."
        ),
        "key_points": [
            "Hook wraps behind their lead leg, instep on the ankle",
            "Sleeve grip plus collar or ankle grip controls the posture",
            "Free foot frames on the far hip to manage distance",
            "Off-balance forward before any sweep or back take",
            "The sweep threat opens the berimbolo underneath",
        ],
        "requirements": [
            "Hip and ankle flexibility for the deep hook",
            "A partner comfortable being swept from standing",
        ],
        "standards": [
            "IBJJF: de la Riva sweeps score 2 points; the position is neutral",
            "De la Riva lineage: the guard is named for Ricardo de la Riva",
        ],
        "citations": [CIT_SAULO, CIT_RENZO],
        "sig_lens": (
            "Signature lens: the de la Riva is the covenant of the hook - "
            "one wrapped ankle holds the standing giant accountable."
        ),
    },
    {
        "key": "darce_choke",
        "name": "Darce Choke",
        "group": "Chokes",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "The darce choke, named for Joe D'Arce, is the arm-triangle "
            "choke shot through from the front: the attacker's arm threads "
            "under the opponent's near arm and around the neck, locking with "
            "the biceps grip, and the squeeze compresses the carotid against "
            "the opponent's own shoulder. It appears in scrambles when the "
            "opponent turtles or shoots sloppily. Fast, tight, and hard to "
            "see coming."
        ),
        "how_it_works": (
            "Step 1: when the opponent's head drops low with an arm "
            "exposed - from a sprawl or a turtle - thread your arm under "
            "their near armpit and across the back of their neck. Step 2: "
            "grip your own biceps with the threading hand and place the "
            "other hand behind their head or shoulder. Step 3: drop your "
            "weight onto them, walking your hips toward their head to close "
            "the triangle. Step 4: pinch the elbows and drive the choking "
            "shoulder into the neck, compressing the carotid against their "
            "trapped shoulder. Step 5: hold steady - no cranking - and "
            "release on the tap. Depth of the thread decides the finish."
        ),
        "key_points": [
            "Thread deep under the armpit and across the neck",
            "Lock the biceps grip before applying pressure",
            "Walk the hips toward their head to close the space",
            "Their own shoulder becomes the second wall of the choke",
            "Steady squeeze, instant release on the tap",
        ],
        "requirements": [
            "Long-arm leverage helps but timing matters more",
            "A partner who taps to arm-triangles early",
        ],
        "standards": [
            "IBJJF: legal at all belt levels, gi and no-gi",
            "Named for Joe D'Arce, who popularized it in competition",
        ],
        "citations": [CIT_DANAHER, CIT_IBJJF],
        "sig_lens": (
            "Signature lens: the darce is the covenant of the scramble - "
            "signed in motion, collected before the dust settles."
        ),
    },
    {
        "key": "guillotine_choke",
        "name": "Guillotine Choke",
        "group": "Chokes",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "The guillotine choke is the front headlock turned into a "
            "finisher: the attacker's arm wraps around the opponent's neck "
            "with the chin in the crook of the elbow, the hands lock, and "
            "the hips drive back to compress the neck. It is the classic "
            "punishment for a sloppy takedown - the head drops low, the arm "
            "closes like the blade it is named for, and the shot becomes a "
            "nap. Every grappler learns both to apply it and to respect it."
        ),
        "how_it_works": (
            "Step 1: as they shoot with the head low and to the side, wrap "
            "your arm around their neck, their chin in the crook of your "
            "elbow. Step 2: lock your hands together - chin strap or "
            "high-elbow grip - keeping the choking wrist straight. Step 3: "
            "sit back and sprawl the hips away, extending their neck into "
            "the lock. Step 4: close the elbow of the choking arm down "
            "toward your ribs while lifting slightly with the lock. Step 5: "
            "hold the squeeze without cranking the spine, and release on "
            "the tap. The sprawl-back is the finish; the arms only hold "
            "the shape."
        ),
        "key_points": [
            "Chin in the crook of the elbow, wrist straight",
            "Lock the hands before the hips move",
            "Sprawl back to extend the neck into the choke",
            "Close the choking elbow to the ribs to finish",
            "Squeeze the choke, never crank the neck",
        ],
        "requirements": [
            "A sprawl to pair with the lock",
            "A partner who taps to front chokes without pride",
        ],
        "standards": [
            "IBJJF: legal at all belt levels, gi and no-gi",
            "Gracie curriculum: the guillotine is the core front choke",
        ],
        "citations": [CIT_GRACIE, CIT_DANAHER, CIT_IBJJF],
        "sig_lens": (
            "Signature lens: the guillotine is the covenant of the dropped "
            "head - bow low and the blade signs for you."
        ),
    },
    {
        "key": "omoplata",
        "name": "Omoplata",
        "group": "Joint Locks",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "The omoplata is the shoulder lock of the guard: the attacker "
            "swings a leg over the opponent's shoulder, sits up, and uses "
            "the hips and legs to rotate the shoulder behind the back like "
            "a kimura done with the whole body. Named from the Portuguese "
            "for shoulder blade, it attacks, sweeps, and transitions to the "
            "back all from one movement. It is the guard player's answer to "
            "the opponent who stacks forward."
        ),
        "how_it_works": (
            "Step 1: from closed guard, as they posture or stack, swing one "
            "leg over their same-side shoulder and pivot your hips out to "
            "the side. Step 2: sit up and trap their arm between your legs, "
            "your shin across their back. Step 3: control their far hip or "
            "belt to stop them rolling forward, and flatten your hips to "
            "the mat. Step 4: sit tall and lean back slightly, rotating "
            "their shoulder with your leg pressure - the joint locks as the "
            "arm turns behind the back. Step 5: if they roll forward to "
            "escape, follow the roll and finish, or take the sweep points "
            "and the top position. Slow pressure, instant release."
        ),
        "key_points": [
            "Swing the leg over as they posture or stack forward",
            "Pivot the hips fully out to the side before sitting up",
            "Control the far hip to stop the forward roll escape",
            "Flatten the hips to the mat to apply the rotation",
            "The forward roll they escape with becomes your sweep",
        ],
        "requirements": [
            "Hip mobility to swing the leg over the shoulder",
            "A partner who taps to shoulder rotation early",
        ],
        "standards": [
            "IBJJF: legal at all belt levels, gi and no-gi",
            "Gracie curriculum: the omoplata is the core guard shoulder lock",
        ],
        "citations": [CIT_GRACIE, CIT_SAULO, CIT_IBJJF],
        "sig_lens": (
            "Signature lens: the omoplata is the covenant of the turning "
            "blade - the shoulder signs where the leg commands."
        ),
    },
    {
        "key": "north_south_choke",
        "name": "North-South Choke",
        "group": "Chokes",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The north-south choke is the head-and-arm compression finish "
            "from the north-south position: the attacker wraps an arm around "
            "the opponent's head, locks it against their own side, and drops "
            "the weight through the shoulder to compress the carotids. It "
            "looks like a hug and finishes like a vise. Monson and Maia made "
            "it famous at the highest levels by finishing elite opponents "
            "who thought they were safe underneath."
        ),
        "how_it_works": (
            "Step 1: from north-south, slide your arm under their head and "
            "around, locking your hand to your own far lat or biceps. Step 2: "
            "drop your shoulder behind their head and settle your weight "
            "through it, chest to the back of their head. Step 3: walk your "
            "feet away slightly to stretch them out and kill their frames. "
            "Step 4: sink the hips and let gravity compress the neck between "
            "your arm and your ribs - the carotids close under steady "
            "weight. Step 5: do not muscle it; the position finishes it. "
            "Release on the tap. The choke is in the shoulder placement, "
            "not the squeeze."
        ),
        "key_points": [
            "Arm wrapped fully around the head, locked to your own side",
            "Shoulder drops behind their head, weight sinks through it",
            "Walk the feet out to stretch them and kill frames",
            "Gravity finishes it - muscling ruins the angle",
            "Release on the tap; the compression fades fast",
        ],
        "requirements": [
            "A stable north-south position held first",
            "A partner who taps to compression chokes early",
        ],
        "standards": [
            "IBJJF: legal at all belt levels, gi and no-gi",
            "Famous at elite level via Monson and Maia finishes",
        ],
        "citations": [CIT_DANAHER, CIT_IBJJF],
        "sig_lens": (
            "Signature lens: the north-south choke is the covenant of the "
            "compass - head north, weight south, signature in the middle."
        ),
    },
    {
        "key": "anaconda_choke",
        "name": "Anaconda Choke",
        "group": "Chokes",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The anaconda choke is the rolling arm-triangle: the attacker's "
            "arm threads under the opponent's neck and through the armpit, "
            "the hands lock, and the attacker rolls - the gator roll - to "
            "tighten the coil around the neck. It is the darce's rolling "
            "cousin, born for scrambles where the opponent turtles and "
            "turns. The roll is the lock; the arms only hold the shape."
        ),
        "how_it_works": (
            "Step 1: from the front headlock with their arm trapped, thread "
            "your arm under their neck and out through their far armpit. "
            "Step 2: lock your hands - palm to palm or biceps grip - keeping "
            "the choking arm deep. Step 3: step over their body and roll "
            "toward the locked side, the gator roll, pulling them with you. "
            "Step 4: land with your weight on their trapped side, pinch the "
            "elbows, and let the coil compress the carotid against their own "
            "shoulder. Step 5: hold steady without cranking and release on "
            "the tap. Commit to the roll - half rolls give up the position."
        ),
        "key_points": [
            "Thread deep: under the neck, out the far armpit",
            "Lock the hands before the roll starts",
            "Commit fully to the gator roll toward the lock",
            "Land heavy on the trapped side to close the coil",
            "The roll tightens it; the arms only hold the shape",
        ],
        "requirements": [
            "Comfort rolling with a partner's weight",
            "A partner who taps to arm-triangles early",
        ],
        "standards": [
            "IBJJF: legal at all belt levels, gi and no-gi",
            "Scramble-born: the classic counter to the turtle",
        ],
        "citations": [CIT_DANAHER, CIT_IBJJF],
        "sig_lens": (
            "Signature lens: the anaconda is the covenant of the coil - "
            "the roll signs it tighter with every turn."
        ),
    },
    {
        "key": "berimbolo",
        "name": "Berimbolo",
        "group": "Sweeps",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The berimbolo is the inverted spin under the standing opponent "
            "from the de la Riva guard: the guard player rolls underneath, "
            "takes the back, and scores. It defined an era of competition "
            "jiu-jitsu in the 2010s, with the Mendes brothers and the "
            "Atos team turning it into a back-taking system. It looks like "
            "acrobatics; it is really just the de la Riva sweep continued "
            "underneath instead of over the top."
        ),
        "how_it_works": (
            "Step 1: establish the de la Riva hook with sleeve and ankle or "
            "collar grips against the standing opponent. Step 2: pull them "
            "forward onto the hook, then kick the hook through as you invert "
            "- head under their hips, shoulders to the mat. Step 3: spin "
            "underneath to their far side, keeping the grips to steer their "
            "weight. Step 4: come up behind them, establish the back with "
            "one hook, then the second, and lock the seatbelt grip. Step 5: "
            "attack the rear naked choke or hold the back for points. The "
            "inversion must be committed - hesitation underneath a standing "
            "opponent gets you flattened."
        ),
        "key_points": [
            "De la Riva hook and grips established first",
            "Pull them forward onto the hook before inverting",
            "Invert fully - head under hips, commit to the spin",
            "Steer with the grips while spinning underneath",
            "Come up on the back with hooks and seatbelt, not the choke first",
        ],
        "requirements": [
            "Comfort inverting with weight above you",
            "A partner who stands stably in the de la Riva",
        ],
        "standards": [
            "IBJJF: back takes with hooks score 4 points",
            "Mendes/Atos lineage: defined 2010s competition guard play",
        ],
        "citations": [CIT_SAULO, CIT_RENZO, CIT_IBJJF],
        "sig_lens": (
            "Signature lens: the berimbolo is the covenant of the underside "
            "- the back is taken from below, never asked for."
        ),
    },
    {
        "key": "ezekiel_choke",
        "name": "Ezekiel Choke",
        "group": "Chokes",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The Ezekiel choke is the sleeve choke: from the mount or side "
            "control, the attacker slides one hand inside their own opposite "
            "sleeve, wraps the forearm across the opponent's neck, and pulls "
            "the free hand to compress both carotids. Ezequiel Paraguassu "
            "used it to surprise the judo world at the 1988 Olympics trials "
            "era, and it remains the gi choke that needs no collar grip. It "
            "is the choke you do not see because the setup looks like "
            "harmless hand-fighting."
        ),
        "how_it_works": (
            "Step 1: from mount, slide your hand deep inside your own "
            "opposite sleeve, gripping the cloth. Step 2: wrap that forearm "
            "across their neck, blade of the forearm on one carotid. Step 3: "
            "grip your own sleeved wrist with the free hand and pull it "
            "across, closing the vise. Step 4: drop your weight forward and "
            "turn slightly to the sleeved side to add pressure. Step 5: "
            "hold the compression steady and release on the tap. The sleeve "
            "grip must be deep - a shallow grip slips off under pressure."
        ),
        "key_points": [
            "Hand buried deep inside your own opposite sleeve",
            "Forearm blade across the neck, not the hand",
            "Free hand pulls the sleeved wrist across to close the vise",
            "Drop the weight forward to add pressure",
            "A shallow sleeve grip is a failed choke - re-grip deep",
        ],
        "requirements": [
            "A gi with sleeves loose enough for the inside grip",
            "A partner who taps to sleeve chokes early",
        ],
        "standards": [
            "IBJJF: legal at all belt levels in the gi",
            "Named for Ezequiel Paraguassu, who revealed it in 1988",
        ],
        "citations": [CIT_GRACIE, CIT_IBJJF],
        "sig_lens": (
            "Signature lens: the Ezekiel is the covenant of the hidden "
            "blade - the sleeve signs what the hands conceal."
        ),
    },
    {
        "key": "ankle_lock",
        "name": "Straight Ankle Lock",
        "group": "Joint Locks",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The straight ankle lock is the fundamental leg lock: the "
            "attacker's forearm wedges under the opponent's Achilles tendon "
            "like a fulcrum, the foot is trapped under the armpit, and the "
            "attacker arches back to hyperextend the ankle and pressure the "
            "knee. It is legal at every belt level and is the safe doorway "
            "into leg locking - the mechanics teach control of the leg "
            "entanglement before any rotational lock is ever attempted."
        ),
        "how_it_works": (
            "Step 1: from ashi garami or a leg entanglement, trap their foot "
            "under your armpit with the toes pointed, and wedge your "
            "forearm - blade up - under their Achilles. Step 2: grip your "
            "own hands or gi to lock the configuration, keeping their knee "
            "controlled so the leg cannot turn. Step 3: pinch your elbows "
            "and fall your weight back, arching like a bow. Step 4: the "
            "forearm acts as a fulcrum under the Achilles while the armpit "
            "traps the foot - pressure builds on the ankle and knee. Step 5: "
            "apply slowly and release the instant they tap. Never reap "
            "across with force; control the knee line at all times."
        ),
        "key_points": [
            "Forearm blade wedged under the Achilles as the fulcrum",
            "Foot trapped deep under the armpit, toes pointed",
            "Control the knee line so the leg cannot rotate out",
            "Arch back like a bow - the back does the work",
            "Slow pressure, instant release; respect the knee",
        ],
        "requirements": [
            "A leg entanglement (ashi garami) controlled first",
            "A partner who taps to foot and ankle pressure immediately",
        ],
        "standards": [
            "IBJJF: legal at all belt levels, gi and no-gi",
            "The safe doorway to leg locks; rotational locks come later",
        ],
        "citations": [CIT_DANAHER, CIT_IBJJF],
        "sig_lens": (
            "Signature lens: the ankle lock is the covenant of the fulcrum - "
            "one forearm signs beneath the tendon, the back collects."
        ),
    },
    {
        "key": "heel_hook",
        "name": "Heel Hook Fundamentals",
        "group": "Joint Locks",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The heel hook is the most powerful and most dangerous legal "
            "technique in grappling: the attacker's forearm traps the "
            "opponent's heel and rotates it, transmitting torque directly "
            "into the knee ligaments. It finishes fights in seconds and ends "
            "careers when applied recklessly. This record covers only the "
            "fundamentals - recognition, control positions, and the "
            "non-negotiable safety rules - because the heel hook demands "
            "more responsibility than any other technique in this database. "
            "In IBJJF it is legal only for brown and black belt adults in "
            "no-gi."
        ),
        "how_it_works": (
            "Step 1: recognize the entanglement - outside ashi or the saddle "
            "- and secure the heel with the forearm in the pocket, hand "
            "gripping your own wrist or biceps. Step 2: control the knee "
            "line completely; the lock is only safe to drill when the leg "
            "cannot slip. Step 3: in drilling, apply ZERO rotation - catch "
            "and release is the only acceptable training method below "
            "expert supervision. Step 4: the tap for a heel hook comes "
            "before pain, because ligament damage precedes the pain signal. "
            "Step 5: any partner may call stop at any time, and the lock "
            "releases instantly. Drill entries and escapes, never finishes, "
            "until a qualified black belt coach clears full application."
        ),
        "key_points": [
            "The most dangerous legal technique - treat it that way",
            "Catch and release only in drilling; zero rotation without expert supervision",
            "Tap comes before pain - ligaments fail before the warning",
            "Control the knee line completely before anything else",
            "Any partner can call stop; release is instant and total",
        ],
        "requirements": [
            "Direct supervision by a qualified black belt coach",
            "Training partners who tap early and communicate constantly",
            "IBJJF legality: brown and black belt adults, no-gi only",
        ],
        "standards": [
            "IBJJF: heel hooks legal only for brown/black adult no-gi",
            "Safety standard: catch-and-release drilling until expert clearance",
        ],
        "citations": [CIT_DANAHER, CIT_IBJJF],
        "sig_lens": (
            "Signature lens: the heel hook is the covenant with a warning "
            "seal - the signature is power, the witness is restraint."
        ),
    },
    {
        "key": "inverted_recovery",
        "name": "Inverted Guard Recovery",
        "group": "Escapes",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The inverted guard recovery, built on the granby roll, is the "
            "emergency exit of advanced jiu-jitsu: when the guard is nearly "
            "passed and the hips are trapped, the defender rolls over the "
            "shoulder, inverts underneath, and re-establishes guard from "
            "below. It turns a nearly-finished pass into a scramble the "
            "defender can win. It demands comfort upside down that only "
            "comes from hundreds of granby rolls."
        ),
        "how_it_works": (
            "Step 1: as the pass collapses your guard, tuck the chin and "
            "post the far hand to protect the neck. Step 2: kick your legs "
            "over in a granby roll - a backward shoulder roll - going under "
            "their pressure instead of fighting it. Step 3: keep the knees "
            "tight to the chest through the inversion so they cannot catch "
            "a leg. Step 4: as you come around underneath, shoot the legs "
            "back into a guard - closed, open, or half - before they "
            "settle their weight. Step 5: face them and rebuild frames "
            "immediately; the recovery only counts when the guard is "
            "re-established. Roll with their force, never against it."
        ),
        "key_points": [
            "Tuck the chin and post the far hand before rolling",
            "Granby under their pressure - roll with it, not against it",
            "Knees tight to the chest through the whole inversion",
            "Re-insert the guard before they settle their weight",
            "Rebuild frames the instant the guard is back",
        ],
        "requirements": [
            "Hundreds of granby rolls for inversion comfort",
            "Neck strength and a matted surface",
        ],
        "standards": [
            "IBJJF: guard recovery resets the position; no points for escapes",
            "Advanced curriculum: the granby is the emergency guard recovery",
        ],
        "citations": [CIT_SAULO, CIT_DANAHER],
        "sig_lens": (
            "Signature lens: the inversion is the covenant of the underside - "
            "when the guard falls, go beneath and sign again."
        ),
    },
    {
        "key": "xguard_entry",
        "name": "X-Guard Entry",
        "group": "Positions",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The x-guard is the standing opponent's nightmare: the guard "
            "player slides underneath, hooks both legs behind the opponent's "
            "legs in an X, and controls a leg and the far hip. From "
            "underneath, sweeps come in every direction and the standing "
            "player cannot generate any offense. Marcelo Garcia made it the "
            "most feared guard of the 2000s, sweeping the best passers in "
            "the world from a position that looks like hiding."
        ),
        "how_it_works": (
            "Step 1: from half guard or open guard against a standing "
            "opponent, dive underneath as they pressure forward. Step 2: "
            "cross your legs behind their legs in an X - one hook behind "
            "each leg - with your head tight to their far hip. Step 3: "
            "control their near ankle with one hand and their far hip or "
            "belt with the other. Step 4: extend the X to lift them, then "
            "dump them in any direction they lean - the classic x-guard "
            "sweep takes them backward over your hooks. Step 5: follow up "
            "to the top position or the back as they fall. Stay compact "
            "underneath; reaching out gets your arms trapped."
        ),
        "key_points": [
            "Dive under as they pressure forward - use their momentum",
            "X hooks behind both legs, head tight to the far hip",
            "Control the near ankle and the far hip",
            "Extend the X to lift, then dump the way they lean",
            "Stay compact - reaching arms get trapped underneath",
        ],
        "requirements": [
            "Comfort fighting from completely underneath",
            "A partner who pressures forward realistically",
        ],
        "standards": [
            "IBJJF: x-guard sweeps score 2 points",
            "Garcia lineage: the defining guard of 2000s competition",
        ],
        "citations": [CIT_RENZO, CIT_SAULO, CIT_IBJJF],
        "sig_lens": (
            "Signature lens: the x-guard is the covenant signed from below - "
            "the smallest signature topples the tallest stance."
        ),
    },
]
