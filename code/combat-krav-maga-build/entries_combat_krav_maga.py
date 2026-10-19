#!/usr/bin/env python3
"""Entries for the Krav Maga Combat databases (combat batch 2, 2026-10-17).

Verified 2026-10-17 (combat batch 2): RAW SWEEP over the full manifest
(2,410 databases) PLUS every shard index title in jah-databases-data-1
PLUS the main-repo data dir: zero 'combat-krav-maga*' slugs/names; zero
title collisions for all 68 planned titles (34 public + 34 Signature
Edition) run through the whole-system dedupe gate - zero refusals, zero
collisions. The paste's rule was applied by name/purpose/record
schema/capabilities: a ladder-ordered krav maga technique archive with
step-by-step body mechanics, drill timers, and training calculators is a
distinct capability from the sibling combat databases (karate, boxing,
BJJ, muay thai, judo, capoeira, kickboxing, taekwondo, savate, lethwei),
so BUILD NEW is the verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  combat-krav-maga              - The Krav Maga Combat Database
                                 (public-harvest: real, fact-checked krav
                                 maga - the Israeli self-defense system
                                 founded by Imi Lichtenfeld - simultaneous
                                 defense and attack, defenses against
                                 grabs, chokes, and weapon threats,
                                 striking, and ground survival, every
                                 technique a full record with HOW TO DO IT
                                 step-by-step body mechanics; standard
                                 references Levine and Whitman Complete
                                 Krav Maga 2007; Kahn Krav Maga: An
                                 Essential Guide 2004; Krav Maga Worldwide
                                 official curriculum; IKMF grading
                                 syllabus; FEKM official program)
  combat-krav-maga-signature    - The Krav Maga Combat Signature Database
                                 (his original Signature Combat Method:
                                 every defense a covenant of the body,
                                 the burst the oath of forward motion,
                                 retzev the signature written in
                                 continuous combat; src signature, titles
                                 suffixed " (Signature Edition)", never
                                 presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBKM- (public) and JAH-CBKMS- (signature), verified free
in the manifest id_prefix values (zero hits) and zero hits in every shard
index file.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_krav_maga.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Screening: civilian self-defense instruction only - personal-protection
training, nothing about military operations or systems. Nothing
hate-adjacent, profane, or inappropriate; no religious talk. Standing
exclusion honored: nothing on neutralizing or defeating military or
defense-grade systems.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Combat Method: "
            "every defense a covenant of the body, the burst the oath of "
            "forward motion, and retzev the signature written in continuous "
            "combat. Clearly labeled Signature-made, never presented as "
            "authentic public record.")

CIT_LEVINE = ("Levine D, Whitman J. Complete Krav Maga: The Ultimate Guide "
              "to Over 230 Self-Defense and Combative Techniques. Ulysses "
              "Press; 2007.")
CIT_KAHN = ("Kahn D. Krav Maga: An Essential Guide to the Renowned "
            "Method - for Fitness and Self-Defense. St. Martin's Griffin; "
            "2004.")
CIT_KMW = ("Krav Maga Worldwide. Official Krav Maga Curriculum: Yellow "
           "through Black Belt. Los Angeles, California.")
CIT_IKMF = ("International Krav Maga Federation. Krav Maga Grading "
            "Syllabus: Practitioner through Expert Levels.")
CIT_FEKM = ("Federation Europeenne de Krav-Maga. Official Krav Maga Program "
            "and Grading System.")
CIT_HISTORY = ("Lichtenfeld I. Founder of krav maga; developed the system "
               "in the 1940s-1960s and formalized the civilian curriculum "
               "thereafter.")

ENTRIES = [
    {
        "key": "fighting_stance",
        "name": "Krav Maga Fighting Stance",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The krav maga fighting stance is the platform every technique "
            "stands on. The feet sit about 1.3 times shoulder width apart - "
            "for a 0.45 meter shoulder width that is a 0.585 meter base - "
            "with the strong side back, the weight split 60 percent forward "
            "and 40 percent back, so an 80 kilogram student carries about 48 "
            "kilograms on the front foot and 32 on the rear. The hands guard "
            "the face, the chin tucks, the elbows stay tight, and the body "
            "blades slightly. From this stance the student can punch, kick, "
            "sprawl, burst forward, or retreat without resetting the feet."
        ),
        "how_it_works": (
            "Step 1: step the dominant foot back about one shoulder width so "
            "the feet are 1.3 times shoulder width apart, toes pointing "
            "roughly forward. Step 2: bend both knees softly and settle the "
            "weight 60 percent on the front foot and 40 percent on the rear, "
            "weight on the balls of the feet. Step 3: raise both hands to "
            "cheekbone height, palms facing inward, elbows tucked to the "
            "ribs. Step 4: tuck the chin to the chest and blade the torso "
            "about 30 degrees to narrow the target. Step 5: bounce lightly "
            "in place and check that you can lift either foot instantly - if "
            "a foot is stuck, the weight split is wrong."
        ),
        "key_points": [
            "Feet about 1.3 times shoulder width apart, strong side back",
            "Weight split 60 percent front and 40 percent rear, on the balls of the feet",
            "Hands at cheekbone height, elbows tucked, chin down",
            "Knees soft and springy - never locked, never flat-footed",
            "The stance must allow instant punching, kicking, bursting, or retreating",
        ],
        "requirements": [
            "A flat training surface with room to step in all directions",
            "A mirror or partner to check the 60/40 weight split and hand height",
        ],
        "standards": [
            "Krav Maga Worldwide: fighting stance is the first element of the yellow belt curriculum",
            "IKMF: stance, movement, and guard are tested at every practitioner grade",
        ],
        "citations": [CIT_LEVINE, CIT_KMW],
        "sig_lens": (
            "Signature lens: the stance is the oath of the ground - the "
            "feet sign the covenant, the 60/40 split seals it, and the "
            "guard keeps the promise."
        ),
    },
    {
        "key": "footwork",
        "name": "Krav Maga Footwork and Movement",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Krav maga footwork moves the stance without breaking it. The "
            "rule is simple: the foot nearest the direction of travel moves "
            "first, and the stance is rebuilt with every step. A training "
            "step of 0.5 meters at 2 steps per second covers 10 meters in 10 "
            "seconds, and the classic drill runs 10 steps - 5 forward, 5 "
            "back - per 5-second round, six rounds for a 30-second footwork "
            "block. Advance to close distance, retreat to buy time, move "
            "laterally to change the angle, and never cross the feet, which "
            "collapses the base."
        ),
        "how_it_works": (
            "Step 1: from the fighting stance, decide the direction - the "
            "lead foot moves first going forward or sideways, the rear foot "
            "first going back. Step 2: slide or step about 0.5 meters and "
            "immediately rebuild the stance: same width, same 60/40 split, "
            "hands still up. Step 3: keep the head level - no bouncing up "
            "and down, which telegraphs and wastes energy. Step 4: practice "
            "the advance, the retreat, and the lateral shuffle as separate "
            "drills before mixing them. Step 5: add pivots - turning the "
            "whole stance 90 or 180 degrees - for angle changes against "
            "multiple directions."
        ),
        "key_points": [
            "The foot nearest the direction of travel always moves first",
            "Rebuild the stance after every step - width, weight split, guard",
            "Never cross the feet; crossing collapses the base of support",
            "Head stays level; bouncing telegraphs and wastes energy",
            "Advance to close, retreat to buy time, move laterally to change angles",
        ],
        "requirements": [
            "Open floor space of at least 10 meters for advance/retreat lines",
            "A timer for the 5-second, 10-step footwork rounds",
        ],
        "standards": [
            "Krav Maga Worldwide: footwork drills open every yellow belt class",
            "FEKM: movement and stance are graded before any combatives",
        ],
        "citations": [CIT_LEVINE, CIT_FEKM],
        "sig_lens": (
            "Signature lens: footwork is the signature in motion - each "
            "step re-signs the stance, and the line of travel is the "
            "sentence it writes."
        ),
    },
    {
        "key": "punch_combatives",
        "name": "Krav Maga Punch Combatives",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Krav maga punches are thrown from the fighting stance with full "
            "hip rotation behind them. The core set is the jab, the cross, "
            "the hook, and the uppercut, drilled as a four-punch combination "
            "that lands in about 1.0 second at 0.25 seconds per punch. A "
            "straight punch driven by roughly 4 kilograms of effective arm "
            "and shoulder mass accelerating at 60 meters per second squared "
            "delivers about 240 newtons of force. Ten full combinations is a "
            "10-second combatives round. The punches always return along the "
            "same path to the guard - what goes out comes straight back."
        ),
        "how_it_works": (
            "Step 1: from the stance, snap the lead hand straight out for "
            "the jab, rotating the fist to palm-down at extension. Step 2: "
            "drive the rear hand straight through for the cross, pivoting "
            "the rear foot and rotating the hips fully. Step 3: bring the "
            "lead elbow up to shoulder height and whip the hook across, "
            "weight shifting onto the lead leg. Step 4: drop the rear "
            "shoulder and drive the uppercut up the centerline, knees "
            "bending into it. Step 5: return every punch along its own path "
            "to the guard before the next one fires, and breathe out "
            "sharply with each strike."
        ),
        "key_points": [
            "Every punch rotates the hips and pivots the feet - no arm-only punches",
            "The four-punch combination lands in about 1.0 second",
            "Fists return along their own path to the guard every time",
            "Exhale sharply with each punch to brace the core",
            "Keep the non-punching hand glued to the cheek",
        ],
        "requirements": [
            "Heavy bag or focus mitts for impact training",
            "Hand wraps and gloves once contact intensity rises",
        ],
        "standards": [
            "Krav Maga Worldwide: punch combatives are core yellow belt material",
            "IKMF: straight punches and hooks are tested at practitioner level 1",
        ],
        "citations": [CIT_LEVINE, CIT_KAHN],
        "sig_lens": (
            "Signature lens: the punch is the signature of the hip - the "
            "fist only delivers what the ground, the legs, and the turning "
            "hip have already written."
        ),
    },
    {
        "key": "palm_heel",
        "name": "Krav Maga Palm-Heel Strike",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The palm-heel strike hits with the hard base of the palm "
            "instead of the knuckles, which spares the small bones of the "
            "hand. A 3000-newton strike spread over the 0.008 square meter "
            "palm surface lands at about 375 kilopascals, while the same "
            "force on the 0.004 square meter knuckle surface of a fist lands "
            "at about 750 kilopascals - roughly double the pressure on a far "
            "more fragile structure. The mechanics are identical to the "
            "straight punch: hip rotation, straight line, full return to "
            "guard. It is the preferred strike for hard targets like the "
            "chin and the nose."
        ),
        "how_it_works": (
            "Step 1: open the hand and pull the fingers back hard, locking "
            "the wrist straight so the palm heel becomes one solid surface. "
            "Step 2: drive the palm straight out along the centerline, "
            "rotating the hips exactly as in the cross punch. Step 3: strike "
            "with the heel of the palm only, fingers clear of the target. "
            "Step 4: snap the hand straight back to the guard along the "
            "same line. Step 5: drill it on the bag alternating with the "
            "cross punch so the body learns both from the same hip motion."
        ),
        "key_points": [
            "Strike with the heel of the palm, fingers pulled back and clear",
            "Same hip rotation and line as the straight punch",
            "Preferred over the fist for hard targets like chin and nose",
            "Lock the wrist straight - a bent wrist collapses on impact",
            "Snaps back to guard along its own path",
        ],
        "requirements": [
            "Heavy bag or pads for impact practice",
            "Hand wraps once volume training begins",
        ],
        "standards": [
            "Krav Maga Worldwide: palm-heel strikes are taught alongside straight punches",
            "Kahn: open-hand strikes protect the striker's hand on hard targets",
        ],
        "citations": [CIT_KAHN, CIT_KMW],
        "sig_lens": (
            "Signature lens: the palm heel is the covenant of the open "
            "hand - it strikes with the whole surface and keeps the "
            "promise to the bones of the fist."
        ),
    },
    {
        "key": "elbow_strikes",
        "name": "Krav Maga Elbow Strikes",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Elbow strikes are krav maga's close-range answer: when the "
            "distance collapses, the elbow replaces the fist. The forearm "
            "and hand weigh about 2.5 kilograms, and whipped at 12 meters "
            "per second they carry about 180 joules of kinetic energy "
            "focused on the sharp point of the elbow - devastating at a "
            "range of only 0.35 meters. The set includes the horizontal "
            "elbow, the upward elbow, the downward elbow, and the spinning "
            "elbow, all driven by violent hip and shoulder rotation with the "
            "fist glued to the shoulder for structure."
        ),
        "how_it_works": (
            "Step 1: bring the fist tight to the shoulder on the striking "
            "side so the elbow becomes a single rigid weapon. Step 2: for "
            "the horizontal elbow, whip the hips and shoulders around and "
            "drive the elbow across at face height. Step 3: for the upward "
            "elbow, drop the weight and drive the elbow up under the chin. "
            "Step 4: for the downward elbow, raise the elbow high and chop "
            "straight down with the body weight behind it. Step 5: always "
            "follow through past the target and return the guard hand to "
            "the face immediately."
        ),
        "key_points": [
            "The fist stays glued to the shoulder - the elbow is the weapon",
            "All power comes from hip and shoulder rotation, never the arm alone",
            "Horizontal, upward, downward, and spinning variants cover every close angle",
            "Effective at 0.35 meters where punches have no room",
            "Follow through past the target, then recover the guard",
        ],
        "requirements": [
            "Elbow pads for partner drilling",
            "Heavy bag for full-power repetitions",
        ],
        "standards": [
            "Krav Maga Worldwide: elbow combatives enter at orange belt",
            "IKMF: close-range elbows are core practitioner-level material",
        ],
        "citations": [CIT_LEVINE, CIT_IKMF],
        "sig_lens": (
            "Signature lens: the elbow is the short signature - written "
            "close, in one violent rotation, where long weapons cannot go."
        ),
    },
    {
        "key": "knee_strikes",
        "name": "Krav Maga Knee Strikes",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The knee strike drives the point of the knee up into the "
            "groin, thigh, or torso while the hands pull the target down "
            "into it. The thigh weighs about 10 kilograms; driven at 8 "
            "meters per second and stopped in 0.05 seconds, it delivers "
            "about 1600 newtons of force. The hip travels about 0.45 meters "
            "into the strike, and the standing leg stays slightly bent with "
            "the foot planted. In krav maga the knee is almost always "
            "paired with a grab or clinch that drags the attacker down onto "
            "the rising knee - two forces meeting at one point."
        ),
        "how_it_works": (
            "Step 1: grab the attacker's head, shoulders, or clothing with "
            "both hands and pull down sharply. Step 2: drive the knee "
            "straight up the centerline, thrusting the hips forward 0.45 "
            "meters as the knee rises. Step 3: keep the toes pointed down "
            "so the knee point leads, and stay on the ball of the standing "
            "foot. Step 4: meet the pull and the knee at the same instant - "
            "the collision of the two forces is the strike. Step 5: set the "
            "foot back down into the fighting stance, hands back to the "
            "guard, ready to repeat or burst."
        ),
        "key_points": [
            "Pull the target down as the knee drives up - two forces, one point",
            "Hips thrust 0.45 meters forward into every knee",
            "Toes pointed down, knee point leading, standing foot planted",
            "Pairs naturally with grabs, clinches, and choke defenses",
            "Recover to the stance after every knee",
        ],
        "requirements": [
            "Thai pads or a heavy bag held at torso height",
            "A partner for the pull-down timing drill",
        ],
        "standards": [
            "Krav Maga Worldwide: knee strikes are fundamental combatives from yellow belt",
            "FEKM: knees paired with pulling are graded at the first levels",
        ],
        "citations": [CIT_LEVINE, CIT_FEKM],
        "sig_lens": (
            "Signature lens: the knee is the rising covenant - the hands "
            "pull the oath downward while the hip signs it upward."
        ),
    },
    {
        "key": "front_kick_groin",
        "name": "Krav Maga Front Kick to the Groin",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The front kick to the groin is krav maga's signature long-range "
            "stopper: fast, simple, and fight-ending. The leg weighs about "
            "15 kilograms, and snapped at 10 meters per second it carries "
            "about 750 joules of kinetic energy up into the groin. The "
            "kicking foot rechambers along the same path in about 0.3 "
            "seconds, so the kicker is back in stance before the attacker "
            "can grab the leg. It is taught as the default answer to a "
            "frontal threat because it needs no setup and works from the "
            "fighting stance with one motion."
        ),
        "how_it_works": (
            "Step 1: from the stance, lift the rear knee sharply to waist "
            "height, keeping the guard hands up. Step 2: snap the lower leg "
            "out and up, striking with the instep or shin into the groin, "
            "hips thrusting forward. Step 3: rechamber the leg along the "
            "exact reverse path - knee up, then foot down. Step 4: set the "
            "foot back into the fighting stance in about 0.3 seconds total. "
            "Step 5: follow immediately with combatives - the kick is the "
            "opener, never the whole answer."
        ),
        "key_points": [
            "Knee lifts first, then the lower leg snaps out - never swing the whole leg",
            "Strike with the instep or shin, hips thrusting forward",
            "Rechamber along the reverse path in about 0.3 seconds",
            "The default answer to a frontal threat - fast and simple",
            "Always follow with combatives; the kick opens, the hands finish",
        ],
        "requirements": [
            "Heavy bag for full-power repetitions",
            "Groin protection for any partner work",
        ],
        "standards": [
            "Krav Maga Worldwide: the groin kick is the first kick taught, at yellow belt",
            "IKMF: front kick to the groin is a core practitioner technique",
        ],
        "citations": [CIT_LEVINE, CIT_IKMF],
        "sig_lens": (
            "Signature lens: the groin kick is the long signature - one "
            "line written from the stance, 750 joules, and back before it "
            "can be caught."
        ),
    },
    {
        "key": "hammerfist",
        "name": "Krav Maga Hammerfist Strike",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The hammerfist swings the bottom edge of a clenched fist like a "
            "hammer, striking downward or sideways with the sturdy ulnar "
            "edge of the hand. The hand and forearm weigh about 3 kilograms; "
            "driven downward at 8 meters per second they deliver about 96 "
            "joules - while gravity alone on a 0.6 meter drop only gives "
            "3.43 meters per second, so the muscles do most of the work. It "
            "is the natural strike from a clinch, a grab defense, or any "
            "position where the hands are already high, and it spares the "
            "knuckles entirely."
        ),
        "how_it_works": (
            "Step 1: clench the fist and raise the elbow so the bottom edge "
            "of the fist faces the target. Step 2: swing the whole arm down "
            "like a hammer, rotating the shoulders and dropping the body "
            "weight into it. Step 3: strike with the fleshy bottom edge of "
            "the fist, wrist straight. Step 4: for the sideways hammerfist, "
            "swing across at head height with full hip rotation. Step 5: "
            "recover the hand to the guard and be ready to strike again - "
            "hammerfists chain naturally in pairs."
        ),
        "key_points": [
            "Strike with the bottom edge of the fist, wrist locked straight",
            "Gravity assists but muscle drive does most of the work",
            "The natural strike from clinches and grab defenses",
            "Spares the knuckles - no small hand bones take the impact",
            "Chains naturally in pairs with full recovery between",
        ],
        "requirements": [
            "Focus mitts or a heavy bag",
            "Awareness of surroundings when swinging - the arc is wide",
        ],
        "standards": [
            "Krav Maga Worldwide: hammerfist strikes are basic combatives",
            "Kahn: hammerfists suit close-range follow-ups after defenses",
        ],
        "citations": [CIT_KAHN, CIT_KMW],
        "sig_lens": (
            "Signature lens: the hammerfist is the falling signature - "
            "raised high, signed downward, sealed with the weight of the body."
        ),
    },
]

ENTRIES += [
    {
        "key": "inside_defense",
        "name": "Krav Maga Inside Defense Against a Straight Punch",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The inside defense is krav maga's core answer to a straight "
            "punch: a short sweeping deflection that rides the punch off the "
            "centerline while the other hand fires back. A punch traveling "
            "10 meters per second covers the 0.6 meter gap in 0.06 seconds, "
            "so the defending hand only needs to move about 0.2 meters "
            "laterally in that same 0.06 seconds - roughly 3.3 meters per "
            "second of hand speed - to clear the line. The counterpunch "
            "launches 0.1 seconds later, making defense and attack one "
            "motion. It is the first expression of krav maga's central "
            "principle: defend and counterattack simultaneously."
        ),
        "how_it_works": (
            "Step 1: as the punch comes, sweep the same-side hand across "
            "your face, deflecting the punch outward with the palm and "
            "forearm - a short 0.2 meter ride, not a hard block. Step 2: at "
            "the same instant, fire the opposite hand straight down the "
            "centerline into the attacker's face. Step 3: step slightly "
            "forward and offline as you defend, cutting the angle. Step 4: "
            "follow the counter with combatives - punches, elbows, knees - "
            "until the threat is down. Step 5: disengage to a safe distance "
            "and scan for more threats."
        ),
        "key_points": [
            "Deflect, do not block - a 0.2 meter ride clears the line",
            "Defense and counterattack fire at the same time, always",
            "Deflect with the same-side hand, counter with the other",
            "Step forward and slightly offline while defending",
            "Follow with combatives, then disengage and scan",
        ],
        "requirements": [
            "A partner throwing slow straight punches to build timing",
            "Focus mitts for the simultaneous counter",
        ],
        "standards": [
            "Krav Maga Worldwide: inside defense is the first punch defense taught",
            "IKMF: simultaneous defense and attack is graded from practitioner level 1",
        ],
        "citations": [CIT_LEVINE, CIT_KMW],
        "sig_lens": (
            "Signature lens: the inside defense is the first covenant of "
            "simultaneity - the defending hand signs the deflection while "
            "the other hand signs the answer."
        ),
    },
    {
        "key": "wrist_grab",
        "name": "Krav Maga Defense Against a Wrist Grab",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "A wrist grab is broken by attacking the weak point of the grip: "
            "the attacker's thumb. The defender yanks the captured hand "
            "sharply toward the attacker's thumb with the whole body, "
            "generating about 400 newtons of pull on a 0.3 meter lever - "
            "about 120 newton-meters of torque against a thumb grip that "
            "can resist only a fraction of that. The escape takes one "
            "explosive motion and ends with a counterstrike, because a "
            "freed wrist means nothing if the attacker simply grabs again."
        ),
        "how_it_works": (
            "Step 1: instantly rotate your captured hand so the thumb side "
            "faces the attacker's thumb - the weak point of their grip. "
            "Step 2: step back and yank your whole body weight toward that "
            "thumb, tearing the wrist free in one explosive pull. Step 3: as "
            "the hand breaks free, it chambers into a strike - punch, "
            "palm-heel, or hammerfist. Step 4: deliver the counterstrike "
            "immediately; never admire the escape. Step 5: disengage and "
            "scan, hands back in the guard."
        ),
        "key_points": [
            "Attack the thumb - the weak point of every grip",
            "Pull with the whole body, not the arm - about 400 newtons of bodyweight pull",
            "One explosive motion; hesitation lets the grip reset",
            "The freed hand chambers directly into a counterstrike",
            "Always finish with a strike, then disengage and scan",
        ],
        "requirements": [
            "A partner applying progressively stronger wrist grabs",
            "Open space to step back into the pull",
        ],
        "standards": [
            "Krav Maga Worldwide: wrist grab releases are yellow belt defenses",
            "FEKM: releases against grabs are among the first defenses graded",
        ],
        "citations": [CIT_LEVINE, CIT_FEKM],
        "sig_lens": (
            "Signature lens: the wrist release is the covenant of the weak "
            "point - the whole body signs against the single thumb, and "
            "the thumb always loses."
        ),
    },
    {
        "key": "defense_360",
        "name": "Krav Maga 360-Degree Outside Defense",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The 360-degree defense answers circular attacks - hooks, "
            "slaps, and haymakers - coming from any direction. The defender "
            "chops the forearm across the incoming limb at 90 degrees while "
            "bursting forward into the attack, smothering its power. An "
            "attack launched from 1.5 meters at 8 meters per second arrives "
            "in 0.1875 seconds, which is inside the 0.2 second trained "
            "reaction window - so the defense is drilled against 8 sectors "
            "of 45 degrees each until the chop is reflexive and the body "
            "moves before conscious thought. The standard drill runs random "
            "attacks every 3 seconds for 5 minutes: 100 repetitions."
        ),
        "how_it_works": (
            "Step 1: as the circular strike comes, chop your forearm across "
            "its path at a right angle, meeting force with structure. Step "
            "2: burst forward into the attacker as you chop, smothering the "
            "strike before it develops full power. Step 3: keep the other "
            "hand glued to your face for the second punch that often "
            "follows. Step 4: counter immediately with punches and elbows "
            "once the attack is smothered. Step 5: drill all 8 sectors - "
            "high, middle, and low on both sides - until direction no longer "
            "matters."
        ),
        "key_points": [
            "Chop the forearm across the attack at 90 degrees",
            "Burst forward into the strike to smother its power",
            "The other hand stays home guarding the face",
            "Covers 8 sectors of 45 degrees - every circular angle",
            "Counter the instant the attack is smothered",
        ],
        "requirements": [
            "Forearm guards for high-repetition partner drilling",
            "A partner attacking from random directions on a 3-second cadence",
        ],
        "standards": [
            "Krav Maga Worldwide: 360 defenses are core orange belt material",
            "IKMF: outside defenses against circular attacks are practitioner fundamentals",
        ],
        "citations": [CIT_LEVINE, CIT_IKMF],
        "sig_lens": (
            "Signature lens: the 360 defense is the covenant of the full "
            "circle - eight sectors, one chop, and the body moves before "
            "the mind has signed anything."
        ),
    },
    {
        "key": "front_choke_pluck",
        "name": "Krav Maga Defense Against a Front Choke",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The front choke defense is krav maga's famous pluck: both "
            "hands hook over the attacker's wrists and tear downward with "
            "the whole body while the hips drive forward. Two hands pulling "
            "300 newtons each deliver about 600 newtons of downward pluck "
            "against arms that can press only about 400 newtons - the pluck "
            "wins by roughly 200 newtons. The pluck must land inside the "
            "first second, before the choke sets, and it is married to an "
            "immediate groin kick or knee. Tuck the chin the instant hands "
            "touch the throat to buy the airway time."
        ),
        "how_it_works": (
            "Step 1: the instant hands close on your throat, tuck the chin "
            "hard to protect the airway. Step 2: hook both hands over the "
            "attacker's wrists, thumbs down. Step 3: tear both hands "
            "violently downward and outward while driving your hips forward "
            "into the attacker - about 600 newtons of pluck. Step 4: as the "
            "choke breaks, drive a knee or front kick into the groin. Step "
            "5: follow with combatives until the attacker is down, then "
            "disengage and scan."
        ),
        "key_points": [
            "Tuck the chin the instant hands touch the throat",
            "Hook both hands over the wrists and pluck down and out with the body",
            "About 600 newtons of pluck beats about 400 newtons of press",
            "The pluck must land inside the first second",
            "Marry the pluck to a groin kick or knee, then combatives",
        ],
        "requirements": [
            "A partner applying a slow, controlled front choke",
            "Throat guards or careful control while learning the pluck",
        ],
        "standards": [
            "Krav Maga Worldwide: the front choke pluck is a signature yellow belt defense",
            "Kahn: the pluck is the canonical answer to the frontal choke",
        ],
        "citations": [CIT_KAHN, CIT_KMW],
        "sig_lens": (
            "Signature lens: the pluck is the covenant of the throat - "
            "both hands sign downward at once, and the airway keeps its "
            "promise."
        ),
    },
    {
        "key": "side_headlock",
        "name": "Krav Maga Defense Against a Side Headlock",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The side headlock traps the head under the attacker's arm and "
            "bends the defender over. Krav maga answers with structure: the "
            "near hand frames against the attacker's hip, the far hand "
            "reaches over to control, and the hips bridge explosively "
            "upward. Bridging lifts about 60 percent of an 80 kilogram "
            "attacker's weight - roughly 48 kilograms, or 471 newtons - "
            "which breaks the lock's leverage, and a 0.25 meter shrimp "
            "creates the space to pull the head free. Counterstrikes follow "
            "the instant the head is out."
        ),
        "how_it_works": (
            "Step 1: turn your chin into the attacker's body to protect the "
            "neck and buy space. Step 2: frame the near hand hard against "
            "the attacker's hip and reach the far arm over their back. "
            "Step 3: bridge the hips explosively upward - about 471 newtons "
            "of lift - while shrimping 0.25 meters to make space. Step 4: "
            "pull the head out through the space as the lock loosens. Step "
            "5: counter immediately with elbows and knees, then disengage "
            "and scan."
        ),
        "key_points": [
            "Turn the chin into the attacker to protect the neck",
            "Frame the near hand on the hip, far arm over the back",
            "Bridge explosively - about 471 newtons of hip lift",
            "Shrimp 0.25 meters to create the escape space",
            "Counter the instant the head is free",
        ],
        "requirements": [
            "A matted surface for the bridging and shrimping",
            "A partner applying a controlled side headlock",
        ],
        "standards": [
            "Krav Maga Worldwide: headlock defenses are orange belt material",
            "IKMF: headlock escapes are tested at practitioner levels",
        ],
        "citations": [CIT_LEVINE, CIT_IKMF],
        "sig_lens": (
            "Signature lens: the headlock escape is the covenant of the "
            "bridge - the hips sign upward, the space opens, and the head "
            "keeps its freedom."
        ),
    },
    {
        "key": "shirt_grab",
        "name": "Krav Maga Defense Against a Two-Handed Shirt Grab",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "A two-handed shirt grab pins the defender's clothing and "
            "usually precedes a headbutt or a pull into a strike. Krav maga "
            "answers with a double pluck: both hands hook over the "
            "attacker's wrists and tear down and out with about 250 newtons "
            "per hand - 500 newtons total - while the hips drive in and a "
            "groin kick or knee fires in the same 0.5 second window. The "
            "defense is simultaneous by design: both hands pluck while a "
            "leg strikes, so the attacker is broken and hit before they can "
            "escalate the grab."
        ),
        "how_it_works": (
            "Step 1: trap the attacker's hands against your chest with your "
            "own hands pressing down on theirs. Step 2: hook over both "
            "wrists and pluck violently down and outward with the whole "
            "body - about 500 newtons. Step 3: at the same instant, drive a "
            "knee or front kick into the groin. Step 4: follow with hand "
            "combatives - punches and elbows - as the grab breaks. Step 5: "
            "disengage to distance and scan."
        ),
        "key_points": [
            "Trap their hands to your chest first so they cannot re-grab",
            "Double pluck down and out - about 500 newtons total",
            "A groin kick or knee fires in the same 0.5 second window",
            "Defense and attack are one simultaneous motion",
            "Follow with combatives, then disengage and scan",
        ],
        "requirements": [
            "A partner grabbing the shirt with both hands at increasing intensity",
            "An old shirt or gi top - grabs tear clothing",
        ],
        "standards": [
            "Krav Maga Worldwide: shirt grab defenses are yellow belt material",
            "FEKM: defenses against clothing grabs are early-grade requirements",
        ],
        "citations": [CIT_LEVINE, CIT_FEKM],
        "sig_lens": (
            "Signature lens: the shirt-grab defense is the covenant of "
            "both hands - they sign the pluck together while the leg "
            "signs the answer."
        ),
    },
    {
        "key": "bear_hug_free",
        "name": "Krav Maga Defense Against a Bear Hug with Arms Free",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "In a bear hug with arms free, the attacker wraps the torso "
            "while the defender's arms stay outside the embrace. Krav maga "
            "exploits this immediately: drop the weight low, strike the "
            "groin or face with the free hands, and hammer the attacker's "
            "arms at the elbows. A rear elbow strike from the 2.5 kilogram "
            "forearm at 10 meters per second carries about 125 joules into "
            "the attacker's ribs or face. The low base - hips dropped a "
            "full stance - makes the defender nearly impossible to lift, "
            "and the strikes break the hug from the inside."
        ),
        "how_it_works": (
            "Step 1: the instant the hug closes, drop your hips low and "
            "widen the base so you cannot be lifted. Step 2: strike "
            "immediately with the free hands - groin strikes, eye rakes, "
            "and rear elbows at about 125 joules. Step 3: hammer down on "
            "the attacker's forearms at the elbows to weaken the wrap. "
            "Step 4: as the hug loosens, turn into the attacker and follow "
            "with knees and punches. Step 5: disengage and scan once the "
            "attacker releases."
        ),
        "key_points": [
            "Drop the hips instantly - a low base cannot be lifted",
            "Free arms mean immediate strikes: groin, face, rear elbows",
            "Hammer the attacker's forearms at the elbows to break the wrap",
            "Turn into the attacker as the hug loosens",
            "Follow with combatives, then disengage and scan",
        ],
        "requirements": [
            "A partner applying a controlled bear hug from the front or rear",
            "A matted area in case the drill goes to the ground",
        ],
        "standards": [
            "Krav Maga Worldwide: bear hug defenses are orange belt material",
            "IKMF: bear hug escapes are practitioner-level requirements",
        ],
        "citations": [CIT_LEVINE, CIT_IKMF],
        "sig_lens": (
            "Signature lens: the free-arm bear hug defense is the covenant "
            "of the low base - the hips sign downward and the free hands "
            "sign everywhere at once."
        ),
    },
    {
        "key": "bear_hug_pinned",
        "name": "Krav Maga Defense Against a Bear Hug with Arms Pinned",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "A bear hug with arms pinned is far more dangerous: the "
            "attacker's arms trap the defender's arms against the body. "
            "Krav maga creates space first - shrugging the shoulders and "
            "wedging the forearms to open about 0.15 meters of room per "
            "side - then drops the base, turns 90 degrees in about 0.4 "
            "seconds (about 3.9 radians per second of rotation), and "
            "counterattacks with the newly freed limbs. Without the initial "
            "space-making, no strike is possible; with it, the whole "
            "arsenal returns."
        ),
        "how_it_works": (
            "Step 1: shrug hard and wedge your forearms outward to create "
            "about 0.15 meters of space on each side. Step 2: drop your hips "
            "low the moment any space opens. Step 3: turn 90 degrees toward "
            "one side in about 0.4 seconds, freeing one arm as you rotate. "
            "Step 4: strike immediately with the freed arm - elbow, "
            "hammerfist, or punch - and follow with knees. Step 5: keep "
            "striking until the hug breaks, then disengage and scan."
        ),
        "key_points": [
            "Make space first - shrug and wedge about 0.15 meters per side",
            "Drop the base the instant any space opens",
            "Turn 90 degrees in about 0.4 seconds to free an arm",
            "The freed arm strikes immediately - no pause",
            "Keep striking until the hug breaks, then disengage",
        ],
        "requirements": [
            "A partner applying a controlled arms-pinned bear hug",
            "Forearm guards for the wedging repetitions",
        ],
        "standards": [
            "Krav Maga Worldwide: arms-pinned bear hug is an advanced orange belt defense",
            "FEKM: pinned-arm releases require the space-making shrug first",
        ],
        "citations": [CIT_LEVINE, CIT_FEKM],
        "sig_lens": (
            "Signature lens: the pinned bear hug defense is the covenant "
            "of made space - the shoulders sign the first 0.15 meters, "
            "and the turn signs the rest."
        ),
    },
    {
        "key": "hair_grab",
        "name": "Krav Maga Defense Against a Hair Grab",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "A hair grab controls the head by the hair, yanking it to steer "
            "the body. Krav maga's answer is to kill the leverage: both of "
            "the defender's hands clamp down over the attacker's grabbing "
            "hand with about 300 newtons each - 600 newtons total - pinning "
            "it to the head so it can no longer pull, then the defender "
            "steps sharply toward the attacker's thumb side and rotates, "
            "shortening the pull by 0.2 meters and breaking the grip's "
            "mechanics. Once the hand is trapped against the skull, the "
            "attacker is holding a fixed post, not a lever."
        ),
        "how_it_works": (
            "Step 1: instantly clamp both hands over the attacker's "
            "grabbing hand, pressing it hard against your head - about 600 "
            "newtons of pin. Step 2: step sharply toward the attacker's "
            "thumb side, shortening their pull by 0.2 meters. Step 3: rotate "
            "your body under the trapped hand, peeling the grip against its "
            "own wrist angle. Step 4: as the grip breaks, counter with "
            "punches and elbows. Step 5: disengage and scan."
        ),
        "key_points": [
            "Clamp both hands over the grabbing hand - about 600 newtons of pin",
            "Pin the hand to your head so it cannot pull",
            "Step toward the thumb side to shorten the leverage by 0.2 meters",
            "Rotate under the trapped hand to break the wrist angle",
            "Counter the instant the grip breaks",
        ],
        "requirements": [
            "A partner with a firm but controlled hair grip",
            "Long hair tied or a wig cap for safe drilling",
        ],
        "standards": [
            "Krav Maga Worldwide: hair grab defenses are orange belt material",
            "IKMF: the two-hand clamp is the standard hair-grab answer",
        ],
        "citations": [CIT_LEVINE, CIT_IKMF],
        "sig_lens": (
            "Signature lens: the hair-grab defense is the covenant of the "
            "clamp - both hands sign over the grabbing hand, and the "
            "lever becomes a post."
        ),
    },
    {
        "key": "rear_choke",
        "name": "Krav Maga Defense Against a Rear Choke",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "A rear choke - an arm around the throat from behind - is one of "
            "the most dangerous empty-hand attacks, so krav maga treats it "
            "as a race against the first second. The defender tucks the "
            "chin, plucks at the choking arm, and pivots 180 degrees toward "
            "the attack in about 0.4 seconds - about 7.85 radians per "
            "second of rotation - which unwinds the choke's leverage. The "
            "pluck, the turn, and the first counterstrike all land inside 1 "
            "second. Turning toward the attack, never away, is the rule that "
            "saves the airway."
        ),
        "how_it_works": (
            "Step 1: tuck the chin violently to the chest and raise the "
            "shoulders to shield the neck. Step 2: hook one hand over the "
            "choking arm and pluck down hard. Step 3: pivot 180 degrees "
            "toward the attacker in about 0.4 seconds, stepping deep - "
            "turn into the choke, never away. Step 4: as you complete the "
            "turn, strike with the free hand - punch, palm-heel, or elbow. "
            "Step 5: follow with combatives until the threat ends, then "
            "disengage and scan."
        ),
        "key_points": [
            "Tuck the chin and raise the shoulders instantly",
            "Pluck the choking arm down while pivoting",
            "Turn 180 degrees toward the attacker in about 0.4 seconds",
            "Never turn away - turning away tightens the choke",
            "Pluck, turn, and first strike all land inside 1 second",
        ],
        "requirements": [
            "A partner applying a slow, controlled rear choke",
            "Throat guards and strict control while learning",
        ],
        "standards": [
            "Krav Maga Worldwide: rear choke defense is a core orange belt technique",
            "Kahn: the turn-toward principle is the canonical rear-choke answer",
        ],
        "citations": [CIT_KAHN, CIT_KMW],
        "sig_lens": (
            "Signature lens: the rear-choke defense is the covenant of the "
            "turn - the body signs 180 degrees toward the danger, and "
            "the choke unwinds itself."
        ),
    },
    {
        "key": "ground_survival",
        "name": "Krav Maga Ground Survival and the Technical Stand-Up",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Krav maga treats the ground as a place to escape from, not to "
            "fight on: get up as fast as possible while protected. The "
            "technical stand-up does this in four phases - post the hand, "
            "swing the far leg through, post the far foot, stand - in about "
            "1.2 seconds total, with one hand always guarding and kicks "
            "keeping the attacker at least 2 meters away until you rise. "
            "The guard, the bridge, and the shrimp from grappling are "
            "borrowed only as tools to create the standing opportunity."
        ),
        "how_it_works": (
            "Step 1: from the ground, keep one hand posted and one guarding "
            "the face, and kick at the attacker to hold 2 meters of "
            "distance. Step 2: post the near hand on the ground and swing "
            "the far leg through under the body. Step 3: plant the far foot "
            "and lift the hips, keeping the guard hand up. Step 4: stand in "
            "about 1.2 seconds total, eyes on the attacker the whole way, "
            "and immediately re-establish the fighting stance."
        ),
        "key_points": [
            "The ground is for escaping, not for fighting - stand up first",
            "Technical stand-up runs four phases in about 1.2 seconds",
            "One hand always guards while the other posts",
            "Kicks maintain at least 2 meters of distance until you rise",
            "Eyes stay on the attacker through the entire stand-up",
        ],
        "requirements": [
            "A matted surface for ground repetitions",
            "A partner advancing slowly to pressure the stand-up",
        ],
        "standards": [
            "Krav Maga Worldwide: ground survival and stand-up are green belt fundamentals",
            "IKMF: the technical stand-up is tested at practitioner levels",
        ],
        "citations": [CIT_LEVINE, CIT_IKMF],
        "sig_lens": (
            "Signature lens: the technical stand-up is the covenant of "
            "return - four phases sign the way back to the feet, and the "
            "ground releases its claim."
        ),
    },
    {
        "key": "kicks_ground",
        "name": "Krav Maga Kicking from the Ground",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Before the technical stand-up is possible, kicks from the "
            "ground keep a standing attacker at bay. Lying on the side or "
            "back, the defender drives stomping and thrusting kicks into "
            "the attacker's shins, knees, and groin at a reach of about 1.2 "
            "meters. The 15 kilogram leg driven upward at 7 meters per "
            "second carries about 368 joules - more than enough to stop an "
            "advance. The kicks sweep a 180-degree arc in front of the body, "
            "and every kick chambers back to guard the stand-up."
        ),
        "how_it_works": (
            "Step 1: fall to one side, never flat on the back, with the top "
            "leg chambered and the bottom leg posted. Step 2: drive stomping "
            "kicks into the attacker's shins and knees - about 368 joules "
            "per kick - keeping 1.2 meters of range. Step 3: sweep the kicks "
            "across a 180-degree arc so the attacker cannot circle. Step 4: "
            "use a hard kick's impact as the moment to begin the technical "
            "stand-up. Step 5: rise with the guard up, never turning your "
            "back."
        ),
        "key_points": [
            "Lie on the side, never flat on the back",
            "Stomping kicks target shins, knees, and groin at 1.2 meters range",
            "Each kick carries about 368 joules - enough to stop an advance",
            "Sweep a 180-degree arc so the attacker cannot circle",
            "Convert a hard kick's impact into the technical stand-up",
        ],
        "requirements": [
            "A matted surface for ground kicking repetitions",
            "Shin guards for partner drills",
        ],
        "standards": [
            "Krav Maga Worldwide: ground kicking precedes the stand-up in the curriculum",
            "FEKM: kicks from the ground are graded with ground survival",
        ],
        "citations": [CIT_LEVINE, CIT_FEKM],
        "sig_lens": (
            "Signature lens: ground kicks are the covenant of distance - "
            "the leg signs a 180-degree arc, and the attacker cannot "
            "cross the line it writes."
        ),
    },
    {
        "key": "clinch",
        "name": "Krav Maga Clinch Fighting and Close-Quarter Combatives",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The clinch is the standing grapple - chest to chest, fighting "
            "for head position and underhooks. Krav maga treats it as a "
            "launchpad for the close arsenal: knees, elbows, and head "
            "control, not a place to rest. The pummeling drill builds the "
            "position: 10 underhook switches in 20 seconds, or one clean "
            "switch every 2 seconds. Driving the head down with about 235 "
            "newtons of forward pressure - roughly 24 kilograms - breaks "
            "the attacker's posture and opens the knees and elbows."
        ),
        "how_it_works": (
            "Step 1: crash into the clinch with the head tight to the "
            "attacker's chest or shoulder, never leaving space. Step 2: "
            "pummel for inside position - swim the arms for double "
            "underhooks, one switch every 2 seconds. Step 3: snap the head "
            "down with about 235 newtons of pressure while pulling with "
            "the underhooks. Step 4: fire knees into the thighs and torso "
            "and elbows over the top as the posture breaks. Step 5: shove "
            "off to striking range or take the back - never stay chest to "
            "chest without attacking."
        ),
        "key_points": [
            "Head tight to the chest or shoulder - no space in the clinch",
            "Pummel for double underhooks: one switch every 2 seconds",
            "Snap the head down with about 235 newtons of pressure",
            "Knees and elbows fire the instant posture breaks",
            "Never rest chest to chest - attack or exit",
        ],
        "requirements": [
            "A partner for pummeling and head-position drills",
            "Mouthguard and headgear for live clinch rounds",
        ],
        "standards": [
            "Krav Maga Worldwide: clinch work is green belt material",
            "IKMF: close-quarter combatives are tested at intermediate grades",
        ],
        "citations": [CIT_LEVINE, CIT_IKMF],
        "sig_lens": (
            "Signature lens: the clinch is the covenant of closeness - "
            "the head signs the position, the underhooks seal it, and the "
            "knees deliver the terms."
        ),
    },
    {
        "key": "bursting",
        "name": "Krav Maga Bursting: Closing Distance Under Attack",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Bursting is krav maga's explosive forward entry: from outside "
            "range, the defender detonates forward 2 meters in 0.5 seconds - "
            "about 4 meters per second - while throwing combatives the "
            "whole way in. The burst smothers long attacks, collapses the "
            "attacker's timing, and turns defense into a clinch or a "
            "flurry. Three strikes land during the 0.5 second burst - about "
            "6 strikes per second - so the attacker is hit before they can "
            "reset. Bursting is always forward and always violent; "
            "retreating under attack is the last resort."
        ),
        "how_it_works": (
            "Step 1: from the stance, load the rear leg like a spring. "
            "Step 2: explode forward 2 meters in 0.5 seconds, driving off "
            "the rear foot. Step 3: throw strikes continuously during the "
            "burst - about 6 per second - so the entry is covered. Step 4: "
            "arrive in the clinch or in punching range with the guard "
            "intact. Step 5: continue with combatives or the clinch game; "
            "the burst is the entry, not the finish."
        ),
        "key_points": [
            "Burst 2 meters in 0.5 seconds - about 4 meters per second",
            "Strike continuously during the burst, about 6 strikes per second",
            "Always forward, always explosive - never retreat by default",
            "The burst smothers long attacks before they develop",
            "Arrive in range with the guard intact and keep attacking",
        ],
        "requirements": [
            "At least 5 meters of clear runway for burst repetitions",
            "A partner holding pads at the entry point",
        ],
        "standards": [
            "Krav Maga Worldwide: bursting is drilled from the earliest levels",
            "Kahn: explosive forward motion is a defining krav maga principle",
        ],
        "citations": [CIT_KAHN, CIT_KMW],
        "sig_lens": (
            "Signature lens: the burst is the oath of forward motion - 2 "
            "meters signed in half a second, and retreat is never the "
            "first word."
        ),
    },
]

ENTRIES += [
    {
        "key": "retzev",
        "name": "Krav Maga Retzev: Continuous Combat Motion",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Retzev - Hebrew for continuous motion - is krav maga's "
            "fighting doctrine: once the fight starts, never stop attacking "
            "until the threat is down. Strikes flow at about 3 per second, "
            "so a 30-second retzev round delivers about 90 strikes; at "
            "roughly 150 joules per strike that is about 13500 joules of "
            "work per round, with 60 seconds of rest between 5 rounds. "
            "There are no pauses to admire a good hit, no resetting to "
            "admire distance - every strike chambers the next, targets "
            "switch fluidly, and the attacker is overwhelmed by volume and "
            "pressure until they fall."
        ),
        "how_it_works": (
            "Step 1: open with the burst or the first defense - the entry "
            "is the first word of the combination. Step 2: chain strikes at "
            "about 3 per second, letting each strike's recoil chamber the "
            "next - punches to elbows to knees to kicks. Step 3: switch "
            "targets constantly - head, body, groin, legs - so no defense "
            "settles. Step 4: keep the feet driving, circling or bursting, "
            "never planting flat. Step 5: stop only when the threat is "
            "down, then disengage, scan, and check yourself."
        ),
        "key_points": [
            "About 3 strikes per second, every strike chambers the next",
            "A 30-second round delivers about 90 strikes and 13500 joules",
            "Switch targets constantly - head, body, groin, legs",
            "Feet always driving - circle or burst, never plant flat",
            "Stop only when the threat is down, then disengage and scan",
        ],
        "requirements": [
            "Heavy bag for 30-second continuous rounds",
            "A timer: 30 seconds work, 60 seconds rest, 5 rounds",
        ],
        "standards": [
            "Krav Maga Worldwide: retzev is the continuous-combat doctrine of the system",
            "IKMF: continuous striking is demonstrated at advanced practitioner grades",
        ],
        "citations": [CIT_LEVINE, CIT_IKMF],
        "sig_lens": (
            "Signature lens: retzev is the signature written in continuous "
            "combat - 3 strikes a second, no pauses, until the page is full."
        ),
    },
    {
        "key": "knife_live_side",
        "name": "Krav Maga Defense Against a Knife Threat on the Live Side",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "A knife threat on the live side means the blade is on the same "
            "side as your lead hand - the side you can reach fastest. Krav "
            "maga's answer is redirect, control, counterattack: the lead "
            "hand sweeps the knife arm about 30 degrees off the centerline, "
            "moving 0.4 meters in 0.1 seconds - about 4 meters per second of "
            "hand speed - then both hands clamp the weapon arm with about "
            "500 newtons of two-on-one control while knees and punches "
            "finish the fight. The body bursts slightly offline as the "
            "hands work, and the knife arm is never released until the "
            "attacker is down."
        ),
        "how_it_works": (
            "Step 1: as the threat presents, sweep the lead hand across to "
            "redirect the knife arm about 30 degrees off your centerline. "
            "Step 2: clamp both hands onto the weapon arm - about 500 "
            "newtons of two-on-one control - and pin it to your body. Step "
            "3: burst slightly offline so your torso leaves the blade's "
            "line. Step 4: counterattack with knees, punches, and kicks "
            "while never releasing the weapon arm. Step 5: strip or secure "
            "the knife only after the attacker is down, then disengage."
        ),
        "key_points": [
            "Redirect the knife arm about 30 degrees off the centerline",
            "Hand speed about 4 meters per second - the sweep must beat the thrust",
            "Two-on-one control: about 500 newtons clamping the weapon arm",
            "Burst slightly offline as the hands redirect",
            "Never release the weapon arm until the attacker is down",
        ],
        "requirements": [
            "A rubber or wooden training knife - never a live blade",
            "A partner presenting slow, controlled knife threats",
        ],
        "standards": [
            "Krav Maga Worldwide: knife threat defenses are green belt and above",
            "IKMF: weapon defenses require controlled training blades only",
        ],
        "citations": [CIT_LEVINE, CIT_IKMF],
        "sig_lens": (
            "Signature lens: the live-side knife defense is the covenant "
            "of the near hand - it signs the redirect in 0.1 seconds, "
            "and both hands seal the control."
        ),
    },
    {
        "key": "knife_dead_side",
        "name": "Krav Maga Defense Against a Knife Threat on the Dead Side",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "A knife threat on the dead side - the blade on the side of "
            "your rear hand - is the harder problem, because the nearest "
            "defending hand is farther away. Krav maga solves it with body "
            "rotation: the torso turns 90 degrees offline while stepping "
            "0.6 meters to the side, the rear hand sweeps across to redirect "
            "the blade, and the whole defense-counter lands in about 0.35 "
            "seconds. The turn does the work the reach cannot: by the time "
            "the blade arrives, the body is gone and the counter is already "
            "coming back."
        ),
        "how_it_works": (
            "Step 1: rotate the torso 90 degrees away from the blade while "
            "stepping 0.6 meters offline. Step 2: sweep the rear hand "
            "across the body to redirect the knife arm off the line. Step "
            "3: clamp into two-on-one control of the weapon arm as the turn "
            "completes - total time about 0.35 seconds. Step 4: "
            "counterattack with the free limbs - knees and punches - while "
            "holding the weapon arm. Step 5: finish, secure the knife, and "
            "disengage."
        ),
        "key_points": [
            "The torso turns 90 degrees offline - rotation beats reach",
            "Step 0.6 meters to the side as you turn",
            "Rear hand sweeps across to redirect the blade",
            "Whole defense lands in about 0.35 seconds",
            "Clamp two-on-one, counter, and never release the weapon arm early",
        ],
        "requirements": [
            "A rubber or wooden training knife",
            "A partner presenting dead-side threats at low speed first",
        ],
        "standards": [
            "Krav Maga Worldwide: dead-side knife defense is advanced green belt material",
            "FEKM: offline body rotation is the graded dead-side principle",
        ],
        "citations": [CIT_LEVINE, CIT_FEKM],
        "sig_lens": (
            "Signature lens: the dead-side defense is the covenant of "
            "rotation - the body signs 90 degrees away, and the blade "
            "arrives at an empty line."
        ),
    },
    {
        "key": "stick_attack",
        "name": "Krav Maga Defense Against a Stick Attack",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A stick or club attack - usually an overhead swing - is "
            "answered with the 360 defense family: intercept the swinging "
            "arm, burst inside the weapon's arc, and counter at close "
            "range. A 0.7 meter stick swung overhead traces its 180-degree "
            "arc in about 0.4 seconds, the tip reaching about 5.5 meters "
            "per second, so the defender bursts inside the 0.7 meter radius "
            "in about 0.3 seconds - beating the swing by a tenth of a "
            "second. Inside the arc the stick is useless; elbows, knees, "
            "and head control finish the fight."
        ),
        "how_it_works": (
            "Step 1: as the stick rises, chop the forearm up to intercept "
            "the swinging arm at 90 degrees - the 360 defense. Step 2: "
            "burst forward inside the 0.7 meter arc in about 0.3 seconds, "
            "smothering the swing. Step 3: control the weapon arm with "
            "both hands, pinning it. Step 4: counter with elbows, knees, "
            "and punches at close range where the stick cannot work. Step "
            "5: strip the stick only after the attacker is controlled, "
            "then disengage."
        ),
        "key_points": [
            "Intercept the swinging arm with the 360 defense, not the stick",
            "Burst inside the 0.7 meter arc in about 0.3 seconds",
            "Inside the arc the stick is useless - own that range",
            "Two-on-one control of the weapon arm",
            "Counter with elbows and knees, then strip and disengage",
        ],
        "requirements": [
            "A padded training stick - never a hardwood baton for beginners",
            "Forearm guards for interception repetitions",
        ],
        "standards": [
            "Krav Maga Worldwide: stick defenses are blue belt and above",
            "IKMF: impact-weapon defenses are advanced practitioner material",
        ],
        "citations": [CIT_LEVINE, CIT_IKMF],
        "sig_lens": (
            "Signature lens: the stick defense is the covenant of the "
            "inside arc - the body signs its entry in 0.3 seconds, and "
            "the swing writes on empty air."
        ),
    },
    {
        "key": "knife_slash",
        "name": "Krav Maga Defense Against a Slashing Knife Attack",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A slashing knife attack sweeps the blade across in a 180-degree "
            "arc that takes about 0.25 seconds - too fast to catch "
            "mid-swing. Krav maga's answer is timing: burst in during the "
            "slash's retraction, when the attacker's arm is extended and "
            "recovering, through a 0.15 second window. The defender covers "
            "1 meter in that 0.15 seconds - about 6.7 meters per second - "
            "jams the weapon arm with the 360 defense, and converts "
            "instantly to two-on-one control with knees and strikes. You do "
            "not block the slash; you arrive inside it."
        ),
        "how_it_works": (
            "Step 1: read the slash and lean back just enough to let the "
            "180-degree arc miss - about 0.25 seconds of patience. Step 2: "
            "as the arm extends and retracts, burst 1 meter in 0.15 seconds "
            "to jam the weapon arm. Step 3: apply the 360 chop to the "
            "attacking arm and clamp two-on-one control. Step 4: drive "
            "knees and punches while holding the weapon arm pinned. Step 5: "
            "secure the knife after the attacker is down, then disengage."
        ),
        "key_points": [
            "Do not catch the slash mid-swing - its 180-degree arc takes 0.25 seconds",
            "Burst 1 meter in the 0.15 second retraction window",
            "Jam the weapon arm with the 360 defense on entry",
            "Convert instantly to two-on-one control",
            "Counter with knees while the weapon arm stays pinned",
        ],
        "requirements": [
            "A rubber training knife with a visible edge marker",
            "A partner slashing at controlled speed",
        ],
        "standards": [
            "Krav Maga Worldwide: slash defenses are advanced blue belt material",
            "FEKM: timing-based entries are graded at advanced levels",
        ],
        "citations": [CIT_LEVINE, CIT_FEKM],
        "sig_lens": (
            "Signature lens: the slash defense is the covenant of timing - "
            "the body waits 0.25 seconds, then signs 1 meter in 0.15, "
            "inside the arc."
        ),
    },
    {
        "key": "knife_overhead_stab",
        "name": "Krav Maga Defense Against an Overhead Knife Stab",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The overhead stab - the classic icepick attack - drops the "
            "blade from above. A stab descending 1.2 meters at 6 meters per "
            "second reaches the target in 0.2 seconds, so the defense must "
            "intercept, not evade: both forearms chop up at 45 degrees to "
            "meet the stabbing arm while the body bursts forward and "
            "slightly offline, and the other hand is already punching. The "
            "block and the counter are one motion inside that 0.2 second "
            "window, followed by two-on-one control of the knife arm and "
            "the full combatives finish."
        ),
        "how_it_works": (
            "Step 1: as the knife rises overhead, chop both forearms up at "
            "45 degrees to intercept the stabbing arm - inside the 0.2 "
            "second window. Step 2: burst forward and slightly offline as "
            "you intercept, smothering the stab's power. Step 3: the "
            "non-blocking hand punches immediately - block and counter are "
            "one motion. Step 4: convert to two-on-one control of the knife "
            "arm and drive knees and elbows. Step 5: secure the knife after "
            "the attacker is down, then disengage and scan."
        ),
        "key_points": [
            "Intercept at 45 degrees with both forearms - inside 0.2 seconds",
            "A 1.2 meter stab at 6 meters per second cannot be outrun, only intercepted",
            "Burst forward and slightly offline while intercepting",
            "Block and counter are one simultaneous motion",
            "Two-on-one control, combatives, then secure and disengage",
        ],
        "requirements": [
            "A rubber training knife",
            "Forearm guards for interception repetitions",
        ],
        "standards": [
            "Krav Maga Worldwide: overhead stab defense is advanced material",
            "IKMF: stab defenses are tested at advanced practitioner grades",
        ],
        "citations": [CIT_LEVINE, CIT_IKMF],
        "sig_lens": (
            "Signature lens: the overhead-stab defense is the covenant of "
            "interception - both forearms sign upward at 45 degrees, and "
            "the falling blade meets its answer."
        ),
    },
    {
        "key": "handgun_front",
        "name": "Krav Maga Defense Against a Handgun Threat from the Front",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A handgun threat from the front is answered only when the gun "
            "is within arm's reach: redirect the muzzle, control the "
            "weapon, counterattack. The defending hand travels 0.5 meters "
            "at about 8 meters per second - 0.0625 seconds - to sweep the "
            "muzzle about 45 degrees off the body while the torso bursts "
            "offline. Both hands then clamp the weapon with about 600 "
            "newtons of control as knees and strikes break the attacker's "
            "grip. This is a last-resort technique for when compliance "
            "would be worse - distance and escape are always preferred when "
            "they exist."
        ),
        "how_it_works": (
            "Step 1: confirm the gun is within arm's reach - this defense "
            "only works in contact range. Step 2: sweep the muzzle about "
            "45 degrees off your body in 0.0625 seconds while bursting your "
            "torso offline. Step 3: clamp both hands onto the weapon - "
            "about 600 newtons of control - keeping the muzzle pointed away. "
            "Step 4: counterattack with knees, punches, and kicks while "
            "holding the weapon. Step 5: strip the gun only after the "
            "attacker is down, then leave immediately."
        ),
        "key_points": [
            "Only when the gun is within arm's reach - otherwise comply or escape",
            "Redirect the muzzle about 45 degrees off the body in 0.0625 seconds",
            "Burst the torso offline as the hand redirects",
            "Two-hand control: about 600 newtons on the weapon",
            "Counter, strip only when safe, then leave immediately",
        ],
        "requirements": [
            "A brightly colored inert training gun - never a real firearm",
            "Expert supervision; this is last-resort material",
        ],
        "standards": [
            "Krav Maga Worldwide: handgun defenses are advanced brown belt material",
            "IKMF: firearm defenses are taught only at advanced grades with inert trainers",
        ],
        "citations": [CIT_LEVINE, CIT_IKMF],
        "sig_lens": (
            "Signature lens: the front handgun defense is the covenant of "
            "the last resort - the hand signs 45 degrees in a sixteenth "
            "of a second, and the body is already gone."
        ),
    },
    {
        "key": "multiple_attackers",
        "name": "Krav Maga Multiple Attacker Defense",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Against multiple attackers, krav maga's doctrine is stacking: "
            "move constantly so the attackers line up behind each other and "
            "only one can reach you at a time. Footwork keeps all threats "
            "inside a 60-degree cone in front of you - never let one circle "
            "behind. The defender circles 3 meters in about 1 second, "
            "scans each attacker in a 0.5 second cycle, strikes the nearest "
            "threat with full retzev, and never stays in one spot longer "
            "than 2 seconds. The goal is always escape through the gap the "
            "movement creates."
        ),
        "how_it_works": (
            "Step 1: burst toward the nearest gap - never back into a "
            "corner. Step 2: circle constantly, about 3 meters per second, "
            "keeping every attacker inside a 60-degree cone ahead of you. "
            "Step 3: strike the closest attacker with full continuous "
            "combatives to drop or drive them back. Step 4: scan on a 0.5 "
            "second cycle - eyes move, feet move, never fixate on one "
            "attacker. Step 5: take the first escape route the movement "
            "opens; fighting multiple attackers to a finish is the failure "
            "mode."
        ),
        "key_points": [
            "Stack the attackers - keep them lined up so only one reaches you",
            "Keep all threats inside a 60-degree cone; never let one behind you",
            "Circle about 3 meters per second; never stay put longer than 2 seconds",
            "Scan on a 0.5 second cycle - eyes and feet always moving",
            "Escape through the gap; finishing multiple attackers is the failure mode",
        ],
        "requirements": [
            "Two or more partners attacking at controlled intensity",
            "A large open area with clear escape routes marked",
        ],
        "standards": [
            "Krav Maga Worldwide: multiple-attacker tactics are advanced curriculum",
            "IKMF: stacking and escape are tested at advanced grades",
        ],
        "citations": [CIT_LEVINE, CIT_IKMF],
        "sig_lens": (
            "Signature lens: multiple-attacker defense is the covenant of "
            "the moving cone - 60 degrees of attention, 3 meters a "
            "second, and the gap is the signature's exit."
        ),
    },
    {
        "key": "handgun_behind",
        "name": "Krav Maga Defense Against a Handgun Threat from Behind",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A handgun pressed to the back is answered with a violent spin: "
            "the defender pivots 180 degrees toward the gun side in about "
            "0.4 seconds - about 7.85 radians per second - sweeping the "
            "muzzle offline as the turn completes, then clamping two-on-one "
            "control and counterattacking within 0.5 seconds of the turn's "
            "start. Turning toward the weapon, with the sweeping arm "
            "already moving, means the muzzle is redirected before the "
            "attacker can track the spin. Like all firearm defenses, this "
            "is last-resort material for contact range when escape and "
            "compliance are worse options."
        ),
        "how_it_works": (
            "Step 1: feel the muzzle's position - the turn goes toward the "
            "gun side. Step 2: pivot 180 degrees in about 0.4 seconds, "
            "sweeping the near hand across to redirect the muzzle offline "
            "as you turn. Step 3: clamp both hands onto the weapon - "
            "two-on-one control - the instant the turn completes. Step 4: "
            "counterattack with knees and strikes while holding the weapon, "
            "all within 0.5 seconds of the turn's start. Step 5: strip the "
            "gun only after the attacker is down, then leave immediately."
        ),
        "key_points": [
            "Turn toward the gun side - never away from the muzzle",
            "Pivot 180 degrees in about 0.4 seconds - about 7.85 radians per second",
            "Sweep the muzzle offline as the turn completes",
            "Two-on-one control the instant the turn ends",
            "Counter within 0.5 seconds of the turn's start; strip only when safe",
        ],
        "requirements": [
            "A brightly colored inert training gun - never a real firearm",
            "Expert supervision; last-resort material only",
        ],
        "standards": [
            "Krav Maga Worldwide: rear handgun defense is expert-level material",
            "IKMF: rear firearm defenses are taught only at the highest grades",
        ],
        "citations": [CIT_LEVINE, CIT_IKMF],
        "sig_lens": (
            "Signature lens: the rear handgun defense is the covenant of "
            "the spin - 180 degrees signed in 0.4 seconds, and the muzzle "
            "finds only the turn's wake."
        ),
    },
    {
        "key": "long_gun",
        "name": "Krav Maga Defense Against a Long Gun Threat",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A long gun - rifle or shotgun - threat from the front is "
            "answered like the handgun defense but with a longer weapon to "
            "control: the barrel is about 1.0 meter of leverage the "
            "attacker can swing. The defender redirects the muzzle offline "
            "with a 0.8 meter sidestep, clamps two-on-one control with "
            "about 700 newtons - more than the handgun's 600, because the "
            "longer weapon gives the attacker more leverage - and "
            "counterattacks while pinning the barrel away, securing control "
            "within 0.3 seconds of the redirect. The longer the weapon, "
            "the more critical the offline step."
        ),
        "how_it_works": (
            "Step 1: confirm contact range - the muzzle must be reachable. "
            "Step 2: sidestep 0.8 meters offline while sweeping the barrel "
            "away from your body with the near hand. Step 3: clamp both "
            "hands onto the weapon - about 700 newtons of two-on-one "
            "control - within 0.3 seconds of the redirect. Step 4: drive "
            "knees and strikes into the attacker while pinning the barrel "
            "away from everyone. Step 5: strip the long gun only after the "
            "attacker is controlled, then leave immediately."
        ),
        "key_points": [
            "Only at contact range - the muzzle must be reachable",
            "Sidestep 0.8 meters offline; the longer the weapon, the bigger the step",
            "Two-on-one control: about 700 newtons within 0.3 seconds",
            "Pin the barrel away from yourself and any bystanders",
            "Counter, strip only when safe, then leave immediately",
        ],
        "requirements": [
            "An inert long-gun trainer - never a real firearm",
            "Expert supervision; last-resort material only",
        ],
        "standards": [
            "Krav Maga Worldwide: long gun defenses are expert-level material",
            "IKMF: long-gun defenses are taught only at the highest grades",
        ],
        "citations": [CIT_LEVINE, CIT_IKMF],
        "sig_lens": (
            "Signature lens: the long-gun defense is the covenant of the "
            "long redirect - 0.8 meters offline, 700 newtons of control, "
            "and the barrel signs at empty air."
        ),
    },
    {
        "key": "third_party",
        "name": "Krav Maga Third-Party Protection",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Third-party protection means shielding another person - a "
            "child, a partner, a stranger - from an attack. Krav maga's "
            "doctrine is simple: put your body between the threat and the "
            "protectee, move the protectee to cover, and fight from the "
            "shield position. Shoving a 60 kilogram protectee 2 meters to "
            "cover in 1 second takes about 2 meters per second of push "
            "speed - roughly 4 meters per second squared of acceleration, "
            "or about 240 newtons of shove. You fight one-handed if you "
            "must, keeping the other arm as the shield wall, and you "
            "disengage toward cover, never away from the person you are "
            "protecting."
        ),
        "how_it_works": (
            "Step 1: step between the threat and the protectee, making "
            "your body the wall. Step 2: shove or drag the protectee 2 "
            "meters toward cover - about 240 newtons of push - while "
            "keeping your guard toward the threat. Step 3: fight from the "
            "shield position with punches, elbows, and kicks, one arm "
            "always screening the protectee. Step 4: keep moving toward "
            "cover - 5 meters in about 2.5 seconds - never letting the "
            "threat get an angle around you. Step 5: once the protectee is "
            "behind cover, disengage to cover yourself."
        ),
        "key_points": [
            "Your body is the wall between the threat and the protectee",
            "Move the protectee 2 meters to cover - about 240 newtons of shove",
            "Fight one-handed if needed; one arm always screens",
            "Advance toward cover at about 2 meters per second",
            "Never let the threat get an angle around you",
        ],
        "requirements": [
            "A partner playing the protectee and one as the threat",
            "A marked cover position 5 meters from the start",
        ],
        "standards": [
            "Krav Maga Worldwide: third-party protection is advanced curriculum",
            "IKMF: protection of others is tested at expert grades",
        ],
        "citations": [CIT_LEVINE, CIT_IKMF],
        "sig_lens": (
            "Signature lens: third-party protection is the covenant of the "
            "wall - the body signs itself between danger and the other, "
            "and holds the line."
        ),
    },
    {
        "key": "stress_drills",
        "name": "Krav Maga Stress Drills and Scenario Training",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Techniques learned calm fail under adrenaline unless they are "
            "drilled under stress. Krav maga's stress drills push the heart "
            "rate to 150-170 beats per minute - through sprints, striking "
            "flurries, and chaos - then demand technique, because fine "
            "motor skill degrades about 30 percent at 170 beats per minute "
            "and only gross, drilled movements survive. The standard session "
            "runs 5 scenarios of 3 minutes each - 15 minutes of continuous "
            "pressure - with attackers, noise, low light, and fatigue, "
            "training the student to decide and act when thinking is hard."
        ),
        "how_it_works": (
            "Step 1: elevate the heart rate to 150-170 beats per minute "
            "with a 60-second sprint or striking flurry. Step 2: enter the "
            "scenario immediately - grab, choke, weapon threat, multiple "
            "attackers - with no rest. Step 3: execute the drilled defense "
            "and retzev while partners add noise, shoving, and changing "
            "attacks. Step 4: run 5 scenarios of 3 minutes each - 15 "
            "minutes total - rotating roles. Step 5: debrief every scenario: "
            "what worked at 170 beats per minute is what you actually own."
        ),
        "key_points": [
            "Drive the heart rate to 150-170 beats per minute before technique",
            "Fine motor skill degrades about 30 percent at 170 beats per minute",
            "5 scenarios of 3 minutes each - 15 minutes of continuous pressure",
            "Add noise, low light, fatigue, and changing attacks",
            "What works at 170 beats per minute is what you actually own",
        ],
        "requirements": [
            "A safe training area with mats and clear boundaries",
            "A heart-rate monitor or pulse check between scenarios",
            "Trained partners who can pressure without injuring",
        ],
        "standards": [
            "Krav Maga Worldwide: stress and scenario training caps every level",
            "IKMF: fight-stress simulation is part of advanced grading",
        ],
        "citations": [CIT_LEVINE, CIT_IKMF],
        "sig_lens": (
            "Signature lens: stress drills are the covenant of proof - "
            "the technique signs at 170 beats per minute, or it was "
            "never truly signed."
        ),
    },
]
