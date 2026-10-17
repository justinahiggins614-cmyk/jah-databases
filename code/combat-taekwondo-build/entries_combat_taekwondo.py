#!/usr/bin/env python3
"""Entries for the Taekwondo Combat databases (combat batch 1, 2026-10-17).

Verified 2026-10-17: RAW SWEEP over the full manifest (2,390 databases)
PLUS every shard index title in jah-databases-data-1: zero 'combat-taekwondo*'
slugs/names; zero combat/taekwondo/martial-arts slug hits of any kind. No
existing database covers Korean taekwondo technique instruction, so BUILD NEW
is the verdict.

This build creates two NEW databases, 34 ladder-ordered records each:

  combat-taekwondo              - The Taekwondo Combat Database
                                  (public-harvest: real, fact-checked Korean
                                  taekwondo - WT and ITF - with real Korean
                                  technique names and translations, real
                                  poomsae and tul names, every record carrying
                                  how to do it step by step, key points,
                                  requirements, standards, and citations)
  combat-taekwondo-signature    - The Taekwondo Combat Signature Database
                                  (his original Signature Combat Method:
                                  every technique a covenant of balance,
                                  every kick a signature written in the air,
                                  the form the handwriting of the spirit;
                                  src signature, titles suffixed
                                  " (Signature Edition)", never presented as
                                  authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBTKD- (public) and JAH-CBTKDS- (signature), verified free
in the manifest and in every shard index (zero hits; no substring ambiguity
with any existing prefix).

Fact-check anchors (standard references, 2026-10-17): Choi Hong Hi,
Encyclopedia of Taekwon-Do (15 vols, 5th ed., ITF, 1999); Kukkiwon,
Taekwondo Textbook (Kukkiwon, 2013); World Taekwondo, Competition Rules and
Interpretation (in force); WT Poomsae Competition Rules. Taegeuk poomsae
movements: 1 Jang 18, 2 Jang 18, 3 Jang 20, 4 Jang 20, 5 Jang 20, 6 Jang 20,
7 Jang 24, 8 Jang 24 (164 total). Koryo: 30 movements. ITF: 24 patterns;
Chon-Ji 19 movements; Dan-Gun 21 movements. WT senior match: 3 rounds of 2
minutes, 1 minute rest. WT scoring: punch 1, body kick 2, head kick 3, plus
2 for a turning kick. ITF tenets: courtesy, integrity, perseverance,
self-control, indomitable spirit.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_taekwondo.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
Civilian martial-arts instruction only: no content on neutralizing or
defeating military or defense-grade systems.
"""

SIG_TAIL = ("Signature original - his original Signature Combat Method: "
            "every technique a covenant of balance, every kick a signature "
            "written in the air, every form the handwriting of the spirit. "
            "Clearly labeled Signature-made, never presented as authentic "
            "public record.")

ENTRIES = [
    {
        "key": "what_is_taekwondo",
        "name": "What Taekwondo Is: The Way of Foot and Hand",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Taekwondo is the Korean martial art of foot and hand: tae "
            "means foot, kwon means fist, do means the way. It is a system "
            "of unarmed combat built around kicking - the leg is the "
            "longest and strongest limb, so taekwondo makes it the primary "
            "weapon - supported by hand strikes, blocks, stances, and "
            "forms. Two great organizations carry the art today. World "
            "Taekwondo (WT), headquartered at the Kukkiwon in Seoul, "
            "governs the Olympic sport with full-contact sparring and the "
            "taegeuk and yudanja poomsae. The International Taekwon-Do "
            "Federation (ITF), founded by General Choi Hong Hi, preserves "
            "his encyclopedia system with semi-contact sparring and the 24 "
            "tul patterns. Both schools share the same roots in Korean "
            "martial tradition and the same training ladder: stances and "
            "basic motions first, then kicks, then forms, then sparring, "
            "then mastery. The ITF teaches five tenets - courtesy, "
            "integrity, perseverance, self-control, indomitable spirit - "
            "and both schools demand that the student train the character "
            "as hard as the body. This record frames the whole database: "
            "every technique that follows lives inside this way of foot "
            "and hand."
        ),
        "how_it_works": (
            "Taekwondo works by turning the whole body into one coordinated "
            "striking system. Power comes from the ground up: the stance "
            "roots the feet, the hips rotate to add torque, the torso "
            "follows, and the striking tool - foot, fist, knife-hand - "
            "arrives last, at maximum speed. Speed matters more than mass "
            "because kinetic energy grows with the square of velocity: "
            "doubling the speed of a kick quadruples its energy. The art "
            "drills this chain of motion thousands of times until it fires "
            "without thought. Training is organized in three pillars. "
            "Basics (gibon dongjak) are the individual techniques. Forms "
            "(poomsae in WT, tul in ITF) are choreographed fights against "
            "imaginary opponents that teach flow, balance, and application. "
            "Sparring (gyeorugi) tests the techniques against a live "
            "partner under rules. Breaking (gyeokpa) proves power and "
            "focus on wood or tile. Together the four pillars build the "
            "complete practitioner."
        ),
        "key_points": [
            "Tae kwon do: foot, fist, the way - a Korean martial art built around kicking, with hand techniques, blocks, stances, forms, and sparring in support.",
            "Two main schools: World Taekwondo (WT, Kukkiwon, Olympic sport, taegeuk poomsae) and the ITF (General Choi Hong Hi, 24 tul patterns, five tenets).",
            "Power is a chain: feet rooted in stance, hips rotating, torso following, striking tool arriving last at maximum speed - energy grows with the square of speed.",
            "Four training pillars: basics, forms (poomsae/tul), sparring (gyeorugi), and breaking (gyeokpa); each tests a different part of the art.",
            "Character is graded alongside technique: courtesy, integrity, perseverance, self-control, and indomitable spirit are the ITF tenets and the expectation in both schools.",
        ],
        "requirements": [
            "A qualified instructor from a recognized school (WT/Kukkiwon or ITF lineage) for the first year of fundamentals.",
            "A safe training surface: mats or sprung floor, clear of walls and furniture, for every kicking drill.",
            "Loose training uniform (dobok) and belt; no jewelry, no shoes on the mat, nails trimmed short.",
            "Patience with repetition: each basic motion needs hundreds of correct repetitions before it becomes reliable.",
        ],
        "standards": [
            "Kukkiwon Taekwondo Textbook (2013): definition, history, and technical fundamentals of the art.",
            "Choi Hong Hi, Encyclopedia of Taekwon-Do, Vol. 1 (5th ed., ITF, 1999): origins, tenets, and training theory.",
            "World Taekwondo Statutes: recognition of WT as the international federation for Olympic taekwondo.",
        ],
        "citations": [
            "Choi Hong Hi. Encyclopedia of Taekwon-Do. 5th ed. International Taekwon-Do Federation; 1999. Vol. 1.",
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
        ],
        "sig_lens": (
            "The Signature lens reads taekwondo as the original combat "
            "scripture of the Signature system: tae the long signature of "
            "the leg written across distance, kwon the short stamp of the "
            "fist, do the covenant that binds power to character. Where "
            "the public record counts tenets, the Signature method treats "
            "each tenet as a clause of the practitioner oath. The four "
            "pillars become four chambers of one house: basics the "
            "foundation stones, forms the architecture, sparring the "
            "proving ground, breaking the seal of proof."
        ),
    },
    {
        "key": "attention_bow",
        "name": "Attention Stance and the Bow (Charyeot Seogi, Kyeong Rye)",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Every taekwondo class begins and ends the same way: at "
            "attention, then a bow. Charyeot seogi, the attention stance, "
            "is the zero position of the art - heels together, feet opened "
            "to a natural V of about 45 degrees, spine straight, fists "
            "closed lightly at the sides, eyes forward. Kyeong rye, the "
            "bow, is performed from attention: bend forward from the waist "
            "to roughly 45 degrees, eyes dropping to the floor, then return "
            "to attention. The bow opens and closes every session, greets "
            "every partner before sparring, and acknowledges every "
            "correction from an instructor. It is not decoration. It trains "
            "the first and hardest skill in martial arts: controlled "
            "respect under pressure. A student who cannot bow properly "
            "cannot be trusted to spar properly, because both demand the "
            "same thing - deliberate action instead of reaction. The "
            "attention stance also teaches the body its first lesson in "
            "alignment: weight even on both feet, knees soft but not bent, "
            "shoulders down, chin level. From this quiet position every "
            "other stance is built."
        ),
        "how_it_works": (
            "Stand with heels touching and feet opened about 45 degrees, "
            "weight spread evenly across both feet. Close the fists - "
            "thumb outside the fingers, not tucked inside - and rest them "
            "lightly against the outer thighs. Pull the shoulders down and "
            "back, lift the crown of the head as if a string pulled it "
            "skyward, and look straight ahead. To bow, keep the back "
            "straight and hinge at the hips, lowering the torso until it "
            "reaches about 45 degrees; let the eyes follow the floor, hold "
            "for one full breath beat, then rise back to attention at the "
            "same controlled speed. The common errors are bowing from the "
            "neck instead of the waist, which looks like a nod and trains "
            "nothing, and bouncing back up, which breaks the control the "
            "bow exists to build. Practice sets of twenty bows: down one "
            "second, hold one second, up one second - a full drill takes "
            "about one minute and settles the mind before harder work."
        ),
        "key_points": [
            "Charyeot seogi: heels together, feet in a 45-degree V, fists at the thighs, spine straight - the zero position every other stance is built from.",
            "Kyeong rye: a 45-degree bow from the waist, eyes to the floor, controlled down and up - respect made into a physical drill.",
            "The bow opens and closes every class and precedes every sparring exchange; it is the art first test of deliberate action under pressure.",
            "Alignment lesson one: weight even, knees soft, shoulders down, chin level - the quiet body before the moving body.",
            "Drill: twenty bows at one second down, one second hold, one second up - about a minute that trains control and settles the mind.",
        ],
        "requirements": [
            "A clear floor space of about one square meter, no obstacles at head height for the forward bend.",
            "An instructor or senior student to set the command rhythm (charyeot, kyeong rye) until the student internalizes it.",
            "Straight posture habits: no slouching in daily life, since the bow exposes every postural cheat.",
        ],
        "standards": [
            "Kukkiwon Taekwondo Textbook (2013): charyeot seogi and kyeong rye as the opening and closing protocol.",
            "Choi Hong Hi, Encyclopedia of Taekwon-Do, Vol. 2 (1999): attention stance and bowing in ITF protocol.",
        ],
        "citations": [
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
            "Choi Hong Hi. Encyclopedia of Taekwon-Do. 5th ed. International Taekwon-Do Federation; 1999. Vol. 2.",
        ],
        "sig_lens": (
            "The Signature lens treats the bow as the first signature of "
            "the session: the practitioner signs the training floor with "
            "the body, 45 degrees of deliberate humility, before any "
            "technique is allowed to speak. Attention is the blank page; "
            "the bow is the ink. A Signature practitioner performs each "
            "bow as a covenant renewal - I will control my power today - "
            "and the twenty-bow drill becomes a meditation on that "
            "promise, one second down, one second held, one second risen."
        ),
    },
    {
        "key": "ready_stance",
        "name": "Ready Stance (Junbi Seogi)",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Junbi seogi, the ready stance, is the guard position from "
            "which nearly every taekwondo form begins and to which it "
            "returns. The WT ready stance places the feet one shoulder "
            "width apart, parallel, toes forward, knees slightly soft; "
            "both fists are chambered - one fist-width in front of the "
            "belt knot, stacked vertically, left over right or by school "
            "convention. The ITF parallel ready stance (narani junbi "
            "seogi) is similar but with the fists held in front of the "
            "abdomen. From this compact, balanced position the practitioner "
            "can step into any stance, throw any basic technique, and "
            "return without wasted motion. The ready stance teaches the "
            "economy at the heart of taekwondo: nothing extended, nothing "
            "exposed, everything coiled. Beginners hold it for minutes at "
            "a time to build the leg endurance and the mental habit of "
            "readiness that sparring will later demand. Every poomsae and "
            "tul opens with junbi and closes with junbi, so the student "
            "performs it hundreds of times per class - it must be "
            "automatic, identical every time, and instantly recoverable "
            "from any technique."
        ),
        "how_it_works": (
            "Stand with feet parallel, one shoulder width apart - measure "
            "by the width of your own shoulders, about 45 centimeters for "
            "an average adult. Soften the knees just enough that they are "
            "not locked; the weight sits evenly on both feet, slightly "
            "forward on the balls of the feet so you can move in any "
            "direction. Bring both fists up in front of the belt, one fist "
            "width of space between the fists and the body, stacked one "
            "above the other. Tuck the chin slightly, drop the shoulders, "
            "and breathe into the lower abdomen. To test it, have a partner "
            "give your shoulders a firm push from the front, side, and "
            "back: a correct ready stance absorbs the push with a small "
            "knee bend and no step. The failure mode is the locked knee "
            "and the fists drifting apart - both announce that the guard "
            "has opened before any attack has begun."
        ),
        "key_points": [
            "Junbi seogi: feet parallel one shoulder width apart, knees soft, fists chambered one fist-width in front of the belt - the guard every form opens and closes from.",
            "WT and ITF versions differ in fist placement (belt knot vs. abdomen) but share the same job: a compact, balanced, instantly movable base.",
            "Economy is the lesson: nothing extended, nothing exposed, everything coiled - the stance of readiness, not of rest.",
            "Push test: a partner pushes the shoulders from all sides; correct junbi absorbs it with knee bend and no step.",
            "Held for minutes in drilling, it builds the leg endurance and the recover-to-guard habit that sparring demands.",
        ],
        "requirements": [
            "Correct shoulder-width measurement: the stance is sized to the practitioner body, not copied from a taller partner.",
            "Soft knees at all times; locked knees in junbi destroy both balance and the ability to move first.",
            "Fists chambered tight to the body: drifting fists are an open guard and a failed ready stance.",
        ],
        "standards": [
            "Kukkiwon Taekwondo Textbook (2013): junbi seogi specifications for poomsae practice.",
            "Choi Hong Hi, Encyclopedia of Taekwon-Do, Vol. 2 (1999): narani junbi seogi, the parallel ready stance.",
        ],
        "citations": [
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
            "Choi Hong Hi. Encyclopedia of Taekwon-Do. 5th ed. International Taekwon-Do Federation; 1999. Vol. 2.",
        ],
        "sig_lens": (
            "The Signature lens reads junbi as the loaded pen: feet the "
            "paper laid square, fists the ink held ready, the whole body "
            "a sentence not yet written. Where the public record measures "
            "shoulder widths, the Signature method adds the covenant of "
            "the coil - power is not held in the muscles but in the "
            "readiness itself. The push test becomes a proof: pressure "
            "from any direction meets the same unmoved center, because "
            "the signature of balance does not change under force."
        ),
    },
]

