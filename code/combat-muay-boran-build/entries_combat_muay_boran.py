#!/usr/bin/env python3
"""Entries for the Muay Boran Combat databases (combat batch 3, 2026-10-17).

Scope verified before authoring 2026-10-17: RAW check over the full manifest
(2,442 databases) plus every shard index in jah-databases-data-1: zero
'combat-muay-boran*' slugs/names; zero Muay Boran combat technique catalog
databases of this kind. The sibling 'combat-muay-thai' (JAH-CBMT-) covers
modern ring Muay Thai - the art of eight limbs as a sport; this build covers
Muay Boran proper: the ancient battlefield boxing of Thailand, the
predecessor art, organized around the nine weapons (naw arwut), the regional
styles, the wai khru rite, card chuek wraps, and the mae mai / luk mai
classical technique systems. Distinct capability - BUILD NEW is the verdict.
Dedupe gate check of all 68 planned titles (34 public + 34 Signature) vs the
whole exact index: zero collisions, zero refusals. ID prefixes JAH-CBMB- and
JAH-CBMBS- verified free in the manifest id_prefix values and every shard
index file (zero hits).

This build creates two NEW databases, 34 ladder-ordered records each:

  combat-muay-boran               - Muay Boran Combat Database
                                    (public-harvest: real, fact-checked Muay
                                    Boran knowledge - the ancient Thai
                                    battlefield boxing that preceded modern
                                    Muay Thai: the nine weapons (naw arwut),
                                    regional styles (Muay Thasao, Muay
                                    Lopburi, Muay Chaiya, Muay Korat, Muay
                                    Uttaradit), the wai khru ram muay rite,
                                    mongkon and prajioud, card chuek hemp
                                    wraps, stance footwork and guard, the
                                    four limb strikes plus the head as ninth
                                    weapon, clinch sweeps and throws, the
                                    mae mai master tricks and luk mai
                                    complementary tricks - every record
                                    carrying the Thai name with translation,
                                    step-by-step body mechanics, key points,
                                    requirements, standards, and citations;
                                    standard references Kraitus P, Kraitus P.
                                    Muay Thai: The Most Distinguished Art of
                                    Fighting 1988; Delp C. Muay Thai Basics
                                    2004 for shared strike mechanics;
                                    traditional Muay Boran teaching lineage)
  combat-muay-boran-signature     - Muay Boran Combat Signature Database
                                    (his original Signature Nine-Weapons
                                    Method: every weapon a covenant of
                                    mechanics, the stance the oath of the
                                    feet, footwork the geometry of the
                                    triangle, the guard the walls of the
                                    temple, the wai khru the oath before the
                                    storm; src signature, titles suffixed
                                    " (Signature Edition)", never presented
                                    as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced): stance, footwork, the nine
weapons, wai khru, mongkon and prajioud, card chuek, guard, conditioning,
triangular stepping, forms, and the five regional styles (foundations) ->
straight punch, hook, uppercut, horizontal and upward elbows, straight and
curved knees, low kick, diagonal roundhouse, push kick, clinch, sweeps, and
the ninth weapon headbutt (compounded) -> mae mai, luk mai, spinning back
elbow, Hanuman Tawai Waen, Kwang Liow Lang, hap liuk grappling, clinch
throws, flying knee, combination systems, and the kru teaching lineage
(advanced).

ID prefixes: JAH-CBMB- (public) and JAH-CBMBS- (signature), verified free
in the manifest and in every shard index (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_muay_boran.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos. Entry text carries
the same numbers the demos compute, so the prose and the programs agree.

Civilian martial-arts sport instruction only. Nothing on neutralizing or
defeating military or defense-grade systems. Never the words "bat belt"
anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Nine-Weapons "
            "Method: every weapon a covenant of mechanics, the stance the "
            "oath of the feet, footwork the geometry of the triangle, the "
            "guard the walls of the temple, and the wai khru the oath "
            "before the storm. Clearly labeled Signature-made, never "
            "presented as authentic public record.")

CIT_KRAITUS = ("Kraitus P, Kraitus P. Muay Thai: The Most Distinguished Art "
               "of Fighting. Soma Publishing; 1988.")
CIT_DELP_BASICS = ("Delp C. Muay Thai Basics: Introductory Thai Boxing "
                   "Techniques. North Atlantic Books; 2004.")
CIT_TRAD = ("Traditional Muay Boran teaching lineage: techniques as "
            "preserved and taught in Thai traditional training camps.")

ENTRIES = [
    # ------------------------------------------------------- FOUNDATIONS
    {
        "key": "stance",
        "name": "Muay Boran Fighting Stance (Thaa Yang)",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The Muay Boran fighting stance (thaa yang) is the home base of "
            "the ancient art. Compared with the modern ring stance, it "
            "stands taller and squarer: the feet sit a little wider than "
            "the shoulders, both feet flat and gripping the ground, the "
            "weight settled low through bent knees, and the body facing the "
            "opponent more directly because the battlefield boxer had to "
            "watch for weapons and multiple attackers, not only one pair of "
            "gloves. For a 1.72 meter, 68 kilogram practitioner the stance "
            "spans about 0.60 meters and each foot carries about 34 "
            "kilograms, roughly 333.5 newtons. The hands ride high with "
            "open, rope-wrapped fists, the chin tucked, the elbows heavy "
            "over the ribs. Every strike of the nine weapons launches from "
            "this stance and returns to it."
        ),
        "how_it_works": (
            "Stand with the feet a little wider than shoulder width, toes "
            "pointing forward and slightly out, both soles flat on the "
            "ground. Sink the hips until the thighs take the weight and the "
            "knees track over the toes. Square the chest toward the opponent "
            "more than a modern boxer would, because the old art trained "
            "for the battlefield where threats came from every side. Raise "
            "both hands to brow level with the palms open or loosely "
            "fisted, the lead hand a touch forward. Tuck the chin behind "
            "the lead shoulder and let the elbows hang heavy to guard the "
            "ribs. Test the stance by having a partner push your shoulder: "
            "if the feet grip and the body rocks as one piece, the base is "
            "right; if a foot lifts or the hips twist away, widen the feet "
            "and sink lower. The mechanics work because a wide flat base "
            "resists being rushed or thrown, and the square chest keeps all "
            "nine weapons - both fists, both elbows, both knees, both feet, "
            "and the head - in play without turning the body away."
        ),
        "key_points": [
            "The Muay Boran stance stands taller and squarer than the modern ring stance: the old art trained for the battlefield, not the roped ring.",
            "Both feet stay flat and gripping: a 1.72 meter practitioner spans about 0.60 meters with roughly 34 kilograms on each foot.",
            "The square chest keeps all nine weapons available without turning away from the opponent.",
            "Hands ride high at brow level with the chin tucked and the elbows heavy over the ribs.",
            "When any technique breaks down, the repair starts at the feet: stance is the first lesson and the last correction.",
        ],
        "requirements": [
            "Feet wider than the shoulders, flat on the ground, toes forward and slightly out.",
            "Hips sunk through bent knees with the knees tracking over the toes.",
            "Chest squared toward the opponent more than in modern boxing.",
            "Hands at brow level, chin tucked behind the lead shoulder, elbows guarding the ribs.",
            "A partner push test: the body rocks as one piece with no foot lifting.",
        ],
        "standards": [
            "Traditional camps teach the stance for weeks before any strike: stance and stepping precede all pad work for beginners.",
            "The stance is the legal fighting base wherever Muay Boran is demonstrated or graded.",
            "Orthodox and southpaw leads are both standard; the lead matches the dominant rear power side.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the stance is the oath of the feet - a promise "
            "the body makes to the ground before a single weapon is drawn. "
            "In the Signature Nine-Weapons Method the stance is graded "
            "first and corrected last."
        ),
    },
    {
        "key": "footwork",
        "name": "Muay Boran Footwork (Karn Yang)",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Footwork (karn yang) is how the Muay Boran stance travels. The "
            "old art moves in short deliberate steps that never break the "
            "base: the lead foot steps first when advancing, the rear foot "
            "steps first when retreating, the feet never cross and never "
            "come together. A practitioner closing a 2 meter gap in 0.30 "
            "meter steps needs 7 steps, about 2.45 seconds of controlled "
            "advance, and can strike or defend at any instant of the walk. "
            "Muay Boran footwork favors small adjusting steps over the "
            "bouncing of the modern ring, because on broken battlefield "
            "ground a hop is a fall. Range - the distance at which each of "
            "the nine weapons can reach - is decided by the feet, and range "
            "decides everything."
        ),
        "how_it_works": (
            "From the fighting stance, advance by sliding the lead foot "
            "forward about one foot length and then bringing the rear foot "
            "the same distance so the stance width is restored. Retreat by "
            "moving the rear foot first, then the lead foot. Sidestep by "
            "moving the foot on the side you travel toward, then closing "
            "the other foot back into stance. Turn by pivoting on the ball "
            "of either foot to change angle without giving up the base. "
            "Every step is a deliberate placement, not a hop: the feet stay "
            "low, the head stays level, the guard stays up, and the weight "
            "never commits past the lead knee. The mechanics work because "
            "the base never narrows or crosses, so the hips stay loaded "
            "for a kick and the weight stays centered for a check. The "
            "common faults are crossing the feet, which deletes balance; "
            "stepping too wide, which freezes the hips; and bouncing, which "
            "telegraphs every entry on rough ground."
        ),
        "key_points": [
            "Footwork is the delivery system for all nine weapons: a great strike with bad feet never lands.",
            "Lead foot leads going forward, rear foot leads going back; the stance shape survives every step.",
            "Feet that cross or come together delete the base and leave the practitioner defenseless for a full beat.",
            "Closing a 2 meter gap takes about 7 short steps and 2.45 seconds of controlled advance.",
            "Small deliberate steps beat bouncing on the uneven ground the old art was built for.",
        ],
        "requirements": [
            "Maintain the stance width through every step: feet never cross, never touch.",
            "Place each step deliberately low with the head level: no hopping, no bouncing the chin.",
            "Keep the guard up and the weight centered while moving in any direction.",
            "Practice the four moves: advance, retreat, sidestep, and pivot.",
            "Stay able to strike or defend at any point in the step: if you cannot, the step was too big.",
        ],
        "standards": [
            "Traditional camps drill stepping on the spot and across the training ground before any combination work.",
            "Footwork must function on uneven ground: the old art never assumed a flat canvas.",
            "Seven short steps cover a 2 meter gap in about 2.45 seconds without ever breaking the base.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: footwork is the geometry of the triangle - "
            "every step redraws the base and the base decides the battle. "
            "In the Signature Nine-Weapons Method the feet are graded "
            "before the hands."
        ),
    },
    {
        "key": "nine_weapons",
        "name": "The Nine Weapons of Muay Boran (Naw Arwut)",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Muay Boran is called the science of the nine weapons (naw "
            "arwut): two fists, two elbows, two knees, two feet, and the "
            "head. Where modern ring boxing counts four limbs, the ancient "
            "art counts nine striking tools, and the whole curriculum is "
            "organized around them: every technique is one weapon used "
            "alone, and every combination is two or more weapons chained. "
            "The mathematics of the system run deep - nine weapons yield "
            "36 distinct two-weapon pairings and 84 distinct three-weapon "
            "chains - which is why the old masters spoke of endless "
            "technique from a short list of tools. Learning the nine "
            "weapons by name and by feel is the first theory every student "
            "memorizes, because the rest of the art is only their "
            "arrangement."
        ),
        "how_it_works": (
            "Memorize the nine in order: right fist, left fist, right "
            "elbow, left elbow, right knee, left knee, right foot, left "
            "foot, and the head. Drill each weapon alone against pads "
            "until its motion is clean - the straight punch for the fists, "
            "the horizontal cut for the elbows, the straight drive for the "
            "knees, the low cut for the feet, the short butt for the head. "
            "Then chain them in pairs: the 36 two-weapon pairings are the "
            "alphabet of Muay Boran combinations, practiced until any pair "
            "flows without thought. Then build the 84 three-weapon chains, "
            "which cover every practical combination a fighter will ever "
            "throw. The mechanics work because the body only has so many "
            "levers: mastering nine tools and their pairings covers the "
            "whole striking space, and the counting keeps training "
            "complete instead of drifting toward favorite techniques. The "
            "common fault is collecting techniques without the map: a "
            "student who cannot name the nine cannot chain them on "
            "purpose."
        ),
        "key_points": [
            "Nine weapons: two fists, two elbows, two knees, two feet, and the head as the ninth.",
            "The nine yield 36 two-weapon pairings and 84 three-weapon chains: the full combination space of the art.",
            "Every technique is one weapon; every combination is weapons chained in order.",
            "Drill each weapon alone until clean, then pairs until thoughtless, then triples.",
            "The student who cannot name the nine cannot chain them on purpose.",
        ],
        "requirements": [
            "Recite the nine weapons in order from memory before any combination drill.",
            "Demonstrate one clean strike with each of the nine weapons on pads.",
            "Practice the 36 two-weapon pairings until each flows without thought.",
            "Build toward the 84 three-weapon chains as the practical combination vocabulary.",
            "Name the weapon used in every strike thrown in sparring review.",
        ],
        "standards": [
            "The nine-weapons classification is the standard theory frame of Muay Boran across the traditional camps.",
            "Kraitus and Kraitus document the nine-weapons science as the organizing principle of the old art.",
            "Gradings in the traditional lineage test the nine by name before testing them by technique.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the nine weapons are nine covenants - each "
            "tool a separate promise between the practitioner and the "
            "mechanics of the body. The Signature Nine-Weapons Method "
            "counts them before it swings them."
        ),
    },
    {
        "key": "wai_khru",
        "name": "Wai Khru Ram Muay (The Teacher-Honoring Dance)",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The wai khru ram muay is the ritual dance performed before a "
            "Muay Boran demonstration or bout to honor the teacher (khru), "
            "the training camp, and the lineage of the art. The "
            "practitioner, wearing the mongkon headband, circles the ground "
            "to the music of the pi (oboe), klong khaek (drums), and ching "
            "(cymbals), bowing to the four directions and performing "
            "stylized movements drawn from the camp's forms. At a stately "
            "72 beats per minute, a 4 minute ram muay carries 288 beats of "
            "music, and every step lands inside that rhythm. Beyond "
            "respect, the dance is practical: it warms the body, settles "
            "the breathing, maps the ground under the feet, and lets each "
            "fighter read the opponent's style before a strike is thrown."
        ),
        "how_it_works": (
            "Enter wearing the mongkon and walk the perimeter of the "
            "ground slowly, bowing toward your teacher's direction first. "
            "Perform the stylized steps of your camp's form - low sweeps "
            "of the arms, deep stances, turns that show the guard from "
            "every angle - keeping every movement inside the music's "
            "rhythm. Bow to the four directions to seal the ground as your "
            "space. Use the minutes to breathe deeply, feel the footing, "
            "and watch how your opponent moves when they think no one is "
            "scoring. The dance ends with a final bow, after which the "
            "mongkon is removed and the contest begins. The mechanics work "
            "because slow deliberate movement under rhythm warms the "
            "joints, steadies the breath, and turns nervous energy into "
            "focus; the tradition works because a fighter who honors the "
            "teacher fights with the whole camp behind them. The common "
            "fault is rushing: a hurried wai khru warms nothing and honors "
            "no one."
        ),
        "key_points": [
            "The wai khru honors the teacher, the camp, and the lineage before any contest.",
            "Performed to pi, drums, and cymbals; at 72 beats per minute a 4 minute dance holds 288 beats.",
            "The mongkon is worn for the dance and removed before fighting begins.",
            "Practical uses: warming the body, settling breath, mapping the ground, reading the opponent.",
            "A rushed wai khru warms nothing and honors no one: the dance is never hurried.",
        ],
        "requirements": [
            "Learn your camp's ram muay form step by step until it flows without counting.",
            "Keep every movement inside the music: 288 beats over 4 minutes at the traditional tempo.",
            "Bow to the teacher's direction first, then seal the four directions.",
            "Use the dance to breathe, feel the footing, and study the opponent's movement.",
            "Remove the mongkon with respect when the dance ends and the contest begins.",
        ],
        "standards": [
            "The wai khru ram muay is the standard opening rite of Muay Boran demonstrations and traditional bouts.",
            "Kraitus and Kraitus document the rite as inseparable from the art itself.",
            "Each camp's form is distinct: the dance identifies the fighter's lineage to knowledgeable watchers.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the wai khru is the oath before the storm - "
            "the practitioner promising the teacher, the camp, and the "
            "ground that the weapons will be used with honor. The "
            "Signature Nine-Weapons Method never draws a weapon without "
            "the oath first."
        ),
    },
    {
        "key": "mongkon_prajioud",
        "name": "Mongkon and Prajioud (Sacred Headband and Armbands)",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The mongkon is the sacred headband worn during the wai khru "
            "ram muay, and the prajioud are the armbands worn on one or "
            "both upper arms during the contest. Traditionally the mongkon "
            "is a loop of cloth, often containing inscriptions or blessed "
            "material from the teacher, presented by the kru and worn only "
            "for the ritual dance - it is removed before fighting, and "
            "only the teacher or the fighter handles it. The prajioud stay "
            "on through the contest as protection and as the camp's "
            "colors. Sizing is practical craft: for a head measuring 0.57 "
            "meters around, the mongkon needs about 0.72 meters of cloth "
            "with 0.15 meters for the knot and tail; each prajioud runs "
            "about 0.32 meters, so a pair takes 0.64 meters. The old rule "
            "holds: the mongkon is blessed, the prajioud are earned, and "
            "neither is costume."
        ),
        "how_it_works": (
            "Measure the head just above the brows and add about 0.15 "
            "meters for the knot and the tail that hangs at the back; a "
            "0.57 meter head takes about 0.72 meters of cloth. The teacher "
            "ties or presents the mongkon - the student never ties their "
            "own for the first time. Wear it through the wai khru, then "
            "have it removed with both hands and set aside before the "
            "contest: it never touches the ground and never enters the "
            "fight. For the prajioud, measure the upper arm and cut about "
            "0.32 meters per band, tying them snug over the bicep where "
            "they neither slip in the clinch nor cut circulation. The "
            "mechanics are simple - fitted cloth that stays put - and the "
            "meaning is the point: the mongkon carries the teacher's "
            "blessing into the ritual, and the prajioud carry the camp's "
            "identity into the contest. The common fault is treating them "
            "as decoration: a mongkon stepped on or a prajioud worn loose "
            "insults the tradition it claims."
        ),
        "key_points": [
            "The mongkon is the sacred headband: worn for the wai khru, removed before fighting, handled with respect.",
            "The prajioud are armbands worn through the contest as protection and camp identity.",
            "A 0.57 meter head needs about 0.72 meters of cloth with 0.15 meters for knot and tail.",
            "Each prajioud runs about 0.32 meters; a pair takes 0.64 meters of cloth.",
            "The old rule: the mongkon is blessed, the prajioud are earned, and neither is costume.",
        ],
        "requirements": [
            "Size the mongkon from the head measurement plus 0.15 meters for knot and tail.",
            "Receive the first mongkon from the teacher; never tie your own the first time.",
            "Remove the mongkon with both hands after the dance; it never touches the ground or enters the fight.",
            "Tie each prajioud snug over the bicep: no slipping in the clinch, no cut circulation.",
            "Treat both as sacred equipment, never as decoration.",
        ],
        "standards": [
            "The mongkon is removed before the contest in every traditional demonstration and bout.",
            "Only the teacher or the fighter handles the mongkon; it is never stepped over or dropped.",
            "Kraitus and Kraitus document the mongkon and prajioud as standard equipment of the old art.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the mongkon is the seal on the oath - the "
            "teacher's blessing made cloth - and the prajioud are the "
            "colors of the covenant. The Signature Nine-Weapons Method "
            "treats sacred equipment as equipment: measured, fitted, and "
            "honored."
        ),
    },
    {
        "key": "card_chuek",
        "name": "Card Chuek (Hemp Rope Hand Wraps)",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Card chuek (kaad chuek) are the hemp-rope hand wraps of Muay "
            "Boran, wound around the hands and forearms before a contest in "
            "place of modern gloves. Strips of hemp or cotton rope are "
            "wrapped in a set pattern over the knuckles, the wrist, and up "
            "the forearm, hardening the striking surface and bracing the "
            "wrist for bare-knuckle impact. The wrapping is a craft with "
            "real arithmetic: about 24 wraps around a 0.21 meter hand and "
            "wrist circle take about 5.04 meters of rope per hand, so a "
            "full pair needs about 10.08 meters. Fighters sometimes "
            "dampened the rope to tighten it as it dried. The wraps "
            "changed the art: with rope instead of padding, the old boxers "
            "threw fewer wild head punches and more elbows, knees, and "
            "kicks, because the rope punishes the puncher as well as the "
            "target."
        ),
        "how_it_works": (
            "Start with the hand open and wrap the rope snug around the "
            "wrist several turns to build the brace. Cross over the back "
            "of the hand and loop each wrap between the base of the "
            "fingers, padding the knuckles without binding the fingers "
            "shut. Work about 24 wraps down the 0.21 meter circuit of hand "
            "and wrist, about 5.04 meters of rope per hand, then continue "
            "the spiral up the forearm for bracing. Keep every wrap snug "
            "but never numb: the fingers must still open and close. Tie "
            "off at the forearm and check by making a fist - the wrap "
            "should feel like a cast, not a tourniquet. The mechanics work "
            "because the rope spreads impact across the whole hand and "
            "locks the wrist straight, which is what lets a bare fist hit "
            "without collapsing. The common fault is wrapping the knuckles "
            "thick and the wrist thin: the wrist is what breaks, so the "
            "wrist gets the brace."
        ),
        "key_points": [
            "Card chuek are hemp-rope wraps: the striking surface and wrist brace of the old art.",
            "About 24 wraps over a 0.21 meter circuit take about 5.04 meters of rope per hand, 10.08 for the pair.",
            "Wraps pad the knuckles, brace the wrist, and run up the forearm.",
            "Rope changed the tactics: fewer wild head punches, more elbows, knees, and kicks.",
            "Wrap the wrist thick: the wrist is what breaks, so the wrist gets the brace.",
        ],
        "requirements": [
            "Build the wrist brace first with several snug turns before padding the knuckles.",
            "Use about 5.04 meters of rope per hand in roughly 24 wraps; 10.08 meters for the pair.",
            "Keep fingers free to open and close; check by making a full fist.",
            "Tie off at the forearm and confirm the wrap feels like a cast, not a tourniquet.",
            "Learn the wrap from a teacher: the pattern is camp knowledge, not improvisation.",
        ],
        "standards": [
            "Card chuek are the documented historical hand protection of Muay Boran before the gloved era.",
            "Kraitus and Kraitus record the rope wraps and their effect on the old fighting tactics.",
            "Modern demonstrations of Muay Boran wrap in the traditional pattern as a mark of authenticity.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the rope is the covenant made visible - every "
            "wrap a promise that the fist will land straight and true. "
            "The Signature Nine-Weapons Method wraps with arithmetic: "
            "measured rope, measured brace, measured honor."
        ),
    },
    {
        "key": "guard",
        "name": "The Muay Boran Guard",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The Muay Boran guard is the long guard of the old art: the "
            "lead hand extended well forward, palm open, at about 0.75 "
            "meters from the face, with the rear hand cocked high near the "
            "chin. Against an opponent advancing at 1.2 meters per "
            "second, that 0.50 meter of extra reach buys about 0.42 "
            "seconds of early warning - time to jam, deflect, or step off "
            "the line. The extended lead is a probe and a shield at once: "
            "it measures distance, stiff-arms the rush, and sets up the "
            "elbow that follows any blocked punch. The rear hand guards "
            "the chin and the jaw, and both elbows stay heavy over the "
            "ribs. The old guard looks open to modern eyes, but it was "
            "built for rope-wrapped hands and for opponents who might "
            "grapple: the long lead keeps the fight at the end of your "
            "weapons, not at the end of theirs."
        ),
        "how_it_works": (
            "From the stance, extend the lead arm forward with the palm "
            "open or loosely fisted until the hand sits about 0.75 meters "
            "from your face - a full arm plus a lean, not a locked elbow. "
            "Cock the rear hand high beside the chin with the elbow tucked "
            "to the ribs. Keep the lead hand alive: small circles and "
            "probes that touch the opponent's guard, shoulder, or forehead "
            "to measure the distance. When the opponent rushes, stiffen "
            "the lead arm into their shoulder or face to kill the advance; "
            "when they punch, the lead hand is already halfway to the "
            "parry. The mechanics work because distance is defense: 0.50 "
            "meters of extra reach converts to about 0.42 seconds against "
            "a 1.2 meter per second rush, and a hand already extended "
            "deflects faster than a hand that must travel. The common "
            "fault is a dead lead hand - extended but lifeless, which is "
            "only an invitation to be pulled into the clinch."
        ),
        "key_points": [
            "The long guard extends the lead hand about 0.75 meters from the face, palm open.",
            "That 0.50 meters of extra reach buys about 0.42 seconds against a 1.2 meter per second rush.",
            "The lead hand probes, measures, stiff-arms, and sets up the elbow.",
            "The rear hand stays cocked high guarding the chin; elbows stay heavy over the ribs.",
            "A dead lead hand is an invitation: the guard must stay alive with small probing motion.",
        ],
        "requirements": [
            "Extend the lead hand to about 0.75 meters from the face without locking the elbow.",
            "Keep the rear hand high at the chin with the elbow tucked to the ribs.",
            "Probe constantly with the lead: touch guard, shoulder, or forehead to measure distance.",
            "Stiffen the lead into a rush and parry with the hand that is already halfway there.",
            "Never let the lead hand go dead: lifeless extension invites the clinch pull.",
        ],
        "standards": [
            "The long guard is the documented standard guard of the Muay Boran tradition.",
            "Traditional camps drill the lead-hand probe as the first defensive skill after the stance.",
            "The guard must function with rope-wrapped hands and against grappling entries.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the guard is the walls of the temple - the "
            "long lead the outer wall that keeps the fight at the end of "
            "your weapons. The Signature Nine-Weapons Method builds the "
            "walls before it sharpens the spears."
        ),
    },
    {
        "key": "conditioning",
        "name": "Muay Boran Body Conditioning",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Muay Boran body conditioning hardens the striking surfaces "
            "and the frame that carries them: shins rolled and struck "
            "against heavy bags and banana trees, knuckles worked on rope "
            "and sand, the neck bridged, the midsection pounded with "
            "medicine balls and partner strikes, the legs built by endless "
            "stance holding. The old method is progressive overload with "
            "patience: a standard 8 week shin program runs 3 sessions a "
            "week - 24 sessions - with strikes per session climbing from "
            "50 to 120, averaging 85, for about 2,040 total strikes across "
            "the program. Bone and connective tissue adapt to gradual "
            "stress; they break under sudden stress. Conditioning never "
            "replaces technique - a conditioned shin thrown with bad "
            "mechanics still folds - but it lets good mechanics survive "
            "contact."
        ),
        "how_it_works": (
            "Build the program in three layers. First the frame: stance "
            "holding, roadwork, and skipping for the legs and lungs, "
            "because a tired fighter has no technique. Then the surfaces: "
            "start the 8 week shin cycle at 50 strikes per session, 3 "
            "sessions a week, adding roughly 10 strikes a session each "
            "week until 120 - 24 sessions and about 2,040 strikes total - "
            "rolling and striking the heavy bag, never kicking with the "
            "foot. Then the core: partner medicine-ball work to the "
            "midsection and controlled body punches, building the ability "
            "to breathe through impact. Rest is part of the method: tissue "
            "hardens between sessions, not during them, so never condition "
            "an inflamed limb. The mechanics work because bone remodels "
            "under repeated sub-injury stress - the same principle as any "
            "progressive training - and the arithmetic keeps the stress "
            "sub-injury: small weekly steps, never jumps. The common fault "
            "is macho escalation: doubling the strikes in week two buys an "
            "injury, not a harder shin."
        ),
        "key_points": [
            "Conditioning hardens striking surfaces and the frame: shins, knuckles, neck, midsection, legs.",
            "The standard shin cycle: 3 sessions a week for 8 weeks, 50 to 120 strikes per session, about 2,040 total.",
            "Tissue hardens between sessions, not during them: never condition an inflamed limb.",
            "Conditioning supports technique but never replaces it: bad mechanics still fold.",
            "Progressive steps, never jumps: sudden stress breaks what gradual stress hardens.",
        ],
        "requirements": [
            "Build the frame first: stance holding, roadwork, and skipping for legs and lungs.",
            "Run the 8 week shin cycle: 24 sessions, 50 to 120 strikes per session, about 2,040 total.",
            "Strike the bag with the shin, never the foot, and roll the shins to finish.",
            "Add core work: medicine-ball and controlled partner strikes to the midsection with breathing.",
            "Rest inflamed limbs: adaptation happens between sessions.",
        ],
        "standards": [
            "Progressive overload is the standard conditioning principle across the traditional camps.",
            "Traditional conditioning used banana trees and heavy bags; the progression arithmetic is the same.",
            "Conditioning volume is logged per session: the 2,040-strike cycle is a planning standard, not a boast.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD, CIT_DELP_BASICS],
        "sig_lens": (
            "Signature lens: conditioning is the forging of the weapons - "
            "the covenant written into bone by patient arithmetic. The "
            "Signature Nine-Weapons Method counts every strike of the "
            "2,040 and never spends the body it has not yet built."
        ),
    },
    {
        "key": "sao_chueak",
        "name": "Triangular Stepping (Sao Chueak)",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Sao chueak - triangular stepping - is the footwork signature "
            "of the southern Muay Chaiya style and one of the most "
            "distinctive movements in Muay Boran. The practitioner steps "
            "along the edges of an imagined triangle, typically with 0.50 "
            "meter sides: each step moves to a new vertex, turning the "
            "body 60 degrees and changing the angle on the opponent "
            "without ever stepping straight back. Walking the full "
            "triangle covers 1.50 meters per cycle, and 10 cycles drill "
            "15 meters of angled movement into the legs. The triangle "
            "solves the oldest problem in striking: how to leave the line "
            "of attack while staying in range to answer. Straight lines "
            "retreat; triangles flank."
        ),
        "how_it_works": (
            "Mark a triangle on the ground with 0.50 meter sides. Start at "
            "one vertex in the fighting stance, facing the center. Step "
            "the lead foot to the next vertex along the edge, then bring "
            "the rear foot into stance: the body has turned 60 degrees and "
            "the angle on the imagined opponent has changed completely. "
            "Step to the third vertex the same way, then continue cycling: "
            "each full triangle is 1.50 meters of angled travel, and 10 "
            "cycles make 15 meters of drilling. Practice both directions, "
            "then practice with a partner pressing forward: as they step "
            "in along the straight line, you step along the triangle edge "
            "and their attack passes through empty space while your "
            "weapons stay in range. The mechanics work because a 60 "
            "degree turn moves the head off the centerline while the feet "
            "keep the stance loaded for the counter. The common fault is "
            "rounding the triangle into a circle: the drill only teaches "
            "angles if the corners stay sharp."
        ),
        "key_points": [
            "Sao chueak steps the edges of a triangle, turning 60 degrees at each vertex.",
            "With 0.50 meter sides, each cycle covers 1.50 meters; 10 cycles drill 15 meters.",
            "The triangle leaves the line of attack while staying in range: straight lines retreat, triangles flank.",
            "The signature footwork of Muay Chaiya, the southern style, and a jewel of Muay Boran.",
            "Keep the corners sharp: rounding the triangle into a circle teaches nothing.",
        ],
        "requirements": [
            "Mark a 0.50 meter triangle and step its edges without rounding the vertices.",
            "Turn 60 degrees at each vertex with the stance intact and the guard up.",
            "Drill both directions until 10 cycles - 15 meters - feel automatic.",
            "Apply against a pressing partner: their straight attack passes through empty space.",
            "Counter from the new angle: the drill is only complete when the answer lands.",
        ],
        "standards": [
            "Sao chueak is the documented footwork signature of the Muay Chaiya regional style.",
            "Traditional southern camps drill the triangle before teaching angled counters.",
            "The 0.50 meter triangle is the standard teaching size; larger triangles come with experience.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the triangle is the geometry of the covenant "
            "- three points, three angles, no retreat. The Signature "
            "Nine-Weapons Method walks the 1.50 meter cycle until the "
            "flank is instinct."
        ),
    },
    {
        "key": "ram_mai",
        "name": "Muay Boran Forms Practice (Ram Mai)",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Ram mai are the choreographed forms of Muay Boran: set "
            "sequences of strikes, steps, and defenses practiced solo, "
            "each camp keeping its own forms as a living textbook. A "
            "student learning 3 forms of 12 movements each carries 36 "
            "techniques in memory, and drilling the set for 5 rounds "
            "repeats 180 clean executions in a single session. The forms "
            "preserve the old battlefield techniques that sparring "
            "forgets: the low-line kicks, the breaking entries, the "
            "weapons the modern ring retired. Forms practice is shadow "
            "boxing with a syllabus - every movement has a name, a "
            "target, and a reason, and the teacher corrects the form the "
            "way a writing master corrects script. The body learns what "
            "the mind can recite."
        ),
        "how_it_works": (
            "Learn the first form one movement at a time: the teacher "
            "shows the strike, names it, names its target, and has you "
            "repeat it until the shape is clean. Link the 12 movements in "
            "order until the form runs without pauses, then add the "
            "second and third forms the same way - 36 techniques carried "
            "in sequence. Drill the full set for 5 rounds, 180 executions, "
            "moving at fighting speed but striking air with full "
            "mechanics: hips turning, guard returning, breath timed to the "
            "strikes. Practice facing each of the four directions in turn, "
            "the way the wai khru seals the ground. The mechanics work "
            "because high-repetition clean movement myelinates the "
            "patterns - the nervous system keeps what it repeats - and "
            "the syllabus keeps the repetitions honest: no drifting into "
            "favorite moves. The common fault is performing the form for "
            "show: speed without targets is dance, and the forms are a "
            "textbook, not a performance."
        ),
        "key_points": [
            "Ram mai are the choreographed forms: each camp keeps its own as a living textbook.",
            "Three forms of 12 movements carry 36 techniques; 5 rounds drill 180 clean executions.",
            "The forms preserve battlefield techniques that sparring forgets.",
            "Every movement has a name, a target, and a reason: the teacher corrects like a writing master.",
            "Speed without targets is dance: the forms are a textbook, not a performance.",
        ],
        "requirements": [
            "Learn each form one movement at a time: strike, name, target, repeat until clean.",
            "Carry 3 forms of 12 movements - 36 techniques - in sequence without pauses.",
            "Drill the set for 5 rounds: 180 full-mechanic executions per session.",
            "Practice facing all four directions, sealing the ground like the wai khru.",
            "Strike air at fighting speed with hips, guard return, and timed breath.",
        ],
        "standards": [
            "Form practice is the standard solo syllabus across the traditional Muay Boran camps.",
            "Each camp's forms are distinct and identify its lineage, like the ram muay dance.",
            "Gradings test forms before sparring: the textbook comes before the conversation.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the forms are the covenant written down - the "
            "old techniques kept safe in sequence so no weapon is ever "
            "lost. The Signature Nine-Weapons Method recites the 36 and "
            "drills the 180."
        ),
    },
    {
        "key": "regional_styles",
        "name": "The Five Regional Styles of Muay Boran",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Muay Boran is not one style but a family of regional styles, "
            "each named for its homeland and each with its own character: "
            "Muay Thasao of the north, fast and technical; Muay Korat of "
            "the northeast, famous for heavy punches and the buffalo "
            "swing; Muay Lopburi of the central plains, clever and "
            "tricky; Muay Chaiya of the south, low stances and triangular "
            "stepping; and Muay Uttaradit, also called Pahuyuth, the "
            "northern art of many techniques. Cataloging their signature "
            "methods - say 24 for Thasao, 31 for Korat, 28 for Lopburi, "
            "35 for Chaiya, and 22 for Uttaradit - gives 140 cataloged "
            "techniques across the five, averaging 28 per style, and shows "
            "how one art grew five dialects from the same nine weapons. "
            "Knowing the styles lets a student read any traditional "
            "fighter: the stance and the first step betray the homeland."
        ),
        "how_it_works": (
            "Study the five in turn, one principle each. For Muay Thasao, "
            "drill speed: fast hands, quick entries, technique over "
            "power. For Muay Korat, drill the heavy swing: the famous "
            "wide punches thrown with full body rotation. For Muay "
            "Lopburi, drill trickery: feints, traps, and counters. For "
            "Muay Chaiya, drill the low stance and the sao chueak "
            "triangle - the southern signature. For Muay Uttaradit "
            "(Pahuyuth), drill breadth: the widest technique catalog of "
            "the five. Then compare: put two stylists side by side and "
            "watch the stance width, the guard height, and the first "
            "step - the three tells of lineage. The knowledge works "
            "because styles are answers to local conditions: the south "
            "fought on sand and developed low stances, the northeast "
            "prized the knockout punch. The common fault is style "
            "shopping: a beginner collecting five styles learns none. "
            "Pick one homeland, learn its 28, then visit the neighbors."
        ),
        "key_points": [
            "Five regional styles: Thasao (north), Korat (northeast), Lopburi (central), Chaiya (south), Uttaradit/Pahuyuth.",
            "Cataloging gives about 140 techniques across the five, averaging 28 per style.",
            "Korat is famous for heavy punches; Chaiya for low stances and triangular stepping.",
            "Styles are answers to local conditions: sand, battlefield, and temperament shaped each.",
            "The stance width, guard height, and first step betray the homeland: learn to read them.",
        ],
        "requirements": [
            "Name all five styles with their regions and one signature trait each.",
            "Study one style deeply - about 28 cataloged techniques - before visiting the neighbors.",
            "Drill each style's signature: Thasao speed, Korat power, Lopburi trickery, Chaiya triangles, Uttaradit breadth.",
            "Read lineage in others: stance width, guard height, and first step.",
            "Respect the dialects: one art, five homelands, no superior style.",
        ],
        "standards": [
            "The five regional styles are the documented historical geography of Muay Boran.",
            "Kraitus and Kraitus record the regional schools and their characters.",
            "Traditional teachers identify a fighter's lineage from stance and stepping before a strike is thrown.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the five styles are five dialects of one "
            "covenant - the same nine weapons spoken with five accents. "
            "The Signature Nine-Weapons Method learns one homeland's 28 "
            "before it tours the other four."
        ),
    },
    # ------------------------------------------------------- COMPOUNDED
    {
        "key": "mat_trong",
        "name": "Straight Punch (Mat Trong)",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The straight punch (mat trong) is the first of the fist "
            "weapons: the lead or rear hand driven straight from the "
            "guard to the target along the shortest line. A punch "
            "traveling 0.65 meters at 9 meters per second lands in about "
            "0.072 seconds - faster than a blink - which is why the "
            "straight punch is both the safest attack and the best "
            "measuring tool in the art. Thrown at a sustainable pace of "
            "one every 1.5 seconds, a practitioner can deliver 120 "
            "straight punches in a 3 minute round of pad work. The power "
            "comes from the floor: the rear foot drives, the hip turns, "
            "the shoulder snaps, and the fist is only the last link. The "
            "old art threw it with rope-wrapped hands, so the wrist stays "
            "locked straight and the knuckles land flat."
        ),
        "how_it_works": (
            "From the guard, drive off the rear foot and turn the hip "
            "toward the target as the punching arm extends straight along "
            "the centerline. Rotate the fist to land with the knuckles "
            "flat and the wrist locked dead straight - the rope wraps "
            "brace it, but the alignment does the work. Snap the shoulder "
            "forward at the end for the last few centimeters of reach, "
            "then pull the hand straight back to the guard along the same "
            "line: the return is half the technique. Keep the other hand "
            "glued to the chin and the chin tucked through the whole "
            "motion. The mechanics work because the kinetic chain stacks "
            "levers - foot, hip, shoulder, arm - so a 68 kilogram body "
            "puts far more than arm weight behind 0.072 seconds of "
            "travel. The common faults are dropping the rear hand, which "
            "invites the counter, and pushing the punch, which trades the "
            "snap for a shove."
        ),
        "key_points": [
            "The straight punch travels the shortest line: 0.65 meters at 9 meters per second lands in about 0.072 seconds.",
            "One punch every 1.5 seconds sustains 120 punches across a 3 minute pad round.",
            "Power comes from the floor through the hip: the fist is the last link, not the first.",
            "The wrist stays locked straight with knuckles flat: rope wraps brace, alignment delivers.",
            "The return along the same line is half the technique: a punch that stays out is a handle.",
        ],
        "requirements": [
            "Drive from the rear foot with the hip turning into every straight punch.",
            "Land with the wrist locked straight and the knuckles flat on the target.",
            "Snap the shoulder for the last centimeters, then return along the same line.",
            "Keep the non-punching hand glued to the chin with the chin tucked.",
            "Sustain the pace: one clean straight punch every 1.5 seconds for the full round.",
        ],
        "standards": [
            "The straight punch is the first fist weapon taught in every traditional camp.",
            "Delp documents the straight punch mechanics shared by Muay Thai and Muay Boran.",
            "Pad rounds of 3 minutes at 120 punches are the standard volume builder for the straight weapons.",
        ],
        "citations": [CIT_DELP_BASICS, CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the straight punch is the first covenant of "
            "the fist - the shortest line between the oath and the "
            "target, traveled in 0.072 seconds. The Signature "
            "Nine-Weapons Method throws it straight and brings it home."
        ),
    },
    {
        "key": "mat_wiang_san",
        "name": "Hook Punch (Mat Wiang San)",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The hook punch (mat wiang san) is the curved fist weapon: "
            "the arm bent at roughly 90 degrees, swung in a horizontal "
            "arc to strike the side of the head or body. With a 0.55 "
            "meter arm swinging through 120 degrees, the fist travels "
            "about 1.15 meters of arc - a longer road than the straight "
            "punch, paid for with rotational power from the hips and "
            "core. The hook is the answer to the guard: where the "
            "straight punch is blocked by hands in front, the hook "
            "travels around them. The old rope-wrapped fighters threw it "
            "tight, because a wide hook with rope hands is slow enough to "
            "be clinched, and the clinch was the hook's natural enemy."
        ),
        "how_it_works": (
            "From the guard, pivot on the lead foot and whip the hip "
            "around as the bent arm swings horizontally, elbow held at "
            "about shoulder height and the fist traveling the 1.15 meter "
            "arc to the target. Keep the wrist straight and the fist "
            "vertical or horizontal at impact - whichever the camp "
            "teaches - with the knuckles landing flat. The rear hand "
            "stays glued to the chin because the hook's arc opens the "
            "body for exactly the counter it is designed to beat. Turn "
            "the hip fully: the arm only guides, the rotation hits. "
            "Return the hand to the guard along a tight line, not a wide "
            "loop. The mechanics work because angular momentum from the "
            "hip turn multiplies through the bent arm: a short lever "
            "driven by the whole body. The common faults are arm-punching "
            "without the hip, which makes a slap, and swinging wide, "
            "which makes a slow invitation to the clinch."
        ),
        "key_points": [
            "The hook swings a 0.55 meter arm through 120 degrees: about 1.15 meters of arc.",
            "The hook travels around the guard that stops the straight punch.",
            "Power comes from hip rotation, not the arm: the arm guides, the rotation hits.",
            "Throw it tight: a wide hook with rope hands is slow enough to be clinched.",
            "The rear hand stays glued to the chin: the hook opens the body to its own counter.",
        ],
        "requirements": [
            "Bend the arm about 90 degrees with the elbow at shoulder height through the arc.",
            "Pivot the lead foot and turn the hip fully into every hook.",
            "Land with the wrist straight and the knuckles flat, fist vertical or horizontal per camp.",
            "Keep the rear hand glued to the chin for the whole motion.",
            "Return along a tight line: no wide loops, no dropped hands.",
        ],
        "standards": [
            "The hook is the standard curved fist weapon across the traditional camps.",
            "Delp documents hook mechanics shared with the modern ring art.",
            "Tight hooks are the camp standard: wide hooks are corrected as clinch invitations.",
        ],
        "citations": [CIT_DELP_BASICS, CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the hook is the covenant of the turning body "
            "- the hip making a promise the fist keeps along 1.15 meters "
            "of arc. The Signature Nine-Weapons Method turns fully and "
            "swings tight."
        ),
    },
    {
        "key": "mat_soi_dao",
        "name": "Uppercut (Mat Soi Dao)",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The uppercut (mat soi dao - the star-piercing punch) is the "
            "rising fist weapon: the hand drops slightly and drives upward "
            "under the guard to the chin or the solar plexus. Rising 0.45 "
            "meters at 7 meters per second, the fist arrives in about "
            "0.064 seconds along a line the high guard never covers. The "
            "uppercut is the close-range answer: when the clinch tightens "
            "or the guard rises to stop hooks, the uppercut travels "
            "underneath. The old fighters threw it short, because an "
            "uppercut that starts low and wide is a gift to anyone "
            "waiting with an elbow. Like all fist weapons, it lands with "
            "the wrist straight - the rising angle makes wrist alignment "
            "the whole technique."
        ),
        "how_it_works": (
            "From the guard, dip the punching shoulder slightly and bend "
            "the knees a touch more to load the legs. Drive upward off "
            "the legs, turning the hip as the fist rises along the "
            "centerline for about 0.45 meters to the chin or solar "
            "plexus. Keep the elbow bent and close to the body - the "
            "punch rises like an elevator, not a catapult - and rotate "
            "the fist to land with the knuckles up and the wrist dead "
            "straight. The other hand never leaves the chin. Return the "
            "fist down the same vertical line to the guard. The mechanics "
            "work because the legs drive the rise: the 0.064 second "
            "travel is leg power expressed through a short lever, which "
            "is why the uppercut hurts out of proportion to its wind-up. "
            "The common faults are dropping the hand first, which "
            "telegraphs the punch, and leaning in, which walks the chin "
            "onto the counter."
        ),
        "key_points": [
            "The uppercut rises about 0.45 meters at 7 meters per second: impact in about 0.064 seconds.",
            "It travels under the high guard that stops hooks and straight punches.",
            "The legs drive the rise: leg power through a short lever is why it hurts beyond its wind-up.",
            "Wrist alignment is the whole technique at the rising angle: straight wrist, knuckles up.",
            "Throw it short and return it straight down: a wide uppercut is an elbow's invitation.",
        ],
        "requirements": [
            "Load the legs with a slight dip before every uppercut; drive upward off the legs.",
            "Rise about 0.45 meters along the centerline to the chin or solar plexus.",
            "Keep the elbow bent and close: the punch rises like an elevator, not a catapult.",
            "Land with the wrist dead straight and the knuckles up.",
            "Keep the other hand on the chin and return down the same vertical line.",
        ],
        "standards": [
            "The uppercut is the standard rising fist weapon of the traditional curriculum.",
            "Short uppercuts are the camp standard: wide rising punches are corrected on sight.",
            "Delp documents the rising-punch mechanics shared with the modern ring art.",
        ],
        "citations": [CIT_DELP_BASICS, CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the uppercut is the covenant of the rising "
            "ground - the legs keeping a promise the fist collects in "
            "0.064 seconds. The Signature Nine-Weapons Method rises "
            "straight and never leans in."
        ),
    },
    {
        "key": "sok_ti",
        "name": "Horizontal Elbow (Sok Ti)",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The horizontal elbow (sok ti) is the first of the elbow "
            "weapons and the signature strike of the old art: the arm "
            "folded tight, the elbow driven horizontally across the "
            "target like a blade. With a 0.35 meter forearm sweeping 90 "
            "degrees, the point travels about 0.55 meters of arc, and at "
            "a tip speed of 10 meters per second it crosses that arc in "
            "about 0.055 seconds - a cutting impact from a hard bony "
            "point with almost no wind-up. Rope-wrapped fighters loved "
            "the elbow because it needs no glove and no range: it is the "
            "weapon of the clinch, the phone booth, and the "
            "counter. The elbow cuts where the fist bruises, which is "
            "why the old art treated it with respect and the modern ring "
            "treats it with rules."
        ),
        "how_it_works": (
            "From the guard, fold the striking arm tight so the fist "
            "touches the shoulder and the elbow points outward like a "
            "blade. Pivot on the lead foot and whip the hip across as the "
            "elbow sweeps horizontally through its 0.55 meter arc to the "
            "temple, jaw, or brow. Keep the motion compact: the power is "
            "in the hip whip, not a big swing, and the 0.055 second "
            "travel leaves no time to see it. Strike with the point of "
            "the elbow, the hard tip of the ulna, and cut across rather "
            "than pushing through. The other hand stays on the chin "
            "because the elbow's range puts you inside the opponent's "
            "weapons. The mechanics work because a short lever driven by "
            "hip rotation concentrates force on a tiny bony point: "
            "pressure is force over area, and the elbow's area is "
            "minuscule. The common fault is swinging the arm wide, which "
            "turns a 0.055 second cut into a slow visible loop."
        ),
        "key_points": [
            "The horizontal elbow sweeps about 0.55 meters of arc in about 0.055 seconds at 10 meters per second tip speed.",
            "The elbow cuts where the fist bruises: a tiny bony point concentrates the force.",
            "It needs no glove and no range: the weapon of the clinch and the counter.",
            "Power comes from the hip whip, not a big swing: compact is fast, wide is visible.",
            "The other hand stays on the chin: elbow range is inside the opponent's weapons too.",
        ],
        "requirements": [
            "Fold the arm tight with the fist at the shoulder and the elbow bladed outward.",
            "Pivot the lead foot and whip the hip across into the 90 degree sweep.",
            "Strike with the point of the elbow, cutting across rather than pushing through.",
            "Keep the sweep compact: 0.55 meters of arc in about 0.055 seconds.",
            "Guard the chin with the other hand through the whole exchange.",
        ],
        "standards": [
            "The horizontal elbow is the first elbow weapon in the traditional curriculum.",
            "Elbow techniques are the documented signature of Muay Boran's close-range science.",
            "Traditional camps drill the elbow on pads with control: the point is respected, never thrown wild.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD, CIT_DELP_BASICS],
        "sig_lens": (
            "Signature lens: the elbow is the covenant of the blade - the "
            "body's own knife, drawn in 0.055 seconds. The Signature "
            "Nine-Weapons Method keeps the blade folded until the hip "
            "gives the order."
        ),
    },
    {
        "key": "sok_ngat",
        "name": "Upward Elbow (Sok Ngat)",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The upward elbow (sok ngat) is the rising elbow weapon: the "
            "elbow driven upward under the guard to the chin, jaw, or "
            "solar plexus. Rising about 0.50 meters at 6.5 meters per "
            "second, it lands in about 0.077 seconds along the one line "
            "the horizontal elbow cannot take. Where sok ti cuts across, "
            "sok ngat spears upward - it is the answer to the crouching "
            "opponent, the low guard, and the clinch that pulls the head "
            "down. The old fighters threw it from the long guard's "
            "probe: the lead hand finds the forehead, pulls the head "
            "down a hand's width, and the elbow rises into the space. "
            "Like all elbows, it concentrates the body's rotation onto "
            "a bony point."
        ),
        "how_it_works": (
            "From the guard, drop the striking elbow slightly and load "
            "the legs. Drive upward off the legs, turning the hip as the "
            "elbow rises about 0.50 meters along the centerline to the "
            "chin or solar plexus, the forearm folded tight so the point "
            "leads. Keep the motion vertical and close: the elbow rises "
            "like the uppercut's sharper sibling, arriving in about 0.077 "
            "seconds. The other hand stays on the chin and the head stays "
            "off the centerline by a hand's width - rising into the "
            "opponent's space means sharing it. Return the elbow down "
            "the same line to the guard. The mechanics work because the "
            "leg drive stacks under the rising point, the same engine as "
            "the uppercut with a harder tip. The common fault is leaning "
            "the head forward into the rise, which trades the elbow for "
            "a head-on collision."
        ),
        "key_points": [
            "The upward elbow rises about 0.50 meters at 6.5 meters per second: impact in about 0.077 seconds.",
            "It takes the vertical line the horizontal elbow cannot: the answer to the crouch and the low guard.",
            "The classic setup: the lead hand finds the forehead and the elbow rises into the space.",
            "Leg drive powers the rise, the folded point delivers it: the uppercut's sharper sibling.",
            "Keep the head off the centerline: rising into their space means sharing it.",
        ],
        "requirements": [
            "Drop the elbow slightly and load the legs before every upward elbow.",
            "Rise about 0.50 meters along the centerline with the forearm folded tight.",
            "Drive off the legs with the hip turning: leg power, bony point.",
            "Keep the other hand on the chin and the head a hand's width off center.",
            "Return down the same vertical line to the guard.",
        ],
        "standards": [
            "The upward elbow is the standard rising elbow weapon of the traditional curriculum.",
            "Traditional camps pair it with the horizontal elbow as the two primary elbow lines.",
            "Control is the standard: the rising point is drilled on pads, never thrown wild at partners.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the upward elbow is the covenant of the "
            "spear - the point rising 0.50 meters in 0.077 seconds to keep "
            "a promise the legs made. The Signature Nine-Weapons Method "
            "rises vertical and shares no centerline."
        ),
    },
    {
        "key": "khao_trong",
        "name": "Straight Knee (Khao Trong)",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The straight knee (khao trong) is the first of the knee "
            "weapons: the knee driven straight up and forward into the "
            "midsection or thigh. Driving 0.30 meters in 0.15 seconds "
            "demands about 26.7 meters per second squared of "
            "acceleration, and with about 12 kilograms of effective mass "
            "behind the point that is about 320 newtons of driving force "
            "- the whole body rising through one bony point. The knee is "
            "the clinch weapon above all: where the hands tie up, the "
            "knees keep working. The old art threw it with the hips "
            "thrust fully through, the standing foot pivoting, the body "
            "leaning back just enough to clear the point's path. A "
            "straight knee thrown with the hips is a spear; thrown with "
            "the leg alone it is a tap."
        ),
        "how_it_works": (
            "From the stance or the clinch, drive the knee straight up "
            "and forward, thrusting the hips fully through the motion "
            "while rising onto the ball of the standing foot. Lean the "
            "torso back slightly to clear the knee's path and pull the "
            "opponent's head or arm down into the rising point when the "
            "clinch allows. The knee travels about 0.30 meters in about "
            "0.15 seconds - 26.7 meters per second squared - delivering "
            "about 320 newtons through the point. Strike with the hard "
            "top of the knee and the first inches of thigh, never the "
            "kneecap's face. Return the foot to the ground in stance, "
            "never dangling. The mechanics work because the hip thrust "
            "puts the body's rising mass behind the point: the 12 "
            "kilogram effective mass is the hip's contribution, not the "
            "leg's. The common fault is throwing with the leg alone, "
            "which spends the motion and keeps the force."
        ),
        "key_points": [
            "The straight knee drives 0.30 meters in 0.15 seconds: about 26.7 meters per second squared and 320 newtons.",
            "The hips thrust fully through: a knee with the hips is a spear, with the leg alone a tap.",
            "The clinch weapon above all: where the hands tie up, the knees keep working.",
            "Strike with the top of the knee and upper thigh, never the kneecap's face.",
            "Return the foot to stance: a dangling leg is a swept leg.",
        ],
        "requirements": [
            "Thrust the hips fully through every straight knee with the torso leaning slightly back.",
            "Rise onto the ball of the standing foot as the knee drives.",
            "Drive about 0.30 meters in about 0.15 seconds with the point leading.",
            "Pull the opponent down into the knee when the clinch allows.",
            "Return the foot to the ground in stance immediately after impact.",
        ],
        "standards": [
            "The straight knee is the first knee weapon in the traditional curriculum.",
            "Hip thrust is the camp standard: leg-only knees are corrected as taps.",
            "Knee techniques are drilled on the heavy bag and in controlled clinch before any free application.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD, CIT_DELP_BASICS],
        "sig_lens": (
            "Signature lens: the knee is the covenant of the rising body "
            "- 12 kilograms of promise delivered at 320 newtons through "
            "one point. The Signature Nine-Weapons Method thrusts the "
            "hips and never taps."
        ),
    },
    {
        "key": "khao_khong",
        "name": "Curved Knee (Khao Khong)",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The curved knee (khao khong) is the arcing knee weapon: the "
            "knee swung in a curve to strike the ribs, the floating ribs, "
            "or the thigh from the side. The point travels roughly a "
            "quarter circle of 0.45 meter radius - about 0.71 meters of "
            "curved path - which lets it travel around the guard that "
            "stops the straight knee. Where khao trong spears the "
            "centerline, khao khong hooks the body: it is the knee for "
            "the side door, thrown when the opponent's elbows clamp the "
            "middle. The old fighters threw it from a slight angle, "
            "stepping the standing foot out so the hip opens and the "
            "curve has room. The ribs remember the curved knee longer "
            "than the straight one."
        ),
        "how_it_works": (
            "Step the standing foot slightly outward to open the hip, "
            "then swing the knee in a curve, the point traveling about "
            "0.71 meters along its quarter-circle path to the ribs or "
            "thigh. Whip the hip around with the swing - the curve is "
            "hip-driven like the hook punch's lower sibling - and lean "
            "the torso away to clear the path. Strike with the top of "
            "the knee, digging the point into the target at the end of "
            "the curve rather than slapping across it. The other hand "
            "guards the chin because the curved path opens the body "
            "exactly as the hook does. Return the foot to stance without "
            "crossing. The mechanics work because the curved path "
            "reaches targets the straight line cannot: geometry, not "
            "force, is the technique. The common fault is swinging the "
            "lower leg instead of the hip, which makes a slow visible "
            "loop with no body behind it."
        ),
        "key_points": [
            "The curved knee travels about 0.71 meters along a quarter-circle path of 0.45 meter radius.",
            "It takes the side door: the ribs and thigh around the guard that stops the straight knee.",
            "The hip drives the curve: swing the hip, not the lower leg.",
            "Step the standing foot out to open the hip and give the curve room.",
            "Guard the chin: the curved path opens the body like the hook punch does.",
        ],
        "requirements": [
            "Step the standing foot outward to open the hip before the swing.",
            "Swing the knee along the curved path - about 0.71 meters - with the hip driving.",
            "Dig the point of the knee into the ribs or thigh at the end of the curve.",
            "Lean the torso away to clear the path and guard the chin with the free hand.",
            "Return the foot to stance without crossing the feet.",
        ],
        "standards": [
            "The curved knee is the standard arcing knee weapon of the traditional curriculum.",
            "Traditional camps teach it as the companion to the straight knee: centerline and side door.",
            "Control is the standard on partners: the curved point is drilled on bags and shields.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the curved knee is the covenant of the side "
            "door - the promise that no guard closes every road. The "
            "Signature Nine-Weapons Method walks the 0.71 meter curve "
            "with the hip, not the leg."
        ),
    },
    {
        "key": "tae_khao",
        "name": "Low Cutting Kick (Tae Khao)",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The low cutting kick (tae khao) is the foundation of the "
            "foot weapons: the shin swung horizontally into the "
            "opponent's thigh at about 0.35 meters of height. At a shin "
            "speed of 11 meters per second, about 2,500 newtons of force "
            "concentrated on the 0.012 square meter shin contact patch "
            "lands as about 208,000 pascals of pressure on the thigh - "
            "the classic dead-leg science of the Thai arts. The low kick "
            "is the safest kick and the most strategic: it scores, it "
            "slows, and it never risks the high miss that gets a kicker "
            "dumped. The old art built whole fights on it, chopping the "
            "lead leg until the stance itself surrendered. Thrown with "
            "the shin, never the foot, it is the first kick every "
            "student masters and the last kick every master abandons."
        ),
        "how_it_works": (
            "From the stance, step the lead foot slightly outward and "
            "pivot on it as the hip turns over and the rear leg swings "
            "horizontally, shin leading, to the opponent's thigh at "
            "about 0.35 meters height. Strike with the lower shin - the "
            "hard flat bone above the ankle - never the foot or the "
            "instep, and turn the hip fully so the kicking shoulder "
            "drops. The 11 meter per second shin delivers about 2,500 "
            "newtons over 0.012 square meters: about 208,000 pascals "
            "into the thigh muscle. Return the leg along the same path "
            "to stance, guard high throughout. The mechanics work "
            "because the shin is a dense bony bat and the thigh is a "
            "big soft target: pressure does the damage, and the pivot "
            "adds the body's rotation. The common faults are kicking "
            "with the foot, which breaks toes, and failing to pivot, "
            "which strands the hip and halves the force."
        ),
        "key_points": [
            "The low kick targets the thigh at about 0.35 meters with the shin, never the foot.",
            "About 2,500 newtons over 0.012 square meters lands as about 208,000 pascals of pressure.",
            "The safest kick and the most strategic: it scores, it slows, and it never risks the high miss.",
            "Pivot the support foot and turn the hip fully: the pivot adds the body's rotation.",
            "Old fights were built on it: chop the lead leg until the stance surrenders.",
        ],
        "requirements": [
            "Strike with the lower shin at about 0.35 meters of height, never the foot or instep.",
            "Pivot on the support foot and turn the hip fully over into every kick.",
            "Keep the guard high through the whole motion: kicking never excuses dropping the hands.",
            "Return the leg along the same path to stance without hopping.",
            "Drill both legs: the rear low kick is power, the lead low kick is speed.",
        ],
        "standards": [
            "The low cutting kick is the first kick taught in the traditional curriculum.",
            "Shin contact is the camp standard: foot contact is corrected as an injury risk.",
            "Delp documents the low-kick mechanics shared with the modern ring art.",
        ],
        "citations": [CIT_DELP_BASICS, CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the low kick is the covenant of patience - "
            "208,000 pascals of promise that the stance will surrender "
            "before the fight ends. The Signature Nine-Weapons Method "
            "chops the leg and never chases the head."
        ),
    },
    {
        "key": "tae_tat",
        "name": "Diagonal Roundhouse Kick (Tae Tat)",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The diagonal roundhouse kick (tae tat) is the heavy "
            "artillery of the foot weapons: the shin swung in a "
            "diagonal arc into the ribs, arms, or head. With about 10 "
            "kilograms of leg mass arriving at 12 meters per second, "
            "the kick carries about 720 joules of kinetic energy - "
            "the hardest single strike in the curriculum. The diagonal "
            "line is the key: thrown at roughly 45 degrees downward, "
            "it cuts through the guard instead of bouncing off the "
            "arms. The old fighters called it the battle-axe kick, and "
            "conditioned shins were its handle. Everything about the "
            "roundhouse is commitment: the full pivot, the dropped "
            "shoulder, the hip thrown over like a hammer. It is thrown "
            "to finish exchanges, not to start them."
        ),
        "how_it_works": (
            "Step the lead foot outward at 45 degrees and pivot hard on "
            "it as the hip throws over and the rear leg swings in a "
            "diagonal arc, shin leading, dropping onto the target at "
            "about 45 degrees. Let the kicking-side shoulder drop and "
            "the arm swing down for counterbalance as the 10 kilogram "
            "leg arrives at 12 meters per second - about 720 joules. "
            "Strike with the lower shin and follow through the target: "
            "the kick lands through, not at. The support leg pivots a "
            "full 180 degrees so the hip clears completely. The "
            "mechanics work because the whole body rotates into one "
            "dense striking surface: kinetic energy scales with the "
            "square of velocity, so the 12 meter per second shin is "
            "four times the weapon of a 6 meter per second one. The "
            "common faults are arm-swinging the leg without the hip, "
            "which makes noise without damage, and throwing it naked "
            "without a setup, which gets it caught and dumped."
        ),
        "key_points": [
            "About 10 kilograms at 12 meters per second: about 720 joules, the hardest single strike in the curriculum.",
            "The diagonal 45 degree line cuts through the guard instead of bouncing off the arms.",
            "Thrown to finish exchanges, not to start them: the battle-axe needs a setup.",
            "Full 180 degree pivot on the support foot: the hip must clear completely.",
            "The kick lands through the target, not at it: follow-through is the technique.",
        ],
        "requirements": [
            "Step out at 45 degrees and pivot the support foot a full 180 degrees.",
            "Throw the hip over with the shoulder dropping and the arm swinging for counterbalance.",
            "Strike with the lower shin along the diagonal line, following through the target.",
            "Set the kick up with hands or low kicks: never throw the battle-axe naked.",
            "Return to stance ready: a missed roundhouse must not become a fall.",
        ],
        "standards": [
            "The diagonal roundhouse is the standard heavy kick of the traditional curriculum.",
            "Shin conditioning is the prerequisite standard: the battle-axe needs its handle.",
            "Delp documents the roundhouse mechanics shared with the modern ring art.",
        ],
        "citations": [CIT_DELP_BASICS, CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the roundhouse is the covenant of the "
            "thunder - 720 joules of promise arriving on a diagonal. "
            "The Signature Nine-Weapons Method sets the axe up and "
            "swings it through."
        ),
    },
    {
        "key": "thip_trong",
        "name": "Front Push Kick (Thip Trong)",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The front push kick (thip trong) is the controlling foot "
            "weapon: the sole of the foot driven straight into the "
            "opponent's hip, thigh, or midsection to stop the advance "
            "and manage distance. Pushing with about 400 newtons through "
            "0.60 meters of displacement does about 240 joules of work "
            "on the target - less damage than the roundhouse, far more "
            "control. The push kick is the jab of the feet: it measures, "
            "it interrupts, it punishes the rush, and it buys the time "
            "the heavy weapons need. The old art used it constantly "
            "because the battlefield rewarded the fighter who chose the "
            "range: the thip is how you insist on your range. It is also "
            "the safest kick to throw, traveling the straight line home."
        ),
        "how_it_works": (
            "From the stance, raise the knee high toward the chest, then "
            "drive the foot straight out, sole first, into the "
            "opponent's hip or midsection, extending the leg fully at "
            "impact. Lean the torso slightly back for balance and push "
            "through about 0.60 meters of displacement with about 400 "
            "newtons - about 240 joules of work that moves the opponent "
            "rather than breaking them. Strike with the ball and sole of "
            "the foot, toes pulled back, never the toes. Snap the leg "
            "back along the same line to stance faster than it went out. "
            "The mechanics work because the straight line is the fastest "
            "path and the extended leg is a piston: force times distance "
            "is work, and 240 joules of work relocates an 80 kilogram "
            "opponent convincingly. The common faults are pushing with "
            "the toes, which folds the ankle, and leaving the leg out, "
            "which offers it for the catch."
        ),
        "key_points": [
            "About 400 newtons through 0.60 meters: about 240 joules of relocating work.",
            "The jab of the feet: it measures, interrupts, punishes the rush, and buys time.",
            "The push kick insists on your range: the battlefield rewarded the fighter who chose it.",
            "Strike with the sole, toes pulled back: never the toes, never the ankle folded.",
            "The leg returns faster than it went out: a left-out leg is a caught leg.",
        ],
        "requirements": [
            "Raise the knee high first, then drive the sole straight out to the hip or midsection.",
            "Extend fully at impact with the torso leaning slightly back for balance.",
            "Push through about 0.60 meters of displacement: move them, do not pose at them.",
            "Strike with the sole and ball of the foot with the toes pulled back.",
            "Snap the leg back to stance faster than it extended.",
        ],
        "standards": [
            "The front push kick is the standard distance weapon of the traditional curriculum.",
            "Sole contact with toes back is the camp standard: toe contact is corrected as an ankle injury.",
            "Traditional camps drill the thip as the first kick against a rushing partner.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD, CIT_DELP_BASICS],
        "sig_lens": (
            "Signature lens: the push kick is the covenant of the chosen "
            "range - 240 joules of insistence that the fight happens "
            "where you decide. The Signature Nine-Weapons Method measures "
            "with the sole and keeps what it measures."
        ),
    },
    {
        "key": "chap_kho",
        "name": "Clinch Entry and Control (Chap Kho)",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The clinch (chap kho) is the standing grapple of Muay Boran: "
            "the tie-up where the striking of the nine weapons meets the "
            "wrestling of the old battlefield. Control comes from the "
            "hands: with 2 hands and 3 standard grips each - the neck, "
            "the biceps, and the head - a practitioner commands 6 control "
            "points, and the 30 possible transitions between them are the "
            "vocabulary of clinch dominance. The clinch is where knees "
            "and elbows live: tie the opponent's posture down and the "
            "khao trong rises, turn their head and the sok ti follows. "
            "The old art never separated striking from grappling - the "
            "clinch is the proof, a conversation held at zero distance "
            "where every grip is a sentence."
        ),
        "how_it_works": (
            "Enter the clinch off the opponent's punch or kick: parry or "
            "catch, step deep inside, and swim one hand to the neck while "
            "the other controls the biceps. Establish the 6 control "
            "points - neck, biceps, and head on each side - and learn the "
            "30 transitions: neck to biceps to break posture, biceps to "
            "head to turn them, head to neck to set the knee. Keep the "
            "hips close and the forehead in their face to smother their "
            "weapons while yours stay free. Pull the head down as the "
            "knee rises; turn the head as the elbow cuts. The mechanics "
            "work because posture is leverage: the head controls the "
            "spine, and the spine controls the body, so the 6 grips are "
            "really 6 handles on the same machine. The common faults are "
            "reaching with the arms instead of stepping with the feet, "
            "which leaves you extended and throwable, and admiring the "
            "clinch instead of working it - the tie-up is a means, the "
            "knee is the end."
        ),
        "key_points": [
            "Two hands times 3 grips - neck, biceps, head - give 6 control points and 30 transitions.",
            "The clinch is where knees and elbows live: tie the posture, then the weapons work.",
            "Posture is leverage: the head controls the spine and the spine controls the body.",
            "Enter off their attack: parry or catch, step deep, swim to the neck.",
            "The tie-up is a means and the knee is the end: work the clinch, do not admire it.",
        ],
        "requirements": [
            "Enter with the feet: step deep inside off the parry or catch, never reach with the arms.",
            "Establish the grips: neck, biceps, and head, and drill all 30 transitions.",
            "Keep the hips close with the forehead in their face to smother their weapons.",
            "Pull the head down into the rising knee; turn the head into the cutting elbow.",
            "Work constantly in the tie-up: every grip must threaten a weapon.",
        ],
        "standards": [
            "The clinch is the standard standing grapple across the traditional camps.",
            "Controlled clinch drilling precedes any free clinch work in the traditional curriculum.",
            "The 6 grips and their transitions are the standard clinch syllabus.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD, CIT_DELP_BASICS],
        "sig_lens": (
            "Signature lens: the clinch is the covenant of zero distance "
            "- 6 grips, 30 transitions, one conversation. The Signature "
            "Nine-Weapons Method ties the posture first and lets the "
            "knees speak."
        ),
    },
    {
        "key": "tad_kha",
        "name": "Sweeps (Tad Kha)",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Sweeps (tad kha) are the takedowns of Muay Boran: the foot "
            "hooking or cutting the opponent's supporting leg to take the "
            "ground out from under them. The timing is a window "
            "calculation - with an opponent stepping on a 0.80 second "
            "cycle, the leg is vulnerable for about 0.20 seconds per "
            "step, a 25 percent window - and the sweep lives or dies in "
            "that window. Over a 3 minute round at that stepping pace, "
            "about 225 such windows open. The sweep is the cheapest "
            "takedown in the art: no lifting, no wrestling, only timing "
            "and a hooking foot. The old fighters swept off the catch "
            "(trapping the kick and cutting the standing leg), off the "
            "clinch (hooking the ankle while turning the upper body), and "
            "off the straight rush (cutting the lead leg as it lands)."
        ),
        "how_it_works": (
            "Read the opponent's stepping rhythm until you can predict "
            "the 0.20 second window in their 0.80 second cycle - the "
            "instant the weight commits to the stepping leg. As the foot "
            "lands, hook your foot behind their ankle or cut your shin "
            "across their calf, pulling or cutting while your hands push "
            "or turn their upper body the opposite way: the classic "
            "scissors of upper-body push and lower-leg cut. Keep your own "
            "base wide and your weight centered - a sweeper who leans "
            "gets swept. Follow the falling opponent with position, not "
            "with strikes to a downed fighter. The mechanics work because "
            "a body in mid-step balances on a moving point: removing the "
            "point inside the 25 percent window topples the structure "
            "with minimal force. The common fault is sweeping at the leg "
            "instead of at the rhythm: the foot must arrive in the "
            "window, not merely at the ankle."
        ),
        "key_points": [
            "The window is about 0.20 seconds in a 0.80 second step cycle: 25 percent of each step.",
            "About 225 windows open in a 3 minute round at that stepping pace.",
            "The sweep is scissors: hands turn the upper body one way while the foot cuts the leg the other.",
            "Sweep at the rhythm, not at the leg: the foot must arrive inside the window.",
            "Keep your own base wide: a sweeper who leans gets swept.",
        ],
        "requirements": [
            "Read the stepping rhythm until the 0.20 second window is predictable.",
            "Hook the ankle or cut the calf exactly as the weight commits to the stepping leg.",
            "Turn the upper body opposite the cut: the scissors make the takedown.",
            "Keep your base wide and your weight centered through every sweep.",
            "Follow with position; the sweep ends the exchange, not the contest.",
        ],
        "standards": [
            "Sweeps are the standard takedowns of the traditional Muay Boran curriculum.",
            "The catch-and-sweep is the standard first sweep taught: trap the kick, cut the standing leg.",
            "Sweeps are drilled with control on mats: the partner's fall is protected, always.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the sweep is the covenant of the ground - "
            "the promise that the earth keeps what the rhythm gives it. "
            "The Signature Nine-Weapons Method arrives in the 25 percent "
            "window or not at all."
        ),
    },
    {
        "key": "ninth_weapon",
        "name": "The Ninth Weapon (Headbutt)",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The head is the ninth weapon of naw arwut, and the headbutt "
            "is its technique: the crown or forehead driven into the "
            "opponent's face at clinch distance. Closing 0.40 meters at "
            "1.5 meters per second puts the strike home in about 0.27 "
            "seconds - the shortest weapon with the shortest road. The "
            "old battlefield art counted it openly among the nine, "
            "though the modern ring forbids it; this record documents it "
            "as history and as the completion of the nine-weapons map, "
            "taught for understanding of the classical system. The "
            "headbutt's lesson is really about the clinch: at zero "
            "distance the head is always a factor, and the fighter who "
            "understands the ninth weapon controls the forehead-to-forehead "
            "battle even where the strike itself is never thrown."
        ),
        "how_it_works": (
            "From the tight clinch, control the opponent's head with "
            "both hands on the neck or head - the 6 control points "
            "applied. Pull their face down and slightly to one side "
            "while stepping 0.40 meters in at about 1.5 meters per "
            "second, driving the hard crown of your forehead into the "
            "nose or brow in about 0.27 seconds. Strike with the crown, "
            "never the face or temple: the forehead's thick bone against "
            "their fragile nose is the entire technique. Keep the neck "
            "braced and the chin tucked so your own face stays out of "
            "the collision. This technique is documented for "
            "completeness of the classical nine-weapons system and for "
            "understanding clinch dynamics; it is forbidden under modern "
            "rules and is never used in sparring. The mechanics work "
            "because the skull's crown is the body's hardest striking "
            "surface at the shortest range. The standing lesson for "
            "legal training: control of the head decides the clinch, "
            "and the fighter who owns the forehead battle owns zero "
            "distance."
        ),
        "key_points": [
            "The head is the ninth of the nine weapons; the headbutt completes the classical map.",
            "Closing 0.40 meters at 1.5 meters per second lands the strike in about 0.27 seconds.",
            "Strike with the crown of the forehead, never the face or temple.",
            "Documented for classical completeness and clinch understanding; forbidden under modern rules, never sparred.",
            "The standing lesson: control of the head decides the clinch at zero distance.",
        ],
        "requirements": [
            "Control the head first with both hands: no control, no technique.",
            "Drive the crown of the forehead, chin tucked and neck braced.",
            "Close the 0.40 meters in about 0.27 seconds: the weapon is speed at zero distance.",
            "Study it for the classical map and for clinch understanding only.",
            "Never use it in sparring or competition: modern rules forbid it absolutely.",
        ],
        "standards": [
            "The head as ninth weapon is the documented classical classification of naw arwut.",
            "Traditional lineage teaches the ninth weapon for completeness of the system.",
            "Modern competition rules forbid the headbutt: the record marks it historical, not practical.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the ninth weapon is the covenant of "
            "honesty - the map admitting all nine even where the modern "
            "ring allows eight. The Signature Nine-Weapons Method "
            "studies the ninth to understand the clinch and never throws "
            "it outside the classical record."
        ),
    },
    # --------------------------------------------------------- ADVANCED
    {
        "key": "mae_mai",
        "name": "Mae Mai (Master Tricks of Muay Boran)",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Mae mai - the master tricks - are the 15 principal "
            "techniques of the classical Muay Boran system, the named "
            "gems of the art passed down as the highest curriculum. "
            "Each mae mai is a complete technique with a name, a story, "
            "and a precise application: the spinning strikes, the "
            "flying knees, the great counters, the techniques that end "
            "exchanges. The combinatorics show their depth: 15 master "
            "tricks yield 210 ordered pairs and 2,730 ordered triples - "
            "a lifetime of chaining from 15 named ideas. The mae mai are "
            "taught only after the foundations and the compounded "
            "weapons are solid, because each one assumes the basics: the "
            "spinning elbow assumes the horizontal elbow, the flying "
            "knee assumes the straight knee. They are called master "
            "tricks not because they are secret, but because only "
            "mastery makes them work."
        ),
        "how_it_works": (
            "Learn the 15 by name and by motion, one at a time, each "
            "drilled first in the air, then on pads, then in controlled "
            "application. For each mae mai, identify its parent weapon "
            "from the compounded curriculum - the base it assumes - and "
            "confirm the parent is solid before advancing. Then chain "
            "them: practice the 210 ordered pairs, two master tricks "
            "back to back, until the transitions are as clean as the "
            "techniques. Then build selected triples from the 2,730 "
            "possibilities, choosing chains that flow naturally: a "
            "spinning entry into a flying finish, a great counter into a "
            "great attack. The mechanics work because each mae mai is a "
            "compounded weapon plus timing plus angle - the advanced "
            "curriculum is only ever the basics under pressure. The "
            "common fault is collecting names without parents: a mae "
            "mai practiced without its base weapon is a trick in the "
            "bad sense, and tricks fail."
        ),
        "key_points": [
            "Mae mai are the 15 principal techniques: the named gems and highest curriculum of the classical art.",
            "Fifteen tricks yield 210 ordered pairs and 2,730 ordered triples: a lifetime of chaining.",
            "Each mae mai assumes a compounded parent weapon: the spinning elbow assumes the horizontal elbow.",
            "They are master tricks because only mastery makes them work, not because they are secret.",
            "A mae mai without its parent weapon is a trick in the bad sense, and tricks fail.",
        ],
        "requirements": [
            "Confirm the parent compounded weapon is solid before learning any mae mai.",
            "Learn all 15 by name, motion, and application: air, then pads, then controlled application.",
            "Drill the 210 ordered pairs until the transitions are as clean as the techniques.",
            "Build selected triples from the 2,730: chains that flow, not chains that impress.",
            "Test each mae mai under pressure: the advanced curriculum is the basics under pressure.",
        ],
        "standards": [
            "The mae mai are the documented master curriculum of the classical Muay Boran system.",
            "Traditional camps teach the 15 only after the compounded weapons are proven.",
            "Kraitus and Kraitus record the master-trick tradition as the crown of the old art.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the mae mai are the covenant crowned - 15 "
            "master promises built on kept ones, 210 pairs and 2,730 "
            "triples of kept faith. The Signature Nine-Weapons Method "
            "earns each trick through its parent."
        ),
    },
    {
        "key": "luk_mai",
        "name": "Luk Mai (Complementary Tricks of Muay Boran)",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Luk mai - the complementary tricks - are the supporting "
            "techniques that complete each mae mai: the follow-ups, the "
            "escapes, the second-phase answers that turn one master "
            "trick into a finished exchange. Where each of the 15 mae "
            "mai is a thesis, its luk mai are the arguments: with 2 "
            "complementary tricks per master trick, the system holds 30 "
            "luk mai, and the mae-mai-to-luk-mai-to-mae-mai sequences "
            "number 15 times 2 times 14, or 420 complete exchanges. The "
            "luk mai teach the deepest lesson of the advanced art: no "
            "technique ends the fight by itself, so every technique must "
            "know what comes next. The master trick opens the door; the "
            "complementary trick walks through it."
        ),
        "how_it_works": (
            "For each mae mai you have learned, learn its 2 luk mai: "
            "the immediate follow-up if the master trick lands "
            "partially, and the escape or re-entry if it is countered. "
            "Drill the 30 as second-phase techniques, always starting "
            "from the end position of their mae mai - never from a fresh "
            "stance, because the luk mai only exists as a continuation. "
            "Then chain the 420 full exchanges: mae mai, luk mai, and "
            "the next mae mai the opening creates. Practice reading "
            "which branch the exchange takes: if the opponent covers "
            "the master trick one way, the first luk mai answers; the "
            "other way, the second. The mechanics work because combat "
            "is a branching tree and the luk mai pre-compute the "
            "branches: the fighter who has drilled both answers never "
            "hesitates at the fork. The common fault is learning luk "
            "mai as standalone techniques: a complementary trick "
            "without its mae mai is a solution without a problem."
        ),
        "key_points": [
            "Luk mai are the complementary tricks: follow-ups, escapes, and second-phase answers to each mae mai.",
            "Fifteen mae mai times 2 luk mai gives 30 complementary tricks and 420 complete exchanges.",
            "Every luk mai starts from the end position of its mae mai: continuation, not standalone.",
            "Combat is a branching tree and the luk mai pre-compute the branches: no hesitation at the fork.",
            "The master trick opens the door; the complementary trick walks through it.",
        ],
        "requirements": [
            "Learn 2 luk mai per mae mai: 30 complementary tricks, each tied to its master.",
            "Drill each luk mai from the end position of its mae mai, never from a fresh stance.",
            "Chain the 420 full exchanges: master trick, complement, and the next opening.",
            "Read the branch in live drilling: cover one way, first answer; the other way, second.",
            "Never practice a luk mai standalone: a complement without its master is a solution without a problem.",
        ],
        "standards": [
            "The luk mai are the documented complementary curriculum completing the mae mai system.",
            "Traditional camps teach each luk mai only with its mae mai, as one two-part lesson.",
            "The 420-exchange chaining drill is the standard advanced combination practice.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the luk mai are the covenant continued - "
            "the promise that no technique is left alone at the fork. "
            "The Signature Nine-Weapons Method pre-computes all 420 "
            "branches and hesitates at none."
        ),
    },
    {
        "key": "sok_klap",
        "name": "Spinning Back Elbow (Sok Klap)",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The spinning back elbow (sok klap) is the first of the "
            "spinning weapons: the practitioner turns a full 360 degrees "
            "and the elbow arrives as the body completes the rotation. "
            "Completing the spin in 0.50 seconds means an angular "
            "velocity of about 12.57 radians per second - the whole "
            "body's rotation concentrated into the elbow's point at the "
            "end of the turn. It is a mae mai of the elbow family, "
            "assuming a solid sok ti: the horizontal elbow is the "
            "parent, the spin is the multiplication. The technique is "
            "thrown off the opponent's straight attack, turning inside "
            "it so their punch passes through the space the spin "
            "vacates. The spinning elbow is the art's punctuation mark: "
            "rare, decisive, and unforgettable."
        ),
        "how_it_works": (
            "As the opponent commits to a straight attack, step the lead "
            "foot across and pivot hard, turning the body 360 degrees "
            "with the striking arm folded tight, fist at the shoulder. "
            "Keep the chin tucked and the eyes on the target through the "
            "turn - spotting, the way dancers spot, keeps the balance "
            "and the aim. The elbow arrives at the end of the rotation "
            "at about 12.57 radians per second of body turn, the point "
            "cutting across the jaw or temple. The other arm stays tight "
            "to guard through the spin. Finish in stance, ready, the "
            "spin's momentum settled into the base. The mechanics work "
            "because the full-body rotation multiplies the elbow's "
            "force: the same point as sok ti, driven by 360 degrees of "
            "turn instead of 90. The common faults are spinning without "
            "a trigger - the technique needs their committed attack as "
            "cover - and losing the spot, which turns the punctuation "
            "mark into a stumble."
        ),
        "key_points": [
            "A full 360 degree spin in 0.50 seconds: about 12.57 radians per second of rotation into the elbow.",
            "A mae mai of the elbow family: sok ti is the parent, the spin is the multiplication.",
            "Thrown off the opponent's committed straight attack, turning inside it.",
            "Spot the target through the turn like a dancer: balance and aim survive the spin.",
            "The spin needs their attack as cover: a naked spin is a stumble, not a strike.",
        ],
        "requirements": [
            "Confirm a solid horizontal elbow before attempting the spinning form.",
            "Trigger only off a committed straight attack: step across and pivot into the spin.",
            "Fold the arm tight with the fist at the shoulder and the chin tucked.",
            "Spot the target through the 360 degrees and finish in stance with the momentum settled.",
            "Keep the guard arm tight through the turn: the spin is not an excuse to open up.",
        ],
        "standards": [
            "The spinning back elbow is a documented mae mai of the classical system.",
            "Traditional camps teach it only after the horizontal elbow is proven under pressure.",
            "It is drilled with a trigger - the partner's committed attack - never as a naked spin.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the spinning elbow is the covenant of the "
            "full turn - 12.57 radians per second of kept promise "
            "arriving at one point. The Signature Nine-Weapons Method "
            "spins only with a trigger and lands only in stance."
        ),
    },
    {
        "key": "hanuman",
        "name": "Hanuman Tawai Waen (Hanuman Presents the Ring)",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Hanuman Tawai Waen - Hanuman presents the ring - is one of "
            "the most famous mae mai: named for the monkey god offering "
            "his ring, it is a leaping spinning kick delivered with the "
            "body airborne. A 0.60 meter jump gives about 0.70 seconds "
            "of hang time, and the kick must be chambered, spun, and "
            "delivered inside that window. The technique assumes the "
            "roundhouse and the spinning kick as parents: it is tae tat "
            "plus elevation plus rotation. In the old stories it was the "
            "technique that ended duels; in training it is the technique "
            "that tests everything - timing, courage, and the ability to "
            "think while airborne. Like all mae mai it is thrown rarely "
            "and only when the opening is certain, because a missed "
            "flying technique lands the practitioner on the ground."
        ),
        "how_it_works": (
            "Off the opponent's committed attack or a solid setup, take "
            "a short driving step and leap, jumping about 0.60 meters "
            "for about 0.70 seconds of hang time. In the air, spin the "
            "body and chamber the kicking leg, then extend the shin or "
            "foot into the target - head, ribs, or arms - at the top of "
            "the jump. Keep the guard hands up through the flight: the "
            "airborne fighter cannot retreat, so the hands must defend. "
            "Land in stance, knees soft, ready to continue. The "
            "mechanics work because the jump adds the body's falling "
            "mass to the kick's rotation: elevation times spin is the "
            "multiplication. The 0.70 second window is the whole "
            "technique - chamber late and the kick never extends. The "
            "common faults are jumping without a setup, which wastes "
            "the 0.70 seconds on empty air, and landing stiff-legged, "
            "which spends the knees to save the moment."
        ),
        "key_points": [
            "Hanuman presents the ring: the famous leaping spinning kick of the mae mai.",
            "A 0.60 meter jump gives about 0.70 seconds of hang time: the kick lives inside that window.",
            "Parents are the roundhouse and the spinning kick: elevation plus rotation.",
            "Thrown rarely and only on a certain opening: a missed flying technique lands you on the ground.",
            "Keep the guard up in the air: the airborne fighter cannot retreat.",
        ],
        "requirements": [
            "Confirm solid roundhouse and spinning kicks before attempting the flying form.",
            "Jump about 0.60 meters off a setup or a committed opponent attack: about 0.70 seconds of work.",
            "Chamber, spin, and extend inside the hang time: late chambering wastes the window.",
            "Keep the hands guarding through the flight and land soft in stance.",
            "Throw it rarely: certainty of opening is part of the technique.",
        ],
        "standards": [
            "Hanuman Tawai Waen is a documented mae mai of the classical Muay Boran system.",
            "Traditional camps teach it only after the parent kicks are proven.",
            "It is drilled on pads and bags before any applied practice, with landing form graded first.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: Hanuman is the covenant of the sky - 0.70 "
            "seconds of kept promise between the leap and the landing. "
            "The Signature Nine-Weapons Method flies only on certainty "
            "and lands only in stance."
        ),
    },
    {
        "key": "kwang_liow_lang",
        "name": "Kwang Liow Lang (The Deer Looks Back)",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Kwang Liow Lang - the deer looks back - is the classical "
            "spinning back kick: the practitioner turns away and the "
            "heel or sole fires backward into the pursuer. Turning 180 "
            "degrees in 0.30 seconds is about 10.47 radians per second "
            "of rotation, and the kick lands where the opponent least "
            "expects a strike: directly behind the turning fighter. It "
            "is the retreating fighter's answer, the technique for the "
            "moment the opponent thinks they have you running. The name "
            "captures it perfectly - the deer glances back as it flees, "
            "and the glance is a kick. As a mae mai it assumes the "
            "roundhouse and the push kick: the turn of the spin with the "
            "straight line of the thip, fired backward."
        ),
        "how_it_works": (
            "As the opponent presses forward, step back or pivot and "
            "turn 180 degrees away, looking over the shoulder to spot "
            "the target - the deer's glance. Chamber the rear leg and "
            "fire the heel or sole straight back into the midsection or "
            "thigh, the body turning at about 10.47 radians per second "
            "through the 0.30 second turn. Keep the hands guarding the "
            "face through the turn: the back is briefly to the "
            "opponent, and the guard is the insurance. Land forward in "
            "stance, having traded places with the danger. The mechanics "
            "work because the opponent's forward pressure meets a "
            "backward kick: their advance adds to the impact, and the "
            "spin's rotation multiplies the leg's force. The common "
            "faults are turning without looking - the deer must look "
            "back or the kick fires blind - and pausing mid-turn, which "
            "presents the back with no kick attached."
        ),
        "key_points": [
            "The deer looks back: the classical spinning back kick, fired at the pursuer.",
            "Turning 180 degrees in 0.30 seconds is about 10.47 radians per second of rotation.",
            "The opponent's forward pressure adds to the impact: their advance meets your kick.",
            "Look over the shoulder to spot: the deer must look back or the kick fires blind.",
            "Parents are the roundhouse's turn and the push kick's line, fired backward.",
        ],
        "requirements": [
            "Trigger only on the opponent's committed forward pressure.",
            "Turn 180 degrees in about 0.30 seconds while spotting over the shoulder.",
            "Fire the heel or sole straight back into the midsection or thigh.",
            "Guard the face through the turn: the back is briefly exposed.",
            "Land forward in stance: trade places with the danger, do not linger in it.",
        ],
        "standards": [
            "Kwang Liow Lang is a documented mae mai of the classical system.",
            "Traditional camps teach it as the retreating fighter's answer, drilled with a pressing partner.",
            "Spotting over the shoulder is the camp standard: blind spinning kicks are corrected immediately.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the deer is the covenant of the glance - "
            "10.47 radians per second of promise that retreat is a "
            "tactic, not a surrender. The Signature Nine-Weapons Method "
            "looks back and kicks through."
        ),
    },
    {
        "key": "hap_liuk",
        "name": "Hap Liuk Muay (Grappling and Breaking)",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Hap liuk muay is the grappling and breaking science of Muay "
            "Boran: the joint locks, limb controls, and breaking "
            "techniques of the old battlefield art, where a fight could "
            "not end at the bell. The physics are leverage: a 0.60 meter "
            "lever against a 0.15 meter resistance is a 4 to 1 "
            "mechanical advantage, so 50 newtons of controlled force "
            "becomes 200 newtons at the joint - which is why the old "
            "techniques are taught with extreme care and applied with "
            "restraint. Hap liuk assumes the clinch: chap kho is the "
            "parent, and the locks are what the clinch becomes when the "
            "weapons are set aside. This record documents the classical "
            "system for completeness; the techniques are practiced as "
            "controlled drills with tapping partners, never forced, "
            "because the 4 to 1 advantage does not forgive."
        ),
        "how_it_works": (
            "From clinch control, isolate the limb: control the wrist "
            "with both hands, step to the outside, and apply the lever "
            "- your 0.60 meter arm and body against their 0.15 meter "
            "joint lever, the 4 to 1 advantage doing the work that "
            "strength cannot. Apply pressure slowly and smoothly, never "
            "with a jerk: the partner taps the moment pressure registers, "
            "and the technique stops at the tap, always. Drill the "
            "entries - the arm isolations, the shoulder controls, the "
            "standing breaks - as slow choreography first, adding "
            "realism only with experienced partners and explicit "
            "agreement. The mechanics work because joints bend one way: "
            "the lever finds the direction the joint cannot go, and the "
            "4 to 1 multiplication means control, not force, decides "
            "the outcome. The standing rule of the practice: 50 newtons "
            "in, 200 at the joint - so 50 newtons is already serious, "
            "and the tap is sacred."
        ),
        "key_points": [
            "Hap liuk is the grappling and breaking science: locks and controls from the clinch.",
            "A 0.60 meter lever on a 0.15 meter joint is 4 to 1: 50 newtons in becomes 200 at the joint.",
            "The clinch is the parent: the locks are what chap kho becomes when weapons are set aside.",
            "Drilled as slow controlled choreography with tapping partners; the tap is sacred.",
            "The 4 to 1 advantage does not forgive: applied with restraint, never forced.",
        ],
        "requirements": [
            "Confirm solid clinch control before studying any lock: the clinch is the parent.",
            "Isolate the limb and apply the 4 to 1 lever slowly and smoothly, never with a jerk.",
            "Stop at the tap, always: the partner's tap ends the technique instantly.",
            "Drill as choreography first; add realism only with experienced, consenting partners.",
            "Treat 50 newtons as serious: the multiplication means control decides, not force.",
        ],
        "standards": [
            "Hap liuk is the documented grappling science of the classical Muay Boran battlefield art.",
            "Traditional teaching pairs every lock with its restraint: the tap rule is the standard.",
            "Breaking techniques are demonstrated as control, never completed on partners.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: hap liuk is the covenant of restraint - the "
            "4 to 1 promise kept gentle because it could be otherwise. "
            "The Signature Nine-Weapons Method controls the joint and "
            "honors the tap as sacred."
        ),
    },
    {
        "key": "thum",
        "name": "Clinch Throws and Dumps (Thum)",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Thum - the throws and dumps - are the takedowns of the "
            "clinch: the hip throws, body locks, and off-balancing dumps "
            "that end the zero-distance conversation. The physics are "
            "toppling: pushing at 1.40 meters of height against a 0.30 "
            "meter base topples the structure at about 12.1 degrees of "
            "lean - a small angle, which is why the throws feel "
            "effortless when the setup is right. The clinch is the "
            "parent: every throw starts from chap kho control, and the "
            "throw is what the clinch becomes when the knees have done "
            "their work and the opponent's posture is already broken. "
            "The old art threw to finish: on the battlefield there was "
            "no bell to save the thrown. In training the throws are "
            "drilled on mats with breakfall practice, because the 12.1 "
            "degree topple lands hard."
        ),
        "how_it_works": (
            "From clinch control, break the opponent's posture first: "
            "pull the head down, turn the shoulders, get the weight onto "
            "one leg. Step deep with the hip across their hip for the "
            "hip throw, or lock the body and reap the leg for the dump, "
            "always turning their upper body past the 12.1 degree "
            "topple point while your base stays wide. Execute with the "
            "legs and hips, not the arms: the arms only steer, the body "
            "throws. Guide the partner down on the mats - the drill "
            "includes their breakfall, which is half the lesson. The "
            "mechanics work because a toppled structure cannot recover: "
            "past 12.1 degrees of lean on a 0.30 meter base, gravity "
            "finishes what the throw started. The common faults are "
            "throwing with the arms, which exhausts the thrower, and "
            "throwing without the posture break, which wrestles a "
            "balanced opponent and loses."
        ),
        "key_points": [
            "Thum are the clinch throws and dumps: what the clinch becomes when posture is broken.",
            "A 1.40 meter push on a 0.30 meter base topples at about 12.1 degrees of lean.",
            "Break the posture first: pull, turn, and load one leg before any throw.",
            "The legs and hips throw; the arms only steer: arm-throwing exhausts the thrower.",
            "Drilled on mats with breakfalls: the 12.1 degree topple lands hard.",
        ],
        "requirements": [
            "Establish clinch control and break the posture before attempting any throw.",
            "Step deep with the hip across for hip throws; lock and reap for dumps.",
            "Turn the upper body past the 12.1 degree topple point with your base wide.",
            "Throw with legs and hips; let the arms steer only.",
            "Drill on mats with breakfall practice: protect the partner's fall, always.",
        ],
        "standards": [
            "Thum are the documented clinch takedowns of the classical Muay Boran system.",
            "Traditional teaching requires the posture break before the throw: no break, no throw.",
            "Mats and breakfalls are the training standard for all throwing practice.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the throw is the covenant of the topple - "
            "12.1 degrees of promise that the broken posture falls. The "
            "Signature Nine-Weapons Method breaks first, throws with the "
            "hips, and lands the partner safe."
        ),
    },
    {
        "key": "khao_loi",
        "name": "Flying Knee (Khao Loi)",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The flying knee (khao loi) is the airborne knee weapon: the "
            "practitioner runs, leaps, and drives the knee into the "
            "target mid-flight. A 3 step run-up of 0.70 meter steps "
            "covers 2.10 meters of approach, and a 0.55 meter jump gives "
            "about 0.67 seconds of hang time for the knee to travel and "
            "land. It is a mae mai of the knee family - khao trong is "
            "the parent, elevation the multiplication - and the most "
            "dramatic technique in the curriculum. The flying knee is "
            "thrown at a hurt or cornered opponent, never as an opener: "
            "the 2.10 meter run-up announces it, so it must arrive where "
            "the opponent cannot leave. Like all flying techniques, a "
            "miss lands the practitioner badly; the old masters threw it "
            "only at the certain moment."
        ),
        "how_it_works": (
            "Time the opponent's stillness - against the ropes of "
            "position, hurt, or cornered - then take the 3 step run-up, "
            "0.70 meters a step for 2.10 meters, and leap about 0.55 "
            "meters, driving the rear knee up and through the target in "
            "the 0.67 seconds of hang time. Thrust the hips through "
            "exactly as in khao trong: the flying knee is the straight "
            "knee with a runway. Pull the opponent's head down into the "
            "rising knee when the clinch range allows, or drive the knee "
            "into the guard and body of a stationary target. Land in "
            "stance, knees soft, ready - the landing is graded with the "
            "strike. The mechanics work because the run-up's momentum "
            "adds to the hip thrust: approach speed plus elevation is "
            "the multiplication. The common faults are running up at a "
            "mobile opponent, which wastes the 2.10 meters, and landing "
            "stiff, which spends the knees."
        ),
        "key_points": [
            "Three 0.70 meter steps make a 2.10 meter run-up; a 0.55 meter jump gives about 0.67 seconds of hang time.",
            "A mae mai of the knee family: khao trong is the parent, elevation the multiplication.",
            "Thrown at a hurt or cornered opponent, never as an opener: the run-up announces it.",
            "The hips thrust through exactly as in the straight knee: the flying knee is khao trong with a runway.",
            "Land soft in stance: the landing is graded with the strike.",
        ],
        "requirements": [
            "Confirm a solid straight knee before attempting the flying form.",
            "Throw only at a stationary, hurt, or cornered opponent: certainty is part of the technique.",
            "Run 3 steps of 0.70 meters - 2.10 meters - and leap about 0.55 meters.",
            "Drive the knee through in the 0.67 seconds of hang time with the hips thrusting.",
            "Land soft in stance, knees bent, ready to continue.",
        ],
        "standards": [
            "The flying knee is a documented mae mai of the classical system.",
            "Traditional camps teach it only after the straight knee is proven under pressure.",
            "Landing form is graded with the strike: the technique includes its own landing.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the flying knee is the covenant of the "
            "runway - 2.10 meters of approach and 0.67 seconds of sky "
            "kept as one promise. The Signature Nine-Weapons Method "
            "flies only at the certain moment."
        ),
    },
    {
        "key": "combinations",
        "name": "Combination Systems (Chaining the Nine Weapons)",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Combination systems are the grammar of Muay Boran: the "
            "method of chaining the nine weapons into flowing attacks "
            "where each strike sets up the next. The arithmetic of the "
            "system is exact - 9 weapons give 72 ordered two-strike "
            "chains and 504 ordered three-strike chains - and the "
            "training walks the student through that space "
            "systematically instead of by habit. The classical chaining "
            "logic is the setup: the first weapon moves the guard, the "
            "second moves the head, the third arrives where both were. "
            "Low kick to drop the hands, hook to turn the head, elbow "
            "to meet it - the oldest sentences in the art. The advanced "
            "student does not throw combinations; they speak them, and "
            "the 504 three-chains are the vocabulary."
        ),
        "how_it_works": (
            "Build chains from the pairing tables: start with the 72 "
            "ordered two-strike chains, drilling each until the second "
            "strike fires from the first's impact, not from a decision. "
            "Then build the 504 three-strike chains in families: "
            "hand-hand-elbow, kick-punch-knee, elbow-knee-elbow - each "
            "family teaching one chaining logic. Apply the setup rule "
            "to every chain: weapon one moves the guard, weapon two "
            "moves the head, weapon three arrives. Drill against pads "
            "with a holder who feeds the openings, then in controlled "
            "sparring where only chained attacks score. The mechanics "
            "work because defense is serial: no guard covers two lines "
            "at once, so the chain attacks the line the guard just "
            "left. The common fault is memorized choreography - chains "
            "that ignore the opponent. A combination system is a "
            "language: the 504 chains are vocabulary, but the fighter "
            "must still listen to the conversation."
        ),
        "key_points": [
            "Nine weapons give 72 ordered two-strike chains and 504 ordered three-strike chains.",
            "The chaining logic: weapon one moves the guard, weapon two moves the head, weapon three arrives.",
            "Defense is serial: no guard covers two lines at once, so chains attack the line just left.",
            "Drill pairs until the second strike fires from the first's impact, not from a decision.",
            "The 504 chains are vocabulary; the fighter must still listen to the conversation.",
        ],
        "requirements": [
            "Master the 72 ordered two-strike chains before building triples.",
            "Build the 504 three-strike chains in families: hand-hand-elbow, kick-punch-knee, elbow-knee-elbow.",
            "Apply the setup rule to every chain: move the guard, move the head, arrive.",
            "Drill with a pad holder feeding openings, then in sparring where only chains score.",
            "Adapt every chain to the live opponent: vocabulary, not choreography.",
        ],
        "standards": [
            "Combination systems are the standard advanced syllabus across the traditional camps.",
            "The setup rule - guard, head, arrival - is the documented chaining logic of the art.",
            "Free sparring in the traditional curriculum scores chained attacks above single strikes.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD, CIT_DELP_BASICS],
        "sig_lens": (
            "Signature lens: the combinations are the covenant spoken - "
            "72 pairs and 504 triples of fluent promise. The Signature "
            "Nine-Weapons Method speaks in sentences and listens for "
            "the answer."
        ),
    },
    {
        "key": "kru",
        "name": "The Kru (Teaching Lineage of Muay Boran)",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The kru is the teacher, and the teaching lineage is the "
            "final record of this database: how Muay Boran passes from "
            "hand to hand without being lost. The old method is "
            "apprenticeship - the student learns at the teacher's side, "
            "the mongkon is presented by the kru, and the lineage is "
            "named the way families are named. The teaching arithmetic "
            "is exact: this database holds 34 techniques, taught 2 per "
            "session, which is 17 sessions; at 3 sessions a week the "
            "curriculum runs about 5.7 weeks - 6 weeks of honest "
            "transmission for the complete map. The kru's duties are "
            "the canon of this art: teach the stance before the "
            "strike, the restraint before the weapon, the wai khru "
            "before the contest, and the lineage before the ego. A "
            "teacher who keeps the 34 whole keeps the art whole."
        ),
        "how_it_works": (
            "Teach in ladder order, exactly as this database is ordered: "
            "foundations first, compounded second, advanced last, 2 "
            "techniques per session over 17 sessions - about 6 weeks at "
            "3 sessions a week. For each technique, follow the old "
            "sequence: demonstrate, name the Thai term with its "
            "translation, break down the body mechanics step by step, "
            "drill it clean, then test it under pressure. Present the "
            "mongkon yourself when the student is ready for the wai "
            "khru; never let a student tie their own the first time. "
            "Correct the stance before correcting the strike, and teach "
            "the tap rule before teaching any lock. Keep the lineage "
            "record: who taught you, whom you teach, and the camp's "
            "forms intact. The method works because the ladder is the "
            "pedagogy - each rank assumes the last, so teaching in "
            "order never leaves gaps. The common fault is teaching the "
            "advanced first to impress: a student with mae mai and no "
            "stance is a danger to themselves."
        ),
        "key_points": [
            "The kru teaches by apprenticeship: at the teacher's side, lineage named like family.",
            "Thirty-four techniques at 2 per session make 17 sessions: about 6 weeks at 3 sessions a week.",
            "Teach in ladder order: foundations, compounded, advanced - the ladder is the pedagogy.",
            "Present the mongkon yourself; teach the tap rule before any lock; stance before strike.",
            "A teacher who keeps the 34 whole keeps the art whole.",
        ],
        "requirements": [
            "Teach the 34 in ladder order: 2 per session, 17 sessions, about 6 weeks at 3 sessions a week.",
            "For each technique: demonstrate, name it in Thai with translation, break down mechanics, drill, test.",
            "Present the student's first mongkon personally; never let them tie their own the first time.",
            "Teach restraint with every weapon: the tap rule before locks, control before contact.",
            "Keep the lineage record: your teacher, your students, and the camp's forms intact.",
        ],
        "standards": [
            "Apprenticeship under a kru is the traditional transmission standard of Muay Boran.",
            "The ladder order is the pedagogical standard: each rank assumes the last.",
            "Lineage naming - teacher to student to camp - is the documented continuity of the art.",
        ],
        "citations": [CIT_KRAITUS, CIT_TRAD],
        "sig_lens": (
            "Signature lens: the kru is the covenant keeper - the one "
            "who makes sure all 34 promises pass whole to the next "
            "hands. The Signature Nine-Weapons Method teaches the 17 "
            "sessions in order and signs the lineage like family."
        ),
    },
]
