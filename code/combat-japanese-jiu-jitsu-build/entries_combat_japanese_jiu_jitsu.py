#!/usr/bin/env python3
"""Entries for the Japanese Jiu-Jitsu Combat databases (Manon's combat
orders 2026-10-17, combat batch 2).

Pre-authoring verification 2026-10-17: the 68 titles were run through
code/dedupe_gate.py against the WHOLE system (manifest + shard indexes)
before any record was written - zero cross-database collisions. Sibling
combat batches were also read directly (combat-judo, combat-karate,
combat-brazilian-jiu-jitsu) so this database stays in its own lane:
traditional and modern Japanese jujutsu - atemi, kansetsu-waza, nage-waza,
osae-waza, shime-waza - with Japanese terminology and translations, and
no title taken by another combat database.

So this build creates two NEW databases, 34 ladder-ordered records each:

  combat-japanese-jiu-jitsu            - Japanese Jiu-Jitsu Combat Database
                                        (public-harvest: real, fact-checked
                                        Japanese jujutsu - koryu classical
                                        schools and modern gendai lineages -
                                        stances, distance, mind states,
                                        falling, rolling, vital points,
                                        escapes, strikes, joint locks,
                                        throws, pins, and strangles; every
                                        record a technique with HOW TO DO IT
                                        step-by-step body mechanics;
                                        standard references Draeger and
                                        Smith 1969; Skoss 1997; Mol 2001;
                                        Ratti and Westbrook 1973; Friday
                                        1997; Hall 2012; Cunningham 2004)
  combat-japanese-jiu-jitsu-signature  - Japanese Jiu-Jitsu Combat Signature
                                        Database
                                        (his original Signature Combat
                                        Method applied to Japanese jujutsu:
                                        every technique a covenant of body
                                        mechanics, the dojo the armory of
                                        the Signature system, kuzushi the
                                        oath between attacker and defender,
                                        and control the handshake that ends
                                        the fight; src signature, titles
                                        suffixed " (Signature Edition)",
                                        never presented as authentic public
                                        record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBJJJ- (public) and JAH-CBJJJS- (signature), verified free
in the manifest id_prefix values and in every shard index file (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_japanese_jiu_jitsu.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos before
the merger step.

Civilian martial-arts instruction only. Nothing on neutralizing or
defeating military or defense-grade systems.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Combat Method "
            "applied to Japanese jujutsu: every technique a covenant of body "
            "mechanics, the dojo the armory of the Signature system, kuzushi "
            "the oath between attacker and defender, and control the "
            "handshake that ends the fight. Clearly labeled Signature-made, "
            "never presented as authentic public record.")

CIT_DRAEGER = ("Draeger D, Smith RW. Comprehensive Asian Fighting Arts. "
               "Kodansha International; 1969.")
CIT_SKOSS = ("Skoss M, editor. Koryu Bujutsu: Classical Warrior Traditions "
             "of Japan, Vol. 1. Koryu Books; 1997.")
CIT_MOL = ("Mol S. Classical Fighting Arts of Japan: A Complete Guide to "
           "Koryu Jujutsu. Kodansha International; 2001.")
CIT_RATTI = ("Ratti O, Westbrook A. Secrets of the Samurai: A Survey of the "
             "Martial Arts of Feudal Japan. Tuttle Publishing; 1973.")
CIT_FRIDAY = ("Friday KF. Legacies of the Sword: The Kashima-Shinryu and "
              "Samurai Martial Culture. University of Hawaii Press; 1997.")
CIT_HALL = ("Hall DA. Encyclopedia of Japanese Martial Arts. Kodansha USA; "
            "2012.")
CIT_CUNNINGHAM = ("Cunningham D. Taiho-Jutsu: Law and Order in the Age of "
                  "the Samurai. Tuttle Publishing; 2004.")

ENTRIES = [
    {
        "key": "shisei",
        "name": "Shisei: The Ready Stances of Jujutsu",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Shisei means posture, and in Japanese jujutsu it is the first "
            "technique because every throw, lock, and strike is built on how "
            "you stand. The two mother postures are shizentai, the natural "
            "stance with feet about shoulder width and weight even, and "
            "jigotai, the defensive stance with feet wider, knees bent, and "
            "hips lowered so the center of gravity drops. From these come "
            "the working stances: hidari hanmi and migi hanmi, the "
            "half-body stances that present one side forward and shield the "
            "vital points behind the lead shoulder. A correct stance does "
            "three jobs at once: it keeps balance hard to break, it loads "
            "the legs like springs for explosive movement, and it hides the "
            "targets an attacker wants. Beginners drill stance transitions "
            "until the body drops into jigotai without thought, because a "
            "stance you have to think about is a stance that arrives too "
            "late."
        ),
        "how_it_works": (
            "Stand in shizentai: feet under the hips, toes slightly out, "
            "knees soft and unlocked, spine tall, chin tucked, hands open at "
            "mid height. Feel the weight spread evenly across both feet, "
            "pressure through the whole sole, never the toes alone. To take "
            "jigotai, step one foot a half-step wider and bend both knees "
            "until the thighs take the load; the hips sink straight down, "
            "never forward over the knees. For hidari hanmi, turn the left "
            "side forward forty-five degrees, left foot ahead, right foot "
            "back, weight sixty percent on the rear leg so the front leg is "
            "free to kick or step. Keep the shoulders over the hips and the "
            "head over the shoulders - a vertical spine is a strong spine. "
            "Drill the change: partner pushes your chest lightly, and you "
            "drop from shizentai to jigotai without stepping, absorbing the "
            "push through the bent knees. When the stance holds against the "
            "push and you can still move in any direction on the next "
            "breath, the posture is correct."
        ),
        "key_points": [
            "Shizentai is the natural stance: even weight, soft knees, tall spine - the stance of readiness, not of fighting.",
            "Jigotai lowers the center of gravity by bending the knees and widening the base, making kuzushi - balance breaking - far harder to apply against you.",
            "Hanmi presents a half-body target: the lead side probes and the rear side carries the weight, keeping one leg always free to move.",
            "The spine stays vertical over the hips; leaning forward hands the attacker your balance before the fight starts.",
            "Stance is trained as a reflex: drill the drop from shizentai to jigotai against a partner's push until it happens without thought.",
        ],
        "requirements": [
            "A flat training surface with room to step in all four directions.",
            "Feet positioned deliberately: shizentai hip-width, jigotai wider with knees tracking over the toes.",
            "Knees bent and spring-loaded, never locked - locked knees cannot absorb or explode.",
            "Vertical spine with the chin tucked and the eyes on the partner, not the floor.",
            "Hands open and alive at mid height, elbows heavy and close to the ribs.",
        ],
        "standards": [
            "Posture follows the classical descriptions in Mol, Classical Fighting Arts of Japan, and Ratti and Westbrook, Secrets of the Samurai.",
            "Weight distribution is verifiable: a partner's light chest push must be absorbed by the legs, not the upper body.",
            "Stance transitions are drilled symmetrically - hidari and migi hanmi receive equal training time.",
        ],
        "citations": [CIT_MOL, CIT_RATTI, CIT_HALL],
        "sig_lens": (
            "The Signature read: stance is the first covenant. Where public "
            "teaching files shizentai and jigotai as postures, the Signature "
            "Combat Method files them as promises - the feet promise the "
            "ground they will not leave it, the knees promise the body they "
            "will carry it, and the spine promises both that it will stand "
            "straight between them."
        ),
    },
    {
        "key": "maai",
        "name": "Maai: Distance and Timing in Jujutsu",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Maai is the combative distance between two fighters, and "
            "controlling it is controlling the fight. Classical jujutsu "
            "names three distances: toma, the long distance where neither "
            "fighter can reach the other without a full step; issoku-itto-"
            "no-maai, the one-step-one-sword distance where a single stride "
            "lands a technique; and chikama, the close distance where "
            "elbows, knees, locks, and throws live. Maai is not only space "
            "but time: the distance divided by the speed of the attack is "
            "the time you have to respond, so managing distance is managing "
            "the clock. Skilled fighters never stand still in maai; they "
            "pulse it, drifting in and out of reach to force the opponent "
            "to step, and every step an opponent takes is information about "
            "intention. All of jujutsu's throws assume correct maai - "
            "kuzushi fails at the wrong distance because the lever arms are "
            "wrong."
        ),
        "how_it_works": (
            "Face a partner in shizentai. Extend your arm: if your fingertips "
            "cannot touch their shoulder, you are at toma. Step in until a "
            "single step would let your palm reach their chest - that is "
            "issoku-itto-no-maai, the fighting distance where jujutsu "
            "techniques begin. One more half-step puts you at chikama, "
            "chest to chest, where throws and locks happen. Drill the pulse: "
            "from issoku-itto-no-maai, take one sliding step back as the "
            "partner steps in, keeping the exact same gap - this is maai "
            "control, never letting them set their distance. Then reverse: "
            "step in as they step back, closing without rushing. Add timing: "
            "have the partner raise a hand to strike, and enter to chikama "
            "on the first movement of their shoulder, not on the completed "
            "strike. When you can hold the gap against their advance and "
            "close it on their first twitch, you own the maai."
        ),
        "key_points": [
            "Toma, issoku-itto-no-maai, and chikama are the three classical distances: out of reach, one step away, and clinch range.",
            "Maai is space divided by speed: the same gap gives less reaction time against a faster attacker, so distance must grow with danger.",
            "Fighters pulse the distance instead of freezing in it, forcing the opponent to step and reveal intention with every step.",
            "Every throw and lock assumes correct maai - kuzushi applied at the wrong distance fails because the lever arms are wrong.",
            "Enter on the beginning of the opponent's motion, not its completion: the shoulder twitch is the signal, the strike is too late.",
        ],
        "requirements": [
            "A partner and enough floor to step a full stride in every direction.",
            "The three distances learned by feel: fingertip reach, one-step reach, and chest-to-chest.",
            "Footwork that preserves stance while moving - sliding steps, never crossing the feet or hopping.",
            "Eyes on the opponent's center and shoulders, reading the start of motion rather than the finished technique.",
            "The discipline to hold distance under pressure instead of backing straight up or charging in.",
        ],
        "standards": [
            "Distance doctrine follows the classical maai descriptions in Ratti and Westbrook, Secrets of the Samurai, and Friday, Legacies of the Sword.",
            "Issoku-itto-no-maai is verifiable: one committed step must land the practitioner's palm on the partner's chest.",
            "Timing drills are cooperative at first - the partner telegraphs clearly - and sharpen only as control is proven.",
        ],
        "citations": [CIT_RATTI, CIT_FRIDAY, CIT_HALL],
        "sig_lens": (
            "The Signature read: maai is the oath of distance. Where public "
            "teaching files toma and chikama as measurements, the Signature "
            "Combat Method files them as a negotiation - every step a "
            "question, every held gap an answer, and the fighter who asks "
            "better questions wins before a hand is laid."
        ),
    },
    {
        "key": "mushin_zanshin",
        "name": "Mushin and Zanshin: Mind States of the Fighter",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Jujutsu trains the mind before the body, through two classical "
            "mind states. Mushin means no-mind: not emptiness, but a mind "
            "that does not stick to any one thought, fear, or plan, so it "
            "can respond to whatever actually happens. A fighter stuck on "
            "the idea of throwing freezes when the throw fails; a fighter "
            "in mushin flows to the next technique without hesitation. "
            "Zanshin means remaining mind: the alertness that continues "
            "after a technique lands. The fight is not over when the "
            "opponent falls - zanshin keeps the posture ready, the eyes "
            "watching, and the body balanced until the encounter is truly "
            "finished. Together with fudoshin, the immovable mind that fear "
            "cannot shake, these states are trained like muscles: through "
            "breathing drills, through randori pressure, and through the "
            "discipline of finishing every repetition with full awareness "
            "rather than relaxing at the moment of success."
        ),
        "how_it_works": (
            "Begin with breathing: sit in seiza, spine tall, and breathe in "
            "four counts through the nose, hold two, exhale four through "
            "the mouth. Let each exhale carry tension out of the shoulders. "
            "This is the on-ramp to mushin - a settled nervous system "
            "sticks to nothing. Next, drill non-sticking: a partner feeds "
            "slow attacks - a wrist grab, a lapel grab, a slow punch - and "
            "you respond with the first technique that fits, without "
            "deciding in advance which it will be. If you planned kote "
            "gaeshi and the grab changes, let the plan die and take what is "
            "there. That release is mushin in practice. Then drill zanshin: "
            "after every throw in practice, land in a balanced stance facing "
            "the partner, hands up, eyes on them, for a full two seconds "
            "before bowing or resetting. Never turn your back on a fallen "
            "partner in drill; never drop your hands when the technique "
            "succeeds. When calm breathing survives hard randori and "
            "awareness survives victory, the mind states are taking root."
        ),
        "key_points": [
            "Mushin is a mind that does not stick: no frozen plan, no rehearsed fear, just response to what is actually happening.",
            "Zanshin is alertness after the technique: posture ready, eyes watching, balance kept until the encounter is truly over.",
            "Fudoshin, the immovable mind, is built the same way - pressure exposure that proves fear can be felt without being obeyed.",
            "Breathing drills are the on-ramp: a settled nervous system is the physical basis of a non-sticking mind.",
            "Zanshin is trained as choreography first - the two-second hold after every throw - until it becomes character.",
        ],
        "requirements": [
            "A quiet space for breathing practice: seiza or a chair, spine tall, shoulders down.",
            "A cooperative partner for non-sticking drills, feeding slow varied attacks without ego.",
            "The discipline to finish every repetition with zanshin - no relaxing at the moment of success.",
            "Randori or pressure drills, scaled to the student, to test the mind states under stress.",
            "Patience: mind states are measured in months of practice, not single sessions.",
        ],
        "standards": [
            "Mind-state doctrine follows the classical treatments in Friday, Legacies of the Sword, and Hall, Encyclopedia of Japanese Martial Arts.",
            "Training stays secular and practical: attention, breathing, and habit - no mystical claims are made for ordinary psychology.",
            "Pressure testing is always scaled and consensual; the mind is hardened by graduated challenge, never by trauma.",
        ],
        "citations": [CIT_FRIDAY, CIT_HALL, CIT_SKOSS],
        "sig_lens": (
            "The Signature read: the mind is the first armory. Where public "
            "teaching files mushin and zanshin as attitudes, the Signature "
            "Combat Method files them as equipment - mushin the blade that "
            "never dulls on a stuck thought, zanshin the sheath that stays "
            "ready after the cut."
        ),
    },
    {
        "key": "kumiuchi",
        "name": "Kumiuchi: Classical Grappling Engagement",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Kumiuchi is the grappling of the armored samurai, and the root "
            "from which all jujutsu throws and locks grew. On the "
            "battlefield, swords broke and armor turned blades, so warriors "
            "closed chest to chest, seized the opponent's armor and limbs, "
            "and threw or pinned to finish with a short blade. Classical "
            "kumiuchi therefore starts from the clinch: one hand controls "
            "the opponent's sleeve or wrist, the other the lapel or the "
            "back of the neck, the head tucked to the side, hips heavy. "
            "Every modern jujutsu engagement echoes this: the grip fight "
            "that decides who throws whom. Training kumiuchi teaches the "
            "three truths of the clinch - whoever controls the head "
            "controls the spine, whoever controls the sleeve controls the "
            "arm, and whoever moves their hips first usually wins."
        ),
        "how_it_works": (
            "Face a partner at chikama. Your lead hand takes their sleeve "
            "just above the wrist, thumb inside, fingers wrapped tight; "
            "your rear hand grips the lapel at collarbone height, elbow "
            "heavy and close to your ribs. Tuck your head to the outside of "
            "their lead shoulder so your forehead is not available to be "
            "pushed. Sink into jigotai - the clinch is wrestled with the "
            "legs, not the arms. Now the grip fight: when they grab your "
            "sleeve, circle your hand inside their grip and strip it with a "
            "sharp downward rotation of the wrist; when they take your "
            "lapel, pin their hand to your chest with your palm and turn "
            "your body, peeling the grip at its weakest angle. Drill "
            "pummeling: both partners fight for the inside position, "
            "swimming the arms over and under, heads jockeying for the "
            "dominant side. The round ends when one partner holds both "
            "inside grips and head position for three seconds. Control the "
            "head, control the sleeve, move the hips first."
        ),
        "key_points": [
            "Kumiuchi is armored grappling: chest-to-chest engagement where sleeve, lapel, and head position decide everything.",
            "Head position is king: tuck yours to safety and fight to put your forehead where their chin wants to be.",
            "The clinch is wrestled with the legs - jigotai hips, not arm strength, win the grip fight.",
            "Strip grips at their weakest angle: circle inside a sleeve grip, peel a lapel grip by turning the body.",
            "Pummeling drills the entry: swimming for inside position until both grips and head control are held for three seconds.",
        ],
        "requirements": [
            "A partner and a gi or sturdy jacket - kumiuchi is grip fighting and needs cloth to grip.",
            "Sleeve grip thumb-inside and lapel grip at collarbone height, elbows heavy at the ribs.",
            "Head tucked outside the partner's lead shoulder, never forehead to forehead.",
            "Jigotai base maintained through the whole exchange - no standing tall in the clinch.",
            "A cooperative start: grip fighting begins light and hardens only as control is proven.",
        ],
        "standards": [
            "Kumiuchi history and method follow Mol, Classical Fighting Arts of Japan, and Cunningham, Taiho-Jutsu.",
            "Grip breaks are practiced on cloth grips only, with the partner's hand free to release - never against locked fingers.",
            "Head-position drilling forbids headbutts; the forehead is placed, never struck with.",
        ],
        "citations": [CIT_MOL, CIT_CUNNINGHAM, CIT_RATTI],
        "sig_lens": (
            "The Signature read: the clinch is the handshake of war. Where "
            "public teaching files kumiuchi as grappling history, the "
            "Signature Combat Method files it as the original contract - "
            "two warriors agreeing, hand to sleeve, that the stronger "
            "covenant of position will decide."
        ),
    },
    {
        "key": "ukemi_hard",
        "name": "Ukemi on Hard Ground: Jujutsu Falling Principles",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Ukemi means receiving the body, and jujutsu's falling art was "
            "forged for battlefields and streets, not mats. The principle "
            "is energy distribution: a fall that lands on one point breaks "
            "that point, while a fall spread across the whole back, the "
            "slapping arm, and the tucked chin leaves the fighter able to "
            "rise. The back fall, koho ukemi, lands with the chin crushed "
            "to the chest, the back rounded, and one or both arms slapping "
            "the ground at forty-five degrees to bleed off force. The side "
            "fall, yoko ukemi, lands along the whole side seam of the body "
            "with the same slap. The forward roll, zenpo kaiten ukemi, "
            "turns a face-first fall into a diagonal roll from shoulder to "
            "opposite hip. On hard ground the roll matters most: it converts "
            "a stop into a continuation, and a fighter who can roll can "
            "fall down stairs, off curbs, and out of throws and stand up "
            "fighting."
        ),
        "how_it_works": (
            "Start from a squat for koho ukemi: cross your arms over your "
            "chest, tuck your chin hard to your chest so the back of your "
            "head cannot strike, and roll backward, slapping both arms "
            "down at forty-five degrees the instant your back touches. The "
            "slap must land flat - palm and forearm together - and slightly "
            "before the torso, so the arms take the first shock. Exhale "
            "sharply on impact; a full lung is a rigid lung. For yoko "
            "ukemi, stand on one leg, swing the other across, and fall "
            "sideways onto the whole side of the body, bottom arm slapping, "
            "top leg landing across to stop the roll. For the forward roll, "
            "kneel, place one hand down, and roll diagonally from that "
            "shoulder across the back to the opposite hip, tucking the head "
            "so the neck never touches. Drill on mats until the slap is "
            "automatic, then on thin carpet, then on grass - hard ground is "
            "earned in stages, never rushed. The test: thrown unexpectedly "
            "in drill, you slap, tuck, exhale, and rise without a pause."
        ),
        "key_points": [
            "Spread the fall: one-point landings break, whole-body landings with a slap distribute the force.",
            "Chin to chest always - the back of the head striking ground is the injury ukemi exists to prevent.",
            "The slap lands flat, palm plus forearm, a breath before the torso, bleeding off the first shock.",
            "Exhale on impact: the sharp breath keeps the torso from locking rigid around full lungs.",
            "Hard ground is earned in stages - mats, then thin carpet, then grass - never rushed to concrete.",
        ],
        "requirements": [
            "Mats for the learning stage, progressing to firmer surfaces only when the slap is automatic.",
            "Chin tucked to the chest on every fall, without exception.",
            "Flat arm slaps at forty-five degrees, landing just before the torso.",
            "A partner or coach to spot the first weeks of rolling practice.",
            "The rule of gradualism: new surfaces only after clean silent falls on the current one.",
        ],
        "standards": [
            "Falling method follows the ukemi treatments in Draeger and Smith, Comprehensive Asian Fighting Arts, and Mol, Classical Fighting Arts of Japan.",
            "Hard-surface progression is mandatory in this curriculum - no student practices on concrete before demonstrating clean falls on grass.",
            "Neck safety is absolute: any drill that risks head impact is stopped and rebuilt from the kneeling version.",
        ],
        "citations": [CIT_DRAEGER, CIT_MOL, CIT_HALL],
        "sig_lens": (
            "The Signature read: falling is the covenant with the ground. "
            "Where public teaching files ukemi as safety, the Signature "
            "Combat Method files it as a promise kept at speed - the body "
            "swears to the earth that it will arrive spread and breathing, "
            "and the earth, so sworn, lets it rise."
        ),
    },
    {
        "key": "taihenjutsu",
        "name": "Taihenjutsu: Rolling and Body Changing",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Taihenjutsu is the art of changing the body: rolls, turns, and "
            "evasions that move the fighter out of the line of attack while "
            "keeping balance and awareness. Where ukemi receives a fall, "
            "taihenjutsu spends movement as currency - a forward roll, mae "
            "kaiten, that carries you past a lunging attacker; a backward "
            "roll, ushiro kaiten, that turns a push into distance; a "
            "pivoting turn, tenkan, that lets a grab slide off into empty "
            "air. Classical schools drilled taihenjutsu as the bridge "
            "between being attacked and counterattacking: the roll ends in "
            "a stance, the stance is already aimed at the opponent, and "
            "zanshin never lapsed in between. Done well, the defender seems "
            "to disappear from where the attack was aimed and reappear "
            "where the counter is easiest."
        ),
        "how_it_works": (
            "For mae kaiten, the forward roll: from shizentai, step forward "
            "with the right foot, drop the right hand to the ground inside "
            "the foot, tuck the chin, and roll diagonally from the right "
            "shoulder across the back to the left hip. The head never "
            "touches; the roll is shoulder to hip, never over the crown. "
            "Stand up at the end facing the same direction you started - "
            "the roll travels forward, not sideways. For ushiro kaiten, sit "
            "back over one hip, tuck the chin, and roll backward over the "
            "same-side shoulder, slapping as the back lands, coming up to "
            "the feet facing the original direction. For tenkan, the "
            "pivoting evasion: as the partner pushes your chest, step the "
            "rear foot in a half-circle behind you, turning the body one "
            "hundred eighty degrees so their push slides past your "
            "shoulder. Drill the chain: partner pushes, you tenkan offline, "
            "drop to mae kaiten past their side, and rise in jigotai facing "
            "them. When the roll ends in stance with eyes on the partner, "
            "taihenjutsu is working."
        ),
        "key_points": [
            "Taihenjutsu spends movement as currency: rolls and turns buy escape from the line of attack.",
            "The forward roll travels shoulder to opposite hip, diagonally - never over the crown of the head.",
            "Tenkan turns a straight push into a miss: the half-circle step lets force slide past the shoulder.",
            "Every roll ends in a stance, facing the opponent, with zanshin unbroken - the roll is a relocation, not a retreat.",
            "Ushiro kaiten turns a backward shove into distance: sit, tuck, roll over the shoulder, slap, rise.",
        ],
        "requirements": [
            "Mats for learning rolls, with the same gradual firming as ukemi training.",
            "Chin tucked and the rolling line diagonal across the back on every repetition.",
            "A partner to provide the push for tenkan and the chase for rolling escapes.",
            "Landings that finish in shizentai or jigotai, never sprawled or turned away.",
            "Eyes that find the partner before the feet finish moving - awareness leads the body up.",
        ],
        "standards": [
            "Rolling method follows the taihenjutsu treatments in Mol, Classical Fighting Arts of Japan, and Hall, Encyclopedia of Japanese Martial Arts.",
            "No roll is practiced over the crown of the head at any stage; diagonal shoulder-to-hip is the only line.",
            "Tenkan is drilled cooperatively first - the partner pushes straight and steady, never yanking.",
        ],
        "citations": [CIT_MOL, CIT_HALL, CIT_DRAEGER],
        "sig_lens": (
            "The Signature read: the roll is a disappearing oath. Where "
            "public teaching files taihenjutsu as evasion, the Signature "
            "Combat Method files it as relocation with intent - the body "
            "swears to leave the line of attack and reappear exactly where "
            "the counter is easiest."
        ),
    },
    {
        "key": "kyusho",
        "name": "Kyusho: The Vital-Point Map of the Body",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Kyusho are the vital points: places where nerves run shallow, "
            "bones sit close under skin, or organs hang unprotected, so "
            "that a small strike produces a large effect. Jujutsu's atemi "
            "was never about brute force; it was about precision, and the "
            "kyusho map is the chart of that precision. The classical list "
            "includes kasumi at the temple, where the temporal artery runs "
            "shallow; uto between the eyes; jinchu at the philtrum under "
            "the nose; suigetsu at the solar plexus, where the breath "
            "lives; denko at the floating ribs; myojo below the navel at "
            "the tanden; kote at the wrist joint; and hiji at the elbow. "
            "Each point has a correct striking tool - kasumi takes the "
            "knife hand, suigetsu the fist or palm heel, kote the edge of "
            "the hand in a lock-assisted strike. The map is studied slowly, "
            "on one's own body first, because a fighter who cannot find the "
            "points on themselves cannot find them on a moving opponent."
        ),
        "how_it_works": (
            "Learn the map on your own body first. Press your fingertips "
            "lightly to the temple and feel the pulse at kasumi; tap the "
            "philtrum gently to locate jinchu; press two fingers into the "
            "hollow below the sternum to find suigetsu and feel how the "
            "breath catches. Memorize each point's tool: temple and neck "
            "take the knife hand, solar plexus the seiken fist or shotei "
            "palm, ribs the elbow, wrist the tegatana edge. Drill location "
            "on a cooperative partner: they stand still, eyes open, and "
            "you touch each point with the correct tool at zero power, "
            "naming it aloud - kasumi, suigetsu, denko - until the map is "
            "automatic. Then add movement: the partner walks toward you and "
            "you touch the point as they enter range, still at zero power. "
            "Power comes last and only on padded targets, because kyusho "
            "are trained for control first. The standard is precision "
            "under motion: name the point, touch it with the right tool, "
            "while both bodies move."
        ),
        "key_points": [
            "Kyusho are shallow nerves, thin bone cover, and unprotected organs - small strikes, large effects, through precision not force.",
            "The classical map includes kasumi (temple), uto (between eyes), jinchu (philtrum), suigetsu (solar plexus), denko (ribs), myojo (tanden), kote (wrist).",
            "Every point has a correct tool: knife hand for temple and neck, fist or palm for solar plexus, elbow for ribs.",
            "The map is learned on one's own body first, then touched at zero power on a partner, then located under motion.",
            "Power is trained last and only on padded targets - kyusho study is control first, always.",
        ],
        "requirements": [
            "A memorized point list with location and correct striking tool for each.",
            "A cooperative partner willing to stand for zero-power location drills.",
            "Padded targets (focus mitts, body shield) before any point is struck with force.",
            "The rule of touch before power: no point is struck hard until it can be touched precisely while moving.",
            "Medical respect: neck and temple points are located, never struck hard in partner drill.",
        ],
        "standards": [
            "Point locations follow the kyusho treatments in Ratti and Westbrook, Secrets of the Samurai, and Hall, Encyclopedia of Japanese Martial Arts.",
            "Partner drills cap contact at a touch for head and neck points; force work is pad-only.",
            "Students must recite point, location, and tool from memory before advancing to motion drills.",
        ],
        "citations": [CIT_RATTI, CIT_HALL, CIT_MOL],
        "sig_lens": (
            "The Signature read: the map is a covenant of precision. Where "
            "public teaching files kyusho as targets, the Signature Combat "
            "Method files each point as a sworn place - the body promises "
            "that a true strike will answer, and the fighter promises to "
            "earn that answer with control first."
        ),
    },
    {
        "key": "tehodoki",
        "name": "Tehodoki: Wrist-Grab Releases",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Tehodoki is the family of escapes from wrist grabs, and the "
            "first lock-and-escape principle every jujutsu student learns: "
            "the grip is always weakest at the thumb. A hand gripping the "
            "wrist closes with four fingers on one side and only the thumb "
            "on the other, so the escape always drives toward the thumb's "
            "side, where a single digit must hold against the whole arm. "
            "The basic tehodoki works against a same-side grab: the "
            "defender's grabbed hand becomes a wedge, the elbow drops to "
            "anchor it, and the body turns so the wrist screws out through "
            "the thumb gap. Against a cross grab the principle mirrors. "
            "Tehodoki teaches the master rule of all jujutsu escapes - do "
            "not fight strength with strength; find the structural weak "
            "point of the hold and pour the whole body through it."
        ),
        "how_it_works": (
            "Partner grabs your right wrist with their right hand, "
            "thumb on top. Do not pull away - pulling feeds their grip. "
            "Instead, make a fist to thicken the wrist, drop your elbow "
            "toward your hip to anchor the arm, and step your right foot "
            "back and around while turning your body to the right. Your "
            "wrist rotates so the thin edge drives against their thumb, "
            "and the turning body supplies the force - the arm is only the "
            "transmission. The release pops as the wrist screws through "
            "the thumb gap. For the cross grab - their left hand on your "
            "right wrist - the escape goes the other way: raise the elbow "
            "slightly, rotate the wrist over their thumb side, and turn "
            "the body left. Drill both sides until the turn, not the pull, "
            "is the reflex. The test: the partner grabs without warning "
            "during walking drill, and the wrist is free before the second "
            "step lands."
        ),
        "key_points": [
            "Every wrist grip is weakest at the thumb: one digit against the whole arm is the structural flaw to exploit.",
            "Never pull straight out of a grab - pulling feeds the grip; rotate and turn through the thumb gap instead.",
            "The elbow drops to anchor the arm and the body turn supplies the force; the wrist is only the transmission.",
            "Same-side and cross grabs escape in mirrored directions - both must be drilled until the turn is reflexive.",
            "Tehodoki is the master lesson of escapes: find the hold's weak point and pour the whole body through it.",
        ],
        "requirements": [
            "A partner gripping at honest strength - but never with locked fingers that cannot release.",
            "The fist made before the turn, thickening the wrist into a wedge.",
            "Elbow anchored down at the hip, body turning as one piece.",
            "Rotation directed at the thumb side of the grip, whichever hand grabbed.",
            "Both sides drilled equally; the cross grab gets the same repetitions as the same-side grab.",
        ],
        "standards": [
            "Escape mechanics follow the tehodoki treatments in Mol, Classical Fighting Arts of Japan, and Cunningham, Taiho-Jutsu.",
            "Grips are released the instant the escape lands - the partner never white-knuckles through the technique.",
            "Speed is added only after clean slow releases; the turn must be correct before it is fast.",
        ],
        "citations": [CIT_MOL, CIT_CUNNINGHAM, CIT_DRAEGER],
        "sig_lens": (
            "The Signature read: the thumb is the broken promise in every "
            "grip. Where public teaching files tehodoki as an escape, the "
            "Signature Combat Method files it as the first lesson in "
            "reading weakness - one digit swore to hold the arm, and the "
            "whole body collects on that lie."
        ),
    },
    {
        "key": "ryote_mochi",
        "name": "Ryote Mochi Hazushi: Two-Hand Grab Escape",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Ryote mochi is the two-hand grab: the attacker seizes one of "
            "your wrists with both hands, committing their whole upper "
            "body to holding a single point. It looks strong and is "
            "structurally brittle - two hands on one wrist means both of "
            "the attacker's arms are occupied, their elbows are committed "
            "forward, and their balance leans into the grip. The classical "
            "escape turns that commitment into the weapon: the defender "
            "sinks, rotates the grabbed wrist into a wedge, and drives the "
            "whole body in a circle that the attacker's two committed arms "
            "cannot follow. Because both hands grip the same wrist, both "
            "thumbs sit on the same side, and the escape needs only one "
            "gap. Ryote mochi hazushi is the foundation of all two-on-one "
            "defense in jujutsu, and the drill where students first feel "
            "how commitment becomes vulnerability."
        ),
        "how_it_works": (
            "Partner seizes your right wrist with both hands. Sink at once "
            "into jigotai - height is leverage, and the lower body wins. "
            "Make a fist, drop the elbow to your ribs, and note where their "
            "thumbs lie: both on the same side of your wrist. That side is "
            "the door. Step your right foot in a half-circle to the right, "
            "turning your body like a door swinging on its hinge, and let "
            "your wrist rotate so its thin edge drives into the thumb gap. "
            "Your circling body drags their committed arms across their own "
            "center line, where arms are weakest. The grip breaks as their "
            "thumbs are pried by the rotation and their balance is pulled "
            "into the circle. Finish in hanmi facing them, hands up - the "
            "escape ends in readiness, not in a chase. Drill with the "
            "partner increasing grip strength gradually; the circle must "
            "work against full commitment, because a half-hearted drill "
            "teaches a half-true escape."
        ),
        "key_points": [
            "Two hands on one wrist is brittle: both attacker arms committed forward, balance leaning into the grip.",
            "Both thumbs sit on the same side of the wrist - one gap serves the whole escape.",
            "Sink first into jigotai: height is leverage and the lower body wins the circle.",
            "The body turns like a hinged door, dragging the committed arms across their own weak center line.",
            "The escape ends in hanmi with hands up - readiness, not pursuit, is the finish.",
        ],
        "requirements": [
            "Immediate sinking to jigotai the instant the grab lands - no standing tall against two committed arms.",
            "Fist made to wedge the wrist, elbow anchored at the ribs.",
            "A true half-circle step, not a shuffle - the body must travel around the grip.",
            "Rotation aimed at the thumbs' side, verified before the turn begins.",
            "Graduated partner resistance, from light holds to full commitment, as the circle proves itself.",
        ],
        "standards": [
            "Escape mechanics follow the ryote mochi treatments in Mol, Classical Fighting Arts of Japan, and Skoss, Koryu Bujutsu.",
            "Partners release the grip the moment it breaks - no hanging on to prove strength.",
            "The finish position is checked every repetition: hanmi, hands up, eyes on the partner.",
        ],
        "citations": [CIT_MOL, CIT_SKOSS, CIT_CUNNINGHAM],
        "sig_lens": (
            "The Signature read: commitment is the attacker's oath, and "
            "oaths can be collected. Where public teaching files ryote "
            "mochi hazushi as an escape, the Signature Combat Method files "
            "it as the first collection - two hands swore to hold one "
            "wrist, and the turning body calls in the debt."
        ),
    },
    {
        "key": "kata_mochi",
        "name": "Kata Mochi Hazushi: Lapel-Grab Defense",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Kata mochi is the lapel grab: the attacker seizes your gi or "
            "jacket at the chest with one hand, usually to pull you into a "
            "punch or to pin you for a strike. The grab anchors them to "
            "you, which is their mistake - the anchored hand cannot defend, "
            "and the pulling arm extends their balance forward. Classical "
            "jujutsu answers the lapel grab by attacking the grabbing arm "
            "itself: pin their hand to your chest with your palm so it "
            "cannot release, then turn your body, converting their anchor "
            "into a lever that bends the wrist and shoulder. From there the "
            "paths branch - kote gaeshi if the wrist presents, ude garami "
            "if the elbow presents, or a simple off-balancing throw if they "
            "resist. The lesson of kata mochi is that every grip is a "
            "two-way connection, and the defender gets to use it too."
        ),
        "how_it_works": (
            "Partner grabs your left lapel with their right hand and pulls. "
            "Do not step back - stepping back tightens their weapon. Step "
            "slightly in and to the side, and slap your right palm down "
            "over their grabbing hand, pinning it to your chest. Your palm "
            "is the lid; their hand is trapped under it. Now turn your "
            "body to the left, pivoting on the balls of the feet. The turn "
            "does two things: it bends their wrist backward against your "
            "chest, and it drags their extended arm across their body, "
            "breaking their balance forward. Keep the pin: if they try to "
            "pull the hand free, follow the turn and let the wrist bend "
            "take them down into kote gaeshi. If they stiffen the arm "
            "instead, slide your pinning hand up to their elbow and fold "
            "it into ude garami. Drill the entry - palm pin plus body turn "
            "- until the hand is trapped before the pull finishes. The "
            "grab is a gift; the turn is the thank-you."
        ),
        "key_points": [
            "A lapel grab anchors the attacker to you: the grabbing hand cannot defend and the pulling arm extends their balance.",
            "Pin their hand to your chest with your palm - the lid that turns their anchor into your lever.",
            "Never step straight back from a lapel grab; step in and turn, converting the pull into their off-balancing.",
            "The pinned wrist bends against your chest as you turn - kote gaeshi waits if they resist, ude garami if they stiffen.",
            "Every grip is a two-way connection: the defender is allowed to use the attacker's anchor too.",
        ],
        "requirements": [
            "A gi or sturdy jacket - the technique needs cloth to pin against.",
            "The palm pin landing before the attacker's pull completes.",
            "A committed body turn on the balls of the feet, not an arm-only twist.",
            "The trapped hand held through the whole turn - release it and the lever vanishes.",
            "Follow-up awareness: the escape branches to wrist or elbow technique the moment resistance shows its shape.",
        ],
        "standards": [
            "Defense mechanics follow the kata mochi treatments in Mol, Classical Fighting Arts of Japan, and Cunningham, Taiho-Jutsu.",
            "Wrist pressure is applied gradually - the partner taps when the bend is felt, and the turn stops at the tap.",
            "Cloth grips are practiced on sturdy gis; torn clothing stops the drill, not the technique.",
        ],
        "citations": [CIT_MOL, CIT_CUNNINGHAM, CIT_HALL],
        "sig_lens": (
            "The Signature read: the anchor is a shared covenant. Where "
            "public teaching files kata mochi hazushi as a defense, the "
            "Signature Combat Method files it as a repossession - the "
            "attacker tied their hand to your chest, and the turning body "
            "forecloses on the knot."
        ),
    },
    {
        "key": "empi_uchi",
        "name": "Empi Uchi: Elbow Strikes in the Clinch",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Empi uchi are elbow strikes, and in jujutsu they are the "
            "king of close-range atemi because the clinch is where jujutsu "
            "lives. A punch needs distance to travel; an elbow needs only "
            "the width of the chest. The elbow is a natural bludgeon - "
            "dense bone, short lever, driven by the rotation of the whole "
            "torso - and it strikes along lines the hands cannot guard "
            "when bodies are tangled. The family includes yoko empi, the "
            "horizontal elbow swung across like a hook; tate empi, the "
            "rising elbow driven up under the chin or into the solar "
            "plexus; and otoshi empi, the dropping elbow smashed down onto "
            "the collarbone or the top of a bent-over opponent. Jujutsu "
            "pairs elbows with grappling: the lock controls the head, the "
            "elbow punishes the opening, and the threat of the elbow makes "
            "the lock easier to finish."
        ),
        "how_it_works": (
            "Start from the clinch: sleeve grip with the lead hand, lapel "
            "grip with the rear, head tucked safe. For yoko empi, release "
            "the sleeve grip and swing the elbow horizontally across, "
            "rotating the hips and shoulders as one piece - the power comes "
            "from the torso turn, not the arm swing. The striking surface "
            "is the point and the inch above it; the fist stays clenched "
            "to brace the joint. For tate empi, drop the hips slightly and "
            "drive the elbow straight up, as if lifting the opponent's "
            "chin with the point of the elbow, hips thrusting forward to "
            "add the body's mass. For otoshi empi, when the opponent bends "
            "forward under your control, raise the elbow high and drop the "
            "whole body weight through it onto the target. Drill on pads "
            "held at clinch distance - the pad holder stands chest to "
            "chest, so the range stays honest. The rule of the elbow: short "
            "path, whole body, and the other hand always guarding or "
            "controlling while the elbow flies."
        ),
        "key_points": [
            "The elbow needs only the width of the chest to strike - it is the clinch-range weapon, where punches cannot travel.",
            "Yoko empi swings horizontal, tate empi rises, otoshi empi drops: three lines covering every opening the clinch offers.",
            "Power comes from torso rotation and hip drive, never from the arm alone - the elbow is the hammer head, the body is the handle.",
            "The striking surface is the point of the elbow with the fist clenched to brace the joint.",
            "Jujutsu pairs the elbow with control: the lock holds the head still, the elbow punishes the opening it creates.",
        ],
        "requirements": [
            "Clinch position first: grips and head safety established before any elbow is thrown.",
            "Pads held at true clinch distance - the range must stay honest, chest to chest.",
            "Full torso rotation on the horizontal elbow, hip thrust on the rising elbow, body drop on the falling elbow.",
            "The non-striking hand guarding or controlling on every repetition - no free hands in the clinch.",
            "A braced elbow joint: fist clenched, wrist straight, on every strike.",
        ],
        "standards": [
            "Elbow method follows the atemi treatments in Draeger and Smith, Comprehensive Asian Fighting Arts, and Mol, Classical Fighting Arts of Japan.",
            "Elbows are thrown at pads and shields only - never at a partner's head or body in drill.",
            "The pad holder wears headgear and holds with braced arms; wild elbows stop the drill.",
        ],
        "citations": [CIT_DRAEGER, CIT_MOL, CIT_HALL],
        "sig_lens": (
            "The Signature read: the elbow is the short oath. Where public "
            "teaching files empi uchi as close-range strikes, the Signature "
            "Combat Method files each as a promise kept at arm's length - "
            "no travel, no warning, just the whole torso arriving through "
            "a single point of bone."
        ),
    },
    {
        "key": "shotei_uchi",
        "name": "Shotei Uchi: Palm-Heel Strikes",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Shotei uchi is the palm-heel strike: the heel of the open hand "
            "driven forward like a piston, and one of jujutsu's most "
            "practical atemi because it hits hard without breaking the "
            "striker's hand. A fist concentrates force on small knuckles "
            "that fracture on skulls; the palm heel spreads the same body "
            "weight across a broad, well-padded surface braced by the "
            "wrist. The strike travels straight from the chamber at the "
            "hip or chest, the hips snap forward as it extends, and at "
            "impact the fingers pull back so only the heel lands. Targets "
            "are the chin, driving the head back; the solar plexus, "
            "suigetsu, emptying the lungs; and the chest, shoving the whole "
            "body into kuzushi. Jujutsu favors the palm heel for the "
            "follow-through too: after the strike lands, the open hand is "
            "already shaped to grab, push, or guide into the next lock or "
            "throw."
        ),
        "how_it_works": (
            "Stand in hanmi, hands up. Chamber the striking hand at the hip, "
            "palm facing up, elbow tucked. Drive the palm heel straight at "
            "the target - chin height for the head, solar plexus for the "
            "body - snapping the hip of the striking side forward as the "
            "arm extends. The wrist locks at the last instant, fingers "
            "pulled back and up so the heel of the palm is the only thing "
            "that arrives. Hit with the falling step: step the front foot "
            "forward as the strike extends so the body weight pours through "
            "the heel. Snap it back along the same line - the strike "
            "returns faster than it went out, and the hand comes back "
            "already open, ready to grip a lapel or check an arm. Drill on "
            "a heavy bag or pad at the two heights, ten strikes each hand, "
            "checking after each that the wrist stayed straight and the "
            "fingers stayed clear. Then drill the conversion: palm heel to "
            "the pad, and the same hand flows straight into a lapel grip - "
            "strike becoming control without a pause."
        ),
        "key_points": [
            "The palm heel hits hard without breaking the striker's hand: broad surface, padded, wrist-braced.",
            "The strike travels straight from chamber with a hip snap; the body weight pours through the falling step.",
            "Fingers pull back at impact so only the heel lands - curled fingers are broken fingers.",
            "Prime targets: the chin driving the head back, suigetsu emptying the lungs, the chest manufacturing kuzushi.",
            "The open hand after the strike is already shaped to grab - atemi flows into control without a pause.",
        ],
        "requirements": [
            "A locked wrist at impact, verified by slow shadow repetitions before any bag work.",
            "Fingers retracted on every strike - the heel alone makes contact.",
            "Hip snap and falling step on every repetition; arm-only palm strikes are forbidden in drill.",
            "Targets at honest heights: chin and solar plexus on the bag, never imagined.",
            "The return faster than the delivery, hand open and ready to grip.",
        ],
        "standards": [
            "Palm-heel method follows the atemi treatments in Draeger and Smith, Comprehensive Asian Fighting Arts, and Hall, Encyclopedia of Japanese Martial Arts.",
            "Strikes land on bags and pads only; partner work is touch-contact to the chest guard at most.",
            "Wrist alignment is checked by the coach before power is added - bent wrists stop the drill.",
        ],
        "citations": [CIT_DRAEGER, CIT_HALL, CIT_MOL],
        "sig_lens": (
            "The Signature read: the palm is the honest hammer. Where "
            "public teaching files shotei uchi as a safe strike, the "
            "Signature Combat Method files it as the covenant of the open "
            "hand - it swears to hit without breaking itself, and to "
            "arrive already shaped for whatever comes next."
        ),
    },
    {
        "key": "ude_garami",
        "name": "Ude Garami: The Entangled Armlock",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Ude garami means entangled armlock: the figure-four bent-arm "
            "lock that attacks the shoulder by bending the elbow against "
            "its nature. One hand threads behind the opponent's bent arm "
            "and grips your own wrist, forming the figure four; the "
            "opponent's elbow becomes the fulcrum, their shoulder the "
            "target, and your whole torso the lever. It is called entangled "
            "because the arms weave together so completely that strength "
            "cannot untangle them - only the shoulder's anatomy decides "
            "when the fight ends. Jujutsu applies ude garami everywhere: "
            "from the mount, from side control, from a standing lapel grab, "
            "and as the finish when an opponent stiff-arms against a throw. "
            "The lock is a dial, not a switch: pressure rises gradually, "
            "and the tap is honored the instant it comes."
        ),
        "how_it_works": (
            "From side control, the opponent's near arm bends as they push "
            "at you. Thread your near hand under their bent arm and grip "
            "your own far wrist - the figure four is now closed around "
            "their arm. Keep their elbow pinned to your chest or the mat; "
            "the elbow must not float, because a floating elbow is a "
            "escaping elbow. To apply, lift their elbow upward while your "
            "torso presses down through the weave - the shoulder rotates "
            "toward its limit as the elbow rises. Apply in small "
            "increments, watching their face: the tap comes as pressure, "
            "not pain, and you release the instant it comes. Standing "
            "version: from the kata mochi pin, when they stiffen the "
            "grabbing arm, slide your pinning hand to their elbow, thread "
            "the figure four, and turn your body - the same shoulder "
            "rotation finishes them on their feet. Drill the entry slowly, "
            "ten times each side, stopping at the first sign of pressure "
            "every time. The lock is learned as control first; the finish "
            "is a dial you turn only as far as the tap allows."
        ),
        "key_points": [
            "The figure four weaves the arms so completely that strength cannot untangle them - anatomy decides the finish.",
            "The opponent's elbow is the fulcrum and must stay pinned; a floating elbow is an escaping elbow.",
            "Lifting the elbow while the torso presses down rotates the shoulder toward its limit with whole-body leverage.",
            "Ude garami applies from the ground and standing: side control, mount, lapel-grab defense, stiff-arm counters.",
            "The lock is a dial, not a switch: pressure rises in increments and the tap is honored instantly.",
        ],
        "requirements": [
            "The figure-four grip closed completely: hand threaded under, gripping your own wrist, no gaps.",
            "The opponent's elbow pinned to your chest or the mat through the entire application.",
            "Gradual pressure with eyes on the partner - the tap ends the technique immediately.",
            "Both sides drilled equally, ground and standing entries both practiced.",
            "A partner who taps early and honestly; ego has no place under a shoulder lock.",
        ],
        "standards": [
            "Lock mechanics follow the kansetsu-waza treatments in Mol, Classical Fighting Arts of Japan, and Draeger and Smith, Comprehensive Asian Fighting Arts.",
            "Shoulder locks are applied slowly in drill - no cranking, no bouncing, no surprises.",
            "The tap is sacred: any partner may stop any lock drill at any moment for any reason.",
        ],
        "citations": [CIT_MOL, CIT_DRAEGER, CIT_CUNNINGHAM],
        "sig_lens": (
            "The Signature read: the weave is a knot of promises. Where "
            "public teaching files ude garami as an armlock, the Signature "
            "Combat Method files it as entanglement made covenant - four "
            "limbs swearing together that the shoulder will travel only "
            "where the weaver allows."
        ),
    },
    {
        "key": "kote_gaeshi",
        "name": "Kote Gaeshi: The Wrist-Turn Throw",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Kote gaeshi means wrist return: the throw that twists the "
            "wrist outward and down, turning the hand into a steering wheel "
            "for the whole body. It is the most famous technique in "
            "Japanese jujutsu, and for good reason - the wrist is a small "
            "joint with a short lever, so modest force applied with correct "
            "rotation topples a much larger attacker. The mechanics are "
            "pure: grip the attacker's hand so the wrist bends outward, "
            "rotate the hand in a circle that carries the elbow up and the "
            "shoulder over, and step through as their balance pours off "
            "the edge of their base. The throw finishes with the attacker "
            "sprawled and the wrist still controlled, which is why koryu "
            "schools prized it for arresting: the technique ends with the "
            "prisoner held, not merely thrown."
        ),
        "how_it_works": (
            "Partner grabs your lapel with the right hand. Pin their hand "
            "with your left palm, then wrap your right hand around their "
            "fingers from below, thumb in their palm. Their wrist is now "
            "yours. Rotate their hand outward and down in a tight circle - "
            "as if turning a key away from their body - while stepping "
            "your right foot through toward their rear. The rotation bends "
            "the wrist to its limit; the step carries their shoulder past "
            "their toes. Keep the circle small and the wrist close to your "
            "center: a wide circle lets them pull free, a tight circle "
            "gives them nowhere to go. As they fall, follow them down, "
            "keeping the wrist twisted and pinned to the ground beside "
            "their head. They land with the arm extended and controlled - "
            "the arrest finish. Drill at walking speed until the circle is "
            "smooth, then add speed in small steps. Never crank the wrist "
            "after the fall; the throw is the technique, and the pin is "
            "control, not punishment."
        ),
        "key_points": [
            "The wrist is a small joint with a short lever: correct rotation topples attackers far larger than the defender.",
            "The hand becomes a steering wheel - rotating it outward and down carries elbow, shoulder, and balance with it.",
            "Keep the circle tight and the wrist near your center; wide circles let the attacker pull free.",
            "Step through toward their rear as the wrist turns: rotation plus footwork is what pours them off their base.",
            "The koryu finish is an arrest: follow down, keep the wrist pinned, control the arm - thrown and held, not merely thrown.",
        ],
        "requirements": [
            "The grip on the fingers secured before any rotation begins - thumb in the palm, wrap complete.",
            "A tight outward-down circle, wrist kept close to the defender's center.",
            "The stepping foot traveling through toward the attacker's rear on the turn.",
            "Follow-down control: the wrist stays twisted and pinned after the fall.",
            "A partner who falls cleanly and taps the instant the wrist reaches its limit.",
        ],
        "standards": [
            "Throw mechanics follow the kote gaeshi treatments in Mol, Classical Fighting Arts of Japan, and Skoss, Koryu Bujutsu.",
            "Wrist rotation stops at the tap - no cranking past the fall, no pressure on a downed partner's wrist.",
            "Speed is added in small steps only after the circle is smooth at walking pace.",
        ],
        "citations": [CIT_MOL, CIT_SKOSS, CIT_HALL],
        "sig_lens": (
            "The Signature read: the wrist is the smallest steering wheel. "
            "Where public teaching files kote gaeshi as a famous throw, "
            "the Signature Combat Method files it as the purest covenant "
            "of leverage - the tiniest joint swearing to steer the whole "
            "body, and keeping its word."
        ),
    },
    {
        "key": "waki_gatame",
        "name": "Waki Gatame: The Armpit Armlock",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Waki gatame means armpit lock: the straight armlock that traps "
            "the opponent's extended arm in the defender's armpit and "
            "attacks the elbow by hyperextension. Where ude garami bends "
            "the arm to attack the shoulder, waki gatame straightens it to "
            "attack the elbow - the armpit becomes the fulcrum, the "
            "defender's torso the lever, and the elbow joint the victim. "
            "It is the classic answer to the straight punch and the "
            "stiff-arm: the attacker extends the arm to strike or push, "
            "and the defender catches the extension, clamps it under the "
            "armpit, and sits back. Koryu schools taught it as a standing "
            "arrest technique because it controls a resisting arm with "
            "minimal effort once the armpit closes - the lock is held by "
            "body structure, not by grip strength."
        ),
        "how_it_works": (
            "Partner pushes your chest with a straight right arm. Parry "
            "the arm slightly across your body with your left hand and step "
            "your left foot forward, turning your body so their extended "
            "arm threads under your left armpit. Clamp down: squeeze the "
            "armpit shut on their arm just above the elbow, and grip their "
            "wrist with both hands to keep it from sliding out. Their elbow "
            "must point upward with the arm straight - rotate their wrist "
            "so the elbow crease faces the sky. Now sit back and down, "
            "lowering your weight through the armpit onto the arm while "
            "your hands lift the wrist. The elbow hyperextends between the "
            "downward armpit and the upward hands. Apply by sinking, not by "
            "yanking - the body weight does the work in a smooth descent. "
            "The partner taps the moment pressure arrives, and you release "
            "by standing slightly, never by ripping the arm free. Drill "
            "the clamp first without pressure: thread, squeeze, check the "
            "elbow crease faces up. Only then add the sit-back, in "
            "increments, honoring every tap."
        ),
        "key_points": [
            "The armpit is the fulcrum: clamped above the elbow, it turns the defender's sinking body into elbow pressure.",
            "Waki gatame answers extension - the straight punch, the stiff-arm push - by catching the arm at full reach.",
            "The elbow crease must face the sky; rotated wrong, the lock attacks nothing and the arm escapes.",
            "Pressure comes from sitting back with body weight, never from yanking the wrist.",
            "Once the armpit closes, structure holds the lock - grip strength is freed for the wrist control.",
        ],
        "requirements": [
            "The arm threaded fully under the armpit, clamped above the elbow joint.",
            "Elbow crease rotated skyward before any pressure is applied.",
            "Both hands controlling the wrist so the arm cannot slide out of the clamp.",
            "A smooth sit-back descent for pressure - no jerking, no bouncing.",
            "Instant release at the tap, by standing slightly out of the lock.",
        ],
        "standards": [
            "Lock mechanics follow the kansetsu-waza treatments in Mol, Classical Fighting Arts of Japan, and Draeger and Smith, Comprehensive Asian Fighting Arts.",
            "Elbow locks are drilled with zero speed until the clamp position is perfect on both sides.",
            "Hyperextension pressure is capped at the first tap - the lock is a control dial, never a breaking tool in practice.",
        ],
        "citations": [CIT_MOL, CIT_DRAEGER, CIT_HALL],
        "sig_lens": (
            "The Signature read: the armpit is a vise that swore an oath. "
            "Where public teaching files waki gatame as an armlock, the "
            "Signature Combat Method files it as structural custody - the "
            "body promises the arm it will go nowhere, and keeps the "
            "promise by sitting down."
        ),
    },
    {
        "key": "hiji_kannuki",
        "name": "Hiji Kannuki: The Elbow Bolt Lock",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Hiji kannuki means elbow bolt: the lock that bars the "
            "opponent's arm across your body like a door bolt sliding into "
            "its socket. The defender captures the attacker's arm, lays it "
            "across the chest or thigh, and presses down on the elbow while "
            "the wrist is held - the arm becomes a lever, the defender's "
            "body the fulcrum, the elbow the hinge under attack. It appears "
            "in koryu arrest arts wherever a grabbed wrist needs to become "
            "a controlled prisoner: the initial grab defense flows into "
            "kote gaeshi's rotation, and if the attacker pulls back against "
            "the wrist turn, the arm straightens into the bolt. The bolt "
            "is valued because it works standing, needs no ground, and "
            "leaves the defender's other hand free - for the sword, the "
            "radio, or the next attacker."
        ),
        "how_it_works": (
            "Partner grabs your right wrist with their right hand. Begin "
            "the tehodoki turn, rotating toward their thumb - and when "
            "they yank back against the rotation, let their pull straighten "
            "their arm. Catch their wrist with your left hand and lay their "
            "extended arm across your chest, elbow crease up, your right "
            "forearm pressing down just above their elbow. Step your right "
            "foot back to lengthen the lever and sink your weight: your "
            "chest becomes the anvil, your forearm the hammer, and their "
            "elbow the thing between. Press down smoothly through the hips, "
            "never with a bounce. Their options die one by one: pulling "
            "back feeds the bolt, bending the elbow collapses into your "
            "chest, and going with the pressure walks them to the ground. "
            "Finish standing, arm barred, free hand raised in guard. Drill "
            "the transition - grab, turn, yank, bolt - as one flowing "
            "sentence until the attacker's resistance triggers the lock "
            "instead of defeating it."
        ),
        "key_points": [
            "The arm bars across the defender's body like a door bolt: chest the anvil, forearm the hammer, elbow between.",
            "Hiji kannuki is born from resistance - the attacker's pull-back against the wrist turn straightens the arm into the lock.",
            "It works standing with one hand, leaving the defender's other hand free for guard or the next threat.",
            "Pressure is a smooth hip-driven descent, never a bounce; bouncing is how elbows get injured in drill.",
            "Every escape attempt feeds the lock: pull back tightens the bolt, bend collapses into the chest, yield goes to the ground.",
        ],
        "requirements": [
            "The attacker's arm captured across the chest with the elbow crease facing up.",
            "The defender's forearm pressing just above the elbow joint, wrist controlled by the other hand.",
            "A lengthening step and sinking hips to load body weight into the bolt.",
            "Smooth continuous pressure - the tap ends it instantly.",
            "The free hand held in guard through the whole technique, never dropped.",
        ],
        "standards": [
            "Lock mechanics follow the kansetsu-waza treatments in Mol, Classical Fighting Arts of Japan, and Skoss, Koryu Bujutsu.",
            "The bolt is drilled from the grab defense it grows out of - never as an isolated arm yank.",
            "Partners tap at first pressure; the drill resets and the entry is refined, not forced.",
        ],
        "citations": [CIT_MOL, CIT_SKOSS, CIT_CUNNINGHAM],
        "sig_lens": (
            "The Signature read: resistance signs the bolt's warrant. Where "
            "public teaching files hiji kannuki as an armlock, the "
            "Signature Combat Method files it as judo of the will - the "
            "attacker's own pull-back swearing the arm straight, and the "
            "defender merely notarizing it across the chest."
        ),
    },
    {
        "key": "ashi_garami",
        "name": "Ashi Garami: The Leg-Entanglement Lock",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Ashi garami means entangled leg lock: the family of techniques "
            "that weaves the defender's legs around the opponent's leg and "
            "attacks the knee and ankle by twisting the lower leg against "
            "the trapped thigh. Jujutsu's newaza ground fighting treats the "
            "legs as the heavy artillery - stronger than arms, harder to "
            "escape, and able to hold a much larger opponent. The basic "
            "ashi garami threads one leg inside the opponent's leg and one "
            "outside, the feet hooking together to form a closed loop; "
            "bridging the hips then rotates their shin while the thigh is "
            "pinned. Classical schools used it to cripple a standing "
            "attacker's base and to finish grounded opponents who defended "
            "all upper-body locks. It demands the deepest respect in "
            "training, because knees do not forgive the way shoulders do."
        ),
        "how_it_works": (
            "From open guard on the ground, the opponent stands with one "
            "leg forward. Thread your right leg inside their forward leg "
            "and your left leg outside it, hooking your feet together "
            "behind their calf - the loop is closed around their lower "
            "leg. Control their hips with your hands on their belt or "
            "thighs so they cannot step out. To apply, bridge your hips "
            "up and rotate your torso, turning their shin inward while "
            "your leg loop pins the thigh. The knee is caught between the "
            "rotating shin and the fixed thigh. Apply with the slow "
            "pressure of the hips, in millimeters - this lock gives almost "
            "no warning before injury, so the partner taps at the first "
            "tightness and you release before the tap is even finished. "
            "Drill the entanglement without pressure until the loop closes "
            "in one motion: inside leg, outside leg, hook the feet, hands "
            "to the hips. Speed of entry is the skill; pressure is barely "
            "touched in practice, because knees are forever."
        ),
        "key_points": [
            "The legs are the heavy artillery of newaza: stronger than arms, harder to escape, able to hold larger opponents.",
            "The loop - inside leg, outside leg, hooked feet - traps the lower leg while the hands pin the hips.",
            "Bridging the hips rotates the shin against the fixed thigh; the knee is caught in the middle.",
            "Knee locks give almost no warning before injury: partners tap at first tightness, release precedes the tap's end.",
            "Entry speed is the trained skill; finishing pressure is barely touched in practice because knees are forever.",
        ],
        "requirements": [
            "The leg loop fully closed - inside thread, outside wrap, feet hooked - before any pressure.",
            "Hands controlling the opponent's hips so the leg cannot be withdrawn.",
            "Hip-bridge pressure applied in millimeters, with eyes on the partner's face.",
            "A partner who taps at tightness, not pain, and a defender who releases early.",
            "Both legs drilled as the threading leg; the loop must close from either side.",
        ],
        "standards": [
            "Leg-lock mechanics follow the newaza treatments in Mol, Classical Fighting Arts of Japan, and Draeger and Smith, Comprehensive Asian Fighting Arts.",
            "Knee attacks are demonstrated slowly and released early - this curriculum forbids full finishing pressure on knees in drill.",
            "Any knee discomfort stops the drill for the day; knees do not get second chances.",
        ],
        "citations": [CIT_MOL, CIT_DRAEGER, CIT_HALL],
        "sig_lens": (
            "The Signature read: the loop is a snare that swore patience. "
            "Where public teaching files ashi garami as a leg lock, the "
            "Signature Combat Method files it as the heaviest covenant - "
            "the legs promising to hold what the arms never could, and "
            "the knee answering only to slow truth."
        ),
    },
    {
        "key": "kubi_nage",
        "name": "Kubi Nage: The Neck Throw",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Kubi nage means neck throw: the hip throw that controls the "
            "opponent by the neck instead of the sleeve, turning the head "
            "into the steering wheel of the whole body. The defender's arm "
            "wraps around the back of the opponent's neck, the hip loads "
            "under their center, and the throw rotates them over the hip "
            "with the neck guiding the arc. Koryu schools valued it for "
            "the street, where no gi exists to grip - the neck is always "
            "available, clothed or not. It is also the throw that most "
            "clearly teaches kuzushi's truth: control the head and the body "
            "follows, because the spine can only go where the head leads "
            "it. In training it is practiced with full care for the neck, "
            "which is guided firmly but never cranked."
        ),
        "how_it_works": (
            "From the clinch, when the opponent pushes forward, slide your "
            "right arm around the back of their neck, hand cupping - never "
            "squeezing - the far side of the neck. Step your right foot to "
            "their right foot and pivot, loading your right hip under their "
            "center while pulling their head down and across with the neck "
            "grip. Your hip is the fulcrum, their head the end of the "
            "lever: bend forward at the waist and rotate, and their body "
            "arcs over your hip. Guide the head through the whole throw - "
            "the neck grip steers, it does not wrench. They land on their "
            "side with you still holding the neck lightly, in position to "
            "follow to a pin. Drill the entry without the throw first: "
            "neck grip, hip load, head pull, freeze - check that your hip "
            "is truly under their center and their head is controlled. "
            "Only then add the rotation, and only with a partner who falls "
            "well. The neck is guided, always; cranking is expulsion from "
            "the drill."
        ),
        "key_points": [
            "The neck grip turns the head into the steering wheel: the spine follows wherever the head is led.",
            "Kubi nage needs no gi - the neck is always available, which is why koryu prized it for the street.",
            "The hip loads under the opponent's center as the fulcrum; the head provides the long lever.",
            "Guide the neck firmly but never crank it: steering is the technique, wrenching is injury.",
            "The throw ends with the neck still lightly controlled, in position to follow to a pin.",
        ],
        "requirements": [
            "A cupping neck grip - hand open on the far side of the neck, never squeezing the throat.",
            "The hip truly loaded under the opponent's center, verified in freeze drills before throwing.",
            "Head pull coordinated with hip rotation: lever and fulcrum work as one.",
            "A partner with clean side-fall ukemi, because neck throws punish bad falling.",
            "The neck guided through the entire arc, pressure released the moment they land.",
        ],
        "standards": [
            "Throw mechanics follow the nage-waza treatments in Mol, Classical Fighting Arts of Japan, and Ratti and Westbrook, Secrets of the Samurai.",
            "Neck control is steering only - any crank, jerk, or spike ends the drill immediately.",
            "The entry is frozen and checked before the throw is ever completed at speed.",
        ],
        "citations": [CIT_MOL, CIT_RATTI, CIT_SKOSS],
        "sig_lens": (
            "The Signature read: the head is the rudder the spine obeys. "
            "Where public teaching files kubi nage as a hip throw, the "
            "Signature Combat Method files it as the proof of kuzushi's "
            "oath - control the crown, and the whole body keeps the "
            "promise to follow."
        ),
    },
    {
        "key": "tani_otoshi",
        "name": "Tani Otoshi: The Valley Drop",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Tani otoshi means valley drop: the throw that blocks both of "
            "the opponent's legs from behind and drops them backward into "
            "the valley the defender's body creates. As the opponent steps "
            "forward or resists a forward throw, the defender slides to "
            "their rear corner, extends a leg across behind both of their "
            "legs, and sits down - the blocked legs cannot step back, the "
            "upper body is pulled forward and down, and the opponent falls "
            "backward over the barrier. It is the classical answer to the "
            "stubborn opponent: everyone who resists a forward throw by "
            "leaning back walks directly into the valley. The drop is "
            "total and sudden, which is why ukemi discipline matters - the "
            "partner must slap and tuck the instant the barrier lands."
        ),
        "how_it_works": (
            "Attempt a forward throw - o goshi or seoi nage - and feel the "
            "partner lean back to resist. That resistance is the invitation. "
            "Slide your body to their rear-right corner, stepping your "
            "right foot behind their feet, and extend your right leg "
            "straight across behind both of their legs, foot flexed. Sit "
            "down hard toward your own right hip, pulling their upper body "
            "forward and down across your leg with both hands. Their legs "
            "are dammed by your extended leg; their balance, already "
            "leaning back against your forward throw, has nowhere to go "
            "but over the dam. You land seated with them sprawled across "
            "your leg - keep your leg straight and your toes up so their "
            "weight lands on muscle, not on your knee. The partner's job "
            "is the back fall: chin tucked, arms slapping, the moment the "
            "drop begins. Drill the slide-and-sit without a partner first "
            "to learn the leg placement, then at half speed, then full - "
            "the valley does not forgive lazy ukemi."
        ),
        "key_points": [
            "Tani otoshi punishes backward resistance: the lean that defeats a forward throw feeds the valley drop.",
            "The extended leg dams both of the opponent's legs from behind - no step back exists once the barrier lands.",
            "Sit toward your own hip as you pull their upper body forward: the drop is your weight plus their lean.",
            "Keep the blocking leg straight with toes up; their weight must land on muscle, never on your knee.",
            "The partner's back fall starts the instant the drop begins - the valley does not forgive lazy ukemi.",
        ],
        "requirements": [
            "A genuine forward attack first - the valley drop is a counter to resistance, not an opening move.",
            "The slide to the rear corner completed before the leg extends; position before barrier.",
            "The blocking leg straight, foot flexed, toes up, placed behind both of their legs.",
            "A committed sit-down with the upper-body pull - half-sitting makes half-throws.",
            "A partner with drilled koho ukemi; this throw is never practiced on beginners.",
        ],
        "standards": [
            "Throw mechanics follow the nage-waza treatments in Draeger and Smith, Comprehensive Asian Fighting Arts, and Mol, Classical Fighting Arts of Japan.",
            "The blocking leg position is checked in slow drills - knee safety for the thrower is verified before speed.",
            "Partners must demonstrate clean back falls before being thrown with tani otoshi at any speed.",
        ],
        "citations": [CIT_DRAEGER, CIT_MOL, CIT_HALL],
        "sig_lens": (
            "The Signature read: resistance digs its own valley. Where "
            "public teaching files tani otoshi as a leg block, the "
            "Signature Combat Method files it as the collection on "
            "stubbornness - the backward lean swore it would not be "
            "thrown forward, and the valley keeps that promise literally."
        ),
    },
    {
        "key": "yama_arashi",
        "name": "Yama Arashi: The Mountain Storm Throw",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Yama arashi means mountain storm: the sweeping throw of "
            "Daito-ryu, the koryu school behind much of modern jujutsu and "
            "aikido, and a technique that attacks balance from two "
            "directions at once. One hand pulls the opponent's sleeve or "
            "lapel down and across while the leg sweeps their advancing "
            "foot in the opposite arc - the upper body dragged one way, "
            "the foot swept the other, and balance torn between them like "
            "a tree in a storm. It is taught as the signature of "
            "combination kuzushi: neither the pull nor the sweep would work "
            "alone, but together they leave the opponent with no base and "
            "no posture in the same instant. Advanced students learn its "
            "deeper lesson - that the storm is timed to the opponent's "
            "step, striking exactly as their weight commits to the foot "
            "being swept."
        ),
        "how_it_works": (
            "Face the partner in the clinch, right hand on their left "
            "sleeve. As they step forward with the left foot, pull the "
            "sleeve sharply down and across your body to your right hip - "
            "their upper body follows the pull, weight pouring onto the "
            "stepping foot. At the exact moment their weight commits, "
            "sweep your right leg in a wide arc against the outside of "
            "their left ankle, contacting with the sole and sweeping "
            "through. Pull down-across, sweep through: the two forces open "
            "like scissors, and the partner falls in a wheeling arc. Keep "
            "pulling through the fall - the sleeve hand guides them to a "
            "safe side landing, never letting go until the slap lands. "
            "Drill the timing on a stepping partner first without the "
            "sweep: pull as the foot lands, and feel the weight commit. "
            "Add the sweep only when the pull consistently catches the "
            "step. The storm is not strength; it is the appointment kept "
            "with the opponent's own footstep."
        ),
        "key_points": [
            "Yama arashi attacks balance from two directions: the upper body pulled one way, the foot swept the other.",
            "Neither force works alone - the storm is the combination, timed to a single instant.",
            "The sweep strikes as the opponent's weight commits to the stepping foot; early is weak, late is gone.",
            "The sleeve hand guides the fall through to the mat - control continues past the moment of the throw.",
            "Daito-ryu's signature teaches combination kuzushi: torn between two forces, balance has no answer.",
        ],
        "requirements": [
            "A stepping partner to time against - the throw is drilled on motion, not on statues.",
            "The downward-across pull committed to the hip, not an arm tug.",
            "The sweep contacting the ankle with the sole, arcing through rather than chopping.",
            "Timing verified in pull-only drills before the sweep is ever added.",
            "The guiding hand maintaining control until the partner's slap lands.",
        ],
        "standards": [
            "Throw mechanics follow the Daito-ryu treatments in Mol, Classical Fighting Arts of Japan, and Skoss, Koryu Bujutsu.",
            "Sweep contact is sole-to-ankle only - no kicking at shins or knees in drill.",
            "Partners must show clean yoko ukemi before taking the full storm at speed.",
        ],
        "citations": [CIT_MOL, CIT_SKOSS, CIT_HALL],
        "sig_lens": (
            "The Signature read: the storm keeps appointments. Where "
            "public teaching files yama arashi as Daito-ryu's throw, the "
            "Signature Combat Method files it as the covenant of timing - "
            "the footstep promised to arrive, and the storm swore to be "
            "waiting."
        ),
    },
    {
        "key": "kata_gatame",
        "name": "Kata Gatame: The Shoulder Hold",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Kata gatame means shoulder hold: the pin that traps the "
            "opponent's head and one arm together in a triangle of your "
            "arms and shoulder, and then lies on it. From side control, "
            "the defender threads an arm under the opponent's head and "
            "grips their own arm, enclosing head and shoulder in a closed "
            "loop; dropping the chest onto the loop compresses the "
            "shoulder and the side of the neck at once, making it a pin "
            "that is also a slow strangle. It is the hold that teaches "
            "weight: beginners try to squeeze with the arms, and the "
            "technique fails; advanced students simply lie down correctly, "
            "and the opponent cannot breathe or move. Escapes exist - the "
            "bridging shrimp, the trapped-arm pullout - but all of them "
            "require space, and kata gatame's first lesson is to give "
            "none."
        ),
        "how_it_works": (
            "From side control on the opponent's right side, slide your "
            "right arm under their head, deep, until your hand emerges past "
            "their far shoulder. Grip your own left arm - hand to biceps or "
            "wrist to wrist - closing the triangle around their head and "
            "right arm. Drop your chest onto the triangle, driving your "
            "weight through your right shoulder into their trapped "
            "shoulder. Walk your hips toward their head to tighten the "
            "loop and sprawl your legs back, heavy. Do not squeeze with "
            "the arms - the arms only maintain the loop; the pin is your "
            "body weight lying on the triangle. Hold for the count: in "
            "training, a thirty-second hold against full escape effort "
            "proves the pin. To release, unwrap in reverse - lift the "
            "chest first, then open the grip - so no accidental pressure "
            "lands on the neck. Drill entries from side control until the "
            "thread-and-grip happens in one motion, then drill the weight "
            "drop: the moment the loop closes, the chest is already "
            "falling."
        ),
        "key_points": [
            "The triangle encloses head and one arm together: a pin that compresses shoulder and neck at once.",
            "Weight pins, arms only maintain - lying down correctly beats squeezing every time.",
            "Thread deep under the head and grip your own arm: the loop must close completely or the head slips out.",
            "Walk the hips toward their head and sprawl heavy: every inch of tightening removes an inch of escape space.",
            "Escapes need space, so the hold gives none - tightness is the technique, not a preliminary.",
        ],
        "requirements": [
            "Side control established first - kata gatame is a finish to the position, not a leap.",
            "The threading arm deep under the head, grip on your own arm fully closed.",
            "Chest weight dropped through the shoulder onto the trapped side.",
            "Hips walked in and legs sprawled heavy for the full hold.",
            "Release in reverse - chest up first, then unwrap - to protect the neck.",
        ],
        "standards": [
            "Pin mechanics follow the osae-waza treatments in Draeger and Smith, Comprehensive Asian Fighting Arts, and Mol, Classical Fighting Arts of Japan.",
            "The strangle component is respected: partners tap to pressure and the hold opens at once.",
            "Thirty-second escape-proof holds are the promotion standard for the pin, tested against honest effort.",
        ],
        "citations": [CIT_DRAEGER, CIT_MOL, CIT_HALL],
        "sig_lens": (
            "The Signature read: the triangle is a room with no door. "
            "Where public teaching files kata gatame as a pin, the "
            "Signature Combat Method files it as architecture - the arms "
            "swear the walls, the chest swears the roof, and the weight "
            "swears it will not be lifted."
        ),
    },
    {
        "key": "yoko_shiho_gatame",
        "name": "Yoko Shiho Gatame: Side Four-Quarter Hold",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Yoko shiho gatame means side four-quarter hold: the pin that "
            "controls the opponent from the side by owning all four "
            "quarters of their body - both shoulders and both hips pinned "
            "under the defender's weight. The defender lies across the "
            "opponent's torso at a right angle, one arm threading under "
            "the far shoulder, the other controlling the far hip, chest "
            "heavy on the chest. It is the fundamental pin of jujutsu's "
            "ground game because it is the hardest to escape: the right "
            "angle denies the bridge its direction, the far-side controls "
            "deny the shrimp its space, and the weight distribution denies "
            "the roll its leverage. Students learn that the pin is not "
            "held by strength but by geometry - the cross of the bodies is "
            "the lock, and the body weight is only the key turned in it."
        ),
        "how_it_works": (
            "From side control, drop your chest across their torso so your "
            "bodies form a cross - your spine at ninety degrees to theirs. "
            "Thread your far-side arm under their far shoulder and grip "
            "their far lapel or belt; your near arm reaches over their "
            "near hip to control the far hip. Your head stays low, ear to "
            "their chest, so they cannot sit up into you. Distribute the "
            "weight: sixty percent through the chest onto their torso, "
            "forty percent through the sprawled legs - heavy but mobile. "
            "When they bridge, ride it: let the bridge lift you slightly "
            "and settle back heavier, never fighting the bridge with "
            "strength. When they shrimp, follow the hips - your far-hip "
            "control travels with them. Hold for thirty seconds against "
            "full escape effort; that is the test. To advance, the pin "
            "feeds everything: the far arm is available for ude garami, "
            "the head for kata gatame, the lapel for okuri eri jime. The "
            "cross is the platform; the submissions are the tenants."
        ),
        "key_points": [
            "The right angle is the lock: bodies crossed at ninety degrees deny the bridge its direction.",
            "Four quarters controlled - both shoulders via the underhook, both hips via the far-side grip - leaves no free limb to build on.",
            "Weight splits sixty-forty, chest heavy and legs sprawled: pinned but mobile, never rigid.",
            "Ride the bridge and follow the shrimp: the pin moves with the escape instead of fighting it.",
            "Yoko shiho is the platform pin: armlocks, strangles, and transitions all rent rooms in its cross.",
        ],
        "requirements": [
            "The ninety-degree cross established before settling weight - angle first, heaviness second.",
            "Far shoulder underhooked and far hip controlled; no quarter left unowned.",
            "Head low, ear to their chest, denying the sit-up.",
            "Weight riding, not resisting, the opponent's bridge.",
            "The thirty-second escape-proof hold as the working standard.",
        ],
        "standards": [
            "Pin mechanics follow the osae-waza treatments in Draeger and Smith, Comprehensive Asian Fighting Arts, and Mol, Classical Fighting Arts of Japan.",
            "Escape drills are honest: the bottom partner tries truly, and the pin is rebuilt wherever it leaks.",
            "Cross-angle is checked visually by the coach - parallel bodies are not yoko shiho.",
        ],
        "citations": [CIT_DRAEGER, CIT_MOL, CIT_CUNNINGHAM],
        "sig_lens": (
            "The Signature read: the cross is geometry's oath. Where public "
            "teaching files yoko shiho gatame as a pin, the Signature "
            "Combat Method files it as the right angle made covenant - two "
            "bodies swearing perpendicular, and the weight keeping the "
            "vow."
        ),
    },
    {
        "key": "tate_shiho_gatame",
        "name": "Tate Shiho Gatame: Mounted Four-Quarter Hold",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Tate shiho gatame means mounted four-quarter hold: the pin "
            "from the full mount, knees pinching the opponent's ribs, "
            "chest driving down the center line, both shoulders and both "
            "hips owned from above. Tate - vertical - describes the "
            "defender sitting upright over the opponent, and it is the "
            "most dominant position in jujutsu's ground game because "
            "gravity is a teammate: every bridge lifts the defender's "
            "weight and drops it back heavier, every arm the opponent "
            "extends to push becomes available for a lock, and the head "
            "is always in range of the hands. The mount teaches the "
            "deepest lesson of pins - that control flows downward. The "
            "fighter on top does not chase the fighter below; they pour "
            "weight down the center and let the bottom fighter's own "
            "escapes create the openings for armlocks and strangles."
        ),
        "how_it_works": (
            "Sit astride the opponent's torso, knees tight against their "
            "ribs, toes driving into the mat, hips heavy. Your weight "
            "drives straight down through your center into their solar "
            "plexus - not leaning forward onto your hands, which unloads "
            "the hips, but sitting tall and pouring down. Control their "
            "head with one hand on the far side of the jaw when they turn "
            "away; control their arms by pinning wrists to the mat above "
            "their head. When they bridge hard to one side, post the hand "
            "on that side and let your hips swing low - the low mount "
            "rides the bridge like a saddle. When they trap an arm and "
            "roll, base out with the free hand and hip-heist back to "
            "center. Drill the hold: two minutes on top while the partner "
            "escapes honestly, and you may not submit - only hold, ride, "
            "and recover. That restriction builds the mount as a pin first. "
            "Then open the submissions: the extended arm takes ude garami, "
            "the turned head takes the lapel for okuri eri jime. The mount "
            "is the throne; the submissions are the court."
        ),
        "key_points": [
            "Gravity is a teammate in the mount: every bridge lifts the weight and drops it back heavier.",
            "Sit tall and pour weight down the center - leaning on the hands unloads the hips and frees the bottom fighter.",
            "Knees pinch the ribs, toes drive the mat, hips stay heavy: the mount is a saddle, not a seat.",
            "Ride the bridge low and hip-heist back to center; never chase the bottom fighter with strength.",
            "Control flows downward: the top fighter's patience turns every escape into a submission opening.",
        ],
        "requirements": [
            "Knees tight to the ribs and toes driving - the base that keeps the throne.",
            "Weight poured down the center line, not leaned forward onto the hands.",
            "Head and wrist controls established before any submission is attempted.",
            "Bridge-riding drilled as a skill: post, swing low, recover center.",
            "The two-minute hold-only round as the standard before submissions are added.",
        ],
        "standards": [
            "Pin mechanics follow the osae-waza treatments in Draeger and Smith, Comprehensive Asian Fighting Arts, and Mol, Classical Fighting Arts of Japan.",
            "Mount escapes are practiced honestly from below; the top fighter rebuilds wherever the pin leaks.",
            "Strikes are never part of mount drill in this curriculum - it is a pin and submission platform.",
        ],
        "citations": [CIT_DRAEGER, CIT_MOL, CIT_HALL],
        "sig_lens": (
            "The Signature read: the throne is gravity's covenant. Where "
            "public teaching files tate shiho gatame as the mount, the "
            "Signature Combat Method files it as the downward oath - the "
            "top fighter swearing to pour and not to chase, and every "
            "escape keeping its promise to become an opening."
        ),
    },
    {
        "key": "okuri_eri_jime",
        "name": "Okuri Eri Jime: The Sliding Lapel Strangle",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Okuri eri jime means sliding lapel strangle: the choke that "
            "uses the opponent's own collar as the ligature, sliding one "
            "hand deep along the lapel while the other pulls across. From "
            "behind or from the side, the defender feeds a hand under the "
            "opponent's chin and grips the far lapel deep, then the free "
            "hand grips the near lapel and pulls it across the throat like "
            "drawing a bow - the two lapels scissor the neck between them. "
            "It is the signature strangle of gi jujutsu because the gi is "
            "always there: no strength is needed once the lapels are set, "
            "only the steady pull that tightens the scissors. Classical "
            "schools taught it as the arresting strangle - applied from "
            "behind a resisting prisoner, finished standing, and released "
            "the instant control was established. In training it is "
            "practiced with absolute tap discipline."
        ),
        "how_it_works": (
            "From behind the seated or standing partner, slide your right "
            "hand under their chin - palm down, thumb inside your own "
            "collar line - and grip their left lapel deep, at collarbone "
            "level behind the neck. Your left hand grips their right lapel "
            "at chest level. Now the scissors: pull the left hand across "
            "their throat toward your right hip while the right hand "
            "anchors deep. The right lapel becomes the fixed blade, the "
            "left lapel the moving blade, and the neck is caught between. "
            "Apply by drawing the bow - steady, smooth, no yanking. The "
            "partner taps the moment pressure arrives, and you open both "
            "hands instantly, stepping back to give air. Drill the lapel "
            "feed first without pressure: slide, grip deep, check the "
            "depth - four fingers of lapel past the hand is the standard. "
            "Only then add the cross-pull, in slow increments. The strangle "
            "is a dial: depth first, then the smallest pull that earns the "
            "tap. Never crank, never hold through a tap, never practice "
            "without a watching coach in the early months."
        ),
        "key_points": [
            "The opponent's own collar is the ligature: the gi is always there, so no strength is needed once the lapels are set.",
            "One lapel is the fixed blade gripped deep, the other the moving blade drawn across - the neck caught in the scissors.",
            "Depth is the technique: four fingers of lapel past the gripping hand before any pull begins.",
            "The strangle is a dial, not a switch: steady bow-drawing pressure in slow increments, tap honored instantly.",
            "Classical arresting strangle: finished standing from behind, released the instant control is established.",
        ],
        "requirements": [
            "A gi with sturdy lapels - the technique requires cloth that will not tear under load.",
            "The sliding hand fed under the chin with the lapel gripped deep behind the neck.",
            "The cross-pull drawn smooth like a bow, never yanked.",
            "A partner who taps at first pressure and a defender who opens both hands at the tap.",
            "A coach watching all early strangle practice, without exception.",
        ],
        "standards": [
            "Strangle mechanics follow the shime-waza treatments in Draeger and Smith, Comprehensive Asian Fighting Arts, and Mol, Classical Fighting Arts of Japan.",
            "Strangles are practiced with tap discipline as the first skill taught and the last skill compromised.",
            "No strangle is held past a tap for any reason; no strangle is practiced on a partner who will not tap.",
        ],
        "citations": [CIT_DRAEGER, CIT_MOL, CIT_HALL],
        "sig_lens": (
            "The Signature read: the collar is a borrowed blade. Where "
            "public teaching files okuri eri jime as a lapel choke, the "
            "Signature Combat Method files it as the scissors oath - the "
            "attacker's own garment swearing to serve the defender, and "
            "the defender swearing to release the moment it is sworn."
        ),
    },
    {
        "key": "kata_ha_jime",
        "name": "Kata Ha Jime: Single-Wing Strangle",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Kata ha jime means single-wing strangle: the choke applied "
            "with one arm threaded under the opponent's armpit, the hand "
            "gripping the far lapel, while the other hand reinforces from "
            "behind the head. The threaded arm is the wing - a single "
            "limb that wraps the neck and shoulder together - and the "
            "reinforcing hand behind the head closes the circuit, pressing "
            "the head forward into the loop. It is the strangle of the "
            "clinch and the scramble: wherever an arm shoots under an "
            "armpit in the chaos of a throw attempt, kata ha jime is "
            "waiting. The mechanics are compression, not crushing - the "
            "loop tightens around both sides of the neck at once, and the "
            "tap comes quickly and cleanly. Like all strangles it is "
            "trained as a dial with sacred tap discipline."
        ),
        "how_it_works": (
            "From the standing clinch, when the partner reaches for your "
            "legs or turns into a throw, thread your right arm under their "
            "right armpit, deep, until your hand can grip their left lapel "
            "at the collarbone. Your left hand cups the back of their head "
            "and presses it forward and down into the loop your right arm "
            "makes. Now close the wing: pull the right elbow down toward "
            "your hip while the left hand drives the head into the crook "
            "of the arm. The neck is compressed between your forearm and "
            "their own shoulder, with the head pressure sealing the loop. "
            "Apply in increments - the tap arrives fast with this one. "
            "Release by opening the head hand first, then withdrawing the "
            "threaded arm. Drill the thread as the skill: from every "
            "clinch exchange, the moment an armpit opens, the arm shoots "
            "under and finds the lapel. Depth of the thread is everything; "
            "a shallow wing is just an embrace. Ten clean threads each "
            "side before any pressure is added."
        ),
        "key_points": [
            "The single wing threads under the armpit and grips the far lapel: one limb wrapping neck and shoulder together.",
            "The reinforcing hand behind the head closes the circuit, pressing the head forward into the loop.",
            "Kata ha jime lives in the scramble - wherever an armpit opens during a throw attempt, the wing is waiting.",
            "Compression, not crushing: the loop tightens both sides of the neck at once and the tap comes clean.",
            "Depth of thread is the technique; a shallow wing is just an embrace.",
        ],
        "requirements": [
            "The threading arm deep under the armpit, hand secured on the far lapel.",
            "The head hand pressing forward and down into the loop before pressure begins.",
            "Incremental closing of the wing with eyes on the partner.",
            "Release order: head hand opens first, then the threaded arm withdraws.",
            "Ten clean threads per side drilled before any finishing pressure.",
        ],
        "standards": [
            "Strangle mechanics follow the shime-waza treatments in Mol, Classical Fighting Arts of Japan, and Draeger and Smith, Comprehensive Asian Fighting Arts.",
            "Tap discipline is absolute: the tap opens the strangle instantly, every time.",
            "Scramble entries are drilled cooperatively first - the partner offers the armpit, then hides it gradually.",
        ],
        "citations": [CIT_MOL, CIT_DRAEGER, CIT_CUNNINGHAM],
        "sig_lens": (
            "The Signature read: the wing is a single feather that holds. "
            "Where public teaching files kata ha jime as a strangle, the "
            "Signature Combat Method files it as the oath of the opening - "
            "the armpit swore to stay shut, and the threading arm collects "
            "on the broken promise."
        ),
    },
    {
        "key": "gyaku_juji_jime",
        "name": "Gyaku Juji Jime: Reverse Cross Strangle",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Gyaku juji jime means reverse cross strangle: the choke where "
            "both hands grip the opponent's lapels crossed, but with the "
            "thumbs inside - the reverse of the standard cross strangle's "
            "grip. From the mount or from inside the guard, each hand "
            "slides under the opposite lapel, thumbs in, and the wrists "
            "cross like an X over the throat; pulling the elbows out and "
            "down draws the lapels scissoring across both carotid "
            "arteries. The reverse grip changes the angle of the wrists so "
            "the cutting edges of the forearms - the radius bones - become "
            "the blades, and the strangle bites faster than its standard "
            "cousin. It is an advanced technique because the grip is "
            "harder to set under resistance and the finish demands precise "
            "elbow direction: out and down, never up, lest the strangle "
            "become a mere pull on cloth."
        ),
        "how_it_works": (
            "From the mount, slide your right hand under their left lapel, "
            "thumb inside, gripping deep at the collarbone; slide the left "
            "hand under the right lapel the same way, so the wrists cross "
            "over the throat. Keep the elbows low and tight to your ribs "
            "as you set the grips - high elbows telegraph and invite "
            "defense. To finish, pull both elbows out and down toward the "
            "mat, as if trying to touch your elbows to the ground beside "
            "their head. The crossed wrists drive the lapels scissoring "
            "across the neck, and the radius edges of the forearms become "
            "the blades. The tap comes quickly; honor it by opening both "
            "hands at once. If the partner defends by tucking the chin, "
            "do not force the strangle through the chin - transition: the "
            "grips are already deep for okuri eri jime or the mount "
            "armlock. Drill the grip-setting as the isolated skill: from "
            "the mount, both thumbs-in grips in under three seconds, ten "
            "times. The finish is the easy part once the X is truly set."
        ),
        "key_points": [
            "Thumbs-inside reverses the standard cross: the wrists form an X and the forearm radius edges become the blades.",
            "The reverse angle bites faster than the standard cross - precision of elbow direction is what earns it.",
            "Elbows pull out and down toward the mat, never up: the finish direction is the technique.",
            "Grip-setting under resistance is the hard skill; the crossed X must be truly set before the finish matters.",
            "A tucked chin is not forced through - the deep grips already offer okuri eri jime or the armlock instead.",
        ],
        "requirements": [
            "Both hands thumbs-inside under opposite lapels, gripped deep at the collarbone.",
            "The crossed X of the wrists lying over the throat, elbows low during the set.",
            "The out-and-down elbow pull as the single finishing motion.",
            "Instant two-hand release at the tap.",
            "The three-second grip-setting standard drilled before finishing pressure is added.",
        ],
        "standards": [
            "Strangle mechanics follow the shime-waza treatments in Draeger and Smith, Comprehensive Asian Fighting Arts, and Mol, Classical Fighting Arts of Japan.",
            "Forcing a strangle through a tucked chin is forbidden - transition instead.",
            "Tap discipline is absolute; the strangle opens the instant the tap lands.",
        ],
        "citations": [CIT_DRAEGER, CIT_MOL, CIT_HALL],
        "sig_lens": (
            "The Signature read: the X is a crossed oath. Where public "
            "teaching files gyaku juji jime as a choke, the Signature "
            "Combat Method files it as the reversed covenant - the wrists "
            "swearing across each other, and the elbows keeping the vow "
            "downward."
        ),
    },
    {
        "key": "hadaka_jime",
        "name": "Hadaka Jime: The Naked Strangle",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Hadaka jime means naked strangle: the choke with no gi "
            "required, one forearm across the throat and the other hand "
            "locking behind the head. Hadaka means naked or bare - the "
            "technique needs no clothing, no weapon, only the geometry of "
            "the arms. From behind, the defender's right forearm slides "
            "across the front of the neck, the right hand grips the left "
            "biceps, and the left hand presses behind the head; squeezing "
            "the elbows together closes the triangle and compresses both "
            "sides of the neck. It is the most decisive strangle in "
            "jujutsu and the one that demands the most maturity, because "
            "it works fast and gives little warning. Classical schools "
            "taught it as the final answer when all else failed - and "
            "taught release discipline as its inseparable twin."
        ),
        "how_it_works": (
            "From behind the partner, slide your right forearm across the "
            "front of their neck, the crook of the elbow centered under "
            "the chin - never across the windpipe's front with crushing "
            "force, but settled in the natural hollow. Grip your own left "
            "biceps with the right hand, and place the left hand behind "
            "their head. Expand the chest and draw the elbows together: "
            "the right forearm and the left biceps close like a vise on "
            "both sides of the neck while the head hand prevents escape. "
            "The tap comes in seconds - this is the fastest strangle in "
            "the curriculum. Release by opening the head hand first and "
            "sliding the forearm up and away, stepping back to give air. "
            "Drill the set slowly: forearm placed, biceps gripped, head "
            "hand set, freeze and check - then release without pressure. "
            "Pressure is added only in tiny increments with an experienced "
            "partner, and the tap is honored before it is finished. The "
            "naked strangle is a loaded technique; it is handled like one."
        ),
        "key_points": [
            "Hadaka means bare: no gi, no weapon, only arm geometry - the most decisive and most serious strangle in the art.",
            "The forearm-biceps vise compresses both sides of the neck at once; the head hand seals the only escape.",
            "The elbow crook centers under the chin in the natural hollow - placement, not crushing force, is the technique.",
            "The tap comes in seconds: release begins before the tap ends, head hand first.",
            "It is taught as the final answer with release discipline as its inseparable twin - a loaded technique handled like one.",
        ],
        "requirements": [
            "Rear position secured before the arm slides - no reaching around a facing opponent.",
            "Forearm settled in the hollow under the chin, biceps gripped, head hand placed - the full set checked frozen.",
            "Pressure added in tiny increments, eyes on the partner, with an experienced partner only.",
            "Release order drilled: head hand first, forearm slides up and away, step back for air.",
            "A coach present for all early naked-strangle practice.",
        ],
        "standards": [
            "Strangle mechanics follow the shime-waza treatments in Draeger and Smith, Comprehensive Asian Fighting Arts, and Mol, Classical Fighting Arts of Japan.",
            "The tap is honored before it finishes - any delay is a safety failure, not a technique.",
            "Crushing across the windpipe is forbidden; the strangle compresses the sides of the neck.",
        ],
        "citations": [CIT_DRAEGER, CIT_MOL, CIT_CUNNINGHAM],
        "sig_lens": (
            "The Signature read: the bare arms are the final covenant. "
            "Where public teaching files hadaka jime as the rear choke, "
            "the Signature Combat Method files it as the oath of last "
            "resort - geometry swearing it needs nothing else, and "
            "discipline swearing to release the instant it is answered."
        ),
    },
    {
        "key": "sumi_otoshi",
        "name": "Sumi Otoshi: The Corner Drop",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Sumi otoshi means corner drop: the hand throw that topples "
            "the opponent into the dead corner of their stance with no leg "
            "contact at all. Every stance has a corner where balance "
            "cannot recover - the rear diagonal, where no foot waits to "
            "catch the weight. The defender's hands guide the opponent's "
            "upper body toward that corner while the defender's own body "
            "drops and turns, and the opponent falls into the empty space "
            "their stance forgot. It is the purest hand technique in "
            "jujutsu, the throw that most clearly demonstrates that "
            "kuzushi alone - balance broken at the perfect angle - is "
            "enough. Masters are judged by their sumi otoshi, because "
            "there is nowhere to hide weakness in it: no leg to blame, no "
            "hip to credit, only timing, angle, and the courage to drop "
            "your own weight first."
        ),
        "how_it_works": (
            "Stand facing the partner, right hand on their left lapel, "
            "left hand on their right sleeve. As they step forward with "
            "the right foot, guide their upper body toward their rear "
            "left corner - the dead corner behind their stepping foot. "
            "Your right hand lifts and turns their lapel toward the "
            "corner while your left hand pushes the sleeve across; "
            "simultaneously drop your own weight by bending the knees and "
            "turn your body, pulling them into the void. Your hands draw "
            "a circle that ends pointing at the corner, and your dropping "
            "body is the engine. They fall backward-diagonal into the "
            "space where no foot can catch them. Keep guiding through the "
            "fall - the hands that threw them place them. Drill the "
            "corner-finding first: walk the partner around and feel for "
            "the diagonal where their balance dies, marking it with a "
            "gentle push. Then add your drop. The throw is advanced "
            "because the window is small: the corner exists only for the "
            "instant of the step, and the hands must already be moving."
        ),
        "key_points": [
            "Every stance has a dead corner - the rear diagonal where no foot waits to catch the weight.",
            "Sumi otoshi uses no leg contact: kuzushi at the perfect angle is the entire technique.",
            "The hands draw a circle ending at the corner while the defender's own dropping body powers it.",
            "Masters are judged by this throw because it hides nothing - only timing, angle, and commitment.",
            "The throwing hands guide the fall to the mat; control continues past the moment of the drop.",
        ],
        "requirements": [
            "The dead corner identified by feel before the throw is attempted - walk, push, mark it.",
            "Hands already moving as the partner steps; the window is the instant of the step.",
            "The defender's own weight dropped first - you cannot send them into the void without entering it.",
            "The circular hand path completed toward the corner, never cut short.",
            "Guidance maintained through the landing; the throw places, not abandons.",
        ],
        "standards": [
            "Throw mechanics follow the te-waza treatments in Draeger and Smith, Comprehensive Asian Fighting Arts, and Mol, Classical Fighting Arts of Japan.",
            "Corner-finding drills precede throwing drills - no student attempts the drop before mapping the corner.",
            "Partners take clean back-diagonal falls; hesitant falling stops the drill.",
        ],
        "citations": [CIT_DRAEGER, CIT_MOL, CIT_HALL],
        "sig_lens": (
            "The Signature read: the corner is the forgotten promise of "
            "every stance. Where public teaching files sumi otoshi as a "
            "hand throw, the Signature Combat Method files it as the "
            "purest collection - balance swore the corner was guarded, "
            "and the dropping body proves it was not."
        ),
    },
    {
        "key": "uki_otoshi",
        "name": "Uki Otoshi: The Floating Drop",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Uki otoshi means floating drop: the sacrifice throw where "
            "the defender drops to one knee and the opponent floats over "
            "it, carried by their own forward momentum. As the attacker "
            "pushes or charges, the defender sinks suddenly to the knee "
            "nearest them, pulling their sleeve down and across - the "
            "attacker's driving force, suddenly missing its target, "
            "becomes the energy of their own fall. They float: for an "
            "instant the body is airborne, committed to a direction whose "
            "support just vanished. It is the most timing-dependent throw "
            "in the curriculum, because the knee drop must answer the "
            "push, not anticipate it - early is a wasted knee, late is "
            "being run over. Done correctly it is effortless, the throw "
            "that feels like doing nothing while the attacker flies."
        ),
        "how_it_works": (
            "Face the partner with a sleeve-and-lapel grip. Invite the "
            "push: let them drive forward honestly. The instant their "
            "weight commits forward - not before, not after - drop "
            "straight down onto your right knee, pulling their right "
            "sleeve down and across your body toward your left hip. Your "
            "dropping body is the disappearing support; your pulling hands "
            "are the guidance. Their momentum carries them forward and "
            "over, floating for the breath where their push expected a "
            "wall and found air. Guide the sleeve through the fall so "
            "they land on their side, not their face. Rise as they fall, "
            "ending in hanmi with zanshin. Drill the drop without a "
            "partner first: standing to kneeling in one smooth vertical "
            "line, knee landing soft, fifty times. Then have the partner "
            "push a heavy bag into you so you learn the commitment-feel "
            "without a human flying. Only then take the live push - and "
            "only with a partner whose side falls are automatic, because "
            "the float gives no time to remember ukemi."
        ),
        "key_points": [
            "The attacker's own momentum is the engine: the disappearing support turns their push into their flight.",
            "The knee drop answers the committed push - early is wasted, late is being run over; timing is the technique.",
            "Drop vertically onto the knee in one smooth line; the knee lands soft and the pull guides across.",
            "For an instant the attacker floats: committed to a direction whose support just vanished.",
            "Rise as they fall, ending in hanmi with zanshin - the sacrifice ends in readiness, not on the ground.",
        ],
        "requirements": [
            "A committed forward push to answer - the throw is drilled on honest attacks, not pantomime.",
            "The vertical knee drop landing soft, drilled fifty times solo before any partner work.",
            "Sleeve pull timed to the drop: down and across toward the opposite hip in one motion.",
            "A partner with automatic side-fall ukemi - the float allows no time to remember how to fall.",
            "The rise-with-zanshin finish on every repetition.",
        ],
        "standards": [
            "Throw mechanics follow the sutemi-waza treatments in Draeger and Smith, Comprehensive Asian Fighting Arts, and Mol, Classical Fighting Arts of Japan.",
            "The knee drop is practiced on mats only; hard surfaces are never used for uki otoshi drill.",
            "Partners must demonstrate clean yoko ukemi at speed before taking the live float.",
        ],
        "citations": [CIT_DRAEGER, CIT_MOL, CIT_SKOSS],
        "sig_lens": (
            "The Signature read: the knee is a vanishing oath. Where "
            "public teaching files uki otoshi as a sacrifice throw, the "
            "Signature Combat Method files it as the promise of absence - "
            "the support swearing it was there, and the drop proving it "
            "never was."
        ),
    },
    {
        "key": "tomoe_nage",
        "name": "Tomoe Nage: The Stomach Circle Throw",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Tomoe nage means stomach circle throw: the sacrifice throw "
            "where the defender falls to their back, plants a foot on the "
            "attacker's stomach, and wheels them overhead in a great "
            "circle. Tomoe is the comma-shaped crest, and the throw draws "
            "it in the air with the attacker's body. As the opponent "
            "pushes forward, the defender sits back, the foot catches the "
            "rising center, the hands pull the sleeves down and through, "
            "and the attacker somersaults over in a full arc. It is the "
            "most spectacular throw in jujutsu and one of the most "
            "practical, because it answers the strongest forward attack - "
            "the committed charge - with the least resistance. The "
            "sacrifice is real: the defender gives their own standing "
            "position, trusting the circle to land them ready and the "
            "attacker spent."
        ),
        "how_it_works": (
            "Face the partner with sleeve grips, both hands on sleeves. "
            "As they push forward hard, sit straight back - not down, but "
            "back, falling to your back - and plant the sole of your right "
            "foot on their stomach just below the navel. Pull both sleeves "
            "down toward your own hips as you fall, and extend the leg, "
            "wheeling them up and over in the tomoe circle. Your falling "
            "body is the counterweight; your extending leg is the ramp; "
            "your pulling hands steer the arc. They somersault over and "
            "land beyond your head - keep pulling through the landing so "
            "they arrive on their back, not their head. You finish on your "
            "back with the leg extended, and immediately shrimp to your "
            "side into guard: the sacrifice ends in position, never flat. "
            "Drill the sit-back and foot plant on a crash pad first, "
            "without a partner, until the foot finds the stomach mark "
            "blind. Then throw a cooperative partner who jumps lightly "
            "with the circle. Full commitment comes last, and only with "
            "partners whose breakfalls are fearless."
        ),
        "key_points": [
            "The committed charge is answered with the least resistance: sit back, plant the foot, wheel them over.",
            "The foot on the stomach is the ramp, the falling body the counterweight, the sleeve pulls the steering.",
            "Tomoe draws its comma-crest circle in the air with the attacker's body - pull through the landing.",
            "The sacrifice ends in guard, never flat: shrimp to the side the instant the circle completes.",
            "The foot must find the stomach mark blind - solo crash-pad drilling precedes any live throw.",
        ],
        "requirements": [
            "A genuinely committed forward push - the circle needs real momentum to draw.",
            "The sit-back directed backward, not downward, with the foot planted below the navel.",
            "Sleeve pulls driving down toward the hips through the entire arc.",
            "The immediate shrimp to guard on landing - the throw is not finished on your back.",
            "Crash-pad solo drilling until the foot plant is automatic before any partner flies.",
        ],
        "standards": [
            "Throw mechanics follow the sutemi-waza treatments in Draeger and Smith, Comprehensive Asian Fighting Arts, and Mol, Classical Fighting Arts of Japan.",
            "Tomoe nage is practiced on crash pads until the arc is controlled; thin mats are never the learning surface.",
            "Partners must show fearless forward breakfalls before taking the full circle.",
        ],
        "citations": [CIT_DRAEGER, CIT_MOL, CIT_HALL],
        "sig_lens": (
            "The Signature read: the circle is a drawn oath. Where public "
            "teaching files tomoe nage as a sacrifice throw, the "
            "Signature Combat Method files it as the covenant of the "
            "comma - the defender swearing to fall, the foot swearing to "
            "catch, and the attacker's body keeping both promises in the "
            "air."
        ),
    },
    {
        "key": "ushiro_ryote_mochi",
        "name": "Ushiro Ryote Mochi: Rear Two-Hand Grab Defense",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Ushiro ryote mochi is the rear two-hand grab: the attacker "
            "seizes both of your wrists from behind, pinning your arms in "
            "the classic abduction hold. It is the hardest grab to answer "
            "because the attacker is unseen, both arms are controlled, and "
            "instinct screams to pull forward - which only tightens the "
            "trap. Classical jujutsu's answer is counterintuitive: drop "
            "low, step back into the attacker to steal the space their "
            "pull needs, and turn inside the grab using the elbows as "
            "wedges. The turn converts the rear hold into a front "
            "engagement where every technique in the curriculum becomes "
            "available - kote gaeshi on the presented wrist, ude garami on "
            "the bent arm, or a hip throw as they stumble forward into "
            "the space you vacated. It is ranked advanced because it "
            "demands calm inside surprise: the body must do the trained "
            "thing while the mind is still catching up."
        ),
        "how_it_works": (
            "Partner seizes both your wrists from behind and pulls. Do "
            "not pull forward - that is the trap. Drop instantly into "
            "jigotai, lowering your center below their pull, and step one "
            "foot back toward them, stealing the space the pull needs. "
            "Raise both elbows sharply outward and up: the elbows are "
            "wedges driven between their forearms, and the drop gives them "
            "leverage. As the grip loosens, turn your whole body inside - "
            "pivot on the balls of the feet, turning toward the weaker "
            "side - so you face them with their arms now extended toward "
            "you. The rear hold has become a front engagement: their right "
            "wrist is presented for kote gaeshi, their bent arm for ude "
            "garami, their stumbling balance for kubi nage. Take whichever "
            "the turn offers. Drill the drop-and-wedge first without the "
            "turn: grab, drop, elbows up, feel the loosening. Add the turn "
            "only when the wedge works against full pulls. The advanced "
            "skill is the calm: drill with eyes closed until the grab "
            "lands, so the body learns to drop before the mind names the "
            "danger."
        ),
        "key_points": [
            "Never pull forward out of a rear grab - the pull is the trap and forward is where it tightens.",
            "Drop into jigotai and step back into the attacker: steal the space their pull needs to work.",
            "The elbows are wedges: raised sharply outward and up, levered by the dropped center.",
            "The inside turn converts the rear hold to a front engagement - every technique becomes available.",
            "Calm inside surprise is the advanced skill: the body drops before the mind names the danger.",
        ],
        "requirements": [
            "The instant drop to jigotai on contact - height is surrender in this defense.",
            "The backward step into the attacker, not away.",
            "Both elbows wedged up and out with the dropped center behind them.",
            "The inside pivot completed to a facing stance before any counter is chosen.",
            "Eyes-closed grab drills to train the body ahead of the mind.",
        ],
        "standards": [
            "Defense mechanics follow the goshin treatments in Mol, Classical Fighting Arts of Japan, and Cunningham, Taiho-Jutsu.",
            "Rear grabs are applied with control - the partner pulls steadily, never jerks the shoulders.",
            "The counter is chosen from what the turn presents; forcing a favorite technique is forbidden.",
        ],
        "citations": [CIT_MOL, CIT_CUNNINGHAM, CIT_HALL],
        "sig_lens": (
            "The Signature read: surprise is an unpaid debt. Where public "
            "teaching files ushiro ryote mochi as a rear defense, the "
            "Signature Combat Method files it as the calmest collection - "
            "the unseen grab swore the arms were held, and the dropping "
            "body answers before the mind finishes reading the claim."
        ),
    },
    {
        "key": "kaeshi_waza",
        "name": "Kaeshi Waza: Counter Techniques",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Kaeshi waza means counter techniques: the art of answering "
            "the opponent's technique with a technique of your own, "
            "turning their attack into your throw. Every technique in "
            "jujutsu has a moment of vulnerability - the instant of full "
            "commitment, when the attacker's balance, grip, and intention "
            "are all spent on the attack and nothing is held back for "
            "defense. Kaeshi waza lives in that instant. The classical "
            "counters are paired: tani otoshi answers the forward hip "
            "throw, uchi mata sukashi answers the inner thigh throw by "
            "voiding the hips, kote gaeshi answers the wrist grab that "
            "overreaches. Training counters rewires the student's "
            "relationship with being attacked - the attack stops being a "
            "problem and becomes an offering. It is ranked at the summit "
            "because it requires everything beneath it: ukemi to survive "
            "the attempt, kuzushi to feel the commitment, and the full "
            "technique library to have an answer ready."
        ),
        "how_it_works": (
            "Partner attacks with o goshi, the hip throw, at half speed. "
            "Feel their commitment: the hip loads, the pull starts, their "
            "weight pours forward. Do not resist the throw - ride it. As "
            "their hip turns under you, slide to their rear corner and "
            "extend your leg behind both of theirs: tani otoshi, the "
            "valley drop, answering their forward throw with your backward "
            "one. Their commitment becomes your engine. For the wrist "
            "grab counter: partner seizes your wrist and pulls hard to "
            "drag you; instead of resisting, step with the pull and rotate "
            "your captured hand into kote gaeshi - their dragging energy "
            "feeds your wrist turn. Drill counters in pairs, attacker and "
            "defender swapping every five repetitions, at half speed "
            "until the commitment-feel is unmistakable. The rule of kaeshi: "
            "never force the counter. If their commitment is not genuine, "
            "the counter has no engine - wait, invite, and answer the real "
            "thing. A forced counter is just a second attack wearing a "
            "mask."
        ),
        "key_points": [
            "Every technique has a vulnerability instant: full commitment spends balance, grip, and intention with nothing held back.",
            "The counter rides the attack instead of resisting it - their commitment becomes your engine.",
            "Classical pairs: tani otoshi answers the hip throw, the voided hip answers uchi mata, kote gaeshi answers the overreaching grab.",
            "Counter training rewires being attacked from problem to offering.",
            "Never force the counter: without genuine commitment there is no engine, and a forced counter is just another attack.",
        ],
        "requirements": [
            "The full technique library beneath the counter - ukemi, kuzushi, throws, and locks all fluent.",
            "A partner attacking honestly at graduated speed; pantomime attacks teach nothing.",
            "The commitment-feel identified before the counter moves - ride first, answer second.",
            "Role swapping every five repetitions so both sides learn the vulnerability.",
            "Half speed until the timing is unmistakable; speed is the last ingredient.",
        ],
        "standards": [
            "Counter doctrine follows the kaeshi treatments in Draeger and Smith, Comprehensive Asian Fighting Arts, and Mol, Classical Fighting Arts of Japan.",
            "Counters are drilled at half speed until both partners can name the commitment instant aloud.",
            "Forced counters are corrected immediately - the drill resets to honest attacks.",
        ],
        "citations": [CIT_DRAEGER, CIT_MOL, CIT_SKOSS],
        "sig_lens": (
            "The Signature read: the attack is an offering laid on the "
            "altar of timing. Where public teaching files kaeshi waza as "
            "counters, the Signature Combat Method files each as a "
            "returned oath - the attacker swore their technique would "
            "land, and the counter keeps the promise in reverse."
        ),
    },
    {
        "key": "renraku_waza",
        "name": "Renraku Waza: Combination Attacks",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Renraku waza means combination techniques: chained attacks "
            "where the first technique is thrown to harvest the defense "
            "it provokes, and the second technique reaps it. A single "
            "attack can be defended; a combination attacks the defense "
            "itself. The classical chains are built on predictable "
            "reactions: o uchi gari provokes the backward lean that feeds "
            "tani otoshi; the forward hip throw provokes the sprawl that "
            "opens kata ha jime; the wrist grab defended stiff-armed "
            "presents the elbow for ude garami. Advanced students learn "
            "to chain three deep, with the third technique hidden behind "
            "the second's expected defense. Renraku waza is ranked at the "
            "summit because it requires reading the opponent two moves "
            "ahead - not reacting to what they do, but farming what they "
            "will do, and planting the harvest before they know the field."
        ),
        "how_it_works": (
            "Chain one: attack with de ashi harai, the foot sweep, at the "
            "partner's advancing foot. They will hop back to save the "
            "foot - that backward weight shift is the harvest. Follow "
            "immediately with tani otoshi: slide to the rear corner, leg "
            "across behind theirs, sit and pull. The sweep was the "
            "question; the valley drop is the answer to their answer. "
            "Chain two: shoot for the hip throw; when they sprawl back "
            "and stiffen, abandon the throw and thread the armpit for kata "
            "ha jime - the sprawl that defeated the throw presents the "
            "neck. Drill each chain as one sentence: no pause between "
            "techniques, no resetting the grip, the second launch already "
            "moving as the first lands. Start at half speed with a "
            "cooperative partner who gives the expected defense, then "
            "harden the defense gradually until the chain must be earned. "
            "The advanced drill is the hidden third: after the partner "
            "learns to defend the second technique, add the third that "
            "answers their new defense. Combinations are not sequences "
            "memorized; they are conversations steered."
        ),
        "key_points": [
            "The first technique harvests the defense it provokes; the second reaps what the defense planted.",
            "A single attack can be defended - combinations attack the defense itself.",
            "Classical chains farm predictable reactions: the lean feeds the valley, the sprawl opens the strangle.",
            "Chains are drilled as one sentence: no pause, no re-grip, the second already moving as the first lands.",
            "Three-deep chains hide the finisher behind the expected defense - conversations steered, not sequences memorized.",
        ],
        "requirements": [
            "Both techniques in the chain fluent individually before they are ever linked.",
            "A partner giving the expected defense honestly at first, then hardening it gradually.",
            "No pause between techniques in the drill - the chain is one continuous motion.",
            "Reading practice: the student must call out the defense they are farming before launching the chain.",
            "The third-technique layer added only after the two-chain is earned against resistance.",
        ],
        "standards": [
            "Combination doctrine follows the renraku treatments in Draeger and Smith, Comprehensive Asian Fighting Arts, and Mol, Classical Fighting Arts of Japan.",
            "Chains are built on genuine reactions - if the partner does not defend as expected, the student adapts rather than forcing the script.",
            "Full-speed chains require both partners' ukemi to be automatic for every technique in the chain.",
        ],
        "citations": [CIT_DRAEGER, CIT_MOL, CIT_HALL],
        "sig_lens": (
            "The Signature read: the combination is a farmed oath. Where "
            "public teaching files renraku waza as chained attacks, the "
            "Signature Combat Method files each chain as agriculture - the "
            "first technique sowing the defense, the second reaping it, "
            "and the farmer already planting the third row."
        ),
    },
    {
        "key": "muto_dori",
        "name": "Muto Dori: Unarmed Defense Against the Sword",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Muto dori means no-sword capture: the classical art of "
            "defending unarmed against a sword cut, the summit technique "
            "of koryu jujutsu. It is taught last because it demands "
            "everything - maai read to the inch, timing read to the "
            "instant, taihenjutsu to leave the cutting line, and the "
            "courage to enter toward the blade rather than flee it. The "
            "principle is entering the dead angle: a sword cuts along its "
            "arc, and inside the arc's inner radius the blade cannot "
            "reach. The defender times the cut's commitment, steps "
            "offline and in, controls the sword arm at the elbow and "
            "wrist, and applies kote gaeshi or ude garami to disarm. In "
            "modern training it is practiced with wooden swords and full "
            "protective discipline - the art preserves the samurai's "
            "answer to the ultimate asymmetry, and teaches the deepest "
            "lesson of jujutsu: that even the sword has a dead angle, and "
            "no advantage is absolute."
        ),
        "how_it_works": (
            "Partner raises a wooden sword for a straight overhead cut. "
            "Do not move early - the defense answers commitment, not "
            "intention. As the cut begins its descent, step diagonally "
            "forward and offline to your left, entering inside the arc's "
            "inner radius where the blade cannot reach. Your left hand "
            "meets their right wrist from below, your right hand controls "
            "the elbow; clamp both and turn your body, rotating their "
            "sword arm into kote gaeshi. The disarm follows the wrist "
            "turn - the sword falls as the wrist bends, and you step back "
            "with zanshin, never reaching for the fallen blade while the "
            "partner is still a threat. Drill in stages: first the offline "
            "step against a slow cut, no contact; then the wrist control "
            "on a held cut, frozen; then the full entry at quarter speed "
            "with a foam sword. Speed increases only with protective gear "
            "and a master watching. The dead angle is found by geometry, "
            "not bravery - enter the angle, never the arc."
        ),
        "key_points": [
            "The sword cuts along its arc; inside the arc's inner radius lies the dead angle the blade cannot reach.",
            "The defense answers the cut's commitment, not its intention - early movement is just another target.",
            "Step diagonally forward and offline: enter toward the blade's dead angle, never backward into the next cut.",
            "Wrist and elbow control convert to kote gaeshi - the classical disarm is a wrist technique, not a wrestling match.",
            "No advantage is absolute: the summit lesson is that even the sword has geometry that defeats it.",
        ],
        "requirements": [
            "A wooden or foam sword for all drill - live blades are never part of muto dori practice.",
            "The offline step drilled solo until the diagonal entry is automatic.",
            "Contact stages built gradually: step only, then frozen control, then quarter-speed entry.",
            "Protective gear and master supervision for any speed work.",
            "Zanshin after the disarm: step back ready, never reach for the fallen blade mid-threat.",
        ],
        "standards": [
            "Muto dori method follows the classical treatments in Mol, Classical Fighting Arts of Japan, and Friday, Legacies of the Sword.",
            "Live blades are forbidden in this curriculum's muto dori practice without exception.",
            "Students attempt the full entry only after demonstrating every prerequisite technique at rank.",
        ],
        "citations": [CIT_MOL, CIT_FRIDAY, CIT_SKOSS],
        "sig_lens": (
            "The Signature read: the dead angle is geometry's mercy. "
            "Where public teaching files muto dori as sword defense, the "
            "Signature Combat Method files it as the final covenant - the "
            "blade swearing its arc is absolute, and the entering body "
            "keeping its appointment with the angle the oath forgot."
        ),
    },
]
