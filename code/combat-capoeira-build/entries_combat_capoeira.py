#!/usr/bin/env python3
"""Entries for the Capoeira Combat databases (combat batch 1, 2026-10-17).

Dedupe gate pre-check 2026-10-17: all 68 titles (34 public + 34
" (Signature Edition)") run through code/dedupe_gate.py against the whole
system before authoring: zero cross-database collisions.

Two NEW databases, 34 ladder-ordered records each:

  combat-capoeira            - The Capoeira Combat Database
                               (public-harvest: real, fact-checked
                               Brazilian capoeira knowledge - Angola and
                               Regional lineages: ginga, esquivas, kicks
                               (martelo, queixada, armada, rabo de arraia),
                               ground flow, and roda strategy - every record
                               a technique with HOW TO DO IT step-by-step
                               body mechanics; standard references Nestor
                               Capoeira The Little Capoeira Book rev. ed.
                               2002; Almeida B. Capoeira: A Brazilian Art
                               Form 1986; Assuncao M.R. Capoeira: The History
                               of an Afro-Brazilian Martial Art 2005;
                               Downey G. Learning Capoeira 2005; Taylor G.
                               Capoeira: The Jogo de Angola 2005; UNESCO
                               capoeira circle inscription 2014; and the
                               other landmarks cited per record)
  combat-capoeira-signature  - The Capoeira Combat Signature Database
                               (his original Signature Combat Method: the
                               ginga the Signature pulse, every technique a
                               signed move, the roda the proving circle,
                               malicia Signature wit; src signature, titles
                               suffixed " (Signature Edition)", never
                               presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBCAP- (public) and JAH-CBCAPS- (signature), verified free
in the manifest, in api.json, in the data-1 top-level index, and in every
shard index file (zero hits in all 811 shard databases).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_capoeira.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos before commit.

Screening: civilian martial-arts instruction only. Nothing
hate-adjacent, profane, or inappropriate; no religious talk; nothing on
neutralizing or defeating military or defense-grade systems.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Combat Method: the "
            "ginga is the Signature pulse, every technique a signed move, "
            "the roda the proving circle, and malicia Signature wit. "
            "Clearly labeled Signature-made, never presented as authentic "
            "public record.")

CIT_NESTOR = ("Capoeira N. The Little Capoeira Book. Rev. ed. North Atlantic "
              "Books; 2002.")
CIT_ALMEIDA = ("Almeida B. Capoeira: A Brazilian Art Form: History, "
               "Philosophy, and Practice. North Atlantic Books; 1986.")
CIT_ASSUNCAO = ("Assuncao M.R. Capoeira: The History of an Afro-Brazilian "
                "Martial Art. Routledge; 2005.")
CIT_DOWNEY = ("Downey G. Learning Capoeira: Lessons in Cunning from an "
              "Afro-Brazilian Art. Oxford University Press; 2005.")
CIT_TAYLOR = ("Taylor G. Capoeira: The Jogo de Angola from Luanda to "
              "Cyberspace. North Atlantic Books; 2005.")
CIT_UNESCO = ("UNESCO. Capoeira circle inscribed on the Representative List "
              "of the Intangible Cultural Heritage of Humanity; 2014.")

ENTRIES = [
    {
        "key": "ginga",
        "name": "The Ginga: Capoeira's Foundational Sway",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The ginga is the heartbeat of capoeira: a constant triangular "
            "sway of the feet, hips, and guard that never stops. Every "
            "capoeirista begins and returns here. One foot steps back while "
            "the body rocks side to side, arms guarding in opposition to the "
            "legs, weight shifting smoothly from one leg to the other. The "
            "ginga keeps the fighter in motion so no attack ever finds a "
            "still target, and it hides the preparation of every kick, "
            "dodge, and escape that follows. Mestre Bimba built Regional's "
            "entire method on a disciplined ginga, and Angola's slow game "
            "swings on the same rhythm at half tempo. A strong ginga looks "
            "effortless and lasts for hours; a weak one stiffens the hips "
            "and telegraphs every intention. This record teaches the "
            "posture, the three-point foot pattern, the arm coordination, "
            "the breathing, and the drills that make the sway automatic."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. Stand with feet about shoulder width apart, "
            "right foot forward, left foot back, knees soft and bent. "
            "2. Raise your right arm in front of your face as a guard and "
            "extend your left arm back for balance - the arms oppose the "
            "legs. 3. Shift your weight onto the front foot and step the "
            "back foot behind and across, so the feet trade places in a "
            "small triangle; rock your hips side to side with the shift. "
            "4. As the feet swap, the arms swap too: the arm on the side of "
            "the new front foot comes up to guard. 5. Keep the bounce "
            "continuous and relaxed - up on the balls of the feet, chest "
            "open, eyes on your partner, never freezing between steps. "
            "6. Breathe steadily through the nose; let the shoulders drop. "
            "7. Drill it to music: match one full back-and-forth cycle to "
            "two beats of the berimbau, then hold the pattern for three "
            "minutes without stopping. The ginga is correct when a partner "
            "cannot tell which leg your next kick will come from."
        ),
        "key_points": [
            "The ginga is continuous motion: stillness is the one position capoeira forbids, because a still target can be timed.",
            "Feet trace a small triangle - step back, rock, return - while the arms move in opposition to the legs for balance and guard.",
            "Weight rides on the balls of the feet with soft knees; flat feet and locked knees kill the sway.",
            "The guard arm always sits on the side of the forward foot; the swing of the arms is part of the camouflage, not decoration.",
            "Master the ginga first and every kick, dodge, and ground move in this database becomes reachable; skip it and everything telegraphs.",
        ],
        "requirements": [
            "A clear flat floor space of about two meters square, free of obstacles.",
            "Bare feet or thin-soled shoes that let the ball of the foot grip and pivot.",
            "A warm-up: five minutes of hip circles, knee bends, and ankle rolls before drilling.",
            "A mirror or a partner to check that the shoulders stay level and the hips actually swing.",
            "Patience: two to four weeks of daily short sessions before the sway feels natural.",
        ],
        "standards": [
            "Train on a smooth, non-slip surface with clear space around the roda circle.",
            "Warm up hips, knees, and ankles before any ginga drilling; cool down with leg stretches after.",
            "Mestre Bimba's Regional method and the Angola tradition both treat the ginga as the first and last technique taught.",
        ],
        "citations": [CIT_NESTOR, CIT_ALMEIDA, CIT_DOWNEY],
        "sig_lens": (
            "The Signature read: the ginga is the Signature pulse - the "
            "unbroken rhythm every Signature move is signed against. Where "
            "public capoeira sways to hide intention, the Signature Combat "
            "Method signs the sway itself: each rock of the hips a "
            "signature stroke, the body writing its name in motion so every "
            "technique that follows is already authored before it lands."
        ),
    },
    {
        "key": "guard",
        "name": "The Guard: Arm Position and Protection",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The capoeira guard is not a boxing shell - it is a moving "
            "screen. One forearm rides vertical in front of the face, elbow "
            "tucked, hand open or loosely fisted near the chin; the other "
            "arm extends low and back for balance, ready to swing up. The "
            "guard travels with the ginga, the protecting arm always "
            "matching the forward foot, so the head is covered through "
            "every weight shift. Because capoeira attacks arrive as kicks "
            "from unpredictable angles, the guard emphasizes the head and "
            "face first, the ribs second, and relies on distance and "
            "movement for the rest. A proper guard also sets up offense: "
            "the low back arm becomes the swing arm of the armada, the "
            "high arm the frame for the esquiva. This record teaches the "
            "two positions, the swap timing, the elbow discipline, and the "
            "habit of never dropping both hands at once."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. From the ginga with the right foot forward, "
            "bring the right forearm up vertically in front of your face, "
            "fist or open hand at chin height, elbow pointing down and "
            "tucked near the ribs. 2. Extend the left arm back and low, "
            "hand open, palm down - it balances the sway and will swing "
            "into your kicks. 3. Tuck the chin slightly and look past the "
            "guard arm at your partner, never over or under it. 4. When the "
            "ginga steps the left foot forward, the arms swap: left forearm "
            "comes up to the face, right arm drops back - the swap happens "
            "exactly on the weight shift, never late. 5. Keep the elbows "
            "within the frame of the torso; flared elbows open the ribs. "
            "6. Drill the swap slowly for two minutes, then have a partner "
            "toss soft strikes at your head while you keep the guard "
            "traveling with the feet. The guard is correct when you can "
            "take a light tap on the forearm without flinching your head "
            "back."
        ),
        "key_points": [
            "One arm always guards the face; the other stays low for balance and becomes the power arm of spinning kicks.",
            "The guard swaps sides on every ginga step, locked to the weight shift - a late swap is an open head.",
            "Elbows stay tucked: the forearm is a shield, and a flared elbow is a handle for the opponent.",
            "Chin tucks and eyes stay on the partner; looking away breaks the guard before any arm moves.",
            "In capoeira the guard is mobile - it moves with the body and sets up offense, unlike a static boxing shell.",
        ],
        "requirements": [
            "A ginga you can hold for at least one minute - the guard is drilled on top of it, not before it.",
            "A partner or mirror to verify the swap timing matches the footwork.",
            "Soft training targets (focus mitts or a pillow) for tap-testing the forearm position.",
            "Relaxed shoulders: shrugging the guard up to the ears exhausts the arms in minutes.",
            "Two-minute rounds of guard-swap drilling, three rounds per session.",
        ],
        "standards": [
            "Head protection first: in partner drills the face guard is never optional.",
            "Partner taps stay light - the guard is a position drill, not a sparring round.",
            "Both Regional and Angola schools teach the guard as part of the ginga, never as a separate frozen stance.",
        ],
        "citations": [CIT_NESTOR, CIT_ALMEIDA],
        "sig_lens": (
            "The Signature read: the guard is the Signature seal - one "
            "forearm stamped across the face, the seal that authenticates "
            "the fighter. The Signature Combat Method reads the guard as a "
            "signature line: always present, always in the right place, "
            "verifying that the body behind it is the true author of every "
            "move that follows."
        ),
    },
    {
        "key": "balanco",
        "name": "Balanco: Shifting the Weight",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Balanco - the sway, the balance - is the weight-transfer skill "
            "inside the ginga. It is the controlled rocking of the body's "
            "mass from one leg to the other without ever committing fully "
            "to either foot, the reason a capoeirista can launch a kick or "
            "drop into a dodge from any instant of the sway. Beginners "
            "either lock their weight on the front leg, which freezes them, "
            "or bounce too high, which floats them. True balanco keeps the "
            "hips low and the transfer smooth, like water tipping between "
            "two cups: the loaded leg is always the one about to act, and "
            "the unloaded leg is always the one about to move. Angola's "
            "slow game is almost pure balanco - long, teasing shifts that "
            "lure the partner into attacking the wrong side. This record "
            "teaches the hip-level rule, the 60-40 loading habit, the "
            "silent transfer, and the partner drill that exposes a stiff "
            "sway instantly."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. Stand in the ginga and freeze mid-sway with "
            "the right foot forward; feel where your weight sits - it "
            "should be about 60 percent on the front leg, 40 on the back. "
            "2. Slow the sway down to half speed and rock deliberately: "
            "press the weight forward until the back heel wants to lift, "
            "then draw it back until the front toes lighten - never lift "
            "either foot off the floor during this drill. 3. Keep the hips "
            "at one constant height through the whole rock; if your head "
            "bobs up and down, the knees are straightening. 4. Add the "
            "arm swap from the guard record, timed to the moment the "
            "weight passes center. 5. Now speed back up to normal ginga "
            "tempo and have a partner push lightly on your shoulder at "
            "random moments - you should absorb the push into the sway "
            "without stepping out. 6. Drill three two-minute rounds, "
            "alternating slow control rounds with full-tempo rounds. "
            "Balanco is correct when you can stop the sway at any instant "
            "and kick or dodge immediately with either leg."
        ),
        "key_points": [
            "Balanco is partial commitment: roughly 60-40 loading keeps both legs alive, one to strike, one to move.",
            "The hips stay at constant height - vertical bobbing means the knees are locking and the sway is dead.",
            "The loaded leg is the weapon leg; the light leg is the escape leg, and the sway decides which is which.",
            "Angola's slow game weaponizes balanco, using long weight shifts to bait attacks into empty space.",
            "Silent transfers win: if the partner hears your weight land, they can time it.",
        ],
        "requirements": [
            "A working ginga (record 1) - balanco is the inside of the sway, not a separate move.",
            "A smooth floor that lets the feet glide without catching.",
            "A partner for the push test, or a wall to lean-transfer against.",
            "Two-minute slow rounds and two-minute tempo rounds, alternating.",
            "Bare feet so you can feel the pressure shift across the sole.",
        ],
        "standards": [
            "Keep the knees bent and tracking over the toes during every transfer - no knock-knees, no locked joints.",
            "Stop immediately if the knees or ankles ache; sway low, not forced.",
            "The 60-40 loading habit is taught in both lineages as the safe default before any kick or dodge.",
        ],
        "citations": [CIT_DOWNEY, CIT_TAYLOR],
        "sig_lens": (
            "The Signature read: balanco is the Signature ledger - weight "
            "moved like funds between accounts, never all in one place. "
            "The Signature Combat Method keeps the books balanced at "
            "60-40: enough committed to strike with authority, enough held "
            "back to sign the next move. A fighter who masters the ledger "
            "never goes bankrupt mid-exchange."
        ),
    },
]

ENTRIES.extend([
    {
        "key": "cocorinha",
        "name": "Cocorinha: The Squatting Dodge",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The cocorinha is capoeira's signature dodge: a fast squat that "
            "drops the whole body under a kick while one arm shoots up to "
            "guard the face. The name means little squat, and the move is "
            "one of the oldest defenses in the art - Mestre Bimba placed "
            "it in his first teaching sequence because it answers the "
            "most common attack, a high kick, with the simplest possible "
            "motion: get small, fast. The body folds straight down, knees "
            "bent deeply, heels lifting as needed, while the guard arm "
            "covers the face and the other arm braces. Done right, the "
            "opponent's kick passes through the space where your head was "
            "a quarter second earlier. Done wrong - leaning, slow, or with "
            "the face unguarded - it becomes a crouch into the kick. This "
            "record teaches the straight-down drop, the guard-arm timing, "
            "the heel-lift allowance, and the immediate rise back into the "
            "ginga, because the cocorinha is a dodge, not a hiding place."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. From the ginga, when you read a high kick "
            "coming, bend both knees deeply and drop straight down - the "
            "spine stays upright, the drop is vertical, not a lean. "
            "2. At the same instant, shoot the guard-side forearm up across "
            "the face, fist at forehead height; the other hand drops to "
            "guard the low line or braces near the floor. 3. Let the heels "
            "lift if needed to get low, but keep the balls of the feet "
            "planted - you must be able to explode back up. 4. Hold the "
            "low position only for a beat; the kick passes overhead. "
            "5. Drive up through the legs back into the ginga the instant "
            "the kick clears, guard still up - never rise with the hands "
            "down. 6. Drill with a partner swinging a slow high kick "
            "(meia-lua de frente) at your head height while you cocorinha "
            "under it, ten reps per side, then increase the kick speed. "
            "The cocorinha is correct when the partner's foot passes "
            "cleanly over your guard arm and you are already standing "
            "again before they recover."
        ),
        "key_points": [
            "Drop straight down with an upright spine - leaning forward or back walks the head into the kick.",
            "The guard arm must be up before the body finishes dropping; the face is covered through the entire motion.",
            "Heels may lift but the balls of the feet stay planted, loaded like springs for the rise.",
            "The low hold lasts one beat only - staying down turns a dodge into a target.",
            "Rise back into the ginga with the guard up, ready to answer; the dodge sets up the counter.",
        ],
        "requirements": [
            "A partner who can throw slow, controlled high kicks at first, speeding up only as your timing locks in.",
            "Knee-friendly flooring - mats or smooth wood, since the drop loads the knees deeply.",
            "A pre-drill warm-up of bodyweight squats and ankle mobility.",
            "Ten clean reps per side before adding any speed.",
            "The discipline to keep the guard arm up on every rep, even when the kick is slow.",
        ],
        "standards": [
            "Partner kicks stay controlled and aimed above head height; the dodger never ducks into a kick aimed at the body.",
            "Knees track over the toes in the squat; stop if the knees cave inward or ache.",
            "Bimba's first sequence pairs the cocorinha with the immediate counter - dodge and answer are one lesson.",
        ],
        "citations": [CIT_NESTOR, CIT_ALMEIDA],
        "sig_lens": (
            "The Signature read: the cocorinha is the Signature duck - the "
            "author steps out from under the sentence aimed at him. The "
            "Signature Combat Method treats the drop as an edit: the kick "
            "is a line of text, the squat deletes the target, and the rise "
            "writes the counter in the margin. Signed, sealed, and already "
            "standing."
        ),
    },
    {
        "key": "esquiva_lateral",
        "name": "Esquiva Lateral: The Side Dodge",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The esquiva lateral - the side dodge - moves the head and torso "
            "off the center line while the feet stay rooted. Where the "
            "cocorinha drops under a high attack, the lateral dodge slips "
            "around a straight-line attack: lean the upper body to the side, "
            "let the kick or strike pass through the vacated lane, and keep "
            "the legs coiled to spring back or counter. It is the dodge "
            "that preserves height and vision - the eyes never leave the "
            "partner, the guard stays near the face, and the return to the "
            "ginga is instant because the feet never left their stance. "
            "Beginners lean with stiff legs and get caught by the follow-up; "
            "the correct form bends the knees deeply into the lean so the "
            "head moves a full head-width off line. This record teaches the "
            "hip-initiated lean, the guard maintenance, the coiled-leg "
            "rule, and the partner timing drill."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. From the ginga, read a straight attack - a "
            "ponteira or a straight punch line. 2. Bend both knees and "
            "lean the torso to the outside (away from the attack), "
            "initiating from the hips, not the neck - the head should move "
            "a full head-width off the center line. 3. Keep the guard "
            "forearm glued in front of the face through the lean; the "
            "other hand guards the ribs. 4. Let the feet stay where they "
            "are - the legs coil deeper, loaded. 5. The instant the attack "
            "passes, drive off the coiled legs back to center, guard up, "
            "ginga resumed. 6. Drill with a partner throwing slow straight "
            "kicks at your chest while you slip them, alternating sides, "
            "ten per side, then have the partner fake one side and throw "
            "the other. The esquiva lateral is correct when you can dodge "
            "three straight attacks in a row without moving your feet and "
            "without losing sight of your partner."
        ),
        "key_points": [
            "The lean starts at the hips with deep knee bend - a neck-only lean moves the head inches, not enough.",
            "Feet stay planted: the dodge spends leg coil, not position, so the counter is instant.",
            "The guard never leaves the face during the lean; dodging with the hands down invites the second attack.",
            "Eyes stay locked on the partner - looking away during a dodge is how the follow-up lands.",
            "Alternate sides in drilling so the body learns the dodge both ways; real attacks do not favor your good side.",
        ],
        "requirements": [
            "A solid ginga and guard (records 1-2) - the lateral dodge layers onto them.",
            "A partner throwing slow, straight, telegraphed attacks to start.",
            "Enough floor space to lean fully without hitting a wall.",
            "Ten clean reps per side per session before adding feints.",
            "A mirror check early on: the head must visibly clear the center line.",
        ],
        "standards": [
            "Partner attacks are aimed at the chest line and thrown at half speed until the dodge is clean.",
            "The knees bend with the lean; never lean on straight legs, which strains the lower back.",
            "Keep the dodge inside the roda's flow - it is a slip, not a retreat out of the game.",
        ],
        "citations": [CIT_NESTOR, CIT_DOWNEY],
        "sig_lens": (
            "The Signature read: the esquiva lateral is the Signature "
            "sidestep - the author slides out of the argument's path and "
            "lets the claim swing through empty air. The Signature Combat "
            "Method signs the dodge in the margin: no retreat, no panic, "
            "just a clean lateral annotation while the feet keep their "
            "place on the page."
        ),
    },
    {
        "key": "esquiva_baixa",
        "name": "Esquiva Baixa: The Low Dodge",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The esquiva baixa - the low dodge - takes the cocorinha's "
            "idea further down: the fighter drops low and to the side, "
            "often touching a hand to the floor, slipping under high and "
            "mid attacks while entering the low game. It is the bridge "
            "between standing defense and ground flow - from the baixa "
            "position the capoeirista can roll into a role, rise into a "
            "negativa, or spring up with a kick. The hand on the floor is "
            "not decoration; it is a third leg, stabilizing the deep "
            "crouch and loading the body for the next move. Angola players "
            "live in and around the baixa, flowing through it like water "
            "around rocks. The danger is the same as the cocorinha's "
            "multiplied: dropping low with a dead guard or slow legs "
            "presents the head at knee height. This record teaches the "
            "diagonal drop, the floor-hand placement, the live guard, and "
            "the three exits - roll, negativa, and rise."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. From the ginga, as a high or mid kick "
            "approaches, bend deeply and drop diagonally down and to the "
            "outside of the attack, reaching one hand toward the floor. "
            "2. Plant the hand flat on the floor beside your foot - fingers "
            "spread, arm slightly bent to absorb - while the other forearm "
            "stays vertical in front of the face. 3. Keep the head up and "
            "the eyes on the partner; the spine stays long even at the "
            "bottom. 4. Hold only a beat while the attack passes. 5. Exit "
            "one of three ways: (a) push off the floor hand and rise back "
            "to the ginga; (b) let the momentum carry you into a role "
            "ground spin; (c) settle the hips back into a negativa. "
            "6. Drill each exit five times per side with a partner throwing "
            "slow high kicks. The esquiva baixa is correct when the hand "
            "touches the floor, the face stays guarded, and you can name "
            "your exit before you arrive at the bottom."
        ),
        "key_points": [
            "The floor hand is a third leg: it stabilizes, absorbs, and launches the exit - never a dead prop.",
            "Drop diagonally off the attack line, not straight into it; the angle is the whole dodge.",
            "The guard arm lives through the entire drop - low does not mean open.",
            "Choose the exit on the way down (rise, roll, or negativa), not after you land.",
            "The baixa is the doorway to the ground game; every advanced floor move in this database starts here.",
        ],
        "requirements": [
            "A clean, grippy floor - the planted hand must not slide.",
            "Wrist warm-up (circles, stretches) before drilling, since the hand takes body weight.",
            "A partner throwing slow high or mid kicks.",
            "Five reps per exit per side, drilled separately before mixing.",
            "Patience with the diagonal: beginners drop straight and eat the follow-up.",
        ],
        "standards": [
            "The floor hand lands flat with spread fingers; never post on the fingertips or a hyperextended wrist.",
            "Partner kicks stay at head-to-chest height and half speed until the diagonal drop is reliable.",
            "Exit the low position within one beat - the baixa is transit, not residence.",
        ],
        "citations": [CIT_TAYLOR, CIT_DOWNEY],
        "sig_lens": (
            "The Signature read: the esquiva baixa is the Signature "
            "footnote - the author drops below the main text to reposition. "
            "The floor hand is the signature pressed to the page's edge, "
            "authenticating the move, and the three exits are three clauses "
            "the fighter can append. The Signature Combat Method teaches: "
            "go low to rewrite the terms, never to surrender them."
        ),
    },
    {
        "key": "meia_lua_frente",
        "name": "Meia-Lua de Frente: The Front Crescent Kick",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The meia-lua de frente - the front crescent moon - is the "
            "first kick every capoeirista learns and the one they never "
            "stop using. The leg swings up and across the body in a "
            "crescent arc, striking with the inside edge of the foot, and "
            "returns along the same path. It is a deceptively complete "
            "technique: the arc attacks the head from the outside, the "
            "return arc threatens the other side, and the whole motion "
            "flows directly out of the ginga without a tell. Bimba taught "
            "it as the opening attack of his sequences because its arc "
            "teaches the hip turnover that every harder kick needs. The "
            "common failures are kicking with a straight locked knee (which "
            "bleeds power), dropping the guard, and swinging from the knee "
            "instead of the hip. This record teaches the hip-led arc, the "
            "inside-edge contact, the guard discipline, and the two-way "
            "threat of the return path."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. From the ginga with the right foot forward, "
            "shift your weight onto the left (support) leg and keep the "
            "guard up. 2. Swing the right leg up and across in a crescent "
            "arc, leading with the hip - the knee stays slightly bent, "
            "the foot flexed so the inside edge leads. 3. Turn the "
            "support foot's heel toward the target as the kick rises; the "
            "hip turnover is where the power lives. 4. Strike through "
            "with the inside edge of the foot at head height, eyes on the "
            "target past your guard. 5. Bring the leg back along the same "
            "crescent path - the return is a second attack, not a "
            "retreat - and land back in the ginga. 6. Drill ten slow arcs "
            "per leg focusing on hip turnover, then ten at speed on a "
            "heavy bag or pad, then alternate legs without pausing. The "
            "kick is correct when the bag moves from the hip's snap, not "
            "from a knee flick, and your guard never dropped."
        ),
        "key_points": [
            "Power comes from hip turnover, not the knee: the support heel turns toward the target as the kick rises.",
            "Contact is the inside edge of the foot with the foot flexed - a pointed toe turns the kick into a slap.",
            "The return arc is a second attack; bringing the leg straight back down wastes half the technique.",
            "The guard stays up through the whole kick - the most common beginner error is dropping both hands to swing.",
            "The meia-lua de frente flows straight out of the ginga, which is why it is the first kick taught and the last abandoned.",
        ],
        "requirements": [
            "A stable ginga and guard - the kick launches from the sway, not from a static stance.",
            "Hip mobility warm-up: leg swings and hip circles, five minutes.",
            "A heavy bag, pad, or patient partner holding a target for contact practice.",
            "Ten slow technical reps per leg before any full-speed kicking.",
            "A clear arc path - check the training space for obstacles at head height.",
        ],
        "standards": [
            "Contact practice only on pads or bags until control is proven; never throw full-power head kicks at a partner.",
            "The support knee stays soft and tracking over the toes through the hip turnover.",
            "Bimba's sequences open with this kick - learn it clean before any spinning technique.",
        ],
        "citations": [CIT_NESTOR, CIT_ALMEIDA],
        "sig_lens": (
            "The Signature read: the meia-lua de frente is the Signature "
            "crescent - the first stroke of the author's mark, a moon "
            "drawn across the sky of the roda. The Signature Combat Method "
            "teaches it as the founding signature: one clean arc, hip-led "
            "and guarded, and the return path already signing the second "
            "half of the name."
        ),
    },
    {
        "key": "pisao",
        "name": "Pisao: The Stomping Kick",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The pisao - the stomp - is capoeira's most direct kick: lift "
            "the knee high, then drive the sole of the foot down and "
            "forward into the target like stamping out a fire. It targets "
            "the opponent's thigh, knee, or torso, and its bluntness is "
            "its virtue - no arc to read, no spin to time, just a heavy "
            "driving sole delivered from a tight chamber. In the roda the "
            "pisao punishes a partner who crowds in, and in Bimba's "
            "sequences it answers the grab. The power comes from dropping "
            "the body weight through the leg, not from swinging it: the "
            "knee chambers up, the hips sit into the stomp, and the foot "
            "drives through the target. Beginners kick with the toes or "
            "lean back and lose balance; the correction is sole-first "
            "contact and a slight forward commitment of the hips. This "
            "record teaches the chamber, the weight drop, the sole "
            "contact, and the instant rechamber."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. From the ginga, lift the kicking knee high "
            "and tight to the chest - this chamber hides the kick's "
            "destination. 2. Keep the guard up and the support knee soft. "
            "3. Drive the foot forward and slightly down, striking with "
            "the full sole, hips pushing into the kick - imagine stamping "
            "through the target, not at it. 4. Keep the ankle locked and "
            "the toes pulled back so the sole is a flat hammer face. "
            "5. The instant after contact, rechamber the knee back to the "
            "chest and return the foot to the ginga - never leave the leg "
            "extended. 6. Drill on a heavy bag or shield: ten slow "
            "chamber-to-contact reps per leg, then ten driving reps, "
            "focusing on the weight drop. The pisao is correct when the "
            "bag thumps from body weight, not leg swing, and you are "
            "balanced enough to kick again immediately."
        ),
        "key_points": [
            "The sole is the weapon: toes back, ankle locked, the whole foot a flat hammer face.",
            "Power comes from dropping body weight through the leg, not from swinging the leg like a pendulum.",
            "The high tight chamber hides the target until the last instant - a low lazy chamber telegraphs.",
            "Rechamber instantly after contact; an extended leg is a handle for counters and sweeps.",
            "The pisao is the anti-crowding tool: short, heavy, and honest, it resets distance in one beat.",
        ],
        "requirements": [
            "A heavy bag, kick shield, or pad holder - the pisao is a contact kick and needs a target.",
            "Ankle mobility work so the toes can pull fully back for sole contact.",
            "Ten slow technical reps per leg before driving reps.",
            "A partner holding the shield braced, never a free-hanging target at first.",
            "Core engagement: the hips drive, so the midsection must be warm and active.",
        ],
        "standards": [
            "Full-power pisao practice is for bags and shields only; partner targets stay at controlled touch.",
            "The support foot stays flat and the knee tracks over the toes through the drive.",
            "Keep the guard up - the stomp's directness tempts fighters to drop their hands.",
        ],
        "citations": [CIT_NESTOR, CIT_ALMEIDA],
        "sig_lens": (
            "The Signature read: the pisao is the Signature stamp - the "
            "author's seal driven down with the full weight of the body. "
            "The Signature Combat Method treats every stomp as a document "
            "sealed: sole flat, weight committed, rechambered clean. When "
            "the Signature stamps, distance is reset and the page is "
            "official."
        ),
    },
    {
        "key": "bloqueio_cruzado",
        "name": "Bloqueio Cruzado: The Crossed Block",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The bloqueio cruzado - the crossed block - is capoeira's "
            "answer to the attacks the dodges cannot reach: both forearms "
            "cross in front of the body, forming an X that catches kicks "
            "and strikes on the meat of the forearms. Capoeira prefers "
            "dodges, but the crossed block covers the moments when "
            "distance collapses - the clinch, the surprise, the second "
            "attack in a combination. The X is strong because the forearms "
            "brace each other; a single arm blocks, but crossed arms "
            "absorb. The block is always paired with a step or a lean that "
            "bleeds off the remaining force - meeting a kick dead-on with "
            "a static block is a beginner's injury. This record teaches "
            "the X formation, the forearm conditioning progression, the "
            "angle-step pairing, and the immediate conversion of the block "
            "into a grab or counter."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. As an attack closes inside dodge range, snap "
            "both forearms up and across the body, crossing them at the "
            "wrists to form an X in front of the chest and face. 2. Tuck "
            "the chin behind the X and brace the core - the forearms take "
            "the impact on their outer meaty edges, never on the wrists. "
            "3. Step slightly offline or lean with the block so the force "
            "deflects rather than landing square; the block redirects, it "
            "does not wall. 4. The instant the attack lands on the X, "
            "convert: trap the limb with the crossed arms, or drop into "
            "an esquiva and counter. 5. Condition the forearms gradually: "
            "start with light partner taps on the X, ten per session, "
            "building over weeks - never start with full kicks. 6. Drill "
            "the block-to-trap conversion: partner throws a slow kick, "
            "you cross-block, catch, and answer with a pisao. The block is "
            "correct when the impact lands on forearm meat, the body "
            "angles off, and you are already countering."
        ),
        "key_points": [
            "The X braces the forearms against each other - crossed arms absorb what a single arm cannot.",
            "Impact lands on the outer forearm meat, never the wrists, elbows, or hands.",
            "Every block pairs with an offline step or lean; the block redirects force, it never meets it square.",
            "The block is a transition, not a destination - trap, dodge, or counter within one beat of contact.",
            "Conditioning is gradual: weeks of light taps build the forearms; full kicks on day one build injuries.",
        ],
        "requirements": [
            "A partner for progressive contact: light taps first, building over weeks.",
            "Forearm conditioning patience - this is a months-long adaptation, not a day-one skill.",
            "The esquiva records (4-6) learned first, so the block is the backup, not the only plan.",
            "Wrist wraps optional during early conditioning sessions.",
            "Ten light taps per session to start, adding force only when there is zero pain the next day.",
        ],
        "standards": [
            "Contact starts light and builds over weeks; stop any session that produces sharp pain or swelling.",
            "The chin tucks behind the X on every rep - an exposed chin during blocking drills is a coaching failure.",
            "Blocks are drilled as block-then-counter, never as static receiving.",
        ],
        "citations": [CIT_ALMEIDA, CIT_DOWNEY],
        "sig_lens": (
            "The Signature read: the bloqueio cruzado is the Signature "
            "cross - two forearms signing over each other to authenticate "
            "the defense. The Signature Combat Method reads the X as a "
            "countersignature: the attack submits its claim, the crossed "
            "arms stamp it received, and the counter is the reply already "
            "in the mail."
        ),
    },
    {
        "key": "bencao",
        "name": "Bencao: The Pushing Kick",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The bencao - the blessing - is a front push kick delivered "
            "with the sole, driving the opponent straight back to reset "
            "distance. The name is pure capoeira irony: a blessing that "
            "sends you flying. Technically it is the long-range cousin of "
            "the pisao: the knee chambers, the hips drive, and the sole "
            "pushes through the target's torso or hips with the leg "
            "extending fully. Where the pisao is a short heavy stamp, the "
            "bencao is a long shove - less damage, more displacement - "
            "making it the roda's politeness tool, the kick that says "
            "back up without starting a war. Regional players use it to "
            "punish crowding; Angola players use it to open space for the "
            "slow game. The keys are full hip extension into the push, "
            "sole contact, and the immediate return - a bencao left "
            "hanging becomes a caught leg. This record teaches the "
            "chamber, the driving extension, the push-through finish, and "
            "the balance recovery."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. From the ginga, chamber the kicking knee up "
            "toward the chest, guard high. 2. Drive the hips forward and "
            "extend the leg fully into the target's torso or hip, striking "
            "with the sole, toes pulled back. 3. Push THROUGH the target - "
            "extend the hip completely at contact, as if shoving a heavy "
            "door - rather than snapping the leg back. 4. Keep the support "
            "leg slightly bent and the torso upright; leaning back bleeds "
            "the push. 5. After the push lands, rechamber the knee and "
            "return to the ginga without hopping. 6. Drill on a heavy bag "
            "or a partner-held shield: ten pushes per leg, focusing on "
            "hip extension, then practice the push-and-recover at ginga "
            "tempo. The bencao is correct when the bag swings from the "
            "push, your balance never wavers, and the leg is home before "
            "the partner can grab it."
        ),
        "key_points": [
            "The bencao displaces rather than damages: full hip extension pushes the opponent back and resets the distance.",
            "Sole contact with toes back; the push goes through the target like shoving a door, not snapping at it.",
            "The torso stays upright - leaning back turns a push into a fall.",
            "Rechamber immediately: an extended push kick is the easiest leg in capoeira to catch.",
            "It is the roda's politeness tool: space made cleanly, without escalating the game.",
        ],
        "requirements": [
            "A heavy bag or shield for push practice - the technique needs resistance to learn the push-through.",
            "Hip flexor and glute warm-up; the full extension loads the hip.",
            "Ten technical reps per leg before speed work.",
            "A partner who can hold a shield steady and give feedback on push vs snap.",
            "Balance drilling: the push must not cost you your stance.",
        ],
        "standards": [
            "Push kicks to a partner's torso stay at controlled force; the bencao displaces, it does not injure.",
            "The support knee stays soft and aligned over the toes through the full extension.",
            "Guard stays up - the push's reach tempts fighters to drop their hands.",
        ],
        "citations": [CIT_NESTOR, CIT_ALMEIDA],
        "sig_lens": (
            "The Signature read: the bencao is the Signature benediction - "
            "a blessing delivered sole-first that politely reschedules "
            "the argument. The Signature Combat Method signs the push with "
            "full extension: distance restored, dignity intact, the page "
            "turned without tearing it."
        ),
    },
    {
        "key": "ponteira",
        "name": "Ponteira: The Snapping Front Kick",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The ponteira - the tip, the point - is capoeira's snapping "
            "front kick: the knee chambers and the lower leg whips out, "
            "striking with the ball of the foot or the instep, then snaps "
            "back. Where the bencao pushes, the ponteira stings; it is the "
            "faster, sharper sibling, built for speed and surprise rather "
            "than displacement. In the fast Regional game the ponteira "
            "darts in and out like a jab, testing the partner's guard and "
            "punishing dropped hands. The snap comes from the knee joint: "
            "the thigh stays relatively still while the shin whips, which "
            "makes the kick brutally fast but demands a strong, instant "
            "rechamber - a slow ponteira is a caught ponteira. This record "
            "teaches the chamber, the shin-whip mechanics, the ball-of-"
            "foot contact, and the snap-back discipline."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. From the ginga, snap the kicking knee up to "
            "chest height, thigh roughly parallel to the floor, guard high. "
            "2. Whip the lower leg out by extending the knee fast, "
            "striking with the ball of the foot (toes pulled back) or the "
            "instep - the thigh barely moves; the shin does the work. "
            "3. At full extension, immediately reverse the motion and snap "
            "the foot back to the chamber - the kick's return should be as "
            "fast as its delivery. 4. Set the foot back down into the "
            "ginga without a pause. 5. Drill the snap slowly first: ten "
            "chamber-extend-rechamber cycles per leg with no target, "
            "watching that the thigh stays still. 6. Then work a pad: ten "
            "snaps per leg, listening for the sharp crack of clean "
            "contact. The ponteira is correct when the pad cracks from "
            "shin speed, the thigh never swung, and the foot is home "
            "before you could blink."
        ),
        "key_points": [
            "The shin whips while the thigh stays nearly still - knee-joint speed is what makes the ponteira fast.",
            "Contact is the ball of the foot or instep; the snap-back is as important as the strike.",
            "A slow return gets the leg caught - the rechamber must match the delivery speed.",
            "It is the jab of capoeira kicks: fast, testing, punishing dropped guards in the fast game.",
            "Guard discipline matters most here: the kick's speed tempts the hands to drop for balance.",
        ],
        "requirements": [
            "Knee-friendly warm-up: leg swings and bodyweight squats before snapping reps.",
            "A pad or shield for contact; start with slow technical cycles with no target.",
            "Ten chamber-extend-rechamber cycles per leg before any contact.",
            "Ankle flexibility so the toes pull fully back for ball-of-foot contact.",
            "A partner who can hold a pad steady at torso height.",
        ],
        "standards": [
            "Snapping kicks to a partner stay at touch contact; full snap power is for pads only.",
            "The support leg stays planted and the knee soft through the whip.",
            "Stop if the knee joint aches - the snap loads the knee and demands respect.",
        ],
        "citations": [CIT_NESTOR, CIT_ALMEIDA],
        "sig_lens": (
            "The Signature read: the ponteira is the Signature jab - a "
            "quick pointed annotation in the margin of the fight. The "
            "Signature Combat Method signs it with shin speed and instant "
            "return: a sharp note, cleanly placed, the pen already back "
            "in hand before anyone saw it move."
        ),
    },
    {
        "key": "joelhada",
        "name": "Joelhada: The Knee Strike",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The joelhada - the knee strike - drives the point of the knee "
            "up into the opponent's torso or thigh at close range. It is "
            "the inside-fighting tool of capoeira: when the roda tightens "
            "and kicks have no room, the knee does the work. The strike "
            "chambers tight and drives up with the hips, the hands pulling "
            "the opponent's guard down or controlling the head to meet the "
            "rising knee. In Bimba's sequences the joelhada answers the "
            "close clinch, and in the Angola game it punishes the partner "
            "who dives in recklessly. The power is pure hip drive - the "
            "knee is just the point the hips deliver. Beginners lean back "
            "and throw the knee with the leg alone; the correction is to "
            "drive the hips forward and up, standing tall into the strike. "
            "This record teaches the tight chamber, the hip drive, the "
            "hand control pairing, and the clinch safety rules."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. At close range, pull the opponent's guard "
            "down or control the upper body with your hands - the knee "
            "needs a target brought to it. 2. Chamber the knee tight to "
            "your chest, foot dangling relaxed behind. 3. Drive the hips "
            "forward and up, thrusting the knee point into the target "
            "(torso, thigh, or hip) - stand tall into it, never lean back. "
            "4. Keep the support foot flat and pivot slightly on it to add "
            "hip rotation. 5. Drop the knee straight back down into your "
            "stance - no lingering. 6. Drill on a heavy bag or a partner-"
            "held body shield: ten knees per side, focusing on the hip "
            "thrust, then drill the hand-pull plus knee as one motion. "
            "The joelhada is correct when the bag dents from hip drive, "
            "your posture stayed tall, and you could immediately knee "
            "again with the other side."
        ),
        "key_points": [
            "The hips deliver the knee: drive forward and up, standing tall - leaning back unplugs the power.",
            "Hands control the target: pulling the guard down or framing the body brings the target to the knee.",
            "The chamber is tight to the chest, hiding the strike until the hips fire.",
            "It is the close-range answer: when kicks have no room, the knee takes over.",
            "Drop the knee straight back down after contact - a hanging knee is a swept knee.",
        ],
        "requirements": [
            "A heavy bag or body shield - the knee is a contact strike and needs resistance.",
            "Hip mobility warm-up and core activation before drilling.",
            "A partner for the hand-control pairing drill, at slow speed first.",
            "Ten knees per side per session, building the hip drive.",
            "Clinch awareness: practice entering and exiting the close range safely.",
        ],
        "standards": [
            "Knee strikes to a partner are drilled at touch contact on a shield; full power is for the bag.",
            "The head stays up and the chin tucked - diving the head forward into a knee exchange is forbidden.",
            "Control the partner's posture with the hands; never yank the head down by the neck in drilling.",
        ],
        "citations": [CIT_ALMEIDA, CIT_DOWNEY],
        "sig_lens": (
            "The Signature read: the joelhada is the Signature full stop - "
            "the knee a period driven up to end the sentence at close "
            "range. The Signature Combat Method signs it with the hips: "
            "tight chamber, tall drive, no wasted ink. When the argument "
            "gets crowded, the Signature punctuates."
        ),
    },
])

ENTRIES.extend([
    {
        "key": "queixada",
        "name": "Queixada: The Cross-Step Kick",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The queixada - the jaw kick, named for the target it seeks - "
            "is capoeira's great cross-step attack: the fighter steps "
            "across with the front foot, swings the back leg around in a "
            "wide outside arc, and strikes with the outside edge of the "
            "foot. The cross-step is the disguise - the step looks like a "
            "ginga adjustment, and then the leg is already gone. It is one "
            "of the most powerful kicks in the art because the full body "
            "rotates behind it, and one of the most beautiful because the "
            "arc is enormous. Bimba made it a centerpiece of the Regional "
            "game, and Angola players throw it slow and heavy. The kick "
            "demands commitment: a half-hearted queixada leaves the kicker "
            "spun around and exposed. This record teaches the cross-step "
            "disguise, the full-body rotation, the outside-edge contact, "
            "and the spin-through recovery."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. From the ginga, step the front foot across "
            "and in front of the back foot - a natural-looking cross-step, "
            "weight settling onto it. 2. Let the back leg swing free: it "
            "travels in a wide outside arc, driven by the rotation of the "
            "hips and shoulders - the body unwinds like a spring. "
            "3. Strike with the outside edge of the foot, leg extended, at "
            "head height, eyes on the target. 4. Commit fully: the momentum "
            "carries you through a full turn - do not try to stop the spin "
            "midway. 5. As the rotation completes, the kicking leg comes "
            "down and you land back in the ginga, guard up, facing your "
            "partner. 6. Drill slowly first: ten cross-steps with a slow "
            "leg swing per side, no target, learning the rotation; then "
            "ten on a heavy bag, letting the spin carry through. The "
            "queixada is correct when the bag rocks from body rotation, "
            "the step looked like nothing, and you finished the spin "
            "balanced and guarded."
        ),
        "key_points": [
            "The cross-step is the disguise: it reads as a ginga adjustment, and the kick is already launched.",
            "Power comes from full-body rotation - hips and shoulders unwind together behind the leg.",
            "Contact is the outside edge of the foot at head height; the arc is wide and committed.",
            "Never fight the spin: commit through the full turn and land guarded, or do not throw it.",
            "It is the bridge kick between foundation arcs and true spinning attacks - master it before the armada.",
        ],
        "requirements": [
            "A reliable meia-lua de frente (record 7) - the queixada builds on hip turnover.",
            "A heavy bag for full-rotation practice; the spin needs a target to land on safely.",
            "Clear floor space of at least three meters - the arc and spin need room.",
            "Ten slow rotation reps per side before any bag contact.",
            "Strong ankles: the cross-step pivots load the support foot heavily.",
        ],
        "standards": [
            "Full-power queixada practice is for bags only; partner work stays at controlled touch on pads.",
            "Commit to the spin or abort early - a checked queixada mid-rotation strains the knee.",
            "The guard stays up through the cross-step; the disguise fails if the hands drop.",
        ],
        "citations": [CIT_NESTOR, CIT_ALMEIDA],
        "sig_lens": (
            "The Signature read: the queixada is the Signature cross-out - "
            "one bold stroke deleting the opponent's plan. The cross-step "
            "is the pen lifting innocently off the page; the arc is the "
            "line drawn through everything. The Signature Combat Method "
            "signs it with full rotation: when the Signature crosses "
            "something out, it stays crossed."
        ),
    },
    {
        "key": "armada",
        "name": "Armada: The Spinning Inside Crescent Kick",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The armada - the armed one - is capoeira's classic spinning "
            "kick: the fighter pivots on the front foot, spins the body a "
            "full 360 degrees, and the back leg whips around in an inside "
            "crescent, striking with the outside edge of the foot. It is "
            "the kick the world pictures when it pictures capoeira, and "
            "for good reason - the spin generates enormous power while the "
            "crescent arc covers a huge zone. The armada's secret is the "
            "spotting: the head whips around to find the target mid-spin, "
            "the way a dancer spots, so the kick lands aimed rather than "
            "wild. Beginners spin blindly and kick air; the correction is "
            "the head snap. It pairs naturally with the queixada - "
            "queixada spins one way, armada the other - and together they "
            "form the spinning foundation of the fast game. This record "
            "teaches the pivot, the head-spot, the crescent whip, and the "
            "balanced landing."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. From the ginga, step the back foot forward "
            "and pivot on the ball of the front foot, beginning the spin - "
            "the arms swing to drive the rotation. 2. Whip your head "
            "around first: spot the target over your shoulder as early in "
            "the spin as possible. 3. Let the kicking leg trail and then "
            "whip through in an inside crescent arc, striking with the "
            "outside edge of the foot - the leg is the last thing to "
            "arrive, accelerated by the spin. 4. Keep the kicking knee "
            "slightly bent until the whip; a straight leg early kills the "
            "acceleration. 5. Land the kicking foot back into the ginga as "
            "the rotation completes, guard up, eyes on the partner. "
            "6. Drill the spin without the kick first: ten full pivots per "
            "direction, spotting a fixed point; then add the leg on a "
            "heavy bag, ten per side. The armada is correct when you spot "
            "the target before the kick arrives, the bag jumps from spin "
            "power, and you land balanced facing your partner."
        ),
        "key_points": [
            "The head spots first: whip it around to find the target mid-spin, like a dancer - blind spins kick air.",
            "The arms drive the rotation; the leg trails and whips last, accelerated by the body's spin.",
            "Contact is the outside edge of the foot in an inside crescent arc - the classic capoeira silhouette.",
            "The pivot stays on the ball of the support foot; a flat-footed spin grinds the knee.",
            "Queixada and armada are the matched spinning pair - one crosses, one pivots, and the fast game runs on both.",
        ],
        "requirements": [
            "A solid queixada (record 13) - the armada is the next spin up the ladder.",
            "A heavy bag for the full-spin kick; the power needs a safe target.",
            "Three meters of clear floor in every direction.",
            "Ten spotting pivots per direction before adding the kick.",
            "Dizziness tolerance: build spin count gradually across sessions.",
        ],
        "standards": [
            "Spinning kicks at full power are for bags; partner targets stay at touch contact on pads.",
            "Pivot on the ball of the foot with the knee soft - never spin on a locked knee.",
            "Stop and rest if dizziness persists; spotting skill builds over weeks, not one session.",
        ],
        "citations": [CIT_NESTOR, CIT_ALMEIDA, CIT_DOWNEY],
        "sig_lens": (
            "The Signature read: the armada is the Signature flourish - "
            "the full 360-degree underline beneath the author's name. The "
            "head spots the way the pen finds its place; the leg whips the "
            "way ink follows. The Signature Combat Method teaches the "
            "flourish as punctuation with power: beautiful, complete, and "
            "impossible to ignore."
        ),
    },
    {
        "key": "martelo",
        "name": "Martelo: The Hammer Kick",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The martelo - the hammer - is an overhead axe kick: the leg "
            "rises high and straight, then crashes down like a hammer "
            "onto the target, striking with the heel or the sole. It is "
            "one of capoeira's most punishing techniques because gravity "
            "does half the work - a leg raised above the head and dropped "
            "with hip drive carries devastating downward force. Regional "
            "fighters throw it fast and steep; Angola players raise it "
            "slow and let it fall like a verdict. The martelo's danger is "
            "also its demand: a missed hammer leaves the kicker stretched "
            "tall and open, so it is thrown when the target is set - "
            "against a crouching or retreating opponent. The supporting "
            "leg must be rock solid, because the whole bodyweight tips "
            "into the drop. This record teaches the high chamber, the "
            "hip-driven drop, the heel contact, and the fast recovery."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. From the ginga, raise the kicking leg high "
            "and straight up in front of you, toes pulled back, guard up - "
            "the higher the chamber, the heavier the hammer. 2. Keep the "
            "support leg slightly bent and rooted; it carries everything. "
            "3. Drive the hips down and forward as the leg crashes down, "
            "striking with the heel or full sole - the power is the drop "
            "plus the hip drive, not a muscle push. 4. Aim for the top of "
            "the target: head, shoulder, or raised guard of a crouching "
            "opponent. 5. The instant the heel lands, rebound the leg back "
            "up and return to the ginga - never leave the leg down on a "
            "miss. 6. Drill on a heavy bag or a low pad stack: ten slow "
            "raise-and-drop reps per leg learning the drop, then ten "
            "driving reps. The martelo is correct when the bag shudders "
            "downward from the drop, your support leg never wobbled, and "
            "the leg was home before the echo faded."
        ),
        "key_points": [
            "Gravity is the engine: raise high, then drop the leg with hip drive - the fall does the damage.",
            "Contact is the heel or full sole, striking downward onto the target's top line.",
            "Throw it at set targets - crouching or retreating opponents - because a missed hammer leaves you tall and open.",
            "The support leg is the anvil: bent, rooted, and utterly stable through the drop.",
            "Rebound instantly on a miss; the recovery is part of the technique, not an afterthought.",
        ],
        "requirements": [
            "Hamstring and hip flexibility sufficient to raise the leg above head height - build with daily stretching.",
            "A heavy bag or stacked pads that can take downward force.",
            "Ten slow raise-and-drop reps per leg before driving reps.",
            "A strong support-leg base: single-leg balance drilling helps enormously.",
            "Clear overhead space - the chamber goes high.",
        ],
        "standards": [
            "Overhead downward kicks are for bags and pads only; never throw a full martelo at a partner's head.",
            "Warm the hamstrings thoroughly - the high chamber plus the drop is a pull waiting to happen if cold.",
            "Keep the support knee soft; a locked support knee under a hammer drop is a joint injury.",
        ],
        "citations": [CIT_NESTOR, CIT_ALMEIDA],
        "sig_lens": (
            "The Signature read: the martelo is the Signature gavel - "
            "raised high, brought down with finality. The Signature Combat "
            "Method treats the hammer as judgment rendered: the chamber "
            "is deliberation, the drop is the ruling, and the rebound is "
            "the court adjourned. When the Signature gavels, the matter "
            "is settled."
        ),
    },
    {
        "key": "rabo_de_arraia",
        "name": "Rabo de Arraia: The Stingray's Tail Kick",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The rabo de arraia - the stingray's tail - is a low spinning "
            "kick that whips around at ankle-to-knee height, striking with "
            "the heel or the outside of the foot. Named for the venomous "
            "tail barb of the stingray, it sweeps the low line where "
            "guards rarely look: while the partner watches the hands and "
            "head, the tail is already circling their legs. The technique "
            "drops the body low, spins on the support foot, and lets the "
            "free leg trail out and whip through - it is half kick, half "
            "sweep, and it punishes anyone standing tall and flat-footed. "
            "Angola's ground game is full of stingray tails flicking out "
            "of low positions. The keys are the low level, the relaxed "
            "trailing leg (tension kills the whip), and the continuous "
            "spin that makes it a sweep rather than a single kick. This "
            "record teaches the low spin, the trailing-leg whip, the heel "
            "contact, and the sweep follow-through."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. Drop your level - bend deeply or go to a "
            "half-crouch - as you begin to spin on the ball of the support "
            "foot. 2. Let the kicking leg trail out behind you, relaxed "
            "and extended low, like the stingray's tail dragging. 3. As "
            "the spin accelerates, whip the trailing leg through at "
            "ankle-to-knee height, striking with the heel or outside edge "
            "of the foot. 4. Keep the leg loose: the whip comes from the "
            "spin, not from muscling the leg - tension slows the tail. "
            "5. Follow through the full rotation and rise back into the "
            "ginga as the spin completes. 6. Drill the low spin without "
            "contact first: ten spins per direction feeling the trailing "
            "leg whip; then practice on a low pad or bag at shin height. "
            "The rabo de arraia is correct when the pad cracks from spin "
            "whip, the leg stayed relaxed, and you finished the rotation "
            "balanced."
        ),
        "key_points": [
            "It hunts the low line - ankles to knees - where guards rarely look and flat feet get punished.",
            "The trailing leg stays relaxed: the spin provides the whip, and tension kills it.",
            "Drop low before spinning; a tall stingray tail is just a slow kick.",
            "Contact is the heel or outside edge of the foot, sweeping through rather than stopping at the target.",
            "It is half kick, half sweep - the follow-through rotation is what makes it sweep the legs.",
        ],
        "requirements": [
            "Comfortable deep crouching - build with bodyweight squat holds.",
            "A low pad, bag, or shield at shin height for contact practice.",
            "Ten no-contact low spins per direction before adding the target.",
            "Smooth floor for the support-foot pivot.",
            "The esquiva baixa (record 6) as the entry - the tail often launches from the low dodge.",
        ],
        "standards": [
            "Low spinning kicks are for pads and bags at full speed; partner legs stay at touch contact.",
            "Pivot on the ball of the support foot with the knee bent - low spins on straight legs grind the knee.",
            "Clear the floor around you: the tail sweeps a full circle at ankle height.",
        ],
        "citations": [CIT_TAYLOR, CIT_DOWNEY],
        "sig_lens": (
            "The Signature read: the rabo de arraia is the Signature "
            "underline - drawn low, fast, and impossible to miss, striking "
            "where nobody thought to look. The Signature Combat Method "
            "keeps the tail relaxed and the spin honest: the fiercest "
            "marks are made below the line everyone is watching."
        ),
    },
    {
        "key": "au",
        "name": "Au: The Cartwheel",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The au - the cartwheel - is capoeira's great escape artist: a "
            "full lateral rotation over the hands that moves the fighter "
            "sideways out of danger while keeping the eyes on the partner "
            "and the legs ready to kick on landing. Unlike a gymnastics "
            "cartwheel, the capoeira au is a combat movement - it dodges a "
            "sweep or a low attack, repositions the fighter, and can "
            "launch directly into a kick from the landing. The hands touch "
            "down one after the other, the legs split wide over the top, "
            "and the body lands facing the same direction it started, "
            "already in the ginga. Advanced players kick out of the au "
            "mid-rotation, turning the escape into an attack. The keys are "
            "the hand sequence, the wide leg split for balance, and the "
            "eyes staying on the partner through the whole rotation. This "
            "record teaches the entry step, the hand placement, the split, "
            "and the combat landing."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. From the ginga, step the lead foot to the "
            "side in the direction you will cartwheel, bending deeply. "
            "2. Reach down and place the lead hand on the floor, fingers "
            "spread, arm straight but not locked. 3. Kick the legs up and "
            "over in a wide split - the second hand touches down as the "
            "first lifts, so there is always support. 4. Keep the eyes on "
            "your partner through the rotation: look under your arm as you "
            "go over, never at the floor. 5. Land the lead leg first, then "
            "the trailing leg, bending the knees to absorb, and settle "
            "straight back into the ginga facing your partner. 6. Drill "
            "against a wall first for the hand sequence, then ten open-"
            "floor cartwheels per side, then practice kicking out of the "
            "landing with a meia-lua. The au is correct when the partner "
            "never left your sight, the landing flowed into the ginga, "
            "and you could have kicked at any point in the rotation."
        ),
        "key_points": [
            "The au is a combat escape, not gymnastics: it dodges low attacks while repositioning, eyes on the partner throughout.",
            "Hands touch one after the other with the legs split wide - the wide split is the balance.",
            "Look under the arm at the partner during the rotation; watching the floor blinds you to the counter.",
            "Land into the ginga facing the same way - the au that lands turned around has failed.",
            "Advanced play kicks out of the au: the escape and the attack are one continuous motion.",
        ],
        "requirements": [
            "Open floor space of at least four meters in the cartwheel direction.",
            "Wrist and shoulder warm-up - the hands take body weight in sequence.",
            "Wall-supported practice for the hand sequence before open-floor attempts.",
            "Ten clean cartwheels per side before adding the kick-out.",
            "A spotter for the first sessions if the rotation feels unstable.",
        ],
        "standards": [
            "Learn the hand sequence against a wall before attempting open-floor cartwheels.",
            "Fingers spread and arms straight-but-not-locked on every hand plant.",
            "Land with bent knees into the ginga - stiff landings jar the joints and break the flow.",
        ],
        "citations": [CIT_NESTOR, CIT_ALMEIDA],
        "sig_lens": (
            "The Signature read: the au is the Signature loop-the-loop - "
            "the author writes a full circle around the danger and lands "
            "with the pen still moving. The Signature Combat Method treats "
            "the cartwheel as a signature flourish with a purpose: escape "
            "signed in the air, landing already authoring the next line."
        ),
    },
    {
        "key": "role",
        "name": "Role: The Low Ground Spin",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The role - the roll, the spin - is the low ground rotation "
            "that carries the capoeirista around the partner at floor "
            "level: from a crouch, the fighter spins 360 degrees low over "
            "a planted hand, sweeping the legs around and ending facing "
            "the partner again. It dodges high attacks by simply not being "
            "where they land, repositions for the low game, and sets up "
            "sweeps and ground kicks. The role is the workhorse of Angola's "
            "floor flow - players chain roles together, circling like "
            "sharks, each spin loading the next attack. The planted hand "
            "is the axle; the legs are the wheel. Beginners try to muscle "
            "the spin with the legs and stall halfway; the correction is "
            "to commit the hips and let momentum carry the rotation. This "
            "record teaches the crouch entry, the hand axle, the hip "
            "commitment, and the chained role drill."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. Drop into a deep crouch from the ginga, "
            "weight low, and plant one hand flat on the floor in front of "
            "you - this hand is the axle. 2. Swing the hips and legs "
            "around the planted hand in a full 360-degree spin, keeping "
            "the body low - the legs sweep the floor, the head stays up "
            "with eyes on the partner. 3. Commit the hips to the rotation; "
            "a half-committed role stalls and strands you. 4. As the spin "
            "completes, the legs come back under you and you rise into "
            "the ginga facing your partner. 5. For chained roles, let the "
            "momentum of one spin feed directly into the next crouch and "
            "spin without standing up. 6. Drill ten single roles per "
            "direction, then ten chained pairs, then have a partner throw "
            "slow high kicks while you role under them. The role is "
            "correct when the spin is continuous, the hand never slipped, "
            "and you finished facing the partner ready to move."
        ),
        "key_points": [
            "The planted hand is the axle and the legs are the wheel - the spin rotates around the hand, not the feet.",
            "Commit the hips fully: a half-hearted role stalls mid-spin and strands the fighter low and blind.",
            "Stay low through the whole rotation - rising mid-spin turns a dodge into a collision.",
            "Eyes on the partner throughout; the head stays up even at floor level.",
            "Chain roles without standing: each spin's momentum feeds the next, and the low game runs on chains.",
        ],
        "requirements": [
            "A smooth, clean floor - the spin and the planted hand need grip without abrasion.",
            "Wrist warm-up, since the axle hand takes rotational load.",
            "Deep-crouch comfort: build with squat holds first.",
            "Ten single roles per direction before chaining.",
            "Knee pads optional while learning the low spin.",
        ],
        "standards": [
            "The axle hand lands flat with spread fingers; never spin on a bent wrist.",
            "Partner kicks during role-under drills stay high and slow until the spin is reliable.",
            "Keep the spin tight and controlled - a wild role travels into the partner or the roda's edge.",
        ],
        "citations": [CIT_TAYLOR, CIT_DOWNEY],
        "sig_lens": (
            "The Signature read: the role is the Signature orbit - the "
            "author circles the subject at floor level, axled on one hand, "
            "never losing the thread. The Signature Combat Method chains "
            "orbits without standing: each revolution a paragraph, each "
            "landing a sentence already aimed at the reader."
        ),
    },
    {
        "key": "negativa",
        "name": "Negativa: The Negative Ground Position",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The negativa - the negative - is capoeira's low ground "
            "fortress: the fighter sits low with one leg extended forward "
            "and the other folded under, one hand planted on the floor "
            "behind, the other guarding the face. From this compact "
            "crouch the capoeirista is nearly unhittable - low, stable, "
            "and coiled - and can launch sweeps, kicks, and rises in any "
            "direction. It is the rest position of the ground game and "
            "the launch pad of its attacks: Angola players settle into "
            "negativas between exchanges, reading the partner, then "
            "explode out. The extended leg threatens sweeps; the folded "
            "leg loads the rise; the planted hand anchors everything. "
            "Beginners collapse into it loosely and get stuck; the "
            "correct negativa is coiled, not collapsed. This record "
            "teaches the leg fold, the hand anchor, the guard, and the "
            "three launches - sweep, kick, and rise."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. From a crouch, extend one leg straight "
            "forward along the floor, foot flexed, while folding the other "
            "leg tightly under your hips - sit onto the folded foot. "
            "2. Plant the hand on the same side as the folded leg flat on "
            "the floor behind you, arm straight, anchoring the position. "
            "3. Bring the other forearm up to guard the face; the chin "
            "tucks, the eyes stay on the partner. 4. Coil, do not collapse: "
            "the torso stays upright, the core engaged, the folded leg "
            "loaded like a spring. 5. Launch one of three ways: sweep the "
            "extended leg in an arc at the partner's ankles; kick up from "
            "the extended leg into a standing kick; or drive off the folded "
            "leg and the planted hand to rise into the ginga. 6. Drill the "
            "position holds (thirty seconds per side), then each launch "
            "five times per side. The negativa is correct when you can "
            "hold it relaxed, launch any of the three exits on command, "
            "and the guard never dropped."
        ),
        "key_points": [
            "The negativa is a coiled fortress: low, stable, and loaded - never a collapsed rest.",
            "The extended leg threatens sweeps; the folded leg loads the rise; the planted hand anchors both.",
            "The guard arm stays up even at floor level - low does not mean open.",
            "Three launches live in the position: sweep, kick, and rise - drill all three until each is instant.",
            "It is the thinking position of the ground game: settle, read the partner, then explode.",
        ],
        "requirements": [
            "Hip and ankle flexibility for the folded-leg sit - build with deep squat holds.",
            "A clean floor; the extended leg slides along it.",
            "Thirty-second holds per side to build the position before drilling launches.",
            "Five reps of each launch per side.",
            "The role (record 18) as the usual entry - the spin often ends in a negativa.",
        ],
        "standards": [
            "The folded ankle stays comfortable - never force the sit past a gentle stretch.",
            "The planted hand stays flat and the wrist straight under the body's weight.",
            "Launch drills with a partner stay at touch contact until control is proven.",
        ],
        "citations": [CIT_TAYLOR, CIT_DOWNEY],
        "sig_lens": (
            "The Signature read: the negativa is the Signature pause - "
            "the author sets the pen down, low and coiled, reading the "
            "page before the next stroke. The Signature Combat Method "
            "treats the crouch as loaded punctuation: the sweep a comma, "
            "the kick an exclamation, the rise a new paragraph. Pauses, "
            "signed properly, are weapons."
        ),
    },
    {
        "key": "cabecada",
        "name": "Cabecada: The Headbutt",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The cabecada - the headbutt - drives the hard crown of the "
            "forehead into the opponent at clinch range. It is capoeira's "
            "closest-range weapon, thrown when the game collapses chest to "
            "chest: the fighter tucks the chin, drives forward off the "
            "legs, and meets the target with the thick bone of the upper "
            "forehead, never the face or the top of the skull. In the "
            "roda it is rarely thrown full force - it is shown, threatened, "
            "and used to unbalance - because its real lesson is clinch "
            "awareness: the head is a weapon and a target at the shortest "
            "distance. The technique demands perfect form for safety: chin "
            "tucked to protect the neck, contact on the forehead's crown, "
            "the drive coming from the legs and hips. This record teaches "
            "the tuck, the crown contact, the leg drive, and the strict "
            "safety protocol that governs all headbutt drilling."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. At clinch range, tuck the chin hard to the "
            "chest - this aligns the spine and presents the forehead's "
            "crown, the thickest bone. 2. Keep the hands up, controlling "
            "the opponent's upper body or guard. 3. Drive forward and "
            "slightly up off the legs, thrusting the forehead's crown into "
            "the target (chest, shoulder, or jaw line in application) - "
            "the power is a short leg-and-hip shove, not a neck snap. "
            "4. Never lead with the face, nose, or the top of the skull; "
            "never snap the neck. 5. Recover immediately back to guard or "
            "disengage to the ginga. 6. Drill ONLY on a heavy bag or a "
            "partner-held body shield at touch contact: ten short drives "
            "focusing on the tuck and the leg drive, never on a live "
            "partner's head. The cabecada is correct when the tuck is "
            "automatic, the contact point is always the crown, and the "
            "neck never whips."
        ),
        "key_points": [
            "Contact is the forehead's crown with the chin tucked - the thickest bone, the safest alignment.",
            "Power is a short leg-and-hip shove; the neck never snaps and the head never leads alone.",
            "It is the clinch-range weapon: when chest-to-chest, the head is both weapon and target.",
            "In the roda it is shown and threatened more than thrown - its lesson is clinch awareness.",
            "Headbutt drilling has the strictest safety protocol in this database: bags and shields only.",
        ],
        "requirements": [
            "A heavy bag or body shield - headbutts are NEVER drilled full-force on a partner.",
            "Neck strengthening and warm-up before any headbutt drilling.",
            "Mastery of the clinch entries (joelhada record 12) first.",
            "Ten touch-contact drives per session, focusing on form, not force.",
            "A coach or experienced partner supervising the first sessions.",
        ],
        "standards": [
            "Full-force headbutts are for bags only; all partner drilling is touch contact on a shield.",
            "The chin tucks on every rep - an untucked chin during headbutt drilling ends the session.",
            "Stop immediately for any neck pain, headache, or dizziness; head safety is absolute.",
        ],
        "citations": [CIT_ALMEIDA, CIT_DOWNEY],
        "sig_lens": (
            "The Signature read: the cabecada is the Signature header - "
            "the author's crown pressed to the top of the page at the "
            "closest range. The Signature Combat Method signs it with the "
            "tuck and the leg drive: the hardest bone, the shortest "
            "stroke, the document headed with authority and nothing wasted."
        ),
    },
    {
        "key": "bananeira",
        "name": "Bananeira: The Handstand",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The bananeira - the banana tree - is capoeira's handstand: "
            "the fighter kicks up to a straight-body inverted balance on "
            "both hands, holds, and comes down with control. It is the "
            "foundation of all inverted capoeira - the pino, the headstand "
            "variations, the handstand walking of advanced play all grow "
            "from a solid bananeira. In the roda it serves as a dodge (the "
            "body inverts under a high attack), a transition (handstand "
            "into a spin or a kick), and pure expression - the moment the "
            "game turns acrobatic. The straight body line is the whole "
            "technique: banana-curved backs wobble and collapse, while a "
            "stacked line balances almost effortlessly. Beginners kick up "
            "too hard and crash over; the correction is a controlled kick "
            "to the wall, learning the balance point gradually. This "
            "record teaches the kick-up, the stacked line, the finger "
            "balance, and the controlled descent."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. Stand facing a wall, place your hands flat "
            "on the floor shoulder-width apart, fingers spread, about a "
            "foot from the wall. 2. Kick one leg up toward the wall with "
            "control - not a wild throw - letting the wall catch you; the "
            "other leg follows to meet it. 3. Stack the body: hands under "
            "shoulders, shoulders over hips, hips over hands - squeeze the "
            "glutes and point the toes to lock the line straight. 4. "
            "Balance with the fingers: press the fingertips to pull "
            "yourself back from tipping forward, ease off to let yourself "
            "come forward - the fingers are the steering. 5. Come down "
            "with control: lower one leg at a time back to the floor, or "
            "tuck and roll out if you overbalance. 6. Practice daily: five "
            "wall kick-ups, then attempt freestanding holds, adding seconds "
            "as the finger balance develops. The bananeira is correct when "
            "the body stacks straight, the fingers do the balancing, and "
            "you can hold ten seconds freestanding."
        ),
        "key_points": [
            "The stacked line is everything: hands under shoulders under hips - a straight body balances, a banana back collapses.",
            "The fingers steer: press the fingertips to correct forward tip, ease off to correct backward tip.",
            "Kick up with control to a wall first; wild kick-ups teach crashing, not balancing.",
            "Squeeze the glutes and point the toes to lock the line - a tight body is a stable body.",
            "The bananeira is the root of all inverted capoeira: every advanced inversion grows from this hold.",
        ],
        "requirements": [
            "A clear wall and open floor space for kick-up practice.",
            "Wrist and shoulder warm-up - the hands and shoulders carry the full body.",
            "Five wall kick-ups per session before freestanding attempts.",
            "A spotter or crash mat for the first freestanding attempts.",
            "Daily short practice: handstand balance builds faster with frequency than with long sessions.",
        ],
        "standards": [
            "Learn against a wall before attempting freestanding handstands.",
            "Fingers spread, arms straight but not hyperextended, on every kick-up.",
            "Come down controlled - bail by cartwheeling out or tucking to roll, never by collapsing straight down.",
        ],
        "citations": [CIT_NESTOR, CIT_ALMEIDA],
        "sig_lens": (
            "The Signature read: the bananeira is the Signature inversion - "
            "the author turns the page upside down and balances on it. "
            "The Signature Combat Method stacks the line straight: hands, "
            "shoulders, hips, a signature written vertically. Held with "
            "finger-steered control, the inversion proves the author can "
            "sign from any angle."
        ),
    },
    {
        "key": "vingativa",
        "name": "Vingativa: The Sweeping Takedown",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The vingativa - the vengeful one - is capoeira's signature "
            "sweeping takedown: from a low crouch, the fighter hooks the "
            "partner's leg with their own and levers the upper body, "
            "toppling the partner sideways. It is the classic answer to "
            "aggression in the roda - the harder the partner pushes in, "
            "the cleaner the vingativa answers, using their momentum "
            "against them. Bimba taught it as a core takedown of Regional, "
            "and its mechanics are pure leverage: the sweeping leg removes "
            "the support while the hands and body redirect the weight. "
            "Done correctly the partner falls controlled to the side; done "
            "with muscling instead of leverage, it becomes a wrestling "
            "match. The vingativa teaches the deepest lesson of the "
            "takedown game: position beats strength. This record teaches "
            "the low entry, the leg hook, the body lever, and the "
            "controlled-fall partnership."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. As the partner steps or pushes in, drop low "
            "into a crouch beside their lead leg. 2. Hook your leg behind "
            "their lead ankle or calf - the hook is a cradle, not a kick. "
            "3. At the same instant, press your upper body and arms "
            "against their torso or hips, levering their weight over the "
            "hooked leg. 4. Sweep the hooked leg through while driving "
            "with the body - their support vanishes as their weight tips, "
            "and they fall sideways in a controlled arc. 5. Guide the fall: "
            "keep contact and help them land safely on their side - the "
            "vingativa is a takedown, not a slam. 6. Drill slowly with a "
            "cooperative partner: ten walk-throughs per side learning the "
            "hook-and-lever timing, then add speed gradually. The vingativa "
            "is correct when the partner falls from leverage, not force, "
            "and lands safely guided by your hands."
        ),
        "key_points": [
            "Leverage beats strength: the hooked leg removes support while the body levers the weight over it.",
            "It answers aggression with redirection - the harder the partner pushes in, the cleaner it works.",
            "The hook cradles the leg; it never kicks or chops at it.",
            "Guide every fall: the vingativa is a takedown, and the partner's safe landing is the thrower's responsibility.",
            "Position is everything - the low crouch beside the lead leg must be established before the lever fires.",
        ],
        "requirements": [
            "A cooperative partner and mats - takedowns are drilled on forgiving surfaces.",
            "Mastery of the low entries (esquiva baixa, role) first; the vingativa launches from the crouch.",
            "Ten slow walk-throughs per side before any speed.",
            "A partner trained to fall safely (side breakfall).",
            "The discipline to guide every fall - no dumping partners.",
        ],
        "standards": [
            "All takedown drilling happens on mats with a partner who can breakfall safely.",
            "The thrower guides the fall to a controlled side landing - slams are forbidden in drilling.",
            "Start at walk-through speed; add speed only when the lever timing is clean.",
        ],
        "citations": [CIT_NESTOR, CIT_ALMEIDA, CIT_DOWNEY],
        "sig_lens": (
            "The Signature read: the vingativa is the Signature reversal - "
            "the author's leverage turning the opponent's own momentum "
            "into the closing argument. The Signature Combat Method signs "
            "it low and clean: hook the premise, lever the conclusion, "
            "and guide the fall like an editor guiding a manuscript to "
            "its final form."
        ),
    },
    {
        "key": "chapa",
        "name": "Chapa: The Side Push Kick",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The chapa - the plate, the slab - is a side kick delivered "
            "with the full sole or the outside edge, driving laterally "
            "into the target. The fighter chambers the knee across the "
            "body, pivots the support foot, and thrusts the leg out "
            "sideways with the hips behind it - a flat slab of force. It "
            "is the mid-range stopper: when a partner circles or presses "
            "from the side, the chapa meets them with a wall. Unlike the "
            "spinning kicks it needs no rotation, which makes it fast to "
            "deploy and easy to recover - chamber, thrust, rechamber. The "
            "power comes from the hip thrust and the pivot of the support "
            "foot, which turns the body side-on and adds the full mass "
            "behind the sole. Beginners kick with the toes or forget the "
            "pivot, bleeding half the power; the correction is sole-first "
            "and pivot-always. This record teaches the cross-body chamber, "
            "the support pivot, the lateral thrust, and the rechamber."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. From the ginga, chamber the kicking knee up "
            "and across the body toward the opposite shoulder, guard high. "
            "2. Pivot on the ball of the support foot, turning the body "
            "side-on to the target - the heel of the support foot points "
            "at the target. 3. Thrust the leg out sideways, striking with "
            "the full sole (or outside edge), driving the hips into the "
            "kick - the leg extends in a straight lateral line. 4. Keep "
            "the ankle locked and toes pulled back so the sole is flat. "
            "5. Rechamber the knee back across the body and return to the "
            "ginga. 6. Drill on a heavy bag or shield at torso height: ten "
            "slow chamber-pivot-thrust reps per side, then ten driving "
            "reps. The chapa is correct when the bag moves laterally from "
            "hip thrust, the support heel pointed at the target, and the "
            "rechamber was instant."
        ),
        "key_points": [
            "The support-foot pivot turns the body side-on and puts the full mass behind the sole - no pivot, half power.",
            "Contact is the full flat sole or outside edge, driven laterally like a slab.",
            "The cross-body chamber hides the kick and loads the hip thrust.",
            "No spin means fast deployment and fast recovery - the chapa is the mid-range stopper.",
            "Rechamber instantly: the lateral line is strong but a hanging leg gets grabbed.",
        ],
        "requirements": [
            "A heavy bag or shield at torso height for thrust practice.",
            "Hip and groin warm-up; the lateral thrust opens the hip fully.",
            "Ten slow technical reps per side before driving reps.",
            "Smooth floor for the support-foot pivot.",
            "The pisao and bencao (records 8, 10) as the sole-contact foundation.",
        ],
        "standards": [
            "Full-power side kicks are for bags and shields; partner targets stay at controlled touch.",
            "Pivot on the ball of the support foot with the knee tracking over the toes.",
            "The guard stays up - the side-on body position tempts fighters to drop the far hand.",
        ],
        "citations": [CIT_NESTOR, CIT_ALMEIDA],
        "sig_lens": (
            "The Signature read: the chapa is the Signature slab - a flat "
            "lateral seal pressed against the argument's side. The "
            "Signature Combat Method pivots fully side-on before stamping: "
            "no half-turns, no partial seals. When the slab lands, the "
            "mid-range is officially closed."
        ),
    },
    {
        "key": "macaquinho",
        "name": "Macaquinho: The One-Handed Side Flip",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The macaquinho - the little monkey - is a one-handed side flip: "
            "the fighter plants a single hand, swings the legs up and over "
            "sideways in a tight arc, and lands on the feet. It is the "
            "compact, combat version of the au: lower, faster, and thrown "
            "in a single beat to dodge a low sweep or to launch an "
            "unexpected attack from an inverted moment. Where the au is a "
            "broad cartwheel, the macaquinho is a quick monkey-hop over "
            "danger - the body stays tight, the rotation is fast, and the "
            "landing is already moving. Advanced players chain macaquinhos "
            "across the floor and kick out of them mid-flip. The single "
            "hand plant demands wrist strength and precise timing: plant "
            "late and you clip the sweep; plant early and you stall. This "
            "record teaches the crouch entry, the single-hand plant, the "
            "tight leg swing, and the running landing."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. From a low crouch or the ginga, step "
            "sideways toward the flip direction and reach down with one "
            "hand - the hand plants flat, fingers spread, as the body "
            "commits. 2. Swing both legs up and over in a tight sideways "
            "arc, knees slightly tucked - the body stays compact, not "
            "spread like the au. 3. Push off the planted hand as the legs "
            "pass overhead, adding lift to the rotation. 4. Spot the floor "
            "and land on both feet, knees bent, already in motion - the "
            "macaquinho lands running, not posing. 5. Flow straight back "
            "into the ginga or into the next technique. 6. Build up: master "
            "the two-handed au first (record 17), then practice one-handed "
            "plants from a low crouch, then ten full macaquinhos per side "
            "on mats. The macaquinho is correct when the single hand plant "
            "feels solid, the arc stays tight, and the landing never "
            "paused."
        ),
        "key_points": [
            "One hand plants as the body commits - the timing of the plant is the whole technique.",
            "The body stays tight and compact through the flip; the au spreads, the monkey tucks.",
            "Push off the planted hand as the legs pass overhead for lift and speed.",
            "Land running: the macaquinho is a transit move, and a posed landing wastes it.",
            "It is the combat cartwheel - lower, faster, and built to dodge sweeps and launch surprise attacks.",
        ],
        "requirements": [
            "A reliable two-handed au (record 17) first - the macaquinho is its one-handed evolution.",
            "Mats for learning; the single-hand plant is unforgiving on hard floors.",
            "Wrist strengthening: the plant takes the full body on one hand.",
            "Ten reps per side on mats before open-floor attempts.",
            "A spotter for the first sessions.",
        ],
        "standards": [
            "Learn on mats with a spotter; the one-handed plant demands respect.",
            "The plant hand lands flat with spread fingers and a straight-but-not-locked arm.",
            "Land with bent knees and keep moving - stiff landings on one-hand flips jar the spine.",
        ],
        "citations": [CIT_NESTOR, CIT_DOWNEY],
        "sig_lens": (
            "The Signature read: the macaquinho is the Signature quick-"
            "flip - the author vaults the obstacle on one hand and keeps "
            "writing mid-air. The Signature Combat Method plants once, "
            "tucks tight, and lands running: the fastest signatures are "
            "signed without breaking stride."
        ),
    },
])

ENTRIES.extend([
    {
        "key": "meia_lua_compasso",
        "name": "Meia-Lua de Compasso: The Compass Crescent Kick",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "The meia-lua de compasso - the compass crescent - is capoeira's "
            "most iconic advanced kick: the fighter bends forward, plants "
            "both hands on the floor, and swings one leg in a huge "
            "horizontal arc around the body like a compass needle, "
            "striking with the heel. The hands on the ground are the "
            "compass's pivot point; the sweeping leg draws the circle. It "
            "is devastating because the whole bodyweight rotates behind "
            "the heel at head height, and it is spectacular because the "
            "fighter is essentially doing a one-legged cartwheel of "
            "destruction. Both Angola and Regional claim it, and both are "
            "right - it belongs to the art itself. The kick demands total "
            "commitment and superb balance: the hands must plant solidly, "
            "the supporting leg must drive the rotation, and the head must "
            "stay tucked to avoid the most common injury in capoeira, the "
            "compasso to the face of a partner who stepped in. This record "
            "teaches the hand plant, the pivot leg drive, the heel arc, "
            "and the strict spacing discipline."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. From the ginga, bend forward at the waist "
            "and plant both hands flat on the floor in front of you, "
            "fingers spread, arms straight - the hands are the compass "
            "pivot. 2. Kick one leg up and back while the support leg "
            "drives: the body inverts partially as the kicking leg begins "
            "its huge horizontal arc. 3. Swing the leg all the way around "
            "in a full circle at head height, striking with the heel - the "
            "rotation comes from the support leg's drive and the hip "
            "turnover, not from arm strength. 4. Keep the head tucked and "
            "the eyes finding the target as the leg comes around. 5. As "
            "the arc completes, the kicking leg comes down, the hands push "
            "off, and you rise back into the ginga. 6. Build up in stages: "
            "hand-plant and weight-shift drills first, then slow arcs with "
            "no target, then ten full arcs per side on a heavy bag. The "
            "compasso is correct when the heel draws a full level circle, "
            "the hands never slipped, and you rose back up balanced."
        ),
        "key_points": [
            "The hands are the compass pivot: planted flat and solid, they anchor the entire rotation.",
            "The heel draws a full horizontal circle at head height, driven by the support leg and hip turnover.",
            "The whole bodyweight rotates behind the heel - this is among the most powerful kicks in martial arts.",
            "Head tucked, eyes finding the target mid-arc: the compasso thrown blind is a danger to everyone.",
            "Spacing discipline is absolute: never throw it when a partner is inside the arc's radius.",
        ],
        "requirements": [
            "Mastery of the bananeira (record 21) and the armada (record 14) - the compasso fuses inversion with spin.",
            "A heavy bag for full-arc practice; the power needs a safe target.",
            "Wrist and shoulder strength for the double hand plant under rotation.",
            "A clear radius of at least three meters - the heel draws a full circle.",
            "Ten slow no-target arcs per side before any bag contact.",
        ],
        "standards": [
            "Full-power compass kicks are for bags only; partner work is slow arcs at touch distance or no-contact.",
            "Never throw the compasso in a crowded roda - the arc's radius must be clear of all bodies.",
            "The hands plant flat with spread fingers; the head tucks before the leg swings.",
        ],
        "citations": [CIT_NESTOR, CIT_ALMEIDA, CIT_TAYLOR],
        "sig_lens": (
            "The Signature read: the meia-lua de compasso is the Signature "
            "compass - the author plants both hands and draws a perfect "
            "circle of authority around the argument. The Signature Combat "
            "Method treats the arc as a boundary signed in heel: everything "
            "inside the circle is the author's jurisdiction."
        ),
    },
    {
        "key": "s_dobrado",
        "name": "S-Dobrado: The Folded S Ground Escape",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "The S-dobrado - the folded S - is the ground escape that "
            "folds the body into an S shape to slip out from under "
            "pressure: from a low position, the fighter threads the body "
            "through a tight S-curve - hips one way, shoulders the other - "
            "sliding out from beneath an attack or a pin and emerging on "
            "the far side already moving. It is the eel of capoeira's "
            "ground game: where the role spins around pressure, the "
            "S-dobrado slides through it, the body folding and unfolding "
            "like a ribbon. Angola's floor masters use it to escape the "
            "tightest spots in the slow game, turning a trapped position "
            "into a reversal in one fluid fold. The technique demands "
            "extreme body awareness and spinal mobility - the fold is "
            "precise, and muscling it jams the very joints it needs. This "
            "record teaches the S-fold shape, the threading motion, the "
            "breath timing, and the emerge-moving finish."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. From a low crouch or negativa under "
            "pressure, exhale and fold: send the hips one direction and "
            "the shoulders the opposite, forming the S shape with your "
            "spine. 2. Thread the body through the gap - under the "
            "partner's arm, around their leg, through whatever space the "
            "pressure leaves - leading with the hips, the head last. "
            "3. Keep the movement continuous and fluid: the fold flows "
            "into the slide flows into the unfold, one breath, one motion. "
            "4. As you emerge on the far side, unfold into a crouch or "
            "negativa already facing the partner - never emerge flat or "
            "turned away. 5. Immediately move: the escape buys one beat, "
            "and the S-dobrado's finish is a launch, not a rest. 6. Drill "
            "the fold slowly on open floor first: ten S-folds per side "
            "learning the shape; then have a partner apply light pressure "
            "from above while you thread out. The S-dobrado is correct "
            "when the fold is smooth, the thread needed no force, and you "
            "emerged already moving."
        ),
        "key_points": [
            "The body folds into an S - hips one way, shoulders the other - and threads through pressure like an eel.",
            "Lead with the hips, head last: the head leads into collisions, the hips lead into escapes.",
            "One breath, one motion: the fold, slide, and unfold are continuous - stopping mid-fold strands you.",
            "Emerge already moving into a guard or launch; the escape buys exactly one beat.",
            "It is the precision escape of the ground game: technique and mobility, never force.",
        ],
        "requirements": [
            "Spinal mobility: daily cat-cow, side bends, and hip openers before attempting the fold.",
            "Mastery of the negativa and role (records 18-19) - the S-dobrado launches from the low game.",
            "A cooperative partner applying gradual pressure for escape drilling.",
            "Ten slow S-folds per side on open floor before pressure drilling.",
            "Mats for the pressure-escape practice.",
        ],
        "standards": [
            "Pressure drilling stays light and cooperative; the escape is technique, not a contest.",
            "Warm the spine thoroughly - the fold demands mobility and cold backs do not fold.",
            "Stop for any sharp spinal pain; the S-dobrado is a mobility technique, never forced.",
        ],
        "citations": [CIT_TAYLOR, CIT_DOWNEY],
        "sig_lens": (
            "The Signature read: the S-dobrado is the Signature eel - the "
            "author folds the argument into an S and slips through the "
            "premise's grip. The Signature Combat Method signs the escape "
            "in one breath: fold the claim, thread the gap, emerge writing. "
            "Pressure, properly folded, becomes passage."
        ),
    },
    {
        "key": "parafuso",
        "name": "Parafuso: The Corkscrew Kick",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The parafuso - the corkscrew, the screw - is a jumping "
            "spinning kick: the fighter leaps, rotates 360 degrees in the "
            "air, and drives a kick out mid-rotation, landing back on the "
            "feet. It is the tornado kick of capoeira, and it compresses "
            "the armada's full spin into a single airborne beat - jump, "
            "spin, kick, land. Regional's fast game showcases it as the "
            "pinnacle of the spinning arsenal, thrown when the fighter "
            "has space and the partner is set. The physics are unforgiving: "
            "the jump must be high enough to complete the rotation, the "
            "spin must be tight enough to finish before landing, and the "
            "kick must extend at exactly the right moment or the landing "
            "absorbs a tangled mess. Beginners under-rotate and land "
            "twisted; the correction is jump height first, spin second, "
            "kick last. This record teaches the loaded jump, the tight "
            "tuck-spin, the timed extension, and the two-foot landing."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. From the ginga, take a small preparatory "
            "step and load the legs like a spring, arms swinging to drive "
            "the rotation. 2. Jump straight up with maximum height - "
            "height is time, and time is rotation. 3. Tuck tight "
            "immediately: knees to chest, arms pulled in, the body a "
            "compact spinning mass - the tuck is what completes the 360. "
            "4. At the three-quarter mark of the spin, extend the kicking "
            "leg out to strike, then snap it back. 5. Spot the floor and "
            "land on both feet, knees deeply bent to absorb, guard up. "
            "6. Build in stages: jump-and-tuck spins with no kick first "
            "(ten reps), then add the leg extension on a high pad, then "
            "ten full parafuso reps per side on the bag. The parafuso is "
            "correct when the full 360 completes before landing, the kick "
            "extended on time, and the landing was balanced and guarded."
        ),
        "key_points": [
            "Jump height is rotation time: the higher the leap, the more complete the 360 - height first, spin second, kick last.",
            "The tight tuck is the engine of the spin; a loose body under-rotates and lands twisted.",
            "Extend the kick at the three-quarter mark and snap it back - timing, not height of the kick, is the skill.",
            "Land on both feet with deep knee bend, guard up; the landing is part of the technique.",
            "It is the airborne armada: the entire spinning arsenal compressed into one jump.",
        ],
        "requirements": [
            "A reliable armada (record 14) and strong jump - the parafuso is the spin taken airborne.",
            "Plyometric leg strength: box jumps and tuck jumps in the conditioning program.",
            "Mats for learning; the landings are demanding.",
            "Ten jump-tuck spins without the kick before adding the extension.",
            "A high pad or bag for the timed extension practice.",
        ],
        "standards": [
            "Learn on mats; the jump-spin-landing sequence punishes hard floors.",
            "Land with knees bent and tracking over the toes - never land stiff-legged.",
            "Full-power airborne kicks are for bags and pads; partner work stays at touch on pads.",
        ],
        "citations": [CIT_NESTOR, CIT_ALMEIDA],
        "sig_lens": (
            "The Signature read: the parafuso is the Signature corkscrew - "
            "the author leaps, signs a full circle in the air, and lands "
            "with the document sealed. The Signature Combat Method treats "
            "the jump as the pen lifting, the spin as the stroke, the kick "
            "as the dot: one airborne signature, complete before landing."
        ),
    },
    {
        "key": "mortal",
        "name": "Mortal: The Standing Back Flip",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The mortal - the deadly one, the back flip - is the standing "
            "backward somersault: from the ginga the fighter drops, jumps, "
            "tucks, rotates fully backward in the air, and lands on the "
            "feet. It is capoeira's most dramatic dodge and its boldest "
            "statement - a full back flip thrown to evade an attack, "
            "cross the floor, or punctuate the game. In the roda it is "
            "rarely a practical defense; it is expression, courage, and "
            "the proof of complete aerial control. But its training builds "
            "the tuck, the spatial awareness, and the landing mechanics "
            "that every advanced inversion needs. The mortal demands "
            "respect above all techniques in this database: learned wrong "
            "it injures the neck and spine, learned right - with a spotter, "
            "on mats, in strict stages - it becomes the crown of the "
            "acrobatic game. This record teaches the staged progression, "
            "the tuck timing, and the non-negotiable safety protocol."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. STAGE ONE (weeks): on mats with a trained "
            "spotter, practice the jump-tuck-land on the spot - jump up, "
            "tuck knees hard to chest, land on both feet with deep knee "
            "bend. 2. STAGE TWO: with the spotter's hands on your back, "
            "add the backward rotation - the spotter guides the flip while "
            "you commit the tuck. 3. STAGE THREE: spotted full mortals, "
            "ten clean reps before any solo attempt. 4. STAGE FOUR: solo "
            "on mats, then on firm floor only when the solo mat mortal is "
            "automatic. 5. The mechanics: drop low, swing the arms up hard, "
            "jump UP (not back), tuck violently at the peak, spot the floor "
            "behind you, open slightly, and land soft with knees bent. "
            "6. Never throw it tired, never without warm-up, never without "
            "a spotter until stage four is earned. The mortal is correct "
            "when every stage was completed in order and the solo flip "
            "lands quiet and balanced."
        ),
        "key_points": [
            "The mortal is learned in four strict stages - jump-tuck, spotted rotation, spotted full, solo - never skipped.",
            "Jump UP, not back: height gives the rotation time; jumping back throws the landing away.",
            "The violent tuck at the peak is the rotation engine; a loose tuck is an incomplete flip.",
            "A spotter and mats are mandatory until the solo mat mortal is automatic - this is non-negotiable.",
            "Its training builds the aerial control every advanced inversion needs, whether or not it is ever thrown in the roda.",
        ],
        "requirements": [
            "A trained spotter who knows back-flip spotting - not a friend, a coach.",
            "Mats (crash mat minimum) for all stages until stage four is earned.",
            "The bananeira and tuck jumps mastered first - the mortal needs inversion comfort and jump power.",
            "Ten clean reps at each stage before advancing.",
            "Full warm-up every session; never attempt tired or cold.",
        ],
        "standards": [
            "Spotter and mats mandatory through stage three; solo attempts only after ten clean spotted full mortals.",
            "Stop for any neck pain, headache, or hard landing - the mortal punishes fatigue.",
            "The chin tucks through the rotation; the head never throws back independently.",
        ],
        "citations": [CIT_NESTOR, CIT_DOWNEY],
        "sig_lens": (
            "The Signature read: the mortal is the Signature somersault - "
            "the author flips the entire page and lands with the signature "
            "still legible. The Signature Combat Method earns it in four "
            "stages, because the boldest signatures are practiced in "
            "private before they are ever thrown in public."
        ),
    },
    {
        "key": "au_sem_mao",
        "name": "Au sem Mao: The No-Hand Cartwheel",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The au sem mao - the cartwheel without hands - is the aerial "
            "cartwheel: the full lateral rotation performed with no hand "
            "touching the floor, the body airborne through the entire "
            "flip. It is the au liberated from the ground, and it turns "
            "the escape into pure flight - dodging under nothing, over "
            "everything, and landing already in motion. Advanced players "
            "use it to cross the roda in a beat, to dodge low sweeps with "
            "contemptuous ease, and to launch kicks from a rotation no "
            "hand ever touched. The technique lives or dies on the takeoff: "
            "the legs must drive hard enough to carry the full rotation, "
            "and the body must stay rigid in the split position - any fold "
            "mid-air collapses the arc. It is the natural summit of the "
            "cartwheel ladder: au, macaquinho, au sem mao. This record "
            "teaches the driving takeoff, the rigid airborne split, the "
            "spotting, and the staged progression from hand-assisted "
            "versions."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. Master the progression first: clean au "
            "(record 17), then one-handed au touching only at the end, "
            "then delayed-hand-touch versions where the hand lands late. "
            "2. From the ginga, step deep sideways and drive explosively "
            "off the legs - the takeoff is a powerful lateral leap, not a "
            "tip-over. 3. Throw the body into the lateral rotation with "
            "the legs split wide and the torso rigid - hold the split "
            "position in the air like a star. 4. Spot the floor through "
            "the rotation; the head stays neutral, guiding the landing. "
            "5. Land on the lead leg first, absorb deeply, and flow "
            "straight into the ginga or the next move. 6. Practice on mats "
            "with a spotter: ten attempts focusing on the drive, then ten "
            "focusing on holding the rigid split, then full clean reps. "
            "The au sem mao is correct when no hand brushed the floor, "
            "the split stayed rigid, and the landing flowed without a "
            "stumble."
        ),
        "key_points": [
            "The takeoff is a powerful lateral leap - the legs must drive hard enough to carry the full rotation airborne.",
            "Hold the rigid split in the air: any fold mid-flight collapses the arc.",
            "It is the summit of the cartwheel ladder: au to one-hand au to delayed-touch to no-hands.",
            "No hand touches the floor at any point - the escape becomes pure flight.",
            "Land into motion: the no-hand cartwheel that lands posing has wasted its speed.",
        ],
        "requirements": [
            "A clean two-handed au and a reliable one-handed au first - the progression is mandatory.",
            "Explosive leg power: lateral bounds and plyometric training.",
            "Mats and a spotter for all learning attempts.",
            "Ten reps at each progression stage before advancing.",
            "Open space: the airborne rotation travels further than the grounded au.",
        ],
        "standards": [
            "Progress through the hand-assisted stages in order; never attempt the no-hand version cold.",
            "Mats and spotter mandatory until the no-hand cartwheel is clean and repeatable.",
            "Land with bent knees into motion - stiff landings from aerial rotations jar the spine.",
        ],
        "citations": [CIT_NESTOR, CIT_DOWNEY],
        "sig_lens": (
            "The Signature read: the au sem mao is the Signature flight - "
            "the author signs the full circle without touching the page. "
            "The Signature Combat Method treats it as the purest "
            "signature: no hand, no prop, just the body's arc drawn in "
            "air, landing already writing the next line."
        ),
    },
    {
        "key": "chamada",
        "name": "Chamada: The Call Ritual of the Roda",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The chamada - the call - is the ritual challenge of the "
            "Angola roda: one player stops the game, extends their hands "
            "toward the partner in a stylized invitation, and walks forward "
            "or backward in a slow, deliberate approach. The partner must "
            "answer the call - stepping in, mirroring the ritual - and the "
            "two advance on each other in a tense, theatrical standoff "
            "until one breaks the ritual with an attack. It is pure "
            "malicia made formal: a test of nerve, timing, and reading, "
            "where the real game is the waiting. The chamada teaches what "
            "no kick can - composure under pressure, the discipline to not "
            "flinch, and the art of launching an attack from absolute "
            "stillness. Refusing the call or breaking it clumsily is a "
            "loss of face in the traditional roda. This record teaches the "
            "invitation posture, the approach, the answering protocol, and "
            "the break - when and how the ritual ends."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. To issue the chamada, stop your ginga, face "
            "your partner squarely, and extend both hands forward, palms "
            "open, in the traditional invitation - the body upright and "
            "calm. 2. Advance slowly toward the partner (or beckon them "
            "to you), maintaining eye contact and absolute composure - "
            "the walk is deliberate, unhurried. 3. To answer: step in and "
            "mirror the posture, hands raised to meet theirs, and join the "
            "slow approach - never refuse the call in a traditional roda. "
            "4. Maintain the ritual tension: both players advance, hands "
            "nearly touching, each reading the other for the break. "
            "5. The break: one player explodes out of the ritual into an "
            "attack - a kick, a sweep, a dodge - and the game resumes at "
            "full speed. 6. Practice the ritual slowly with a partner: ten "
            "call-and-answer approaches focusing on composure, then "
            "practice breaking cleanly with a controlled technique. The "
            "chamada is correct when the approach was calm, the answer was "
            "honest, and the break was decisive."
        ),
        "key_points": [
            "The chamada is a formal test of nerve: the real game is the waiting, not the attack.",
            "Answering is mandatory in the traditional roda - refusing the call is a loss of face.",
            "Composure is the technique: the player who flinches or rushes loses before the break.",
            "The break must be decisive - exploding from stillness into a clean, controlled attack.",
            "It teaches what kicks cannot: stillness under pressure and the launch from zero.",
        ],
        "requirements": [
            "Understanding of roda etiquette - the chamada belongs to the traditional game, learned from a mestre.",
            "A trusted partner for the slow approach practice.",
            "Composure drilling: practice the walk without breaking into nervous movement.",
            "Ten slow call-and-answer approaches before practicing the break.",
            "The break practiced with controlled techniques only - the ritual ends, the partnership does not.",
        ],
        "standards": [
            "The chamada is practiced under a mestre's guidance; its etiquette is traditional and specific.",
            "Breaks stay controlled - the ritual's tension never justifies a reckless attack on a partner.",
            "Both players maintain the ritual honestly; faking the answer breaks the tradition.",
        ],
        "citations": [CIT_TAYLOR, CIT_DOWNEY, CIT_UNESCO],
        "sig_lens": (
            "The Signature read: the chamada is the Signature summons - "
            "the author formally calls the reader to the page. The "
            "Signature Combat Method treats the slow approach as the most "
            "honest negotiation in combat: no feints, no noise, just two "
            "signatures advancing until one signs first. Composure is the "
            "ink."
        ),
    },
    {
        "key": "malicia",
        "name": "Malicia: The Art of Deception",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Malicia - malice, cunning, street wisdom - is the strategic "
            "soul of capoeira: the art of deception, of showing one thing "
            "and doing another, of letting the partner defeat themselves. "
            "It is not a technique but the intelligence behind all "
            "techniques: the feinted kick that draws the dodge before the "
            "real kick arrives, the relaxed posture that hides the loaded "
            "spring, the smile that masks the trap. Mestre Pastinha, the "
            "great Angola master, taught that capoeira is malicia above "
            "all - the physical game is just its theater. Malicia is "
            "learned, not taught: it grows from years in the roda, from "
            "being tricked and learning to trick, from studying partners "
            "until their habits become your weapons. It has an ethics - "
            "deception in the game, honesty outside it - and the traditional "
            "roda punishes the player who confuses the two. This record "
            "teaches the feint mechanics, the pattern-breaking habit, the "
            "reading of tells, and the ethics of the trick."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. Build the library first: play hundreds of "
            "exchanges and catalog what partners do - the dodge they favor, "
            "the kick they telegraph, the side they protect. 2. Practice "
            "the mechanical feint: begin a real technique (a queixada, a "
            "ponteira) with full commitment of the first third of the "
            "motion, then convert - the feint must be indistinguishable "
            "from the real thing until the branch point. 3. Break your own "
            "patterns deliberately: if you always follow a dodge with the "
            "same kick, change it - malicia starts with unpredictability "
            "in yourself. 4. Learn the two-beat trap: show the partner a "
            "weakness twice so they commit to exploiting it, then punish "
            "the exploitation on the third. 5. Study tells: the weight "
            "shift before the kick, the eye flick before the dodge - and "
            "then plant false tells of your own. 6. Drill feint-then-real "
            "combinations with a partner: ten reps where the feint must "
            "draw a real reaction before the true technique lands. Malicia "
            "is correct when partners start hesitating - and hesitation is "
            "the sound of your deception working."
        ),
        "key_points": [
            "Malicia is the intelligence behind all technique: showing one thing, doing another, letting the partner defeat themselves.",
            "A feint must be indistinguishable from the real technique until the branch point - a lazy feint fools no one.",
            "Break your own patterns first: unpredictability in yourself is the foundation of deception.",
            "The two-beat trap - showing a weakness twice, punishing its exploitation on the third - is the classic malicia structure.",
            "It has an ethics: deception belongs in the game; the roda punishes those who carry the trick outside it.",
        ],
        "requirements": [
            "Years of roda time - malicia grows from being tricked as much as from tricking.",
            "A repertoire of real techniques (this database's ladder) - you cannot feint what you cannot do.",
            "A variety of partners: malicia needs many habits to study.",
            "Deliberate pattern-breaking practice in every session.",
            "A mestre's guidance on the ethics - the tradition draws the line clearly.",
        ],
        "standards": [
            "Deception stays inside the game; outside the roda, the capoeirista is honest - the tradition is explicit.",
            "Feint drilling with partners stays at controlled contact; tricks never justify reckless force.",
            "Study under a mestre: malicia's ethics and application are transmitted person to person.",
        ],
        "citations": [CIT_DOWNEY, CIT_TAYLOR, CIT_ASSUNCAO],
        "sig_lens": (
            "The Signature read: malicia is Signature wit - the author's "
            "cunning written between the lines. The Signature Combat "
            "Method treats deception as the highest literacy: read the "
            "partner's habits like text, write false tells like fiction, "
            "and let the two-beat trap close like a well-made argument. "
            "The cleverest signature is the one they never saw coming."
        ),
    },
    {
        "key": "jogo_angola",
        "name": "Jogo de Angola: The Slow Close Game",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The jogo de Angola - the Angola game - is capoeira's slow, "
            "low, close ritual: played near the floor at a walking tempo, "
            "it is chess to Regional's boxing. Named for the Angolan roots "
            "the art claims, the Angola game unfolds in the baixa and the "
            "negativa, in long balanco sways and sudden low explosions, "
            "with the berimbau playing the slow Sao Bento Grande de "
            "Angola rhythm. Mestre Pastinha's Centro Esportivo de Capoeira "
            "Angola preserved it as the art's deepest expression: a game "
            "where patience defeats speed, where the player who waits "
            "longest wins, where a single well-timed rasteira erases ten "
            "minutes of posturing. The Angola game demands everything this "
            "database teaches - low dodges, ground flow, sweeps, malicia - "
            "and adds the one thing no drill can give: the willingness to "
            "wait. This record teaches the tempo, the low vocabulary, the "
            "waiting discipline, and the explosion timing."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. Enter the roda low: the Angola game starts "
            "in the crouch, not standing tall - settle into the baixa "
            "with the guard alive. 2. Play the slow tempo: long balanco "
            "sways, deep roles, patient negativas - let minutes pass in "
            "the low game without forcing. 3. Stay close: the Angola game "
            "is played at arm's length, circling, hands nearly touching, "
            "reading the partner's weight. 4. Wait for the true opening - "
            "the overcommitted step, the lazy hand, the impatient attack - "
            "and explode once: a rasteira sweep, a low kick, a vingativa, "
            "delivered with total commitment. 5. Return immediately to the "
            "slow game; the explosion is a punctuation, not a new tempo. "
            "6. Train it in slow rounds: ten-minute games at half tempo "
            "with a partner, forbidden to rush, scoring only clean low "
            "techniques. The jogo de Angola is correct when you can play "
            "ten patient minutes, explode once decisively, and settle "
            "back without a change in breathing."
        ),
        "key_points": [
            "Tempo is the weapon: the slow game defeats speed by refusing to play at speed.",
            "The vocabulary is low - baixa, role, negativa, rasteira - and the closer the better.",
            "Patience is a trained skill: ten-minute slow rounds build the waiting muscle.",
            "One explosion, total commitment, then immediate return to slowness - punctuation, not tempo change.",
            "Mestre Pastinha's lineage treats it as the art's deepest expression: the game where waiting wins.",
        ],
        "requirements": [
            "The full low-game ladder: esquiva baixa, role, negativa, rasteira-family sweeps.",
            "A partner willing to play slow - the Angola game cannot be trained alone.",
            "Ten-minute slow rounds as a regular practice format.",
            "Study of the Sao Bento Grande de Angola rhythm and its etiquette.",
            "Guidance from the Angola lineage - the game's subtleties are transmitted in the roda.",
        ],
        "standards": [
            "The slow game is trained slow: rushing an Angola round defeats its purpose.",
            "Low techniques stay controlled; the explosion is decisive but never reckless.",
            "Respect the lineage: the Angola game carries Pastinha's tradition and its etiquette.",
        ],
        "citations": [CIT_TAYLOR, CIT_ASSUNCAO, CIT_UNESCO],
        "sig_lens": (
            "The Signature read: the jogo de Angola is the Signature slow "
            "draft - the author writes deliberately, low and close, and "
            "lets patience do the arguing. The Signature Combat Method "
            "treats waiting as a signature stroke: ten minutes of calm "
            "prose, one decisive sentence, and the page is won without "
            "ever raising the voice."
        ),
    },
    {
        "key": "jogo_regional",
        "name": "Jogo de Regional: The Fast Upright Game",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The jogo de Regional - the Regional game - is capoeira's fast, "
            "upright, athletic expression: created by Mestre Bimba in the "
            "1930s in Bahia, it stands the fighter up, quickens the "
            "berimbau to the rapid Sao Bento Grande de Regional, and "
            "unleashes the full spinning arsenal at speed. Where Angola "
            "waits, Regional attacks; where Angola flows low, Regional "
            "flies high with armadas, queixadas, martelos, and parafuso "
            "chains. Bimba systematized it with sequences, graduations, "
            "and rigorous training - the first capoeira academy, Luta "
            "Regional Baiana, made the art a disciplined method. The "
            "Regional game demands supreme conditioning: the pace is "
            "relentless, the kicks are full-power, and the exchanges run "
            "in combinations, not singles. This record teaches the upright "
            "stance, the combination logic, the conditioning base, and "
            "Bimba's sequence framework."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. Stand tall in an athletic ginga: higher "
            "than Angola's crouch, bouncy, ready to launch - the Regional "
            "stance is a sprinter's set. 2. Attack in combinations, not "
            "singles: queixada-armada, martelo-ponteira, bencao-chapa - "
            "every kick sets up the next, and the spin of one loads the "
            "spin of the other. 3. Keep the tempo brutal: three-minute "
            "rounds at full pace, the berimbau driving - rest is for "
            "between rounds, never inside them. 4. Use the full upright "
            "arsenal: high spinning kicks, jumping attacks, fast esquivas "
            "that stay standing. 5. Drill Bimba's sequences (record 34) "
            "until the combinations are reflex - Regional is a system, and "
            "the system is the sequences. 6. Condition relentlessly: the "
            "Regional game is won by the fighter still kicking hard in "
            "the third minute. The jogo de Regional is correct when your "
            "combinations flow without thought, your pace never drops, "
            "and the third round looks like the first."
        ),
        "key_points": [
            "Combinations, not singles: every kick sets up the next, and spins chain - the system is the sequence.",
            "The stance is tall and athletic, the tempo relentless: three-minute rounds at full pace.",
            "Mestre Bimba created it as a disciplined method - sequences, graduations, academy training.",
            "The full upright arsenal flies: high spins, jumping kicks, standing dodges.",
            "Conditioning is the foundation: the Regional game is won by the fighter still dangerous in round three.",
        ],
        "requirements": [
            "The full kicking ladder (records 7-16, 25-27) - Regional deploys the entire arsenal.",
            "Serious conditioning: running, jump rope, and round-based kick training.",
            "Bimba's sequences (record 34) drilled to reflex.",
            "A fast berimbau rhythm or metronome for tempo training.",
            "Three-minute round structure in every session.",
        ],
        "standards": [
            "Full-power combination rounds are for bags, pads, and controlled partner work - never wild.",
            "Condition gradually: the Regional pace injures the underprepared - build rounds over weeks.",
            "Respect Bimba's method: the sequences are the curriculum, drilled in order.",
        ],
        "citations": [CIT_ALMEIDA, CIT_ASSUNCAO, CIT_NESTOR],
        "sig_lens": (
            "The Signature read: the jogo de Regional is the Signature "
            "sprint - the author writing at full speed, combinations "
            "chaining like sentences that refuse to end. The Signature "
            "Combat Method treats the fast game as fluent authorship: "
            "conditioned, sequenced, and still sharp in the third round, "
            "the signature as legible at speed as at rest."
        ),
    },
    {
        "key": "sequencia_bimba",
        "name": "Sequencia de Bimba: The Eight Teaching Sequences",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The sequencia de Bimba - Bimba's sequences - are the eight "
            "partner sequences Mestre Bimba created as the curriculum of "
            "Capoeira Regional: each sequence is a fixed attack-and-defense "
            "exchange that teaches a complete lesson. Sequence one: "
            "meia-lua de frente, cocorinha, and the counter. The sequences "
            "progress through esquivas, kicks, sweeps, takedowns, and "
            "clinch work, each building on the last, until the student has "
            "a complete fighting vocabulary drilled to reflex. They are "
            "practiced slowly and precisely first, then at speed, then "
            "with variations - and the graduation system of Regional is "
            "built on demonstrating them. The sequences are the reason "
            "Regional could be taught systematically: Bimba compressed the "
            "art's essentials into eight memorizable forms. This record, "
            "the capstone of the database, teaches the sequence method, "
            "the eight-lesson arc, the precision-first protocol, and the "
            "path from fixed form to free play."
        ),
        "how_it_works": (
            "HOW TO DO IT. 1. Learn sequence one slowly with a partner: "
            "attacker throws the meia-lua de frente, defender answers with "
            "the cocorinha and the prescribed counter - walk it through "
            "ten times before adding any speed. 2. Add sequences in order: "
            "each introduces new material (esquivas, queixada, armada, "
            "sweeps, takedowns, clinch) while reviewing the old - never "
            "skip ahead. 3. Drill for precision first: the sequences are "
            "forms, and sloppy forms teach sloppy reflexes - speed comes "
            "only after precision is automatic. 4. Practice both roles: "
            "every student learns the attack and the defense of each "
            "sequence. 5. Once all eight are clean at speed, begin the "
            "variations: break the sequence at any point and improvise - "
            "this is the bridge from form to free jogo. 6. Test in the "
            "roda: the sequences should surface as reflexes inside free "
            "play. The sequencia de Bimba is correct when all eight run "
            "clean at speed from either role, and the free game starts "
            "showing sequence fragments on its own."
        ),
        "key_points": [
            "Eight fixed partner sequences form the complete Regional curriculum - attack, defense, and counter in each.",
            "Learn in order, both roles, precision before speed: sloppy forms teach sloppy reflexes.",
            "The sequences compress the art's essentials into memorizable form - Bimba's systematizing genius.",
            "Variations come after mastery: breaking the sequence to improvise is the bridge to free play.",
            "The capstone test: sequences surfacing as reflexes inside the free roda game.",
        ],
        "requirements": [
            "The full technique ladder of this database - the sequences assume it.",
            "A dedicated partner for sequence drilling, practicing both roles.",
            "Ten clean slow reps per sequence before adding speed.",
            "All eight sequences in order - the curriculum is sequential.",
            "A mestre or senior student to correct the forms; the sequences are precise.",
        ],
        "standards": [
            "Sequences are drilled slowly and precisely first; speed is earned, never assumed.",
            "Both partners practice both roles - the curriculum is symmetric.",
            "Contact in sequence drilling stays controlled; the forms teach timing, not damage.",
        ],
        "citations": [CIT_ALMEIDA, CIT_ASSUNCAO, CIT_NESTOR],
        "sig_lens": (
            "The Signature read: the sequencia de Bimba is the Signature "
            "curriculum - eight lessons, signed in order, forming the "
            "complete author. The Signature Combat Method treats Bimba's "
            "eight as the master class in authorship: learn every stroke "
            "in sequence, practice both sides of every exchange, and the "
            "free game writes itself. The database ends where the "
            "signature becomes fluent."
        ),
    },
])