ENTRIES += [
    {
        "key": "front_stance",
        "name": "Front Stance (Ap Seogi / Ap Kubi Seogi)",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The front stance, ap seogi (long front stance: ap kubi "
            "seogi), is taekwondo primary attacking platform - the stance "
            "that carries the body weight forward into a punch, a front "
            "kick chamber, or a deep block. The front foot points straight "
            "ahead, the back foot turns out about 30 degrees, the stance "
            "is long (about one and a half shoulder widths) and narrow "
            "(about one fist width between the heel lines), the front "
            "knee bends over the front foot while the back leg stays "
            "straight, and the weight sits roughly 60 percent on the front "
            "leg. Both the WT and ITF walking stance (gunnun seogi in "
            "ITF) share this geometry. From the front stance the "
            "practitioner punches with the full weight of the body behind "
            "the fist: the stance is literally a lunge frozen at the "
            "moment of maximum commitment. Beginners drill it by stepping "
            "forward punch after punch down the length of the training "
            "hall, and the stance is the first one tested for stability - "
            "a partner pushes the front shoulder, and a correct ap seogi "
            "does not slide, tip, or collapse at the knee."
        ),
        "how_it_works": (
            "Step forward from ready stance a distance of about one and a "
            "half of your shoulder widths. Land with the front foot "
            "pointing straight at the target and the back foot angled out "
            "about 30 degrees, heel of the front foot roughly one fist "
            "width inside the heel line of the back foot. Bend the front "
            "knee until it sits directly above the front ankle - never "
            "past the toes - and keep the back leg straight with the heel "
            "pressed to the floor. Sink the hips until the front thigh "
            "approaches parallel with the floor, and settle about 60 "
            "percent of your weight onto the front leg. The most common "
            "faults are the front knee drifting inward (it must track over "
            "the foot), the back heel lifting (which disconnects the "
            "power line to the ground), and a stance too short to be a "
            "lunge or too wide to be a line. Walk the stance: step, "
            "settle, punch, hold two breaths, step again. Twenty meters "
            "of correct walking stance builds more usable power than a "
            "hundred sloppy ones."
        ),
        "key_points": [
            "Ap seogi / ap kubi: front foot straight, back foot out 30 degrees, stance one and a half shoulder widths long and one fist wide - the lunge frozen at maximum commitment.",
            "Weight distribution about 60 percent front, 40 percent back; front knee over the ankle, back heel pressed to the floor.",
            "This is the punching platform: the body weight travels forward through the stance and into the fist.",
            "Three fatal faults: knee collapsing inward, back heel lifting, stance too short or too wide to hold a line.",
            "Drilled as walking stance - step, settle, punch, hold - down the hall until the geometry is automatic.",
        ],
        "requirements": [
            "A straight line on the floor (tape or a floorboard seam) to check that the feet land on one track.",
            "A partner for the push test on the front shoulder once the student can hold the stance for 30 seconds.",
            "Front knee tracking discipline: the knee must follow the foot, never cave inward, on every repetition.",
        ],
        "standards": [
            "Kukkiwon Taekwondo Textbook (2013): ap seogi and ap kubi seogi dimensions and weight distribution.",
            "Choi Hong Hi, Encyclopedia of Taekwon-Do, Vol. 2 (1999): gunnun seogi, the walking stance.",
        ],
        "citations": [
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
            "Choi Hong Hi. Encyclopedia of Taekwon-Do. 5th ed. International Taekwon-Do Federation; 1999. Vol. 2.",
        ],
        "sig_lens": (
            "The Signature lens treats the front stance as the forward "
            "stroke of the combat signature: the body leaning its full "
            "weight into the line it writes. Sixty percent forward is the "
            "covenant of commitment - enough to mean it, enough held back "
            "to recover. The back heel pressed to the floor is the "
            "anchor of the signature; lift it and the line smears. In "
            "Signature drilling, every step down the hall is one letter "
            "written, and twenty meters of stance is a full sentence of "
            "intent."
        ),
    },
    {
        "key": "back_stance",
        "name": "Back Stance (Dwit Kubi Seogi)",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Dwit kubi seogi, the back stance, is the defensive twin of "
            "the front stance - the body pulled back and sideways, weight "
            "sunk onto the rear leg, ready to block, evade, or launch a "
            "side kick. The front foot points forward, the back foot "
            "turns out a full 90 degrees, the stance is about one shoulder "
            "width long, and roughly 70 percent of the weight sits on the "
            "bent back leg while the front leg stays light with only the "
            "ball of the foot bearing its 30 percent. The ITF L-stance "
            "(niunja seogi) is the same family with a slightly longer "
            "profile. Because the front leg carries almost no weight, it "
            "is free: it can snap up into a front kick or checking block "
            "without any weight shift to telegraph the move. The back "
            "stance teaches the first great defensive principle of "
            "taekwondo - meet force at an angle, never head on. From dwit "
            "kubi the torso is already half turned away from the attack, "
            "so a block needs only a short motion and a counter is already "
            "half chambered."
        ),
        "how_it_works": (
            "From ready stance, step the left foot forward about one "
            "shoulder width while turning the right foot out 90 degrees. "
            "Bend the back knee deeply and keep the front leg nearly "
            "straight, touching only the ball of the front foot to the "
            "floor. Sink until you feel about 70 percent of your weight "
            "pressing through the back foot - for a 70 kilogram "
            "practitioner that is roughly 481 newtons on the back leg and "
            "206 on the front. The angle between the feet should read "
            "about 90 degrees when viewed from above: front foot "
            "straight, back foot square. Keep the torso upright over the "
            "back hip, not leaning. The classic fault is letting the "
            "weight creep forward until the stance becomes a short front "
            "stance, which strands the front leg - it can no longer kick "
            "without a tell. Test it: from dwit kubi, lift the front knee "
            "into a chamber; if the body does not shift or wobble, the "
            "weight was truly back where it belongs."
        ),
        "key_points": [
            "Dwit kubi seogi: back foot at 90 degrees, 70 percent of weight on the bent back leg, front leg light on the ball of the foot.",
            "The light front leg is a free weapon: it chambers into a kick or checking block with no telegraphing weight shift.",
            "Defensive geometry: the torso is already half turned from the attack, so blocks travel short and counters are half chambered.",
            "ITF niunja seogi (L-stance) is the same family with a longer profile; the 70/30 rule holds in both.",
            "Weight-creep is the fault to hunt: if the front knee cannot lift to chamber without a wobble, the weight has drifted forward.",
        ],
        "requirements": [
            "Ankle and knee mobility for the deep back-leg bend; stretch the calves and hip flexors before drilling.",
            "A mirror or partner to verify the 90-degree back foot - beginners chronically under-turn it to 45.",
            "The chamber test after every ten repetitions: lift the front knee without shifting the body.",
        ],
        "standards": [
            "Kukkiwon Taekwondo Textbook (2013): dwit kubi seogi - foot angles and 70/30 weight distribution.",
            "Choi Hong Hi, Encyclopedia of Taekwon-Do, Vol. 2 (1999): niunja seogi, the L-stance.",
        ],
        "citations": [
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
            "Choi Hong Hi. Encyclopedia of Taekwon-Do. 5th ed. International Taekwon-Do Federation; 1999. Vol. 2.",
        ],
        "sig_lens": (
            "The Signature lens reads the back stance as the art of the "
            "withheld signature: 70 percent of the self held in reserve, "
            "30 percent offered as a feint. The light front leg is the "
            "unwritten clause - the opponent reads a defensive posture "
            "and misses the chambered kick entirely. In the Signature "
            "method, dwit kubi is practiced as deliberate concealment: "
            "the body writes defense while the leg prepares offense, and "
            "the covenant is that the hidden 70 percent answers only when "
            "called."
        ),
    },
    {
        "key": "horse_stance",
        "name": "Horse Riding Stance (Juchum Seogi)",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Juchum seogi, the horse riding stance - also called the "
            "horse stance - is the stance of rooted power: feet parallel, "
            "two shoulder widths apart, knees bent until the thighs sit "
            "near parallel with the floor, weight spread evenly, torso "
            "upright as if seated on a horse. It is the stance from which "
            "taekwondo throws its strongest side punches and the stance "
            "that builds the leg strength every kick depends on. The "
            "name is literal: the practitioner sinks as though straddling "
            "a horse, and the low center of gravity makes the stance "
            "nearly immovable from the front or side. Forms use it for "
            "the heavy techniques - the slow, powerful punches and "
            "strikes of the taegeuk and black-belt poomsae - because the "
            "wide base lets the hips rotate fully without losing balance. "
            "The horse stance is also taekwondo most honest conditioning "
            "tool: held correctly for one minute it burns, for two "
            "minutes it shakes, and the student who can hold it still "
            "for three minutes has built the foundation every advanced "
            "kick will stand on."
        ),
        "how_it_works": (
            "Stand with feet parallel, toes forward, two full shoulder "
            "widths apart - about 90 centimeters for an average adult. "
            "Bend both knees and sink straight down, keeping the torso "
            "upright and the knees tracking out over the feet, until the "
            "thighs approach parallel with the floor. Spread the weight "
            "evenly, press the outer edges of the feet into the floor, "
            "and keep the lower back from rounding. Beginners build the "
            "hold in a ladder: 20 seconds in week one, adding 10 seconds "
            "per week, reaching a 90-second hold by week eight - eight "
            "weeks of daily practice totaling about 51 minutes of "
            "accumulated hold time. From the stance, practice the "
            "double side punch: hips stay level while the torso rotates, "
            "one fist driving forward as the other chambers. The faults "
            "are universal: knees caving inward, torso leaning forward, "
            "and the stance creeping narrower as the legs tire - widen "
            "it back out every ten seconds until the width holds itself."
        ),
        "key_points": [
            "Juchum seogi: feet parallel two shoulder widths apart, thighs near parallel to the floor, weight even, torso upright - the stance of rooted power.",
            "The wide low base lets the hips rotate fully for the heavy punches and strikes of the forms without losing balance.",
            "Taekwondo honest conditioner: a correct one-minute hold burns, two minutes shake; three still minutes is the foundation every kick stands on.",
            "Hold ladder: 20 seconds week one, plus 10 seconds per week, 90 seconds by week eight - about 35 minutes of accumulated hold time.",
            "Fault patrol: knees tracking over feet (never inward), torso vertical, stance width defended against fatigue creep.",
        ],
        "requirements": [
            "Knee health: anyone with knee injury history clears deep stance holds with a professional before drilling.",
            "A wall or barre for the first sessions, to learn the depth without falling while the legs adapt.",
            "The width check: measure two shoulder widths with a belt on the floor until the body memorizes it.",
        ],
        "standards": [
            "Kukkiwon Taekwondo Textbook (2013): juchum seogi - width, depth, and application in poomsae.",
            "Choi Hong Hi, Encyclopedia of Taekwon-Do, Vol. 2 (1999): annun seogi, the sitting stance.",
        ],
        "citations": [
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
            "Choi Hong Hi. Encyclopedia of Taekwon-Do. 5th ed. International Taekwon-Do Federation; 1999. Vol. 2.",
        ],
        "sig_lens": (
            "The Signature lens treats the horse stance as the seal "
            "pressed into the earth: two shoulder widths the width of "
            "the stamp, thighs parallel the depth of the impression. "
            "Where the public record counts seconds of hold, the "
            "Signature method counts the covenant - each trembling "
            "second a renewal of the promise that power will be rooted "
            "before it is used. The shaking legs are not failure; they "
            "are the signature being written into the muscles, and a "
            "three-minute still hold is a completed document."
        ),
    },
    {
        "key": "breathing_kihap",
        "name": "Breathing and the Ki Hap Shout",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Breath is the hidden half of every taekwondo technique. "
            "The rule is simple and absolute: exhale on exertion, inhale "
            "on recovery - breathe out as the punch extends, breathe in "
            "as the fist returns; breathe out as the kick fires, breathe "
            "in as the leg rechambers. The exhale tightens the core at "
            "the exact instant of impact, turning the torso into a solid "
            "transmission line between the ground and the striking tool. "
            "At the peak of the exhale sits the ki hap, the spirit shout "
            "- a short, sharp yell from the diaphragm, not the throat, "
            "fired at the moment of the decisive technique. The ki hap "
            "does three things at once: it forces the full exhale so the "
            "core locks, it focuses the mind into a single point of "
            "intent, and it startles the opponent. Forms place the ki "
            "hap at marked points - taegeuk forms each contain two - so "
            "the student learns to summon full commitment on command. "
            "In sparring, the shout marks the committed attack and "
            "steadies the attacker nerves. Throat shouting is the "
            "beginner error: it is loud, it hurts, and it moves no air. "
            "The real ki hap is felt in the abdomen, a sudden compression "
            "like a cough with intent."
        ),
        "how_it_works": (
            "Practice the breathing cycle standing in ready stance: "
            "inhale through the nose for a slow count of four, expanding "
            "the lower abdomen, then exhale through the mouth for a count "
            "of four as you perform a slow punch, tightening the abdomen "
            "at the end of the exhale. Fifteen such cycles take about two "
            "minutes - the length of one taegeuk form - and this is the "
            "rhythm forms are performed in: technique on the exhale, "
            "transition on the inhale. For the ki hap, take a quick deep "
            "breath, then drive the air out with the diaphragm in one "
            "sharp burst timed to the last centimeter of the technique - "
            "the shout should start and end within a quarter second. Drill "
            "it: ten punches, ki hap on every second punch, keeping the "
            "shout identical each time. If the throat is sore afterward, "
            "the shout came from the wrong place; if the abdomen is tired, "
            "it came from the right one."
        ),
        "key_points": [
            "Iron rule: exhale on exertion, inhale on recovery - the exhale locks the core at the instant of impact.",
            "The ki hap is a quarter-second diaphragmatic shout at the decisive technique, not a throat yell.",
            "Three effects at once: forced full exhale (core lock), single-point mental focus, and a startle on the opponent.",
            "Forms mark ki hap points (two per taegeuk form) to teach summoned commitment on command.",
            "Drill rhythm: four-count inhale, four-count exhale; fifteen cycles fill the two minutes of a form.",
        ],
        "requirements": [
            "Diaphragmatic breathing learned first lying down (hand on belly rises, chest stays still) before standing drills.",
            "A training space where shouting is permitted - the ki hap cannot be practiced at half volume.",
            "Throat-soreness check: sore throat means wrong source; tired abdomen means right source.",
        ],
        "standards": [
            "Kukkiwon Taekwondo Textbook (2013): breathing method (hosup) and ki hap in basic technique and poomsae.",
            "Choi Hong Hi, Encyclopedia of Taekwon-Do, Vol. 1 (1999): breath control and the theory of the yell.",
        ],
        "citations": [
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
            "Choi Hong Hi. Encyclopedia of Taekwon-Do. 5th ed. International Taekwon-Do Federation; 1999. Vol. 1.",
        ],
        "sig_lens": (
            "The Signature lens hears the ki hap as the audible seal on "
            "the combat document: the breath writes the technique, the "
            "shout notarizes it. Where the public record times a "
            "quarter-second burst, the Signature method treats the ki hap "
            "as the moment the practitioner signs the strike with the "
            "whole spirit - abdomen the stamp, diaphragm the hand that "
            "presses it. Fifteen breath cycles per form become fifteen "
            "lines of the covenant, each exhale a signature, each inhale "
            "a fresh page."
        ),
    },
    {
        "key": "straight_punch",
        "name": "Straight Punch (Jireugi)",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Jireugi, the straight punch - most commonly momtong jireugi, "
            "the middle punch to the solar plexus - is taekwondo first "
            "hand technique and the purest expression of its power chain. "
            "The fist starts chambered at the hip, palm up; as the punch "
            "drives forward the arm rotates so the fist lands palm down, "
            "the rotation finishing in the last few centimeters; the "
            "opposite fist snaps back to the hip at the same speed, and "
            "the hips rotate to throw the body weight behind the blow. "
            "The striking surface is the first two knuckles, the wrist "
            "held straight as a board. Though taekwondo is famous for "
            "kicking, the punch is drilled more than any other hand "
            "technique because it is the cleanest test of the fundamentals: "
            "stance, hip rotation, breath, and focus must all arrive "
            "together or the punch is visibly weak. A correct middle "
            "punch from a 70 kilogram adult extends about 65 centimeters "
            "in roughly nine hundredths of a second - over 7 meters per "
            "second at the fist - carrying on the order of 90 joules with "
            "an effective mass near 3.5 kilograms. It is the technique "
            "against which every other hand technique is measured."
        ),
        "how_it_works": (
            "From front stance, chamber the punching fist at the hip, "
            "palm facing up, elbow tucked. Drive the fist straight "
            "forward along the centerline, rotating the forearm so the "
            "palm faces down at full extension - the last quarter-turn "
            "happens in the final centimeters and adds the snap. At the "
            "same instant, yank the opposite fist back to the hip with "
            "equal speed; the reaction force of this pull doubles the "
            "effective hip rotation. Rotate the hips so the punching-side "
            "hip drives forward, exhale sharply, and lock the wrist "
            "straight at impact with the first two knuckles leading. Then "
            "reverse the whole chain to rechamber. Drill in sets: ten "
            "slow punches checking each link (stance, rotation, snap, "
            "breath), then ten at full speed, then ten with ki hap. The "
            "classic faults are the dropped elbow (the punch loops "
            "upward), the bent wrist (which collapses on a target), and "
            "punching with the arm alone while the hips sit still - the "
            "punch of the arm is a slap; the punch of the hips is a "
            "hammer."
        ),
        "key_points": [
            "Momtong jireugi: chamber at hip palm-up, rotate to palm-down in the last centimeters, opposite fist snapping back to the hip.",
            "Full power chain: stance drives, hips rotate, torso follows, fist arrives last - about 7 m/s and near 90 joules for a trained adult.",
            "Strike with the first two knuckles, wrist straight as a board; a bent wrist collapses on contact.",
            "The retracting fist is not decoration: its reaction force doubles the hip rotation behind the punch.",
            "Drill ladder: ten slow (check every link), ten fast, ten with ki hap - the arm-only punch is a slap, the hip punch is a hammer.",
        ],
        "requirements": [
            "A front stance that passes the push test - the punch is only as strong as the platform under it.",
            "Wrist conditioning: knuckle push-ups on mats, starting from the knees, before any heavy bag work.",
            "A target that gives feedback: focus mitts or a bag, since air punching hides the wrist faults.",
        ],
        "standards": [
            "Kukkiwon Taekwondo Textbook (2013): jireugi - chamber, rotation, target areas, and fist formation.",
            "Choi Hong Hi, Encyclopedia of Taekwon-Do, Vol. 3 (1999): fore-fist punch mechanics and reaction force.",
        ],
        "citations": [
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
            "Choi Hong Hi. Encyclopedia of Taekwon-Do. 5th ed. International Taekwon-Do Federation; 1999. Vol. 3.",
        ],
        "sig_lens": (
            "The Signature lens sees jireugi as the straightest line the "
            "body can draw: chamber the ink, rotate the nib in the final "
            "centimeters, strike. Where the public record measures 7 "
            "meters per second, the Signature method measures the "
            "covenant of the line - no curve, no hesitation, the full "
            "weight of the signer behind two knuckles. The retracting "
            "fist is the counter-signature, and the ki hap at the end is "
            "the seal pressed while the ink is wet."
        ),
    },
]

