#!/usr/bin/env python3
"""Entries for the Baguazhang Combat databases (Manon's combat orders 2026-10-17,
combat batch 4 - final round).

Terminology fact-checked 2026-10-17 against Wikipedia 'Baguazhang'
(founder Dong Haichuan 1797-1882, Hebei, originally 'Zhuanzhang'/Turning
Palm, taught in Beijing from about 1864, taught the first three palms -
Single Change, Double Change, Smooth Body - consistently and varied the
last five by student; famous students Yin Fu, Cheng Tinghua, Liang
Zhenpu; circle walking 'turning the circle' as the characteristic stance
and movement training, beginner circle six to twelve feet; weapons
including crescent-shaped deer horn knives unique to the style, wind and
fire wheels, bagua sword, bagua broadsword, staff, spear, cane, hook
sword, judge's pen, straight double-edged sword), New World
Encyclopedia 'Baguazhang' (same founding account; one of the three
principal internal arts alongside xingyiquan and taijiquan), GW Media
'Ba Gua Zhang (Ba Gua Palm)' Kungfu Culture (the Cheng-lineage eight
palm sequence - Dan Huan/Single-change, Shuang Huan/Double-change, Shun
Shi/Go-along, Bei Shen/Back-body, Zhuan Shen/Turn-around, Mo
Shen/Body-grind, Fan Shen/Body-flip, Hui Shen/Body-return - taught in
succession with inexhaustible changes; Tang Ni Bu muddy walk with the
turn and lock in switching moves; palm techniques - pushing,
supporting, leading, moving, hooking, chopping, penetrating, dodging,
intercepting, sticking, following, cutting, smashing, twisting,
lifting, collapsing, tucking, bumping, exploring, flipping; bagua
weapons - Chun Qiu Dao, Zhan Shen Qiang, Lian Huan Jian, bagua dao),
USA Dojo 'About Ba Gua Zhang' (Liang Zhenpu school: Tang Ni Bu mud
sliding step as the walking technique; Koubu toe-in and Baibu toe-out
for changing direction; Waibu outer foot and Neibu inner foot; Tui Mo
Zhang turning the millstone palm - lead hand grinding with index finger
and thumb forming an 'L', torso toward the center, eight steps per
revolution; Gai Mo Zhang covering millstone palm as the deceptive
overhead strike; Dan Huan Zhang single palm change as block then strike
before changing direction), TheFreeDictionary encyclopedia article
(modern styles list - Yin, Cheng, Liang, Gao, Jiang, Shi, Song, Fan,
Liu, Ma, Gong Baotian, Sun, Fu schools), ZhaobaoTaiji 'Baguazhang'
(palm shapes - upward, downward, vertical, hugging, piercing, chopping,
lifting, picking, collapsing, bumping, tucking; the proverb 'shaped like
a swimming dragon, looks like a monkey guarding, sits like a tiger,
turns like an eagle'; 'walk like a dragon, turn like a monkey, change
like a hawk'; scissor legs, buckle and switch, avoid the straight and
hit diagonally), FreedomMartialArt 'Bagua Zhang' (guerrilla-style
tactics, evasive footwork, rooting maintained while in motion,
striking from indirect angles, constant change), and Hay JG. The
Biomechanics of Sports Techniques. 4th ed. Prentice-Hall; 1993
(striking and kicking mechanics, lever arms, momentum).

Creates two NEW databases, 34 ladder-ordered records each:

  combat-baguazhang              - The Baguazhang Combat Database
                                   (public-harvest: real, fact-checked
                                   Baguazhang - the eight trigram palm -
                                   circle walking foundations, the
                                   mud-wading step, the eight palm
                                   changes in sequence, single and double
                                   palm strikes, elbow and shoulder
                                   techniques, deer-horn knife and
                                   straight sword basics, applications -
                                   each record a technique with HOW TO DO
                                   IT step-by-step body mechanics,
                                   ladder-ordered from basics to advanced;
                                   civilian traditional-art scope)
  combat-baguazhang-signature    - The Baguazhang Combat Signature Database
                                   (his original Signature combat method:
                                   the circle as the signature itself -
                                   every palm change a covenant of the
                                   turn, the mud-wading step the first
                                   covenant and mastery the final
                                   signature; src signature, titles
                                   suffixed " (Signature Edition)",
                                   clearly labeled Signature-made, never
                                   presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBBGZ- (public) and JAH-CBBGZS- (signature), verified free
in the manifest id_prefix values and in every data-1 shard directory (zero
hits), and zero existing 'baguazhang' content anywhere in the system.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_baguazhang.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos before writing
pages.

CONCURRENCY: this builder never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes.
A merger handles those. Only db/combat-baguazhang*/, code/combat-baguazhang-build,
the shard data dirs, and the fragment file are written.

Never the words "bat belt" anywhere. No website references. No Facebook.

SCREENING: civilian traditional-art instruction only - nothing
hate-adjacent, profane, or inappropriate; no religious talk; nothing on
neutralizing or defeating military or defense-grade systems.
"""

SIG_TAIL = ("Signature original - his original Signature combat method: the "
            "circle as the signature itself, every palm change a covenant of "
            "the turn, the mud-wading step the first covenant and mastery the "
            "final signature. Clearly labeled Signature-made, never presented "
            "as authentic public record.")

CIT_WIKI = ("Wikipedia contributors. Baguazhang. Wikipedia, The Free "
            "Encyclopedia; accessed 2026-10-17.")
CIT_NWE = ("New World Encyclopedia contributors. Baguazhang. New World "
           "Encyclopedia; accessed 2026-10-17.")
CIT_TFD = ("Baguazhang. TheFreeDictionary Encyclopedia; accessed "
           "2026-10-17.")
CIT_GW = ("GW Media. Ba Gua Zhang (Ba Gua Palm). Kungfu Culture; accessed "
          "2026-10-17.")
CIT_USADOJO = ("About Ba Gua Zhang. USA Dojo; accessed 2026-10-17.")
CIT_ZBT = ("Chinese Traditional Martial Arts - Baguazhang. ZhaobaoTaiji; "
           "accessed 2026-10-17.")
CIT_FMA = ("Bagua Zhang. FreedomMartialArt; accessed 2026-10-17.")
CIT_HAY = ("Hay JG. The Biomechanics of Sports Techniques. 4th ed. "
           "Prentice-Hall; 1993.")

