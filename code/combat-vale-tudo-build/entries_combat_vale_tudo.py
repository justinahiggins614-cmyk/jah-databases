#!/usr/bin/env python3
"""Entries for the Vale Tudo Combat databases (combat batch 3, 2026-10-17).

RAW SWEEP verified 2026-10-17: full manifest (2,442 databases) plus the
whole-system dedupe exact shards (data/dedupe/exact): zero 'vale-tudo' /
'vale tudo' slug or title collisions - the 68 titles (34 public + 34
Signature Edition) were checked one by one against the whole system with
zero refusals. Near-hits reviewed by name/purpose/record schema: the MMA
database (JAH-MMA-) teaches modern unified-rules mixed martial arts as
general technique; the Brazilian jiu-jitsu database (JAH-CBBJJ-) teaches
gi/no-gi grappling; the wrestling database teaches takedowns and control.
None of them teaches the Brazilian vale tudo lineage itself - the
anything-goes challenge-fighting roots, the Portuguese technique names,
the old-rules heritage, the challenge-match history - as its subject, so
BUILD NEW is the verdict under the paste rule.

This build creates two NEW databases, 34 ladder-ordered records each:

  combat-vale-tudo             - Vale Tudo Combat Database
                                 (public-harvest: real, fact-checked
                                 Brazilian vale tudo - the anything-goes
                                 challenge-fighting roots of modern MMA -
                                 every record a technique with HOW TO DO IT
                                 in step-by-step body mechanics, ladder-
                                 ordered from stance and breakfalls through
                                 strikes, clinch, takedowns, ground control
                                 and submissions to heritage, combinations,
                                 strategy, and the code of the art;
                                 civilian sport-training scope; standard
                                 references Snowden Total MMA 2008; Krauss
                                 Brawl 2004; Gentry No Holds Barred 2002;
                                 Gracie and Gracie Brazilian Jiu-Jitsu:
                                 Theory and Technique 2001; Penn Mixed
                                 Martial Arts: The Book of Knowledge 2007)
  combat-vale-tudo-signature  - Vale Tudo Combat Signature Database
                                 (his original Signature Combat Method:
                                 every technique a covenant of discipline,
                                 the fighter the armory of the Signature
                                 system, training the oath between student
                                 and craft, defense the honor guard, and
                                 fight craft the strategy of the Signature
                                 mind; src signature, titles suffixed
                                 " (Signature Edition)", never presented
                                 as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBVT- (public) and JAH-CBVTS- (signature), verified free
in the manifest id_prefix values and in every shard index of
jah-databases-data-1 (zero hits for JAH-CBVT anywhere).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_vale_tudo.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos before the merge.

Never the words "bat belt" anywhere. No website references. No Facebook.
Civilian martial-arts instruction only; nothing on neutralizing or
defeating military or defense-grade systems.
"""

SIG_TAIL = ("Signature original - his original Signature Combat Method: "
            "every technique a covenant of discipline, the fighter the "
            "armory of the Signature system, training the oath between "
            "student and craft, defense the honor guard, and fight craft "
            "the strategy of the Signature mind. Clearly labeled "
            "Signature-made, never presented as authentic public record.")

CIT_SNOWDEN = ("Snowden J. Total MMA: Inside Ultimate Fighting. ECW Press; "
               "2008.")
CIT_KRAUSS = ("Krauss E. Brawl: A Behind-the-Scenes Look at Mixed Martial "
              "Arts Competition. ECW Press; 2004.")
CIT_GENTRY = ("Gentry C. No Holds Barred: Ultimate Fighting and the Martial "
              "Arts Revolution. Milo Books; 2002.")
CIT_GRACIE = ("Gracie R, Gracie R. Brazilian Jiu-Jitsu: Theory and "
              "Technique. Invisible Cities Press; 2001.")
CIT_PENN = ("Penn BJ. Mixed Martial Arts: The Book of Knowledge. Victory "
            "Belt Publishing; 2007.")

