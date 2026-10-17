#!/usr/bin/env python3
"""34 ladder-ordered Lethwei combat technique records (public + Signature lens).

Lethwei (Burmese bareknuckle boxing, 'the art of nine limbs') fact-checked
2026-10-17 against: Wikipedia 'Lethwei' (headbutt = Gowl Tite, punching =
Let Thee, elbow = Tel Daung, kicking = Kan, knee = Doo; traditional KO-or-draw
rules with one two-minute injury timeout per corner; tape-and-gauze hand wraps;
five 3-minute rounds; thaing umbrella; banshay shadowboxing; naban sparring;
kyar ba nyein circle training; Lekkha Moun and Lethwei Yay traditional
gestures), lethwei.net (knockout-only rule), lethwei.com (nine weapons),
fightersvault.com (techniques and rules summary), dojoandring.com (1952
Kyar Ba Nyein modernization, 2016 World Lethwei Championship),
mmafullcontact.com (banshay, naban, kyar ba nyein training methods).

Scope: civilian martial-arts training instruction only.
"""

SIG_TAIL = ("Signature Edition: his original Signature combat method - the "
            "nine limbs as nine covenants, the fighter's mark in every "
            "strike. Clearly labeled Signature-made, never presented as "
            "authentic public record.")

ENTRIES = [
# ---------------------------------------------------------------- FOUNDATIONS
{
    "key": "stance",
    "name": "The Lethwei Fighting Stance",
    "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
    "description": ("The Lethwei fighting stance is the platform every strike, "
                    "clinch entry, and headbutt is launched from. The feet sit "
                    "a little wider than shoulder width, lead foot forward, "
                    "weight balanced near 60 percent on the lead leg so the "
                    "front hand, elbow, knee, and the ninth limb - the head - "
                    "can all fire without a weight shift telegraphing the "
                    "attack. The chin tucks behind the lead shoulder, the "
                    "hands ride high, and the rear heel lifts slightly so the "
                    "hips stay loaded for kicks and knees. Because Lethwei "
                    "permits headbutts, the stance keeps the head forward and "
                    "alive rather than pulled back; a Lethwei fighter's head "
                    "is a weapon, not a liability."),
    "how_it_works": ("1. Step the lead foot forward so the feet are staggered "
                     "about one-and-a-half shoulder widths apart. 2. Turn the "
                     "lead foot slightly inward and keep the rear foot at "
                     "roughly 45 degrees so the hips can pivot for kicks. "
                     "3. Bend both knees softly and drop the center of "
                     "gravity until the thighs begin to load. 4. Carry "
                     "about 60 percent of the weight on the lead leg so the "
                     "front weapons - jab, front elbow, front knee, and "
                     "headbutt - can strike without stepping first. 5. Raise "
                     "both hands to cheek height, elbows tucked to the ribs, "
                     "chin tucked behind the lead shoulder. 6. Check the "
                     "stance by having a partner push the shoulders; the "
                     "fighter should absorb it without stepping."),
    "key_points": [
        "Feet wider than shoulder width, staggered, lead foot slightly inward",
        "Roughly 60 percent of weight on the lead leg keeps the front weapons loaded",
        "Chin tucked behind the lead shoulder, hands high, elbows to the ribs",
        "Rear heel lifted slightly so the hips stay free to pivot for kicks",
        "Head forward and alive - in Lethwei the head is the ninth limb, not a target to hide",
        "Stable against a shoulder push without stepping - the stance test",
    ],
    "requirements": [
        "Open training space at least two meters square",
        "Flat, non-slip surface (sand or mat is traditional)",
        "A partner to test stance stability",
    ],
    "standards": [
        "Thaing tradition: stance work precedes all striking (Wikipedia, Lethwei)",
        "Banshay foundation practice pairs stance with shadowboxing (mmafullcontact.com)",
        "Modern camps teach the high-guard lead-heavy stance for bareknuckle readiness",
    ],
    "citations": [
        "https://en.wikipedia.org/wiki/Lethwei",
        "https://www.mmafullcontact.com/introduction-to-lethwei/",
    ],
    "sig_lens": ("Signature lens: in the Signature method the stance is the "
                 "first covenant - the fighter signs his mark into the ground "
                 "before a single strike is thrown. The nine limbs are nine "
                 "promises, and the stance is where they are kept. Stand "
                 "wrong and every weapon downstream is a broken promise; "
                 "stand right and the whole ladder stands with you."),
},
{
    "key": "footwork",
    "name": "Footwork: The Lethwei Step",
    "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
    "description": ("Lethwei footwork is built on short, grounded steps that "
                    "never cross the feet and never bounce the head into "
                    "headbutt range by accident. The fighter advances by "
                    "stepping the lead foot first and dragging the rear foot "
                    "behind it, retreats by reversing the order, and circles "
                    "by stepping the lead foot around the outside. Because "
                    "knockout is the only certain victory under traditional "
                    "rules, Lethwei footwork is patient and forward-pressing: "
                    "cut the space, stay balanced, and keep every one of the "
                    "nine limbs within firing distance while denying the "
                    "opponent room to load up."),
    "how_it_works": ("1. From the fighting stance, advance: move the lead "
                     "foot six to eight inches forward, then drag the rear "
                     "foot the same distance to restore stance width. "
                     "2. Retreat: move the rear foot back first, then the "
                     "lead foot, so the feet never cross. 3. Circle left: "
                     "step the lead foot left and around while the rear foot "
                     "follows; the hips stay squared to the opponent. "
                     "4. Circle right: step the rear foot right and behind, "
                     "lead foot follows. 5. Pivot: plant the lead foot and "
                     "swing the rear foot 90 degrees to change the angle "
                     "without losing balance. 6. Drill each step for one "
                     "minute without pause, keeping the guard up the entire "
                     "time."),
    "key_points": [
        "Lead foot moves first when advancing; rear foot moves first when retreating",
        "Feet never cross - crossed feet invite sweeps and throws",
        "Steps stay short: six to eight inches keeps the base under the hips",
        "Circling keeps the hips squared to the opponent at all times",
        "Guard stays up through every step - footwork never drops the hands",
        "Forward pressure is the Lethwei habit: cut space, deny room, stay balanced",
    ],
    "requirements": [
        "Open space or a marked ring area",
        "The Lethwei fighting stance already learned",
        "A timer for one-minute step drills",
    ],
    "standards": [
        "Thaing footwork drills are the basis of banshay movement practice",
        "Traditional training: footwork drilled before any strike is taught",
        "Modern camps pair step drills with ring-cutting on the second week",
    ],
    "citations": [
        "https://en.wikipedia.org/wiki/Lethwei",
        "https://www.mmafullcontact.com/introduction-to-lethwei/",
    ],
    "sig_lens": ("Signature lens: the Signature method treats every step as "
                 "a signature stroke - short, deliberate, unmistakable. The "
                 "feet write the fighter's intent on the canvas before the "
                 "hands ever sign anything. Nine limbs, one path: the step "
                 "decides which limb arrives, and the Signature fighter "
                 "never lets his feet write a lie."),
},
{
    "key": "wraps",
    "name": "Hand Wrapping: Gauze and Tape",
    "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
    "description": ("Lethwei is bareknuckle: fighters wrap their hands with "
                    "only tape and gauze - historically hemp rope - with no "
                    "gloves, and officials inspect the wraps before the "
                    "bout. The wrap protects the knuckles and the small bones "
                    "of the hand while adding almost no padding, which is "
                    "exactly the point: the wrap is protection, not a "
                    "weapon. Proper wrapping binds the knuckles into a single "
                    "striking surface, locks the wrist so it cannot buckle on "
                    "impact, and leaves the fingers free to open for the "
                    "clinch. A badly wrapped hand breaks; a well wrapped "
                    "hand survives five rounds of bareknuckle impact."),
    "how_it_works": ("1. Spread the fingers and anchor the gauze around the "
                     "wrist with two full turns. 2. Run the gauze between "
                     "each finger, looping around the knuckles to bind them "
                     "into one surface. 3. Build three to four layers across "
                     "the knuckles, smoothing each layer flat - no lumps, "
                     "which become pressure points. 4. Figure-eight the wrist "
                     "and palm so the wrist is locked straight. 5. Tape over "
                     "the gauze in the same pattern, keeping the tape smooth "
                     "and even, never taping between bare skin and knuckle. "
                     "6. Flex the hand open and closed; the fingers must open "
                     "freely for clinching and the knuckles must feel like "
                     "one block."),
    "key_points": [
        "Only tape and gauze - no gloves, no extra padding, wraps inspected by officials",
        "Knuckles bound into a single striking surface across three to four smooth layers",
        "Wrist locked straight with a figure-eight so it cannot buckle on impact",
        "Fingers stay free to open for the clinch - a closed fist wrap is wrong",
        "No lumps or bunched tape: lumps become pressure points that split skin",
        "Historically hemp rope was used; modern bouts use gauze and tape",
    ],
    "requirements": [
        "Gauze roll and athletic tape",
        "A partner or trainer to wrap or inspect the first attempts",
        "Knowledge of the bout rule: wraps checked by officials before fighting",
    ],
    "standards": [
        "Traditional rule: hands wrapped with only gauze and tape, gloves forbidden (Wikipedia, Lethwei)",
        "Bout attire rules: wraps inspected in front of officials (fightersvault.com)",
        "Historical practice: hemp rope wraps in ancient sand-pit bouts (thesportsutopia.com)",
    ],
    "citations": [
        "https://en.wikipedia.org/wiki/Lethwei",
        "https://fightersvault.com/blog/lethwei-explained-the-brutal-martial-art-of-burmese-boxing",
        "https://thesportsutopia.com/lethwei/",
    ],
    "sig_lens": ("Signature lens: the wrap is the fighter's seal - the "
                 "Signature method treats wrapping as the moment the hands "
                 "are signed over to the nine limbs. Tape and gauze are the "
                 "oath made visible: thin enough to be honest, strong "
                 "enough to be kept. Sign the wrap right, and the hands "
                 "can keep every promise the stance made."),
},
{
    "key": "jab",
    "name": "The Jab: Let Thee",
    "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
    "description": ("The jab is the first of the Let Thee - the punching "
                    "weapons of Lethwei. Thrown straight from the lead hand, "
                    "it measures distance, interrupts the opponent's rhythm, "
                    "and opens the path for the cross, the elbow, and the "
                    "ninth limb. In Lethwei the jab is thrown with a bare "
                    "knuckle, so the wrist must be locked and the first two "
                    "knuckles must land - a sloppy jab with an unaligned "
                    "wrist breaks the hand instead of the opponent. The jab "
                    "snaps out with a quarter-turn of the fist and snaps "
                    "straight back to the guard, because in a nine-limb art "
                    "a hanging hand invites elbows and headbutts."),
    "how_it_works": ("1. From the stance, extend the lead hand straight "
                     "toward the target, driving from the lead shoulder "
                     "rather than swinging the arm. 2. Rotate the fist a "
                     "quarter turn so the palm faces down at full "
                     "extension. 3. Step the lead foot a few inches forward "
                     "as the punch travels, adding body weight to the "
                     "strike. 4. Lock the wrist dead straight so the first "
                     "two knuckles land flat. 5. Snap the hand straight "
                     "back to the cheek the instant it lands - the return "
                     "is as fast as the delivery. 6. Drill three-minute "
                     "rounds of jab-only shadowboxing, then jab on the "
                     "heavy bag, checking that the wrist never bends."),
    "key_points": [
        "Lead-hand straight punch: the measuring stick of the nine limbs",
        "Quarter-turn of the fist, palm down at full extension",
        "Wrist locked straight - bare knuckles punish a bent wrist",
        "First two knuckles land flat on the target",
        "Snaps back to the guard instantly; a hanging hand invites elbows and headbutts",
        "Sets up the cross, the elbow, and clinch entries",
    ],
    "requirements": [
        "Wrapped hands or hand protection for bag work",
        "Heavy bag or pads for impact practice",
        "Mirror or coach to check wrist alignment",
    ],
    "standards": [
        "Let Thee (punching) is the first of the five weapon families (lethwei.com)",
        "Bareknuckle mechanics: wrist alignment is the primary injury control",
        "Banshay drills begin with the jab before any other punch (mmafullcontact.com)",
    ],
    "citations": [
        "https://www.lethwei.com/",
        "https://www.mmafullcontact.com/introduction-to-lethwei/",
        "https://en.wikipedia.org/wiki/Lethwei",
    ],
    "sig_lens": ("Signature lens: the Signature method calls the jab the "
                 "first letter of the fighter's signature - straight, fast, "
                 "and legible. Every combination that follows is a sentence, "
                 "and the jab writes the first word: distance. A Signature "
                 "jab never lies about range, and it never lingers where "
                 "an elbow can answer it."),
},
{
    "key": "cross",
    "name": "The Cross: Let Thee",
    "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
    "description": ("The cross is the rear-hand straight punch of the Let "
                    "Thee family and the heaviest punch in the Lethwei "
                    "arsenal. Its power comes from the floor: the rear foot "
                    "drives, the hips rotate, the shoulder whips, and the "
                    "fist travels the straight line from the chin to the "
                    "target. Under traditional rules, where only a knockout "
                    "wins, the cross is the workhorse finisher - it carries "
                    "the full rotation of the body behind two bare "
                    "knuckles. The classic Lethwei one-two, jab followed by "
                    "cross, is the first combination every student learns, "
                    "and it remains the backbone of championship fights."),
    "how_it_works": ("1. From the stance, drive off the ball of the rear "
                     "foot as if pushing the floor away. 2. Rotate the hips "
                     "sharply so the rear hip swings toward the target. "
                     "3. Extend the rear hand straight from the chin along "
                     "the centerline, turning the fist palm-down at "
                     "extension. 4. Tuck the chin behind the lead shoulder "
                     "as the punch travels - the lead hand stays home to "
                     "guard. 5. Land with the wrist straight and the first "
                     "two knuckles, then retract along the same line. "
                     "6. Drill the one-two: jab sets the range, cross "
                     "follows through the opening, both hands home before "
                     "the count of one."),
    "key_points": [
        "Rear-hand straight punch - the heaviest punch in the arsenal",
        "Power chain: rear foot drives, hips rotate, shoulder whips, fist travels straight",
        "Chin tucks behind the lead shoulder while the lead hand guards",
        "Wrist straight, first two knuckles land - bareknuckle alignment",
        "Retracts along the same line it traveled",
        "The jab-cross one-two is the first combination and the lasting backbone of the art",
    ],
    "requirements": [
        "Wrapped hands for bag and pad work",
        "Heavy bag or focus mitts",
        "The jab already learned, since the one-two pairs them",
    ],
    "standards": [
        "Let Thee includes jabs, crosses, hooks, uppercuts, and spinning backfists (lethwei.com)",
        "Knockout-oriented power mechanics under traditional KO-or-draw rules (lethwei.net)",
        "One-two drilling is standard in modern Lethwei camps",
    ],
    "citations": [
        "https://www.lethwei.com/",
        "https://lethwei.net/knockout/",
        "https://en.wikipedia.org/wiki/Lethwei",
    ],
    "sig_lens": ("Signature lens: if the jab is the first letter, the cross "
                 "is the Signature fighter's full name - the whole body "
                 "signs it. The Signature method teaches the cross as a "
                 "covenant between the floor and the fist: the floor gives "
                 "the drive, the fist keeps the promise. Sign it straight, "
                 "sign it home, and let the guard write the period."),
},
{
    "key": "guard",
    "name": "The Lethwei Guard and Shell",
    "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
    "description": ("The Lethwei guard is a high, tight shell built for a "
                    "sport where elbows, knees, and the headbutt all come "
                    "from inside punching range. Both hands ride at cheek "
                    "height, the forearms form a vertical wall in front of "
                    "the body, and the elbows pin to the ribs so that hooks "
                    "to the body, knees, and elbow strikes meet bone instead "
                    "of soft targets. Because the headbutt is legal, the "
                    "guard also manages head position: the forehead can "
                    "press into the opponent's guard as a frame, but the "
                    "chin never lifts and the eyes never drop. A Lethwei "
                    "guard is never a hiding place - it is a loaded spring "
                    "that fires the elbows back."),
    "how_it_works": ("1. Raise both hands to cheek height, palms facing "
                     "inward, knuckles at the level of the cheekbones. "
                     "2. Pin both elbows tight to the ribs - no daylight "
                     "between elbow and body. 3. Hold the forearms vertical, "
                     "forming a wall from chin to belt line. 4. Tuck the "
                     "chin down behind the lead forearm and keep the eyes "
                     "up, watching the opponent's shoulders and hips. "
                     "5. To shell: when pressured, press the forearms "
                     "together and lean the forehead slightly forward into "
                     "the frame, letting strikes land on bone. 6. Drill: "
                     "partner taps the guard with pads from all angles "
                     "while the fighter keeps the shell sealed and the "
                     "eyes open."),
    "key_points": [
        "Hands at cheek height, forearms vertical, elbows pinned to the ribs",
        "Forearms form a wall from chin to belt line",
        "Chin tucked behind the lead forearm, eyes always up",
        "Forehead can frame forward - legal and useful with headbutts in play",
        "Shelling: press forearms together under pressure, absorb on bone",
        "The guard is a loaded spring - elbows fire back from the shell",
    ],
    "requirements": [
        "Focus mitts or a partner for guard-tap drills",
        "The stance and footwork already comfortable",
    ],
    "standards": [
        "Close-range defense is essential with elbows, knees, and headbutts legal (Wikipedia, Lethwei)",
        "Shelling against the nine limbs is taught before sparring in traditional camps",
        "Eyes-up discipline is enforced in banshay before contact work",
    ],
    "citations": [
        "https://en.wikipedia.org/wiki/Lethwei",
        "https://www.mmafullcontact.com/introduction-to-lethwei/",
    ],
    "sig_lens": ("Signature lens: the Signature method calls the guard the "
                 "unbroken seal - the fighter's promise to himself that no "
                 "limb enters uninvited. Nine weapons outside the wall, "
                 "nine covenants inside it. The seal does not hide the "
                 "fighter; it keeps his signature legible until he chooses "
                 "to sign the next strike."),
},
{
    "key": "lowkick",
    "name": "The Low Kick: Kan",
    "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
    "description": ("The low kick is the first of the Kan - the kicking "
                    "weapons - and the safest kick to learn. Thrown with the "
                    "shin against the opponent's lead thigh, it deadens the "
                    "leg, slows footwork, and punishes every step forward. "
                    "Lethwei low kicks are thrown with full hip rotation and "
                    "land with the hard shin, not the foot; the supporting "
                    "foot pivots so the hips turn completely over, and the "
                    "same-side arm swings down for balance and protection. "
                    "Accumulated low kicks decide fights: a fighter whose "
                    "lead leg is destroyed cannot step into his punches or "
                    "escape the clinch."),
    "how_it_works": ("1. From the stance, step the lead foot slightly to "
                     "the outside to open the angle. 2. Pivot hard on the "
                     "supporting foot, turning the toes away from the "
                     "target as the hips rotate. 3. Swing the kicking leg "
                     "like a bat, keeping it relaxed until the moment of "
                     "impact. 4. Land with the middle of the shin on the "
                     "opponent's lead thigh, hips fully turned over. "
                     "5. Swing the same-side arm down past the hip for "
                     "balance and to shield against counters. 6. Retract "
                     "the leg along the same path and reset the stance - "
                     "never leave the leg hanging."),
    "key_points": [
        "Kan weapon number one: the shin-driven low kick to the lead thigh",
        "Impact with the middle of the shin, never the foot or ankle",
        "Supporting foot pivots fully so the hips turn completely over",
        "Same-side arm swings down for balance and counter protection",
        "Retract along the same path - a hanging leg is caught and swept",
        "Cumulative damage: deadens the leg, kills footwork, sets up the clinch",
    ],
    "requirements": [
        "Heavy bag or thigh pads for impact practice",
        "Bare shins conditioned gradually - start light",
        "The stance and hip pivot already learned",
    ],
    "standards": [
        "Kan (kicking) covers low kicks, roundhouses, hook kicks, axe kicks, and spinning back kicks (lethwei.com)",
        "Shin-on-thigh mechanics shared with the broader thaing kicking tradition",
        "Conditioning the shins is standard camp practice (mmafullcontact.com)",
    ],
    "citations": [
        "https://www.lethwei.com/",
        "https://www.mmafullcontact.com/introduction-to-lethwei/",
        "https://en.wikipedia.org/wiki/Lethwei",
    ],
    "sig_lens": ("Signature lens: the Signature method treats the low kick "
                 "as the foundation stone - the first Kan covenant, signed "
                 "against the opponent's base. You do not attack the fighter "
                 "first; you attack the ground he stands on. Every low kick "
                 "is a reminder written on his lead leg that the Signature "
                 "fighter owns the floor."),
},
{
    "key": "footthrust",
    "name": "The Foot Thrust: Kan",
    "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
    "description": ("The foot thrust - the pushing kick of the Kan family - "
                    "is Lethwei's distance manager. Thrown with the sole of "
                    "the foot into the opponent's hip, thigh, or torso, it "
                    "stops a rushing attacker cold, breaks the clinch before "
                    "it forms, and buys the half-second needed to reload the "
                    "hands. Unlike the roundhouse, the foot thrust pushes "
                    "rather than snaps: the knee chambers high, the hips "
                    "drive forward, and the sole lands flat and shoves. It "
                    "is the polite weapon of a brutal art - control first, "
                    "damage second - and the best defense against an "
                    "opponent who wants to drag the fight into headbutt "
                    "range."),
    "how_it_works": ("1. From the stance, lift the lead knee high, chambered "
                     "tight to the chest. 2. Lean the torso slightly back "
                     "to load the hips. 3. Drive the hips forward and extend "
                     "the leg, landing the flat sole on the opponent's hip "
                     "or torso. 4. Push through the target with the whole "
                     "body weight behind the sole - shove, do not snap. "
                     "5. Snap the knee back to the chamber and place the "
                     "foot down in stance. 6. Drill against a partner "
                     "walking forward: stop each advance with the thrust, "
                     "never letting them reach clinch range."),
    "key_points": [
        "Kan distance weapon: sole of the foot into hip, thigh, or torso",
        "Knee chambers high and tight, hips drive forward, sole lands flat",
        "Pushes through the target with body weight - a shove, not a snap",
        "Stops rushes cold and breaks clinch entries before they form",
        "The best range keeper against an opponent hunting headbutt distance",
        "Chamber and retract crisply - a lazy thrust is caught and dumped",
    ],
    "requirements": [
        "Heavy bag or body shield for push practice",
        "A partner willing to walk forward for range drills",
        "Chambered-knee balance from stance work",
    ],
    "standards": [
        "Foot-thrust is listed among the core Lethwei techniques (Wikipedia, Lethwei)",
        "Range management is a required skill before clinch sparring in traditional camps",
        "Push-kick mechanics belong to the Kan weapon family (lethwei.com)",
    ],
    "citations": [
        "https://en.wikipedia.org/wiki/Lethwei",
        "https://www.lethwei.com/",
    ],
    "sig_lens": ("Signature lens: the Signature method calls the foot thrust "
                 "the doorkeeper - the covenant that decides which limbs "
                 "may enter. It signs a line in the air: this far, no "
                 "farther. A Signature fighter does not chase; he posts "
                 "the boundary with his sole and lets the opponent break "
                 "himself against it."),
},
{
    "key": "banshay",
    "name": "Shadowboxing: Banshay",
    "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
    "description": ("Banshay is the traditional shadowboxing of the thaing "
                    "arts and the foundation of Lethwei training. Fought "
                    "against an imagined opponent, it drills technique, "
                    "footwork, and flow without impact - the fighter moves "
                    "through full combinations, defenses, clinch entries, "
                    "and counters in rhythm, building the muscle memory "
                    "that bareknuckle fighting demands. Banshay is done in "
                    "rounds like a fight, usually three minutes, and a "
                    "serious student performs many rounds daily. It is also "
                    "where a fighter's personal style is born: the "
                    "combinations that flow in banshay are the ones that "
                    "appear under pressure."),
    "how_it_works": ("1. Set a timer for three-minute rounds with one "
                     "minute of rest, matching a bout. 2. Round one: move "
                     "and jab only, focusing on footwork and stance. "
                     "3. Round two: add the cross, hooks, and uppercuts - "
                     "the full Let Thee. 4. Round three: add kicks, knees, "
                     "and elbows, moving through complete nine-limb "
                     "combinations. 5. Round four: practice defense - slip, "
                     "block, shell, and counter an imaginary attack. "
                     "6. Finish every round in stance, hands up, breathing "
                     "controlled - train the recovery as well as the work."),
    "key_points": [
        "Banshay: traditional shadowboxing against an imagined opponent",
        "Builds technique, footwork, and combination flow without impact",
        "Done in three-minute rounds with one-minute rests, like a bout",
        "Early rounds isolate tools; later rounds blend all nine limbs",
        "Defense rounds: slip, block, shell, and counter the imaginary attack",
        "Personal style is born in banshay - what flows here appears under pressure",
    ],
    "requirements": [
        "Open space and a round timer",
        "The stance, footwork, and basic strikes already learned",
        "A mirror is helpful for checking form",
    ],
    "standards": [
        "Banshay is the documented traditional training method of Lethwei (mmafullcontact.com)",
        "Shadowboxing is the required daily practice in thaing camps",
        "Round structure mirrors the three-minute bout rounds (Wikipedia, Lethwei)",
    ],
    "citations": [
        "https://www.mmafullcontact.com/introduction-to-lethwei/",
        "https://en.wikipedia.org/wiki/Lethwei",
    ],
    "sig_lens": ("Signature lens: banshay is the Signature rehearsal - the "
                 "fighter signs his name in the air a thousand times before "
                 "he signs it on an opponent. The Signature method treats "
                 "every shadowboxing round as a draft of the final "
                 "document: revise the flow, sharpen the letters, and when "
                 "the bout comes, sign it without hesitation."),
},
{
    "key": "conditioning",
    "name": "Conditioning the Body for Bareknuckle",
    "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
    "description": ("Bareknuckle fighting demands a body built for impact: "
                    "knuckles, wrists, shins, and the core must all be "
                    "conditioned long before a fighter steps into the ring. "
                    "Traditional Lethwei conditioning pairs roadwork and "
                    "rope skipping for the engine with bag work for the "
                    "weapons - heavy bag rounds harden the knuckles and "
                    "shins, pad rounds sharpen timing, and bodyweight "
                    "exercises build the neck and core that absorb headbutts "
                    "and clinch wrestling. Conditioning is progressive: the "
                    "body adapts to small, repeated loads, never to sudden "
                    "punishment. A fighter who skips conditioning does not "
                    "get tough in the ring - he gets broken."),
    "how_it_works": ("1. Build the engine first: run or skip rope for 20 "
                     "to 30 minutes, three to five days a week. 2. Harden "
                     "the weapons gradually: start with light bag rounds "
                     "and add one round per week, letting the knuckles and "
                     "shins adapt. 3. Strengthen the neck with controlled "
                     "bridges and resistance work - the neck absorbs "
                     "clinch pulls and headbutt collisions. 4. Build the "
                     "core with planks, leg raises, and rotational work so "
                     "the body can take knees and body kicks. 5. Increase "
                     "loads by about ten percent per week, never more. "
                     "6. Rest and eat: adaptation happens in recovery, not "
                     "in the workout."),
    "key_points": [
        "Engine first: roadwork and rope skipping build fight endurance",
        "Weapons hardened progressively - bag work, one added round per week",
        "Neck strengthening absorbs clinch pulls and headbutt collisions",
        "Core work lets the body take knees and body kicks",
        "Loads increase about ten percent per week, never by sudden punishment",
        "Adaptation happens in recovery - rest and food are part of training",
    ],
    "requirements": [
        "Running space or a jump rope",
        "Heavy bag and pads",
        "A progressive weekly plan written down and followed",
    ],
    "standards": [
        "Conditioning for bareknuckle impact is standard Lethwei camp practice (mmafullcontact.com)",
        "Progressive loading is the accepted principle of combat conditioning",
        "Bout readiness requires the five-round engine under modern rules (Wikipedia, Lethwei)",
    ],
    "citations": [
        "https://www.mmafullcontact.com/introduction-to-lethwei/",
        "https://en.wikipedia.org/wiki/Lethwei",
    ],
    "sig_lens": ("Signature lens: conditioning is the Signature method's "
                 "proof of seriousness - the fighter tempers his own "
                 "instruments before he uses them. Knuckles, shins, neck, "
                 "and core are the pen, and a Signature fighter never signs "
                 "with a broken pen. The covenant is simple: the body must "
                 "be worthy of the nine limbs it carries."),
},
{
    "key": "yay",
    "name": "The Traditional Opening: Lethwei Yay",
    "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
    "description": ("Before a traditional Lethwei bout, fighters perform the "
                    "Lethwei Yay - the pre-fight ritual dance that honors "
                    "teachers, ancestors, and the art itself. Alongside the "
                    "Lekkha Moun warrior dance, it is part of the "
                    "traditional gesture that opens every proper bout: slow, "
                    "deliberate movements that display the fighter's style, "
                    "warm the body, and settle the mind before the violence "
                    "begins. The Yay is also tactical - it lets each fighter "
                    "read the other's movement, stance, and temperament "
                    "before the first exchange. To skip the ritual is to "
                    "skip the art; the fight begins with respect, not with "
                    "a punch."),
    "how_it_works": ("1. Enter the ring and face the center, standing tall "
                     "in a relaxed stance. 2. Begin the slow dance "
                     "movements: deliberate steps, flowing arm motions, and "
                     "guard postures that display the fighter's style. "
                     "3. Perform the challenge gestures toward the "
                     "opponent - the Lethwei Yay is also a formal "
                     "declaration of readiness. 4. Use the ritual time to "
                     "breathe deeply, warm the joints, and observe the "
                     "opponent's stance and movement habits. 5. End the "
                     "ritual by touching gloves or the traditional "
                     "acknowledgment, then take the fighting stance. "
                     "6. Carry the calm of the ritual into the first "
                     "exchange - the mind that is settled strikes clean."),
    "key_points": [
        "Lethwei Yay: the pre-fight ritual dance honoring teachers, ancestors, and the art",
        "Performed with the Lekkha Moun warrior dance as the traditional opening gesture",
        "Displays the fighter's style while warming the body and settling the mind",
        "Tactical value: read the opponent's stance, movement, and temperament early",
        "The fight begins with respect, not with a punch",
        "Ritual calm carries into the first exchange",
    ],
    "requirements": [
        "Knowledge of the traditional forms from a qualified teacher",
        "A bout or demonstration setting that honors the ritual",
        "Respect for the tradition - the ritual is never rushed or mocked",
    ],
    "standards": [
        "Lekkha Moun and Lethwei Yay are the documented traditional gestures (Wikipedia, Lethwei)",
        "Traditional bouts open with the ritual before fighting begins",
        "The ritual is part of the thaing cultural heritage of Myanmar",
    ],
    "citations": [
        "https://en.wikipedia.org/wiki/Lethwei",
        "https://thesportsutopia.com/lethwei/",
    ],
    "sig_lens": ("Signature lens: the Signature method treats the Yay as "
                 "the title page - the fighter presents his name, his "
                 "lineage, and his intent before the document of the fight "
                 "is written. A Signature fighter performs the ritual "
                 "completely because the signature at the top of the page "
                 "is what makes everything below it official."),
},

# ---------------------------------------------------------------- COMPOUNDED
{
    "key": "hooks",
    "name": "Hooks and Uppercuts: Let Thee",
    "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
    "description": ("The hook and the uppercut complete the Let Thee punching "
                    "family. The hook travels in a horizontal arc, the arm "
                    "bent at ninety degrees, landing with the knuckles on the "
                    "side of the target; the uppercut rises vertically from "
                    "below, driven by the legs, landing under the chin or "
                    "into the body. Both are close-range weapons that thrive "
                    "in the phone-booth distances Lethwei creates - after a "
                    "slipped punch, inside a broken clinch, or when the "
                    "opponent shells up. Because they are thrown bent-armed, "
                    "hooks and uppercuts pair naturally with the elbows that "
                    "follow them: the hook becomes the horizontal elbow with "
                    "one short step of the arm."),
    "how_it_works": ("1. Hook: from the guard, raise the lead elbow to "
                     "shoulder height with the arm bent at ninety degrees. "
                     "2. Pivot the lead foot and rotate the hips sharply, "
                     "swinging the fist in a tight horizontal arc. "
                     "3. Land with the knuckles, wrist straight, then snap "
                     "back to guard. 4. Uppercut: drop the weight slightly "
                     "by bending the knees. 5. Drive up through the legs "
                     "and hips, punching vertically with the palm facing "
                     "the fighter's own chest. 6. Land under the target "
                     "with a straight wrist, then drop the hand back to "
                     "guard - never loop the uppercut wide."),
    "key_points": [
        "Hook: bent-arm horizontal arc, knuckles land, wrist straight",
        "Uppercut: vertical punch driven by the legs, lands from below",
        "Both are close-range weapons for the distances Lethwei creates",
        "Hook flows into the horizontal elbow - one short step of the arm",
        "Uppercut never loops wide; it rises straight and returns straight",
        "Best thrown after a slip, inside a broken clinch, or against a shell",
    ],
    "requirements": [
        "The jab and cross already solid - the straight punches come first",
        "Heavy bag or uppercut bag for arc practice",
        "Wrapped hands; bent-arm punches still punish bad wrists",
    ],
    "standards": [
        "Hooks and uppercuts belong to the Let Thee family (lethwei.com)",
        "Close-range punching is core to the nine-limb system (Wikipedia, Lethwei)",
        "Hook-to-elbow flow is standard in thaing combination teaching",
    ],
    "citations": [
        "https://www.lethwei.com/",
        "https://en.wikipedia.org/wiki/Lethwei",
    ],
    "sig_lens": ("Signature lens: the hook and uppercut are the Signature "
                 "fighter's curved letters - the straight punches wrote the "
                 "sentence, and now the hand learns to sign around corners. "
                 "The Signature method teaches them as answers: the opponent "
                 "writes a question with his guard, and the curved punch "
                 "signs the reply where the straight line cannot reach."),
},
{
    "key": "elbow",
    "name": "The Elbow: Tel Daung",
    "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
    "description": ("The elbow - Tel Daung - is the signature weapon of close "
                    "Lethwei fighting and the reason the art is so feared "
                    "inside punching range. Thrown horizontally, upward, or "
                    "downward, the elbow concentrates the entire rotation of "
                    "the body into a few inches of bone, and bareknuckle "
                    "elbows cut with terrible efficiency. The horizontal "
                    "elbow mirrors the hook's path with the arm folded; the "
                    "upward elbow mirrors the uppercut; both are thrown with "
                    "a violent hip turn and the full weight of the torso "
                    "behind them. In Lethwei, where fights are won by "
                    "knockout, the elbow is the great equalizer of the "
                    "clinch break and the close exchange."),
    "how_it_works": ("1. Horizontal elbow: raise the lead elbow to shoulder "
                     "height, forearm folded tight, hand near the own "
                     "shoulder. 2. Pivot the lead foot and whip the hips "
                     "around, swinging the elbow horizontally across the "
                     "target. 3. Strike with the point of the elbow, arm "
                     "staying folded - never extend into a punch. 4. Upward "
                     "elbow: drop the weight slightly, then drive up with "
                     "the legs, spearing the elbow point upward under the "
                     "target. 5. Return the elbow to the guard along the "
                     "same path. 6. Drill on pads held close - elbows are "
                     "a close-range weapon, so practice starts at arm's "
                     "length, not at punching range."),
    "key_points": [
        "Tel Daung: the elbow, Lethwei's great close-range equalizer",
        "Horizontal, upward, and downward - the hook and uppercut folded into bone",
        "Whole-body rotation concentrated into inches of elbow point",
        "Arm stays folded; the elbow is never extended into a punch",
        "Thrown with violent hip turn and full torso weight",
        "The clinch break and close exchange are its natural home",
    ],
    "requirements": [
        "Elbow pads or a partner holding pads at close range",
        "The hook and uppercut mechanics already learned",
        "Control: elbows are practiced at reduced power on partners",
    ],
    "standards": [
        "Tel Daung is the documented Burmese term for the elbow (Wikipedia, Lethwei)",
        "Horizontal, upward, flying, and spinning elbows are the recognized set (lethwei.com)",
        "Elbow control in drilling is mandatory camp safety practice",
    ],
    "citations": [
        "https://en.wikipedia.org/wiki/Lethwei",
        "https://www.lethwei.com/",
    ],
    "sig_lens": ("Signature lens: the Signature method calls the elbow the "
                 "exclamation mark - the shortest, sharpest punctuation in "
                 "the fighter's signature. Where the punch signs in ink, "
                 "the elbow signs in steel. A Signature elbow is never "
                 "thrown in anger; it is placed with intent, at the exact "
                 "point where the opponent's sentence ends."),
},
{
    "key": "backfist",
    "name": "The Spinning Backfist",
    "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
    "description": ("The spinning backfist is Lethwei's answer to an opponent "
                    "who circles away: the fighter turns completely, "
                    "whipping the back of the fist around in a full-body "
                    "rotation. The technique belongs to the Let Thee family "
                    "and is listed among its classic weapons. The spin "
                    "generates enormous speed at the fist, but it has a "
                    "price - the fighter's back is exposed mid-turn, so the "
                    "backfist is a committed weapon thrown when the opening "
                    "is real. Done right, it lands with the back of the "
                    "knuckles across the side of the head or jaw; done "
                    "wrong, it spins the fighter into a counter."),
    "how_it_works": ("1. From the stance, step the lead foot across toward "
                     "the rear side to start the turn. 2. Pivot on the ball "
                     "of the lead foot and spin the body a full 360 "
                     "degrees, keeping the eyes on the target as long as "
                     "possible. 3. Extend the rear arm so the back of the "
                     "fist whips around at head height. 4. Land with the "
                     "back of the knuckles, wrist straight, at the moment "
                     "the hips complete the rotation. 5. Continue the spin "
                     "through to the fighting stance - never stop "
                     "half-turned. 6. Drill slowly first: the spin must be "
                     "balanced before it is fast."),
    "key_points": [
        "Full 360-degree body rotation whipping the back of the fist around",
        "Listed among the classic Let Thee weapons (lethwei.com)",
        "The answer to an opponent who circles away",
        "Lands with the back of the knuckles, wrist straight",
        "Committed weapon: the back is exposed mid-turn, so the opening must be real",
        "Spin through to stance - never stop half-turned",
    ],
    "requirements": [
        "Open space for the full spin",
        "Balance and pivot control from footwork drills",
        "Practice slowly before adding speed",
    ],
    "standards": [
        "Spinning backfists are part of the documented Let Thee arsenal (lethwei.com)",
        "Spin techniques require balance-first progression in traditional teaching",
        "Committed-spin discipline: only thrown on genuine openings",
    ],
    "citations": [
        "https://www.lethwei.com/",
        "https://en.wikipedia.org/wiki/Lethwei",
    ],
    "sig_lens": ("Signature lens: the spinning backfist is the Signature "
                 "fighter's flourish - the bold stroke that completes the "
                 "signature when the page turns. The Signature method "
                 "teaches it as a promise with a price: the full turn "
                 "exposes everything, so it is only signed when the "
                 "opening is certain. A flourish thrown on doubt is just "
                 "a scribble."),
},
{
    "key": "clinch",
    "name": "Entering the Clinch",
    "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
    "description": ("The clinch - the standing grapple - is where Lethwei "
                    "becomes its most brutal. Fighters tie up head-to-head "
                    "and shoulder-to-shoulder, each hunting inside position "
                    "for knees, elbows, and the headbutt, and each defending "
                    "the same. Entering the clinch well is a skill in "
                    "itself: the fighter slips or parries a punch, steps "
                    "deep with the lead foot, and secures the neck or the "
                    "biceps before the opponent can frame away. A good "
                    "entry lands the fighter chest-to-chest with head "
                    "position won; a bad entry walks face-first into an "
                    "uppercut or a Gowl Tite."),
    "how_it_works": ("1. Read the opponent's punch and slip or parry it to "
                     "one side. 2. Step deep with the lead foot, closing "
                     "the distance in one committed step. 3. Secure the "
                     "neck with one hand and the biceps or shoulder with "
                     "the other - never reach with both hands at once. "
                     "4. Win head position: forehead against the "
                     "opponent's temple or jaw, never nose-to-nose. "
                     "5. Keep the hips close and the base wide so the "
                     "opponent cannot easily off-balance the entry. "
                     "6. Drill entries from a jab slip, a parried cross, "
                     "and a caught kick, resetting after each tie-up."),
    "key_points": [
        "The clinch: the standing grapple where knees, elbows, and headbutts decide",
        "Enter off a slip, parry, or caught kick - never walk in straight",
        "One committed deep step closes the distance",
        "Secure neck and biceps; never reach with both hands at once",
        "Win head position: forehead to temple, never nose-to-nose",
        "A bad entry walks into an uppercut or a headbutt",
    ],
    "requirements": [
        "A drilling partner and open mat space",
        "Slip and parry skills from defense work",
        "Mouthguard - clinch entries involve accidental head contact",
    ],
    "standards": [
        "Clinching is central to Lethwei's stand-up grappling (Wikipedia, Lethwei)",
        "Entry mechanics are drilled before live clinch sparring in traditional camps",
        "Head position is the first principle taught in the tie-up",
    ],
    "citations": [
        "https://en.wikipedia.org/wiki/Lethwei",
        "https://fightersvault.com/blog/lethwei-explained-the-brutal-martial-art-of-burmese-boxing",
    ],
    "sig_lens": ("Signature lens: entering the clinch is the Signature "
                 "fighter's binding - two documents pressed together until "
                 "only one signature remains legible. The Signature method "
                 "teaches the entry as a contract negotiation: slip the "
                 "objection, step to the table, and take the pen - the "
                 "neck - before the opponent can frame you out of the "
                 "deal."),
},
{
    "key": "knee",
    "name": "The Straight Knee: Doo",
    "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
    "description": ("The knee - Doo - is the engine of the Lethwei clinch. "
                    "Thrown straight up into the opponent's torso or head, "
                    "it is driven by a violent hip thrust: the standing leg "
                    "extends, the hips shoot forward, and the knee spears "
                    "upward while the hands pull the opponent down into "
                    "it. The straight knee is the highest-percentage strike "
                    "in the tie-up because it travels the shortest path and "
                    "lands with the hardest point of the leg. Lethwei "
                    "fighters drill the knee until the hip thrust is "
                    "automatic - in the clinch, the hands pull and the hips "
                    "answer, and the Doo does the rest."),
    "how_it_works": ("1. From the clinch or close range, shift the weight "
                     "onto the standing leg. 2. Drive the hips forward and "
                     "up while lifting the knee straight toward the "
                     "target. 3. Pull down with the hands on the "
                     "opponent's neck, meeting the rising knee with the "
                     "descending head. 4. Strike with the point of the "
                     "knee, toes pointed down to expose the hard upper "
                     "shin and knee. 5. Snap the knee back down to the "
                     "ground - do not leave it hanging to be caught. "
                     "6. Drill: ten knees each side on the bag, then "
                     "partner-held belly pad rounds, hands pulling on "
                     "every rep."),
    "key_points": [
        "Doo: the knee, engine of the Lethwei clinch",
        "Driven by violent hip thrust - standing leg extends, hips shoot forward",
        "Hands pull the opponent down to meet the rising knee",
        "Strikes with the knee point, toes down to expose the hard surface",
        "Shortest path in the tie-up - the highest-percentage clinch strike",
        "Snap it back down; a hanging knee is caught and dumped",
    ],
    "requirements": [
        "Heavy bag or belly pad for impact",
        "A clinch entry already learned for the pulling hands",
        "Hip mobility from stance and kicking work",
    ],
    "standards": [
        "Doo is the documented Burmese term for the knee (Wikipedia, Lethwei)",
        "Straight, spear, jumping, and double flying knees are the recognized set (lethwei.com)",
        "Knee mechanics are drilled on bags before partner clinch work",
    ],
    "citations": [
        "https://en.wikipedia.org/wiki/Lethwei",
        "https://www.lethwei.com/",
    ],
    "sig_lens": ("Signature lens: the straight knee is the Signature "
                 "fighter's piston - the simplest machine in the nine-limb "
                 "workshop and the one that never breaks. Hands pull, hips "
                 "drive, knee signs. The Signature method drills it until "
                 "the motion is a reflex, because in the clinch there is "
                 "no time to think - only time to sign."),
},
{
    "key": "jumpknee",
    "name": "The Spear Knee and Jumping Knee: Doo",
    "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
    "description": ("Beyond the straight knee, the Doo family includes the "
                    "spear knee - thrown with a lunging step so the whole "
                    "body's momentum drives the point forward - and the "
                    "jumping knee, where both feet leave the ground and the "
                    "fighter's falling weight lands behind the strike. The "
                    "spear knee closes distance and impales; the jumping "
                    "knee is the exclamation point of the clinch break, "
                    "thrown as the tie-up separates. Both demand commitment: "
                    "the feet leave their base, so the strike must land or "
                    "the fighter lands badly. In traditional bouts, the "
                    "jumping knee off the clinch break has ended more than "
                    "a few fights by knockout."),
    "how_it_works": ("1. Spear knee: from range, lunge the lead foot deep "
                     "toward the opponent. 2. Drive the rear knee forward "
                     "and up as the body weight transfers onto the lunging "
                     "leg. 3. Land the knee point on the torso, hips fully "
                     "committed through the target. 4. Jumping knee: from "
                     "the clinch break, push off both feet at once. "
                     "5. Drive one knee up while the body is airborne, "
                     "pulling the opponent's head down with the hands. "
                     "6. Land back in stance on both feet, guard up - "
                     "never land on one foot off balance."),
    "key_points": [
        "Spear knee: lunging step drives whole-body momentum through the point",
        "Jumping knee: airborne strike, falling weight lands behind it",
        "The classic clinch-break exclamation point",
        "Both demand full commitment - the feet leave their base",
        "Land back in stance on both feet, guard up",
        "Knockout-grade weapons under traditional KO-or-draw rules",
    ],
    "requirements": [
        "The straight knee mechanics fully drilled first",
        "Soft landing surface for jumping-knee practice",
        "Strong clinch-break timing from clinch work",
    ],
    "standards": [
        "Spear, jumping, and double flying knees are documented Doo variants (lethwei.com)",
        "Airborne techniques require landing discipline in traditional teaching",
        "Commitment discipline: only thrown when the opening justifies the risk",
    ],
    "citations": [
        "https://www.lethwei.com/",
        "https://en.wikipedia.org/wiki/Lethwei",
    ],
    "sig_lens": ("Signature lens: the spear and jumping knees are the "
                 "Signature fighter's capital letters - thrown when the "
                 "sentence demands emphasis. The Signature method teaches "
                 "them as calculated risks: the whole body signs at once, "
                 "airborne and unrepeatable. Sign it big, sign it once, "
                 "and land ready to write the next line."),
},
{
    "key": "roundhouse",
    "name": "The Roundhouse Kick: Kan",
    "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
    "description": ("The roundhouse kick is the flagship of the Kan family "
                    "and one of the most recognizable weapons in all of "
                    "striking. Thrown in a horizontal arc, it lands with "
                    "the shin across the opponent's leg, body, or head, "
                    "driven by a full pivot of the supporting foot and a "
                    "violent rotation of the hips. Lethwei roundhouses are "
                    "thrown with bad intentions - full power, shin first, "
                    "with the arm swinging down for balance and the head "
                    "leaning away from the counter. A clean roundhouse to "
                    "the head is a knockout strike; to the body it folds "
                    "opponents; to the leg it is the argument-ender that "
                    "the low kick began."),
    "how_it_works": ("1. From the stance, pivot hard on the supporting "
                     "foot, turning the toes completely away from the "
                     "target. 2. Whip the hips over so the kicking hip "
                     "points at the target. 3. Swing the leg in a "
                     "horizontal arc, keeping it relaxed until impact. "
                     "4. Land with the middle of the shin - leg, body, or "
                     "head - while the same-side arm swings down and the "
                     "head leans back from the centerline. 5. Follow "
                     "through the target with the hips, then retract the "
                     "leg and reset. 6. Drill on the heavy bag in sets of "
                     "ten per side, checking the pivot on every rep."),
    "key_points": [
        "Flagship Kan weapon: horizontal arc, shin impact, full hip rotation",
        "Supporting foot pivots completely; kicking hip points at the target",
        "Same-side arm swings down, head leans away from the counter",
        "Head, body, or leg - each target changes the fight",
        "Follow through with the hips; retract and reset the stance",
        "Thrown with full power in Lethwei - the low kick's argument-ender",
    ],
    "requirements": [
        "Heavy bag for full-power practice",
        "Conditioned shins - build power gradually",
        "The low-kick pivot already learned",
    ],
    "standards": [
        "Roundhouse kicks are core to the Kan family (lethwei.com)",
        "Shin-first impact is the thaing kicking standard",
        "Full-power bag rounds are the traditional power test",
    ],
    "citations": [
        "https://www.lethwei.com/",
        "https://en.wikipedia.org/wiki/Lethwei",
    ],
    "sig_lens": ("Signature lens: the roundhouse is the Signature fighter's "
                 "broad stroke - the widest signature on the page, written "
                 "with the whole hip. The Signature method teaches it as "
                 "the weapon of decision: when the low kicks have made "
                 "their argument and the hands have written their lines, "
                 "the roundhouse signs the paragraph shut."),
},
{
    "key": "sweeps",
    "name": "Sweeps and Throws",
    "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
    "description": ("Lethwei permits sweeps and throws, and they are the "
                    "quiet assassins of the art. A sweep hooks the "
                    "supporting leg as the opponent steps or kicks, dumping "
                    "him to the canvas; a throw uses the clinch - hip, "
                    "shoulder, or leg reap - to send him down. Under "
                    "traditional rules, a knockdown that the fighter cannot "
                    "beat can end the fight, so every sweep is thrown with "
                    "knockout intent: sweep hard, follow with strikes, and "
                    "never admire the throw. The classic setups are the "
                    "caught kick dump, the clinch hip throw, and the "
                    "foot sweep against a stepping opponent."),
    "how_it_works": ("1. Caught-kick dump: catch the opponent's kick under "
                     "the arm, step deep past the supporting leg. 2. Reap "
                     "the supporting leg with the calf while pushing the "
                     "upper body away. 3. Foot sweep: as the opponent "
                     "steps, hook the ankle with the sole and pull while "
                     "pushing the shoulder. 4. Clinch hip throw: from the "
                     "tie-up, turn the hips in, load the opponent across "
                     "the hip, and rotate. 5. Follow every successful sweep "
                     "or throw immediately - the downed opponent is an "
                     "opening, not a pause. 6. Drill on mats with a "
                     "cooperative partner, increasing resistance gradually."),
    "key_points": [
        "Sweeps and throws are legal and are the quiet assassins of Lethwei",
        "Caught-kick dump: catch, step deep, reap the supporting leg",
        "Foot sweep: hook the stepping ankle while pushing the shoulder",
        "Clinch hip throw: load across the hip and rotate from the tie-up",
        "Thrown with knockout intent - follow every dump immediately",
        "Drilled on mats with gradually increasing resistance",
    ],
    "requirements": [
        "Mats or soft surface for throwing practice",
        "A cooperative drilling partner",
        "Clinch fundamentals already learned",
    ],
    "standards": [
        "Sweeps and throws are permitted techniques (Wikipedia, Lethwei)",
        "Unlimited grappling with sweeps and throws under modern rules (dojoandring.com)",
        "Throw follow-up is required under KO-oriented fight logic (lethwei.net)",
    ],
    "citations": [
        "https://en.wikipedia.org/wiki/Lethwei",
        "https://dojoandring.com/lethwei-the-art-of-nine-limbs-more-brutal-than-muay-thai/",
        "https://lethwei.net/knockout/",
    ],
    "sig_lens": ("Signature lens: sweeps and throws are the Signature "
                 "fighter's eraser - the opponent writes his attack on the "
                 "canvas, and the sweep wipes the sentence away. The "
                 "Signature method teaches them as punctuation of a "
                 "different kind: the period that ends the opponent's "
                 "paragraph and starts your own, written from above."),
},
{
    "key": "headbutt",
    "name": "The Headbutt: Gowl Tite",
    "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
    "description": ("The headbutt - Gowl Tite - is the ninth limb and the "
                    "weapon that separates Lethwei from every other striking "
                    "art. Thrown from the clinch or the close exchange, it "
                    "drives the hard crown of the forehead into the "
                    "opponent's face, temple, or jaw with the full weight "
                    "of the body behind it. It is legal, it is celebrated, "
                    "and it is devastating: headbutts open cuts, break "
                    "noses, and end fights. The technique is thrown with "
                    "the neck braced and the whole torso driving forward - "
                    "never a nod of the head, always a lunge of the body. "
                    "Defense is head position and distance; offense is the "
                    "clinch pull meeting the driving skull."),
    "how_it_works": ("1. From the clinch or close range, brace the neck "
                     "and tuck the chin. 2. Pull the opponent's head down "
                     "with the hands on the neck. 3. Drive the entire "
                     "torso forward and slightly down, leading with the "
                     "crown of the forehead. 4. Strike with the hard upper "
                     "forehead - never the nose or the top of the skull. "
                     "5. Follow through with the body weight; the power "
                     "comes from the lunge, not the nod. 6. Practice the "
                     "motion on the bag and in slow clinch drills only - "
                     "the headbutt is never practiced at full force on a "
                     "partner."),
    "key_points": [
        "Gowl Tite: the ninth limb, legal and celebrated in Lethwei",
        "Drives the crown of the forehead with the full body weight",
        "Thrown from the clinch or the close exchange",
        "Power from the torso lunge, never a nod of the head",
        "Opens cuts, breaks noses, ends fights - the knockout weapon",
        "Practiced on bags and in slow drills only, never full force on partners",
    ],
    "requirements": [
        "Clinch fundamentals and neck conditioning already built",
        "Heavy bag for the driving motion",
        "Strict control: slow drills only with partners",
    ],
    "standards": [
        "Gowl Tite is the documented Burmese term for the headbutt (Wikipedia, Lethwei)",
        "Headbutts are the defining legal weapon of the art of nine limbs (lethwei.com)",
        "Control-first practice is mandatory for dangerous techniques in camp teaching",
    ],
    "citations": [
        "https://en.wikipedia.org/wiki/Lethwei",
        "https://www.lethwei.com/",
    ],
    "sig_lens": ("Signature lens: the ninth limb is the Signature fighter's "
                 "seal in wax - the final stamp pressed into the document "
                 "of the fight. The Signature method teaches the Gowl Tite "
                 "as the covenant of last resort and first respect: the "
                 "head is the hardest promise the body can make, and a "
                 "Signature fighter presses it only where the fight has "
                 "already been decided everywhere else."),
},
{
    "key": "spinelbow",
    "name": "The Spinning Elbow: Tel Daung",
    "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
    "description": ("The spinning elbow takes the Tel Daung and adds a full "
                    "body rotation, whipping the elbow point around in a "
                    "360-degree arc. It is the close-range cousin of the "
                    "spinning backfist and one of the most spectacular "
                    "knockout weapons in Lethwei: the spin multiplies the "
                    "elbow's speed, and the point of the elbow concentrates "
                    "it all into inches of bone. Like all spins, it is a "
                    "committed weapon - the back turns, the guard opens, and "
                    "the strike must land or the fighter pays. It is thrown "
                    "when the opponent retreats along the ropes or when a "
                    "missed strike creates the turning angle."),
    "how_it_works": ("1. From close range, step the lead foot across to "
                     "start the rotation. 2. Spin the body a full 360 "
                     "degrees on the ball of the lead foot, folding the "
                     "rear arm tight so the elbow point leads. 3. Whip "
                     "the elbow horizontally at head height as the hips "
                     "complete the turn. 4. Strike with the elbow point, "
                     "the arm folded - the spin supplies the speed, the "
                     "fold supplies the weapon. 5. Continue through to "
                     "the fighting stance with the guard restored. "
                     "6. Drill the spin slowly on the bag until balance "
                     "is automatic, then add speed."),
    "key_points": [
        "Tel Daung with a full 360-degree spin - the spectacular knockout weapon",
        "Spin multiplies elbow speed; the point concentrates it into bone",
        "Close-range cousin of the spinning backfist",
        "Committed weapon: the back turns, so the opening must be genuine",
        "Thrown against retreating opponents or off a created turning angle",
        "Balance first, speed second - drill the spin slowly on the bag",
    ],
    "requirements": [
        "The spinning backfist and horizontal elbow already learned",
        "Open space and a heavy bag",
        "Balance control from footwork and spin drills",
    ],
    "standards": [
        "Spinning elbows are among the documented Tel Daung variants (lethwei.com)",
        "Spin techniques follow balance-first progression in traditional teaching",
        "Committed-spin discipline applies to all rotation techniques",
    ],
    "citations": [
        "https://www.lethwei.com/",
        "https://en.wikipedia.org/wiki/Lethwei",
    ],
    "sig_lens": ("Signature lens: the spinning elbow is the Signature "
                 "fighter's wax seal spun in the air - a full rotation that "
                 "ends in a single sharp point. The Signature method "
                 "teaches it as the most honest of the spins: everything "
                 "is risked, nothing is hidden, and the elbow signs the "
                 "verdict at the exact center of the turn."),
},
{
    "key": "axekick",
    "name": "The Axe Kick and Hook Kick: Kan",
    "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
    "description": ("The axe kick and the hook kick are the high Kan weapons "
                    "for opponents who shell up or lean away. The axe kick "
                    "rises straight up and crashes down like a blade, the "
                    "heel landing on the shoulder, collarbone, or guard; the "
                    "hook kick swings out and whips back across, the heel "
                    "landing on the side of the head or neck. Both demand "
                    "flexibility and timing - they are thrown over or "
                    "around the guard, not through it. In Lethwei, where "
                    "the guard is a tight shell built for elbows and "
                    "headbutts, the high kicks are the artillery that "
                    "punishes the shell from above and around."),
    "how_it_works": ("1. Axe kick: from stance, raise the leg straight up "
                     "in front of the body, knee nearly locked. 2. Drive "
                     "the heel down hard onto the target, hips slamming "
                     "down with it. 3. Hook kick: swing the leg out to "
                     "the side at head height. 4. Whip the heel back "
                     "across in a hooking motion, pivoting hard on the "
                     "support foot. 5. Land the heel on the side of the "
                     "target and retract immediately. 6. Drill both on "
                     "the bag at reduced height first - flexibility is "
                     "built over weeks, never forced in a day."),
    "key_points": [
        "Axe kick: rises straight, crashes down heel-first like a blade",
        "Hook kick: swings out and whips back across, heel to the side of the target",
        "Both go over or around the guard, never through it",
        "Demand flexibility and timing - built over weeks, never forced",
        "The artillery against the tight Lethwei shell",
        "Retract immediately; high kicks left hanging are caught",
    ],
    "requirements": [
        "Hip and hamstring flexibility work already underway",
        "Heavy bag for high-kick practice",
        "The roundhouse pivot already learned",
    ],
    "standards": [
        "Axe kicks and hook kicks are documented Kan weapons (lethwei.com)",
        "High kicks are thrown over or around the guard in thaing kicking doctrine",
        "Flexibility is built progressively in traditional camp practice",
    ],
    "citations": [
        "https://www.lethwei.com/",
        "https://en.wikipedia.org/wiki/Lethwei",
    ],
    "sig_lens": ("Signature lens: the axe and hook kicks are the Signature "
                 "fighter's tall letters - written above the line where "
                 "the opponent's guard cannot read them. The Signature "
                 "method teaches them as the answer to the shell: when "
                 "the wall will not open, sign over the top of it and "
                 "around the side of it, and let gravity finish the "
                 "sentence."),
},
{
    "key": "combos",
    "name": "Lethwei Combinations: the Nine-Limb Blitz",
    "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
    "description": ("Lethwei combinations chain the nine limbs into flowing "
                    "sequences: punches open the guard, elbows punish the "
                    "close range, knees and kicks follow the openings, and "
                    "the headbutt waits at the end of the clinch entries. "
                    "The classic blitz runs jab-cross-hook, then the rear "
                    "elbow, then the clinch knee - five weapons, one breath. "
                    "Good combinations obey three rules: every strike sets "
                    "up the next, the guard returns between strikes, and "
                    "the sequence ends in a safe position - in stance, in "
                    "the clinch with head position, or out of range. "
                    "Combinations are first built in banshay, then tested "
                    "on pads, then proven in sparring."),
    "how_it_works": ("1. Start with the two-strike core: jab-cross, "
                     "checking that both hands return to guard. 2. Add a "
                     "third weapon: jab-cross-hook, or jab-cross-low kick. "
                     "3. Add the close-range finish: after the hook, fold "
                     "the arm into the horizontal elbow. 4. Add the "
                     "clinch: after the elbow, step in and secure the "
                     "neck. 5. Finish with the knee or break out to "
                     "range - every combination ends safe. 6. Drill the "
                     "five-weapon blitz on pads: jab, cross, hook, "
                     "elbow, knee - one breath, guard home between every "
                     "strike."),
    "key_points": [
        "Chain the nine limbs: punches open, elbows punish, knees and kicks follow",
        "The classic blitz: jab, cross, hook, rear elbow, clinch knee - one breath",
        "Every strike sets up the next strike",
        "Guard returns home between strikes - no hanging hands",
        "Every combination ends safe: in stance, in the clinch, or out of range",
        "Built in banshay, tested on pads, proven in sparring",
    ],
    "requirements": [
        "All individual strikes already learned",
        "Focus mitts and a pad holder for combination rounds",
        "Banshay rounds to build the flow",
    ],
    "standards": [
        "Combination flow is the purpose of banshay practice (mmafullcontact.com)",
        "Guard discipline between strikes is enforced in all camp drilling",
        "Safe endings are required before combinations are sparred",
    ],
    "citations": [
        "https://www.mmafullcontact.com/introduction-to-lethwei/",
        "https://en.wikipedia.org/wiki/Lethwei",
    ],
    "sig_lens": ("Signature lens: combinations are the Signature fighter's "
                 "cursive - the separate letters of the nine limbs joined "
                 "into one flowing signature. The Signature method teaches "
                 "the blitz as a single word written at speed: five "
                 "weapons, one breath, no lifting the pen. And like any "
                 "signature, it must be legible at full speed or it is "
                 "just a scribble."),
},
{
    "key": "clinchdef",
    "name": "Defending the Clinch: Pummeling",
    "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
    "description": ("Pummeling is the wrestling battle for inside position "
                    "in the clinch: both fighters swim their arms for the "
                    "neck and the biceps, each trying to secure the dominant "
                    "tie while denying it. The pummeler keeps the elbows "
                    "tight, the head in good position, and the hips close, "
                    "swimming one arm inside at a time - never both at "
                    "once, which opens the body to knees. Good pummeling "
                    "also defends the headbutt: forehead pressure on the "
                    "opponent's temple keeps his skull away from the face, "
                    "and constant motion denies him the set position the "
                    "Gowl Tite needs. In Lethwei, losing the pummeling "
                    "battle means eating knees, elbows, and the ninth limb."),
    "how_it_works": ("1. From the tie-up, keep the elbows tight to the "
                     "body and the head pressed to the opponent's temple. "
                     "2. Swim one arm inside: circle the hand over the "
                     "opponent's arm and under, securing the neck or "
                     "biceps. 3. While swimming, the other hand maintains "
                     "its grip - one arm moves, one arm holds. 4. Once "
                     "inside, pull the opponent's posture down and keep "
                     "the hips close. 5. If the opponent gets inside, "
                     "swim again immediately - pummeling never stops. "
                     "6. Drill continuous pummeling rounds: two minutes "
                     "of nonstop inside-position wrestling, no strikes."),
    "key_points": [
        "Pummeling: the swim for inside neck-and-biceps position",
        "One arm swims at a time; the other holds - never both at once",
        "Elbows tight, head on the temple, hips close",
        "Forehead pressure on the temple defends the headbutt",
        "Constant motion denies the set position the Gowl Tite needs",
        "Losing the pummeling battle means eating knees, elbows, and the ninth limb",
    ],
    "requirements": [
        "A drilling partner for tie-up rounds",
        "Clinch entry skills already learned",
        "Mouthguard for close contact",
    ],
    "standards": [
        "Inside position is the first principle of the clinch (Wikipedia, Lethwei)",
        "Pummeling rounds are standard in thaing clinch preparation",
        "Head-position defense against the headbutt is taught before live clinch sparring",
    ],
    "citations": [
        "https://en.wikipedia.org/wiki/Lethwei",
        "https://fightersvault.com/blog/lethwei-explained-the-brutal-martial-art-of-burmese-boxing",
    ],
    "sig_lens": ("Signature lens: pummeling is the Signature fighter's "
                 "editing - two authors wrestling over the same sentence "
                 "in the clinch. The Signature method teaches the swim as "
                 "revision: every inside arm is a correction, every denied "
                 "grip is a rejected draft. The fighter who holds the pen "
                 "- the neck - gets to write the ending."),
},
{
    "key": "counters",
    "name": "Counter-Striking in Lethwei",
    "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
    "description": ("Counter-striking is the art of answering: the opponent "
                    "attacks, the fighter defends by inches, and the answer "
                    "lands before the opponent's guard returns. In Lethwei "
                    "the classic counters are the slip-and-cross against "
                    "the jab, the check-and-low-kick against the roundhouse, "
                    "the parry-and-elbow against the hook, and the "
                    "sprawl-and-knee against the clinch entry. Counters work "
                    "because commitment creates openings - every strike the "
                    "opponent throws is a door he opens himself. The "
                    "counter-fighter reads the shoulders and hips, moves "
                    "the minimum distance to survive, and signs the reply "
                    "while the door is still open."),
    "how_it_works": ("1. Watch the opponent's shoulders and hips - strikes "
                     "are telegraphed there, not in the hands. 2. Defend "
                     "by the minimum: slip the jab by inches, check the "
                     "kick with the shin, parry the hook with the glove "
                     "of the hand. 3. Fire the answer while the "
                     "opponent's weapon is still extended: cross over the "
                     "jab, low kick the planted leg, elbow over the hook. "
                     "4. Return to guard or take the angle - the counter "
                     "ends safe. 5. Drill one counter at a time: partner "
                     "throws the same attack for the full round while the "
                     "fighter answers it. 6. Combine counters into "
                     "sequences only after each single counter is "
                     "automatic."),
    "key_points": [
        "Answer the attack: defend by inches, strike before the guard returns",
        "Classic counters: slip-cross, check-low kick, parry-elbow, sprawl-knee",
        "Read the shoulders and hips - strikes telegraph there",
        "Commitment creates openings: every thrown strike is a door opened",
        "Defend by the minimum distance, answer at maximum speed",
        "Drill one counter per round until it is automatic",
    ],
    "requirements": [
        "Solid defense fundamentals: slips, parries, checks",
        "A partner to feed single attacks for counter rounds",
        "The individual strikes already sharp",
    ],
    "standards": [
        "Counter timing is a core skill under knockout-oriented rules (lethwei.net)",
        "Single-attack counter rounds are the traditional teaching progression",
        "Reading the shoulders and hips is standard striking pedagogy",
    ],
    "citations": [
        "https://lethwei.net/knockout/",
        "https://en.wikipedia.org/wiki/Lethwei",
    ],
    "sig_lens": ("Signature lens: the counter is the Signature fighter's "
                 "marginal note - written in the white space the opponent "
                 "leaves open. The Signature method teaches counters as "
                 "the art of the minimum: move the least, read the most, "
                 "and sign the reply in the margin while the opponent's "
                 "own sentence is still unfinished."),
},
{
    "key": "ringcut",
    "name": "Cutting Off the Ring",
    "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
    "description": ("Cutting off the ring is how a Lethwei fighter traps an "
                    "opponent who wants to run: instead of chasing, the "
                    "fighter steps to cut the angle, shrinking the "
                    "available space until the opponent is cornered "
                    "against the ropes. The method is geometric - move to "
                    "where the opponent is going, not where he is, stepping "
                    "on the diagonal that closes two escape routes at "
                    "once. Lethwei rewards the cutter: with knockout the "
                    "only certain victory, the fighter who owns the center "
                    "and denies the exits forces the exchanges that end "
                    "fights. Chasing follows; cutting intercepts."),
    "how_it_works": ("1. Take the center of the ring and hold it - the "
                     "center is the cutter's base. 2. When the opponent "
                     "circles left, step diagonally to the fighter's "
                     "right, closing the angle rather than following. "
                     "3. Keep the lead foot pointed at the opponent's "
                     "escape path, not at the opponent. 4. Feint with "
                     "the jab to freeze the movement, then step to the "
                     "cut angle. 5. Once the opponent's back nears the "
                     "ropes, press with the blitz - trapped opponents "
                     "shell, and shells are for elbows. 6. Drill with a "
                     "partner circling the ring: cut, do not chase, for "
                     "three-minute rounds."),
    "key_points": [
        "Trap the runner: step to cut the angle, never chase",
        "Move to where the opponent is going, not where he is",
        "One diagonal step closes two escape routes at once",
        "Hold the center - the cutter's base is the middle of the ring",
        "Jab-feint to freeze movement, then step to the cut angle",
        "Trapped opponents shell up, and shells are for elbows",
    ],
    "requirements": [
        "A ring or marked area and a circling partner",
        "Footwork: circling and pivoting already comfortable",
        "The combination blitz ready for the trapped opponent",
    ],
    "standards": [
        "Ring control is decisive under KO-oriented rules (lethwei.net)",
        "Angle-cutting is standard instruction in striking camps",
        "Center control precedes the finishing exchanges in traditional fight craft",
    ],
    "citations": [
        "https://lethwei.net/knockout/",
        "https://en.wikipedia.org/wiki/Lethwei",
    ],
    "sig_lens": ("Signature lens: cutting the ring is the Signature "
                 "fighter's framing - drawing the border smaller until the "
                 "opponent's signature has nowhere left to run. The "
                 "Signature method teaches geometry over pursuit: chase "
                 "the man and you follow his story; cut the angle and you "
                 "write the ending yourself."),
},
{
    "key": "naban",
    "name": "Naban: Controlled Sparring",
    "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
    "description": ("Naban is the traditional controlled sparring of the "
                    "thaing arts: partners practice techniques at reduced "
                    "power with full control, emphasizing precision, "
                    "timing, and technique over damage. It sits between "
                    "banshay shadowboxing and full sparring - the "
                    "opponent is real, but the contract is control. "
                    "Fighters agree the targets and the power level, then "
                    "exchange real techniques: entries, counters, clinch "
                    "work, and the dangerous weapons practiced with care. "
                    "Naban is where Lethwei's brutal arsenal becomes "
                    "trainable: the headbutt, the elbows, and the throws "
                    "are all rehearsed here safely before they are ever "
                    "used in earnest."),
    "how_it_works": ("1. Agree the rules with the partner: targets, power "
                     "level, and which weapons are live. 2. Begin at "
                     "half speed, exchanging the agreed techniques with "
                     "full form but controlled contact. 3. Practice the "
                     "dangerous weapons - elbows, headbutt entries, "
                     "throws - at touch or near-touch contact only. "
                     "4. Stop and reset after every clean technique; "
                     "naban is study, not a fight. 5. Increase speed "
                     "gradually across rounds, never increasing power. "
                     "6. End with thanks: the partner who lets you "
                     "practice the dangerous arts safely is a teacher."),
    "key_points": [
        "Naban: traditional controlled sparring - real techniques, controlled power",
        "Between banshay and full sparring: the opponent is real, the contract is control",
        "Targets, power level, and live weapons agreed before every round",
        "Dangerous weapons practiced at touch or near-touch contact",
        "Stop and reset after clean techniques - naban is study, not a fight",
        "Speed may rise across rounds; power never does",
    ],
    "requirements": [
        "A trusted partner who honors the control contract",
        "Protective gear appropriate to the agreed weapons",
        "The techniques already learned in banshay and pad work",
    ],
    "standards": [
        "Naban is the documented controlled-sparring method of Lethwei (mmafullcontact.com)",
        "Control-first practice of dangerous techniques is traditional camp doctrine",
        "Agreed rules before contact are required in thaing training culture",
    ],
    "citations": [
        "https://www.mmafullcontact.com/introduction-to-lethwei/",
        "https://en.wikipedia.org/wiki/Lethwei",
    ],
    "sig_lens": ("Signature lens: naban is the Signature fighter's drafting "
                 "table - where the dangerous sentences are written in "
                 "pencil before they are ever inked. The Signature method "
                 "treats controlled sparring as the highest discipline: "
                 "anyone can sign in anger, but it takes mastery to write "
                 "the headbutt at half speed and mean every letter of it."),
},

# ------------------------------------------------------------------ ADVANCED
{
    "key": "clinchgame",
    "name": "The Clinch Game: Knees, Elbows and the Ninth Limb",
    "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
    "description": ("The advanced clinch game is Lethwei's deepest water: "
                    "from the tie-up, the master chains knees, elbows, and "
                    "the headbutt into continuous offense while denying all "
                    "three. The pattern is pull-and-strike - yank the neck "
                    "down into the rising knee, shove the head up into the "
                    "upward elbow, turn the temple into the driving "
                    "forehead - and every strike is thrown from the position "
                    "the pummeling won. Defense is equally layered: hip "
                    "position kills the knees, forearm frames kill the "
                    "elbows, and constant head movement denies the Gowl "
                    "Tite its set. The fighter who owns the clinch game "
                    "owns the inside of the fight, and the inside of a "
                    "Lethwei fight is where knockouts are manufactured."),
    "how_it_works": ("1. Secure the dominant tie: both hands controlling "
                     "the neck, head on the opponent's temple. 2. Begin "
                     "the chain: pull the neck down sharply into a rising "
                     "straight knee. 3. As the opponent's posture breaks "
                     "upward, shove the head up and spear the upward "
                     "elbow under the chin. 4. When the opponent turns "
                     "his head to escape the elbow, drive the forehead "
                     "into the exposed temple - the ninth limb completes "
                     "the chain. 5. Defensively: keep the hips back from "
                     "the knees, the forearms framing the elbows, and the "
                     "head never still. 6. Drill the chain slowly on a "
                     "cooperative partner, then in naban, then - and only "
                     "then - in live clinch rounds."),
    "key_points": [
        "The deepest water: chaining knees, elbows, and headbutt from the tie-up",
        "Pull-and-strike: yank the neck down into the knee, shove the head up into the elbow",
        "The ninth limb completes the chain when the head turns from the elbow",
        "Every strike thrown from the position the pummeling won",
        "Layered defense: hips back from knees, forearms frame elbows, head never still",
        "The inside of a Lethwei fight is where knockouts are manufactured",
    ],
    "requirements": [
        "Mastery of the clinch, pummeling, knees, elbows, and headbutt entries",
        "A skilled partner for slow chain drilling",
        "Naban control before any live clinch-game rounds",
    ],
    "standards": [
        "Chained clinch offense is the documented heart of the Lethwei tie-up (Wikipedia, Lethwei)",
        "The knee is the engine of the clinch game (lethwei.com)",
        "Progressive resistance - slow, naban, live - is traditional advanced teaching",
    ],
    "citations": [
        "https://en.wikipedia.org/wiki/Lethwei",
        "https://www.lethwei.com/",
    ],
    "sig_lens": ("Signature lens: the clinch game is the Signature "
                 "fighter's illuminated manuscript - every letter "
                 "ornamented, every margin filled, the whole page "
                 "glowing. The Signature method teaches the chain as the "
                 "master's signature: knee, elbow, ninth limb, each "
                 "flowing into the next without lifting the pen. To own "
                 "the clinch game is to write the fight's most beautiful "
                 "and most terrible page."),
},
{
    "key": "rules",
    "name": "Traditional Bout Rules: Knockout or Draw",
    "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
    "description": ("Traditional Lethwei rules are the simplest and most "
                    "demanding in combat sports: there are no judges and no "
                    "points - the only way to win is to knock the opponent "
                    "out, force a technical knockout, or win by doctor "
                    "stoppage, and if neither fighter finishes, the bout is "
                    "a draw. Each corner is allowed one two-minute timeout "
                    "per fight to revive a knocked-down fighter, which has "
                    "produced legendary comebacks. Bouts run five "
                    "three-minute rounds with two-minute rests; fighters "
                    "wear only shorts, a groin guard, and a mouthguard, "
                    "with hands wrapped in tape and gauze and no gloves. "
                    "Everything about the ruleset pushes toward the "
                    "finish - which is why Lethwei fighters fight the way "
                    "they do."),
    "how_it_works": ("1. Understand the win condition: knockout, technical "
                     "knockout, or doctor stoppage - nothing else wins. "
                     "2. Plan for the draw: if the finish does not come, "
                     "both fighters share the result, so every round must "
                     "hunt the knockout. 3. Know the timeout: each corner "
                     "may call one two-minute injury timeout per fight to "
                     "revive their fighter. 4. Respect the attire check: "
                     "wraps inspected by officials, only shorts, groin "
                     "guard, and mouthguard permitted. 5. Fight five "
                     "three-minute rounds with two-minute rests, pacing "
                     "the engine for the full distance. 6. Study the "
                     "modern variant: some promotions now use judges, but "
                     "traditional bouts remain KO-or-draw."),
    "key_points": [
        "No judges, no points: knockout, TKO, or doctor stoppage wins - else a draw",
        "One two-minute injury timeout per corner per fight to revive a fighter",
        "Five three-minute rounds with two-minute rests",
        "Bareknuckle: tape-and-gauze wraps inspected by officials, no gloves",
        "Attire: shorts, groin guard, and mouthguard only",
        "The ruleset pushes every round toward the finish",
    ],
    "requirements": [
        "A sanctioned bout or a qualified coach explaining the ruleset",
        "Understanding of the timeout and how corners use it",
        "Respect for the officials who enforce wraps and attire",
    ],
    "standards": [
        "Traditional rules: KO-only victory, draw otherwise, one two-minute timeout per corner (Wikipedia, Lethwei)",
        "Five three-minute rounds with two-minute rests (dojoandring.com)",
        "Wraps of tape and gauze inspected by officials; gloves forbidden (fightersvault.com)",
        "1952 Kyar Ba Nyein modernization formalized the rules; World Lethwei Championship (2016) brought the modern era (dojoandring.com)",
    ],
    "citations": [
        "https://en.wikipedia.org/wiki/Lethwei",
        "https://dojoandring.com/lethwei-the-art-of-nine-limbs-more-brutal-than-muay-thai/",
        "https://fightersvault.com/blog/lethwei-explained-the-brutal-martial-art-of-burmese-boxing",
        "https://lethwei.net/knockout/",
    ],
    "sig_lens": ("Signature lens: the traditional rules are the Signature "
                 "fighter's terms of service - written in the old hand, "
                 "unchangeable, and perfectly clear. Knockout or draw: the "
                 "document either ends with a signature or it ends "
                 "unsigned. The Signature method embraces the harshness - "
                 "no judges means no politics, no points means no hiding, "
                 "and the timeout means a warrior's heart gets exactly one "
                 "more chance to sign."),
},
{
    "key": "headbuttsetup",
    "name": "Setting Up the Gowl Tite",
    "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
    "description": ("The headbutt rarely lands raw - it is set up. The "
                    "advanced fighter manufactures the Gowl Tite with "
                    "patterns: the knee that forces the head down into the "
                    "forehead, the elbow that turns the head to expose the "
                    "temple, the clinch pull that drags the face into "
                    "range, and the feinted punch that lifts the guard and "
                    "drops the chin into the strike zone. Each setup obeys "
                    "the same logic - move the opponent's head where the "
                    "forehead is already waiting, rather than chasing the "
                    "head with the forehead. The setups are drilled slowly "
                    "and finished on the bag, because the ninth limb is "
                    "never practiced at full force on a partner."),
    "how_it_works": ("1. Setup one - the knee drop: throw the straight "
                     "knee so the opponent's hands drop to block it, then "
                     "drive the forehead into the descending face. "
                     "2. Setup two - the elbow turn: throw the horizontal "
                     "elbow so the opponent turns his head away, exposing "
                     "the temple to the driving forehead. 3. Setup three "
                     "- the clinch drag: from the tie-up, yank the neck "
                     "down hard and meet the falling head with the crown. "
                     "4. Setup four - the feint: feint the cross high so "
                     "the guard lifts, then lunge the forehead under the "
                     "rising hands. 5. Drill each setup slowly with a "
                     "partner, stopping at touch distance. 6. Finish the "
                     "full-power reps on the heavy bag only."),
    "key_points": [
        "The headbutt is manufactured, not thrown raw - four classic setups",
        "Knee drop: hands fall to block the knee, forehead meets the face",
        "Elbow turn: the head turns from the elbow, exposing the temple",
        "Clinch drag: yank the neck down into the waiting crown",
        "Feint: lift the guard with a fake cross, lunge under it",
        "Drilled slowly with partners, finished at full power on the bag only",
    ],
    "requirements": [
        "The headbutt mechanics and clinch game already learned",
        "A cooperative partner for slow setup drilling",
        "A heavy bag for full-power finishing reps",
    ],
    "standards": [
        "Headbutt setups are the advanced application of Gowl Tite (Wikipedia, Lethwei)",
        "Setups move the target to the weapon, not the weapon to the target - standard striking doctrine",
        "Full-power dangerous techniques are finished on bags, never on partners",
    ],
    "citations": [
        "https://en.wikipedia.org/wiki/Lethwei",
        "https://www.lethwei.com/",
    ],
    "sig_lens": ("Signature lens: the setup is the Signature fighter's "
                 "sleight of hand - the audience watches the knee while "
                 "the seal is pressed. The Signature method teaches that "
                 "the ninth limb is too honest to chase: instead, write "
                 "the opponent's head a letter it cannot refuse - a knee, "
                 "an elbow, a pull - and let it walk itself into the "
                 "forehead's waiting signature."),
},
{
    "key": "rhythm",
    "name": "Reading Rhythm: Feints and Timing",
    "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
    "description": ("Every fighter has a rhythm - the tempo of his steps, "
                    "the cadence of his combinations, the beat on which he "
                    "breathes and resets. The advanced Lethwei fighter "
                    "reads that rhythm in the first minute and then breaks "
                    "it: feinting on the opponent's beat to draw the "
                    "reaction, then striking on the half-beat while the "
                    "opponent is still answering the fake. Feints are "
                    "thrown with the whole body - a shoulder twitch for "
                    "the jab, a hip shift for the kick, a level change for "
                    "the takedown that never comes - because only "
                    "believable lies draw real reactions. Timing, the old "
                    "coaches say, beats speed; the fighter who owns the "
                    "tempo owns the fight."),
    "how_it_works": ("1. Spend the first minute reading: count the "
                     "opponent's step cadence and combination rhythm. "
                     "2. Match the rhythm briefly so the opponent "
                     "settles into it. 3. Break it with a feint on his "
                     "beat: twitch the lead shoulder as if jabbing, and "
                     "watch the guard react. 4. Strike on the half-beat "
                     "- while the opponent answers the feint, the real "
                     "weapon is already traveling. 5. Vary the feints: "
                     "shoulder for the jab, hip for the kick, level "
                     "change for the clinch entry. 6. Drill feint-and-hit "
                     "rounds: every real strike must be preceded by a "
                     "believable fake."),
    "key_points": [
        "Read the opponent's rhythm in the first minute: steps, combinations, breathing",
        "Feint on his beat to draw the reaction, strike on the half-beat",
        "Feints use the whole body: shoulder, hip, level change",
        "Only believable lies draw real reactions",
        "Timing beats speed - the fighter who owns the tempo owns the fight",
        "Drill: every real strike preceded by a believable fake",
    ],
    "requirements": [
        "Live sparring experience to read real rhythms",
        "All basic strikes sharp enough to make feints believable",
        "A coach or partner to call out telegraphed vs. honest feints",
    ],
    "standards": [
        "Feint-and-timing work is advanced instruction in striking camps",
        "Rhythm reading is required for championship-level Lethwei",
        "Believable-feint discipline is taught before feints are used in sparring",
    ],
    "citations": [
        "https://lethwei.net/knockout/",
        "https://en.wikipedia.org/wiki/Lethwei",
    ],
    "sig_lens": ("Signature lens: rhythm is the Signature fighter's "
                 "metronome, and the feint is how he steals the "
                 "opponent's. The Signature method teaches timing as "
                 "authorship: first you read the opponent's tempo like a "
                 "manuscript, then you write your strike in the margin "
                 "between his beats. The half-beat is where Signature "
                 "fighters sign their names."),
},
{
    "key": "hardening",
    "name": "Knuckle and Shin Hardening",
    "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
    "description": ("Knuckle and shin hardening is the long, patient work "
                    "of adapting bone and skin to bareknuckle impact. The "
                    "method is progressive overload applied to the "
                    "striking surfaces: weeks of gradually increasing bag "
                    "rounds, starting light and adding volume, let the "
                    "knuckles calcify their callus and the shins deaden "
                    "their nerves without injury. Traditional camps add "
                    "supplementary work - knuckle push-ups, shin rolling, "
                    "and controlled impact drills - but the bag remains "
                    "the king, because nothing conditions a weapon like "
                    "the weapon's real work. The rule is iron: adapt, "
                    "never abuse. Pain that fades by morning is training; "
                    "pain that lingers is damage, and damage is the "
                    "opposite of hardening."),
    "how_it_works": ("1. Start with light bag rounds: three rounds, "
                     "controlled power, perfect form. 2. Add one round "
                     "per week and a small power increase, never both at "
                     "once. 3. Add knuckle push-ups: two sets to start, "
                     "building to five, on a firm surface. 4. Add shin "
                     "conditioning: controlled bag contact, increasing "
                     "reps weekly. 5. Monitor every morning: soreness "
                     "that fades is adaptation; pain that lingers means "
                     "back off for three days. 6. After eight to twelve "
                     "weeks, test on the heavy bag at full power - the "
                     "hands and shins should feel like tools, not "
                     "wounds."),
    "key_points": [
        "Progressive overload for bone and skin: gradual bag rounds over weeks",
        "Add one round per week or a small power increase - never both at once",
        "Knuckle push-ups and controlled shin contact supplement the bag",
        "The bag is king: nothing conditions a weapon like its real work",
        "Morning check: fading soreness is adaptation, lingering pain is damage",
        "Iron rule: adapt, never abuse",
    ],
    "requirements": [
        "Heavy bag access for progressive rounds",
        "A written weekly plan tracking rounds and power",
        "Honest pain monitoring - the discipline to back off",
    ],
    "standards": [
        "Progressive conditioning is standard in Lethwei camps (mmafullcontact.com)",
        "The adapt-never-abuse principle is universal combat-conditioning doctrine",
        "Eight-to-twelve-week hardening blocks precede hard sparring in traditional preparation",
    ],
    "citations": [
        "https://www.mmafullcontact.com/introduction-to-lethwei/",
        "https://en.wikipedia.org/wiki/Lethwei",
    ],
    "sig_lens": ("Signature lens: hardening is the Signature method's "
                 "tempering - the slow forging that turns the fighter's "
                 "instruments from soft iron into steel. A Signature "
                 "fighter does not rush the forge: each week's small "
                 "addition is a layer folded into the blade. The "
                 "signature pressed by hardened knuckles is permanent "
                 "because the pen was made worthy first."),
},
{
    "key": "fightplan",
    "name": "The Five-Round Fight Plan",
    "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
    "description": ("A Lethwei bout runs five three-minute rounds with "
                    "two-minute rests, and the fighter who spends his "
                    "engine in round one rarely sees round five. The "
                    "five-round fight plan allocates effort like a "
                    "budget: round one reads and probes at controlled "
                    "pace; rounds two and three press with the blitz and "
                    "the clinch, spending the bulk of the energy; round "
                    "four is the championship round where the "
                    "knockout hunt peaks; round five spends whatever "
                    "remains, because under KO-or-draw rules there is no "
                    "tomorrow to save it for. Between rounds, the corner "
                    "manages the two-minute rests and holds the single "
                    "injury timeout like a loaded weapon - it is played "
                    "only when it can change the fight."),
    "how_it_works": ("1. Round one: probe at 70 percent - read the "
                     "rhythm, test the guard, spend nothing precious. "
                     "2. Rounds two and three: press at 90 percent - "
                     "the blitz, the clinch, the low kicks accumulate. "
                     "3. Round four: the hunt peaks - every exchange "
                     "commits to the knockout. 4. Round five: spend it "
                     "all - under KO-or-draw there is no tomorrow. "
                     "5. Between rounds: breathe on a count, take "
                     "corner instruction in one sentence, and stand "
                     "before the ten-second clap. 6. Hold the injury "
                     "timeout in reserve: one two-minute revival per "
                     "fight, played only when it can change the "
                     "outcome."),
    "key_points": [
        "Five three-minute rounds, two-minute rests - budget the engine like money",
        "Round one at 70 percent: read, probe, spend nothing precious",
        "Rounds two and three at 90 percent: the blitz and clinch accumulate damage",
        "Round four: the knockout hunt peaks",
        "Round five: spend it all - KO-or-draw leaves no tomorrow",
        "The one injury timeout is held in reserve, played only to change the outcome",
    ],
    "requirements": [
        "The five-round engine already built in conditioning",
        "A corner team that understands the timeout rule",
        "Sparring experience across full five-round simulations",
    ],
    "standards": [
        "Five three-minute rounds with two-minute rests is the standard bout format (dojoandring.com)",
        "One two-minute injury timeout per corner per fight (Wikipedia, Lethwei)",
        "Pacing under KO-or-draw rules is required championship craft (lethwei.net)",
    ],
    "citations": [
        "https://dojoandring.com/lethwei-the-art-of-nine-limbs-more-brutal-than-muay-thai/",
        "https://en.wikipedia.org/wiki/Lethwei",
        "https://lethwei.net/knockout/",
    ],
    "sig_lens": ("Signature lens: the fight plan is the Signature "
                 "fighter's budget - five chapters, one story, and the "
                 "ink must last to the final page. The Signature method "
                 "teaches pacing as narrative discipline: probe in the "
                 "opening, build in the middle, and sign the ending in "
                 "the championship rounds. A Signature fighter never "
                 "runs out of ink before the last line."),
},
{
    "key": "ceremony",
    "name": "From Lethwei Yay to Knockout: the Full Traditional Bout",
    "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
    "description": ("The full traditional bout is the complete Lethwei "
                    "experience, from ritual to result. It begins with "
                    "the Lethwei Yay and the Lekkha Moun warrior dance - "
                    "respect paid before violence. Then the wraps are "
                    "inspected, the fighters take their stances, and five "
                    "three-minute rounds unfold: the probing first, the "
                    "accumulating middle, the hunting championship rounds, "
                    "every exchange shaped by the knowledge that only a "
                    "knockout wins. If a fighter falls, his corner may "
                    "spend its single two-minute timeout to revive him - "
                    "the legendary comebacks of Lethwei are born in those "
                    "two minutes. And if five rounds pass with both "
                    "warriors standing, the bout is a draw, and both "
                    "leave with honor. This is the art of nine limbs in "
                    "its complete form: ritual, craft, courage, and the "
                    "harshest rule in fighting."),
    "how_it_works": ("1. Perform the Lethwei Yay and Lekkha Moun: honor "
                     "the teachers, the ancestors, and the art. 2. "
                     "Submit to the wrap and attire inspection - tape "
                     "and gauze, shorts, groin guard, mouthguard. "
                     "3. Take the stance and fight round one as the "
                     "reading round. 4. Execute the fight plan through "
                     "rounds two to five, hunting the knockout every "
                     "round. 5. If knocked down, the corner decides: "
                     "spend the one two-minute timeout to revive, or "
                     "concede with honor. 6. At the final bell with "
                     "both standing, accept the draw as the tradition "
                     "demands - the bout is complete, the ritual "
                     "closed."),
    "key_points": [
        "The complete bout: ritual, inspection, five rounds, revival, result",
        "Opens with the Lethwei Yay and Lekkha Moun - respect before violence",
        "Wraps and attire inspected by officials before the first bell",
        "Five three-minute rounds, every one hunting the knockout",
        "The single two-minute timeout: the corner's one chance at a legendary comeback",
        "Both standing at the end means a draw - honor for both warriors",
    ],
    "requirements": [
        "Every technique on the ladder already learned and drilled",
        "A sanctioned traditional bout and a qualified corner",
        "Full understanding of the KO-or-draw rules and the timeout",
    ],
    "standards": [
        "The traditional bout format: ritual, five rounds, KO-or-draw, one timeout (Wikipedia, Lethwei)",
        "Lethwei Yay and Lekkha Moun open the traditional bout",
        "The draw is the honorable result when no knockout comes (lethwei.net)",
    ],
    "citations": [
        "https://en.wikipedia.org/wiki/Lethwei",
        "https://lethwei.net/knockout/",
        "https://thesportsutopia.com/lethwei/",
    ],
    "sig_lens": ("Signature lens: the full traditional bout is the "
                 "Signature fighter's completed document - title page, "
                 "five chapters, and an ending written in the old hand. "
                 "The Signature method sees the whole ladder in this one "
                 "night: the stance that made the first promise, the nine "
                 "limbs that kept it, and the knockout - or the honored "
                 "draw - that signs the final line. From Yay to result, "
                 "the Signature is complete."),
},
]

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
ranks = [e["ladder_rank"] for e in ENTRIES]
assert ranks == sorted(ranks), "entries not in ladder order"
assert all(1 <= r <= 10 for r in ranks), "ladder_rank out of range"
assert {e["key"] for e in ENTRIES} == {e["key"] for e in ENTRIES} and len({e["key"] for e in ENTRIES}) == 34
