#!/usr/bin/env python3
"""Entries for the Aikido Combat databases (Manon's combat orders 2026-10-17,
combat batch 2).

Dedupe pre-verified 2026-10-17: all 68 titles (34 public + 34 Signature
Edition) checked through DedupeGate against the whole system before
authoring - zero collisions, zero refusals.

Two NEW databases, 34 ladder-ordered records each:

  combat-aikido              - The Aikido Combat Database
                               (public-harvest: real, fact-checked aikido -
                               tai-sabaki movement, ukemi safe falling, wrist
                               controls (ikkyo through gokyo), throws
                               (irimi-nage, shiho-nage, kotegaeshi and the
                               rest), pins, randori, and weapons disarms -
                               each record carrying real Japanese terminology
                               with translations and step-by-step
                               body-mechanics instruction; standard
                               references the Aikikai Foundation grading
                               tradition, Morihei Ueshiba the founder
                               (O-Sensei, 1883-1969), Budo (1938), and the
                               kyo-waza teaching sequence)
  combat-aikido-signature    - The Aikido Combat Signature Database
                               (his original Signature Aiki Method: every
                               technique a covenant of movement, the art the
                               armory of harmony, blending the oath, the
                               throw the handshake, the pin the honor hold;
                               src signature, titles suffixed " (Signature
                               Edition)", never presented as authentic
                               public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBAIK- (public) and JAH-CBAIKS- (signature), verified free
in the manifest (2,410 databases, zero hits) and in every shard index file
(zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_aikido.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with the
OK marker; the build machine-executes all 68 demos.

Civilian martial-arts instruction only. Nothing hate-adjacent, profane, or
inappropriate; no religious talk. Nothing on neutralizing or defeating
military or defense-grade systems.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Aiki Method: every "
            "technique a covenant of movement, the art the armory of "
            "harmony, blending the oath, the throw the handshake, and the "
            "pin the honor hold. Clearly labeled Signature-made, never "
            "presented as authentic public record.")

CIT_UESHIBA = ("Ueshiba M. Budo: Teachings of the Founder of Aikido. "
               "Kodansha International; 1991 (orig. 1938).")
CIT_AIKIKAI = ("Aikikai Foundation. Aikido grading and technique syllabus "
               "tradition, Hombu Dojo, Tokyo.")
CIT_SAOTOME = ("Saotome M. Aikido and the Harmony of Nature. Shambhala; "
               "1993.")
CIT_SHIODA = ("Shioda G. Aikido Shugyo: Harmony in Confrontation. "
               "Shindensha; 2002.")
CIT_WESTBROOK = ("Westbrook A, Ratti O. Aikido and the Dynamic Sphere. "
                 "Charles E. Tuttle; 1970.")
CIT_PRANIN = ("Pranin S. (ed.) Aikido Masters: Prewar Students of Morihei "
              "Ueshiba. Aiki News; 1993.")

ENTRIES = [
    {
        "key": "what_is_aikido",
        "name": "What Aikido Is: The Way of Harmony",
        "group": "Foundations and History",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Aikido (合気道) is the Japanese martial art whose name means "
            "the way (do) of harmonizing (ai) with life energy (ki). "
            "Founded by Morihei Ueshiba (O-Sensei, 1883-1969), aikido is "
            "built on a single radical idea: instead of meeting force with "
            "force, the practitioner blends with an attacker's motion, "
            "redirects it, and controls the attacker through throws, pins, "
            "and joint locks. There are no competitions in traditional "
            "aikido; the practice is cooperative, with partners taking "
            "turns as attacker (uke) and defender (nage or tori). The art "
            "grew from older Japanese jujutsu schools, especially Daito-ryu "
            "aiki-jujutsu, combined with Ueshiba's spiritual conviction "
            "that true victory is victory over oneself. Training is "
            "physical - falls, rolls, throws, wrist controls - but its "
            "stated purpose is self-mastery and the peaceful resolution of "
            "conflict, which is why aikido dojos attract law enforcement, "
            "security professionals, and civilians seeking real, "
            "non-destructive self-protection skills."
        ),
        "how_it_works": (
            "Aikido works through three physical facts. First, a moving "
            "body is easiest to control when you move with it rather than "
            "stop it: the defender (nage) steps off the line of attack "
            "(tai-sabaki), joining the attacker's momentum instead of "
            "opposing it. Second, balance (kuzushi) is a fragile point: a "
            "small push at the right angle, timed with the attacker's step, "
            "tips the whole body because the center of mass leaves the "
            "support base. Third, joints bend one way: wrist controls and "
            "arm locks guide the attacker's limb to the edge of its natural "
            "range, where pain and structural lock make resistance "
            "impossible without self-injury. Training drills these three "
            "facts at walking speed with a cooperative partner until the "
            "body responds without thinking. Step one is always the same: "
            "get off the center line. Step two is connect - hand to wrist, "
            "body to body - so you can feel where the balance is going. "
            "Step three is lead that balance past its support and down. "
            "The throw or pin is simply the shape the fall takes."
        ),
        "key_points": [
            "Ai means harmony or joining, ki means spirit or life energy, do means the way - the name itself is the curriculum: join the energy, walk the way.",
            "The art has no tournaments in its traditional form; practice is cooperative, alternating attacker (uke) and defender (nage) roles.",
            "It descends from Daito-ryu aiki-jujutsu, reworked by Morihei Ueshiba into an art whose stated aim is resolving conflict without destruction.",
            "Three physical facts power every technique: move with the force, tip the balance (kuzushi), and guide joints to the edge of their range.",
            "Training is slow and cooperative at first; speed and realism grow only as control and safe falling (ukemi) grow with them.",
        ],
        "requirements": [
            "A qualified instructor and a safe training surface (mats or sprung floor), because every technique ends in a fall.",
            "A training partner willing to attack sincerely and fall safely - cooperation, not competition, is the training fuel.",
            "A white keikogi (training uniform) and, after promotion, the hakama (wide pleated trousers) worn by graded students.",
            "Patience: the first months teach falling and footwork, not throws, because ukemi is the license that lets everything else be practiced.",
        ],
        "standards": [
            "Technique names and the kyu/dan grading structure follow the Aikikai Foundation syllabus tradition from Hombu Dojo, Tokyo.",
            "The founder's principles are preserved in Budo (1938), Ueshiba's own technical manual.",
            "Dojo etiquette (reiho) - bowing to the kamiza, to the instructor, and to each partner - is standard across aikido schools.",
        ],
        "citations": [CIT_UESHIBA, CIT_AIKIKAI, CIT_WESTBROOK],
        "sig_lens": (
            "The Signature read: aikido is the covenant of harmony made "
            "visible - the armory where blending is the oath and no "
            "technique destroys what it controls. Where the public record "
            "teaches the way of harmonizing with energy, the Signature "
            "lens frames it as the art's original promise kept: every "
            "movement a handshake with the attacker's force, every pin an "
            "honor hold that refuses to break what it holds."
        ),
    },
    {
        "key": "founder_ueshiba",
        "name": "The Founder: Morihei Ueshiba and the Birth of Aikido",
        "group": "Foundations and History",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Morihei Ueshiba (植芝 盛平, 1883-1969), called O-Sensei (great "
            "teacher), founded aikido after a lifetime of martial study. "
            "Born in Tanabe, Japan, he trained in sumo, in the Yagyu "
            "Shingan-ryu and other jujutsu schools, and most decisively "
            "under Sokaku Takeda of Daito-ryu aiki-jujutsu from 1915. "
            "After deep spiritual experiences in the 1920s, Ueshiba "
            "began teaching that martial technique should express love "
            "and protection rather than destruction, and he named his art "
            "aikido in 1942. He opened the Hombu Dojo in Tokyo, and after "
            "his death his son Kisshomaru and later grandson Moriteru "
            "carried the Aikikai forward, spreading aikido to more than "
            "a hundred countries. Students study the founder's life "
            "because every technique carries his answer to one question: "
            "how do you stop violence without becoming violent?"
        ),
        "how_it_works": (
            "Understanding the founder works as a training tool: his "
            "biography is the art's specification sheet. Step one, trace "
            "the lineage: Daito-ryu gave aikido its joint locks and "
            "aiki principle; Ueshiba's spiritual turn gave it the "
            "non-destructive intent. Step two, read Budo (1938), his own "
            "manual, where techniques already show the blend of "
            "battlefield jujutsu and the founder's philosophy. Step "
            "three, watch how the art changed across his life: the "
            "pre-war techniques are sharp and martial; the post-war "
            "techniques are rounder, flowing, and protective even of the "
            "attacker. Step four, test every technique you learn against "
            "his question - does this control without unnecessary harm? "
            "If a technique only works by breaking the partner, you are "
            "doing the founder's jujutsu, not his aikido. The history is "
            "not decoration; it is the acceptance test for the whole "
            "ladder."
        ),
        "key_points": [
            "Morihei Ueshiba (1883-1969), O-Sensei, trained in sumo, several jujutsu schools, and decisively in Daito-ryu aiki-jujutsu under Sokaku Takeda from 1915.",
            "The art was named aikido in 1942; the Hombu Dojo in Tokyo became its world headquarters under the Aikikai Foundation.",
            "His 1938 manual Budo shows the techniques in their earlier, more martial form before the post-war softening.",
            "The founder's design question - stop violence without becoming violent - is the acceptance test for every technique on this ladder.",
            "Succession passed to his son Kisshomaru and grandson Moriteru, carrying aikido to well over a hundred countries.",
        ],
        "requirements": [
            "Access to Budo (1938) or a reliable translation for the founder's own technical voice.",
            "A timeline sense: pre-war sharpness versus post-war roundness, so students read old photographs correctly.",
            "An instructor who can name the lineage - Daito-ryu roots, Omoto-kyo spiritual period, Aikikai founding - in plain order.",
            "The habit of testing each new technique against the founder's question before calling it learned.",
        ],
        "standards": [
            "Dates and lineage follow the Aikikai Foundation's official history of O-Sensei (1883-1969).",
            "Budo (1938) is cited as the founder's own technical manual.",
            "Prewar student accounts are cross-checked against Pranin's Aikido Masters collection.",
        ],
        "citations": [CIT_UESHIBA, CIT_AIKIKAI, CIT_PRANIN],
        "sig_lens": (
            "The Signature read: the founder built the armory and then "
            "hung the oath on its door - technique must protect even the "
            "one it defeats. Where the public record gives dates and "
            "lineage, the Signature lens treats O-Sensei's life as the "
            "first covenant: every throw after him is measured against "
            "the man who refused to let martial skill become cruelty."
        ),
    },
    {
        "key": "dojo_etiquette",
        "name": "The Aikido Dojo: Etiquette, Bowing, and Rei",
        "group": "Foundations and History",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The dojo (道場, place of the way) runs on rei (礼): etiquette "
            "as a training tool, not decoration. Students bow (zarei from "
            "kneeling, ritsurei standing) when entering and leaving the "
            "mat, toward the kamiza (the shrine or founder's portrait at "
            "the front), toward the instructor at the start and end of "
            "class, and to every partner before and after practice. The "
            "class opens with mokuso (quiet sitting) and a formal bow "
            "sequence, then warm-ups (junbi taiso), technique practice, "
            "and a closing bow. Etiquette does real work: bowing to a "
            "partner is a contract that says 'I will attack sincerely and "
            "protect you completely'; keeping the mat clean and weapons "
            "racked is safety engineering; lining up by rank (sempai "
            "senior, kohai junior) keeps beginners paired with people who "
            "can keep them safe. A student who masters rei has already "
            "learned the first aikido technique: full attention, given "
            "willingly, in both directions."
        ),
        "how_it_works": (
            "Etiquette works by making safety automatic. Step one, the "
            "entering bow: pause at the mat edge, bow toward the kamiza, "
            "then step on - this marks the boundary between street "
            "mind and training mind. Step two, the opening ceremony: "
            "sit in seiza (kneeling), close the eyes for mokuso, then "
            "bow in unison - 'onegai shimasu' (please teach me / please "
            "train with me). Step three, partner protocol: before each "
            "technique, face the partner, bow, and state who attacks "
            "first; after the technique, bow again - 'domo arigato' "
            "(thank you). Step four, the safety habits hidden inside "
            "manners: never walk behind someone practicing weapons, "
            "keep fingernails and toenails short (checked like a "
            "pre-flight list), tie the belt correctly so the gi never "
            "opens mid-throw, and sit seiza at the mat edge when "
            "watching, never sprawling into the practice space. Step "
            "five, the closing bow mirrors the opening. Students who "
            "treat this as choreography miss the point; students who "
            "treat it as a checklist stay unhurt for decades."
        ),
        "key_points": [
            "Rei (etiquette) is a training tool: the bow to a partner is a contract for sincere attacks and complete protection.",
            "Zarei (kneeling bow) and ritsurei (standing bow) mark every boundary: mat edge, class start, class end, partner change.",
            "Mokuso (quiet sitting) opens class; junbi taiso (warm-ups) follow; the closing bow mirrors the opening.",
            "Sempai/kohai (senior/junior) pairing keeps beginners with partners skilled enough to keep them safe.",
            "Manners hide safety engineering: short nails, tied gi, clean mats, and never crossing behind weapons practice.",
        ],
        "requirements": [
            "A keikogi (training uniform) kept clean, and a belt tied so the jacket cannot open during throws.",
            "Short fingernails and toenails, no jewelry or watches on the mat.",
            "Willingness to sit seiza (kneeling) for the opening and closing ceremonies.",
            "Attention to the kamiza direction and the instructor's commands in Japanese - 'onegai shimasu' to begin, 'domo arigato gozaimashita' to close.",
        ],
        "standards": [
            "Reiho (etiquette forms) follow Hombu Dojo convention: zarei, ritsurei, mokuso, and partner bows.",
            "The kamiza faces the class; students line up by rank with seniors to the instructor's right.",
            "Terminology (dojo, rei, seiza, mokuso, sempai, kohai) follows standard Aikikai usage.",
        ],
        "citations": [CIT_AIKIKAI, CIT_WESTBROOK],
        "sig_lens": (
            "The Signature read: the dojo is the armory and etiquette is "
            "its combination lock - every bow a small oath that the "
            "weapons inside will only ever be drawn in practice and in "
            "protection. Where the public record lists the forms, the "
            "Signature lens sees the covenant: attention given willingly, "
            "in both directions, before a single throw is ever taught."
        ),
    },
    {
        "key": "shisei_kamae",
        "name": "Shisei and Kamae: Posture and the Hanmi Stance",
        "group": "Movement and Ukemi",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Shisei (姿勢) is posture; kamae (構え) is the ready stance. In "
            "aikido the default kamae is hanmi (半身, half-body): feet in a "
            "triangle, one foot forward, body turned about sixty degrees "
            "so only half the torso faces the partner - presenting a "
            "small target while keeping both hands between you and the "
            "attack. Weight sits centered and low, knees soft, spine "
            "straight, chin slightly tucked, eyes soft and wide "
            "(metsuke) so the whole partner is seen without staring at "
            "one hand. Shisei is checked constantly because every "
            "technique that fails can be traced to posture that failed "
            "first: leaning forward invites a pull, leaning back "
            "invites a push, and stiff knees kill the footwork. Hanmi "
            "is trained on both sides (hidari-hanmi, left foot forward; "
            "migi-hanmi, right foot forward) until either side feels "
            "like home."
        ),
        "how_it_works": (
            "Build the stance from the ground up. Step one, feet: step "
            "one foot forward about one shoulder-width and turn both "
            "feet roughly sixty degrees toward the partner, so the feet "
            "form a triangle with the back foot - weight 50/50, or "
            "slightly forward. Step two, knees: soften them until the "
            "hips drop a few inches; the test is that someone could "
            "push your shoulders gently and you would rock, not topple. "
            "Step three, spine: straight and vertical, as if a string "
            "lifts the crown of the head; tuck the chin a finger's "
            "width. Step four, hands: raise both hands to chest height, "
            "elbows heavy and slightly bent, fingers together and "
            "alive - the front hand guards, the back hand supports. "
            "Step five, eyes: soften the gaze (metsuke) to take in the "
            "partner's whole body, shoulders to feet, without locking "
            "onto the attacking hand. Step six, switch sides: practice "
            "hidari-hanmi and migi-hanmi equally, because techniques "
            "demand both. Check posture every few minutes at first; "
            "within months the body starts checking itself."
        ),
        "key_points": [
            "Hanmi (half-body stance) turns the body about sixty degrees, presenting a small target while keeping both hands in play.",
            "Shisei (posture) is the root diagnostic: most failed techniques trace back to leaning, stiff knees, or a collapsed spine.",
            "Weight stays centered and low with soft knees; a gentle shoulder push should rock you, not topple you.",
            "Metsuke (soft, wide gaze) watches the whole partner - shoulders to feet - instead of fixating on the attacking hand.",
            "Both sides are trained equally: hidari-hanmi (left forward) and migi-hanmi (right forward).",
        ],
        "requirements": [
            "A flat training surface and enough room to step a full stride in any direction.",
            "Bare feet (standard on the mat) for grip and foot sensitivity.",
            "A mirror or a partner's eyes at first, to catch the lean you cannot feel yet.",
            "Daily short practice: stance is built by repetition, not by one long session.",
        ],
        "standards": [
            "Hanmi, shisei, kamae, and metsuke follow standard Aikikai terminology.",
            "The roughly sixty-degree body angle and triangular foot placement follow Hombu Dojo basic instruction.",
            "Both hanmi sides are required for kyu grading demonstrations.",
        ],
        "citations": [CIT_AIKIKAI, CIT_WESTBROOK, CIT_SHIODA],
        "sig_lens": (
            "The Signature read: posture is the first covenant the body "
            "signs - upright, centered, and ready to receive rather than "
            "to collide. Where the public record measures the angles, "
            "the Signature lens treats hanmi as the oath stance: half the "
            "body offered, none of it surrendered, the armory's door held "
            "open but never unguarded."
        ),
    },
    {
        "key": "ashi_sabaki",
        "name": "Ashi-sabaki: Footwork, Ayumi-ashi and Tsugi-ashi",
        "group": "Movement and Ukemi",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Ashi-sabaki (足捌き) is footwork - the engine under every "
            "aikido technique. The two basic steps are ayumi-ashi (歩み足, "
            "walking step: feet pass each other naturally, as in walking) "
            "and tsugi-ashi (継ぎ足, following step: the back foot follows "
            "the front without passing, keeping the hanmi triangle "
            "intact). Ayumi-ashi covers ground quickly; tsugi-ashi keeps "
            "the stance stable so you can throw or be thrown from it. "
            "Advanced footwork adds okuri-ashi (sliding the stance as a "
            "unit) and the pivots of tenkan, but the rule never changes: "
            "the feet move first, the hands follow, and the hips carry "
            "both. Beginners drill ashi-sabaki across the mat in lines - "
            "forward, backward, and sideways - until the steps are silent, "
            "level (no bobbing), and automatic. If your footwork is "
            "noisy, your technique will be late."
        ),
        "how_it_works": (
            "Drill the steps in order. Step one, ayumi-ashi: from hanmi, "
            "step the back foot forward past the front foot, letting the "
            "body turn naturally - walk, but keep the knees soft and the "
            "head level, as if carrying a full cup of water. Step two, "
            "tsugi-ashi: from hanmi, slide the front foot forward a short "
            "step, then bring the back foot up behind it without passing "
            "- the triangle travels but never breaks. Step three, "
            "backward: reverse both patterns, leading with the back foot. "
            "Step four, silence: practice on a hard floor at home and "
            "listen - each step should land soft, heel then sole, with no "
            "slap. Step five, level: have a partner watch your head "
            "against a wall line; bobbing means the knees are locking. "
            "Step six, combine: cross the mat alternating ayumi-ashi and "
            "tsugi-ashi on command, switching hanmi sides at the wall. "
            "The test is simple: can you move in any direction without "
            "looking at your feet and without losing hanmi? When yes, "
            "the engine is installed."
        ),
        "key_points": [
            "Ayumi-ashi (walking step, feet pass) covers ground; tsugi-ashi (following step, feet never pass) preserves the hanmi triangle.",
            "The hierarchy is feet first, hands follow, hips carry both - hands never outrun the feet.",
            "Good footwork is silent and level: no slapping steps, no bobbing head.",
            "Forward, backward, and sideways patterns are all drilled; techniques demand every direction.",
            "Okuri-ashi (sliding the whole stance) extends the same idea to gliding entries.",
        ],
        "requirements": [
            "A clear lane of mat to walk - beginners drill in lines, not in place.",
            "Soft knees and a level head; a wall line or partner's eye to check bobbing.",
            "A hard floor at home for the silence test (optional but revealing).",
            "Equal practice moving forward, back, and to both sides.",
        ],
        "standards": [
            "Ashi-sabaki, ayumi-ashi, tsugi-ashi, and okuri-ashi follow standard Aikikai terminology.",
            "Footwork patterns are demonstrated in kyu grading examinations.",
            "Silent, level movement is the Hombu Dojo basic-instruction standard.",
        ],
        "citations": [CIT_AIKIKAI, CIT_WESTBROOK],
        "sig_lens": (
            "The Signature read: footwork is the covenant of arrival - "
            "the oath that the body will be where the technique needs it "
            "before the hands ask. Where the public record counts the "
            "steps, the Signature lens hears them: silent feet are the "
            "armory's quiet promise that power travels through the hips, "
            "never through noise."
        ),
    },
    {
        "key": "tenkan_irimi_movement",
        "name": "Tenkan and Irimi: Turning and Entering Movement",
        "group": "Movement and Ukemi",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Tai-sabaki (体捌き) is whole-body movement, and its two "
            "master keys are irimi (入り身, entering: stepping straight "
            "into and past the attack, taking the attacker's blind "
            "side) and tenkan (転換, turning: pivoting 180 degrees on "
            "the front foot so the attack slides past and you finish "
            "behind its line). Irimi answers a straight attack by "
            "becoming the center it cannot reach; tenkan answers by "
            "letting the attack pass and joining its tail. Nearly every "
            "aikido throw is one of these two movements with arms "
            "attached: irimi-nage is irimi plus an arm sweep, "
            "shiho-nage is tenkan plus a wrist turn. Beginners drill "
            "them empty-handed against a partner's straight wrist grab "
            "or face strike until the pivot is one smooth motion, not "
            "two steps. The most common beginner error is turning the "
            "shoulders without moving the feet - tenkan is a foot "
            "pivot, and the body follows the feet."
        ),
        "how_it_works": (
            "Learn tenkan first. Step one, stance: stand in hidari-hanmi "
            "facing the partner. Step two, pivot: slide the front (left) "
            "foot slightly forward, then pivot 180 degrees on the ball "
            "of that foot while the back foot sweeps around behind you - "
            "finish in the mirror hanmi, facing the way you came, the "
            "partner's attack now passing where you were. Step three, "
            "keep the hands: as you turn, the front hand traces a small "
            "circle at chest height - the hands describe what the feet "
            "do. Step four, irimi: from hanmi, step the back foot "
            "diagonally forward past the partner's front foot, driving "
            "off the back leg so the hips - not the shoulders - lead; "
            "your body passes the attack's line and your front hand "
            "meets the partner's face or shoulder as a guide, never a "
            "shove. Step five, blend them: drill tenkan-tenkan-irimi in "
            "sequence across the mat until direction changes cost no "
            "thought. Step six, test: have the partner push your chest "
            "while you tenkan - if you are still there to be pushed, "
            "the feet turned but the center stayed."
        ),
        "key_points": [
            "Irimi (entering) steps into and past the attack to take the blind side; tenkan (turning) pivots 180 degrees to let it pass and join its tail.",
            "Almost every throw is irimi or tenkan with arms attached - the footwork is the technique's skeleton.",
            "Tenkan pivots on the ball of the front foot; the back foot sweeps around - shoulders never turn without the feet.",
            "Irimi is driven by the hips and back leg, with the guiding hand meeting the partner softly, never shoving.",
            "Drill the sequence tenkan-tenkan-irimi across the mat until direction changes are thoughtless.",
        ],
        "requirements": [
            "Solid hanmi and ashi-sabaki first - tai-sabaki stacks on footwork, it does not replace it.",
            "A cooperative partner giving straight, committed attacks (a lazy attack teaches a lazy pivot).",
            "Enough mat space to pivot a full 180 degrees without hitting anyone.",
            "A teacher's eye on the pivot foot - the most common fault is spinning on the heel instead of the ball.",
        ],
        "standards": [
            "Irimi, tenkan, and tai-sabaki follow standard Aikikai terminology.",
            "The 180-degree pivot on the front foot is the Hombu Dojo basic form.",
            "Both movements appear in every kyu grading examination.",
        ],
        "citations": [CIT_AIKIKAI, CIT_WESTBROOK, CIT_SAOTOME],
        "sig_lens": (
            "The Signature read: irimi and tenkan are the two oaths of "
            "position - enter the storm's eye or step aside and let it "
            "pass, but never stand where the blow lands. Where the "
            "public record diagrams the pivot, the Signature lens names "
            "the covenant: the feet swear first, the body keeps the "
            "promise, and the throw is simply the receipt."
        ),
    },
    {
        "key": "ukemi_forward_roll",
        "name": "Ukemi: Mae-ukemi, the Forward Roll",
        "group": "Movement and Ukemi",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Ukemi (受け身, receiving body) is the art of receiving a "
            "technique safely - the license that lets everything else be "
            "practiced. Mae-ukemi (前受け身) is the forward roll: not a "
            "gymnastics tuck but a diagonal roll across the back, from "
            "one hand and shoulder to the opposite hip, that turns a "
            "throw's energy into a smooth rotation. The roll starts low: "
            "one knee touches the mat, the same-side hand reaches forward "
            "in a curved blade, the head tucks to look at the belt, and "
            "the body rolls over the rounded back - never over the top of "
            "the head or straight down the spine. Done well it is silent "
            "and can be repeated dozens of times; done badly it bruises "
            "shoulders and teaches fear. Beginners practice from kneeling "
            "first, then standing, then from a gentle push, and only then "
            "from real throws. A student who cannot roll cannot train - "
            "ukemi is the first and last technique of aikido."
        ),
        "how_it_works": (
            "Build the roll in stages. Stage one, kneeling: kneel on one "
            "knee, place the same-side hand on the mat ahead with fingers "
            "together and thumb tucked (the blade), tuck the chin to look "
            "at your own belt, and round the back like a wheel. Roll "
            "diagonally - hand, forearm, shoulder, across the back to the "
            "opposite hip and leg - and come up on the far foot, hands "
            "already in guard. Stage two, standing: from hanmi, lower the "
            "front knee toward the mat first - the roll begins from low, "
            "never from a standing dive. Stage three, direction: practice "
            "rolling left and right equally; the diagonal path protects "
            "the spine by keeping it off the mat's center line. Stage "
            "four, breathing: exhale on the roll; held breath makes the "
            "body rigid and the landing hard. Stage five, standing up: "
            "finish every roll on balance, facing the partner, hands up - "
            "the roll ends in kamae, not in a heap. Common faults to fix: "
            "rolling over the top of the head (tuck the chin harder), "
            "slapping the mat with a flat hand (keep the blade curved), "
            "and holding the breath (exhale audibly until it becomes "
            "habit)."
        ),
        "key_points": [
            "Mae-ukemi rolls diagonally - hand to opposite hip - across a rounded back, never over the head or straight down the spine.",
            "The roll starts low: the front knee reaches the mat before the body rotates, never a standing dive.",
            "Chin tucked to the belt, blade hand curved with thumb in, exhale on the roll.",
            "Every roll ends standing in guard facing the partner - ukemi finishes in kamae.",
            "Learned in stages: kneeling, then standing, then from a push, then from real throws; both sides equally.",
        ],
        "requirements": [
            "Mats rated for falling practice - never learn rolls on hard floors.",
            "A teacher watching the first hundred rolls; head position errors must be caught early.",
            "Loose gi sleeves and a tied belt - clothing that catches the mat ruins the roll line.",
            "Patience: the diagonal path is unnatural at first and takes weeks to feel round.",
        ],
        "standards": [
            "Mae-ukemi follows the Aikikai forward-roll form: diagonal path, tucked chin, bladed hand.",
            "Forward rolls from kneeling and standing are required in kyu gradings.",
            "Silent rolling is the Hombu Dojo quality standard.",
        ],
        "citations": [CIT_AIKIKAI, CIT_WESTBROOK],
        "sig_lens": (
            "The Signature read: the forward roll is the covenant of "
            "receiving - the oath that whatever force arrives will be "
            "accepted, rounded, and returned as motion instead of "
            "injury. Where the public record maps the diagonal, the "
            "Signature lens honors the receiver: ukemi is the armory's "
            "proof that strength includes knowing how to fall."
        ),
    },
    {
        "key": "ukemi_back_side",
        "name": "Ukemi: Ushiro-ukemi and Yoko-ukemi, Back and Side Falls",
        "group": "Movement and Ukemi",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Not every throw rolls forward. Ushiro-ukemi (後ろ受け身) is "
            "the back fall: the body drops low, the chin tucks hard to "
            "the chest so the head never whips into the mat, and the "
            "rounded back meets the mat while both arms slap down at "
            "forty-five degrees to spread the impact. Yoko-ukemi (横受け身) "
            "is the side fall, used when a throw drives you sideways: one "
            "leg sweeps, the body tips as a unit, the lower arm slaps the "
            "mat a hand's width before the body lands, and the head stays "
            "lifted off the mat. The slap (tegatana strike to the mat) is "
            "not theater - it fires the arm muscles to brace the shoulder "
            "and spreads force across the mat instead of into one joint. "
            "These falls protect against the throws that end backward "
            "and sideways - koshinage, jujinage, sumi-otoshi - and every "
            "aikido student drills them until the tuck-and-slap is "
            "faster than the instinct to catch oneself with a straight "
            "arm, which is how wrists break."
        ),
        "how_it_works": (
            "Ushiro-ukemi first. Step one, get low: from standing, bend "
            "the knees deeply - the fall starts from a crouch, which "
            "halves the drop distance. Step two, tuck: drive the chin to "
            "the chest and round the back; the back of the head must never "
            "lead. Step three, sit and slap: sit back onto the mat, and as "
            "the back meets it, both arms slap down at forty-five degrees "
            "from the body, palms flat, exhaling sharply. Step four, "
            "recover: rock forward and stand, facing the partner. For "
            "yoko-ukemi, step one: from hanmi, swing the front leg across "
            "and let the body tip sideways as one rigid-ish line. Step "
            "two: the lower arm slaps the mat just before the body "
            "arrives, at about forty-five degrees. Step three: keep the "
            "head lifted - imagine holding an orange under the chin - so "
            "it never strikes the mat. Step four: the top leg stays ready "
            "to stand. Drills: practice back falls from a squat, then from "
            "standing with a partner gently pulling; practice side falls "
            "from kneeling, then standing. The golden rule both ways: "
            "never post a straight arm to catch yourself - the slap "
            "replaces the post."
        ),
        "key_points": [
            "Ushiro-ukemi (back fall): deep crouch first, chin to chest, rounded back lands as both arms slap at forty-five degrees.",
            "Yoko-ukemi (side fall): body tips as a unit, lower arm slaps just before landing, head stays lifted off the mat.",
            "The slap braces the shoulder and spreads impact - it replaces the deadly instinct to post a straight arm.",
            "Exhale on every fall; held breath makes the body rigid and the landing hard.",
            "Both falls are drilled from low to high: squat/kneeling, then standing, then from real throws.",
        ],
        "requirements": [
            "Mats rated for falling; these falls strike the mat with the whole back or side.",
            "A teacher confirming head position - chin tucked for back falls, lifted for side falls.",
            "No straight-arm posting, ever; the habit must be broken before throws begin.",
            "Both sides for yoko-ukemi; back falls are symmetric but still need repetition.",
        ],
        "standards": [
            "Ushiro-ukemi and yoko-ukemi follow Aikikai falling forms with the forty-five-degree arm slap.",
            "Back and side falls are required elements of kyu grading demonstrations.",
            "The no-posting rule is a universal dojo safety standard.",
        ],
        "citations": [CIT_AIKIKAI, CIT_WESTBROOK],
        "sig_lens": (
            "The Signature read: the back and side falls are the covenant "
            "of the unexpected - the oath that even the fall you did not "
            "choose will be received safely. Where the public record "
            "teaches the slap, the Signature lens hears the promise "
            "inside it: the body swears to protect the head first, the "
            "arm second, and pride never."
        ),
    },
    {
        "key": "kuzushi",
        "name": "Kuzushi: Breaking the Partner's Balance",
        "group": "Core Principles",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Kuzushi (崩し) is breaking balance - the invisible technique "
            "inside every visible one. A standing person is stable only "
            "while their center of mass stays over their base of support "
            "(the feet); move the center past the edge of the base and "
            "gravity finishes the job. Aikido creates kuzushi three ways: "
            "by leading (guiding the partner's committed motion past its "
            "support), by timing (acting in the instant of a step, when "
            "the base is narrowest), and by angle (pushing or pulling "
            "toward the corners, where the base is weakest - never "
            "straight at the strong front-back line). Beginners try to "
            "throw with the arms; experienced students break the balance "
            "first and let the throw happen almost by itself. The classic "
            "drill is simple: partner stands in hanmi, you take the wrist "
            "and practice finding the direction where they feel light - "
            "that light direction is kuzushi, and every technique on this "
            "ladder is a machine for finding it."
        ),
        "how_it_works": (
            "Learn to feel kuzushi before you try to make it. Step one, "
            "the lightness test: partner stands in hanmi; hold the wrist "
            "lightly and lean your weight in the eight compass directions, "
            "slowly. One or two directions will make the partner feel "
            "suddenly light or step involuntarily - memorize those; they "
            "are the corners, the weak angles. Step two, leading: have "
            "the partner walk toward you pushing your hand; instead of "
            "resisting, walk backward guiding the push slightly to their "
            "front corner - their own committed step carries them past "
            "balance. Step three, timing: practice acting exactly as the "
            "partner's foot lifts to step - the base is narrowest mid-"
            "step, and a feather tips what a shove could not. Step four, "
            "stack it: in ikkyo, the entering step plus the arm guide "
            "together create kuzushi before the pin ever starts. Step "
            "five, audit every technique: ask 'where was the balance "
            "broken?' If the answer is 'with muscle at the end,' the "
            "kuzushi was missing and the technique was wrestling. The "
            "rule: balance first, technique second, strength never."
        ),
        "key_points": [
            "Kuzushi means the center of mass has left the base of support - after that, gravity does the throwing.",
            "It is made three ways: leading committed motion past its support, timing action to the stepping instant, and attacking the weak corner angles.",
            "Never push the strong line (straight front-back); the corners are where balance is fragile.",
            "The lightness test - finding where a held partner feels weightless - teaches the hands to recognize kuzushi.",
            "Techniques that end in muscle failed at kuzushi; balance first, technique second, strength never.",
        ],
        "requirements": [
            "A partner willing to stand still and be experimented on - the lightness test needs a honest, relaxed body.",
            "Slow practice speed; kuzushi at full speed is invisible to the learner.",
            "The eight-direction map memorized: know your partner's weak corners from any grip.",
            "An instructor to confirm that what you feel as lightness is real kuzushi, not the partner being polite.",
        ],
        "standards": [
            "Kuzushi is the foundational principle of all budo, formalized in judo and carried into aikido's aiki application.",
            "Balance-breaking before technique is required in Aikikai grading demonstrations.",
            "The corner-weakness (happo-no-kuzushi, eight-direction) model follows classical budo theory.",
        ],
        "citations": [CIT_AIKIKAI, CIT_WESTBROOK, CIT_SHIODA],
        "sig_lens": (
            "The Signature read: kuzushi is the covenant of the lever - "
            "the oath that no force will be met with force when a "
            "well-placed gram will do. Where the public record maps the "
            "eight directions, the Signature lens finds the promise: find "
            "the light direction and the whole armory moves on a "
            "fingertip."
        ),
    },
    {
        "key": "awase_musubi",
        "name": "Awase and Musubi: Blending and Connecting Energy",
        "group": "Core Principles",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Awase (合わせ, blending or matching) and musubi (結び, "
            "tying or connecting) are the contact principles of aikido. "
            "Musubi is the connection itself: the moment of touch - hand "
            "to wrist, forearm to forearm - when two bodies become one "
            "mechanical system and you can feel the partner's balance "
            "through your hands. Awase is what you do with that "
            "connection: match the attack's speed and direction, join it "
            "rather than block it, and then gently lead it where you "
            "want. Without musubi you are guessing; without awase you "
            "are colliding. The training image is water meeting water: "
            "when the partner grabs your wrist, your hand does not "
            "freeze or yank - it stays soft, matches the grab's pressure, "
            "and moves with it, so the grabber finds nothing to fight. "
            "This is why aikido looks effortless at high level: the "
            "expert is never fighting the attack, only joining it and "
            "editing its destination."
        ),
        "how_it_works": (
            "Train connection as a physical sense. Step one, the touch "
            "drill: partner grabs your wrist (katate-dori); close your "
            "eyes and feel - through the hand - which way their weight "
            "leans. Do not move yet; just read. Step two, matching: as "
            "the partner pushes, let your hand ride the push at exactly "
            "its speed - no faster (that is running away), no slower "
            "(that is resisting). Step three, joining: once matched, "
            "add the smallest curve - guide the push ten degrees off "
            "its line while keeping the same speed, and feel the "
            "partner's balance follow your hand. Step four, the water "
            "test: partner grabs and tries to feel where you are "
            "resisting; adjust until they report feeling nothing solid "
            "to fight - that is musubi holding. Step five, apply: in "
            "every technique's first beat, connect before you move the "
            "feet; the feet then serve the connection instead of "
            "abandoning it. Faults: grabbing back (that is a second "
            "fight), going limp (that is disconnection), and moving the "
            "hands before the body (that is arm-wrestling)."
        ),
        "key_points": [
            "Musubi (connection) makes two bodies one mechanical system; awase (blending) matches the attack's speed and direction instead of blocking it.",
            "Connection is a sense: with eyes closed you should be able to read the partner's weight lean through a wrist grab.",
            "Matching speed exactly - neither faster nor slower - is the physical definition of blending.",
            "The water test: a well-connected defender gives the attacker nothing solid to fight.",
            "Connect before moving the feet; the footwork serves the connection, never abandons it.",
        ],
        "requirements": [
            "A partner giving honest, committed grabs - a limp grab teaches nothing about connection.",
            "Slow practice; connection cannot be felt at speed until it is felt slowly.",
            "Soft hands: no grabbing back, no going limp, no leading with the arms.",
            "An instructor to run the water test and confirm when resistance has actually vanished.",
        ],
        "standards": [
            "Awase and musubi follow classical aiki terminology preserved in the Aikikai tradition.",
            "Connection-before-movement is the Hombu Dojo basic instruction for all techniques.",
            "The principle is examined implicitly in every grading: techniques without musubi are marked as muscled.",
        ],
        "citations": [CIT_AIKIKAI, CIT_SAOTOME, CIT_WESTBROOK],
        "sig_lens": (
            "The Signature read: musubi is the covenant of touch - the "
            "oath that contact will be listening before it is leading. "
            "Where the public record describes blending, the Signature "
            "lens seals the promise: the armory's first weapon is an "
            "open, listening hand, and every throw after is just the "
            "conversation continuing."
        ),
    },
    {
        "key": "maai_atemi",
        "name": "Ma-ai: Distance, Timing, and Atemi Openings",
        "group": "Core Principles",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Ma-ai (間合い) is the harmonious distance - the spacing and "
            "timing between you and the partner where both are safe and "
            "both can act. Too close and you are crowded before you move; "
            "too far and your technique arrives late. Aikido trains three "
            "distances: toma (far, one step beyond reach), uchi-ma (striking "
            "distance, where a step lands a blow), and chika-ma (close, "
            "body to body). Controlling ma-ai means you decide when "
            "contact happens. Atemi (当て身, strikes to the body) is "
            "aikido's punctuation: a strike toward the face or ribs that "
            "the partner must respect, which freezes, turns, or unbalances "
            "them and opens the real technique. Atemi is rarely meant to "
            "land - it is a question the attacker's body must answer, and "
            "the answer is kuzushi. O-Sensei is quoted as saying aikido is "
            "seventy percent atemi: without the strike-threat, partners "
            "stand like statues and no real technique is possible."
        ),
        "how_it_works": (
            "Own the distance first. Step one, measure: face a partner in "
            "hanmi; extend your front arm - if your fingertips just miss "
            "their face, that is uchi-ma; one step back is toma; chest to "
            "chest is chika-ma. Memorize all three in the body. Step two, "
            "control: drill stepping from toma to uchi-ma with a single "
            "tsugi-ashi the instant the partner shifts weight - you "
            "arrive as their balance narrows. Step three, the atemi habit: "
            "in every technique's entry, the free hand travels toward the "
            "partner's face at eye level - not to hit, but to demand "
            "attention; watch how the partner's head turns and weight "
            "shifts. Step four, timing (hyoshi): practice entering on "
            "the partner's inhale or mid-step, when reaction is slowest. "
            "Step five, restraint: atemi in training stops short or "
            "touches lightly - the control of the strike matters more "
            "than its power, because a wild atemi destroys the very "
            "connection the technique needs. The rule: distance is yours "
            "to set, timing is yours to steal, and atemi is the key that "
            "unlocks both."
        ),
        "key_points": [
            "Ma-ai (harmonious distance) has three zones: toma (far), uchi-ma (striking distance), chika-ma (close) - and you decide when contact happens.",
            "Atemi (strikes) are punctuation, not the sentence: they freeze, turn, or unbalance the partner to open the real technique.",
            "O-Sensei's quoted ratio - aikido is seventy percent atemi - marks how central the strike-threat is to making technique real.",
            "Timing (hyoshi) means entering on the partner's inhale or mid-step, when their ability to react is weakest.",
            "Training atemi stops short or touches lightly; control of the strike matters more than its power.",
        ],
        "requirements": [
            "A partner who reacts honestly to atemi - freezing or turning - rather than ignoring it.",
            "The three distances memorized in the body, not just named.",
            "Control: the ability to stop a face strike a finger's width short, every time.",
            "An instructor's correction on timing - entering early is as useless as entering late.",
        ],
        "standards": [
            "Ma-ai, atemi, and hyoshi follow standard Aikikai terminology.",
            "The three distance zones are classical budo ma-ai theory.",
            "Atemi control (stopping short) is a universal dojo safety standard.",
        ],
        "citations": [CIT_AIKIKAI, CIT_SHIODA, CIT_WESTBROOK],
        "sig_lens": (
            "The Signature read: ma-ai is the covenant of the threshold - "
            "the oath that you will choose the ground and the moment, "
            "never cede them. Where the public record measures the "
            "zones, the Signature lens keeps the promise: the atemi is "
            "the armory's question, asked politely at eye level, and the "
            "attacker's own answer becomes the opening."
        ),
    },
    {
        "key": "grip_fundamentals",
        "name": "Grip Fundamentals: Katate-dori and Ryote-dori",
        "group": "Core Principles",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Before the wrist controls come the grips they answer. "
            "Katate-dori (片手取り) is a one-hand grab of one wrist - the "
            "most common attack in aikido practice and the laboratory "
            "where beginners learn blending. Ryote-dori (両手取り) is a "
            "two-hands-on-one-wrist grab, stronger and more committed, "
            "demanding whole-body movement rather than hand tricks. "
            "Morote-dori (both wrists grabbed) and kata-dori (shoulder "
            "grab) complete the basic set. The defender's first lesson "
            "is counterintuitive: do not fight the grip. A grab is "
            "information - it tells you exactly where the attacker's "
            "hand, weight, and attention are - and it is also a handle "
            "the attacker has kindly given you. Every grip release on "
            "this ladder works the same way: move the body (not the "
            "wrist) so the grip's strength points at empty space, then "
            "let the technique grow from the freed hand."
        ),
        "how_it_works": (
            "The universal grip answer, drilled first with katate-dori. "
            "Step one, receive: as the partner grabs your right wrist "
            "with their right hand, keep your hand soft and slightly "
            "cupped - a relaxed wrist is a mobile wrist. Step two, move "
            "the body: tenkan - pivot 180 degrees - while letting the "
            "grabbed hand draw a small circle; the grip's force slides "
            "off because your center is no longer where it was aimed. "
            "Step three, the freed hand: as the pivot completes, your "
            "hand is free or the grip is stretched to its weak angle - "
            "from here it becomes ikkyo, nikyo, or a throw entry. For "
            "ryote-dori (two hands on one wrist): step one, drop the "
            "center - sink the hips so the grabbers' pull meets your "
            "weight, not your arm. Step two, tenkan big - the pivot must "
            "be large because two hands commit more of the attacker's "
            "body. Step three, use the freed motion to enter. Rules for "
            "all grips: the wrist never twists itself free (that injures "
            "your own joint), the body always moves first, and the "
            "release is a side effect of footwork - if you are "
            "arm-wrestling the grip, the feet have stopped."
        ),
        "key_points": [
            "Katate-dori (one hand on one wrist) is the laboratory grip; ryote-dori (two hands on one) demands whole-body answers.",
            "Never fight the grip: a grab is information (where the attacker's weight and attention are) and a handle they gave you.",
            "The wrist never twists itself free - the body moves (tenkan) and the release is a side effect of footwork.",
            "Dropping the center answers the strong two-hand grab: the pull meets your weight, not your arm.",
            "If you are arm-wrestling the grip, the feet have stopped - and stopped feet are the real problem.",
        ],
        "requirements": [
            "A partner who grabs sincerely - a loose grab teaches a loose response.",
            "Working tenkan and solid hanmi first; grip answers are footwork, not hand tricks.",
            "Soft grabbed hand: cupped, relaxed, mobile - tension in the wrist locks your own joint.",
            "An instructor watching that the release comes from the pivot, not from yanking.",
        ],
        "standards": [
            "Katate-dori, ryote-dori, morote-dori, and kata-dori follow standard Aikikai attack terminology.",
            "Grip attacks are the standard opening attacks in kyu grading demonstrations.",
            "The no-yanking rule (protecting the defender's own wrist) is a universal safety standard.",
        ],
        "citations": [CIT_AIKIKAI, CIT_WESTBROOK],
        "sig_lens": (
            "The Signature read: the grab is the covenant offered "
            "backward - the attacker hands you a handle on their own "
            "balance and dares you to use it gently. Where the public "
            "record names the grips, the Signature lens accepts the "
            "gift: every grab is a signed promise that the attacker's "
            "strength now has an address, and the feet know how to "
            "deliver the reply."
        ),
    },
    {
        "key": "ikkyo",
        "name": "Ikkyo: Ude-osae, the First Teaching",
        "group": "Wrist Controls: Kyo Waza",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Ikkyo (一教, first teaching), also called ude-osae (腕押さえ, "
            "arm pin), is the first of the kyo (teachings) - the wrist-"
            "control family that forms aikido's core curriculum. Against "
            "a wrist grab or strike, nage controls the attacker's arm at "
            "the elbow and wrist, guides it in a downward arc, and pins "
            "the attacker face-down with the arm stretched behind the "
            "back at a controlled angle. Ikkyo teaches the master pattern "
            "of all five kyo: enter (irimi), take the arm, break the "
            "balance with the whole body, and finish with a pin that "
            "controls without injury. It is practiced in multiple forms - "
            "omote (front, entering directly) and ura (rear, turning) - "
            "against grabs, strikes, and shoulder grabs. Students spend "
            "years on ikkyo because its pin contains the whole art in "
            "miniature: connection, kuzushi, and merciful control."
        ),
        "how_it_works": (
            "Ikkyo omote against katate-dori, step by step. Step one, "
            "atemi and entry: as the partner grabs your wrist, your free "
            "hand rises toward their face (atemi) while you step in with "
            "irimi - your body passes inside their arm. Step two, take "
            "the arm: your free hand comes over their grabbing arm and "
            "grips above their elbow; your grabbed hand turns palm-up "
            "underneath to control their wrist - you now hold the arm at "
            "both ends. Step three, the arc: keeping your arms in a "
            "rounded frame, step through and guide their arm in a downward "
            "arc toward the mat, your hips - not your shoulders - doing "
            "the work; their balance breaks forward and down. Step four, "
            "the pin: as they go face-down, slide your controlling hand "
            "down to pin their wrist while your body weight settles over "
            "their elbow and shoulder - the arm rests stretched behind "
            "the back at a natural angle, never forced. Step five, hold "
            "with presence: kneel beside them, maintain the pin with "
            "body weight, and keep your eyes up (zanshin). For ura form, "
            "replace the irimi entry with tenkan and guide the same arc "
            "from the turning side. The pin must be painless when the "
            "partner is still - pain is the alarm, not the goal."
        ),
        "key_points": [
            "Ikkyo (ude-osae) is the first teaching: control the arm at elbow and wrist, arc it down, pin face-down with the arm naturally behind the back.",
            "The master pattern of all five kyo: enter, take the arm at both ends, break balance with the hips, pin with body weight.",
            "Omote (front/entering) and ura (rear/turning) forms teach the same control from both irimi and tenkan entries.",
            "The pin is held with settled body weight and zanshin (remaining awareness) - pain is the alarm, never the goal.",
            "Years are spent on ikkyo because it contains the whole art in miniature: connection, kuzushi, merciful control.",
        ],
        "requirements": [
            "Reliable ukemi from the partner - ikkyo ends face-down and the fall must be safe.",
            "Working irimi and tenkan entries; ikkyo is footwork with an arm attached.",
            "A teacher setting the pin angle - the shoulder's safe range must be learned by feel, not guessed.",
            "Slow practice until the arc is smooth; speed with a locked elbow injures shoulders.",
        ],
        "standards": [
            "Ikkyo/ude-osae and the omote/ura forms follow the Aikikai kyo-waza syllabus.",
            "The five kyo sequence (ikkyo through gokyo) is the traditional teaching order.",
            "Pin safety - natural joint angles, body-weight control - is examined in kyu and dan gradings.",
        ],
        "citations": [CIT_AIKIKAI, CIT_UESHIBA, CIT_WESTBROOK],
        "sig_lens": (
            "The Signature read: ikkyo is the first covenant signed in "
            "the armory - the oath that control will be complete and "
            "harm will be zero. Where the public record teaches the arc, "
            "the Signature lens frames the pin as the honor hold in its "
            "purest form: the attacker face-down, the arm held like "
            "something precious, the whole art keeping its oldest "
            "promise."
        ),
    },
    {
        "key": "nikyo",
        "name": "Nikyo: Kote-mawashi, the Second Teaching",
        "group": "Wrist Controls: Kyo Waza",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Nikyo (二教, second teaching), also called kote-mawashi "
            "(小手回し, wrist turn), bends the wrist inward toward the "
            "forearm while twisting, creating a lock that travels up "
            "through the elbow to the shoulder. Where ikkyo controls the "
            "whole arm in an arc, nikyo concentrates on the wrist joint "
            "itself: the defender's hands form a precise grip that folds "
            "the attacker's hand back toward their own forearm, and the "
            "resulting pressure forces the attacker down - resisting "
            "tightens the lock on one's own joint. Nikyo is famous as "
            "the 'come-along' control used in law-enforcement and "
            "security work, because it can move a resisting person with "
            "minimal force once the lock is set. Like ikkyo it has omote "
            "and ura forms, and it is almost always finished with the "
            "same face-down pin. The teaching point of nikyo is precision: "
            "a finger's width of hand placement is the difference between "
            "effortless control and a wrestling match."
        ),
        "how_it_works": (
            "Nikyo against katate-dori, step by step. Step one, entry: "
            "tenkan as the grab lands, your free hand rising to meet the "
            "grabbing hand. Step two, the grip: your free hand takes "
            "their hand from the pinky side, fingers wrapping their "
            "palm-edge while your grabbed hand turns to support from "
            "below - the classic nikyo hand shape is like holding a "
            "sword hilt across their knuckles. Step three, the fold: "
            "keeping their elbow guided downward with your body, bend "
            "their wrist so the back of their hand folds toward their "
            "forearm while rotating slightly - the lock engages when the "
            "wrist reaches the edge of its range. Step four, the "
            "descent: step through with the hips, drawing the locked "
            "wrist in a downward spiral; the attacker folds down to "
            "protect the joint - follow, do not push. Step five, the "
            "pin: settle into the standard face-down pin, maintaining "
            "the wrist fold with gentle, constant pressure. Critical "
            "safety: apply the lock slowly - wrists give little warning "
            "before injury, and the partner taps the mat (or your leg) "
            "to signal the limit. Never crank; the lock should feel "
            "inevitable, not violent."
        ),
        "key_points": [
            "Nikyo (kote-mawashi) folds the wrist inward toward the forearm with a twist; the lock travels wrist to elbow to shoulder.",
            "It is the classic come-along control: once set, minimal force moves a resisting person - the basis of its security and law-enforcement use.",
            "Hand placement precision is everything: a finger's width decides between effortless control and wrestling.",
            "Applied slowly - wrists give little warning before injury; the partner's tap is the absolute limit signal.",
            "Finished with the standard face-down pin, maintaining the wrist fold with gentle constant pressure.",
        ],
        "requirements": [
            "A partner who taps early and honestly - wrist locks demand the clearest communication in the dojo.",
            "Slow, supervised practice until the hand shape is exact; speed comes only after precision.",
            "Working tenkan entry; nikyo without the turn becomes a strength contest at the wrist.",
            "Knowledge of the tap signal and the rule: the tap ends the technique instantly, no exceptions.",
        ],
        "standards": [
            "Nikyo/kote-mawashi follows the Aikikai kyo-waza syllabus as the second teaching.",
            "Wrist-lock safety - slow application, tap-to-release - is a universal dojo standard.",
            "The come-along application follows documented defensive-tactics use of nikyo variants.",
        ],
        "citations": [CIT_AIKIKAI, CIT_WESTBROOK, CIT_SHIODA],
        "sig_lens": (
            "The Signature read: nikyo is the covenant of precision - "
            "the oath that a finger's width of placement replaces a "
            "hundred pounds of force. Where the public record teaches "
            "the fold, the Signature lens honors the economy: the "
            "armory's smallest key opens the heaviest door, and the "
            "lock asks permission (the tap) before it ever insists."
        ),
    },
    {
        "key": "sankyo",
        "name": "Sankyo: Kote-hineri, the Third Teaching",
        "group": "Wrist Controls: Kyo Waza",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Sankyo (三教, third teaching), also called kote-hineri "
            "(小手捻り, wrist twist), spirals the wrist: the attacker's "
            "hand is turned palm-up and rotated outward while the elbow "
            "is guided up, winding the whole arm into a corkscrew lock. "
            "Where nikyo folds the wrist inward, sankyo twists it "
            "outward and upward - the pain and control run along a "
            "spiral path from wrist through elbow to shoulder, and the "
            "attacker rises onto tiptoes or folds down depending on the "
            "spiral's direction. Sankyo is the most three-dimensional of "
            "the kyo: it lifts as much as it presses, which makes it "
            "excellent against larger attackers because the spiral uses "
            "their height against them. It finishes, like its siblings, "
            "in the face-down pin. The teaching point of sankyo is the "
            "spiral: beginners try to twist the wrist in place (which "
            "fights the joint), while the real lock comes from rotating "
            "the whole arm as one piece around its own axis."
        ),
        "how_it_works": (
            "Sankyo against katate-dori, step by step. Step one, entry: "
            "irimi or tenkan as the grab lands, meeting the grabbing "
            "hand with your free hand. Step two, the grip: take their "
            "hand with both of yours in the sankyo hold - your hands "
            "stack on their hand like wringing a cloth, their palm "
            "turning upward. Step three, the spiral: keeping their elbow "
            "pointed down and guided by your body, rotate their hand "
            "outward and upward as one piece - think of turning a "
            "doorknob the size of their whole arm - while you step "
            "through with the hips. Step four, direction: spiral upward "
            "to lift the attacker onto tiptoes (for control and movement) "
            "or spiral downward to fold them to the mat (for the pin); "
            "the elbow must never be forced past its natural range. Step "
            "five, the pin: guide the spiral down into the standard "
            "face-down pin, keeping the wrist twist with gentle pressure. "
            "Safety is paramount: the spiral must rotate the whole arm "
            "as a unit - twisting the wrist while the elbow is fixed "
            "injures the wrist, and lifting the elbow too high injures "
            "the shoulder. Slow, supervised, tap-respected, always."
        ),
        "key_points": [
            "Sankyo (kote-hineri) spirals the whole arm: palm turns up, hand rotates outward, elbow guided - a corkscrew lock wrist to shoulder.",
            "The spiral can lift (attacker rises to tiptoes for control) or fold down (for the pin); the elbow's natural range is never forced.",
            "Rotate the whole arm as one piece around its axis - twisting the wrist in place fights the joint and injures it.",
            "Excellent against larger attackers: the upward spiral uses their height against them.",
            "Slow, supervised, tap-respected - shoulder and wrist safety depend on the spiral staying unified.",
        ],
        "requirements": [
            "A partner who taps early; the spiral lock engages across two joints at once.",
            "An instructor setting the spiral - the unified rotation cannot be learned from description alone.",
            "Working entries (irimi and tenkan); sankyo's grip must be taken on a moving, unbalanced arm.",
            "The discipline to rotate the whole arm, never to twist the wrist against a fixed elbow.",
        ],
        "standards": [
            "Sankyo/kote-hineri follows the Aikikai kyo-waza syllabus as the third teaching.",
            "The whole-arm spiral (never isolated wrist twist) is the Hombu Dojo safety standard.",
            "Finished in the standard face-down pin per the kyo-waza convention.",
        ],
        "citations": [CIT_AIKIKAI, CIT_WESTBROOK],
        "sig_lens": (
            "The Signature read: sankyo is the covenant of the spiral - "
            "the oath that force will travel the long, winding road "
            "rather than the short, breaking one. Where the public "
            "record teaches the twist, the Signature lens follows the "
            "corkscrew: the armory winds the attacker's strength around "
            "itself until strength itself asks for the mat."
        ),
    },
    {
        "key": "yonkyo",
        "name": "Yonkyo: Tekubi-osae, the Fourth Teaching",
        "group": "Wrist Controls: Kyo Waza",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Yonkyo (四教, fourth teaching), also called tekubi-osae "
            "(手首押さえ, wrist press), is the pressure-point lock of the "
            "kyo family. The defender's knuckles press into the soft "
            "tissue on the inner wrist - over the radial nerve area - "
            "while the wrist is bent back, creating an intense, precise "
            "pressure that drops the attacker without large movement. "
            "Unlike its siblings, yonkyo's effectiveness varies with "
            "anatomy: the exact nerve location differs slightly person "
            "to person, so part of learning yonkyo is learning to find "
            "the spot on each partner. Traditional teaching holds that "
            "yonkyo works through the body's meridian/pressure-point "
            "map, and modern students simply note that pressing the "
            "right square centimeter of the inner wrist produces a "
            "disproportionate control effect. It shares the omote/ura "
            "entries and the face-down pin finish of the family. The "
            "teaching point of yonkyo is subtlety: it rewards the "
            "student who has stopped muscling and started feeling."
        ),
        "how_it_works": (
            "Yonkyo against katate-dori, step by step. Step one, entry: "
            "tenkan or irimi as the grab lands, taking the grabbing hand "
            "as in nikyo. Step two, locate: with the base knuckles of "
            "your gripping hand, find the soft hollow on the inner "
            "(palm-side) wrist, slightly toward the thumb side - press "
            "gently and watch the partner's face; the right spot announces "
            "itself. Step three, the press and bend: drive the knuckles "
            "into the spot while bending their wrist back toward their "
            "forearm, keeping their elbow guided down with your body. "
            "Step four, the descent: step through with the hips, letting "
            "the pressure steer the attacker down in a tight spiral - "
            "yonkyo needs very little motion, so keep the movement small "
            "and let the pressure do the work. Step five, the pin: "
            "settle into the face-down pin, maintaining knuckle pressure "
            "with the wrist bent. Calibration matters: too little "
            "pressure and nothing happens; too much and you bruise the "
            "tissue. Practice finding the spot on many partners - "
            "anatomy varies, and the technique is the search as much as "
            "the press. Tap respected instantly, as with all kyo."
        ),
        "key_points": [
            "Yonkyo (tekubi-osae) presses the knuckles into the inner wrist's soft tissue while bending the wrist back - a pressure-point lock.",
            "Effectiveness varies with anatomy; finding the exact spot on each partner is part of the technique.",
            "It needs very little motion - the pressure does the work, so keep the movement small and precise.",
            "It rewards feeling over muscling: the student who has stopped forcing is the one yonkyo starts working for.",
            "Calibrate pressure carefully - too little does nothing, too much bruises tissue; the tap ends it instantly.",
        ],
        "requirements": [
            "Many different partners - the spot's location varies person to person and must be learned by searching.",
            "A light, precise touch; yonkyo punishes the heavy-handed with bruised partners and failed locks.",
            "The nikyo hand-shape foundation; yonkyo's grip grows from the same family.",
            "An instructor confirming the pressure point location on each new partner.",
        ],
        "standards": [
            "Yonkyo/tekubi-osae follows the Aikikai kyo-waza syllabus as the fourth teaching.",
            "Pressure-point safety - calibrated pressure, instant tap release - is a universal dojo standard.",
            "Finished in the standard face-down pin per the kyo-waza convention.",
        ],
        "citations": [CIT_AIKIKAI, CIT_WESTBROOK, CIT_SAOTOME],
        "sig_lens": (
            "The Signature read: yonkyo is the covenant of the small "
            "spot - the oath that the tiniest true point outweighs the "
            "largest false effort. Where the public record maps the "
            "pressure point, the Signature lens keeps the vow of "
            "subtlety: the armory's quietest key, turned by the "
            "listening hand, opens what force cannot."
        ),
    },
    {
        "key": "gokyo",
        "name": "Gokyo: Ude-nobashi, the Fifth Teaching",
        "group": "Wrist Controls: Kyo Waza",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Gokyo (五教, fifth teaching), also called ude-nobashi "
            "(腕伸ばし, arm stretch), completes the kyo family. It "
            "resembles ikkyo's arm control but with a reversed grip "
            "that stretches the arm straight while rotating it - "
            "originally developed as the answer to a knife-hand "
            "attack, where grabbing the attacker's wrist the ikkyo way "
            "would pull your hand across the blade. The reversed grip "
            "keeps the defender's hands clear while still taking the "
            "arm at both ends, arcing it down, and finishing in the "
            "familiar face-down pin. Gokyo's lesson is adaptability: "
            "the same body mechanics as ikkyo, re-gripped for a "
            "different danger. Students usually meet gokyo late among "
            "the five because its value only becomes clear once ikkyo "
            "is instinctive - then the reversed grip reads as a single "
            "intelligent variation rather than a new technique. With "
            "gokyo, the wrist-control ladder is complete: five "
            "teachings, one pin, and a full vocabulary for any arm "
            "that reaches you."
        ),
        "how_it_works": (
            "Gokyo against a wrist grab or strike, step by step. Step "
            "one, entry: irimi as the attack comes, exactly as for "
            "ikkyo - the footwork does not change. Step two, the "
            "reversed grip: instead of ikkyo's over-the-elbow hand, "
            "your hand slides under and around so the palms face "
            "opposite - the grip stretches the attacker's arm straight "
            "rather than folding it, and your hands stay on the safe "
            "side of a hypothetical blade line. Step three, the arc: "
            "as in ikkyo, step through with the hips and guide the "
            "extended arm in a downward arc - the straight arm gives "
            "you a longer lever, so the kuzushi arrives even earlier. "
            "Step four, the pin: settle into the standard face-down "
            "pin, controlling the stretched arm with the reversed grip "
            "maintained. Step five, the contrast drill: practice ikkyo "
            "then gokyo alternately against the same attack and feel "
            "how the footwork and arc are identical while only the "
            "hands change - that sameness is the lesson. Safety note: "
            "the straight-arm lever is powerful; guide it, never snap "
            "it, and keep the elbow's natural range sacred."
        ),
        "key_points": [
            "Gokyo (ude-nobashi) is ikkyo's body mechanics with a reversed grip - developed to answer blade attacks without crossing the blade line.",
            "The reversed grip stretches the arm straight, giving a longer lever and earlier kuzushi.",
            "Its lesson is adaptability: same footwork, same arc, re-gripped hands for a different danger.",
            "Usually learned last of the five because it reads as one intelligent variation once ikkyo is instinctive.",
            "The straight-arm lever is powerful - guide it, never snap it; the elbow's natural range is sacred.",
        ],
        "requirements": [
            "Instinctive ikkyo first - gokyo is a variation, not a starting point.",
            "A partner simulating the knife-hand attack line so the reversed grip's purpose is visible.",
            "Careful elbow-range awareness; the extended lever multiplies both control and risk.",
            "The contrast drill (ikkyo/gokyo alternating) to lock in the shared body mechanics.",
        ],
        "standards": [
            "Gokyo/ude-nobashi follows the Aikikai kyo-waza syllabus as the fifth teaching.",
            "The blade-aware origin is preserved in traditional weapons-takings instruction.",
            "Finished in the standard face-down pin per the kyo-waza convention.",
        ],
        "citations": [CIT_AIKIKAI, CIT_UESHIBA, CIT_WESTBROOK],
        "sig_lens": (
            "The Signature read: gokyo is the covenant of the second "
            "answer - the oath that the art keeps a variation ready for "
            "the danger the first answer cannot touch. Where the public "
            "record reverses the grip, the Signature lens honors the "
            "foresight: the armory stocks two keys for one door, because "
            "the blade line deserves its own respect."
        ),
    },
    {
        "key": "irimi_nage",
        "name": "Irimi-nage: The Entering Throw",
        "group": "Throws: Nage Waza",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Irimi-nage (入り身投げ, entering throw) is aikido's signature "
            "throw: nage enters straight through the attack (irimi), one "
            "hand guiding the attacker's head or neck while the body "
            "drives past, and the attacker is thrown backward over nage's "
            "entering motion. It looks like walking through a door the "
            "attacker was guarding - by the time they react, nage is "
            "already past and their balance is gone. The classic form "
            "answers a face strike (shomen-uchi): nage steps in beside "
            "the strike, the guiding hand meets the attacker's chin or "
            "neck, and the hips drive forward as the hand draws a "
            "downward arc. Irimi-nage teaches the purest lesson of the "
            "art: the throw is not done to the partner, it is done by "
            "the entry - the partner simply runs out of balance to stand "
            "on. It demands good ukemi, because the fall is backward and "
            "committed."
        ),
        "how_it_works": (
            "Irimi-nage omote against shomen-uchi (overhead face strike), "
            "step by step. Step one, the entry: as the strike falls, step "
            "in deep with irimi to the attacker's blind side - your body "
            "passes inside the striking arm, hips leading, head staying "
            "back from the strike line. Step two, the guide: your front "
            "hand rises to meet the attacker's chin, jaw, or the side of "
            "the neck - a guiding touch, fingers together, never a shove "
            "or a grab. Step three, the drive: keep walking - the back "
            "leg drives, the hips surge forward, and the guiding hand "
            "draws a smooth downward arc; do not stop to 'throw,' because "
            "stopping breaks the kuzushi. Step four, the release: as the "
            "attacker's balance tips backward past their heels, let the "
            "guiding hand continue its arc - they fall backward into "
            "ushiro-ukemi. Step five, zanshin: finish facing the fallen "
            "partner, balanced, hands ready. Common faults: grabbing the "
            "neck (that is wrestling), stopping the feet to muscle the "
            "throw (that kills the entry), and leaning the head into the "
            "strike (keep the head back - the hips enter, not the face)."
        ),
        "key_points": [
            "Irimi-nage throws by entry: step through the attack to the blind side, guide the head or neck in a downward arc, and keep walking.",
            "The throw is done by the entry, not to the partner - they run out of balance to stand on.",
            "The guiding hand touches the chin, jaw, or neck softly - never grabs, never shoves.",
            "Stopping the feet to muscle the throw kills it; the back leg drives continuously through the technique.",
            "The fall is backward and committed - the partner needs reliable ushiro-ukemi before this is practiced at speed.",
        ],
        "requirements": [
            "Deep, committed irimi - a shallow entry leaves you in the strike zone.",
            "A partner with solid back-fall ukemi; the throw lands the attacker on their back.",
            "The guiding touch: fingers together, contact but no grab, practiced slowly first.",
            "Head discipline: the hips enter while the head stays back from the strike line.",
        ],
        "standards": [
            "Irimi-nage follows the Aikikai nage-waza syllabus in omote and ura forms.",
            "The shomen-uchi entry is the classical teaching form.",
            "Backward-fall ukemi proficiency is the safety prerequisite for full-speed practice.",
        ],
        "citations": [CIT_AIKIKAI, CIT_UESHIBA, CIT_WESTBROOK],
        "sig_lens": (
            "The Signature read: irimi-nage is the covenant of the open "
            "door - the oath that the way through is forward, never "
            "around, and the only thing thrown is the attacker's "
            "certainty. Where the public record teaches the entry, the "
            "Signature lens walks it: the armory's front door is a "
            "walking step, and balance is the toll."
        ),
    },
    {
        "key": "shiho_nage",
        "name": "Shihonage: The Four-Direction Throw",
        "group": "Throws: Nage Waza",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Shiho-nage (四方投げ, four-direction throw) is named for the "
            "legend that it can throw in all four directions. Against a "
            "wrist grab, nage turns the attacker's wrist as in a sword "
            "cut, pivots (tenkan) under the raised arm, and throws the "
            "attacker by guiding the locked wrist in a great vertical "
            "circle - the attacker falls where the circle completes. It "
            "is the most visibly spectacular aikido throw and one of the "
            "most instructive: the wrist turn must be exact (the 'sword' "
            "must cut truly), the pivot must pass fully under the arm "
            "(half a tenkan strands you), and the throw's circle must "
            "stay vertical (a tilted circle becomes a shoulder wrench). "
            "Shiho-nage appears against nearly every basic attack - "
            "grabs, strikes, shoulder grabs - which is why it anchors the "
            "middle of the ladder: learn its circle and you own a throw "
            "for any arm that reaches you."
        ),
        "how_it_works": (
            "Shiho-nage against katate-dori, step by step. Step one, the "
            "sword hand: as the partner grabs your wrist, raise your "
            "grabbed hand like drawing a sword - fingers together, thumb "
            "tucked - turning their wrist so their palm faces up and "
            "their arm extends. Step two, the turn: step back and tenkan "
            "fully, pivoting under their raised arm until you face the "
            "same direction they do, your joined hands high - you have "
            "passed under the bridge. Step three, the circle: keeping "
            "their wrist locked in the sword-turn, step forward and cut "
            "downward in a great vertical circle, your hips driving the "
            "motion; their body follows the locked wrist over and down. "
            "Step four, the finish: complete the circle to the mat - the "
            "attacker takes a forward roll or breakfall at the circle's "
            "end. Step five, the pin option: instead of releasing into "
            "the throw, keep the wrist and settle into the kneeling pin "
            "with the arm folded. Faults that injure: an incomplete "
            "tenkan (your head stays under their arm - dangerous), a "
            "tilted circle (torques the shoulder sideways), and cranking "
            "the wrist turn with the hands instead of the body."
        ),
        "key_points": [
            "Shiho-nage (four-direction throw) locks the wrist with a sword-like turn, pivots fully under the raised arm, and throws along a great vertical circle.",
            "The tenkan must complete - half a pivot strands your head under their arm, which is dangerous.",
            "The circle stays vertical; a tilted circle becomes a shoulder wrench instead of a throw.",
            "Answers nearly every basic attack - grabs, strikes, shoulder grabs - making it the ladder's middle anchor.",
            "The pin option (kneeling, arm folded) teaches the same lock as a control instead of a throw.",
        ],
        "requirements": [
            "A complete tenkan - the pivot-under is the technique's most safety-critical inch.",
            "The sword-hand shape: fingers together, thumb tucked, wrist turn driven by the body.",
            "A partner with committed forward-roll ukemi for the full-circle finish.",
            "An instructor checking the circle's verticality before any speed is added.",
        ],
        "standards": [
            "Shiho-nage follows the Aikikai nage-waza syllabus against grabs, strikes, and kata-dori.",
            "The vertical cutting circle follows the sword-cut (ken) model of Hombu Dojo instruction.",
            "Full-pivot completion is a universal safety standard for this throw.",
        ],
        "citations": [CIT_AIKIKAI, CIT_UESHIBA, CIT_WESTBROOK],
        "sig_lens": (
            "The Signature read: shiho-nage is the covenant of the full "
            "circle - the oath that the pivot will be completed, the cut "
            "will be true, and no half-measure will stand under a raised "
            "arm. Where the public record teaches the four directions, "
            "the Signature lens draws the circle: the armory's compass "
            "has no unfinished arcs."
        ),
    },
    {
        "key": "kotegaeshi",
        "name": "Kotegaeshi: The Wrist Turn-Back Throw",
        "group": "Throws: Nage Waza",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Kotegaeshi (小手返し, wrist turn-back) is the throw form of "
            "the wrist twist: nage turns the attacker's wrist outward "
            "and back on itself - as if turning it inside out - while "
            "stepping through, and the attacker is thrown in a tight "
            "spiral to the mat. It is one of aikido's most famous "
            "techniques and one of its most delicate: the same twist "
            "that throws effortlessly will injure the wrist if applied "
            "with a snap instead of a spiral. Kotegaeshi typically "
            "answers punches and grabs - the classic form meets a "
            "straight punch (tsuki), blends with tenkan, and turns the "
            "punching wrist back on its own arm. The teaching point is "
            "the spiral path: the wrist travels a smooth corkscrew, "
            "never a sudden kink, and the throw happens because the "
            "attacker's body follows the wrist to protect it. Done "
            "right, the partner seems to pour themselves onto the mat."
        ),
        "how_it_works": (
            "Kotegaeshi against tsuki (straight punch), step by step. "
            "Step one, blend: as the punch comes, tenkan off its line, "
            "your front hand meeting the punching wrist softly - parry "
            "with the body, not the hand. Step two, the hold: take the "
            "wrist with both hands in the kotegaeshi grip - one hand on "
            "the wrist, the other cupping their hand, thumbs clear of "
            "pressure points. Step three, the spiral: keeping their "
            "elbow guided downward, turn their hand outward and back "
            "toward their own forearm in a smooth corkscrew - imagine "
            "turning a key in a lock the size of their arm. Step four, "
            "step through: as the spiral tightens, step forward with "
            "the hips, drawing the locked wrist down and across; the "
            "attacker spirals to the mat to protect the wrist - follow "
            "the fall, do not push it. Step five, the pin: keep the "
            "wrist turn and settle into the kneeling pin with gentle "
            "pressure. Safety is the whole technique: the spiral must "
            "be smooth and continuous - any snap or kink at speed "
            "injures the wrist joint. Practice slowly until the "
            "corkscrew path is glassy, and respect the tap absolutely."
        ),
        "key_points": [
            "Kotegaeshi (wrist turn-back) throws by spiraling the wrist outward and back on itself while stepping through.",
            "The wrist travels a smooth corkscrew, never a sudden kink - the spiral is the entire safety of the technique.",
            "Classically answers the straight punch (tsuki): blend with tenkan, take the punching wrist, turn it back.",
            "The attacker falls to protect the wrist - follow the fall, never push it.",
            "Finishes in the kneeling pin with the wrist turn maintained under gentle pressure.",
        ],
        "requirements": [
            "Glass-smooth spiral mechanics at slow speed before any pace is added - snapping injures wrists.",
            "A partner who taps at the first wrist pressure; the lock gives less warning than it seems.",
            "Working tenkan blend; the punch must be joined before its wrist can be taken.",
            "An instructor verifying the corkscrew path - the kink fault must be caught early.",
        ],
        "standards": [
            "Kotegaeshi follows the Aikikai nage-waza syllabus, classically against tsuki.",
            "The smooth-spiral (no-snap) rule is a universal wrist-safety standard.",
            "The kneeling pin finish follows the standard katame-waza convention.",
        ],
        "citations": [CIT_AIKIKAI, CIT_WESTBROOK, CIT_SHIODA],
        "sig_lens": (
            "The Signature read: kotegaeshi is the covenant of the "
            "returned wrist - the oath that the hand which struck will "
            "be guided home gently, turned back like a page rather than "
            "torn. Where the public record teaches the corkscrew, the "
            "Signature lens keeps the promise of smoothness: the armory "
            "never snaps what it can spiral."
        ),
    },
    {
        "key": "jujinage",
        "name": "Jujinage: The Crossed-Arms Throw",
        "group": "Throws: Nage Waza",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Juji-nage (十字投げ, cross throw), commonly called jujinage, "
            "crosses the attacker's arms into an X (the kanji for ten, "
            "十) and throws along the crossed structure. Against a "
            "two-hand grab (ryote-dori) or a strike, nage gathers both "
            "of the attacker's arms, crosses them at the wrists, and "
            "steps through - the crossed arms lock each other, and the "
            "attacker, unable to uncross without breaking structure, is "
            "thrown forward over the lock. It is a beautiful lesson in "
            "using the attacker's own body as the locking mechanism: no "
            "joint is forced, because the arms imprison each other. "
            "Jujinage demands precise arm geometry - the cross must be "
            "true, wrists stacked, elbows guided down - or the attacker "
            "simply unfolds and walks out. When the geometry is right, "
            "the throw feels like tipping a crossed gate."
        ),
        "how_it_works": (
            "Jujinage against ryote-dori, step by step. Step one, drop "
            "and gather: as both wrists are grabbed, sink the hips and "
            "bring your hands together in front of your center, drawing "
            "the attacker's hands toward each other. Step two, the "
            "cross: guide their right wrist over their left (or the "
            "reverse - pick the cross that their grab suggests), "
            "stacking the wrists so the arms form a clean X with their "
            "elbows pointing down. Step three, lock the structure: "
            "press your hands gently down the crossed line - their arms "
            "now brace against each other and cannot unfold without "
            "their own elbows colliding. Step four, step through: enter "
            "with irimi or turn with tenkan, driving your center forward "
            "along the crossed arms' line; the attacker, locked in their "
            "own X, tips forward over the structure into a forward roll "
            "or breakfall. Step five, follow: keep the crossed wrists "
            "guided to the mat - releasing early lets the arms unfold "
            "mid-fall. Faults: a loose cross (wrists not stacked lets "
            "them slip out), lifting the elbows (breaks the lock), and "
            "throwing with the arms instead of stepping through with "
            "the hips."
        ),
        "key_points": [
            "Juji-nage crosses the attacker's arms into an X (十) at the wrists; the crossed arms lock each other - no joint is forced.",
            "The cross must be true: wrists stacked, elbows guided down, or the attacker simply unfolds.",
            "The throw is a step-through with the hips along the crossed line - tipping a crossed gate, not muscling arms.",
            "Classically answers ryote-dori (two-hand grab) and committed strikes.",
            "Keep the crossed wrists guided to the mat; releasing early lets the structure unfold mid-fall.",
        ],
        "requirements": [
            "Exact arm geometry - the stacked-wrist X must be learned by feel with an instructor's hands-on correction.",
            "A partner who commits to the grab; a half-hearted ryote-dori never forms the cross.",
            "Forward-roll ukemi from the partner for the tipping finish.",
            "Hip-driven stepping; arm-only attempts fail and teach bad habits.",
        ],
        "standards": [
            "Juji-nage follows the Aikikai nage-waza syllabus against ryote-dori and strikes.",
            "The crossed-arm (juji) structure follows classical jujutsu locking theory.",
            "Forward-fall ukemi is the safety prerequisite for the full throw.",
        ],
        "citations": [CIT_AIKIKAI, CIT_WESTBROOK],
        "sig_lens": (
            "The Signature read: jujinage is the covenant of the crossed "
            "gate - the oath that the attacker's own structure will be "
            "the only lock required. Where the public record teaches the "
            "X, the Signature lens admires the economy: the armory "
            "builds no cage when the visitor brings their own bars."
        ),
    },
    {
        "key": "kaiten_nage",
        "name": "Kaiten-nage: The Rotary Throw",
        "group": "Throws: Nage Waza",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Kaiten-nage (回転投げ, rotary throw) spins the attacker "
            "like a wheel: nage takes the attacking arm, turns it in a "
            "great vertical wheel (uchi-kaiten, inner rotation, or "
            "soto-kaiten, outer rotation), and the attacker rolls over "
            "the turning arm to the mat. The classic form answers a "
            "shoulder grab or strike from behind the arm - nage steps "
            "in, the arm is wound into the wheel, and one more turn "
            "pours the attacker forward. Kaiten-nage is the throw that "
            "most clearly shows aikido's rotary soul: everything is "
            "circles, and the circle does the work while the muscles "
            "merely suggest. It has a famous standing finish - the "
            "attacker can be brought back up into a standing arm lock "
            "instead of thrown - which makes it a favorite for "
            "demonstrations of control without damage. The wheel must "
            "stay round and vertical; an oval wheel wrenches the "
            "shoulder."
        ),
        "how_it_works": (
            "Uchi-kaiten-nage against kata-dori (shoulder grab), step by "
            "step. Step one, enter: as the hand lands on your shoulder, "
            "step in with irimi, your near hand rising inside their arm. "
            "Step two, wind the wheel: take their wrist and begin turning "
            "it in a vertical circle in front of you - their arm winds "
            "around like a wheel rolling forward, elbow guided, never "
            "forced. Step three, complete the rotation: keep the wheel "
            "round and vertical, stepping with it; the attacker's body "
            "is drawn over the turning arm as the circle completes. Step "
            "four, the throw: as the wheel comes down, guide it to the "
            "mat - the attacker rolls forward over the wheel's line. "
            "Step five, the standing option: instead of completing the "
            "throw, stop the wheel at its top with the arm wound and "
            "hold - the attacker stands locked, controlled without a "
            "fall. Faults: an oval or tilted wheel (shoulder danger), "
            "winding with the hands instead of stepping with the body "
            "(arm-wrestling), and rushing the wind-up (the partner needs "
            "time to follow the circle safely)."
        ),
        "key_points": [
            "Kaiten-nage (rotary throw) winds the attacking arm in a great vertical wheel (uchi inner or soto outer rotation) and pours the attacker over it.",
            "The wheel must stay round and vertical - an oval or tilted wheel wrenches the shoulder.",
            "The famous standing finish stops the wheel at its top: the attacker stands locked, controlled without a fall.",
            "It most clearly shows aikido's rotary soul: circles do the work, muscles merely suggest.",
            "Wind with the stepping body, never with the hands alone - hand-winding is arm-wrestling.",
        ],
        "requirements": [
            "A round, vertical wheel learned slowly - the shoulder's safety lives in the circle's shape.",
            "A partner who follows the wheel at its speed; rushing the wind-up strands the partner mid-circle.",
            "Working irimi entry to get inside the grabbing arm.",
            "An instructor's eye on wheel geometry before the standing-lock finish is attempted.",
        ],
        "standards": [
            "Kaiten-nage (uchi/soto) follows the Aikikai nage-waza syllabus against grabs and strikes.",
            "The vertical-wheel model follows Hombu Dojo rotary-throw instruction.",
            "Shoulder-safe circle geometry is a universal safety standard.",
        ],
        "citations": [CIT_AIKIKAI, CIT_WESTBROOK, CIT_SAOTOME],
        "sig_lens": (
            "The Signature read: kaiten-nage is the covenant of the "
            "wheel - the oath that every attack will be given a perfect "
            "circle to travel and a soft place to arrive. Where the "
            "public record teaches the rotation, the Signature lens "
            "keeps it round: the armory's wheel never wobbles, and the "
            "standing finish proves control needs no crash."
        ),
    },
    {
        "key": "sumi_otoshi",
        "name": "Sumi-otoshi: The Corner Drop",
        "group": "Throws: Nage Waza",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Sumi-otoshi (隅落とし, corner drop) is the minimalist throw: "
            "nage guides the attacker's balance to a corner - the weak "
            "diagonal angle - and simply lets them fall there, with "
            "almost no visible technique. Against a wrist grab, nage "
            "steps to the attacker's front corner while drawing the "
            "grabbed hand across, and the attacker drops as if the floor "
            "tilted. It looks like nothing, which is exactly the point: "
            "sumi-otoshi is pure kuzushi made visible, the throw with "
            "the technique removed. Because there is so little to hold "
            "onto, it is also the throw that most exposes muscling - if "
            "you push, it is not sumi-otoshi. Students practice it to "
            "calibrate their kuzushi sense: when you can drop a partner "
            "with a step and a hand-draw, your balance-breaking is "
            "honest. The fall is usually a side fall (yoko-ukemi), so "
            "the partner must be ready sideways."
        ),
        "how_it_works": (
            "Sumi-otoshi against katate-dori, step by step. Step one, "
            "connect: receive the grab with a soft hand and feel the "
            "partner's weight - find which front corner is light. Step "
            "two, step to the corner: take a decisive step toward that "
            "front corner (their weak diagonal), your body moving as one "
            "piece. Step three, draw across: as you step, draw the "
            "grabbed hand gently across your own center line toward the "
            "corner - the hand travels maybe a foot, no more. Step four, "
            "the drop: their balance, already committed to the corner, "
            "has nowhere to stand - they drop into a side fall; you "
            "simply continue your step and let gravity collect. Step "
            "five, follow through: finish balanced, facing the fallen "
            "partner, your drawing hand relaxed. The entire technique "
            "should feel like tipping a glass that was already sliding "
            "off the table. Faults: pushing at the end (that is a shove, "
            "not a drop), stepping without drawing the hand (the corner "
            "never loads), and drawing the hand without stepping (arm-"
            "only, no kuzushi). If the partner does not fall, the corner "
            "was wrong - find it again, do not force it."
        ),
        "key_points": [
            "Sumi-otoshi (corner drop) guides balance to the weak diagonal corner and lets the attacker fall - pure kuzushi with the technique removed.",
            "The hand travels about a foot; the step does the work - pushing at the end makes it a shove, not a drop.",
            "It looks like nothing, which is the point: it calibrates whether your balance-breaking is honest.",
            "If the partner does not fall, the corner was wrong - find it again, never force it.",
            "The fall is typically a side fall (yoko-ukemi); the partner must be ready sideways.",
        ],
        "requirements": [
            "Honest kuzushi sense from the kuzushi record - sumi-otoshi is its examination.",
            "A partner who falls when the balance is truly gone (and stays up when it is not) - honest feedback only.",
            "Side-fall ukemi proficiency from the partner.",
            "The discipline to abandon a failed attempt and re-find the corner instead of muscling.",
        ],
        "standards": [
            "Sumi-otoshi follows the Aikikai nage-waza syllabus against grabs.",
            "The corner-drop (happo-no-kuzushi applied) model follows classical budo theory.",
            "No-force finishing is the grading standard: muscled sumi-otoshi is marked as failed kuzushi.",
        ],
        "citations": [CIT_AIKIKAI, CIT_WESTBROOK],
        "sig_lens": (
            "The Signature read: sumi-otoshi is the covenant of the "
            "empty hand - the oath that mastery needs no display, only "
            "the true corner and one honest step. Where the public "
            "record teaches the drop, the Signature lens bows to the "
            "minimal: the armory's quietest throw, keeping its promise "
            "that the smallest true thing outweighs the largest forced "
            "one."
        ),
    },
    {
        "key": "aiki_otoshi",
        "name": "Aiki-otoshi: The Aiki Drop",
        "group": "Throws: Nage Waza",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Aiki-otoshi (合気落とし, aiki drop) drops the attacker by "
            "scooping the legs: nage enters deep, one arm gathering the "
            "attacker's far leg or both legs while the other hand guides "
            "the upper body, and the attacker is tipped backward over the "
            "scoop. It is one of the few aikido throws that directly "
            "attacks the legs, and it looks startlingly simple - a deep "
            "entry, a scoop, a tip. The classic form answers a strike or "
            "grab: nage irimi-enters past the attack, drops low, gathers "
            "the leg, and rises slightly while guiding the head back. "
            "The teaching point is level change: most aikido happens "
            "upright, but aiki-otoshi demands dropping the hips below the "
            "attacker's and driving up - the legs do the lifting the arms "
            "cannot. It needs a partner with good back-fall ukemi, "
            "because the tip is sudden and total."
        ),
        "how_it_works": (
            "Aiki-otoshi against a strike or grab, step by step. Step "
            "one, deep entry: irimi past the attack to the blind side, "
            "stepping deeper than for irimi-nage - your hips must arrive "
            "beside their legs. Step two, level change: drop your hips "
            "low, knees bent deeply, back straight - you are now below "
            "their center. Step three, the scoop: your near arm gathers "
            "behind their far knee or both knees (never the front of the "
            "knee joint - scoop the back of the leg), while your other "
            "hand guides their upper body or head gently backward. Step "
            "four, the tip: drive up slightly with the legs while "
            "guiding the upper body back - the attacker tips backward "
            "over the scooped leg like a felled post. Step five, guide "
            "the fall: keep the guiding hand with them to the mat so "
            "the back fall is controlled, then finish in zanshin. "
            "Faults: scooping the front of the knee (joint danger - "
            "always the back of the leg), staying upright (no level "
            "change means arm-lifting, which fails and strains the "
            "back), and dropping the partner without the guiding hand "
            "(uncontrolled falls injure)."
        ),
        "key_points": [
            "Aiki-otoshi (aiki drop) scoops the back of the leg while guiding the upper body back - a deep entry, a level change, a tip.",
            "Always scoop behind the knee, never the front of the joint - front-of-knee scooping endangers the joint.",
            "The level change is the technique: drop the hips below the attacker's center and let the legs do the lifting.",
            "The guiding hand stays with the partner to the mat - uncontrolled drops injure.",
            "Needs a partner with solid back-fall ukemi; the tip is sudden and total.",
        ],
        "requirements": [
            "Deep knee bend with a straight back - the level change must be trained as a squat pattern first.",
            "A partner with reliable ushiro-ukemi; the fall is backward and complete.",
            "The back-of-leg scoop rule memorized as an absolute - no exceptions.",
            "An instructor supervising the first scoops; leg attacks are unfamiliar to most aikido students.",
        ],
        "standards": [
            "Aiki-otoshi follows the Aikikai nage-waza syllabus against strikes and grabs.",
            "The behind-the-knee scoop is the universal joint-safety standard.",
            "Guided falls (hand stays with the partner) are required in grading demonstrations.",
        ],
        "citations": [CIT_AIKIKAI, CIT_WESTBROOK],
        "sig_lens": (
            "The Signature read: aiki-otoshi is the covenant of the low "
            "road - the oath that the strong will be met below their "
            "strength, where the legs are honest and the arms cannot "
            "lie. Where the public record teaches the scoop, the "
            "Signature lens drops with it: the armory kneels to lift, "
            "and the fall is guided home like something carried."
        ),
    },
    {
        "key": "koshinage",
        "name": "Koshinage: Hip Throws",
        "group": "Throws: Nage Waza",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "Koshi-nage (腰投げ, hip throw) is aikido's hip-throw family, "
            "shared with its judo cousin: nage turns the hips in front of "
            "the attacker, loads the attacker's body across the hip, and "
            "throws by straightening the legs and turning. Aikido's "
            "versions - o-goshi (major hip), ko-goshi (minor hip), and "
            "the dropping variations - all follow the same physics: get "
            "the hips below the attacker's center, make hip-to-hip "
            "contact, and let the legs do the lifting. Koshi-nage sits "
            "at the advanced tier because the entry is intimate - your "
            "back is to the attacker mid-throw - which demands total "
            "commitment and a partner whose forward-roll ukemi is "
            "flawless. Done well it is the most decisive throw on the "
            "ladder: once the hips are in, the throw is inevitable. Done "
            "with a high hip or a bent back, it is a back injury waiting "
            "to happen, which is why teachers gate it behind years of "
            "ukemi and posture training."
        ),
        "how_it_works": (
            "O-goshi form against a grab, step by step. Step one, entry: "
            "as the partner grabs or pushes, step in deep with tsugi-ashi "
            "and turn 180 degrees, pulling their arm across so your back "
            "meets their front - your hips must finish below theirs. "
            "Step two, contact: settle your hips against their lower "
            "abdomen/upper thighs, knees deeply bent, back straight - "
            "the load sits on the hips, never on the bent spine. Step "
            "three, the load: draw their upper body forward over your "
            "back with the guiding arm while your hips wedge under their "
            "center - they should feel light, draped across you. Step "
            "four, the throw: straighten the legs explosively while "
            "turning the hips, guiding their body over in a forward arc "
            "- the legs throw, the arms only steer. Step five, guide: "
            "keep the guiding hand with them into their forward roll. "
            "Safety absolutes: hips below theirs before loading (a high "
            "hip means you lift with the back - stop immediately), back "
            "straight throughout, and never attempt with a partner whose "
            "forward ukemi is not solid. Drill the entry and load "
            "without throwing for weeks; the throw itself is the easy "
            "part once the position is right."
        ),
        "key_points": [
            "Koshi-nage (hip throw): turn the hips in below the attacker's center, load across the hip, throw by straightening the legs and turning.",
            "Hips must finish below the attacker's - a high hip means lifting with the back, which is how backs are injured.",
            "The legs throw and the arms only steer; back stays straight throughout the load.",
            "Gated behind years of ukemi and posture training because the entry turns your back mid-throw.",
            "Drill entry-and-load without throwing for weeks; the position is the technique, the throw is the receipt.",
        ],
        "requirements": [
            "Flawless forward-roll ukemi from the partner - hip throws launch the attacker decisively.",
            "A deep, straight-backed squat pattern trained separately before any loading.",
            "An instructor gating the technique: no koshi-nage until posture and ukemi are proven.",
            "A partner of appropriate size at first; loading a much heavier partner is advanced practice.",
        ],
        "standards": [
            "Koshi-nage (o-goshi, ko-goshi forms) follows the Aikikai nage-waza syllabus.",
            "The hips-below-center and straight-back rules are universal throwing safety standards.",
            "Forward-roll ukemi proficiency is the prerequisite for hip-throw practice.",
        ],
        "citations": [CIT_AIKIKAI, CIT_WESTBROOK, CIT_SHIODA],
        "sig_lens": (
            "The Signature read: koshi-nage is the covenant of the low "
            "hip - the oath that the body will go beneath the problem "
            "and lift it with the legs' honest strength. Where the "
            "public record teaches the load, the Signature lens honors "
            "the kneel: the armory's heaviest throw begins with the "
            "deepest bow of the hips."
        ),
    },
    {
        "key": "udekime_nage",
        "name": "Udekime-nage: The Straight-Arm Throw",
        "group": "Throws: Nage Waza",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "Udekime-nage (腕決め投げ, arm-lock throw) locks the attacker's "
            "arm straight - typically with the elbow braced against nage's "
            "shoulder or forearm - and throws by driving the locked arm "
            "down and through. Against a grab or strike, nage takes the "
            "arm, straightens it into the lock (ude-garami family "
            "mechanics applied standing), and the attacker must fall to "
            "protect the elbow: resisting the throw means resisting with "
            "a locked joint, which the body refuses to do. It is an "
            "advanced technique because the margin between control and "
            "elbow injury is measured in inches and in the attacker's "
            "cooperation - the lock must be applied with the body, never "
            "snapped with the hands. Udekime-nage teaches the advanced "
            "lesson that a straight arm is a lever, and a lever with a "
            "human being attached must be moved the way you would carry "
            "something fragile: firmly, smoothly, and never suddenly."
        ),
        "how_it_works": (
            "Udekime-nage against katate-dori, step by step. Step one, "
            "entry: tenkan as the grab lands, drawing the grabbing arm "
            "out to extension. Step two, the lock: guide their arm so "
            "the elbow straightens with their palm turning up, and brace "
            "their upper arm against your shoulder or forearm - the arm "
            "is now a straight lever with the elbow as the fulcrum "
            "point you control. Step three, body application: step "
            "through with the hips, driving your braced structure "
            "forward and down - the lock tightens through body movement, "
            "never through yanking the wrist. Step four, the throw: as "
            "the lock reaches its limit, continue the downward drive; "
            "the attacker falls forward or to the side to release the "
            "elbow pressure - follow with the guiding hand. Step five, "
            "release the lock the instant they fall - holding a locked "
            "elbow past the fall is how injuries happen. Safety rules: "
            "apply slowly, never snap; keep the elbow's natural range "
            "sacred; the partner taps at the first elbow pressure and "
            "you release immediately. Practice the lock-and-release "
            "without throwing until the margin feels obvious."
        ),
        "key_points": [
            "Udekime-nage (straight-arm throw) braces the attacker's straightened arm and throws by driving the locked lever down through body movement.",
            "The margin between control and elbow injury is inches - the lock is applied with the body, never snapped with the hands.",
            "Release the lock the instant the partner falls; holding a locked elbow past the fall causes injury.",
            "The partner taps at the first elbow pressure and the technique stops immediately - no exceptions.",
            "Its lesson: a straight arm is a lever, and a lever with a person attached is carried firmly, smoothly, never suddenly.",
        ],
        "requirements": [
            "An instructor's direct supervision - elbow-lock throws are never self-taught.",
            "A partner who taps early and a nage who releases instantly; the communication must be flawless.",
            "Slow practice until the lock's engagement point is felt precisely - speed only after the margin is obvious.",
            "Working tenkan and arm-extension control from the kyo-waza foundation.",
        ],
        "standards": [
            "Udekime-nage follows the Aikikai nage-waza syllabus as an advanced arm-lock throw.",
            "The no-snap, tap-release rules are universal joint-lock safety standards.",
            "Elbow-range preservation is examined in advanced grading demonstrations.",
        ],
        "citations": [CIT_AIKIKAI, CIT_WESTBROOK],
        "sig_lens": (
            "The Signature read: udekime-nage is the covenant of the "
            "straight line - the oath that the longest lever will be "
            "moved the most gently. Where the public record teaches the "
            "brace, the Signature lens keeps the vow of fragility: the "
            "armory carries its sharpest lever like glass, and releases "
            "it the instant the fall begins."
        ),
    },
    {
        "key": "katame_waza",
        "name": "Katame-waza: Pins and Immobilizations",
        "group": "Pins and Freestyle",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "Katame-waza (固め技, pinning techniques) is the art of "
            "holding: after any throw or control, nage settles the "
            "attacker into an immobilization that can be maintained "
            "indefinitely without injury. The standard aikido pin - used "
            "after ikkyo through gokyo, kotegaeshi, and shiho-nage - "
            "holds the attacker face-down: the controlled arm is folded "
            "or extended behind the back at a natural angle, nage kneels "
            "beside the shoulder with body weight settled over it, one "
            "hand controlling the wrist, the knee or hip blocking the "
            "shoulder, and the eyes up in zanshin. A good pin is "
            "painless to the still partner and inescapable to the moving "
            "one: any attempt to rise tightens the attacker's own joint "
            "against the hold. Advanced study adds pin transitions - "
            "flowing from one pin to another as the partner shifts - and "
            "the judgment of when to pin versus when to throw. The pin "
            "is aikido's answer to 'then what': control that can wait "
            "for help, for calm, or for the conflict to end."
        ),
        "how_it_works": (
            "The standard face-down pin, step by step. Step one, arrive "
            "with the technique: the pin is never applied to a standing, "
            "balanced partner - it follows a completed throw or lock, "
            "with the partner already going down. Step two, shape the "
            "arm: fold or extend the controlled arm behind the back to "
            "its natural resting angle - never force the shoulder past "
            "comfort. Step three, settle: kneel beside the partner's "
            "shoulder, sink your body weight over the shoulder joint, "
            "one hand holding the wrist, your knee or hip blocking the "
            "shoulder from rolling. Step four, the pressure test: ask "
            "the partner to try to rise slowly - the structure should "
            "hold through geometry, not muscle; adjust until it does. "
            "Step five, zanshin: eyes up, watching the surroundings, "
            "breathing normally - the pin is held by a calm body, not a "
            "tense one. Step six, release: to let up, ease the wrist "
            "control first and step back smoothly - never shove off. "
            "Transitions: practice flowing from the ikkyo pin to the "
            "kotegaeshi pin as the partner shifts, keeping contact "
            "through the change. The rule of all pins: painless to the "
            "still, inescapable to the moving."
        ),
        "key_points": [
            "Katame-waza (pinning techniques) immobilize through geometry and settled body weight - painless to the still partner, inescapable to the moving one.",
            "The standard pin: attacker face-down, arm at its natural angle behind the back, nage kneeling with weight over the shoulder, eyes up in zanshin.",
            "Pins are never applied to a standing, balanced partner - they follow a completed throw or lock.",
            "Advanced study adds pin transitions: flowing between pins as the partner shifts, keeping contact throughout.",
            "Release by easing the wrist control and stepping back smoothly - never shove off a pinned partner.",
        ],
        "requirements": [
            "A completed throw or lock first - the pin is a finish, not an opening.",
            "Knowledge of the shoulder's natural range; the arm is shaped, never forced.",
            "A partner who tests the pin honestly by trying to rise slowly.",
            "Zanshin habit: eyes up and breathing calm while holding - tension is a failed pin.",
        ],
        "standards": [
            "Katame-waza follows the Aikikai pinning syllabus; the face-down pin is the standard finish of the kyo-waza.",
            "The painless-to-the-still standard is examined in kyu and dan gradings.",
            "Zanshin (remaining awareness) during pins is a universal budo standard.",
        ],
        "citations": [CIT_AIKIKAI, CIT_WESTBROOK],
        "sig_lens": (
            "The Signature read: the pin is the covenant of the held - "
            "the oath that the defeated will be kept safe until the "
            "storm passes. Where the public record teaches the shape, "
            "the Signature lens keeps the honor hold: the armory's "
            "strongest lock is the one that never needs to hurt, only "
            "to wait."
        ),
    },
    {
        "key": "randori",
        "name": "Randori: Freestyle Practice Against Multiple Attackers",
        "group": "Pins and Freestyle",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Randori (乱取り, free practice) is aikido's freestyle: one "
            "defender against multiple attackers (futari-dori, two "
            "attackers; sannin-dori, three; yonin-dori, four), all "
            "attacking freely with grabs and strikes while nage responds "
            "with any technique. It is the art's pressure test and its "
            "most famous spectacle - the image of one calm figure "
            "throwing attackers in every direction. Randori strategy is "
            "movement, not technique collection: keep moving so only one "
            "attacker can reach you at a time, never let two attackers "
            "form a line with you between them, throw and move on "
            "immediately (never admire a throw), and use each thrown "
            "attacker as a momentary shield. Beginners start with "
            "two attackers at walking speed; the speed and number grow "
            "only with control. Randori is where the whole ladder is "
            "examined at once: footwork, blending, kuzushi, ukemi (yours, "
            "as you get caught), and above all zanshin - awareness of "
            "everyone, everywhere, all the time."
        ),
        "how_it_works": (
            "Randori principles, trained in stages. Stage one, the "
            "triangle: with two attackers, move constantly so you form "
            "a triangle with them - never stand on the line between "
            "them, or both reach you at once. Stage two, one at a time: "
            "engage the nearest attacker with the simplest technique "
            "you own (often irimi-nage or kokyu), throw, and move on "
            "before the throw lands - your feet never stop. Stage three, "
            "the shield: let a falling attacker pass between you and "
            "the next one; their body buys you a half-second. Stage "
            "four, breathing and eyes: breathe continuously (holding "
            "breath freezes you), keep the gaze wide (metsuke) to track "
            "all attackers peripherally - looking at one means losing "
            "the others. Stage five, scaling: start futari-dori at "
            "half speed with trusted partners; add speed, then a third "
            "attacker, then a fourth, only when control is proven at "
            "each stage. Stage six, recovery: when caught (it happens), "
            "take clean ukemi and re-enter - panicking is the only real "
            "failure. Rules: no techniques you cannot control, no "
            "stopping to finish pins (throw and move), and the senior "
            "partners set the intensity, never the junior."
        ),
        "key_points": [
            "Randori (freestyle) pits one defender against two to four free attackers; it is the art's pressure test and most famous form.",
            "Strategy is movement: triangle positioning (never between two attackers), one attacker at a time, throw and move on immediately.",
            "Use falling attackers as momentary shields; keep the gaze wide (metsuke) and the breath continuous.",
            "When caught, take clean ukemi and re-enter - panicking is the only real failure.",
            "Scale slowly: two attackers at half speed first; seniors set intensity, and no uncontrolled techniques ever.",
        ],
        "requirements": [
            "Solid ukemi from everyone - randori throws come from all directions at speed.",
            "The full technique vocabulary at reflexive level; randori leaves no time to think.",
            "Trusted partners who scale intensity honestly and protect the defender.",
            "A large mat with clear boundaries and an instructor supervising every round.",
        ],
        "standards": [
            "Randori (futari/sannin/yonin-dori) follows Aikikai freestyle practice convention.",
            "Multiple-attacker randori is a required demonstration at dan gradings.",
            "Intensity-scaling by senior partners is the universal safety standard.",
        ],
        "citations": [CIT_AIKIKAI, CIT_WESTBROOK, CIT_SHIODA],
        "sig_lens": (
            "The Signature read: randori is the covenant of the calm "
            "center - the oath that one aware body can answer many "
            "without hurry and without fear. Where the public record "
            "counts the attackers, the Signature lens watches the "
            "defender's breath: the armory's final exam is not "
            "technique but composure, kept moving."
        ),
    },
    {
        "key": "jiyu_waza",
        "name": "Jiyu-waza: Free Technique Practice",
        "group": "Pins and Freestyle",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Jiyu-waza (自由技, free techniques) is freestyle against a "
            "single attacker: the partner attacks with any grab or "
            "strike, and nage answers with whatever technique fits - no "
            "script, no announced attack. Where randori tests awareness "
            "against many, jiyu-waza tests adaptability against one: "
            "can the body choose the right technique without the mind "
            "interfering? Training usually runs as continuous flow - "
            "attack, technique, ukemi, re-attack without pause - which "
            "builds the stamina and spontaneity that scripted practice "
            "cannot. Teachers watch for the moment students stop "
            "'selecting' techniques and start responding: the entries "
            "get shorter, the blends get earlier, and the same attack "
            "starts producing different techniques on different "
            "repetitions. Jiyu-waza is the bridge between the ladder's "
            "drills and real application - the place where thirty "
            "separate techniques become one art."
        ),
        "how_it_works": (
            "Run jiyu-waza in rounds. Round one, limited menu: the "
            "attacker uses only katate-dori and shomen-uchi; nage may "
            "use only ikkyo, irimi-nage, and shiho-nage - constraints "
            "build fluency before freedom. Round two, open attacks: any "
            "grab or strike, same three techniques - now the choice is "
            "about reading the attack. Round three, open techniques: "
            "any attack, any technique from the ladder - the full "
            "vocabulary, chosen in the moment. Round four, continuous "
            "flow: no pauses between repetitions; the attacker re-"
            "attacks the instant they recover ukemi - this builds the "
            "stamina and the habit of zanshin between techniques. "
            "Coaching cues: if you are thinking of technique names, slow "
            "down - naming is the mind interfering; if the same attack "
            "always gets the same answer, deliberately vary it; if you "
            "freeze, default to irimi-tenkan footwork and let the hands "
            "catch up. The goal is not to win the round but to reach "
            "the state where the body answers before the mind finishes "
            "the question."
        ),
        "key_points": [
            "Jiyu-waza (free techniques): one attacker, any attack, any technique - the test of adaptability that scripted practice cannot give.",
            "Trained in rounds with expanding freedom: limited menu, then open attacks, then open techniques, then continuous flow.",
            "The goal is response without selection - the body answering before the mind finishes naming the technique.",
            "Continuous-flow rounds build stamina and the habit of zanshin between techniques.",
            "If you freeze, default to irimi-tenkan footwork and let the hands catch up.",
        ],
        "requirements": [
            "The technique vocabulary at reflexive level - jiyu-waza examines the whole ladder at once.",
            "An attacker who varies attacks honestly rather than feeding the defender's favorite.",
            "Stamina: continuous rounds are aerobic; build up round length gradually.",
            "A teacher watching for mind-interference (freezing, naming) versus genuine response.",
        ],
        "standards": [
            "Jiyu-waza follows Aikikai freestyle practice convention as the single-attacker complement to randori.",
            "Free-technique demonstration is required at dan gradings.",
            "Continuous-flow etiquette (immediate re-attack after ukemi) is the standard training format.",
        ],
        "citations": [CIT_AIKIKAI, CIT_WESTBROOK],
        "sig_lens": (
            "The Signature read: jiyu-waza is the covenant of the "
            "unscripted - the oath that the art lives in the body, not "
            "in the drill card. Where the public record opens the menu, "
            "the Signature lens listens for the silence after the last "
            "named technique: the armory's truest weapon is the answer "
            "that arrives before the question is finished."
        ),
    },
    {
        "key": "tanto_dori",
        "name": "Tanto-dori: Knife Disarms",
        "group": "Weapons, Disarms, and Advanced Practice",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Tanto-dori (短刀取り, knife taking) is aikido's answer to the "
            "knife: against thrusts (tsuki) and downward cuts "
            "(shomen-uchi with the blade), nage blends off the line, "
            "controls the knife arm, and takes the weapon - typically "
            "with kotegaeshi, sankyo, or shiho-nage mechanics adapted to "
            "keep every part of nage's body off the blade line. Training "
            "uses a wooden or rubber tanto (never a live blade), and the "
            "art is explicit about the hierarchy: the best defense "
            "against a knife is distance and escape; tanto-dori exists "
            "for when escape has already failed. The technical keys are "
            "absolute: never grab at the knife hand with the other hand "
            "crossing the blade, control the elbow rather than the wrist "
            "(the wrist is too close to the edge), and finish with the "
            "weapon secured and the attacker pinned. Tanto-dori is "
            "advanced because the cost of error is absolute - which is "
            "why it is drilled slowly, with wooden weapons, under direct "
            "supervision, and never rushed."
        ),
        "how_it_works": (
            "Tanto-dori against a straight thrust, training form, step "
            "by step. Step one, the line: as the thrust comes, move "
            "completely off its line with irimi or tenkan - the blade "
            "must pass through empty air; this is ninety percent of the "
            "defense. Step two, the arm: meet the knife arm above the "
            "elbow with both hands - control the elbow, never reach for "
            "the wrist or the knife itself. Step three, the lock: apply "
            "kotegaeshi or sankyo mechanics to the controlled arm, "
            "keeping your body behind the elbow and your hands off the "
            "blade's plane. Step four, the take: as the lock folds the "
            "attacker down, strip or catch the tanto with the hand "
            "farthest from the edge, securing it immediately. Step five, "
            "the pin: pin the attacker face-down with the weapon held "
            "clear of both bodies. Training rules, absolute: wooden or "
            "rubber tanto only, ever; slow speed until every line is "
            "perfect; the attacker thrusts committedly but never "
            "redirects mid-thrust to 'catch' the defender; and the "
            "hierarchy is taught first - escape beats disarm, and "
            "tanto-dori is the last resort made trainable. Never "
            "practice with a live blade, never improvise at speed."
        ),
        "key_points": [
            "Tanto-dori (knife taking) answers thrusts and cuts by leaving the line completely, controlling the elbow (never the wrist or knife), and taking the weapon with adapted kotegaeshi/sankyo/shiho-nage mechanics.",
            "The hierarchy is explicit: escape is the best defense; tanto-dori exists for when escape has already failed.",
            "Training uses wooden or rubber tanto only - never a live blade, never improvised at speed.",
            "The blade line is sacred: no hand ever crosses the blade's plane during the technique.",
            "Finish with the weapon secured clear of both bodies and the attacker pinned.",
        ],
        "requirements": [
            "Wooden or rubber training tanto - the live blade never enters the dojo.",
            "Direct instructor supervision for every repetition; knife work is never solo-drilled.",
            "Mastery of the underlying locks (kotegaeshi, sankyo) empty-handed first - tanto-dori adapts them, it does not teach them.",
            "A partner trained to thrust committedly without redirecting to catch the defender.",
        ],
        "standards": [
            "Tanto-dori follows the Aikikai weapons-taking syllabus with wooden tanto.",
            "The escape-first hierarchy is the universal self-defense instruction standard.",
            "Training-weapon-only practice is an absolute dojo safety rule.",
        ],
        "citations": [CIT_AIKIKAI, CIT_UESHIBA, CIT_WESTBROOK],
        "sig_lens": (
            "The Signature read: tanto-dori is the covenant of the last "
            "resort - the oath that the art keeps an answer even for "
            "the moment escape failed, and that the answer will be "
            "practiced with wood until it deserves no sharper test. "
            "Where the public record teaches the take, the Signature "
            "lens keeps the hierarchy holy: the armory's bravest "
            "technique is the one it hopes you never need."
        ),
    },
    {
        "key": "tachi_jo_dori",
        "name": "Tachi-dori and Jo-dori: Sword and Staff Disarms",
        "group": "Weapons, Disarms, and Advanced Practice",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Tachi-dori (太刀取り, sword taking) and jo-dori (杖取り, "
            "staff taking) extend the disarm curriculum to long weapons: "
            "against a bokken (wooden sword) cut or a jo (short staff) "
            "thrust or swing, nage enters inside the weapon's arc - "
            "closer than the attacker expects - controls the weapon "
            "arm, and takes the weapon with adapted throwing mechanics. "
            "The governing insight is range: long weapons are "
            "devastating at their reach and helpless inside it, so the "
            "defender's whole task is to arrive inside the arc before "
            "it completes. Training uses wooden weapons throughout, and "
            "like tanto-dori it is gated behind complete empty-handed "
            "mastery - every tachi-dori is an irimi-nage or shiho-nage "
            "wearing a sword. These disarms are advanced because the "
            "timing window is unforgiving: entering a fraction late "
            "means meeting the weapon at full speed, so the entry is "
            "drilled at slow speed hundreds of times before any pace."
        ),
        "how_it_works": (
            "Jo-dori against a staff thrust, training form, step by "
            "step. Step one, read the range: as the thrust extends, "
            "recognize the weapon's full reach - your target is inside "
            "it, past the tip. Step two, the entry: irimi deep along "
            "the staff's line, your body sliding past the tip before "
            "the thrust completes - timing beats speed; you move as "
            "the attack begins, not after. Step three, the arm: both "
            "hands take the staff arm above the elbow, pinning it to "
            "your center as in the knife defense - control the limb, "
            "not the weapon. Step four, the take: apply shiho-nage or "
            "irimi-nage mechanics to the controlled arm; as the "
            "attacker folds, strip the jo with the far hand and step "
            "clear. Step five, secure: hold the taken weapon pointed "
            "away from both bodies and pin or control the attacker. "
            "For tachi-dori against a downward cut: enter inside the "
            "cut's arc as it falls (never after), take the sword arm, "
            "and throw with kokyu or irimi-nage mechanics, securing "
            "the bokken the same way. Absolute rules: wooden weapons "
            "only, slow until the entry timing is perfect, and the "
            "attacker never redirects mid-swing to catch the entrant."
        ),
        "key_points": [
            "Tachi-dori (sword taking) and jo-dori (staff taking) defeat long weapons by entering inside their arc before it completes - devastating at reach, helpless inside it.",
            "Control the weapon arm above the elbow, never the weapon itself; every disarm is an empty-handed throw wearing a weapon.",
            "Timing beats speed: move as the attack begins - entering a fraction late means meeting the weapon at full speed.",
            "Strip the weapon with the far hand and secure it pointed away from both bodies.",
            "Wooden weapons only, slow until entry timing is perfect; the attacker never redirects mid-swing to catch the entrant.",
        ],
        "requirements": [
            "Complete empty-handed mastery first - tachi-dori and jo-dori adapt irimi-nage and shiho-nage, they do not replace them.",
            "Wooden bokken and jo; the training weapons never leave the supervised drill.",
            "Hundreds of slow entries before any pace - the timing window is unforgiving and must be grooved.",
            "An attacker trained to commit without redirecting; a 'catching' attacker makes the drill dangerous.",
        ],
        "standards": [
            "Tachi-dori and jo-dori follow the Aikikai weapons-taking syllabus with wooden weapons.",
            "The inside-the-arc entry model follows classical budo weapons-defense theory.",
            "No-redirect attacker protocol is a universal weapons-drill safety standard.",
        ],
        "citations": [CIT_AIKIKAI, CIT_UESHIBA, CIT_WESTBROOK],
        "sig_lens": (
            "The Signature read: the long-weapon disarms are the "
            "covenant of the inside road - the oath that courage will "
            "be timed, not merely brave, and the shortest path past "
            "danger is through it. Where the public record teaches the "
            "arc, the Signature lens times the entry: the armory's "
            "longest weapons fall to the shortest step, taken at the "
            "exact right instant."
        ),
    },
    {
        "key": "kaeshi_waza",
        "name": "Kaeshi-waza: Counter Techniques",
        "group": "Weapons, Disarms, and Advanced Practice",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Kaeshi-waza (返し技, counter techniques) is the art of "
            "answering a technique with a technique: as the partner "
            "applies ikkyo, nage reverses the connection - borrowing the "
            "partner's own committed motion - and throws or pins them "
            "with a counter such as kote-gaeshi-kaeshi or shiho-nage-"
            "kaeshi. Counters work on a humbling principle: every "
            "technique, sincerely applied, gives the receiver perfect "
            "information about the giver's balance - and a skilled "
            "receiver can spend that information. Training kaeshi-waza "
            "teaches two advanced lessons at once: how to apply "
            "techniques so they cannot be countered (commitment without "
            "overextension, kuzushi maintained throughout), and how "
            "sensitive the advanced body has become (feeling the "
            "counter opening the instant it appears). It is practiced "
            "slowly and cooperatively - a counter applied at speed to "
            "an unready partner is simply an ambush - and it marks the "
            "student's arrival at the level where techniques are no "
            "longer separate moves but one continuous conversation."
        ),
        "how_it_works": (
            "A basic counter - answering shiho-nage with kotegaeshi - "
            "step by step. Step one, feel the technique: as the partner "
            "begins shiho-nage's wrist turn, do not resist; instead feel "
            "where their balance commits - the counter lives in their "
            "commitment. Step two, borrow it: as they pivot under your "
            "arm, let your controlled hand stay soft and follow their "
            "motion one beat longer than they expect - their kuzushi "
            "of you becomes your kuzushi of them. Step three, reverse "
            "the connection: turn their turning wrist back with "
            "kotegaeshi mechanics, stepping through as their own pivot "
            "carries them past balance. Step four, finish gently: guide "
            "the counter to a controlled fall or pin - the point is the "
            "reversal, not the impact. Step five, the giver's lesson: "
            "now reverse roles and feel how the counter was possible - "
            "where did your balance overextend? Close that gap next "
            "repetition. Training rules: slow and cooperative always; "
            "the partner must know the counter is coming (announced "
            "counters first, then unannounced at low speed); never "
            "counter a partner who is still learning the base technique "
            "- counters are for students who own the original."
        ),
        "key_points": [
            "Kaeshi-waza (counter techniques) answer a technique with a technique, borrowing the giver's committed motion to reverse it.",
            "Every sincere technique gives the receiver perfect information about the giver's balance - the counter spends that information.",
            "It teaches both sides at once: how to counter, and how to apply techniques so they cannot be countered.",
            "Practiced slowly and cooperatively - a speed counter on an unready partner is an ambush, not training.",
            "Counters are only for students who own the base technique; never counter someone still learning the original.",
        ],
        "requirements": [
            "Ownership of the base techniques - you cannot counter what you cannot do.",
            "A partner who knows the counter is coming (announced first, unannounced only at low speed later).",
            "Slow, cooperative practice; the reversal is studied, not sprung.",
            "An instructor pairing students by level - mismatched counter practice injures the less skilled partner.",
        ],
        "standards": [
            "Kaeshi-waza follows the Aikikai advanced syllabus as counter-forms of the core techniques.",
            "The announced-before-unannounced progression is the universal counter-training safety standard.",
            "Level-matched pairing for counter practice is a dojo safety rule.",
        ],
        "citations": [CIT_AIKIKAI, CIT_WESTBROOK, CIT_SHIODA],
        "sig_lens": (
            "The Signature read: kaeshi-waza is the covenant of the "
            "conversation - the oath that no technique is the last word, "
            "and every committed motion donates its balance to whoever "
            "listens best. Where the public record teaches the reversal, "
            "the Signature lens hears the dialogue: the armory's "
            "techniques talk to each other, and the advanced student has "
            "learned to listen in."
        ),
    },
    {
        "key": "hanmi_handachi_suwari",
        "name": "Hanmi-handachi and Suwari-waza: Seated and Kneeling Techniques",
        "group": "Weapons, Disarms, and Advanced Practice",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Hanmi-handachi (半身半立ち, half-standing) is aikido practiced "
            "with nage kneeling and the attacker standing: the defender "
            "answers grabs and strikes from the knees, which removes the "
            "legs from the equation and forces the techniques to work on "
            "hip movement and upper-body blending alone. Suwari-waza "
            "(座り技, seated techniques) goes further - both partners "
            "kneel, moving on the knees (shikko, knee-walking) through "
            "the full technique catalog. These forms are the art's "
            "laboratory for purity: without leg drive, every trace of "
            "muscling is exposed, and the student learns whether their "
            "ikkyo or shiho-nage truly runs on hips and connection or "
            "was secretly running on leg strength. They also carry the "
            "art's historical memory - techniques born for seated "
            "castle life, where standing to fight was not an option. "
            "Knee-walking itself (shikko) is a conditioning art: gliding "
            "on the knees with an upright torso builds the hip mobility "
            "that powers every throw on the ladder."
        ),
        "how_it_works": (
            "Shikko (knee-walking) first, then technique. Step one, the "
            "kneel: from seiza, rise slightly onto the knees with the "
            "torso perfectly upright - the hips, not the thighs, will "
            "drive. Step two, the glide: step forward on the knees one "
            "at a time, keeping the torso level and upright, toes "
            "pointed behind - it should feel like the hips are walking "
            "while the knees merely touch down. Step three, turns: "
            "pivot on the knees for tenkan, keeping the same upright "
            "torso - most beginners jackknife forward here; the teacher "
            "corrects it relentlessly. Step four, hanmi-handachi "
            "technique: kneeling, receive the standing partner's wrist "
            "grab; answer with ikkyo or shiho-nage using only hip shift "
            "and arm blending - if the technique fails, the legs were "
            "doing secret work in your standing version. Step five, "
            "suwari-waza: both kneeling, practice the kyo-waza set "
            "moving entirely in shikko. Conditioning notes: knees need "
            "gradual adaptation - short sessions on good mats, never on "
            "hard floors; persistent knee pain means stop and consult, "
            "not push through. The payoff: when you stand back up, your "
            "techniques run on hips alone, and everything gets lighter."
        ),
        "key_points": [
            "Hanmi-handachi (defender kneeling, attacker standing) and suwari-waza (both kneeling) remove the legs and expose whether techniques truly run on hips and connection.",
            "Shikko (knee-walking) is the foundation: gliding on the knees with a perfectly upright torso, driven by the hips.",
            "They are the art's purity laboratory - every trace of muscling shows when the legs cannot help.",
            "They carry historical memory: techniques born for seated castle life, where standing was not an option.",
            "Knees adapt gradually on good mats only; persistent pain means stop, never push through.",
        ],
        "requirements": [
            "Good mats and gradual adaptation - knee-walking conditions tissue that standing never loads.",
            "An upright torso held relentlessly; the jackknife-forward fault must be corrected from the first session.",
            "The standing versions of the techniques already owned - seated forms refine, they do not introduce.",
            "Medical caution: pre-existing knee conditions must be cleared before shikko practice.",
        ],
        "standards": [
            "Hanmi-handachi and suwari-waza follow the Aikikai syllabus; both appear in dan grading examinations.",
            "Shikko form (upright torso, hip-driven glide) follows Hombu Dojo basic instruction.",
            "Knee-safety progression (mats only, gradual loading) is a universal dojo standard.",
        ],
        "citations": [CIT_AIKIKAI, CIT_UESHIBA, CIT_WESTBROOK],
        "sig_lens": (
            "The Signature read: the seated forms are the covenant of "
            "the honest hip - the oath that technique will stand on "
            "connection alone, with the legs' secret help confessed and "
            "removed. Where the public record teaches the kneel, the "
            "Signature lens stays low with it: the armory's purest "
            "techniques are the ones that work from the floor."
        ),
    },
    {
        "key": "aiki_ken_jo",
        "name": "Aiki-ken and Aiki-jo: Wooden Sword and Staff Forms",
        "group": "Weapons, Disarms, and Advanced Practice",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Aiki-ken (合気剣, aiki sword) and aiki-jo (合気杖, aiki staff) "
            "are aikido's weapons arts: solo and paired forms with the "
            "bokken (wooden sword) and jo (short staff, about 50 inches) "
            "that teach what empty-handed technique cannot - true "
            "distance, true timing, and the consequence of error. The "
            "founder insisted weapons and empty hands are one study "
            "(riai): the sword cut is shiho-nage's circle, the staff "
            "thrust is irimi's entry, and tenkan is simply getting off "
            "the cut's line. Basic practice includes the ken suburi "
            "(seven solo cutting drills), the jo suburi (twenty solo "
            "staff drills in the Iwama tradition), and paired kata where "
            "partners trade cuts and thrusts at full commitment. "
            "Students discover that a partner swinging a bokken cannot "
            "be bluffed - lazy blending that 'worked' empty-handed "
            "collapses instantly - which is why weapons sit at the top "
            "of the ladder: they are the examiners of everything below."
        ),
        "how_it_works": (
            "Begin with ken suburi, the seven solo cuts. Cut one, "
            "shomen: from kamae, raise the bokken overhead and cut "
            "straight down the center line, hips dropping as the blade "
            "falls - the cut is powered by the hips, not the arms. Cuts "
            "two through seven add the angled, thrusting, and turning "
            "cuts; each is drilled until the blade's path is exact and "
            "the body stays balanced throughout. Then jo suburi: the "
            "twenty solo staff forms - thrusts (tsuki), strikes "
            "(shomen, yokomen), sweeps, and spins - drilled until the "
            "staff feels like an extension of the hands. Then paired "
            "practice: one partner cuts shomen, the other enters with "
            "the empty-handed irimi that the cut taught - this is riai "
            "made physical, the same body solving the same problem with "
            "and without the weapon. Then kata: the thirteen-count jo "
            "kata and the paired ken forms, memorized as movement "
            "sentences. Safety: bokken and jo are wood but they are "
            "weapons - full protective distance, controlled cuts that "
            "stop on the line, and paired practice only under "
            "supervision. The lesson weapons teach: distance is real, "
            "timing is real, and everything below this record is now "
            "being graded by wood."
        ),
        "key_points": [
            "Aiki-ken (wooden sword) and aiki-jo (short staff) teach true distance, true timing, and consequence - the examiners of everything below them on the ladder.",
            "Riai (the unity principle): the sword cut is shiho-nage's circle, the staff thrust is irimi's entry - weapons and empty hands are one study.",
            "Ken suburi (seven solo cuts) and jo suburi (twenty solo staff forms, Iwama tradition) build the vocabulary; paired kata makes it conversational.",
            "Cuts are powered by the hips, not the arms; the blade's path must be exact and the body balanced throughout.",
            "Wood is still a weapon: full protective distance, cuts that stop on the line, paired practice only under supervision.",
        ],
        "requirements": [
            "A bokken and jo of appropriate length and weight - sized to the student, not borrowed at random.",
            "Enough clear space for a full sword arc in every direction - weapons need a larger safety radius.",
            "The empty-handed ladder substantially complete - weapons examine the art, they do not introduce it.",
            "Supervised paired practice only; solo suburi may be drilled alone once the forms are set.",
        ],
        "standards": [
            "Aiki-ken and aiki-jo follow the Aikikai/Iwama weapons syllabus: ken suburi, jo suburi, paired kata.",
            "The riai (weapons/empty-hand unity) principle follows O-Sensei's teaching preserved by Morihiro Saito.",
            "Weapons safety distance and supervised paired practice are universal dojo standards.",
        ],
        "citations": [CIT_AIKIKAI, CIT_UESHIBA, CIT_SAOTOME, CIT_WESTBROOK],
        "sig_lens": (
            "The Signature read: the weapons forms are the covenant of "
            "the true line - the oath that distance and timing are real "
            "things, measured in wood, and every empty-handed promise "
            "below will be examined against them. Where the public "
            "record teaches the suburi, the Signature lens salutes the "
            "examiners: the armory's highest shelf holds the wooden "
            "sword, grading everything beneath it."
        ),
    },
]