ENTRIES = [
    {
        "key": "bgz-meaning",
        "name": "What Baguazhang Means: The Eight Trigram Palm",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Baguazhang means 'eight trigram palm' - one of the three "
            "principal Chinese internal martial arts, alongside xingyiquan "
            "and taijiquan. The art is credited to Dong Haichuan "
            "(1797-1882) of Hebei Province, who originally called it "
            "'Zhuanzhang' (Turning Palm) and taught it in Beijing from about "
            "1864. His famous students founded the enduring lineages: Yin "
            "Fu (Yin style), Cheng Tinghua (Cheng style), and Liang Zhenpu "
            "(Liang style). The 'eight trigrams' of the name are the eight "
            "basic figures of the Book of Changes - heaven, earth, thunder, "
            "wind, water, fire, mountain, lake - and the art pairs each with "
            "a palm strategy. Baguazhang is palm-based: strikes are delivered "
            "with the open hand, the body constantly turning, the fighter "
            "never meeting force head-on but changing around it."
        ),
        "how_it_works": (
            "Step 1: Say the name in parts - 'ba' (eight), 'gua' (trigram), "
            "'zhang' (palm) - so the eight strategies stay attached to the "
            "palm that performs them. Step 2: Learn the founder's story as "
            "the frame - Dong Haichuan synthesized the martial arts of his "
            "Hebei region with circle-walking training, taught in Beijing, "
            "and passed the art to students who each founded a style. Step 3: "
            "Learn the three internal arts as a family - xingyiquan, "
            "taijiquan, and baguazhang share internal power mechanics but "
            "baguazhang is distinct in its constant circular movement. "
            "Step 4: Treat every later technique as one of the eight "
            "trigrams in motion - each palm change is one trigram's "
            "strategy written with the hands."
        ),
        "key_points": [
            "'Eight trigram palm' - eight strategies, one palm art",
            "Founded by Dong Haichuan (1797-1882), Hebei, taught Beijing from about 1864",
            "Originally called Zhuanzhang - Turning Palm",
            "Lineages: Yin Fu, Cheng Tinghua, Liang Zhenpu styles",
            "One of the three principal internal arts with xingyiquan and taijiquan",
            "Palm-based, circular, never force-on-force",
        ],
        "requirements": [
            "A clear practice space and an open mind about circular movement",
            "No equipment - the first lessons are history, vocabulary, and posture",
        ],
        "standards": [
            "Student can name the founder, the founding century, and the three internal arts",
            "Student can translate 'baguazhang' as 'eight trigram palm'",
            "Student can name the three famous students and their styles",
        ],
        "citations": [CIT_WIKI, CIT_NWE, CIT_TFD],
        "sig_lens": (
            "His Signature reading of what baguazhang means: the circle is "
            "the signature itself - eight trigram strategies written in "
            "turning steps, the founder's synthesis as the first covenant "
            "of the system."
        ),
    },
    {
        "key": "bgz-circle-walking",
        "name": "Circle Walking: The Foundation Drill",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Circle walking - 'turning the circle' - is baguazhang's "
            "characteristic method of stance and movement training. Every "
            "form of baguazhang uses it. The practitioner walks around the "
            "edge of a circle in low stances, facing the center, holding "
            "upper-body postures, and periodically changing direction as "
            "forms are executed. For a beginner the circle is six to twelve "
            "feet in diameter; students first learn flexibility and proper "
            "body alignment through these basic exercises, then move on to "
            "more complex forms and internal power mechanics. One "
            "revolution of the circle is walked in eight steps - one for "
            "each of the eight trigrams. Circle walking builds leg "
            "strength, smooth weight transitions, balance, and the calm "
            "nervous system that lets a fighter change direction at will."
        ),
        "how_it_works": (
            "Step 1: Mark a circle six to eight feet across on the floor - "
            "chalk, tape, or a rope ring. Step 2: Stand on the circle's edge "
            "facing the center, feet shoulder-width, knees soft, spine tall, "
            "weight sinking. Step 3: Walk the edge counterclockwise, each "
            "step landing along the circle line, taking exactly eight steps "
            "per full revolution - count them. Step 4: Keep the torso turned "
            "toward the center while the feet walk the edge; the waist does "
            "the twisting, not the knees. Step 5: Stay low and even - the "
            "head must not bob up and down as you step. Step 6: Walk for "
            "five minutes one direction, then change direction and walk "
            "five minutes back. Step 7: Add weeks of practice before "
            "changing the upper-body posture - the legs learn first."
        ),
        "key_points": [
            "Walk the edge of the circle, face the center, torso twisted inward",
            "Beginner circle: six to twelve feet in diameter",
            "Eight steps per revolution - one per trigram",
            "The waist twists, not the knees",
            "Head stays level - no bobbing",
            "Direction changes are the heart of the art",
        ],
        "requirements": [
            "A marked circle on flat ground, six to twelve feet across",
            "Supportive flat shoes; loose clothing",
            "Five to ten minutes of uninterrupted walking time",
        ],
        "standards": [
            "Student walks eight even steps per revolution, both directions",
            "Head height varies less than a finger-width across a revolution",
            "Student can walk the circle for ten minutes without stopping",
        ],
        "citations": [CIT_WIKI, CIT_USADOJO, CIT_FMA],
        "sig_lens": (
            "His Signature reading of circle walking: the circle is the "
            "first covenant - every revolution writes the signature deeper "
            "into the legs, and the calm center is where his Signature "
            "power is stored."
        ),
    },
    {
        "key": "bgz-mud-wading",
        "name": "The Mud-Wading Step (Tang Ni Bu)",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Tang Ni Bu - the mud-wading (or mud-sliding) step - is "
            "baguazhang's trademark walking technique. The foot slides "
            "forward low over the ground as if wading through soft mud: the "
            "sole barely leaves the floor, the step is short and gripping, "
            "and the body's weight transfers without rising. In the Liang "
            "Zhenpu school this is the single walking technique, described "
            "as a fluid motion like sliding on soft mud or clay. Because the "
            "foot never lifts high, the practitioner keeps 'rooting' while "
            "in motion and can launch an attack at any time - unlike arts "
            "that root only from a fixed stance. The mud-wading step is "
            "paired with special attention to the turn and the lock in the "
            "switching moves, where direction changes happen."
        ),
        "how_it_works": (
            "Step 1: Stand in a low walking posture, weight on the rear "
            "leg, front foot flat. Step 2: Slide the front foot forward "
            "along the floor - the sole skims the ground, toes lightly "
            "gripping, heel low - about one foot-length of travel. Step 3: "
            "Transfer weight smoothly onto the sliding foot without letting "
            "the head rise; the sinking feeling stays constant. Step 4: "
            "Bring the rear foot up to just behind the front foot, sole "
            "skimming, and repeat. Step 5: Practice along a straight line "
            "first - twenty slides out, twenty back - then carry the slide "
            "onto the circle. Step 6: Speed the slide gradually, but never "
            "let the foot lift higher than a coin's thickness off the "
            "floor. Step 7: In the switching moves, let the sliding foot "
            "turn and lock the direction - the step itself does the turning."
        ),
        "key_points": [
            "Tang Ni Bu: the mud-wading / mud-sliding step",
            "Sole skims the floor - never lifts high",
            "Weight transfers without the head rising",
            "Rooting is kept WHILE moving - attack can launch anytime",
            "The step turns and locks direction in the switching moves",
        ],
        "requirements": [
            "A smooth flat floor (the slide needs low friction)",
            "Flat-soled shoes; twenty feet of straight practice space",
        ],
        "standards": [
            "Foot clears the floor by less than a coin's thickness",
            "Head height constant across twenty slides",
            "Student can slide the full circle in both directions",
        ],
        "citations": [CIT_USADOJO, CIT_GW, CIT_FMA],
        "sig_lens": (
            "His Signature reading of the mud-wading step: the foot that "
            "never leaves the earth signs his name on the ground with every "
            "slide - low, constant, unbroken."
        ),
    },
    {
        "key": "bgz-swing-hook-steps",
        "name": "Swing Step and Hook Step (Bai Bu and Kou Bu)",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Direction changes on the baguazhang circle are made with two "
            "paired steps: Bai Bu, the swing step (toe-out), and Kou Bu, "
            "the hook step (toe-in, pigeon-toed). The swing step opens the "
            "trailing foot outward to start a change of direction; the hook "
            "step turns the lead foot inward across the line of travel to "
            "stop motion in one direction and lock the new one. Together "
            "with Shunbu - plain forward stepping - these are the three "
            "commonly used stepping terms, and all three are practiced "
            "constantly. Two more terms complete the beginner's footwork "
            "vocabulary: Waibu, the outer foot (farther from the circle's "
            "center), and Neibu, the inner foot (closer to the center) - "
            "because every drill names which foot is doing what relative to "
            "the center."
        ),
        "how_it_works": (
            "Step 1: Walk the circle with mud-wading steps and identify the "
            "inner foot (Neibu) and outer foot (Waibu) at every step. Step 2: "
            "To begin a direction change, swing the outer foot outward - Bai "
            "Bu - toes pointing away from the center, opening the hips to "
            "the new direction. Step 3: Hook the inner foot across - Kou Bu "
            "- toes turning inward pigeon-toed, stopping the old direction "
            "dead. Step 4: Let the body turn on the locked hook step while "
            "the swing foot settles onto the new circle line. Step 5: "
            "Resume mud-wading steps in the new direction - eight steps per "
            "revolution again. Step 6: Drill the pair on a line first: swing "
            "out, hook in, turn, walk back - ten pairs each side. Step 7: "
            "Never let the hook step collapse the knee inward; the knee "
            "tracks over the toes even when pigeon-toed."
        ),
        "key_points": [
            "Bai Bu: swing/toe-out step - opens the new direction",
            "Kou Bu: hook/toe-in step - stops the old direction, locks the turn",
            "Shunbu: plain forward stepping - the third common term",
            "Waibu/Neibu: outer/inner foot relative to the circle center",
            "Knee tracks over toes even in the pigeon-toed hook",
        ],
        "requirements": [
            "The marked circle from the circle-walking drill",
            "Flat shoes with grip for the hook step's lock",
        ],
        "standards": [
            "Student names Waibu and Neibu correctly at any point in the walk",
            "Direction change completes within two steps, no stumble",
            "Ten clean swing-hook pairs each side on the line",
        ],
        "citations": [CIT_USADOJO, CIT_ZBT],
        "sig_lens": (
            "His Signature reading of the swing and hook steps: the swing "
            "opens the door of the circle and the hook locks it behind him - "
            "every direction change a signed turn, never an accident."
        ),
    },
    {
        "key": "bgz-posture-alignment",
        "name": "Posture and Alignment on the Circle",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Proper body alignment is the first thing baguazhang teaches - "
            "students learn flexibility and alignment through the basic "
            "exercises before any complex form. The posture: head upright "
            "as if suspended from above, chin slightly tucked, spine tall "
            "but not stiff, shoulders dropped and rounded forward, chest "
            "hollowed, back rounded, waist relaxed so it can twist, hips "
            "sunk, knees bent and tracking over the toes, feet gripping "
            "with the mud-wading slide. The torso turns toward the circle's "
            "center while the feet walk the edge - this waist twist is the "
            "engine of every palm change. A traditional image: sit as steady "
            "as a sedan chair - the upper body rides level and calm while "
            "the legs do the walking."
        ),
        "how_it_works": (
            "Step 1: Stand tall, then sink by bending the knees - feel the "
            "weight drop into the thighs, not the lower back. Step 2: Tuck "
            "the chin a finger-width and imagine the crown of the head "
            "lifted by a string. Step 3: Drop the shoulders down and let "
            "them round slightly forward; hollow the chest a little. Step 4: "
            "Relax the waist - place hands on the hips and rotate the "
            "torso left and right while the feet stay planted, feeling the "
            "waist twist freely. Step 5: Walk the circle holding this "
            "shape, torso toward center, for three minutes. Step 6: Check "
            "the sedan-chair test - a partner watches your head against a "
            "doorframe line; it must not rise or dip. Step 7: When the "
            "thighs burn, sink one finger-width lower and keep walking - "
            "the burn is the posture teaching the legs."
        ),
        "key_points": [
            "Alignment first - before any complex form",
            "Head suspended, chin tucked, spine tall",
            "Shoulders dropped, chest hollowed, back rounded",
            "Waist relaxed and twisting - the engine of the palm changes",
            "Sit as steady as a sedan chair - upper body rides level",
        ],
        "requirements": [
            "A mirror or partner for the head-level check",
            "The marked circle; patience for the thigh burn",
        ],
        "standards": [
            "Student holds aligned posture for five minutes of circle walking",
            "Head height steady within a finger-width",
            "Waist turns freely with feet planted - no knee strain",
        ],
        "citations": [CIT_WIKI, CIT_ZBT, CIT_HAY],
        "sig_lens": (
            "His Signature reading of the posture: the aligned body is the "
            "pen - head the nib, waist the hinge, legs the hand that writes "
            "the circle."
        ),
    },
    {
        "key": "bgz-static-postures",
        "name": "The Eight Static Palm Postures (Ding Shi Ba Zhang)",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Walking the circle while holding static upper-body postures is "
            "baguazhang's core training method - and an effective meditation. "
            "The eight static postures (Ding Shi Ba Zhang) are held, one at "
            "a time, while walking the circle: pressing-down palm, holding-up "
            "palm, embracing palm, pushing palm, single and double hook "
            "palms, hiding-flower-under-leaf, and point-to-heaven-pluck-earth "
            "among the traditional sets. Each posture shapes the arms in a "
            "rounded, concave form - palms alive, fingers extended, the "
            "classic baguazhang hand with the thumb and index finger forming "
            "an open 'L'. Walking with a fixed posture trains the shoulders "
            "to stay dropped while the arms work, the waist to twist under a "
            "stable frame, and the mind to settle into quiet awareness while "
            "the body keeps moving."
        ),
        "how_it_works": (
            "Step 1: Learn the pushing-palm shape first - lead arm extended "
            "toward the circle's center, palm facing out, thumb and index "
            "finger forming an 'L', fingers together and extended, rear palm "
            "close to the body with fingertips just below the lead elbow. "
            "Step 2: Walk the circle holding this shape for two minutes each "
            "direction - shoulders must stay dropped, elbows never locked. "
            "Step 3: Add the embracing-palm shape - both arms rounded as if "
            "holding a large ball at chest height - and walk two minutes. "
            "Step 4: Practice the pressing-down palm - both palms pressing "
            "toward the ground at waist height - for two minutes. Step 5: "
            "Cycle through all the postures you know, two minutes each, "
            "never letting the shoulders creep up. Step 6: When a posture "
            "tires the arms, check the waist - the twist, not the shoulders, "
            "should carry the shape. Step 7: Finish each session with one "
            "slow circle in the pushing-palm shape, breathing deeply."
        ),
        "key_points": [
            "Static postures held while walking - training and meditation in one",
            "Classic hand: thumb and index finger form an open 'L'",
            "Palms concave and alive, fingers extended, elbows never locked",
            "Shoulders stay dropped - the waist twist carries the shape",
            "Lead palm toward center, rear palm guarding near the body",
        ],
        "requirements": [
            "The marked circle; a timer for two-minute posture holds",
            "Shoulders must be warm - arm circles before starting",
        ],
        "standards": [
            "Student walks three postures, two minutes each, both directions",
            "Shoulders stay visibly dropped through the whole cycle",
            "Hand shapes hold the 'L' without finger splay",
        ],
        "citations": [CIT_WIKI, CIT_USADOJO],
        "sig_lens": (
            "His Signature reading of the static postures: eight handshapes "
            "are eight signatures - each one held against the turning "
            "circle until the body remembers it without being told."
        ),
    },
    {
        "key": "bgz-single-change",
        "name": "Single Palm Change (Dan Huan Zhang)",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The Single Palm Change is the first of the eight palm changes - "
            "and the one Dong Haichuan taught every student. 'Dan Huan "
            "Zhang' means single-change palm: one hand opens the change as "
            "the walker reverses direction on the circle. In fighting terms "
            "it is one block followed by a strike, then a change of "
            "direction to face the next threat. The movement: walking the "
            "circle in the millstone-palm posture, the practitioner swings "
            "and hooks the steps, turns the body fully on the lock, the "
            "lead hand sweeps across to deflect while the rear hand issues "
            "forward - and the walk resumes in the opposite direction. "
            "Dong Haichuan consistently taught only the first three palms "
            "(Single Change, Double Change, Smooth Body) and varied the "
            "rest, so the Single Change carries the whole art's DNA."
        ),
        "how_it_works": (
            "Step 1: Walk the circle in the millstone-palm posture, eight "
            "steps per revolution. Step 2: On the chosen step, swing the "
            "outer foot out (Bai Bu) and hook the inner foot in (Kou Bu), "
            "locking the turn. Step 3: As the body turns, the lead hand "
            "sweeps horizontally across the chest - this is the deflecting "
            "block, palm concave, arm rounded. Step 4: The rear hand drives "
            "forward past the turning body - the strike - palm heel leading, "
            "issued from the waist twist, not the shoulder. Step 5: Settle "
            "onto the new circle line facing the center, both palms back in "
            "the millstone shape. Step 6: Walk on in the new direction - "
            "one change complete. Step 7: Drill: walk four steps, single "
            "change, walk four steps, single change - ten changes each "
            "side, keeping the eight-step rhythm."
        ),
        "key_points": [
            "First of the eight palm changes - taught to every student by Dong Haichuan",
            "One block (lead hand sweeps) then one strike (rear hand issues)",
            "Built on the swing-step / hook-step turn",
            "The strike issues from the waist twist, not the shoulder",
            "Ends walking the opposite direction - block, strike, change, continue",
        ],
        "requirements": [
            "Solid circle walking, mud-wading step, and swing-hook turns",
            "The millstone-palm posture held comfortably",
        ],
        "standards": [
            "Ten clean single changes each side without breaking step rhythm",
            "Strike visibly driven by waist turn",
            "Direction fully reversed, walking resumed within two steps",
        ],
        "citations": [CIT_GW, CIT_USADOJO, CIT_WIKI],
        "sig_lens": (
            "His Signature reading of the Single Palm Change: the first "
            "covenant of the turn - one hand deflects the world, one hand "
            "answers it, and the circle keeps his signature unbroken."
        ),
    },
    {
        "key": "bgz-double-change",
        "name": "Double Palm Change (Shuang Huan Zhang)",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The Double Palm Change is the second of the eight palm "
            "changes - 'Shuang Huan Zhang', the double-change palm. Where "
            "the Single Change leads with one hand, the Double Change "
            "brings both hands into the turn: the arms describe a full "
            "circle in front of the body as the direction reverses, one "
            "palm deflecting high while the other controls low, or both "
            "palms changing over in a continuous wheel. It teaches the "
            "coordination that all later changes depend on - both hands "
            "working as one turning system while the feet swing, hook, and "
            "lock below. Like the Single Change, it was among the three "
            "palms Dong Haichuan taught every student, and it appears at "
            "the head of every lineage's sequence."
        ),
        "how_it_works": (
            "Step 1: Walk the circle in the millstone-palm posture. Step 2: "
            "Begin the turn with the swing step and hook step, as in the "
            "single change. Step 3: As the body turns, let BOTH hands rise "
            "and describe a vertical circle in front of the chest - the "
            "lead hand sweeps up and over while the rear hand circles "
            "under, the two hands passing like wheels. Step 4: The upper "
            "hand finishes deflecting outward at head height while the "
            "lower hand settles guarding the ribs - both palms concave, "
            "both alive. Step 5: Land the turn on the new circle line, "
            "torso to the center, and walk on. Step 6: The key drill: "
            "alternate single change and double change - walk four steps, "
            "single, four steps, double - feeling how the double uses both "
            "hands where the single used one. Step 7: Keep the arm-circle "
            "continuous; any pause or hitch means the waist stopped "
            "driving the hands."
        ),
        "key_points": [
            "Second of the eight palm changes - both hands turn as one system",
            "Arms describe a full circle like wheels during the turn",
            "One hand deflects high while the other controls low",
            "The foundation coordination for all later changes",
            "No hitch in the arm-circle - the waist drives continuously",
        ],
        "requirements": [
            "Clean Single Palm Change on both sides",
            "Relaxed shoulders - double-hand circling punishes tension",
        ],
        "standards": [
            "Ten double changes each side, arm-circle continuous",
            "Hands finish in guarding positions, palms concave",
            "Student can alternate single and double changes without pausing",
        ],
        "citations": [CIT_GW, CIT_WIKI],
        "sig_lens": (
            "His Signature reading of the Double Palm Change: the second "
            "covenant - both hands turn as one wheel, and his signature "
            "gains its second stroke."
        ),
    },
    {
        "key": "bgz-single-palm-strike",
        "name": "Single Palm Strike Mechanics",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "The single palm strike is baguazhang's basic blow - delivered "
            "with the open hand, driven by the turning body. The striking "
            "surface is the palm heel and the whole palm face; the hand "
            "stays concave and alive, fingers together, the 'L' of thumb "
            "and index finger intact. Power comes from the ground through "
            "the turning waist: as the body rotates on the circle, the "
            "striking arm is carried and released like the tip of a whip. "
            "Because baguazhang strikes from indirect angles - entering "
            "from the side or the turn - the palm lands where the guard is "
            "not. The classic targets are the torso: the strike pushes "
            "through the target with the body's turning momentum behind it, "
            "rather than snapping back."
        ),
        "how_it_works": (
            "Step 1: Stand in the millstone posture facing a pad or heavy "
            "bag at arm's length. Step 2: Shape the striking hand - palm "
            "concave, fingers together and slightly tensed, thumb and index "
            "in the 'L'. Step 3: Turn the waist away from the target a "
            "quarter-turn, loading the body like a coiled spring - the arm "
            "stays relaxed. Step 4: Drive the waist back toward the target; "
            "let the arm be thrown forward by the turn, palm heel leading. "
            "Step 5: Strike through the pad - the palm lands and the body "
            "keeps turning an inch past contact, pushing through. Step 6: "
            "Recover by letting the turning body carry the hand back, not "
            "by yanking the arm. Step 7: Drill ten strikes each side, "
            "checking that the feet never leave their root - the power is "
            "waist-turn times arm length, never arm muscle alone."
        ),
        "key_points": [
            "Open hand, palm heel and palm face as the striking surface",
            "Power = ground through the turning waist - the arm is the whip tip",
            "Strike THROUGH the target with turning momentum",
            "Hand stays concave and alive, the 'L' intact",
            "Delivered from indirect angles - where the guard is not",
        ],
        "requirements": [
            "A pad or heavy bag; wrist wraps for beginners",
            "Solid waist-twist from the posture work",
        ],
        "standards": [
            "Ten strikes each side with visible waist-driven power",
            "Feet stay rooted - no hopping into the strike",
            "Palm shape correct on contact, every rep",
        ],
        "citations": [CIT_HAY, CIT_GW, CIT_FMA],
        "sig_lens": (
            "His Signature reading of the single palm strike: the turning "
            "body is the hand and the palm is the pen - the strike signs "
            "through the target in one turning stroke."
        ),
    },
    {
        "key": "bgz-double-palm-strike",
        "name": "Double Palm Strike Mechanics",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "The double palm strike sends both hands to the target together - "
            "a pushing, shocking blow driven by the whole turning body. "
            "Both palms face the target, concave and alive, and the strike "
            "lands with the combined mass of the torso behind it: the "
            "practitioner steps or turns into the blow so the body weight "
            "arrives with the hands. In the palm changes it appears as the "
            "finishing issue - both palms driving forward as the turn "
            "completes. The double palm is also the art's characteristic "
            "push: trained against a partner, it teaches issuing force "
            "through both arms without leaning, the spine staying tall while "
            "the legs drive. Because both hands commit, the strike is "
            "always thrown from a turned, angled position - never squared "
            "up - so the body is already moving off the opponent's line."
        ),
        "how_it_works": (
            "Step 1: Face the pad at arm's length, feet in the walking "
            "stance, both palms up at chest height. Step 2: Turn the waist "
            "a quarter-turn to load, both hands drawing slightly back and "
            "down - the coil. Step 3: Drive forward: legs push the ground, "
            "waist turns, both palms shoot forward together, striking "
            "surface the two palm heels side by side. Step 4: Let the body "
            "weight arrive WITH the hands - the front foot's mud-wading "
            "slide carries the mass into the blow. Step 5: Push through "
            "two inches past contact, then let the turn carry the hands "
            "back - never lean the torso past the hips. Step 6: Partner "
            "drill: partner offers a chest pad and calls 'turn' - you turn, "
            "step, and issue; partner checks that your spine stayed tall. "
            "Step 7: Ten issues each side; the pad-holder should feel body "
            "weight, not arm push."
        ),
        "key_points": [
            "Both palms together - combined torso mass behind the blow",
            "The body's weight arrives WITH the hands via the sliding step",
            "Spine stays tall - no leaning into the push",
            "Always thrown turned and angled, never squared up",
            "The characteristic finishing issue of the palm changes",
        ],
        "requirements": [
            "A partner with a body pad; the single-palm mechanics first",
            "Enough floor for a sliding step into the strike",
        ],
        "standards": [
            "Pad-holder feels body weight in ten consecutive issues",
            "No torso lean past the hips on any rep",
            "Both palms land together, not one before the other",
        ],
        "citations": [CIT_HAY, CIT_GW],
        "sig_lens": (
            "His Signature reading of the double palm strike: both hands "
            "sign at once - the whole turning body behind a single "
            "two-handed stroke."
        ),
    },
    {
        "key": "bgz-millstone-palm",
        "name": "Turning the Millstone Palm (Tui Mo Zhang)",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Tui Mo Zhang - turning the millstone palm - is baguazhang's "
            "trademark posture. The lead hand extends toward the opponent "
            "(or the circle's center in solo practice) with the palm facing "
            "outward, grinding in small circles as if turning an invisible "
            "millstone; the index finger and thumb form an 'L', both palms "
            "hold a circular, concave shape, the rear palm stays close to "
            "the body with its fingertips just below the lead elbow, and "
            "the torso turns toward the center while the feet walk the "
            "edge. The grinding is not decoration: the small circles train "
            "the lead arm to deflect, stick, and redirect contact while "
            "walking, and the posture is the launching platform for the "
            "Single Palm Change. Walking the millstone posture IS the "
            "beginner's baguazhang."
        ),
        "how_it_works": (
            "Step 1: Take the millstone shape - lead arm extended at chest "
            "height toward the center, palm out, 'L' formed, rear palm near "
            "the ribs below the lead elbow. Step 2: Begin grinding - small "
            "horizontal circles with the lead palm, as if pushing a heavy "
            "millstone around, driven by the waist, not the shoulder. Step 3: "
            "Walk the circle in the mud-wading step while grinding - eight "
            "steps per revolution, torso to the center. Step 4: Feel the "
            "deflection: have a partner press lightly against your grinding "
            "palm - redirect their push to the side with the circle, never "
            "meeting it straight. Step 5: Reverse the grind's direction "
            "every two revolutions. Step 6: Walk five minutes each way, "
            "grinding continuously. Step 7: Finish by sinking one "
            "finger-width lower and grinding slower - the slow grind shows "
            "where the shoulders try to take over."
        ),
        "key_points": [
            "The trademark posture - lead hand grinding like a millstone",
            "Index finger and thumb form an 'L'; palms circular and concave",
            "Rear palm guards near the body, below the lead elbow",
            "Grinding driven by the waist, not the shoulder",
            "The deflection trainer and the Single Change's platform",
        ],
        "requirements": [
            "The marked circle; a partner for the deflection check",
            "Relaxed shoulders - grinding punishes shrugging",
        ],
        "standards": [
            "Five minutes of continuous grinding walk each direction",
            "Partner's push redirected sideways, never met straight",
            "Shoulders stay dropped for the whole session",
        ],
        "citations": [CIT_USADOJO, CIT_GW],
        "sig_lens": (
            "His Signature reading of the millstone palm: the grinding hand "
            "writes his signature in circles on the air - every revolution "
            "of the stone a revolution of the covenant."
        ),
    },
    {
        "key": "bgz-breathing",
        "name": "Breathing and Relaxation in Practice",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Baguazhang is walked on the breath. The practice demands deep, "
            "natural breathing coordinated with the steps: typically the "
            "practitioner breathes in over several steps and out over "
            "several more, the belly expanding on the inhale and settling "
            "on the exhale, never holding the breath during the turns. "
            "Relaxation is trained as deliberately as footwork - the "
            "shoulders drop, the chest hollows, the waist loosens - because "
            "tension locks the waist twist that drives every palm change, "
            "and a locked waist means arm-only technique. Circle walking "
            "with settled breathing doubles as meditation: the mind quiets "
            "into the rhythm of step and breath while the body keeps "
            "moving, which is why the old schools walked the circle for "
            "long sessions. Breathe wrong and the circle is just walking; "
            "breathe right and it becomes baguazhang."
        ),
        "how_it_works": (
            "Step 1: Stand still and find the belly breath - hand on the "
            "lower belly, inhale through the nose feeling it expand, exhale "
            "through the nose feeling it settle. Step 2: Walk the circle "
            "slowly, inhaling for four steps and exhaling for four steps - "
            "count the steps, not the seconds. Step 3: During the palm "
            "changes, keep the breath flowing - exhale gently through the "
            "turn and the strike, never holding. Step 4: Scan for tension "
            "every revolution: shoulders, jaw, fists - drop each one on an "
            "exhale. Step 5: Lengthen the cycle as you settle - six steps "
            "in, six steps out - without forcing. Step 6: Walk one full "
            "slow circle with the eyes soft, attention on the breath and "
            "the feet only. Step 7: End every session with three slow "
            "breaths standing still, hands resting on the lower belly."
        ),
        "key_points": [
            "Breathe in steps - four in, four out to start",
            "Belly expands on inhale, settles on exhale; nose breathing",
            "Never hold the breath through turns or strikes",
            "Tension locks the waist - scan and drop it every revolution",
            "Settled breathing turns circle walking into meditation",
        ],
        "requirements": [
            "The marked circle; no equipment",
            "A quiet space helps the first breathing sessions",
        ],
        "standards": [
            "Student holds 4-in/4-out breathing for five minutes of walking",
            "No breath-holding visible during palm changes",
            "Shoulders and jaw visibly relaxed on the tension scan",
        ],
        "citations": [CIT_WIKI, CIT_ZBT],
        "sig_lens": (
            "His Signature reading of the breath: the breath is the ink - "
            "steady, deep, unbroken - and the relaxed body is the hand that "
            "never cramps around the pen."
        ),
    },
]

