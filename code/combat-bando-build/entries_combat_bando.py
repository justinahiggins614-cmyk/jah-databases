#!/usr/bin/env python3
"""Entries for the Bando Combat databases (Manon's combat orders 2026-10-17,
combat batch 3).

Terminology fact-checked 2026-10-17 against Wikipedia 'Bando' (nine ABA
animal systems - bull, boar, cobra, viper, python, panther, tiger, scorpion,
eagle; aka = empty-handed forms/kata; basics taught as stances and footholds
for months; black belt requires aka, stick weapons, bladed weapons,
sparring, and a fitness test with minimum five years training; belts white,
green, brown, black with yellow as advanced white in some schools; Maung
Gyi taught Hanthawaddy bando in Washington DC from the early 1960s), the
'Bando' encyclopedia entries (9x9 technique-principle matrix; the student
grasps underlying principles because one technique fits one situation but
the principle fits many; boar = furious powerful rushes, cobra = lightning
fast strikes to vital targets, python = wraps and crushes; strategies
emulated, not mimicry; free fighting/middle style similar to tournament
karate; related arts lethwei bareknuckle striking and naban Burmese
wrestling), and the seven thaing systems list (bando empty-hand combat,
banshay weapons, lethwei, naban grappling, shan thaing soft/internal,
khut thaing pressure point techniques, arweththa mental discipline).

Creates two NEW databases, 34 ladder-ordered records each:

  combat-bando              - The Bando Combat Database
                              (public-harvest: real, fact-checked Burmese
                              bando - the hand-to-hand complement to the
                              thaing weapon arts - each record a technique
                              with HOW TO DO IT step-by-step body mechanics,
                              ladder-ordered from basics to advanced;
                              civilian traditional-art scope)
  combat-bando-signature    - The Bando Combat Signature Database
                              (his original Signature combat method: the
                              empty hand as the signature itself, every
                              technique a covenant of balance, the nine
                              animal strategies as nine covenants; src
                              signature, titles suffixed " (Signature
                              Edition)", clearly labeled Signature-made,
                              never presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBBD- (public) and JAH-CBBDS- (signature), verified free
in the manifest id_prefix values and in every shard index file (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_bando.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos before writing
pages.

CONCURRENCY: this builder never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes.
A merger handles those. Only db/combat-bando*/, code/combat-bando-build,
the shard data dirs, and the fragment file are written.

Never the words "bat belt" anywhere. No website references. No Facebook.

SCREENING: civilian traditional-art instruction only - nothing
hate-adjacent, profane, or inappropriate; no religious talk; nothing on
neutralizing or defeating military or defense-grade systems.
"""

SIG_TAIL = ("Signature original - his original Signature combat method: the "
            "empty hand as the signature itself, every technique a covenant "
            "of balance, the nine animal strategies as nine covenants, the "
            "stance the first covenant and mastery the final signature. "
            "Clearly labeled Signature-made, never presented as authentic "
            "public record.")

CIT_MAUNGGYI = ("Maung Gyi. Bando: Philosophy, Principles and Practice. "
                "Xlibris Corporation; 2000.")
CIT_WIKI_BANDO = ("Wikipedia contributors. Bando. Wikipedia, The Free "
                  "Encyclopedia; accessed 2026-10-17.")
CIT_ABA = ("American Bando Association. Bando training: the nine animal "
           "systems (bull, boar, cobra, viper, python, panther, tiger, "
           "scorpion, eagle), aka empty-handed forms, naban grappling, and "
           "the 9x9 technique-principle matrix; accessed 2026-10-17.")
CIT_MTF = ("Myanmar Thaing Federation. Thaing: the seven Burmese martial "
           "systems - bando empty-hand combat, banshay weapons, lethwei "
           "bareknuckle striking, naban grappling, shan thaing soft "
           "internal art, khut thaing pressure point techniques, arweththa "
           "mental discipline; accessed 2026-10-17.")
CIT_HAY = ("Hay JG. The Biomechanics of Sports Techniques. 4th ed. "
           "Prentice-Hall; 1993.")