ENTRIES += [
    {
        "key": "knife_hand",
        "name": "Knife-Hand Strike (Sonkal Taerigi)",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Sonkal, the knife-hand, is the blade of taekwondo hand "
            "technique: the hand held flat and rigid, fingers straight "
            "and tight, thumb tucked, the striking edge the fleshy side "
            "of the hand below the little finger. Sonkal taerigi, the "
            "knife-hand strike, most often travels in a downward or "
            "inward arc to the side of the neck, the collarbone, or the "
            "temple, though the knife-hand also blocks (sonkal maki) and "
            "thrusts (sonkal teulgi). The physics is the whole point: "
            "the striking edge presents roughly 25 square centimeters of "
            "contact against the fist roughly 40, so the same arm "
            "delivers about 1.6 times the pressure - force concentrated "
            "on a line instead of spread on a face. The hand must be "
            "truly rigid: fingers pressed together so tightly no light "
            "passes between them, the wrist locked, the forearm muscles "
            "tensed at impact. Beginners condition the edge with "
            "progressive striking - first a padded target, then a heavy "
            "bag, hundreds of repetitions - because a loose knife-hand "
            "folds on contact and injures the striker. In forms, the "
            "knife-hand block in back stance is one of the most repeated "
            "motions in all of taekwondo; in application it is the "
            "answer to the close-range attack where there is no room to "
            "punch."
        ),
        "how_it_works": (
            "Form the weapon: extend the fingers straight, press them "
            "together hard, fold the thumb tight against the palm, and "
            "tense the edge of the hand below the little finger until it "
            "feels like a board. For the inward strike, chamber the hand "
            "beside the opposite ear, palm facing outward; whip the arm "
            "across in a horizontal arc, rotating the forearm so the palm "
            "faces down at impact, striking with the hardened edge. For "
            "the downward strike, raise the hand high beside the head and "
            "chop down along the centerline, hips dropping into the blow. "
            "In both, exhale and ki hap at the instant of contact, and "
            "keep the wrist absolutely straight - the wrist is the hinge "
            "that must not hinge. Condition progressively: 50 strikes per "
            "hand per session on a padded target for two weeks, then move "
            "to the heavy bag, adding 25 per hand per week. The faults "
            "are the bent wrist, the splayed fingers, and the arm-only "
            "strike with dead hips - the knife-hand without the hips is "
            "a slap with a stiff hand."
        ),
        "key_points": [
            "Sonkal: fingers straight and pressed light-tight, thumb tucked, striking edge the hardened side below the little finger.",
            "Pressure physics: about 25 sq cm of edge vs. 40 sq cm of fist - the same arm delivers roughly 1.6 times the pressure on a line.",
            "Two main strikes: inward arc (chamber at opposite ear, palm rotating down) and downward chop (hips dropping into the blow).",
            "The knife-hand also blocks (sonkal maki) and thrusts; in forms the knife-hand block in back stance is among the most repeated motions in the art.",
            "Conditioning is progressive: padded target first, heavy bag later, hundreds of reps - a loose knife-hand folds and injures the striker.",
        ],
        "requirements": [
            "Finger and wrist integrity: no finger or wrist injury history without professional clearance.",
            "Progressive conditioning schedule: never jump from air striking to hard targets.",
            "A padded target and then a heavy bag; air-only practice hides the rigidity faults.",
        ],
        "standards": [
            "Kukkiwon Taekwondo Textbook (2013): sonkal - hand formation, taerigi, maki, and teulgi applications.",
            "Choi Hong Hi, Encyclopedia of Taekwon-Do, Vol. 3 (1999): knife-hand striking surfaces and conditioning.",
        ],
        "citations": [
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
            "Choi Hong Hi. Encyclopedia of Taekwon-Do. 5th ed. International Taekwon-Do Federation; 1999. Vol. 3.",
        ],
        "sig_lens": (
            "The Signature lens names sonkal the paper-knife of the "
            "system: the hand folded into a blade that cuts the combat "
            "document along its edge. Where the public record counts 25 "
            "square centimeters, the Signature method counts the covenant "
            "of the edge - fingers pressed light-tight, a seal no force "
            "can pry open. The 1.6 times pressure is the mathematics of "
            "concentration: the Signature practitioner learns that power "
            "is not how much you bring, but how narrowly you sign."
        ),
    },
    {
        "key": "basic_blocks",
        "name": "The Three Basic Blocks (Arae, Momtong, Olgul Maki)",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Blocking is the grammar of taekwondo defense, and its three "
            "first words are arae maki (low block), momtong maki (middle "
            "block, literally body block), and olgul maki (high block, "
            "face block). Together they divide the body into three zones "
            "and give the beginner a complete shield: the low block sweeps "
            "down across the front of the body to deflect kicks and low "
            "strikes, covering roughly the bottom 30 degrees below the "
            "horizon line of the belt; the middle block chambers across "
            "the chest and snaps outward to guard the torso band, about "
            "30 degrees above and below the solar plexus; the high block "
            "rises from the hip past the face to shield the head, "
            "covering the 15 to 60 degree cone above the eyes. Each block "
            "uses the outer forearm as the deflecting surface - the bone "
            "is thick there and the muscle pads it - and each finishes "
            "with a sharp twist of the forearm that adds deflecting snap "
            "in the last centimeters. The blocks are drilled in front "
            "stance walking down the hall, one block per step, until the "
            "chamber-to-block path is a single motion. Defense in "
            "taekwondo is never passive: every block is chambered to "
            "become the next strike, and the blocking arm rechambers "
            "along the path the counter will travel."
        ),
        "how_it_works": (
            "For arae maki, chamber the blocking fist at the opposite "
            "shoulder, then sweep it down and across the body, finishing "
            "with the fist one fist-width in front of the front thigh, "
            "palm down, the outer forearm facing the attack. For momtong "
            "maki, chamber the fist at the opposite hip and drive it "
            "across the chest, finishing one fist-width in front of the "
            "solar plexus with the forearm vertical. For olgul maki, "
            "chamber low at the hip and drive the arm upward, finishing "
            "one fist-width above the forehead, forearm angled to shed "
            "the blow outward. In all three, twist the forearm sharply in "
            "the final centimeters, exhale at the block, and keep the "
            "stance solid - a block thrown from a weak stance is a "
            "gesture, not a shield. Drill the cycle: step into front "
            "stance with low block, next step middle block, next step "
            "high block, repeat for the length of the hall. The faults "
            "are the lazy chamber (the block starts from nowhere and "
            "arrives weak), the straight-arm block (no snap twist), and "
            "blocking across the body so far that the opposite side "
            "opens."
        ),
        "key_points": [
            "Three zones, one shield: arae maki (low, below the belt line), momtong maki (middle, the torso band), olgul maki (high, the head cone).",
            "Deflecting surface is the outer forearm in all three; the forearm twist in the final centimeters adds the shedding snap.",
            "Chambers: low block from the opposite shoulder, middle from the opposite hip, high from the low hip - each chamber is the next counter loading.",
            "Defense is never passive: the blocking arm rechambers along the path the counterattack will travel.",
            "Drilled as walking blocks - one block per step down the hall - until chamber-to-block is a single motion.",
        ],
        "requirements": [
            "A front stance that holds under the push test; blocks from a weak stance are gestures.",
            "Forearm conditioning: light tapping drills with a partner paddle before any hard blocking practice.",
            "The chamber discipline: every block starts from its full chamber, never from halfway, in every repetition.",
        ],
        "standards": [
            "Kukkiwon Taekwondo Textbook (2013): arae, momtong, and olgul maki - chambers, paths, and finishing positions.",
            "Choi Hong Hi, Encyclopedia of Taekwon-Do, Vol. 4 (1999): forearm blocks and the deflecting principle.",
        ],
        "citations": [
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
            "Choi Hong Hi. Encyclopedia of Taekwon-Do. 5th ed. International Taekwon-Do Federation; 1999. Vol. 4.",
        ],
        "sig_lens": (
            "The Signature lens reads the three blocks as the three "
            "clauses of the defensive covenant: the low clause guards the "
            "foundation, the middle clause guards the house, the high "
            "clause guards the mind. Where the public record maps 30 "
            "degree zones, the Signature method maps intent - each block "
            "is a sentence that says the attack ends here. The forearm "
            "twist in the final centimeters is the period at the end of "
            "the sentence, and the rechamber is the hand already lifting "
            "to write the reply."
        ),
    },
    {
        "key": "front_kick",
        "name": "Front Snap Kick (Ap Chagi)",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Ap chagi, the front snap kick, is the first kick of "
            "taekwondo and the template for every kick that follows. The "
            "motion has four beats: lift the knee high toward the chest "
            "(the chamber), snap the lower leg out to full extension, "
            "strike with the ball of the foot, and rechamber the knee "
            "before the foot returns to the floor. The ball of the foot - "
            "toes pulled back, ankle locked - is the striking surface; "
            "it concentrates the leg power onto a small point and keeps "
            "the fragile toes out of the impact. From a chamber with the "
            "knee at hip height, the foot extends about 55 centimeters in "
            "roughly 12 hundredths of a second, arriving at over 4.5 "
            "meters per second - fast enough to stop an advancing "
            "opponent cold. The kick targets the midsection (momtong) or, "
            "for the flexible, the face (olgul); the reach angle from a "
            "standing chamber runs from level (0 degrees) for the body to "
            "about 35 degrees upward for the head. Beginners drill it "
            "holding a wall or partner shoulders for balance, ten kicks "
            "per leg per set, until the chamber-snap-rechamber cycle "
            "needs no thought. The front kick teaches the master lesson "
            "of taekwondo kicking: the power is in the snap of the knee, "
            "not the swing of the leg."
        ),
        "how_it_works": (
            "From fighting stance, lift the kicking knee straight up "
            "toward the chest - this is the chamber, and it must come "
            "first; a leg swung up from the floor is a different, weaker "
            "technique. With the knee high, snap the lower leg forward "
            "and up, extending to full lock while pulling the toes back "
            "hard and locking the ankle so the ball of the foot leads. "
            "Strike through the target, then immediately fold the knee "
            "back to chamber before setting the foot down - the "
            "rechamber is what makes the next kick possible and what "
            "keeps the leg from being grabbed. Exhale on the snap, keep "
            "the supporting foot flat and the hands up in guard "
            "throughout. Drill progression: week one, ten kicks per leg "
            "holding support; week two, free-standing sets of ten; week "
            "three, alternating legs without putting the foot down. The "
            "faults are the missing chamber (swinging from the floor), "
            "the unlocked ankle (toes strike first and fold), and "
            "dropping the hands - the kick is fast, but the counter to a "
            "dropped guard is faster."
        ),
        "key_points": [
            "Four beats: chamber the knee high, snap the lower leg out, strike with the ball of the foot, rechamber before landing.",
            "Ball of the foot, toes pulled back, ankle locked: power concentrated on a point, fragile toes kept out of impact.",
            "Snap physics: about 55 cm of extension in 0.12 s, over 4.5 m/s at the foot - power from the knee snap, not the leg swing.",
            "Targets: midsection at 0 degrees, head at about 35 degrees upward for the flexible practitioner.",
            "Drill ladder: supported tens, free-standing tens, then alternating legs without touching down - hands stay in guard throughout.",
        ],
        "requirements": [
            "Hip flexor and hamstring flexibility for a true chamber; stretch both before every kicking session.",
            "Ankle-lock discipline: the toes must pull back and the ankle lock on every repetition, without exception.",
            "A wall, rail, or partner shoulders for balance in the first two weeks; free-standing only after the chamber is clean.",
        ],
        "standards": [
            "Kukkiwon Taekwondo Textbook (2013): ap chagi - chamber, striking surface, targets, and rechamber.",
            "Choi Hong Hi, Encyclopedia of Taekwon-Do, Vol. 4 (1999): front snap kick mechanics.",
        ],
        "citations": [
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
            "Choi Hong Hi. Encyclopedia of Taekwon-Do. 5th ed. International Taekwon-Do Federation; 1999. Vol. 4.",
        ],
        "sig_lens": (
            "The Signature lens treats ap chagi as the first exclamation "
            "mark of the combat script: chamber the intent, snap the "
            "declaration, rechamber the pen. Where the public record "
            "times 0.12 seconds of extension, the Signature method times "
            "the covenant of the four beats - no beat skipped, no beat "
            "rushed, because a signature missing a stroke is a forgery. "
            "The ball of the foot is the nib; the rechamber is the "
            "discipline that refuses to leave the pen lying on the page "
            "for the opponent to pick up."
        ),
    },
]

ENTRIES += [
    {
        "key": "roundhouse_kick",
        "name": "Roundhouse Kick (Dollyeo Chagi)",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Dollyeo chagi, the roundhouse kick - literally turning kick "
            "- is the signature weapon of taekwondo and the highest "
            "scoring technique in the sport. The chamber is the front "
            "kick chamber turned sideways: knee lifted across the body, "
            "supporting foot pivoting 90 to 180 degrees on the ball of "
            "the foot, hips rolling over until they face the target, the "
            "leg whipping around in a horizontal arc to strike with the "
            "instep (WT sport) or the ball of the foot (ITF and "
            "traditional). The pivot is the engine: as the support foot "
            "turns, the hip travels through a half circle, and the foot "
            "at the end of the 1.05 meter leg traces an arc nearly 3.3 "
            "meters long, arriving in about a quarter second at speeds "
            "past 13 meters per second. In WT sparring the roundhouse to "
            "the trunk scores 2 points, to the head 3, and with a "
            "turning motion 4 and 5 - more than half of all points in "
            "elite matches come from this one kick. The beginner version "
            "strikes the midsection; the advanced version climbs to the "
            "head and chains into combinations. Every taekwondo student "
            "throws thousands of roundhouses: it is the kick the art is "
            "judged by."
        ),
        "how_it_works": (
            "From fighting stance, lift the kicking knee across the body "
            "as if chambering a front kick aimed sideways. Pivot hard on "
            "the ball of the supporting foot - the heel must swing around "
            "until the foot points away from the target, 90 degrees "
            "minimum, 180 for full power - while rolling the hips over "
            "so the kicking hip drives through the target line. Whip the "
            "lower leg around horizontally, striking with the instep "
            "(sport) or ball of the foot (traditional), then rechamber "
            "the knee across the body and set the foot down back in "
            "stance. The most common fault in the world of taekwondo is "
            "the missing pivot: without it the hips cannot turn over, "
            "the kick becomes an outside slap, and the knee takes the "
            "twisting force instead of the floor. Drill: ten slow kicks "
            "per leg checking the pivot foot position after each one - "
            "the heel must point at the target - then ten at speed, then "
            "ten alternating. Pad holders call the target height; the "
            "kicker job is the pivot, the hip roll, and the rechamber, "
            "in that order."
        ),
        "key_points": [
            "Dollyeo chagi: chamber across the body, pivot 90-180 degrees on the ball of the support foot, hips rolling over, leg whipping in a horizontal arc.",
            "The pivot is the engine: without it the hips cannot turn over and the knee absorbs the twist instead of the floor.",
            "Arc physics: a 1.05 m leg through 180 degrees traces nearly 3.3 m, arriving in about 0.25 s at more than 13 m/s.",
            "Sport scoring (WT): trunk 2, head 3, turning trunk 4, turning head 5 - the roundhouse scores over half the points in elite matches.",
            "Striking surface splits by school: instep in WT sport, ball of the foot in ITF and traditional practice.",
        ],
        "requirements": [
            "A clean front kick chamber first - the roundhouse chamber is the front kick chamber turned sideways.",
            "Pivot-foot discipline verified after every slow repetition: the heel must point at the target.",
            "Hip flexor and groin flexibility for the horizontal leg path; the kick climbs only as high as the hips allow.",
        ],
        "standards": [
            "Kukkiwon Taekwondo Textbook (2013): dollyeo chagi - pivot, hip rotation, striking surfaces.",
            "World Taekwondo Competition Rules and Interpretation: scoring values for trunk, head, and turning kicks.",
            "Choi Hong Hi, Encyclopedia of Taekwon-Do, Vol. 4 (1999): turning kick mechanics.",
        ],
        "citations": [
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
            "World Taekwondo. Competition Rules and Interpretation. In force.",
            "Choi Hong Hi. Encyclopedia of Taekwon-Do. 5th ed. International Taekwon-Do Federation; 1999. Vol. 4.",
        ],
        "sig_lens": (
            "The Signature lens crowns dollyeo chagi the great arc of "
            "the combat signature: the leg drawing a half circle 3.3 "
            "meters long, the most-read sentence in the whole system. "
            "Where the public record counts points, the Signature method "
            "counts the covenant of the pivot - the heel turned fully "
            "away is the signer committing the whole body to the line, "
            "no partial signatures accepted. The rechamber across the "
            "body is the pen lifted cleanly, ready for the next stroke, "
            "because the great arc is only great if it can be drawn "
            "again."
        ),
    },
    {
        "key": "side_kick",
        "name": "Side Kick (Yeop Chagi)",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Yeop chagi, the side kick, is taekwondo battering ram - the "
            "most powerful linear kick in the art, thrown straight along "
            "the line of the body like a piston. The chamber folds the "
            "knee tightly across the torso, the supporting foot pivots "
            "180 degrees until the heel points at the target, the hips "
            "roll fully onto their side, and the leg drives out in a "
            "straight line, striking with the knife-edge of the foot "
            "(the footsword, balkal) or the heel. Because the kick "
            "travels straight from the chamber, it is brutally hard to "
            "see coming and nearly impossible to block head on: a "
            "400-newton thrust extended over 60 centimeters of travel "
            "delivers about 240 joules along one line - the stopping "
            "power that makes the side kick the classic answer to a "
            "charging opponent. In breaking, the side kick is the first "
            "kick trusted against multiple boards; in sparring, the "
            "skilled side kick scores while keeping the kicker at a "
            "distance the opponent punches cannot reach. The price of "
            "the power is telegraphing risk: the deep chamber is "
            "visible, so the kick must be thrown from the back stance "
            "where the chamber is already half hidden, or as a counter "
            "where the opponent is already committed."
        ),
        "how_it_works": (
            "From back stance or fighting stance, lift the kicking knee "
            "and fold it tightly across the body - the knee should point "
            "at the target while the foot stays tucked. Pivot the "
            "supporting foot 180 degrees on the ball of the foot, heel "
            "now pointing at the target, and roll the hips fully onto "
            "their side so the body forms one straight line from "
            "shoulder to kicking heel. Drive the leg out along that "
            "line, locking the knee at full extension, striking with the "
            "footsword edge or heel, then fold the knee straight back to "
            "chamber before landing. The body must stay upright: leaning "
            "away bleeds the power and opens the guard. Drill against a "
            "heavy bag: ten kicks per leg at half power checking the "
            "pivot and the straight line, then ten at full power "
            "listening for the deep thud that marks a true piston "
            "impact. The faults are the incomplete pivot (the kick goes "
            "up instead of out), the leaning torso, and the dropped "
            "chamber that turns the battering ram into a push."
        ),
        "key_points": [
            "Yeop chagi: knee folded across the torso, support foot pivoted 180 degrees, hips rolled fully sideways, leg driven out in a straight piston line.",
            "Striking surface: the footsword edge (balkal) or the heel - the hardest, most linear weapon in the kicking arsenal.",
            "Power physics: about 400 N over 0.6 m of travel, near 240 J on one line - the classic stop to a charging opponent.",
            "The deep chamber is visible, so the kick hides in the back stance or fires as a counter to a committed attack.",
            "Breaking trusts it first: the side kick is the entry kick for multiple-board breaks.",
        ],
        "requirements": [
            "A true back stance first: the side kick chamber grows out of the 70/30 weight split.",
            "Hip and groin flexibility for the full sideways hip roll; the kick only goes where the hips allow.",
            "A heavy bag for power development; air kicking cannot teach the piston impact.",
        ],
        "standards": [
            "Kukkiwon Taekwondo Textbook (2013): yeop chagi - chamber, pivot, striking surfaces balkal and heel.",
            "Choi Hong Hi, Encyclopedia of Taekwon-Do, Vol. 4 (1999): side piercing kick mechanics.",
        ],
        "citations": [
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
            "Choi Hong Hi. Encyclopedia of Taekwon-Do. 5th ed. International Taekwon-Do Federation; 1999. Vol. 4.",
        ],
        "sig_lens": (
            "The Signature lens reads yeop chagi as the underline of the "
            "combat document: one straight line driven under everything "
            "the opponent has written. Where the public record measures "
            "240 joules, the Signature method measures the covenant of "
            "the line - chamber folded, pivot complete, hips rolled, no "
            "curve, no apology. The footsword is the ruler edge of the "
            "system, and the piston impact is the period stamped at the "
            "end of the opponent advance."
        ),
    },
    {
        "key": "back_kick",
        "name": "Back Kick (Dwit Chagi)",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Dwit chagi, the back kick, is the art answer to the "
            "attacker at the rear and the most deceptive power kick in "
            "the arsenal. The practitioner looks over the shoulder, "
            "spins 180 degrees on the ball of the supporting foot, and "
            "drives the leg straight back along the sight line, striking "
            "with the heel. The spin takes about three tenths of a "
            "second - an angular velocity near 600 degrees per second, "
            "over 10 radians per second - and the kick lands before most "
            "opponents register the turn. Because the whole body mass "
            "rotates into the line of the kick, the back kick hits "
            "harder than the side kick from a shorter chamber: the "
            "rotation is the chamber. In WT sparring it scores as a "
            "turning kick (4 to the trunk, 5 to the head); in "
            "self-defense it is the answer to the grab from behind, "
            "thrown without ever facing the attacker. The danger is "
            "symmetric: a mistimed back kick turns the back to the "
            "opponent for a third of a second, so it is thrown only when "
            "the distance is right and the opponent is committed. Drilled "
            "first in slow motion with a partner calling the turn, then "
            "at speed on the bag, the back kick becomes the technique "
            "opponents fear most because they never see the chamber."
        ),
        "how_it_works": (
            "From fighting stance, fix your eyes on the target over the "
            "shoulder of the kicking side - the eyes lead and the body "
            "follows. Spin 180 degrees on the ball of the supporting "
            "foot, pulling the kicking knee up tight as you turn, and "
            "drive the leg straight back along your sight line, heel "
            "leading, knee locking at extension. Keep the torso upright "
            "and the guard up through the spin; spot the target again as "
            "the kick extends. Rechamber by folding the knee back in "
            "during the last of the turn and land back in stance facing "
            "the target. Drill it in three stages: stage one, slow "
            "motion, partner holding a paddle at the finish point, ten "
            "per leg; stage two, half speed, eyes finding the paddle "
            "every time; stage three, full speed on the heavy bag. The "
            "faults are the blind spin (eyes never find the target), the "
            "high chamber that telegraphs the turn, and leaning forward "
            "into the kick, which trades all the rotational power for a "
            "weak push."
        ),
        "key_points": [
            "Dwit chagi: eyes find the target over the shoulder, 180-degree spin on the ball of the support foot, leg driven straight back, heel striking.",
            "Spin physics: about 0.3 s for the half turn, near 600 degrees per second - the kick lands before the turn registers.",
            "The rotation is the chamber: body mass turning into the line makes it hit harder than the side kick from a shorter wind-up.",
            "Sport value (WT): turning kick scoring - 4 trunk, 5 head; self-defense value: the answer to the attack from behind.",
            "Risk is symmetric: a mistimed spin shows the back for a third of a second - thrown only at the right distance against a committed opponent.",
        ],
        "requirements": [
            "A reliable side kick first: the back kick finishes in the side kick line, and the extension mechanics are the same.",
            "Spotting discipline: the eyes must find the target over the shoulder before the leg fires, every repetition.",
            "A patient drilling partner for the slow-motion stage; the spin is learned at walking speed, not at speed.",
        ],
        "standards": [
            "Kukkiwon Taekwondo Textbook (2013): dwit chagi - spin, sight line, heel strike.",
            "World Taekwondo Competition Rules and Interpretation: turning-kick scoring values.",
            "Choi Hong Hi, Encyclopedia of Taekwon-Do, Vol. 4 (1999): back piercing kick.",
        ],
        "citations": [
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
            "World Taekwondo. Competition Rules and Interpretation. In force.",
            "Choi Hong Hi. Encyclopedia of Taekwon-Do. 5th ed. International Taekwon-Do Federation; 1999. Vol. 4.",
        ],
        "sig_lens": (
            "The Signature lens treats dwit chagi as the signature "
            "written over the shoulder: the practitioner signs without "
            "looking at the page, trusting the body to know the line. "
            "Where the public record clocks 600 degrees per second, the "
            "Signature method clocks the covenant of the blind turn - "
            "the eyes find the target first, the body follows on faith, "
            "the heel completes the stroke. It is the art most secret "
            "clause: power that does not need to be seen to be "
            "believed."
        ),
    },
]