ENTRIES += [
    {
        "key": "bgz-flowing-body",
        "name": "Third Palm Change: Flowing Body Palm (Shun Shi Zhang)",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The Flowing Body Palm - 'Shun Shi Zhang', the go-along palm - "
            "is the third of the eight palm changes and the last of the "
            "three Dong Haichuan taught every student. 'Shun shi' means "
            "going along with the momentum: where the first two changes "
            "stop and reverse the walk, the flowing change rides the body's "
            "existing motion and turns it, smooth as water finding a new "
            "channel. The walker flows around the turn rather than braking "
            "into it - the hands follow the body's lead, one palm leading "
            "the flow while the other guards the turn. This change teaches "
            "the art's central lesson: never oppose force, even your own "
            "momentum - redirect it. In application it is the art of "
            "entering with the opponent's push instead of against it."
        ),
        "how_it_works": (
            "Step 1: Walk the circle briskly in the millstone posture - "
            "feel the walking momentum. Step 2: Instead of braking into the "
            "swing-hook stop, let the outer foot swing wide (Bai Bu) and "
            "CARRY the body's momentum around the turn. Step 3: The lead "
            "hand flows with the turn, palm leading like the prow of a "
            "boat, redirecting rather than blocking. Step 4: The rear hand "
            "sweeps to guard the body's new line as the turn completes. "
            "Step 5: Walk out of the turn without any stop in the rhythm - "
            "a listener should hear no break in your footfalls. Step 6: "
            "Partner drill: partner pushes your lead shoulder as you walk - "
            "flow around the push into the change instead of resisting it. "
            "Step 7: Alternate with the single change - single (stop and "
            "reverse) versus flowing (ride and redirect) - ten of each, "
            "feeling the difference."
        ),
        "key_points": [
            "Third palm change - the last of the three taught to every student",
            "'Go along with the momentum' - redirect, never oppose",
            "No braking into the turn - the footfalls never break rhythm",
            "Lead hand flows like a prow; rear hand guards the new line",
            "The application: entering with the opponent's push",
        ],
        "requirements": [
            "Clean single and double changes; brisk confident circle walking",
            "A partner for the push-and-flow drill",
        ],
        "standards": [
            "No audible break in footfall rhythm through the change",
            "Partner's push redirected into the turn, not resisted",
            "Student can demo single vs flowing change on demand",
        ],
        "citations": [CIT_GW, CIT_WIKI, CIT_FMA],
        "sig_lens": (
            "His Signature reading of the Flowing Body Palm: the third "
            "covenant - his signature flows around every obstacle like "
            "water, never lifting the pen."
        ),
    },
    {
        "key": "bgz-back-body",
        "name": "Fourth Palm Change: Back-Body Palm (Bei Shen Zhang)",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The Back-Body Palm - 'Bei Shen Zhang' - is the fourth palm "
            "change: the change you make when the threat is behind you. "
            "The walker turns the body fully, presenting the back to the "
            "old direction while the hands cover the new one - the torso "
            "rotates a full half-turn on the locked hook step, one palm "
            "sweeping behind to guard the back while the other issues "
            "forward into the new facing. It trains the fighter to change "
            "facing completely without losing guard - the back is never "
            "truly exposed because the turning hands cover it through the "
            "rotation. In application it answers a grab or strike from "
            "behind: turn into the threat, the sweeping hand clearing the "
            "attack while the body spins to face it."
        ),
        "how_it_works": (
            "Step 1: Walk the circle in millstone posture. Step 2: Swing "
            "and hook, but commit to the FULL turn - rotate the torso a "
            "complete half-turn on the hook step, letting the back face "
            "where you came from. Step 3: As you turn, sweep one palm in "
            "a wide arc behind you - this is the back-guard, clearing "
            "anything at your back. Step 4: The other palm issues forward "
            "into the new facing as the turn completes - strike and guard "
            "arrive together. Step 5: Settle facing the center on the new "
            "line, both palms in guard, and walk on. Step 6: Slow-motion "
            "drill first - the full turn at half speed, ten times - then "
            "bring it to walking speed. Step 7: Partner drill: partner "
            "taps your back mid-walk; turn with the back-body change and "
            "finish facing them in guard."
        ),
        "key_points": [
            "Fourth palm change - the change for a threat behind",
            "Full half-turn of the torso on the locked hook step",
            "One palm sweeps behind as back-guard; the other issues forward",
            "The back is never exposed - the turning hands cover it",
            "Finishes facing the new threat in full guard",
        ],
        "requirements": [
            "Solid swing-hook turns; comfort with full torso rotation",
            "A partner for the back-tap drill",
        ],
        "standards": [
            "Full half-turn completed without stumbling, ten reps each side",
            "Back-guard sweep visibly covers the rear through the turn",
            "Partner back-tap answered facing them in guard within two steps",
        ],
        "citations": [CIT_GW, CIT_WIKI],
        "sig_lens": (
            "His Signature reading of the Back-Body Palm: the fourth "
            "covenant - even his back is guarded, and the turn itself "
            "becomes the signature's shield."
        ),
    },
    {
        "key": "bgz-turning-body",
        "name": "Fifth Palm Change: Turning Body Palm (Zhuan Shen Zhang)",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The Turning Body Palm - 'Zhuan Shen Zhang' - is the fifth palm "
            "change and the purest expression of 'turning the circle'. "
            "Here the whole body becomes the turning mechanism: the walker "
            "spins on the axis of the weighted leg while the free foot "
            "repositions, the palms winding around the body like a coiling "
            "rope, and the direction reverses in a single continuous "
            "rotation. Nothing stops, nothing resets - the turn IS the "
            "technique. It trains the deep waist-and-hip rotation that "
            "powers the advanced changes, and it is the change that most "
            "confuses an opponent: the baguazhang fighter seems to spin "
            "away and arrives striking from the side. Dong Haichuan varied "
            "the last five changes by student, and the turning-body change "
            "was often the test of whether a student truly owned the waist "
            "twist."
        ),
        "how_it_works": (
            "Step 1: Walk the circle and plant the weight fully on the "
            "inner foot - this is the axis. Step 2: Let the outer foot "
            "swing free and begin rotating the whole body around the "
            "weighted leg - hips lead, shoulders follow, head last. Step 3: "
            "Wind the palms around the turning body - one high guarding the "
            "head line, one low guarding the body, both moving with the "
            "rotation like a coiling rope. Step 4: Complete the rotation "
            "and place the free foot on the new circle line - one "
            "continuous spin, no stutter steps. Step 5: Walk on in the new "
            "direction, palms settling to millstone. Step 6: Drill the "
            "axis: practice the spin standing still first - ten full "
            "rotations on each leg - then carry it onto the walk. Step 7: "
            "Speed check: the turn should take the time of two walking "
            "steps, no more."
        ),
        "key_points": [
            "Fifth palm change - the whole body as the turning mechanism",
            "Spin on the weighted leg's axis; hips lead, head last",
            "Palms wind around the body like a coiling rope",
            "One continuous rotation - the turn IS the technique",
            "The classic waist-twist test of the advanced student",
        ],
        "requirements": [
            "Strong single-leg balance; the first four changes clean",
            "Ankle-supporting shoes for the pivot work",
        ],
        "standards": [
            "Ten full stationary rotations each leg without wobble",
            "Circle turn completed in two step-times, no stutter",
            "Palms maintain guard positions through the whole spin",
        ],
        "citations": [CIT_GW, CIT_WIKI, CIT_ZBT],
        "sig_lens": (
            "His Signature reading of the Turning Body Palm: the fifth "
            "covenant - the whole body becomes the pen's turning point, "
            "and the spin writes the circle in a single stroke."
        ),
    },
    {
        "key": "bgz-rubbing-body",
        "name": "Sixth Palm Change: Rubbing Body Palm (Mo Shen Zhang)",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "'Rubbing palm technique' is even used as an alternate name for "
            "the whole art - and the sixth palm change, Mo Shen Zhang, the "
            "body-grind or rubbing-body palm, is why. In this change the "
            "practitioner turns INTO the opponent's space and grinds past "
            "them: the body rubs along the opponent's guard, the palms "
            "sticking and grinding in small circles, stealing balance "
            "through friction and pressure rather than impact. The movement "
            "is close, continuous, and smothering - the walker turns so "
            "tight to the center that an attacker finds no gap to strike "
            "into. It trains sticking and following: once contact is made, "
            "the palms never leave the opponent's arms, grinding them "
            "aside as the body turns through."
        ),
        "how_it_works": (
            "Step 1: Partner stands at the circle's center holding a guard "
            "up - you walk the edge in millstone posture. Step 2: Turn in "
            "tight - swing-hook into the partner's space, closing the "
            "distance until your lead forearm touches their guard. Step 3: "
            "Grind: small circles with the lead palm against their guard, "
            "sticking to it, never losing contact, the waist driving the "
            "circles. Step 4: Let the grinding circles walk their guard "
            "aside - friction and angle, not shoving - as your body turns "
            "past them. Step 5: Complete the turn on the far side, rear "
            "palm ready to issue, and walk on. Step 6: Solo drill: grind "
            "against a doorframe edge - feel the forearm stick and slide "
            "without bouncing off. Step 7: The rule of the rub - if "
            "contact breaks, you pushed; if it holds and moves them, you "
            "ground."
        ),
        "key_points": [
            "Sixth palm change - the grind that names the art's alternate title",
            "Turn INTO the opponent's space and grind past",
            "Palms stick and never leave the opponent's arms",
            "Balance stolen through friction and pressure, not impact",
            "Contact must hold - pushing breaks it, grinding moves them",
        ],
        "requirements": [
            "A willing partner; forearm conditioning from the millstone work",
            "Close-range comfort - this change is body-to-body",
        ],
        "standards": [
            "Partner's guard moved aside without any shove or bounce",
            "Contact held unbroken through the whole turn",
            "Student can demo the doorframe grind with silent sticking",
        ],
        "citations": [CIT_GW, CIT_FMA],
        "sig_lens": (
            "His Signature reading of the Rubbing Body Palm: the sixth "
            "covenant - his signature grinds close and never lifts from "
            "the page, stealing the opponent's balance stroke by stroke."
        ),
    },
    {
        "key": "bgz-overturning-body",
        "name": "Seventh Palm Change: Overturning Body Palm (Fan Shen Zhang)",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The Overturning Body Palm - 'Fan Shen Zhang', the body-flip "
            "palm - is the seventh change: the sudden reversal. The walker "
            "is moving one way and, in a single explosive turn, the body "
            "flips - the hips overturn, the palms whip over like a wave "
            "breaking, and the walk resumes the opposite way with a strike "
            "already issued. It is the art's ambush change: practiced "
            "slow it looks like a graceful roll of the body; done fast it "
            "is a violent reversal that lands the practitioner behind the "
            "opponent's expectation. The overturn trains the fast-twitch "
            "waist reversal - hips snapping from one twist to the other - "
            "which is also the engine of the art's explosive short strikes."
        ),
        "how_it_works": (
            "Step 1: Walk the circle at moderate speed in millstone "
            "posture. Step 2: Coil - turn the waist fully INTO the walk "
            "direction, loading the hips like a twisted rope. Step 3: "
            "Release - snap the hips the other way, letting the stored "
            "twist whip the body around; the feet swing-hook to catch the "
            "new direction. Step 4: As the body flips, the palms whip over "
            "- one sweeping high across, one driving low - like a wave "
            "breaking over the turn. Step 5: Land the flip already "
            "striking: the low palm issues as the feet settle. Step 6: "
            "Drill slow first - ten slow overturns each side feeling the "
            "coil-and-release - then add speed in small steps. Step 7: "
            "Never force the flip with the knees; if the knees complain, "
            "the coil was too deep - shorten it."
        ),
        "key_points": [
            "Seventh palm change - the sudden reversal, the ambush change",
            "Coil the waist one way, snap it the other - the flip",
            "Palms whip over like a breaking wave",
            "Lands already striking as the feet settle",
            "The fast-twitch waist reversal behind the art's explosive strikes",
        ],
        "requirements": [
            "Healthy knees and a warmed-up waist; the turning-body change first",
            "Space to practice the flip without obstacles",
        ],
        "standards": [
            "Ten slow overturns each side with visible coil-and-release",
            "Full-speed flip lands striking within two steps",
            "No knee pain or wobble on landing",
        ],
        "citations": [CIT_GW, CIT_HAY],
        "sig_lens": (
            "His Signature reading of the Overturning Body Palm: the "
            "seventh covenant - the sudden reversal, his signature flipping "
            "the page and striking before the ink dries."
        ),
    },
    {
        "key": "bgz-returning-body",
        "name": "Eighth Palm Change: Returning Body Palm (Hui Shen Zhang)",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The Returning Body Palm - 'Hui Shen Zhang', the body-return "
            "palm - is the eighth and last change: the completion of the "
            "sequence. After the overturn's explosion, the returning change "
            "gathers everything back - the body returns to the circle, the "
            "palms return to guard, the breath returns to rhythm, and the "
            "walk resumes as if the whole sequence were one unbroken "
            "circle. It teaches the most advanced lesson of the eight: "
            "every technique ends where the next begins. The returning "
            "change is practiced as the seal on the full eight-change form - "
            "single, double, flowing, back-body, turning, rubbing, "
            "overturning, returning - and a clean return means the "
            "practitioner can run the entire sequence without stopping, "
            "each change feeding the next."
        ),
        "how_it_works": (
            "Step 1: Run the seven changes before it in order, walking "
            "between each - this is the sequence the return completes. "
            "Step 2: From the overturn's landing, do NOT reset - gather: "
            "draw the palms back to the body in a collecting circle. Step 3: "
            "Turn the body home - a smooth swing-hook that brings you back "
            "onto the circle line facing the center. Step 4: Settle the "
            "palms into the millstone posture and the breath into the "
            "step-count. Step 5: Walk on - the sequence is complete, and "
            "the walk is the same walk you started with. Step 6: Drill the "
            "full eight in order, slowly, until the transitions disappear - "
            "a listener hears only continuous footfalls. Step 7: The test: "
            "run all eight changes twice through without a single pause; "
            "any stop means one change has not yet learned to feed the next."
        ),
        "key_points": [
            "Eighth palm change - the completion and the seal of the sequence",
            "Gathers body, palms, and breath back to the circle",
            "Every technique ends where the next begins",
            "The full order: single, double, flowing, back-body, turning, rubbing, overturning, returning",
            "Clean return = the whole sequence runs without stopping",
        ],
        "requirements": [
            "All seven previous changes; stamina for the full sequence",
            "A timer - the full run is the endurance test",
        ],
        "standards": [
            "Full eight-change sequence run twice without pausing",
            "No break in footfall rhythm at any transition",
            "Return lands in millstone posture, breath on count",
        ],
        "citations": [CIT_GW, CIT_WIKI],
        "sig_lens": (
            "His Signature reading of the Returning Body Palm: the eighth "
            "covenant - the seal of the sequence, his signature returning "
            "to the circle complete and unbroken."
        ),
    },
    {
        "key": "bgz-covering-millstone",
        "name": "Covering Millstone Palm (Gai Mo Zhang)",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Gai Mo Zhang - the covering millstone palm - is the art's "
            "deceptive overhead strike. The hand is held behind the head, "
            "hidden from the opponent's view, until the last instant - "
            "then it leaps over the head and crashes down onto the "
            "opponent's head or upper torso. The deception is the "
            "technique: the opponent watches the grinding lead hand and "
            "the turning body, never seeing the strike cocked behind the "
            "skull. The blow itself is a full-body drop - the waist turns, "
            "the body sinks, and the palm falls with the weight of the "
            "turn behind it. It is trained from the millstone posture so "
            "the hidden hand is always ready, and it is the classic answer "
            "to an opponent who has learned to watch the lead hand."
        ),
        "how_it_works": (
            "Step 1: Walk the circle in millstone posture; let the rear "
            "hand drift up behind the head - hidden, relaxed, palm facing "
            "out. Step 2: Keep grinding with the lead hand - the visible "
            "hand holds the opponent's attention. Step 3: On the turn, "
            "drop the body weight and whip the hidden hand over the head "
            "in a tight arc - the palm falls like a hammer onto the "
            "target line. Step 4: The power comes from the sink-and-turn: "
            "knees bend deeper, waist rotates, the falling arm is just the "
            "delivery. Step 5: Recover the hand behind the head as the "
            "turn completes - it disappears again. Step 6: Pad drill: "
            "partner holds a pad at head height and watches your lead hand "
            "- strike the pad with the hidden hand ten times; they should "
            "flinch late every time. Step 7: Never telegraph - if the "
            "shoulder rises before the strike, the deception is dead."
        ),
        "key_points": [
            "The deceptive overhead strike - hidden behind the head",
            "Leaps over at the last instant onto head or upper torso",
            "The visible grinding hand holds the opponent's attention",
            "Power from sink-and-turn, not the arm",
            "No telegraph - a rising shoulder kills the deception",
        ],
        "requirements": [
            "The millstone posture; a partner with a head-height pad",
            "Shoulder mobility for the overhead arc",
        ],
        "standards": [
            "Ten hidden-hand strikes; partner flinches late each time",
            "No shoulder rise before the strike",
            "Hand returns to hidden position after every strike",
        ],
        "citations": [CIT_USADOJO, CIT_HAY],
        "sig_lens": (
            "His Signature reading of the covering millstone: the hidden "
            "stroke - his signature keeps one hand unseen until the moment "
            "it signs."
        ),
    },
    {
        "key": "bgz-trigrams",
        "name": "The Eight Trigrams and the Palms",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The 'eight trigrams' of baguazhang's name are not decoration - "
            "each trigram is a fighting strategy, and each palm change is "
            "its physical expression. Qian (heaven) is creative force - "
            "upward, expanding movements. Kun (earth) is receptive power - "
            "grounding, absorbing techniques. Zhen (thunder) is arousing "
            "energy - sudden, explosive actions. Xun (wind) is gentle "
            "penetration - flowing, entering strategies. Kan (water) is "
            "danger and depth - adaptive, sinking methods. Li (fire) is "
            "clarity - sharp, precise strikes. Gen (mountain) is stillness - "
            "rooted, immovable defense. Dui (lake) is joyful expression - "
            "smooth, complete techniques. Advanced students map each palm "
            "change to its trigram and train the change AS the strategy: "
            "the overturning change practiced as thunder, the rubbing "
            "change as water, the flowing change as wind."
        ),
        "how_it_works": (
            "Step 1: Memorize the eight trigrams with their qualities - "
            "heaven, earth, thunder, wind, water, fire, mountain, lake. "
            "Step 2: Assign each palm change a trigram: single change to "
            "heaven (direct and creative), double to earth (grounded "
            "control), flowing to wind, back-body to mountain (immovable "
            "guard), turning to lake (smooth completion), rubbing to water "
            "(adaptive sticking), overturning to thunder (explosive), "
            "returning to fire (clarity of completion). Step 3: Walk the "
            "circle and perform each change while holding its trigram's "
            "quality in mind - thunder changes snap, water changes flow. "
            "Step 4: Partner drill: partner attacks, and you answer with "
            "the trigram the situation calls for - sudden rush, answer "
            "with thunder; push, answer with water. Step 5: Journal which "
            "trigram each change feels like to YOU - the mapping is a "
            "training tool, and personal truth beats rote assignment. "
            "Step 6: Run the eight changes naming each trigram aloud."
        ),
        "key_points": [
            "Each trigram is a fighting strategy, each change its expression",
            "Heaven/earth/thunder/wind/water/fire/mountain/lake",
            "Thunder = explosive, water = adaptive, wind = entering, mountain = rooted",
            "Train each change AS its strategy, not just as choreography",
            "Strategy selection becomes reflex: read the attack, answer with the trigram",
        ],
        "requirements": [
            "All eight palm changes learned; a training journal",
            "A partner for the strategy-selection drill",
        ],
        "standards": [
            "Student names all eight trigrams with qualities from memory",
            "Eight changes performed each embodying its trigram's quality",
            "Partner drill: correct trigram answer three times in a row",
        ],
        "citations": [CIT_WIKI, CIT_ZBT],
        "sig_lens": (
            "His Signature reading of the trigrams: eight strategies, eight "
            "strokes of one signature - heaven through lake, his covenant "
            "written in every element."
        ),
    },
    {
        "key": "bgz-elbow",
        "name": "Elbow Techniques of Baguazhang",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The elbow is baguazhang's close-range answer - when the "
            "turning body closes past palm range, the elbow takes over. "
            "The art's elbows are thrown from the turn: the folding elbow "
            "drops down and in as the body rotates, the rising elbow comes "
            "up under the opponent's guard on the overturn, and the "
            "horizontal elbow whips across as the body spins. Because the "
            "elbow is short and hard, it does its damage through the "
            "body's rotation - the waist snap multiplies the short lever "
            "into a heavy blow. Baguazhang trains elbows inside the palm "
            "changes: the rubbing change's close turn hides the folding "
            "elbow, the overturning change's flip delivers the rising "
            "elbow, and the turning change's spin carries the horizontal "
            "one. Never an arm punch - always the body's turn, shortened."
        ),
        "how_it_works": (
            "Step 1: Learn the three elbow shapes empty-handed: folding "
            "(forearm folds, elbow drops down-in), rising (elbow drives up "
            "under), horizontal (elbow whips across at chest height). Step 2: "
            "For each, the drill is turn-then-elbow: rotate the waist "
            "fully and let the elbow be carried - the arm does not swing, "
            "the body turns it into the target. Step 3: Pad work: partner "
            "holds a body pad close - practice the folding elbow from the "
            "rubbing change's turn, ten each side. Step 4: Practice the "
            "rising elbow from the overturn's flip - the flip's momentum "
            "is the strike's power. Step 5: Practice the horizontal elbow "
            "from the turning change's spin. Step 6: Flow drill: walk the "
            "circle, and on each change, finish with the elbow that change "
            "hides - the changes become elbow deliveries. Step 7: Safety - "
            "elbows are partner-drilled on pads only, never on bodies."
        ),
        "key_points": [
            "The close-range answer when the turn passes palm range",
            "Folding, rising, and horizontal elbows - all thrown from the turn",
            "Waist snap multiplies the short lever - never an arm punch",
            "Each palm change hides an elbow: rubbing/folding, overturning/rising, turning/horizontal",
            "Partner elbow work on pads only",
        ],
        "requirements": [
            "Body pads and a partner; the rubbing, overturning, and turning changes",
            "Elbow pads for the first sessions",
        ],
        "standards": [
            "Three elbow shapes demoed with visible waist-driven power",
            "Ten pad strikes each elbow each side, no arm-swinging",
            "Flow drill: correct hidden elbow for each of three changes",
        ],
        "citations": [CIT_HAY, CIT_GW],
        "sig_lens": (
            "His Signature reading of the elbows: the close stroke - when "
            "the circle tightens past palm range, his signature shortens "
            "to the elbow and still signs true."
        ),
    },
    {
        "key": "bgz-shoulder",
        "name": "Shoulder Strike: The Kao Bump",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The shoulder strike - the kao bump - is baguazhang's whole-body "
            "collision technique. The practitioner turns into the opponent "
            "and meets them with the shoulder, driving through with the "
            "legs and the rotation: it is less a strike than a moving wall. "
            "The kao is delivered from the circle's turn - as the body "
            "rotates past the opponent, the shoulder drops slightly and "
            "drives through their center, uprooting rather than hurting. "
            "Baguazhang favors the kao because it fits the art's geometry: "
            "the fighter is already turning past the opponent's line, so "
            "the shoulder is simply what arrives first. Trained against a "
            "heavy bag or a padded partner, the kao teaches the deepest "
            "lesson of the art - the whole body weight, moving on the "
            "circle, is the weapon; the shoulder is just where it touches."
        ),
        "how_it_works": (
            "Step 1: Stand beside a heavy bag (not in front) - this is the "
            "angle the kao uses. Step 2: Turn the body toward the bag, "
            "dropping the near shoulder slightly and tucking the chin. Step 3: "
            "Drive: push off the rear leg and rotate the whole body INTO "
            "the bag, shoulder meeting it as the turn completes - the "
            "contact is the body's arrival, not a lunge. Step 4: Follow "
            "through two inches past contact, then let the turn carry you "
            "past the bag - the kao moves THROUGH, never stops on. Step 5: "
            "Ten bumps each shoulder on the bag, checking that the feet "
            "stayed under the body - no falling into the bag. Step 6: "
            "Partner drill with a body pad: partner walks, you turn past "
            "them with the kao - they should feel moved, not hit. Step 7: "
            "The kao from the changes: practice bumping out of the "
            "rubbing change's close turn."
        ),
        "key_points": [
            "The whole-body collision - a moving wall, not a punch",
            "Delivered from the turn, beside the opponent, driving through",
            "Uproots rather than hurts - moves the opponent's center",
            "The body's arrival is the strike - no lunging",
            "Follows through past contact, never stops on the target",
        ],
        "requirements": [
            "A heavy bag or padded partner; the rubbing change's close turn",
            "Shoulder mobility warm-up",
        ],
        "standards": [
            "Ten bag bumps each shoulder, feet under the body throughout",
            "Partner drill: partner moved off-balance, not bruised",
            "Kao delivered from the rubbing change's turn on demand",
        ],
        "citations": [CIT_HAY, CIT_FMA],
        "sig_lens": (
            "His Signature reading of the shoulder strike: the wall stroke - "
            "his whole turning body signs at once, and the shoulder is "
            "where the signature lands."
        ),
    },
    {
        "key": "bgz-palm-variations",
        "name": "Palm Strike Variations: The Hand Arsenal",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Beyond the basic push, baguazhang's palm shapes form a full "
            "arsenal: the upward palm, downward palm, vertical palm, "
            "hugging palm, piercing palm, chopping palm, lifting palm, "
            "picking palm, collapsing palm, bumping palm, and tucking palm. "
            "The main techniques read like a complete fighting vocabulary: "
            "pushing, supporting, leading, moving, hooking, chopping, "
            "penetrating, dodging, intercepting, sticking, following, "
            "cutting, smashing, twisting, lifting, collapsing, tucking, "
            "bumping, exploring, cutting, and flipping. Each shape is a "
            "tool with a job: the piercing palm spears through gaps, the "
            "chopping palm cuts down across the guard, the lifting palm "
            "uproots from below, the collapsing palm drops weight onto the "
            "target. The advanced student stops thinking 'which strike' "
            "and lets the turning body's position choose the palm shape - "
            "the hand becomes whatever the angle requires."
        ),
        "how_it_works": (
            "Step 1: Learn the eleven shapes empty-handed, naming each as "
            "you form it - upward, downward, vertical, hugging, piercing, "
            "chopping, lifting, picking, collapsing, bumping, tucking. Step 2: "
            "For each shape, find its job on the pad: pierce the gap, chop "
            "the guard line, lift from below, collapse from above - ten "
            "reps each. Step 3: Walk the circle and change palm shapes "
            "every revolution - the hands cycle the arsenal while the feet "
            "keep the eight-step rhythm. Step 4: Partner feeds attacks "
            "slowly; answer each with the shape the angle calls for - high "
            "attack, collapsing palm; low attack, lifting palm. Step 5: "
            "Combine: single change finished with a chopping palm, double "
            "change finished with piercing palms. Step 6: Speed ladder: "
            "shapes in order, then random order called by the partner. Step 7: "
            "The test - partner calls a technique name ('intercepting!', "
            "'twisting!') and you show its shape instantly."
        ),
        "key_points": [
            "Eleven palm shapes: upward, downward, vertical, hugging, piercing, chopping, lifting, picking, collapsing, bumping, tucking",
            "Twenty-plus techniques: pushing through flipping - a complete vocabulary",
            "Each shape has a job - the angle chooses the shape",
            "Trained on pads, on the walk, and against fed attacks",
            "Goal: the hand becomes whatever the angle requires",
        ],
        "requirements": [
            "Pads; a partner for the feed-and-answer drills",
            "All basic palm mechanics solid first",
        ],
        "standards": [
            "Eleven shapes formed and named correctly on demand",
            "Ten clean reps of each shape's job on the pad",
            "Random-call test: correct shape instantly, eight of ten",
        ],
        "citations": [CIT_ZBT, CIT_GW],
        "sig_lens": (
            "His Signature reading of the palm arsenal: eleven handshapes, "
            "one signature - his hand becomes whatever the turning angle "
            "requires, and every shape signs."
        ),
    },
    {
        "key": "bgz-sticking-turning",
        "name": "Sticking, Following, and Turning Entries",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Sticking and following - never losing contact once it is made - "
            "is the bridge between baguazhang's forms and its fighting. The "
            "practitioner meets the opponent's arm, sticks to it with the "
            "grinding palm, follows wherever it moves, and turns the body "
            "around the contact point: the opponent's own arm becomes the "
            "axle of their defeat. Entries use the art's diagonal geometry - "
            "avoid the straight line and hit diagonally: step to the "
            "opponent's outside at forty-five degrees while turning, so "
            "their force passes through empty space and your palms arrive "
            "from their blind angle. The classic entries are diagonal-out "
            "(stepping outside their lead) and direct-in (threading inside "
            "their guard on the turn) - both powered by the swing-hook "
            "footwork, both ending with the practitioner beside or behind "
            "the opponent, never in front of their power."
        ),
        "how_it_works": (
            "Step 1: Partner extends an arm; place your lead palm on their "
            "forearm and stick - light pressure, never grabbing. Step 2: "
            "Partner moves the arm slowly in circles; follow with the "
            "sticking palm, keeping contact, letting your body turn with "
            "their motion. Step 3: Add the entry: as they push, step "
            "diagonal-out at forty-five degrees with the swing-hook, "
            "turning your body around their arm - you end beside them. Step 4: "
            "From beside them, the free palm issues to their exposed side - "
            "slow and controlled. Step 5: Practice direct-in: thread "
            "inside their guard on the turn, ending chest-to-side. Step 6: "
            "Speed the feed gradually - the stick must survive at every "
            "speed, or the entry is just chasing. Step 7: The rule: if you "
            "lose the stick, you lost the technique - reset and re-stick."
        ),
        "key_points": [
            "Stick once contact is made - never lose it, never grab",
            "The opponent's arm becomes the axle you turn around",
            "Avoid the straight, hit diagonally - forty-five degree entries",
            "Diagonal-out: outside their lead; direct-in: inside their guard",
            "End beside or behind - never in front of their power",
        ],
        "requirements": [
            "A cooperative partner; the rubbing change's sticking first",
            "Mats - entries end with throws in later training",
        ],
        "standards": [
            "Stick maintained through partner's full arm circles",
            "Diagonal-out entry lands beside the partner ten times",
            "Direct-in entry lands chest-to-side without collision",
        ],
        "citations": [CIT_GW, CIT_FMA, CIT_ZBT],
        "sig_lens": (
            "His Signature reading of sticking and turning: his palm never "
            "leaves the page once it touches - following every move until "
            "the circle turns the opponent's own arm into his signature."
        ),
    },
]