ENTRIES = [
    {
        "key": "bando-meaning",
        "name": "What Bando Means: The Empty Hand",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Bando is the Burmese art of empty-hand combat - the hand-to-hand "
            "complement to thaing, the Burmese weapon arts. The word is read "
            "several ways: the art of empty hand combat, a way of "
            "self-discipline, a system of self defense. It is the unarmed "
            "half of a complete Burmese martial tradition whose other halves "
            "include banshay (weapons), lethwei (bareknuckle striking), and "
            "naban (Burmese wrestling and grappling). In the West the best "
            "known form is the Hanthawaddy style taught by Maung Gyi, who "
            "began teaching bando in Washington DC in the early 1960s, and "
            "carried forward by the American Bando Association, whose system "
            "holds nine animal styles - bull, boar, cobra, viper, python, "
            "panther, tiger, scorpion, and eagle - studied only after the "
            "basics are mastered. All bando schools start the same way: "
            "basic stances and footholds, drilled for months, sometimes for "
            "years, because every technique that follows stands on them. "
            "Empty-hand forms are called aka, and the basis of the system is "
            "a 9x9 matrix of techniques and principles: one technique may "
            "fit only one situation, but the principle underneath it fits "
            "many. Rank runs white, green, brown, black - some schools add "
            "yellow as an advanced white - and black belt takes a minimum "
            "of five years, demanding proficiency in aka, stick weapons, "
            "bladed weapons, sparring, and a physical fitness test. This "
            "record frames the whole database: every later record is one "
            "technique in that matrix, taught as a principle first."
        ),
        "how_it_works": (
            "Learning bando works by principle before pattern. First, "
            "stand. Set your feet at shoulder width, knees softly bent, "
            "weight centered, and hold the position until it is boring - "
            "that is the foothold lesson, and traditional schools keep "
            "students here for months. Second, step without crossing your "
            "feet: lead foot moves first going forward, rear foot moves "
            "first going back, always returning to the same balanced "
            "stance. Third, learn one strike - the straight punch - thrown "
            "from the hip with the body turning behind it, not from the "
            "shoulder alone. Fourth, learn one defense - the parry - "
            "meeting an attack with the forearm at an angle so it slides "
            "past rather than colliding head on. Fifth, learn one kick "
            "and one breakfall, so the body knows both ends of falling and "
            "rising. Only when these move without thought does the student "
            "enter the animal systems, where the boar teaches the rush, "
            "the cobra the fast hand, the python the wrap, and each animal "
            "is emulated as a strategy rather than mimicked as a pose. "
            "Forms (aka) bind the basics into flowing sequences; sparring "
            "tests them under pressure; the 9x9 matrix then lets the "
            "student build new techniques from old principles. Train "
            "slowly, breathe steadily, and never drill a technique at "
            "speed before its mechanics are clean at half speed."
        ),
        "key_points": [
            "Bando is the empty-hand half of the Burmese thaing tradition: banshay covers weapons, lethwei bareknuckle striking, naban wrestling - bando is the unarmed core that ties them together.",
            "The ABA system teaches nine animal styles - bull, boar, cobra, viper, python, panther, tiger, scorpion, eagle - only after basics, because animals are strategies to emulate, not poses to mimic.",
            "The 9x9 matrix of techniques and principles is the operating system: one technique fits one situation, the principle underneath fits many, so learn the principle.",
            "Every school starts with stances and footholds for months or years - the stance is the foundation the whole ladder stands on.",
            "Black belt takes a minimum of five years and demands aka forms, stick and bladed weapons, sparring, and a fitness test: bando is a long covenant, not a quick course.",
        ],
        "requirements": [
            "A flat training space with room to step in all directions, and a partner or a heavy bag for the strike lessons.",
            "Comfortable clothing that lets the hips and shoulders turn freely, and a mouthguard once sparring begins.",
            "Patience for the foothold stage: months of stance work before the animal systems, exactly as traditional schools require.",
            "A qualified instructor for anything involving a partner - throws, joint controls, and sparring are never learned safely from text alone.",
            "A training log, because the ladder spans years and memory alone cannot track what the body has earned.",
        ],
        "standards": [
            "Techniques are taught to Maung Gyi's Hanthawaddy lineage principles: principles first, patterns second, pressure testing last.",
            "Terminology follows the ABA and Myanmar Thaing Federation usage: bando, thaing, aka, naban, khut thaing, and the nine animal system names.",
            "Training safety follows the civilian traditional-art scope: controlled contact, protective equipment for sparring, and breakfalls before any throwing practice.",
        ],
        "citations": [CIT_WIKI_BANDO, CIT_ABA, CIT_MTF, CIT_MAUNGGYI],
        "sig_lens": (
            "The Signature read: the empty hand is the signature itself. "
            "Where public bando files a technique, the Signature combat "
            "method files a covenant - the stance the first covenant, "
            "balance the keeping of it, every strike a mark made in the "
            "air with intent, and the nine animal strategies nine "
            "covenants the student signs with the body over five years."
        ),
    },
    {
        "key": "ready-stance",
        "name": "The Ready Stance and Footholds",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The ready stance is the first technique of bando and the one "
            "practiced longest. All bando schools begin with stances and "
            "footholds, and the preliminary stage can last months or years, "
            "because every punch, kick, and throw is only as good as the "
            "ground it stands on. A foothold is not a pose struck for a "
            "photograph - it is the living contract between the fighter's "
            "feet and the floor: weight placed so the body can move in any "
            "direction without first rebalancing, knees bent so the legs "
            "act as springs, and the center of gravity low enough that a "
            "push becomes information rather than a fall. The ready stance "
            "taught here keeps the feet at shoulder width, the lead foot "
            "turned slightly inward, the rear foot angled out, roughly "
            "sixty percent of the weight forward and forty back, both knees "
            "softly bent, the torso upright but coiled, and the hands up "
            "guarding the chin and ribs. From this one position the student "
            "can step, strike, kick, clinch, or breakfall without a "
            "preparatory shift that a partner could read."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: stand with feet at shoulder "
            "width, toes pointing forward. Two: step the left foot forward "
            "half a stride and angle it slightly inward; angle the rear "
            "foot outward about thirty degrees - this is the foothold. "
            "Three: bend both knees until you feel the thighs wake up, "
            "keeping the back straight and the chest open. Four: settle "
            "about sixty percent of your weight onto the front foot and "
            "forty on the rear - you should be able to lift either heel a "
            "finger's width without falling over. Five: raise both hands, "
            "lead hand at cheek height, rear hand at chin height, elbows "
            "tucked to protect the ribs. Six: breathe into the belly, relax "
            "the shoulders down away from the ears, and look forward with "
            "soft eyes that see the whole room, not just one point. Seven: "
            "hold. Test the stance by having a partner gently push your "
            "shoulders from each direction - adjust until a push informs "
            "you rather than moves you. Eight: practice sinking and rising "
            "an inch without the head bobbing - smooth legs, quiet head. "
            "Drill this stance at the start of every session, five minutes "
            "minimum, until the body finds it without being told."
        ),
        "key_points": [
            "The stance is the first technique: all bando schools drill stances and footholds for months because everything else stands on them.",
            "Sixty-forty weight distribution keeps both legs loaded so the body can move in any direction without a readable rebalancing shift.",
            "Soft knees turn the legs into springs that absorb pushes and feed power upward; locked knees do neither.",
            "Hands guard chin and ribs with elbows tucked - the stance protects while it prepares, never one or the other.",
            "A good stance passes the push test: a gentle shove from any direction informs the student instead of moving them.",
        ],
        "requirements": [
            "A flat, non-slippery floor and enough room to be pushed from all sides safely.",
            "Training shoes or bare feet on a mat - never socks on a hard floor during stance and push testing.",
            "Five minutes of stance holding at the start of every session, worked up to longer holds over the months.",
            "A partner for the push test, instructed to push gently and progressively, never to shove hard.",
            "Patience: traditional schools keep students at the foothold stage for months, sometimes years.",
        ],
        "standards": [
            "Stance geometry follows the ABA basics curriculum: shoulder-width base, angled feet, soft knees, guarded hands.",
            "Progress is measured by the push test and by silent movement - the head stays level when the legs sink.",
            "Safety: the push test is always gentle and consensual; the student, not the partner, sets the intensity.",
        ],
        "citations": [CIT_ABA, CIT_WIKI_BANDO, CIT_MAUNGGYI],
        "sig_lens": (
            "The Signature read: the stance is the first covenant. Sixty "
            "percent forward is a promise to engage, forty back a promise "
            "to endure; the floor is the witness. Where public bando files "
            "a foothold, the Signature method files an oath of balance "
            "kept in every direction."
        ),
    },
    {
        "key": "stepping",
        "name": "Stepping: Advance, Retreat, and Circle",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "If the stance is the first technique, stepping is the second: "
            "movement that keeps the stance alive while the ground changes. "
            "Bando footwork follows one iron rule - never cross the feet - "
            "because crossed feet cannot push, cannot turn, and cannot "
            "recover. To advance, the lead foot moves first and the rear "
            "foot follows; to retreat, the rear foot moves first and the "
            "lead foot follows. Circling shifts the whole foothold around "
            "a center without ever letting the feet pass each other. This "
            "is what the months of stance training buy: feet that carry "
            "the stance from place to place instead of abandoning it at "
            "the first step. Good footwork is quiet - the head glides at "
            "one height, the weight never commits fully to a moving foot, "
            "and every step ends in a stance that can strike, block, or "
            "breakfall. Students drill stepping in straight lines, then "
            "in circles, then against a partner's pressure, until the "
            "correct foot moves first without thought."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: begin in the ready stance. "
            "Two: to advance, slide the lead foot forward about half a "
            "foot-length, keeping it low to the floor, then draw the rear "
            "foot up the same distance - the stance should look unchanged, "
            "only relocated. Three: to retreat, reverse the order - the "
            "rear foot moves first, then the lead foot follows back the "
            "same distance. Four: to circle left, step the lead foot left "
            "and slightly around, then bring the rear foot with it; the "
            "body turns but the feet never cross. Five: keep the head at "
            "one level - imagine a glass of water balanced on your head "
            "and step without spilling it. Six: keep roughly sixty-forty "
            "weight on a moving foot at most; the planted foot stays ready "
            "to drive. Seven: breathe out on each step for the first "
            "hundred repetitions, then let the breath settle into rhythm. "
            "Eight: drill the line drill - ten steps forward, ten back, "
            "ten circling each way - and finish by holding the stance for "
            "one minute. Speed comes last: clean slow steps become fast "
            "clean steps, but rushed steps teach only rushing."
        ),
        "key_points": [
            "Never cross the feet: the lead foot leads forward, the rear foot leads backward, and circling moves the whole foothold as one.",
            "Every step ends in a stance - stepping is the stance relocating, not the stance being abandoned.",
            "The head glides at one level; bobbing up and down announces every movement to a watchful partner.",
            "Weight stays off the moving foot so the planted foot is always ready to drive a strike or a kick.",
            "Slow clean steps become fast clean steps; drilling at speed before the mechanics are clean teaches only mistakes.",
        ],
        "requirements": [
            "A long clear floor line - tape on the floor works - for the line drill: ten forward, ten back.",
            "Enough open space to circle in both directions without obstacles at ankle height.",
            "A metronome or counted breath to keep early drilling slow and even.",
            "A partner, later, to add pressure: the student steps while the partner advances, teaching footwork under stress.",
            "Footwear with grip or a clean mat; the step slides low and slipping feet teach fear instead of footwork.",
        ],
        "standards": [
            "Footwork follows the ABA basics curriculum: no crossed feet, stance preserved through every step.",
            "Progress is measured by the level-head test and by the lead-foot-first rule under partner pressure.",
            "Safety: the line drill is done at walking pace for the first weeks; partner pressure drills stay at half speed until the stance holds.",
        ],
        "citations": [CIT_ABA, CIT_MAUNGGYI, CIT_HAY],
        "sig_lens": (
            "The Signature read: stepping is the covenant in motion. The "
            "stance is an oath kept in one place; the step carries the "
            "oath across the floor unbroken. Where public bando files "
            "footwork, the Signature method files a promise that balance "
            "is never left behind."
        ),
    },
    {
        "key": "straight-punch",
        "name": "The Straight Punch",
        "group": "Core Strikes",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The straight punch is bando's first strike and its most honest "
            "teacher. It travels the shortest road - a straight line from "
            "guard to target and back - which is why it is also the "
            "fastest punch and the one that teaches hip rotation, the "
            "engine of every hand strike that follows. Power in a straight "
            "punch does not come from the arm; it comes from the floor, "
            "up through the legs, across the turning hips, through the "
            "shoulder, and out along the extended arm, arriving as one "
            "connected chain. The fist strikes with the first two knuckles, "
            "the wrist stays straight as a board behind them, and the punch "
            "snaps back along the same line the instant it lands - the "
            "return is half the technique, because a hand left out is a "
            "handle for the other person. Students throw it first from the "
            "stance in the air, then into a bag or pads, then in partner "
            "drills, and its honesty never fades: any flaw in stance, "
            "rotation, or guard shows up immediately in the punch."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: take the ready stance, hands "
            "guarding chin and ribs. Two: to throw the lead straight, push "
            "off the rear foot and turn the lead hip a quarter turn toward "
            "the target - the hip starts the punch, not the arm. Three: "
            "extend the lead arm straight along the line from your chin to "
            "the target, rotating the fist so the knuckles turn over at the "
            "end, palm facing down. Four: strike with the first two "
            "knuckles only, wrist locked straight - imagine the forearm and "
            "fist as one unbending rod. Five: at the instant of contact, "
            "tense the whole body for a heartbeat - the snap - then relax "
            "and pull the fist straight back to guard along the same line. "
            "Six: for the rear straight, push off the rear foot harder, "
            "turn the rear hip fully through, and let the shoulder cover "
            "the chin as the arm extends - the rear hand travels farther "
            "and hits harder because the whole body is behind it. Seven: "
            "exhale sharply on every punch; the breath times the snap. "
            "Eight: drill in sets - fifty slow in the air checking form in "
            "a mirror, fifty into the bag or pads, then partner drills at "
            "half speed. Never punch with a bent wrist, never drop the "
            "other hand, and never lean past your front knee."
        ),
        "key_points": [
            "Power comes from the floor through the turning hips, not from the arm - the arm is the delivery, the body is the engine.",
            "The first two knuckles strike with a straight locked wrist; a bent wrist is how hands get injured.",
            "The punch snaps back along the same line instantly; the return is half the technique.",
            "The rear straight hits harder because the whole body's rotation is behind it - hip turn is the difference between a push and a punch.",
            "Exhale on every punch: the breath times the snap and keeps the body from holding tension.",
        ],
        "requirements": [
            "A mirror for the first air-punch sets, so the student can see the hip turn and the returning hand.",
            "A heavy bag or focus mitts with a partner once form is clean in the air.",
            "Hand protection: wraps and gloves for bag work, always.",
            "A stance that passes the push test - without it the punch has no engine.",
            "Controlled partner drills at half speed before any contact sparring.",
        ],
        "standards": [
            "Strike mechanics follow the kinetic chain principle: ground, legs, hips, shoulder, arm, knuckles - each link adds, none is skipped.",
            "Form standard: hip leads, wrist straight, opposite hand guards, full return to guard.",
            "Safety: bag work always gloved and wrapped; partner drills use controlled touch contact only, with headgear once speed rises.",
        ],
        "citations": [CIT_ABA, CIT_HAY, CIT_MAUNGGYI],
        "sig_lens": (
            "The Signature read: the straight punch is the shortest oath - "
            "a straight line sworn from guard to target. Where public bando "
            "files a punch, the Signature method files a promise kept at "
            "speed: hip, shoulder, knuckle, return, all one unbroken "
            "signature written in the air."
        ),
    },
    {
        "key": "backfist-hammer",
        "name": "The Backfist and Hammer Strike",
        "group": "Core Strikes",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The backfist and the hammer strike are the straight punch's "
            "curved cousins: where the straight punch drives along a line, "
            "these swing along an arc and land with the back of the fist "
            "or the bottom edge of the hand. The backfist whips out and "
            "back like a snapped towel, striking with the back of the "
            "knuckles - fast, surprising, and natural as a follow-up when "
            "the straight punch misses or is parried. The hammer strike "
            "lands with the fleshy bottom edge of the fist, the same "
            "surface used to pound a table, and it is one of the safest "
            "strikes in the art because the wrist is naturally straight "
            "and the contact surface is broad and padded. Both strikes "
            "draw their power from rotation: the shoulder whips the arm "
            "around and the body turns with it, so the strike arrives "
            "with the whole torso's momentum behind a small fast surface. "
            "Students learn them as counters - the backfist answering a "
            "missed straight, the hammer answering a clinch or a bent-over "
            "opponent - and both return to guard on the same arc they "
            "traveled."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: from the ready stance, for "
            "the lead backfist, whip the lead hand out along a horizontal "
            "arc at head height, turning the hips with it - the strike is "
            "a snap, not a push. Two: contact with the back of the first "
            "two knuckles, wrist firm, then snap the hand straight back to "
            "guard on the same arc; the backfist lives and dies by its "
            "return. Three: for the hammer strike, raise the hand and bring "
            "the bottom edge of the fist down or across in a short arc, "
            "elbow bent, striking with the fleshy heel of the hand - "
            "imagine hammering a nail with the side of your fist. Four: "
            "drive each strike with a sharp quarter-turn of the hips; the "
            "arm rides the rotation, it does not muscle the strike alone. "
            "Five: exhale on the snap, and let the shoulders stay down - "
            "raised shoulders bleed power and invite fatigue. Six: drill "
            "the backfist as an answer - throw a straight punch, and the "
            "instant it would land, fire the backfist on the same side. "
            "Seven: drill the hammer as an answer to the clinch - from "
            "close, short downward hammers, always returning to a guard or "
            "a grip. Eight: never swing wild arcs that carry past the "
            "target; the arc ends at contact and the hand comes home."
        ),
        "key_points": [
            "The backfist is a whip, not a push: horizontal arc, back-of-knuckle contact, instant return on the same arc.",
            "The hammer strike lands with the padded bottom edge of the fist - one of the safest strikes because the wrist stays naturally straight.",
            "Both strikes are powered by hip and torso rotation; the arm rides the turn rather than muscling alone.",
            "They shine as answers: the backfist after a missed straight, the hammer in the clinch - counters, not openers.",
            "Shoulders stay down and the arc ends at contact; wild swings that carry past the target are just spinning.",
        ],
        "requirements": [
            "Clean straight-punch mechanics first - the hip turn learned there drives these strikes too.",
            "A bag or pads for the hammer strike, which lands harder than it looks.",
            "Wrist awareness: the backfist wrist must be firm at contact, never floppy.",
            "Partner drills at half speed for the counter timing - the backfist answers the straight, not the air.",
            "Return-to-guard discipline: every rep ends with the hand home, not admiring the strike.",
        ],
        "standards": [
            "Arc-strike mechanics: rotation-driven, contact on the correct surface, immediate return along the same path.",
            "Form standard: hips turn with the strike, opposite hand guards, contact surface correct.",
            "Safety: partner drills use touch contact for the backfist; hammer strikes stay on pads or bags until control is proven.",
        ],
        "citations": [CIT_ABA, CIT_HAY, CIT_MAUNGGYI],
        "sig_lens": (
            "The Signature read: the arc is the oath curved. The straight "
            "punch swears a line; the backfist swears a circle and returns "
            "home, the hammer swears downward with the honest heel of the "
            "hand. Where public bando files curved strikes, the Signature "
            "method files promises that come back."
        ),
    },
    {
        "key": "open-hand",
        "name": "The Open-Hand Chop and Palm Heel",
        "group": "Core Strikes",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Not every strike needs a fist. The open-hand chop - the "
            "knife-hand - strikes with the hardened bottom edge of the "
            "hand, fingers straight and pressed together, thumb tucked, "
            "the whole hand rigid as a blade. The palm heel drives with "
            "the thick pad at the base of the palm, wrist bent back, "
            "fingers up. Both are older than the gloved fist and both "
            "have honest advantages: the hand stays relaxed until the "
            "instant of contact, so the strike is fast; the contact "
            "surfaces are broad and padded compared to bare knuckles; and "
            "the open hand flows naturally into grabs, parries, and the "
            "wraps of the python system later in the ladder. The chop "
            "travels in arcs - downward, sideways, rising - while the "
            "palm heel drives straight like a punch thrown with an open "
            "hand. Students condition the hand edge gradually on pads, "
            "never on hard surfaces, and learn early that the open hand "
            "is a tool of precision: it strikes, then it can hold."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: form the knife-hand - "
            "fingers straight, pressed tightly together, thumb folded "
            "against the palm, the bottom edge of the hand rigid. Two: "
            "for the downward chop, raise the hand beside the head and "
            "bring the edge down in a short arc, hips turning with it, "
            "contacting with the bottom edge only - never the fingers. "
            "Three: for the sideways chop, swing the edge across "
            "horizontally at neck-to-shoulder height, stepping in with "
            "the same-side foot to add the body's weight. Four: for the "
            "palm heel, bend the wrist back, fingers pointing up, and "
            "drive the heel of the palm straight forward exactly like a "
            "straight punch, hips turning behind it. Five: keep the hand "
            "relaxed until the last instant, then rigid at contact - "
            "tension held too early slows the strike, tension at contact "
            "makes it land. Six: return the hand to guard or convert it "
            "immediately into a grab or parry; the open hand never has to "
            "travel home empty. Seven: condition gradually - fifty light "
            "chops on a pad daily, increasing slowly over months, never "
            "striking hard surfaces. Eight: drill the chop-to-grab flow: "
            "chop, and as the hand passes, close the fingers into a "
            "controlling grip."
        ),
        "key_points": [
            "The knife-hand strikes with the rigid bottom edge of the hand, fingers together and thumb tucked - never the fingers.",
            "The palm heel drives straight like a punch with the thick pad of the palm, wrist bent back.",
            "The hand stays relaxed until the instant of contact: early tension slows the strike, contact tension lands it.",
            "The open hand flows into grabs, parries, and wraps - it strikes, then it can hold.",
            "Hand edges condition gradually on pads over months; hard surfaces are never the teacher.",
        ],
        "requirements": [
            "A soft pad for conditioning the hand edge - never boards, walls, or hard surfaces.",
            "Clean hip-turn mechanics from the straight punch, which drive the chop and palm heel too.",
            "A partner for the chop-to-grab flow drill, at slow speed first.",
            "Patience with the hand: edge conditioning is measured in months, not sessions.",
            "Wrist flexibility work so the palm heel's bent-back wrist is comfortable and strong.",
        ],
        "standards": [
            "Hand formation standard: knife-hand rigid with tucked thumb; palm heel with wrist fully bent back and fingers up.",
            "Contact standard: edge-only for the chop, heel-of-palm only for the palm strike - fingers never take impact.",
            "Safety: conditioning is progressive and pad-based; partner drills use controlled touch on the body.",
        ],
        "citations": [CIT_ABA, CIT_MAUNGGYI, CIT_HAY],
        "sig_lens": (
            "The Signature read: the open hand is the oath with options. "
            "The fist swears one thing; the open hand swears to strike "
            "and then to hold, to parry, to wrap. Where public bando files "
            "hand strikes, the Signature method files a promise that the "
            "hand will decide, at the last instant, what it is for."
        ),
    },
    {
        "key": "elbow",
        "name": "The Elbow Strike",
        "group": "Core Strikes",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The elbow is the close-range answer to every question the "
            "fists cannot reach. Short, hard, and driven by the whole "
            "torso, the elbow strike lands with the point or the flat of "
            "the elbow - one of the hardest natural weapons on the human "
            "body - and it needs almost no room to work. Where punches "
            "need distance to extend, elbows thrive in the clinch, against "
            "a rushing opponent, or when a strike is smothered halfway. "
            "The mechanics are pure rotation: the hips and shoulders whip "
            "around and the bent arm rides the turn, the elbow arriving "
            "like the head of a hammer swung on a short handle. Students "
            "learn the horizontal elbow first - swung across at head "
            "height with a full hip turn - then the upward elbow, the "
            "downward elbow, and the spinning elbow much later in the "
            "ladder. Because the elbow is short and the target is close, "
            "the strike is also a shield: the same rotation that throws "
            "the elbow covers the chin behind the shoulder."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: from the ready stance, bend "
            "the lead arm so the fist rests near your own chin, elbow "
            "pointing outward at shoulder height - this is the loaded "
            "position. Two: for the horizontal elbow, whip the hips a "
            "quarter turn and swing the elbow across horizontally, "
            "contacting with the point of the elbow; the shoulder of the "
            "striking arm rises to cover your chin as it travels. Three: "
            "for the upward elbow, drop the hips slightly and drive the "
            "elbow up in a tight arc, as if uppercutting with the elbow "
            "point - the legs push, the torso lifts, the elbow rides. "
            "Four: for the downward elbow, raise the elbow high and drop "
            "it straight down with the body's weight behind it, stepping "
            "in as it falls. Five: in every version the opposite hand "
            "stays glued to guard - elbows are thrown one at a time, the "
            "other hand always home. Six: exhale sharply and tense at "
            "contact, then relax and reload the arm immediately. Seven: "
            "drill on pads held close - the pad holder stands at elbow "
            "range, not punch range - ten of each angle per side. Eight: "
            "never throw elbows at a partner's head in drills; elbows are "
            "a pad, bag, and controlled-sparring technique only."
        ),
        "key_points": [
            "The elbow is the close-range weapon: short, hard, driven by full torso rotation, needing almost no room.",
            "Horizontal, upward, and downward elbows cover every close angle; the striking shoulder covers the chin as it travels.",
            "The opposite hand never leaves guard - elbows are thrown one at a time while the other hand stays home.",
            "The bent arm is a short hammer handle: the hips and shoulders swing it, the arm does not muscle it.",
            "Elbows are pad, bag, and controlled-sparring techniques; they are never thrown at a partner's head in drills.",
        ],
        "requirements": [
            "Elbow pads or a well-padded target: the point of the elbow is hard and unforgiving to holders.",
            "A pad holder who stands at true elbow range - close enough that a punch would smother.",
            "Clean hip rotation from the straight-punch work; without it the elbow is just an arm waving.",
            "A mouthguard and headgear once elbows enter controlled sparring, and strict no-head-contact rules in drills.",
            "Patience: the spinning elbow waits for the advanced ladder - horizontal, upward, and downward come first.",
        ],
        "standards": [
            "Elbow mechanics: bent arm, full hip and shoulder rotation, correct contact surface, opposite hand guarding.",
            "Range standard: elbows are thrown only where a punch would smother - if the arm can extend fully, it is not elbow range.",
            "Safety: no elbow contact to a partner's head in drills; controlled sparring with elbows requires headgear, mouthguard, and instructor supervision.",
        ],
        "citations": [CIT_ABA, CIT_HAY, CIT_MAUNGGYI],
        "sig_lens": (
            "The Signature read: the elbow is the oath kept close. When "
            "distance fails, the covenant shortens its handle and swears "
            "again at arm's length. Where public bando files a close-range "
            "strike, the Signature method files a promise that needs no "
            "room to be kept."
        ),
    },
    {
        "key": "parry-guard",
        "name": "The Parry and the Forearm Guard",
        "group": "Defenses",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Bando defense begins with a principle, not a block: meet "
            "force at an angle and let it pass. The parry is a small, "
            "precise deflection - the open hand or forearm brushes an "
            "incoming strike just enough to miss, using the attacker's "
            "own speed to carry it past the target. It costs almost no "
            "energy, it keeps both hands free to answer, and it teaches "
            "the deeper bando lesson that defense is redirection, not "
            "collision. Behind the parry stands the forearm guard: both "
            "forearms raised, elbows tucked, forming a shell that catches "
            "what the parry misses. Students drill the parry first "
            "against slow straight punches, learning the two golden "
            "details - deflect, do not push, and move the head with the "
            "parry, never trusting the hands alone. The guard is the "
            "insurance; the parry is the art; head movement is the habit "
            "that makes both work."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: from the ready stance, "
            "when a straight punch comes, brush it aside with the open "
            "lead hand - a short sideways flick of the wrist, contacting "
            "the attacker's wrist or forearm, moving it inches, not feet. "
            "Two: parry across your body with the lead hand against their "
            "lead punch (outside parry), or parry inward with the rear "
            "hand - always deflecting the strike past your head, never "
            "into your other hand's path. Three: move your head with the "
            "parry - slip it a few inches off the line as the hand "
            "brushes; hands can miss, and the head must not be where the "
            "punch was aimed. Four: the instant the parry lands, answer - "
            "parry and counter are one motion, not two; the hand that "
            "parried is already on its way back to strike. Five: for the "
            "forearm guard, raise both forearms vertical in front of the "
            "face, elbows tucked to the ribs, and let kicks and wild "
            "punches land on the forearms while you step or circle out. "
            "Six: drill slowly with a partner - one throws slow straights, "
            "the other parries and answers with a touch counter. Seven: "
            "never catch a punch by grabbing at it; the parry is a brush, "
            "and grabbing commits the hand. Eight: keep the elbows in - "
            "a parry thrown with a flared elbow opens the ribs it was "
            "meant to protect."
        ),
        "key_points": [
            "Defense is redirection, not collision: the parry brushes an attack inches off line and lets its own speed carry it past.",
            "Parry and counter are one motion - the deflecting hand is already returning as a strike.",
            "Move the head with the parry; hands can miss, and the head must not be where the punch was aimed.",
            "The forearm guard is the insurance behind the art: both forearms up, elbows tucked, a shell for what the parry misses.",
            "Never grab at a punch - the parry is a brush, and a committed grabbing hand is a captured hand.",
        ],
        "requirements": [
            "A cooperative partner throwing slow, honest straight punches - the parry is learned against real lines, not air.",
            "Touch-contact rules in parry drills: the counter answers with a touch, never a strike.",
            "Headgear once parry drills add speed, because even brushed punches sometimes land.",
            "A mirror for solo parry mechanics: the brush should be small, the elbows staying tucked.",
            "The discipline to deflect inches: beginners parry in feet, and feet-wide parries open the guard.",
        ],
        "standards": [
            "Parry mechanics: small deflection at an angle, head moving off line, immediate counter, elbows tucked.",
            "Timing standard: the parry meets the attack, never chases it - late parries are just waving.",
            "Safety: partner parry drills use controlled touch contact; headgear required as speed increases.",
        ],
        "citations": [CIT_ABA, CIT_MAUNGGYI, CIT_HAY],
        "sig_lens": (
            "The Signature read: the parry is the oath declined gracefully. "
            "Where public bando files a deflection, the Signature method "
            "files a promise to never meet force with force when an angle "
            "will do - the attacker's own speed becomes the witness that "
            "carries it past."
        ),
    },
    {
        "key": "knee",
        "name": "The Knee Strike",
        "group": "Core Strikes",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The knee is the body's battering ram: the hardest joint "
            "driven by the strongest muscles, arriving upward or forward "
            "with the full weight of a dropping, thrusting body behind "
            "it. In bando the knee belongs to the clinch and to close "
            "range, where punches smother and elbows have done their work "
            "- it is the strike that finishes what close range started. "
            "The mechanics are a violent hinge: the standing leg roots "
            "into the floor, the hips thrust forward and up, and the "
            "knee snaps up like a trapdoor, the hands pulling the "
            "opponent down into it in the clinch or simply guarding while "
            "the knee works. Students learn the straight knee first - "
            "driven forward and up into a pad held at body height - and "
            "discover immediately that the knee's power comes from the "
            "hip thrust, not from lifting the leg; a lifted knee is a "
            "gesture, a thrusted knee is a weapon. Balance is the price: "
            "every knee stands on one leg, so the standing foot, the "
            "rooted hip, and the guarding hands must all do their jobs at "
            "once."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: from the ready stance, step "
            "the lead foot slightly forward and plant it - this is the "
            "root, and everything depends on it. Two: thrust the hips "
            "forward and upward as if trying to touch the target with "
            "your belt buckle; the knee rises because the hips drive it, "
            "not because the leg lifts it. Three: snap the knee up and "
            "forward, contacting with the bony point of the knee, toes "
            "pointed down and the foot relaxed behind - a flexed foot "
            "bleeds power and risks the toes. Four: at the same instant, "
            "pull down with both hands - in the clinch, the hands grip "
            "behind the neck and pull the target down into the rising "
            "knee; the collision of the two forces is the strike. Five: "
            "keep the torso upright; leaning back to admire the knee "
            "destroys balance and telegraphs the strike. Six: set the "
            "foot back down into the stance immediately - the knee "
            "returns to the ground it came from. Seven: drill on a pad "
            "held at body height, ten per leg, alternating, focusing on "
            "the hip thrust; then drill the pull-down with a partner "
            "holding the pad at clinch range. Eight: never practice full "
            "knees on a partner's body - pads, bags, and controlled "
            "touch in sparring only."
        ),
        "key_points": [
            "The knee's power comes from the hip thrust, not from lifting the leg - a lifted knee is a gesture, a thrusted knee is a weapon.",
            "In the clinch the hands pull the target down into the rising knee; the collision of the two forces is the strike.",
            "Toes point down and the foot stays relaxed - a flexed foot bleeds power and endangers the toes.",
            "The torso stays upright and the foot returns to stance immediately; leaning back destroys balance.",
            "Every knee stands on one leg, so the planted root foot does half the work of the strike.",
        ],
        "requirements": [
            "A body pad or heavy bag at torso height for knee impact - never a partner's body.",
            "A clinch partner for the pull-down drill, working at half speed with touch control.",
            "Hip mobility work: the thrust must be comfortable before it is powerful.",
            "Balance drilling on the root leg - single-leg stance holds build the foundation the knee stands on.",
            "Protective equipment and instructor supervision once knees enter controlled sparring.",
        ],
        "standards": [
            "Knee mechanics: rooted standing leg, forward-up hip thrust, knee point contact, toes down, immediate return to stance.",
            "Clinch standard: hands control and pull down while the knee rises - the two forces meet, neither works alone.",
            "Safety: full knees land on pads and bags only; partner work is controlled touch with protective gear.",
        ],
        "citations": [CIT_ABA, CIT_HAY, CIT_MAUNGGYI],
        "sig_lens": (
            "The Signature read: the knee is the oath driven upward. The "
            "body's strongest hinge swears with the hip, and the hands "
            "pull the world down to meet it. Where public bando files a "
            "close-range strike, the Signature method files a promise "
            "kept on one leg."
        ),
    },
    {
        "key": "front-kick",
        "name": "The Front Kick",
        "group": "Kicking",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The front kick is the longest straight weapon in the empty "
            "hand: a piston that chambers at the hip, snaps out, and "
            "recoils, striking with the ball of the foot. It teaches the "
            "three-phase kick - chamber, extend, recoil - that every later "
            "kick in the ladder reuses, which is why it is taught before "
            "the low kick and the roundhouse. The chamber is the secret: "
            "the knee rises high and tight first, hiding the kick's "
            "intention, and then the lower leg snaps out from the chamber "
            "like a switchblade, so the strike arrives faster and less "
            "readably than a leg swung from the floor. Students strike "
            "with the ball of the foot - toes pulled back, ankle locked - "
            "into pads held at body height, and learn the two classic "
            "failures: kicking with the toes, which folds the foot, and "
            "leaning back, which trades balance for a few inches of reach "
            "that the chamber would have given for free."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: from the ready stance, "
            "shift your weight onto the lead leg - the kicking leg must "
            "be unweighted to move. Two: raise the rear knee high and "
            "tight toward your chest, thigh parallel to the floor - this "
            "is the chamber, and it hides the kick. Three: snap the lower "
            "leg out from the chamber, extending toward the target, toes "
            "pulled sharply back so the ball of the foot leads, ankle "
            "locked rigid. Four: drive the hips forward a few inches as "
            "the leg extends - the kick is a piston, and the hips are the "
            "cylinder behind it. Five: the instant of contact, tense the "
            "whole leg for a heartbeat, then snap the foot straight back "
            "to the chamber - recoil is half the kick. Six: set the foot "
            "down back into the stance; never let the kicking leg dangle. "
            "Seven: keep the torso upright and the hands guarding - the "
            "kick must not cost the guard. Eight: drill ten slow chambers "
            "without extending, then ten full kicks per leg into a pad, "
            "then the step-in front kick: step the lead foot forward and "
            "kick with the rear leg as the weight transfers."
        ),
        "key_points": [
            "Every kick follows chamber, extend, recoil - the front kick teaches the pattern all later kicks reuse.",
            "The high tight chamber hides the kick's intention; a leg swung from the floor announces itself.",
            "Strike with the ball of the foot, toes pulled back and ankle locked - toes fold, balls of feet do not.",
            "The hips drive forward behind the extending leg; the kick is a piston and the hips are the cylinder.",
            "Recoil is half the kick: snap back to chamber and set the foot down into stance - never let the leg dangle.",
        ],
        "requirements": [
            "A kicking pad or heavy bag at body height, held by a partner who can take the thrust.",
            "Ankle and hip mobility: the chamber must be comfortable before it is fast.",
            "A mirror for the first chamber drills, to check the knee rises tight and the torso stays upright.",
            "The guard habit: hands must stay up through every rep, checked by the partner calling out drops.",
            "Floor space to step in - the step-in front kick needs room to travel.",
        ],
        "standards": [
            "Kick mechanics: unweighted kicking leg, high tight chamber, ball-of-foot contact, hip drive, full recoil.",
            "Form standard: torso upright, hands guarding, kicking foot returns to stance - no dangling legs.",
            "Safety: kicks land on pads and bags; partner drills use controlled touch; toes-back foot position is mandatory to protect the foot.",
        ],
        "citations": [CIT_ABA, CIT_HAY, CIT_MAUNGGYI],
        "sig_lens": (
            "The Signature read: the front kick is the longest oath - a "
            "piston sworn from the hip. Where public bando files a "
            "straight kick, the Signature method files a promise in three "
            "phases: chamber the intent, extend the word, recoil the hand "
            "before the echo fades."
        ),
    },
    {
        "key": "low-kick",
        "name": "The Bando Low Kick",
        "group": "Kicking",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The low kick is bando's quiet workhorse: a swinging strike "
            "with the shin that attacks the thigh and calf, the legs an "
            "opponent must stand on. Unlike the front kick's piston, the "
            "low kick is a bat - the hip swings the whole leg through the "
            "target in an arc, contacting with the hard middle of the shin, "
            "and its purpose is accumulation rather than spectacle. One "
            "low kick is an annoyance; a dozen change how a person moves, "
            "stand, and thinks. The mechanics demand commitment: the "
            "standing foot pivots, the hips turn over fully so the kicking "
            "hip finishes past the target line, and the shin - not the "
            "foot, never the foot - does the work. Students condition the "
            "shins gradually on bags, never on hard objects, and learn "
            "the low kick's twin: the checking defense, lifting the knee "
            "so an incoming low kick meets the hard shin instead of the "
            "soft thigh."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: from the ready stance, step "
            "the lead foot slightly outward to open the hips - the kick "
            "needs the doorway open. Two: pivot hard on the ball of the "
            "standing foot, turning the heel toward the target; the pivot "
            "is the engine and the most common thing beginners forget. "
            "Three: swing the kicking leg in an arc toward the opponent's "
            "thigh, letting the hip turn over fully - imagine throwing "
            "your hip past the target. Four: contact with the middle of "
            "the shin, leg slightly bent at impact, the whole leg relaxed "
            "until the last instant like a rope with a knot in it. Five: "
            "follow through a few inches past contact, then swing the leg "
            "back and set it down into stance - the low kick returns on "
            "its own arc. Six: keep the same-side hand guarding the face "
            "throughout; the swinging hip tries to pull the guard down, "
            "and the guard must win. Seven: to check a low kick, lift "
            "your lead knee sharply so the incoming shin meets your "
            "raised shin - hard meets hard, and the check costs you "
            "nothing. Eight: drill fifty light low kicks per leg on the "
            "bag before any power; shins condition over months, and a "
            "bruised shin that cannot train is a week lost."
        ),
        "key_points": [
            "The shin, never the foot, is the contact surface - the middle of the shin is a bat, the foot is a liability.",
            "The standing-foot pivot is the engine; beginners forget it and kick with the leg alone.",
            "The hip turns over fully past the target line - commitment, not a tap, is what makes the low kick accumulate.",
            "The same-side hand guards through the swing; the hip tries to pull the guard down and the guard must win.",
            "The check - lifting the knee so shin meets shin - is the low kick's twin and must be drilled alongside it.",
        ],
        "requirements": [
            "A heavy bag for shin conditioning - never hard objects, trees, or posts.",
            "Months of gradual conditioning: fifty light kicks per leg before any power work.",
            "A partner with a leg pad for targeted low-kick practice at thigh height.",
            "The pivot habit drilled in the air first - pivot, swing, return - before bag contact.",
            "Ice and rest protocols: conditioned shins are built by recovery, not by punishment.",
        ],
        "standards": [
            "Low-kick mechanics: standing-foot pivot, full hip turnover, middle-shin contact, same-side guard maintained.",
            "Conditioning standard: progressive bag work only; no hard-surface conditioning at any level.",
            "Safety: partner low-kick drills use pads and controlled contact; the check is drilled slowly before speed is added.",
        ],
        "citations": [CIT_ABA, CIT_HAY, CIT_MAUNGGYI],
        "sig_lens": (
            "The Signature read: the low kick is the patient oath - sworn "
            "not once but a dozen times, each one a small promise that "
            "the ground beneath the opponent is no longer theirs. Where "
            "public bando files a leg kick, the Signature method files a "
            "covenant of accumulation."
        ),
    },
    {
        "key": "breakfall",
        "name": "The Breakfall",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Every art that throws must first teach falling, and bando "
            "teaches the breakfall before any student is thrown. A "
            "breakfall spreads the force of a fall across the broadest "
            "possible surface - the whole side of the body, the slapping "
            "arm, the exhaled breath - so no single point takes the "
            "impact. The technique is counterintuitive: instead of "
            "reaching out to catch yourself, which breaks wrists and "
            "collarbones, you tuck the chin, round the body, slap the "
            "mat with the whole arm a hand's width before the body "
            "arrives, and exhale hard so the torso is empty and soft at "
            "impact. Students learn the back breakfall first - sitting "
            "down and rolling back onto the mat - then the side breakfall, "
            "then the forward rolling breakfall, each from lower heights "
            "before higher ones. The breakfall is also bando's humility "
            "lesson: the ground is the final teacher, and the student "
            "who can fall well can train hard for decades."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: for the back breakfall, "
            "squat low, tuck your chin hard to your chest - the chin tuck "
            "is non-negotiable, it keeps the head off the mat. Two: roll "
            "backward, and a hand's width before your back reaches the "
            "mat, slap the mat hard with both arms extended at forty-five "
            "degrees, palms down - the slap spreads the force and the "
            "timing matters more than the strength. Three: exhale sharply "
            "as you land, emptying the lungs so the torso is soft, and "
            "let the rounded back take the impact across its whole "
            "surface. Four: for the side breakfall, fall sideways from a "
            "crouch, slapping with the downside arm and landing on the "
            "whole side - leg, hip, ribs, arm - never the shoulder point "
            "alone. Five: for the forward breakfall, dive forward over "
            "one shoulder, tucking into a ball and rolling across the "
            "back from shoulder to opposite hip. Six: never reach out "
            "with a straight arm to catch yourself - that is how wrists "
            "break; the arm slaps, it does not post. Seven: practice from "
            "sitting, then squatting, then standing, then from a gentle "
            "partner push - height comes last. Eight: drill until the "
            "slap-exhale-tuck happens without thought, because a real "
            "fall gives no time to think."
        ),
        "key_points": [
            "Tuck the chin to the chest always - the chin tuck is what keeps the head off the mat in every fall.",
            "Slap the mat with the whole arm just before the body arrives; the slap spreads the force, and timing beats strength.",
            "Exhale hard at impact so the torso is empty and soft - a full rigid torso takes damage, an empty one rides it out.",
            "Never post a straight arm to catch yourself; the arm slaps, it does not post - posting breaks wrists.",
            "Learn from sitting, then squatting, then standing, then pushed - height is the last variable added, never the first.",
        ],
        "requirements": [
            "A proper mat - thick enough that repeated falls do not bruise; concrete and thin carpet are never acceptable.",
            "An instructor present for the first standing and pushed falls.",
            "A partner who pushes gently and progressively for the pushed-fall stage.",
            "No jewelry, no hard objects in pockets, and tied-back hair for rolling falls.",
            "The discipline to stay at low heights until the slap-exhale-tuck is automatic.",
        ],
        "standards": [
            "Breakfall mechanics: chin tucked, arm slap timed before body contact, exhale at impact, force spread across broad surfaces.",
            "Progression standard: sitting, squatting, standing, pushed - no stage skipped, height added last.",
            "Safety: mats mandatory; straight-arm posting is corrected immediately every time it appears.",
        ],
        "citations": [CIT_ABA, CIT_MAUNGGYI, CIT_HAY],
        "sig_lens": (
            "The Signature read: the breakfall is the oath to the ground. "
            "Every fighter meets the floor; the covenant is to meet it "
            "well - chin tucked, arm slapping, breath given up freely. "
            "Where public bando files a safety technique, the Signature "
            "method files a promise that no fall will end the training."
        ),
    },
]
ENTRIES.extend([
    {
        "key": "aka-first",
        "name": "The First Aka: Empty-Hand Form",
        "group": "Forms",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Aka are the empty-handed forms of bando - the kata of the "
            "Burmese tradition, flowing sequences of strikes, blocks, "
            "steps, and turns performed solo against imaginary opponents. "
            "Proficiency in aka is one of the black belt requirements, "
            "alongside stick weapons, bladed weapons, sparring, and the "
            "fitness test, because the form is where the basics stop "
            "being separate drills and start being one moving thing. The "
            "first aka a student learns is deliberately simple: a "
            "straight-line sequence that walks through the ready stance, "
            "the step, the straight punch, the parry, the front kick, and "
            "the turn, each technique flowing into the next without the "
            "pauses that drills allow. Practicing aka builds what partner "
            "work cannot: the internal map of where every limb is without "
            "looking, the breathing rhythm that carries through a long "
            "sequence, and the habit of finishing every technique in a "
            "stance ready for the next. Students perform the form slowly "
            "first - speed is a reward for correctness - and the form is "
            "never considered learned until it can be done mirror-smooth "
            "at full speed, in both directions, on demand."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: learn the sequence in "
            "chunks of three moves - never try to memorize a whole form "
            "at once; three moves, then three more, then join them. Two: "
            "walk the form at half speed with no power, checking each "
            "stance as you arrive - the form is a journey between stances, "
            "and sloppy stances make a sloppy form. Three: add the breath "
            "pattern - exhale on every strike, inhale on every transition "
            "and turn; the breath is the form's metronome. Four: sharpen "
            "the eyes - look where you strike before the technique moves, "
            "never after; the eyes lead, the body follows. Five: drill "
            "the turns separately, because turns are where forms fall "
            "apart - step, pivot, settle, then strike, in that order. Six: "
            "bring the speed up gradually over weeks, keeping every "
            "technique full-sized; small fast techniques are a different "
            "form than the one you learned. Seven: practice the form in "
            "both directions - mirror it - so the body learns the pattern, "
            "not just the side. Eight: perform it for an instructor or a "
            "camera; the form you can do watched is the form you actually "
            "know. Train the first aka daily - five slow repetitions beat "
            "one fast sloppy one."
        ),
        "key_points": [
            "Aka are bando's empty-hand forms: solo sequences where strikes, blocks, steps, and turns become one moving thing.",
            "Learn in chunks of three moves, joining them only when each chunk is clean - the whole form is never memorized at once.",
            "The breath is the metronome: exhale on strikes, inhale on transitions, and the form carries itself.",
            "The eyes lead and the body follows - look at the target before the technique moves, never after.",
            "Mirror the form in both directions so the body learns the pattern, not just the favored side.",
        ],
        "requirements": [
            "Enough clear floor to step, turn, and kick in all directions without hitting anything.",
            "A mirror or a camera for form checks - the form you can do watched is the form you know.",
            "The foundations solid first: stance, step, straight punch, parry, and front kick must be clean before the form.",
            "Daily short practice: five slow correct repetitions beat one fast sloppy one.",
            "An instructor to correct the turns, which are where every beginner's form falls apart.",
        ],
        "standards": [
            "Form standard: full stances, full-sized techniques, correct breath pattern, eyes leading - speed added only after correctness.",
            "The first aka must be performable mirror-smooth at full speed in both directions before the next is taught.",
            "Safety: forms are solo and low-risk, but fatigue-driven sloppiness is corrected, not drilled.",
        ],
        "citations": [CIT_WIKI_BANDO, CIT_ABA, CIT_MAUNGGYI],
        "sig_lens": (
            "The Signature read: the aka is the oath written in full. "
            "Drills are single words; the form is the sentence, and the "
            "body learns to speak in complete promises. Where public "
            "bando files a kata, the Signature method files a covenant "
            "recited without pause."
        ),
    },
    {
        "key": "tiger",
        "name": "Tiger System: Raking Strikes",
        "group": "Animal Systems",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The tiger is the first animal system most students meet, and "
            "it teaches the strategy of the committed attack: the tiger "
            "does not tap and retreat, it closes and rakes. In the ABA's "
            "nine animal systems, each animal is emulated as a fighting "
            "strategy rather than mimicked as a pose - the student does "
            "not pretend to be a tiger, but adopts the tiger's survival "
            "logic of powerful, raking, finishing attacks. The tiger's "
            "signature is the raking strike: the hand, fingers slightly "
            "hooked, tears down or across in a ripping motion, driven by "
            "a deep stance and a full drop of body weight. The tiger "
            "system also teaches the psychology of commitment - once the "
            "attack starts, it finishes, with no half-measures - and the "
            "stance work is deliberately low and rooted, because the "
            "tiger fights from the ground it owns. Students drill the "
            "rake on pads first, learning to tear rather than slap, and "
            "discover that the tiger's real lesson is not the claw but "
            "the follow-through: every tiger technique continues past "
            "contact until the job is done."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: drop into a low rooted "
            "stance - the tiger stance is lower than the ready stance, "
            "weight settled, because raking strikes need the body's drop "
            "behind them. Two: raise the hand high with fingers hooked "
            "like claws, wrist firm - the rake is a tearing tool, not a "
            "slap. Three: drive the hand down or across the target in a "
            "ripping motion, dropping your body weight with it; the "
            "power comes from the fall of the body, not the swing of the "
            "arm. Four: let the strike continue past contact - the rake "
            "tears through, it does not stop at the surface; "
            "follow-through is the tiger's signature. Five: the other "
            "hand guards or controls throughout - the tiger's off-hand "
            "holds while the raking hand works. Six: step in with the "
            "rake, closing distance as you strike; the tiger does not "
            "rake from far away. Seven: drill the downward rake on a pad "
            "ten times per hand, then the cross-rake, focusing on the "
            "body drop - if the stance does not sink, the rake is just "
            "an arm waving. Eight: practice the commitment drill - one "
            "rake, one step, one more rake, no pauses; the tiger does "
            "not tap and admire, it finishes."
        ),
        "key_points": [
            "The tiger teaches committed attack: close, rake, and follow through - no half-measures, no tapping and retreating.",
            "Animals are strategies to emulate, not poses to mimic: the student adopts the tiger's survival logic, not a costume.",
            "The rake tears with hooked fingers, powered by the body's drop from a low rooted stance - the fall is the engine.",
            "Follow-through is the signature: the rake continues past contact until the job is done.",
            "The off-hand guards or controls while the raking hand works - the tiger's two hands have two jobs.",
        ],
        "requirements": [
            "A low stance built on the foothold months - the tiger stance punishes weak legs.",
            "A pad or bag for raking practice; partner work uses controlled touch only.",
            "Wrist and finger conditioning through gradual pad work - hooked fingers must be strong.",
            "The commitment habit: drills that forbid pausing between rake and step.",
            "An instructor to check the body drop - without it the rake is decoration.",
        ],
        "standards": [
            "Tiger mechanics: low rooted stance, hooked-hand rake, body drop powering the tear, full follow-through, off-hand working.",
            "Strategy standard: the student must show the tiger's logic - closing, committing, finishing - not just the hand shape.",
            "Safety: rakes are pad and bag techniques; partner drills use touch contact with hand protection.",
        ],
        "citations": [CIT_ABA, CIT_WIKI_BANDO, CIT_MAUNGGYI],
        "sig_lens": (
            "The Signature read: the tiger is the covenant of commitment. "
            "Where public bando files an animal system, the Signature "
            "method files a promise to finish - the rake does not stop at "
            "the surface, and neither does the oath."
        ),
    },
    {
        "key": "boar",
        "name": "Boar System: The Rushing Entry",
        "group": "Animal Systems",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The boar's strategy is the furious, powerful rush: where the "
            "tiger commits to the strike, the boar commits to the ground "
            "itself, charging through distance with overwhelming forward "
            "pressure. In the ABA's animal systems the boar is the "
            "embodiment of unstoppable entry - the student learns to cross "
            "the dangerous middle distance not with caution but with a "
            "committed, protected rush that arrives before the defender "
            "can set. The mechanics are a wedge: head tucked, shoulders "
            "rolled in, elbows tight, driving off the rear leg in a "
            "straight line, striking as the rush arrives rather than "
            "after it stops. The boar teaches that hesitation in the "
            "middle distance is the most dangerous choice of all - "
            "better to be fully committed going in than half-committed "
            "standing still. Students drill the rush against pads, "
            "learning to keep the guard intact at speed and to strike "
            "on arrival, and the system's deeper lesson is courage as a "
            "technique: the rush is trained until forward pressure feels "
            "safer than retreat."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: from the ready stance, tuck "
            "the chin, roll the shoulders slightly in, and tighten the "
            "elbows - the boar's wedge protects the head and ribs at "
            "speed. Two: drive off the rear leg explosively and charge "
            "straight forward, keeping the steps short and driving - long "
            "leaping steps lose balance and the guard. Three: keep the "
            "hands up through the entire rush; speed tempts the hands "
            "down, and the drill is failed if the guard drops. Four: as "
            "you arrive, strike - the straight punch or the elbow thrown "
            "from the rush's momentum, not after stopping to set up. Five: "
            "drive through the target line, not to it; the rush ends "
            "past the opponent, with you turning to face them from a "
            "stance, never stopping in front of them. Six: practice the "
            "three-step rush - drive, drive, strike - on a straight line "
            "marked on the floor. Seven: add the partner drill: the "
            "partner retreats slowly while you rush under control, "
            "stopping at arm's length with a touch strike. Eight: build "
            "speed last - the wedge, the guard, and the arrival strike "
            "must be perfect at walking pace before the rush is allowed "
            "to run."
        ),
        "key_points": [
            "The boar's strategy is the furious powerful rush: committed forward pressure that crosses the middle distance before the defender can set.",
            "The wedge - chin tucked, shoulders in, elbows tight - protects the head and ribs at speed.",
            "Strike on arrival, not after stopping: the rush's momentum is part of the strike.",
            "Drive through the target line, ending past it in a stance - never stop in front of the opponent.",
            "Hesitation in the middle distance is the most dangerous choice; the boar trains forward pressure until it feels safer than retreat.",
        ],
        "requirements": [
            "A long clear runway - the rush needs ten to fifteen feet of straight open floor.",
            "A heavy bag or a pad holder braced for impact at the end of the rush.",
            "The guard habit under speed: drills fail and repeat whenever the hands drop.",
            "Strong legs and ankles - the explosive drive punishes weak foundations.",
            "An instructor controlling the partner rush drills, with strict stopping distances.",
        ],
        "standards": [
            "Boar mechanics: wedge guard, explosive rear-leg drive, short driving steps, strike on arrival, drive-through finish in stance.",
            "Control standard: full guard maintained at full speed; any dropped guard fails the rep.",
            "Safety: partner rush drills stop at arm's length with touch contact; the bag takes the full rush, people do not.",
        ],
        "citations": [CIT_ABA, CIT_WIKI_BANDO, CIT_MAUNGGYI],
        "sig_lens": (
            "The Signature read: the boar is the covenant of courage. "
            "Where public bando files a rushing entry, the Signature "
            "method files a promise that the middle distance will be "
            "crossed, not contemplated - forward pressure sworn at full "
            "speed with the guard unbroken."
        ),
    },
    {
        "key": "eagle",
        "name": "Eagle System: Hooking and Grasping",
        "group": "Animal Systems",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The eagle's strategy is control from above: hooking, "
            "grasping, and seizing the opponent's limbs and balance "
            "before striking. Where the tiger rakes and the boar rushes, "
            "the eagle catches - its talon-like hand shapes hook over "
            "wrists, behind necks, and under elbows, turning the "
            "opponent's own structure into a handle. The system's genius "
            "is that a grasped limb is a neutralized limb: one controlled "
            "wrist means one fewer weapon to fear, and the eagle builds "
            "its attacks on that arithmetic. Students develop the hooked "
            "hand - fingers curled like talons, thumb strong - through "
            "grip training and partner catching drills, learning to seize "
            "a wrist in motion, to hook behind the neck in the clinch, "
            "and to pull the caught limb into the strike that follows. "
            "The eagle also teaches the high guard: hands held high like "
            "wings, ready to come down over anything that rises. Its "
            "deeper lesson is patience as a weapon - the eagle waits for "
            "the limb to extend, then owns it."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: form the talon - fingers "
            "curled hard, thumb pressed against the fingers, the whole "
            "hand a hook; squeeze a ball or grip trainer daily to build "
            "the talon's strength. Two: practice the wrist catch - as a "
            "partner extends a slow straight punch, hook your lead hand "
            "over their wrist from above and pull it down and across your "
            "body, stepping offline as you pull. Three: the instant the "
            "wrist is caught, strike with the free hand - catch and hit "
            "are one beat, not two; the caught limb is the opening. Four: "
            "for the neck hook, in clinch range, hook the talon hand "
            "behind the partner's neck and pull down firmly while your "
            "other hand guards - control the head and you control the "
            "body. Five: drill the high guard - hands held high, elbows "
            "in - dropping the talons over incoming arms like wings "
            "folding. Six: train the timing slowly: the catch must meet "
            "the extended limb, never chase it; chasing hands get hit. "
            "Seven: flow drill - partner throws slow combinations, you "
            "catch one wrist per combination and answer with a touch "
            "strike. Eight: never crank a caught wrist or neck in drills "
            "- the eagle controls, it does not break; joint safety is "
            "absolute."
        ),
        "key_points": [
            "The eagle's strategy is control from above: hooking and grasping limbs, turning the opponent's structure into a handle.",
            "A grasped limb is a neutralized limb - one controlled wrist is one fewer weapon to fear, and the eagle builds on that arithmetic.",
            "Catch and hit are one beat: the seized wrist is the opening, and the free hand answers instantly.",
            "The talon hand - curled fingers, strong thumb - is built with daily grip training, not wished into existence.",
            "The catch meets the extended limb; chasing hands get hit - patience is the eagle's real weapon.",
        ],
        "requirements": [
            "Grip training tools: a squeeze ball or grip trainer for daily talon building.",
            "A cooperative partner for catching drills, moving slowly and honestly.",
            "Strict joint-safety rules: caught wrists and necks are controlled, never cranked.",
            "The high guard habit - hands high, elbows in - drilled until it is the default.",
            "An instructor supervising all clinch catching work.",
        ],
        "standards": [
            "Eagle mechanics: talon hand formation, catch from above on the extended limb, offline step with the pull, immediate answer.",
            "Timing standard: the catch meets, never chases; late catches are abandoned, not forced.",
            "Safety: zero joint cranking in drills; neck hooks use firm control only, released on any tap.",
        ],
        "citations": [CIT_ABA, CIT_WIKI_BANDO, CIT_MAUNGGYI],
        "sig_lens": (
            "The Signature read: the eagle is the covenant of control. "
            "Where public bando files hooking and grasping, the Signature "
            "method files a promise to own what is extended - the talon "
            "does not chase, it waits, and what it catches it keeps."
        ),
    },
    {
        "key": "cobra",
        "name": "Cobra System: Lightning Hand Strikes",
        "group": "Animal Systems",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The cobra's strategy is lightning-fast strikes to vital "
            "targets: the fastest hands in the nine animal systems, "
            "delivered with the suddenness of a snake's bite. The ABA's "
            "animal systems describe the cobra as using lightning fast "
            "strikes to vital targets, and the training follows that "
            "logic exactly - speed first, precision second, power a "
            "distant third, because the cobra's strike is over before "
            "the target knows it began. The system's signature is the "
            "fingertip and spear-hand strike: fingers extended and "
            "tightly joined, striking like a spearhead, or the first two "
            "knuckles snapping out in blinding doubles and triples. "
            "Students build cobra hands through speed drills - striking "
            "at a swinging target, at a partner's moving guard, at a "
            "hanging paper - learning that the strike's power comes from "
            "relaxation and snap, never from muscle. The deeper lesson is "
            "economy: the cobra moves nothing it does not need, sways "
            "offline by inches, and its whole art is the discipline of "
            "the shortest possible path from stillness to contact."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: relax completely - shake "
            "out the shoulders, arms, and hands; the cobra strike cannot "
            "be muscled, and tension is its enemy. Two: from the guard, "
            "snap the lead hand straight out and back in one blink, "
            "fingers together, striking with the fingertips or the first "
            "two knuckles - the strike is a flick of the whole arm, not "
            "a push. Three: the hand returns faster than it went out; "
            "the cobra's head is never left extended. Four: drill the "
            "double - two snaps in one breath, the second landing before "
            "the first is perceived; then the triple. Five: add the sway "
            "- as you strike, shift the head and torso inches offline, "
            "so the strike and the evasion are one motion. Six: practice "
            "on a hanging sheet of paper: the goal is to snap it without "
            "pushing it, which teaches the strike to end at contact. "
            "Seven: train the spear-hand - fingers extended, tightly "
            "joined, thumb tucked - striking pads only, never a partner, "
            "until the hand is conditioned over months. Eight: spar the "
            "cobra lightly with a partner, scoring touches with speed "
            "alone; if you are muscling, you are not doing the cobra."
        ),
        "key_points": [
            "The cobra's strategy is lightning-fast strikes to vital targets: speed first, precision second, power a distant third.",
            "Relaxation is the engine - the strike is a snap, never a muscled push; tension is the cobra's enemy.",
            "The hand returns faster than it goes out; the cobra's head is never left extended.",
            "Strike and sway are one motion: the head shifts inches offline as the hand snaps out.",
            "The paper drill teaches the strike to end at contact - snap the paper without pushing it.",
        ],
        "requirements": [
            "A hanging paper or light swinging target for snap training.",
            "Pads for spear-hand conditioning - fingers condition over months, never against hard targets.",
            "A partner with a moving guard for timing the snaps against motion.",
            "The relaxation habit: shoulder-shaking breaks between every speed set.",
            "Light-contact sparring rules for cobra practice - speed scores, power is forbidden.",
        ],
        "standards": [
            "Cobra mechanics: fully relaxed arm, snap extension, instant return, offline sway integrated, shortest path from guard.",
            "Speed standard: the double lands before the first is perceived; muscled strikes fail the drill.",
            "Safety: spear-hand strikes land on pads only until months of conditioning; partner work is light touch.",
        ],
        "citations": [CIT_ABA, CIT_WIKI_BANDO, CIT_MAUNGGYI],
        "sig_lens": (
            "The Signature read: the cobra is the covenant of speed. Where "
            "public bando files lightning hand strikes, the Signature "
            "method files a promise kept before it is perceived - the "
            "shortest path from stillness to contact, sworn in a blink."
        ),
    },
])
ENTRIES.extend([
    {
        "key": "viper",
        "name": "Viper System: Sinuous Evasion",
        "group": "Animal Systems",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The viper's strategy is the strike that cannot be found: "
            "sinuous, weaving movement that slips around defenses and "
            "arrives from angles the guard was not built to cover. Where "
            "the cobra is fast in a straight line, the viper is "
            "unfindable in a curve - its body flows offline, its hands "
            "weave through gaps, and its attacks come from the side "
            "door while the defender watches the front. Students learn "
            "the viper's signature sway: a fluid lateral shift of the "
            "head and torso that moves inches but changes everything, "
            "combined with weaving hand strikes that travel around "
            "rather than through the guard. The footwork is serpentine - "
            "small sliding steps that never commit the weight, always "
            "ready to flow the other way. The viper's deeper lesson is "
            "that straight lines are honest and therefore readable: the "
            "fighter who moves only in straight lines can be timed, "
            "while the fighter who flows is always somewhere slightly "
            "different than expected. Drills pair the sway with the "
            "counter, teaching the body that evasion and attack are the "
            "same flowing motion."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: from the ready stance, "
            "practice the sway - shift the head and shoulders six inches "
            "to the outside while the feet stay planted, then flow back; "
            "the sway is a liquid motion, never a jerk. Two: add the "
            "weaving strike - as you sway outside, let the lead hand "
            "travel in a small curve around the guard line, arriving "
            "from the side angle; the curve is what makes it unfindable. "
            "Three: drill the serpentine step - slide the lead foot six "
            "inches offline, let the rear foot follow, weight never fully "
            "committing; you should be able to reverse direction "
            "instantly. Four: combine them - sway, serpentine step, "
            "weaving strike - as one flowing sequence with no pauses "
            "between the parts. Five: practice against a partner's slow "
            "straight punches: sway offline by inches and let the weaving "
            "hand answer around their guard. Six: keep everything small "
            "- the viper's movements are inches, not feet; big weaves "
            "are just dancing and they get hit. Seven: breathe smoothly "
            "through the flow; held breath makes the body rigid and the "
            "viper is never rigid. Eight: drill the reversal - flow one "
            "way, then instantly flow back the other; the viper's "
            "deadliest trait is that it is never where it was."
        ),
        "key_points": [
            "The viper's strategy is the unfindable strike: sinuous movement that arrives from angles the guard was not built to cover.",
            "The sway moves the head inches offline in a liquid motion - small, smooth, and timed to the attack.",
            "Weaving strikes travel around the guard rather than through it; the curve is what makes them unfindable.",
            "Serpentine footwork never commits the weight, so direction can reverse instantly - the viper is never where it was.",
            "Evasion and attack are one flowing motion: the sway carries the counter with it.",
        ],
        "requirements": [
            "A partner throwing slow straight punches to sway against - the viper is learned against real lines.",
            "A mirror for the sway: it must be liquid, and mirrors do not flatter jerks.",
            "The discipline of smallness: drills fail when the weave grows bigger than inches.",
            "Smooth breathing through the flow - held breath makes a rigid body.",
            "Touch-contact sparring to test the weave against a live guard.",
        ],
        "standards": [
            "Viper mechanics: liquid sway, serpentine uncommitted steps, curved weaving strikes, instant reversibility.",
            "Size standard: all viper movement stays within inches; anything larger is not the viper.",
            "Safety: partner sway drills use slow punches and touch counters; speed rises only with control.",
        ],
        "citations": [CIT_ABA, CIT_WIKI_BANDO, CIT_MAUNGGYI],
        "sig_lens": (
            "The Signature read: the viper is the covenant of the "
            "unfindable. Where public bando files sinuous evasion, the "
            "Signature method files a promise to never be where the "
            "attack expected - sworn in inches, kept in curves."
        ),
    },
    {
        "key": "python",
        "name": "Python System: Wraps and Crushes",
        "group": "Animal Systems",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The python's strategy is the one the ABA's animal systems "
            "describe most vividly: the python wraps and crushes and "
            "locks the opponent. Where other animals strike, the python "
            "enfolds - its limbs coil around the opponent's arms, neck, "
            "and torso, and each coil tightens the last until movement "
            "itself becomes the enemy. The system's techniques are "
            "wrapping controls: the arm wraps over and under the "
            "opponent's arm, the body turns in to coil the torso, the "
            "legs hook to break the base, and every wrap is a lock "
            "waiting for its final turn. Students learn that the "
            "python never hurries - haste breaks the coil - and that "
            "the wrap's power comes from the whole body turning as one "
            "screw, not from arm strength. The python's deeper lesson is "
            "that control compounds: one wrap limits, two wraps stop, "
            "three wraps finish, and the patient fighter who builds the "
            "coils one by one is never in a race. All python work is "
            "partner work, and all of it ends the instant the partner "
            "taps - the coil is a tool of control, and control means "
            "knowing when to release."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: from a clinch or close "
            "exchange, wrap your arm over your partner's arm and under "
            "your own - the over-under coil is the python's first loop; "
            "move slowly and let the partner feel each stage. Two: step "
            "in close, chest to chest, and turn your whole torso like a "
            "screw - the coil tightens from the body turn, not from "
            "squeezing with the arms. Three: add the second loop - your "
            "other arm wraps the partner's torso or neck gently, always "
            "with the partner's comfort as the gauge; you are building "
            "control, not pain. Four: hook your leg behind their leg to "
            "break the base - the coil now holds the body and the base "
            "together. Five: tighten one quarter-turn at a time, pausing "
            "between turns; the python's patience is the technique. Six: "
            "the instant the partner taps - hand tap, foot tap, or word - "
            "release completely and immediately; the tap is sacred and "
            "instant. Seven: drill the wrap flow slowly - over-under, "
            "turn, second loop, leg hook, quarter-turn - until the "
            "sequence is smooth at a walking pace. Eight: never apply a "
            "wrap at speed or with force on a partner who has not agreed "
            "to the drill; the python is practiced in slow cooperation "
            "or not at all."
        ),
        "key_points": [
            "The python wraps and crushes and locks: each coil tightens the last, and control compounds - one wrap limits, two stop, three finish.",
            "The coil tightens from the whole body's screw-turn, not from arm squeezing; haste breaks the coil.",
            "The tap is sacred: hand, foot, or word, the release is instant and complete, every time.",
            "Python work is slow cooperative partner work - the wrap is built one quarter-turn at a time with the partner's comfort as the gauge.",
            "The deeper lesson is patience as a weapon: the python never hurries, and never races.",
        ],
        "requirements": [
            "A fully cooperative partner and a mat - python work never happens standing on hard floors.",
            "An instructor present for all wrapping and locking drills, no exceptions.",
            "The tap rule understood by both partners before any coil is built.",
            "Slow-speed discipline: the wrap flow is drilled at walking pace until it is smooth.",
            "Joint-safety knowledge: wraps control position; they are never cranked for pain.",
        ],
        "standards": [
            "Python mechanics: over-under coil, whole-body screw turn, progressive loops, leg hook for the base, quarter-turn tightening.",
            "Control standard: the partner's comfort gauges the coil; any tap ends the technique instantly.",
            "Safety: slow cooperative drilling only; no speed, no force, no unagreed wrapping - ever.",
        ],
        "citations": [CIT_ABA, CIT_WIKI_BANDO, CIT_MAUNGGYI],
        "sig_lens": (
            "The Signature read: the python is the covenant of compounding "
            "control. Where public bando files wraps and locks, the "
            "Signature method files a promise that tightens one "
            "quarter-turn at a time - and a promise to release the "
            "instant it is asked."
        ),
    },
    {
        "key": "panther",
        "name": "Panther System: The Sweep",
        "group": "Animal Systems",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The panther's strategy is the sudden takedown: silent "
            "approach, explosive sweep, the fight decided in the instant "
            "the opponent's base disappears. In the ABA's animal systems "
            "the panther is the master of the leg sweep - a low, fast "
            "strike with the foot or calf against the opponent's ankle "
            "or calf, timed to the exact moment their weight commits to "
            "that leg. The sweep is bando's most technical takedown "
            "because it uses almost no strength: it is pure timing, "
            "leveraging the opponent's own weight transfer against them. "
            "Students learn to read the step - the telltale shift of "
            "weight onto the lead leg - and to answer it with a sweep "
            "that arrives as the weight lands, not before and not after. "
            "The panther's deeper lesson is patience in motion: the "
            "fighter circles quietly, offering no target, and the sweep "
            "is the period at the end of a sentence the opponent did not "
            "know was being written. Every sweep drill ends with the "
            "partner's breakfall, because the panther always respects "
            "the ground it sends people to."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: circle your partner "
            "quietly at kicking range, watching their feet - the sweep "
            "targets the exact moment weight commits to the lead leg. "
            "Two: as their lead foot plants and their weight shifts onto "
            "it, swing your rear foot in a low fast arc against the back "
            "of their ankle or calf - the sweep is a scythe, not a kick, "
            "and it stays inches off the floor. Three: time it to the "
            "weight transfer - sweeping an unweighted leg does nothing, "
            "sweeping a weighted leg at the wrong angle does little; the "
            "window is the heartbeat when the weight lands. Four: as the "
            "sweep connects, pull their upper body gently the other way "
            "with your guard hand - the sweep takes the base, the hand "
            "takes the balance, and the two together take the person. "
            "Five: follow them down with control - never turn away from "
            "a falling partner; the panther stays responsible. Six: the "
            "partner breakfalls - side or back fall, slapping and "
            "exhaling - and both reset. Seven: drill the timing slowly: "
            "partner steps, you sweep at half speed, fifty times each "
            "side, until the weight-transfer moment is unmistakable. "
            "Eight: never sweep at full speed until the partner's "
            "breakfall is automatic - the sweep is only as safe as the "
            "fall it causes."
        ),
        "key_points": [
            "The panther's strategy is the sudden takedown: the sweep removes the base at the exact moment weight commits to it.",
            "The sweep is pure timing, not strength - an unweighted leg cannot be swept, and timing is the whole technique.",
            "The sweep is a low scythe inches off the floor, paired with a gentle pull on the upper body: base and balance go together.",
            "Read the step: the telltale weight shift onto the lead leg is the sweep's invitation.",
            "Every sweep drill ends with the partner's breakfall - the panther respects the ground it sends people to.",
        ],
        "requirements": [
            "A mat and a partner whose breakfall is automatic - the sweep waits for the fall, never the reverse.",
            "Ankle and calf conditioning for the sweeping leg through gradual bag work.",
            "The timing eye: fifty slow reps per side reading the weight transfer before any speed.",
            "An instructor supervising all live sweep practice.",
            "The discipline to follow the partner down with control and reset together.",
        ],
        "standards": [
            "Panther mechanics: low scythe sweep at the weight-transfer moment, paired upper-body guidance, controlled follow-through.",
            "Timing standard: the sweep lands as the weight lands - early and late sweeps are failed reps.",
            "Safety: full-speed sweeps only with automatic breakfalls, on mats, under instructor supervision.",
        ],
        "citations": [CIT_ABA, CIT_WIKI_BANDO, CIT_MAUNGGYI],
        "sig_lens": (
            "The Signature read: the panther is the covenant of timing. "
            "Where public bando files a leg sweep, the Signature method "
            "files a promise to arrive at the exact heartbeat the weight "
            "lands - and to honor the fall it causes."
        ),
    },
    {
        "key": "bull",
        "name": "Bull System: Charging Power",
        "group": "Animal Systems",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The bull's strategy is overwhelming forward power: where the "
            "boar rushes to enter, the bull charges to demolish - a "
            "full-body drive that treats the opponent's guard as a door "
            "to go through rather than a wall to go around. In the ABA's "
            "nine animal systems the bull is the heaviest hitter, and "
            "its techniques are built on mass in motion: the charging "
            "shoulder, the driving double-hand push, the low tackle-like "
            "entry that lifts and dumps. Students learn that the bull's "
            "power is not anger - anger makes the charge wild and the "
            "wild charge is easily sidestepped - but committed structure: "
            "head up, back straight, driving off the rear leg, hitting "
            "with the shoulder and hips as one battering ram. The bull "
            "teaches the difference between force and fury: force is "
            "aimed and structured, fury is neither, and only force can be "
            "trained. All bull entries are drilled on bags and pads first, "
            "because the bull's honesty is that it commits everything - "
            "and everything committed must be aimed."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: lower your level - bend "
            "the knees deeply and drop the hips; the bull charges low, "
            "because low beats high when mass meets mass. Two: drive off "
            "the rear leg in a straight line, head up and eyes forward - "
            "never drop the head, a lowered head cannot see the sidestep. "
            "Three: strike with the lead shoulder, turning the hips into "
            "it at the last instant - the shoulder is the battering ram's "
            "head, the hips and legs are the crew pushing it. Four: keep "
            "the arms in a tight guard or wrapping position through the "
            "charge; flailing arms are handles for the opponent. Five: "
            "drive through, not to - the charge ends three steps past "
            "the contact point, with you turning back in stance. Six: "
            "drill the charge on a heavy bag: lower, drive, shoulder "
            "contact, drive through - ten reps, resting between, because "
            "full bull charges are exhausting. Seven: practice the "
            "structured stop - charge, and on the instructor's clap, "
            "stop dead in stance; the bull must be able to halt its own "
            "power. Eight: partner drills are bag-only for the full "
            "charge; with a partner, drill only the low entry step and "
            "the shoulder touch, never the full drive."
        ),
        "key_points": [
            "The bull's strategy is overwhelming forward power: mass in motion, aimed and structured, treating the guard as a door.",
            "Force is trained, fury is not: the bull's charge is aimed structure - head up, back straight, driving off the rear leg.",
            "The lead shoulder is the battering ram's head; the hips and legs are the crew pushing it.",
            "Drive through, not to: the charge ends past the contact point, turning back in stance.",
            "The bull must be able to halt its own power - the structured stop is as much the technique as the charge.",
        ],
        "requirements": [
            "A heavy bag that can take a full charging shoulder - the bull is not a pad technique.",
            "Strong legs and a healthy back: the low drive punishes weak foundations.",
            "The structured-stop drill mastered before any full-speed charge.",
            "A long clear runway with nothing to hit beyond the bag.",
            "An instructor's clap as the stop signal - the bull answers to a voice, not to adrenaline.",
        ],
        "standards": [
            "Bull mechanics: low level, rear-leg drive, head up, shoulder contact with hip turn, drive-through finish, structured stop.",
            "Control standard: the charge halts dead on the clap at any point - an unstoppable bull is an untrained bull.",
            "Safety: full charges land on the heavy bag only; partner work is limited to the entry step and shoulder touch.",
        ],
        "citations": [CIT_ABA, CIT_WIKI_BANDO, CIT_MAUNGGYI],
        "sig_lens": (
            "The Signature read: the bull is the covenant of structured "
            "force. Where public bando files a charging entry, the "
            "Signature method files a promise that power will be aimed - "
            "fury is never sworn, only force, and force can be halted on "
            "a clap."
        ),
    },
    {
        "key": "scorpion",
        "name": "Scorpion System: Deceptive Strikes",
        "group": "Animal Systems",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The scorpion's strategy is deception: the strike that comes "
            "from where the eyes are not looking, the tail that arches "
            "over while the claws hold the attention. In the ABA's nine "
            "animal systems the scorpion is the master of the feint and "
            "the unexpected angle - its techniques show one thing and "
            "deliver another, and its students learn that attention is "
            "the real battlefield. The system's signature is the "
            "overhand arc: the hand travels up and over like the "
            "scorpion's tail, arriving from above and behind the guard's "
            "edge, often after the other hand has shown a low or straight "
            "threat to pull the guard down or out. Students drill the "
            "feint-strike pair until the feint is honest - a feint that "
            "the body does not believe is just waving, and waving gets "
            "hit. The scorpion's deeper lesson is about perception: "
            "every fighter guards what they see, so the art is in "
            "deciding what they see. It is also the system's ethics "
            "lesson - deception in technique is fair craft; deception "
            "outside the agreed rules of training is not, and the "
            "scorpion's student is held to that line strictly."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: establish a pattern - "
            "throw two or three honest low straight strikes so the "
            "partner's guard learns to expect them; the scorpion's "
            "deception needs a truth to hide behind. Two: on the next "
            "exchange, begin the same low strike - same shoulder, same "
            "hip, same first six inches - so the body believes it. Three: "
            "at the commitment point, arc the hand up and over instead, "
            "the elbow rising like the scorpion's tail, striking down "
            "from above and behind the guard's edge. Four: the other hand "
            "stays honest - it guards, or it shows the low threat again; "
            "the tail strikes while the claws hold the attention. Five: "
            "return instantly along the arc; the overhand that lingers is "
            "a gift to the counter. Six: drill the pair slowly - feint "
            "low, arc over - fifty times, until the first six inches of "
            "both are identical. Seven: add the angle change - step "
            "offline as the tail arcs, so the strike arrives from a new "
            "direction as well as a new height. Eight: spar the scorpion "
            "lightly, and count: if the partner reads the arc more than "
            "once in ten, the feint is not honest yet - go back to the "
            "slow pair."
        ),
        "key_points": [
            "The scorpion's strategy is deception: show one thing, deliver another - the tail arcs over while the claws hold the attention.",
            "Every deception needs a truth to hide behind: establish the honest pattern first, then break it.",
            "The feint must be honest - the first six inches identical - because a feint the body does not believe is just waving.",
            "The overhand arc returns instantly along its path; a lingering tail is a gift to the counter.",
            "Deception in technique is fair craft; the scorpion's student holds the line on deception outside the agreed rules.",
        ],
        "requirements": [
            "A cooperative partner with a live guard to deceive - the scorpion is learned against real attention.",
            "The slow pair drilled fifty times before any speed: identical first six inches, always.",
            "Light-contact sparring to test whether the arc is actually read or actually lands.",
            "The honesty check: if the partner reads it more than once in ten, back to slow drilling.",
            "An instructor to hold the ethics line on fair deception in training.",
        ],
        "standards": [
            "Scorpion mechanics: established pattern, identical feint initiation, arcing overhand from above the guard's edge, instant return, offline step.",
            "Deception standard: the technique must actually deceive a live guard in light sparring - theory without results is not the scorpion.",
            "Safety: light contact only for deception sparring; the arc's target is the guard's edge, control is absolute.",
        ],
        "citations": [CIT_ABA, CIT_WIKI_BANDO, CIT_MAUNGGYI],
        "sig_lens": (
            "The Signature read: the scorpion is the covenant of the "
            "unseen. Where public bando files deceptive strikes, the "
            "Signature method files a promise about attention itself - "
            "that what is shown will be honest, and what is hidden will "
            "be fair."
        ),
    },
    {
        "key": "naban-clinch",
        "name": "Naban: Standing Clinch Control",
        "group": "Grappling and Naban",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Naban is Burmese wrestling - the grappling art of the thaing "
            "family, and bando's closest relative. Where bando strikes at "
            "range, naban controls at contact: the standing clinch is its "
            "front door, the position where two fighters grip head, neck, "
            "and arms, each fighting for the inside position that decides "
            "everything after. Clinch control is not hugging - it is a "
            "standing wrestling match fought with frames, underhooks, "
            "head position, and hip placement, and the fighter who wins "
            "the clinch usually wins what follows. Students learn the "
            "plumb - both hands behind the opponent's neck, elbows tight, "
            "controlling the head - and its counters: the frame, the "
            "underhook, the head-position battle. The clinch teaches the "
            "body's truth about strength: structure beats muscle, the "
            "fighter with the better frame controls the stronger fighter, "
            "and relaxation under pressure is a skill drilled, not a gift. "
            "All clinch work is cooperative partner training with clear "
            "tap and release rules."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: enter the clinch from "
            "striking range with your guard up - never reach for the "
            "clinch with your hands down; the entry is earned, not given. "
            "Two: establish the plumb - both hands behind the partner's "
            "neck, fingers interlaced or palms on the skull, elbows "
            "pulled tight to your ribs; the elbows-in position is the "
            "whole technique. Three: control the head - pull it down "
            "gently and turn it slightly; where the head goes, the body "
            "follows, and head control is clinch control. Four: fight for "
            "inside position - your arms inside theirs, your head to the "
            "side of theirs, your hips close; drill the pummeling flow - "
            "swim one arm inside, they swim back - as a continuous "
            "cooperative rhythm. Five: frame when you are losing - "
            "forearm across their neck or shoulder, creating space to "
            "re-pummel; the frame is the clinch's emergency brake. Six: "
            "stay relaxed and breathe - the clinch punishes tension, and "
            "the relaxed fighter feels the partner's intentions first. "
            "Seven: drill three-minute pummeling rounds, switching "
            "partners, with the rule that anyone can call a reset at any "
            "time. Eight: respect the tap and the word - any discomfort "
            "with neck pressure ends the round instantly, no questions."
        ),
        "key_points": [
            "Naban is Burmese wrestling, bando's grappling relative: the standing clinch is its front door and inside position decides everything after.",
            "The plumb - hands behind the neck, elbows tight to the ribs - is the position; elbows-in is the whole technique.",
            "Control the head and you control the body; the frame - forearm across neck or shoulder - is the emergency brake.",
            "Structure beats muscle: the better frame controls the stronger fighter, and relaxation under pressure is drilled, not gifted.",
            "Pummeling - swimming for inside position - is drilled as a continuous cooperative rhythm, not a fight.",
        ],
        "requirements": [
            "A cooperative partner and a mat - clinch work never happens on hard floors.",
            "Clear tap, word, and reset rules agreed before any clinch round begins.",
            "An instructor present for all clinch training.",
            "Neck and shoulder warm-ups: the clinch loads the neck, and cold necks get hurt.",
            "The relaxation habit - tension is the clinch beginner's tax, paid in exhaustion.",
        ],
        "standards": [
            "Clinch mechanics: guarded entry, plumb with elbows in, head control, inside-position pummeling, framing as the reset.",
            "Cooperation standard: pummeling is a shared rhythm; muscling through a partner's frame fails the drill.",
            "Safety: any neck discomfort ends the round instantly; no cranking, no jerking, ever.",
        ],
        "citations": [CIT_WIKI_BANDO, CIT_ABA, CIT_MTF, CIT_MAUNGGYI],
        "sig_lens": (
            "The Signature read: the clinch is the covenant of structure. "
            "Where public naban files standing control, the Signature "
            "method files a promise that frame will beat force - sworn "
            "chest to chest, kept with elbows in and breath steady."
        ),
    },
    {
        "key": "naban-throw",
        "name": "Naban: The Hip Throw",
        "group": "Grappling and Naban",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The hip throw is naban's signature takedown and the "
            "mechanical marvel of the grappling ladder: a smaller person "
            "throwing a larger one by turning the hip into a fulcrum and "
            "the opponent's own forward pressure into the throwing force. "
            "The technique is pure leverage - the thrower steps in, turns "
            "the back to the opponent, seats the hips below the "
            "opponent's hips, and then straightens the legs and pulls, "
            "levering the opponent's body over the hip like a sack over "
            "a fence. Students discover the throw's paradox on day one: "
            "muscling it fails, and relaxing into the leverage succeeds - "
            "the hip throw punishes strength and rewards position. It is "
            "taught only after the breakfall is automatic, only on mats, "
            "only with a cooperative partner, and only under an "
            "instructor's eye, because the throw ends with a person in "
            "the air. The hip throw is also the ladder's clearest proof "
            "of the 9x9 matrix principle: the specific throw fits one "
            "situation, but the principle - the hip as fulcrum, the "
            "opponent's force as the engine - appears in half the "
            "grappling arts on earth."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: from the clinch, pull your "
            "partner slightly forward - the hip throw needs their "
            "pressure coming toward you; never try to throw a person who "
            "is pulling away. Two: step in deep, your back foot landing "
            "between their feet, and turn your back to them in one "
            "smooth pivot - the turn, not the pull, is the entry. Three: "
            "sink your hips below theirs, back straight, knees bent - "
            "your hips are now the fulcrum and they must be the lower "
            "ones. Four: pull their upper body forward and down over "
            "your shoulder while you straighten your legs explosively - "
            "legs drive, arms guide, hips lever; the throw is a leg "
            "press with a steering wheel. Five: keep pulling through the "
            "throw - the partner should travel over your hip in a clean "
            "arc, not get stuck halfway. Six: as they fall, guide them - "
            "never let go of a person you are throwing; the thrower is "
            "responsible for the landing. Seven: the partner breakfalls - "
            "side fall, slap, exhale - and both partners reset and switch "
            "roles. Eight: drill the entry without the throw first - "
            "step, turn, sink - fifty times; then add the throw at "
            "quarter effort, building up only as the partner's comfort "
            "allows."
        ),
        "key_points": [
            "The hip throw is pure leverage: your hips become the fulcrum below theirs, and their forward pressure becomes the throwing force.",
            "Muscling fails and position succeeds - the throw punishes strength and rewards the correct entry.",
            "The entry is step, turn, sink: deep step between their feet, smooth pivot, hips below hips - before any pull.",
            "The throw is a leg press with a steering wheel: legs drive explosively, arms guide, hips lever.",
            "The thrower is responsible for the landing: guide the partner through the arc, never let go mid-throw.",
        ],
        "requirements": [
            "An automatic breakfall in the partner - the throw waits for the fall, never the reverse.",
            "A proper mat, an instructor present, and a cooperative partner: all three, every time.",
            "The entry drilled fifty times without the throw before any lift is attempted.",
            "Knee and back health: the deep sink and leg drive load both, and pain stops the drill.",
            "Role switching: every thrower is also thrown, every session.",
        ],
        "standards": [
            "Hip-throw mechanics: forward-pressure setup, deep step, smooth turn, hips below hips, leg drive with guiding pull, controlled arc.",
            "Leverage standard: the throw must work without muscling - if it needs strength, the position is wrong.",
            "Safety: mats mandatory, instructor present, cooperative partner only, thrower guides the landing, breakfall automatic first.",
        ],
        "citations": [CIT_ABA, CIT_MTF, CIT_HAY, CIT_MAUNGGYI],
        "sig_lens": (
            "The Signature read: the hip throw is the covenant of leverage. "
            "Where public naban files a takedown, the Signature method "
            "files a promise that position will beat power - the hip the "
            "fulcrum, the opponent's own pressure the engine, the landing "
            "the thrower's responsibility."
        ),
    },
])
ENTRIES.extend([
    {
        "key": "naban-pin",
        "name": "Naban: Ground Holds and Pins",
        "group": "Advanced Grappling",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "When naban's standing work succeeds, the fight goes to the "
            "ground - and the ground has its own grammar. The pin is "
            "naban's ground-control technique: holding the opponent's "
            "shoulders to the mat with weight, position, and leverage "
            "rather than squeezing strength. A good pin is heavy the way "
            "a blanket is heavy - distributed, smothering, inescapable "
            "without being painful - and it is the foundation of all "
            "advanced ground work, because control must come before any "
            "finish. Students learn the side pin first: chest to chest, "
            "hips low and heavy, head positioned to block the escape, "
            "arms controlling the far arm and the near hip. The pin "
            "teaches the ground's central lesson: weight is a technique. "
            "The relaxed heavy fighter pins the tense strong fighter, "
            "because tension holds the body up and relaxation lets it "
            "sink. Escapes are drilled alongside every pin - the bridge, "
            "the shrimp, the underhook recovery - so both partners learn "
            "both sides, and every pin ends on the tap with an instant, "
            "complete release."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: from a grounded partner, "
            "settle into the side pin - your chest on theirs, your hips "
            "low and heavy near the mat, your head on the far side "
            "blocking their turn into you. Two: control the far arm - "
            "your arm under their head or over their far shoulder - and "
            "the near hip with your other hand; two points of control "
            "minimum, always. Three: be heavy, not strong - relax your "
            "whole body and let your weight sink through them into the "
            "mat; if your muscles are working hard, you are doing it "
            "wrong. Four: keep your base wide - knees spread, toes "
            "driving - so their bridge cannot tip you; a narrow pin is "
            "a pin waiting to be reversed. Five: the partner practices "
            "the bridge escape - hips exploding upward to create space - "
            "and the shrimp escape - hips scooting out to recover guard; "
            "you ride the escape lightly, learning to feel it early. Six: "
            "switch roles every three minutes - every pinner is also "
            "pinned, every session. Seven: drill the pin transitions - "
            "side pin to mount to back control - as a slow flow, never "
            "racing; the ground rewards the smooth, not the fast. Eight: "
            "the tap ends everything instantly - hand, foot, or word - "
            "and the release is complete before the next breath."
        ),
        "key_points": [
            "The pin holds with weight, position, and leverage - heavy like a blanket, distributed and smothering, never squeezing strength.",
            "Weight is a technique: the relaxed heavy fighter pins the tense strong fighter, because relaxation lets the body sink.",
            "Two points of control minimum - far arm and near hip - with a wide base that no bridge can tip.",
            "Every pin is drilled with its escapes - the bridge and the shrimp - so both partners learn both sides of the ground.",
            "The tap ends everything instantly and the release is complete; control means knowing when to let go.",
        ],
        "requirements": [
            "A mat and a cooperative partner - ground work never happens on hard floors.",
            "An instructor present for all pin and transition drilling.",
            "The tap rule drilled before the first pin: hand, foot, or word ends it instantly.",
            "Role switching every three minutes - no one only pins.",
            "Hip mobility and core endurance: the ground game is built on both.",
        ],
        "standards": [
            "Pin mechanics: chest-to-chest weight, low heavy hips, head blocking the turn, two-point control, wide base.",
            "Weight standard: the pin must work through relaxation and position - muscled pins fail the drill.",
            "Safety: instant release on any tap; no pressure on the neck or throat in pin practice; instructor present always.",
        ],
        "citations": [CIT_ABA, CIT_MTF, CIT_MAUNGGYI],
        "sig_lens": (
            "The Signature read: the pin is the covenant of weight. Where "
            "public naban files ground control, the Signature method files "
            "a promise that heaviness will be earned by relaxation - sworn "
            "chest to chest, released the instant it is asked."
        ),
    },
    {
        "key": "khut-thaing",
        "name": "Khut Thaing: Pressure-Point Study",
        "group": "Advanced Principles",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Khut thaing is the pressure-point art of the thaing family - "
            "the study of the body's sensitive points and the precise, "
            "controlled striking or pressing methods used on them. In "
            "bando's advanced ladder it is taught as a study, not a "
            "weapon: the student learns the anatomy - where nerves run "
            "close to the surface, where joints are vulnerable to "
            "leverage, where the body's alarm points live - because the "
            "advanced fighter must understand the machine they have spent "
            "years learning to move. The training is academic and "
            "controlled: points are located on charts and on the student's "
            "own body first, pressure is applied gradually and lightly "
            "with a partner, and the entire study is framed by the "
            "civilian traditional-art scope - knowledge for understanding "
            "the body, for controlled training, and for the deeper "
            "appreciation of why bando's strikes target what they target. "
            "Students map the major points - the jaw hinge, the side of "
            "the neck's great vessels, the solar plexus, the floating "
            "ribs, the inner thigh's nerve line, the instep - and drill "
            "only light touch location with a partner, never force. Khut "
            "thaing's real lesson is restraint: to know exactly where "
            "harm lives and to choose, every time, not to go there."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: study the chart first - "
            "learn the major points on paper: jaw hinge, side of the "
            "neck, solar plexus, floating ribs, inner thigh nerve line, "
            "instep, and the wrist and elbow leverage points. Two: find "
            "each point on your own body with light fingertip pressure - "
            "your own anatomy is the first textbook, and it cannot be "
            "hurt by your own careful touch. Three: with a partner, "
            "practice location only - light fingertip touch on the agreed "
            "point, the partner confirming or correcting the location; "
            "this is a mapping drill, not a striking drill. Four: learn "
            "the leverage points through the python wraps - the wrist "
            "and elbow controls from the animal system, applied slowly "
            "to the point of control and never beyond. Five: drill the "
            "restraint protocol - approach the point, locate it, and "
            "stop; the advanced student proves knowledge by stopping, "
            "not by continuing. Six: study why bando's strikes target "
            "what they target - connect each point to the strikes learned "
            "in the core ladder. Seven: keep a study journal mapping each "
            "point, its anatomy, and the safe training method for it. "
            "Eight: never practice force on any point with a partner - "
            "khut thaing in this school is knowledge and control, and "
            "force has no place in its drills."
        ),
        "key_points": [
            "Khut thaing is the thaing family's pressure-point study: the anatomy of sensitive points, taught as knowledge, not as a weapon.",
            "The student's own body is the first textbook - every point is found on yourself with careful touch before any partner work.",
            "Partner drills are location-only: light fingertip touch on agreed points, mapping, never force.",
            "The restraint protocol is the technique: approach, locate, and stop - the advanced student proves knowledge by stopping.",
            "The real lesson is restraint: to know exactly where harm lives and to choose, every time, not to go there.",
        ],
        "requirements": [
            "Anatomy charts of the major points for the study phase.",
            "A cooperative partner and explicit agreement on which points are mapped in each session.",
            "An instructor present for all partner point-location work.",
            "A study journal for mapping each point, its anatomy, and its safe training method.",
            "The restraint ethic understood before the first partner drill - knowledge, not force.",
        ],
        "standards": [
            "Study standard: every point mapped on chart, then on self, then located lightly on a partner - in that order, never skipped.",
            "Force standard: zero force on points in partner drills; leverage controls stop at the point of control.",
            "Safety: partner point work is location-only with light touch; any discomfort ends the drill instantly.",
        ],
        "citations": [CIT_MTF, CIT_ABA, CIT_MAUNGGYI],
        "sig_lens": (
            "The Signature read: khut thaing is the covenant of restraint. "
            "Where the thaing family files pressure-point knowledge, the "
            "Signature method files a promise to know exactly where harm "
            "lives - and to stop one inch before it, every time."
        ),
    },
    {
        "key": "combos",
        "name": "Combination Chains: Principle Over Pattern",
        "group": "Advanced Strikes",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "A combination is not a memorized sequence - it is a "
            "conversation, and bando's advanced striking teaches the "
            "grammar, not the script. The 9x9 matrix principle governs "
            "here: one technique fits one situation, but the principle "
            "underneath fits many, so the advanced student learns to "
            "build combinations from principles - the straight punch "
            "draws the guard, the hook goes around it; the low kick "
            "plants the weight, the sweep takes it. Students drill the "
            "classic chains first - jab-cross-hook, punch-low kick, "
            "parry-counter-sweep - but the training goal is improvisation: "
            "reading the partner's reactions and chaining the next "
            "technique to what the last one created. Every combination "
            "follows the same architecture: an opener that demands a "
            "response, a second strike that exploits the response, and a "
            "finisher or exit that ends the exchange safely. The advanced "
            "lesson is that combinations are built on the opponent's "
            "reactions, not on your plan - the plan is just the first "
            "word, and the opponent writes the rest."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: master the two-beat chain "
            "first - jab, cross - thrown as one breath, the second punch "
            "leaving as the first returns; drill it a hundred times until "
            "it is a single word. Two: add the third beat - jab, cross, "
            "hook - the hook turning the hips fully as the cross's "
            "momentum feeds it; three beats, one breath, no pauses. Three: "
            "learn the architecture - opener, exploitation, exit: the "
            "opener demands a response (the jab), the second exploits it "
            "(the cross through the opened guard), the third ends it "
            "(the hook) or exits (step out to stance). Four: drill the "
            "cross-range chain - straight punch, low kick: the punch "
            "plants their weight on the lead leg, the kick takes the "
            "planted leg. Five: drill the defense-to-offense chain - "
            "parry, straight counter, sweep: the parry creates the "
            "opening, the counter uses it, the sweep finishes the "
            "exchange. Six: practice improvisation - the partner feeds "
            "random guards and reactions, and you chain two to three "
            "techniques to whatever appears. Seven: always end in stance "
            "- a combination that leaves you unbalanced is a sentence "
            "without a period. Eight: spar the chains lightly, counting "
            "clean three-beat chains; if the beats separate into single "
            "strikes, slow down and rebuild."
        ),
        "key_points": [
            "Combinations are conversations, not scripts: learn the grammar - opener, exploitation, exit - and improvise the sentences.",
            "Every chain is built on the opponent's reactions: the opener demands a response, the next strikes exploit it.",
            "The two-beat chain comes first - jab-cross as one breath - and the third beat only after the two are a single word.",
            "Cross-range chains link the ranges: the punch plants the weight, the kick takes the planted leg.",
            "Every combination ends in stance - a chain that leaves you unbalanced is a sentence without a period.",
        ],
        "requirements": [
            "Clean single techniques first: the chain is only as honest as its links.",
            "A bag for the hundred-rep chain drilling, then pads, then a cooperative partner.",
            "A partner who feeds varied guards and reactions for the improvisation stage.",
            "Light-contact sparring to test chains against a live, thinking guard.",
            "The breath discipline: multi-beat chains are thrown on controlled exhales, never gasped.",
        ],
        "standards": [
            "Chain mechanics: each beat full-sized and clean, no pauses between beats, stance recovered at the end.",
            "Architecture standard: every drilled chain must show opener, exploitation, and exit - random flurries are not combinations.",
            "Safety: chain sparring is light contact with headgear; the sweep finish is drilled separately on mats.",
        ],
        "citations": [CIT_ABA, CIT_MAUNGGYI, CIT_HAY],
        "sig_lens": (
            "The Signature read: the combination is the covenant in "
            "conversation. Where public bando files striking chains, the "
            "Signature method files a promise to listen - the opener "
            "asks, the opponent answers, and the oath is completed in "
            "their own words."
        ),
    },
    {
        "key": "counters",
        "name": "Counter-Attack Timing",
        "group": "Advanced Principles",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The counter-attack is bando's highest-percentage offense: "
            "instead of creating an opening, you use the one the "
            "opponent creates by attacking. Every attack has a "
            "vulnerable moment - the instant of commitment, when the "
            "attacker's weight and attention are fully invested in their "
            "own strike and their guard is at its thinnest. The "
            "counter-fighter's art is living in that instant: seeing the "
            "attack early, meeting it with a parry or sway that costs "
            "almost nothing, and answering into the opening before it "
            "closes. Students train the three counter timings - the "
            "simultaneous counter (answering as the attack comes), the "
            "parry-counter (deflect then answer in one beat), and the "
            "draw-counter (inviting the attack to create the opening) - "
            "and learn that timing beats speed: the slower fighter with "
            "better timing lands first. The deeper lesson is psychological: "
            "the counter-fighter must be comfortable being attacked, "
            "must not flinch, and must trust the parry - courage as a "
            "technical skill, drilled until calm under fire is a habit."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: drill the recognition - "
            "have a partner throw slow straight punches while you only "
            "watch, calling out 'now' at the commitment instant; you "
            "cannot counter what you cannot see. Two: learn the "
            "parry-counter - parry their jab with your lead hand and let "
            "your rear straight fire in the same beat; drill it slowly "
            "until the two actions are one motion. Three: learn the "
            "simultaneous counter - as their straight comes, sway inches "
            "offline and throw your own straight over the top of theirs; "
            "the two punches cross and yours lands because your head is "
            "not where they aimed. Four: learn the draw - drop your lead "
            "hand an inch to invite their jab, then parry-counter the "
            "jab you invited; the draw manufactures the opening on "
            "purpose. Five: drill all three at increasing speed with a "
            "cooperative partner, touch contact only. Six: practice the "
            "calm - have the partner increase pressure while you focus "
            "on steady breathing and soft eyes; flinching is the "
            "counter-fighter's tax and it is paid in missed timings. "
            "Seven: spar counter-only rounds - you may only score with "
            "counters, which forces the timing to develop. Eight: never "
            "chase a missed counter - if the timing fails, reset to "
            "guard; the counter-fighter's discipline is in the reset."
        ),
        "key_points": [
            "The counter uses the opening the opponent creates: every attack has a commitment instant when the guard is thinnest.",
            "Three timings - simultaneous, parry-counter, and draw - cover every way an opening can be taken or made.",
            "Timing beats speed: the slower fighter with better timing lands first, because the counter starts from the opponent's move.",
            "The parry-counter is one motion, not two: deflect and answer in the same beat.",
            "Calm under fire is a technical skill - the counter-fighter trains not flinching until it is a habit.",
        ],
        "requirements": [
            "A partner willing to attack honestly at controlled speeds - counters are learned against real commitment.",
            "The parry and sway solid first: the counter is built on defenses that already work.",
            "Touch-contact rules for all counter drilling; headgear as speed rises.",
            "Counter-only sparring rounds to force the timing to develop under pressure.",
            "An instructor to watch the flinch - it hides in the shoulders and must be coached out.",
        ],
        "standards": [
            "Counter mechanics: recognition of the commitment instant, minimal defense, immediate answer into the opening, reset to guard.",
            "Timing standard: the counter must land in the attack's own beat - late answers are just trading.",
            "Safety: touch contact in counter drills; no chasing missed counters into wild exchanges.",
        ],
        "citations": [CIT_ABA, CIT_MAUNGGYI, CIT_HAY],
        "sig_lens": (
            "The Signature read: the counter is the covenant kept in the "
            "opponent's own beat. Where public bando files counter-attack "
            "timing, the Signature method files a promise to be calm "
            "where the attack is committed - and to answer before the "
            "echo fades."
        ),
    },
    {
        "key": "multiple-attackers",
        "name": "Positioning Against Multiple Attackers",
        "group": "Advanced Principles",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "No technique defeats numbers - only positioning does. "
            "Bando's advanced principle for multiple attackers is "
            "geometry, not heroics: keep moving so that only one "
            "attacker can reach you at a time, stacking them in a line "
            "or a narrow cone while you deal with the nearest. The "
            "fighter who stands still between two attackers is finished "
            "by arithmetic; the fighter who circles, using one attacker "
            "as a shield against the other, turns numbers into a queue. "
            "Students drill the stacking footwork - circling always "
            "toward the outside of the group, never into the middle - "
            "and learn the three rules: never grapple one while another "
            "is free, never turn your back on the unengaged, and never "
            "stop moving. The training is scenario drilling with "
            "cooperative partners at walking pace first, building the "
            "habit of constant repositioning, and it carries bando's "
            "honest disclaimer: the best defense against multiple "
            "attackers is not being there, and positioning is for the "
            "moment when leaving was not an option."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: when facing two partners "
            "in a drill, move immediately - circle toward the outside, "
            "so one partner ends up between you and the other; this is "
            "stacking, and it is the whole art. Two: engage only the "
            "nearest - quick touch strikes or a push to keep them "
            "occupied - while your feet keep repositioning to maintain "
            "the stack. Three: never grapple - clinching one attacker "
            "while the other is free is how the drill is failed; keep "
            "everything at arm's length and keep moving. Four: use the "
            "near attacker as a shield - position so their body blocks "
            "the far attacker's path to you. Five: drill the reset - "
            "when the stack breaks and both can reach you, disengage "
            "with a push and sprint-circle to rebuild the line; the "
            "reset is a technique, not a retreat. Six: practice at "
            "walking pace with two cooperative partners, then three, "
            "speed rising only as the stacking habit holds. Seven: keep "
            "your head on a swivel - the drill is failed the moment you "
            "fixate on one attacker and lose the other. Eight: end every "
            "drill by reaching the marked exit - the scenario's goal is "
            "always the door, because the honest objective is leaving."
        ),
        "key_points": [
            "No technique defeats numbers - only positioning does: stack the attackers so only one can reach you at a time.",
            "Circle toward the outside, never into the middle; the stationary fighter between two attackers is finished by arithmetic.",
            "Never grapple one while another is free - the clinch is a gift to the unengaged attacker.",
            "Use the near attacker as a shield, blocking the far attacker's path with their own body.",
            "The scenario's goal is always the exit: positioning buys the moment when leaving was not an option - until it is.",
        ],
        "requirements": [
            "Two to three cooperative partners for scenario drilling, starting at walking pace.",
            "A large clear space with a marked exit - the drill needs room to circle and a goal to reach.",
            "Touch-contact rules: the drill trains positioning, not striking.",
            "An instructor running the scenario, controlling speed and calling resets.",
            "The honesty briefing before every session: leaving is the best defense, and this trains the worst case.",
        ],
        "standards": [
            "Positioning standard: the stack must be maintained - if two attackers can reach the student at once, the rep is failed.",
            "Movement standard: constant repositioning, head swiveling, never fixating on one attacker.",
            "Safety: walking pace until the habit holds; touch contact only; the exit is always the drill's objective.",
        ],
        "citations": [CIT_ABA, CIT_MAUNGGYI],
        "sig_lens": (
            "The Signature read: positioning is the covenant of geometry. "
            "Where public bando files multiple-attacker principles, the "
            "Signature method files a promise to never fight arithmetic "
            "with heroics - only with angles, movement, and the door."
        ),
    },
    {
        "key": "close-quarter",
        "name": "Close-Quarter Elbow and Knee Chains",
        "group": "Advanced Strikes",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "When the range collapses - in the clinch, against the ropes "
            "of a ring, in a crowded exchange - the long weapons go quiet "
            "and the short ones take over. The advanced close-quarter "
            "chain links elbows and knees into continuous combinations: "
            "horizontal elbow, opposite knee, upward elbow, driving knee, "
            "each strike's recoil feeding the next strike's chamber. This "
            "is bando's infighting engine, and it runs on three fuels - "
            "hip rotation that never stops turning, a guard that never "
            "fully opens, and conditioning that lets the fighter think "
            "while exhausted. Students build the chains on pads first, "
            "learning the rhythm - strike, recoil, strike - until four "
            "and six-beat chains flow without thought, then take them to "
            "the clinch with a cooperative partner at controlled contact. "
            "The close-quarter lesson is that range dictates weapons: "
            "the fighter who tries to punch in elbow range is unarmed, "
            "and the fighter who flows elbow-to-knee-to-elbow is never "
            "without an answer. Every chain ends with an exit - a push, "
            "a turn, a step out - because the clinch is a place to visit, "
            "not to live."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: on the pads, drill the "
            "two-beat - lead horizontal elbow, rear knee - as one breath, "
            "the knee's hip thrust starting as the elbow recoils. Two: "
            "add the third beat - upward elbow on the other side - then "
            "the fourth - driving knee; four beats, continuous hip "
            "rotation, the torso turning like a crankshaft that never "
            "stops. Three: keep one hand guarding through every beat - "
            "the chain is elbow, guard, knee, guard; the guard is part "
            "of the rhythm, not a pause in it. Four: breathe in the "
            "gaps - sharp exhales on the strikes, a quick sip of air on "
            "the transitions; the chain suffocates the fighter who holds "
            "their breath. Five: take the four-beat to the clinch with a "
            "cooperative partner at touch contact - elbow touches, knee "
            "touches, feeling the range where punches would smother. Six: "
            "drill the exit - after the last beat, frame with the "
            "forearm and step out to stance; the chain ends outside, not "
            "inside. Seven: build to six beats over weeks, adding angles "
            "- downward elbow, side knee - as the four-beat becomes "
            "automatic. Eight: spar the infighting lightly with headgear, "
            "scoring only with clean chained beats; single strikes do not "
            "count, which forces the chain to develop."
        ),
        "key_points": [
            "Range dictates weapons: in elbow range the puncher is unarmed, and the elbow-to-knee chain is never without an answer.",
            "The chain runs on continuous hip rotation - the torso turns like a crankshaft that never stops between beats.",
            "The guard is part of the rhythm, not a pause in it: elbow, guard, knee, guard.",
            "Breathe in the gaps - sharp exhales on strikes, quick air on transitions; held breath suffocates the chain.",
            "Every chain ends with an exit - frame and step out; the clinch is a place to visit, not to live.",
        ],
        "requirements": [
            "Pads held at true close range for the chain-building phase - the holder stands where punches smother.",
            "A cooperative clinch partner for the touch-contact stage, with headgear and mouthguards.",
            "The conditioning base: close-quarter chains are exhausting, and exhaustion without conditioning teaches panic.",
            "The four-beat automatic before any six-beat is attempted.",
            "An instructor supervising all clinch chain sparring.",
        ],
        "standards": [
            "Chain mechanics: continuous hip rotation, correct elbow and knee surfaces, guard maintained through every beat, framed exit.",
            "Flow standard: four beats without pauses or thought - hesitation between beats fails the rep.",
            "Safety: touch contact in clinch chain work; headgear and mouthguard mandatory; the exit drilled every rep.",
        ],
        "citations": [CIT_ABA, CIT_HAY, CIT_MAUNGGYI],
        "sig_lens": (
            "The Signature read: the close-quarter chain is the covenant "
            "that never stops turning. Where public bando files infighting "
            "combinations, the Signature method files a promise sworn on "
            "a crankshaft - strike, guard, strike, exit - kept at the "
            "range where long weapons go quiet."
        ),
    },
    {
        "key": "sweep-throw",
        "name": "The Sweep-to-Throw Chain",
        "group": "Advanced Grappling",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The advanced grappler does not choose between the sweep and "
            "the throw - they chain them, so that defending one delivers "
            "the other. The sweep-to-throw chain is naban's compound "
            "takedown: the panther's leg sweep threatens the base, and "
            "when the opponent shifts weight to save the swept leg, the "
            "hip throw takes the shifted weight over the fulcrum. It is "
            "the grappling equivalent of the striking combination - "
            "opener, exploitation, finish - and it teaches the advanced "
            "principle that a defended technique is not a failed "
            "technique if it was the setup. Students drill the chain as "
            "a flow: enter the clinch, threaten the sweep, feel the "
            "weight shift, turn into the hip throw, guide the partner "
            "down, and both reset. The chain demands the sensitivity "
            "trained in all the earlier grappling - the throw cannot be "
            "forced on a schedule, it must be taken when the sweep "
            "creates it. Like every takedown in this school, it is "
            "drilled on mats, with a cooperative partner, under an "
            "instructor's eye, and the thrower owns the landing."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: from the clinch, threaten "
            "the sweep - swing the leg low at their ankle without full "
            "commitment; the threat is the technique's first half. Two: "
            "feel their weight shift away from the threatened leg - this "
            "is the moment the chain exists for; do not rush it, feel "
            "it. Three: as the weight commits to the other leg, turn "
            "into the hip throw entry - deep step, pivot, hips below "
            "hips - using their shifted momentum as your throwing force. "
            "Four: drive with the legs and guide with the arms, levering "
            "them over the hip in a clean arc. Five: guide the landing - "
            "hold the control through the fall, never releasing a person "
            "you are throwing. Six: the partner breakfalls and both "
            "reset, switching roles every few reps. Seven: drill the "
            "sensitivity slowly - partner shifts weight on purpose at "
            "first, so you learn the feeling; then they resist the sweep "
            "honestly and you take what the resistance gives. Eight: "
            "never force the throw when the weight does not shift - a "
            "chained throw taken at the wrong moment is just a muscled "
            "throw, and muscled throws fail the drill."
        ),
        "key_points": [
            "A defended technique is not a failed technique if it was the setup: the threatened sweep creates the weight shift the throw needs.",
            "The chain is opener, exploitation, finish - the sweep threatens the base, the shift feeds the hip throw.",
            "Sensitivity is the technique: the throw is taken when the sweep creates it, never forced on a schedule.",
            "The partner's shifted momentum becomes the throwing force - their defense powers your offense.",
            "The thrower owns the landing: guide through the fall, never release mid-throw, and switch roles often.",
        ],
        "requirements": [
            "The panther sweep and the hip throw both solid individually - the chain links mastered techniques, not shaky ones.",
            "A mat, a cooperative partner with an automatic breakfall, and an instructor present.",
            "The sensitivity drilled slowly first: exaggerated weight shifts before honest resistance.",
            "Role switching every few reps - both partners learn the chain from both sides.",
            "The discipline to abandon the throw when the shift never comes.",
        ],
        "standards": [
            "Chain mechanics: sweep threat, felt weight shift, hip-throw entry on the shift, leveraged arc, guided landing.",
            "Timing standard: the throw entry begins on the weight shift - early entries muscle, late entries miss.",
            "Safety: mats mandatory; thrower guides every landing; breakfall automatic before full chains.",
        ],
        "citations": [CIT_ABA, CIT_MTF, CIT_MAUNGGYI],
        "sig_lens": (
            "The Signature read: the sweep-to-throw chain is the covenant "
            "of the setup. Where public naban files a compound takedown, "
            "the Signature method files a promise that no defense will "
            "be wasted - the threatened sweep is kept as the throw's "
            "invitation."
        ),
    },
    {
        "key": "advanced-aka",
        "name": "The Advanced Aka: Form Becomes Fighting",
        "group": "Forms",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "At the top of the ladder, the aka stops being a performance "
            "and becomes a fight. The advanced aka is longer, faster, and "
            "built from the whole curriculum - animal system techniques, "
            "grappling entries, counters, and sweeps woven into one "
            "continuous sequence - and it is practiced with intent: every "
            "technique thrown at a real imaginary opponent, every "
            "transition a real repositioning, the whole form a solo "
            "sparring match. This is the stage the black belt test "
            "demands: proficiency in aka alongside weapons, sparring, and "
            "fitness, because the advanced form proves that the student's "
            "techniques are not a collection but a system. Students learn "
            "the advanced aka in the same chunked way as the first - "
            "three moves at a time - but now each chunk is analyzed: what "
            "principle does this sequence teach, what attack does it "
            "answer, what would you do if the imaginary opponent did "
            "something else. The form is also the student's archive: "
            "years from now, the aka will still contain every technique "
            "the body learned, available for review in a few minutes of "
            "solo practice. At this level the form is never finished - it "
            "is refined for life."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: learn the advanced "
            "sequence in three-move chunks, exactly as with the first "
            "aka - the method that built the foundation builds the roof. "
            "Two: analyze each chunk - name the principle it teaches, "
            "the attack it answers, and the technique it chains from; "
            "the advanced student can lecture the form, not just perform "
            "it. Three: practice with intent - visualize a real opponent "
            "for every technique, with distance, timing, and resistance; "
            "empty visualization makes an empty form. Four: vary the "
            "imaginary opponent - sometimes they rush, sometimes they "
            "retreat, sometimes they counter - and let the form's "
            "transitions answer each version. Five: drill the form's "
            "grappling entries with a partner separately, then fold the "
            "solo visualization back in. Six: perform at full speed with "
            "full power into the air, holding every stance and finishing "
            "every technique - the advanced aka is a workout as well as "
            "a study. Seven: perform it watched - for the instructor, "
            "for the camera, for the test panel; the form you can do "
            "under eyes is the form you own. Eight: begin refining - "
            "the advanced aka is practiced for life, and each year finds "
            "new depth in the same sequence."
        ),
        "key_points": [
            "The advanced aka is a solo sparring match: every technique thrown with intent at a real imaginary opponent.",
            "The advanced student can lecture the form - naming each chunk's principle, the attack it answers, and the chain it belongs to.",
            "Vary the imaginary opponent - rusher, retreater, counter-fighter - and let the transitions answer each version.",
            "The form is the student's archive: years later, every technique the body learned is still in it, reviewable in minutes.",
            "The advanced aka is never finished - it is refined for life, and each year finds new depth in the same sequence.",
        ],
        "requirements": [
            "The full curriculum beneath it: animal systems, grappling, counters, and sweeps must be real techniques, not rumors.",
            "The first aka solid - the advanced form builds on the method that built the foundation.",
            "A partner for the grappling-entry sections, drilled separately and folded back in.",
            "An instructor or test panel to perform for - the watched form is the owned form.",
            "The lifetime habit: the advanced aka is daily practice, not a test piece.",
        ],
        "standards": [
            "Advanced form standard: full speed, full power, intent in every technique, analyzable chunks, performable under observation.",
            "Knowledge standard: the student explains the form's principles, not just executes its motions.",
            "Safety: full-power air practice with joint awareness; partner sections drilled cooperatively.",
        ],
        "citations": [CIT_WIKI_BANDO, CIT_ABA, CIT_MAUNGGYI],
        "sig_lens": (
            "The Signature read: the advanced aka is the covenant recited "
            "in full. Where public bando files a black-belt form, the "
            "Signature method files the whole oath at once - every "
            "technique the body ever swore, spoken in one continuous "
            "promise, refined for life."
        ),
    },
    {
        "key": "controlled-sparring",
        "name": "Controlled Sparring: Free Fighting",
        "group": "Sparring",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Sparring is where the ladder is tested: free fighting under "
            "controlled rules, the middle style of bando practice that "
            "the tradition compares to tournament karate - continuous, "
            "technical, and stopped by the referee's judgment rather "
            "than by damage. Everything learned - stance, strikes, "
            "parries, kicks, animal strategies, counters, grappling "
            "entries - is now used against a thinking, resisting partner "
            "who is trying to do the same to you. The rules make it a "
            "laboratory instead of a brawl: controlled contact, "
            "protective equipment, banned targets, an instructor "
            "refereeing, and the tap or the call stopping everything "
            "instantly. Students spar in rounds with rest between, "
            "starting with single-technique sparring - only jabs score, "
            "then only counters - and graduating to free sparring where "
            "the whole curriculum is legal under the safety rules. The "
            "sparring lesson is humility delivered personally: every "
            "fighter discovers which techniques actually work under "
            "pressure and which only worked on cooperative partners, and "
            "that discovery is the most valuable technique of all."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: gear up - headgear, "
            "mouthguard, gloves, shin guards, groin protection; no gear, "
            "no sparring, no exceptions. Two: agree the rules with your "
            "partner and the referee - what scores, what contact level, "
            "what is banned, how rounds and stoppages work; the "
            "agreement is part of the technique. Three: start with "
            "single-technique rounds - three minutes where only the jab "
            "scores, then only the low kick, then only counters - so "
            "each tool is tested alone. Four: graduate to free sparring "
            "rounds - three minutes on, one minute rest - using the "
            "whole curriculum at controlled contact. Five: work your "
            "game plan each round - this round you are the cobra, all "
            "speed; next round you are the counter-fighter; the plan "
            "gives the chaos a shape. Six: breathe and stay relaxed - "
            "the sparring beginner holds their breath and gases in a "
            "minute; the veteran breathes and lasts the round. Seven: "
            "review after every session - what landed, what failed, what "
            "surprised you; the journal turns experience into curriculum. "
            "Eight: respect every stoppage - the tap, the referee's "
            "call, the partner's wince; the laboratory only works if "
            "everyone trusts the stops."
        ),
        "key_points": [
            "Sparring is the laboratory: the whole curriculum tested against a thinking, resisting partner under controlled rules.",
            "Single-technique rounds come first - each tool tested alone before the whole curriculum is legal.",
            "The rules are part of the technique: agreed scoring, contact level, banned targets, and trusted stoppages.",
            "Fight each round with a game plan - be the cobra, be the counter-fighter - so the chaos has a shape.",
            "The review after is the real training: what landed, what failed, and what only worked on cooperative partners.",
        ],
        "requirements": [
            "Full protective gear: headgear, mouthguard, gloves, shin guards, groin protection - no gear, no sparring.",
            "An instructor refereeing every round, with absolute stoppage authority.",
            "Agreed rules before every session: scoring, contact, bans, round structure.",
            "The foundations and compounded techniques genuinely learned - sparring tests the curriculum, it does not teach it.",
            "A training journal for the post-session review.",
        ],
        "standards": [
            "Sparring standard: controlled contact, continuous technical fighting, referee-controlled rounds with rest.",
            "Progression standard: single-technique rounds before free sparring; contact rises only with control.",
            "Safety: full gear always; banned targets respected; any stoppage - tap, call, or wince - ends the action instantly.",
        ],
        "citations": [CIT_ABA, CIT_WIKI_BANDO, CIT_MAUNGGYI],
        "sig_lens": (
            "The Signature read: sparring is the covenant under fire. "
            "Where public bando files free fighting, the Signature method "
            "files a promise to bring every oath ever sworn - stance, "
            "strike, animal, counter - and let the laboratory judge them "
            "honestly."
        ),
    },
    {
        "key": "nine-by-nine",
        "name": "The 9x9 Matrix: Building Your Own Technique",
        "group": "Mastery Principles",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The final record of the ladder is not a technique but the "
            "machine that makes techniques: the 9x9 matrix of techniques "
            "and principles that the ABA calls the basis of the bando "
            "system. Nine techniques cross nine principles - eighty-one "
            "cells - and each cell is a lesson: this technique taught "
            "through this principle, this principle expressed through "
            "this technique. The matrix exists because of bando's core "
            "insight, stated in the tradition's own teaching: one "
            "technique may only be useful in a certain situation, but the "
            "principle the technique is built on will be useful in many "
            "situations. The advanced student is encouraged to grasp the "
            "underlying principles precisely so they can build their own "
            "techniques - to take the hip rotation of the straight punch, "
            "the timing of the panther sweep, the commitment of the "
            "tiger, and assemble something new that the matrix would "
            "recognize as legitimate. This record teaches the method: "
            "extract the principle, test it across techniques, combine "
            "principles deliberately, pressure-test the result in "
            "controlled sparring, and file it back into the student's "
            "personal matrix. The ladder ends where it began - with the "
            "student as the author."
        ),
        "how_it_works": (
            "HOW TO DO IT - step by step. One: pick a technique you own "
            "- the straight punch is ideal - and extract its principle: "
            "hip rotation drives the strike. Two: test the principle "
            "across techniques - apply hip rotation to the backfist, the "
            "elbow, the low kick; the principle should improve all of "
            "them, which proves it is a principle and not a habit. Three: "
            "pick a second principle - the panther's timing, say - and "
            "combine the two deliberately: a hip-driven strike timed to "
            "the opponent's weight shift. Four: build the new technique "
            "slowly - solo first, then on pads, then with a cooperative "
            "partner - checking at each stage that both principles are "
            "really present. Five: pressure-test it in controlled "
            "sparring: does it work against resistance, or only in the "
            "drill; the laboratory is the judge. Six: name it and file "
            "it - write the technique, its parent principles, and its "
            "test results in your journal; your personal matrix now has "
            "eighty-two cells. Seven: teach it to a junior student - the "
            "technique you cannot teach is a technique you do not own. "
            "Eight: repeat for life - the matrix is never complete, and "
            "the master is simply the student who never stopped adding "
            "cells."
        ),
        "key_points": [
            "The 9x9 matrix crosses nine techniques with nine principles: eighty-one cells, each a lesson in what a technique is built on.",
            "One technique fits one situation, but its principle fits many - grasp the principle and you can build the technique.",
            "Extract, test across techniques, combine deliberately, pressure-test in sparring, file the result: that is the method.",
            "A principle proves itself by improving every technique it touches; a habit only flatters the one it came from.",
            "The technique you cannot teach is a technique you do not own - teaching completes the cell.",
        ],
        "requirements": [
            "A technique genuinely owned - the matrix builds from mastery, not from wishes.",
            "Pads, a cooperative partner, and controlled sparring for the build-and-test cycle.",
            "A journal for the personal matrix: every new cell filed with its principles and test results.",
            "A junior student to teach each new technique to - teaching is the ownership test.",
            "An instructor to validate that new techniques stay within the school's safety standards.",
        ],
        "standards": [
            "Matrix standard: every new technique must name its parent principles and pass the cross-technique test.",
            "Testing standard: the laboratory - controlled sparring - judges every new cell; drill-only techniques are not filed.",
            "Safety: new techniques are pressure-tested under the same protective rules as the rest of the curriculum.",
        ],
        "citations": [CIT_ABA, CIT_WIKI_BANDO, CIT_MAUNGGYI],
        "sig_lens": (
            "The Signature read: the matrix is the covenant that writes "
            "itself. Where public bando files eighty-one cells of "
            "technique and principle, the Signature method files a "
            "promise that the student will become the author - extracting, "
            "combining, testing, and filing new oaths for life."
        ),
    },
])