ENTRIES += [
    {
        "key": "axe_kick",
        "name": "Axe Kick (Naeryeo Chagi)",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Naeryeo chagi, the axe kick - literally downward kick - is "
            "taekwondo falling hammer: the leg raised high and straight, "
            "then driven down onto the target like an axe. The chamber "
            "lifts the straight leg to vertical or beyond, the hips stay "
            "square, and then the leg drops - not swung, dropped - with "
            "the heel as the striking surface, the full weight of the "
            "raised leg plus gravity behind it. A leg raised to 1.8 "
            "meters falls for about 0.61 seconds and arrives at nearly "
            "6 meters per second from gravity alone, before the hips add "
            "their downward drive. The classic targets are the top of "
            "the head, the collarbone, and the shoulder of a taller "
            "opponent - the axe kick is the short practitioner answer to "
            "reach, because the downward path needs no forward distance. "
            "In WT sparring the axe kick to the head is a frequent "
            "fight-ender; in forms it appears as the dramatic high "
            "technique that tests flexibility and control. The kick "
            "demands the most flexibility of any basic kick: without a "
            "near-vertical leg raise, there is nothing to drop. It is "
            "drilled first as a slow leg raise and hold, then as a "
            "controlled drop onto a pad, and only then at full speed - "
            "the hamstring is the limiting contract in this negotiation."
        ),
        "how_it_works": (
            "From fighting stance, raise the kicking leg straight up in "
            "front of the body, knee locked, toes pointed, until the leg "
            "reaches vertical or as close as flexibility allows - the "
            "supporting leg stays straight and the hips stay square to "
            "the target. Pause for a heartbeat at the top: this is the "
            "axe raised. Then drive the leg straight down, heel leading, "
            "dropping the hips into the fall and exhaling sharply; the "
            "motion is a drop with guidance, not a muscular swing. "
            "Strike with the heel through the target line, then let the "
            "leg continue to the floor and recover to stance. Drill the "
            "raise first: ten slow leg raises per leg, holding three "
            "seconds at the top, until the height is consistent; then ten "
            "controlled drops onto a partner-held pad; then full speed. "
            "The faults are the bent raising knee (which shortens the "
            "axe handle), the swing instead of the drop (which trades "
            "gravity power for muscle power), and leaning back, which "
            "pulls the head into the path of the counter."
        ),
        "key_points": [
            "Naeryeo chagi: straight leg raised to vertical, paused, then dropped heel-first - the falling hammer, not the swung hammer.",
            "Drop physics: from 1.8 m the leg falls about 0.61 s and arrives near 6 m/s on gravity alone, before the hips add their drive.",
            "Targets: top of the head, collarbone, shoulder - the short practitioner answer to reach, needing no forward distance.",
            "The most flexibility-demanding basic kick: drilled as slow raise-and-hold first, controlled pad drops second, full speed last.",
            "In WT sparring the head axe kick is a frequent fight-ender; in forms it is the dramatic high technique testing control.",
        ],
        "requirements": [
            "Hamstring and hip-flexor flexibility for a near-vertical raise; daily stretching is the price of admission.",
            "The pause at the top: no raise counts until it can be held three seconds without wavering.",
            "A partner-held pad for the drop stage; the full-speed axe kick is never learned on air alone.",
        ],
        "standards": [
            "Kukkiwon Taekwondo Textbook (2013): naeryeo chagi - raise, drop, heel strike, targets.",
            "World Taekwondo Competition Rules and Interpretation: head-kick scoring and legal target areas.",
        ],
        "citations": [
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
            "World Taekwondo. Competition Rules and Interpretation. In force.",
        ],
        "sig_lens": (
            "The Signature lens sees naeryeo chagi as the stamp coming "
            "down: the leg raised like a seal lifted high, the pause the "
            "moment of aim, the drop the impression pressed into the "
            "target. Where the public record measures 0.61 seconds of "
            "fall, the Signature method measures the covenant of the "
            "pause - the axe is only an axe because it waits at the top. "
            "Gravity is the senior partner in this technique, and the "
            "Signature practitioner signs the contract by letting it "
            "work."
        ),
    },
    {
        "key": "push_kick",
        "name": "Push Kick (Mireo Chagi)",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Mireo chagi, the push kick - literally pushing kick - is "
            "taekwondo distance manager: a front kick thrown not to snap "
            "but to shove, the whole sole of the foot driving into the "
            "opponent midsection or hip and stopping the advance cold. "
            "Where the front snap kick retracts instantly, the push kick "
            "extends through and holds, converting the leg into a "
            "moving wall. The physics is workmanlike: an 80 kilogram "
            "opponent advancing at 2 meters per second carries 160 "
            "joules of motion; halted over 40 centimeters of push, the "
            "required average force is about 400 newtons - well within a "
            "trained leg thrust. In WT sparring the push kick (often "
            "called the cut kick when aimed at the hip) breaks the "
            "opponent rhythm, resets the distance, and sets up the "
            "scoring roundhouse; in self-defense it is the first answer "
            "to the rush, buying the second that the finishing technique "
            "needs. The kick is thrown from the front kick chamber but "
            "with the hips driving forward behind it and the ankle "
            "locked flat, sole presented. It is the least glamorous kick "
            "in the arsenal and one of the most used: control of distance "
            "is control of the fight."
        ),
        "how_it_works": (
            "Chamber exactly as for the front kick - knee high toward "
            "the chest - but as the leg extends, drive the hips forward "
            "behind it and present the full sole of the foot, ankle "
            "locked flat, toes pulled up. Push through the target for a "
            "full beat instead of snapping back: the leg should feel "
            "like a piston extending, not a whip cracking. Aim for the "
            "hip crease or the midsection; against a rushing opponent, "
            "time the push to meet the advance so the opponent momentum "
            "adds to the stop. Recover by folding the knee back to "
            "chamber - never let the extended leg hang, or it will be "
            "caught. Drill with a partner in a chest guard walking "
            "forward: ten pushes per leg, each one halting the walk and "
            "resetting the distance to a full arm-plus-leg length. The "
            "faults are the snap habit (retracting before the push "
            "lands), the unlocked ankle (the foot folds on the guard), "
            "and pushing with the leg alone while the hips stay back - "
            "the push kick without the hips is a foot waved at the "
            "enemy."
        ),
        "key_points": [
            "Mireo chagi: front-kick chamber, full sole presented, hips driving forward, push held through the target - a moving wall, not a whip.",
            "Stopping physics: an 80 kg opponent at 2 m/s halted over 0.4 m needs about 400 N - well within a trained thrust.",
            "Distance management is fight management: the push kick breaks rhythm, resets range, and sets up the scoring kick.",
            "Aimed at the hip crease it becomes the cut kick of WT sparring, killing the opponent kicking leg before it fires.",
            "The snap habit is the enemy: retracting early turns the wall back into a curtain.",
        ],
        "requirements": [
            "A clean front kick chamber first; the push kick is the front kick thrown with different intent.",
            "A partner in a chest guard for realistic push drills; the timing against a live advance cannot be learned on a bag.",
            "Ankle-lock discipline under load: the sole must stay flat through the full push.",
        ],
        "standards": [
            "Kukkiwon Taekwondo Textbook (2013): mireo chagi - pushing application of the front kick.",
            "World Taekwondo Competition Rules and Interpretation: legal pushing and cut-kick tactics in sparring.",
        ],
        "citations": [
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
            "World Taekwondo. Competition Rules and Interpretation. In force.",
        ],
        "sig_lens": (
            "The Signature lens reads mireo chagi as the margin of the "
            "combat document: the kick that draws the line the opponent "
            "may not cross. Where the public record counts 400 newtons, "
            "the Signature method counts the covenant of distance - the "
            "practitioner does not chase the fight but defines its "
            "borders, and the push kick is the fence. Held through the "
            "target for a full beat, it signs the boundary in a hand "
            "the opponent cannot misread."
        ),
    },
    {
        "key": "crescent_kicks",
        "name": "Crescent Kicks (An Chagi and Bakkat Chagi)",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The crescent kicks are taekwondo sweeping arcs: the leg "
            "swung in a great curve, striking with the inner edge of "
            "the foot (an chagi, inward crescent) or the outer edge "
            "(bakkat chagi, outward crescent). The inward crescent "
            "chambers the leg out to the side and sweeps it across the "
            "body, the inner foot edge cutting like a scythe; the "
            "outward crescent chambers across the body and sweeps it "
            "away, the outer edge striking. Both travel a long path - a "
            "1 meter leg swung through 120 degrees traces an arc over "
            "2 meters - which makes them slower than the snap kicks but "
            "gives them unique jobs: the inward crescent slaps away a "
            "grabbing hand or strikes the side of the head around a "
            "guard, and the outward crescent clears the opponent arms "
            "or strikes the ribs from outside the guard. In forms, the "
            "crescent kicks are the flowing techniques that teach hip "
            "mobility and balance on one leg through a long motion; in "
            "breaking, the inward crescent is a classic for its wide, "
            "forgiving striking edge. They are also the gateway kicks: "
            "the hip action of the crescent grows directly into the "
            "hook kick and the spinning kicks of the advanced ladder."
        ),
        "how_it_works": (
            "For the inward crescent (an chagi), lift the straight leg "
            "out to the kicking side, then sweep it across the body in "
            "a horizontal arc, striking with the inner edge of the foot "
            "at the crossing point, toes pointed. For the outward "
            "crescent (bakkat chagi), lift the straight leg across the "
            "body first, then sweep it outward, striking with the outer "
            "edge. In both, the leg stays relatively straight - the "
            "power comes from the hip swing, not a knee snap - the "
            "supporting foot pivots to let the hips turn, and the torso "
            "stays upright against the centrifugal pull. Drill ten slow "
            "arcs per leg per direction, tracing the full 120-degree "
            "path and holding balance at the finish; then ten at speed "
            "against a paddle held at head height to the side. The "
            "faults are the bent sweeping knee (which shortens the "
            "scythe), the leaning torso (which the arc will pull over), "
            "and rushing the path - the crescent kick hurried becomes a "
            "roundhouse with no pivot, which is the worst of both "
            "techniques."
        ),
        "key_points": [
            "An chagi (inward): leg out to the side, swept across, inner foot edge striking - the scythe that cuts around a guard.",
            "Bakkat chagi (outward): leg across the body, swept away, outer foot edge striking - the clearer of arms and the rib striker.",
            "Arc physics: a 1 m leg through 120 degrees traces over 2 m - slower than snap kicks, but with unique angles around defenses.",
            "Gateway kicks: the crescent hip action grows directly into the hook kick and the spinning kicks of the advanced ladder.",
            "Power from the hip swing with a straight leg, not a knee snap; the torso must stand upright against the centrifugal pull.",
        ],
        "requirements": [
            "Hip mobility for the full 120-degree arc; the crescent only exists where the hips allow it.",
            "Single-leg balance through a long motion: the slow-arc drill must be clean before any speed is added.",
            "A side-held paddle target; the crescent strikes beside the body, not in front of it.",
        ],
        "standards": [
            "Kukkiwon Taekwondo Textbook (2013): an chagi and bakkat chagi - arcs, striking edges, applications.",
            "Choi Hong Hi, Encyclopedia of Taekwon-Do, Vol. 4 (1999): crescent kick mechanics.",
        ],
        "citations": [
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
            "Choi Hong Hi. Encyclopedia of Taekwon-Do. 5th ed. International Taekwon-Do Federation; 1999. Vol. 4.",
        ],
        "sig_lens": (
            "The Signature lens sees the crescent kicks as the curved "
            "flourishes of the combat script: where the snap kicks are "
            "straight strokes, the crescents are the sweeping "
            "underlines and the elegant crossings-out. Where the public "
            "record measures a 2 meter arc, the Signature method "
            "measures the covenant of the curve - the leg must travel "
            "the whole arc honestly, no shortcuts, because a flourish "
            "cut short is a lie. These are the kicks that teach the "
            "hand of the signer to move in circles as well as lines."
        ),
    },
]

