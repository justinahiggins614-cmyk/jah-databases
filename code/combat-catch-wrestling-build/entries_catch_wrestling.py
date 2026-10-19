#!/usr/bin/env python3
"""Entries for the Catch Wrestling Combat databases (combat batch 3).

Catch-as-catch-can wrestling: hooks, rides, submissions, and pinning
combinations, taught along the teaching ladder from foundations through
compounded to advanced. Public records are real, fact-checked catch
wrestling knowledge; Signature records reframe the same ladder through
his original Signature Combat Method lens, clearly labeled.

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written
in ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBCW- (public) and JAH-CBCWS- (signature), verified free
in the manifest (2442 databases, zero exact/substring hits) and in every
shard index in jah-databases-data-1 (zero hits). No 'catch wrestling'
titles anywhere in the shard indexes; the dedupe gate check on all 68
titles returned zero refusals.

Citations are real landmarks of the art: Shannon J. Say Uncle!
Catch-As-Catch-Can Wrestling (ECW Press; 2005); Hackenschmidt G. The Way
to Live (Athletic Publications; 1908); Burns M. Lessons in Wrestling and
Physical Culture (Farmer Burns School of Wrestling; 1914); the Robinson /
Gotch catch coaching lineage (20th century); United World Wrestling
international wrestling rules; USA Wrestling coaching materials.

Safety frame carried in requirements: catch wrestling is trained with a
cooperative partner under supervision; every submission is practiced with
early taps, and neck and leg attacks are drilled with control first.

Numerical cores are all hand-computed 2026-10-17 and machine-verified by
the demos (see demos_catch_wrestling.py). Every demo prints real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Combat Method: the "
            "hook is the oath, the ride is the watch, and the pin is the "
            "seal. Every technique is a covenant of leverage - the "
            "wrestler swears the position, the partner keeps it honest, and "
            "the hold is the signature. Clearly labeled Signature-made, "
            "never presented as authentic public record.")

CIT_SHANNON = ("Shannon J. Say Uncle! Catch-As-Catch-Can Wrestling. ECW "
               "Press; 2005.")
CIT_HACK = ("Hackenschmidt G. The Way to Live: In Health and Physical "
            "Fitness. Athletic Publications; 1908.")
CIT_BURNS = ("Burns M. Lessons in Wrestling and Physical Culture. Farmer "
             "Burns School of Wrestling; 1914.")
CIT_LINEAGE = ("Robinson B, Gotch K. Catch-as-catch-can wrestling coaching "
               "lineage (Lancashire tradition through the 20th century).")
CIT_UWW = ("United World Wrestling. International Wrestling Rules "
           "(freestyle and Greco-Roman control positions).")
CIT_USAW = ("USA Wrestling. Coaching materials: stance, ties, escapes, and "
            "pinning combinations.")

SUPERVISION = ("A cooperative training partner and qualified coach "
               "supervision; practice new techniques slowly before adding "
               "speed or resistance.")
TAP_EARLY = ("Tap early and often when drilling submissions - the tap is "
             "the contract that keeps both partners safe.")
NECK_LEG = ("Extra control on neck and leg attacks: drill with hands, not "
            "weight, until the entry is clean.")
CONDITION = ("The conditioning to hold the position honestly: grip, neck, "
             "and hip strength built in short daily blocks.")
MAT_SPACE = ("A clean mat with room to move, no jewelry, trimmed nails.")

ENTRIES = [
    {
        "key": "stance",
        "name": "The Catch Wrestlers Stance and Base",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The stance is the root of everything in catch-as-catch-can "
            "wrestling. A wrestler stands with feet roughly shoulder width "
            "apart, one foot slightly ahead of the other, knees bent, hips "
            "low, back straight with the chest up, and weight on the balls "
            "of the feet. The hands stay in front, elbows in, one hand "
            "usually lower to guard the legs. This base does three jobs at "
            "once: it makes the wrestler hard to knock over, it loads the "
            "legs so a shot can fire instantly, and it keeps the head "
            "positioned so the neck cannot be grabbed. Catch wrestlers of "
            "the old Lancashire tradition worked upright more than modern "
            "wrestlers, but the principle never changed - the hips stay "
            "under the shoulders, the weight stays mobile, and nothing "
            "sticks out for the opponent to grab. Every drill in this "
            "database starts by checking the stance, because every "
            "technique fails when the base is wrong."
        ),
        "how_it_works": (
            "Step 1: stand with feet shoulder width apart, dominant foot "
            "about half a foot-length ahead. Step 2: bend the knees until "
            "the hips drop to roughly half the standing height, keeping "
            "the back straight and the chest up rather than rounded "
            "forward. Step 3: shift weight onto the balls of the feet so "
            "the heels feel light enough to pivot. Step 4: set the hands - "
            "lead hand low and forward near the opponent's lead hand, "
            "trail hand guarding the chin, elbows tucked inside the knees. "
            "Step 5: keep the head up with eyes on the opponent's chest, "
            "never bent down where a head tie can be taken. Step 6: test "
            "the base - a partner pushes the chest from the front and "
            "sides; the stance passes when the feet adjust without the "
            "hips rising. Step 7: move in stance - slide forward, "
            "backward, and in circles, keeping the lead foot forward and "
            "the hips at the same height, so the base survives motion."
        ),
        "key_points": [
            "The hips stay under the shoulders at all times; the moment the hips rise above the stance height, every shot and defense gets weaker.",
            "Weight rides the balls of the feet, which keeps the heels free to pivot and the legs loaded like springs.",
            "Hands stay in front with elbows inside the knees - elbows that flare become handles for ties and drags.",
            "Head up, eyes on the chest: a dropped head is the first grip the opponent takes for free.",
            "Stance is mobile - drill sliding in all directions without the hips bouncing, so the base survives real movement.",
        ],
        "requirements": [
            SUPERVISION,
            "A flat training surface with room to slide in stance without obstacles.",
            "Light footwear or bare feet on a mat, as the school permits.",
            TAP_EARLY,
            "Five minutes of stance-and-motion drilling per session before any live wrestling.",
        ],
        "standards": [
            "Stance height is checked against the wrestler's own hip line: hips at roughly half standing height with the back straight.",
            "Base is tested with partner pressure from front and both sides; passing means the feet adjust while the hips stay low.",
        ],
        "citations": [CIT_SHANNON, CIT_HACK, CIT_USAW],
        "sig_lens": (
            "The Signature read: the stance is the first covenant of the "
            "Signature Combat Method. Before any hook or ride exists, the "
            "wrestler signs the floor with his feet - width the witness, "
            "hips the seal, hands the promise that nothing comes free. "
            "Where public wrestling teaches position, the Signature Method "
            "teaches the oath of position: the base holds because the "
            "wrestler swore it would."
        ),
    },
    {
        "key": "posture",
        "name": "Posture, Level Changes, and Penetration Steps",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Posture is what the stance does under pressure, and the level "
            "change is how a wrestler drops from upright to the legs in "
            "one motion. Catch wrestling attacks the legs by changing "
            "levels: the hips drop two to four inches lower than the "
            "stance, the head stays up, and the lead knee drives forward "
            "over the toe in the penetration step. The penetration step "
            "covers the distance to the opponent's legs - the lead knee "
            "lands on the mat between the opponent's feet while the trail "
            "leg drives behind, the head presses into the opponent's side "
            "rather than straight into the chest, and the hands reach for "
            "the legs together. Done right, the level change happens "
            "without the hands dropping first (dropping the hands telegraphs "
            "the shot), and the head never leads the motion where it can "
            "be snapped down. This record pairs with the stance record: "
            "the stance is the loaded position, the level change is the "
            "release."
        ),
        "how_it_works": (
            "Step 1: start in stance with eyes on the opponent's chest. "
            "Step 2: drop the hips two to four inches by bending the knees "
            "deeper - the hands stay up during the drop, they do not swing "
            "down first. Step 3: fire the penetration step - the lead knee "
            "drives forward and down to the mat between the opponent's "
            "feet while the trail leg pushes off hard behind. Step 4: the "
            "head places into the opponent's ribs or hip, cheek tight, "
            "never buried in the center of the chest where the sprawl "
            "lands. Step 5: both hands reach together to secure the legs "
            "at the knees or thighs. Step 6: drive forward through the "
            "position - head up, hips driving, feet stepping - instead of "
            "pulling the legs back from a dead stop. Step 7: drill the "
            "return - after the shot, reset to stance without standing "
            "upright, so the next level change costs nothing."
        ),
        "key_points": [
            "The hips drop before the hands move; hands that drop first warn the opponent and lose the level change.",
            "The lead knee lands between the opponent's feet, not at them - the penetration step must close the whole gap.",
            "Head position decides the shot: into the side keeps the drive alive, into the chest feeds the sprawl.",
            "Drive through the finish with the feet, never pull the legs from a dead stop - momentum finishes takedowns.",
            "Reset without standing up: a level change that ends in a tall stance wastes the next attack.",
        ],
        "requirements": [
            SUPERVISION,
            "Mat space long enough for three full penetration steps without hitting a wall.",
            "Knee pads or a soft mat surface, since the lead knee lands on the mat every rep.",
            TAP_EARLY,
            CONDITION,
        ],
        "standards": [
            "Penetration step lands with the lead knee between the partner's feet and the trail foot driving from behind, checked visually.",
            "Head contact is into the side of the torso with the cheek tight; head-into-chest repetitions are corrected immediately.",
        ],
        "citations": [CIT_SHANNON, CIT_BURNS, CIT_USAW],
        "sig_lens": (
            "The Signature read: the level change is the second covenant - "
            "the wrestler swears the floor by dropping to it on purpose. "
            "The Signature Combat Method treats the penetration step as a "
            "signature across the mat: the knee signs between the "
            "opponent's feet, the head seals against the ribs, and the "
            "drive is the ink that never lifts."
        ),
    },
    {
        "key": "ties",
        "name": "Hand Fighting: Collar Ties and Inside Control",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Hand fighting is the standing battle before the takedown - the "
            "constant contest for the grips that decide who attacks. The "
            "collar tie cups the back of the opponent's neck with the "
            "fingers, thumb beside the ear, controlling the head from "
            "which every posture flows. Inside control means winning the "
            "inside of the arms: elbows in, hands on the inside of the "
            "opponent's biceps or wrists, so any push comes from a position "
            "of advantage. From a collar tie the wrestler can snap the head "
            "down, circle to angles, and set up shots; from inside control "
            "he can pummel to better ties and block the opponent's offense "
            "before it starts. Catch wrestling treats hand fighting as "
            "real offense, not stalling - the wrestler who wins the hands "
            "wins the first grip of every exchange, and in catch the first "
            "honest grip often becomes the first hook."
        ),
        "how_it_works": (
            "Step 1: from stance, extend the lead hand to the inside of the "
            "opponent's arm, palm cupping the back of the neck with the "
            "thumb beside the ear - this is the collar tie. Step 2: keep "
            "the elbow of the tying arm low and heavy, pulling down "
            "slightly so the tie controls rather than rests. Step 3: with "
            "the other hand, win inside position on the opponent's bicep "
            "or wrist - pummel (swim the arm inside) whenever the opponent "
            "takes your inside. Step 4: use the collar tie to move the head "
            "- push to circle, pull to snap - while the inside hand "
            "blocks the opponent's attempts to tie back. Step 5: when the "
            "opponent fights the tie, follow the motion: their push becomes "
            "your pull, their pull becomes the opening for a shot. Step 6: "
            "never let both of the opponent's hands get inside yours at "
            "once - that is the lost position, and the correction is to "
            "pummel one arm inside immediately. Step 7: drill two-minute "
            "hand-fighting rounds with no takedowns allowed, scoring only "
            "inside control and head movement."
        ),
        "key_points": [
            "Inside control is the currency of the standing battle: elbows in, hands inside, and the opponent's offense dies at the wrists.",
            "The collar tie controls the head, and the head controls the spine - move the head and the whole body follows.",
            "Pummeling is the correction for lost inside position: swim the arm inside the moment the opponent takes it.",
            "Follow the opponent's resistance instead of fighting it - pushes become pulls and pulls become shot openings.",
            "Hand fighting is scored in practice with no takedowns, so the grip battle gets trained as its own skill.",
        ],
        "requirements": [
            SUPERVISION,
            "A partner willing to tie up and pummel at increasing intensity.",
            "Trimmed nails and no jewelry, since hand fighting is constant hand contact.",
            TAP_EARLY,
            CONDITION,
        ],
        "standards": [
            "Collar tie cups the back of the neck with fingers curled and thumb beside the ear - no throat contact, no grabbing the chin.",
            "Two-minute hand-fighting rounds are scored on inside control time, not on takedowns.",
        ],
        "citations": [CIT_SHANNON, CIT_BURNS, CIT_USAW],
        "sig_lens": (
            "The Signature read: hand fighting is the argument before the "
            "verdict. The Signature Combat Method counts every inside grip "
            "as a signed clause - the wrestler who holds the inside holds "
            "the pen, and every collar tie is a draft of the head's "
            "future. Win the hands and the hooks are already written."
        ),
    },
    {
        "key": "wrist_control",
        "name": "Wrist Control and the Two-on-One Tie",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Wrist control is the simplest honest grip in wrestling: hold "
            "the opponent's wrist and you hold one quarter of his offense. "
            "Catch wrestlers chain wrist control into the two-on-one (the "
            "Russian tie), where both hands grip a single one of the "
            "opponent's arms - one hand on the wrist, one on the tricep or "
            "elbow. Two hands against one arm is leverage arithmetic that "
            "always favors the pair: the controlled arm can be dragged "
            "across the body, pulled down for a snap, or used as a lever "
            "to turn the opponent. From the two-on-one the classic "
            "follow-ups are the arm drag to the back, the snap-down to the "
            "front headlock, and the single-leg when the opponent steps to "
            "recover. This is also the gateway to catch's submission game - "
            "the two-on-one wrist is where the double wrist lock begins, "
            "so every rep of this tie quietly rehearses a hook."
        ),
        "how_it_works": (
            "Step 1: grip the opponent's wrist with a full-hand grip, "
            "thumb wrapped, on the inside of the tie. Step 2: step to the "
            "outside of the controlled arm so your body is beside their "
            "arm rather than in front of it. Step 3: bring the second hand "
            "to the tricep or elbow of the same arm - now two hands own one "
            "arm, and the grip is the two-on-one. Step 4: keep the "
            "controlled wrist above your own elbow line and the elbow of "
            "the arm bent no more than ninety degrees, so the lever stays "
            "short for you and long for them. Step 5: drag - pull the arm "
            "across their body and step behind to the back; or snap - pull "
            "down sharply and follow to the front headlock. Step 6: if "
            "they pull back hard, ride the pull and change direction into "
            "a single-leg on the near leg. Step 7: drill both exits - arm "
            "drag and snap-down - alternating, so the two-on-one always "
            "ends in motion rather than a stalemate."
        ),
        "key_points": [
            "Two hands on one arm is leverage that always wins the arithmetic - the single arm cannot out-pull the pair.",
            "Step to the outside of the controlled arm; the angle makes the drag and the snap-down possible.",
            "Keep the controlled wrist high and the arm bent - a straightened arm is the opponent's escape route.",
            "The tie has two honest exits, the arm drag and the snap-down, and the drill always ends in one of them.",
            "This tie is the first rehearsal of the double wrist lock - every clean rep is a hook practiced in disguise.",
        ],
        "requirements": [
            SUPERVISION,
            "Full-hand wrist grips with thumbs wrapped - no finger-only grips that slip under load.",
            TAP_EARLY,
            "A partner who resists the drag realistically but taps to any wrist pressure immediately.",
            MAT_SPACE,
        ],
        "standards": [
            "The second hand lands on the tricep or elbow of the controlled arm, never on the shoulder or neck.",
            "Drill alternates the arm-drag exit and the snap-down exit in equal numbers so neither becomes the only habit.",
        ],
        "citations": [CIT_SHANNON, CIT_LINEAGE, CIT_USAW],
        "sig_lens": (
            "The Signature read: the two-on-one is the Signature Combat "
            "Method's first doubled signature - two hands signing one "
            "arm. Where public wrestling counts it as a tie, the Signature "
            "lens counts it as an unsigned hook: the wrist is already "
            "witnessed, and the double wrist lock is only the formal "
            "reading of what the tie has written."
        ),
    },
    {
        "key": "snapdown",
        "name": "The Snap-Down and Go-Behind",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The snap-down is catch wrestling's front-door takedown: from a "
            "collar tie or two-on-one, the wrestler pulls the opponent's "
            "head down sharply, breaking their posture, then circles behind "
            "as the head drops. When the head goes down, the hips follow "
            "and the hands reach for the mat - the opponent is now on all "
            "fours, and the wrestler is behind with the classic go-behind "
            "control. The go-behind is one of the highest-percentage "
            "scoring positions in wrestling: from behind, the wrestler "
            "locks hands around the waist or takes a tight waist, settles "
            "the hips, and begins the ride. Catch wrestlers chain the "
            "snap-down to the front headlock series when the opponent "
            "posts, and to the go-behind when the head drops cleanly. Five "
            "snaps per side in drilling, with the go-behind finished every "
            "rep, builds the reflex that turns every tie into a takedown "
            "threat."
        ),
        "how_it_works": (
            "Step 1: establish the collar tie or two-on-one with the "
            "elbow heavy. Step 2: pull the head down and slightly to one "
            "side in a sharp, short motion - the power comes from the "
            "back and hips, not the arm alone. Step 3: as the head drops, "
            "step to the side the head was pulled toward, circling behind. "
            "Step 4: keep contact - the hand that snapped stays on the head "
            "or neck, guiding it down as you circle. Step 5: when the "
            "opponent's hands hit the mat, release the head and lock "
            "around the waist or take a tight waist with the near arm. "
            "Step 6: settle the hips behind their hips, chest on their "
            "back, and establish the ride - you are now in the "
            "go-behind. Step 7: if they post a hand to stop the fall, "
            "switch the grip to the chin strap and take the front headlock "
            "instead of forcing the go-behind."
        ),
        "key_points": [
            "The snap is short and sharp from the back and hips - a long arm-only pull wastes the tie.",
            "Circle toward the side the head was pulled; chasing straight behind lets the opponent square up.",
            "Keep the snapping hand on the head through the circle so the posture never recovers mid-motion.",
            "The go-behind is the highest-percentage finish: waist lock or tight waist, hips settled, ride established.",
            "A posted hand is not a failure - it is the front headlock, the snap-down's built-in second option.",
        ],
        "requirements": [
            SUPERVISION,
            "Collar tie control established before any snap is attempted.",
            TAP_EARLY,
            "Partners who go with the snap rather than stiffening the neck against it.",
            CONDITION,
        ],
        "standards": [
            "The snap pulls the head down and to the side; straight-down pulls that compress the neck are corrected.",
            "Every drilling rep finishes with either the go-behind or the front headlock - no rep ends in a stalemate.",
        ],
        "citations": [CIT_SHANNON, CIT_BURNS, CIT_USAW],
        "sig_lens": (
            "The Signature read: the snap-down is the verdict after the "
            "hand-fighting argument. The Signature Combat Method treats "
            "the broken posture as a signed confession - the head signs "
            "downward, the circle signs behind, and the go-behind is the "
            "seal pressed on the back. Every tie was a draft; the snap is "
            "the execution."
        ),
    },
    {
        "key": "front_headlock",
        "name": "The Front Headlock (Chin Strap)",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The front headlock is the position wrestling returns to more "
            "than any other: the opponent's head is tucked under the "
            "wrestler's arm, chin strapped by the forearm, with the other "
            "hand controlling the far arm or elbow. From here the wrestler "
            "can score the go-behind, attack the guillotine, work the "
            "chin-whip turn, or simply hold and break the opponent down to "
            "the mat. The keys are the chin strap - the forearm across the "
            "chin, not the throat - and the hips back, so the position "
            "cannot be lifted. Catch wrestlers favor the front headlock "
            "because it is a crossroads: the same grip becomes a control, "
            "a takedown, and a submission, and the opponent must defend "
            "all three at once. Drill the entries (snap-down, sprawl "
            "rebound, missed shot) and the exits (go-behind, guillotine, "
            "chin whip) as one connected series."
        ),
        "how_it_works": (
            "Step 1: from the snap-down or a sprawl, wrap the near arm "
            "over the opponent's head so the forearm lies across the chin "
            "and the hand grips the far tricep or elbow - the chin strap. "
            "Step 2: hips go back and down, chest heavy on the opponent's "
            "upper back, so the head cannot be lifted. Step 3: the free "
            "hand controls the near elbow or wrist to block the sit-out. "
            "Step 4: to go behind, pull the chin strap toward you and "
            "circle to the side as the opponent's head comes up, sliding "
            "to the back. Step 5: for the guillotine, slide the strapping "
            "forearm deeper so the wrist sits under the chin and close "
            "the grip hand to the chest. Step 6: for the chin whip, whip "
            "the head toward the mat on the far side while stepping over "
            "to turn them. Step 7: if the opponent locks their hands to "
            "defend, keep the strap and walk the hips back - the pressure "
            "builds until one of the three exits opens."
        ),
        "key_points": [
            "The strap goes across the chin, never the throat - the position is a chin strap, not a choke, until the guillotine is chosen.",
            "Hips back and chest heavy make the headlock unliftable; hips forward make it a gift to the opponent.",
            "One grip serves three exits - go-behind, guillotine, chin whip - and the drill trains all three from the same entry.",
            "The free hand has a job: control the near elbow so the sit-out escape is closed before it starts.",
            "Patience is a technique here: hold the strap, walk the hips back, and let the pressure open an exit.",
        ],
        "requirements": [
            SUPERVISION,
            TAP_EARLY,
            "Forearm across the chin only - any throat pressure is an immediate reset and correction.",
            NECK_LEG,
            CONDITION,
        ],
        "standards": [
            "Chin strap placement is verified on the chin/jaw line with the hand gripping far tricep or elbow before any exit is attempted.",
            "Drill cycles all three exits (go-behind, guillotine, chin whip) from the same snap-down entry.",
        ],
        "citations": [CIT_SHANNON, CIT_LINEAGE, CIT_USAW],
        "sig_lens": (
            "The Signature read: the front headlock is the crossroads "
            "where the Signature Combat Method keeps three signed roads "
            "open at once. The chin strap is the oath, the hips-back the "
            "witness, and the opponent must answer all three exits with "
            "one defense. Where public wrestling sees a control, the "
            "Signature lens sees a triple-sealed letter waiting for the "
            "opponent to choose which seal breaks first."
        ),
    },
    {
        "key": "sprawl",
        "name": "Sprawl and Leg Defense",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The sprawl is the answer to every leg attack: as the opponent "
            "shoots, the wrestler throws the legs back, drops the hips to "
            "the mat, and drives the chest and hips down onto the "
            "attacker's head and shoulders. The legs go back wide so the "
            "attacker cannot circle to one, the hips stay heavy so the "
            "attacker cannot lift, and the hands post on the head or "
            "shoulders to keep the attacker's face on the mat. From the "
            "sprawl the wrestler works the crossface, spins behind for the "
            "go-behind, or takes the front headlock as the attacker tries "
            "to come up. The sprawl must be reflexive - it is drilled from "
            "a whistle or a tap until the legs fire without thought, "
            "because a thinking sprawl arrives one step too late. Ten "
            "sprawls at the start of every session keeps the reflex honest."
        ),
        "how_it_works": (
            "Step 1: on the shot (or the whistle in drilling), throw both "
            "legs straight back, landing on the tops of the feet with the "
            "legs wide. Step 2: drop the hips to the mat, driving the "
            "weight down through the hips onto the attacker's head and "
            "shoulders. Step 3: post the hands on the attacker's head or "
            "upper back, keeping their face pointed at the mat. Step 4: "
            "keep the head up and the chest broad - do not collapse onto "
            "the attacker, stay heavy and mobile. Step 5: work the "
            "crossface with the near forearm across the attacker's face "
            "toward the far side. Step 6: as the attacker turns away from "
            "the crossface, spin behind and take the go-behind; if they "
            "try to stand into you, wrap the front headlock. Step 7: drill "
            "the full chain - sprawl, crossface, spin behind - as one "
            "motion, resetting to stance between reps."
        ),
        "key_points": [
            "Both legs go back together and wide - a single-leg trail lets the attacker finish on the standing leg.",
            "Hips drive down onto the attacker's head and shoulders; the sprawl is a weapon of weight, not a retreat.",
            "Hands post on the head or upper back to keep the face on the mat - the attacker who sees the ceiling is already beaten.",
            "The sprawl has two exits, the crossface spin-behind and the front headlock, and drilling always finishes one of them.",
            "Reflex is the standard: drill from a whistle until the legs fire without a decision.",
        ],
        "requirements": [
            SUPERVISION,
            "Mat space behind for the full leg throw without hitting walls or other pairs.",
            "Partners who shoot at realistic speed but never at full power in drilling.",
            TAP_EARLY,
            CONDITION,
        ],
        "standards": [
            "The sprawl lands hips-to-mat with legs back and wide, verified visually before the crossface is worked.",
            "Ten whistle-start sprawls open every session; the reflex is the requirement, not the theory.",
        ],
        "citations": [CIT_SHANNON, CIT_BURNS, CIT_USAW],
        "sig_lens": (
            "The Signature read: the sprawl is the Signature Combat "
            "Method's refusal, signed with the hips. Where the shot is the "
            "opponent's claim on the legs, the sprawl is the counter-"
            "signature - legs witnessed back, weight sealed down, and the "
            "attacker's face pressed to the mat as the notary stamp. "
            "Every whistle is a new document; the reflex is the hand that "
            "never hesitates."
        ),
    },
    {
        "key": "hip_bump",
        "name": "Hip Bump and Sit-Out Escapes from Bottom",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The bottom position is where matches are lost, and the hip "
            "bump and sit-out are how wrestlers leave it. The hip bump "
            "(hip heist) explodes the hips upward and to one side, "
            "dislodging the rider's weight so the bottom wrestler can face "
            "him. The sit-out turns the hips out from under the opponent: "
            "posting a hand, swinging the hips through, and coming up to "
            "face the opponent or take the back. Both escapes share one "
            "rule - the bottom wrestler must move before the top wrestler "
            "settles; a settled ride is ten times harder to escape. Catch "
            "wrestling values the bottom game because the old matches "
            "were won and lost there: the man underneath who could always "
            "escape forced the top man to attack, and the attacker who "
            "overcommits gets reversed. Drill each escape fifty times per "
            "side before it is trusted in live wrestling."
        ),
        "how_it_works": (
            "Step 1: from the bottom referee's position (hands and knees, "
            "opponent riding), keep the elbows tight and the head up. Step "
            "2: for the hip bump, bridge the hips hard up and to one side, "
            "throwing the rider's weight off-center. Step 3: as the weight "
            "shifts, turn into the opening - face the opponent, post the "
            "hands, and come to a base. Step 4: for the sit-out, post the "
            "near hand on the mat and swing the hips out and through to "
            "the far side in one motion. Step 5: keep the far arm tight to "
            "the body during the sit-out so it cannot be trapped. Step 6: "
            "finish facing the opponent in stance, or continue the motion "
            "to take the back if the rider over-follows. Step 7: chain "
            "them - if the hip bump stalls, sit out off the same bridge; "
            "if the sit-out is blocked, bump again. The escapes are a "
            "pair, not two solos."
        ),
        "key_points": [
            "Escape before the ride settles: the first two seconds underneath are worth more than the next twenty.",
            "The hip bump throws the rider's weight off-center first; the turn into the opening comes second.",
            "The sit-out swings the hips through in one motion with the far arm tight - a loose arm gets trapped.",
            "Both escapes finish facing the opponent in stance; an escape that ends flat is not finished.",
            "The bump and the sit-out are chained off the same bridge, so a blocked escape becomes the other escape.",
        ],
        "requirements": [
            SUPERVISION,
            "A partner riding at increasing pressure, never at full pinning force in drilling.",
            TAP_EARLY,
            CONDITION,
            MAT_SPACE,
        ],
        "standards": [
            "Each escape is drilled fifty times per side before use in live wrestling.",
            "Finishing position is verified: facing the opponent in stance, not flat or turned away.",
        ],
        "citations": [CIT_BURNS, CIT_USAW, CIT_LINEAGE],
        "sig_lens": (
            "The Signature read: the bottom is not a defeat in the "
            "Signature Combat Method - it is a document under review. The "
            "hip bump is the objection, the sit-out the appeal, and the "
            "finish facing the opponent is the case reopened. Where public "
            "wrestling teaches survival underneath, the Signature lens "
            "teaches authorship: the man who escapes writes the next "
            "chapter."
        ),
    },
    {
        "key": "granby",
        "name": "The Granby Roll and Inversion Escapes",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "The Granby roll is the escape for when the top wrestler has "
            "committed to a turn: the bottom wrestler rolls under his own "
            "shoulder, inverts, and comes up behind or beside the attacker. "
            "Named for the wrestlers who made it famous, the Granby works "
            "because the top man's weight is committed forward - the roll "
            "goes where the weight cannot follow. The inversion family "
            "includes the shoulder roll, the Peterson roll, and the simple "
            "hip-over escape: all share the principle of going under "
            "rather than fighting the pressure. Catch wrestlers use the "
            "Granby both defensively (escaping a deep half nelson or "
            "cradle attempt) and offensively (rolling through into a leg "
            "attack). It is an athletic move that demands practice on "
            "both sides until the roll is a reflex, because a slow Granby "
            "hands the top man the back."
        ),
        "how_it_works": (
            "Step 1: as the top wrestler commits weight forward for a "
            "turn, tuck the chin and post the near hand. Step 2: roll over "
            "the near shoulder, going under the attacker's pressure rather "
            "than pushing against it. Step 3: invert - let the hips go "
            "over the head, keeping the body tight and round. Step 4: kick "
            "the legs through the roll so the hips clear the attacker's "
            "grip. Step 5: land facing the opponent or, if the roll went "
            "deep, come up behind to the go-behind. Step 6: for the "
            "Peterson variation, catch the attacker's far ankle during the "
            "roll and sit through to turn the tables into a pinning "
            "combination. Step 7: drill both sides slowly with a partner "
            "applying light forward pressure, adding speed only when the "
            "roll is clean and the chin stays tucked."
        ),
        "key_points": [
            "The Granby goes under committed weight - it answers forward pressure, not patient control.",
            "Chin tucked and body round: the roll is a ball, and a ball has no handles for the top man.",
            "The legs kick through to clear the hips; a roll that stops halfway gives up the back.",
            "The Peterson variation turns the escape into a pin by catching the far ankle mid-roll.",
            "Both sides, slow first: a fast, sloppy Granby is a gift of the back to the opponent.",
        ],
        "requirements": [
            SUPERVISION,
            "A partner applying light forward pressure that increases only as the roll cleans up.",
            TAP_EARLY,
            CONDITION,
            "Neck flexibility work before drilling - the tucked chin must be comfortable, not forced.",
        ],
        "standards": [
            "The roll is drilled slowly on both sides with the chin tucked before any speed is added.",
            "Landing position is verified: facing the opponent or behind them, never flat under the attacker.",
        ],
        "citations": [CIT_SHANNON, CIT_USAW, CIT_LINEAGE],
        "sig_lens": (
            "The Signature read: the Granby is the Signature Combat "
            "Method's vanishing signature - the wrestler signs himself "
            "out from under the attack and re-signs behind it. Where the "
            "top man pressed his claim forward, the roll is the document "
            "slipping out from under the stamp. Public wrestling calls it "
            "an escape; the Signature lens calls it a relocation of "
            "authorship."
        ),
    },
    {
        "key": "bridge",
        "name": "Bridging: The Pin-Defense Bridge",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "The bridge is the last line of pin defense: with the shoulders "
            "on the mat and a pin imminent, the wrestler arches onto the "
            "head and feet, lifting the hips and shoulders off the mat so "
            "the shoulders cannot be held down. Catch-as-catch-can was "
            "decided by pins, so the bridge was survival itself - the old "
            "timers held bridges for minutes. A proper bridge posts the "
            "head (top of the head, not the forehead) and the feet wide, "
            "arches the back high, and keeps the arms free to fight the "
            "hands. From the bridge the wrestler walks the feet, turns the "
            "hips, and works back to the belly or reverses the position. "
            "The bridge is also trained as conditioning: neck bridges held "
            "for time build the exact strength that pin defense requires. "
            "Three thirty-second bridges per session is the honest minimum "
            "for a wrestler who wants to survive underneath."
        ),
        "how_it_works": (
            "Step 1: as the shoulders near the mat, tuck the chin and post "
            "the top of the head on the mat - never the forehead, which "
            "compresses the neck wrong. Step 2: post the feet wide, heels "
            "under or outside the hips. Step 3: arch hard - drive the hips "
            "to the ceiling, lifting the shoulders off the mat. Step 4: "
            "keep the arms free to fight the opponent's hands and hooks; "
            "the bridge holds the position while the hands do the work. "
            "Step 5: walk the feet in small steps to turn the hips away "
            "from the pressure, following the direction of the attack. "
            "Step 6: when the pressure eases, kick the hips over and belly "
            "down, or continue the turn to reverse. Step 7: train the "
            "bridge as conditioning - hold for time, rock gently front to "
            "back, and build from thirty seconds toward two minutes."
        ),
        "key_points": [
            "Post the top of the head, never the forehead - the bridge is a neck arch, not a neck compression.",
            "Hips to the ceiling: the bridge wins by height, lifting the shoulders out of the pin.",
            "The arms stay free to fight hands while the bridge holds the structure - structure and hand-fighting are separate jobs.",
            "Walk the feet to turn the hips away from pressure; a static bridge is eventually flattened.",
            "Bridge holds are conditioning: thirty seconds is the minimum, two minutes is the standard of the old timers.",
        ],
        "requirements": [
            SUPERVISION,
            "Gradual bridge conditioning - never force a deep bridge on an unprepared neck.",
            TAP_EARLY,
            "A partner who applies pinning pressure progressively, not suddenly.",
            "Neck warm-up and flexibility work before every bridging session.",
        ],
        "standards": [
            "Head posts on the top of the head with the chin tucked; forehead posting is corrected immediately.",
            "Bridge holds progress from thirty seconds toward two minutes across the training block.",
        ],
        "citations": [CIT_HACK, CIT_BURNS, CIT_SHANNON],
        "sig_lens": (
            "The Signature read: the bridge is the Signature Combat "
            "Method's final seal under pressure. Where the pin is the "
            "opponent's claim to have finished the document, the bridge "
            "is the paper rising off the desk - unsigned, unheld, and "
            "arching toward the ceiling. The old timers held it for "
            "minutes; the Signature lens holds it as long as the oath "
            "requires."
        ),
    },
]

ENTRIES += [
    {
        "key": "tight_waist",
        "name": "The Tight Waist and Crossface Ride",
        "group": "Rides and Turns",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "The tight waist and crossface is the first ride every wrestler "
            "learns: from behind the opponent, the near arm wraps around "
            "the waist with the hand locking on the far hip (tight waist), "
            "while the far forearm drives across the face toward the far "
            "side (crossface). The chest stays heavy on the opponent's "
            "back, the hips stay behind their hips, and the legs post wide "
            "for base. From this ride the wrestler breaks the opponent "
            "down flat, works the half nelson, or lifts for the return. "
            "The crossface is the steering wheel: pressure on the face "
            "turns the head, the head turns the shoulders, and the "
            "shoulders decide the pin. Catch wrestling rides to break the "
            "opponent down and keep him there - the ride is not a rest "
            "position, it is a machine for turning the man underneath "
            "toward his back, one breakdown at a time."
        ),
        "how_it_works": (
            "Step 1: from the go-behind, wrap the near arm around the "
            "waist and lock the hand on the far hip or the far wrist - "
            "the tight waist. Step 2: bring the far forearm across the "
            "opponent's face, driving toward the far side - the crossface. "
            "Step 3: settle the chest heavy on their back and the hips "
            "behind their hips, legs posted wide. Step 4: break them down "
            "- drive forward and to the side with the crossface while the "
            "tight waist pulls the hips, flattening the opponent to the "
            "belly. Step 5: when they build back up, meet the rise with "
            "the crossface and break them down again - the ride is a "
            "cycle, not a hold. Step 6: as they flatten, slide the "
            "crossface arm under the far arm for the half nelson, or chop "
            "the near arm for the bar arm. Step 7: drill the breakdown "
            "cycle - break down, let them build, break down again - until "
            "the ride runs without thought."
        ),
        "key_points": [
            "The tight waist locks the hips while the crossface steers the head - control both ends and the middle follows.",
            "Chest heavy, hips behind, legs wide: the ride is a structure, and a broken structure is a reversal.",
            "The breakdown is a cycle - flatten them, let them build, flatten them again - until the turn opens.",
            "The crossface drives toward the far side, turning the head, shoulders, and eventually the back.",
            "The ride feeds the turns: half nelson and bar arm both start from the crossface position.",
        ],
        "requirements": [
            SUPERVISION,
            "The crossface drives across the cheek and jaw - never across the throat or into the eyes.",
            TAP_EARLY,
            "A partner who builds back up realistically so the breakdown cycle can be drilled.",
            CONDITION,
        ],
        "standards": [
            "Crossface placement is verified across the cheek/jaw line before pressure is applied.",
            "Drill runs the full breakdown cycle - down, build, down - with the ride structure intact throughout.",
        ],
        "citations": [CIT_USAW, CIT_BURNS, CIT_SHANNON],
        "sig_lens": (
            "The Signature read: the ride is the watch in the Signature "
            "Combat Method - the wrestler keeps the hours on the "
            "opponent's back. The tight waist is the first hand on the "
            "clock, the crossface the second, and the breakdown cycle is "
            "time itself wearing the man underneath down. Public wrestling "
            "rides to control; the Signature lens rides to record every "
            "minute until the pin signs itself."
        ),
    },
    {
        "key": "half_nelson",
        "name": "The Half Nelson",
        "group": "Rides and Turns",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "The half nelson is the most famous turn in wrestling: from "
            "the side or behind, the wrestler slides one arm under the "
            "opponent's near arm and locks the hand on the back of the "
            "opponent's neck, then drives forward and across to turn the "
            "shoulders to the mat. The power comes from the legs and hips "
            "driving through, not from the arm alone - the arm is the "
            "hook, the body is the engine. The half nelson is finished "
            "with the chest on the opponent's chest, the free hand "
            "controlling the far wrist or posting for base, and the hips "
            "driving until the shoulders are flat. Catch wrestlers chain "
            "it with the tight waist, the crossface, and the far-side "
            "cradle: when the opponent fights the half nelson by turning "
            "in, the cradle is waiting; when he turns away, the half "
            "nelson finishes. Fifty half nelsons per side in drilling "
            "builds the turn that ends matches."
        ),
        "how_it_works": (
            "Step 1: from the ride, slide the near arm under the "
            "opponent's near arm, threading deep. Step 2: lock the hand "
            "on the back of the opponent's neck - palm on the neck, not "
            "the head. Step 3: the free hand controls the far wrist or "
            "posts on the mat for base. Step 4: drive with the legs and "
            "hips forward and across, using the locked arm as the lever "
            "that turns the shoulders. Step 5: keep driving until the "
            "chest is on their chest and the shoulders are flat - do not "
            "stop at the first turn of the shoulders. Step 6: if the "
            "opponent turns into you to fight it, switch to the far-side "
            "cradle; if they turn away, finish the half nelson. Step 7: "
            "drill the entry from the crossface ride, the finish, and the "
            "cradle switch as one connected chain."
        ),
        "key_points": [
            "The arm is the hook and the body is the engine - legs and hips drive the turn, not the arm alone.",
            "Lock the hand on the back of the neck, palm down, so the lever turns the shoulders rather than cranking the head.",
            "Drive through the finish: chest on chest, shoulders flat - a half-turned opponent is a reversed wrestler.",
            "The chain is the technique: half nelson, cradle switch when they turn in, finish when they turn away.",
            "Fifty reps per side makes the turn reflexive; the half nelson must fire without a decision.",
        ],
        "requirements": [
            SUPERVISION,
            "The lock goes on the back of the neck, never a chin or throat crank.",
            TAP_EARLY,
            NECK_LEG,
            "A partner who fights the turn realistically so the cradle switch can be drilled.",
        ],
        "standards": [
            "Hand placement verified on the back of the neck with the palm flat before the drive begins.",
            "Finish position verified: chest on chest with both shoulders flat to the mat.",
        ],
        "citations": [CIT_BURNS, CIT_USAW, CIT_SHANNON],
        "sig_lens": (
            "The Signature read: the half nelson is the Signature Combat "
            "Method's first signed turn - one arm under, one hand on the "
            "neck, and the body's drive as the witness. Where public "
            "wrestling counts it as a move, the Signature lens counts it "
            "as the oath of the ride made visible: the hook signed, the "
            "drive witnessed, the shoulders sealed to the mat."
        ),
    },
    {
        "key": "bar_arm",
        "name": "The Bar Arm and Chicken Wing",
        "group": "Rides and Turns",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The bar arm (chicken wing) pins the opponent's arm behind "
            "their back and uses it as the lever to turn them: the "
            "wrestler chops the near arm, threads his own arm through, and "
            "locks the opponent's wrist up behind the back, then drives "
            "across to turn the shoulders down. It is a shoulder lock as "
            "well as a turn - the trapped arm's shoulder is the fulcrum, "
            "and the pressure on it forces the body to follow or submit. "
            "Catch wrestling, where submissions counted alongside pins, "
            "treated the chicken wing as both: the turn for the pin and "
            "the lock for the tap. The entries come from the ride (chop "
            "the arm as they build up), from the front headlock (thread "
            "the trapped arm), and from scrambles where an arm is left "
            "behind. Control the wrist high between the shoulder blades "
            "and the leverage is total; let it slide low and the escape "
            "opens."
        ),
        "how_it_works": (
            "Step 1: from the ride, as the opponent posts the near arm, "
            "chop it and thread your near arm through above their elbow. "
            "Step 2: lock their wrist up behind their back, holding it "
            "high between the shoulder blades with your hand. Step 3: the "
            "free hand takes a tight waist or the far wrist for control. "
            "Step 4: drive across with the hips and chest, using the "
            "trapped arm as the lever to turn the shoulders to the mat. "
            "Step 5: keep the wrist high throughout the turn - height is "
            "leverage, and a dropping wrist is an escaping wrist. Step 6: "
            "if they bridge hard, settle the weight and walk the turn "
            "around rather than forcing through the bridge. Step 7: drill "
            "the chicken wing as both a pinning turn and a controlled "
            "shoulder lock, with the partner tapping to the lock version "
            "early."
        ),
        "key_points": [
            "The trapped arm is the lever and the shoulder is the fulcrum - height of the wrist decides the leverage.",
            "Keep the wrist high between the shoulder blades through the whole turn; a sliding wrist is an escaping wrist.",
            "The drive comes from hips and chest across, not from yanking the trapped arm.",
            "The chicken wing is both a turn and a lock - drill the pin version and the tap version as one technique.",
            "Against the bridge, walk the turn around patiently rather than forcing through it.",
        ],
        "requirements": [
            SUPERVISION,
            TAP_EARLY,
            NECK_LEG,
            "A partner who taps to shoulder pressure immediately in the lock version.",
            "The wrist is held, never yanked - smooth pressure only.",
        ],
        "standards": [
            "Wrist held high between the shoulder blades, verified before the turning drive begins.",
            "Lock version is drilled with early taps; the pin version with full turning drive.",
        ],
        "citations": [CIT_SHANNON, CIT_LINEAGE, CIT_USAW],
        "sig_lens": (
            "The Signature read: the chicken wing is the Signature Combat "
            "Method's double-sealed document - a turn and a lock in one "
            "grip. The trapped arm signs twice: once toward the pin, once "
            "toward the tap, and the wrist height is the ink. Where public "
            "wrestling sees a move, the Signature lens sees a covenant "
            "with two possible endings, both already written."
        ),
    },
    {
        "key": "double_leg",
        "name": "The Double-Leg Takedown with the Hook Finish",
        "group": "Takedowns and Throws",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The double leg is wrestling's fundamental takedown: change "
            "levels, penetrate, wrap both legs, and drive through. The "
            "catch wrestler's version finishes with the hook - after the "
            "drive, the trail leg hooks behind the opponent's legs or the "
            "wrestler drops to finish with a leg hook that kills the "
            "base. The keys are the penetration step landing deep (knee "
            "between their feet), the head in the side (never the chest), "
            "and the drive continuing through the finish rather than "
            "stopping at contact. Against the sprawl, the double leg "
            "becomes a chain: drive to a knee, switch to the single, or "
            "lift and return. Old catch matches were often decided by "
            "this one shot landed cleanly - the double leg that finishes "
            "puts the wrestler straight into the ride with the opponent "
            "broken down."
        ),
        "how_it_works": (
            "Step 1: from stance, change levels without dropping the hands "
            "first. Step 2: fire the penetration step - lead knee to the "
            "mat between their feet, trail leg driving behind. Step 3: the "
            "head goes to the side (ribs or hip), cheek tight, both arms "
            "wrapping the legs at the knees. Step 4: drive forward - head "
            "up, hips in, feet stepping - through the opponent, not into "
            "them. Step 5: the hook finish - as they fall, the trail leg "
            "hooks behind their legs or the wrestler drops the hips to "
            "kill the base. Step 6: follow to the mat chest-to-chest, "
            "taking the tight waist or half nelson as they land. Step 7: "
            "against the sprawl, keep driving to a knee and chain to the "
            "single leg rather than bailing out."
        ),
        "key_points": [
            "The knee lands between their feet and the head goes to the side - depth and head position decide the shot.",
            "Drive through the finish with the feet stepping; stopping at contact is how double legs die.",
            "The hook finish kills the base on the way down so the landing goes straight into the ride.",
            "Follow to the mat chest-to-chest and take the ride grips before the opponent recovers.",
            "Against the sprawl the shot becomes a chain - single leg, lift, or knee-drive - never a bailout.",
        ],
        "requirements": [
            SUPERVISION,
            "Mat space for the full drive and landing without obstacles.",
            "Knee protection for the penetration-step knee.",
            TAP_EARLY,
            CONDITION,
        ],
        "standards": [
            "Penetration knee lands between the partner's feet with the head in the side, verified each rep.",
            "Landing finishes chest-to-chest with ride grips taken before the reset.",
        ],
        "citations": [CIT_USAW, CIT_BURNS, CIT_SHANNON],
        "sig_lens": (
            "The Signature read: the double leg is the Signature Combat "
            "Method's full-signature takedown - both legs witnessed, the "
            "drive the ink, the hook the seal. Where the penetration step "
            "was a signature across the mat, the double leg is the whole "
            "document: level change the heading, penetration the body, "
            "hook finish the closing seal straight into the ride."
        ),
    },
    {
        "key": "double_wrist_lock",
        "name": "The Double Wrist Lock (Kimura Grip)",
        "group": "Hooks and Submissions",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The double wrist lock is catch wrestling's signature "
            "submission: both of the attacker's hands grip one of the "
            "defender's arms in a figure-four, and the arm is rotated "
            "behind the back to attack the shoulder. It is the submission "
            "the two-on-one tie has been rehearsing since the foundations "
            "- the same two-hands-on-one-arm arithmetic, now bent into a "
            "lock. The figure-four grip (one hand gripping the wrist, the "
            "other hand gripping your own wrist behind their arm) gives "
            "total control of the lever, and the finish rotates the arm up "
            "behind the back with the attacker's body weight. Catch "
            "wrestlers apply it from side control, from the north-south "
            "position, and standing from the two-on-one. The tap comes "
            "from shoulder rotation, so the lock is applied with smooth, "
            "steady pressure - never a jerk."
        ),
        "how_it_works": (
            "Step 1: isolate the arm - from side control or the two-on-"
            "one, control the wrist with one hand. Step 2: thread your "
            "other arm behind their arm and grip your own wrist, forming "
            "the figure-four - two hands now own one arm completely. Step "
            "3: keep their elbow bent at roughly ninety degrees and their "
            "wrist above their elbow line so the lever stays short. Step "
            "4: step or pivot so your body is beside them, not on top of "
            "the trapped arm. Step 5: rotate the arm up behind their back "
            "with smooth, steady pressure from the whole body - the "
            "shoulder rotation, not arm strength, makes the tap. Step 6: "
            "the free hand (if standing) controls their body so they "
            "cannot turn out of the lock. Step 7: release the instant the "
            "partner taps; in drilling, the lock is a control position "
            "first and a finish second."
        ),
        "key_points": [
            "The figure-four grip gives total control of the lever - two hands on one arm is the arithmetic of the whole technique.",
            "Keep the elbow at ninety degrees and the wrist high; a straightening arm is an escaping arm.",
            "The finish is smooth body-weight rotation, never a jerk - the shoulder is attacked by position, not by yanking.",
            "Isolate before you lock: the arm must be separated from the body before the figure-four goes on.",
            "The tap ends the rep instantly; the lock is drilled as a control position as often as a finish.",
        ],
        "requirements": [
            SUPERVISION,
            TAP_EARLY,
            NECK_LEG,
            "Smooth, steady pressure only - jerking the lock is an immediate stop and correction.",
            "A partner who taps early to shoulder rotation.",
        ],
        "standards": [
            "Figure-four grip verified (hand on wrist, other hand on own wrist behind their arm) before rotation begins.",
            "Finish applied with steady body-weight pressure; any jerking motion fails the rep.",
        ],
        "citations": [CIT_SHANNON, CIT_LINEAGE, CIT_BURNS],
        "sig_lens": (
            "The Signature read: the double wrist lock is the Signature "
            "Combat Method's namesake seal - the tie from the foundations "
            "returns as the hook, fully signed. Two hands witnessed one "
            "wrist in the two-on-one; now the figure-four is the formal "
            "reading of that witness, and the shoulder's rotation is the "
            "paper folding itself. The tap is the opponent co-signing."
        ),
    },
    {
        "key": "americana",
        "name": "The Key Lock (Americana)",
        "group": "Hooks and Submissions",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The key lock (americana) attacks the shoulder by pinning the "
            "opponent's arm to the mat and rotating the forearm upward: "
            "from side control or mount, the wrestler traps the near arm, "
            "threads his arm under it, grips his own wrist in a figure-"
            "four, and paints the opponent's hand toward their own head. "
            "The shoulder is the fulcrum and the pinned elbow is the "
            "anchor - the rotation has nowhere to go but into the joint. "
            "It is the mirror of the double wrist lock: where the double "
            "wrist lock takes the arm behind the back, the key lock pins "
            "it to the floor and turns it there. The two are drilled as a "
            "pair because the defense to one feeds the other - the "
            "opponent who straightens the arm to escape the key lock "
            "offers the arm bar, and the one who bends it to escape the "
            "arm bar offers the key lock."
        ),
        "how_it_works": (
            "Step 1: from side control, isolate the near arm and pin it "
            "to the mat beside the opponent's head. Step 2: thread your "
            "near arm under their arm, above the elbow. Step 3: grip your "
            "own wrist with your other hand to complete the figure-four. "
            "Step 4: keep their elbow pinned to the mat - the elbow is "
            "the anchor, and a lifting elbow is an escaping elbow. Step "
            "5: rotate their hand toward their head with smooth pressure, "
            "keeping your chest heavy on their arm. Step 6: if they "
            "straighten the arm to defend, follow into the straight arm "
            "bar; if they bridge, settle the weight and keep the elbow "
            "pinned. Step 7: release on the tap; drill the key lock to "
            "arm-bar switch as the standard combination."
        ),
        "key_points": [
            "The elbow pinned to the mat is the anchor - every escape starts with the elbow lifting, so it never lifts.",
            "The finish paints their hand toward their head with smooth, chest-heavy pressure.",
            "The key lock and the arm bar are a drilled pair: straightening defends one and offers the other.",
            "Isolate the arm from the body before the figure-four goes on; a connected arm is a defended arm.",
            "Chest stays heavy on the trapped arm through the whole rotation - lightness is escape.",
        ],
        "requirements": [
            SUPERVISION,
            TAP_EARLY,
            NECK_LEG,
            "Smooth pressure only - no cranking against a bridged opponent.",
            "A partner who taps to shoulder rotation early.",
        ],
        "standards": [
            "Elbow verified pinned to the mat before rotation begins; rotation with a floating elbow is corrected.",
            "Drill includes the key lock to arm-bar switch as the standard combination.",
        ],
        "citations": [CIT_SHANNON, CIT_LINEAGE, CIT_USAW],
        "sig_lens": (
            "The Signature read: the key lock is the mirror seal to the "
            "double wrist lock - the same figure-four, the same shoulder, "
            "but signed to the floor instead of the back. The Signature "
            "Combat Method drills them as a pair of witnesses: the "
            "opponent's defense testifies for one lock or the other, and "
            "the wrestler simply reads whichever testimony is offered."
        ),
    },
    {
        "key": "toe_hold",
        "name": "The Figure-Four Toe Hold",
        "group": "Hooks and Submissions",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The figure-four toe hold is the classic catch wrestling leg "
            "lock: the attacker controls the opponent's foot, threads his "
            "arms in a figure-four around the leg, and rotates the foot to "
            "attack the ankle. It is the lower-body mirror of the double "
            "wrist lock - the same figure-four arithmetic applied to the "
            "foot instead of the hand. The grip goes: one hand on the "
            "toes, the other arm threaded through to grip the own wrist, "
            "with the attacker's body positioned to the outside of the leg "
            "so the rotation torques the ankle. Old catch wrestlers "
            "considered the toe hold a fundamental rather than an "
            "advanced technique - it was taught early because leg locks "
            "were simply part of the game. The tap comes from ankle "
            "rotation, so control of the leg above the ankle is what "
            "makes the lock honest; without leg control the foot just "
            "spins free."
        ),
        "how_it_works": (
            "Step 1: control the leg - trap it between your legs or under "
            "your arm so the knee cannot turn freely. Step 2: grip the "
            "toes/forefoot with one hand, fingers wrapped. Step 3: thread "
            "your other arm under their leg and grip your own wrist, "
            "forming the figure-four around the leg. Step 4: position your "
            "body to the outside of their leg so the rotation has a "
            "direction to go. Step 5: rotate the foot inward/outward with "
            "smooth pressure from the arms and body - the ankle rotation, "
            "not yanking the toes, makes the tap. Step 6: keep the leg "
            "controlled above the ankle throughout; if the knee turns, "
            "reset the leg control before continuing. Step 7: release on "
            "the tap; drill entries from the leg-ride and from scrambles "
            "with the leg control as the scored element."
        ),
        "key_points": [
            "Leg control above the ankle is the lock - without it the foot spins free and there is no technique.",
            "The figure-four around the leg mirrors the double wrist lock: same arithmetic, lower body.",
            "Body positioned to the outside gives the rotation its direction; square-on is weak.",
            "The tap comes from ankle rotation applied smoothly, never from yanking the toes.",
            "Entries are drilled from the leg-ride and scrambles with leg control as the scored element.",
        ],
        "requirements": [
            SUPERVISION,
            TAP_EARLY,
            NECK_LEG,
            "Leg control established before any rotation - rotation on a loose leg is a reset.",
            "A partner who taps early to ankle pressure.",
        ],
        "standards": [
            "Leg trapped (between legs or under arm) with the knee controlled before the figure-four is applied.",
            "Rotation is smooth and steady; any yanking of the toes fails the rep.",
        ],
        "citations": [CIT_SHANNON, CIT_LINEAGE, CIT_BURNS],
        "sig_lens": (
            "The Signature read: the toe hold is the Signature Combat "
            "Method's lower seal - the figure-four that signed the wrist "
            "now signs the foot. Where public instruction sometimes "
            "treats leg locks as advanced, the Signature lens treats them "
            "as foundational: the oath of leverage does not change from "
            "arm to leg, only the limb that signs it."
        ),
    },
]

ENTRIES += [
    {
        "key": "ankle_lock",
        "name": "The Straight Ankle Lock (Achilles Hold)",
        "group": "Hooks and Submissions",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The straight ankle lock attacks the ankle and Achilles by "
            "trapping the opponent's leg, wedging the foot under the "
            "attacker's armpit, and bridging the hips while the forearm "
            "presses into the Achilles. It is the simplest honest leg "
            "lock: one leg, one wedge, one bridge. The mechanics are a "
            "lever - the attacker's forearm is the fulcrum on the "
            "Achilles, the armpit traps the foot as the load, and the hip "
            "bridge is the force. Catch wrestlers finished it from the "
            "leg-ride, from scrambles, and from the standing leg pickup. "
            "The leg must be controlled at the knee and the foot wedged "
            "deep in the armpit before the bridge begins; a shallow wedge "
            "slips and a loose knee turns the lock into a scramble. The "
            "tap comes from Achilles compression, applied by bridging the "
            "hips - never by falling backward with the body weight."
        ),
        "how_it_works": (
            "Step 1: trap the leg - control it at the knee with your legs "
            "or arms so it cannot turn. Step 2: wedge the foot deep under "
            "your armpit, toes up, with your forearm across the Achilles "
            "tendon. Step 3: grip your own hands together (or grip the "
            "thigh) to lock the wedge - the foot must not slide. Step 4: "
            "fall your weight slightly to the side of the trapped leg and "
            "bridge the hips upward - the hip bridge, not a backward "
            "fall, applies the pressure. Step 5: keep the trapped knee "
            "controlled throughout; if it turns, stop and re-trap. Step "
            "6: the forearm stays on the Achilles with steady pressure - "
            "the compression builds, it is not a strike. Step 7: release "
            "on the tap; drill the wedge depth as the scored element, "
            "since depth is the whole lock."
        ),
        "key_points": [
            "The wedge is the lock: foot deep in the armpit, forearm on the Achilles, hands locked before any pressure.",
            "The hip bridge applies the pressure - falling backward with body weight is not the technique.",
            "Knee control is non-negotiable; a turning knee turns the lock into a scramble.",
            "The lever is honest: forearm fulcrum on the Achilles, foot trapped as the load, hips as the force.",
            "Wedge depth is drilled as the scored element because depth is the whole lock.",
        ],
        "requirements": [
            SUPERVISION,
            TAP_EARLY,
            NECK_LEG,
            "The bridge is applied with steady hip pressure - no sudden backward falls.",
            "A partner who taps early to Achilles compression.",
        ],
        "standards": [
            "Foot wedged deep under the armpit with the forearm on the Achilles verified before the bridge.",
            "Pressure applied by hip bridge only; backward-fall finishes are corrected.",
        ],
        "citations": [CIT_SHANNON, CIT_LINEAGE, CIT_BURNS],
        "sig_lens": (
            "The Signature read: the straight ankle lock is the Signature "
            "Combat Method's simplest sealed lever - one wedge, one "
            "bridge, one oath. The foot signs into the armpit, the "
            "forearm witnesses on the Achilles, and the hips press the "
            "seal. Public instruction calls it basic; the Signature lens "
            "calls it pure, because no technique in the database is more "
            "honest about what leverage is."
        ),
    },
    {
        "key": "arm_bar",
        "name": "The Straight Arm Bar from Top Position",
        "group": "Hooks and Submissions",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The straight arm bar attacks the elbow by trapping the "
            "opponent's arm straight and bridging the hips into the "
            "elbow joint: from the top, the wrestler isolates an arm, "
            "pins it across his hips or chest, and extends it until the "
            "elbow is the fulcrum. It is the third member of the arm-lock "
            "family drilled as a set - key lock for the bent arm, double "
            "wrist lock for the arm behind the back, arm bar for the "
            "straight arm. The entries come from the mount, from side "
            "control when the opponent pushes, and from the guard when "
            "the opponent posts. The arm must be isolated from the body "
            "and the thumb pointed up (or the pinky controlled) so the "
            "elbow cannot turn out; the finish is a hip bridge into the "
            "elbow, smooth and controlled. The arm bar is drilled with the "
            "key lock as a switching pair because the defenses feed each "
            "other."
        ),
        "how_it_works": (
            "Step 1: isolate the arm - from the top, separate it from the "
            "opponent's body and control the wrist. Step 2: pin the arm "
            "across your hips with their thumb up, your legs controlling "
            "their head and body. Step 3: keep the arm straight and tight "
            "to your chest - a bent elbow is a key lock, not an arm bar, "
            "and the switch is the drill. Step 4: bridge the hips up into "
            "the elbow with smooth, steady pressure. Step 5: control their "
            "posture with your legs so they cannot stack and relieve the "
            "pressure. Step 6: if they bend the arm to defend, follow "
            "into the key lock; if they pull the arm free, take the "
            "double wrist lock on the retreat. Step 7: release on the tap; "
            "drill the arm bar to key lock switch as the standard pair."
        ),
        "key_points": [
            "Isolate the arm from the body first - a connected arm is a defended arm.",
            "Thumb up and arm tight to the chest keeps the elbow from turning out of the lock.",
            "The finish is a smooth hip bridge into the elbow, never a yank on the wrist.",
            "The arm bar and key lock are a switching pair: bent defends one and offers the other.",
            "Legs control the posture through the finish so the stack defense never relieves the pressure.",
        ],
        "requirements": [
            SUPERVISION,
            TAP_EARLY,
            NECK_LEG,
            "Smooth hip-bridge pressure only - pulling the wrist is an immediate correction.",
            "A partner who taps early to elbow pressure.",
        ],
        "standards": [
            "Arm isolated and pinned across the hips with the thumb up before the bridge begins.",
            "Drill includes the arm bar to key lock switch as the standard combination.",
        ],
        "citations": [CIT_SHANNON, CIT_LINEAGE, CIT_USAW],
        "sig_lens": (
            "The Signature read: the arm bar is the Signature Combat "
            "Method's straight-edge seal - the lock with no bend in it, "
            "signed across the hips. Where the key lock pins the bent arm "
            "to the floor and the double wrist lock folds it behind the "
            "back, the arm bar writes the elbow's limit in a straight "
            "line. The switching pair is the Method's honesty: every "
            "defense is just the next signature."
        ),
    },
    {
        "key": "guillotine",
        "name": "The Guillotine from the Front Headlock",
        "group": "Hooks and Submissions",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The guillotine is the front headlock grown into a choke: the "
            "wrestler's forearm wraps under the opponent's chin, the hand "
            "grips the own wrist or chest, and the body drops or arches to "
            "close the hold. It is the highest-percentage submission from "
            "the front headlock because the entry is the position "
            "wrestlers already live in - every snap-down and every sprawl "
            "offers it. The mechanics close the forearm against the "
            "throat: the wrapping arm's wrist sits under the chin, the "
            "gripping hand pulls to the chest, and the hips drop or the "
            "back arches to tighten. The arm-in variation (with the "
            "opponent's arm trapped inside) and the high-elbow finish are "
            "the two refinements drilled once the basic close is clean. "
            "The guillotine is practiced with the go-behind as the paired "
            "exit from the front headlock - the opponent who defends the "
            "choke by posture gives the back."
        ),
        "how_it_works": (
            "Step 1: from the front headlock, slide the strapping forearm "
            "deeper so the wrist sits under the chin. Step 2: grip your "
            "own wrist or pull the hand to your chest, closing the loop. "
            "Step 3: drop the hips and arch the back slightly to close "
            "the forearm against the throat - the closure comes from the "
            "body, not from squeezing the arms. Step 4: keep the "
            "opponent's head controlled low; a head that rises is a head "
            "escaping. Step 5: for the arm-in variation, trap their arm "
            "inside the loop before closing. Step 6: if they posture up "
            "hard to defend, follow the motion and take the go-behind - "
            "the choke and the back-take are the paired exits. Step 7: "
            "release on the tap; drill the close as a body motion (hips "
            "drop, back arch) rather than an arm squeeze."
        ),
        "key_points": [
            "The wrist sits under the chin and the hand closes to the chest - depth of the wrap decides the choke.",
            "The body closes the hold (hips drop, back arches); the arms only hold the shape.",
            "Keep the head low through the finish - a rising head is an escaping head.",
            "The guillotine and the go-behind are paired exits from the front headlock; the defense to one offers the other.",
            "Drill the close as a body motion, never as an arm squeeze - squeezing is fatigue, closing is technique.",
        ],
        "requirements": [
            SUPERVISION,
            TAP_EARLY,
            NECK_LEG,
            "The wrap goes under the chin - direct throat crushing without the wrap is a reset.",
            "A partner who taps early to choke pressure.",
        ],
        "standards": [
            "Wrist under the chin with the hand closed to the chest verified before the body closes.",
            "Drill pairs the guillotine with the go-behind from the same front headlock entry.",
        ],
        "citations": [CIT_SHANNON, CIT_LINEAGE, CIT_USAW],
        "sig_lens": (
            "The Signature read: the guillotine is the front headlock "
            "signing its own name - the chin strap that was a control "
            "becomes a seal. The Signature Combat Method treats the deep "
            "wrap as the headlock's true signature: the wrist witnesses "
            "under the chin, the body presses the seal, and the paired "
            "go-behind stands ready as the second witness if the first "
            "seal is refused."
        ),
    },
    {
        "key": "single_leg",
        "name": "The Single-Leg Dump and Trip Finish",
        "group": "Takedowns and Throws",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The single leg attacks one leg: the wrestler secures the leg "
            "at the knee and thigh, keeps the head tight to the hip, and "
            "finishes by dumping the opponent over the trapped leg or "
            "tripping the free leg. It is the chain wrestler's takedown - "
            "when the double leg meets the sprawl, the single leg is "
            "already there. The dump finish lifts and turns the opponent "
            "over the captured leg; the trip finish hooks the free leg "
            "while driving; the run-the-pipe finish changes direction and "
            "runs the leg across. The head position is the whole "
            "technique: head tight to the hip, ear on the thigh, never "
            "dangling outside where the guillotine or the crossface "
            "waits. Catch wrestlers finish the single leg straight into "
            "the ride - the dump lands the opponent broken down, and the "
            "ride grips are taken before the landing settles."
        ),
        "how_it_works": (
            "Step 1: penetrate to the leg - head to the hip, arms wrapping "
            "the knee and thigh together. Step 2: keep the head tight, "
            "ear on the thigh, and the captured leg's knee controlled. "
            "Step 3: for the dump, lift the leg and turn the opponent "
            "over it, stepping the free foot across. Step 4: for the "
            "trip, hook the free leg with your foot while driving "
            "forward through the captured leg. Step 5: for run-the-pipe, "
            "change direction sharply and run the captured leg across "
            "your body. Step 6: follow the finish to the mat, taking the "
            "tight waist or half nelson as they land. Step 7: drill the "
            "double-leg-to-single-leg chain as one motion, since the "
            "single is most often the second shot, not the first."
        ),
        "key_points": [
            "Head tight to the hip with the ear on the thigh - head position is the whole technique.",
            "The captured leg is controlled at knee and thigh; a loose leg is a lost leg.",
            "Three honest finishes - dump, trip, run-the-pipe - drilled as one family, not three solos.",
            "The finish lands straight into the ride grips; the takedown is not over until the ride is on.",
            "The single leg is the chain's second shot - drill it off the double-leg entry, not from a standstill.",
        ],
        "requirements": [
            SUPERVISION,
            "Mat space for the drive and the directional changes.",
            TAP_EARLY,
            "A partner who defends with whizzers and hops at realistic speed.",
            CONDITION,
        ],
        "standards": [
            "Head verified tight to the hip with the ear on the thigh before any finish is attempted.",
            "Each finish lands with ride grips taken before the reset.",
        ],
        "citations": [CIT_USAW, CIT_BURNS, CIT_SHANNON],
        "sig_lens": (
            "The Signature read: the single leg is the Signature Combat "
            "Method's second signature - the shot that signs after the "
            "first is refused. The head seals to the hip, the leg is "
            "witnessed at knee and thigh, and the three finishes are "
            "three ways of writing the same ending. The chain is the "
            "Method's creed: no shot stands alone."
        ),
    },
    {
        "key": "fireman",
        "name": "The Firemans Carry",
        "group": "Takedowns and Throws",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The fireman's carry is the spectacular shoulder throw of "
            "wrestling: the wrestler drops under the opponent's arm, takes "
            "the far thigh, and carries the opponent across the shoulders "
            "before dumping them to the mat. It is a timing throw - it "
            "works when the opponent pushes forward or reaches, and the "
            "wrestler changes levels underneath the pressure. The entry "
            "threads the head under the opponent's near arm while the "
            "hands take the far leg; the lift comes from the legs "
            "standing up with the opponent draped across the shoulders; "
            "the finish dumps to the side with control. Old catch "
            "wrestlers loved the fireman's carry because it turned the "
            "opponent's aggression into the throw - the harder they "
            "pushed, the higher they flew. Drill the entry slowly until "
            "the head threads cleanly, because a mistimed fireman's carry "
            "offers the back."
        ),
        "how_it_works": (
            "Step 1: as the opponent pushes or reaches, change levels and "
            "thread your head under their near arm. Step 2: the near hand "
            "takes their far thigh while the far hand controls their near "
            "arm or waist. Step 3: drop your hips below theirs - the "
            "throw needs you underneath, not beside. Step 4: stand up "
            "with the legs, draping the opponent across your shoulders. "
            "Step 5: dump to the side with control, keeping the far-leg "
            "grip through the landing. Step 6: follow to the mat into "
            "side control or the ride. Step 7: drill the timing entry "
            "against a partner who pushes forward on a signal, adding "
            "speed only when the head threads cleanly every time."
        ),
        "key_points": [
            "The fireman's carry is a timing throw - it answers forward pressure, it does not create it.",
            "The head threads under the near arm while the hips drop below theirs; underneath is the whole position.",
            "The legs do the lifting - standing up with the opponent draped, not pulling with the arms.",
            "Keep the far-leg grip through the dump so the landing goes straight into control.",
            "A mistimed entry offers the back, so the thread is drilled slowly until it is clean.",
        ],
        "requirements": [
            SUPERVISION,
            "A partner who pushes forward on signal at increasing realism.",
            TAP_EARLY,
            "Mat space for the lift and the controlled dump.",
            "The dump is controlled - no throwing the partner without the landing grip.",
        ],
        "standards": [
            "Head threads under the near arm with the hips below the partner's hips before the lift.",
            "Landing finishes with the far-leg grip held and control taken before the reset.",
        ],
        "citations": [CIT_BURNS, CIT_SHANNON, CIT_USAW],
        "sig_lens": (
            "The Signature read: the fireman's carry is the Signature "
            "Combat Method's borrowed signature - the opponent's push "
            "becomes the pen that writes his own flight. The wrestler "
            "only provides the paper (the shoulders) and the timing (the "
            "thread); the opponent's aggression does the writing. "
            "Public wrestling calls it spectacular; the Signature lens "
            "calls it efficient, because the thrower barely lifts."
        ),
    },
    {
        "key": "hip_throw",
        "name": "Hip Throws and the Head-and-Arm Throw",
        "group": "Takedowns and Throws",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Hip throws load the opponent onto the hip and rotate them "
            "over: the wrestler gets the hips below the opponent's hips, "
            "loads the body across, and turns. The head-and-arm throw is "
            "the family's most famous member - the wrestler controls the "
            "head and arm together, steps across, and throws over the "
            "hip. These are commitment throws: once the hips are in, the "
            "throw must finish, because a stalled hip throw offers the "
            "back. The keys are hip position (below theirs), the load "
            "(their weight settled onto your hip, not held in the arms), "
            "and the turn (the hips rotate, the arms guide). Catch "
            "wrestlers used hip throws as counters to forward pressure "
            "and as setups from the over-under tie. The landing is "
            "followed chest-to-chest into the ride - the throw is the "
            "entry, the pin is the point."
        ),
        "how_it_works": (
            "Step 1: from the tie, control the head and arm together (for "
            "the head-and-arm) or the waist and arm (for the hip throw). "
            "Step 2: step across so your hips are below their hips and "
            "your back is to their chest. Step 3: load - settle their "
            "weight onto your hip by bending the knees, not by pulling "
            "with the arms. Step 4: rotate the hips sharply, guiding with "
            "the head-and-arm grip, throwing them over the hip. Step 5: "
            "keep the grip through the landing and follow chest-to-chest. "
            "Step 6: take the ride grips (tight waist, half nelson) as "
            "they land. Step 7: drill the load separately - partner "
            "draped, knees bend, weight settled - before adding the "
            "rotation, since the load is the throw."
        ),
        "key_points": [
            "Hips below their hips before anything else - the throw is impossible from above.",
            "The load settles their weight onto your hip by bending the knees; the arms guide, they do not lift.",
            "Commitment is the technique: once the hips are in, the rotation must finish.",
            "The grip stays through the landing so the throw flows into the ride.",
            "The load is drilled separately first, because the load is the throw and the turn is just the finish.",
        ],
        "requirements": [
            SUPERVISION,
            "A partner who goes with the throw and lands safely.",
            TAP_EARLY,
            "Mat space for the rotation and landing.",
            "Controlled landings - the partner is guided down, never launched.",
        ],
        "standards": [
            "Hips verified below the partner's hips with the weight loaded (not arm-held) before rotation.",
            "Landing followed chest-to-chest with ride grips taken before the reset.",
        ],
        "citations": [CIT_HACK, CIT_BURNS, CIT_SHANNON],
        "sig_lens": (
            "The Signature read: the hip throw is the Signature Combat "
            "Method's pivot seal - the whole body becomes the stamp. The "
            "hips sign below, the load is the ink settling, and the "
            "rotation presses the opponent's back toward the mat like a "
            "seal toward wax. Public instruction teaches a throw; the "
            "Signature lens teaches a signature written with the entire "
            "body at once."
        ),
    },
    {
        "key": "cradle_near",
        "name": "The Near-Side Cradle",
        "group": "Pinning Combinations",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The near-side cradle locks the opponent's head and near knee "
            "together: the wrestler wraps one arm around the head and the "
            "other around the near leg, locks the hands, and rocks the "
            "opponent onto their shoulders. It is one of the "
            "highest-percentage pins in wrestling because the lock attacks "
            "both ends of the body at once - the folded position leaves "
            "no base to bridge from. The entries come from the ride (as "
            "they build up), from the half nelson chain (as they turn in), "
            "and from scrambles where the head and knee come close. The "
            "lock must be tight before the rock begins: head and knee "
            "drawn together, hands locked, chest heavy. Once locked, the "
            "wrestler rocks back, putting the shoulders to the mat, and "
            "holds the lock while the pin is counted. Fifty cradles per "
            "side makes the lock reflexive."
        ),
        "how_it_works": (
            "Step 1: from the ride, as the opponent builds up, wrap the "
            "near arm around their head. Step 2: wrap the far arm around "
            "their near knee, drawing knee and head together. Step 3: "
            "lock the hands - palm to palm or wrist grip - with the lock "
            "tight before any rocking. Step 4: chest goes heavy on their "
            "chest as the lock cinches. Step 5: rock back, sitting "
            "through, putting their shoulders to the mat. Step 6: keep "
            "the lock tight and the weight settled while the pin is "
            "secured - do not release to celebrate early. Step 7: drill "
            "the lock (head to knee, hands locked) as the scored element, "
            "since the rock without the lock is just a roll."
        ),
        "key_points": [
            "Head and knee drawn together with the hands locked - the lock is the pin, the rock is just the delivery.",
            "The lock must be tight before the rock begins; rocking a loose cradle is just rolling around.",
            "Chest heavy through the cinch keeps the opponent folded while the lock is secured.",
            "Rock back and sit through to put the shoulders down - the pin is held, not wished for.",
            "The cradle is the half nelson's chained partner: turn in to fight the nelson and the cradle is waiting.",
        ],
        "requirements": [
            SUPERVISION,
            "The lock is cinched with steady pressure - no yanking the head toward the knee.",
            TAP_EARLY,
            NECK_LEG,
            "A partner who fights the lock realistically so the entries can be drilled.",
            CONDITION,
        ],
        "standards": [
            "Hands locked with head and knee drawn together, verified before the rock begins.",
            "Pin held with the lock tight and weight settled; early release fails the rep.",
        ],
        "citations": [CIT_USAW, CIT_BURNS, CIT_SHANNON],
        "sig_lens": (
            "The Signature read: the cradle is the Signature Combat "
            "Method's folding seal - the document folded until head meets "
            "knee and the hands lock the crease. Where the half nelson "
            "turns the page, the cradle folds it: both ends witnessed "
            "together, the rock the press, and the pin the flat, final, "
            "unfoldable seal."
        ),
    },
    {
        "key": "cradle_far",
        "name": "The Far-Side and Inside-Out Cradles",
        "group": "Pinning Combinations",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The far-side cradle locks the head with the far knee instead "
            "of the near: the wrestler reaches across to trap the far leg "
            "while controlling the head, folding the opponent the long "
            "way. The inside-out cradle starts from the opponent's "
            "defense - as they sit out or turn in against a near-side "
            "attempt, the wrestler switches the leg grip to the far side "
            "and completes the lock from the new angle. These are the "
            "cradle family's answers to defense: the near-side cradle is "
            "the first attempt, and the far-side and inside-out are what "
            "the attempt becomes when the opponent moves. The principle "
            "never changes - head and knee together, hands locked, rock "
            "to the shoulders - only the route to the lock changes. "
            "Drilling all three as one chain teaches the wrestler to "
            "follow the opponent's defense into the pin rather than "
            "restarting."
        ),
        "how_it_works": (
            "Step 1: for the far-side cradle, control the head and reach "
            "across to trap the far knee, drawing them together the long "
            "way. Step 2: lock the hands with the fold tight. Step 3: "
            "for the inside-out, start the near-side cradle; as the "
            "opponent sits out or turns in, switch the leg arm to the far "
            "knee without releasing the head. Step 4: re-lock the hands "
            "on the new angle and cinch. Step 5: rock to the shoulders "
            "with the chest heavy, as with the near-side. Step 6: hold "
            "the lock through the pin - the switch is not an excuse to "
            "loosen. Step 7: drill the chain - near-side attempt, "
            "defense, inside-out switch, pin - as one continuous motion."
        ),
        "key_points": [
            "The far-side cradle folds the long way: head to far knee, same lock principle, different route.",
            "The inside-out is a switch, not a restart - the head control never releases during the change.",
            "Defense is the setup: the opponent's sit-out or turn-in is what opens the far-side lock.",
            "Re-lock tight on the new angle before rocking; a switched but loose lock is no lock.",
            "All three cradles drill as one chain so the wrestler follows defense into the pin.",
        ],
        "requirements": [
            SUPERVISION,
            "Steady pressure on the lock - no yanking during the switch.",
            TAP_EARLY,
            NECK_LEG,
            "A partner who defends the near-side cradle realistically to open the switch.",
            CONDITION,
        ],
        "standards": [
            "Head control maintained through the entire switch; releasing the head fails the rep.",
            "Hands re-locked tight on the new angle before the rock begins.",
        ],
        "citations": [CIT_USAW, CIT_SHANNON, CIT_LINEAGE],
        "sig_lens": (
            "The Signature read: the far-side and inside-out cradles are "
            "the Signature Combat Method's proof that the seal follows "
            "the paper. The opponent's defense moves the document, and "
            "the wrestler's switch moves the seal with it - head never "
            "released, hands re-locked, the fold completed from the new "
            "angle. Public wrestling calls it a counter; the Signature "
            "lens calls it the same signature, rewritten where the "
            "opponent put the page."
        ),
    },
    {
        "key": "head_arm",
        "name": "The Head-and-Arm Choke (Arm Triangle)",
        "group": "Hooks and Submissions",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The head-and-arm choke traps the opponent's head and one arm "
            "together against the wrestler's side: the arm wraps the head, "
            "the opponent's own shoulder becomes the second side of the "
            "choke, and the wrestler's body closes the triangle. It is "
            "the submission version of the head-and-arm control that "
            "wrestlers already use for throws and pins - the same grip "
            "that throws can choke when the angle closes. The mechanics "
            "compress both sides of the neck: the wrapping arm on one "
            "side, their own trapped shoulder on the other. The finish "
            "walks the hips to the side and drops the weight, closing the "
            "triangle with the body rather than squeezing with the arm. "
            "Catch wrestlers prized it because it came from positions "
            "they already owned - the head-and-arm was home, and the "
            "choke was just home with the door closed."
        ),
        "how_it_works": (
            "Step 1: from the head-and-arm control (side or front), wrap "
            "the arm around the head with their arm trapped inside "
            "against your side. Step 2: lock the grip - hand to bicep or "
            "figure-four - so the trap cannot open. Step 3: walk your "
            "hips to the side of the trapped arm, closing the angle. Step "
            "4: drop your weight and drive your shoulder into the close - "
            "the body closes the triangle, the arm only holds the shape. "
            "Step 5: keep their trapped arm tight to your side; if it "
            "pulls out, the choke is gone. Step 6: adjust the angle by "
            "small hip steps until the pressure builds - the finish is "
            "found, not forced. Step 7: release on the tap; drill the "
            "angle-walk as the scored element, since angle is the choke."
        ),
        "key_points": [
            "Their own trapped shoulder is the second side of the choke - the technique uses the opponent's body against them.",
            "Walk the hips to the side to close the angle; the body closes the triangle, not the arm squeeze.",
            "The trapped arm must stay tight to your side - if it pulls out, there is no choke.",
            "Small hip steps find the finish; forcing a bad angle is how the position is lost.",
            "The same head-and-arm grip that throws and pins also chokes - one control, three endings.",
        ],
        "requirements": [
            SUPERVISION,
            TAP_EARLY,
            NECK_LEG,
            "The choke is closed with body angle and weight - no cranking the head.",
            "A partner who taps early to choke pressure.",
        ],
        "standards": [
            "Grip locked with the arm trapped tight to the side before the angle walk begins.",
            "Finish found by hip steps and weight drop; arm-squeeze finishes are corrected.",
        ],
        "citations": [CIT_SHANNON, CIT_LINEAGE, CIT_USAW],
        "sig_lens": (
            "The Signature read: the head-and-arm choke is the Signature "
            "Combat Method's closed-door seal - the grip that threw and "
            "pinned now signs the quiet ending. The opponent's own "
            "shoulder co-signs against him, the hips walk the angle like "
            "a pen finding the line, and the weight presses the final "
            "seal. One control, three endings, all already written."
        ),
    },
]

ENTRIES += [
    {
        "key": "can_opener",
        "name": "The Can Opener Neck Crank",
        "group": "Hooks and Submissions",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The can opener is catch wrestling's classic neck crank: from "
            "inside the opponent's guard or from the top, the wrestler "
            "cups the back of the head with both hands and drives it "
            "toward the chest, cranking the neck. It is a pain-compliance "
            "hold from the old days, when catch matches allowed it and "
            "the tap was the whole game. This record teaches it for "
            "historical completeness and for defense - the wrestler must "
            "know the can opener to recognize it and to counter it - with "
            "strict training limits: it is drilled as a control position "
            "with minimal pressure, never cranked in practice. The "
            "defense is posture: head up, back straight, hands fighting "
            "the grips before the crank starts. Modern sport rules "
            "restrict or ban neck cranks, so the can opener is taught as "
            "history, control, and defense, not as a competition "
            "technique."
        ),
        "how_it_works": (
            "Step 1: recognize the position - the opponent's hands cup "
            "the back of your head and begin driving it forward. Step 2: "
            "defense first - posture up immediately, head back, hands "
            "inside fighting their grips before the pressure builds. Step "
            "3: for the historical technique, both hands cup the back of "
            "the head with the fingers interlaced. Step 4: the elbows "
            "drive down and the hands pull the head toward the chest with "
            "steady, minimal pressure in drilling. Step 5: the top "
            "wrestler's weight stays back - leaning in adds dangerous "
            "force. Step 6: in practice the hold is shown as a control "
            "position only, and the partner taps at the first pressure. "
            "Step 7: drill the defense - posture, hand-fight, and "
            "escape - as the live element, since defense is the usable "
            "skill."
        ),
        "key_points": [
            "The can opener is taught for history, control, and defense - it is a restricted technique in modern sport rules.",
            "The defense is posture: head up and hands fighting the grips before the crank starts.",
            "In drilling it is a control position with minimal pressure, never cranked.",
            "Recognizing the grip early is the whole defense - late recognition is a lost position.",
            "The live drilled element is the escape, not the crank.",
        ],
        "requirements": [
            SUPERVISION,
            TAP_EARLY,
            NECK_LEG,
            "Minimal pressure only in drilling - the crank is demonstrated, never applied.",
            "The partner taps at the first pressure and the hold is released instantly.",
            "Knowledge of the local sport rules on neck cranks before any practice.",
        ],
        "standards": [
            "Drilling pressure is minimal and controlled; any full-force application fails the session.",
            "Defense (posture and grip-fighting) is drilled live; the crank itself is shown as control only.",
        ],
        "citations": [CIT_SHANNON, CIT_LINEAGE, CIT_BURNS],
        "sig_lens": (
            "The Signature read: the can opener is the Signature Combat "
            "Method's sealed archive - a technique kept for knowledge, "
            "not for use. The Method signs it as history: the grip "
            "witnessed, the defense authored, and the crank itself left "
            "unsigned. Where the old game allowed it, the Signature lens "
            "files it under control and recognition, because the oath of "
            "the Method is that both partners walk off the mat whole."
        ),
    },
    {
        "key": "banana_split",
        "name": "The Banana Split",
        "group": "Hooks and Submissions",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The banana split is the leg-ride submission: from the "
            "leg-ride position (legs grapevined or hooked inside the "
            "opponent's legs), the wrestler controls both of the "
            "opponent's legs and spreads them, attacking the hips and "
            "groin with the stretch. It is a control-and-submit from the "
            "ride - the top wrestler is already behind, the legs are "
            "already controlled, and the split is the finish the position "
            "was always offering. The mechanics are a spreading lever: "
            "each of the opponent's legs is controlled and the "
            "wrestler's body drives the spread with the hips. It is "
            "drilled with control and early taps, since the stretch "
            "attacks a sensitive area. The banana split teaches the "
            "leg-ride as an attacking position rather than a stalling "
            "one - from the grapevine, the top man is always one spread "
            "away from the finish."
        ),
        "how_it_works": (
            "Step 1: establish the leg-ride - hooks or grapevines inside "
            "the opponent's legs from behind, chest on their back. Step 2: "
            "control each of their legs: one with your legs, one with "
            "your hands at the ankle or knee. Step 3: keep your weight "
            "settled and your base wide so the ride cannot be shaken. "
            "Step 4: spread the legs with your body - drive the hips "
            "through while the controls hold each leg, stretching with "
            "steady pressure. Step 5: the spread comes from the hips and "
            "body, not from yanking the ankles with the arms. Step 6: "
            "maintain the ride structure through the finish - a broken "
            "ride is a lost split. Step 7: release on the tap; drill the "
            "leg control as the scored element, since control is the "
            "split."
        ),
        "key_points": [
            "The leg-ride is an attacking position: from the grapevine the top man is one spread from the finish.",
            "Each leg is controlled separately - one by the legs, one by the hands - before any spread begins.",
            "The spread comes from the hips and body driving through, not from yanking ankles.",
            "The ride structure stays intact through the finish; a broken ride is a lost split.",
            "Control is drilled as the scored element because control is the split.",
        ],
        "requirements": [
            SUPERVISION,
            TAP_EARLY,
            NECK_LEG,
            "Steady spreading pressure only - sudden yanks are an immediate stop.",
            "A partner who taps early to the stretch.",
            "The hold is released the instant the tap comes.",
        ],
        "standards": [
            "Both legs controlled (one by legs, one by hands) with the ride settled before the spread.",
            "Spread applied by steady hip/body pressure; arm-yank finishes are corrected.",
        ],
        "citations": [CIT_SHANNON, CIT_LINEAGE, CIT_USAW],
        "sig_lens": (
            "The Signature read: the banana split is the Signature Combat "
            "Method's spreading seal - the ride that was a watch becomes "
            "a verdict. Both legs witnessed separately, the hips press "
            "the spreading seal, and the opponent's own base testifies "
            "against him. Public wrestling sometimes treats the leg-ride "
            "as a rest; the Signature lens treats it as a signed threat "
            "that only waits for the spread."
        ),
    },
    {
        "key": "heel_hook",
        "name": "The Heel Hook",
        "group": "Advanced Hooks and Chains",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The heel hook is the most feared leg lock in grappling: the "
            "attacker traps the opponent's leg, cups the heel in the "
            "crook of the elbow, and rotates the foot to torque the knee. "
            "It attacks the knee ligaments rotationally, which is why it "
            "is taught only to experienced practitioners, drilled with "
            "extreme control, and finished with the earliest taps in the "
            "sport. Catch wrestling's old-timers used heel hooks as "
            "match-enders, and the modern game treats them with matching "
            "respect. The mechanics: the leg is controlled at the knee "
            "and hip so it cannot turn with the rotation, the heel is "
            "seated deep in the elbow crook, and the attacker's body "
            "rotates - the torque goes to the knee because the leg above "
            "it is locked. This record teaches recognition, control, "
            "defense, and the controlled application; the live finish is "
            "for advanced practitioners under direct supervision only."
        ),
        "how_it_works": (
            "Step 1: trap the leg - control it at the knee and hip so the "
            "leg cannot rotate with the foot. Step 2: cup the heel deep "
            "in the crook of your elbow, forearm across the Achilles. "
            "Step 3: lock your hands (grip your own wrist or bicep) so "
            "the heel cannot slip. Step 4: position your body to the "
            "outside, keeping their knee controlled and their hip pinned. "
            "Step 5: rotate with your whole body - the torque comes from "
            "body rotation, never from twisting the hands. Step 6: apply "
            "pressure gradually and release at the first tap or the first "
            "sign of resistance - the heel hook is caught, not cranked. "
            "Step 7: drill entries and leg control as the live elements; "
            "the finish is demonstrated with minimal pressure under "
            "direct supervision."
        ),
        "key_points": [
            "The heel hook torques the knee rotationally - it is taught only to experienced practitioners with extreme control.",
            "Leg control at the knee and hip is the lock; without it there is no technique, only danger.",
            "The heel seats deep in the elbow crook with the hands locked - depth and the lock are the whole hold.",
            "The rotation comes from the whole body, never from twisting the hands.",
            "It is caught, not cranked: gradual pressure, earliest taps, instant release.",
        ],
        "requirements": [
            "Advanced practitioners only, under direct qualified supervision.",
            TAP_EARLY,
            NECK_LEG,
            "Gradual pressure with instant release - cranking is an immediate stop to the session.",
            "A partner who taps at the first sign of pressure, before any pain.",
            "Knowledge of the local sport rules on heel hooks before any practice.",
        ],
        "standards": [
            "Leg controlled at knee and hip with the heel deep in the elbow crook before any rotation.",
            "Finish demonstrated with minimal pressure; entries and leg control are the live drilled elements.",
        ],
        "citations": [CIT_SHANNON, CIT_LINEAGE, CIT_BURNS],
        "sig_lens": (
            "The Signature read: the heel hook is the Signature Combat "
            "Method's most solemn seal - the one signed only by advanced "
            "hands, witnessed slowly, and released at the first whisper "
            "of the tap. The Method's oath is that both partners walk "
            "off whole, so this seal is taught as recognition and "
            "control first, finish last, and always under the direct eye "
            "of the coach. Power signed without restraint is not a "
            "signature - it is a tear in the document."
        ),
    },
    {
        "key": "japanese_necktie",
        "name": "The Japanese Necktie",
        "group": "Advanced Hooks and Chains",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The Japanese necktie is the front-headlock choke refined: "
            "from the front headlock, the wrestler threads the arm "
            "through so the forearm wraps the neck with the opponent's "
            "arm trapped, locks the grip, and drops the weight to close. "
            "It is tighter than the basic guillotine because the "
            "threading arm and the trapped arm form a closed loop - the "
            "neck is wrapped on both sides with no slack to posture out "
            "of. The entry comes from the snap-down, the sprawl rebound, "
            "or the failed shot, exactly like the guillotine, but the "
            "finish threads deeper: the choking arm goes under the chin "
            "and through, the hand grips the own lat or bicep, and the "
            "body drops to the side. It is an advanced technique because "
            "the threading must be clean - a sloppy thread is just a "
            "loose guillotine - and the finish requires the weight drop "
            "to be timed with the lock."
        ),
        "how_it_works": (
            "Step 1: from the front headlock, slide the choking arm deep "
            "so the forearm wraps under the chin. Step 2: thread the arm "
            "through, trapping their near arm inside the loop. Step 3: "
            "lock the grip - hand to your own bicep or lat - closing the "
            "loop with no slack. Step 4: drop your weight to the side of "
            "the trapped arm, closing the wrap with the body. Step 5: "
            "keep their head low and the loop closed through the drop - "
            "slack is escape. Step 6: adjust with small hip steps until "
            "the pressure builds; the finish is found, not forced. Step "
            "7: release on the tap; drill the thread (deep wrap, trapped "
            "arm, locked grip) as the scored element, since the thread is "
            "the choke."
        ),
        "key_points": [
            "The thread is the choke: deep wrap under the chin, their arm trapped, grip locked with no slack.",
            "The loop closes on both sides of the neck, which is why the necktie beats the posture defense.",
            "The body drops to close - weight and angle finish what the arms only shape.",
            "Keep the head low through the drop; slack anywhere is escape everywhere.",
            "The thread is drilled as the scored element because a sloppy thread is just a loose guillotine.",
        ],
        "requirements": [
            SUPERVISION,
            TAP_EARLY,
            NECK_LEG,
            "The wrap goes under the chin with the loop closed - no raw throat crushing.",
            "A partner who taps early to choke pressure.",
            "Clean threading before any weight drop - sloppy threads are reset.",
        ],
        "standards": [
            "Deep wrap with the arm trapped and the grip locked verified before the weight drop.",
            "Finish found by hip steps and weight; forced squeezes are corrected.",
        ],
        "citations": [CIT_SHANNON, CIT_LINEAGE, CIT_USAW],
        "sig_lens": (
            "The Signature read: the Japanese necktie is the guillotine's "
            "signature rewritten with a finer pen. The thread is the "
            "careful handwriting - deep wrap, trapped arm, locked grip - "
            "and the weight drop is the press that sets the ink. Where "
            "the basic choke is a bold signature, the necktie is "
            "calligraphy: same name, finer lines, no room for the "
            "opponent to slip a finger between the letters."
        ),
    },
    {
        "key": "power_half",
        "name": "The Power Half Nelson and Leg-Ride Chains",
        "group": "Advanced Hooks and Chains",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The power half nelson is the half nelson with the legs "
            "joined to the attack: from the leg-ride (grapevine or hooks "
            "in), the wrestler threads the half nelson while the legs "
            "control the opponent's base, and the turn uses the whole "
            "body - legs spreading or lifting, arm levering, chest "
            "driving. It is one of the most devastating turns in "
            "wrestling because the opponent is attacked at both ends at "
            "once with no base left to defend from. The leg-ride chains "
            "extend it: grapevine to power half, hooks to banana split, "
            "leg-ride to toe hold - the legs never stop working while the "
            "upper body turns and locks. This is advanced because the "
            "coordination is total: the legs, the arm, and the chest must "
            "fire as one motion, and the ride must stay settled through "
            "the turn."
        ),
        "how_it_works": (
            "Step 1: establish the leg-ride - grapevines or hooks inside "
            "their legs, chest on their back, base wide. Step 2: thread "
            "the half nelson with the near arm, locking the hand on the "
            "back of the neck. Step 3: keep the legs active - grapevines "
            "spreading or hooks lifting - so their base stays broken. "
            "Step 4: drive the turn with everything at once: legs, arm "
            "lever, and chest driving across. Step 5: follow the turn to "
            "chest-on-chest, keeping a leg hook through the finish so "
            "they cannot re-base. Step 6: chain - if they fight the turn, "
            "the legs switch to the banana split; if they expose a foot, "
            "the toe hold is there. Step 7: drill the coordination slowly "
            "- legs, arm, chest as one motion - before adding speed, "
            "since the chain is only as strong as its timing."
        ),
        "key_points": [
            "Both ends attacked at once with no base left - that is what makes the power half devastating.",
            "The legs never stop working: grapevines spreading or hooks lifting while the arm levers.",
            "Legs, arm, and chest fire as one motion; the chain is timing, not strength.",
            "Keep a leg hook through the finish so the opponent cannot re-base mid-turn.",
            "The chains are the technique: power half, banana split, toe hold - one ride, three endings.",
        ],
        "requirements": [
            SUPERVISION,
            "The half nelson lock on the back of the neck - never a head crank.",
            TAP_EARLY,
            NECK_LEG,
            "A partner who fights the turn realistically so the chains can be drilled.",
            CONDITION,
        ],
        "standards": [
            "Leg-ride settled with the half nelson locked before the combined drive begins.",
            "Drill runs the full chain - power half, banana split switch, toe hold option - as one ride.",
        ],
        "citations": [CIT_USAW, CIT_SHANNON, CIT_LINEAGE],
        "sig_lens": (
            "The Signature read: the power half is the Signature Combat "
            "Method's full-body signature - legs, arm, and chest signing "
            "at once. Where the basic half nelson was one arm's oath, "
            "the power half is the whole body testifying: the legs "
            "witness the base broken, the arm witnesses the turn, the "
            "chest presses the seal. The chains are the Method's creed "
            "written large - one ride, three endings, no wasted motion."
        ),
    },
    {
        "key": "scarf_armbar",
        "name": "The Scarf-Hold Arm Bar",
        "group": "Advanced Hooks and Chains",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The scarf-hold arm bar attacks the far arm from the scarf "
            "hold (kesa-gatame): the wrestler holds the opponent's head "
            "and near arm tight to the chest, and when the opponent "
            "reaches or pushes with the far arm, the wrestler traps it, "
            "swings the legs over, and finishes the straight arm bar. It "
            "is a transition submission - the scarf hold is the pinning "
            "position, and the arm bar is what the position becomes when "
            "the far arm moves. The keys are the scarf hold itself (head "
            "and arm crushed tight, hips heavy, no space) and the swing: "
            "the legs swing over the head in one motion while the trapped "
            "arm is pinned to the chest. It is advanced because the "
            "transition window is short - the far arm is only available "
            "for a moment - and the swing must land with the arm already "
            "isolated."
        ),
        "how_it_works": (
            "Step 1: establish the scarf hold - their head and near arm "
            "tight to your chest, your hips heavy, no space. Step 2: "
            "watch the far arm; when it reaches or pushes, trap it "
            "against your chest with your near arm. Step 3: in one "
            "motion, swing your legs over their head, keeping the "
            "trapped arm pinned to your chest. Step 4: land with their "
            "arm across your hips, thumb up, legs controlling their head "
            "and body. Step 5: bridge the hips into the elbow with smooth "
            "pressure. Step 6: if they pull the arm free mid-swing, "
            "follow into the double wrist lock on the retreat. Step 7: "
            "release on the tap; drill the swing as one motion, since "
            "the window is short and hesitation loses the arm."
        ),
        "key_points": [
            "The scarf hold must be airtight first - space in the hold is space for the far arm to escape.",
            "The far arm is only available for a moment; the trap and the swing are one motion, not two.",
            "The trapped arm stays pinned to the chest through the swing - the isolation travels with you.",
            "Land with the arm across the hips, thumb up, before the bridge begins.",
            "The missed swing has a follow-up: the double wrist lock on the retreating arm.",
        ],
        "requirements": [
            SUPERVISION,
            TAP_EARLY,
            NECK_LEG,
            "The swing is controlled - no flinging the legs over a resisting partner.",
            "A partner who reaches with the far arm realistically to open the window.",
            "Smooth bridge pressure only on the finish.",
        ],
        "standards": [
            "Scarf hold verified airtight (head and arm tight, hips heavy) before the transition is drilled.",
            "Trap and swing executed as one motion; two-step attempts are corrected.",
        ],
        "citations": [CIT_SHANNON, CIT_LINEAGE, CIT_USAW],
        "sig_lens": (
            "The Signature read: the scarf-hold arm bar is the Signature "
            "Combat Method's turning seal - the pinning hold that becomes "
            "a lock in a single motion. The scarf hold is the signed "
            "page; the far arm's reach is the opponent adding a line the "
            "wrestler did not ask for; the swing is the Method striking "
            "that line and writing the arm bar over it. One motion, no "
            "hesitation, the window sealed shut."
        ),
    },
    {
        "key": "hook_chains",
        "name": "Submission Chains: Linking Hooks into Combinations",
        "group": "Advanced Hooks and Chains",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Submission chains are catch wrestling's highest art: instead "
            "of attacking one lock, the wrestler attacks in combinations "
            "where each defense opens the next lock. The double wrist lock "
            "becomes the arm bar when the arm straightens; the arm bar "
            "becomes the key lock when it bends; the key lock becomes the "
            "double wrist lock when they turn. On the legs, the ankle lock "
            "becomes the heel hook when the leg turns, and the toe hold "
            "follows the foot wherever it goes. The principle is that the "
            "opponent has only so many defenses, and each defense is a "
            "movement the wrestler has already rehearsed - the chain does "
            "not chase the opponent, it waits where the defense is going. "
            "Chains are drilled as flows: three locks minimum per chain, "
            "no stopping between them, the partner giving honest defenses "
            "so the transitions are real."
        ),
        "how_it_works": (
            "Step 1: start the first lock of the chain (for example, the "
            "double wrist lock) with full control. Step 2: as the partner "
            "defends honestly (turning, straightening, bridging), follow "
            "the defense - do not fight it. Step 3: the defense names the "
            "next lock: straightening arm to arm bar, bending arm to key "
            "lock, turning body to double wrist lock re-attack. Step 4: "
            "transition without releasing control - the hands move from "
            "lock to lock while the body stays heavy. Step 5: each lock "
            "in the chain is applied with real (controlled) finishing "
            "pressure so the defense is honest. Step 6: minimum three "
            "locks per chain rep, no pauses between them. Step 7: drill "
            "both the arm chain and the leg chain as flows, with the "
            "partner's defenses getting sharper as the chain gets "
            "smoother."
        ),
        "key_points": [
            "Each defense opens the next lock - the chain waits where the defense is going instead of chasing.",
            "The arm chain: double wrist lock to arm bar (straightens) to key lock (bends) to double wrist lock (turns).",
            "Transitions keep control: hands move lock to lock while the body stays heavy - no releases between links.",
            "Every lock gets real controlled finishing pressure so the partner's defense stays honest.",
            "Three locks minimum per rep with no pauses; the chain is a flow, not three separate techniques.",
        ],
        "requirements": [
            SUPERVISION,
            TAP_EARLY,
            NECK_LEG,
            "A partner giving honest, progressive defenses - the chain needs real reactions.",
            "Controlled finishing pressure on every link; the tap is respected instantly at each stage.",
            "Advanced practitioners for full-speed chains; beginners drill the transitions slowly.",
        ],
        "standards": [
            "Chain reps run three locks minimum with no pauses and no loss of control between links.",
            "Each link reaches controlled finishing pressure before the transition - skipped links fail the rep.",
        ],
        "citations": [CIT_SHANNON, CIT_LINEAGE, CIT_BURNS],
        "sig_lens": (
            "The Signature read: the submission chain is the Signature "
            "Combat Method's compound signature - not one seal but a "
            "document of seals, each defense notarized into the next "
            "lock. The wrestler does not chase; he has already signed "
            "every page the defense can turn to. Public instruction "
            "teaches locks; the Signature lens teaches the inevitability "
            "between them - the chain is the oath that no defense goes "
            "unanswered."
        ),
    },
    {
        "key": "flow",
        "name": "The Catch Chain: Ride, Hook, and Pin Flow",
        "group": "Advanced Hooks and Chains",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The catch chain is the whole art in one flow: from the "
            "takedown the wrestler takes the ride, from the ride works "
            "the turn, from the turn takes the hook, and from the hook "
            "secures the pin - or the tap, whichever the opponent offers "
            "first. It is the capstone record of this database because "
            "it contains every tier: the stance and ties of the "
            "foundations, the rides and locks of the compounded tier, and "
            "the chains of the advanced tier, all in one continuous "
            "motion. The chain is drilled as a full round: takedown to "
            "ride (sixty seconds of breakdowns), ride to turn (half "
            "nelson or cradle), turn to hook (the submission that the "
            "turn exposes), hook to pin (shoulders flat, lock held). The "
            "wrestler who can run the catch chain smoothly has the whole "
            "database in his body - not as thirty-four separate "
            "techniques, but as one art."
        ),
        "how_it_works": (
            "Step 1: open with the tie battle - win the hands (two "
            "minutes of hand fighting in drilling). Step 2: hit the "
            "takedown - snap-down to go-behind or the double leg with "
            "the hook finish. Step 3: establish the ride - tight waist "
            "and crossface, sixty seconds of breakdown cycles. Step 4: "
            "work the turn - half nelson, switching to the cradle when "
            "they turn in. Step 5: take the hook the turn exposes - "
            "double wrist lock, key lock, or arm bar from the control. "
            "Step 6: secure the finish - shoulders flat for the pin with "
            "the lock held, or the tap from the hook. Step 7: drill the "
            "full chain as a round with no stops between phases; the "
            "transitions are the technique, and a chain with pauses is "
            "not a chain."
        ),
        "key_points": [
            "The catch chain is the whole database in one flow: tie, takedown, ride, turn, hook, pin.",
            "Each phase feeds the next - the takedown lands in the ride, the ride opens the turn, the turn exposes the hook.",
            "The finish is whichever the opponent offers first: the pin or the tap are the same chain's two endings.",
            "Transitions are the technique: drill the full round with no stops between phases.",
            "Rank ten is not a new move - it is all thirty-three records moving as one art.",
        ],
        "requirements": [
            SUPERVISION,
            TAP_EARLY,
            NECK_LEG,
            CONDITION,
            "Full protective drilling progression - the chain is run at increasing intensity, never full on day one.",
            "A partner who wrestles honestly through every phase so the transitions are real.",
        ],
        "standards": [
            "Full chain drilled as a continuous round: tie, takedown, sixty-second ride, turn, hook, pin/tap.",
            "No stops between phases; pauses between phases fail the rep.",
        ],
        "citations": [CIT_SHANNON, CIT_LINEAGE, CIT_HACK, CIT_BURNS],
        "sig_lens": (
            "The Signature read: the catch chain is the Signature Combat "
            "Method's complete document - every oath of the ladder "
            "signed in order, from the stance's first covenant to the "
            "pin's final seal. The tie is the heading, the takedown the "
            "body, the ride the watch kept over it, the hook the seal "
            "pressed, the pin the flat final page. Thirty-four records, "
            "one art, one signature: the wrestler's."
        ),
    },
]

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
_ranks = [e["ladder_rank"] for e in ENTRIES]
assert _ranks == sorted(_ranks), "entries not in ladder order"
assert all(1 <= r <= 10 for r in _ranks)
_tiers = [e["ladder_tier"] for e in ENTRIES]
assert all(t in ("foundations", "compounded", "advanced") for t in _tiers)
