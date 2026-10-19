#!/usr/bin/env python3
"""Entries for the Kalaripayattu Combat databases (combat batch 3, 2026-10-17).

Two NEW databases, 34 ladder-ordered records each:

  combat-kalaripayattu            - The Kalaripayattu Combat Database
                                    (public-harvest: real, fact-checked
                                    kalaripayattu knowledge - the Indian
                                    martial art of Kerala: vanakkam
                                    salutation, the eight ashtavadivu animal
                                    postures, chuvadukal footwork, kalugal
                                    leg conditioning, meyyorukkam body
                                    control, meippayattu body forms, swasam
                                    breath control, kolthari wooden weapons
                                    (muchan, otta, kol), angathari metal
                                    weapons (kadhara, kuntham, vaal,
                                    paricha, valum parichayum, gada, madu,
                                    urumi), verumkai empty-hand combat, kaal
                                    adikal kicks, uzhichil oil massage,
                                    marma sthana vital-point knowledge taught
                                    as traditional heritage, kalari chikitsa
                                    bone-setting tradition - each record a
                                    full technique with step-by-step body
                                    mechanics; standard references Zarrilli
                                    When the Body Becomes All Eyes 1998,
                                    Draeger and Smith Asian Fighting Arts
                                    1969, Reid and Croucher The Way of the
                                    Warrior 1983, Green and Svinth Martial
                                    Arts of the World 2010, Frawley Ranade
                                    and Lele Ayurveda and Marma Therapy
                                    2003, and the Indian Kalarippayattu
                                    Federation technical syllabus)
  combat-kalaripayattu-signature  - The Kalaripayattu Combat Signature
                                    Database
                                    (his original Signature combat method:
                                    every technique a covenant of body and
                                    breath, the vadivu the oath of the
                                    animal, the weapon the signature of the
                                    hand, the kalari the archive of the
                                    ancestors written in motion; src
                                    signature, titles suffixed " (Signature
                                    Edition)", never presented as authentic
                                    public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBKP- (public) and JAH-CBKPS- (signature), verified free
in the manifest id_prefix values and zero hits in every shard index file.

Dedupe: all 68 titles (34 public + 34 Signature Edition) run through the
whole-system dedupe gate before authoring - zero refusals, zero collisions.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_kalaripayattu.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

Screening: civilian traditional-art instruction only. Marma sthana is
taught strictly as traditional heritage knowledge - the anatomical study
of the body vital points as handed down in the kalari tradition, centered
on the healing discipline of marma chikitsa and body awareness - never as
instruction in harming anyone. Nothing hate-adjacent, profane, or
inappropriate; no religious talk. Nothing on neutralizing or defeating
military or defense-grade systems - the standing exclusion holds.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature combat method: every "
            "technique a covenant of body and breath, the vadivu the oath of "
            "the animal, the weapon the signature of the hand, and the kalari "
            "the archive of the ancestors written in motion. Clearly labeled "
            "Signature-made, never presented as authentic public record.")

CIT_ZARRILLI = ("Zarrilli P. When the Body Becomes All Eyes: Paradigms, "
                "Discourses and Practices of Power in Kalarippayattu, a South "
                "Indian Martial Art. Oxford: Oxford University Press; 1998.")
CIT_DRAEGER = ("Draeger D, Smith R. Asian Fighting Arts. Tokyo: Kodansha "
               "International; 1969.")
CIT_REID = ("Reid H, Croucher M. The Way of the Warrior: The Paradox of the "
            "Martial Arts. Woodstock: Overlook Press; 1983.")
CIT_GREEN = ("Green T, Svinth J, editors. Martial Arts of the World: An "
             "Encyclopedia of History and Innovation. Santa Barbara: "
             "ABC-CLIO; 2010.")
CIT_FRAWLEY = ("Frawley D, Ranade S, Lele A. Ayurveda and Marma Therapy: "
               "Energy Points in Yogic Healing. Twin Lakes: Lotus Press; 2003.")
CIT_IKF = ("Indian Kalarippayattu Federation. Technical syllabus and "
           "competition rules: meippayattu, kolthari, angathari, verumkai. "
           "Current edition.")

ENTRIES = [
    {
        "key": "vanakkam",
        "name": "Vanakkam (The Kalari Salutation)",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description":
            "Vanakkam is the salutation that opens every kalaripayattu "
            "training session and the first lesson every student learns. The "
            "practitioner faces the poothara, the stepped altar platform that "
            "stands in the southwest corner of the kalari training pit, "
            "brings the palms together at the chest, and bows - honoring the "
            "guru who teaches, the ground that receives the training, and the "
            "lineage of masters handed down through the art. The traditional "
            "kalari itself is a sunken rectangular pit, roughly forty-two "
            "feet long by twenty-one feet wide, aligned east to west, and "
            "entering it with the salutation marks the boundary between "
            "ordinary life and disciplined practice. Every weapon form, every "
            "empty-hand sequence, and every advanced drill in the art begins "
            "and ends with vanakkam, which is why the masters teach that the "
            "salutation is not decoration but the first technique: respect "
            "made physical.",
        "how_it_works":
            "Stand at the entrance of the kalari facing inward toward the "
            "poothara in the southwest corner. Bring the feet together and "
            "press the palms together at the center of the chest, fingers "
            "pointing upward, elbows relaxed at the sides. Touch the joined "
            "hands first to the forehead, then lower them to the chest while "
            "bowing the head and bending slightly forward from the waist. "
            "Some lineages touch the earth of the pit with the right hand "
            "after the bow, honoring the ground itself. Rise back to standing "
            "with the hands still joined, then lower the hands to the sides. "
            "Perform the same salutation at the close of training, facing the "
            "poothara again, so every session is bracketed by respect. Hold "
            "each phase for a slow count of three and keep the breathing "
            "steady and quiet throughout.",
        "key_points": [
            "Category: foundations - the opening and closing of all practice.",
            "Faces the poothara, the stepped altar in the southwest corner of the kalari.",
            "Palms joined at the chest, touch to the forehead, bow from the waist.",
            "Honors the guru, the training ground, and the lineage of masters.",
            "The traditional kalari pit measures about forty-two feet by twenty-one feet, aligned east to west.",
            "Every form and drill begins and ends with vanakkam.",
        ],
        "requirements": [
            "A kalari or training space with a marked southwest corner or poothara.",
            "Bare feet; the art is practiced barefoot on the earth of the pit.",
            "Quiet attention; the salutation is performed without talking.",
        ],
        "standards": [
            "Traditional kalari curriculum - vanakkam as the first lesson.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - opening salutation.",
        ],
        "citations": [CIT_ZARRILLI, CIT_REID, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, vanakkam is the oath sworn before "
            "the archive opens: the joined palms the seal, the bow the "
            "signature, and the poothara the witness. The Signature method "
            "teaches that no technique is thrown until respect is given, "
            "because the ground that catches you must first be honored.",
    },
    {
        "key": "gaja",
        "name": "Gaja Vadivu (Elephant Posture)",
        "group": "Stances",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description":
            "Gaja vadivu, the elephant posture, is the first of the eight "
            "ashtavadivu animal postures and the stance that teaches forward "
            "driving power in kalaripayattu. The practitioner stands in a "
            "deep frontal stance with the weight committed forward, the front "
            "knee bent over the toes, the rear leg extended and rooted, and "
            "the arms held like the trunk and tusks of the elephant - one arm "
            "extended forward, the other guarding. Like the elephant it is "
            "named for, the posture is immovable once set and unstoppable "
            "once it advances: students hold it for long counts to build the "
            "leg strength that every weapon form and every empty-hand "
            "sequence will borrow. The eight vadivus together are the alphabet "
            "of kalaripayattu stances, and gaja is their first letter.",
        "how_it_works":
            "Face forward and step one foot ahead about one and a half "
            "shoulder-widths, keeping the feet about one shoulder-width apart "
            "side to side. Bend the front knee until it tracks directly over "
            "the toes of the front foot, pressing the front foot flat into "
            "the earth. Extend the rear leg straight back and press the rear "
            "heel toward the floor with the rear foot turned slightly outward. "
            "Settle about sixty percent of the weight onto the front leg and "
            "square the hips to the front. Extend the lead arm forward at "
            "shoulder height with the fingers together, the rear hand held "
            "back near the hip in a guard. Keep the back straight, the chest "
            "open, and the gaze fixed forward. Hold for slow counts of ten, "
            "then step through and repeat on the other side.",
        "key_points": [
            "Category: stances - first of the eight ashtavadivu animal postures.",
            "Deep frontal stance: front knee over the toes, rear leg extended and rooted.",
            "Weight about sixty percent forward, hips square to the front.",
            "Lead arm extended like the trunk, rear hand guarding at the hip.",
            "Builds the leg strength all later forms borrow.",
        ],
        "requirements": [
            "Flat earthen or matted training surface with forward stepping room.",
            "Bare feet; warmed-up knees and hips.",
            "A guru or senior to check knee tracking and hip squareness.",
        ],
        "standards": [
            "Ashtavadivu syllabus - gaja vadivu posture standard.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - stances.",
        ],
        "citations": [CIT_ZARRILLI, CIT_DRAEGER, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, gaja vadivu is the oath of the "
            "elephant: the front leg the vow that will not bend backward, "
            "the rear leg the witness rooted in the earth, and the sixty "
            "percent forward the honest measure of commitment. The Signature "
            "method signs every forward technique with this posture first.",
    },
    {
        "key": "simha",
        "name": "Simha Vadivu (Lion Posture)",
        "group": "Stances",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description":
            "Simha vadivu, the lion posture, is the second of the eight "
            "ashtavadivu animal postures and the stance of coiled readiness. "
            "The practitioner crouches low with the knees bent wide, the "
            "weight sunk between the legs, the chest lifted, and the hands "
            "held open and forward like the paws of a lion about to spring. "
            "Where the elephant posture drives forward, the lion posture "
            "gathers: it teaches the body to store power in the bent legs "
            "and release it upward and outward in a single motion. Students "
            "practice rising from the crouch into strikes and settling back "
            "into the crouch without losing balance, building the spring in "
            "the legs that later powers jumps, kicks, and the sudden "
            "advances of verumkai empty-hand work.",
        "how_it_works":
            "Stand with the feet about two shoulder-widths apart, toes turned "
            "slightly outward. Bend both knees deeply and sink the hips until "
            "the thighs approach parallel with the ground, keeping the back "
            "straight and the chest lifted. Press the knees outward so each "
            "knee tracks over its own foot and never collapses inward. Spread "
            "the weight evenly between both legs, fifty percent on each "
            "side. Hold both hands open in front of the chest, fingers "
            "together and slightly cupped like paws, elbows bent and relaxed. "
            "Fix the gaze forward and breathe steadily into the lower "
            "abdomen. Hold for slow counts of ten. To drill the spring, rise "
            "halfway and settle back down ten times without the knees "
            "drifting inward.",
        "key_points": [
            "Category: stances - second of the eight ashtavadivu animal postures.",
            "Low crouch: knees wide and bent, thighs near parallel to the ground.",
            "Weight even at fifty-fifty; back straight; chest lifted.",
            "Hands open and forward like the paws of a lion.",
            "Teaches the legs to store power and release it in one motion.",
        ],
        "requirements": [
            "Flat training surface with side-to-side room.",
            "Bare feet; thoroughly warmed-up knees, hips, and ankles.",
            "Never force depth through knee pain; build the crouch over weeks.",
        ],
        "standards": [
            "Ashtavadivu syllabus - simha vadivu posture standard.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - stances.",
        ],
        "citations": [CIT_ZARRILLI, CIT_GREEN, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, simha vadivu is the oath of the "
            "lion: the crouch the held breath before the spring, the even "
            "weight the balanced scales, and the open paws the promise that "
            "power is gathered, not wasted. The Signature method treats this "
            "posture as the vault where leg power is stored.",
    },
    {
        "key": "ashva",
        "name": "Ashva Vadivu (Horse Posture)",
        "group": "Stances",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description":
            "Ashva vadivu, the horse posture, is the third of the eight "
            "ashtavadivu animal postures and the great side-facing stance of "
            "kalaripayattu. The feet stand parallel about two shoulder-widths "
            "apart with the toes pointing forward, the knees bend and press "
            "outward over the toes, and the weight spreads evenly while the "
            "back stays straight and the hips sink. Named for the stance of a "
            "rider on horseback, it is the posture from which the art throws "
            "its side strikes, wields the long staff across the body, and "
            "absorbs force from either flank. Long holds in ashva vadivu "
            "forge the thigh and hip strength that carries the practitioner "
            "through the weapon forms without tiring.",
        "how_it_works":
            "Stand with the feet together, then step one foot sideways about "
            "two shoulder-widths so the feet are parallel and the toes point "
            "straight forward. Bend both knees and press them outward so each "
            "knee tracks over its own foot, sinking the hips until the thighs "
            "reach a deep, powerful bend while the back stays straight and "
            "upright. Keep the feet flat with the toes gripping the floor and "
            "do not let the knees fall inward. Distribute the weight evenly, "
            "fifty percent on each leg, pull the lower abdomen in, and set "
            "the hands in guard at the chest. Hold for slow counts of ten to "
            "twenty, breathing steadily, while a partner checks that the "
            "knees stay outside the feet and the back does not lean.",
        "key_points": [
            "Category: stances - third of the eight ashtavadivu animal postures.",
            "Feet parallel, about two shoulder-widths apart, toes forward.",
            "Knees bent and pressed outward, tracking over the toes.",
            "Weight even at fifty-fifty; back straight; hips sunk.",
            "The side-facing root of staff work and flank defense.",
        ],
        "requirements": [
            "Flat training surface with side-to-side room.",
            "Bare feet; warmed-up knees and hips.",
            "A mirror or partner to check knee tracking and back posture.",
        ],
        "standards": [
            "Ashtavadivu syllabus - ashva vadivu posture standard.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - stances.",
        ],
        "citations": [CIT_ZARRILLI, CIT_DRAEGER, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, ashva vadivu is the oath of the "
            "horse: two legs the pillars of a gate, the even weight the "
            "balanced scales, and the outward knees the walls no wind moves. "
            "The Signature method treats this stance as the anvil on which "
            "side-facing power is forged.",
    },
    {
        "key": "varaha",
        "name": "Varaha Vadivu (Boar Posture)",
        "group": "Stances",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description":
            "Varaha vadivu, the boar posture, is the fourth of the eight "
            "ashtavadivu animal postures and the stance of the low, rooting "
            "charge. The practitioner drops into a deep, forward-leaning "
            "crouch with the head lowered and the shoulders rounded, the "
            "weight driven low and forward, and the hands held low and ready "
            "like the tusks of the boar. The boar does not retreat and does "
            "not rise to meet force - it goes under it, rooting forward from "
            "below - and the posture teaches exactly that lesson: how to "
            "enter low, stay rooted while advancing, and drive upward from "
            "the legs. It is the posture of the takedown entries and the low "
            "evasions of the empty-hand work.",
        "how_it_works":
            "From a standing position, step one foot forward about one and a "
            "half shoulder-widths and sink into a deep crouch, bending both "
            "knees until the rear knee nearly brushes the ground behind you. "
            "Lean the torso forward about thirty degrees with the head tucked "
            "slightly and the shoulders rounded, keeping the back flat rather "
            "than hunched. Settle about seventy percent of the weight onto "
            "the front leg, the front foot flat and the knee tracking over "
            "the toes. Hold both hands low in front of the body, elbows bent, "
            "palms open and angled upward like tusks. Advance by driving off "
            "the rear leg in short rooting steps, staying low throughout. "
            "Drill ten advances and ten retreats without rising.",
        "key_points": [
            "Category: stances - fourth of the eight ashtavadivu animal postures.",
            "Deep forward-leaning crouch: torso about thirty degrees forward.",
            "Weight about seventy percent on the front leg, driven low.",
            "Hands held low and ready like the tusks of the boar.",
            "Teaches low entries, rooting advances, and evasion from below.",
        ],
        "requirements": [
            "Flat training surface with forward stepping room.",
            "Bare feet; warmed-up knees, hips, and lower back.",
            "A partner to check that the back stays flat, never hunched.",
        ],
        "standards": [
            "Ashtavadivu syllabus - varaha vadivu posture standard.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - stances.",
        ],
        "citations": [CIT_ZARRILLI, CIT_GREEN, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, varaha vadivu is the oath of the "
            "boar: the low crouch the vow to go under what cannot be moved, "
            "the seventy percent forward the rooting promise, and the "
            "tusk-hands the pledge that the low road is also the strong "
            "road. The Signature method signs every low entry with this "
            "posture.",
    },
    {
        "key": "sarpam",
        "name": "Sarpam Vadivu (Serpent Posture)",
        "group": "Stances",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description":
            "Sarpam vadivu, the serpent posture, is the fifth of the eight "
            "ashtavadivu animal postures and the art ground-level stance. The "
            "practitioner lowers the body until the torso rides close to the "
            "earth, the legs folded and coiled beneath, the weight fluid "
            "rather than fixed, and the hands held ready to strike from the "
            "coil. The serpent does not stand against force; it yields, "
            "slides, and rises where it is not expected - and the posture "
            "teaches the body that same lesson: suppleness under pressure, "
            "movement without telegraphing, and the sudden rise from the "
            "ground into technique. It is the root of the art ground escapes, "
            "low sweeps, and the flowing floor work of the advanced forms.",
        "how_it_works":
            "From a deep crouch, lower one knee to the ground and fold the "
            "legs so the body rides low, the torso upright but close to the "
            "earth, about one forearm height above the floor. Coil the rear "
            "leg beneath the body with the foot tucked, the front foot flat "
            "and ready to drive. Keep the weight fluid - roughly half on the "
            "folded legs, half ready to shift - never locked onto one point. "
            "Hold the hands at chest height, elbows in, fingers together, "
            "ready to extend like the strike of the serpent. Practice the "
            "serpent rise: drive off the front foot and uncoil upward into a "
            "standing guard in one smooth motion, then sink back down. Drill "
            "ten rises and ten sinks, keeping the motion silent.",
        "key_points": [
            "Category: stances - fifth of the eight ashtavadivu animal postures.",
            "Ground-level posture: torso about one forearm height above the floor.",
            "Legs folded and coiled beneath the body; weight fluid, never locked.",
            "Teaches suppleness under pressure and the sudden rise from the ground.",
            "Root of ground escapes, low sweeps, and floor work.",
        ],
        "requirements": [
            "Soft earthen or matted surface; the knees contact the ground.",
            "Bare feet and bare knees; warmed-up hips, knees, and spine.",
            "Practice the rise slowly first; speed comes after silence.",
        ],
        "standards": [
            "Ashtavadivu syllabus - sarpam vadivu posture standard.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - stances.",
        ],
        "citations": [CIT_ZARRILLI, CIT_REID, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, sarpam vadivu is the oath of the "
            "serpent: the coil the vow that stillness is not surrender, the "
            "fluid weight the promise to move where force is not, and the "
            "silent rise the signature of patience. The Signature method "
            "treats this posture as the lesson that the ground is an ally, "
            "not a defeat.",
    },
    {
        "key": "marjjara",
        "name": "Marjjara Vadivu (Cat Posture)",
        "group": "Stances",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description":
            "Marjjara vadivu, the cat posture, is the sixth of the eight "
            "ashtavadivu animal postures and the stance of lightness. The "
            "practitioner stands on the balls of the feet with the heels "
            "raised, the knees soft and springy, the body upright but ready, "
            "and the hands held light and quick - the whole body balanced "
            "like a cat that lands without sound. The cat never commits its "
            "weight until it must, and the posture teaches exactly that: how "
            "to stay mobile, how to shift in any direction without "
            "telegraphing, and how to land from jumps and kicks without "
            "noise or shock. Every silent advance and every soft landing in "
            "the art is built on the cat posture.",
        "how_it_works":
            "Stand with the feet about one shoulder-width apart and rise onto "
            "the balls of both feet, heels lifted about two finger-widths "
            "off the ground. Soften the knees into a light spring, keeping "
            "them directly over the toes, and settle the weight evenly across "
            "the balls of the feet with the body upright. Hold the hands in "
            "a light guard at chest height, elbows relaxed and slightly bent, "
            "fingers together. Practice the cat step: shift the weight fully "
            "onto one foot, lift the other foot silently, place it down "
            "without sound, then transfer the weight - forward, back, and to "
            "each side. Drill twenty silent steps in each direction, then "
            "practice small hops landing on the balls of the feet with no "
            "slap of the heels.",
        "key_points": [
            "Category: stances - sixth of the eight ashtavadivu animal postures.",
            "Balanced on the balls of the feet, heels raised about two finger-widths.",
            "Knees soft and springy, weight never committed until needed.",
            "Teaches silent movement, quick direction changes, and soft landings.",
            "Foundation of the art jumps, kicks, and quiet advances.",
        ],
        "requirements": [
            "Flat, quiet training surface where footfalls can be heard.",
            "Bare feet; warmed-up ankles, calves, and knees.",
            "A partner listening with eyes closed to judge the silence of the steps.",
        ],
        "standards": [
            "Ashtavadivu syllabus - marjjara vadivu posture standard.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - stances.",
        ],
        "citations": [CIT_ZARRILLI, CIT_DRAEGER, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, marjjara vadivu is the oath of the "
            "cat: the raised heels the vow to never be caught flat-footed, "
            "the silent step the signature of patience, and the springy knee "
            "the promise that the body is always ready. The Signature method "
            "treats lightness as a discipline, not a gift.",
    },
    {
        "key": "kukkuda",
        "name": "Kukkuda Vadivu (Rooster Posture)",
        "group": "Stances",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description":
            "Kukkuda vadivu, the rooster posture, is the seventh of the eight "
            "ashtavadivu animal postures and the art one-legged stance. The "
            "practitioner stands on a single bent leg with the other knee "
            "raised high and chambered, the torso upright, and the arms held "
            "like the wings and beak of the rooster - one hand guarding high, "
            "the other low. The rooster strikes with its spurs from a "
            "single-legged base, and the posture teaches the body that same "
            "skill: perfect balance on one leg while the other leg is free to "
            "kick, knee, or step in any direction. All of the art high kicks "
            "and jumping techniques are chambered from the rooster posture, "
            "which is why students hold it for long counts on each leg.",
        "how_it_works":
            "Stand on the left leg with the knee softly bent and the foot "
            "flat, toes gripping the floor. Raise the right knee to hip "
            "height, thigh parallel to the ground, the lower leg hanging "
            "relaxed and ready to extend. Keep the torso upright, the lower "
            "abdomen pulled in, and the gaze fixed on a single point ahead - "
            "the eyes steady the balance. Hold the left hand high in guard "
            "near the temple and the right hand low across the abdomen. "
            "Breathe slowly and hold the posture for slow counts of ten, "
            "then lower the leg without touching down and repeat. When the "
            "hold is steady, practice the rooster kick: extend the raised "
            "leg into a front kick and rechamber without losing balance. "
            "Drill ten holds and ten kick-chambers on each leg.",
        "key_points": [
            "Category: stances - seventh of the eight ashtavadivu animal postures.",
            "Single-legged base: standing knee softly bent, other knee chambered at hip height.",
            "Torso upright; gaze fixed on one point to steady the balance.",
            "The chamber from which all high kicks and jumps are thrown.",
            "Builds the one-legged balance the kicking art demands.",
        ],
        "requirements": [
            "Flat training surface with room to extend the leg.",
            "Bare feet; warmed-up hips, knees, and ankles.",
            "A fixed visual point ahead to anchor the balance.",
        ],
        "standards": [
            "Ashtavadivu syllabus - kukkuda vadivu posture standard.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - stances.",
        ],
        "citations": [CIT_ZARRILLI, CIT_GREEN, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, kukkuda vadivu is the oath of the "
            "rooster: the single standing leg the vow that one root is "
            "enough, the chambered knee the held word waiting to be spoken, "
            "and the fixed gaze the signature of undivided attention. The "
            "Signature method teaches that balance is attention made "
            "physical.",
    },
    {
        "key": "matsya",
        "name": "Matsya Vadivu (Fish Posture)",
        "group": "Stances",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description":
            "Matsya vadivu, the fish posture, is the eighth and last of the "
            "ashtavadivu animal postures and the stance of pure flow. The "
            "practitioner moves through a low, gliding posture with the body "
            "level and the weight shifting smoothly from leg to leg, the arms "
            "sweeping in continuous arcs like fins - never stopping, never "
            "locking, always moving. The fish does not fight the water; it "
            "becomes it, and the posture teaches the body that same lesson: "
            "how to flow around force instead of meeting it, how to change "
            "levels without breaking rhythm, and how to link techniques into "
            "unbroken sequences. With the fish posture the alphabet of the "
            "eight vadivus is complete, and the student can spell any "
            "movement the art requires.",
        "how_it_works":
            "Begin in a medium crouch with the feet about one and a half "
            "shoulder-widths apart and the knees bent. Keeping the torso "
            "level at the same height throughout, glide the weight smoothly "
            "onto the front leg while the arms sweep forward in a rounded "
            "arc, then glide the weight back onto the rear leg while the "
            "arms circle back - a continuous figure-eight of weight and "
            "arms, never pausing at either end. Let the knees bend and "
            "straighten softly with each shift so the head stays level like "
            "a fish gliding through water. Practice the flow for two full "
            "minutes without stopping, then add level changes: sink lower on "
            "one sweep, rise slightly on the next, keeping the motion "
            "unbroken. The drill is mastered when the shifts become silent "
            "and continuous.",
        "key_points": [
            "Category: stances - eighth of the eight ashtavadivu animal postures.",
            "Low gliding posture: torso level, weight flowing leg to leg.",
            "Arms sweep in continuous arcs like fins; motion never locks.",
            "Teaches flowing around force and linking techniques into sequences.",
            "Completes the eight-vadivu alphabet of kalaripayattu stances.",
        ],
        "requirements": [
            "Flat training surface with room for continuous shifting.",
            "Bare feet; warmed-up knees, hips, and shoulders.",
            "Two unbroken minutes of flow per drill round.",
        ],
        "standards": [
            "Ashtavadivu syllabus - matsya vadivu posture standard.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - stances.",
        ],
        "citations": [CIT_ZARRILLI, CIT_REID, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, matsya vadivu is the oath of the "
            "fish: the unbroken glide the vow to never meet force head-on, "
            "the level head the promise of calm inside motion, and the "
            "fin-arms the signature of adaptation. The Signature method "
            "treats flow as the highest form of strength.",
    },
    {
        "key": "chuvadukal",
        "name": "Chuvadukal (Kalari Footwork Patterns)",
        "group": "Footwork and Conditioning",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description":
            "Chuvadukal are the footwork patterns of kalaripayattu - the "
            "rehearsed stepping sequences that teach the feet where to go "
            "before the hands and weapons ever move. Each chuvadu is a short "
            "pattern of steps: advances, retreats, side steps, turns, and "
            "level changes, drilled in the vadivu postures until the feet "
            "find their places without thought. The art holds that a fighter "
            "is only as good as the feet, because every strike, every block, "
            "and every weapon cut is delivered from a step - and a wrong step "
            "spoils the finest technique. Students drill the chuvadukal daily "
            "for years, and the masters can read a student level by watching "
            "the feet alone.",
        "how_it_works":
            "Begin in gaja vadivu, the elephant posture. Step the rear foot "
            "forward past the front foot into a new gaja vadivu facing the "
            "same direction - this is the basic advance, one chuvadu. Step "
            "back to the start - the basic retreat. Drill the advance and "
            "retreat ten times each, keeping the stance deep and the weight "
            "committed on every step. Next, from ashva vadivu, step sideways "
            "and settle back into ashva vadivu - the side step - ten times "
            "to each side. Then practice the turn: from gaja vadivu, pivot "
            "on the front foot and swing the rear leg around to face the "
            "opposite direction, settling into gaja vadivu again - ten turns "
            "each way. Link them: advance, advance, turn, retreat, side step "
            "- one flowing sequence. Drill the linked sequence for five "
            "minutes without stopping.",
        "key_points": [
            "Category: footwork - the rehearsed stepping patterns of the art.",
            "Basic patterns: advance, retreat, side step, turn, level change.",
            "Every pattern is drilled inside the vadivu postures.",
            "Every strike and weapon cut is delivered from a step.",
            "Masters read a student level by watching the feet alone.",
        ],
        "requirements": [
            "Flat training surface with room to advance, retreat, and turn.",
            "Bare feet; the eight vadivus learned first.",
            "Five unbroken minutes per linked-sequence drill.",
        ],
        "standards": [
            "Traditional kalari curriculum - chuvadukal stepping syllabus.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - footwork.",
        ],
        "citations": [CIT_ZARRILLI, CIT_DRAEGER, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, the chuvadukal are the oath of the "
            "feet: each step a word, each pattern a sentence, and the linked "
            "sequence the paragraph the body writes on the earth. The "
            "Signature method teaches that the feet speak first and the "
            "hands only echo them.",
    },
    {
        "key": "kalugal",
        "name": "Kalugal (Leg Conditioning Exercises)",
        "group": "Footwork and Conditioning",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description":
            "Kalugal are the leg conditioning exercises of kalaripayattu - "
            "the swings, stretches, and splits that build the extraordinary "
            "leg flexibility and strength the art is known for. Kal means leg "
            "in Malayalam, and the kalugal take the legs through their full "
            "range: forward swings, side swings, circular swings, deep lunges, "
            "and the progressive splits, each held and repeated until the "
            "legs move freely in every direction. The art high kicks, its "
            "jumping techniques, and its deep vadivu holds are all impossible "
            "without the kalugal, which is why students perform them at the "
            "start of every session after the warm-up. Flexible, powerful "
            "legs are the engine of kalaripayattu, and the kalugal build that "
            "engine.",
        "how_it_works":
            "Stand beside a wall or post for light balance support. Swing the "
            "right leg forward and up as high as comfortable, keeping the "
            "knee straight and the toes pointed, then let it swing back down "
            "without forcing - ten forward swings, then ten on the left leg. "
            "Turn to face the support and swing each leg sideways across the "
            "body and out - ten side swings each leg. Then swing each leg in "
            "a full circle from the hip, five circles each direction per leg. "
            "Finish with the deep lunge: step far forward, sink until the "
            "rear knee nearly touches the ground, and hold for a slow count "
            "of ten - five lunges each side. For the splits, ease into front "
            "and side splits only as far as the body allows, holding each "
            "for thirty slow breaths, never bouncing. Total kalugal time: "
            "about fifteen minutes.",
        "key_points": [
            "Category: conditioning - leg swings, stretches, and splits.",
            "Forward, side, and circular swings build full range of motion.",
            "Deep lunges build the strength behind the flexibility.",
            "Progressive splits, held for thirty breaths, never bounced.",
            "Performed at the start of every session after warm-up.",
        ],
        "requirements": [
            "Flat training surface; a wall or post for light balance support.",
            "Bare feet or flexible training shoes; loose clothing.",
            "A full warm-up first; never stretch cold muscles.",
            "Stop at sharp pain; flexibility is built over months, not forced in a day.",
        ],
        "standards": [
            "Traditional kalari curriculum - kalugal conditioning syllabus.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - conditioning.",
        ],
        "citations": [CIT_ZARRILLI, CIT_REID, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, the kalugal are the oath of the "
            "legs: each swing a vow of range, each held split a promise of "
            "patience, and the fifteen minutes the daily signature renewed. "
            "The Signature method treats flexibility as strength that has "
            "learned manners.",
    },
    {
        "key": "meyyorukkam",
        "name": "Meyyorukkam (Body Control Exercises)",
        "group": "Footwork and Conditioning",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description":
            "Meyyorukkam is the body-control conditioning of kalaripayattu - "
            "mey meaning body and orukkam meaning preparation or control. It "
            "is the system of push-ups, sit-ups, back bends, twists, animal "
            "walks, and floor exercises that forges the whole body into a "
            "single responsive instrument. Where the kalugal build the legs, "
            "the meyyorukkam builds everything else: the arms that wield the "
            "weapons, the waist that turns the strikes, the back that holds "
            "the postures, and the coordination that links them all. The "
            "exercises are performed in flowing circuits, often in the "
            "vadivu postures themselves, so strength and stance grow together "
            "and the body learns control in the exact shapes the art will "
            "demand.",
        "how_it_works":
            "Begin with ten slow push-ups, the body straight from head to "
            "heels, lowering until the chest nearly touches the floor. Follow "
            "with ten sit-ups, hands crossed at the chest, rising with the "
            "abdomen and not the neck. Then the back bend: lie face down, "
            "place the hands beside the chest, and press the torso up into a "
            "cobra arch - hold for five slow breaths, repeat five times. Next "
            "the waist twists: stand in ashva vadivu and rotate the torso "
            "fully left and right, ten twists each side, keeping the hips "
            "steady. Then the animal walks: cross the floor in the simha "
            "crouch for ten steps, then in the sarpam low glide for ten "
            "steps. Finish with ten jumping squats. Rest one minute and "
            "repeat the whole circuit twice more - three circuits total, "
            "about twenty minutes.",
        "key_points": [
            "Category: conditioning - whole-body control circuits.",
            "Push-ups, sit-ups, back bends, waist twists, animal walks, jumping squats.",
            "Performed in flowing circuits, often inside the vadivu postures.",
            "Builds the arms, waist, back, and coordination together.",
            "Three circuits of about twenty minutes per session.",
        ],
        "requirements": [
            "Flat training surface with room for floor work and animal walks.",
            "Bare feet; loose training clothing.",
            "A full warm-up first; one minute of rest between circuits.",
            "Build from one circuit to three over the first months.",
        ],
        "standards": [
            "Traditional kalari curriculum - meyyorukkam conditioning syllabus.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - conditioning.",
        ],
        "citations": [CIT_ZARRILLI, CIT_DRAEGER, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, meyyorukkam is the oath of the whole "
            "body: the push-up the vow of the arms, the back bend the promise "
            "of the spine, the animal walks the signature of the vadivus in "
            "motion. The Signature method forges the body as one instrument, "
            "never as separate parts.",
    },
    {
        "key": "meippayattu",
        "name": "Meippayattu (Body Training Forms)",
        "group": "Footwork and Conditioning",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description":
            "Meippayattu is the body-training form of kalaripayattu - mei "
            "meaning body and payattu meaning practice or exercise - the "
            "linked sequences of stances, steps, turns, jumps, and kicks "
            "performed without weapons. It is the first full form the student "
            "learns and the daily practice that never ends: the vadivus, the "
            "chuvadukal, the kicks, and the body-control exercises woven into "
            "flowing routines that train balance, timing, breath, and "
            "endurance all at once. The traditional curriculum holds "
            "eighteen meippayattu sequences of increasing difficulty, and the "
            "student must perform them with precision before ever touching a "
            "weapon. Meippayattu is where the body learns the grammar of the "
            "art; the weapons later only give it new words.",
        "how_it_works":
            "Begin in vanakkam, then step into gaja vadivu. Perform the first "
            "sequence: advance two steps in gaja vadivu, turn into ashva "
            "vadivu, side-step twice, drop into simha vadivu, rise with a "
            "front kick from kukkuda vadivu, land in marjjara vadivu, and "
            "glide through matsya vadivu back to the start - one flowing "
            "round. Keep the breath coordinated: exhale on each kick and "
            "turn, inhale on each settle into stance. Perform the round five "
            "times without stopping, then rest one minute. As training "
            "progresses, the guru adds sequences: jumps from the cat posture, "
            "spinning kicks, floor rolls from the serpent posture - up to the "
            "full eighteen sequences. A complete meippayattu session runs "
            "about thirty minutes.",
        "key_points": [
            "Category: forms - the linked body-training sequences.",
            "Woven from vadivus, chuvadukal, kicks, jumps, and turns - no weapons.",
            "Eighteen traditional sequences of increasing difficulty.",
            "Must be mastered before the student touches any weapon.",
            "Trains balance, timing, breath, and endurance together.",
        ],
        "requirements": [
            "A kalari or open training space with room for jumps and turns.",
            "Bare feet; the eight vadivus and chuvadukal learned first.",
            "Thirty minutes per full session; water nearby.",
        ],
        "standards": [
            "Traditional kalari curriculum - eighteen meippayattu sequences.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - meippayattu.",
        ],
        "citations": [CIT_ZARRILLI, CIT_GREEN, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, meippayattu is the oath of the "
            "grammar: the stances the letters, the sequences the sentences, "
            "and the eighteen forms the book the body writes before it is "
            "given a pen. The Signature method teaches that the weapon never "
            "teaches the body - the body teaches the weapon.",
    },
    {
        "key": "swasam",
        "name": "Swasam (Breath Control in the Kalari)",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description":
            "Swasam is breath control in kalaripayattu - swasam meaning "
            "breath - the discipline of coordinating every movement with the "
            "inhale and exhale until breath and body move as one. The art "
            "teaches that power without breath is noise: the strike lands "
            "with the exhale, the stance settles with the inhale, and the "
            "advanced practitioner can regulate the breath through the "
            "longest forms without gasping. Students practice seated "
            "breathing first, then breathing inside each vadivu hold, then "
            "breathing through the full meippayattu sequences - a ladder "
            "within the ladder. Proper swasam gives the practitioner "
            "endurance, calm under pressure, and the internal rhythm that "
            "the masters say separates the trained body from the merely "
            "strong one.",
        "how_it_works":
            "Sit cross-legged with the back straight and the hands resting on "
            "the knees. Inhale slowly through the nose for a count of four, "
            "filling the lower abdomen first and then the chest. Hold the "
            "breath for a count of four. Exhale slowly through the nose for "
            "a count of six, emptying the chest first and then the abdomen. "
            "Rest for a count of two and repeat - ten full cycles, about "
            "three minutes. Next, take the breathing into the stances: hold "
            "gaja vadivu and breathe the same four-four-six-two pattern for "
            "ten cycles, then ashva vadivu for ten cycles. Finally, walk the "
            "meippayattu sequence breathing out on every kick, turn, and "
            "strike, and breathing in on every settle into stance. Never "
            "hold the breath under strain; if dizziness comes, sit and "
            "breathe normally.",
        "key_points": [
            "Category: foundations - breath coordinated with all movement.",
            "Basic pattern: inhale four counts, hold four, exhale six, rest two.",
            "Exhale on kicks, turns, and strikes; inhale settling into stance.",
            "Practiced seated first, then in stance holds, then in full forms.",
            "Gives endurance, calm, and the internal rhythm of the art.",
        ],
        "requirements": [
            "A quiet space; seated or standing practice needs little room.",
            "Ten slow cycles per round; about three minutes seated.",
            "Never hold the breath under strain; sit if dizziness comes.",
        ],
        "standards": [
            "Traditional kalari curriculum - swasam breath discipline.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - breathing.",
        ],
        "citations": [CIT_ZARRILLI, CIT_FRAWLEY, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, swasam is the oath of the breath: "
            "the inhale the promise gathered, the hold the word weighed, and "
            "the exhale the signature released with the strike. The Signature "
            "method teaches that the breath is the first weapon and the last "
            "teacher.",
    },
    {
        "key": "muchan",
        "name": "Muchan (Short Stick)",
        "group": "Weapons - Wood",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description":
            "The muchan is the short wooden stick of kalaripayattu - about a "
            "cubit long, roughly eighteen to twenty-four inches of dense "
            "hardwood - and the first weapon placed in the student hands. "
            "After the long discipline of meippayattu, the muchan teaches "
            "the hand what the body already knows: how to extend a line from "
            "the shoulder through the arm into the weapon, how to strike "
            "with the hip behind it, and how to guard with the stick as an "
            "extension of the forearm. The short stick is fast, forgiving, "
            "and honest - every error of body mechanics shows instantly in "
            "the stick path. Students drill strikes, blocks, and disarms "
            "with the muchan, often in pairs, before the guru permits the "
            "longer and more demanding wooden weapons.",
        "how_it_works":
            "Grip the muchan near one end with a firm but relaxed fist, the "
            "thumb along the stick and not wrapped over the fingers. Stand "
            "in gaja vadivu with the stick held at the hip. Strike one: "
            "step forward and swing the stick in a downward diagonal arc "
            "across the body, turning the hip into the cut and exhaling "
            "sharply - the stick should whistle, not wobble. Rechamber to "
            "the hip. Strike two: the upward diagonal from low to high. "
            "Strike three: the horizontal cut at shoulder height, pivoting on "
            "the feet. Drill ten of each cut, then the guard: hold the "
            "muchan across the body like a forearm block and have a partner "
            "tap it lightly with a second stick - ten guards each side. "
            "Finish with the disarm drill: partner grips your stick; twist "
            "the wrist and pull along the stick axis to free it - ten each "
            "hand. Total drill time about twenty minutes.",
        "key_points": [
            "Category: weapons - the first weapon, about eighteen to twenty-four inches of hardwood.",
            "Teaches the hand to extend the body line into the weapon.",
            "Three basic cuts: downward diagonal, upward diagonal, horizontal.",
            "Guard held across the body like an extended forearm.",
            "Paired drills teach timing before the longer wooden weapons.",
        ],
        "requirements": [
            "Two hardwood muchan sticks; a training partner for paired drills.",
            "Meippayattu body forms learned first - the weapon follows the body.",
            "Protective eyewear for paired stick drills; controlled contact only.",
            "Twenty minutes per drill session.",
        ],
        "standards": [
            "Traditional kalari curriculum - kolthari stage, first weapon.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - wooden weapons.",
        ],
        "citations": [CIT_ZARRILLI, CIT_DRAEGER, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, the muchan is the oath of the hand: "
            "the short stick the first signature the student is allowed to "
            "write, the whistle of the cut the proof the hip signed it, and "
            "the paired drill the covenant that the weapon is practiced with "
            "a partner, never against one. The Signature method gives the "
            "hand its pen only after the body has learned its letters.",
    },
    {
        "key": "otta",
        "name": "Otta (Curved Stick)",
        "group": "Weapons - Wood",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description":
            "The otta is the curved wooden stick of kalaripayattu - a "
            "short, stout club bent like an elephant tusk, about eighteen "
            "inches long - and the weapon unique to this art. No other "
            "martial tradition wields its exact shape. The otta trains the "
            "body for the sword: its curve teaches the wrist to roll the cut, "
            "its weight teaches the forearm to drive through, and its short "
            "reach forces the practitioner to step deep into range - exactly "
            "the lessons the sword will later demand. The otta forms are "
            "among the most beautiful in the art, the curved stick tracing "
            "arcs around the body as the practitioner advances, turns, and "
            "crouches through the vadivus. Mastery of the otta is the "
            "gateway to the metal weapons.",
        "how_it_works":
            "Grip the otta at its straight end with the curved head forward, "
            "the fist firm and the wrist relaxed. Stand in gaja vadivu. The "
            "first otta cut: step forward and sweep the curved head in a "
            "downward arc across the body, rolling the wrist at the end of "
            "the cut so the curve bites through - exhale on the cut. "
            "Rechamber. The second cut: the rising arc from low to high, "
            "wrist rolling the opposite way. The third: the hooking cut, "
            "where the curve catches and pulls - practice hooking a "
            "partner held stick and drawing it aside. Drill ten of each cut "
            "on each side, stepping deep into every cut - the short reach "
            "demands committed footwork. Then the otta form: link the cuts "
            "with advances, turns, and crouches through the vadivus for "
            "three unbroken minutes.",
        "key_points": [
            "Category: weapons - the curved tusk-shaped stick unique to kalaripayattu.",
            "About eighteen inches of dense wood; trains the body for the sword.",
            "The curve teaches the wrist to roll through the cut.",
            "Short reach forces deep, committed footwork.",
            "Mastery of the otta opens the gate to the metal weapons.",
        ],
        "requirements": [
            "A hardwood otta; meippayattu and muchan training completed first.",
            "Training partner for hooking drills; protective eyewear.",
            "Room to advance, turn, and crouch with the weapon.",
        ],
        "standards": [
            "Traditional kalari curriculum - kolthari stage, otta forms.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - wooden weapons.",
        ],
        "citations": [CIT_ZARRILLI, CIT_GREEN, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, the otta is the oath of the curve: "
            "the tusk-shape the vow that no other art signs this way, the "
            "rolling wrist the signature of adaptation, and the deep step "
            "the promise that short reach is answered with full commitment. "
            "The Signature method treats the otta as the rehearsal before "
            "the sword takes the stage.",
    },
    {
        "key": "kol",
        "name": "Kol (Long Staff)",
        "group": "Weapons - Wood",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description":
            "The kol is the long staff of kalaripayattu - a straight wooden "
            "pole about five feet long, roughly the height of the "
            "practitioner - and the weapon of reach and rhythm. Where the "
            "short sticks teach the hand, the staff teaches the whole body: "
            "both hands work the pole, the waist turns every strike, the "
            "feet dance to keep the range, and the staff spins, thrusts, and "
            "sweeps in continuous motion. The kol forms are the most "
            "athletic of the wooden-weapon stage, full of spins, jumps, and "
            "low sweeps, and they build the coordination that the spear will "
            "later demand. A practitioner who has mastered the staff moves "
            "like the pole is a third limb.",
        "how_it_works":
            "Grip the staff with both hands about shoulder-width apart, the "
            "right hand leading. Stand in ashva vadivu. The basic thrust: "
            "slide the rear hand forward and drive the staff tip straight "
            "ahead, stepping into gaja vadivu as the tip extends - exhale on "
            "the thrust. The basic sweep: swing the staff horizontally at "
            "knee height, pivoting the feet and turning the waist fully. The "
            "overhead strike: raise the staff high and bring it down in a "
            "diagonal arc, stepping deep. Drill ten of each on both sides. "
            "Then the spin: pass the staff hand over hand in front of the "
            "body, keeping it parallel to the ground - ten spins each "
            "direction. Link them into the staff form: thrust, sweep, spin, "
            "overhead strike, turn - three unbroken minutes, the staff never "
            "stopping.",
        "key_points": [
            "Category: weapons - the long staff, about five feet of straight hardwood.",
            "Both hands work the pole; the waist turns every strike.",
            "Basic techniques: thrust, low sweep, overhead strike, spin.",
            "Builds the coordination the spear will later demand.",
            "The most athletic forms of the wooden-weapon stage.",
        ],
        "requirements": [
            "A straight hardwood staff about the practitioner height.",
            "Muchan and otta training completed first.",
            "Open space: the staff needs a full circle of clear room.",
            "A partner at safe distance for thrust-accuracy drills.",
        ],
        "standards": [
            "Traditional kalari curriculum - kolthari stage, staff forms.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - wooden weapons.",
        ],
        "citations": [CIT_ZARRILLI, CIT_DRAEGER, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, the kol is the oath of reach: the "
            "five-foot pole the vow that the body extends beyond the skin, "
            "the turning waist the signature on every strike, and the "
            "unbroken spin the promise of rhythm without pause. The Signature "
            "method treats the staff as the body longest sentence.",
    },
    {
        "key": "kolthari",
        "name": "Kolthari (Wooden-Weapon Forms)",
        "group": "Weapons - Wood",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description":
            "Kolthari is the wooden-weapons stage of kalaripayattu - kol "
            "meaning wood and thari meaning practice - the complete "
            "curriculum of the muchan, the otta, and the kol woven into "
            "formal paired and solo forms. It is the second great stage of "
            "the art, after meippayattu and before the metal weapons of "
            "angathari. In kolthari the student learns not just to swing a "
            "stick but to fight with it: the attack forms, the defense "
            "forms, the disarms, and the paired exercises where two "
            "practitioners trade attacks and counters at speed. The wooden "
            "weapons forgive mistakes that metal would not, which is why "
            "the tradition places this entire stage before any blade is "
            "touched - kolthari is where judgment is trained.",
        "how_it_works":
            "The kolthari session opens with vanakkam and the meippayattu "
            "warm-up. Solo forms first: perform the muchan form - the three "
            "cuts linked with advances, retreats, and turns through the "
            "vadivus - three unbroken minutes. Then the otta form, three "
            "minutes, then the staff form, three minutes. Rest one minute "
            "between forms. Paired exercises next, with a partner and "
            "controlled contact: partner attacks with a slow overhead cut; "
            "step offline into ashva vadivu and guard with the muchan across "
            "the body - ten exchanges, then swap roles. Increase the speed "
            "gradually over weeks, never beyond control. Finish with the "
            "disarm sequence: partner thrusts with the staff; parry offline, "
            "trap the pole, and twist it free - five each side. Total "
            "kolthari session: about forty-five minutes.",
        "key_points": [
            "Category: weapons - the complete wooden-weapons stage.",
            "Woven from muchan, otta, and kol solo and paired forms.",
            "The second great stage: after meippayattu, before metal weapons.",
            "Paired exercises trade attacks and counters at controlled speed.",
            "Wood forgives what metal would not - this stage trains judgment.",
        ],
        "requirements": [
            "Full set of wooden weapons: muchan, otta, and staff.",
            "A trained partner for all paired exercises.",
            "Protective eyewear; controlled contact only, speed built over weeks.",
            "Forty-five minutes per full session.",
        ],
        "standards": [
            "Traditional kalari curriculum - kolthari as the second stage.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - wooden weapons.",
        ],
        "citations": [CIT_ZARRILLI, CIT_GREEN, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, kolthari is the oath of the wood: "
            "the muchan the first word, the otta the curved sentence, the "
            "staff the long paragraph, and the paired exercise the dialogue. "
            "The Signature method treats this stage as the school of "
            "judgment, where the weapon is wood so the lesson can be "
            "learned without the price of steel.",
    },
    {
        "key": "kadhara",
        "name": "Kadhara (Dagger)",
        "group": "Weapons - Metal",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description":
            "The kadhara is the dagger of kalaripayattu - a double-edged "
            "blade about twelve to fifteen inches long with a sturdy hilt - "
            "and the first metal weapon the student is permitted to hold. "
            "After the long apprenticeship of wood, the dagger teaches "
            "respect: its edge is real, its point is real, and every drill "
            "is performed with the control the metal demands. The kadhara "
            "forms teach close-range work - the thrust, the draw cut, the "
            "reverse-grip techniques, and the empty-hand assists where the "
            "free hand traps and controls while the blade works. Because the "
            "dagger is short, it forces the practitioner into the deep "
            "vadivu entries learned in the body forms; the blade never "
            "reaches alone.",
        "how_it_works":
            "Grip the kadhara with the blade extending from the thumb side "
            "of the fist for the standard grip, firm but not white-knuckled. "
            "Stand in gaja vadivu. The straight thrust: step deep and drive "
            "the point straight forward from the hip, the free hand pulling "
            "back to the hip to add the twist - exhale on the thrust. The "
            "draw cut: sweep the edge across in a tight arc, the wrist "
            "rolling. The reverse grip: turn the blade to extend from the "
            "little-finger side for the close hooking techniques. Drill ten "
            "thrusts and ten draw cuts on each side, always stepping deep - "
            "the short blade demands committed entries. Paired drill with a "
            "partner holding a wooden dagger: partner thrusts slowly; step "
            "offline, trap the attacking arm with the free hand, and answer "
            "with a controlled thrust that stops short - ten exchanges each "
            "role. All metal drills at slow speed; speed is earned over "
            "months.",
        "key_points": [
            "Category: weapons - the first metal weapon, a twelve to fifteen inch double-edged dagger.",
            "Teaches close-range work: thrust, draw cut, reverse-grip techniques.",
            "The free hand traps and controls while the blade works.",
            "Short reach demands the deep vadivu entries of the body forms.",
            "All metal drills at slow, controlled speed - speed is earned.",
        ],
        "requirements": [
            "A training kadhara; wooden daggers for all paired drills.",
            "Kolthari wooden-weapons stage completed and approved by the guru.",
            "A trained partner; protective eyewear; first-aid kit present.",
            "Slow speed only until the guru permits otherwise.",
        ],
        "standards": [
            "Traditional kalari curriculum - angathari stage, first metal weapon.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - metal weapons.",
        ],
        "citations": [CIT_ZARRILLI, CIT_DRAEGER, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, the kadhara is the oath of the "
            "edge: the first metal the vow that control precedes power, the "
            "deep entry the promise that the blade never reaches alone, and "
            "the slow drill the signature of patience. The Signature method "
            "gives the student steel only after wood has taught judgment.",
    },
    {
        "key": "kuntham",
        "name": "Kuntham (Spear)",
        "group": "Weapons - Metal",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description":
            "The kuntham is the spear of kalaripayattu - a wooden shaft "
            "about five to six feet long tipped with a metal head - and the "
            "weapon of the longest reach in the art. The spear teaches "
            "distance: how to hold an opponent at the point, how to close "
            "the distance in a single committed step, and how to recover the "
            "long weapon after the thrust without losing balance. The staff "
            "training of kolthari transfers directly - the hands already "
            "know the pole - but the spear head adds consequence, and every "
            "form is performed with the precision the point demands. The "
            "kuntham forms include the thrust, the sweeping cuts with the "
            "shaft, the butt strikes, and the spinning recoveries that bring "
            "the long weapon back to guard.",
        "how_it_works":
            "Grip the spear with both hands, the lead hand about two feet "
            "behind the head. Stand in ashva vadivu. The straight thrust: "
            "slide the rear hand forward and drive the point straight ahead, "
            "stepping deep into gaja vadivu as the point extends - the whole "
            "body behind the tip, exhale on the thrust. Recover by drawing "
            "the spear straight back to guard without lifting the point. The "
            "shaft sweep: swing the shaft horizontally at leg height, "
            "pivoting fully on the feet. The butt strike: reverse the spear "
            "and drive the butt end forward in close range. Drill ten "
            "thrusts, ten sweeps, and ten butt strikes, then link them: "
            "thrust, recover, sweep, spin the spear back to guard - the "
            "spear form, three unbroken minutes. Practice the thrust "
            "accuracy against a marked target at spear length plus one step.",
        "key_points": [
            "Category: weapons - the spear, five to six feet with a metal head.",
            "The longest reach in the art; teaches distance and recovery.",
            "Techniques: straight thrust, shaft sweep, butt strike, spinning recovery.",
            "Staff training transfers directly; the head adds consequence.",
            "The whole body drives behind the point on every thrust.",
        ],
        "requirements": [
            "A kuntham spear; kolthari staff training completed first.",
            "Open space: a full spear circle of clear room.",
            "A marked target for thrust-accuracy drills; a partner at safe distance.",
            "Controlled speed; the point is real.",
        ],
        "standards": [
            "Traditional kalari curriculum - angathari stage, spear forms.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - metal weapons.",
        ],
        "citations": [CIT_ZARRILLI, CIT_GREEN, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, the kuntham is the oath of distance: "
            "the long shaft the vow to hold range with discipline, the "
            "committed step the promise that distance is closed whole, and "
            "the spinning recovery the signature of never being left "
            "extended. The Signature method treats the spear as the lesson "
            "that reach is responsibility.",
    },
    {
        "key": "vaal",
        "name": "Vaal (Sword)",
        "group": "Weapons - Metal",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description":
            "The vaal is the sword of kalaripayattu - a curved or straight "
            "single-edged blade about two and a half feet long - and the "
            "heart of the angathari metal-weapons stage. Every lesson of the "
            "wooden otta was a rehearsal for this moment: the wrist roll, "
            "the deep step, the hip behind the cut. The sword forms teach "
            "the full vocabulary of the blade - the downward cut, the "
            "rising cut, the horizontal cut, the thrust, and the flowing "
            "combinations that link them as the practitioner advances, "
            "turns, and crouches through the vadivus. In the tradition the "
            "sword is treated with reverence: it is saluted before practice, "
            "never pointed carelessly, and handled as the emblem of the "
            "warrior discipline itself.",
        "how_it_works":
            "Grip the sword with the edge aligned with the knuckles, the "
            "fist firm and the wrist supple. Begin with vanakkam to the "
            "weapon, then stand in gaja vadivu. The downward cut: raise the "
            "blade high and bring it down in a diagonal arc, stepping forward "
            "and turning the hip fully into the cut - the wrist rolls at the "
            "end exactly as the otta taught. The rising cut: sweep from low "
            "to high. The horizontal cut: pivot and cut at shoulder height. "
            "The thrust: extend the point straight from the hip with a deep "
            "step. Drill ten of each cut on both sides at slow speed, the "
            "blade always under complete control. Then the sword form: link "
            "the cuts with advances, retreats, turns, and vadivu changes - "
            "three unbroken minutes. End with vanakkam to the weapon. Never "
            "practice the sword form at speed until the guru permits it.",
        "key_points": [
            "Category: weapons - the sword, about two and a half feet of single-edged blade.",
            "The heart of the angathari metal-weapons stage.",
            "Four core cuts: downward, rising, horizontal, and the thrust.",
            "Every otta lesson - wrist roll, deep step, hip drive - transfers here.",
            "Saluted before practice; handled with reverence, never carelessly.",
        ],
        "requirements": [
            "A training vaal; otta and kolthari stages completed first.",
            "Open space with a full clear circle; no partner within blade range during solo forms.",
            "Slow speed only until the guru permits otherwise.",
            "The sword is saluted before and after every session.",
        ],
        "standards": [
            "Traditional kalari curriculum - angathari stage, sword forms.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - metal weapons.",
        ],
        "citations": [CIT_ZARRILLI, CIT_DRAEGER, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, the vaal is the oath of the blade: "
            "the saluted sword the vow that power is reverent, the rolling "
            "wrist the signature learned on wood, and the deep step the "
            "promise that the cut is delivered whole. The Signature method "
            "treats the sword as the emblem of discipline, not of harm.",
    },
    {
        "key": "paricha",
        "name": "Paricha (Shield)",
        "group": "Weapons - Metal",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description":
            "The paricha is the shield of kalaripayattu - a round buckler "
            "about twelve to fifteen inches across, traditionally of hide or "
            "metal over a wooden core, gripped at the center - and the "
            "art answer to the attack. The shield is not a wall to hide "
            "behind but an active weapon: it deflects, it beats aside, it "
            "binds the opponent weapon, and its rim strikes. Students learn "
            "the shield together with the sword because the two are "
            "partners - the paricha guards the line while the vaal answers - "
            "and the shield forms teach the angles of defense: the high "
            "guard, the low guard, the sweeping parry, and the bind. A "
            "practitioner skilled with the paricha can stand in the storm of "
            "attacks and choose the moment to answer.",
        "how_it_works":
            "Grip the paricha at its center boss with the fist, the forearm "
            "behind the shield face. Stand in ashva vadivu with the shield "
            "held before the torso. The high guard: raise the shield to cover "
            "head and chest, elbow tucked. The low guard: drop it to cover "
            "the abdomen and lead leg. The sweeping parry: swing the shield "
            "in an arc to beat an incoming attack offline - practice with a "
            "partner tapping a wooden stick against the shield, ten parries "
            "each side. The bind: catch the partner stick on the shield face "
            "and press it offline while stepping in - ten binds. Drill the "
            "guard changes: high, low, high, low - twenty changes, keeping "
            "the shield always between you and the partner. Then the shield "
            "form: advances and turns with guard changes and parries, three "
            "unbroken minutes.",
        "key_points": [
            "Category: weapons - the round shield, twelve to fifteen inches across.",
            "An active weapon: deflects, beats aside, binds, and rim-strikes.",
            "Guards: high guard for head and chest, low guard for body and leg.",
            "Techniques: sweeping parry, bind, guard changes.",
            "The sword partner - the shield guards the line while the blade answers.",
        ],
        "requirements": [
            "A paricha shield; a partner with a wooden practice weapon.",
            "Protective eyewear; controlled contact only.",
            "Sword training underway - shield and sword are learned together.",
        ],
        "standards": [
            "Traditional kalari curriculum - angathari stage, shield forms.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - metal weapons.",
        ],
        "citations": [CIT_ZARRILLI, CIT_DRAEGER, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, the paricha is the oath of the "
            "guard: the round face the vow to meet force with angles, not "
            "with fear, the sweeping parry the signature of redirection, and "
            "the bind the promise that defense chooses its moment. The "
            "Signature method treats the shield as the patient partner of "
            "the blade.",
    },
    {
        "key": "valum_parichayum",
        "name": "Valum Parichayum (Sword and Shield)",
        "group": "Weapons - Metal",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description":
            "Valum parichayum is the combined art of sword and shield - vaal "
            "meaning sword and paricha meaning shield - the signature paired "
            "weapons of kalaripayattu and the summit of the angathari stage "
            "before the advanced weapons. The two hands learn different "
            "jobs and do them at once: the shield hand guards, parries, and "
            "binds while the sword hand cuts and thrusts, and the body "
            "moves both through the vadivus in continuous flow. The "
            "valum parichayum forms are the most complete expression of the "
            "art battlefield method - defense and attack as one motion - and "
            "students drill them for years, first solo, then in the paired "
            "exercises where two practitioners trade sword-and-shield "
            "sequences at controlled speed.",
        "how_it_works":
            "Take the paricha in the lead hand and the vaal in the rear "
            "hand; stand in gaja vadivu. The basic exchange: partner attacks "
            "with a slow overhead cut - parry it offline with the shield, "
            "step deep, and answer with a controlled sword cut that stops "
            "short - ten exchanges, then swap roles. Solo form next: advance "
            "in gaja vadivu cutting downward with the sword while the shield "
            "holds high guard; turn into ashva vadivu, shield sweeping a "
            "parry, sword cutting horizontal; drop toward simha vadivu, "
            "shield low, sword thrusting. Link the sequence for three "
            "unbroken minutes, the two hands working their different jobs "
            "without tangling. Paired form: two practitioners perform the "
            "exchange sequence together, attack and defense alternating, at "
            "slow controlled speed - five minutes. Speed increases only with "
            "the guru permission.",
        "key_points": [
            "Category: weapons - the combined sword-and-shield method.",
            "Shield hand guards, parries, and binds; sword hand cuts and thrusts.",
            "The summit of the angathari stage before the advanced weapons.",
            "Defense and attack as one continuous motion.",
            "Drilled solo first, then in paired exchanges at controlled speed.",
        ],
        "requirements": [
            "Training vaal and paricha; sword and shield forms learned separately first.",
            "A trained partner for all paired exchanges.",
            "Protective eyewear; controlled contact only.",
            "Speed increases only with the guru permission.",
        ],
        "standards": [
            "Traditional kalari curriculum - angathari stage, combined arms.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - metal weapons.",
        ],
        "citations": [CIT_ZARRILLI, CIT_GREEN, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, valum parichayum is the oath of the "
            "pair: the shield the vow of patience, the sword the promise of "
            "decision, and the two hands the signature that defense and "
            "answer are one motion. The Signature method treats the combined "
            "arms as the complete sentence of the battlefield art.",
    },
    {
        "key": "verumkai",
        "name": "Verumkai (Empty-Hand Combat)",
        "group": "Empty Hand",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description":
            "Verumkai is the empty-hand combat of kalaripayattu - verum "
            "meaning bare or empty and kai meaning hand - the art of "
            "fighting with no weapon at all. It is taught late in the "
            "curriculum, after the weapons, because the tradition holds that "
            "the empty hand is the most advanced weapon: with no stick and "
            "no blade to extend the reach, the practitioner must enter deep, "
            "move perfectly, and use the whole body as the weapon. Verumkai "
            "woven from everything learned before - the vadivu entries, the "
            "chuvadukal footwork, the kicks of the rooster posture, the "
            "traps and controls of the dagger work - into strikes, locks, "
            "throws, and evasions. The empty hand is where the art proves "
            "that the body itself was the weapon all along.",
        "how_it_works":
            "Face a partner at training distance in gaja vadivu, both with "
            "open hands. The basic entry: partner extends an arm slowly - "
            "step deep offline into ashva vadivu, trap the extended arm with "
            "both hands, and turn the hip to unbalance - ten entries, then "
            "swap roles. The palm strike: from the trap, step in and drive "
            "the heel of the palm forward from the hip, stopping short of "
            "contact - ten each hand. The leg sweep: as the partner steps, "
            "sweep the supporting leg with your own at ankle height with a "
            "controlled touch - ten each side, the partner practicing the "
            "breakfall. The evasion: partner pushes toward your chest; yield "
            "into sarpam vadivu, let the push pass, and rise beside the "
            "partner - ten evasions. Link them: entry, trap, palm strike "
            "(stopped short), sweep (controlled touch) - the verumkai "
            "sequence, five minutes of slow, precise practice.",
        "key_points": [
            "Category: empty hand - combat with no weapon, taught after the weapons.",
            "Woven from vadivu entries, chuvadukal, kicks, and dagger-work controls.",
            "Techniques: deep entries, traps, palm strikes, leg sweeps, evasions.",
            "All partner contact controlled; strikes stop short, sweeps touch lightly.",
            "Proves the body itself was the weapon all along.",
        ],
        "requirements": [
            "A trained partner; the full weapons curriculum before it.",
            "Matted surface for breakfall practice.",
            "Controlled contact only: strikes stop short, sweeps touch lightly.",
            "The guru supervises all paired empty-hand work.",
        ],
        "standards": [
            "Traditional kalari curriculum - verumkai as the late empty-hand stage.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - empty hand.",
        ],
        "citations": [CIT_ZARRILLI, CIT_REID, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, verumkai is the oath of the bare "
            "hand: the deep entry the vow that the body goes where the "
            "weapon cannot, the stopped-short strike the signature of "
            "control, and the controlled touch the promise that mastery is "
            "measured in restraint. The Signature method treats the empty "
            "hand as the final proof of the whole ladder.",
    },
    {
        "key": "kaal_adikal",
        "name": "Kaal Adikal (Kalari Kicks)",
        "group": "Empty Hand",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description":
            "Kaal adikal are the kicks of kalaripayattu - kaal meaning leg "
            "and adi meaning strike - and they are among the highest and "
            "most spectacular kicks in the world martial arts. Chambered "
            "from the kukkuda rooster posture and powered by the kalugal leg "
            "conditioning, the kalari kicks include the straight front kick, "
            "the high side kick, the spinning kick, the jumping kick, and "
            "the sweeping low kick, all delivered with the body upright and "
            "the standing leg rooted. The tradition teaches kicks as part of "
            "the meippayattu body forms long before they appear in "
            "verumkai, so that by the time the student kicks against a "
            "partner, the chamber, the extension, and the rechamber are "
            "already instinct. The kick is never thrown for show; it is the "
            "rooster spur, fast and chambered.",
        "how_it_works":
            "Stand in kukkuda vadivu, the rooster posture, on the left leg "
            "with the right knee chambered at hip height. The front kick: "
            "extend the right leg straight forward at hip height, driving "
            "with the ball of the foot, then rechamber to the knee-up "
            "position without touching down - ten kicks, then switch legs. "
            "The side kick: from the chamber, pivot on the standing foot and "
            "extend the leg sideways at hip height - ten each leg. The "
            "spinning kick: from gaja vadivu, spin on the front foot and "
            "extend the rear leg into a back kick at waist height, landing "
            "back in stance - five each side, slowly. Practice all kicks "
            "against a held pad with a partner: ten front kicks, ten side "
            "kicks per leg, striking the pad with control. Finish with the "
            "kick form: front kick, side kick, spinning kick linked with "
            "vadivu changes - three unbroken minutes.",
        "key_points": [
            "Category: empty hand - among the highest kicks in the world martial arts.",
            "Chambered from kukkuda vadivu; powered by kalugal conditioning.",
            "The kicks: front, side, spinning, jumping, and low sweeping.",
            "Chamber, extension, rechamber - the kick returns as fast as it goes.",
            "Taught in the body forms long before partner practice.",
        ],
        "requirements": [
            "Kukkuda vadivu balance and kalugal flexibility built first.",
            "A held kicking pad and a partner for target practice.",
            "Matted surface for jumping-kick practice.",
            "Never kick a partner; pads only, with control.",
        ],
        "standards": [
            "Traditional kalari curriculum - kaal adikal kicking syllabus.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - kicks.",
        ],
        "citations": [CIT_ZARRILLI, CIT_DRAEGER, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, the kaal adikal are the oath of the "
            "rooster spur: the chamber the vow held, the extension the word "
            "spoken, and the rechamber the signature that nothing is left "
            "hanging. The Signature method treats the kick as punctuation - "
            "fast, precise, and always returned to the sentence.",
    },
    {
        "key": "gada",
        "name": "Gada (Mace)",
        "group": "Weapons - Metal",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description":
            "The gada is the mace of kalaripayattu - a heavy-headed club of "
            "wood or metal, about two to three feet long with a weighted "
            "head - and the weapon of pure power in the art. Where the sword "
            "cuts and the spear pierces, the mace crushes through guards: it "
            "teaches the practitioner to generate force from the ground up, "
            "through the legs, the waist, and the shoulders, into a single "
            "devastating arc. The gada forms are short and heavy - there is "
            "no flourish with the mace, only the chamber, the step, and the "
            "fall of the head. Training with the gada builds the grip, the "
            "shoulders, and the whole-body coordination that makes every "
            "other weapon heavier in the hand and lighter in the technique.",
        "how_it_works":
            "Grip the gada near the end of the handle with both hands "
            "overlapping, the head resting near the shoulder. Stand in gaja "
            "vadivu. The overhead smash: raise the mace high behind the "
            "head, step deep forward, and bring the head down in a vertical "
            "arc, the whole body dropping into the stance behind it - exhale "
            "sharply on the fall. The side smash: swing the head in a "
            "horizontal arc at shoulder height, pivoting fully on the feet. "
            "The rising smash: sweep from low to high. Drill five of each - "
            "the mace is heavy and the sets stay short - then rest one "
            "minute. Practice the guard: hold the mace across the body, the "
            "heavy head ready to beat aside an attack. Link the three "
            "smashes with steps and turns into the gada form - two unbroken "
            "minutes. Never train the mace to exhaustion; heavy-weapon "
            "fatigue causes injury.",
        "key_points": [
            "Category: weapons - the mace, two to three feet with a weighted head.",
            "The weapon of pure power; force generated from the ground up.",
            "Three smashes: overhead, side, and rising.",
            "Short heavy sets of five; never train to exhaustion.",
            "Builds the grip and whole-body power behind all other weapons.",
        ],
        "requirements": [
            "A training gada of appropriate weight for the student size.",
            "Kolthari stage completed; strong vadivu stances.",
            "Open space with a full clear circle; no partner in range.",
            "Short sets with rest; stop at fatigue.",
        ],
        "standards": [
            "Traditional kalari curriculum - angathari stage, mace forms.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - metal weapons.",
        ],
        "citations": [CIT_ZARRILLI, CIT_GREEN, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, the gada is the oath of weight: the "
            "heavy head the vow that power comes from the ground, the short "
            "set the promise of respect for the body, and the falling arc "
            "the signature of total commitment. The Signature method treats "
            "the mace as the teacher of honesty - it cannot be faked.",
    },
    {
        "key": "madu",
        "name": "Madu (Twin Horn Dagger)",
        "group": "Weapons - Metal",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description":
            "The madu is the twin horn dagger of kalaripayattu - a pair of "
            "short blades or sharpened horns joined at the handles, "
            "traditionally made from the antlers of the deer, one point "
            "facing forward and one back - and one of the most distinctive "
            "weapons in the world martial arts. Wielded as a pair, the madu "
            "is simultaneously shield and dagger: one horn parries and traps "
            "while the other strikes, and the crossed horns can catch and "
            "bind an opponent weapon. The madu forms are intricate, the two "
            "hands weaving independent patterns while the body moves through "
            "the vadivus. It is an advanced weapon, taught only after the "
            "student has proven control with the single dagger and the "
            "sword, because the madu punishes inattention twice over.",
        "how_it_works":
            "Take a madu in each hand, gripping the joined handles so one "
            "horn points forward and one back from each fist. Stand in "
            "ashva vadivu. The basic parry-strike: as a partner taps a "
            "wooden stick toward you slowly, parry it offline with the left "
            "madu and answer with a controlled forward thrust of the right "
            "madu that stops short - ten exchanges, then swap the roles of "
            "the hands. The bind: catch the partner stick between the "
            "crossed horns of one madu, twist, and draw it offline - ten "
            "binds each hand. The weave: move both madu in alternating "
            "figure-eight patterns in front of the body while advancing in "
            "gaja vadivu - the two hands independent, the body steady. "
            "Drill the weave for three unbroken minutes. All paired madu "
            "work at slow speed with wooden practice weapons.",
        "key_points": [
            "Category: weapons - the twin horn dagger, wielded as a pair.",
            "Traditionally of deer antler; one horn forward, one back per hand.",
            "Simultaneously shield and dagger: one horn parries, the other strikes.",
            "The crossed horns catch and bind an opponent weapon.",
            "Advanced weapon - taught after the single dagger and sword are proven.",
        ],
        "requirements": [
            "A pair of training madu; wooden practice weapons for paired drills.",
            "Kadhara and vaal training completed and approved by the guru.",
            "A trained partner; protective eyewear; slow speed only.",
            "The guru supervises all paired madu work.",
        ],
        "standards": [
            "Traditional kalari curriculum - angathari stage, advanced weapons.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - metal weapons.",
        ],
        "citations": [CIT_ZARRILLI, CIT_GREEN, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, the madu is the oath of the pair: "
            "the forward horn the vow of answer, the back horn the promise "
            "of guard, and the independent hands the signature that the "
            "body can speak two sentences at once. The Signature method "
            "treats the twin daggers as the proof of divided attention "
            "mastered.",
    },
    {
        "key": "urumi",
        "name": "Urumi (Flexible Sword)",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description":
            "The urumi is the flexible sword of kalaripayattu - a long band "
            "of spring steel, four to six feet, sharp on both edges, that "
            "coils like a whip - and the most famous weapon of the art. Worn "
            "coiled around the waist like a belt, the urumi is drawn and "
            "set spinning in continuous arcs around the body, the flexible "
            "blade whistling as it cuts the air in every direction at once. "
            "No shield can fully guard against it and no single parry stops "
            "it, which is why the tradition teaches it only to advanced "
            "students of proven control: a mistimed urumi cuts its own "
            "wielder. The urumi forms are the pinnacle of the weapon art - "
            "the practitioner spinning at the center of a storm of steel.",
        "how_it_works":
            "The urumi is learned in stages over many months, always under "
            "the guru direct supervision. Stage one: a cloth band the length "
            "of the urumi, learning the spin patterns - the horizontal spin "
            "around the body, the vertical figure-eight, the transitions - "
            "until the band never touches the body. Stage two: a blunt "
            "metal practice urumi, repeating the patterns at slow speed. "
            "Stage three, only with the guru permission: the sharp urumi. "
            "The basic spin: hold the handle, step into ashva vadivu, and "
            "set the blade circling horizontally around the body at waist "
            "height, the free hand guiding the plane - the blade must pass "
            "cleanly without touching. Drill ten clean spins, rest, repeat. "
            "The form links spins with turns and level changes - two "
            "unbroken minutes. Stop at the first loss of control; the "
            "urumi rewards only the patient.",
        "key_points": [
            "Category: weapons - the flexible whip-sword, four to six feet of spring steel.",
            "Worn coiled at the waist; cuts in continuous spinning arcs.",
            "Learned in stages: cloth band, then blunt steel, then sharp - over months.",
            "A mistimed urumi endangers its own wielder; control is everything.",
            "The pinnacle of the weapon art, taught only to proven advanced students.",
        ],
        "requirements": [
            "A cloth practice band, then a blunt training urumi; the sharp urumi only with guru permission.",
            "The full angathari curriculum completed.",
            "Open space with a wide clear circle; no one else in the training area.",
            "The guru directly supervises every urumi session.",
        ],
        "standards": [
            "Traditional kalari curriculum - angathari stage, the advanced flexible sword.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - advanced weapons.",
        ],
        "citations": [CIT_ZARRILLI, CIT_DRAEGER, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, the urumi is the oath of the storm: "
            "the coiled steel the vow of patience worn at the waist, the "
            "clean spin the signature of absolute control, and the staged "
            "learning the promise that the most dangerous lesson is taught "
            "slowest. The Signature method treats the urumi as the final "
            "examination of everything the ladder taught.",
    },
    {
        "key": "uzhichil",
        "name": "Uzhichil (Kalari Oil Massage)",
        "group": "Body Knowledge",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description":
            "Uzhichil is the oil massage of kalaripayattu - the systematic "
            "full-body massage with warm sesame oil, given by the guru or a "
            "trained practitioner, that is as much a part of the training "
            "as the forms themselves. After the hard conditioning of the "
            "kalugal and meyyorukkam, the uzhichil loosens the muscles, "
            "keeps the joints supple, and teaches the student the map of "
            "the own body - where it is tight, where it is strong, where it "
            "needs care. The massage follows the muscle lines with rhythmic "
            "strokes, and in the traditional kalari it is given regularly "
            "through the training season. Uzhichil is also the doorway to "
            "the deeper body knowledge of the art: the hands that learn the "
            "muscles in massage go on to learn the marma points and the "
            "bone-setting of kalari chikitsa.",
        "how_it_works":
            "Warm pure sesame oil until it is comfortably warm to the touch, "
            "never hot, and spend three minutes working it over the whole "
            "body. The receiver lies on a mat; the giver works with steady "
            "rhythmic strokes. Massage each foot with the thumbs for two "
            "minutes, then stroke up each leg along the muscle lines - ten "
            "long strokes per leg, about two minutes a leg. Work the thighs "
            "with the palms in firm circles for three minutes per leg. "
            "Massage the lower back with palm strokes outward from the "
            "spine - four minutes - then the shoulders and arms, ten "
            "strokes per arm, about two and a half minutes a side. Finish "
            "at the head and neck with gentle fingertip circles for two "
            "minutes, and close with two minutes of slow rest strokes over "
            "the whole body. Total session: about thirty minutes. The "
            "receiver rests for ten minutes afterward and bathes in warm "
            "water. Uzhichil is given two to three times per week during "
            "heavy training seasons.",
        "key_points": [
            "Category: body knowledge - the systematic oil massage of the kalari.",
            "Warm sesame oil, rhythmic strokes along the muscle lines.",
            "Loosens muscles, keeps joints supple, maps the body for the student.",
            "Given two to three times per week in heavy training seasons.",
            "The doorway to marma knowledge and kalari chikitsa.",
        ],
        "requirements": [
            "Pure sesame oil, warmed - never hot; a mat in a warm room.",
            "A trained giver; the receiver rests ten minutes after.",
            "Warm bath after the session; about thirty minutes per session.",
            "Gentle pressure on the neck and joints; firm on the large muscles.",
        ],
        "standards": [
            "Traditional kalari curriculum - uzhichil as training-season practice.",
            "Ayurvedic oil-massage discipline allied to the kalari tradition.",
        ],
        "citations": [CIT_ZARRILLI, CIT_FRAWLEY, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, uzhichil is the oath of care: the "
            "warm oil the vow that the body is maintained, not merely used, "
            "the rhythmic strokes the signature of attention, and the body "
            "map learned the promise that knowledge begins with touch. The "
            "Signature method treats recovery as training, not as rest from "
            "it.",
    },
    {
        "key": "marma",
        "name": "Marma Sthana (Vital-Point Knowledge)",
        "group": "Body Knowledge",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description":
            "Marma sthana is the traditional knowledge of the body vital "
            "points as handed down in the kalari tradition - marma meaning "
            "a vulnerable or vital point, sthana meaning place. The "
            "tradition counts one hundred and eight marma points across the "
            "human body, mapped over centuries of observation in the "
            "Ayurvedic and kalari healing disciplines. In kalaripayattu "
            "this knowledge is taught strictly as heritage: the study of "
            "where the body is delicate, taught alongside the healing art "
            "of marma chikitsa so that the student understands the body "
            "fragility in order to protect it - in training partners, in "
            "patients, and in the self. The points are learned by location "
            "charts, by touch in massage, and by the guru guidance, and the "
            "first lesson of marma study is responsibility: this knowledge "
            "exists to heal and to safeguard, never to harm.",
        "how_it_works":
            "Marma study begins with the charts: the student learns the "
            "one hundred and eight points by region - the head and neck, "
            "the torso front and back, the arms, the legs - naming each "
            "point and its location on the body. Next comes touch: in "
            "uzhichil massage the guru guides the student hands to feel the "
            "points beneath the skin, learning them as living anatomy "
            "rather than diagram dots. The student then studies the "
            "classical groupings: the points of the head, the points of the "
            "heart region, the points of the joints - and the traditional "
            "cautions attached to each region. Study sessions run about "
            "thirty minutes: ten minutes of chart review, ten minutes of "
            "guided touch on a willing partner, ten minutes of the guru "
            "teaching on the healing applications. Advancement is by the "
            "guru assessment of accuracy and, above all, of the student "
            "demonstrated responsibility.",
        "key_points": [
            "Category: body knowledge - the one hundred and eight vital points of tradition.",
            "Taught strictly as heritage: anatomy, healing, and responsibility.",
            "Learned by charts, by touch in massage, and by guru guidance.",
            "Paired with marma chikitsa - the knowledge exists to heal and safeguard.",
            "The first lesson is responsibility: never to harm.",
        ],
        "requirements": [
            "A willing study partner; anatomical charts of the marma points.",
            "Uzhichil massage training completed first - touch before theory.",
            "The guru directly supervises all marma study.",
            "Thirty-minute study sessions; advancement by guru assessment.",
        ],
        "standards": [
            "Traditional kalari curriculum - marma sthana as heritage knowledge.",
            "Ayurvedic marma discipline: one hundred and eight points (Frawley, Ranade, Lele).",
        ],
        "citations": [CIT_ZARRILLI, CIT_FRAWLEY, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, marma sthana is the oath of the "
            "healer: the one hundred and eight points the map of human "
            "fragility, the guided touch the signature of responsibility, "
            "and the healing application the promise that knowledge serves "
            "protection. The Signature method teaches the vital points so "
            "that every hand in the art knows how precious the body is.",
    },
    {
        "key": "kalari_chikitsa",
        "name": "Kalari Chikitsa (Bone-Setting Tradition)",
        "group": "Body Knowledge",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description":
            "Kalari chikitsa is the traditional bone-setting and injury "
            "treatment of the kalari - chikitsa meaning treatment - the "
            "healing discipline that has always walked beside the martial "
            "discipline. The kalari gurukkal is traditionally both teacher "
            "and healer: the same hands that guide the forms set the "
            "dislocated joint, bind the sprain, and massage the bruise. "
            "Kalari chikitsa covers the assessment of training injuries, "
            "the manual techniques for joints and soft tissue, the herbal "
            "oils and poultices of the tradition, and the rehabilitation "
            "exercises that return the practitioner to training. Students "
            "learn it by assisting the guru with real cases over years - "
            "there is no shortcut to the healer hands. The tradition holds "
            "that one who learns to fight must learn to mend, or the art is "
            "only half learned.",
        "how_it_works":
            "Study begins with observation: the student assists the guru "
            "during treatment sessions, learning the assessment sequence - "
            "look at the injury, ask how it happened, feel gently for "
            "swelling heat and misalignment, compare with the uninjured "
            "side. Next the basic techniques, practiced first on uninjured "
            "partners: the joint mobilizations - slow, gentle circles of "
            "the shoulder, elbow, wrist, knee, and ankle through their full "
            "range, ten circles each direction; the soft-tissue strokes with "
            "warm herbal oil along the muscle lines; the binding - wrapping "
            "a sprain with firm even bandaging that supports without "
            "cutting circulation. The rehabilitation: progressive return-to-"
            "training exercises matched to the healing stage. Sessions run "
            "about forty-five minutes. Serious injuries - suspected "
            "fractures, deep wounds, head injuries - are always referred to "
            "modern medical care; the tradition knows its boundaries.",
        "key_points": [
            "Category: body knowledge - the traditional bone-setting and injury treatment.",
            "The gurukkal is traditionally both teacher and healer.",
            "Assessment: look, ask, feel gently, compare with the uninjured side.",
            "Techniques: joint mobilization, herbal-oil strokes, binding, rehabilitation.",
            "Serious injuries are always referred to modern medical care.",
        ],
        "requirements": [
            "Years of assisting the guru with real cases; no shortcut to healer hands.",
            "Herbal oils, bandages, and a clean treatment space.",
            "Uzhichil and marma study completed first.",
            "Know the boundaries: fractures, deep wounds, and head injuries go to modern care.",
        ],
        "standards": [
            "Traditional kalari curriculum - kalari chikitsa as the healing discipline.",
            "Ayurvedic treatment discipline allied to the kalari tradition.",
        ],
        "citations": [CIT_ZARRILLI, CIT_FRAWLEY, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, kalari chikitsa is the oath of the "
            "mender: the assessing hands the vow to understand before "
            "touching, the gentle mobilization the signature of patience, "
            "and the referral to modern care the promise of honesty about "
            "limits. The Signature method holds that one who learns the "
            "forms must learn the mending, or the art is half learned.",
    },
    {
        "key": "angathari",
        "name": "Angathari (Metal-Weapon Forms)",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description":
            "Angathari is the metal-weapons stage of kalaripayattu - angam "
            "meaning body or limb, thari meaning practice, in some tellings "
            "the practice of the body against metal - the complete "
            "curriculum of blades and points: the kadhara dagger, the "
            "kuntham spear, the vaal sword, the paricha shield, the combined "
            "valum parichayum, the gada mace, and the madu twin daggers, "
            "woven into formal solo and paired forms. It is the third great "
            "stage of the art, after meippayattu and kolthari, and the "
            "longest: students typically spend years in angathari, because "
            "each weapon is a complete study and the paired exercises demand "
            "absolute control. The metal does not forgive, so the stage "
            "forges judgment, precision, and the calm that only comes from "
            "practicing dangerous things safely for a very long time.",
        "how_it_works":
            "The angathari session opens with vanakkam to the weapons, then "
            "the meippayattu warm-up. Solo forms in ladder order: the "
            "kadhara dagger form - thrusts, draw cuts, and entries, three "
            "minutes; the kuntham spear form - thrusts, sweeps, and "
            "recoveries, three minutes; the vaal sword form - the four cuts "
            "linked with vadivu changes, three minutes; the valum "
            "parichayum combined form - three minutes; the gada mace form - "
            "two minutes; the madu twin-dagger weave - three minutes. Rest "
            "one minute between forms. Paired exercises follow at slow "
            "controlled speed: dagger against dagger - trap and answer, ten "
            "exchanges; sword and shield against sword and shield - parry, "
            "bind, and controlled answer, ten exchanges; spear against "
            "spear - thrust, parry offline, and recover, ten exchanges. "
            "Total angathari session: about ninety minutes. Speed advances "
            "only by guru permission, weapon by weapon.",
        "key_points": [
            "Category: advanced - the complete metal-weapons stage.",
            "Woven from dagger, spear, sword, shield, combined arms, mace, and twin daggers.",
            "The third great stage: after meippayattu and kolthari; the longest stage.",
            "Solo forms build precision; paired exercises build judgment.",
            "The metal does not forgive - control is the whole curriculum.",
        ],
        "requirements": [
            "The full set of training metal weapons; kolthari stage completed.",
            "A trained partner for all paired exercises.",
            "Protective eyewear; first-aid kit present; ninety minutes per session.",
            "Speed advances only by guru permission, weapon by weapon.",
        ],
        "standards": [
            "Traditional kalari curriculum - angathari as the third stage.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - metal weapons.",
        ],
        "citations": [CIT_ZARRILLI, CIT_DRAEGER, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, angathari is the oath of the metal: "
            "the dagger the first word, the spear the long sentence, the "
            "sword the signature, and the paired exercise the dialogue held "
            "at slow speed. The Signature method treats this longest stage "
            "as the forge where judgment is tempered like steel.",
    },
    {
        "key": "verumkai_uttama",
        "name": "Verumkai Uttama (Advanced Empty-Hand)",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description":
            "Verumkai uttama is the advanced empty-hand of kalaripayattu - "
            "uttama meaning highest or supreme - the summit of the bare-hand "
            "art taught only to senior students. Where basic verumkai "
            "teaches entries, traps, and controls, the uttama level teaches "
            "the seamless flow: multiple attackers handled by position and "
            "timing rather than force, weapon defenses where the empty hand "
            "meets the stick and the blade with evasion and control, and the "
            "integration of the marma body knowledge into the gentlest "
            "effective controls. The hallmark of verumkai uttama is economy - "
            "the senior practitioner ends the encounter in a single motion, "
            "having moved less than anyone else in the room. It is the art "
            "proving that the highest technique looks like nothing at all.",
        "how_it_works":
            "All uttama practice is slow, precise, and supervised. The "
            "positional drill: two partners approach slowly from different "
            "angles; the practitioner yields with chuvadukal footwork, "
            "keeping both in view and never letting them flank - five "
            "minutes of continuous movement, no contact. The stick defense: "
            "partner swings a wooden stick slowly overhead; step offline "
            "into sarpam vadivu, let the swing pass, rise beside the "
            "partner and control the weapon arm with both hands - ten "
            "repetitions, then swap. The control sequence: from the trap, "
            "guide the partner to the ground with a leg sweep touched "
            "lightly at the ankle and settle them with a held control - ten "
            "each side, the partner practicing the breakfall. The flow "
            "form: entries, traps, sweeps, and evasions linked without "
            "pausing - five unbroken minutes. Every technique stops short "
            "of harm; control is graded above all.",
        "key_points": [
            "Category: advanced - the supreme empty-hand, taught only to seniors.",
            "Positional work against multiple approaches; evasion over force.",
            "Weapon defenses by offline movement and control, never by blocking.",
            "Marma body knowledge integrated into the gentlest effective controls.",
            "Economy is the hallmark: the encounter ends in a single motion.",
        ],
        "requirements": [
            "Senior standing; basic verumkai and the weapons curriculum completed.",
            "Two trained partners for positional drills; matted surface.",
            "The guru directly supervises all uttama practice.",
            "Control graded above all; every technique stops short of harm.",
        ],
        "standards": [
            "Traditional kalari curriculum - verumkai uttama as the senior empty-hand.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - advanced empty hand.",
        ],
        "citations": [CIT_ZARRILLI, CIT_REID, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, verumkai uttama is the oath of "
            "economy: the single motion the vow that less is more, the "
            "offline step the signature of wisdom over force, and the "
            "gentle control the promise that the highest hand harms least. "
            "The Signature method treats the supreme empty-hand as proof "
            "that mastery looks like nothing at all.",
    },
    {
        "key": "sarva_shastra",
        "name": "Sarva Shastra Prayogam (Mastery of the Full Arsenal)",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description":
            "Sarva shastra prayogam is the mastery of the full arsenal - "
            "sarva meaning all, shastra meaning weapon or science, prayogam "
            "meaning application - the capstone of the kalaripayattu ladder "
            "where the practitioner demonstrates command of every stage: the "
            "vanakkam and the eight vadivus, the meippayattu body forms, the "
            "kolthari wooden weapons, the angathari metal weapons, the "
            "verumkai empty hand, the urumi flexible sword, and the body "
            "knowledge of uzhichil, marma, and kalari chikitsa. It is not a "
            "single form but the synthesis - the ability to move between "
            "stages without hesitation, to choose the right response for "
            "each moment, and to teach the ladder to others. In the "
            "tradition, the practitioner who reaches sarva shastra prayogam "
            "is recognized as a complete martial artist and a keeper of the "
            "art, entrusted with carrying it to the next generation.",
        "how_it_works":
            "The synthesis is demonstrated as a complete session performed "
            "without pause. Open with vanakkam, then the eight vadivus held "
            "in sequence - one minute each. Perform two meippayattu "
            "sequences - ten minutes. Take up the wooden weapons: muchan "
            "form, otta form, staff form - three minutes each. Take up the "
            "metal: dagger form, spear form, sword form, sword-and-shield "
            "form - three minutes each. Demonstrate the urumi spin - two "
            "minutes of clean patterns. Close with the verumkai flow form - "
            "five minutes - and vanakkam. Total demonstration: about sixty "
            "minutes of unbroken practice. The guru assesses not speed but "
            "completeness: every stage present, every transition clean, the "
            "breath steady throughout, and the body knowledge evident in "
            "how the practitioner cares for the training partners. Passing "
            "this demonstration marks the practitioner as a keeper of the "
            "art.",
        "key_points": [
            "Category: advanced - the capstone synthesis of the whole ladder.",
            "Commands every stage: stances, body forms, wooden and metal weapons, empty hand, urumi, body knowledge.",
            "A sixty-minute unbroken demonstration, assessed on completeness.",
            "Transitions clean, breath steady, partners cared for.",
            "Marks the practitioner as a keeper of the art for the next generation.",
        ],
        "requirements": [
            "The entire ladder completed: every stage approved by the guru.",
            "Full set of training weapons; a kalari or large training space.",
            "Peak physical condition; sixty minutes of unbroken demonstration.",
            "The guru and senior practitioners as assessors.",
        ],
        "standards": [
            "Traditional kalari curriculum - sarva shastra prayogam as the capstone.",
            "Indian Kalarippayattu Federation (IKF) technical syllabus - mastery assessment.",
        ],
        "citations": [CIT_ZARRILLI, CIT_GREEN, CIT_IKF],
        "sig_lens":
            "Through the Signature lens, sarva shastra prayogam is the final "
            "oath: the sixty unbroken minutes the complete signature, every "
            "stage a word in it, and the keeper recognition the promise to "
            "carry the archive forward. The Signature method ends where it "
            "began - with vanakkam - because the ladder is a circle, and "
            "the master returns to the salutation as a teacher.",
    },
]