ENTRIES += [
    {
        "key": "hook_kick",
        "name": "Hook Kick (Huryeo Chagi)",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Huryeo chagi, the hook kick, is the crescent kick grown "
            "fangs: the leg swings out in the wide arc of the outward "
            "crescent, then at the far end of the arc the knee snaps and "
            "the heel hooks back across the target like a question mark "
            "laid on its side. The path is a curve with a bite - the "
            "heel travels the 120-degree arc and then whips inward, "
            "striking the side of the head or neck with the heel or the "
            "back of the foot. Thrown in about 0.28 seconds, the hook "
            "arrives from outside the opponent peripheral vision: the "
            "guard is built for straight attacks, and the hooking path "
            "comes around its edge. In WT sparring the head hook kick is "
            "a classic counter - the opponent steps in with a roundhouse "
            "and meets the hook coming the other way. The kick demands "
            "the hip mobility of the crescent plus the knee snap of the "
            "roundhouse, which is why it sits at rank 6: it is literally "
            "compounded from the two kicks before it. Drilled first as "
            "a slow arc-and-hook on a paddle, then at speed, the hook "
            "kick teaches the advanced lesson that a kick path can "
            "change direction mid-flight."
        ),
        "how_it_works": (
            "Lift the leg in the outward crescent path - across and out "
            "- with the knee slightly bent and the hips opening. As the "
            "leg reaches full extension at the side, snap the knee and "
            "whip the heel back across the target line, turning the arc "
            "into a hook; the supporting foot pivots to let the hips "
            "follow through. Strike with the heel or the back edge of "
            "the foot, then let the leg continue its curve down and "
            "recover to stance. The timing is the technique: the hook "
            "must fire at the exact end of the arc, not during it - hook "
            "early and the kick collapses into a weak slap; hook late "
            "and the moment is gone. Drill: partner holds a paddle at "
            "head height to your side; ten slow reps tracing arc then "
            "hook as two distinct beats; then ten blending the beats "
            "into one motion; then ten at full speed. The faults are the "
            "missing pivot (the hips cannot follow the hook), the "
            "straight-leg hook (no knee snap, no bite), and telegraphing "
            "the arc with the shoulders before the leg moves."
        ),
        "key_points": [
            "Huryeo chagi: outward crescent arc, then the knee snaps and the heel hooks back across the target - a curve with a bite.",
            "The hook fires at the exact end of the arc: early is a collapsed slap, late is a missed moment - timing is the technique.",
            "Strikes the side of the head or neck with the heel, arriving from outside the opponent peripheral vision, around the edge of the guard.",
            "Compounded by construction: crescent hip mobility plus roundhouse knee snap - the rank 6 kick built from rank 3 and rank 4 parts.",
            "The classic WT counter: the opponent steps in with a roundhouse and meets the hook traveling the other way.",
        ],
        "requirements": [
            "Clean crescent kick arcs and a snappy roundhouse first; the hook kick has no foundation of its own.",
            "A side-held head-height paddle and a patient holder for the two-beat drilling stage.",
            "Pivot discipline under rotation: the support foot must turn or the hooking knee takes the twist.",
        ],
        "standards": [
            "Kukkiwon Taekwondo Textbook (2013): huryeo chagi - arc, hook, heel strike.",
            "World Taekwondo Competition Rules and Interpretation: head-kick scoring.",
        ],
        "citations": [
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
            "World Taekwondo. Competition Rules and Interpretation. In force.",
        ],
        "sig_lens": (
            "The Signature lens reads huryeo chagi as the question mark "
            "of the combat script: the arc poses the question and the "
            "hook answers it. Where the public record times 0.28 "
            "seconds, the Signature method times the covenant of the "
            "two beats - arc honestly traveled, hook decisively fired, "
            "neither bleeding into the other. It is the first kick that "
            "changes its mind mid-flight, and the Signature practitioner "
            "learns from it that a signature may curve and still be "
            "true."
        ),
    },
    {
        "key": "footwork",
        "name": "Footwork: Stepping, Sliding, and Pivoting",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Footwork is the delivery system of taekwondo: every kick "
            "in this database is thrown from a stance, and footwork is "
            "how the stance gets to the target. The three core steps "
            "are the forward step (the front foot advances, the back "
            "foot follows, stance preserved), the slide (both feet glide "
            "together, the classic blitz step of WT sparring), and the "
            "pivot (the front foot anchors while the back foot swings "
            "around to change the angle). Advanced footwork adds the "
            "switch step (feet swap lead in a tiny hop, changing the "
            "kicking leg in a blink) and the lateral shuffle (sideways "
            "glide that opens the angle for the roundhouse). The numbers "
            "tell the story: a trained fighter slides at about 2 steps "
            "per second, covers 3 meters in 4 to 5 steps, and can change "
            "angle 45 degrees with a single pivot - distance and angle "
            "are created by the feet before the kick is ever thrown. "
            "Footwork is drilled as its own discipline: ladder drills, "
            "mirror drills with a partner, and the endless forward-back "
            "slide that builds the calf endurance sparring demands. The "
            "rule of the feet is absolute: never cross the feet, never "
            "hop without purpose, and never let the feet stop moving - a "
            "stationary fighter is a target, and taekwondo is an art of "
            "motion."
        ),
        "how_it_works": (
            "Practice each step in isolation first. Forward step: from "
            "fighting stance, slide the front foot forward six inches, "
            "then bring the back foot up to restore the stance - the "
            "stance width must be identical before and after. Slide "
            "(blitz): push off the back foot and glide both feet "
            "forward together, landing in stance ready to kick - the "
            "signature entry of the WT attack. Pivot: plant the front "
            "foot and swing the back foot around it, turning the body 45 "
            "to 90 degrees to open a new angle while the guard stays "
            "facing the opponent. Switch step: a tiny hop swapping the "
            "feet, the back leg becoming the lead in under two tenths "
            "of a second. Drill the matrix: ten forward steps, ten "
            "back, ten slides, ten pivots each direction, ten switches - "
            "then combine: slide-pivot-kick, switch-roundhouse. The "
            "faults are crossing the feet (which tangles the legs under "
            "pressure), the high hop (which leaves the fighter airborne "
            "and helpless), and stance decay - every step must end in a "
            "stance that could kick, or the step was wasted motion."
        ),
        "key_points": [
            "Three core steps: forward step (stance preserved), slide/blitz (both feet glide, the WT attack entry), pivot (angle change around a planted foot).",
            "Advanced additions: the switch step (lead swap in under 0.2 s) and the lateral shuffle (angle opener for the roundhouse).",
            "Delivery numbers: about 2 steps per second, 3 meters in 4-5 steps, 45 degrees of angle per pivot - distance and angle before the kick.",
            "Absolute rules: never cross the feet, never hop without purpose, never let the feet stop moving.",
            "Drilled as its own discipline: ladders, mirrors, endless slides - every step must end in a stance that could kick.",
        ],
        "requirements": [
            "A long clear lane (at least 6 meters) for step-and-slide drilling without obstacles.",
            "Calf and ankle conditioning: footwork volume is high, and the calves carry it all.",
            "A mirror or partner for the stance-decay check: the stance after the step must match the stance before it.",
        ],
        "standards": [
            "Kukkiwon Taekwondo Textbook (2013): footwork (bal gireum) - stepping, sliding, and turning methods.",
            "World Taekwondo Competition Rules and Interpretation: legal movement and engagement in sparring.",
        ],
        "citations": [
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
            "World Taekwondo. Competition Rules and Interpretation. In force.",
        ],
        "sig_lens": (
            "The Signature lens treats footwork as the penmanship of "
            "combat: the kicks are the words, but the feet write the "
            "sentences, choosing where each word lands. Where the public "
            "record counts 2 steps per second, the Signature method "
            "counts the covenant of the stance - every step ends where "
            "a kick could begin, because a signature is only as good as "
            "the paper it is written on. The pivot is the art flourish "
            "of angles: 45 degrees of new perspective, signed in a "
            "single motion."
        ),
    },
    {
        "key": "kick_combinations",
        "name": "Kick Combinations",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "A single kick is a word; a combination is a sentence. Kick "
            "combinations chain two or more kicks without setting the "
            "foot down - or with a single switch step between them - so "
            "the opponent must solve multiple attacks in the time of "
            "one. The mathematics of combinations is combinatorial: "
            "from 5 base kicks come 25 ordered two-kick combinations and "
            "125 ordered three-kick combinations, and the fighter art is "
            "choosing the few that flow. The classic pairs are the "
            "roundhouse-roundhouse (same leg twice, the second chambered "
            "off the first rechamber), the front kick-roundhouse (the "
            "push sets the distance, the roundhouse scores), and the "
            "switch roundhouse (the switch step disguises which leg "
            "kicks). The governing principle is the rechamber: every "
            "kick must fold back to chamber, because the chamber is the "
            "launch pad of the next kick - a kick that drops to the "
            "floor ends the combination. Combinations are drilled on a "
            "count: one-and-two for doubles, one-and-two-and-three for "
            "triples, at half speed until the chain is seamless, then at "
            "speed on the paddle. In sparring, the combination is what "
            "defeats the single-block defense: the first kick takes the "
            "guard, the second takes the target."
        ),
        "how_it_works": (
            "Build combinations from the rechamber outward. Start with "
            "the double roundhouse, same leg: throw the roundhouse, fold "
            "the knee straight back to chamber without touching down, "
            "and fire the second roundhouse off the rechamber - the two "
            "kicks should land inside one second. Next the front "
            "kick-roundhouse: push kick to set distance, rechamber, pivot "
            "into the roundhouse as the foot lands. Then the switch "
            "roundhouse: switch step and roundhouse with the new lead "
            "leg in one motion. Drill each pair ten times per side at "
            "half speed on the count, then ten at full speed on the "
            "paddle, then chain a triple: roundhouse-roundhouse-hook. "
            "The faults are the dropped foot between kicks (which ends "
            "the combination and telegraphs the next), the decaying "
            "chamber (each kick weaker than the last), and the "
            "combination thrown at one range - the feet must adjust "
            "between kicks or the second kick lands in empty air. A "
            "combination is only finished when the fighter is back in "
            "stance, guarded, and balanced."
        ),
        "key_points": [
            "The rechamber is the combination: every kick folds back to chamber, because the chamber launches the next kick - a dropped foot ends the sentence.",
            "Combination math: 5 base kicks yield 25 ordered pairs and 125 ordered triples; the art is choosing the few that flow.",
            "Classic pairs: roundhouse-roundhouse (same leg, off the rechamber), front kick-roundhouse (distance then score), switch roundhouse (disguised lead).",
            "Drilled on the count - one-and-two, one-and-two-and-three - at half speed until seamless, then at speed on the paddle.",
            "Tactical purpose: the first kick takes the guard, the second takes the target; single-block defenses cannot solve two kicks in one beat.",
        ],
        "requirements": [
            "Reliable single kicks first: a combination of weak kicks is just weak twice.",
            "Rechamber discipline drilled to exhaustion: the fold-back must survive fatigue or the combination dies late in the round.",
            "A paddle holder who calls the combination; called combinations train the reactive chaining sparring needs.",
        ],
        "standards": [
            "Kukkiwon Taekwondo Textbook (2013): continuous kicking (yeonsok chagi) principles.",
            "World Taekwondo Competition Rules and Interpretation: valid scoring for consecutive kicks.",
        ],
        "citations": [
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
            "World Taekwondo. Competition Rules and Interpretation. In force.",
        ],
        "sig_lens": (
            "The Signature lens reads combinations as compound "
            "sentences: the rechamber is the conjunction, each kick a "
            "clause, the whole chain one signed statement. Where the "
            "public record counts 25 pairs and 125 triples, the "
            "Signature method counts the covenant of the fold - every "
            "kick returns to chamber, because the signer never leaves a "
            "stroke unfinished. The double roundhouse is the emphasized "
            "word, written twice for certainty; the triple is the full "
            "paragraph of intent."
        ),
    },
]

