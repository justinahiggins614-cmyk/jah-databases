#!/usr/bin/env python3
"""Entries for the Shaolin Kung Fu Combat databases (combat batch 3).

Shaolin kung fu - the martial art of the Shaolin Temple at Dengfeng,
Henan, China - is built on stances, fundamental forms, and the five
animal styles (dragon, tiger, crane, leopard, snake). This build creates
two NEW databases, 34 ladder-ordered records each:

  combat-shaolin-kung-fu             - Shaolin Kung Fu Combat Database
                                       (public-harvest: real, fact-checked
                                       Shaolin kung fu - stances, strikes,
                                       kicks, blocks, fundamental forms,
                                       the five animal styles, staff basics,
                                       and traditional conditioning - every
                                       record a full technique with
                                       step-by-step body mechanics, real
                                       Chinese terminology with
                                       translations; standard references
                                       Shahar The Shaolin Monastery 2008;
                                       Wong Kiew Kit The Art of Shaolin
                                       Kung Fu 2002; Yang Jwing-Ming
                                       Shaolin Long Fist Kung Fu 2008;
                                       the Yi Jin Jing classical manual;
                                       Chow and Spangler Kung Fu 1982;
                                       Smith Chinese Boxing 1974)
  combat-shaolin-kung-fu-signature  - Shaolin Kung Fu Combat Signature
                                       Database
                                       (his original Signature Shaolin
                                       Method: every stance a vow of the
                                       legs, every strike a signature of
                                       the body, the five animals the five
                                       seals of the system, the form the
                                       archive of the art; src signature,
                                       titles suffixed " (Signature
                                       Edition)", never presented as
                                       authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written
in ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBSK- (public) and JAH-CBSKS- (signature), verified free
in the manifest and in every shard index of jah-databases-data-1
(zero hits for "JAH-CBSK" across all 853 index files; zero "CBSK"
id_prefix values in the manifest). Slugs combat-shaolin-kung-fu and
combat-shaolin-kung-fu-signature verified absent from the manifest.

Dedupe: all 68 titles (34 public + 34 Signature Edition) checked against
the DedupeGate over the whole system before authoring - zero refusals.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_shaolin_kung_fu.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Civilian traditional-art scope: stance, strike, kick, form, and
conditioning instruction for traditional practice and sport. No
religious talk. Never the words "bat belt" anywhere. No website
references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Shaolin Method: "
            "every stance a vow of the legs, every strike a signature of "
            "the body, the five animals the five seals of the system, the "
            "form the archive of the art. Clearly labeled Signature-made, "
            "never presented as authentic public record.")

CIT_SHAHAR = ("Shahar M. The Shaolin Monastery: History, Religion, and the "
              "Chinese Martial Arts. University of Hawaii Press; 2008.")
CIT_WONG = ("Wong Kiew Kit. The Art of Shaolin Kung Fu. Tuttle Publishing; "
            "2002.")
CIT_YANG = ("Yang Jwing-Ming. Shaolin Long Fist Kung Fu. YMAA Publication "
            "Center; 2008.")
CIT_YIJINJING = ("Yi Jin Jing (Muscle Tendon Change Classic). Classical "
                 "Chinese qigong and conditioning manual, Ming dynasty "
                 "compilation.")
CIT_CHOW = ("Chow D, Spangler R. Kung Fu: History, Philosophy, and "
            "Technique. Unique Publications; 1982.")
CIT_SMITH = ("Smith RW. Chinese Boxing: Masters and Methods. Kodansha "
             "International; 1974.")

ENTRIES = [
    {
        "key": "salute",
        "name": "The Shaolin Salute (Bao Quan Li)",
        "group": "Stances",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Every Shaolin training session begins and ends the same way: "
            "with the bao quan li, the fist-hug salute. The right hand "
            "closes into a fist and the left palm wraps over it, both held "
            "at chest height a fist-width from the body, and the head bows "
            "slightly. The gesture carries the code of the training hall: "
            "the fist is strength, the palm is restraint, and the bow is "
            "respect for the teacher, the training partners, and the art "
            "itself. Students salute when entering the floor, when a form "
            "begins and ends, when receiving correction, and when training "
            "concludes. The salute is the first technique taught because "
            "it frames everything after it: Shaolin kung fu is practiced "
            "with discipline first and force second. Performed well, the "
            "salute takes about two and a half seconds - raise the hands "
            "together, hold a half beat, bow, hold, rise - and it is "
            "repeated three times at the opening and closing of practice."
        ),
        "how_it_works": (
            "HOW TO DO IT. Stand in a natural stance with feet together "
            "and weight even. Step 1: raise both hands to chest height at "
            "the same time - the right hand closes into a fist, thumb "
            "folded over the fingers, while the left hand stays open with "
            "fingers together. Step 2: wrap the left palm over the right "
            "fist so the left fingers cover the right knuckles, holding "
            "the joined hands one fist-width in front of the chest with "
            "elbows relaxed and slightly down. Step 3: hold the position "
            "for a half beat, eyes forward, breathing steady. Step 4: bow "
            "the head and upper body forward about fifteen degrees while "
            "the hands stay at chest height. Step 5: hold the bow for one "
            "full breath. Step 6: rise back to the joined-hands position, "
            "then lower the hands to the sides. The common errors are "
            "slapping the hands together noisily, holding the hands too "
            "high near the chin or too low near the belly, and rushing "
            "the bow so it becomes a nod. Practice the full sequence "
            "three times slowly at the start of every session until the "
            "hands meet in exactly the same place every time."
        ),
        "key_points": [
            "Right fist wrapped by left palm at chest height, one fist-width from the body, elbows relaxed and slightly down.",
            "The salute encodes the training code: strength under restraint, respect for teacher, partners, and art.",
            "Performed at session open and close, at form start and finish, and when receiving correction.",
            "The full gesture - raise, hold, bow fifteen degrees, hold one breath, rise - takes about two and a half seconds.",
            "Precision matters more than speed: the hands must meet in exactly the same place every time.",
        ],
        "requirements": [
            "A clear floor space and a settled standing posture with feet together before the hands move.",
            "Right fist closed properly with the thumb folded over the fingers, not sticking out.",
            "Left palm open with fingers together, wrapping the right fist so the knuckles are covered.",
            "A bow of about fifteen degrees from the head and upper body, hands unmoving at chest height.",
            "Three unhurried repetitions at the opening and closing of each training session.",
        ],
        "standards": [
            "The joined hands sit at chest height, never drifting toward the chin or the belly.",
            "The bow is a controlled incline of head and torso, not a quick nod of the neck alone.",
            "Each salute matches the last: same hand position, same timing, same depth of bow.",
        ],
        "citations": [CIT_SHAHAR, CIT_WONG],
        "sig_lens": (
            "The Signature read: the salute is the first covenant of the "
            "session. Before the body signs anything with force, it signs "
            "with respect - the fist swears strength, the palm swears "
            "restraint, and the bow seals both. Where public teaching "
            "files etiquette, the Signature method files an oath."
        ),
    },
    {
        "key": "wuji",
        "name": "Wuji Standing Posture (Wuji Zhuang)",
        "group": "Stances",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Wuji zhuang, the standing of no-extremes, is the zero posture "
            "of Shaolin practice: feet together, body upright, arms hanging "
            "relaxed at the sides, breathing slow and natural. Every form "
            "begins from stillness, and wuji is where stillness is trained. "
            "The student stands for three to five minutes, settling the "
            "weight evenly across both feet, lengthening the spine as if "
            "the crown of the head were suspended from above, and letting "
            "the shoulders drop away from the ears. The breath follows a "
            "quiet cadence - in for four counts, a brief pause, out for "
            "six counts - which gives a twelve-second cycle and thirty "
            "complete cycles in six minutes. Wuji teaches the two skills "
            "every later stance depends on: true structural alignment, "
            "with the joints stacked so the skeleton carries the weight, "
            "and mental quiet, so the body can be commanded without "
            "tension. It looks like doing nothing; it is the foundation "
            "of doing everything."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: bring the feet together so the inner "
            "edges touch, weight spread evenly - half on each foot, and on "
            "each foot balanced across heel, ball, and outer edge. Step 2: "
            "let the knees soften without bending them deliberately; the "
            "legs are straight but never locked. Step 3: tuck the hips very "
            "slightly so the lower back lengthens, and imagine the crown "
            "of the head drawn upward while the tailbone drops downward. "
            "Step 4: drop the shoulders, let the arms hang with the palms "
            "facing the thighs and the fingers naturally extended, and "
            "rest the tongue lightly on the roof of the mouth. Step 5: "
            "begin the breath cadence - breathe in through the nose for "
            "four slow counts, pause for two, breathe out through the nose "
            "for six counts, feeling the belly rise and fall rather than "
            "the chest. Step 6: stand for three minutes at first, adding a "
            "minute each week until ten minutes is comfortable, keeping "
            "the gaze soft and forward. If the mind wanders, return "
            "attention to the breath count; if a muscle tenses, breathe "
            "into it and let it release without moving the posture."
        ),
        "key_points": [
            "Feet together, weight even, knees soft but never locked, spine lengthened crown-up and tailbone-down.",
            "The breath cadence is in for four counts, pause for two, out for six: a twelve-second cycle.",
            "Shoulders dropped, arms hanging with palms to the thighs, tongue resting on the roof of the mouth.",
            "Trains structural alignment - skeleton carrying weight - and mental quiet before any movement.",
            "Build from three minutes toward ten minutes, adding one minute per week of practice.",
        ],
        "requirements": [
            "A flat, quiet standing spot where the full body can be held still for minutes.",
            "Feet together with weight genuinely even left to right and heel to ball.",
            "An unforced twelve-second breath cycle: four counts in, two pause, six out.",
            "A soft forward gaze and a settled mind, returning to the breath count whenever attention drifts.",
            "Daily practice, starting at three minutes and lengthening gradually.",
        ],
        "standards": [
            "The body shows no visible sway: joints stacked, skeleton carrying the load.",
            "The breath stays nasal, silent, and even for the full duration of the stand.",
            "Tension is released on discovery, never held: a tense shoulder is breathed open, not forced.",
        ],
        "citations": [CIT_WONG, CIT_YIJINJING],
        "sig_lens": (
            "The Signature read: wuji is the blank page before the "
            "signature is written. The body files its alignment, the "
            "breath files its cadence, and only when both are recorded "
            "does movement begin. Where public teaching files stillness, "
            "the Signature method files the zero point of all later "
            "measurement."
        ),
    },
    {
        "key": "ma_bu",
        "name": "Horse Stance (Ma Bu)",
        "group": "Stances",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Ma bu, the horse stance, is the root of Shaolin kung fu. The "
            "feet stand about two shoulder-widths apart with toes pointing "
            "forward, the knees bend until the thighs sit parallel to the "
            "ground, the back stays straight and upright, and the fists "
            "rest at the hips. It is called the horse stance because the "
            "rider's seat on a horse takes the same shape: wide, low, and "
            "stable. For a practitioner with a forty-five centimeter "
            "thigh, the ninety-degree knee puts the hip joint about "
            "forty-five centimeters above the floor and spreads the base "
            "about ninety centimeters wide. Every Shaolin student holds "
            "this stance daily, beginning with thirty-second holds and "
            "building toward several minutes, because ma bu builds the "
            "leg strength, hip openness, and rooted stability that every "
            "punch, kick, and form draws on. Weak legs make weak kung fu; "
            "the horse stance is where strong legs are made."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: step the feet apart to about two "
            "shoulder-widths, toes pointing straight forward, weight even. "
            "Step 2: bend the knees and sink straight down as if sitting "
            "onto a low stool, keeping the back straight and upright - do "
            "not lean forward. Step 3: continue sinking until the thighs "
            "are parallel to the floor, with the knees tracking directly "
            "over the toes and pushed slightly outward, never caving "
            "inward. Step 4: tuck the hips slightly under so the lower "
            "back is flat, and pull the fists back to the hips with the "
            "elbows pointing back. Step 5: breathe steadily into the "
            "belly and hold the position, starting at thirty seconds and "
            "adding fifteen seconds each week. The three classic errors "
            "are leaning the torso forward, letting the knees collapse "
            "inward past the big toes, and rising too high so the thighs "
            "leave parallel. Check the stance in a mirror from the side: "
            "ear, shoulder, hip, and knee should show one clean vertical "
            "line of support behind a horizontal thigh."
        ),
        "key_points": [
            "Feet two shoulder-widths apart, toes forward, thighs parallel to the floor, back straight and upright.",
            "A forty-five centimeter thigh at a ninety-degree knee sets the hip about forty-five centimeters high over a ninety-centimeter base.",
            "Knees track over the toes and press slightly outward; caving inward is the error that injures knees.",
            "Fists chambered at the hips, hips tucked slightly under, breath steady into the belly.",
            "Begin with thirty-second holds and add fifteen seconds weekly toward multi-minute stances.",
        ],
        "requirements": [
            "Enough floor space for a stance two shoulder-widths wide with room to sink.",
            "Thighs genuinely parallel to the floor, verified in a mirror or by a training partner.",
            "Knees aligned over the toes for the entire hold, with no inward collapse.",
            "An upright torso with the lower back flat, never rounded or arched hard.",
            "A timed hold, starting at thirty seconds, lengthened a little each week.",
        ],
        "standards": [
            "The thigh-floor parallel is the pass mark: above parallel is not yet ma bu.",
            "The knee never travels inside the line of the big toe.",
            "The hold is silent and steady - no bouncing, no shifting, no held breath.",
        ],
        "citations": [CIT_YANG, CIT_WONG, CIT_CHOW],
        "sig_lens": (
            "The Signature read: the horse stance is the vow the legs "
            "make to the ground. Two shoulder-widths wide, thighs level "
            "as a written line, the body files its first signature in "
            "sweat. Where public teaching files a leg exercise, the "
            "Signature method files the root of every later technique."
        ),
    },
    {
        "key": "gong_bu",
        "name": "Bow Stance (Gong Bu)",
        "group": "Stances",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Gong bu, the bow stance, is the lunging stance behind most "
            "Shaolin punches: the front leg bends deeply with the knee "
            "over the ankle, the back leg extends straight with the foot "
            "turned out about forty-five degrees, and the torso stays "
            "upright over the hips. It is named for the archer's bow - "
            "the front leg the bent bow, the back leg the drawn string. "
            "Weight sits roughly seventy percent on the front leg and "
            "thirty percent on the back, so a seventy-kilogram "
            "practitioner loads the front leg with forty-nine kilograms "
            "(about four hundred eighty newtons) and the back leg with "
            "twenty-one kilograms (about two hundred six newtons). The "
            "stance teaches forward drive: the back leg pushes the floor "
            "away and the hip carries the punch forward. Nearly every "
            "straight punch, palm strike, and advancing combination in "
            "the basic forms is thrown from gong bu, which is why it is "
            "drilled from the first week."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: from a natural stand, step one foot "
            "forward about one and a half shoulder-widths, keeping both "
            "feet pointing forward at first. Step 2: bend the front knee "
            "and sink until the front thigh approaches parallel, with the "
            "knee stacked directly above the ankle - the knee must never "
            "pass in front of the toes. Step 3: straighten the back leg "
            "fully and turn the back foot outward about forty-five "
            "degrees, pressing the whole sole flat to the floor with the "
            "heel down. Step 4: settle the hips so the weight divides "
            "seventy percent front and thirty percent back, and keep the "
            "torso upright with the shoulders over the hips. Step 5: hold "
            "for thirty seconds each side, then practice stepping forward "
            "from stance to stance, landing each time with the knee over "
            "the ankle and the back heel down. The classic errors are a "
            "front knee drifting past the toes, a back heel lifting off "
            "the floor, and leaning the chest forward over the front "
            "knee, which unloads the back leg and kills the drive."
        ),
        "key_points": [
            "Front knee bent with knee over ankle, back leg straight, back foot turned out forty-five degrees with heel down.",
            "Weight divides about seventy percent front and thirty percent back: forty-nine and twenty-one kilograms for a seventy-kilogram student.",
            "Torso upright with shoulders over hips; the drive comes from the back leg pushing the floor.",
            "The stance of the straight punch: nearly every advancing hand technique rides on gong bu.",
            "Drill both sides equally, holding thirty seconds per side before stepping practice.",
        ],
        "requirements": [
            "A forward step of about one and a half shoulder-widths with both feet initially forward.",
            "A front knee stacked over the ankle, never traveling past the toes.",
            "A fully straight back leg with the entire sole grounded and the heel down.",
            "The seventy-thirty weight split, felt as heavy front leg and light driving back leg.",
            "Equal practice on left-lead and right-lead stances.",
        ],
        "standards": [
            "The back heel stays glued to the floor through the whole stance and every punch thrown from it.",
            "The front knee tracks the front toes exactly, with no inward or outward drift.",
            "The torso remains vertical: the shoulders stay over the hips, not over the front knee.",
        ],
        "citations": [CIT_YANG, CIT_CHOW],
        "sig_lens": (
            "The Signature read: the bow stance is the signature of "
            "forward intent - the archer's bow drawn in the legs. "
            "Seventy percent of the weight files itself on the front "
            "foot while the back leg keeps its heel down like a seal "
            "on the floor. Where public teaching files a lunge, the "
            "Signature method files a promise of direction."
        ),
    },
    {
        "key": "xu_bu",
        "name": "Empty Stance (Xu Bu)",
        "group": "Stances",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Xu bu, the empty stance - also called the cat stance - keeps "
            "the front leg empty of weight so it can kick in an instant. "
            "The back leg bends deeply and carries about ninety percent "
            "of the weight while the front foot rests on the floor with "
            "only the ball or toes touching, the heel raised. For a "
            "seventy-kilogram practitioner that means the back leg holds "
            "sixty-three kilograms (about six hundred eighteen newtons) "
            "and the front leg barely ten percent. The torso stays "
            "upright, the hands guard high, and the body coils like a cat "
            "about to spring - hence the nickname. Xu bu teaches the "
            "ready leg: because the front foot carries almost nothing, it "
            "can lift into a kick, a knee, or a quick step with no weight "
            "shift to telegraph the move. It appears in the basic forms "
            "wherever a kick is about to follow, and it is the stance of "
            "patience - loaded, quiet, and ready."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: from a natural stand, step one foot "
            "forward about half a shoulder-width and place only the ball "
            "of the foot on the floor, heel raised. Step 2: bend the back "
            "leg deeply and sink the weight onto it until roughly ninety "
            "percent sits on the back foot and ten percent on the front "
            "ball - the front knee stays soft and the front leg feels "
            "weightless. Step 3: keep the torso upright with the hips "
            "tucked slightly under, and raise both hands to a guard in "
            "front of the chest. Step 4: breathe steadily and hold for "
            "twenty seconds per side, checking that the front foot could "
            "lift at any moment without any shift of balance. Step 5: "
            "practice the readiness test - from xu bu, snap the front "
            "knee straight up into a chamber and set it back down without "
            "the torso swaying. The classic errors are putting real "
            "weight on the front foot (which makes it a weak bow stance), "
            "letting the back knee cave inward, and leaning the torso "
            "back to counterbalance instead of sinking the hips."
        ),
        "key_points": [
            "Back leg bent deeply carrying about ninety percent of the weight; front foot touches with ball or toes only.",
            "A seventy-kilogram student loads the back leg with sixty-three kilograms and the front foot with seven.",
            "Torso upright, hands guarding high, body coiled and quiet like a cat before springing.",
            "The empty front leg can kick, knee, or step with no telegraphing weight shift.",
            "The readiness test: lift the front knee to chamber and replace it with zero torso sway.",
        ],
        "requirements": [
            "A deep bend in the back leg with the back foot flat and the knee tracking the toes.",
            "A front foot carrying only about ten percent of the weight, heel raised.",
            "An upright torso with hips tucked slightly under, not leaning back.",
            "Both hands raised to a chest-high guard throughout the stance.",
            "Twenty-second holds per side plus the knee-lift readiness test.",
        ],
        "standards": [
            "The front foot lifts freely at any moment: if balance shifts when it rises, the stance is too heavy.",
            "The back knee never passes inside the big-toe line of the back foot.",
            "The hold is motionless: no rocking, no bouncing, no weight creeping forward.",
        ],
        "citations": [CIT_YANG, CIT_WONG],
        "sig_lens": (
            "The Signature read: the empty stance files ninety percent "
            "of the body on the back leg and leaves the front leg blank "
            "like an unsigned line - ready to be written as a kick at "
            "any instant. Where public teaching files a light stance, "
            "the Signature method files pure potential."
        ),
    },
    {
        "key": "pu_bu",
        "name": "Crouch Stance (Pu Bu)",
        "group": "Stances",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Pu bu, the crouch stance, drops the body to its lowest "
            "fighting level: one leg folds completely beneath the body "
            "while the other extends straight out to the side with the "
            "foot flat on the floor, and the torso stays upright. A "
            "standing practitioner's center of mass rides about one meter "
            "above the floor; in a full pu bu it drops to roughly "
            "forty-five centimeters - a fifty-five centimeter descent "
            "that puts the body below most incoming strikes and loads "
            "the folded leg like a compressed spring. The stance is the "
            "home of the sweeping kick: from the low crouch, the extended "
            "leg whips around to sweep an opponent's supporting leg while "
            "the folded leg drives the turn. Pu bu also builds extreme "
            "hip and ankle mobility, which is why it appears in the "
            "warming sequences of the basic forms. Beginners hold a high "
            "crouch first and sink lower over weeks; forcing the full "
            "depth before the hips are ready strains the knees."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: from a wide stand, shift all the "
            "weight onto one leg and begin bending it deeply. Step 2: "
            "extend the other leg straight out to the side, keeping the "
            "whole sole of the extended foot flat on the floor with toes "
            "pointing up or slightly outward. Step 3: continue sinking "
            "until the buttock rests near the heel of the folded leg, "
            "with the folded knee tracking over its toes and the torso "
            "upright - do not fold forward over the extended leg. Step 4: "
            "place the hands in a guard or rest them lightly for balance "
            "while learning, and hold for fifteen seconds per side. Step "
            "5: practice the rise - drive up through the folded leg back "
            "to standing without pushing off the floor with the hands. "
            "The classic errors are lifting the extended foot's heel, "
            "collapsing the chest forward onto the thigh, and letting the "
            "folded knee cave inward under the load. Build depth "
            "gradually: a high crouch held well beats a deep crouch held "
            "badly."
        ),
        "key_points": [
            "One leg folds fully beneath the body, the other extends straight sideways with the whole sole flat.",
            "The center of mass drops from about one meter standing to roughly forty-five centimeters: a fifty-five centimeter descent.",
            "Torso upright over the folded leg; the folded knee tracks its toes and never caves inward.",
            "The home stance of the sweeping kick: the low crouch loads the spring for the sweep.",
            "Begin with a high crouch and sink lower over weeks; never force depth the hips are not ready for.",
        ],
        "requirements": [
            "A folded leg with the buttock near the heel and the knee tracking over the toes.",
            "An extended leg with the entire sole flat on the floor, toes up or slightly out.",
            "An upright torso with no forward collapse onto the thigh.",
            "Fifteen-second holds per side, rising by leg drive alone without hand assistance.",
            "Gradual depth progression matched to hip and ankle mobility.",
        ],
        "standards": [
            "The extended foot stays fully flat: a lifted heel fails the stance.",
            "The spine stays vertical; the chest never rests on the extended thigh.",
            "The rise is driven by the folded leg, smooth and without hand pushes.",
        ],
        "citations": [CIT_YANG, CIT_CHOW],
        "sig_lens": (
            "The Signature read: the crouch stance signs the body at its "
            "lowest line - fifty-five centimeters closer to the ground, "
            "where the folded leg files itself as a compressed spring. "
            "Where public teaching files a low stance, the Signature "
            "method files the loading of the sweep."
        ),
    },
    {
        "key": "xie_bu",
        "name": "Cross Stance (Xie Bu)",
        "group": "Stances",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Xie bu, the cross stance, weaves the legs into a tight "
            "screw: the front leg crosses over the back, both knees bend "
            "deeply, and the body sinks until the back knee hovers just "
            "above the floor behind the front heel. The stance packs the "
            "whole body into a narrow column, which makes it a resting "
            "and turning stance - the feet are too tangled to kick from, "
            "but the coiled position unwinds explosively into spins, "
            "sweeps, and direction changes. Compared with the horse "
            "stance's broad ninety-centimeter base, xie bu stands on a "
            "footprint barely thirty centimeters wide, trading stability "
            "for compactness and rotational readiness. In the basic forms "
            "it appears at the turning points, where the practitioner "
            "screws down low and then unwinds into the next technique. "
            "The knees must track carefully here: the crossed position "
            "tempts the knees inward, and the stance is only safe when "
            "each knee follows its own toes."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: from a natural stand, step one foot "
            "across in front of the other so the legs cross at the "
            "shins. Step 2: bend both knees and sink straight down, "
            "keeping the torso upright and the weight centered between "
            "the feet. Step 3: continue sinking until the back knee "
            "hovers just above the floor directly behind the front heel, "
            "with the front foot flat and the back foot on its ball. "
            "Step 4: check the knees - each knee must track over its own "
            "toes despite the cross; if either knee drifts inward, widen "
            "the cross slightly. Step 5: hold for fifteen seconds per "
            "side, then practice the unwind: drive up and pivot into a "
            "bow stance facing the new direction. The classic errors are "
            "sinking with the knees caving inward, which strains the "
            "joints, and leaning the torso to one side to find balance "
            "instead of centering the weight. Beginners should practice "
            "beside a wall for balance until the screw-down feels stable."
        ),
        "key_points": [
            "Front leg crosses over the back, both knees bend deeply, back knee hovering just above the floor behind the front heel.",
            "The footprint is barely thirty centimeters wide versus the horse stance's ninety: compactness traded for stability.",
            "A turning stance: the coiled cross unwinds explosively into spins, sweeps, and direction changes.",
            "Each knee must track over its own toes despite the cross; inward drift strains the joints.",
            "Hold fifteen seconds per side, then drill the unwind into a bow stance in the new direction.",
        ],
        "requirements": [
            "A genuine cross of the legs at the shins, not merely feet placed close together.",
            "A deep sink with the back knee hovering just above the floor behind the front heel.",
            "Knees tracking over their own toes for the entire stance.",
            "An upright torso with weight centered between the two feet.",
            "Fifteen-second holds per side plus the unwind-to-bow-stance transition drill.",
        ],
        "standards": [
            "Neither knee crosses the midline of its own foot: knees follow toes, always.",
            "The torso shows no sideways lean; balance comes from centering, not tilting.",
            "The unwind is one smooth drive upward and around, with no stutter step.",
        ],
        "citations": [CIT_YANG, CIT_WONG],
        "sig_lens": (
            "The Signature read: the cross stance screws the body into "
            "its most compact signature - a thirty-centimeter column "
            "wound like a spring, filed low and ready to unwind. Where "
            "public teaching files a rest stance, the Signature method "
            "files the coil before the turn."
        ),
    },
    {
        "key": "duli_bu",
        "name": "Single-Leg Stance (Du Li Bu)",
        "group": "Stances",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Du li bu, the single-leg stance, stands on one leg while the "
            "other knee rises to hip height - the crane posture of Shaolin "
            "practice. It trains the two halves of balance: the standing "
            "leg learns to root through the sole with the ankle making "
            "constant micro-adjustments, and the raised knee learns to "
            "stay chambered and ready, since every knee strike and front "
            "kick in the art launches from exactly this chamber. The "
            "classic training ladder runs eight weeks: beginners hold ten "
            "seconds per leg, and each two weeks the target doubles - ten "
            "seconds, then twenty, then forty, then eighty - until the "
            "stance can be held well past a minute with the eyes open and "
            "then with the eyes closed. The torso stays upright, the hands "
            "guard high, and the raised knee points forward with the foot "
            "flexed or pointed depending on the kick being prepared. Weak "
            "balance makes every kick a gamble; du li bu makes the gamble "
            "a certainty."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: stand naturally, then shift all the "
            "weight onto one foot, spreading the sole's contact across "
            "heel, ball, and outer edge. Step 2: raise the other knee "
            "straight up until the thigh is parallel to the floor, with "
            "the lower leg hanging naturally and the foot flexed. Step 3: "
            "stand the torso tall - crown up, hips level, no leaning to "
            "the standing-leg side - and raise the hands to a guard. Step "
            "4: breathe slowly and hold, starting at ten seconds per leg, "
            "timing each side with a clock. Step 5: follow the eight-week "
            "ladder - weeks one and two at ten seconds, weeks three and "
            "four at twenty, weeks five and six at forty, weeks seven and "
            "eight at eighty seconds - then add eyes-closed holds. The "
            "classic errors are leaning the torso over the standing leg, "
            "letting the raised knee drift sideways, and gripping the "
            "floor with the toes instead of settling the whole sole. If "
            "balance fails, step down calmly and reset; grabbing at "
            "furniture teaches the ankle nothing."
        ),
        "key_points": [
            "One leg roots through the full sole while the other knee rises to hip height, thigh parallel to the floor.",
            "The eight-week ladder doubles the hold every two weeks: ten, twenty, forty, then eighty seconds per leg.",
            "The standing ankle makes constant micro-adjustments; the torso stays tall with no sideways lean.",
            "Every knee strike and front kick launches from this exact chamber, so the stance is kick readiness itself.",
            "Advanced practice adds eyes-closed holds once eighty seconds eyes-open is comfortable.",
        ],
        "requirements": [
            "Full-sole contact on the standing foot across heel, ball, and outer edge.",
            "A raised knee with the thigh parallel to the floor and the foot flexed.",
            "A tall, level torso with the hands in a guard and no lean toward the standing leg.",
            "Timed holds starting at ten seconds per leg, both legs trained equally.",
            "The eight-week doubling ladder, advanced to eyes-closed holds.",
        ],
        "standards": [
            "No toe-gripping: the foot rests on the floor, it does not claw it.",
            "The raised knee points forward and stays chambered; sideways drift fails the hold.",
            "Balance is recovered by ankle adjustment, not by arm windmilling or stepping down.",
        ],
        "citations": [CIT_WONG, CIT_YIJINJING],
        "sig_lens": (
            "The Signature read: the single-leg stance files balance as "
            "a signature written on one foot - the ankle the pen making "
            "micro-adjustments, the raised knee the line waiting to "
            "become a kick. Where public teaching files a balance drill, "
            "the Signature method files the chamber of all kicking."
        ),
    },
    {
        "key": "chong_quan",
        "name": "Forward Punch (Chong Quan)",
        "group": "Basic Techniques",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Chong quan, the forward punch, is the first strike of Shaolin "
            "kung fu: the fist travels straight from the hip to the "
            "target, rotating one hundred eighty degrees along the way so "
            "it leaves palm-up and lands palm-down. The rotation is the "
            "corkscrew that tightens the forearm and aligns the first two "
            "knuckles - the index and middle knuckles - as the striking "
            "surface. Power does not come from the arm: the back leg "
            "drives into the floor, the hip turns, the shoulder follows, "
            "and the fist is merely the delivery point of a wave that "
            "starts at the ground. A trained punch can send the fist at "
            "around eight meters per second; with an effective striking "
            "mass of about four kilograms, the kinetic energy reaches "
            "roughly one hundred twenty-eight joules - the physics of a "
            "well-thrown punch, computed not guessed. The punch is thrown "
            "from the horse stance in basic drilling and from the bow "
            "stance when advancing, and it retracts along the same line "
            "twice as fast as it extended."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: chamber the fist at the hip, palm up, "
            "with the elbow pointing back and the shoulder relaxed and "
            "down. Step 2: drive the back foot into the floor and turn "
            "the hip toward the target, letting the shoulder follow the "
            "hip - the fist begins moving only after the hip has started. "
            "Step 3: extend the arm straight toward the target at "
            "shoulder height, rotating the fist one hundred eighty "
            "degrees during the extension so it lands palm-down. Step 4: "
            "at full extension, tighten the fist hard for an instant and "
            "strike with the first two knuckles, keeping the wrist "
            "straight so the knuckles, wrist, and elbow form one line. "
            "Step 5: snap the fist back along the same path to the hip, "
            "palm rotating back to palm-up, twice as fast as it went out. "
            "The classic errors are punching with the arm while the hip "
            "stays still, lifting the shoulder toward the ear, bending "
            "the wrist on impact, and leaving the fist out instead of "
            "snapping it back. Drill in sets of twenty per arm, checking "
            "in a mirror that the shoulder never rises."
        ),
        "key_points": [
            "The fist rotates one hundred eighty degrees in flight: palm-up at the hip, palm-down at impact.",
            "Power starts at the floor: back leg drives, hip turns, shoulder follows, fist delivers.",
            "Impact lands on the first two knuckles with a straight wrist, knuckles-wrist-elbow in one line.",
            "A trained punch reaches about eight meters per second, carrying roughly one hundred twenty-eight joules.",
            "The fist retracts along the same line twice as fast as it extended; a left-out punch is a caught punch.",
        ],
        "requirements": [
            "A proper fist: fingers folded tight, thumb folded over the fingers, wrist straight.",
            "A chambered start with the fist at the hip, palm up, elbow back, shoulder down.",
            "Hip rotation leading the punch: the hip turns first, the fist follows.",
            "Full one-hundred-eighty-degree rotation completed exactly at full extension.",
            "An instant snap-back to chamber, twice as fast as the extension.",
        ],
        "standards": [
            "The shoulder stays down through the whole punch: a risen shoulder fails the rep.",
            "Contact is made with the first two knuckles only, never the flat fingers or bent wrist.",
            "Every punch is paired with its retraction: extension without snap-back is incomplete.",
        ],
        "citations": [CIT_YANG, CIT_CHOW, CIT_SMITH],
        "sig_lens": (
            "The Signature read: the forward punch is the body's first "
            "signature stroke - a straight line drawn from hip to target, "
            "the fist rotating one hundred eighty degrees like a seal "
            "being turned in wax. Where public teaching files a punch, "
            "the Signature method files the wave that starts at the "
            "floor."
        ),
    },
    {
        "key": "tui_zhang",
        "name": "Open Palm Strike (Tui Zhang)",
        "group": "Basic Techniques",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Tui zhang, the pushing palm, strikes with the heel of the "
            "open hand: fingers point up and slightly back, the palm heel "
            "leads, and the whole body drives forward behind it as if "
            "shoving a heavy door. Where the punch concentrates force on "
            "two knuckles, the palm spreads it across the heel of the "
            "hand - at the same striking force of fifteen hundred "
            "newtons, the palm's one hundred twenty square centimeters "
            "delivers about one hundred twenty-five thousand pascals "
            "while a fist's forty square centimeters delivers three "
            "hundred seventy-five thousand. The palm trades penetration "
            "for push: it moves the target's whole mass, which makes it "
            "the pushing, deflecting, and close-range striking tool of "
            "the art. The strike is thrown from the bow stance with the "
            "hip driving exactly as in the punch, and it pairs naturally "
            "with grabs and pulls - one hand pulls while the palm pushes."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: chamber the hand at the hip or ribs "
            "with the palm facing up and the fingers relaxed. Step 2: "
            "drive the back leg into the floor and turn the hip toward "
            "the target, exactly as in the forward punch. Step 3: thrust "
            "the hand forward and upward in a straight line, rotating the "
            "palm to face the target during the extension. Step 4: just "
            "before contact, snap the fingers back so they point up and "
            "slightly toward you, driving the heel of the palm into the "
            "target with the wrist locked straight. Step 5: follow "
            "through two or three inches past the contact point, then "
            "snap the hand back to chamber. The classic errors are "
            "striking with limp fingers instead of the palm heel, "
            "letting the wrist bend backward on impact, and pushing with "
            "the arm while the hip stays quiet. Practice against a heavy "
            "bag or a partner's held pad to learn the difference between "
            "a slap and a driven palm."
        ),
        "key_points": [
            "Contact is made with the heel of the palm, fingers snapped back and pointing up, wrist locked straight.",
            "The palm spreads force: fifteen hundred newtons over the palm gives about one hundred twenty-five thousand pascals versus three hundred seventy-five thousand for a fist.",
            "The palm pushes and moves the target's mass; the fist penetrates - different tools for different jobs.",
            "The hip drives the palm exactly as it drives the punch: back leg, hip turn, then hand.",
            "Follow through two to three inches past contact, then snap back to chamber.",
        ],
        "requirements": [
            "An open hand with fingers together and snapped back at the moment of impact.",
            "A locked straight wrist driving the palm heel, never a bent or floppy wrist.",
            "Hip-driven power from the bow stance, not arm-only pushing.",
            "Two to three inches of follow-through past the contact point.",
            "A full retraction to chamber after every strike.",
        ],
        "standards": [
            "Impact lands on the palm heel: finger-first contact fails the strike.",
            "The wrist stays straight under load; any backward bend ends the set until form is fixed.",
            "The strike visibly moves the bag or pad: a palm that does not push is a wave, not a strike.",
        ],
        "citations": [CIT_YANG, CIT_SMITH],
        "sig_lens": (
            "The Signature read: the pushing palm is the open hand's "
            "signature - no longer a fist's point but a seal's broad "
            "face, moving the whole mass it touches. Where public "
            "teaching files a palm strike, the Signature method files "
            "the push that relocates the world."
        ),
    },
    {
        "key": "shang_jia",
        "name": "Rising Block (Shang Jia)",
        "group": "Basic Techniques",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Shang jia, the rising block, sends the forearm upward from "
            "the hip to above the forehead, deflecting downward "
            "traveling attacks away at an angle. The block never meets "
            "force head-on: the forearm rises at roughly forty-five "
            "degrees to the incoming line, so an eight hundred newton "
            "downward strike is split - about five hundred sixty-six "
            "newtons slide off along the angled forearm while only about "
            "five hundred sixty-six newtons press into the block itself, "
            "and the deflection carries the attack past the head. The "
            "blocking surface is the outer forearm, the fist stays "
            "closed, and the elbow ends slightly bent above the forehead "
            "with the body settled low in stance. Shang jia is drilled "
            "against slow overhead strikes first, then against faster "
            "ones, and it is always paired with an immediate counter - "
            "the block is half a technique; the counter completes it."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: chamber the blocking arm across the "
            "body with the fist at the opposite hip, palm facing the "
            "body. Step 2: as the attack descends, drive the forearm "
            "upward and outward in a rising arc, rotating the fist so the "
            "palm faces outward at the top. Step 3: meet the attack with "
            "the outer forearm about a hand's width above the forehead, "
            "the forearm angled about forty-five degrees so the strike "
            "slides off rather than stopping dead. Step 4: settle the "
            "stance lower at the moment of contact - the block is rooted "
            "in the legs, not held up by the shoulder. Step 5: "
            "immediately counter with the other hand while the blocking "
            "arm stays in place for a beat. The classic errors are "
            "blocking with the flat of the forearm facing the strike "
            "square-on, which takes the full force; reaching up with a "
            "straight arm and a risen shoulder; and dropping the blocking "
            "arm instantly instead of holding it through the counter."
        ),
        "key_points": [
            "The forearm rises from the opposite hip to above the forehead, meeting the attack at about forty-five degrees.",
            "The angle splits the force: an eight hundred newton strike sheds about five hundred sixty-six newtons along the angled arm.",
            "Contact is made with the outer forearm, elbow slightly bent, fist closed, palm facing outward.",
            "The block is rooted by settling the stance lower at the moment of contact, not by shoulder strength.",
            "Every block is paired with an immediate counter from the other hand; the block alone is half a technique.",
        ],
        "requirements": [
            "A chambered start with the fist at the opposite hip, palm to the body.",
            "A rising arc that finishes with the forearm above the forehead at roughly forty-five degrees.",
            "Outer-forearm contact with a closed fist and slightly bent elbow.",
            "A stance that settles lower exactly at the moment of contact.",
            "An immediate counter strike thrown while the block holds its position.",
        ],
        "standards": [
            "The forearm never meets the attack square-on: the forty-five degree deflection angle is mandatory.",
            "The shoulder stays down; a shrugged block fails the rep.",
            "The blocking arm holds its ground through the counter, not dropping early.",
        ],
        "citations": [CIT_YANG, CIT_CHOW],
        "sig_lens": (
            "The Signature read: the rising block is the signature of "
            "refusal - the forearm rising at forty-five degrees, "
            "splitting eight hundred newtons and filing most of it away "
            "along the angle. Where public teaching files a block, the "
            "Signature method files a redirection with a counter "
            "attached."
        ),
    },
    {
        "key": "deng_tui",
        "name": "Front Snap Kick (Deng Tui)",
        "group": "Basic Techniques",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Deng tui, the front snap kick, is the first kick of Shaolin "
            "kung fu: the knee chambers up to the chest, the foot snaps "
            "straight out heel-first into the target, and the leg "
            "re-chambers along the same path. Deng means to stamp or "
            "pedal, and the kick stamps with the heel - the hardest, "
            "most compact striking surface of the foot. The leg is a "
            "heavy lever: a twelve-kilogram leg snapping the foot to "
            "nine meters per second carries about four hundred eighty-six "
            "joules of kinetic energy, which is why the kick is a "
            "fight-ending tool even at beginner level. The chamber is "
            "everything: the knee must rise fully before the foot "
            "extends, because a kick thrown from a low knee is a push, "
            "not a snap. Beginners drill the kick from the empty stance, "
            "where the kicking leg already carries no weight, and "
            "graduate to kicking from a full standing step."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: from the empty stance, keep the "
            "supporting leg slightly bent with the whole sole grounded. "
            "Step 2: snap the kicking knee straight up until the thigh "
            "is parallel to the floor and the lower leg hangs - this "
            "full chamber is non-negotiable. Step 3: drive the foot "
            "straight out toward the target, extending the knee sharply "
            "so the heel leads and the toes pull back toward the shin. "
            "Step 4: strike with the heel, the hips pushing slightly "
            "forward into the kick, then immediately re-chamber the knee "
            "back to the chest along the same path. Step 5: set the foot "
            "back down into the empty stance without stamping it down. "
            "The classic errors are extending the foot before the knee "
            "has chambered, which bleeds all the power; pointing the "
            "toes, which exposes them to injury; and leaning the torso "
            "back away from the kick, which pulls the hips out of the "
            "strike. Drill ten kicks per leg against a pad, demanding a "
            "sharp crack of the pad on every rep."
        ),
        "key_points": [
            "Chamber first: the knee rises to the chest with the thigh parallel to the floor before the foot extends.",
            "The heel leads with toes pulled back; the heel is the striking surface, never the toes.",
            "A twelve-kilogram leg at nine meters per second carries about four hundred eighty-six joules.",
            "Re-chamber along the same path immediately after impact; a left-out leg is a caught leg.",
            "Drilled from the empty stance first, where the kicking leg already carries no weight.",
        ],
        "requirements": [
            "A full knee chamber with the thigh parallel to the floor before any extension.",
            "Heel-first extension with the toes pulled back toward the shin.",
            "A slightly bent supporting leg with the whole sole grounded through the kick.",
            "Hip drive pushing slightly forward into the strike at the moment of extension.",
            "Immediate re-chamber and a controlled set-down back into stance.",
        ],
        "standards": [
            "No extension before the chamber: a kick that extends from a low knee is a failed rep.",
            "The toes stay pulled back on every rep; pointed toes end the set.",
            "The pad cracks sharply on contact: a pushing thud means the snap was lost.",
        ],
        "citations": [CIT_YANG, CIT_CHOW, CIT_SMITH],
        "sig_lens": (
            "The Signature read: the front snap kick files the leg as a "
            "stamp - chambered like a loaded seal, driven heel-first at "
            "nine meters per second, then withdrawn along its own line. "
            "Where public teaching files a kick, the Signature method "
            "files four hundred eighty-six joules of punctuation."
        ),
    },
    {
        "key": "ce_chuai",
        "name": "Side Kick (Ce Chuai)",
        "group": "Basic Techniques",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Ce chuai, the side kick, chambers the knee across the body "
            "and then extends the leg straight out to the side, striking "
            "with the heel or the outer edge of the foot. Chuai means to "
            "kick with a thrusting stamp, and the side kick is the most "
            "powerful kick in the basic syllabus because the full hip "
            "and the whole leg drive along one line into the target. "
            "With a leg ninety-two centimeters long, full extension "
            "reaches ninety-two centimeters from the hip, and the "
            "training target is set at eighty percent of maximum reach - "
            "about seventy-four centimeters - where the leg still holds "
            "its structure at impact. The kick demands a full pivot on "
            "the supporting foot: the heel of the support foot must turn "
            "to point at the target, which opens the hip and lets the "
            "kicking leg travel straight. Without the pivot the hip "
            "stays closed and the kick collapses into a weak angled push."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: from a fighting stance, shift the "
            "weight onto the supporting leg. Step 2: chamber the kicking "
            "knee up and across the body so the knee points at the "
            "target line while the foot stays tucked. Step 3: pivot on "
            "the ball of the supporting foot until its heel points at "
            "the target - this opens the hip fully and is the key to the "
            "whole kick. Step 4: extend the kicking leg straight out to "
            "the side in one thrusting line, striking with the heel or "
            "the outer edge of the foot, toes pulled back. Step 5: "
            "re-chamber the knee back across the body and set the foot "
            "down without losing balance. The classic errors are "
            "skipping the pivot, which leaves the hip closed and the "
            "kick weak; leaning the torso away from the kick instead of "
            "keeping it upright; and striking with the flat of the foot "
            "instead of the heel or edge. Drill against a pad held at "
            "about seventy-four centimeters from the hip - eighty "
            "percent of a ninety-two centimeter leg - and demand a "
            "thrusting impact, not a slap."
        ),
        "key_points": [
            "The knee chambers across the body, then the leg extends straight sideways, striking with heel or outer edge.",
            "The supporting foot pivots until its heel points at the target: no pivot, no hip opening, no power.",
            "A ninety-two centimeter leg reaches ninety-two centimeters; the training target sits at eighty percent, about seventy-four centimeters.",
            "The kick is a thrusting stamp along one line: the full hip drives behind the heel.",
            "Re-chamber across the body and set down with balance intact; the torso stays upright throughout.",
        ],
        "requirements": [
            "A cross-body knee chamber with the foot tucked before any extension.",
            "A complete pivot on the supporting foot with the heel turned to the target.",
            "Heel-or-edge contact with the toes pulled back, never the flat of the foot.",
            "An upright torso with no sideways lean away from the kick.",
            "A full re-chamber and controlled set-down after every kick.",
        ],
        "standards": [
            "The pivot is verified on every rep: the support heel points at the target at full extension.",
            "Contact is heel or outer edge only; flat-foot contact fails the rep.",
            "The kick thrusts the pad back along the kick line; a slapping impact means the hip never opened.",
        ],
        "citations": [CIT_YANG, CIT_SMITH],
        "sig_lens": (
            "The Signature read: the side kick is the signature written "
            "sideways - the hip the hand, the heel the pen, thrust along "
            "one straight line at eighty percent of the leg's full "
            "reach. Where public teaching files a kick, the Signature "
            "method files a stamp delivered on a pivot."
        ),
    },
    {
        "key": "huan_bu",
        "name": "Stance Transitions (Huan Bu Fa)",
        "group": "Basic Techniques",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Huan bu fa, the method of changing stances, is the footwork "
            "that connects every stance in the art: stepping forward "
            "(shang bu), stepping back (che bu), and shifting between "
            "horse, bow, empty, and cross stances without rising up or "
            "losing balance. Stances are only as useful as the steps "
            "between them, and the rule of Shaolin footwork is that the "
            "body's height never changes during a transition - the head "
            "rides level like a bowl of water carried on the crown. The "
            "training measure is cadence: beginners drill transitions at "
            "sixty steps per minute, intermediates at ninety, and "
            "advanced students at one hundred twenty, with each step "
            "covering about sixty centimeters. A three-minute drill at "
            "ninety steps per minute therefore covers roughly one "
            "hundred sixty-two meters of stance changes - footwork as "
            "conditioning as well as skill. Every form is, at bottom, a "
            "sequence of huan bu with hand techniques attached."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: begin in the horse stance at full "
            "depth, thighs parallel to the floor. Step 2: to step forward "
            "into a bow stance, slide the back foot up to the front foot "
            "without rising, then step the front foot forward sixty "
            "centimeters and sink into the bow stance - the head stays "
            "level throughout. Step 3: to shift to the empty stance, draw "
            "the front foot back to the ball-of-foot position while "
            "sinking the weight onto the back leg. Step 4: to step back, "
            "reverse the pattern, always moving the feet along the floor "
            "rather than lifting them high. Step 5: drill the cycle - "
            "horse to bow to empty to cross and back - to a metronome, "
            "starting at sixty steps per minute and adding ten per week "
            "toward one hundred twenty. The classic errors are bobbing "
            "up between stances, which breaks the root; taking steps of "
            "uneven length, which breaks the rhythm; and letting the "
            "hands drop while the feet work, which breaks the guard. "
            "Practice facing a wall with a hand lightly touching it: if "
            "the hand presses or leaves the wall, the head bobbed."
        ),
        "key_points": [
            "Footwork connects the stances: step forward, step back, and shift between horse, bow, empty, and cross without rising.",
            "The head rides level through every transition, like a bowl of water on the crown - no bobbing.",
            "Cadence ladder: sixty steps per minute beginner, ninety intermediate, one hundred twenty advanced.",
            "At ninety steps per minute with sixty-centimeter steps, a three-minute drill covers about one hundred sixty-two meters.",
            "Every form is a sequence of stance transitions with hand techniques attached.",
        ],
        "requirements": [
            "Full-depth stances at both ends of every transition: no rising up between them.",
            "Feet that slide and step along the floor, not lifted high or stamped.",
            "Steps of even length - about sixty centimeters - kept to a metronome.",
            "Hands held in guard throughout: the feet work, the hands do not rest.",
            "The wall test: a light hand on a wall must neither press nor leave it during transitions.",
        ],
        "standards": [
            "Head height is constant: any visible bob fails the drill.",
            "Step length stays even within ten centimeters across the whole drill.",
            "Cadence holds steady for the full three minutes without rushing or fading.",
        ],
        "citations": [CIT_YANG, CIT_CHOW],
        "sig_lens": (
            "The Signature read: stance transitions are the cursive "
            "between the signatures - the stances are the characters, "
            "the footwork the strokes that join them, written at up to "
            "one hundred twenty steps per minute without the head ever "
            "bobbing. Where public teaching files footwork, the "
            "Signature method files the connective script."
        ),
    },
    {
        "key": "wu_bu_quan",
        "name": "Five Stance Fist (Wu Bu Quan)",
        "group": "Basic Forms",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Wu bu quan, the Five Stance Fist, is the first complete form "
            "of Shaolin kung fu: a short sequence that links the five "
            "fundamental stances - horse, bow, empty, crouch, and cross - "
            "with punches, palm strikes, and blocks into one flowing "
            "pattern. It is the graduation exercise of the foundations: "
            "a student who can perform wu bu quan cleanly has proven "
            "every basic stance and every basic hand technique under the "
            "pressure of continuous movement. The form runs about forty "
            "movements; at a beginner tempo of one and a half seconds per "
            "movement it takes roughly sixty seconds, at a crisp one "
            "second per movement about forty seconds, and at a sharp "
            "three-quarter second pace about thirty seconds. Each stance "
            "must still hit full depth inside the flow - the form tests "
            "whether the stances survive when the student is thinking "
            "about what comes next. Traditionally it is practiced daily "
            "for months before any longer form is taught."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: open with the Shaolin salute from the "
            "natural stance, then drop into the horse stance. Step 2: "
            "perform the first section in horse stance - alternating "
            "forward punches with full hip rotation, holding each stance "
            "at full depth. Step 3: step forward through the stance "
            "transitions into bow stance for the punching and palm "
            "section, driving each technique from the back leg. Step 4: "
            "shift into the empty stance for the blocking section, "
            "keeping the front leg light and ready. Step 5: drop through "
            "the crouch stance and the cross stance for the low section, "
            "then rise and close with the salute. Practice the form in "
            "three passes: first pass slowly at one and a half seconds "
            "per movement checking every stance depth; second pass at one "
            "second per movement for flow; third pass at three-quarter "
            "second pace for sharpness. The classic errors are letting "
            "the stances rise as the form speeds up, pausing between "
            "sections instead of flowing, and forgetting the closing "
            "salute."
        ),
        "key_points": [
            "The first complete Shaolin form: five stances linked with punches, palms, and blocks in one flowing pattern.",
            "About forty movements: roughly sixty seconds at beginner tempo, forty at crisp pace, thirty at sharp pace.",
            "Every stance must hold full depth inside the flow; the form tests stances under the pressure of sequence.",
            "The graduation exercise of the foundations: clean wu bu quan proves every basic stance and hand technique.",
            "Practiced daily for months before any longer form is taught; three passes per session at three tempos.",
        ],
        "requirements": [
            "All five stances - horse, bow, empty, crouch, cross - at full depth throughout the form.",
            "The opening and closing Shaolin salute, performed with the same precision as in stillness.",
            "Continuous flow with no pauses between sections.",
            "Three practice passes per session: slow check, flowing, then sharp.",
            "Hip-driven hand techniques on every punch and palm, even at speed.",
        ],
        "standards": [
            "Stance depth at speed matches stance depth in stillness: rising under tempo fails the pass.",
            "The form runs without hesitation from salute to salute; a forgotten sequence restarts the pass.",
            "Each tempo pass hits its timing: sixty, forty, and thirty seconds within a five-second margin.",
        ],
        "citations": [CIT_YANG, CIT_WONG, CIT_CHOW],
        "sig_lens": (
            "The Signature read: the Five Stance Fist is the first full "
            "signature of the student - five stance-characters written "
            "in one flowing hand across forty movements and sixty "
            "seconds. Where public teaching files a beginner form, the "
            "Signature method files the proof that the foundations hold "
            "under motion."
        ),
    },
    {
        "key": "tan_tui",
        "name": "Spring Legs (Tan Tui Shi Er Lu)",
        "group": "Basic Forms",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Tan tui, Spring Legs, is the twelve-road kicking form that "
            "builds the legs of northern kung fu: twelve short roads "
            "(shi er lu), each a compact sequence of kicks, stances, and "
            "punches, drilled until the legs snap like springs. Tan "
            "means to spring or snap, and every kick in the form is "
            "thrown with that elastic quality - chamber, snap, "
            "re-chamber - rather than swung. The twelve roads are "
            "trained as a ladder: road one at hip height, about ninety "
            "centimeters, with each road adding roughly five centimeters "
            "of target height, so road twelve demands kicks at about "
            "one hundred forty-five centimeters - head height for most "
            "students. Each road takes about twenty seconds at training "
            "tempo, so the full twelve run about four minutes of "
            "continuous kicking. Tan tui is the reason northern stylists "
            "are famous for their legs: months of the twelve roads give "
            "the kicking endurance and snap that single-kick drilling "
            "alone cannot."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: learn road one alone - a short "
            "sequence of front snap kicks and bow-stance punches at hip "
            "height - drilling it until the chamber-snap-rechamber "
            "cycle is automatic. Step 2: add one road per week, each new "
            "road introducing a new kick or combination at five "
            "centimeters more height than the last. Step 3: drill each "
            "road ten times per side before moving on, demanding the "
            "spring quality on every kick: the foot must snap out and "
            "back, never swing. Step 4: once all twelve roads are known, "
            "run them in sequence at twenty seconds per road for the "
            "four-minute full set. Step 5: finish every session with the "
            "roads performed at full speed and full height, then walk "
            "the legs out with slow stance transitions. The classic "
            "errors are swinging the kicks from the hip without "
            "chambering, letting the target height sag as fatigue sets "
            "in, and holding the breath through the roads instead of "
            "breathing with each kick."
        ),
        "key_points": [
            "Twelve short roads, each a compact kicking sequence drilled until the legs snap like springs.",
            "Height ladder: road one at about ninety centimeters, plus five centimeters per road, to about one hundred forty-five at road twelve.",
            "Each road runs about twenty seconds; the full twelve take about four minutes of continuous kicking.",
            "Every kick keeps the spring quality - chamber, snap, re-chamber - and is never swung from the hip.",
            "New road added weekly; each road drilled ten times per side before advancing.",
        ],
        "requirements": [
            "The front snap kick's full chamber on every kick in every road.",
            "Target heights honored per road: the height ladder is the training, not a suggestion.",
            "Ten repetitions per side per road before a new road is added.",
            "Breathing synchronized with the kicks: exhale on each snap.",
            "The four-minute full twelve-road set performed at the end of each kicking session.",
        ],
        "standards": [
            "The snap is audible on the pad: a swinging kick that thuds instead of cracks fails the road.",
            "Road twelve is kicked at genuine head height: sagging targets fail the set.",
            "All twelve roads run without stopping: a break mid-set restarts the count.",
        ],
        "citations": [CIT_YANG, CIT_CHOW, CIT_SMITH],
        "sig_lens": (
            "The Signature read: Spring Legs files the legs as twelve "
            "wound springs, each road tensioned five centimeters higher "
            "than the last until the twelfth releases at head height. "
            "Where public teaching files a kicking form, the Signature "
            "method files the ladder the legs climb."
        ),
    },
    {
        "key": "hu_zhao",
        "name": "Tiger Claw Strike (Hu Zhao)",
        "group": "Animal Styles",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Hu zhao, the tiger claw, shapes the hand into the tiger's "
            "weapon: fingers spread wide and hooked at the joints, thumb "
            "pressed out to the side, the palm hollowed - a claw that "
            "strikes, rakes, and grabs. The tiger is the first of the "
            "five Shaolin animals taught because its lesson is the "
            "simplest: committed ferocity. The claw rakes downward and "
            "across in arcs about forty centimeters long - a hand with a "
            "nineteen-centimeter reach sweeping a one-hundred-twenty-"
            "degree arc carves roughly forty centimeters of raking path - "
            "tearing with the fingertips, then closes into a grip that "
            "pulls the target into a knee or a throw. Tiger training "
            "pairs the claw with deep horse-stance work, because the "
            "tiger's power comes from a low, rooted body driving forward. "
            "The hands are conditioned gradually: fingertip pushups on a "
            "soft surface, then claw strikes into a canvas bag of rice, "
            "building the finger strength the technique demands."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: form the claw - spread all five "
            "fingers wide, hook them at the second joints like talons, "
            "press the thumb out sideways, and hollow the palm. Step 2: "
            "settle into a deep horse stance, because the tiger strikes "
            "from a low root. Step 3: rake the claw downward and across "
            "the target in a forty-centimeter arc, leading with the "
            "fingertips and driving from the hip and shoulder, not the "
            "wrist. Step 4: at the end of the rake, close the claw into "
            "a full grip and pull sharply back toward the hip. Step 5: "
            "condition the hands three times a week - start with "
            "fingertip pushups against a wall, progress to the floor, "
            "and rake a rice-filled canvas bag in sets of twenty per "
            "hand. The classic errors are raking with a flat slapping "
            "hand instead of hooked talons, striking from a high weak "
            "stance, and pulling with the arm while the hip stays still."
        ),
        "key_points": [
            "The claw: fingers spread and hooked at the second joints, thumb out, palm hollowed - a striking, raking, grabbing tool.",
            "The rake travels about forty centimeters: a nineteen-centimeter hand sweeping one hundred twenty degrees.",
            "The tiger is the first animal taught: its lesson is committed ferocity from a low root.",
            "Each rake ends by closing into a grip and pulling the target back toward the hip.",
            "Hands conditioned progressively: wall fingertip pushups, then floor, then raking a rice bag in sets of twenty.",
        ],
        "requirements": [
            "A true claw shape on every rep: hooked fingers, out thumb, hollow palm - never a flat slap.",
            "A deep horse stance beneath every strike: the tiger does not strike from high stances.",
            "Hip and shoulder driving each rake, with the wrist firm and uninvolved.",
            "The rake-to-grip-to-pull sequence completed on every technique, not just the rake.",
            "Hand conditioning three times weekly, progressed from wall to floor to rice bag.",
        ],
        "standards": [
            "The fingertips lead visibly: a flat-handed rake fails the rep.",
            "The stance stays at full horse depth through the whole raking set.",
            "The rice bag shows the rake marks: twenty strikes per hand leave twenty clean raking lines.",
        ],
        "citations": [CIT_WONG, CIT_CHOW, CIT_SHAHAR],
        "sig_lens": (
            "The Signature read: the tiger claw is the first animal "
            "seal - five talons hooked and filed as one weapon, raking "
            "forty centimeters of arc from a horse-stance root. Where "
            "public teaching files a claw strike, the Signature method "
            "files ferocity with a grip at the end of it."
        ),
    },
    {
        "key": "she_quan",
        "name": "Snake Fist Hand Form (She Quan)",
        "group": "Animal Styles",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "She quan, the snake style, shapes the hand into the snake's "
            "head: fingers pressed tightly together and extended, thumb "
            "tucked against the palm, the whole hand a flat spearhead. "
            "The snake's lesson is precision and speed over power - the "
            "hand darts out like a striking serpent to soft targets, "
            "then coils back instantly. A trained snake-hand dart covers "
            "sixty centimeters of extension in about twelve hundredths "
            "of a second, reaching roughly five meters per second at the "
            "fingertips - too fast to catch, aimed where armor does not "
            "cover. The body coils with the strike: the waist turns, the "
            "stance shifts between bow and empty, and the withdrawing "
            "hand guards the line the striking hand just left. Snake "
            "training emphasizes finger and wrist conditioning - pressing "
            "the spearhead hand into a sand tray in sets of fifty - "
            "because the technique is worthless if the fingers buckle on "
            "contact."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: form the snake hand - press all four "
            "fingers tightly together and extend them straight, tuck the "
            "thumb tight against the palm, and stiffen the wrist so the "
            "hand is one flat spearhead. Step 2: chamber the hand at the "
            "ribs with the elbow down. Step 3: dart the hand straight out "
            "at the target, extending the arm fully in about twelve "
            "hundredths of a second, the body coiling forward from the "
            "waist as the hand flies. Step 4: snap the hand back along "
            "the same line the instant it reaches full extension - the "
            "snake never leaves its head out. Step 5: condition the hand "
            "daily by pressing the spearhead into a tray of sand in sets "
            "of fifty, keeping the fingers perfectly straight under "
            "pressure. The classic errors are letting the fingers splay "
            "on impact, which collapses the spearhead; darting with the "
            "arm while the waist stays still; and leaving the hand "
            "extended, which invites it to be grabbed."
        ),
        "key_points": [
            "The snake hand: fingers pressed tight and extended, thumb tucked, wrist stiff - a flat spearhead.",
            "The dart covers sixty centimeters in about twelve hundredths of a second: roughly five meters per second at the fingertips.",
            "Precision over power: the strike darts to soft targets and coils back instantly.",
            "The waist coils with every dart; the withdrawing hand guards the line just vacated.",
            "Daily conditioning: pressing the spearhead into sand in sets of fifty with fingers perfectly straight.",
        ],
        "requirements": [
            "A true spearhead hand on every rep: fingers together, thumb tucked, wrist locked straight.",
            "Full sixty-centimeter extension completed in the dart, not a short jab.",
            "Instant withdrawal along the same line the moment full extension is reached.",
            "Waist-driven coiling behind every dart, never arm-only striking.",
            "Daily sand-tray pressing in sets of fifty to condition the fingers and wrist.",
        ],
        "standards": [
            "The fingers never splay on contact: a buckled spearhead fails the set.",
            "The dart visibly blurs: a slow, trackable hand is not yet the snake.",
            "The hand returns to chamber faster than it left; a lingering hand fails the rep.",
        ],
        "citations": [CIT_WONG, CIT_SHAHAR, CIT_CHOW],
        "sig_lens": (
            "The Signature read: the snake is the second animal seal - "
            "the hand filed to a single spearhead point, darting sixty "
            "centimeters in twelve hundredths of a second and gone "
            "before it can be caught. Where public teaching files a "
            "hand shape, the Signature method files speed that refuses "
            "to be held."
        ),
    },
    {
        "key": "he_zui",
        "name": "Crane Beak Strike (He Zui)",
        "group": "Animal Styles",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "He zui, the crane beak, pinches the thumb and fingertips "
            "together into a sharp point - the beak of the crane - and "
            "pecks with it in short, precise strikes. The crane's lesson "
            "is grace under precision: the body stays light and balanced, "
            "often on one leg, while the beak darts to small, exact "
            "targets. The physics of the beak is concentration: a four "
            "hundred newton peck delivered through a beak tip of two "
            "square centimeters (two ten-thousandths of a square meter) "
            "produces about two million pascals of pressure - the force "
            "of a much heavier blow focused onto a point. Crane training "
            "pairs the beak with single-leg stance work, because the "
            "crane's classic posture is du li bu, the crane standing on "
            "one leg, striking while perfectly balanced. The beak is "
            "formed slowly and carefully hundreds of times before it is "
            "ever struck with, since a collapsed beak injures the "
            "striker's own fingers."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: form the beak - bring the thumb and "
            "all four fingertips together into a single point, pressing "
            "them firmly so the hand forms a tight cone. Step 2: settle "
            "into the single-leg stance, the crane's own posture, with "
            "the standing leg rooted and the body tall. Step 3: peck the "
            "beak forward and slightly down in a short darting motion, "
            "driving from the shoulder and elbow with the wrist locked, "
            "aiming at a precise small target. Step 4: snap the beak "
            "back to guard immediately - the peck is a touch and a "
            "withdrawal, never a push. Step 5: drill the beak formation "
            "itself daily: form and release the point one hundred times, "
            "then peck a soft hanging target in sets of twenty per hand. "
            "The classic errors are a loose beak that collapses on "
            "contact, pecking with the wrist bent, and losing the "
            "single-leg balance by leaning into the peck instead of "
            "staying tall."
        ),
        "key_points": [
            "The beak: thumb and fingertips pinched into one tight point, a cone of concentrated force.",
            "Four hundred newtons through a two-square-centimeter tip yields about two million pascals of pressure.",
            "The crane's lesson is grace under precision: light, balanced, exact - often fought from the single-leg stance.",
            "The peck is a darting touch and instant withdrawal, never a push or a lean.",
            "Beak formation drilled daily: one hundred formations before striking sets of twenty per hand.",
        ],
        "requirements": [
            "A tight, collapsed-proof beak on every rep: thumb and fingertips pressed into one point.",
            "A locked wrist driving the peck from shoulder and elbow.",
            "The single-leg stance held tall and balanced through every peck.",
            "Short darting pecks with immediate withdrawal, never leaning pushes.",
            "Daily beak-formation practice: one hundred formations plus striking sets.",
        ],
        "standards": [
            "The beak holds its point under pressure: any collapse fails the set until formation is rebuilt.",
            "Balance never wavers: the standing foot stays planted and the torso stays tall.",
            "Each peck lands on the marked small target; scattered pecks are not yet the crane.",
        ],
        "citations": [CIT_WONG, CIT_SHAHAR],
        "sig_lens": (
            "The Signature read: the crane beak is the third animal "
            "seal - the whole hand filed down to a single point that "
            "delivers two million pascals from a balanced crane's leg. "
            "Where public teaching files a hand shape, the Signature "
            "method files precision standing on one leg."
        ),
    },
    {
        "key": "bao_quan",
        "name": "Leopard Fist Strike (Bao Quan)",
        "group": "Animal Styles",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Bao quan, the leopard fist, folds the fingers only at the "
            "second joints so the middle knuckles form a striking ridge - "
            "the leopard's paw, half open and half closed. The leopard's "
            "lesson is speed and angles: where the tiger commits to the "
            "straight line, the leopard darts in from the side with fast, "
            "whipping strikes. The half-fist concentrates force on a "
            "small ridge: at twelve hundred newtons of striking force, "
            "the leopard's three square centimeters of knuckle ridge "
            "deliver about four million pascals, against about four "
            "hundred eighty thousand pascals for a full fist's twenty-"
            "five square centimeters - more than eight times the "
            "pressure from the same arm. Leopard techniques pair the "
            "fist with quick stance shifts and low, darting footwork, "
            "and the style's combinations chain three or four strikes "
            "where other styles throw one. The knuckles are conditioned "
            "on a canvas bag, because the ridge must be bone-hard to "
            "survive its own physics."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: form the leopard fist - fold the "
            "fingers at the second joints only, pressing the middle "
            "knuckles forward into a flat ridge, with the thumb braced "
            "against the side of the index finger. Step 2: chamber at "
            "the hip or ribs with the ridge facing forward. Step 3: whip "
            "the fist out in a fast, slightly hooking line, snapping the "
            "wrist at the end so the knuckle ridge leads into the "
            "target. Step 4: retract instantly and follow with the "
            "second and third strikes of the combination - the leopard "
            "never throws one strike alone. Step 5: condition the ridge "
            "three times a week with sets of thirty strikes per hand "
            "into a canvas bag, starting light and building force over "
            "months. The classic errors are folding the fingers into a "
            "full fist, which loses the ridge; striking with a bent "
            "wrist that collapses the angle; and throwing single "
            "leopard strikes instead of the style's chained "
            "combinations."
        ),
        "key_points": [
            "The leopard fist: fingers folded at the second joints, middle knuckles forming a flat striking ridge.",
            "Twelve hundred newtons over three square centimeters gives about four million pascals - over eight times a full fist's pressure.",
            "The leopard's lesson is speed and angles: fast whipping strikes darting in from the side, never one alone.",
            "Each strike ends with a wrist snap driving the knuckle ridge into the target, then instant retraction.",
            "Knuckle conditioning: sets of thirty per hand into a canvas bag, three times weekly, force built over months.",
        ],
        "requirements": [
            "A true half-fist ridge on every rep: second-joint fold, thumb braced, never a full fist.",
            "A wrist snap at impact driving the ridge forward with a straight, firm wrist.",
            "Chained combinations of three to four strikes: single leopard strikes are incomplete.",
            "Quick stance shifts and low darting footwork beneath the hands.",
            "Progressive knuckle conditioning on the canvas bag, never jumping to full force.",
        ],
        "standards": [
            "The ridge is visible and flat at impact: a curled full fist fails the rep.",
            "The wrist stays straight under the snap; any collapse ends the set.",
            "Combinations flow without pauses: a broken chain restarts the combination.",
        ],
        "citations": [CIT_WONG, CIT_CHOW, CIT_SHAHAR],
        "sig_lens": (
            "The Signature read: the leopard fist is the fourth animal "
            "seal - the hand half-closed and filed to a knuckle ridge "
            "that multiplies pressure eightfold, thrown in chains of "
            "three and four. Where public teaching files a fist "
            "variation, the Signature method files speed that arrives "
            "from the side."
        ),
    },
    {
        "key": "long_xing",
        "name": "Dragon Form (Long Xing Quan)",
        "group": "Animal Styles",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Long xing, the dragon form, moves like the mythical dragon: "
            "the waist coils and uncoils, the body weaves in zigzag "
            "stepping, and the hands strike with dragon claws - three-"
            "fingered gripping claws that seize and tear. The dragon's "
            "lesson is flowing, whole-body power: every technique is "
            "driven by the waist's rotation, and the waist is the "
            "dragon's engine. The physics are rotational: a waist "
            "turning one hundred eighty degrees in half a second spins "
            "at about six point three radians per second, and a hand "
            "riding at sixty-five centimeters from the spine reaches "
            "about four point one meters per second from the waist turn "
            "alone - before the arm even extends. Dragon stepping "
            "zigzags low across the floor in bow and cross stances, the "
            "torso twisting with each step so the practitioner is never "
            "a flat target. The form trains the practitioner to think in "
            "spirals: power that corkscrews instead of pushing straight."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: form the dragon claw - thumb, index, "
            "and middle finger extended and slightly hooked, ring and "
            "little finger folded - a three-fingered seizing claw. Step "
            "2: settle into a bow stance and coil the waist fully to one "
            "side, winding the torso like a spring. Step 3: unwind the "
            "waist explosively toward the target, letting the coiled "
            "torso whip the clawed hand out in a seizing strike - the "
            "hand travels because the waist turned, not because the arm "
            "pushed. Step 4: step zigzag to the next position, coiling "
            "the waist to the opposite side with each step, keeping the "
            "body low and the torso twisted. Step 5: drill the waist "
            "coil alone first - one hundred eighty degree turns in half "
            "a second, ten per side - until the four point one meters "
            "per second hand speed comes from the turn itself, then add "
            "the claws and the stepping. The classic errors are arming "
            "the strike while the waist stays still, stepping in "
            "straight lines instead of zigzags, and standing tall, which "
            "unwinds the coil."
        ),
        "key_points": [
            "The dragon claw: three hooked fingers - thumb, index, middle - a seizing and tearing tool.",
            "The waist is the engine: a one-hundred-eighty-degree turn in half a second spins at about six point three radians per second.",
            "A hand at sixty-five centimeters from the spine reaches about four point one meters per second from the waist turn alone.",
            "Stepping zigzags low through bow and cross stances with the torso coiling each step: never a flat target.",
            "The dragon's lesson is flowing whole-body power that corkscrews instead of pushing straight.",
        ],
        "requirements": [
            "A true three-fingered dragon claw on every hand technique.",
            "Full waist coiling before every strike: the torso winds like a spring, then releases.",
            "Zigzag stepping kept low, with the body twisting into each new position.",
            "Hand speed visibly coming from the waist turn, not from arm pushing.",
            "Solo waist-coil drilling - ten full turns per side - before the claws are added.",
        ],
        "standards": [
            "The waist turns first on every technique: an arm-led strike fails the rep.",
            "The stepping pattern zigzags: straight-line stepping fails the drill.",
            "The body stays low and twisted; standing tall unwinds the dragon.",
        ],
        "citations": [CIT_WONG, CIT_SHAHAR, CIT_CHOW],
        "sig_lens": (
            "The Signature read: the dragon is the fifth animal seal - "
            "the waist filed as the engine, coiling and releasing at "
            "six point three radians per second while the body zigzags "
            "in spirals. Where public teaching files a form, the "
            "Signature method files power that corkscrews."
        ),
    },
    {
        "key": "hei_hu",
        "name": "Black Tiger Fist (Hei Hu Quan)",
        "group": "Animal Styles",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Hei hu quan, the Black Tiger Fist, is the aggressive tiger "
            "form of Shaolin: deep stances, heavy claw and palm strikes, "
            "and a forward pressure that never steps back. Where the "
            "single tiger claw strike teaches the weapon, the Black "
            "Tiger form teaches the tiger's temperament - every "
            "combination advances, every block becomes a grab, every "
            "grab becomes a pull into a knee or throw. The form's "
            "combinations are built on a strict timing: three strikes in "
            "three-quarter of a second, each strike landing a quarter "
            "second apart, so the practitioner learns to chain heavy "
            "techniques without the pauses that let an opponent recover. "
            "A ten-combination drill therefore delivers thirty strikes in "
            "about seven and a half seconds of impact time, with the "
            "footwork flowing continuously beneath. Black Tiger is "
            "traditionally taught after the student has proven the basic "
            "tiger claw and the horse stance, because the form's low, "
            "driving stances punish weak legs immediately."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: open from the salute into a deep horse "
            "stance with tiger claws chambered at the hips. Step 2: "
            "drive forward into a bow stance, raking the lead claw down "
            "and across while the rear claw guards - the step and the "
            "rake land together. Step 3: without pausing, shift the "
            "weight and drive the rear claw forward in a palm-heel "
            "thrust, a quarter second after the rake. Step 4: complete "
            "the three-strike chain with a pulling grab that drags the "
            "target into a rising knee, the third quarter-second beat. "
            "Step 5: drill the three-strike timing to a metronome at "
            "four beats per second - strike on three consecutive beats, "
            "step on the fourth - until ten combinations flow without a "
            "pause. The classic errors are pausing between the strikes, "
            "which breaks the tiger's pressure; rising out of the deep "
            "stances as the form speeds up; and clawing with the arms "
            "while the steps lag behind the hands."
        ),
        "key_points": [
            "The aggressive tiger form: deep stances, heavy claws and palms, forward pressure that never steps back.",
            "Combination timing is strict: three strikes in three-quarter seconds, one every quarter second.",
            "Ten combinations deliver thirty strikes in about seven and a half seconds of impact time.",
            "Every block becomes a grab and every grab a pull: the tiger's techniques chain without pauses.",
            "Taught only after the basic tiger claw and a proven horse stance: the low driving stances punish weak legs.",
        ],
        "requirements": [
            "Deep horse and bow stances held at full depth through the entire form.",
            "The three-strike chain timed to quarter-second beats: rake, thrust, pull-to-knee.",
            "Continuous forward pressure: no backward steps anywhere in the form.",
            "Tiger claws formed correctly on every hand technique.",
            "Metronome drilling at four beats per second until ten combinations flow unbroken.",
        ],
        "standards": [
            "No pauses inside a combination: a gap between strikes fails the chain.",
            "Stance depth at form speed matches stance depth in stillness.",
            "The steps land with the strikes: hands and feet arrive together on every beat.",
        ],
        "citations": [CIT_WONG, CIT_CHOW, CIT_SHAHAR],
        "sig_lens": (
            "The Signature read: the Black Tiger is the tiger's "
            "temperament filed as a form - three strikes per "
            "three-quarter second, thirty strikes in seven and a half "
            "seconds, forward pressure with no step back. Where public "
            "teaching files an animal form, the Signature method files "
            "relentlessness on a metronome."
        ),
    },
    {
        "key": "xiao_hong_quan",
        "name": "Small Flood Fist (Xiao Hong Quan)",
        "group": "Classic Forms",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Xiao hong quan, the Small Flood Fist, is the classic "
            "beginner long form of Shaolin: hong means vast or flood-"
            "like, and the form moves like water rising - steady, "
            "continuous, and covering ground. It is traditionally the "
            "first long form taught after the basic short forms, and it "
            "contains the whole Shaolin alphabet in miniature: horse and "
            "bow stances, punches, palms, blocks, kicks, and turns, "
            "arranged in four sections of about twelve movements each - "
            "forty-eight movements in total. At a training tempo of one "
            "and a quarter seconds per movement the form runs about "
            "sixty seconds; at performance tempo of eight-tenths of a "
            "second per movement it runs about thirty-eight seconds. "
            "Xiao hong quan is the form by which Shaolin schools judge "
            "readiness for advanced training: a student who performs it "
            "with full stances, sharp techniques, and unbroken flow has "
            "earned the longer forms. It is practiced daily for a year "
            "or more before da hong quan, its bigger sibling, is taught."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: learn the form one section at a time - "
            "twelve movements per section - drilling each section until "
            "it flows before the next is added. Step 2: practice at the "
            "training tempo of one and a quarter seconds per movement, "
            "checking every stance depth and every technique's shape in "
            "a mirror. Step 3: link the sections, running the full "
            "forty-eight movements in about sixty seconds without "
            "stopping. Step 4: sharpen the tempo toward eight-tenths of "
            "a second per movement, about thirty-eight seconds for the "
            "form, while keeping the stances at full depth. Step 5: "
            "perform the form three times per session - once slow for "
            "precision, once at training tempo for flow, once at "
            "performance tempo for spirit. The classic errors are "
            "learning the whole form at once and knowing none of it "
            "well, letting the stances rise as the tempo sharpens, and "
            "pausing at the section boundaries instead of flowing "
            "through them."
        ),
        "key_points": [
            "The classic beginner long form: the whole Shaolin alphabet - stances, punches, palms, blocks, kicks, turns - in miniature.",
            "Four sections of about twelve movements: forty-eight movements total.",
            "About sixty seconds at training tempo, about thirty-eight seconds at performance tempo.",
            "The readiness test for advanced training: full stances, sharp techniques, unbroken flow.",
            "Learned one section at a time, practiced daily for a year or more before the bigger sibling form.",
        ],
        "requirements": [
            "Section-by-section learning: each twelve-movement section flows before the next is added.",
            "Full stance depth and clean technique shapes verified in a mirror at training tempo.",
            "The complete forty-eight-movement run without stopping, three times per session.",
            "Three tempos per session: slow for precision, training for flow, performance for spirit.",
            "Unbroken flow across the section boundaries: no pauses between sections.",
        ],
        "standards": [
            "The form's timing hits its marks: sixty seconds training, thirty-eight performance, within five seconds.",
            "Stance depth at performance tempo matches stance depth in the slow pass.",
            "The form runs start to finish from memory with no hesitation or restarting.",
        ],
        "citations": [CIT_YANG, CIT_WONG, CIT_SHAHAR, CIT_CHOW],
        "sig_lens": (
            "The Signature read: the Small Flood Fist is the first long "
            "signature - forty-eight movements filed in four sections, "
            "the whole alphabet of the art written in sixty seconds. "
            "Where public teaching files a beginner form, the Signature "
            "method files the entrance examination of the system."
        ),
    },
    {
        "key": "sao_tui",
        "name": "Sweeping Kick (Sao Tang Tui)",
        "group": "Basic Techniques",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Sao tang tui, the sweeping kick, whips the leg in a low "
            "circle to strike the opponent's supporting leg and take the "
            "root out from under them. Sao means to sweep, and the leg "
            "sweeps like a broom: the practitioner drops into the crouch "
            "stance and spins, the extended leg circling at ankle height. "
            "The geometry of the sweep is an area weapon: a ninety-"
            "centimeter leg sweeping a full one-hundred-eighty-degree arc "
            "covers about one point two seven square meters of floor - "
            "everything standing inside that half-circle is in range. "
            "The sweep connects with the lower shin or the inner ankle "
            "against the opponent's ankle or lower shin, timed to the "
            "moment their weight commits to the leg. It is trained first "
            "as a solo spin in the crouch stance for balance and speed, "
            "then against a padded target, and only then with a partner "
            "in controlled drills - because a real sweep drops a person "
            "to the floor."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: from a standing position, drop into "
            "the crouch stance with the sweeping leg extended. Step 2: "
            "pivot on the folded leg's foot and whip the extended leg "
            "around in a low, fast circle at ankle height, keeping the "
            "sweeping leg straight and the toes up. Step 3: strike with "
            "the lower shin or inner ankle against the target's ankle or "
            "lower shin, driving through the target rather than tapping "
            "it. Step 4: complete the spin and rise back to a guard "
            "stance in one motion, ready to follow up. Step 5: drill the "
            "solo spin first - ten full sweeps per side for speed and "
            "balance - then sweep a low padded target, then practice "
            "with a partner at quarter speed with full control. The "
            "classic errors are sweeping too high, which misses the "
            "ankle and wastes the technique; rising out of the crouch "
            "during the spin, which kills the power; and sweeping with "
            "the foot instead of the shin, which injures the sweeper's "
            "own ankle."
        ),
        "key_points": [
            "The leg whips in a low circle at ankle height from the crouch stance, striking the opponent's supporting leg.",
            "A ninety-centimeter leg sweeping one hundred eighty degrees covers about one point two seven square meters.",
            "Contact is lower shin or inner ankle against the target's ankle or lower shin, timed to their weight commitment.",
            "Trained in stages: solo spins, then padded target, then controlled partner drills at quarter speed.",
            "The spin completes and the practitioner rises to guard in one motion, ready to follow up.",
        ],
        "requirements": [
            "A full crouch stance as the launch position, held low through the entire spin.",
            "A straight sweeping leg with toes up, circling at genuine ankle height.",
            "Shin-or-inner-ankle contact: never the foot, which risks the sweeper's own ankle.",
            "Ten solo spins per side for speed and balance before any target work.",
            "Partner practice only at quarter speed with full control: a real sweep drops a person.",
        ],
        "standards": [
            "The sweep stays at ankle height: a high sweep fails the rep.",
            "The crouch stays low through the spin: rising up fails the rep.",
            "The spin completes into a balanced guard stance, not a stumble.",
        ],
        "citations": [CIT_YANG, CIT_CHOW, CIT_SMITH],
        "sig_lens": (
            "The Signature read: the sweeping kick files the leg as a "
            "broom - a ninety-centimeter arc covering one point two "
            "seven square meters of floor, erasing whatever root stands "
            "inside it. Where public teaching files a takedown kick, "
            "the Signature method files the removal of the ground "
            "beneath."
        ),
    },
    {
        "key": "da_hong_quan",
        "name": "Big Flood Fist (Da Hong Quan)",
        "group": "Classic Forms",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Da hong quan, the Big Flood Fist, is the longer, harder "
            "sibling of the Small Flood Fist: where the small form runs "
            "forty-eight movements, the big form runs about ninety-six, "
            "with deeper stances, longer combinations, and jumps and "
            "sweeps the small form does not contain. It is traditionally "
            "taught only after a year or more of xiao hong quan, and it "
            "is a stamina test as much as a technique test - ninety-six "
            "movements at one second per movement run about ninety-six "
            "seconds of continuous full-power motion, and at roughly "
            "sixty joules of work per movement the form demands about "
            "five thousand seven hundred sixty joules from the "
            "practitioner. The form's longer combinations chain kicks "
            "into punches into sweeps without pause, and its turning "
            "sections demand the cross stance and crouch stance at speed. "
            "Da hong quan is the form that separates students who know "
            "techniques from students who can fight with them: "
            "everything is performed at full power, full depth, and full "
            "speed, with no rest anywhere inside."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: master xiao hong quan completely "
            "first - da hong quan is not taught to students who have not "
            "earned it through the small form. Step 2: learn the big "
            "form in six sections of about sixteen movements each, "
            "drilling each section at half speed until the longer "
            "combinations flow. Step 3: build stamina separately with "
            "stance holds and the twelve roads of tan tui, because the "
            "form's ninety-six seconds of continuous motion will expose "
            "any conditioning gap. Step 4: link the sections into the "
            "full ninety-six-movement run, practicing three times per "
            "session with full rest between runs. Step 5: sharpen to "
            "performance tempo - about one second per movement, ninety-"
            "six seconds total - with every stance at full depth and "
            "every technique at full power. The classic errors are "
            "starting the big form before the small form is truly "
            "mastered, fading in the final two sections as stamina "
            "fails, and shortening the combinations to survive the form "
            "instead of building the stamina to perform it."
        ),
        "key_points": [
            "The bigger sibling of the Small Flood Fist: about ninety-six movements with deeper stances, longer combinations, jumps, and sweeps.",
            "Ninety-six movements at one second each run about ninety-six seconds of continuous full-power motion.",
            "At roughly sixty joules per movement, the form demands about five thousand seven hundred sixty joules.",
            "Taught only after a year or more of the small form: it separates students who know techniques from students who can fight.",
            "Six sections of sixteen movements, learned at half speed, then linked and sharpened to performance tempo.",
        ],
        "requirements": [
            "Complete mastery of xiao hong quan before the first section of da hong quan is taught.",
            "Section-by-section learning at half speed: six sections of about sixteen movements.",
            "Separate stamina building through stance holds and tan tui kicking roads.",
            "The full ninety-six-movement run three times per session with full rest between.",
            "Full power, full depth, and full speed in the final performance: no rest anywhere inside.",
        ],
        "standards": [
            "The full form runs in about ninety-six seconds at one second per movement, within ten seconds.",
            "The final two sections match the first two in stance depth and technique sharpness: fading fails the run.",
            "No shortened combinations: every technique of the form is performed as taught.",
        ],
        "citations": [CIT_YANG, CIT_WONG, CIT_SHAHAR, CIT_CHOW],
        "sig_lens": (
            "The Signature read: the Big Flood Fist is the long "
            "signature - ninety-six movements, five thousand seven "
            "hundred sixty joules, no rest anywhere inside. Where "
            "public teaching files an advanced form, the Signature "
            "method files the flood that tests whether the small "
            "signature was real."
        ),
    },
    {
        "key": "gun_fa",
        "name": "Shaolin Staff Basics (Shao Lin Gun Fa)",
        "group": "Weapons",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Shao lin gun fa, the Shaolin staff method, is the foundation "
            "of the art's weapons training: the staff is traditionally "
            "the first weapon taught, and the old saying holds that the "
            "staff sweeps a large area. The basic staff is about two "
            "meters long - roughly the practitioner's height plus a "
            "head - and the basics are grips, thrusts, sweeps, overhead "
            "blocks, and spins. The staff's physics reward rotation: "
            "spun at three revolutions per second, the tip of a two-"
            "meter staff (one meter from the hands) travels at about "
            "eighteen point eight meters per second - faster than any "
            "punch, which is why the staff dominates at range. The five "
            "basic techniques are the straight thrust (ci), the sweeping "
            "strike (sao), the overhead block (jia), the wrapping parry "
            "(chan), and the spinning strike (wu). Staff training begins "
            "with solo spinning for wrist strength and control, then "
            "partner drills with padded staves, and the iron rule from "
            "the first day is control: a two-meter lever at eighteen "
            "meters per second forgives nothing."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: take the staff with a grip one hand "
            "at each end-third, hands about shoulder-width apart, and "
            "learn the ready posture in a horse stance. Step 2: drill "
            "the straight thrust - slide the rear hand forward and drive "
            "the tip straight at the target, then pull it back - in sets "
            "of twenty per side. Step 3: drill the sweeping strike, "
            "swinging the staff in a horizontal arc at waist height with "
            "the hips turning behind it. Step 4: drill the overhead "
            "block, raising the staff horizontally above the head to meet "
            "downward attacks, and the spinning strike, rotating the "
            "staff around the body in a full circle. Step 5: practice "
            "solo spinning daily - figure-eight spins in front of the "
            "body, ten per direction - to build the wrist strength and "
            "control the weapon demands. The classic errors are gripping "
            "too tightly, which kills the spin; letting the tip drop "
            "during spins, which kills the line; and practicing near "
            "people or walls before control is earned. Train with a "
            "padded or rattan staff until the spins stay clean for a "
            "full minute."
        ),
        "key_points": [
            "The first weapon of Shaolin: about two meters long, the staff sweeps a large area.",
            "Spun at three revolutions per second, the staff tip travels at about eighteen point eight meters per second.",
            "The five basics: thrust, sweeping strike, overhead block, wrapping parry, spinning strike.",
            "Training order: solo spinning for control, then padded partner drills - control is the iron rule from day one.",
            "Daily figure-eight spins, ten per direction, build the wrist strength the weapon demands.",
        ],
        "requirements": [
            "A staff of about the practitioner's height plus a head, gripped at the end-thirds.",
            "The ready posture in horse stance with hands shoulder-width apart on the staff.",
            "Clean execution of all five basic techniques: thrust, sweep, block, parry, spin.",
            "Daily solo spinning practice: figure-eights, ten per direction, tip never dropping.",
            "A padded or rattan staff and clear space until a full minute of clean spins is earned.",
        ],
        "standards": [
            "The staff tip stays on line through every spin: a dropping tip fails the set.",
            "The grip stays firm but relaxed: white knuckles mean the spin will die.",
            "No person or wall is ever within the staff's two-meter circle during practice.",
        ],
        "citations": [CIT_SHAHAR, CIT_WONG, CIT_CHOW],
        "sig_lens": (
            "The Signature read: the staff is the long signature - two "
            "meters of line drawn at eighteen point eight meters per "
            "second, sweeping its circle with the iron rule of control. "
            "Where public teaching files a weapon, the Signature method "
            "files reach with responsibility."
        ),
    },
    {
        "key": "tong_zi_gong",
        "name": "Child Skill Conditioning (Tong Zi Gong)",
        "group": "Conditioning",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Tong zi gong, the Child Skill, is Shaolin's flexibility "
            "conditioning system: the leg stretches, splits, and high-"
            "hold exercises that give northern kung fu its famous high "
            "kicks. Tong zi means child, and the name reflects the "
            "method's demand - the suppleness of a child, built or "
            "rebuilt through patient daily stretching. The core program "
            "runs twelve weeks: the student measures the side-split "
            "width, typically starting around one hundred twenty "
            "centimeters, and adds about five centimeters per week "
            "through held stretches and leg-hold drills, reaching about "
            "one hundred eighty centimeters - a full side split - by "
            "week twelve. The daily session is thirty minutes: ten "
            "minutes of warm joint rotations, fifteen minutes of held "
            "stretches (front splits, side splits, and standing leg "
            "holds), and five minutes of slow kicking through the new "
            "range. Tong zi gong is never forced: the stretch is held "
            "at the edge of discomfort and breathed into, because torn "
            "tissue sets the student back months."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: warm the joints for ten minutes - "
            "ankle circles, knee circles, hip circles, and leg swings, "
            "front to back and side to side, until the hips feel loose. "
            "Step 2: perform the front split stretch, easing down until "
            "a firm stretch is felt and holding for sixty seconds per "
            "side while breathing slowly. Step 3: perform the side "
            "split stretch the same way, measuring the width weekly and "
            "recording it to track the five-centimeter-per-week "
            "progression. Step 4: drill standing leg holds - raise the "
            "leg to the front, side, and back and hold for ten seconds "
            "each, three rounds - to build strength inside the new "
            "range. Step 5: finish with slow kicks through the full new "
            "range of motion, then walk the legs out. The classic errors "
            "are bouncing in the stretch, which triggers the muscles to "
            "tighten against the stretch; stretching cold, which "
            "invites tears; and chasing the weekly measurement by "
            "forcing depth, which trades a number this week for an "
            "injury next month."
        ),
        "key_points": [
            "Shaolin's flexibility system: the stretches and holds behind the art's famous high kicks.",
            "Twelve-week program: side splits from about one hundred twenty centimeters, plus five per week, to about one hundred eighty.",
            "Daily thirty minutes: ten warmup, fifteen held stretches, five slow kicks through the new range.",
            "Strength is built inside the new range with standing leg holds: ten seconds each direction, three rounds.",
            "Never forced: the stretch is held at the edge of discomfort and breathed into; torn tissue costs months.",
        ],
        "requirements": [
            "A ten-minute joint warmup before any stretching: ankles, knees, hips, and leg swings.",
            "Sixty-second held stretches per side for front and side splits, breathed into slowly.",
            "Weekly split-width measurement recorded to verify the five-centimeter progression.",
            "Standing leg holds in three directions to strengthen the new range of motion.",
            "Daily practice: flexibility gained is flexibility kept only through repetition.",
        ],
        "standards": [
            "No bouncing in any stretch: bouncing fails the session.",
            "No stretching cold: the warmup is mandatory, not optional.",
            "Depth is never forced past the week's target: chasing numbers causes the injuries.",
        ],
        "citations": [CIT_WONG, CIT_YIJINJING, CIT_YANG],
        "sig_lens": (
            "The Signature read: the Child Skill files flexibility as a "
            "twelve-week signature - one hundred twenty centimeters "
            "becoming one hundred eighty, five centimeters of new line "
            "per week, never forced. Where public teaching files "
            "stretching, the Signature method files patience measured "
            "in centimeters."
        ),
    },
    {
        "key": "tie_bu_shan",
        "name": "Iron Cloth Body Conditioning (Tie Bu Shan)",
        "group": "Conditioning",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Tie bu shan, the Iron Cloth Shirt, is Shaolin's body "
            "conditioning method: progressive striking of the torso with "
            "padded bags to toughen the muscles and train the body to "
            "absorb impact. The name promises a shirt of iron cloth - "
            "not invulnerability, but a conditioned body that meets "
            "force with structure instead of flinching. Training runs "
            "eight weeks: week one uses twenty light strikes per side "
            "per session across three sessions, and each week adds ten "
            "strikes per side and a firmer bag, so week eight delivers "
            "ninety strikes per side per session - two hundred seventy "
            "per week - with the body conditioned to take them. Every "
            "strike is met with an exhale and a tensing of the torso "
            "muscles at the instant of impact: the conditioning is as "
            "much about the body's response as the skin's toughness. "
            "The method is practiced only under qualified supervision, "
            "never on the head, throat, or joints, and never by striking "
            "beyond what the week's progression allows."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: stand in a horse stance and have a "
            "partner tap the torso - chest, sides, and abdomen - with a "
            "soft canvas bag, twenty taps per side, exhaling and tensing "
            "the muscles at each contact. Step 2: over eight weeks, add "
            "ten strikes per side per week and progress from a soft bag "
            "to a firmer one, reaching ninety strikes per side per "
            "session by week eight. Step 3: on every strike, breathe out "
            "sharply and harden the torso at the exact instant of "
            "impact, then relax between strikes - the exhale-timing is "
            "the core skill. Step 4: train three sessions per week with "
            "rest days between, allowing the body to adapt. Step 5: "
            "advance only when the current week's strikes produce no "
            "lingering soreness the next day. The iron rules are "
            "absolute: never strike the head, throat, spine, or joints; "
            "never train through sharp pain or bruising that does not "
            "fade; never practice without a qualified supervisor; and "
            "never skip weeks of the progression - the body adapts on "
            "its own schedule, not the student's ambition."
        ),
        "key_points": [
            "Progressive torso conditioning: padded-bag strikes that teach the body to absorb impact with structure.",
            "Eight-week ladder: twenty strikes per side in week one, plus ten weekly, to ninety per side by week eight.",
            "Every strike is met with a sharp exhale and torso tensing at the instant of impact: timing is the core skill.",
            "Three sessions per week with rest days: the body adapts between sessions, not during them.",
            "Absolute rules: never the head, throat, spine, or joints; never through sharp pain; never unsupervised; never skipped weeks.",
        ],
        "requirements": [
            "A qualified supervisor present for every conditioning session.",
            "A horse stance base with the torso presented squarely to the strikes.",
            "The eight-week progression honored exactly: twenty per side plus ten weekly, bag firmness graduated.",
            "Exhale-and-tense timing on every single strike, relaxed between strikes.",
            "Three sessions weekly with rest days, advancing only when no soreness lingers.",
        ],
        "standards": [
            "Forbidden targets are never struck: head, throat, spine, and joints are absolute exclusions.",
            "Sharp pain or non-fading bruising stops the session and the progression until cleared.",
            "The week's strikes produce no next-day soreness before the next week's load is taken.",
        ],
        "citations": [CIT_WONG, CIT_YIJINJING, CIT_SHAHAR],
        "sig_lens": (
            "The Signature read: the Iron Cloth Shirt files the torso "
            "as conditioned ground - twenty strikes per side becoming "
            "ninety across eight weeks, each met with an exhale timed "
            "like a seal stamped at the instant of impact. Where public "
            "teaching files toughening, the Signature method files the "
            "body's learned answer to force."
        ),
    },
    {
        "key": "pao_quan",
        "name": "Cannon Fist (Pao Quan)",
        "group": "Advanced Forms",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Pao quan, the Cannon Fist, is Shaolin's explosive long-range "
            "form: pao means cannon, and the form's punches fire like "
            "artillery - long, sudden, and delivered with the whole "
            "body's mass behind a short burst of acceleration. Where the "
            "basic punch teaches the line, the cannon fist teaches the "
            "explosion: the punch travels sixty centimeters in about "
            "fifteen hundredths of a second, and with two thousand "
            "newtons of force behind it the burst delivers about eight "
            "thousand watts of striking power - force times distance "
            "divided by time. The form chains these cannon shots with "
            "advancing footwork, each punch fired from a fresh bow "
            "stance as the body surges forward. Pao quan is taught at "
            "the advanced level because the explosion demands perfect "
            "structure: a mistimed cannon punch with a bent wrist or a "
            "raised shoulder injures the striker, not the target. The "
            "form's rhythm is distinctive - stillness, then detonation, "
            "then stillness again."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: perfect the basic forward punch "
            "first - the cannon fist is an advanced expression of it, "
            "not a replacement. Step 2: from a bow stance, coil the "
            "body slightly by turning the hip a fraction away, loading "
            "the rear leg like a spring. Step 3: detonate - drive the "
            "rear leg, whip the hip through, and fire the fist sixty "
            "centimeters in about fifteen hundredths of a second, "
            "tightening the whole body at the instant of full "
            "extension. Step 4: freeze for a beat at full extension, "
            "the body a single rigid line from rear heel to knuckles, "
            "then snap back to guard. Step 5: drill the single cannon "
            "shot in sets of ten per side against a heavy bag, then "
            "learn the form's advancing chains - step, detonate, step, "
            "detonate - keeping the stillness-detonation-stillness "
            "rhythm. The classic errors are muscling the punch with the "
            "arm instead of detonating from the leg, losing the wrist "
            "line under the explosive load, and rushing the stillness "
            "between shots, which turns cannon fire into mere punching."
        ),
        "key_points": [
            "Shaolin's explosive long-range form: punches fired like cannon - long, sudden, whole-body mass behind them.",
            "Sixty centimeters in about fifteen hundredths of a second at two thousand newtons: about eight thousand watts of striking power.",
            "Each shot fires from a fresh bow stance as the body surges forward: step, detonate, step, detonate.",
            "The rhythm is stillness, detonation, stillness: the pause between shots is part of the technique.",
            "Advanced level only: the explosion demands perfect structure, or it injures the striker.",
        ],
        "requirements": [
            "A perfected basic forward punch before the first cannon shot is attempted.",
            "The coiled loading: hip turned a fraction away, rear leg sprung, before each detonation.",
            "Full-body tightening at the exact instant of full extension: rear heel to knuckles one rigid line.",
            "The freeze-and-snap-back: a beat of stillness at extension, then instant retraction.",
            "Bag work in sets of ten per side before the form's advancing chains are learned.",
        ],
        "standards": [
            "The wrist line holds under explosive load: any bend fails the set immediately.",
            "The stillness between shots is genuine: rushing the rhythm fails the form.",
            "The bag moves violently on each shot: a pushing bag means the detonation was lost.",
        ],
        "citations": [CIT_YANG, CIT_WONG, CIT_SHAHAR],
        "sig_lens": (
            "The Signature read: the Cannon Fist files the punch as "
            "artillery - sixty centimeters in fifteen hundredths of a "
            "second, eight thousand watts, with stillness filed between "
            "every shot like silence between cannonades. Where public "
            "teaching files an advanced form, the Signature method "
            "files detonation with discipline."
        ),
    },
    {
        "key": "luo_han_quan",
        "name": "Arhat Fist (Luo Han Quan)",
        "group": "Advanced Forms",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Luo han quan, the Arhat Fist, is one of the oldest Shaolin "
            "forms: luo han are the arhats, the enlightened disciples of "
            "the tradition, and the form is traditionally structured "
            "around eighteen hands - eighteen core techniques, each "
            "expanded into about four movements, giving seventy-two "
            "movements in the full form. It is a complete fighting "
            "system in one form: the eighteen hands cover striking, "
            "kicking, sweeping, locking, and throwing, each hand a "
            "complete technique with its entry, execution, and finish. "
            "At a training tempo of one and a quarter seconds per "
            "movement the form runs about ninety seconds; at a sharp "
            "eight-tenths tempo it runs about fifty-eight seconds. Luo "
            "han quan is taught at the advanced level because the "
            "eighteen hands demand everything the student has learned - "
            "deep stances for the throws, spring legs for the kicks, "
            "animal hands for the strikes - integrated into single "
            "flowing techniques. To perform the Arhat Fist well is to "
            "demonstrate the complete Shaolin syllabus in one form."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: learn the eighteen hands one at a "
            "time as individual techniques - each hand drilled as a "
            "complete entry, execution, and finish before it joins the "
            "form. Step 2: expand each hand into its four movements, "
            "practicing the transitions inside the hand until they flow. "
            "Step 3: link the hands in order, running the seventy-two "
            "movements at the training tempo of one and a quarter "
            "seconds per movement - about ninety seconds for the form. "
            "Step 4: sharpen toward eight-tenths of a second per "
            "movement, about fifty-eight seconds total, keeping every "
            "stance deep and every technique complete. Step 5: practice "
            "each hand's application with a partner in slow, controlled "
            "drills, so the form's techniques are understood as fighting "
            "methods, not dance. The classic errors are learning the "
            "sequence without learning the hands - a form of empty "
            "movements; rushing the tempo before the techniques are "
            "clean; and performing the locks and throws at speed with a "
            "partner, which is dangerous and forbidden - applications "
            "are drilled slowly or not at all."
        ),
        "key_points": [
            "One of the oldest Shaolin forms: eighteen hands, each expanded to four movements, seventy-two movements total.",
            "A complete fighting system in one form: striking, kicking, sweeping, locking, and throwing across the eighteen hands.",
            "About ninety seconds at training tempo, about fifty-eight seconds at sharp tempo.",
            "Advanced level: the eighteen hands integrate everything learned - stances, kicks, animal hands - into single techniques.",
            "Each hand learned as a complete technique first: entry, execution, and finish before it joins the sequence.",
        ],
        "requirements": [
            "All eighteen hands learned individually as complete techniques before form assembly.",
            "Four-movement expansions flowing inside each hand.",
            "The full seventy-two-movement run at training tempo without stopping.",
            "Partner application drills performed slowly and with control: never at speed.",
            "Tempo sharpening only after the techniques are clean at training tempo.",
        ],
        "standards": [
            "Every hand is demonstrable as a fighting technique, not just a sequence of shapes.",
            "The form's timing hits its marks: ninety seconds training, fifty-eight sharp, within ten seconds.",
            "Partner drills stay slow and controlled: any speed in lock or throw practice fails the session.",
        ],
        "citations": [CIT_SHAHAR, CIT_WONG, CIT_CHOW, CIT_YANG],
        "sig_lens": (
            "The Signature read: the Arhat Fist files eighteen hands as "
            "eighteen complete signatures - seventy-two movements, "
            "ninety seconds, the whole syllabus sealed in one form. "
            "Where public teaching files an old form, the Signature "
            "method files the archive of the art written in motion."
        ),
    },
    {
        "key": "mei_hua_quan",
        "name": "Plum Blossom Fist (Mei Hua Quan)",
        "group": "Advanced Forms",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Mei hua quan, the Plum Blossom Fist, is the Shaolin form "
            "trained on the plum blossom poles: wooden stakes planted in "
            "the quincunx pattern of plum blossom petals - four poles "
            "at the corners of a square and one in the center - on which "
            "the practitioner performs footwork and techniques. The "
            "poles punish every imprecise step: with the five poles set "
            "one meter apart, the diagonal step from a corner pole to "
            "the center covers about one point four one meters, and a "
            "foot placed wrong finds empty air. The form's lesson is "
            "absolute footwork precision under the pressure of elevation "
            "- the poles stand about a meter high, so a fall is a real "
            "fall. Students train the form on the ground for months "
            "before mounting the poles, then begin with simple stepping "
            "patterns between the five poles, and only then perform the "
            "full form above the ground. Mei hua quan produces the "
            "light, exact footwork that marks the advanced Shaolin "
            "practitioner."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: master the form completely on flat "
            "ground - the poles are never the place to learn the "
            "sequence. Step 2: study the pole pattern: five poles, four "
            "at the corners of a one-meter square and one in the "
            "center, each about a meter high. Step 3: practice simple "
            "stepping on the poles first - step from pole to pole, "
            "corner to center, learning the one point four one meter "
            "diagonal by feel, keeping the weight centered over each "
            "pole. Step 4: perform the form's footwork sections on the "
            "poles at half speed, with a partner spotting, before "
            "attempting any hand techniques above the ground. Step 5: "
            "perform the complete form on the poles, then return to "
            "ground practice to keep the techniques sharp - the poles "
            "train the feet, the ground trains the hands. The classic "
            "errors are mounting the poles before the form is known on "
            "the ground, looking down at the feet instead of ahead, "
            "which destroys balance, and rushing the stepping, which "
            "invites the fall the poles are waiting to give."
        ),
        "key_points": [
            "The pole form: five stakes in the plum-blossom quincunx - four corners of a one-meter square plus the center.",
            "The diagonal corner-to-center step covers about one point four one meters: every step must be exact.",
            "The form is mastered on the ground for months before a single pole is mounted.",
            "Pole training begins with simple stepping, then footwork sections at half speed with a spotter.",
            "The lesson is absolute footwork precision under the pressure of elevation: a wrong step finds empty air.",
        ],
        "requirements": [
            "Complete knowledge of the form on flat ground before pole work begins.",
            "The five-pole pattern memorized: corners, center, and the one point four one meter diagonal.",
            "Simple pole-to-pole stepping mastered before any form sections are attempted above ground.",
            "A spotter present for all early pole practice.",
            "Continued ground practice alongside pole work: the poles train feet, the ground trains hands.",
        ],
        "standards": [
            "The gaze stays forward on the poles: looking down at the feet fails the drill.",
            "Every step lands centered on its pole: a sliding or searching foot restarts the pattern.",
            "No rushing: speed on the poles is earned over months, never taken.",
        ],
        "citations": [CIT_WONG, CIT_SHAHAR, CIT_CHOW],
        "sig_lens": (
            "The Signature read: the Plum Blossom Fist files footwork "
            "as a signature written on five poles - each step a "
            "character placed exactly, the one point four one meter "
            "diagonal measured by feel above a meter of air. Where "
            "public teaching files a pole form, the Signature method "
            "files precision with consequences."
        ),
    },
    {
        "key": "tie_sha_zhang",
        "name": "Iron Sand Palm (Tie Sha Zhang)",
        "group": "Conditioning",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Tie sha zhang, the Iron Sand Palm, is Shaolin's progressive "
            "hand conditioning: the practitioner strikes bags of "
            "increasingly hard filling - first beans, then sand, then "
            "iron filings - until the hands are conditioned like iron "
            "wrapped in cotton. The method runs in three phases of one "
            "hundred days each: phase one strikes a bean bag one hundred "
            "times per session, totaling about ten thousand strikes; "
            "phase two strikes a sand bag one hundred times per "
            "session, about ten thousand more; phase three strikes an "
            "iron-filing bag one hundred times per session, about ten "
            "thousand more - roughly thirty thousand conditioned strikes "
            "across three hundred days. Each phase is followed by "
            "medicated hand care from the traditional formulas, and the "
            "hands are never trained through injury. Iron Sand Palm is "
            "the summit of Shaolin hand conditioning and is practiced "
            "only under a qualified teacher: rushed or unsupervised "
            "conditioning cripples the hands it means to strengthen."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: under a qualified teacher's "
            "supervision, begin phase one - strike a canvas bag of "
            "mung beans with the palm heel, one hundred strikes per "
            "session, once daily, for one hundred days. Step 2: apply "
            "the traditional medicated hand wash after every session "
            "and rest the hands completely one day per week. Step 3: "
            "only when one hundred days are complete with no injury, "
            "begin phase two - the same one hundred daily strikes into "
            "a bag of coarse sand for one hundred days. Step 4: "
            "complete phase two cleanly, then begin phase three - one "
            "hundred daily strikes into a bag of iron filings for one "
            "hundred days. Step 5: maintain with two light sessions per "
            "week thereafter; the conditioning is kept, not pushed "
            "further. The iron rules: never train through pain, "
            "swelling, or numbness; never skip the hand care; never "
            "advance phases early; and never practice without the "
            "teacher's supervision - unsupervised iron palm is how "
            "hands are ruined."
        ),
        "key_points": [
            "Three phases of one hundred days: beans, then sand, then iron filings - about thirty thousand strikes total.",
            "One hundred palm-heel strikes per session, once daily, with one full rest day per week.",
            "Medicated hand care after every session: the recovery is part of the method, not an accessory.",
            "Each phase begins only after the previous one hundred days complete with no injury.",
            "The summit of Shaolin hand conditioning: teacher-supervised only, never rushed, never unsupervised.",
        ],
        "requirements": [
            "A qualified teacher supervising the entire three-hundred-day program.",
            "The three bags in order: mung beans, coarse sand, iron filings - never skipped or reordered.",
            "One hundred strikes per session, once daily, one rest day weekly, for one hundred days per phase.",
            "Traditional medicated hand care after every session without exception.",
            "Immediate stop and rest at any pain, swelling, or numbness: the hands are never trained through injury.",
        ],
        "standards": [
            "No phase is advanced early: one hundred clean days is the only doorway to the next bag.",
            "No session is ever performed unsupervised: solo iron palm fails the program.",
            "The hands show no injury at any phase change: damaged hands restart the phase, not continue it.",
        ],
        "citations": [CIT_WONG, CIT_YIJINJING, CIT_SHAHAR],
        "sig_lens": (
            "The Signature read: the Iron Sand Palm files the hands "
            "across three hundred days - ten thousand strikes per bag, "
            "thirty thousand total, each followed by the medicated "
            "care that seals the work. Where public teaching files "
            "conditioning, the Signature method files a three-hundred-"
            "day signature written in iron."
        ),
    },
    {
        "key": "yi_zhi_chan",
        "name": "One-Finger Zen (Yi Zhi Chan)",
        "group": "Conditioning",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Yi zhi chan, One-Finger Zen, is the legendary summit of "
            "Shaolin finger conditioning: the practitioner builds the "
            "strength to support the body on a single fingertip. Training "
            "begins with fingertip pushups on all five fingers, "
            "progresses to fewer fingers over many months, and only at "
            "the advanced stage attempts the single-finger support. The "
            "physics are stark: a seventy-kilogram practitioner placing "
            "thirty percent of the body weight - twenty-one kilograms, "
            "about two hundred six newtons - onto one fingertip with a "
            "contact area of about one and a half square centimeters "
            "loads that fingertip with roughly one point four million "
            "pascals. Nothing in the method is rushed: each stage is "
            "held for months until the fingers, wrist, and shoulder "
            "carry the load without pain, and the practice is always "
            "supervised. Yi zhi chan is as much a meditation as a "
            "conditioning exercise - the stillness required to balance "
            "on one finger is the zen of its name."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: under supervision, begin with "
            "fingertip pushups on all five fingers of each hand, three "
            "sets of ten, on a firm but forgiving surface. Step 2: over "
            "months, reduce the fingers - five to four to three to two "
            "- spending at least two months at each stage with no pain "
            "before reducing further. Step 3: at two fingers, begin "
            "static holds: support the body's weight on two fingertips "
            "for ten seconds, building to sixty. Step 4: only when the "
            "two-finger hold is solid and painless, attempt the single-"
            "finger support with most of the weight still on the feet, "
            "shifting load onto the finger a fraction at a time over "
            "further months. Step 5: practice the stillness itself - "
            "the balanced hold with slow breathing is the exercise, not "
            "just the strength. The iron rules: never train through "
            "finger, wrist, or shoulder pain; never jump stages; never "
            "practice unsupervised; and stop the session the moment "
            "form degrades, because a collapsed finger under load is "
            "injured."
        ),
        "key_points": [
            "The summit of Shaolin finger conditioning: building toward supporting the body on a single fingertip.",
            "Twenty-one kilograms - thirty percent of seventy - on one and a half square centimeters loads about one point four million pascals.",
            "Staged over many months: five fingers to four to three to two, at least two painless months per stage.",
            "Static holds precede loading: ten seconds building to sixty on two fingers before one finger is attempted.",
            "As much meditation as conditioning: the stillness of the balanced hold is the zen of the name.",
        ],
        "requirements": [
            "Qualified supervision for the entire multi-month program.",
            "Fingertip pushups beginning on all five fingers: three sets of ten per hand.",
            "At least two painless months at each finger count before any reduction.",
            "Graduated load shifting onto the single finger: fractions of body weight over months, never all at once.",
            "Immediate stop at any finger, wrist, or shoulder pain, or the moment form degrades.",
        ],
        "standards": [
            "No stage is ever skipped or shortened: two painless months is the minimum at each count.",
            "No unsupervised practice at any stage: solo one-finger training fails the program.",
            "Pain, swelling, or numbness stops the program until fully resolved: the fingers are never trained through injury.",
        ],
        "citations": [CIT_WONG, CIT_YIJINJING, CIT_SHAHAR],
        "sig_lens": (
            "The Signature read: One-Finger Zen files the whole body "
            "balanced on a single point - one point four million "
            "pascals on a fingertip, held in stillness that is itself "
            "the exercise. Where public teaching files a legend, the "
            "Signature method files the staged, supervised road that "
            "makes the legend reachable."
        ),
    },
    {
        "key": "wu_xing_he_yi",
        "name": "Five Animals Combined (Wu Xing He Yi)",
        "group": "Animal Styles",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Wu xing he yi, the Five Animals Combined as One, is the "
            "summit form of Shaolin animal styles: dragon, tiger, crane, "
            "leopard, and snake woven into a single flowing form where "
            "each animal's techniques answer the last. The form's "
            "mathematics show its depth: with five animals and ordered "
            "transitions between every pair, the form contains twenty "
            "distinct animal-to-animal transitions, and the number of "
            "possible three-animal chains drawn from the five is sixty - "
            "the form selects its chains from this space to teach the "
            "practitioner to think in animals, not in techniques. A "
            "tiger's committed rake becomes a snake's darting withdrawal; "
            "a crane's balanced peck becomes a leopard's angled chain; "
            "a dragon's coiling waist carries every change. The form is "
            "taught only after each animal has been learned separately, "
            "and it is the final examination of the animal curriculum: "
            "the student must shift spirit as well as shape, becoming "
            "each animal fully for the length of its techniques before "
            "the next takes over."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: master each of the five animals "
            "separately - dragon, tiger, crane, leopard, snake - with "
            "their hands, stances, and stepping proven in the earlier "
            "records of this database. Step 2: learn the twenty "
            "transitions in pairs: practice shifting from each animal "
            "to each other animal until every ordered pair flows - "
            "tiger to snake, snake to crane, crane to leopard, and all "
            "the rest. Step 3: learn the form's chosen chains, the "
            "sequences of animals the form strings together, drilling "
            "each chain until the spirit shifts with the shape. Step 4: "
            "perform the complete form, changing animals cleanly at "
            "each transition with no blending or hesitation - each "
            "animal must be fully itself while it lasts. Step 5: "
            "practice the form's improvisation drills: called at "
            "random, shift to the named animal instantly, proving the "
            "transitions live outside the memorized sequence. The "
            "classic errors are blending the animals into a generic "
            "middle style, hesitating at the transitions while the mind "
            "catches up, and performing the shapes without the "
            "spirits - the form without the animals is just movement."
        ),
        "key_points": [
            "The summit of the animal curriculum: dragon, tiger, crane, leopard, and snake woven into one flowing form.",
            "Five animals give twenty ordered animal-to-animal transitions; sixty possible three-animal chains form the drill space.",
            "Each animal's techniques answer the last: tiger's rake becomes snake's withdrawal, crane's peck becomes leopard's chain.",
            "Taught only after each animal is mastered separately: the form integrates, it does not introduce.",
            "The final examination: the student must shift spirit as well as shape, each animal fully itself while it lasts.",
        ],
        "requirements": [
            "Separate mastery of all five animals - hands, stances, stepping - before the combined form begins.",
            "All twenty ordered transitions drilled in pairs until every animal-to-animal shift flows.",
            "The form's chosen chains learned as sequences, with spirit shifting at each transition.",
            "Random-call improvisation drills: instant shifts to a named animal outside the memorized sequence.",
            "Clean transitions with no blending or hesitation: each animal fully itself for its techniques.",
        ],
        "standards": [
            "No generic middle style: a blended animal fails the transition.",
            "No hesitation at transitions: the shift is instant or it is not yet learned.",
            "The random-call drill is passed: any named animal assumed instantly from any other.",
        ],
        "citations": [CIT_WONG, CIT_SHAHAR, CIT_CHOW, CIT_YANG],
        "sig_lens": (
            "The Signature read: the Five Animals Combined files the "
            "five seals as one document - twenty transitions, sixty "
            "chains, each animal fully itself and then instantly the "
            "next. Where public teaching files a summit form, the "
            "Signature method files the system signing with all five "
            "hands at once."
        ),
    },
]
