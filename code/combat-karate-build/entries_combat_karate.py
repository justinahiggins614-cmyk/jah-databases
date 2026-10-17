#!/usr/bin/env python3
"""Entries for the Karate Combat databases (combat batch 1, 2026-10-17).

Two NEW databases, 34 ladder-ordered records each:

  combat-karate              - The Karate Combat Database
                               (public-harvest: real, fact-checked karate
                               knowledge - Okinawan and Japanese karate:
                               Shotokan, Goju-Ryu, Shorin-Ryu, Kyokushin
                               and kin - every stance, strike, block, kick,
                               kata movement, and kumite principle taught
                               as a full technique record with step-by-step
                               body mechanics; standard references Funakoshi
                               Karate-Do Kyohan 1973, Nakayama Best Karate
                               1977-1987 and Dynamic Karate 1966, Oyama This
                               is Karate 1965 and Advanced Karate 1970,
                               Higaonna Traditional Karate-do Okinawa Goju
                               Ryu 1985, Pfluger 25 Shotokan Katas 2009,
                               and JKA technical standards)
  combat-karate-signature    - The Karate Combat Signature Database
                               (his original Signature combat method: every
                               technique a covenant of body and breath, the
                               stance the oath of the ground, the strike
                               the signature of the hip, kata the archive
                               of the ancestors written in motion; src
                               signature, titles suffixed " (Signature
                               Edition)", never presented as authentic
                               public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBK- (public) and JAH-CBKS- (signature), verified free
in the manifest id_prefix values and zero hits in every shard index file.

Dedupe: all 68 titles (34 public + 34 Signature Edition) run through the
whole-system dedupe gate before authoring - zero refusals, zero collisions.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_karate.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Screening: civilian martial-arts instruction only. Nothing hate-adjacent,
profane, or inappropriate; no religious talk. Nothing on neutralizing or
defeating military or defense-grade systems - the standing exclusion holds.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature combat method: every "
            "technique a covenant of body and breath, the stance the oath of "
            "the ground, the strike the signature of the hip, and kata the "
            "archive of the ancestors written in motion. Clearly labeled "
            "Signature-made, never presented as authentic public record.")

CIT_FUNAKOSHI_KYOHAN = ("Funakoshi G. Karate-Do Kyohan: The Master Text. "
                        "Tokyo: Kodansha International; 1973.")
CIT_FUNAKOSHI_WAY = ("Funakoshi G. Karate-Do: My Way of Life. Tokyo: Kodansha "
                     "International; 1975.")
CIT_NAKAYAMA_BEST = ("Nakayama M. Best Karate series, vols. 1-11. Tokyo: "
                     "Kodansha International; 1977-1987.")
CIT_NAKAYAMA_DYNAMIC = ("Nakayama M. Dynamic Karate. Tokyo: Kodansha "
                        "International; 1966.")
CIT_OYAMA_THIS = ("Oyama M. This is Karate. Tokyo: Japan Publications; 1965.")
CIT_OYAMA_ADV = ("Oyama M. Advanced Karate. Tokyo: Japan Publications; 1970.")
CIT_HIGAONNA = ("Higaonna M. Traditional Karate-do: Okinawa Goju Ryu, vol. 1: "
                "The Fundamental Techniques. Tokyo: Minato Research; 1985.")
CIT_PFLUGER = ("Pfluger A. 25 Shotokan Katas. 2nd ed. Dornheim: Schlatt "
               "Books; 2009.")
CIT_JKA = ("Japan Karate Association. JKA Technical Standards and Grading "
           "Syllabus: kihon, kata, kumite. Tokyo: JKA; current edition.")

ENTRIES = [
    {
        "key": "zenkutsu",
        "name": "Zenkutsu-dachi (Front Stance)",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description":
            "Zenkutsu-dachi, the front stance, is the first stance every karate "
            "student learns and the foundation of all forward-driving power in "
            "Okinawan and Japanese karate. The front leg bends deeply with the "
            "knee tracking directly over the foot while the rear leg stays "
            "straight and drives into the floor; the hips stay square to the "
            "front and the torso stays upright with the back straight. Roughly "
            "sixty percent of the body weight settles over the front leg, and "
            "the feet sit about two shoulder-widths apart from front to back, "
            "the rear foot angled about thirty degrees outward for a stable "
            "base. Nearly every forward punch, strike, and block in the basic "
            "curriculum is thrown from this stance, which is why masters call "
            "it the stance that teaches the legs to speak.",
        "how_it_works":
            "Stand in a natural ready position with feet together. Step one "
            "foot straight forward about two of your own shoulder-widths, "
            "keeping the feet roughly one shoulder-width apart side to side. "
            "Bend the front knee until it sits directly above the toes of the "
            "front foot, about a ninety-degree bend, and press the front foot "
            "flat into the floor. Straighten the rear leg fully and press the "
            "rear heel down into the floor with the rear foot turned about "
            "thirty degrees outward. Square the hips to face directly forward, "
            "pull the lower abdomen in, keep the back straight and upright, "
            "and settle about sixty percent of your weight onto the front leg. "
            "Hold for slow counts of ten while a partner checks that the front "
            "knee does not drift past the toes and the rear heel stays down.",
        "key_points": [
            "Category: stances - the root of all forward technique.",
            "Front knee tracks directly over the toes, about a ninety-degree bend.",
            "Rear leg straight with the heel pressed into the floor.",
            "Rear foot angled about thirty degrees outward for lateral stability.",
            "Hips square to the front; torso upright; back straight.",
            "Weight distribution about sixty percent front, forty percent rear.",
            "Feet about two shoulder-widths apart front to back.",
        ],
        "requirements": [
            "Flat, non-slippery training surface with room to step forward.",
            "Bare feet or flat dojo shoes; loose training uniform.",
            "A mirror or partner to check knee, heel, and hip alignment.",
            "Five to ten minutes of leg warm-up before deep stance holding.",
        ],
        "standards": [
            "JKA kihon stance standards (zenkutsu-dachi).",
            "Shotokan grading syllabus - 9th kyu stance requirements.",
        ],
        "citations": [CIT_FUNAKOSHI_KYOHAN, CIT_NAKAYAMA_BEST, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, zenkutsu-dachi is the oath the body "
            "swears to the ground: the front leg the vow, the rear leg the "
            "witness, and the sixty-forty weight the honest measure of "
            "commitment. Every forward technique in the Signature method is "
            "signed by this stance before it is thrown.",
    },
    {
        "key": "kiba",
        "name": "Kiba-dachi (Horse Stance)",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description":
            "Kiba-dachi, the horse stance, is the wide side-facing stance named "
            "for the posture of a rider on horseback. The feet sit parallel "
            "about two shoulder-widths apart with the toes pointing straight "
            "forward, the knees bend and press outward over the toes, and the "
            "weight spreads evenly fifty-fifty between the legs while the back "
            "stays straight and the hips sink low. It is the signature stance "
            "of the Tekki (Naihanchi) kata line and the root of all side-facing "
            "technique, teaching the legs to root while the upper body stays "
            "free to strike, block, and turn. Beginners build leg strength and "
            "hip stability here that every later stance borrows.",
        "how_it_works":
            "Stand with feet together, then step one foot sideways about two "
            "shoulder-widths so the feet are parallel and the toes point "
            "straight forward. Bend both knees and press them outward so each "
            "knee tracks over its own foot, sinking the hips until the thighs "
            "approach a deep, powerful bend while the back stays straight and "
            "upright. Keep the feet flat and the toes gripping the floor; do "
            "not let the knees collapse inward. Distribute the weight evenly, "
            "fifty percent on each leg, pull the lower abdomen in, and set the "
            "fists at the hips or in a guard. Hold for slow counts, breathing "
            "steadily, while a partner checks that the knees stay outside the "
            "feet and the back does not lean.",
        "key_points": [
            "Category: stances - the root of all side-facing technique.",
            "Feet parallel, about two shoulder-widths apart, toes forward.",
            "Knees bent and pressed outward, tracking over the toes.",
            "Weight even: fifty percent on each leg.",
            "Back straight and upright; hips sunk; abdomen pulled in.",
            "Signature stance of the Tekki (Naihanchi) kata line.",
        ],
        "requirements": [
            "Flat, non-slippery training surface with side-to-side room.",
            "Bare feet or flat dojo shoes.",
            "Warmed-up knees and hips; never force depth through knee pain.",
            "A mirror or partner to check knee tracking and back posture.",
        ],
        "standards": [
            "JKA kihon stance standards (kiba-dachi).",
            "Shorin-Ryu and Shotokan Naihanchi/Tekki stance requirements.",
        ],
        "citations": [CIT_FUNAKOSHI_KYOHAN, CIT_NAKAYAMA_DYNAMIC, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, kiba-dachi is the rider's covenant: "
            "two legs the pillars of a gate, the even weight the balanced "
            "scales, and the outward knees the walls no wind moves. The "
            "Signature method treats this stance as the anvil on which "
            "side-facing power is forged.",
    },
    {
        "key": "kamae",
        "name": "Kamae (Fighting Guard)",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description":
            "Kamae is the fighting guard posture - the ready position from "
            "which all kumite begins and to which it returns. From a front or "
            "side stance base, the lead hand extends toward the opponent at "
            "about face height, roughly a forearm's length ahead of the face, "
            "while the rear hand guards the chin and jaw; both elbows tuck "
            "close to the body, angled in about twenty to thirty degrees, to "
            "shield the ribs. The guard is alive rather than rigid: hands "
            "relaxed but ready, eyes on the opponent, weight settled so the "
            "body can move in any direction. A correct kamae both protects the "
            "vital targets and hides the practitioner's intentions.",
        "how_it_works":
            "Settle into a front stance or a free sparring stance with knees "
            "soft and weight balanced. Raise the lead hand to about face "
            "height, extending it roughly a forearm's length ahead of your "
            "face with the fist loosely closed and the knuckles facing the "
            "opponent. Bring the rear hand up to guard the chin and jaw, the "
            "fist about a fist's width from the chin. Tuck both elbows close "
            "to the ribs, angled inward about twenty to thirty degrees, so "
            "the forearms shield the torso. Keep the shoulders relaxed and "
            "down, the eyes fixed on the opponent's chest and eyes, and the "
            "stance light enough to step instantly. Practice raising the "
            "guard from a natural stance in one smooth motion until it becomes "
            "reflex.",
        "key_points": [
            "Category: stances and guard - the ready posture of kumite.",
            "Lead hand at face height, about a forearm's length ahead.",
            "Rear hand guards the chin and jaw.",
            "Elbows tucked to the ribs, angled in twenty to thirty degrees.",
            "Guard is relaxed but ready; eyes on the opponent.",
            "Weight settled and mobile - able to move any direction instantly.",
        ],
        "requirements": [
            "A stable stance base (front stance or sparring stance).",
            "Clear space to extend the arms without hitting walls or partners.",
            "Light hand or focus-mitt work to test guard integrity.",
            "A partner to check that the chin and ribs stay covered.",
        ],
        "standards": [
            "JKA kumite kamae standards.",
            "Shotokan and Kyokushin sparring guard conventions.",
        ],
        "citations": [CIT_NAKAYAMA_DYNAMIC, CIT_OYAMA_THIS, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, kamae is the drawn bow before the "
            "arrow: the lead hand the question, the rear hand the answer kept "
            "in reserve, and the tucked elbows the walls of the house. The "
            "Signature method reads a fighter's guard the way a reader reads "
            "a first sentence.",
    },
    {
        "key": "chokuzuki",
        "name": "Choku-zuki (Straight Punch)",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description":
            "Choku-zuki, the straight punch, is the first strike of karate and "
            "the measure of all punching to come. Thrown from a front stance "
            "with the fist chambered at the hip, the punching arm drives "
            "straight to the target while the fist rotates one hundred eighty "
            "degrees - from palm-up at the hip to palm-down at full extension "
            "in the classic corkscrew - and the opposite fist pulls sharply "
            "back to the hip in hikite. At the instant of full extension the "
            "whole body locks for a fraction of a second in kime, the focus "
            "of power, with the shoulder, hip, and stance aligned behind the "
            "first two knuckles. A trained straight punch carries the mass of "
            "the arm, about four kilograms, at roughly seven meters per "
            "second, delivering on the order of one hundred joules of kinetic "
            "energy along a straight line.",
        "how_it_works":
            "Stand in zenkutsu-dachi with the right fist chambered at the "
            "right hip, palm up, elbow close to the body. Drive the right "
            "fist straight forward along the centerline toward the target at "
            "solar-plexus height, rotating the fist so it finishes palm-down "
            "at full extension. At the same instant, snap the left fist back "
            "to the left hip, palm up, in hikite - the pull adds rotation to "
            "the torso. Lock the shoulder down, align the wrist straight "
            "behind the first two knuckles, and freeze the whole body for an "
            "instant at full extension: that is kime. Immediately relax and "
            "rechamber along the same line. Practice slowly in the air, then "
            "on a makiwara or heavy bag, checking that the elbow never flares "
            "and the punch never drops below the line.",
        "key_points": [
            "Category: hand strikes - the first and fundamental punch.",
            "Fist rotates one hundred eighty degrees: palm-up to palm-down.",
            "Hikite: the opposite fist pulls sharply to the hip.",
            "Strike with the first two knuckles; wrist straight and locked.",
            "Kime: whole-body focus for an instant at full extension.",
            "About four kilograms of arm mass at seven meters per second: roughly one hundred joules.",
        ],
        "requirements": [
            "Front stance base with correct knee and heel alignment.",
            "Clear line of practice; makiwara, bag, or pads for contact work.",
            "Wrist wraps or correct fist formation to protect the wrist.",
            "Slow air practice before any contact practice.",
        ],
        "standards": [
            "JKA kihon punching standards (choku-zuki, oi-zuki, gyaku-zuki).",
            "Shotokan 9th-8th kyu punching requirements.",
        ],
        "citations": [CIT_FUNAKOSHI_KYOHAN, CIT_NAKAYAMA_BEST, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, choku-zuki is the straight line the "
            "Signature draws between intention and impact: the chamber the "
            "held breath, the rotation the turning of the key, hikite the "
            "anchor thrown behind, and kime the period at the end of the "
            "sentence. Nothing in the Signature method travels crooked.",
    },
    {
        "key": "kokutsu",
        "name": "Kokutsu-dachi (Back Stance)",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description":
            "Kokutsu-dachi, the back stance, is the defensive counterpart of "
            "the front stance: the weight shifts back so about seventy percent "
            "rests on the rear leg while the front foot stays light, often "
            "with only the ball or the light heel touching, ready to kick or "
            "shift. The feet form an L-shape about one and a half "
            "shoulder-widths long, the rear foot turned outward about ninety "
            "degrees and the front foot pointing forward, and the torso turns "
            "about forty-five degrees to present a narrow target while both "
            "knees bend to keep the stance rooted. Blocks thrown from back "
            "stance - the knife-hand block above all - borrow its coiled, "
            "ready-to-spring quality.",
        "how_it_works":
            "From a natural stance, step one foot back and to the side so the "
            "feet form an L-shape about one and a half shoulder-widths long: "
            "front foot pointing forward, rear foot turned outward about "
            "ninety degrees. Bend both knees and sink until the rear knee sits "
            "over the rear foot and the stance feels rooted. Shift about "
            "seventy percent of your weight onto the rear leg; the front leg "
            "stays light with the front foot ready to lift. Turn the torso "
            "about forty-five degrees so the chest angles away from the "
            "front, narrowing the target. Keep the back straight and the head "
            "facing forward over the front shoulder. Practice shifting between "
            "front stance and back stance without rising up, keeping the head "
            "at one level.",
        "key_points": [
            "Category: stances - the defensive, weight-back stance.",
            "About seventy percent of weight on the rear leg; front leg light.",
            "Feet in an L-shape, about one and a half shoulder-widths long.",
            "Rear foot turned outward about ninety degrees.",
            "Torso angled about forty-five degrees; head facing forward.",
            "Home stance of the knife-hand block (shuto-uke).",
        ],
        "requirements": [
            "Flat, non-slippery training surface.",
            "Bare feet or flat dojo shoes.",
            "A mirror or partner to check the L-shape and weight shift.",
            "Ankle and knee warm-up before deep holding.",
        ],
        "standards": [
            "JKA kihon stance standards (kokutsu-dachi).",
            "Shotokan grading syllabus - 8th-7th kyu stance requirements.",
        ],
        "citations": [CIT_FUNAKOSHI_KYOHAN, CIT_NAKAYAMA_BEST, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, kokutsu-dachi is the drawn-back bow: "
            "seventy percent of the archer's weight in the rear leg, the front "
            "foot the arrow already half-nocked. The Signature method teaches "
            "defense here not as retreat but as the loading of the next answer.",
    },
    {
        "key": "nekoashi",
        "name": "Neko-ashi-dachi (Cat Stance)",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description":
            "Neko-ashi-dachi, the cat stance, is the lightest and most mobile "
            "of the basic stances, named for the poised readiness of a cat "
            "about to spring. About ninety percent of the body weight rests "
            "on the rear leg, which bends deeply with the foot flat, while "
            "the front foot touches the ground only with the ball, the heel "
            "raised and the knee guarding the centerline - the front leg is "
            "free to kick, sweep, or shift in an instant. The feet sit close "
            "together, about one shoulder-width apart front to back, and the "
            "torso stays upright and narrow. It appears throughout advanced "
            "kata and is the launch pad for the front kick and for rapid "
            "evasive footwork.",
        "how_it_works":
            "Stand naturally, then shift about ninety percent of your weight "
            "onto one leg - the rear leg - and bend that knee deeply with the "
            "foot flat on the floor. Slide the other foot forward about one "
            "shoulder-width so only the ball of the foot touches the ground, "
            "heel raised, toes gripping lightly. Let the front knee bend and "
            "angle inward slightly so it guards the centerline. Keep the "
            "torso upright, the back straight, and the hands in guard; the "
            "front leg should feel weightless, able to lift into a kick "
            "without any shift of weight. Practice lifting the front knee "
            "into a front-kick chamber and setting it back down without "
            "wobbling, then alternate legs.",
        "key_points": [
            "Category: stances - the lightest, most mobile basic stance.",
            "About ninety percent of weight on the rear leg.",
            "Front foot touches with the ball only; heel raised.",
            "Front knee guards the centerline; front leg free to kick instantly.",
            "Feet close: about one shoulder-width apart front to back.",
            "Torso upright; the stance of poised readiness.",
        ],
        "requirements": [
            "Flat, non-slippery training surface.",
            "Strong ankles and calves; build hold times gradually.",
            "A wall or partner nearby when first learning the balance.",
            "Bare feet to develop toe and ball-of-foot grip.",
        ],
        "standards": [
            "JKA kihon stance standards (neko-ashi-dachi).",
            "Shotokan and Shorin-Ryu advanced kata stance requirements.",
        ],
        "citations": [CIT_FUNAKOSHI_KYOHAN, CIT_NAKAYAMA_BEST, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, neko-ashi-dachi is the held breath "
            "before the pounce: ninety percent of the self in the rooted leg, "
            "ten percent a whisper on the ball of the foot. The Signature "
            "method keeps this stance the way a cat keeps its patience - "
            "total, and ready to end in a single motion.",
    },
    {
        "key": "ageuke",
        "name": "Age-uke (Rising Block)",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description":
            "Age-uke, the rising block, is the upward-sweeping forearm block "
            "that meets descending attacks - punches, strikes, and grabs aimed "
            "at the head and face - and carries them up and away. The blocking "
            "forearm starts chambered low across the opposite hip, then rises "
            "in a powerful arc to finish above the forehead with the outer "
            "forearm facing outward and the fist about a fist's width above "
            "the head; the opposite fist pulls to the hip in hikite, driving "
            "torso rotation into the block. Thrown from front stance with a "
            "sharp hip snap, the block intercepts the attack at roughly a "
            "forty-five-degree rising angle and deflects it past the head "
            "rather than stopping it dead.",
        "how_it_works":
            "Stand in zenkutsu-dachi. Chamber the blocking arm low across the "
            "opposite hip, fist closed, palm facing the body, and pull the "
            "other fist to the hip. Drive the blocking forearm upward in a "
            "rising arc, rotating the forearm so the outer edge faces outward "
            "at the finish, and stop with the fist about a fist's width above "
            "the forehead. At the same instant snap the hips and pull the "
            "opposite fist hard to the hip. Meet the incoming attack with the "
            "outer forearm about halfway up the arc, deflecting it upward and "
            "outward past the head - never reach for it; let the attack come "
            "into the rising plane. Freeze an instant at the top with the "
            "shoulder down and the elbow slightly bent, then rechamber along "
            "the same path.",
        "key_points": [
            "Category: blocks - the rising defense against head attacks.",
            "Blocking forearm rises from the opposite hip to above the forehead.",
            "Contact with the outer forearm, about halfway up the rising arc.",
            "Fist finishes about a fist's width above the head.",
            "Hikite and hip snap drive rotation into the block.",
            "Deflects upward and outward; never reaches for the attack.",
        ],
        "requirements": [
            "Front stance base with stable knee and heel.",
            "A partner with focus mitts or a slow incoming strike for timing.",
            "Forearm conditioning built gradually; never block full force early.",
            "Clear overhead space for the rising arc.",
        ],
        "standards": [
            "JKA kihon blocking standards (age-uke).",
            "Shotokan grading syllabus - 9th-8th kyu block requirements.",
        ],
        "citations": [CIT_FUNAKOSHI_KYOHAN, CIT_NAKAYAMA_BEST, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, age-uke is the sunrise drawn with "
            "the forearm: the chamber the night, the rising arc the dawn, and "
            "the fist above the forehead the sun clearing the hill. The "
            "Signature method teaches the block to carry trouble upward, "
            "where it cannot land.",
    },
    {
        "key": "sotouke",
        "name": "Soto-uke (Outside Block)",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description":
            "Soto-uke, the outside block, is the middle-level block that "
            "sweeps from outside to inside across the centerline to deflect "
            "punches aimed at the torso. The blocking arm chambers high by "
            "the ear on the blocking side, then the forearm sweeps down and "
            "across in about a ninety-degree arc, meeting the attack with the "
            "outer forearm at solar-plexus height and finishing with the fist "
            "about a fist's width in front of the opposite shoulder. The "
            "opposite fist pulls to the hip in hikite while the hips rotate "
            "into the block, so the deflection carries the attack across and "
            "away from the body. It is one of the five fundamental blocks of "
            "the basic curriculum and the workhorse middle defense of the "
            "Heian kata.",
        "how_it_works":
            "Stand in zenkutsu-dachi. Chamber the blocking arm up beside the "
            "ear on the blocking side, elbow bent and fist near the head, "
            "palm facing outward; pull the other fist to the hip. Sweep the "
            "blocking forearm down and across the body in a tight arc of "
            "about ninety degrees, rotating the forearm so the outer edge "
            "faces the incoming attack. Meet the punch with the outer forearm "
            "at about solar-plexus height and finish with the blocking fist "
            "about a fist's width in front of the opposite shoulder, elbow "
            "slightly bent and shoulder down. Snap the hips into the motion "
            "and pull hikite hard. The block deflects the attack across the "
            "body and outward - guide it past, do not try to stop it in "
            "place. Rechamber along the same arc.",
        "key_points": [
            "Category: blocks - the outside-to-inside middle defense.",
            "Chambers high beside the ear on the blocking side.",
            "Forearm sweeps about a ninety-degree arc down and across.",
            "Contact with the outer forearm at solar-plexus height.",
            "Finishes a fist's width in front of the opposite shoulder.",
            "Hikite and hip rotation power the deflection across the body.",
        ],
        "requirements": [
            "Front stance base with stable alignment.",
            "A partner throwing slow, straight middle punches for timing.",
            "Gradual forearm conditioning; controlled contact only.",
            "Mirror work to check the arc stays tight to the body.",
        ],
        "standards": [
            "JKA kihon blocking standards (soto-uke).",
            "Shotokan grading syllabus - 9th-8th kyu block requirements.",
        ],
        "citations": [CIT_FUNAKOSHI_KYOHAN, CIT_NAKAYAMA_BEST, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, soto-uke is the gate swinging shut "
            "from the outside: the chamber the gate held open, the sweeping "
            "arc the closing, and the fist before the opposite shoulder the "
            "bar dropped across. The Signature method closes this gate with "
            "the whole hip behind it.",
    },
    {
        "key": "uchiuke",
        "name": "Uchi-uke (Inside Block)",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description":
            "Uchi-uke, the inside block, is the mirror of the outside block: "
            "a middle-level defense that sweeps from inside to outside, "
            "carrying torso punches away from the body. The blocking arm "
            "chambers low across the opposite hip with the palm facing the "
            "body, then the forearm sweeps up and outward in about a "
            "ninety-degree arc, rotating so the inner forearm meets the "
            "attack at solar-plexus height and finishes with the fist about "
            "a fist's width outside the shoulder on the blocking side. Hip "
            "rotation and hikite drive the block, and the deflection pushes "
            "the attack outward past the ribs. Together with the outside "
            "block it gives the practitioner a complete middle defense in "
            "both directions.",
        "how_it_works":
            "Stand in zenkutsu-dachi. Chamber the blocking arm low across the "
            "opposite hip, fist closed with the palm facing the body, and pull "
            "the other fist to the hip. Sweep the blocking forearm up and "
            "outward in an arc of about ninety degrees, rotating the forearm "
            "so the inner edge faces the incoming punch. Meet the attack with "
            "the inner forearm at about solar-plexus height and finish with "
            "the fist about a fist's width outside the shoulder on the "
            "blocking side, elbow slightly bent, shoulder down. Rotate the "
            "hips sharply into the motion and pull hikite to the hip. The "
            "block carries the punch outward and past the ribs - deflect, do "
            "not collide. Return along the same arc to the chamber.",
        "key_points": [
            "Category: blocks - the inside-to-outside middle defense.",
            "Chambers low across the opposite hip, palm facing the body.",
            "Forearm sweeps about a ninety-degree arc up and outward.",
            "Contact with the inner forearm at solar-plexus height.",
            "Finishes a fist's width outside the shoulder, blocking side.",
            "Mirror of the outside block; together they cover both directions.",
        ],
        "requirements": [
            "Front stance base with stable alignment.",
            "A partner throwing slow middle punches for timing practice.",
            "Gradual forearm conditioning; controlled contact only.",
            "Mirror work to verify the chamber and the finishing position.",
        ],
        "standards": [
            "JKA kihon blocking standards (uchi-uke).",
            "Shotokan grading syllabus - 8th-7th kyu block requirements.",
        ],
        "citations": [CIT_FUNAKOSHI_KYOHAN, CIT_NAKAYAMA_BEST, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, uchi-uke is the gate swinging the "
            "other way: chambered low like a held secret, rising to turn the "
            "attack aside with the inside of the arm. The Signature method "
            "pairs it with its mirror twin so no middle attack finds an open "
            "door.",
    },
    {
        "key": "gedanbarai",
        "name": "Gedan-barai (Downward Sweeping Block)",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description":
            "Gedan-barai, the downward sweeping block, is the low defense that "
            "sweeps attacks aimed at the stomach, groin, and legs down and "
            "away. The blocking arm chambers high by the opposite ear, then "
            "the forearm sweeps downward across the body in a broad arc of "
            "about one hundred twenty degrees, meeting the attack with the "
            "outer forearm and finishing low with the fist about a fist's "
            "width above the front knee. Hip rotation and hikite drive the "
            "sweep, and the block's downward angle carries low kicks and "
            "punches into the floor rather than merely stopping them. It "
            "opens the Heian Shodan kata and is the first block most students "
            "ever learn.",
        "how_it_works":
            "Stand in zenkutsu-dachi. Raise the blocking fist to the opposite "
            "ear, elbow bent, with the palm facing outward, and pull the other "
            "fist to the hip. Sweep the blocking arm downward across the body "
            "in a broad arc of about one hundred twenty degrees, rotating the "
            "forearm so the outer edge leads. Meet the low attack with the "
            "outer forearm about halfway down the arc and finish with the "
            "fist about a fist's width above the front knee, arm nearly "
            "straight, shoulder down. Rotate the hips sharply and pull hikite "
            "hard to the hip at the same instant. The sweep deflects the "
            "attack downward and outward, past the leg. Freeze an instant at "
            "the bottom, then rechamber up to the opposite ear along the same "
            "path.",
        "key_points": [
            "Category: blocks - the downward low defense.",
            "Chambers high by the opposite ear.",
            "Forearm sweeps a broad arc of about one hundred twenty degrees.",
            "Contact with the outer forearm, finishing above the front knee.",
            "Hip rotation and hikite drive the downward deflection.",
            "Opens Heian Shodan; the first block most students learn.",
        ],
        "requirements": [
            "Front stance base with the front knee correctly aligned.",
            "A partner throwing slow low strikes or low kicks for timing.",
            "Gradual forearm conditioning; controlled contact only.",
            "Clear space below and across the body for the full sweep.",
        ],
        "standards": [
            "JKA kihon blocking standards (gedan-barai).",
            "Shotokan grading syllabus - 9th kyu block requirements.",
        ],
        "citations": [CIT_FUNAKOSHI_KYOHAN, CIT_NAKAYAMA_BEST, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, gedan-barai is the broom of the "
            "house: raised to the ear like a held breath, swept down in one "
            "honest arc to clear the floor of trouble. The Signature method "
            "sweeps low attacks the way a careful keeper sweeps a threshold "
            "- completely, and without looking down.",
    },
    {
        "key": "shutouchi",
        "name": "Shuto-uchi (Knife-Hand Strike)",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description":
            "Shuto-uchi, the knife-hand strike, is the snapping strike "
            "delivered with the blade of the hand - the hardened outer edge "
            "from the little-finger side of the palm to the wrist. Thrown with "
            "a sharp hip snap and a whipping rotation of the forearm, the "
            "hand travels in a short arc to targets at the temple, the side "
            "of the neck, the ribs, and the collarbone, the fingers held "
            "tight together and the thumb tucked. Because the striking surface "
            "is small and the hand moves fast - a half-kilogram hand at nine "
            "meters per second carries about twenty joules - the strike "
            "concentrates force on a narrow line. It is both a finishing "
            "strike and, reversed, the basis of the knife-hand block.",
        "how_it_works":
            "Stand in zenkutsu-dachi or kokutsu-dachi. Chamber the striking "
            "hand beside the opposite ear with the palm facing outward and "
            "the fingers extended and pressed tightly together, thumb tucked "
            "against the hand. Snap the hips and whip the hand outward and "
            "downward in a short arc toward the target, rotating the forearm "
            "so the blade of the hand - the little-finger edge - leads. "
            "Strike with the hardened edge, keeping the wrist straight and "
            "the fingers rigid, and freeze an instant at contact with the "
            "shoulder down. Pull the opposite hand back to the hip in hikite "
            "as the strike lands. Practice first in the air for the snap, "
            "then on a padded target, checking that the fingers stay together "
            "and the thumb never leads.",
        "key_points": [
            "Category: hand strikes - the blade-of-hand snapping strike.",
            "Strikes with the little-finger edge of the hand, fingers tight, thumb tucked.",
            "Short whipping arc driven by a sharp hip snap.",
            "Targets: temple, side of neck, ribs, collarbone.",
            "Half-kilogram hand at nine meters per second: about twenty joules on a narrow line.",
            "Reversed, the same shape becomes the knife-hand block.",
        ],
        "requirements": [
            "Stable stance base; kokutsu-dachi is the classical home.",
            "Padded targets for contact; never strike hard surfaces with the hand blade early.",
            "Finger and wrist conditioning built gradually.",
            "A partner or mirror to check the arc and the thumb position.",
        ],
        "standards": [
            "JKA kihon striking standards (shuto-uchi).",
            "Shotokan and Shorin-Ryu hand-blade technique standards.",
        ],
        "citations": [CIT_FUNAKOSHI_KYOHAN, CIT_NAKAYAMA_DYNAMIC, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, shuto-uchi is the Signature written "
            "with the edge of the hand: the chamber the raised pen, the hip "
            "snap the flourish, and the blade the ink laid in one line. The "
            "Signature method keeps the fingers together the way a signature "
            "keeps its letters - joined, or it is not one.",
    },
    {
        "key": "maegeri",
        "name": "Mae-geri (Front Kick)",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description":
            "Mae-geri, the front kick, is the first kick of karate and the "
            "foundation of all kicking: a straight thrust delivered with the "
            "ball of the foot. From a fighting stance the knee lifts high - "
            "chambered at about hip height with the foot cocked back - then "
            "the leg snaps straight forward, driving the ball of the foot "
            "into the target at stomach or chest height before rechambering "
            "along the same line and setting the foot down. A leg of about "
            "ninety centimeters gives the kick a reach of nearly a meter from "
            "the hip, and the rechamber is as important as the extension: the "
            "kick goes out and comes back like a piston. It appears in Heian "
            "Nidan, the first kata to include kicks, and in every style from "
            "Shotokan to Kyokushin.",
        "how_it_works":
            "Stand in a fighting stance with hands in guard. Lift the front "
            "knee straight up to about hip height, keeping the supporting leg "
            "slightly bent, and cock the kicking foot back so the toes point "
            "down and the ball of the foot is exposed - this is the chamber. "
            "Snap the lower leg straight forward, driving the ball of the "
            "foot into the target while leaning the torso slightly back for "
            "balance and keeping the hands in guard. Freeze an instant at "
            "full extension with the supporting foot flat. Immediately "
            "rechamber - pull the knee back up along the same line - and set "
            "the foot back down into stance. Practice the chamber slowly "
            "against a wall, then the full kick on a bag or shield, checking "
            "that the foot stays cocked and the kick rechambers every time.",
        "key_points": [
            "Category: kicks - the first and fundamental kick.",
            "Chamber: knee lifted to hip height, foot cocked, toes down.",
            "Strikes with the ball of the foot (koshi).",
            "Leg of ninety centimeters gives nearly a meter of reach.",
            "Rechamber along the same line - the kick is a piston, not a swing.",
            "Hands stay in guard; torso leans slightly back for balance.",
        ],
        "requirements": [
            "Fighting stance with good single-leg balance.",
            "A wall or rail for chamber practice; bag or shield for contact.",
            "Hip flexor and ankle warm-up before kicking.",
            "Clear space ahead; never kick toward people without protection.",
        ],
        "standards": [
            "JKA kihon kicking standards (mae-geri).",
            "Shotokan grading syllabus - 8th-7th kyu kicking requirements.",
        ],
        "citations": [CIT_FUNAKOSHI_KYOHAN, CIT_NAKAYAMA_BEST, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, mae-geri is the piston of the body: "
            "the chamber the drawn breath, the snap the exhaled word, and the "
            "rechamber the promise that every extension returns home. The "
            "Signature method measures a kick not by how far it goes out but "
            "by how honestly it comes back.",
    },
    {
        "key": "kiai",
        "name": "Kiai (Spirit Shout)",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description":
            "Kiai, the spirit shout, is the short, sharp exhalation - voiced "
            "as a shout - released at the instant of a technique's focus. It "
            "is not mere noise: the shout tightens the abdomen, empties the "
            "lungs in a burst of about three to five tenths of a second, and "
            "locks the body into kime exactly as the strike lands. "
            "Traditionally the kiai startles and unbalances the opponent while "
            "focusing the practitioner's own spirit, and kata specify its "
            "placement - Heian Shodan, for example, carries its kiai on the "
            "final techniques. A correct kiai comes from the lower abdomen "
            "(tanden), not the throat, and leaves the body settled rather "
            "than strained.",
        "how_it_works":
            "Stand in front stance and throw a slow straight punch. As the "
            "punch reaches full extension, forcefully exhale from the lower "
            "abdomen in a short burst of about three to five tenths of a "
            "second, voicing it as a sharp shout - the sound should start "
            "deep in the belly, not in the throat. Time the shout so its peak "
            "lands exactly with the punch's kime, the instant of focus; the "
            "abdomen tightens like a drumhead at that moment. Do not hold the "
            "breath before shouting and do not strain the throat - the power "
            "is in the abdominal compression, the voice is its echo. Practice "
            "the kiai with punches, then place it in kata at the traditional "
            "points, keeping the body relaxed immediately after.",
        "key_points": [
            "Category: principles - breath and spirit focused into sound.",
            "Short sharp exhalation of three to five tenths of a second.",
            "Timed exactly with kime, the instant of the technique's focus.",
            "Comes from the lower abdomen (tanden), never from the throat.",
            "Tightens the abdomen and focuses power; traditionally startles the opponent.",
            "Kata specify kiai placement - learn the traditional points.",
        ],
        "requirements": [
            "Relaxed throat and warmed-up voice; never shout through strain.",
            "A technique with clean kime to time the shout against.",
            "Understanding of kata kiai points for the forms practiced.",
            "Consideration for neighbors - kiai is loud by design.",
        ],
        "standards": [
            "JKA kata performance standards (kiai placement).",
            "Shotokan and Goju-Ryu kata conventions.",
        ],
        "citations": [CIT_FUNAKOSHI_WAY, CIT_NAKAYAMA_DYNAMIC, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, kiai is the Signature spoken aloud: "
            "three tenths of a second in which breath, belly, and spirit sign "
            "the technique together. The Signature method treats the shout as "
            "punctuation - it belongs exactly at the end of the sentence, "
            "never in the middle.",
    },
    {
        "key": "ibuki",
        "name": "Ibuki (Power Breathing)",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description":
            "Ibuki is the power-breathing method of Goju-Ryu and related "
            "Okinawan styles: a slow, deep inhalation through the nose of "
            "about four seconds followed by a forceful, audible exhalation "
            "through the mouth of about two seconds, the abdomen and whole "
            "body tensing progressively as the breath leaves. It is the "
            "engine of the Sanchin kata, where every movement rides one "
            "breath cycle, and it trains the practitioner to generate power "
            "from the compressed core rather than from the limbs alone. At "
            "ten breath cycles per minute, a three-minute Sanchin performs "
            "about thirty full ibuki breaths. Beginners learn it standing "
            "still before ever applying it in kata.",
        "how_it_works":
            "Stand in sanchin-dachi or a natural stance with the fists "
            "chambered. Inhale slowly through the nose for about four "
            "seconds, filling the lower abdomen first and letting the breath "
            "rise; keep the shoulders down and the body relaxed. Then exhale "
            "forcefully through the mouth for about two seconds, tensing the "
            "abdomen, the fists, and the whole body progressively harder as "
            "the breath empties - the exhalation is audible, a controlled "
            "rush, not a shout. At the bottom of the breath the body is at "
            "maximum tension for an instant; then release everything and "
            "begin the next inhalation. Practice ten slow cycles standing "
            "still, then link one cycle to each movement of Sanchin, the "
            "tension peaking as each technique completes.",
        "key_points": [
            "Category: principles - the power-breathing engine of Goju-Ryu.",
            "Inhale about four seconds through the nose; exhale about two seconds through the mouth.",
            "Body tenses progressively as the breath empties.",
            "Ten breath cycles per minute; about thirty breaths in a three-minute Sanchin.",
            "The engine of Sanchin kata: one breath cycle per movement.",
            "Learn standing still before applying it in kata.",
        ],
        "requirements": [
            "A quiet space to hear and control the breath.",
            "Sanchin-dachi or a stable natural stance.",
            "No breath-holding to dizziness - stop and breathe normally if light-headed.",
            "A teacher to check that tension releases fully between cycles.",
        ],
        "standards": [
            "Goju-Ryu Sanchin breathing standards.",
            "Okinawan Goju-Ryu grading syllabus - breathing requirements.",
        ],
        "citations": [CIT_HIGAONNA, CIT_OYAMA_ADV],
        "sig_lens":
            "Through the Signature lens, ibuki is the bellows of the forge: "
            "four seconds drawing the fire in, two seconds blasting it into "
            "the steel of the body. The Signature method breathes this way "
            "because power that does not come from the breath is borrowed, "
            "and borrowed power must be returned.",
    },
    {
        "key": "gyakuzuki",
        "name": "Gyaku-zuki (Reverse Punch)",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description":
            "Gyaku-zuki, the reverse punch, is the power punch of karate: the "
            "punch thrown with the hand opposite the forward foot, so the full "
            "rotation of the hips drives behind it. From front stance the rear "
            "fist chambers at the hip, then the hips rotate about forty-five "
            "degrees as the fist drives straight to the target, the body "
            "weight transferring forward onto the front leg and the opposite "
            "fist pulling to the hip in hikite. Because the torso's mass "
            "rotates into the punch, a reverse punch can carry an effective "
            "mass of fifteen kilograms at seven meters per second - on the "
            "order of three hundred seventy joules - several times the energy "
            "of a straight punch thrown without hip rotation. It is the "
            "finishing technique of countless kata and kumite exchanges.",
        "how_it_works":
            "Stand in zenkutsu-dachi with the left foot forward and the right "
            "fist chambered at the right hip, palm up. Drive the right fist "
            "straight toward the target at solar-plexus height while rotating "
            "the hips about forty-five degrees, turning the right hip forward "
            "as the punch extends. Rotate the fist to palm-down at full "
            "extension, keep the wrist straight behind the first two knuckles, "
            "and simultaneously snap the left fist back to the hip in hikite. "
            "Let the weight transfer forward onto the front leg and freeze "
            "the whole body for an instant at impact - kime - with the rear "
            "heel driving into the floor. Rechamber along the same line. "
            "Practice slowly to feel the hip lead the fist, then build speed "
            "on a bag, checking that the punch never outruns the hip.",
        "key_points": [
            "Category: hand strikes - the power punch driven by hip rotation.",
            "Thrown with the hand opposite the forward foot.",
            "Hips rotate about forty-five degrees into the punch.",
            "Effective mass about fifteen kilograms at seven meters per second: roughly three hundred seventy joules.",
            "Hikite and forward weight transfer complete the technique.",
            "The finishing punch of kata and kumite exchanges.",
        ],
        "requirements": [
            "Solid front stance; the rear heel must stay grounded.",
            "Heavy bag or pads for power development.",
            "Hip mobility warm-up; the rotation must not strain the lower back.",
            "A partner or mirror to verify the hip leads the fist.",
        ],
        "standards": [
            "JKA kihon punching standards (gyaku-zuki).",
            "Shotokan grading syllabus - 7th-6th kyu punching requirements.",
        ],
        "citations": [CIT_FUNAKOSHI_KYOHAN, CIT_NAKAYAMA_BEST, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, gyaku-zuki is the Signature's "
            "exclamation: the hip the hand that writes, the rotating torso "
            "the arm behind it, and the fifteen kilograms the ink pressed "
            "into the page. The Signature method never asks the arm to sign "
            "alone - the whole body holds the pen.",
    },
    {
        "key": "oizuki",
        "name": "Oi-zuki (Lunge Punch)",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description":
            "Oi-zuki, the lunge punch, is the advancing punch thrown with the "
            "same-side hand as the forward foot while stepping forward into a "
            "new front stance. The step covers about nine-tenths of a meter - "
            "one full stance length - and the punch lands at the exact instant "
            "the front foot plants, so the body's forward momentum adds to "
            "the punch. Timing is everything: the fist must arrive within "
            "about five hundredths of a second of the foot planting, neither "
            "early (an arm punch) nor late (a pushed punch). It is the "
            "signature technique of Heian Shodan, which opens with three "
            "advancing lunge punches, and the basic tool for closing distance "
            "in kumite.",
        "how_it_works":
            "Stand in zenkutsu-dachi with the left foot forward and the left "
            "fist chambered at the hip. Step the left foot forward about "
            "nine-tenths of a meter into a new front stance while driving the "
            "left fist straight to the target, rotating to palm-down at "
            "extension. Time the punch so it lands within about five "
            "hundredths of a second of the front foot planting - the step and "
            "the strike arrive together. Pull the right fist to the hip in "
            "hikite and freeze an instant at kime with the new stance solid. "
            "Step through and repeat, chaining lunge punches down the floor. "
            "Practice the timing slowly first: foot and fist as one event, "
            "never two.",
        "key_points": [
            "Category: hand strikes - the advancing punch with the step.",
            "Same-side hand as the forward foot; step about nine-tenths of a meter.",
            "Punch lands within five hundredths of a second of the foot planting.",
            "Forward momentum of the step adds to the punch.",
            "Signature technique of Heian Shodan's opening sequence.",
            "Foot and fist arrive as one event, never two.",
        ],
        "requirements": [
            "A clear lane of floor for stepping practice.",
            "Front stance that stays correct while moving.",
            "Targets or a partner at the correct distance for timing.",
            "Ankle and knee warm-up for the stepping impact.",
        ],
        "standards": [
            "JKA kihon punching standards (oi-zuki).",
            "Shotokan grading syllabus - 8th-7th kyu requirements.",
        ],
        "citations": [CIT_FUNAKOSHI_KYOHAN, CIT_NAKAYAMA_BEST, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, oi-zuki is the Signature advancing "
            "across the page: the step the hand moving right, the punch the "
            "pen touching down, and the five-hundredths-of-a-second window "
            "the discipline that keeps the writing legible. The Signature "
            "method advances and signs in a single motion.",
    },
    {
        "key": "uraken",
        "name": "Uraken-uchi (Back-Fist Strike)",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description":
            "Uraken-uchi, the back-fist strike, is the snapping strike "
            "delivered with the back of the fist - the knuckle side - in a "
            "fast whipping arc. From a chamber across the body, the arm "
            "extends and the wrist snaps at the end so the back of the fist "
            "lashes the target, typically the temple, the nose, or the ribs "
            "at close range; the arc covers about one hundred twenty degrees "
            "and the snap, not the arm's push, delivers the force. It is a "
            "close-range, high-speed technique - the strike of Heian Nidan's "
            "famous sequences - and it teaches the practitioner to strike "
            "with relaxation and whip rather than muscle.",
        "how_it_works":
            "Stand in zenkutsu-dachi. Chamber the striking fist across the "
            "body at about chest height on the opposite side, the back of the "
            "fist facing outward. Whip the arm outward in an arc of about one "
            "hundred twenty degrees toward the target, keeping the arm relaxed "
            "until the last instant. At the end of the arc, snap the wrist so "
            "the back of the fist lashes into the target - the knuckles lead "
            "and the wrist stays straight at contact. Freeze an instant, then "
            "snap the fist back along the same arc to the chamber. Practice "
            "the snap slowly in the air, feeling the wrist do the work, then "
            "build speed on a pad, checking that the arm stays relaxed and "
            "the power comes from the whip.",
        "key_points": [
            "Category: hand strikes - the whipping back-fist snap.",
            "Strikes with the back (knuckle side) of the fist.",
            "Arc of about one hundred twenty degrees across the body.",
            "The wrist snap at the end delivers the force, not the arm's push.",
            "Close-range targets: temple, nose, ribs.",
            "Signature strike of Heian Nidan's sequences.",
        ],
        "requirements": [
            "Relaxed shoulders and loose wrist for the whip mechanics.",
            "Pads for contact; the snap can surprise the wrist early.",
            "Front stance or fighting stance base.",
            "A partner to hold targets at correct close range.",
        ],
        "standards": [
            "JKA kihon striking standards (uraken-uchi).",
            "Shotokan grading syllabus - 7th-6th kyu requirements.",
        ],
        "citations": [CIT_FUNAKOSHI_KYOHAN, CIT_NAKAYAMA_BEST, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, uraken is the backhand flourish: "
            "the arm the ribbon, the wrist the flick that cracks it, and the "
            "one-hundred-twenty-degree arc the signature's underline. The "
            "Signature method whips rather than pushes, because ink laid by "
            "a whip dries faster.",
    },
    {
        "key": "mawashigeri",
        "name": "Mawashi-geri (Roundhouse Kick)",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description":
            "Mawashi-geri, the roundhouse kick, is the swinging kick that "
            "travels in a horizontal arc to strike with the instep or the "
            "ball of the foot. The knee lifts and chambers to the side, the "
            "supporting foot pivots about ninety to one hundred eighty "
            "degrees, and the hips turn over completely so the leg swings "
            "through like a bat, the foot traveling an arc of up to one "
            "hundred eighty degrees - a leg of ninety-five centimeters sweeps "
            "nearly one and a half meters of arc. Targets run from the outer "
            "thigh to the ribs to the head. It is the most versatile kick in "
            "kumite and a staple of Kyokushin and full-contact styles, where "
            "its swinging power decides matches.",
        "how_it_works":
            "Stand in a fighting stance. Lift the kicking knee up and to the "
            "side, chambering it across the body at about hip height, while "
            "pivoting on the supporting foot - let the support foot turn "
            "ninety to one hundred eighty degrees so the heel points at the "
            "target. Turn the hips over completely, swinging the lower leg "
            "through in a horizontal arc and extending it to strike with the "
            "instep (or the ball of the foot for penetration). Keep the hands "
            "in guard and lean the torso slightly away for balance. Freeze an "
            "instant at contact, then rechamber the knee along the same arc "
            "and set the foot down. Practice the pivot slowly first - the hip "
            "turnover is the kick - then build the swing on a bag.",
        "key_points": [
            "Category: kicks - the swinging roundhouse arc kick.",
            "Knee chambers to the side; supporting foot pivots ninety to one hundred eighty degrees.",
            "Hips turn over completely; the leg swings like a bat.",
            "Strikes with the instep or the ball of the foot.",
            "Ninety-five-centimeter leg sweeps nearly one and a half meters of arc.",
            "Targets: outer thigh, ribs, head; the versatile kumite kick.",
        ],
        "requirements": [
            "Hip mobility warm-up; the turnover demands open hips.",
            "Heavy bag or shields for the swinging impact.",
            "Good single-leg balance on the supporting foot.",
            "Clear lateral space for the full arc.",
        ],
        "standards": [
            "JKA kihon kicking standards (mawashi-geri).",
            "Kyokushin and Shotokan kumite kicking standards.",
        ],
        "citations": [CIT_NAKAYAMA_DYNAMIC, CIT_OYAMA_THIS, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, mawashi-geri is the Signature's "
            "great sweeping underline: the pivoting foot the compass point, "
            "the turning hip the hand, and the one-and-a-half-meter arc the "
            "flourish that closes the line. The Signature method turns the "
            "hip over completely, because a half-turn writes only half the "
            "word.",
    },
    {
        "key": "yokogeri",
        "name": "Yoko-geri (Side Kick)",
        "group": "Foundations",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description":
            "Yoko-geri, the side kick, is the linear thrusting kick driven "
            "sideways with the edge of the foot (sokuto). The knee chambers "
            "high across the body, the supporting foot pivots a full one "
            "hundred eighty degrees so the heel aims at the target, and the "
            "leg thrusts straight out to the side, the foot bladed with toes "
            "pulled back so the knife-edge strikes. Unlike the roundhouse's "
            "swing, the side kick is a piston: chamber, thrust, rechamber. It "
            "comes in two flavors - keage, the snapping upward version, and "
            "kekomi, the thrusting penetrating version - and it is the "
            "strongest kick in the curriculum for stopping an advancing "
            "opponent, appearing in Heian Nidan and throughout advanced kata.",
        "how_it_works":
            "Stand in a fighting stance. Lift the kicking knee high across "
            "the body, chambering it tight at about hip height, while pivoting "
            "on the supporting foot a full one hundred eighty degrees until "
            "the heel points at the target and the body's side faces the "
            "opponent. Blade the kicking foot - pull the toes back and tense "
            "the edge of the foot (sokuto). Thrust the leg straight out to "
            "the side, driving the heel and the foot's edge into the target "
            "with the leg fully extended and the torso leaning slightly away. "
            "For keage, snap it; for kekomi, drive through. Rechamber the knee "
            "at once and set the foot down. Practice the pivot and chamber "
            "against a wall before thrusting into a shield.",
        "key_points": [
            "Category: kicks - the linear side thrust with the foot's edge.",
            "Strikes with the knife-edge of the foot (sokuto), toes pulled back.",
            "Supporting foot pivots a full one hundred eighty degrees.",
            "Two flavors: keage (snap) and kekomi (thrust).",
            "A piston, not a swing: chamber, thrust, rechamber.",
            "The strongest stop-kick against an advancing opponent.",
        ],
        "requirements": [
            "Strong hip flexors and good single-leg balance.",
            "A wall for pivot-and-chamber practice; shields for thrusting.",
            "Ankle mobility to blade the foot safely.",
            "Clear lateral space; the pivot needs room.",
        ],
        "standards": [
            "JKA kihon kicking standards (yoko-geri keage/kekomi).",
            "Shotokan grading syllabus - 6th-5th kyu kicking requirements.",
        ],
        "citations": [CIT_FUNAKOSHI_KYOHAN, CIT_NAKAYAMA_BEST, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, yoko-geri is the Signature's "
            "straightedge: the pivoting heel the ruler's end, the bladed foot "
            "the drawn line, and the thrust the rule laid down without "
            "deviation. The Signature method thrusts sideways because some "
            "truths can only be written across.",
    },
    {
        "key": "uramawashi",
        "name": "Ura-mawashi-geri (Hook Kick)",
        "group": "Foundations",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description":
            "Ura-mawashi-geri, the hook kick, is the deceptive kick that "
            "swings out past the target and hooks back across it with the "
            "heel. The leg travels outward in a wide arc of about one hundred "
            "thirty-five degrees, passing outside the opponent's guard, then "
            "the knee bends and the heel whips back across the target - "
            "typically the temple or the side of the head - like a hook. The "
            "deception is the technique: the opponent tracks the leg going "
            "wide and misses the return. It demands flexible hips and precise "
            "timing, and it appears in advanced kata and high-level kumite "
            "as the answer to a tight guard.",
        "how_it_works":
            "Stand in a fighting stance. Swing the kicking leg outward in a "
            "wide arc of about one hundred thirty-five degrees, letting it "
            "travel past the outside of the target while pivoting on the "
            "supporting foot. As the leg passes the target line, bend the knee "
            "and whip the heel back across the target in a hooking motion, "
            "striking with the heel or the back of the foot. Keep the motion "
            "continuous - out and back in one flow - with the hands in guard "
            "and the eyes on the target throughout. Rechamber and set the "
            "foot down. Practice the arc slowly in the air to learn the path, "
            "then the hook on a pad held at head height, checking that the "
            "heel, not the toes, leads the return.",
        "key_points": [
            "Category: kicks - the deceptive out-and-back hook.",
            "Leg swings wide in an arc of about one hundred thirty-five degrees.",
            "Heel hooks back across the target: temple or side of head.",
            "The deception is the technique - the guard tracks the wrong motion.",
            "Continuous flow: out and back in one motion.",
            "Demands flexible hips and precise timing.",
        ],
        "requirements": [
            "Advanced hip flexibility; warm up thoroughly.",
            "Pads held at head height for the hooking contact.",
            "Strong supporting-leg balance through the wide arc.",
            "Slow air practice to learn the path before any contact.",
        ],
        "standards": [
            "JKA kihon kicking standards (ura-mawashi-geri).",
            "Shotokan advanced kata and kumite kicking standards.",
        ],
        "citations": [CIT_NAKAYAMA_DYNAMIC, CIT_OYAMA_ADV, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, ura-mawashi is the Signature's "
            "feint: the leg writes wide to draw the eye, and the heel signs "
            "on the return, where no one is looking. The Signature method "
            "teaches that the most honest strike is sometimes the one that "
            "arrives from the direction the reader stopped watching.",
    },
    {
        "key": "ushirogeri",
        "name": "Ushiro-geri (Back Kick)",
        "group": "Foundations",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description":
            "Ushiro-geri, the back kick, is the powerful thrust delivered "
            "backward with the heel after a one-hundred-eighty-degree turn. "
            "The practitioner looks over the shoulder to acquire the target, "
            "pivots the supporting foot, chambers the kicking knee across the "
            "body, and drives the heel straight back into the opponent's "
            "midsection - the body's full turning mass behind a single heel. "
            "It is among the most powerful kicks in karate and the classic "
            "answer to a pursuer, appearing in advanced kata such as Kanku "
            "Dai and in high-level kumite as a counter to aggressive "
            "pressure.",
        "how_it_works":
            "Stand in a fighting stance. Look over the kicking-side shoulder "
            "to acquire the target - never kick blind. Pivot on the supporting "
            "foot and turn the body one hundred eighty degrees, chambering the "
            "kicking knee tightly across the body as you turn. Drive the heel "
            "straight back into the target, extending the leg fully with the "
            "foot bladed and the toes pointing down, the torso leaning "
            "forward over the technique for balance. Freeze an instant at full "
            "extension, then rechamber the knee and turn back to face the "
            "opponent, resetting the guard. Practice the turn and chamber "
            "slowly against a wall, then the thrust into a shield, checking "
            "that the eyes find the target before the leg moves.",
        "key_points": [
            "Category: kicks - the turning backward heel thrust.",
            "Turn one hundred eighty degrees; look over the shoulder first - never kick blind.",
            "Chamber the knee across the body during the turn.",
            "Drive the heel straight back; full turning mass behind one heel.",
            "Among the most powerful kicks in karate.",
            "Classic counter to aggressive forward pressure.",
        ],
        "requirements": [
            "Spacious training area; the turn needs room behind.",
            "Shields or a heavy bag for the powerful thrust.",
            "Strong balance through the pivot; practice the turn slowly first.",
            "A partner to call the target so the eyes learn to acquire it.",
        ],
        "standards": [
            "JKA kihon kicking standards (ushiro-geri).",
            "Shotokan advanced kata (Kanku Dai) kicking standards.",
        ],
        "citations": [CIT_NAKAYAMA_BEST, CIT_OYAMA_ADV, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, ushiro-geri is the Signature written "
            "over the shoulder: the look the reading of the line, the turn "
            "the turning of the page, and the heel the stamp pressed into "
            "what pursued. The Signature method never kicks blind, because a "
            "signature unwitnessed is only a rumor.",
    },
    {
        "key": "hizageri",
        "name": "Hiza-geri (Knee Strike)",
        "group": "Foundations",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description":
            "Hiza-geri, the knee strike, is the close-range weapon that drives "
            "the knee upward into the opponent's thigh, ribs, or head. From "
            "the clinch or close guard the hands pull the opponent down and "
            "in while the hips thrust forward and the knee spears upward - "
            "the knee rising to about one hundred twenty centimeters for a "
            "rib strike - so the opponent's weight meets the rising knee. It "
            "is the infighting technique par excellence, bridging karate's "
            "long-range kicks and its grappling entries, and it appears in "
            "kata bunkai wherever the embusen brings the practitioner chest "
            "to chest with the imagined opponent.",
        "how_it_works":
            "From a close fighting stance or clinch, grip the opponent's head, "
            "neck, or shoulders - in solo practice, imagine pulling a heavy "
            "bag down. Pull sharply downward and inward with the hands while "
            "thrusting the hips forward and driving the knee straight up "
            "toward the target: thigh, ribs at about one hundred twenty "
            "centimeters, or, with a jump or a bent opponent, the head. Keep "
            "the supporting leg slightly bent and the torso upright; the power "
            "comes from the hip thrust and the downward pull meeting, not "
            "from swinging the lower leg. Set the foot back down into stance "
            "at once. Practice on a heavy bag or shield held at rib height, "
            "checking that the hands pull as the knee rises - the two motions "
            "are one.",
        "key_points": [
            "Category: kicks - the close-range rising knee.",
            "Hands pull the opponent down as the knee drives up; the two motions are one.",
            "Knee rises to about one hundred twenty centimeters for a rib strike.",
            "Power from hip thrust and downward pull, not leg swing.",
            "The infighting bridge between long kicks and grappling entries.",
            "Appears in kata bunkai at chest-to-chest range.",
        ],
        "requirements": [
            "A heavy bag or a partner with a body shield.",
            "Close-range comfort; practice the pull-and-drive slowly first.",
            "Hip flexor warm-up; the drive is explosive.",
            "Mouthguard and control when practicing with a partner.",
        ],
        "standards": [
            "JKA kumite infighting standards.",
            "Kyokushin and Shotokan close-range technique standards.",
        ],
        "citations": [CIT_OYAMA_THIS, CIT_NAKAYAMA_DYNAMIC, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, hiza-geri is the Signature's "
            "rising period: the hands the sentence pulled down to meet it, "
            "the knee the dot driven up from below. The Signature method "
            "fights close the way it writes close - with the whole body "
            "leaning into the mark.",
    },
    {
        "key": "shutouke",
        "name": "Shuto-uke (Knife-Hand Block)",
        "group": "Foundations",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description":
            "Shuto-uke, the knife-hand block, is the elegant open-hand defense "
            "thrown from back stance against middle and high attacks. The "
            "hands cross in front of the chest - the blocking hand open with "
            "fingers extended, the supporting hand chambered - then they open "
            "outward like a fan: the blocking knife-hand sweeps to about "
            "shoulder height at a sixty-degree angle while the other hand "
            "pulls back to guard the ribs. The block meets the attack with "
            "the blade of the hand and forearm, deflecting it outward, and "
            "the open hand is instantly ready to grab, strike, or counter. It "
            "is the signature technique of the Heian kata's turning sequences "
            "and the hallmark of the back stance.",
        "how_it_works":
            "Stand in kokutsu-dachi. Cross both hands in front of the chest: "
            "the blocking hand open, fingers extended and thumb tucked, palm "
            "facing the chest; the other hand chambered beneath it. In one "
            "motion, sweep the blocking hand outward and slightly upward to "
            "about shoulder height, rotating so the blade of the hand faces "
            "the incoming attack, while the other hand pulls back to the ribs "
            "in guard. The hands open like a fan to about a sixty-degree "
            "spread. Meet the attack with the blade of the hand and outer "
            "forearm, deflecting it outward past the shoulder, and freeze an "
            "instant with the blocking arm slightly bent. The open blocking "
            "hand stays live - ready to grab or strike. Return through the "
            "chest cross to the chamber.",
        "key_points": [
            "Category: blocks - the open-hand fan defense from back stance.",
            "Hands cross at the chest, then open like a fan to sixty degrees.",
            "Blocking hand finishes at about shoulder height, blade outward.",
            "Meets the attack with the blade of the hand and outer forearm.",
            "The open hand stays live: ready to grab, strike, or counter.",
            "Signature technique of the Heian turning sequences.",
        ],
        "requirements": [
            "Back stance base with correct seventy-thirty weight.",
            "A partner throwing middle punches for timing.",
            "Open-hand conditioning; fingers extended but not rigid.",
            "Mirror work to check the chest cross and the fan opening.",
        ],
        "standards": [
            "JKA kihon blocking standards (shuto-uke).",
            "Shotokan grading syllabus - 7th-6th kyu block requirements.",
        ],
        "citations": [CIT_FUNAKOSHI_KYOHAN, CIT_NAKAYAMA_BEST, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, shuto-uke is the opening fan: the "
            "chest cross the fan folded, the sixty-degree spread the fan "
            "opened, and the live open hand the page still blank behind it. "
            "The Signature method blocks with an open hand because a closed "
            "fist has already decided what comes next, and the Signature "
            "prefers to keep its options.",
    },
    {
        "key": "moroteuke",
        "name": "Morote-uke (Augmented Block)",
        "group": "Foundations",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description":
            "Morote-uke, the augmented block, is the reinforced inside block "
            "in which the second fist braces behind the blocking forearm at "
            "the elbow, adding the second arm's mass and structure to the "
            "defense. Thrown from front stance against a strong middle attack, "
            "the primary arm performs the inside-block sweep while the "
            "supporting fist drives in behind the elbow - the reinforcement "
            "adds roughly forty percent more structural resistance, turning "
            "a deflection into a wall. It teaches the compounded lesson that "
            "two limbs working as one structure outperform two limbs working "
            "as two techniques, and it appears in Heian Sandan and in "
            "advanced kumite against committed attacks.",
        "how_it_works":
            "Stand in zenkutsu-dachi. Chamber the primary arm low across the "
            "opposite hip as for the inside block, and chamber the supporting "
            "fist at the opposite hip. Sweep the primary forearm up and "
            "outward in the inside-block arc while driving the supporting fist "
            "in behind the primary elbow, the supporting forearm bracing the "
            "block like a strut. Both arms arrive together: the primary "
            "forearm meets the attack at solar-plexus height while the support "
            "locks behind the elbow. Rotate the hips into the motion and "
            "freeze an instant with the reinforced structure solid. The block "
            "stops or heavily deflects the attack rather than merely guiding "
            "it. Rechamber both arms along their paths.",
        "key_points": [
            "Category: blocks - the reinforced two-arm defense.",
            "Primary arm sweeps the inside-block arc; supporting fist braces behind the elbow.",
            "Reinforcement adds about forty percent more structural resistance.",
            "Both arms arrive together as one structure, not two techniques.",
            "Thrown from front stance against strong committed attacks.",
            "Appears in Heian Sandan and advanced kumite.",
        ],
        "requirements": [
            "Solid inside block mechanics learned first.",
            "A partner throwing committed middle attacks for pressure testing.",
            "Forearm and elbow conditioning; the brace loads the joint.",
            "Control: the reinforced block hits hard - pad the contact.",
        ],
        "standards": [
            "JKA kihon blocking standards (morote-uke).",
            "Shotokan grading syllabus - 6th-5th kyu block requirements.",
        ],
        "citations": [CIT_FUNAKOSHI_KYOHAN, CIT_NAKAYAMA_BEST, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, morote-uke is the Signature with a "
            "witness: one arm writes the block, the second stands behind it "
            "and swears to it, and the forty percent is the weight a second "
            "voice gives a testimony. The Signature method reinforces because "
            "some attacks deserve more than one answer.",
    },
    {
        "key": "heianshodan",
        "name": "Heian Shodan (First Peaceful Mind Kata)",
        "group": "Foundations",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description":
            "Heian Shodan, the first kata of the Heian (Pinan) series, is the "
            "gateway form of Shotokan and Shorin-Ryu karate, created by the "
            "Okinawan master Anko Itosu as the entry to the five Peaceful "
            "Mind forms. Its twenty-one movements walk a straight I-shaped "
            "embusen - the floor pattern - through downward blocks, lunge "
            "punches, rising blocks, and the kata's closing hammer-fist "
            "strikes, each technique thrown with full kime and a kiai on the "
            "final movements. Performed at about two seconds per movement, "
            "the kata runs roughly forty-five seconds and teaches the "
            "beginner to link stance, block, and punch into continuous "
            "motion. Every black belt in these styles has walked this line "
            "thousands of times.",
        "how_it_works":
            "Begin in yoi (ready stance), feet together, fists at the thighs. "
            "Step left into front stance with a downward block, then advance "
            "with three lunge punches down the center line. Turn and repeat "
            "the block-and-punch sequences to both sides, keeping every stance "
            "deep and every technique at full extension with kime. Perform "
            "the rising-block section with sharp hip rotation, then the "
            "closing sequence with hammer-fist strikes, placing the kiai on "
            "the traditional final techniques. Walk the I-shaped embusen "
            "without drifting: each turn pivots on the ball of the foot and "
            "lands in a correct stance. Breathe naturally, one breath per "
            "technique, and finish by returning to yoi. Practice the kata in "
            "sections first, then as one continuous forty-five-second form.",
        "key_points": [
            "Category: kata - the gateway form of the Heian series.",
            "Twenty-one movements on an I-shaped embusen (floor pattern).",
            "Created by Anko Itosu as the entry to the five Peaceful Mind forms.",
            "Techniques: downward blocks, lunge punches, rising blocks, hammer-fists.",
            "About two seconds per movement: roughly forty-five seconds total.",
            "Kiai on the traditional final techniques.",
        ],
        "requirements": [
            "All five basic blocks and the lunge punch learned first.",
            "A clear floor lane for the I-shaped embusen.",
            "Knowledge of the traditional kiai points.",
            "A teacher to correct the turns and stance depths.",
        ],
        "standards": [
            "JKA kata standards (Heian Shodan).",
            "Shotokan grading syllabus - 8th-7th kyu kata requirement.",
        ],
        "citations": [CIT_FUNAKOSHI_KYOHAN, CIT_NAKAYAMA_BEST, CIT_PFLUGER, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, Heian Shodan is the first chapter of "
            "the archive: twenty-one movements the first twenty-one sentences, "
            "the I-shaped embusen the ruled line they are written on. The "
            "Signature method walks this line thousands of times because the "
            "first chapter must be the most honest.",
    },
    {
        "key": "heiannidan",
        "name": "Heian Nidan (Second Peaceful Mind Kata)",
        "group": "Foundations",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description":
            "Heian Nidan, the second kata of the Heian series, is the form "
            "that introduces kicks and back-fist strikes to the student's "
            "repertoire. Its twenty-six movements add the front kick and the "
            "side snap kick to the blocking and punching vocabulary of Heian "
            "Shodan, alongside the kata's famous back-fist and hammer-fist "
            "combinations thrown from back stance and front stance. The "
            "embusen turns more sharply than the first kata's, demanding "
            "clean pivots and instant stance changes between the kicks. It "
            "teaches the compounded skill of mixing hand and foot techniques "
            "in continuous flow - the moment the student's karate gains its "
            "second dimension.",
        "how_it_works":
            "Begin in yoi. Open with the kata's signature back-stance "
            "sequences: knife-hand blocks and back-fist strikes with sharp "
            "hip rotation. When the kata calls for the front kick, chamber "
            "the knee high from back stance, snap the kick with the ball of "
            "the foot, rechamber, and set the foot down into a correct stance "
            "without hopping. Perform the side snap kick (yoko-geri keage) "
            "with a full supporting-foot pivot. Keep the embusen's sharper "
            "turns clean: pivot on the ball of the foot and land each stance "
            "at full depth. Place the kiai at the traditional points and "
            "finish at yoi. Practice the kick sections separately until the "
            "chamber-to-stance landing is silent, then run the full "
            "twenty-six-movement form.",
        "key_points": [
            "Category: kata - the second Heian form; kicks enter the curriculum.",
            "Twenty-six movements with sharper embusen turns.",
            "First kata to include kicks: front kick and side snap kick.",
            "Signature back-fist and hammer-fist combinations.",
            "Teaches mixing hand and foot techniques in continuous flow.",
            "Chamber-to-stance landings must be silent and stable.",
        ],
        "requirements": [
            "Heian Shodan performed cleanly first.",
            "Front kick and side snap kick mechanics learned in kihon.",
            "A clear floor lane for the turning embusen.",
            "Knowledge of the traditional kiai points.",
        ],
        "standards": [
            "JKA kata standards (Heian Nidan).",
            "Shotokan grading syllabus - 7th-6th kyu kata requirement.",
        ],
        "citations": [CIT_FUNAKOSHI_KYOHAN, CIT_NAKAYAMA_BEST, CIT_PFLUGER, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, Heian Nidan is the second chapter, "
            "where the archive learns to write with its feet: twenty-six "
            "sentences, and for the first time the pen leaves the desk. The "
            "Signature method marks this kata as the moment the student's "
            "handwriting gains its second dimension.",
    },
    {
        "key": "tekkishodan",
        "name": "Tekki Shodan (First Iron Horse Kata)",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description":
            "Tekki Shodan, the first Iron Horse kata - known as Naihanchi "
            "Shodan in Okinawan lineages - is the kata performed entirely in "
            "horse stance along a single straight line. The practitioner "
            "never steps forward or back: the embusen is one lateral line, "
            "and all power comes from hip vibration, stance-rooted rotation, "
            "and the crossing-step footwork unique to the form. Its close-"
            "range elbow strikes, back-fists, and reinforced blocks teach "
            "fighting with the back against a wall - legend says the kata was "
            "designed for combat on a narrow bridge or between rice-paddy "
            "ridges. It is the advanced student's school of hip power and "
            "the signature kata of the horse stance.",
        "how_it_works":
            "Begin in yoi, then step into kiba-dachi facing sideways to the "
            "embusen line. Perform the opening reinforced blocks with a sharp "
            "vibration of the hips - the power comes from the hip snap, not "
            "the arms. Execute the kata's crossing steps (kosa-dachi "
            "transitions) by bringing one foot across the other without rising "
            "up, staying low in horse stance throughout. Throw the elbow "
            "strikes by driving the hip into each one, keeping the back "
            "straight and the stance rooted. Never step off the single "
            "straight line: every technique faces sideways along the embusen. "
            "Place the kiai at the traditional points and finish in "
            "kiba-dachi. Practice the hip vibration slowly first - the whole "
            "kata is a study in generating power without stepping.",
        "key_points": [
            "Category: kata - the horse-stance line kata (Naihanchi Shodan).",
            "Entire kata in kiba-dachi on a single straight lateral line.",
            "Power from hip vibration and rooted rotation, never from stepping.",
            "Close-range elbow strikes, back-fists, reinforced blocks.",
            "Crossing-step footwork (kosa-dachi transitions) without rising.",
            "Legend: designed for fighting on a narrow bridge or paddy ridge.",
        ],
        "requirements": [
            "Deep, stable horse stance held comfortably.",
            "Understanding of hip vibration mechanics.",
            "A straight floor line to train the lateral embusen.",
            "Teacher guidance for the crossing steps and elbow mechanics.",
        ],
        "standards": [
            "JKA kata standards (Tekki Shodan).",
            "Shotokan grading syllabus - 5th-4th kyu kata requirement.",
        ],
        "citations": [CIT_FUNAKOSHI_KYOHAN, CIT_NAKAYAMA_BEST, CIT_PFLUGER, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, Tekki Shodan is the Signature "
            "written on a tightrope: one straight line, no forward step, and "
            "all the ink squeezed from the hips. The Signature method keeps "
            "this kata as proof that power is not travel - it is the ground, "
            "refusing to move, speaking through the body.",
    },
    {
        "key": "hangetsu",
        "name": "Hangetsu (Half Moon Kata)",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description":
            "Hangetsu, the Half Moon kata - Seisan in Okinawan lineages - is "
            "the form of slow breathing and sudden explosion. Its forty-one "
            "movements alternate between slow, tension-filled sequences "
            "performed with deep ibuki breathing in the half-moon stance and "
            "fast, explosive combinations thrown at full speed: roughly half "
            "the kata is slow and half is fast, and the contrast is the "
            "lesson. The slow sections build the rooted, pressurized body of "
            "Sanchin-like training; the fast sections release it. The kata "
            "runs about one hundred forty seconds - twenty slow movements at "
            "six seconds each plus twenty-one fast movements at one second "
            "each - and teaches the "
            "advanced student to shift gears between stillness and violence "
            "without losing the center.",
        "how_it_works":
            "Begin in yoi. For the slow sections, sink into hangetsu-dachi "
            "(half-moon stance), breathe with deep ibuki - four seconds in, "
            "two seconds out - and move with progressive full-body tension, "
            "each technique pressurized like Sanchin. For the fast sections, "
            "release everything: explode through the combinations at full "
            "speed with sharp kime, then settle instantly back into the slow "
            "breathing. The transitions are the technique - never let a fast "
            "section bleed tension into a slow one or vice versa. Walk the "
            "kata's embusen with the half-moon footwork, place the kiai at "
            "the traditional points, and finish at yoi. Practice the slow "
            "half and the fast half separately before joining them.",
        "key_points": [
            "Category: kata - the slow-fast contrast form (Seisan lineage).",
            "Forty-one movements: roughly half slow, half fast.",
            "Slow sections use deep ibuki breathing with full-body tension.",
            "Fast sections explode at full speed with sharp kime.",
            "The transitions between gears are the technique.",
            "Twenty slow movements at six seconds plus twenty-one fast at one second: about one hundred forty seconds total.",
            "Teaches stillness-to-violence shifting.",
        ],
        "requirements": [
            "Ibuki breathing learned and practiced.",
            "Hangetsu-dachi (half-moon stance) stability.",
            "Stamina for the slow tension sections; they are exhausting.",
            "A teacher to judge the slow-fast contrast honestly.",
        ],
        "standards": [
            "JKA kata standards (Hangetsu).",
            "Shotokan grading syllabus - 4th-3rd kyu kata requirement.",
        ],
        "citations": [CIT_FUNAKOSHI_KYOHAN, CIT_NAKAYAMA_BEST, CIT_PFLUGER, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, Hangetsu is the Signature written in "
            "two inks: the slow half in heavy black, pressed deep, and the "
            "fast half in a slash of red. The Signature method changes gears "
            "the way the moon changes phase - completely, and without "
            "apology.",
    },
    {
        "key": "bunkai",
        "name": "Bunkai (Kata Application Analysis)",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description":
            "Bunkai is the analysis and practical application of kata "
            "movements - the process of taking each formal movement and "
            "discovering the throws, locks, strikes, and escapes hidden "
            "inside it. Every kata movement carries at least one application, "
            "and a twenty-one-movement kata like Heian Shodan yields "
            "twenty-one or more practical techniques once bunkai is applied. "
            "The study proceeds in three levels: kihon bunkai (the basic, "
            "literal application), oyo bunkai (applied variations against "
            "realistic attacks), and the deeper ura (hidden) readings that "
            "reveal grappling and vital-point work inside seemingly simple "
            "blocks. Bunkai is what turns kata from dance back into combat "
            "science.",
        "how_it_works":
            "Take one kata movement - for example, the downward block that "
            "opens Heian Shodan. First, perform the kihon bunkai: have a "
            "partner throw the literal attack (a front kick) and apply the "
            "block exactly as the kata shows, then follow with the kata's "
            "own counter. Second, develop oyo bunkai: vary the attack (a "
            "grab, a punch) and find how the same movement answers it, "
            "keeping the kata's body mechanics honest. Third, study the ura "
            "reading: the chamber becomes a grab, the block a throw or lock. "
            "Practice each application slowly with a compliant partner, then "
            "at realistic speed with protective equipment, always checking "
            "that the application uses the kata's exact stance, hip motion, "
            "and timing - if it does not, it is not that kata's bunkai.",
        "key_points": [
            "Category: principles - the combat science hidden inside kata.",
            "Every kata movement carries at least one practical application.",
            "Three levels: kihon bunkai, oyo bunkai, and ura (hidden) readings.",
            "A twenty-one-movement kata yields twenty-one or more techniques.",
            "Applications must use the kata's exact stance, hip motion, and timing.",
            "Turns kata from formal exercise back into combat science.",
        ],
        "requirements": [
            "The kata itself performed correctly first - bunkai without kata is invention.",
            "A trained, compliant partner for application practice.",
            "Protective equipment for realistic-speed work.",
            "A teacher to verify the ura readings against the tradition.",
        ],
        "standards": [
            "JKA kata application (bunkai) standards.",
            "Shotokan and Goju-Ryu bunkai conventions.",
        ],
        "citations": [CIT_FUNAKOSHI_KYOHAN, CIT_NAKAYAMA_BEST, CIT_HIGAONNA, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, bunkai is the reading of the "
            "archive: every kata movement a sealed letter, every application "
            "the letter opened. The Signature method insists the reading use "
            "the kata's exact handwriting - stance, hip, and timing - or it "
            "is not a reading at all, only a guess.",
    },
    {
        "key": "kumite",
        "name": "Kumite (Sparring Method)",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description":
            "Kumite, sparring, is the living laboratory of karate: the "
            "structured progression from prearranged drills to free fighting. "
            "The ladder runs kihon ippon kumite (one-step sparring: one "
            "announced attack, one defense and counter), sanbon kumite "
            "(three-step), jiyu ippon kumite (semi-free one-step), and finally "
            "jiyu kumite (free sparring). At every level the governing "
            "concepts are ma-ai - the engagement distance, roughly one arm's "
            "reach plus one step, about one and six-tenths meters - and "
            "control: techniques stop at the target's surface in traditional "
            "sparring, proving speed and accuracy without injury. Kumite is "
            "where stance, strike, block, and kata bunkai are tested against "
            "a resisting partner.",
        "how_it_works":
            "Begin with kihon ippon kumite: face a partner at ma-ai, about "
            "one and six-tenths meters apart. The attacker announces a "
            "target (for example, a head punch) and attacks once at full "
            "speed; the defender blocks and counters once, both freezing at "
            "kime with full control - the technique stops at the surface. "
            "Alternate roles and repeat for all basic attacks. Progress to "
            "sanbon (three attacks), then jiyu ippon (unannounced single "
            "attacks), and only then to jiyu kumite: free sparring with "
            "continuous movement, feints, and combinations, still with "
            "complete control. At every level, maintain ma-ai, keep the "
            "guard, and stop every technique - control is the technique. "
            "Wear a mouthguard and, for free sparring, approved mitts and "
            "body protection, under a teacher's supervision.",
        "key_points": [
            "Category: principles - the structured path from drills to free sparring.",
            "Progression: kihon ippon, sanbon, jiyu ippon, jiyu kumite.",
            "Ma-ai: the engagement distance, about one and six-tenths meters.",
            "Control: techniques stop at the target's surface in traditional sparring.",
            "Tests stance, strike, block, and bunkai against a resisting partner.",
            "Protective equipment and teacher supervision for free sparring.",
        ],
        "requirements": [
            "All basic attacks, blocks, and counters learned in kihon first.",
            "Mouthguard; mitts and body protection for free sparring.",
            "A trained partner and a supervising teacher.",
            "The discipline of control: never sacrifice it for speed.",
        ],
        "standards": [
            "JKA kumite progression and safety standards.",
            "Shotokan and Kyokushin sparring conventions.",
        ],
        "citations": [CIT_NAKAYAMA_DYNAMIC, CIT_OYAMA_THIS, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, kumite is the Signature tested: the "
            "drills the practice signatures, ma-ai the margin of the page, "
            "control the proof that the hand is master of the pen. The "
            "Signature method spars to verify the archive, never to deface "
            "it.",
    },
    {
        "key": "taisabaki",
        "name": "Tai-sabaki (Body Shifting)",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description":
            "Tai-sabaki, body shifting, is the art of moving the body off the "
            "line of attack instead of meeting force with force. Rather than "
            "blocking a committed strike head-on, the practitioner pivots or "
            "steps the body thirty to forty-five degrees offline - a step of "
            "nine-tenths of a meter at forty-five degrees carries the body "
            "about sixty-four centimeters sideways, completely clear of a "
            "straight attack - while the hands guide, unbalance, or counter "
            "the attacker. It is the evasive heart of advanced kumite and "
            "kata bunkai, appearing wherever a kata turn implies slipping an "
            "attack, and it teaches the strategic lesson that the best block "
            "is not being where the attack lands.",
        "how_it_works":
            "Have a partner throw a slow straight punch at your chest. As the "
            "punch comes, pivot on the balls of your feet and shift your body "
            "thirty to forty-five degrees offline - step the front foot to "
            "the side or pivot the stance so your centerline leaves the "
            "attack's path. Let your lead hand lightly guide the punching arm "
            "past while your body is already gone; the evasion, not the hand, "
            "does the work. Immediately counter from the new angle - the "
            "attacker's flank is now open. Practice both directions, then "
            "with gradually faster attacks, checking that the head stays "
            "level and the stance stays rooted through the shift. Drill the "
            "forty-five-degree pivot until the body moves before the mind "
            "decides.",
        "key_points": [
            "Category: principles - evasive body movement off the attack line.",
            "Shift thirty to forty-five degrees offline instead of blocking head-on.",
            "A nine-tenths-meter step at forty-five degrees moves the body sixty-four centimeters sideways.",
            "Hands guide or unbalance; the evasion does the work.",
            "The evasive heart of advanced kumite and kata bunkai.",
            "The best block is not being where the attack lands.",
        ],
        "requirements": [
            "Solid stances that stay rooted through pivots.",
            "A partner throwing slow, committed straight attacks.",
            "Open floor space in all directions for the shifts.",
            "Patience: the pivot must precede the decision, through drilling.",
        ],
        "standards": [
            "JKA advanced kumite movement standards.",
            "Shotokan and Goju-Ryu tai-sabaki conventions.",
        ],
        "citations": [CIT_NAKAYAMA_DYNAMIC, CIT_FUNAKOSHI_KYOHAN, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, tai-sabaki is the Signature stepping "
            "aside: the attack writes its line, and the body simply declines "
            "to be the paper. The Signature method teaches the forty-five-"
            "degree pivot as the politest refusal in combat - complete, "
            "silent, and already countering.",
    },
    {
        "key": "atemi",
        "name": "Atemi Waza (Vital-Point Striking Principles)",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description":
            "Atemi waza is the traditional body of knowledge concerning "
            "striking the body's vulnerable points - the targets catalogued "
            "across centuries of Okinawan and Japanese martial study and "
            "preserved inside kata. The classical target map covers about a "
            "dozen primary zones: the temple, the jaw hinge, the nose, the "
            "side of the neck, the collarbone, the solar plexus, the "
            "floating ribs, the groin, the inner thigh, the knee, the instep, "
            "and the back of the hand. Traditional instruction pairs this "
            "map with strict training ethics: vital-point study is practiced "
            "on pads and dummies, with controlled touch-only contact on "
            "partners, under a qualified teacher. This record teaches the "
            "map and the mechanics as civilian martial-arts knowledge - how "
            "the techniques work and how they are trained safely - which is "
            "how the tradition itself transmits it.",
        "how_it_works":
            "Learn the target map first on a training dummy or chart: temple, "
            "jaw hinge, nose, side of neck, collarbone, solar plexus, "
            "floating ribs, groin, inner thigh, knee, instep, back of hand - "
            "about a dozen primary zones. For each zone, learn which "
            "technique the kata prescribes (knife-hand to the neck, "
            "back-fist to the temple, knee to the ribs) and practice the "
            "mechanics on a pad: correct angle, correct striking surface, "
            "full hip rotation, instant kime. With a partner, practice "
            "touch-only - the technique stops at the surface with zero "
            "penetration - and only under a qualified teacher's supervision. "
            "Study the kata bunkai that encodes each target so the knowledge "
            "stays connected to the forms. Never practice vital-point contact "
            "at power on a person; the tradition's safety rules are part of "
            "the technique.",
        "key_points": [
            "Category: principles - the classical target map of Okinawan and Japanese karate.",
            "About a dozen primary zones: temple, jaw, nose, neck, collarbone, solar plexus, ribs, groin, thigh, knee, instep, hand.",
            "Each zone pairs with the technique the kata prescribes.",
            "Train mechanics on pads and dummies; touch-only with partners.",
            "Strict training ethics under a qualified teacher are part of the art.",
            "Civilian martial-arts knowledge: how the techniques work and how they are trained safely.",
        ],
        "requirements": [
            "A qualified teacher - this material is never self-taught.",
            "Training dummies, pads, and charts for the target map.",
            "Absolute control: touch-only contact with partners, never power.",
            "Maturity and training ethics; the knowledge carries responsibility.",
        ],
        "standards": [
            "Okinawan karate kyusho study conventions.",
            "JKA and Goju-Ryu advanced curriculum safety standards.",
        ],
        "citations": [CIT_HIGAONNA, CIT_FUNAKOSHI_KYOHAN, CIT_OYAMA_ADV],
        "sig_lens":
            "Through the Signature lens, atemi waza is the index of the "
            "archive: a dozen entries, each cross-referenced to its kata, "
            "each handled with the care an archivist gives fragile pages. "
            "The Signature method studies the map completely and touches it "
            "lightly, because a signature that harms the paper is forgery, "
            "not writing.",
    },
    {
        "key": "sanchin",
        "name": "Sanchin (Three Battles Kata)",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description":
            "Sanchin, the Three Battles kata - the battle of mind, body, and "
            "breath - is the foundation form of Goju-Ryu and one of the "
            "oldest kata in karate, rooted in Fujian Chinese boxing. "
            "Performed in sanchin-dachi with deep ibuki breathing and "
            "progressive full-body tension, every movement is a study in "
            "rooted power: the practitioner advances slowly, tensing harder "
            "with each exhalation, while a teacher traditionally tests the "
            "structure with strikes and pushes (shime). A full performance "
            "runs about three minutes and contains about thirty breath "
            "cycles - ten per minute at four seconds in and two seconds out. "
            "Masters call it the kata that builds the body all other kata "
            "are performed with.",
        "how_it_works":
            "Stand in sanchin-dachi: feet in the hourglass stance, knees "
            "bent and pressed inward, fists chambered. Begin the ibuki cycle: "
            "inhale four seconds through the nose, then step and thrust "
            "forward while exhaling two seconds through the mouth, tensing "
            "the abdomen, fists, and whole body progressively harder as the "
            "breath empties. Each movement rides exactly one breath cycle; "
            "at the bottom of each exhalation the body is at maximum tension "
            "for an instant, then releases into the next inhalation. Advance "
            "step by step down the floor, keeping the stance low and the "
            "spine straight, for about three minutes and thirty breath "
            "cycles. Under a teacher, receive shime - testing strikes to the "
            "shoulders, abdomen, and legs - to verify the tension is real. "
            "Finish by releasing all tension and breathing normally.",
        "key_points": [
            "Category: kata - the Goju-Ryu foundation form of breath and tension.",
            "The Three Battles: mind, body, and breath.",
            "Sanchin-dachi with ibuki breathing: four seconds in, two seconds out.",
            "About thirty breath cycles in a three-minute performance.",
            "Progressive full-body tension peaking at each exhalation's end.",
            "Shime: the teacher tests the structure with strikes and pushes.",
        ],
        "requirements": [
            "Ibuki breathing practiced until natural.",
            "Sanchin-dachi held comfortably at depth.",
            "A qualified Goju-Ryu teacher - shime is never self-administered.",
            "Cardiovascular readiness; the tension work is demanding.",
        ],
        "standards": [
            "Goju-Ryu Sanchin performance and shime standards.",
            "Okinawan Goju-Ryu grading syllabus.",
        ],
        "citations": [CIT_HIGAONNA, CIT_OYAMA_ADV],
        "sig_lens":
            "Through the Signature lens, Sanchin is the Signature pressed in "
            "wet concrete: three minutes, thirty breaths, and the whole body "
            "the stamp. The Signature method keeps this kata as the proof "
            "that the archive is written not on paper but in the practitioner's "
            "own flesh - mind, body, and breath signing as one.",
    },
    {
        "key": "kankudai",
        "name": "Kanku Dai (Viewing the Sky Kata)",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description":
            "Kanku Dai, the great Viewing the Sky kata - Kusanku Dai in "
            "Okinawan lineages, named for the Chinese envoy Kusanku - is the "
            "longest and most comprehensive kata of the Shotokan curriculum "
            "and the summit of this ladder. Its sixty-five movements open "
            "with the practitioner gazing skyward, hands rising to part the "
            "clouds, and unfold across every technique family: knife-hand "
            "blocks, double punches (yama-zuki), kicks including the back "
            "kick, the kata's famous jump, and slow tension sequences that "
            "echo Sanchin. At about one and a half seconds per movement the "
            "form runs roughly one hundred seconds of continuous, varied "
            "combat study. Funakoshi called it his favorite kata; it contains, "
            "in one form, nearly the entire art.",
        "how_it_works":
            "Begin in yoi, then open the kata by looking skyward and raising "
            "both hands slowly overhead as if parting clouds - the signature "
            "opening. Move through the form's sections: the slow tension "
            "sequences with deep breathing, the knife-hand block series in "
            "back stance with sharp turns, the double-punch (yama-zuki) "
            "thrusts in front stance, the kicking section including the back "
            "kick with its one-hundred-eighty-degree turn, and the jump - "
            "spring from a crouch, tuck the knees, and land silently in a "
            "correct stance. Keep every embusen line true and every stance at "
            "full depth across all sixty-five movements; the kata punishes "
            "fatigue with sloppy stances, so pace the breathing. Place the "
            "two kiai at the traditional points and finish at yoi. Learn the "
            "kata in four sections before joining them into the full "
            "hundred-second form.",
        "key_points": [
            "Category: kata - the longest Shotokan kata; the summit of the ladder.",
            "Sixty-five movements; opens gazing skyward, hands parting clouds.",
            "Named for the Chinese envoy Kusanku (Kusanku Dai lineage).",
            "Contains every family: blocks, double punches, kicks, back kick, jump, tension sequences.",
            "About one and a half seconds per movement: roughly one hundred seconds total.",
            "Funakoshi's favorite kata; nearly the entire art in one form.",
        ],
        "requirements": [
            "All Heian kata, Tekki Shodan, and Bassai Dai performed cleanly first.",
            "Stamina for one hundred seconds of continuous full-power kata.",
            "A large clear floor for the kata's wide embusen and the jump.",
            "A teacher to correct the sixty-five movements' details.",
        ],
        "standards": [
            "JKA kata standards (Kanku Dai).",
            "Shotokan grading syllabus - 1st dan kata requirement.",
        ],
        "citations": [CIT_FUNAKOSHI_KYOHAN, CIT_NAKAYAMA_BEST, CIT_PFLUGER, CIT_JKA],
        "sig_lens":
            "Through the Signature lens, Kanku Dai is the complete archive in "
            "one volume: sixty-five movements, sixty-five chapters, opening "
            "with the eyes on the sky because the Signature is witnessed by "
            "heaven before it is read by men. The Signature method places "
            "this kata at the ladder's summit as the form that contains all "
            "other forms - the signature that signs the whole book.",
    },
]