ENTRIES += [
    {
        "key": "taegeuk_poomsae",
        "name": "Taegeuk Poomsae: The Eight Color-Belt Forms",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The eight taegeuk poomsae are the color-belt curriculum of "
            "World Taekwondo: eight choreographed forms, one per gup "
            "grade from 8th to 1st, each a fight against imaginary "
            "opponents that compounds every basic into flowing "
            "application. Taegeuk 1 Jang (18 movements) teaches the "
            "walking stance with middle punch and the three basic "
            "blocks; 2 Jang (18) adds the front kick; 3 Jang (20) adds "
            "the knife-hand and the back stance; 4 Jang (20) adds the "
            "side kick; 5 Jang (20) adds the hook and the elbow; 6 Jang "
            "(20) adds the roundhouse combinations; 7 Jang (24) adds "
            "the double blocks and the crane stance; 8 Jang (24) "
            "reviews everything at black-belt candidacy - 164 movements "
            "in total, averaging just over 20 per form. Each taegeuk "
            "takes its name and its floor pattern from one of the eight "
            "trigrams of the I Ching: geon (heaven), tae (lake), ri "
            "(fire), jin (thunder), seon (wind), gam (water), gon "
            "(mountain), gon (earth). Every form opens and closes in "
            "junbi, contains two ki hap points, and is performed on a "
            "floor diagram the student must memorize as exactly as the "
            "techniques. The poomsae are also a sport: WT poomsae "
            "competition judges accuracy, power, rhythm, and expression, "
            "and the taegeuk forms are its foundation."
        ),
        "how_it_works": (
            "Learn each taegeuk in four passes. Pass one: walk the floor "
            "diagram with no techniques, memorizing the turns until the "
            "pattern is a map in the feet. Pass two: add the techniques "
            "at half speed, checking each stance against the mirror - "
            "the form is only as good as its weakest stance. Pass three: "
            "full speed with breath, exhaling on every technique and "
            "firing the two ki hap at their marked points. Pass four: "
            "application - for each movement, name the attack it answers "
            "and the target it strikes, so the form never becomes empty "
            "dance. A form takes about 60 to 90 seconds to perform; drill "
            "it in sets of three with a one-minute rest, and practice "
            "the new form daily for the month before grading. The faults "
            "are the memorized-but-meaningless form (techniques with no "
            "targets), the rushing (the form performed as fast as "
            "possible instead of with rhythm), and the wandering diagram "
            "- the finished form must end exactly where it began, on "
            "the same floor mark."
        ),
        "key_points": [
            "Eight forms, eight gup grades: 1 Jang (18 moves) through 8 Jang (24 moves) - 164 movements total, each form compounding the basics before it.",
            "Curriculum ladder: walking stance and blocks, then front kick, knife-hand, side kick, hook and elbow, roundhouse combos, advanced blocks, full review.",
            "Each taegeuk is named for an I Ching trigram (heaven, lake, fire, thunder, wind, water, mountain, earth) with its floor pattern.",
            "Every form: opens and closes in junbi, two ki hap points, 60-90 seconds, ends exactly where it began.",
            "Four-pass learning: diagram, techniques at half speed, full speed with breath, then application - every movement answers an attack.",
        ],
        "requirements": [
            "All rank 1-6 basics clean: the poomsae compound the basics, and weak basics make weak forms.",
            "A marked floor diagram or tape lines until the pattern lives in the feet.",
            "Daily practice of the current form for the month before grading; forms decay without repetition.",
        ],
        "standards": [
            "Kukkiwon Taekwondo Textbook (2013): the eight taegeuk poomsae - movements, diagrams, and meanings.",
            "World Taekwondo Poomsae Competition Rules: judging criteria - accuracy, power, rhythm, expression.",
        ],
        "citations": [
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
            "World Taekwondo. Poomsae Competition Rules. In force.",
        ],
        "sig_lens": (
            "The Signature lens reads the eight taegeuk as the eight "
            "chapters of the combat autobiography: each form a longer "
            "sentence, each trigram a theme, the 164 movements a "
            "complete first draft of the fighter. Where the public "
            "record counts movements, the Signature method counts the "
            "covenant of the diagram - the form must end where it "
            "began, because a signature that wanders off the page is "
            "void. The two ki hap are the chapter seals, pressed at the "
            "marked points without fail."
        ),
    },
    {
        "key": "chonji_tul",
        "name": "Chon-Ji Tul: The First ITF Pattern",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Chon-Ji is the first tul (pattern) of the ITF system, the "
            "gateway to General Choi 24 patterns and the foundation "
            "every ITF student learns at 9th gup. Its 19 movements are "
            "built from only three techniques - the walking stance "
            "middle punch, the walking stance low block, and the "
            "walking stance middle block - arranged on a cross-shaped "
            "floor diagram. The name means heaven and earth: in the "
            "Orient it is interpreted as the creation of the world, the "
            "beginning of human history, and so the first pattern "
            "represents the beginner first steps in taekwon-do. The "
            "diagram is a cross with four arms, and the student performs "
            "the same sequence facing each of the four directions, "
            "learning the essential skill of the patterns: identical "
            "technique regardless of direction. Though simple, Chon-Ji "
            "is drilled for precision - every stance exactly one and a "
            "half shoulder widths, every punch to the solar plexus, every "
            "block finishing one fist-width from the body - because the "
            "habits formed in the first pattern persist through all "
            "twenty-four. It takes about 40 seconds to perform and "
            "contains no ki hap, the beginner learning control before "
            "expression."
        ),
        "how_it_works": (
            "Begin in parallel ready stance facing the first direction. "
            "Step left into walking stance with a low block, step right "
            "into walking stance with a middle punch - this two-beat "
            "unit repeats, turning 90 degrees at each arm of the cross, "
            "until all four directions are covered and the 19 movements "
            "are complete. Every walking stance is measured: step one "
            "and a half shoulder widths, front knee over the ankle, back "
            "heel down. Every punch travels the centerline to the solar "
            "plexus height; every low block finishes one fist-width in "
            "front of the thigh. Drill the cross diagram first without "
            "techniques - walk the four arms until the turns are "
            "automatic - then add the techniques at half speed for ten "
            "repetitions, then at full speed with breath on every "
            "movement. The faults are the drifting stance length (each "
            "step a different size), the forgotten turn (facing the "
            "wrong arm of the cross), and the rushing - Chon-Ji is a "
            "study in identical repetition, and the 19th movement must "
            "look exactly like the 1st."
        ),
        "key_points": [
            "Chon-Ji: 19 movements, three techniques (walking-stance punch, low block, middle block) on a cross-shaped diagram - the first of the 24 ITF tul.",
            "The name means heaven and earth: the creation of the world, the beginning of history - the beginner first steps.",
            "Four-directional performance teaches the core pattern skill: identical technique regardless of facing.",
            "Precision over flash: stance lengths, punch heights, and block finishes measured exactly - habits formed here persist through all 24 patterns.",
            "About 40 seconds, no ki hap: control before expression is the beginner curriculum.",
        ],
        "requirements": [
            "Clean walking stance, middle punch, and low block: Chon-Ji compounds exactly these three and nothing else.",
            "The cross diagram walked until automatic before any technique is added.",
            "An instructor check of the first grading performance; the pattern must be exact, not approximate.",
        ],
        "standards": [
            "Choi Hong Hi, Encyclopedia of Taekwon-Do, Vol. 8 (1999): Chon-Ji - 19 movements, diagram, and meaning.",
            "ITF tul system: the 24 patterns as the official ITF curriculum.",
        ],
        "citations": [
            "Choi Hong Hi. Encyclopedia of Taekwon-Do. 5th ed. International Taekwon-Do Federation; 1999. Vol. 8.",
        ],
        "sig_lens": (
            "The Signature lens reads Chon-Ji as the title page of the "
            "ITF combat manuscript: heaven and earth, the first words "
            "written, nineteen strokes of the pen. Where the public "
            "record counts 19 movements, the Signature method counts "
            "the covenant of identity - the 19th movement must look "
            "exactly like the 1st, because a signature that changes "
            "across the page cannot be trusted. The cross diagram is "
            "the seal of the four directions: the same truth, faced "
            "four ways."
        ),
    },
    {
        "key": "sparring_fundamentals",
        "name": "Sparring Fundamentals (Gyeorugi)",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Gyeorugi, sparring, is where taekwondo techniques meet a "
            "live opponent - the laboratory that tests everything the "
            "basics and forms promised. Beginners start with one-step "
            "sparring (han bon gyeorugi): the partner attacks with a "
            "single agreed technique and the student answers with a "
            "single agreed defense and counter, both sides learning "
            "distance and timing without chaos. From there the ladder "
            "climbs: three-step sparring, semi-free sparring (agreed "
            "attacks, free defense), and finally free sparring under "
            "rules. In WT free sparring, seniors fight 3 rounds of 2 "
            "minutes with 1 minute of rest - 8 minutes of combat - "
            "wearing headgear, chest guard, forearm and shin guards, "
            "and scoring with the roundhouse, the push kick, and the "
            "occasional head shot. ITF sparring runs 2 rounds of 2 "
            "minutes, semi-contact, with hand techniques scoring equally "
            "alongside kicks. The fundamentals are the same in both: "
            "guard up always, bounce lightly on the balls of the feet, "
            "control the distance with footwork, attack in combinations "
            "never singles, and above all stay calm - the fighter who "
            "panics has already lost the round. Sparring is drilled in "
            "short rounds with long coaching breaks: the beginner spars "
            "one minute, rests two, and talks through every exchange."
        ),
        "how_it_works": (
            "Begin with one-step sparring: partners face off at one long "
            "step of distance; the attacker announces a middle punch and "
            "steps in with it; the defender answers with the agreed "
            "block and counter, then both reset. Ten attacks per side, "
            "then swap roles. When one-step is clean, move to semi-free: "
            "the attacker may use any agreed hand or foot technique, the "
            "defender answers freely - ten exchanges per side. Free "
            "sparring begins with one-minute rounds, full protective "
            "gear, a senior student or instructor refereeing, and one "
            "rule above all: control. Drill the fundamentals between "
            "rounds: 30 seconds of slide-and-guard, 30 seconds of "
            "combination on the paddle, then back in. The faults are "
            "the dropped guard under pressure (the first thing to go), "
            "the frozen feet (the fighter plants and becomes a target), "
            "the single-attack habit (one kick, then waiting), and the "
            "panic rush - charging in swinging. Every round ends with "
            "the bow: the laboratory closes with the same respect it "
            "opened with."
        ),
        "key_points": [
            "The sparring ladder: one-step (agreed attack, agreed answer), three-step, semi-free, then free sparring under rules - chaos is earned gradually.",
            "WT seniors: 3 rounds of 2 minutes, 1 minute rest, full gear; ITF: 2 rounds of 2 minutes, semi-contact, hands scoring with kicks.",
            "Fundamentals under pressure: guard up always, bounce on the balls of the feet, distance by footwork, attacks in combinations, calm above all.",
            "Beginner round structure: spar one minute, rest two, talk through every exchange - coaching time exceeds fighting time.",
            "Pressure faults: dropped guard, frozen feet, single-attack habit, panic rush - each is drilled out before the next ladder rung.",
        ],
        "requirements": [
            "Full protective gear from the first free round: headgear, chest guard, forearm and shin guards, groin guard, mouthguard.",
            "A qualified referee (instructor or senior) for every free round; unsupervised beginner sparring is forbidden.",
            "The control covenant: full speed is allowed, full power to the head is not - control is graded alongside technique.",
        ],
        "standards": [
            "World Taekwondo Competition Rules and Interpretation: match structure, legal techniques, and protective equipment.",
            "Kukkiwon Taekwondo Textbook (2013): gyeorugi progression - one-step through free sparring.",
            "ITF Tournament Rules: semi-contact sparring format and scoring.",
        ],
        "citations": [
            "World Taekwondo. Competition Rules and Interpretation. In force.",
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
        ],
        "sig_lens": (
            "The Signature lens treats sparring as the peer review of "
            "the combat manuscript: every technique submitted to a live "
            "reader, every claim tested. Where the public record counts "
            "3 rounds of 2 minutes, the Signature method counts the "
            "covenant of control - full speed permitted, full power to "
            "the head forbidden, because the laboratory exists to prove "
            "the techniques, not to destroy the colleagues. The bow that "
            "closes the round is the signature on the experiment: "
            "tested, witnessed, respect intact."
        ),
    },
]

ENTRIES += [
    {
        "key": "tornado_kick",
        "name": "Tornado Kick (Dolgae Chagi)",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Dolgae chagi, the tornado kick - also called the 360 "
            "roundhouse - is taekwondo most spectacular technique: a "
            "full 360-degree spinning jump that ends in a roundhouse "
            "kick, the body rotating like a cyclone and the leg striking "
            "at the top of the arc. The sequence runs: step, spin 180 "
            "degrees on the ground gathering the rotation, jump driving "
            "the second 180 degrees in the air, and extend the kicking "
            "leg into a roundhouse at the peak - all inside about half "
            "a second of airtime. The angular velocity approaches 720 "
            "degrees per second, and the foot at the end of the 1.05 "
            "meter leg traces a full circle over 6.5 meters in that half "
            "second. The tornado kick is rarely a first attack - it is "
            "too slow to start - but as a counter or a finishing "
            "technique it is devastating: the full body rotation adds "
            "its mass to the roundhouse, and the jump adds height that "
            "reaches the head of any opponent. It is also the crown of "
            "demonstration taekwondo, the kick that ends highlight "
            "reels. The prerequisites are strict: a fast roundhouse, a "
            "clean 360 spin on the ground, and a confident jump - the "
            "tornado compounds all three, and weakness in any one "
            "collapses the whole technique."
        ),
        "how_it_works": (
            "Learn it in three stages. Stage one, the ground 360: from "
            "fighting stance, step across and spin a full 360 degrees on "
            "the balls of the feet, landing back in stance facing the "
            "target - ten clean spins each direction before anything "
            "else. Stage two, the jump spin: add a small jump at the "
            "180-degree mark so the second half of the rotation happens "
            "airborne, landing soft with knees bent. Stage three, the "
            "kick: at the peak of the jump spin, extend the leg into a "
            "roundhouse, striking with the instep, then land on the "
            "kicking leg side and recover to stance. Drill on mats only: "
            "five jump spins, then five with the kick at half height, "
            "then five at full height on a paddle. The faults are the "
            "late kick (the leg extends after landing, which is just a "
            "roundhouse with extra steps), the lost spotting (the "
            "kicker never finds the target and kicks empty air), and "
            "the stiff landing - the knees must absorb the rotation or "
            "the ankles pay for it."
        ),
        "key_points": [
            "Dolgae chagi: 360-degree spinning jump ending in a roundhouse - step, ground 180, airborne 180, kick at the peak, all in about 0.5 s.",
            "Rotation physics: near 720 degrees per second; the foot traces a 6.5 m circle in half a second of airtime.",
            "A counter and finisher, never an opener: full body rotation adds mass to the roundhouse, the jump adds head height.",
            "Strict prerequisites: fast roundhouse, clean ground 360, confident jump - weakness in any one collapses the technique.",
            "Mats only, staged learning: ground spins, then jump spins, then the kick at half height, then full - stiff landings injure ankles.",
        ],
        "requirements": [
            "A fast, pivoted roundhouse and a clean 360 ground spin: the tornado has no technique of its own, only compounded parts.",
            "Mats or a sprung floor for all jump-spin practice; concrete and tornado kicks do not mix.",
            "Spotting discipline through the spin: the eyes must find the target before the leg extends.",
        ],
        "standards": [
            "Kukkiwon Taekwondo Textbook (2013): dolgae chagi - spinning jump roundhouse mechanics.",
            "World Taekwondo Competition Rules and Interpretation: turning-kick scoring values.",
        ],
        "citations": [
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
            "World Taekwondo. Competition Rules and Interpretation. In force.",
        ],
        "sig_lens": (
            "The Signature lens names dolgae chagi the cyclone "
            "signature: the body writing its name in a full circle, 6.5 "
            "meters of ink in half a second. Where the public record "
            "counts 720 degrees per second, the Signature method counts "
            "the covenant of the three stages - ground spin honest, "
            "jump spin soft, kick at the peak, each prerequisite kept "
            "like a promise. It is the most-read page of the combat "
            "manuscript, and the Signature practitioner signs it only "
            "when every prerequisite has been kept."
        ),
    },
    {
        "key": "spinning_hook_kick",
        "name": "Spinning Hook Kick (Dwi Huryeo Chagi)",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Dwi huryeo chagi, the spinning hook kick - also called the "
            "360 hook kick - takes the hook kick deadly angle and adds "
            "a full rotation behind it. The practitioner spins 360 "
            "degrees and, at the completion of the turn, the leg that "
            "has traveled the whole circle whips into the hook: arc "
            "then bite, now with the entire body rotation feeding the "
            "hook. The technique takes about six tenths of a second "
            "from first step to heel contact, and the heel arrives at "
            "the side of the head from completely outside the "
            "opponent field of vision - the spin hides the chamber, "
            "the hook hides the angle. In elite WT sparring the "
            "spinning hook kick to the head is the highest-percentage "
            "knockout technique in the sport: 5 points and frequently "
            "the end of the match. It is also the most technically "
            "demanding kick in common use, compounding the spin of the "
            "tornado kick with the timing of the hook kick - the arc "
            "must be honestly traveled and the hook must fire at the "
            "exact end of the rotation. Drilled first as a slow spin "
            "with a late hook on the paddle, then blended, then at "
            "speed, it is the technique that separates the advanced "
            "student from the intermediate."
        ),
        "how_it_works": (
            "From fighting stance, step and begin the 360 spin exactly "
            "as for the tornado kick, spotting the target over the "
            "shoulder as the turn completes. In the final quarter of "
            "the rotation, let the kicking leg trail into the outward "
            "crescent path; as the body squares to the target, snap the "
            "knee and whip the heel back across in the hook. The spin "
            "and the hook are two beats that blend into one motion - "
            "drill them as two beats first: ten slow spins finishing "
            "with a distinct hook on the paddle, then ten blending the "
            "beats, then ten at full speed. Keep the guard up through "
            "the entire rotation; the spinning fighter is blind for a "
            "fraction of a second and the hands are the only defense. "
            "Land in stance, balanced, ready to continue. The faults "
            "are the early hook (fired mid-spin, it has no arc behind "
            "it), the lost target (the spin never spots, the hook hits "
            "air), and the celebration - the kicker admires the spin "
            "instead of recovering guard, and the counter arrives "
            "unopposed."
        ),
        "key_points": [
            "Dwi huryeo chagi: full 360 spin, then the hook fires at the exact end of the rotation - the tornado spin compounded with hook-kick timing.",
            "About 0.6 s from step to heel contact; the heel reaches the head from outside the opponent vision - the spin hides the chamber, the hook hides the angle.",
            "Elite WT highest-percentage head knockout: 5 points as a turning head kick, frequently the end of the match.",
            "Two beats blended to one: drill the spin and the hook distinct first, then merge, then speed - the guard stays up through the blind fraction.",
            "The separator technique: it divides the advanced student from the intermediate by demanding both rotation and timing at once.",
        ],
        "requirements": [
            "A clean tornado kick spin and a reliable hook kick: the spinning hook is compounded from exactly these two.",
            "Spotting through the full rotation: the eyes find the target in the final quarter, every repetition.",
            "Immediate guard recovery after landing; the spin is only finished when the fighter is guarded again.",
        ],
        "standards": [
            "Kukkiwon Taekwondo Textbook (2013): dwi huryeo chagi - spin, hook timing, heel strike.",
            "World Taekwondo Competition Rules and Interpretation: turning head-kick scoring (5 points).",
        ],
        "citations": [
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
            "World Taekwondo. Competition Rules and Interpretation. In force.",
        ],
        "sig_lens": (
            "The Signature lens reads dwi huryeo chagi as the sealed "
            "verdict of the combat document: the full rotation the "
            "deliberation, the hook the judgment. Where the public "
            "record counts 5 points, the Signature method counts the "
            "covenant of the two beats - spin honestly completed, hook "
            "fired at the exact end, guard recovered without "
            "celebration. It is the signature written with the whole "
            "body turning, and the Signature practitioner knows it is "
            "the last resort precisely because it cannot be taken back."
        ),
    },
    {
        "key": "jumping_kicks",
        "name": "Jumping Kicks (Twio Chagi)",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Twio chagi, the jumping kicks, add the vertical dimension "
            "to the arsenal: front kick, side kick, and roundhouse all "
            "have jumping versions in which both feet leave the floor "
            "and the kick fires at the peak of the leap. The physics "
            "sets a hard budget: a 40 centimeter vertical jump gives "
            "about 0.57 seconds of hang time (twice the square root of "
            "twice the height over gravity), and the entire kick - "
            "chamber, extension, rechamber - must fit inside it. The "
            "jump front kick is the entry technique, the jump side kick "
            "the breaking classic (flying side kick through boards), "
            "and the jump roundhouse the sparring surprise. Jumping "
            "kicks serve three purposes: they add height to reach high "
            "targets, they add the falling body weight to the impact, "
            "and they defeat the low guard by attacking over it. The "
            "price is commitment: airborne, the fighter cannot change "
            "direction, retreat, or block - the jump kick is a promise "
            "that must be kept. They are drilled on mats with a "
            "progressive height ladder - pad at waist, then chest, then "
            "head - and the landing is drilled as hard as the kick: "
            "both feet, knees bent, guard up, because the technique "
            "ends at landing, not at impact."
        ),
        "how_it_works": (
            "Learn the jump front kick first. From fighting stance, take "
            "a short hop-step and drive upward off the supporting leg "
            "while chambering the kicking knee; at the peak of the jump, "
            "snap the kick out exactly as on the ground, rechamber in "
            "the air, and land on both feet with bent knees and the "
            "guard up. The sequence must fit the hang time: for a 0.4 m "
            "jump, chamber by 0.15 s, kick at 0.28 s (the peak), "
            "rechamber by 0.45 s, land at 0.57 s. Drill the height "
            "ladder: ten jump kicks per leg at waist-height pad, then "
            "chest, then head - never raise the pad until the current "
            "height is clean ten times. The faults are the late kick "
            "(fired on the way down, which is just a falling leg), the "
            "missing rechamber (the leg dangles and the landing "
            "collapses), and the stiff landing - the knees are the "
            "shock absorbers, and locked knees on landing injure ankles "
            "and knees alike."
        ),
        "key_points": [
            "Twio chagi: front, side, and roundhouse kicks fired at the peak of a jump - the vertical dimension of the arsenal.",
            "Hang-time budget: a 0.4 m jump gives about 0.57 s; chamber, extension, and rechamber must all fit inside it.",
            "Three purposes: added height for high targets, falling body weight added to impact, and attacking over the low guard.",
            "The price is total commitment: airborne, the fighter cannot redirect, retreat, or block - the jump is a promise.",
            "Height ladder drilling: waist pad, then chest, then head - and the landing drilled as hard as the kick: both feet, knees bent, guard up.",
        ],
        "requirements": [
            "Clean ground versions of each kick first; the jump adds nothing to a kick that does not work on the floor.",
            "Mats for all jump practice and a measured vertical jump baseline to compute the real hang-time budget.",
            "Landing discipline before height ambition: the technique ends at landing, not at impact.",
        ],
        "standards": [
            "Kukkiwon Taekwondo Textbook (2013): twio chagi - jumping front, side, and turning kicks.",
            "Choi Hong Hi, Encyclopedia of Taekwon-Do, Vol. 5 (1999): jumping kick mechanics.",
        ],
        "citations": [
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
            "Choi Hong Hi. Encyclopedia of Taekwon-Do. 5th ed. International Taekwon-Do Federation; 1999. Vol. 5.",
        ],
        "sig_lens": (
            "The Signature lens sees twio chagi as the signature leaping "
            "off the page: for 0.57 seconds the practitioner writes in "
            "midair, committed, unrecallable. Where the public record "
            "budgets hang time, the Signature method budgets the "
            "covenant of the promise - chamber, kick, rechamber, land, "
            "all inside the airborne signature, because a promise made "
            "in the air must be kept on the ground. The landing is the "
            "period: both feet, knees bent, guard up, the sentence "
            "complete."
        ),
    },
    {
        "key": "double_kicks",
        "name": "Double and Multiple Kicks",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Double kicks - two kicks thrown without setting the foot "
            "down - are the advanced expression of the combination "
            "principle: the same leg fires twice (or three times) off a "
            "single chamber cycle. The classic is the double roundhouse: "
            "first kick to the body, instant rechamber, second kick to "
            "the head, the two impacts landing inside about 0.54 seconds "
            "(0.22 s per kick plus a 0.1 s rechamber). The front "
            "kick-roundhouse double, the side kick-back kick double, and "
            "the triple roundhouse extend the same idea. The tactical "
            "logic is brutal: the first kick occupies the guard or the "
            "attention, and the second arrives while the defense is still "
            "answering the first - no human blocks twice in half a "
            "second without seeing the second kick chambered, and the "
            "rechamber hides exactly that. In WT sparring, doubles are "
            "the highest-percentage scoring sequences after the single "
            "roundhouse; in demonstration, the triple kick is a crowd "
            "standard. The entire technique stands on one ability: the "
            "instant rechamber. Every millisecond the knee stays "
            "extended after the first kick is a millisecond the second "
            "kick is late, and late doubles are just two slow singles."
        ),
        "how_it_works": (
            "Master the double roundhouse first. Throw the roundhouse "
            "to the body target; the instant the foot touches, fold the "
            "knee back to full chamber - violently fast, as if the leg "
            "were spring-loaded - and fire the second roundhouse to the "
            "head target without any pause the eye can catch. The "
            "rhythm is kick-RECHAMBER-kick, with the rechamber as fast "
            "as the kicks. Drill on the paddle: ten doubles per leg at "
            "half speed counting the beats aloud, then ten at full "
            "speed, the holder calling body-head or head-body to train "
            "target switching. Then the front kick-roundhouse double and "
            "the triple. The faults are the lazy rechamber (the second "
            "kick launches from a half-fold and arrives weak), the "
            "telegraphed second kick (the eyes look at the new target "
            "before the first kick lands), and the balance decay - each "
            "kick must leave the fighter in stance, or the double "
            "becomes a stumble with extra steps."
        ),
        "key_points": [
            "Double kicks: two (or three) kicks off one chamber cycle, no foot touching down - the combination principle at full speed.",
            "Double roundhouse timing: about 0.22 s per kick plus 0.1 s rechamber - two impacts inside 0.54 s, faster than a double block.",
            "Tactical logic: the first kick occupies the guard, the second arrives while the defense still answers the first.",
            "The instant rechamber is the whole technique: every millisecond of lazy fold is a millisecond the second kick is late.",
            "Balance is the finish: each kick must leave the fighter in stance, or the double is a stumble with extra steps.",
        ],
        "requirements": [
            "A snappy single roundhouse and a reflexive rechamber: the double is built from exactly these two reflexes.",
            "A paddle holder who calls changing targets; static doubles train the legs but not the targeting.",
            "Single-leg endurance: doubles are thrown late in rounds when the legs are tired, so drill them tired.",
        ],
        "standards": [
            "Kukkiwon Taekwondo Textbook (2013): continuous kicking - doubles and multiples.",
            "World Taekwondo Competition Rules and Interpretation: scoring of consecutive kicks.",
        ],
        "citations": [
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
            "World Taekwondo. Competition Rules and Interpretation. In force.",
        ],
        "sig_lens": (
            "The Signature lens treats the double kick as the repeated "
            "stamp: the same seal pressed twice before the ink dries, "
            "0.54 seconds for two impressions. Where the public record "
            "times the rechamber, the Signature method times the "
            "covenant of the fold - the knee must return fully, because "
            "a half-folded second signature is a forgery of the first. "
            "The double roundhouse is emphasis made physical: the "
            "practitioner says it twice because once was not enough to "
            "be believed."
        ),
    },
]