ENTRIES += [
    {
        "key": "bgz-deerhorn-basics",
        "name": "Deer-Horn Knives: The Basics (Lu Jiao Dao)",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The deer-horn knives - 'Lu Jiao Dao' - are baguazhang's "
            "signature weapon: crescent-shaped blades unique to the style, "
            "held one in each hand, their interlocking crescents forming a "
            "deer's antlers. Each knife combines multiple blade edges, "
            "points, and hooks in a single compact weapon: it can cut, "
            "hook, trap, lock, and stab, and the two knives work as a "
            "system - one hooking while the other cuts. Training begins "
            "with the grip and the guard: the knives are held so the "
            "crescents frame the hands, the walker circles with the blades "
            "woven into the palm changes, and every empty-hand technique "
            "gains edges. The deer-horn knives turn the art's core skills - "
            "sticking, turning, trapping - into bladed techniques without "
            "changing the body mechanics at all."
        ),
        "how_it_works": (
            "Step 1: Begin with safe trainers (wood or blunt) - never live "
            "blades until the form is owned. Step 2: Learn the grip: the "
            "handle sits across the palm, crescents framing the hand "
            "front and back, the weapon an extension of the palm shape. "
            "Step 3: Take the guard - both knives up, crescents interlocked "
            "in front of the chest like antlers, elbows in. Step 4: Walk "
            "the circle holding the guard - the blades must not wobble; "
            "wobble means the wrists are working instead of the waist. Step 5: "
            "Practice the basic cuts: lead knife sweeps horizontally, rear "
            "knife follows - the millstone grind, now with edges. Step 6: "
            "Practice the hook: catch a training post's peg with a "
            "crescent and pull - feel how the hook traps. Step 7: Weave "
            "the knives into the single and double palm changes - the "
            "empty-hand choreography does not change, only the hands gain "
            "blades."
        ),
        "key_points": [
            "Lu Jiao Dao: crescent-shaped deer-horn knives, unique to baguazhang",
            "Held one per hand; crescents frame the hands like antlers",
            "Cut, hook, trap, lock, and stab - the two knives work as a system",
            "Empty-hand body mechanics unchanged - the hands simply gain blades",
            "Train with safe trainers first - never live blades early",
        ],
        "requirements": [
            "Wooden or blunt deer-horn knife trainers (a pair)",
            "All eight empty-hand palm changes solid",
            "A clear training space - the crescents sweep wide",
        ],
        "standards": [
            "Circle walked with guard, blades steady, no wrist wobble",
            "Basic cuts and hooks demoed on a training post",
            "Knives woven into single and double changes without breaking rhythm",
        ],
        "citations": [CIT_WIKI, CIT_NWE],
        "sig_lens": (
            "His Signature reading of the deer-horn knives: the antlered "
            "signature - his covenant gains crescents, and every turning "
            "stroke now cuts as it signs."
        ),
    },
    {
        "key": "bgz-deerhorn-changes",
        "name": "Deer-Horn Knives: Changes and Trapping",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "With the basics owned, the deer-horn knives are woven through "
            "the full eight palm changes - and their trapping game begins. "
            "The crescents are made for trapping: an opponent's wrist, "
            "weapon, or arm slides into a crescent's curve and locks, and "
            "the turn of the body levers it. The changes become trapping "
            "sequences: the single change's sweep hooks the attacker's arm "
            "into a crescent, the double change's wheel traps high and low "
            "together, the rubbing change's grind locks and drags. Because "
            "the knives never leave the hands, the practitioner fights "
            "with the same continuous turning the empty hand uses - there "
            "are no draws, no resets, just the circle with edges. Advanced "
            "training pairs two practitioners with trainers, trading "
            "traps at walking speed, learning to feel the lock before "
            "forcing it."
        ),
        "how_it_works": (
            "Step 1: With trainers, practice the single trap: partner "
            "extends a training baton; hook it into a lead crescent and "
            "turn the body - the turn, not the arm, does the trapping. Step 2: "
            "Practice the double trap: high crescent catches high, low "
            "crescent catches low, in the double change's wheel. Step 3: "
            "Weave the knives through all eight changes slowly - map where "
            "each change's motion becomes a trap. Step 4: Partner drill at "
            "walking speed: partner feeds slow attacks, you trap and turn "
            "past - no force, just the lock and the circle. Step 5: Learn "
            "the release: after the trap, the crescent opens and the other "
            "knife cuts - trap-then-cut is the knives' signature rhythm. "
            "Step 6: Build to half speed, then three-quarter - the traps "
            "must work by feel, never by muscling. Step 7: The rule of the "
            "crescents: a trap you have to force is a trap you missed - "
            "reset and let the turn do it."
        ),
        "key_points": [
            "The crescents trap wrists, arms, and weapons in their curves",
            "The body's turn levers the trap - never arm strength",
            "Each palm change becomes a trapping sequence",
            "Trap-then-cut: the knives' signature rhythm",
            "No draws, no resets - the circle with edges",
        ],
        "requirements": [
            "Deer-horn basics; a partner with trainers and a training baton",
            "Protective eyewear - crescents sweep near the face",
        ],
        "standards": [
            "Single and double traps demoed on a fed baton",
            "Knives woven through all eight changes without rhythm breaks",
            "Partner drill: three clean trap-and-turn-pasts at half speed",
        ],
        "citations": [CIT_WIKI, CIT_NWE],
        "sig_lens": (
            "His Signature reading of the knife changes: the trapping "
            "signature - his crescents catch and hold, and the turning "
            "covenant levers every lock."
        ),
    },
    {
        "key": "bgz-straight-sword",
        "name": "Straight Sword Basics (Jian) in Baguazhang",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The straight double-edged sword - the jian - is the gentleman "
            "of baguazhang's arsenal, and the art is known for practicing "
            "with extremely large versions of its weapons, including the "
            "bagua sword. The jian's techniques in baguazhang follow the "
            "circle: the sword is carried through the palm changes, "
            "thrusting on the turns, sweeping on the walks, the blade an "
            "extension of the palm shapes the hand already knows. Basic "
            "jian work trains the thirteen methods - thrust, cut, sweep, "
            "parry, point, flick, and their companions - but always on the "
            "move: baguazhang never plants to fence. The sword teaches what "
            "the empty hand only suggests - extension: every technique "
            "must be performed with the body's turn, because the long "
            "blade punishes arm-only movement instantly. Beginners start "
            "with a light practice sword and the walking circle."
        ),
        "how_it_works": (
            "Step 1: Take a light practice jian; learn the grip - thumb "
            "and index pinching the guard, the sword an extension of the "
            "forearm. Step 2: Learn the guard: sword held across the body, "
            "point toward the circle's center, the free hand in a palm "
            "shape behind. Step 3: Walk the circle with the sword in "
            "guard - the point must stay steady; wobble means the shoulder "
            "is steering. Step 4: Practice the thrust on the turn: "
            "swing-hook, turn the body, and let the turn drive the point "
            "forward - the arm extends, the waist delivers. Step 5: "
            "Practice the sweep on the walk: horizontal cuts powered by "
            "the walking turn. Step 6: Weave the sword into the single and "
            "double changes - thrust where the palm struck, sweep where it "
            "deflected. Step 7: Form work: link thrust-sweep-turn into a "
            "flowing sequence, the blade never stopping."
        ),
        "key_points": [
            "The jian: straight, double-edged - the gentleman of the arsenal",
            "Baguazhang trains oversized versions - the bagua sword",
            "Thrust on the turns, sweep on the walks - always moving",
            "The blade punishes arm-only movement - the waist must deliver",
            "Thirteen methods, all performed on the circle",
        ],
        "requirements": [
            "A light practice jian (never sharp for beginners)",
            "The palm changes solid - the sword follows the hands",
            "A long clear space for the blade's arc",
        ],
        "standards": [
            "Circle walked in sword guard, point steady",
            "Thrust and sweep demoed with waist-driven power",
            "Sword woven into single and double changes cleanly",
        ],
        "citations": [CIT_WIKI, CIT_GW],
        "sig_lens": (
            "His Signature reading of the straight sword: the extended "
            "signature - his covenant lengthened to a blade, signing on "
            "the air three feet from his hand."
        ),
    },
    {
        "key": "bgz-spear-staff",
        "name": "Spear and Staff: The Oversized Weapons",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Baguazhang is famous for practicing with extremely large "
            "weapons - the bagua broadsword, the great bagua sword, long "
            "spears, and heavy staffs. The oversized weapons are not "
            "affectation: their weight and length force the whole body to "
            "work. A light staff can be swung with the arms; a great "
            "bagua spear cannot - it demands the waist turn, the leg drive, "
            "and the circle walk, exactly the mechanics the empty hand "
            "needs. Training begins with the staff: sweeping, thrusting, "
            "and coiling it around the body on the walk, learning to let "
            "the long weapon's momentum carry the turns. The spear adds "
            "the point: thrusting on the changes, the whole body behind a "
            "single driving line. When the student returns to the "
            "empty hand after the great weapons, the palms feel impossibly "
            "light - and impossibly fast."
        ),
        "how_it_works": (
            "Step 1: Start with a standard-length staff, not the great "
            "weapons - the mechanics come first. Step 2: Learn the sliding "
            "grip: hands shift along the staff as it sweeps, never locked. "
            "Step 3: Walk the circle sweeping the staff horizontally - the "
            "turn of the waist drives the sweep, the hands only guide. Step 4: "
            "Practice the thrust on the turn: plant the swing-hook, rotate, "
            "and drive the staff's end forward with the body's rotation. "
            "Step 5: Graduate to the longer, heavier staff - feel how the "
            "weight FORCES the waist to work. Step 6: Take up the spear: "
            "same thrusts, now with a point - accuracy on the turn, "
            "striking a marked target. Step 7: Return to the empty hand "
            "after a weapons session and walk the changes - note the new "
            "speed in the palms."
        ),
        "key_points": [
            "Extremely large weapons are the tradition - great swords, long spears, heavy staffs",
            "The weight forces whole-body mechanics - no arm-only swinging possible",
            "Staff first: sweeps and thrusts on the walk and the turns",
            "Spear: the thrusting point driven by the body's rotation",
            "After the great weapons, the empty hands feel light and fast",
        ],
        "requirements": [
            "A staff, then a long spear; a very clear training space",
            "The sword basics first; strong waist-turn mechanics",
        ],
        "standards": [
            "Staff swept and thrust on the walk with waist-driven power",
            "Spear thrusts hit a marked target on the turn, eight of ten",
            "Student reports and shows the empty-hand speed gain",
        ],
        "citations": [CIT_WIKI, CIT_GW],
        "sig_lens": (
            "His Signature reading of the great weapons: the heavy "
            "signature - his covenant written with a spear's weight until "
            "the empty hand signs faster than thought."
        ),
    },
    {
        "key": "bgz-swimming-body",
        "name": "Swimming Body: The Evasive Strategy (You Shen)",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The old boxing proverb describes the baguazhang fighter as "
            "'shaped like a swimming dragon' - and swimming body (you "
            "shen) is the strategy that earns it. The fighter never stays "
            "where the opponent aimed: constant angular change, the body "
            "slipping around attacks like water around stone, always "
            "moving, always turning, striking from the sides and behind. "
            "The tactical signature is guerrilla-style: evasive footwork "
            "escapes the opponent's strong power, and when the moment "
            "opens, the counter is sudden and ferocious, using any part of "
            "the body. Crucially, the baguazhang fighter keeps 'rooting' "
            "while in motion - unlike arts that root only from a fixed "
            "stance, the swimming body can launch an attack at any instant "
            "of the evasion. Strategy emphasizes constant change in "
            "response to combat's spontaneous, live quality."
        ),
        "how_it_works": (
            "Step 1: Partner throws slow straight attacks; practice the "
            "swim - step diagonal-out on the swing-hook, letting the attack "
            "pass through where you were. Step 2: Never step straight "
            "back - every evasion is angular, forty-five degrees or more, "
            "with the body turning. Step 3: Add the return: the moment the "
            "attack misses, your turning body is already beside them - "
            "issue the palm. Step 4: Drill the rhythm: evade-evade-counter, "
            "evade-counter-counter - the counter must come from the "
            "evasion's own motion, not as a separate move. Step 5: Partner "
            "increases speed gradually; your rule never changes - be where "
            "the attack is not. Step 6: Practice the root-in-motion: "
            "partner calls 'now' at random during your evasion - freeze "
            "and show you could strike from that exact position. Step 7: "
            "Spar lightly with the single rule: no straight-line retreats "
            "allowed."
        ),
        "key_points": [
            "'Shaped like a swimming dragon' - never where the attack aimed",
            "Guerrilla tactics: evade the strong, counter sudden and ferocious",
            "Rooting kept while in motion - attack can launch from any instant",
            "Every evasion angular - never straight back",
            "The counter comes from the evasion's own motion",
        ],
        "requirements": [
            "A partner feeding attacks; protective gear for the counters",
            "All entries and turn mechanics solid",
        ],
        "standards": [
            "Ten fed attacks evaded angularly, none met head-on",
            "Counter lands from the evasion's motion eight of ten",
            "Random 'now' freeze shows a strike-ready position every time",
        ],
        "citations": [CIT_FMA, CIT_ZBT],
        "sig_lens": (
            "His Signature reading of the swimming body: the untouchable "
            "signature - his covenant flows around every attack like water "
            "and signs from where the opponent never looked."
        ),
    },
    {
        "key": "bgz-coiling-power",
        "name": "Coiling Power: Spiral Force Generation",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Coiling power is baguazhang's internal engine: the body winds "
            "like a rope and unwinds into the strike. Every joint "
            "participates in a spiral - the feet grip and turn, the knees "
            "coil, the hips wind, the waist twists, the spine rotates, the "
            "shoulders roll, and the palm arrives as the end of the "
            "corkscrew. The spiral does two jobs at once: it stores elastic "
            "energy like a twisted spring, and it lets force travel around "
            "obstacles - a coiled strike can curve past a guard that would "
            "stop a straight punch. The palm changes are coiling drills in "
            "disguise: the turning-body change winds the rope, the "
            "overturning change snaps it, the rubbing change keeps it wound "
            "under pressure. Advanced training isolates the coil - standing "
            "spirals, seated waist winds - until the unwind becomes the "
            "default way the body moves."
        ),
        "how_it_works": (
            "Step 1: Stand and wind: turn the feet, knees, hips, waist, "
            "and shoulders progressively in one direction - feel the body "
            "become a twisted rope, the stretch loading the muscles. Step 2: "
            "Unwind: release the coil from the ground up - feet, knees, "
            "hips, waist, shoulders, palm - the palm shoots forward as the "
            "last link. Step 3: Pad drill: throw coiled palm strikes, "
            "comparing wound versus unwound - the pad-holder reports the "
            "difference. Step 4: Walk the coil: wind during four steps of "
            "the circle, unwind into a palm strike on the fifth - the "
            "walk loads the spring. Step 5: Practice the curve: place a "
            "guard pad to the side and throw the coiled strike around it - "
            "the spiral's arc does what a straight line cannot. Step 6: "
            "Seated waist winds: sit and rotate the waist against "
            "resistance (a partner's hands) to isolate the engine. Step 7: "
            "The test: three coiled strikes in a row, each visibly "
            "wound-then-released, no arm-pushing."
        ),
        "key_points": [
            "The body winds like a rope - every joint in the spiral",
            "Stores elastic energy; releases ground-up: feet to palm",
            "Curves around guards that stop straight strikes",
            "The palm changes are coiling drills in disguise",
            "Wind on the walk, unwind into the strike",
        ],
        "requirements": [
            "A heavy pad; a partner for the resistance winds",
            "A fully warmed-up spine - coiling demands mobility",
        ],
        "standards": [
            "Pad-holder confirms coiled strikes hit clearly harder",
            "Curved strike lands around a guard pad eight of ten",
            "Three consecutive wound-then-released strikes, no arm-push",
        ],
        "citations": [CIT_HAY, CIT_ZBT],
        "sig_lens": (
            "His Signature reading of coiling power: the wound signature - "
            "his covenant twists like a rope and unwinds in a single "
            "corkscrew stroke."
        ),
    },
    {
        "key": "bgz-old-eight-form",
        "name": "The Old Eight Palms Form: Linking the Changes",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The Old Eight Palms form links all eight changes - single, "
            "double, flowing body, back-body, turning body, rubbing body, "
            "overturning body, returning body - into one continuous "
            "sequence, the 'old eight palms' passed down in the Cheng "
            "lineage. Each change flows into the next with walking steps "
            "between, and the full form is walked without stopping: the "
            "returning change of one round becomes the opening walk of the "
            "next. The form is the art's textbook and its examination - "
            "a teacher watching the old eight sees every flaw: a "
            "hesitation between changes, a shoulder that rises in the "
            "overturn, a grind that loses contact in the rub. Traditionally "
            "the form is practiced in both directions, then with the "
            "changes reordered, then with applications drawn from each "
            "change against a partner - the form is never just "
            "choreography, it is the art's compressed library."
        ),
        "how_it_works": (
            "Step 1: List the eight in order and walk them slowly with "
            "four walking steps between each - single, double, flowing, "
            "back-body, turning, rubbing, overturning, returning. Step 2: "
            "Remove the pauses: the walking steps between changes stay, "
            "but the changes themselves connect - finish one, walk, begin "
            "the next. Step 3: Run the form in the opposite direction - "
            "every change mirrored. Step 4: Time the form and smooth it: "
            "the goal is continuous footfalls, no dead stops anywhere. Step 5: "
            "Reorder drill: teacher calls changes in random order and you "
            "perform each from the walk - the form's pieces must work "
            "independently. Step 6: Application round: for each change, "
            "partner feeds the attack that change answers - the form "
            "becomes eight live techniques. Step 7: The examination: "
            "perform the full form both directions, then the random-order "
            "round, without a single hesitation."
        ),
        "key_points": [
            "All eight changes linked: the Cheng lineage's old eight palms",
            "Walked continuously - the return feeds the next round",
            "The teacher's examination: every flaw visible in the form",
            "Practiced both directions, then reordered, then applied",
            "Never just choreography - the art's compressed library",
        ],
        "requirements": [
            "All eight changes individually clean; stamina for continuous rounds",
            "A teacher or senior partner for the examination",
        ],
        "standards": [
            "Full form both directions without a single stop",
            "Random-order round: correct change from the walk every time",
            "Application round: eight live answers to fed attacks",
        ],
        "citations": [CIT_GW, CIT_WIKI],
        "sig_lens": (
            "His Signature reading of the old eight form: the complete "
            "signature - all eight covenants in one unbroken line, the "
            "whole art signed without lifting the pen."
        ),
    },
    {
        "key": "bgz-entering-side",
        "name": "Combat Applications: Entering from the Side",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Baguazhang's combat application is entering from the side: "
            "the fighter never meets the attack's line but steps around "
            "it and arrives at the opponent's flank, where guards are "
            "thin and balance is narrow. The entry is built from the "
            "art's footwork - swing and hook steps, the mud-wading slide, "
            "the turning body - combined with the palm changes' "
            "deflections: the lead hand deflects the attack along its own "
            "line while the body is already moving past it. In the classic "
            "application of the single change, one hand blocks and the "
            "other strikes as the direction changes - and the practitioner "
            "finishes beside the opponent, striking from the blind angle. "
            "Every application follows the same grammar: deflect along "
            "their line, turn past their shoulder, strike from the side, "
            "and keep walking - the entry never stops moving."
        ),
        "how_it_works": (
            "Step 1: Partner throws a slow straight punch; practice the "
            "single-change application - lead hand deflects the punch "
            "along its line while your swing-hook steps carry you to their "
            "outside. Step 2: Finish beside them with the rear palm's "
            "strike to the pad on their ribs - controlled, light contact. "
            "Step 3: Practice the double-change application: both hands "
            "wheel - one deflecting high, one controlling low - as you turn "
            "past to the other side. Step 4: Practice the flowing "
            "application: go WITH a pushing attack, riding it around into "
            "their flank. Step 5: Speed ladder: partner feeds faster; your "
            "entries must stay angular - any straight-line meeting is a "
            "failure, reset. Step 6: The continuity rule: after each entry "
            "and strike, keep walking the circle - the application ends in "
            "motion, ready for the next threat. Step 7: Spar the entries "
            "lightly: partner attacks, you may only answer with entries "
            "from the changes."
        ),
        "key_points": [
            "Never meet the attack's line - step around it to the flank",
            "Deflect along their line while the body moves past",
            "Single change: block, strike, and finish beside them",
            "The blind angle is the target - guards are thin there",
            "Every application ends in motion, ready for the next threat",
        ],
        "requirements": [
            "Full protective gear; a partner feeding attacks",
            "All eight changes and the entries solid at slow speed",
        ],
        "standards": [
            "Ten entries land beside the partner, none met head-on",
            "Strikes controlled and light on every rep",
            "Sparring round: entries only, continuous motion maintained",
        ],
        "citations": [CIT_USADOJO, CIT_FMA, CIT_GW],
        "sig_lens": (
            "His Signature reading of the side entry: the flanking "
            "signature - his covenant never meets force head-on but signs "
            "from the blind angle, always moving."
        ),
    },
    {
        "key": "bgz-multiple-attackers",
        "name": "Multiple Attackers: The Circle Strategy",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The circle is baguazhang's answer to multiple attackers. A "
            "fighter who keeps moving on a circle never lets attackers "
            "surround them: the constant turning keeps all threats in "
            "front, the angular footwork slips between attackers, and each "
            "palm change's direction reversal becomes a tool for facing the "
            "next threat - in fighting terms, the single change is one "
            "block and one strike before changing direction to fight other "
            "opponents. The strategy: keep walking, never get fixed; use "
            "one attacker as a shield against the others; strike and keep "
            "moving - the swimming body applied to the group. Training uses "
            "two, then three partners attacking in turn: the practitioner "
            "walks the circle, and every attack is answered with a change "
            "that turns to face the next attacker. The cardinal rule - "
            "taught from the first day of circle walking - is never stop "
            "moving."
        ),
        "how_it_works": (
            "Step 1: Two partners stand at opposite sides; you walk the "
            "circle between them. Step 2: Partner A attacks slowly - answer "
            "with a single change: deflect, strike the pad, and the "
            "change's reversal turns you to face partner B. Step 3: Partner "
            "B attacks - answer with the next change, turning back to A. "
            "Step 4: Keep the walk going between attacks - the circle never "
            "stops, even when no one is attacking. Step 5: Add a third "
            "partner; the turns must now pick targets - the changes become "
            "target selection. Step 6: Practice the shield: maneuver so "
            "one partner is always between you and the others - the circle "
            "does this naturally if you keep turning. Step 7: Speed up "
            "gradually; the rule is absolute - if you stop moving, the "
            "drill resets."
        ),
        "key_points": [
            "Keep moving on the circle - never let them surround you",
            "Each change's reversal turns you to face the next threat",
            "One block and one strike, then change direction to the next opponent",
            "Use one attacker as a shield against the others",
            "The cardinal rule: never stop moving",
        ],
        "requirements": [
            "Two to three partners; full protective gear; pads",
            "All applications solid one-on-one first",
        ],
        "standards": [
            "Two-attacker drill: five exchanges each, circle never stopped",
            "Three-attacker drill: correct target selection on every turn",
            "Shield positioning held for a full minute",
        ],
        "citations": [CIT_USADOJO, CIT_FMA],
        "sig_lens": (
            "His Signature reading of the circle strategy: the surrounding "
            "signature - no matter how many hands reach for it, his "
            "covenant keeps turning and signs them one by one."
        ),
    },
    {
        "key": "bgz-mastery-circle",
        "name": "Mastery: The Advanced Circle",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Mastery in baguazhang is the circle itself, deepened: the "
            "advanced practitioner shrinks the circle - from twelve feet "
            "toward six, then smaller - until the turns happen in a phone "
            "booth's space, the waist doing what the feet once did. The "
            "advanced circle is walked lower, longer, and with load: "
            "sessions stretch past the hour, the postures are held through "
            "the full eight changes, and the walk continues under "
            "weighted vests or with the great weapons. The internal work "
            "deepens too - the settled breathing becomes the default, the "
            "coiling becomes unconscious, and the eight trigrams become "
            "reflexes rather than concepts. The old schools measured "
            "mastery simply: walk the small circle for an hour, perform "
            "the old eight without a flaw, and answer any attack from the "
            "walk - then walk it all again tomorrow. The circle never "
            "ends; the mastery is in never leaving it."
        ),
        "how_it_works": (
            "Step 1: Shrink your circle by one foot and walk it for a "
            "month - then shrink again; the goal is the smallest circle "
            "you can turn cleanly in. Step 2: Lower the walk: sink one "
            "finger-width below your comfortable depth and hold it for the "
            "session. Step 3: Extend the session: add five minutes a week "
            "until you walk a full hour without stopping. Step 4: Walk the "
            "full old-eight form on the small circle, both directions. Step 5: "
            "Add load: a weighted vest or the great spear - the circle "
            "with weight teaches the deepest root. Step 6: Test the "
            "reflexes: partner attacks at random during the walk - answer "
            "from the walk with the correct change, no preparation. Step 7: "
            "The master's routine: small circle, low walk, full form, "
            "weighted - one hour, every day; the circle is not a drill "
            "anymore, it is where you live."
        ),
        "key_points": [
            "Shrink the circle - the waist learns what the feet once did",
            "Walk lower, longer, and with load",
            "The old eight on the small circle, both directions",
            "Trigrams as reflexes: answer any attack from the walk",
            "The circle never ends - mastery is never leaving it",
        ],
        "requirements": [
            "Years of foundation - this record is the far end of the ladder",
            "A weighted vest; the great weapons; a testing partner",
            "Medical clearance for loaded endurance training",
        ],
        "standards": [
            "One hour of continuous small-circle walking",
            "Old eight performed flawlessly on the small circle",
            "Random attacks answered correctly from the walk, ten of ten",
        ],
        "citations": [CIT_WIKI, CIT_ZBT],
        "sig_lens": (
            "His Signature reading of mastery: the final covenant - the "
            "circle shrunk to a single point and his signature written "
            "there forever, the pen never lifting."
        ),
    },
]