ENTRIES = [
    {
        "key": "vt_what_is",
        "name": "What Is Vale Tudo: The Anything-Goes Roots of MMA",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Vale tudo is Portuguese for anything goes, and it is the name "
            "of the Brazilian no-holds-barred fighting tradition that "
            "became modern mixed martial arts. In the early twentieth "
            "century, Brazilian circus wrestlers and fighters took open "
            "challenge matches - any style against any style, almost no "
            "rules - and in the 1920s the Gracie family of Rio de Janeiro "
            "began issuing the famous Gracie Challenge, inviting fighters "
            "of every art to test themselves. Carlos Gracie and his "
            "brothers, above all Helio Gracie, fought boxers, wrestlers, "
            "judoka, and capoeiristas in bouts that proved a smaller "
            "fighter could win with leverage and ground fighting. Through "
            "the 1950s and 1960s vale tudo filled Brazilian stadiums; in "
            "the 1990s the International Vale Tudo Championship and the "
            "World Vale Tudo Championship carried the name worldwide, and "
            "the first Ultimate Fighting Championship in 1993 - co-founded "
            "by Rorion Gracie - was vale tudo exported to America. Every "
            "technique in this database comes from that lineage: striking, "
            "clinching, takedowns, and ground fighting taught as one "
            "complete civilian sport."
        ),
        "how_it_works": (
            "Studying vale tudo works by learning the lineage first and the "
            "techniques second, because the art only makes sense as a "
            "complete fighting system. Step one: learn the three ranges the "
            "old challenge fighters lived in - free striking range, the "
            "clinch, and the ground - and accept that a vale tudo fighter "
            "must be dangerous in all three. Step two: pick a qualified "
            "school or coach, because vale tudo techniques involve strikes "
            "and chokes that must be learned with a partner under "
            "supervision; never drill chokes or throws alone or at full "
            "force. Step three: build the base in ladder order - stance, "
            "footwork, breakfalls, basic punches, then clinch, takedown "
            "defense, guard, and escapes - before touching advanced "
            "submissions. Step four: train each technique in three speeds - "
            "slow and precise for mechanics, medium with a cooperating "
            "partner for timing, and live but controlled sparring for "
            "reality. Step five: condition the body gradually, because old "
            "vale tudo was attrition fighting and the modern sport still "
            "rewards the fighter who is strong in the third round. Keep a "
            "training log of sessions, techniques, and sparring rounds; the "
            "log is how the ladder becomes a curriculum instead of a pile "
            "of tricks."
        ),
        "key_points": [
            "Vale tudo means anything goes: the Brazilian challenge-fighting tradition of style-versus-style bouts with minimal rules, the direct ancestor of modern MMA.",
            "The Gracie Challenge of the 1920s onward proved leverage and ground fighting could defeat larger strikers, and the family carried that lesson into the first UFC in 1993.",
            "Vale tudo is a three-range system - striking, clinch, ground - and every record in this database belongs to one of those ranges.",
            "The old events ran with minimal rules while the modern sport uses the Unified Rules; this database teaches the civilian sport version with safety at every step.",
            "Learn in ladder order and in three speeds - slow for mechanics, medium for timing, live but controlled for reality - and keep a training log.",
        ],
        "requirements": [
            "A qualified coach or school: strikes, throws, and chokes must be learned with supervised partners, never from text alone.",
            "A safe training space: mats for grappling and breakfalls, open floor for footwork, heavy bag for striking.",
            "Basic protective gear: mouthguard, groin protection, and later headgear and shin guards for controlled sparring.",
            "A training partner willing to drill cooperatively before either of you goes live.",
            "Patience with the ladder: stance, footwork, and breakfalls come before submissions, with no skipping.",
        ],
        "standards": [
            "Technique names keep their Portuguese where the art named them - chute baixo, cotovelada, joelhada, mata-leao - with the English beside them.",
            "Historical claims follow the standard histories: Snowden 2008, Krauss 2004, Gentry 2002.",
            "Every technique is taught as civilian sport training: tap early on submissions, controlled contact in sparring, and qualified supervision for chokes and throws.",
        ],
        "citations": [CIT_SNOWDEN, CIT_KRAUSS, CIT_GENTRY],
        "sig_lens": (
            "The Signature read: vale tudo is the covenant of the complete "
            "fighter - no range refused, no excuse kept. Where the old "
            "challenge matches tested style against style, the Signature "
            "Combat Method tests the student against himself: stance the "
            "oath, footwork the march, and every technique a kept promise "
            "between student and craft."
        ),
    },
    {
        "key": "vt_stance",
        "name": "The Vale Tudo Open Stance",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The vale tudo stance is the fighter's home base: an open, "
            "mobile posture that must serve striking, takedown defense, "
            "and clinch entries all at once. Unlike a pure boxer's "
            "side-on stance, the vale tudo stance is more square - the "
            "lead foot forward, the rear foot back and slightly out, knees "
            "soft, weight balanced so the fighter can sprawl backward "
            "against a shot or drive forward into a takedown without "
            "re-setting the feet. The hands ride high with the chin tucked "
            "behind the lead shoulder, elbows in to protect the ribs, and "
            "the lead hand extended a little to measure distance. The "
            "stance is narrow enough to move and wide enough to wrestle: "
            "too bladed and the fighter cannot sprawl; too square and the "
            "lead leg is a free target for low kicks. Everything in this "
            "database launches from this stance, so it is drilled until "
            "it is unconscious."
        ),
        "how_it_works": (
            "Take the stance in six steps. Step one: stand with feet about "
            "shoulder-width apart, then step the left foot (for an "
            "orthodox fighter) forward about half a stride and the right "
            "foot back the same amount, so the feet are staggered heel to "
            "toe. Step two: turn the lead foot inward about 45 degrees and "
            "the rear foot outward about 45 degrees, giving a stable "
            "platform that still pivots. Step three: bend both knees until "
            "they sit over the toes and sink the hips about ten centimeters, "
            "keeping the back straight and the chest facing the opponent "
            "more squarely than a boxer would. Step four: split the weight "
            "evenly, 50-50, on the balls of the feet - weight on the heels "
            "kills movement and invites the takedown. Step five: raise both "
            "hands to cheek height, tuck the chin behind the lead shoulder, "
            "and pin the elbows to the ribs. Step six: bounce lightly in "
            "place for thirty seconds without the stance collapsing - if "
            "the knees straighten or the hands drop, reset and repeat. "
            "Drill: hold the stance for three one-minute rounds, checking "
            "in a mirror that the chin stays tucked and the weight stays "
            "forward on the feet."
        ),
        "key_points": [
            "The vale tudo stance is more square than a boxing stance because it must defend takedowns and launch them, not only punch.",
            "Feet staggered heel-to-toe, knees bent, weight 50-50 on the balls of the feet: mobility and wrestling base in one posture.",
            "Hands high, chin tucked behind the lead shoulder, elbows pinned to the ribs - the shell that every defense starts from.",
            "Too bladed and you cannot sprawl; too square and the lead leg eats low kicks - the stance is a deliberate compromise.",
            "Drill it until it is unconscious: three one-minute rounds in front of a mirror before any other technique.",
        ],
        "requirements": [
            "A mirror or a coach's eye to check the stance from the front and the side.",
            "Flat, grippy footwear or bare feet on mats - no sliding shoes.",
            "Thirty seconds of honest bouncing to test whether the stance holds under motion.",
            "The chin tucked and the hands at cheek height on every rep, no exceptions.",
            "Three one-minute stance rounds as the warm-up of every session until the posture is automatic.",
        ],
        "standards": [
            "Stance width scales with the fighter: roughly 55 percent of standing height from lead toe to rear toe.",
            "Weight distribution is checked on the balls of the feet - heels on the floor during motion is a fault to correct.",
            "The stance is re-checked at the start of every technique in this database, since every technique launches from it.",
        ],
        "citations": [CIT_PENN, CIT_GRACIE],
        "sig_lens": (
            "The Signature read: the stance is the oath the fighter swears "
            "with his feet - I will not be moved cheaply, and I will move "
            "when I choose. The Signature fighter treats the stance as the "
            "armory door: everything the system owns marches out of it, "
            "and nothing enters without permission."
        ),
    },
    {
        "key": "vt_breakfall",
        "name": "Vale Tudo Breakfalls: Falling Without Injury",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Breakfalls - ukemi in the Japanese arts the Brazilians "
            "absorbed - are the art of hitting the ground without getting "
            "hurt, and in vale tudo they are survival equipment. Takedowns, "
            "trips, and throws put fighters on the mat dozens of times per "
            "session, and the fighter who cannot fall safely will be "
            "injured long before he learns to fight. The principle is "
            "simple physics: spread the impact across the largest possible "
            "surface, never let the head strike, and exhale on contact so "
            "the torso does not take the blow as a rigid drum. There are "
            "four falls - back, side, front, and the forward roll - and "
            "each ends with the chin tucked, the arms slapping the mat to "
            "bleed off force, and the body relaxed rather than braced. Old "
            "vale tudo fighters learned this the hard way on hard "
            "surfaces; the modern student learns it on mats, which is why "
            "it comes third in the ladder, before any throwing begins."
        ),
        "how_it_works": (
            "Learn the back fall first, in five steps. Step one: squat low "
            "with arms crossed over the chest and chin tucked hard to the "
            "chest - the chin tuck is non-negotiable, because the head "
            "must never whip into the mat. Step two: roll backward onto "
            "the upper back, rounding the spine like a wheel, and slap "
            "both arms down onto the mat at 45 degrees from the body just "
            "before the back lands - the slap spreads the force and the "
            "timing matters more than the strength. Step three: exhale "
            "sharply through the mouth on impact, keeping the belly firm "
            "but not rigid. Step four: let the legs follow naturally, "
            "never posting a straight arm behind you - a posted arm breaks "
            "at the wrist or elbow. Step five: stand up and repeat ten "
            "times, then progress to falling from standing, then to being "
            "gently pushed. The side fall is the same mechanics rotated 90 "
            "degrees, landing on the side of the thigh, hip, and lat with "
            "one arm slapping; the front fall lands on the forearms and "
            "the tops of the feet with the head turned to one side; the "
            "forward roll tucks the chin and rolls diagonally across the "
            "back from one shoulder to the opposite hip. Drill all four "
            "for five minutes at the start of every grappling session."
        ),
        "key_points": [
            "Breakfalls are survival equipment: takedowns put you on the mat dozens of times per session, and safe falling is what lets you train tomorrow.",
            "The physics is spreading force: slap the mat with the arms, land on broad surfaces, exhale on contact, and never let the head strike.",
            "Four falls cover everything - back, side, front, and the forward roll - each ending with the chin tucked and the body relaxed.",
            "Never post a straight arm to catch yourself; the posted arm is the most common breakfall injury in the sport.",
            "Drill all four falls for five minutes at the start of every grappling session until falling safely is reflex.",
        ],
        "requirements": [
            "A matted surface - never learn breakfalls on concrete, wood, or thin carpet.",
            "A coach or experienced partner to check the chin tuck and the slap timing on the first sessions.",
            "Ten clean back falls from a squat before attempting falls from standing height.",
            "Relaxed shoulders on impact: bracing rigidly concentrates the force instead of spreading it.",
            "The sharp exhale on every landing, drilled until it happens without thought.",
        ],
        "standards": [
            "The chin stays tucked to the chest on every fall - head contact with the mat is an immediate stop-and-correct fault.",
            "Arms slap the mat at roughly 45 degrees from the torso, palms down, just before the body lands.",
            "Progression is fixed: squat height, then standing height, then pushed falls, then falls from throws - never skipped.",
        ],
        "citations": [CIT_GRACIE, CIT_PENN],
        "sig_lens": (
            "The Signature read: the breakfall is the covenant of the "
            "ground - the fighter swears he will meet the mat as an ally, "
            "not an enemy. The Signature student learns to fall before he "
            "learns to throw, because the armory keeps no weapon it cannot "
            "survive."
        ),
    },
    {
        "key": "vt_footwork",
        "name": "Vale Tudo Footwork: Pressure, Angles, and Retreat",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Footwork is how the vale tudo fighter controls the only "
            "territory that matters: the space between two bodies. The "
            "old challenge fighters won as much with their feet as with "
            "their hands, cutting off the ring or the mat, stepping to "
            "angles where the opponent's weapons cannot reach, and "
            "retreating without crossing their feet into a takedown. Vale "
            "tudo footwork has three jobs: maintain the stance while "
            "moving, control distance, and set the angle for the next "
            "technique. The rules are few but absolute - never cross the "
            "feet, never hop with both feet off the ground, keep the "
            "weight balanced so a level change or sprawl is always one "
            "step away. Pressure footwork walks the opponent down; angular "
            "footwork steps offline to the lead side; retreat footwork "
            "gives ground in good order instead of running."
        ),
        "how_it_works": (
            "Drill footwork in four patterns. Pattern one, the advance: "
            "from the stance, step the lead foot forward half a step and "
            "drag the rear foot the same distance, keeping the stance "
            "width identical - the feet move like rails, never crossing. "
            "Pattern two, the retreat: rear foot steps back first, lead "
            "foot follows, same rail discipline. Pattern three, the "
            "lateral step: lead foot steps sideways, rear foot follows, "
            "used to circle away from the opponent's power hand. Pattern "
            "four, the angle step: as the opponent advances, step the lead "
            "foot 45 degrees to the outside and pivot the rear foot, so "
            "you face his flank while his punch falls past your shoulder - "
            "this is the angle that sets up the low kick and the double "
            "leg later in the ladder. Do each pattern the length of the "
            "mat and back, ten lengths per session, keeping the hands up "
            "and the knees bent the whole way. The test: a partner pushes "
            "lightly at your shoulders while you move - if you stumble or "
            "cross your feet, slow down and rebuild the pattern. Advanced "
            "drill: the partner calls advance, retreat, left, right, or "
            "angle at random, and you move instantly without breaking "
            "stance."
        ),
        "key_points": [
            "Footwork controls distance and angle: the fighter who controls the space controls which techniques are possible.",
            "Feet move like rails - step and drag, never cross, never hop with both feet airborne - so the stance survives the motion.",
            "Four patterns cover everything: advance, retreat, lateral step, and the 45-degree angle step that sets up attacks.",
            "The angle step to the outside is the money move of vale tudo footwork: it dodges the power hand and opens the low kick and the shot.",
            "Pressure walks the opponent down, retreat gives ground in good order; both keep the fighter balanced and ready to sprawl or shoot.",
        ],
        "requirements": [
            "Open floor or mat space at least six meters long for full-length footwork patterns.",
            "The stance from the previous record, held without collapse through every step.",
            "Hands up and chin tucked during all movement - footwork drilled with dropped hands builds a dropped-hands habit.",
            "A partner for the push test and the random-call drill once the solo patterns are clean.",
            "Ten lengths per pattern per session until the feet move without conscious thought.",
        ],
        "standards": [
            "Feet never cross and never leave the ground together during basic patterns - crossing is an immediate reset.",
            "Stance width stays constant through the step-and-drag; narrowing or widening the base is a fault.",
            "Movement stays on the balls of the feet with the knees bent; flat-footed shuffling is corrected on the spot.",
        ],
        "citations": [CIT_PENN, CIT_KRAUSS],
        "sig_lens": (
            "The Signature read: footwork is the march of the Signature "
            "system - every step a deliberate claim on the ground between "
            "two fighters. The Signature fighter does not chase and does "
            "not flee; he arrives at the angle he chose, on feet he trusts."
        ),
    },
    {
        "key": "vt_jab",
        "name": "The Vale Tudo Jab",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The jab is the lead-hand straight punch, and in vale tudo it "
            "is the most thrown strike in the sport: a fast, economical "
            "probe that measures distance, disrupts the opponent's rhythm, "
            "sets up every combination, and keeps a wrestler honest about "
            "shooting in. The old Brazilian fighters used the jab the way "
            "a fencer uses the point - constant, annoying, and suddenly "
            "doubled or tripled when the opening appears. Mechanically the "
            "jab is a snap, not a push: the lead fist travels straight "
            "from the chin to the target with the elbow tucked, the "
            "shoulder rolling forward to add reach, the rear hand glued to "
            "the chin, and the fist rotating to land with the knuckles "
            "horizontal. It returns along the same line twice as fast as "
            "it left, because a jab that lingers gets grabbed, parried, "
            "or countered."
        ),
        "how_it_works": (
            "Throw the jab in five steps. Step one: from the stance, pick "
            "a target - the heavy bag at chin height, or a partner's open "
            "palm. Step two: extend the lead arm straight out, rotating "
            "the fist a quarter turn so the palm faces down at impact, "
            "while the lead shoulder rolls forward to squeeze out the last "
            "centimeters of reach. Step three: step the lead foot forward "
            "a few centimeters as the punch extends, letting the body "
            "weight fall into the strike - the power comes from the step "
            "and the shoulder, never from leaning. Step four: keep the "
            "rear hand on the chin and the rear elbow on the ribs through "
            "the entire punch; the chin tucks behind the lead shoulder as "
            "it rolls. Step five: snap the fist back to the chin along the "
            "same line, faster than it went out. Drill: three rounds of "
            "three minutes on the bag, throwing only jabs - single, "
            "double, and triple - counting clean snaps and resetting the "
            "stance between every exchange. Common faults: dropping the "
            "rear hand, leaning the head forward past the lead knee, and "
            "pushing the punch instead of snapping it."
        ),
        "key_points": [
            "The jab is the most thrown strike in vale tudo: it measures distance, breaks rhythm, sets up combinations, and deters takedowns.",
            "It is a snap, not a push - straight out from the chin, fist rotating palm-down, shoulder rolling for reach, and back twice as fast.",
            "Power comes from the small forward step and the shoulder roll, never from leaning the head past the lead knee.",
            "The rear hand stays glued to the chin for the whole punch; the jab must never cost you your defense.",
            "Drill it alone first - three three-minute rounds of single, double, and triple jabs on the bag - before pairing it with anything.",
        ],
        "requirements": [
            "A heavy bag or a partner holding focus mitts at chin height.",
            "The stance and footwork records solid, since the jab steps with the lead foot.",
            "Hand wraps and gloves for bag work to protect the knuckles and wrist.",
            "The rear hand on the chin for every rep - a coach should be able to tap it and find it home.",
            "Snap and return: the fist must travel back along its line faster than it extended.",
        ],
        "standards": [
            "The punch travels in a straight line from chin to target and back; looping or dropping the elbow is a fault.",
            "The head stays behind the lead shoulder, never leaning past the lead knee.",
            "Bag rounds are counted in clean snaps, not arm punches - quality reps build the weapon, sloppy reps build bad habits.",
        ],
        "citations": [CIT_PENN, CIT_KRAUSS],
        "sig_lens": (
            "The Signature read: the jab is the Signature scout - first "
            "through the door, last to linger. It swears the covenant of "
            "the lead hand: measure truly, strike cleanly, return home, "
            "and never leave the chin uncovered."
        ),
    },
    {
        "key": "vt_cross",
        "name": "The Vale Tudo Cross",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The cross is the rear-hand straight punch, the power punch of "
            "the vale tudo fundamentals, thrown across the body behind the "
            "jab. Where the jab probes, the cross commits: the rear "
            "shoulder, hip, and foot rotate together to drive the fist "
            "through the target, and the old Brazilian strikers built "
            "entire challenge-match victories on the jab-cross, one-two "
            "that split the guard and ended the argument. The cross is "
            "also the punch most likely to leave a beginner exposed, "
            "because its rotation opens the body - which is why the "
            "record insists on the chin tuck, the returning lead hand, "
            "and the discipline to throw it only off a set jab or a clean "
            "angle. Thrown correctly it is the hardest straight punch in "
            "the arsenal; thrown carelessly it is an invitation to be "
            "taken down."
        ),
        "how_it_works": (
            "Throw the cross in six steps. Step one: from the stance, throw "
            "a light jab to set the range - the cross is almost never "
            "thrown naked. Step two: rotate the rear hip and shoulder "
            "forward together, pivoting on the ball of the rear foot so "
            "the heel turns outward; the power starts at the floor, not "
            "the shoulder. Step three: extend the rear arm straight along "
            "the line the jab opened, fist rotating palm-down, aiming "
            "through the target rather than at it. Step four: as the punch "
            "lands, snap the lead hand back to the chin - it left to jab "
            "and it must be home before the cross lands. Step five: tuck "
            "the chin behind the lead shoulder throughout; the head does "
            "not drift over the front foot. Step six: pull the rear hand "
            "straight back to guard and reset the hips - never drop the "
            "hand in a loop, which is the classic beginner tell. Drill: "
            "on the bag, throw jab-cross in threes - one light, one "
            "medium, one committed - for three three-minute rounds, "
            "checking after each round that the stance survived the "
            "rotation."
        ),
        "key_points": [
            "The cross is the power punch of the fundamentals: rear hip, shoulder, and foot rotating as one to drive the fist through the target.",
            "It is thrown behind the jab, never naked - the jab sets the range and the cross spends the power.",
            "The lead hand must be home on the chin before the cross lands; the cross must never cost the fighter his guard.",
            "Rotation opens the body, so discipline matters: chin tucked, head off the center line, hand straight back to guard.",
            "Aim through the target, pivot on the ball of the rear foot, and reset the stance after every committed cross.",
        ],
        "requirements": [
            "A reliable jab first - the cross is a second punch, not a first idea.",
            "A heavy bag that can take committed power shots without swinging wildly.",
            "Hand wraps, gloves, and a checked stance before adding power.",
            "The rear-foot pivot drilled slowly before speed is added; power without the pivot is arm punching.",
            "A coach watching the first power rounds for the dropped lead hand and the looping return.",
        ],
        "standards": [
            "The rear heel pivots outward and the hip and shoulder rotate as one unit - no arm-only crosses.",
            "The chin stays tucked behind the lead shoulder and the head stays off the center line through the punch.",
            "The rear hand returns straight to guard along its line; looping the return is a fault.",
        ],
        "citations": [CIT_PENN, CIT_GENTRY],
        "sig_lens": (
            "The Signature read: the cross is the Signature hammer - the "
            "covenant of committed power. It swears to spend itself "
            "fully and return home safely: rotation as the oath, the "
            "guard as the honor kept."
        ),
    },
    {
        "key": "vt_hook",
        "name": "The Vale Tudo Lead Hook",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The lead hook is the curved punch of the fundamentals, thrown "
            "with the lead hand on an arc to attack around the opponent's "
            "guard. In vale tudo it earns its place because the old "
            "challenge fights so often collapsed into phone-booth range, "
            "where straight punches get smothered and the hook still "
            "lands: around the guard to the temple, or dug under the elbow "
            "to the ribs. The hook's power comes from violent hip and torso "
            "rotation with a bent arm held rigid at roughly ninety degrees "
            "- the arm is the hammer head, the hips are the handle. It is "
            "a short-range weapon that demands the fighter step into the "
            "pocket, which is why it is taught after the straight punches: "
            "the beginner must first learn distance before learning to "
            "abandon it."
        ),
        "how_it_works": (
            "Throw the lead hook in six steps. Step one: from the stance, "
            "take a small step with the lead foot to close to hook range - "
            "about one forearm from the target. Step two: raise the lead "
            "elbow to shoulder height with the arm bent at roughly ninety "
            "degrees and the fist vertical or palm-down; the elbow, not "
            "the fist, leads the motion. Step three: pivot hard on the "
            "lead foot and rotate the hips and torso, whipping the bent "
            "arm across in a tight arc - the power is the rotation, and "
            "the arm stays locked in its bend like a rigid hook. Step four: "
            "land with the knuckles on the side of the target, wrist "
            "straight, never slapping with an open or bent wrist. Step "
            "five: keep the rear hand glued to the chin and the chin "
            "tucked, because the hook's rotation briefly squares the body. "
            "Step six: return the lead hand straight back to guard, not in "
            "a loop. Drill: on the bag, throw the jab-cross-hook as a "
            "three-punch unit for three rounds, then hooks to the body - "
            "dropping the level by bending the knees, never the waist - "
            "aiming under the bag's midline."
        ),
        "key_points": [
            "The hook attacks around the guard on an arc: the arm bent near ninety degrees, the elbow leading, the hips supplying the violence.",
            "It is a pocket-range weapon for the phone-booth distances where straight punches get smothered.",
            "Land with the knuckles and a straight wrist - a slapping hook injures the striker's own hand.",
            "The rear hand stays home and the chin stays tucked, because the hook's rotation briefly squares the body.",
            "Change levels with the knees for body hooks, never by folding at the waist into an uppercut.",
        ],
        "requirements": [
            "Solid jab and cross first - the hook is usually the third punch of the combination, not the first.",
            "A heavy bag at close range, or a partner holding a body protector for body hooks.",
            "Wraps and gloves: the hook loads the wrist sideways, so support matters more than for straight punches.",
            "The ninety-degree arm bend held rigid through the arc - a straightening arm turns the hook into a slap.",
            "Body hooks drilled with knee bend, not waist fold, to keep the head out of counter range.",
        ],
        "standards": [
            "The elbow rides at shoulder height for head hooks and the arm holds its bend through the entire arc.",
            "The lead foot pivots with the rotation; a planted lead foot bleeds the power and strains the knee.",
            "Head hooks and body hooks are drilled as separate tools with separate level changes.",
        ],
        "citations": [CIT_PENN, CIT_KRAUSS],
        "sig_lens": (
            "The Signature read: the hook is the Signature scythe - the "
            "covenant of the close quarter. It swears that when distance "
            "collapses, the fighter does not panic but shortens his "
            "weapons and swings the arc he rehearsed a thousand times."
        ),
    },
    {
        "key": "vt_lowkick",
        "name": "The Low Kick: Chute Baixo",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The low kick - chute baixo in Portuguese - is the signature "
            "strike of the Brazilian game: a shin-driven kick to the "
            "opponent's thigh that destroys mobility, punishes stance, and "
            "set up half the takedowns in vale tudo history. The old "
            "Brazilian fighters learned it from the Thai boxers and made "
            "it their own, chopping the lead leg until the opponent could "
            "neither advance nor retreat. It lands with the shin, never "
            "the foot - the shin is a baseball bat and the foot is a bag "
            "of small bones - and it is thrown with a full hip turn, the "
            "supporting foot pivoting so the kicker's whole body rotates "
            "into the blow. A single clean low kick buckles the leg; a "
            "dozen end the fight's movement. Defense exists - the check, "
            "taught later - which is why the low kick is set up with "
            "punches, never thrown naked into a ready opponent."
        ),
        "how_it_works": (
            "Throw the low kick in six steps. Step one: from the stance, "
            "set it up with a jab or a cross - the hands occupy the "
            "opponent's eyes while the kick travels below them. Step two: "
            "step the lead foot slightly outward and pivot hard on its "
            "ball, opening the hips like a gate. Step three: swing the "
            "rear leg through with the knee slightly bent, rotating the "
            "hips fully so the kicking hip turns over and the shin, not "
            "the foot, becomes the striking surface. Step four: strike "
            "the outside or inside of the opponent's thigh with the middle "
            "of the shin, following through the target rather than "
            "stopping on it. Step five: let the kicking leg swing through "
            "and plant it back into stance - or, for the advanced "
            "variation, step through into a new angle. Step six: keep the "
            "hands up through the entire kick, because the kick drops one "
            "side of the guard and counters come over the top. Drill: on "
            "the heavy bag, throw ten low kicks per leg per round for "
            "three rounds, checking that the shin - never the instep - "
            "takes the impact, and condition the shins gradually over "
            "months, never by kicking hard objects."
        ),
        "key_points": [
            "Chute baixo is the signature Brazilian strike: a shin-driven kick to the thigh that destroys the opponent's mobility.",
            "It lands with the shin, never the foot - the shin is the bat, the foot is fragile - with a full hip turn behind it.",
            "The supporting foot pivots hard on its ball; without the pivot the hips cannot turn over and the kick is a slap.",
            "Set it up with punches, never thrown naked: the hands occupy the eyes while the kick travels underneath.",
            "Condition shins gradually on the bag over months; kicking hard objects is how beginners break their own legs.",
        ],
        "requirements": [
            "A heavy bag for full-power reps - never practice full-power low kicks on a partner's unprotected leg.",
            "Shin guards for any partner drilling, even at light contact.",
            "The hip turn drilled slowly first: pivot, turn over, shin contact, plant - speed comes last.",
            "Hands up through every kick; the kick opens one side of the guard and must not open both.",
            "Gradual shin conditioning over months on pads and bags, never on trees, posts, or other hard objects.",
        ],
        "standards": [
            "Contact is made with the middle of the shin; instep contact is an immediate correction.",
            "The kicking hip turns fully over at impact - an unturned hip marks an arm-style kick with no power.",
            "Low kicks are set up behind punches in drilling; naked kicks are a sparring fault until the advanced levels.",
        ],
        "citations": [CIT_KRAUSS, CIT_PENN],
        "sig_lens": (
            "The Signature read: the low kick is the Signature axe at the "
            "root - the covenant that mobility is earned and can be "
            "taken. It swears to chop the stance, not the man: patient, "
            "repeated, honest work that fells the biggest tree."
        ),
    },
]
ENTRIES.extend([
    {
        "key": "vt_clinch",
        "name": "The Vale Tudo Clinch Tie",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The clinch is the standing grapple - chest to chest, arms "
            "tied up, foreheads near - and in vale tudo it is the bridge "
            "between striking and takedowns. The old challenge fights "
            "spent enormous time here: one fighter tying up the other's "
            "arms to stop the punches, working for the underhook that "
            "controls the torso, or breaking to strike. The clinch tie "
            "begins with the entry - stepping inside the punching range "
            "with the head positioned to the side, never straight into a "
            "knee - and continues with pummeling, the swimming of the "
            "arms for inside position. Whoever owns the inside owns the "
            "clinch: double underhooks mean control and the takedown is "
            "near; double overhooks mean defense and the need to pummel "
            "out. The clinch is also where knees and elbows live, so the "
            "head position and the hand fight decide who eats them."
        ),
        "how_it_works": (
            "Enter and work the clinch in six steps. Step one: close the "
            "distance behind a jab or a level change, stepping deep with "
            "the lead foot to the outside of the opponent's lead foot. "
            "Step two: place the head on the opponent's lead-shoulder side, "
            "cheek to his chest or shoulder - never head-on, where the "
            "knee meets the face. Step three: swim the arms inside for the "
            "underhooks, hands clasped behind his back or on his far "
            "shoulder; if he has the underhooks, pummel - swim one arm "
            "over and one under in a continuous cycle until you own the "
            "inside. Step four: control the head with one hand when "
            "possible, pulling it down to break his posture, because a "
            "broken posture cannot throw knees or defend takedowns. Step "
            "five: use short footwork - the clinch has no long steps, only "
            "small drags and pivots to off-balance him toward your "
            "takedown. Step six: break cleanly when you want to strike: "
            "push the head down, step back to range with the hands up, "
            "never turning away. Drill: three two-minute rounds of pure "
            "pummeling with a partner, no strikes, fighting only for the "
            "underhooks - the winner of the pummel wins the clinch."
        ),
        "key_points": [
            "The clinch is the bridge between striking and takedowns: chest to chest, arms tied, where underhooks decide control.",
            "Enter behind a punch with the head to the side - head-on entries meet the knee.",
            "Pummeling is the hand fight for inside position: swim continuously until you own the underhooks.",
            "Control the head to break posture; a broken-posture opponent cannot knee, cannot punch, and cannot sprawl.",
            "Break cleanly back to range with the hands up - turning away from the clinch is how knockouts happen.",
        ],
        "requirements": [
            "A partner for all clinch work - the clinch cannot be learned on a bag.",
            "Mouthguard in, because heads collide in the clinch even in friendly drilling.",
            "The head-to-the-side entry drilled slowly before any live pummeling.",
            "Continuous pummeling rounds with no strikes to isolate the hand fight.",
            "Short, balanced footwork: long steps in the clinch get you thrown.",
        ],
        "standards": [
            "Head position is checked on every entry: cheek to chest or shoulder on the outside, never forehead to forehead.",
            "Double underhooks are the control standard; double overhooks are the signal to pummel out, not to rest.",
            "Clinch breaks are done facing the partner with hands up - turning the back is a fault.",
        ],
        "citations": [CIT_PENN, CIT_KRAUSS],
        "sig_lens": (
            "The Signature read: the clinch is the Signature embrace - "
            "the covenant of the inside. It swears that in the tangle of "
            "arms, position is honesty: own the underhook and you own the "
            "truth of the exchange."
        ),
    },
    {
        "key": "vt_sprawl",
        "name": "The Sprawl: Stopping the Takedown",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The sprawl is the striker's answer to the wrestler and the "
            "single most important defensive technique in vale tudo: when "
            "the opponent shoots for the legs, the defender throws his "
            "hips back and his legs out behind him, landing chest-heavy on "
            "the shooter's back and shoulders. Done right, the shooter's "
            "arms close on empty air where the legs used to be, and his "
            "face meets the defender's full weight driving down through "
            "his neck and shoulders. The old vale tudo strikers lived by "
            "the sprawl - it is what let a puncher survive against the "
            "Gracie-style takedown game. The sprawl is not a jump "
            "backward; it is a violent hip-throw to the mat behind you, "
            "paired with a downward push on the opponent's head and "
            "shoulders. Speed matters more than strength: the hips must "
            "beat the hands."
        ),
        "how_it_works": (
            "Sprawl in five steps. Step one: read the level change - the "
            "opponent's hips drop and his head comes forward - and react "
            "instantly; hesitation is the sprawl's only true enemy. Step "
            "two: throw both legs straight back as far as they go while "
            "dropping the hips to the mat, landing on the tops of the feet "
            "with the legs wide - the hips travel back and down, not up. "
            "Step three: as the hips land, drive the chest and the full "
            "body weight down onto the opponent's upper back, neck, and "
            "shoulders, sprawling heavy like a blanket of concrete. Step "
            "four: push his head down with both hands or crossface him "
            "with a forearm, keeping his face in the mat so he cannot "
            "come up the body to finish the takedown. Step five: circle "
            "to the side and stand back up, or spin behind for the back - "
            "never stand straight up in front of him, which invites the "
            "second shot. Drill: a partner shoots lightly from three "
            "meters, then two, then one, while you sprawl and crossface; "
            "ten reps per distance per session. The advanced version adds "
            "the whizzer once the sprawl is reflex."
        ),
        "key_points": [
            "The sprawl beats the shot by removing the target: hips thrown back and down, legs out behind, weight crushing onto the shooter's back.",
            "It is a hip-throw backward, not a jump: the hips must beat the opponent's hands to the mat.",
            "Drive the chest onto his upper back and push his head down - a face-down shooter cannot finish the takedown.",
            "Circle out or spin behind after the sprawl; standing straight up in front invites the second shot.",
            "Speed over strength: drill against closer and faster shots until the sprawl is pure reflex.",
        ],
        "requirements": [
            "A partner shooting at controlled speed - the sprawl is a reaction drill, not a solo exercise.",
            "Mats, because the drill ends with both bodies on the floor.",
            "The level-change read: hips drop, head comes forward - drilled until the reaction is instant.",
            "Legs thrown wide and straight back; narrow or bent legs leave the hips in reach.",
            "The crossface or head-push on every rep, so the finish becomes part of the reflex.",
        ],
        "standards": [
            "Hips land on the mat behind the original stance line with legs extended - a standing sprawl is no sprawl.",
            "The defender's weight drives down through the opponent's neck and shoulders, not onto his own knees.",
            "Every sprawl ends with a circle-out or a spin-behind, never a straight stand-up in front of the shooter.",
        ],
        "citations": [CIT_PENN, CIT_GENTRY],
        "sig_lens": (
            "The Signature read: the sprawl is the Signature denial - the "
            "covenant that what is yours stays yours. It swears the hips "
            "will travel faster than any hand, and the mat behind you "
            "belongs to you alone."
        ),
    },
    {
        "key": "vt_guard",
        "name": "Closed Guard in Vale Tudo",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The closed guard - legs wrapped around the opponent's waist, "
            "ankles locked behind his back, from the bottom - is the "
            "position that made Brazilian fighting famous: the smaller "
            "fighter on his back, controlling the larger fighter with his "
            "legs, safe from punches and hunting submissions. In vale tudo "
            "the guard is both shield and weapon. As a shield, the legs "
            "control distance: the guard player keeps the opponent's "
            "posture broken, his weight managed, and his strikes smothered. "
            "As a weapon, the guard is the launchpad for the sweeps and "
            "submissions that fill the advanced ladder - the armbar, the "
            "triangle, the kimura all begin here. The beginner's job is "
            "simpler: hold the position, break the posture, and survive. "
            "The closed guard only works while the ankles stay locked; the "
            "moment they open, the guard is open, and the passing battle "
            "begins."
        ),
        "how_it_works": (
            "Play the closed guard in six steps. Step one: from your back, "
            "wrap both legs around the opponent's waist and lock your "
            "ankles behind his back - high on the back is control, low on "
            "the hips is loose. Step two: grip his sleeves, collar, or "
            "wrists and pull his head down toward your chest, breaking his "
            "posture; an upright opponent in your guard is a puncher, a "
            "broken-posture opponent is a passenger. Step three: keep your "
            "hips mobile - shrimp slightly side to side so he cannot stack "
            "his weight straight down onto you. Step four: when he "
            "postures up to strike, pull him back down with the legs and "
            "arms together, or threaten the hip-bump sweep to make him "
            "post a hand - every defense he makes opens an attack. Step "
            "five: never let both of his arms control your head at once; "
            "swim one arm inside and keep an elbow between you and his "
            "chest. Step six: if he stands to pass, keep the ankle lock "
            "until the last moment, then open into the open guard game - "
            "but that is the compounded ladder. Drill: three three-minute "
            "rounds of guard retention, partner trying to pass at half "
            "speed, you keeping the ankles locked and the posture broken."
        ),
        "key_points": [
            "The closed guard is shield and weapon: legs locked around the waist control the opponent while the arms break his posture.",
            "Ankles locked high on the back is control; the guard only exists while the lock holds.",
            "Break the posture first: an upright opponent punches, a broken-posture opponent is controlled.",
            "Keep the hips mobile with small shrimps so his weight never stacks straight down onto you.",
            "Every attack he defends opens another: the guard is a system of threats, not a single hold.",
        ],
        "requirements": [
            "A grappling partner and mats - the guard is a two-person position.",
            "The breakfall record solid, since guard play starts from the back on the mat.",
            "Grip fighting basics: control his wrists or collar before he controls yours.",
            "Hip mobility: the shrimp from the hip-escape record is the guard's engine.",
            "Patience: the beginner's guard goal is retention and posture-breaking, not submissions.",
        ],
        "standards": [
            "Ankles stay locked behind the back through all retention drilling; an opened lock means the guard is open.",
            "The opponent's posture is broken toward the guard player's chest before any attack is attempted.",
            "Guard retention rounds are done at controlled speed - the beginner survives first and attacks later.",
        ],
        "citations": [CIT_GRACIE, CIT_PENN],
        "sig_lens": (
            "The Signature read: the guard is the Signature fortress - "
            "the covenant of the bottom. It swears that being underneath "
            "is not being beaten: the legs are walls, the posture-break "
            "is the gate, and every visitor enters on the guard player's "
            "terms."
        ),
    },
    {
        "key": "vt_hipescape",
        "name": "The Hip Escape: Shrimping to Safety",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The hip escape - the shrimp - is the fundamental ground "
            "movement of the entire Brazilian game: lying on your back or "
            "side, you bridge slightly, turn onto your side, and scoot "
            "your hips away from the opponent, creating the space that "
            "every guard recovery and every mount escape requires. It is "
            "named for the shrimp-like curl of the body, and it is the "
            "first ground technique every vale tudo student learns, "
            "because without it there is no escape from bad positions - "
            "only waiting. The mechanics are all hips and frames: the arms "
            "make a rigid frame against the opponent's body, the legs "
            "drive, and the hips slide through the gap the frame protects. "
            "Done in a chain - shrimp, shrimp, shrimp - it walks the "
            "fighter across the mat and, with a leg inserted at the right "
            "moment, rebuilds the guard from underneath the mount or side "
            "control."
        ),
        "how_it_works": (
            "Shrimp in five steps. Step one: lie on your back with knees "
            "bent and feet flat, arms in a frame - one forearm across the "
            "imaginary opponent's chest, the other hand on his shoulder or "
            "bicep. Step two: bridge your hips a few centimeters off the "
            "mat - just enough to unstick them, not a full bridge. Step "
            "three: turn onto one side as the hips come down, so your "
            "side, not your back, faces the opponent; the frame stays "
            "rigid through the turn. Step four: scoot the hips away along "
            "the mat, pushing with the feet, moving the hips a full body "
            "length from where they started. Step five: reset to your back "
            "and repeat to the other side - shrimping is always chained "
            "in alternating directions. Drill: shrimp the full length of "
            "the mat and back, ten lengths per session, keeping the frames "
            "up the whole way; then drill with a partner applying light "
            "pressure from side control while you shrimp and insert a knee "
            "to recover the guard. The test is simple: if your frames "
            "collapse or you push with your arms instead of moving your "
            "hips, slow down and rebuild."
        ),
        "key_points": [
            "The shrimp is the fundamental ground movement: bridge slightly, turn to the side, scoot the hips away, and every escape becomes possible.",
            "The arms make a rigid frame and the hips do the traveling - pushing with the arms instead of moving the hips is the classic fault.",
            "Shrimping is always chained in alternating directions; one shrimp makes space, the chain makes escapes.",
            "The knee inserted during the shrimp rebuilds the guard - the shrimp is the engine of guard recovery.",
            "Drill it as conditioning: ten mat lengths per session until the movement needs no thought.",
        ],
        "requirements": [
            "Open mat space for full-length shrimping lines.",
            "The frame concept: forearms as a rigid barrier, not pushing arms.",
            "A partner for the pressure version once the solo movement is clean.",
            "Alternating sides on every chain - one-sided shrimping builds a one-sided escape game.",
            "The bridge kept small: a big bridge wastes energy and lifts you into the opponent's weight.",
        ],
        "standards": [
            "Hips travel a full body length per shrimp along the mat - short scoots are corrected.",
            "Frames stay up through the entire movement; collapsed frames mean the drill stops and rebuilds.",
            "The movement is hips-first: the test is whether the hips move before the arms push.",
        ],
        "citations": [CIT_GRACIE, CIT_PENN],
        "sig_lens": (
            "The Signature read: the shrimp is the Signature retreat - "
            "the covenant that ground is never surrendered, only traded "
            "for space. It swears the hips will travel and the frames "
            "will hold, and from that small honest movement the whole "
            "ground game is rebuilt."
        ),
    },
    {
        "key": "vt_uppercut",
        "name": "The Vale Tudo Uppercut",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The uppercut is the rising punch of the compounded ladder, "
            "thrown upward with a bent arm to attack the chin and the "
            "solar plexus from below the opponent's line of sight. In "
            "vale tudo it is the close-range finisher: when the guard is "
            "high and tight against straight punches and hooks, the "
            "uppercut travels up the middle where the guard is not. The "
            "old Brazilian fighters threw it in the clinch break and in "
            "the pocket, often as the last punch of a combination when "
            "the opponent covered up. Its power comes from the legs and "
            "hips driving upward - the punch is the top of a kinetic "
            "chain that starts with bent knees - and its danger to the "
            "thrower is the level change it resembles: a sloppy uppercut "
            "drops the hands and the head into counters, so it is thrown "
            "with the rear hand home and the chin tucked, always."
        ),
        "how_it_works": (
            "Throw the rear uppercut in six steps. Step one: from the "
            "stance, bend the knees a few centimeters to load the legs - "
            "the dip is small, never a squat. Step two: drop the rear "
            "shoulder slightly and keep the rear elbow tucked to the "
            "ribs, fist at chest height with the palm facing you. Step "
            "three: drive up with the legs and rotate the rear hip "
            "forward, punching upward in a tight arc aimed at the chin or "
            "the solar plexus, fist rotating palm-up at impact. Step four: "
            "keep the lead hand glued to the chin and the chin tucked "
            "throughout - the uppercut must never cost the guard. Step "
            "five: do not overextend upward; the punch ends at chin "
            "height of the target, and the elbow stays bent - a "
            "straightened arm turns the uppercut into a weak shovel. Step "
            "six: return the rear hand straight down to guard and reset "
            "the knees. Drill: on the bag, throw jab-cross-rear uppercut "
            "as a unit for three rounds, then practice the lead uppercut "
            "the same way, checking in the mirror that the dip stays "
            "small and the rear hand stays home."
        ),
        "key_points": [
            "The uppercut attacks from below the line of sight: up the middle to the chin and solar plexus where the high guard is not.",
            "Power comes from the legs driving up through the hips - the punch is the top of a chain that starts with bent knees.",
            "The dip is small and the elbow stays bent; overextending upward turns the punch into a weak, exposed shovel.",
            "The opposite hand stays home and the chin stays tucked - the uppercut must never cost the fighter his guard.",
            "It is the combination finisher: thrown last, when the opponent has covered up against the straight punches.",
        ],
        "requirements": [
            "The jab, cross, and hook solid, since the uppercut usually closes a combination.",
            "A heavy bag for the upward arc - the uppercut cannot be shadowboxed into real power.",
            "Knee bend drilled as a small dip; beginners who squat telegraph the punch by a full second.",
            "The guard hand home on every rep, checked by a coach or in the mirror.",
            "Both sides drilled: rear uppercut first, lead uppercut second.",
        ],
        "standards": [
            "The punching elbow stays bent through impact - a straight arm at contact is a fault.",
            "The knee dip is a load of a few centimeters, never a visible squat.",
            "The punch travels up the middle on a tight arc; wide looping uppercuts are corrected to the tight line.",
        ],
        "citations": [CIT_PENN, CIT_KRAUSS],
        "sig_lens": (
            "The Signature read: the uppercut is the Signature rising - "
            "the covenant of the low road. It swears that what is "
            "buried - the legs, the patience, the small dip - will rise "
            "through the middle where no guard was built."
        ),
    },
    {
        "key": "vt_elbows",
        "name": "Elbow Strikes: Cotoveladas",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The elbow strike - cotovelada in Portuguese - is the close-"
            "quarters blade of vale tudo: the forearm folds and the point "
            "of the elbow becomes the striking surface, concentrating all "
            "the rotation of the torso into a few square centimeters. The "
            "old vale tudo rules made elbows famous - they cut, they "
            "stun, and at clinch range they land where punches cannot "
            "chamber. There are four basic elbows: the horizontal elbow "
            "swung across like a short hook, the upward elbow rising like "
            "a compact uppercut, the downward spike dropped onto the "
            "brow, and the spinning elbow that turns the whole body into "
            "the blow. Because the elbow is a short weapon, it is thrown "
            "from the clinch, the pocket, and the ground - and because it "
            "cuts easily, it is drilled on pads and bags, never at full "
            "power on a partner's face."
        ),
        "how_it_works": (
            "Throw the horizontal elbow in six steps. Step one: from the "
            "clinch or the pocket, raise the lead elbow to shoulder "
            "height with the arm folded tight - the fist nearly touches "
            "the shoulder. Step two: pivot on the lead foot and rotate "
            "the hips and torso violently, swinging the elbow across on a "
            "tight horizontal arc; the arm stays folded, the rotation "
            "does the work. Step three: strike with the point of the "
            "elbow, wrist straight and fist tucked, landing across the "
            "target - never with a loose swinging arm. Step four: keep "
            "the rear hand on the chin throughout; the elbow's rotation "
            "tempts the guard open. Step five: return the arm to the "
            "folded guard immediately - a dangling elbow gets grabbed. "
            "Step six: drill the other three the same way - the upward "
            "elbow rising from the chambered fold, the downward spike "
            "dropping with a small level change, the spinning elbow "
            "thrown only after the first three are clean, with a full "
            "shoulder check for what's behind you. Drill: on the bag, "
            "ten of each elbow per round for three rounds, checking that "
            "the point of the elbow - never the forearm - takes the "
            "impact."
        ),
        "key_points": [
            "The cotovelada concentrates torso rotation into the point of the elbow: a short weapon that cuts and stuns at ranges where punches cannot chamber.",
            "Four elbows cover the close game: horizontal, upward, downward spike, and the spinning elbow for advanced students.",
            "The arm stays folded tight with the fist near the shoulder - the rotation does the work, not an arm swing.",
            "Strike with the point of the elbow, wrist straight; forearm contact is a fault and a lost cut.",
            "Drill on pads and bags only at power; elbows cut easily, so partner work stays light and controlled.",
        ],
        "requirements": [
            "The clinch record solid, since most elbows are thrown from the clinch or the pocket.",
            "A heavy bag or Thai pads for full-power reps - never full power on a partner.",
            "The folded-arm chamber drilled until the fist finds the shoulder without thought.",
            "Headgear for any partner elbow drilling, even at light contact.",
            "The spinning elbow held until the first three elbows are clean - it turns the back and needs mat awareness.",
        ],
        "standards": [
            "Contact is made with the point of the elbow; forearm or fist contact is corrected immediately.",
            "The arm remains folded through the strike - an unfolding arm turns the elbow into a weak slap.",
            "The guard hand stays home through the rotation; the elbow must never cost the chin its cover.",
        ],
        "citations": [CIT_KRAUSS, CIT_PENN],
        "sig_lens": (
            "The Signature read: the elbow is the Signature blade - the "
            "covenant of the folded arm. It swears that the shortest "
            "weapon, honestly chambered, cuts deeper than the longest "
            "weapon wildly swung."
        ),
    },
    {
        "key": "vt_knees",
        "name": "Knee Strikes from the Vale Tudo Clinch",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The knee strike - joelhada - is the clinch's finishing weapon "
            "in vale tudo: with the opponent's posture broken and his "
            "head pulled down, the fighter drives the knee upward into the "
            "body and, in the old rules, the head. The Brazilians adopted "
            "it from Thai boxing and made it a vale tudo staple, because "
            "the clinch that controls the head controls the knees, and "
            "the knees end arguments about who owns the inside. The "
            "mechanics are a violent hip thrust: the standing leg stays "
            "planted, the hips drive forward and up, and the knee rises "
            "on a spear line with the toes pointed down and the hands "
            "pulling the opponent's head into the blow. In the modern "
            "sport, knees to the head of a grounded opponent are banned - "
            "this record teaches the standing clinch knee to the body, "
            "the legal and fundamental version, drilled on pads and bags."
        ),
        "how_it_works": (
            "Throw the clinch knee in six steps. Step one: from the "
            "clinch with head control, pull the opponent's head down with "
            "both hands clasped behind his neck - the pull and the knee "
            "are one motion, not two. Step two: plant the standing foot "
            "and rise onto its ball, keeping the base leg slightly bent "
            "for balance. Step three: thrust the hips forward and upward "
            "while driving the knee up in a straight spear line, toes "
            "pointed down, aiming the point of the knee at the solar "
            "plexus or the ribs. Step four: at the moment of impact, pull "
            "down hard with the hands - the collision of the rising knee "
            "and the falling head multiplies the force. Step five: return "
            "the knee straight down to the mat without swinging it out to "
            "the side; a swinging return gets caught for the takedown. "
            "Step six: reset the clinch grip immediately and be ready to "
            "knee again - knees are thrown in volleys, not singles. "
            "Drill: on the Thai pads held at body height, throw ten knees "
            "per side per round for three rounds, checking that the hip "
            "thrust, not the leg lift, powers the strike."
        ),
        "key_points": [
            "The joelhada is the clinch finisher: head pulled down with the hands while the knee spears up to meet it.",
            "Power comes from the hip thrust driving forward and up - the knee is the spearhead, the hips are the shaft.",
            "Toes point down and the knee travels a straight line; a looping knee is slow and catchable.",
            "Return the knee straight down after impact - swinging it wide invites the takedown.",
            "Knees are thrown in volleys behind head control; the single knee is the setup, the volley is the weapon.",
        ],
        "requirements": [
            "The clinch tie record solid, including head control and posture-breaking.",
            "Thai pads or a heavy bag for full-power reps - knees are never thrown hard at a partner's body unprotected.",
            "Balance on the standing leg drilled first: ten slow knees per side holding the clinch grip.",
            "The hand-pull and the knee timed as one motion; pulling without kneeing wastes the control.",
            "Body protector for any partner knee drilling, even at reduced power.",
        ],
        "standards": [
            "The knee travels straight up on a spear line with toes pointed down - looping is corrected.",
            "Impact is timed with the downward hand pull; knee and pull land together.",
            "The standing foot stays planted on its ball through the strike - hopping or falling forward is a fault.",
        ],
        "citations": [CIT_KRAUSS, CIT_PENN],
        "sig_lens": (
            "The Signature read: the knee is the Signature spear - the "
            "covenant of the broken posture. It swears that control comes "
            "first and the finish second: pull the head down honestly, "
            "and the knee will find the road you built."
        ),
    },
    {
        "key": "vt_doubleleg",
        "name": "The Double Leg Takedown in Vale Tudo",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The double leg takedown is the definitive takedown of the "
            "Brazilian game: the fighter changes levels, penetrates deep "
            "between the opponent's legs, wraps both legs, and drives "
            "through to put him on the mat. It is the technique that made "
            "the Gracie challenge matches possible - the striker's "
            "punches meant nothing once both legs were wrapped - and it "
            "remains the highest-percentage takedown in the sport. The "
            "double leg has four phases: the setup, usually punches that "
            "occupy the hands and the eyes; the level change, dropping the "
            "hips below the opponent's; the penetration step, a deep lunge "
            "that puts the shoulder into the opponent's midsection; and "
            "the finish, driving forward while the arms scoop the legs "
            "and the head stays tight to the body. Head position decides "
            "everything: head inside risks the guillotine, head tight to "
            "the outside hip is safe."
        ),
        "how_it_works": (
            "Shoot the double leg in seven steps. Step one: set it up - "
            "throw a jab-cross so the opponent's hands rise and his eyes "
            "follow the punches. Step two: change levels by bending the "
            "knees, dropping your hips below his, keeping the back "
            "straight - never bend at the waist, which feeds the "
            "guillotine. Step three: take the penetration step, lunging "
            "deep with the lead leg so the lead knee lands on the mat "
            "between his feet and your shoulder meets his midsection. "
            "Step four: wrap both arms around his legs, hands clasped "
            "behind his knees, head pressed tight to the outside of his "
            "hip - cheek to hip, never head inside. Step five: drive "
            "forward off the back leg, pushing with the shoulder while "
            "the arms scoop the legs upward. Step six: as he falls, follow "
            "him down into side control or the mount - the takedown is "
            "only half the technique; the landing position is the other "
            "half. Step seven: drill the finish separately - cut the "
            "corner by circling as he falls so you land past his guard. "
            "Drill: ten penetration steps without a partner per round, "
            "then ten full doubles on a cooperative partner per round, "
            "for three rounds."
        ),
        "key_points": [
            "The double leg is the highest-percentage takedown in vale tudo: level change, penetrate, wrap both legs, drive through.",
            "Set it up with punches - the hands occupy the eyes while the level change happens underneath.",
            "Head tight to the outside hip, never inside: head position is the difference between a takedown and a guillotine.",
            "The penetration step must be deep - lead knee to the mat between his feet, shoulder to his midsection.",
            "Finish past the guard: follow the fall and land in side control, because the takedown is only half the technique.",
        ],
        "requirements": [
            "The stance, footwork, and breakfall records - the shot starts from stance and ends with someone falling.",
            "A cooperative partner and mats for all live reps.",
            "The level change drilled as a knee bend with a straight back; waist-bending is the guillotine invitation.",
            "Ten clean penetration steps solo before any partner shooting.",
            "The corner-cut finish drilled separately until the landing position is automatic.",
        ],
        "standards": [
            "The back stays straight through the level change - bending at the waist is an immediate stop-and-correct.",
            "The head finishes tight to the outside of the hip; head-inside finishes are not drilled at this level.",
            "Every rep ends in a control position past the guard, never in a scramble with no position.",
        ],
        "citations": [CIT_GRACIE, CIT_PENN],
        "sig_lens": (
            "The Signature read: the double leg is the Signature flood - "
            "the covenant of the level changed. It swears to go beneath "
            "the storm of punches and rise with both legs wrapped: the "
            "humble road under the battle, honestly traveled."
        ),
    },
])
ENTRIES.extend([
    {
        "key": "vt_singleleg",
        "name": "The Single Leg Takedown in Vale Tudo",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The single leg takedown is the double leg's precise sibling: "
            "instead of wrapping both legs, the fighter captures one, "
            "controls it, and uses it as a lever to topple the opponent. "
            "In vale tudo it shines where the double leg struggles - "
            "against a wide, sprawling stance, or when the opponent "
            "defends one leg and leaves the other. The classic entries "
            "are the snatch single, snatching the ankle from outside, and "
            "the high single, driving the shoulder into the thigh while "
            "wrapping the leg high. Once the leg is captured, the finishes "
            "multiply: run the pipe by stepping across and kicking the "
            "supporting leg out, lift and dump by elevating the leg and "
            "driving, or trip by hooking the far ankle. The single leg "
            "demands head position as strict as the double's - head tight "
            "to the body, never reaching across - and it rewards the "
            "fighter who chains finishes when the first one stalls."
        ),
        "how_it_works": (
            "Shoot the snatch single in seven steps. Step one: set it up "
            "with punches or an angle step to the opponent's lead-leg "
            "side. Step two: change levels with bent knees and a straight "
            "back. Step three: reach with the near arm and snatch the "
            "ankle or wrap the leg just above the ankle, pulling it to "
            "your shoulder while your head presses tight against his "
            "thigh - head inside the leg line, never reaching across his "
            "body. Step four: stand up with the leg, keeping it tight to "
            "your chest so he hops on one foot. Step five: run the pipe - "
            "step your outside leg across behind his supporting leg while "
            "driving your shoulder into his thigh, kicking his base out "
            "from under him. Step six: as he falls, keep the leg and "
            "follow him down into side control. Step seven: if he hops "
            "away instead, switch to the lift-and-dump - elevate the "
            "captured leg high and drive forward through him. Drill: ten "
            "snatch-and-stand reps per leg per round, then ten full "
            "finishes per round, for three rounds, alternating the pipe "
            "and the dump."
        ),
        "key_points": [
            "The single leg captures one leg and uses it as a lever: snatch the ankle, stand with it, and finish with the pipe or the dump.",
            "It shines where the double leg struggles - wide stances, one-leg defenses, and scrambles.",
            "Head tight to the thigh, never reaching across the body: head position is safety, as with the double.",
            "Chain the finishes: when the pipe stalls, lift and dump; when the dump stalls, trip the far ankle.",
            "Keep the captured leg tight to the chest while standing - a loose leg is a lost leg.",
        ],
        "requirements": [
            "The double leg record first - the level change and penetration are shared mechanics.",
            "A partner who can hop and fall safely; all finishes end with someone on the mat.",
            "The snatch drilled slowly to protect the partner's ankle - no yanking at speed until control is clean.",
            "Both finishes drilled separately before chaining: the pipe and the lift-and-dump.",
            "Mats and a coach checking head position on the first live rounds.",
        ],
        "standards": [
            "The head stays on the inside line, tight to the thigh - reaching across the body is a fault.",
            "The captured leg is held tight to the chest through the stand-up; a dangling leg is corrected.",
            "Every rep finishes in a control position on the ground, never in a standing stalemate.",
        ],
        "citations": [CIT_GRACIE, CIT_PENN],
        "sig_lens": (
            "The Signature read: the single leg is the Signature lever - "
            "the covenant of the one thing held truly. It swears that a "
            "single honest grip, kept tight and finished with patience, "
            "topples what two arms waving could not."
        ),
    },
    {
        "key": "vt_whizzer",
        "name": "The Whizzer and Takedown Defense Chains",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The whizzer is the overhook defense that turns a takedown "
            "attempt into the defender's attack: when the opponent shoots "
            "and gets head-inside or reaches deep, the defender throws an "
            "overhook - the arm over the opponent's shoulder and deep "
            "under his armpit - and uses it as a lever to stuff the head "
            "down, sprawl the hips back, and break the shot. Combined with "
            "the sprawl from the foundations ladder, the whizzer gives "
            "the vale tudo fighter a complete takedown defense chain: "
            "sprawl first to kill the penetration, whizzer second to "
            "control the upper body, crossface third to turn the corner. "
            "The old Brazilian fighters prized the whizzer because the "
            "challenge matches were full of wrestlers, and the man who "
            "could stuff the shot stayed standing where his strikes "
            "lived. It is a leverage technique, not a strength "
            "technique: the overhook arm is a long lever on the "
            "opponent's shoulder, and the hips going back do the real "
            "work."
        ),
        "how_it_works": (
            "Defend with the whizzer chain in six steps. Step one: as the "
            "opponent shoots, sprawl the hips back first - the whizzer "
            "without the sprawl is an invitation to be lifted. Step two: "
            "throw the near arm over his shoulder and thread it deep "
            "under his armpit, grabbing your own wrist or his far lat - "
            "this is the whizzer, the overhook that becomes your lever. "
            "Step three: straighten the whizzer arm hard and drive his "
            "head and shoulder down toward the mat, using the lever to "
            "break his posture while your hips stay heavy on his back. "
            "Step four: crossface with the free hand - forearm across his "
            "face, pushing his head away - which turns his shoulders and "
            "kills any remaining drive. Step five: circle toward the "
            "whizzer side, stepping around his body as his shot dies. "
            "Step six: when his hands hit the mat, spin behind and take "
            "the back, or stand up and disengage - the chain ends with "
            "you in control, never in a neutral scramble. Drill: partner "
            "shoots at half speed, you sprawl-whizzer-crossface-circle, "
            "ten reps per side per round for three rounds."
        ),
        "key_points": [
            "The whizzer is the overhook lever that stuffs the shot: sprawl first, overhook deep, drive the head down, crossface, circle.",
            "It chains with the sprawl: the sprawl kills the penetration, the whizzer controls the upper body, the crossface turns the corner.",
            "Leverage, not strength: the overhook arm is a long lever on his shoulder while your hips do the heavy work behind.",
            "Thread the whizzer deep under the armpit - a shallow overhook on the shoulder slips off under pressure.",
            "Every chain ends in control: the back take or the clean disengage, never a neutral scramble.",
        ],
        "requirements": [
            "The sprawl record as reflex first - the whizzer is step two of the chain, not step one.",
            "A partner shooting at controlled speed for all reps.",
            "The deep overhook drilled slowly: over the shoulder, under the armpit, grip secured.",
            "The crossface added only after the whizzer control is clean.",
            "Both sides drilled, since shots come to both hips.",
        ],
        "standards": [
            "The sprawl precedes the whizzer on every rep - whizzer without sprawl is corrected.",
            "The overhook threads deep under the armpit with a secured grip; a shallow hook is a fault.",
            "The chain ends with the back take or disengagement; stopping at the stuff is incomplete.",
        ],
        "citations": [CIT_PENN, CIT_GENTRY],
        "sig_lens": (
            "The Signature read: the whizzer is the Signature answer - "
            "the covenant that every attack carries its own defeat. It "
            "swears to meet the shoot not with panic but with the "
            "overhook lever, and to turn the takedown into the takedown "
            "defended."
        ),
    },
    {
        "key": "vt_guardpass",
        "name": "Pressure Passing the Guard in Vale Tudo",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Guard passing is the art of getting past the opponent's legs "
            "to reach a dominant position, and pressure passing is the "
            "vale tudo way: no flashy jumps, just relentless shoulder "
            "pressure, hip control, and weight that makes the bottom "
            "fighter carry you until his guard breaks. The old Brazilian "
            "top game was built on this - the passer stacks, smashes, and "
            "slides through, pinning one leg, controlling the hips, and "
            "advancing inch by inch. The two fundamental passes are the "
            "knee slice, driving the knee across the thigh while "
            "controlling the upper body, and the over-under, pinning one "
            "leg under the shoulder while the other arm goes over the far "
            "side. Both obey the same law: control the hips and the head "
            "before moving the legs, because the hips are the guard's "
            "engine and the head is its steering."
        ),
        "how_it_works": (
            "Pass with the knee slice in seven steps. Step one: from "
            "inside the open guard, control the opponent's hips with your "
            "hands - one on the hip bone, one controlling a sleeve or the "
            "head. Step two: pin his near leg to the mat with your "
            "same-side hand or your shin, killing its ability to re-guard. "
            "Step three: step your far leg up into a combat base, knee up "
            "and foot flat, so your weight can drive forward. Step four: "
            "slice your near knee across his thigh, keeping your chest "
            "heavy on his torso and your head low - the pressure goes "
            "through your shoulder into his chest, not into the air. Step "
            "five: as the knee clears the leg, slide the hips through and "
            "settle into side control, keeping the underhook that "
            "controls his far arm. Step six: never let both of his arms "
            "frame on your neck during the pass; swim one arm inside if he "
            "frames. Step seven: stabilize side control for a three-count "
            "before celebrating - the pass is only complete when the "
            "position is held. Drill: three three-minute rounds of pass-"
            "versus-retain, alternating the knee slice and the over-under."
        ),
        "key_points": [
            "Pressure passing is the vale tudo top game: shoulder pressure, hip control, and relentless weight instead of flashy movement.",
            "Control the hips and the head before moving the legs - the hips are the guard's engine and the head is its steering.",
            "The knee slice and the over-under are the two fundamental passes; both pin a leg and drive the chest through.",
            "Keep the chest heavy and the head low through the pass - pressure that goes into the air passes nothing.",
            "The pass is only complete when side control is stabilized for a three-count.",
        ],
        "requirements": [
            "The closed guard record understood from the bottom, so you know what the guard player is trying to do.",
            "A partner playing guard at controlled resistance for all passing rounds.",
            "The combat base - one knee up, one knee down - drilled as a stable platform before passing.",
            "Hip control established before every pass attempt; passing without hip control is scrambling.",
            "The three-count stabilization drilled as part of every rep.",
        ],
        "standards": [
            "Hips and head are controlled before the legs advance on every pass - no control, no pass.",
            "The passer's chest stays heavy on the opponent through the transition; daylight between chests is a fault.",
            "Side control is held for a three-count to complete the rep; immediate submission hunting skips the stabilization.",
        ],
        "citations": [CIT_GRACIE, CIT_PENN],
        "sig_lens": (
            "The Signature read: the pressure pass is the Signature tide "
            "- the covenant of the inevitable advance. It swears no "
            "hurry and no retreat: control the hips, pin the leg, and let "
            "honest weight do what haste cannot."
        ),
    },
    {
        "key": "vt_sidecontrol",
        "name": "Side Control and the Crossface in Vale Tudo",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Side control - chest to chest across the opponent's torso, "
            "from the side - is the first great dominant position of the "
            "vale tudo ground game, and the crossface is its enforcer. "
            "From here the top fighter is heavy, stable, and free to "
            "strike or to hunt submissions, while the bottom fighter "
            "carries the weight and plans his escape. The position's power "
            "is in the details: the crossface - the shoulder driven "
            "across the opponent's jaw, turning his head away - breaks "
            "the bottom fighter's alignment and kills his bridging power; "
            "the underhook on the far side controls the far arm; the hips "
            "stay low and heavy, blocking the hip escape with the knees. "
            "The old Brazilian top fighters made side control a place of "
            "attrition: every breath the bottom man takes is taxed, every "
            "bridge is stuffed, until the escape attempt itself becomes "
            "the submission opening."
        ),
        "how_it_works": (
            "Hold and attack from side control in six steps. Step one: "
            "settle perpendicular across the opponent's chest, hips low, "
            "chest heavy on his chest, knees wide for base - one knee by "
            "his hip blocking the escape, the other posted for balance. "
            "Step two: drive the near shoulder across his jaw - the "
            "crossface - turning his head away from you; his bridge now "
            "pushes sideways instead of into you. Step three: secure the "
            "underhook on the far side, hand reaching deep under his far "
            "armpit, which controls his far arm and anchors your weight. "
            "Step four: keep your head low and tight to his chest, so "
            "there is no space for him to shrimp into - space is the "
            "bottom man's currency and you are bankrupt him. Step five: "
            "when he bridges, ride it - go with the motion and resettle, "
            "never fighting the bridge with stiffness. Step six: attack "
            "when he moves - the kimura when he pushes, the armbar when "
            "he reaches, the knee-on-belly transition when he turns. "
            "Drill: three three-minute rounds of hold-and-transition, "
            "partner escaping at half speed, you maintaining and "
            "attacking the openings."
        ),
        "key_points": [
            "Side control is the first great dominant ground position: heavy, stable, and the launchpad for strikes and submissions.",
            "The crossface - shoulder across the jaw turning the head away - breaks alignment and kills bridging power.",
            "Underhook the far arm and keep the hips low: control the far side and the near escape route at once.",
            "Leave no space: the head stays tight to his chest, because space is the bottom fighter's currency.",
            "Attack the escape attempts: the bridge becomes the kimura, the reach becomes the armbar, the turn becomes knee-on-belly.",
        ],
        "requirements": [
            "The guard pass record solid, since side control is where passes land.",
            "A partner escaping at controlled speed for all holding rounds.",
            "The crossface drilled with control - it is pressure, not a strike; jaw pressure is applied gradually.",
            "Hip mobility on the bottom side understood, so you can recognize and stuff the shrimp.",
            "The three attacks - kimura, armbar, knee-on-belly - previewed so the position has somewhere to go.",
        ],
        "standards": [
            "Hips stay low and heavy with knees wide; high floating hips are corrected immediately.",
            "The crossface turns the head away on every hold - a face-up opponent still has his bridge.",
            "No space between the chests; a hand's width of daylight is a fault to resettle.",
        ],
        "citations": [CIT_GRACIE, CIT_PENN],
        "sig_lens": (
            "The Signature read: side control is the Signature weight - "
            "the covenant of the honest top. It swears to be heavy "
            "without cruelty: crossface the jaw, underhook the arm, and "
            "let position, patiently held, become the attack."
        ),
    },
    {
        "key": "vt_mount",
        "name": "Mount Control and Ground Strikes in Vale Tudo",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The mount - seated on the opponent's chest with a knee on "
            "each side - is the most dominant position in vale tudo, the "
            "place the old challenge fighters called the throne. From the "
            "mount the top fighter can strike downward with gravity's "
            "help while the bottom fighter can only bridge, roll, and "
            "pray; it is the position from which more vale tudo fights "
            "have been finished than any other. Control comes from the "
            "hips: low, heavy, with the knees pinching the ribs and the "
            "feet hooked under the legs or grapevined to kill the bridge. "
            "The beginner's mount is a balancing act - too high and the "
            "bridge throws you, too low and the elbows escape. The "
            "advanced mount is a system: high mount to isolate the arms, "
            "low mount to ride the bridges, and the transitions between "
            "them timed to the bottom man's panic."
        ),
        "how_it_works": (
            "Control the mount in six steps. Step one: settle with your "
            "knees pinched tight to his ribs, hips low on his belly, "
            "hands posted on the mat or controlling his wrists - never "
            "rest your hands on his chest where he can trap them. Step "
            "two: when he bridges, ride it - lift your hips slightly "
            "with the motion and resettle, keeping the knees pinched; "
            "fighting the bridge with stiffness is how mounts are lost. "
            "Step three: when he tries the elbow escape, block the hip "
            "with your hand and resettle your weight onto the escaping "
            "side. Step four: climb to the high mount - knees up under "
            "his armpits - when his arms are controlled, which isolates "
            "the arms for the armbar. Step five: from the high mount, "
            "attack - the armbar when an arm extends, the cross-collar "
            "grip when he turns his head, or controlled ground strikes in "
            "sparring with full safety gear and a coach present. Step "
            "six: if he rolls to his stomach, take the back instead of "
            "fighting to stay mounted - the mount that becomes the back "
            "take is the advanced game. Drill: three two-minute rounds of "
            "mount maintenance, partner bridging and escaping at half "
            "speed."
        ),
        "key_points": [
            "The mount is the throne of vale tudo: the most dominant position, where gravity assists every strike and the bottom man can only bridge.",
            "Control lives in the hips - low, heavy, knees pinching the ribs - not in the hands.",
            "Ride the bridge, do not fight it: lift with the motion and resettle, keeping the knees pinched.",
            "High mount isolates the arms for the armbar; low mount rides out the panic - transition between them with the bottom man's energy.",
            "When he rolls to his stomach, take the back: the mount that becomes the back take is the advanced game.",
        ],
        "requirements": [
            "The side control record solid, since the mount is usually reached through side control.",
            "A partner bridging and escaping at controlled speed.",
            "Full safety gear and a coach present for any ground-strike sparring from the mount.",
            "The elbow-escape block drilled: hand on the hip, weight resettled to the escaping side.",
            "The back take previewed, so the rolling opponent becomes an opportunity, not an escape.",
        ],
        "standards": [
            "Knees stay pinched to the ribs with hips low; floating high without arm control is corrected.",
            "Hands never rest on the opponent's chest where they can be trapped - post on the mat or control wrists.",
            "Ground strikes from the mount are drilled only with full protective gear, controlled contact, and coaching supervision.",
        ],
        "citations": [CIT_GRACIE, CIT_PENN],
        "sig_lens": (
            "The Signature read: the mount is the Signature throne - the "
            "covenant of the high ground honestly earned. It swears to "
            "hold without cruelty and to finish without malice: heavy "
            "hips, patient hands, and the throne kept by balance, not by "
            "force."
        ),
    },
    {
        "key": "vt_armbar",
        "name": "The Armbar from Mount in Vale Tudo",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The armbar - hyperextending the elbow by trapping the arm "
            "between the legs with the hips as the fulcrum - is the "
            "signature submission of the Brazilian game and the most "
            "famous finish in vale tudo history. From the mount, when the "
            "bottom fighter pushes to escape, his arm extends - and the "
            "top fighter swings a leg over the head, falls back, and "
            "breaks the arm straight over the hips. The leverage is "
            "enormous: the whole posterior chain bridges against the "
            "small joint of the elbow, which is why the armbar is applied "
            "with exquisite slowness in training and finished the instant "
            "the partner taps. The old vale tudo fighters ended challenge "
            "matches with this technique in seconds; the modern student "
            "learns it as the crown of the compounded ladder, drilled "
            "thousands of times at zero resistance before it is ever "
            "applied live."
        ),
        "how_it_works": (
            "Apply the armbar from mount in seven steps. Step one: from "
            "the high mount, wait for the push - when he extends an arm "
            "to push your chest or bridge, that arm is the target. Step "
            "two: trap the arm tight to your chest with both hands, "
            "controlling the wrist. Step three: swing the leg on the "
            "target-arm side over his head in a wide arc, keeping the "
            "trapped arm pinned to your chest through the whole swing - "
            "losing the arm during the swing loses the submission. Step "
            "four: fall back to the mat, bringing him slightly toward you "
            "as you go, and clamp your knees tight around his shoulder "
            "and head - knees pinched, his thumb pointing to the sky. "
            "Step five: bridge your hips upward slowly while pulling his "
            "wrist down toward your chest - the elbow straightens over "
            "your hips, which are the fulcrum. Step six: the instant your "
            "partner taps - hand on you, hand on the mat, or verbally - "
            "release completely and check on him. Step seven: drill the "
            "entry and the swing at zero resistance for hundreds of reps "
            "before ever applying pressure; the finish is practiced as "
            "position-only, stopping at the clamped knees, until control "
            "is absolute."
        ),
        "key_points": [
            "The armbar is the signature submission of the Brazilian game: trap the arm, swing the leg over the head, hips as the fulcrum.",
            "The push is the trigger - from the high mount, the extended pushing arm is the opening; never chase an arm that is not offered.",
            "Keep the trapped arm pinned to your chest through the entire leg swing; losing it mid-swing loses everything.",
            "Knees clamp tight around shoulder and head with the thumb to the sky - the clamp is the lock, the bridge is the finish.",
            "Release the instant the partner taps and drill the finish at zero resistance for hundreds of reps before applying pressure.",
        ],
        "requirements": [
            "The mount record solid, especially the high mount and riding the bridge.",
            "A trusted partner and a clear tap protocol agreed before any armbar drilling.",
            "Hundreds of zero-resistance entry reps before any pressure is applied.",
            "The wrist controlled with both hands through the swing - one-handed control drops the arm.",
            "Immediate release on the tap, every time, no exceptions - this is the sport's most sacred rule.",
        ],
        "standards": [
            "Pressure is applied slowly with the hips, never yanked; the finish is a bridge, not a jerk.",
            "The partner's tap - physical or verbal - ends the technique instantly; continuing past the tap is expulsion-level misconduct.",
            "Live application waits until the zero-resistance entry is clean for hundreds of reps.",
        ],
        "citations": [CIT_GRACIE, CIT_PENN],
        "sig_lens": (
            "The Signature read: the armbar is the Signature lever of "
            "levers - the covenant of the extended arm. It swears that "
            "leverage honestly applied needs no cruelty: trap truly, "
            "swing cleanly, and release the instant honor - the tap - "
            "is given."
        ),
    },
    {
        "key": "vt_rnc",
        "name": "The Rear Naked Choke in Vale Tudo",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The rear naked choke - mata-leao, the lion killer, in "
            "Portuguese - is the definitive back-control submission of "
            "vale tudo: from behind the opponent, one arm encircles the "
            "neck, the other locks the figure-four, and the squeeze "
            "compresses the carotid arteries until consciousness fades. "
            "It is called naked because it needs no gi, and it is the "
            "highest-percentage submission in the sport's history - more "
            "fights have ended to the mata-leao than to any other choke. "
            "The old challenge fighters prized it because the back is the "
            "position with no defense: the opponent cannot see the "
            "attack, cannot strike effectively, and every escape attempt "
            "tightens the hold. In training it is applied with total "
            "control and released the instant the partner taps or goes "
            "limp - the choke is practiced as a blood choke, squeezing "
            "the sides of the neck, never crushing the windpipe."
        ),
        "how_it_works": (
            "Apply the rear naked choke in seven steps. Step one: secure "
            "the back with both hooks in - heels inside his thighs - and "
            "one arm controlling his upper body, keeping your chest tight "
            "to his back. Step two: with your choking arm, reach under "
            "his chin - if the chin is tucked, use the hand to lift it "
            "patiently rather than forcing. Step three: encircle the neck "
            "so your elbow sits under his chin and your hand reaches past "
            "his far shoulder. Step four: lock the figure-four - your free "
            "hand goes behind his head and your choking hand grips your "
            "own bicep, the free hand pressing on the back of his head. "
            "Step five: expand the chest and squeeze the elbows together, "
            "compressing the sides of the neck - the pressure goes to the "
            "carotids, not the windpipe. Step six: hold with steady "
            "pressure; the trained partner taps within seconds - release "
            "instantly and completely. Step seven: if he goes limp before "
            "tapping, release immediately, lay him on his side, and let "
            "him recover - then discuss what happened, because every "
            "blackout in training is a lesson about tap timing. Drill: "
            "entries and locks at zero pressure for hundreds of reps; the "
            "squeeze is only ever finished in supervised sparring."
        ),
        "key_points": [
            "The mata-leao is the lion killer: the highest-percentage submission in vale tudo history, applied from the back where there is no defense.",
            "It is a blood choke compressing the carotid arteries on the sides of the neck - never a windpipe crush.",
            "The figure-four lock - choking hand to own bicep, free hand behind the head - is the structure; the chest expansion is the squeeze.",
            "Both hooks in and chest-to-back control come first; the choke without back control is a gift the opponent escapes.",
            "Release instantly on the tap or on any limpness - every blackout in training is a lesson about tapping earlier.",
        ],
        "requirements": [
            "Back control fundamentals: both hooks in and chest-to-back connection before any choke is attempted.",
            "A trusted partner, a clear tap protocol, and a coach supervising all finishing reps.",
            "The chin-lift done patiently with the hand, never forced with the forearm.",
            "Hundreds of zero-pressure entry-and-lock reps before the squeeze is ever finished.",
            "The recovery protocol known cold: release, side-lying position, and a calm debrief after any blackout.",
        ],
        "standards": [
            "Pressure goes to the sides of the neck, never the front of the throat; windpipe crushing is a fault.",
            "The tap or any limpness ends the technique instantly - no exceptions, no finishing the rep.",
            "The squeeze is only finished in supervised sparring; all drilling is entries and locks at zero pressure.",
        ],
        "citations": [CIT_GRACIE, CIT_PENN],
        "sig_lens": (
            "The Signature read: the mata-leao is the Signature silence "
            "- the covenant of the back taken. It swears that the most "
            "decisive weapon needs the least violence: encircle truly, "
            "squeeze steadily, and honor the tap as the highest law of "
            "the armory."
        ),
    },
    {
        "key": "vt_guillotine",
        "name": "The Guillotine Choke in Vale Tudo",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The guillotine choke - guilhotina - is the front headlock "
            "submission that punishes every sloppy takedown: when the "
            "opponent shoots with his head down or leaves his neck "
            "exposed in the clinch, the defender encircles the neck with "
            "one arm, locks the grip, and arches back to finish. It is "
            "the sprawl's best friend and the double leg's nightmare - "
            "the old vale tudo strikers ended wrestlers' nights with it "
            "when the sprawl alone was not enough. The guillotine works "
            "standing, in the guard, and on the ground; the standing "
            "version, finished with a high elbow and an arched back, is "
            "the classic. Like all chokes it is a blood choke on the "
            "carotids, applied with control and released on the tap - "
            "and its great lesson is defensive: the record teaches the "
            "head position that avoids it as carefully as the attack "
            "itself."
        ),
        "how_it_works": (
            "Apply the standing guillotine in seven steps. Step one: as "
            "the opponent shoots head-down or dips in the clinch, sprawl "
            "your hips back first - the guillotine without the sprawl "
            "gets you taken down holding a neck. Step two: encircle his "
            "neck with your choking arm, reaching deep so your wrist sits "
            "past his throat line and your elbow points to the sky. Step "
            "three: lock the grip - choking hand to your own chest or "
            "wrist, free hand reinforcing - keeping the encircling arm's "
            "elbow high, which is the whole mechanical secret. Step four: "
            "arch your back and extend upward, pulling his head into your "
            "ribs as your hips drive back - the finish is the arch, not "
            "an arm squeeze. Step five: if he is still defending, sit "
            "back into the guard, keeping the high elbow, and finish "
            "from your back with the same arch. Step six: release "
            "instantly on the tap. Step seven: drill the defensive lesson "
            "equally - when you shoot, keep the head tight to the hip "
            "and never reach head-inside, because the guillotine is "
            "always waiting for the careless shot. Drill: ten sprawl-to-"
            "guillotine entries per side per round, finishing only in "
            "supervised sparring."
        ),
        "key_points": [
            "The guilhotina punishes the sloppy shot: encircle the exposed neck, lock the high-elbow grip, arch back to finish.",
            "Sprawl first, choke second - the guillotine without the sprawl is a takedown you paid to attempt.",
            "The high elbow is the mechanical secret; the finish is the back arch driving the hips away, not an arm squeeze.",
            "It works standing, in the guard, and grounded - if the standing finish stalls, sit back and finish from the guard.",
            "The record's great defensive lesson: shoot head-tight to the hip, because the guillotine waits for every careless shot.",
        ],
        "requirements": [
            "The sprawl as reflex and the double leg's head position understood - the guillotine lives in the space between them.",
            "A partner shooting at controlled speed for entries; finishing only in supervised sparring.",
            "The deep encirclement drilled slowly - a shallow arm around the head finishes nothing and wastes the sprawl.",
            "The high-elbow grip locked before the arch begins; arching without the lock is just bending backward.",
            "The tap protocol sacred: release instantly, every time.",
        ],
        "standards": [
            "The sprawl precedes the choke on every standing entry - no sprawl, no guillotine.",
            "Pressure is a blood choke on the carotids with the high elbow; cranking the neck is a fault.",
            "Defensive head position - head tight to the hip on every shot - is drilled as part of this record.",
        ],
        "citations": [CIT_GRACIE, CIT_PENN],
        "sig_lens": (
            "The Signature read: the guillotine is the Signature toll - "
            "the covenant of the defended gate. It swears that every "
            "careless entry pays its price, and that the honest sprawl "
            "collects what the sloppy shot owes."
        ),
    },
])
ENTRIES.extend([
    {
        "key": "vt_triangle",
        "name": "The Triangle Choke from Guard in Vale Tudo",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The triangle choke - triangulo - is the guard's masterpiece: "
            "the legs form a figure-four around the opponent's neck and "
            "one arm, and the squeeze compresses the carotids while the "
            "trapped shoulder does half the work. It is the submission "
            "that made the highlight reels of vale tudo - the bottom "
            "fighter, apparently losing, suddenly locking the triangle "
            "and finishing the fight from his back. The triangle punishes "
            "the two great errors of the top game: leaving one arm inside "
            "the guard while posturing up, and stacking forward without "
            "controlling the hips. Setting it up is the advanced skill - "
            "the entries come from the failed armbar, the overhook "
            "battle, and the opponent's own pass attempt - while the "
            "finish is pure mechanics: angle out, lock the figure-four, "
            "pull the head down, and squeeze with the whole lower body."
        ),
        "how_it_works": (
            "Lock the triangle in seven steps. Step one: from the closed "
            "guard, wait for the error - he postures up with one arm "
            "inside your guard, or he drives forward to pass. Step two: "
            "control the trapped arm across your body, pulling it between "
            "your legs so his shoulder, not just his arm, is inside your "
            "triangle. Step three: swing one leg over his shoulder and "
            "lock the figure-four - ankle behind the opposite knee - with "
            "his neck and one arm inside the lock. Step four: angle your "
            "body ninety degrees to the side, so you face his trapped "
            "shoulder rather than his chest; the angle is the choke, and "
            "the flat triangle is the beginner's graveyard. Step five: "
            "pull his head down with your hands clasped behind it while "
            "raising your hips slightly - the head-down plus hips-up "
            "closes the vise. Step six: squeeze by driving the locked "
            "legs together and bridging the hips, compressing the carotids "
            "between your thigh and his own shoulder. Step seven: release "
            "on the tap, instantly. Drill: the entry-to-lock at zero "
            "pressure for hundreds of reps; the angle-out practiced as a "
            "separate movement until the ninety degrees is automatic."
        ),
        "key_points": [
            "The triangulo is the guard's masterpiece: legs in a figure-four around neck and one arm, the trapped shoulder doing half the choking.",
            "It punishes the top game's two great errors: the arm left inside during the posture-up, and the forward stack without hip control.",
            "The angle is the choke: swing ninety degrees to face the trapped shoulder, because the flat triangle finishes nothing.",
            "Pull the head down and raise the hips to close the vise; the squeeze is the whole lower body, not the calves alone.",
            "Entries come from his errors and your other attacks - the failed armbar is the classic triangle setup.",
        ],
        "requirements": [
            "The closed guard and armbar records solid - the triangle is set up by the threats they create.",
            "A partner making the classic errors at controlled speed: the posture-up with the arm inside.",
            "The figure-four leg lock drilled until the ankle finds the knee without looking.",
            "The ninety-degree angle-out drilled as a separate movement before any finishing.",
            "The tap protocol absolute: the triangle closes fast, so the release must be faster.",
        ],
        "standards": [
            "The body angles ninety degrees before the squeeze begins - flat triangles are corrected to the angle.",
            "The trapped arm is controlled across the body with the shoulder inside the lock, not just the wrist.",
            "All drilling is entry-to-lock at zero pressure; the squeeze is finished only in supervised sparring.",
        ],
        "citations": [CIT_GRACIE, CIT_PENN],
        "sig_lens": (
            "The Signature read: the triangle is the Signature geometry "
            "- the covenant of the angle. It swears that position is "
            "mathematics: ninety degrees honestly taken, the figure-four "
            "honestly locked, and the vise closes by law, not by force."
        ),
    },
    {
        "key": "vt_kimura",
        "name": "The Kimura from Side Control in Vale Tudo",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The kimura - named for Masahiko Kimura, the judoka who broke "
            "Helio Gracie's arm with it in their famous 1951 bout at the "
            "Maracana stadium - is the figure-four shoulder lock that "
            "attacks the shoulder joint by rotating the arm behind the "
            "back. In vale tudo it is the great punisher of the push: "
            "from side control, when the bottom fighter pushes against "
            "the chest to escape, his arm extends into the trap, and the "
            "top fighter captures the wrist, threads the figure-four, "
            "and rotates. The leverage attacks the shoulder's natural "
            "range - which is why the kimura is finished with slow, "
            "patient rotation in training and the partner taps to the "
            "pressure long before the joint is threatened. It is also a "
            "position machine: the threat of the kimura makes opponents "
            "give up the back, the armbar, and the mount escape, so the "
            "advanced fighter uses it as much for what it creates as for "
            "what it finishes."
        ),
        "how_it_works": (
            "Apply the kimura from side control in seven steps. Step one: "
            "from side control with the underhook, wait for the push - "
            "when he pushes your chest or hip with his far arm, that arm "
            "is the target. Step two: capture his wrist with your near "
            "hand and sit back slightly, bringing his arm across his own "
            "body. Step three: thread your far arm under his captured arm "
            "and grip your own wrist, forming the figure-four - your "
            "hands make a closed circuit around his arm. Step four: step "
            "over his head with your near leg or sit through to north-"
            "south, keeping the figure-four tight through the movement - "
            "the transition is where kimuras are lost. Step five: with "
            "his arm bent at ninety degrees behind his back, rotate his "
            "hand slowly toward his own head, keeping his elbow pinned to "
            "your body as the fulcrum. Step six: apply the rotation with "
            "the whole torso, slowly and patiently - the shoulder gives "
            "long before it breaks, and the tap comes early. Step seven: "
            "release instantly on the tap. Drill: the capture-to-figure-"
            "four at zero resistance for hundreds of reps; the rotation "
            "practiced as a slow six-count, never a yank."
        ),
        "key_points": [
            "The kimura is the figure-four shoulder lock named for Masahiko Kimura's 1951 victory over Helio Gracie: capture the wrist, thread the lock, rotate the arm behind the back.",
            "It punishes the push - the extended escaping arm from side control walks into the trap.",
            "The figure-four is a closed circuit: your hands locked around his arm, his elbow pinned to your body as the fulcrum.",
            "Finish with slow whole-torso rotation on a six-count; the shoulder taps long before it is threatened - yanking is forbidden.",
            "It is a position machine: the kimura threat creates the back take, the armbar, and the mount - use it for what it creates.",
        ],
        "requirements": [
            "The side control record solid, especially the underhook and the crossface.",
            "A partner pushing to escape at controlled speed - the kimura feeds on the push.",
            "The figure-four grip drilled until the hands find each other without looking.",
            "The slow six-count rotation practiced with a partner giving early verbal feedback.",
            "The release reflex: instant on the tap, drilled as part of every rep.",
        ],
        "standards": [
            "The rotation is applied slowly with the torso on a six-count - any yank is an immediate stop.",
            "The partner taps to early pressure; the joint is never taken near its limit in training.",
            "The figure-four stays closed through all transitions; an opened grip means the rep restarts.",
        ],
        "citations": [CIT_GRACIE, CIT_GENTRY],
        "sig_lens": (
            "The Signature read: the kimura is the Signature history - "
            "the covenant named for the man who proved the lock. It "
            "swears patience over violence: the slow rotation, the early "
            "tap honored, and the shoulder respected as a joint, not a "
            "target."
        ),
    },
    {
        "key": "vt_sweeps",
        "name": "Scissor and Hip-Bump Sweeps in Vale Tudo",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Sweeps - raspagens - are the guard player's reversals: using "
            "leverage and timing to topple the top fighter and take his "
            "place, moving from bottom to top in a single motion. In vale "
            "tudo the sweep is worth double, because the top position is "
            "where strikes live - reversing the position reverses the "
            "fight. The two fundamental sweeps are the scissor sweep, "
            "where the legs scissor across the opponent's base while the "
            "arms pull him over, and the hip-bump sweep, where the guard "
            "player sits up explosively into the opponent's chest when he "
            "postures up. Both obey the sweep law: off-balance first, "
            "then technique. The sweep attempted on a balanced opponent "
            "is a gift of position; the sweep timed to his posture-up or "
            "his pass attempt is a reversal. The advanced guard chains "
            "them: threaten the hip bump, and when he posts his hand to "
            "stop it, take the scissor."
        ),
        "how_it_works": (
            "Hit the scissor sweep in six steps. Step one: from the "
            "closed guard, control one of his arms across your body - "
            "grip the sleeve or wrist and pin it to your chest. Step two: "
            "open the guard and place your near shin across his belly as "
            "a barrier while your other leg scissors back behind his far "
            "knee. Step three: load his weight onto the trapped side by "
            "pulling his controlled arm and shifting your hips - feel him "
            "get heavy on the scissor side. Step four: scissor the legs "
            "violently - top leg chops down across the belly, bottom leg "
            "kicks back behind the knee - while pulling his arm across "
            "and driving with your hips. Step five: follow him over and "
            "land in the mount, keeping the arm trapped for the armbar "
            "threat. Step six: chain it - drill the hip-bump as the "
            "companion: when he postures up to stop your attacks, sit up "
            "into his chest, overhook his arm, and roll him over your "
            "shoulder. Drill: ten scissor sweeps and ten hip bumps per "
            "side per round, then live chains - bump threatened, scissor "
            "taken - for three rounds."
        ),
        "key_points": [
            "Raspagens reverse the fight: the guard player topples the top fighter and takes his place, and in vale tudo the top is where strikes live.",
            "The scissor sweep chops the base from under him while the arms pull him over; the hip bump explodes upward when he postures.",
            "Off-balance first, then technique: the sweep timed to his posture-up or pass attempt is a reversal, the sweep on a balanced man is a gift.",
            "Chain them: threaten the hip bump, and when he posts his hand to stop it, take the scissor sweep he just opened.",
            "Follow every sweep into the mount with the arm still trapped - the sweep that lands in a scramble is half a sweep.",
        ],
        "requirements": [
            "The closed guard and hip escape records solid - sweeps are guard attacks built on guard retention.",
            "A partner reacting at controlled speed: posturing up, attempting passes, giving the timing cues.",
            "The arm-across control drilled first; sweeping without the arm trapped is pushing a balanced man.",
            "Both sweeps drilled on both sides - one-sided sweepers get passed to their weak side.",
            "The mount landing practiced as part of every rep, not as an afterthought.",
        ],
        "standards": [
            "The opponent is off-balanced onto the sweep side before the scissor fires - balanced-man sweeps are corrected.",
            "The trapped arm stays controlled through the entire sweep and the landing.",
            "Every sweep rep ends mounted with the armbar threat alive; scramble landings are incomplete reps.",
        ],
        "citations": [CIT_GRACIE, CIT_PENN],
        "sig_lens": (
            "The Signature read: the sweep is the Signature reversal - "
            "the covenant that the bottom is a position, not a verdict. "
            "It swears timing over strength: off-balance him honestly, "
            "scissor cleanly, and rise to the mount you earned."
        ),
    },
    {
        "key": "vt_flyingknee",
        "name": "The Flying Knee: Joelhada Voadora",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The flying knee - joelhada voadora - is the most spectacular "
            "technique in the vale tudo arsenal: the fighter launches "
            "himself into the air and drives the knee into the target, "
            "adding the body's falling weight to the hip thrust. The old "
            "Brazilian strikers threw it as the ultimate distance-closer, "
            "covering two meters in a single explosive jump, and the "
            "highlight reels of the 1990s vale tudo scene are full of "
            "fights ended by it. It is an advanced technique for three "
            "reasons: it commits the whole body to the air, leaving no "
            "base to defend the takedown if it misses; it demands perfect "
            "timing, because the target must be there when the knee "
            "arrives; and it is thrown at full power or not at all. The "
            "record teaches it as a bag and pad technique first, a "
            "timed counter second, and a sparring weapon only for advanced "
            "students under a coach's eye."
        ),
        "how_it_works": (
            "Throw the flying knee in six steps. Step one: from outside "
            "range, read the moment - the opponent stationary, covering "
            "up, or stepping in predictably. Step two: take a short "
            "stutter step with the lead foot to load the spring. Step "
            "three: explode upward and forward off the rear leg, driving "
            "the rear knee up violently while the arms swing down and "
            "back for lift - the whole body leaves the ground as one "
            "coiled spring. Step four: at the apex, thrust the hips "
            "forward into the knee exactly as in the standing clinch "
            "knee, toes pointed down, aiming the point of the knee at the "
            "chin, chest, or body. Step five: land on the kicking-side "
            "foot first, then the other, back into stance with hands up - "
            "the landing is part of the technique, and falling out of it "
            "is how takedowns happen. Step six: drill it on the heavy bag "
            "held at head height - ten per side per round for three "
            "rounds - before ever timing it on pads with a partner, and "
            "only attempt it in sparring when the coach approves the "
            "timing. Misses are drilled too: land balanced and reset, "
            "because the missed flying knee is the takedown's best friend."
        ),
        "key_points": [
            "The joelhada voadora adds the body's airborne weight to the knee: the ultimate distance-closer and the sport's most spectacular strike.",
            "It is advanced because it commits everything: miss, and there is no base left to defend the takedown.",
            "The spring is one coiled motion - stutter step, rear-leg explosion, knee driven with the hip thrust at the apex.",
            "The landing is part of the technique: land balanced in stance with hands up, or the miss becomes a takedown.",
            "Bag first, timed pads second, sparring only with the coach's approval - the flying knee is earned in stages.",
        ],
        "requirements": [
            "The standing knee record clean - the flying knee is the same mechanics with a launch added.",
            "Explosive leg strength and balance: single-leg hops and box jumps as conditioning prerequisites.",
            "A heavy bag at head height for all early reps - never learn the launch on a partner.",
            "The balanced landing drilled as its own skill before any timing work.",
            "Coach approval before any sparring attempt - the flying knee at sparring speed is an advanced privilege.",
        ],
        "standards": [
            "The hips thrust into the knee at the apex exactly as in the standing knee - a leg lifted without the thrust is corrected.",
            "Every rep ends in a balanced stance with hands up; falling out of the landing is a failed rep.",
            "The miss recovery - land balanced and reset - is drilled as deliberately as the strike.",
        ],
        "citations": [CIT_KRAUSS, CIT_PENN],
        "sig_lens": (
            "The Signature read: the flying knee is the Signature flight "
            "- the covenant of total commitment. It swears that when the "
            "moment is truly read, the fighter spends everything at once: "
            "the spring, the spear, and the balanced landing of a man who "
            "meant it."
        ),
    },
    {
        "key": "vt_subchains",
        "name": "Chaining Submissions: Armbar to Triangle to Omoplata",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Chaining submissions is the advanced art of never accepting "
            "a failed attack: when the opponent defends the armbar, his "
            "defense opens the triangle; when he defends the triangle, "
            "his posture opens the omoplata shoulder lock. The old "
            "Brazilian masters called this the submission system - not a "
            "collection of tricks but a net, where every escape route is "
            "another trap. The mechanics are transitional: the fighter "
            "holds the attacking structure loosely enough to flow, keeps "
            "the hips mobile, and reads the defense as a gift rather than "
            "a failure. The classic chain runs armbar to triangle to "
            "omoplata from the guard and mount, but the principle is "
            "universal: attack, read the defense, take the opening the "
            "defense created. Chaining is drilled as flow first - "
            "continuous movement with a cooperative partner - and only "
            "later as live hunting, because the transitions must be "
            "smooth before they can be fast."
        ),
        "how_it_works": (
            "Drill the guard chain in six steps. Step one: from the "
            "closed guard, attack the armbar on his extended arm - "
            "trap, swing the leg, clamp. Step two: when he pulls the arm "
            "back and postures up to defend, do not chase it - instead, "
            "swing the leg over his shoulder into the triangle, using his "
            "upward defense as your entry. Step three: when he stacks "
            "forward to defend the triangle, angle out and swing the leg "
            "over his back into the omoplata, trapping his arm behind him "
            "with your legs. Step four: finish the omoplata by sitting up "
            "and rotating his arm behind his back with your hips - or, "
            "when he rolls to escape it, follow the roll and take the "
            "armbar on the far side. Step five: the rule of the chain - "
            "never force a defended submission; the moment he commits to "
            "the defense, you are already moving to the next attack. Step "
            "six: drill as flow rolling - ten minutes of continuous "
            "attack-transition-attack with a cooperative partner, no "
            "finishes, only transitions - until the chain runs without "
            "pauses. Then, and only then, add the finishes in supervised "
            "sparring."
        ),
        "key_points": [
            "Chaining is the submission system: the defended armbar opens the triangle, the defended triangle opens the omoplata - every defense is another trap.",
            "Never force a defended submission: the moment he commits to the defense, you are already moving to the next attack.",
            "The transitions are the technique: hold the attacking structure loosely, keep the hips mobile, and flow.",
            "Drill as flow first - ten minutes of continuous attack-transition-attack with no finishes - until the chain runs without pauses.",
            "The principle is universal beyond the classic chain: attack, read the defense, take the opening the defense created.",
        ],
        "requirements": [
            "The armbar, triangle, and kimura/omoplata mechanics each solid individually - chains are built from clean links.",
            "A cooperative partner for flow drilling; chaining cannot be learned against full resistance first.",
            "Ten-minute flow rounds with no finishes, focused purely on transitions.",
            "The omoplata entry drilled separately before it is chained - it is the least familiar link.",
            "Supervised sparring for all finishing; flow drilling stays finish-free.",
        ],
        "standards": [
            "Transitions flow without pauses or strength battles - a stuck chain is reset to flow speed.",
            "No defended submission is forced; forcing is the fault the whole record exists to cure.",
            "The chain is drilled in both directions - armbar to triangle and triangle to armbar - so no link is one-way.",
        ],
        "citations": [CIT_GRACIE, CIT_PENN],
        "sig_lens": (
            "The Signature read: the chain is the Signature net - the "
            "covenant of the unaccepted failure. It swears that no "
            "defense is an ending: every door he closes is a door you "
            "built, and the net tightens with his own struggling."
        ),
    },
    {
        "key": "vt_grounddef",
        "name": "Bottom Survival: Defending Ground Strikes",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Bottom survival is the vale tudo skill nobody wants to need "
            "and everybody must have: defending yourself from strikes "
            "while trapped underneath a dominant opponent. The old "
            "challenge matches were often won here - the top fighter "
            "raining punches while the bottom fighter survived, escaped, "
            "or reversed. Survival has a strict hierarchy: first, protect "
            "the head - tuck the chin, keep the hands high, use the "
            "forearms as a shield; second, control the distance - frames "
            "on the hips and shoulders keep the striker from posturing up "
            "for power; third, never stay flat - shrimp to a side, "
            "because the flat back is the anvil the strikes are forged "
            "on; fourth, escape in layers - hip escape to guard, bridge "
            "to create space, technical stand-up when the distance opens. "
            "The record is taught with full safety gear and controlled "
            "contact only, because the only way to learn survival is to "
            "practice it against honest, measured pressure."
        ),
        "how_it_works": (
            "Survive from the bottom in six steps. Step one: the moment "
            "you are mounted or side-controlled, shell up - forearms "
            "tight to the face, chin tucked, elbows in - making the head "
            "a small, hard target. Step two: get to your side with a "
            "shrimp - never accept the flat back, which lets him posture "
            "up for full-power strikes. Step three: establish frames - "
            "one forearm across his hip, one hand on his shoulder or "
            "bicep - keeping his weight off your chest and his posture "
            "broken. Step four: when he raises up to strike, that is "
            "your moment - the space he makes for power is the space you "
            "use to shrimp deeper and insert the knee, recovering the "
            "half guard. Step five: from the half guard, get the underhook "
            "and come up to your side, then technical stand-up - hand "
            "posted behind, far leg back, standing without turning away. "
            "Step six: drill it as positional sparring - partner on top "
            "with light, controlled strikes through full safety gear, you "
            "surviving and escaping, three two-minute rounds. The gear "
            "and the control are non-negotiable; survival is learned "
            "against honest pressure, never against punishment."
        ),
        "key_points": [
            "Bottom survival has a strict hierarchy: protect the head, control the distance with frames, never stay flat, escape in layers.",
            "The shell - forearms to the face, chin tucked, elbows in - makes the head a small, hard target.",
            "Shrimp to the side immediately: the flat back is the anvil that ground strikes are forged on.",
            "His power is your opening: when he postures up to strike, the space he makes is the space you escape through.",
            "Escape in layers - shell, shrimp, frames, knee in, half guard, underhook, technical stand-up - never in one desperate burst.",
        ],
        "requirements": [
            "Full safety gear - headgear, mouthguard, gloves - and a coach supervising all strike-survival drilling.",
            "The hip escape and guard records solid, since every escape route runs through them.",
            "A partner giving honest, measured, controlled pressure - never punishment disguised as drilling.",
            "The technical stand-up drilled solo until it is clean before it is used under pressure.",
            "The tap and the stop word respected instantly by both partners.",
        ],
        "standards": [
            "All strike-survival drilling uses controlled contact with full gear and coaching supervision - full-power ground strikes are never a drill.",
            "The flat back is corrected on sight: every survival rep starts with the shrimp to the side.",
            "Escapes are layered and patient; explosive bridging without frames is corrected to the frame-first method.",
        ],
        "citations": [CIT_KRAUSS, CIT_PENN],
        "sig_lens": (
            "The Signature read: survival is the Signature patience - "
            "the covenant of the unbroken. It swears that the worst "
            "position is still a position: shell the head, frame the "
            "distance, and escape in layers, because the storm always "
            "spends itself against the prepared."
        ),
    },
    {
        "key": "vt_heritage",
        "name": "Vale Tudo Heritage Techniques: History of the Old Rules",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "This record is history, taught as history: the techniques of "
            "the old vale tudo rules that the modern sport has banned. "
            "In the Brazilian challenge era and the early International "
            "Vale Tudo Championship, bouts ran with minimal rules - no "
            "biting, no eye-gouging, no groin strikes - and that was "
            "nearly the whole list. Headbutts (cabecadas) were legal and "
            "decisive; knees and kicks to the head of a grounded opponent, "
            "stomps, and soccer kicks were part of the game; bouts could "
            "run without rounds or time limits until somebody quit. The "
            "modern Unified Rules of MMA ban all of it: headbutts, "
            "12-to-6 elbows, strikes to the spine and back of the head, "
            "kicks and knees to a grounded opponent, stomps, and more - "
            "thirty-one fouls in the current unified list. This record "
            "exists so the student understands what the old fighters "
            "actually did, why the rules changed, and why none of these "
            "techniques are drilled, sparred, or used: they are heritage, "
            "not curriculum."
        ),
        "how_it_works": (
            "Study the heritage in five steps. Step one: learn the old "
            "rule sets - the challenge-match customs of the 1920s to "
            "1960s, the IVC rules of 1997 that allowed headbutts and "
            "limited rounds, and the Pride FC rules that permitted knees "
            "and kicks to a downed opponent. Step two: study the "
            "techniques as film and text only - the cabecada driven from "
            "the clinch, the soccer kick and stomp against the grounded "
            "fighter - understanding their mechanics without ever "
            "practicing them on a partner. Step three: learn the unified "
            "rules' thirty-one fouls by heart, because the modern vale "
            "tudo student competes and spars under them. Step four: "
            "understand why the rules changed - the headbutt's cuts, the "
            "soccer kick's trauma, the need for the sport to be "
            "sanctionable and survivable. Step five: carry the heritage "
            "as knowledge, not as technique - the old fighters' "
            "toughness is honored by training hard within the modern "
            "rules, not by reviving what the rules buried. Test: name "
            "the banned techniques and the unified fouls that ban them; "
            "the student who cannot is not ready to represent the art."
        ),
        "key_points": [
            "Heritage, not curriculum: the old-rules techniques - headbutts, soccer kicks, stomps, knees to the grounded head - are studied as history, never drilled or used.",
            "The old game ran on minimal rules: no biting, no eye-gouging, no groin strikes, and nearly everything else permitted.",
            "The modern Unified Rules ban all of it in a thirty-one-foul list the student must know by heart.",
            "Study the techniques as film and text only: understand the mechanics, never practice them on a partner.",
            "Honor the old fighters' toughness by training hard within the modern rules - that is how heritage is carried.",
        ],
        "requirements": [
            "The full ladder before this record - heritage is the advanced student's context, not the beginner's temptation.",
            "Study materials: films and texts of the old bouts, discussed with a coach who knows the history.",
            "The thirty-one unified fouls memorized - the modern rules are the student's actual rulebook.",
            "A clear gym policy: banned techniques are never drilled, never sparred, never used.",
            "The maturity to treat this record as knowledge: understanding without practicing.",
        ],
        "standards": [
            "No banned technique is ever drilled on a partner or a bag as a technique - this record is study-only.",
            "The student can name the banned techniques and the unified fouls covering them before advancing.",
            "All sparring and competition preparation follows the Unified Rules foul list without exception.",
        ],
        "citations": [CIT_GENTRY, CIT_KRAUSS, CIT_SNOWDEN],
        "sig_lens": (
            "The Signature read: heritage is the Signature memory - the "
            "covenant with the old fighters. It swears to remember what "
            "they endured without repeating what the rules buried: honor "
            "the toughness, keep the knowledge, and fight the modern "
            "fight."
        ),
    },
    {
        "key": "vt_combos",
        "name": "Vale Tudo Combinations: Striking into the Takedown",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Combinations are the advanced striker's language: punches, "
            "kicks, knees, and takedowns strung together so each "
            "technique hides the next. In vale tudo the combinations have "
            "a special job beyond damage - they blend the ranges, so the "
            "opponent defending punches walks into the takedown, and the "
            "opponent defending the takedown eats the knee. The classic "
            "vale tudo combination is the strike-to-shot: jab, cross, "
            "level change, double leg - the punches occupy the hands and "
            "eyes while the shot happens underneath. The advanced "
            "versions add the low kick as the bridge - jab, cross, low "
            "kick, cross, shot - and the clinch entry as the finisher. "
            "Combinations are drilled in layers: first the hands alone, "
            "then hands with the kick, then the full blend with the "
            "takedown on a cooperative partner, and only then at speed. "
            "The rule of combinations is that every strike must earn its "
            "place: no wasted motion, no telegraphed rhythm, every punch "
            "setting up what follows."
        ),
        "how_it_works": (
            "Build the jab-cross-shot in six steps. Step one: drill the "
            "jab-cross alone on the bag until the two punches are one "
            "motion - three rounds, counting clean pairs. Step two: add "
            "the level change after the cross - jab, cross, drop the hips "
            "- without shooting, so the level change becomes part of the "
            "rhythm. Step three: add the penetration step on a cooperative "
            "partner - jab, cross, level change, shoot to the body lock "
            "without finishing, ten reps. Step four: add the finish - "
            "drive through to the double leg and land past the guard. "
            "Step five: add the low kick bridge - jab, cross, low kick, "
            "cross, shot - drilling the kick-to-punch transition slowly, "
            "since the stance shift is the hard part. Step six: spar the "
            "combination at controlled speed, with the partner defending "
            "honestly - if he stops the shot, take the data and adjust "
            "the setup, because combinations are hypotheses tested in "
            "sparring. Drill: five three-minute rounds per session, "
            "rotating through three combinations - hands-to-shot, "
            "kick-bridged, and clinch-entry - until each runs without "
            "thought."
        ),
        "key_points": [
            "Vale tudo combinations blend the ranges: the punches hide the takedown, the takedown threat opens the strikes.",
            "The classic is the strike-to-shot - jab, cross, level change, double leg - with the hands occupying the eyes while the shot goes underneath.",
            "Build in layers: hands alone, then the level change, then the shot on a cooperative partner, then the full blend at speed.",
            "Every strike must earn its place: no wasted motion, no telegraphed rhythm, every punch setting up what follows.",
            "Spar combinations as hypotheses: if he stops the shot, take the data and adjust the setup.",
        ],
        "requirements": [
            "The jab, cross, low kick, and double leg each solid individually - combinations multiply clean techniques, not sloppy ones.",
            "A heavy bag for the striking layers and a cooperative partner for the takedown layers.",
            "The level change drilled as part of the punching rhythm before any shooting.",
            "Controlled sparring for testing, with honest defense from the partner.",
            "Three combinations in the rotation per session - depth beats a long list of half-learned blends.",
        ],
        "standards": [
            "The level change follows the last punch without a pause - a visible gap between striking and shooting is corrected.",
            "Every combination ends in a control position or a clean reset; combinations that dissolve into scrambles are rebuilt.",
            "The stance survives every layer - combinations that collapse the stance are slowed down until it holds.",
        ],
        "citations": [CIT_PENN, CIT_KRAUSS],
        "sig_lens": (
            "The Signature read: the combination is the Signature sentence "
            "- the covenant of techniques that speak as one. It swears "
            "that no strike stands alone: each punch is a word, the "
            "takedown is the period, and the fluent fighter writes in "
            "paragraphs."
        ),
    },
    {
        "key": "vt_strategy",
        "name": "Vale Tudo Fight Strategy: Pacing, Rounds, and the Corner",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Fight strategy is the advanced mind of vale tudo: the plan "
            "that turns techniques into victory across rounds. The old "
            "challenge fights had no rounds and no time limits - they "
            "were wars of attrition - but the modern sport runs in "
            "rounds, and the strategist plans for all of them. Strategy "
            "has four pillars. First, pacing: the fighter who spends "
            "everything in round one is a gift to round three - output is "
            "budgeted, with the hardest work saved for the moments that "
            "decide. Second, the game plan: built from the fighter's "
            "strengths against the opponent's weaknesses, with a primary "
            "path and a backup - the striker hunts the knockout early "
            "and the takedown defense late, the grappler survives the "
            "early storm to drown the opponent deep. Third, the corner: "
            "between rounds, one voice, simple instructions, water, and "
            "honest damage assessment - the corner is the fighter's "
            "second brain. Fourth, adaptation: the plan survives first "
            "contact, but the strategist reads the fight as it happens "
            "and adjusts between rounds."
        ),
        "how_it_works": (
            "Build a fight strategy in six steps. Step one: assess "
            "honestly - list your three best weapons and your three worst "
            "habits, because the plan must route around the truth. Step "
            "two: study the opponent - his stance, his favorite "
            "techniques, where he fades - from film or from the first "
            "exchange. Step three: write the game plan in three lines: "
            "what you do in round one, what changes in round two, how you "
            "close in round three - each line naming techniques, not "
            "wishes. Step four: budget the output - decide the strike and "
            "takedown volume per round, holding roughly twenty percent in "
            "reserve for the championship moments. Step five: rehearse "
            "the corner - designate one voice, practice the sixty-second "
            "break with water, ice, and two simple adjustments, because "
            "the corner that panics loses the fighter. Step six: spar "
            "with the plan - five rounds with a partner playing the "
            "opponent's style, corner breaks between, adjusting the plan "
            "each round. The test of strategy is the third round of that "
            "sparring: if the plan is still running when you are tired, "
            "it is a real plan."
        ),
        "key_points": [
            "Strategy turns techniques into victory: pacing, the game plan, the corner, and adaptation across the rounds.",
            "Budget the output: the fighter who spends everything in round one is a gift to round three - hold twenty percent in reserve.",
            "The game plan is three lines - round one, round two, round three - naming techniques, not wishes, with a backup path.",
            "The corner is the second brain: one voice, sixty seconds, water, and two simple adjustments - never panic.",
            "Adaptation is the fourth pillar: read the fight as it happens and adjust the plan between rounds.",
        ],
        "requirements": [
            "The full technique ladder - strategy without techniques is daydreaming.",
            "Honest self-assessment: three best weapons and three worst habits written down.",
            "A coach or cornerman who knows your game and speaks with one voice between rounds.",
            "Five-round sparring with corner breaks to rehearse the plan under fatigue.",
            "Film study or live reads of opponents to build the game plan from evidence.",
        ],
        "standards": [
            "The game plan is written in three lines naming specific techniques before any sparring tests it.",
            "Output is budgeted per round with a stated reserve; empty-tank third rounds are a planning fault.",
            "Corner work is rehearsed: one voice, sixty seconds, two adjustments - chaos between rounds is corrected in training.",
        ],
        "citations": [CIT_SNOWDEN, CIT_KRAUSS],
        "sig_lens": (
            "The Signature read: strategy is the Signature mind - the "
            "covenant of the long fight. It swears to think in rounds, "
            "spend in budgets, and listen to the one true voice in the "
            "corner: the plan is the promise the fighter keeps to "
            "himself."
        ),
    },
    {
        "key": "vt_code",
        "name": "The Vale Tudo Code: Respect, Safety, and Preparation",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The vale tudo code is the ethic that holds the art together: "
            "respect for the partner, safety as the first technique, and "
            "preparation as the daily practice. The old challenge fighters "
            "fought with minimal rules, but the gyms that produced them "
            "ran on strict custom - the tap honored instantly, the "
            "beginner protected, the hard sparring earned. This record is "
            "the capstone of the ladder because it governs everything "
            "below it: the student who has learned thirty-three "
            "techniques and not the code is dangerous, not skilled. The "
            "code has five articles. Respect the tap: release instantly, "
            "every time, no exceptions. Protect the beginner: match "
            "intensity to the least experienced partner. Train the "
            "defense: for every attack learned, learn its escape. Prepare "
            "the body: conditioning, rest, and honest weight management, "
            "because the unprepared fighter endangers himself and his "
            "partner. Represent the art: outside the gym, the vale tudo "
            "student is a citizen first - the techniques are for the mat, "
            "the ring, and self-defense of the gravest kind, never for "
            "the street, the bar, or the ego."
        ),
        "how_it_works": (
            "Live the code in five practices. Practice one: the tap drill "
            "- in every submission rep, the applier releases the instant "
            "the partner taps, and the partners switch roles, until the "
            "release is faster than thought. Practice two: the intensity "
            "ladder - every sparring round is declared light, medium, or "
            "hard before it starts, and either partner can call it down "
            "a level at any time without shame. Practice three: the "
            "defense pairing - for every new attack drilled, drill its "
            "escape in the same session, so no student owns a weapon "
            "without its shield. Practice four: the preparation log - "
            "sleep, sessions, injuries, and weight tracked weekly, "
            "because the code demands the body be ready for what the art "
            "asks. Practice five: the representation rule - discussed "
            "openly in the gym, signed by new students: the art is for "
            "the mat and the ring, and the student who uses it outside "
            "those places answers to the gym and the law. The coach "
            "tests the code the way he tests technique: by watching. The "
            "student who taps late, spars recklessly, or boasts is "
            "corrected or removed - because the code is the art's immune "
            "system."
        ),
        "key_points": [
            "The code is the capstone of the ladder: thirty-three techniques without the ethic is dangerous, not skilled.",
            "Respect the tap: release instantly, every time, no exceptions - the tap is the sport's most sacred rule.",
            "Match intensity to the least experienced partner, and let either partner call any round down a level without shame.",
            "For every attack learned, learn its escape in the same session: no weapon without its shield.",
            "The art is for the mat and the ring: the student represents vale tudo as a citizen first, and answers for any misuse.",
        ],
        "requirements": [
            "The full ladder studied - the code governs the techniques, so it is learned last and practiced always.",
            "A gym culture that enforces the code: coaches who correct late taps and reckless sparring on sight.",
            "The intensity ladder declared before every sparring round: light, medium, or hard, adjustable downward without shame.",
            "The preparation log kept weekly: sleep, sessions, injuries, weight.",
            "The representation rule understood and signed: the art's techniques stay on the mat and in the ring.",
        ],
        "standards": [
            "The tap ends every submission instantly in all drilling and sparring - continuation past the tap is expulsion-level misconduct.",
            "Sparring intensity is declared and mutually adjustable; undeclared hard rounds are a code violation.",
            "Every new attack is paired with its escape in the same session - unpaired weapons are not taught.",
        ],
        "citations": [CIT_GRACIE, CIT_PENN, CIT_SNOWDEN],
        "sig_lens": (
            "The Signature read: the code is the Signature oath itself - "
            "the covenant that contains all covenants. It swears that "
            "power without honor is just violence, and the Signature "
            "fighter is never just violent: tap honored, partner "
            "protected, art represented, always."
        ),
    },
])

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
_ranks = [e["ladder_rank"] for e in ENTRIES]
assert _ranks == sorted(_ranks), "entries not in ladder order"
assert len({e["key"] for e in ENTRIES}) == 34, "duplicate entry keys"