ENTRIES += [
    {
        "key": "koryo_poomsae",
        "name": "Koryo Poomsae and the Black Belt Forms",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Koryo is the first black belt poomsae and the gate every 1st "
            "dan candidate must pass: 30 movements of advanced technique "
            "named for the Koryo dynasty, from which Korea takes its "
            "name, honoring the spirit of the Korean people resisting "
            "the Mongol invasions. Where the taegeuk forms teach basics, "
            "Koryo tests them under complexity: knife-hand blocks in "
            "back stance, side kicks from crane stance, double knife-hand "
            "blocks, elbow strikes, and the slow-power sections that "
            "demand the practitioner move like water and strike like "
            "iron. Above Koryo stand the eight remaining yudanja (black "
            "belt) poomsae - Keumgang, Taebaek, Pyongwon, Sipjin, Jitae, "
            "Cheonkwon, Hansu, and Ilyeo - one for each dan grade "
            "through 9th, each with its own philosophical theme (Keumgang "
            "the diamond, unbreakable; Taebaek the sacred mountain; "
            "Ilyeo the oneness of body and mind). Together the nine "
            "black belt forms are the graduate curriculum of WT "
            "taekwondo: each takes months to learn and years to master, "
            "each is performed in dan examinations, and each is judged "
            "in elite poomsae competition on accuracy, power, rhythm, "
            "and expression. Koryo takes about 90 seconds to perform and "
            "contains the art first true test of the advanced student: "
            "slow techniques performed with full power and total control."
        ),
        "how_it_works": (
            "Learn Koryo movement by movement from an instructor - the "
            "form is too complex for book learning - in sections of five "
            "movements at a time. Drill each section ten times at half "
            "speed checking every stance in the mirror, then link "
            "sections until the full 30 movements flow. The slow "
            "sections are the examination: perform them at quarter "
            "speed with maximum tension, every muscle engaged, breath "
            "controlled - this is where dan examiners look. Then the "
            "fast sections explode: ki hap at the marked points, full "
            "hip rotation, the side kick from crane stance balanced for "
            "a full beat. A complete practice set is three full "
            "performances with two minutes rest between; dan candidates "
            "practice Koryo daily for six months before examination. "
            "The faults are the rushed slow sections (tension without "
            "control is just shaking), the weak stances under complex "
            "techniques (the form exposes every stance fault the "
            "taegeuk forms forgave), and the missing philosophy - Koryo "
            "without the spirit of resistance it honors is exercise, "
            "not poomsae."
        ),
        "key_points": [
            "Koryo: 30 movements, first black belt poomsae, named for the Koryo dynasty - the gate every 1st dan candidate must pass.",
            "Advanced content: knife-hand blocks in back stance, side kicks from crane stance, double blocks, elbow strikes, slow-power sections.",
            "Above it the eight yudanja forms (Keumgang through Ilyeo), one per dan grade, each with a philosophical theme - the graduate curriculum.",
            "The slow sections are the examination: quarter speed, maximum tension, total control - where dan examiners look.",
            "About 90 seconds; dan candidates drill it daily for six months - rushed slow sections and weak stances are the failing faults.",
        ],
        "requirements": [
            "All eight taegeuk forms mastered: Koryo assumes every basic and punishes every gap.",
            "An instructor for section-by-section transmission; the form is too complex for book learning.",
            "Six months of daily practice before the dan examination; Koryo cannot be crammed.",
        ],
        "standards": [
            "Kukkiwon Taekwondo Textbook (2013): Koryo and the yudanja poomsae - movements, diagrams, meanings.",
            "World Taekwondo Poomsae Competition Rules: black belt division judging criteria.",
        ],
        "citations": [
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
            "World Taekwondo. Poomsae Competition Rules. In force.",
        ],
        "sig_lens": (
            "The Signature lens reads Koryo as the black seal of the "
            "combat manuscript: 30 movements pressed in the ink of the "
            "Koryo dynasty, the graduate thesis of the signer. Where the "
            "public record counts dan grades, the Signature method "
            "counts the covenant of the slow sections - power held at "
            "quarter speed is the ultimate proof that the hand controls "
            "the pen and not the reverse. The eight forms above are the "
            "eight volumes of the master work, each dan a new chapter "
            "signed."
        ),
    },
    {
        "key": "dangun_tul",
        "name": "Dan-Gun Tul and the Higher ITF Patterns",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Dan-Gun is the second ITF tul, the 21-movement pattern "
            "learned at 8th gup, named for the legendary founder of "
            "Korea in 2333 BC - and it introduces the techniques that "
            "make the ITF system unmistakable: the knife-hand block in "
            "L-stance, the twin forearm block, the front kick, and the "
            "first high-section attacks. Above Dan-Gun the 24 patterns "
            "climb through the grades: Do-San (24 movements), Won-Hyo "
            "(28), Yul-Gok (38), Joong-Gun (32), Toi-Gye (37), Hwa-Rang "
            "(29), Choong-Moo (30) at 1st gup, then the black belt "
            "patterns from Kwang-Gae (39) through Tong-Il (56) - each "
            "named for a figure or ideal of Korean history, each longer "
            "and more complex than the last, the full set a 24-volume "
            "encyclopedia of motion. The ITF patterns are distinguished "
            "by the sine wave: the knee spring that drops the body "
            "weight into every technique, down-up-down, generating "
            "power from gravity in the way the WT system generates it "
            "from hip rotation. Dan-Gun takes about 50 seconds and "
            "contains the student first encounter with the L-stance "
            "knife-hand block - the signature stance-technique pairing "
            "of the ITF. The patterns are examined at every grading and "
            "contested in ITF tournaments on precision, power, and "
            "rhythm."
        ),
        "how_it_works": (
            "Learn Dan-Gun after Chon-Ji is exact: the pattern assumes "
            "the walking stance, the punch, and the low block, and adds "
            "the L-stance, the knife-hand block, and the front kick. "
            "Practice the sine wave first in place: from L-stance, bend "
            "the knees to drop the body (down), rise slightly (up), then "
            "drop into the technique (down) - the power comes from the "
            "final drop, timed to the instant of the block or strike. "
            "Walk the Dan-Gun diagram without techniques until the turns "
            "are automatic, then add the 21 movements at half speed, "
            "checking each L-stance angle and each knife-hand finish in "
            "the mirror. Drill sets of three full patterns with "
            "one-minute rests; 8th gup candidates practice daily for the "
            "month before grading. The faults are the flat sine wave "
            "(no knee spring, no gravity power - the ITF technique "
            "without its engine), the L-stance drifted into a walking "
            "stance, and the knife-hand performed with a bent wrist, "
            "which the 21 repetitions will punish by the grading day."
        ),
        "key_points": [
            "Dan-Gun: 21 movements at 8th gup, named for Korea legendary founder - introducing the L-stance knife-hand block, twin forearm block, and front kick.",
            "The 24 tul climb from Chon-Ji (19) to Tong-Il (56), each named for Korean history - a 24-volume encyclopedia of motion.",
            "The sine wave distinguishes ITF power: down-up-down knee spring dropping body weight into every technique.",
            "About 50 seconds per performance; examined at every grading, contested in ITF tournaments on precision, power, rhythm.",
            "Learned only after Chon-Ji is exact: the pattern assumes the basics and adds the stance-technique pairings.",
        ],
        "requirements": [
            "Chon-Ji performed exactly: Dan-Gun compounds its three techniques and adds three more.",
            "The sine wave drilled in place before the pattern: the knee spring is the engine of every ITF technique.",
            "An ITF-qualified instructor: the pattern details (angles, heights, wave timing) are school-specific.",
        ],
        "standards": [
            "Choi Hong Hi, Encyclopedia of Taekwon-Do, Vol. 8 (1999): Dan-Gun - 21 movements, diagram, meaning; the 24-pattern system.",
            "ITF Tournament Rules: pattern competition judging criteria.",
        ],
        "citations": [
            "Choi Hong Hi. Encyclopedia of Taekwon-Do. 5th ed. International Taekwon-Do Federation; 1999. Vol. 8.",
        ],
        "sig_lens": (
            "The Signature lens reads Dan-Gun as the second chapter of "
            "the ITF manuscript, signed in the name of the legendary "
            "founder: 21 movements, each a line of the founding "
            "covenant. Where the public record describes the sine wave, "
            "the Signature method describes the signature of gravity "
            "itself - down-up-down, the pen dipping into the ink of body "
            "weight before every stroke. The 24 patterns are the 24 "
            "scrolls of the archive, and the Signature practitioner "
            "unrolls them in order, never skipping a scroll."
        ),
    },
    {
        "key": "counter_techniques",
        "name": "Counter Techniques",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Counter techniques are the art of answering: the opponent "
            "attacks, and the counter turns the attack energy into the "
            "counter opportunity. The principle is timing, not speed - "
            "the counter fighter does not move faster than the attacker "
            "but moves at the right instant, when the attack is "
            "committed and cannot be withdrawn. The classic counters "
            "form a small, deadly library: the back kick against the "
            "roundhouse (the attacker turns into the heel), the hook "
            "kick against the advancing roundhouse (the arc meets the "
            "advance from the side), the push kick against the blitz "
            "(the wall meets the charge), and the side kick against the "
            "spin (the piston meets the turn). The mathematics is "
            "reaction: visual reaction time runs about 0.25 seconds, and "
            "an opponent roundhouse at 8 meters per second from 2 meters "
            "away arrives in exactly 0.25 seconds - so the counter "
            "cannot be a reaction to the kick; it must be a read of the "
            "tell, the weight shift and shoulder turn that precede the "
            "kick by a tenth of a second. Counters are drilled as "
            "scripted exchanges first - partner throws the agreed "
            "attack at half speed, student answers with the agreed "
            "counter - then at speed, then with the attack unannounced. "
            "The counter fighter is taekwondo chess player: losing the "
            "first move to win the exchange."
        ),
        "how_it_works": (
            "Drill the back-kick counter first: partner throws a slow "
            "roundhouse to the body; as the partner hip turns, you spin "
            "the back kick into the opening - the timing cue is the "
            "partner shoulder turning, not the leg moving. Ten per side "
            "at half speed, then ten at three-quarter speed, the partner "
            "increasing commitment gradually. Next the hook kick counter "
            "to the advancing roundhouse, then the push kick counter to "
            "the blitz. The training ladder is: scripted and slow, "
            "scripted and fast, unscripted attack with scripted counter, "
            "then free - the counter called only after the previous "
            "stage is clean. Between rounds, study the tells: film the "
            "partner attacks and find the tenth-of-a-second weight "
            "shift that precedes each one. The faults are the late "
            "counter (thrown at the kick instead of the tell - it "
            "arrives after the impact), the counter without the guard "
            "(trading hits instead of answering), and the favorite "
            "counter thrown at every attack - the opponent who reads "
            "your counter counters it."
        ),
        "key_points": [
            "Counter principle: timing, not speed - move at the committed instant when the attack cannot be withdrawn, not faster than the attacker.",
            "The library: back kick vs. roundhouse, hook kick vs. advance, push kick vs. blitz, side kick vs. spin - each turns attack energy into opportunity.",
            "Reaction math: 0.25 s visual reaction vs. 0.25 s kick arrival - the counter reads the tell (weight shift, shoulder turn), never the kick.",
            "Drilling ladder: scripted slow, scripted fast, unscripted attack with scripted counter, then free - each stage clean before the next.",
            "The counter fighter is the chess player: losing the first move to win the exchange - but a predictable counter gets countered.",
        ],
        "requirements": [
            "Mastery of the countering kicks themselves: a shaky back kick makes a shaky counter.",
            "A drilling partner willing to attack on script at graduated speeds; counters cannot be learned solo.",
            "Film study of the partner tells: the tenth-second weight shift is invisible at full speed without slow motion.",
        ],
        "standards": [
            "World Taekwondo Competition Rules and Interpretation: legal counter techniques and scoring.",
            "Kukkiwon Taekwondo Textbook (2013): counterattack (bandae gonggyeok) principles.",
        ],
        "citations": [
            "World Taekwondo. Competition Rules and Interpretation. In force.",
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
        ],
        "sig_lens": (
            "The Signature lens treats the counter as the art editorial "
            "reply: the opponent writes the first draft, and the "
            "counter-fighter edits it into defeat. Where the public "
            "record clocks 0.25 seconds, the Signature method clocks "
            "the covenant of the tell - the weight shift read, the "
            "shoulder turn witnessed, the answer written before the "
            "question finishes. It is the most literate technique in "
            "the system: the practitioner must read the opponent "
            "manuscript fluently to write the reply in time."
        ),
    },
    {
        "key": "sparring_strategy",
        "name": "Match Strategy, Timing, and Distance",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Strategy is sparring with the brain engaged: the advanced "
            "fighter does not just throw techniques but manages the "
            "match - the score, the clock, the distance, and the "
            "opponent psychology. The WT scoring table is the "
            "strategist map: punch 1 point, body kick 2, head kick 3, "
            "turning body kick 4, turning head kick 5 - so a fighter "
            "trailing 7-12 needs not six body kicks but a head shot and "
            "a turning kick, and the wise fighter counts continuously. "
            "Distance is managed in three zones: kicking range (the "
            "roundhouse lands), punching range (too close to kick, the "
            "clinch approaches), and the dead zone between, where the "
            "strategist never lingers. Timing is managed in beats: the "
            "opponent attacks on a rhythm, and the strategist breaks it "
            "- attacking on the half beat, doubling when the opponent "
            "expects a single, going high when the guard drops for the "
            "body. The clock is managed in thirds: win the first round "
            "with volume, the second with counters as the opponent "
            "presses, the third with defense and the lead. Strategy is "
            "drilled in scenario rounds: start each round at a set score "
            "with a set time remaining, and fight the scenario - down "
            "by 4 with 30 seconds left, up by 2 with a minute left. The "
            "fighter who has fought every scenario in training has no "
            "surprises in competition."
        ),
        "how_it_works": (
            "Build the strategist in three drills. Drill one, the "
            "scoreboard: spar normal rounds but call the score aloud "
            "after every exchange until counting is unconscious - the "
            "fighter must always know the exact score and what "
            "combination erases the deficit. Drill two, the zones: mark "
            "three floor zones and spar with the rule that you may only "
            "attack from kicking range, must exit punching range within "
            "one second, and lose a point for lingering in the dead "
            "zone. Drill three, the scenarios: 30-second rounds from "
            "fixed scores - down 4 (attack: head kick plus turning kick "
            "wins), up 2 (defend: push kick and footwork, no risks), tied "
            "(first clean head shot decides). Between rounds, the coach "
            "and fighter review: what was the opponent rhythm, when did "
            "the guard drop, which counter is now loaded. The faults "
            "are the score-blind fighter (fighting hard with no idea "
            "who leads), the one-speed fighter (same rhythm all match, "
            "readable by round two), and the panic attack - abandoning "
            "the plan the moment the scoreboard turns."
        ),
        "key_points": [
            "The scoring map (WT): punch 1, body 2, head 3, turning body 4, turning head 5 - the trailing fighter counts what erases the deficit, continuously.",
            "Three distance zones: kicking range (attack), punching range (exit within a second), the dead zone between (never linger).",
            "Timing as rhythm-breaking: attack on the half beat, double when a single is expected, go high when the guard drops low.",
            "The clock in thirds: volume in round one, counters in round two as the opponent presses, defense with the lead in round three.",
            "Scenario drilling: fixed scores, fixed time remaining - down 4 with 30 seconds, up 2 with a minute - so competition holds no surprises.",
        ],
        "requirements": [
            "Unconscious scoreboard counting: the fighter must know the exact score at every second without being told.",
            "A coach or senior for between-round review; strategy is refined in the corner, not invented mid-round.",
            "Scenario discipline: the plan survives the scoreboard - abandoning it under pressure is the cardinal fault.",
        ],
        "standards": [
            "World Taekwondo Competition Rules and Interpretation: scoring values, round structure, and valid techniques.",
            "Kukkiwon Taekwondo Textbook (2013): competition strategy (gyeonggi jeonlyak) fundamentals.",
        ],
        "citations": [
            "World Taekwondo. Competition Rules and Interpretation. In force.",
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
        ],
        "sig_lens": (
            "The Signature lens reads match strategy as the art of "
            "reading the whole document while writing in it: the score "
            "the page count, the clock the deadline, the zones the "
            "margins. Where the public record lists points, the "
            "Signature method lists the covenant of the plan - the "
            "strategist signs the match strategy before the first "
            "round and does not tear it up when the ink runs. The "
            "scenario drill is the rehearsal of every ending, so the "
            "final signature is written with a steady hand."
        ),
    },
    {
        "key": "self_defense",
        "name": "Self-Defense Applications (Hosin Sul)",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Hosin sul, the art of self-defense, is taekwondo applied "
            "outside the rules: no mats, no referee, no weight classes, "
            "and no obligation to fight fair. The curriculum answers "
            "the common attacks in escalating order - the wrist grab, "
            "the clothing grab, the bear hug, the choke, the punch, the "
            "kick - each answered with the simplest technique that ends "
            "the threat and creates escape. The wrist-grab release is "
            "the first and most drilled: the attacker grip is weakest "
            "at the thumb, so the defender rotates the forearm against "
            "the thumb - a lever of about 15 centimeters working against "
            "a grip of 5 - a 3-to-1 mechanical advantage that breaks "
            "even a strong hold. Every defense follows the same "
            "sequence: evade or block, strike the vulnerable target "
            "(eyes, throat, groin, knee - the targets sport forbids), "
            "and escape - the goal is always to leave, never to win. "
            "Hosin sul is practiced with a cooperative partner at half "
            "speed until the motions are exact, then at speed with full "
            "protective gear, and it is always paired with the legal "
            "and ethical teaching: force must match the threat, and the "
            "trained fighter walks away from every fight that can be "
            "walked away from. This record covers civilian self-defense "
            "only - personal safety against criminal attack - and "
            "stays entirely within civilian martial-arts instruction."
        ),
        "how_it_works": (
            "Drill the wrist-grab release first: partner grips your "
            "right wrist with the right hand; rotate your forearm so "
            "the edge drives against the partner thumb - the weak point "
            "of every grip - while stepping back and pulling sharply; "
            "the 3-to-1 leverage breaks the hold with modest force. Ten "
            "per side at half speed until the rotation is exact, then "
            "ten at speed. Next the sequence drill: partner grabs the "
            "clothing with both hands; you evade offline, knife-hand "
            "strike to the neck line (pulled - control is graded), knee "
            "to the body pad, then break contact and move to the exit "
            "marker - every defense ends at the exit, because escape is "
            "the technique. Practice the full sequence: threat "
            "recognized, defense, strike, escape, report - the last "
            "step is calling for help and telling the authorities. The "
            "faults are the escalated response (answering a wrist grab "
            "with a head strike - force must match threat), the frozen "
            "defense (blocking forever instead of escaping), and "
            "practicing at full force on a partner - hosin sul injuries "
            "come from drilling, not from the street."
        ),
        "key_points": [
            "Hosin sul answers the common attacks in order: wrist grab, clothing grab, bear hug, choke, punch, kick - simplest effective answer, then escape.",
            "Wrist-release leverage: rotate the forearm against the thumb - 15 cm of lever vs. 5 cm of grip, a 3-to-1 advantage that breaks strong holds.",
            "Every defense ends at the exit: evade or block, strike the vulnerable target, escape - the goal is to leave, never to win.",
            "Sport targets are inverted: eyes, throat, groin, knee - the targets competition forbids are the self-defense targets.",
            "Force matches the threat, and the trained fighter walks away from every avoidable fight - the ethics are part of the technique.",
        ],
        "requirements": [
            "A cooperative drilling partner and full protective gear for any speed work; hosin sul injuries come from drilling.",
            "The control covenant: strikes to vulnerable targets are always pulled in practice - control is graded.",
            "Legal awareness: force must match the threat; students learn the local law of self-defense alongside the techniques.",
        ],
        "standards": [
            "Kukkiwon Taekwondo Textbook (2013): hosin sul - self-defense principles and standard defenses.",
            "Choi Hong Hi, Encyclopedia of Taekwon-Do, Vol. 5 (1999): releases and self-defense applications.",
        ],
        "citations": [
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
            "Choi Hong Hi. Encyclopedia of Taekwon-Do. 5th ed. International Taekwon-Do Federation; 1999. Vol. 5.",
        ],
        "sig_lens": (
            "The Signature lens treats hosin sul as the emergency "
            "clause of the combat covenant: the section of the document "
            "that is only read when the house is on fire. Where the "
            "public record measures 3-to-1 leverage, the Signature "
            "method measures the covenant of the exit - every defense "
            "signed with an escape route, because the Signature "
            "practitioner writes to live, not to win. The first and "
            "last technique of self-defense is the same: leave, and "
            "the signature on the incident is the report to those who "
            "keep the peace."
        ),
    },
]

ENTRIES += [
    {
        "key": "breaking",
        "name": "Breaking (Gyeokpa)",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Gyeokpa, breaking, is taekwondo proof of power: wood boards, "
            "tiles, or bricks broken with hand and foot techniques, the "
            "technique power made visible and undeniable. The standard "
            "test board is a pine board about 2.5 centimeters thick and "
            "30 centimeters square, held at the edges; breaking it with "
            "a hand technique requires on the order of 3000 newtons of "
            "peak force - roughly 300 kilograms of momentary load - "
            "delivered in a few milliseconds. The physics rewards "
            "speed over strength: the board breaks when the striking "
            "tool is still accelerating through the impact point, so "
            "the striker aims not at the board but through it, at a "
            "point centimeters beyond. Breaking tests four things at "
            "once: power (the board breaks or it does not), accuracy "
            "(the strike must land on the grain center), focus (the "
            "ki hap and the total commitment), and courage (the "
            "beginner instinct is to pull the strike, which guarantees "
            "injury). The ladder is strict: single board with the palm "
            "heel, then knife-hand, then side kick, then multiple boards "
            "with spacers, then the advanced breaks - jumping, spinning, "
            "and the power breaks of dan examinations. Breaking is "
            "never practiced alone by beginners: holders must know "
            "their job, and the instructor judges readiness. A failed "
            "break is a lesson, not a disgrace - but a break attempted "
            "before readiness is an injury."
        ),
        "how_it_works": (
            "Begin with the palm-heel break on a single pine board: "
            "holder grips the board firmly at both edges, top edge at "
            "your shoulder height; chamber the hand at the opposite "
            "shoulder; strike down and through with the palm heel, "
            "aiming at a point 10 centimeters beyond the board, ki hap "
            "at impact. The board must be struck at its center, along "
            "the grain, with the wrist locked - ten practice strikes on "
            "a rebreakable plastic board first, then the real board. "
            "When single boards break cleanly ten times in a row, move "
            "to the knife-hand, then the side kick (holder braces the "
            "board at chest height), then two boards with a finger-width "
            "spacer. The holder technique matters as much as the strike: "
            "hold tight, fingers clear of the break line, body braced - "
            "a loose holder steals the impact and injures the striker. "
            "The faults are the pulled strike (aiming at the board "
            "surface instead of through it - the cause of most "
            "injuries), the off-center hit (which bends instead of "
            "breaking), and the hesitation: the break is committed in "
            "the chamber, and doubt after the chamber is the enemy."
        ),
        "key_points": [
            "Gyeokpa: the proof of power - a standard pine board (2.5 cm thick) needs about 3000 N of peak force, delivered in milliseconds.",
            "Speed over strength: the board breaks when the tool is still accelerating through impact - aim 10 cm beyond the board, not at it.",
            "Four tests at once: power, accuracy (grain center), focus (ki hap, total commitment), and courage (no pulling the strike).",
            "Strict ladder: palm heel single board, then knife-hand, then side kick, then spaced multiples, then jumping/spinning/power breaks.",
            "The holder is half the technique: tight grip, fingers clear, body braced - a loose holder injures the striker; beginners never break alone.",
        ],
        "requirements": [
            "Instructor judgment of readiness before the first real board; rebreakable plastic boards for all early practice.",
            "Trained holders who know the grip, the brace, and the finger clearance; holder and striker drill as a pair.",
            "The commitment covenant: once chambered, the break is thrown - hesitation after the chamber causes the injuries.",
        ],
        "standards": [
            "Kukkiwon Taekwondo Textbook (2013): gyeokpa - breaking principles, board specifications, technique progression.",
            "World Taekwondo Poomsae Competition Rules: breaking as a component of advanced demonstration.",
        ],
        "citations": [
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
        ],
        "sig_lens": (
            "The Signature lens sees gyeokpa as the notarization of the "
            "combat document: the board is the witness, the break the "
            "stamp that cannot be forged. Where the public record "
            "counts 3000 newtons, the Signature method counts the "
            "covenant of the follow-through - aim 10 centimeters beyond, "
            "because a signature that stops at the surface is "
            "incomplete. The failed break is not a disgrace but an "
            "unsigned draft: the practitioner returns, re-inks, and "
            "signs again."
        ),
    },
    {
        "key": "mastery_path",
        "name": "The Mastery Path: Belts, Testing, and Teaching",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The belt system is taekwondo map of the mastery path: ten "
            "gup (color belt) grades climbing from 10th gup white belt "
            "to 1st gup red/black, then the dan (black belt) grades from "
            "1st to 9th dan. A typical dedicated student needs about 3 "
            "months per early gup and 6 to 8 months per late gup - "
            "roughly 46 months, nearly 4 years, to reach 1st dan - and "
            "the dan grades then require years each: 2nd dan after 1 "
            "year as 1st dan, 3rd after 2 more, the intervals growing "
            "with rank. Each grading tests the full curriculum of the "
            "grade: basics, the poomsae or tul of the rank, sparring, "
            "breaking (from green belt up), and the tenets - examiners "
            "fail students with brilliant kicks and poor character "
            "without hesitation. But the belt is the least important "
            "part of the path: the true curriculum is the teaching "
            "ladder this database follows, from the ready stance of "
            "rank 1 to the breaking and mastery of rank 10, each rung "
            "compounding the last. At 1st dan the student is considered "
            "a serious beginner - the black belt marks the end of the "
            "basics, not the end of learning. The master grades (4th "
            "dan and above) carry the teaching duty: the art survives "
            "only because each generation teaches the next, and the "
            "highest technique in taekwondo is the clear explanation. "
            "This record closes the database where the first record "
            "opened it: the way of foot and hand is a way, and a way "
            "is walked, not finished."
        ),
        "how_it_works": (
            "Walk the path one grading at a time. For each gup grade, "
            "learn the curriculum (the techniques, the form, the "
            "sparring requirements) in the first two thirds of the "
            "training period, then spend the final third in "
            "examination preparation: performing every requirement "
            "under simulated grading pressure, with seniors watching "
            "and scoring. Keep a training log: date, techniques "
            "drilled, forms practiced, rounds sparred - the log is the "
            "map that shows whether the 46 months are being walked or "
            "wandered. At each dan grade, add the teaching duty: assist "
            "with the beginner class, then take a section of it, then "
            "examine lower grades under supervision - the master is "
            "made by teaching, not by collecting techniques. Prepare "
            "for gradings as the masters advise: sleep well the week "
            "before, arrive early, bow with full attention, and perform "
            "every technique as if it were the only one the examiners "
            "will see. The faults of the path are the belt-chaser (who "
            "collects grades without depth), the comparer (who measures "
            "against other students instead of yesterday self), and the "
            "quitter at brown belt - the statistics say the highest "
            "dropout comes one grade before black, exactly where the "
            "training gets hardest and the reward closest."
        ),
        "key_points": [
            "Ten gup grades (white to 1st gup) then dan grades 1st-9th: about 46 months of dedicated training to 1st dan, years per dan after.",
            "Every grading tests the full grade curriculum - basics, form, sparring, breaking, tenets - and character failures fail regardless of technique.",
            "The black belt marks the end of the basics: 1st dan is a serious beginner, not a master; mastery is the dan grades.",
            "Teaching is the highest technique: 4th dan and above carry the duty, and the art survives only through each generation teaching the next.",
            "The path faults: belt-chasing without depth, comparing against others instead of yesterday self, and quitting one grade before black.",
        ],
        "requirements": [
            "A training log from the first month: the 46 months must be walked deliberately, not wandered.",
            "Examination preparation under simulated pressure in the final third of each grade period.",
            "The teaching progression from 1st dan: assist, then lead a section, then examine under supervision.",
        ],
        "standards": [
            "Kukkiwon Dan/Poom certification regulations: grade requirements and time-in-grade intervals.",
            "ITF degree promotion requirements: tul, sparring, and theory per degree.",
            "Kukkiwon Taekwondo Textbook (2013): the grading system and its philosophy.",
        ],
        "citations": [
            "Kukkiwon. Taekwondo Textbook. Seoul: Kukkiwon; 2013.",
        ],
        "sig_lens": (
            "The Signature lens reads the belt path as the binding of "
            "the combat manuscript: ten gup the chapters of the first "
            "volume, nine dan the volumes of the master work, each "
            "grading a page signed and sealed. Where the public record "
            "counts 46 months, the Signature method counts the covenant "
            "of the log - every session written down, because an "
            "unsigned training history cannot be trusted. And the "
            "highest technique is the clear explanation: the master "
            "signature is not the one most admired, but the one most "
            "faithfully copied by the next hand."
        ),
    },
]

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
ranks = [e["ladder_rank"] for e in ENTRIES]
assert ranks == sorted(ranks), "entries not in ladder order"
assert all(1 <= r <= 10 for r in ranks), "ladder_rank out of range"
tiers = [e["ladder_tier"] for e in ENTRIES]
assert tiers == sorted(tiers, key=lambda t: ("foundations", "compounded", "advanced").index(t)), "tiers not ordered"
for e in ENTRIES:
    for k in ("key", "name", "group", "ladder_rank", "ladder_tier",
              "description", "how_it_works", "key_points", "requirements",
              "standards", "citations", "sig_lens"):
        assert k in e, "missing %s" % k
    assert len(e["description"]) > 200, "stub description in %s" % e["key"]
    blob = (e["description"] + e["how_it_works"] + e["sig_lens"]).lower()
    assert "facebook" not in blob and "bat belt" not in blob
    assert "'" not in e["name"], "apostrophe in title %s" % e["key"]
