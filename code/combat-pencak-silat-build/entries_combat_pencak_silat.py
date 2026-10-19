#!/usr/bin/env python3
"""Entries for the Pencak Silat Combat databases (combat batch 3, 2026-10-17).

Two NEW databases, 34 ladder-ordered records each:

  combat-pencak-silat            - The Pencak Silat Combat Database
                                   (public-harvest: real, fact-checked
                                   Indonesian pencak silat knowledge -
                                   kuda-kuda stances, sikap guard postures,
                                   langkah footwork, pukulan punches,
                                   tendangan kicks, tangkisan blocks,
                                   elakan evasions, tangkapan catches,
                                   sapuan sweeps, bantingan throws, kuncian
                                   joint locks, guntingan scissors, jurus
                                   forms, kembangan flow, tanding sport
                                   rules, and the toya, golok, karambit,
                                   and keris blade heritage - every record
                                   a full technique with step-by-step body
                                   mechanics; standard references Draeger
                                   Weapons and Fighting Arts of Indonesia
                                   1972, Maryono Pencak Silat in the
                                   Indonesian Archipelago 1998, IPSI
                                   competition rules, PERSILAT international
                                   regulations, and the 2019 UNESCO
                                   Intangible Cultural Heritage inscription)
  combat-pencak-silat-signature  - The Pencak Silat Combat Signature Database
                                   (his original Signature silat method:
                                   every technique a covenant of body and
                                   breath, the kuda-kuda the oath of the
                                   earth, the jurus the archive of the
                                   ancestors written in motion, and the
                                   langkah the signature of the path; src
                                   signature, titles suffixed " (Signature
                                   Edition)", never presented as authentic
                                   public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBPS- (public) and JAH-CBPSS- (signature), verified free
in the manifest id_prefix values and zero hits in every shard index file.

Dedupe: all 68 titles (34 public + 34 Signature Edition) run through the
whole-system dedupe gate before authoring - zero refusals, zero collisions.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_pencak_silat.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

Screening: civilian traditional-art instruction only - the Indonesian
martial art of pencak silat as cultural heritage and disciplined training.
Nothing hate-adjacent, profane, or inappropriate; no religious talk.
Nothing on neutralizing or defeating military or defense-grade systems -
the standing exclusion holds. Blade entries (toya, golok, karambit, keris)
cover traditional heritage handling, form, and safety only.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature silat method: every "
            "technique a covenant of body and breath, the kuda-kuda the oath "
            "of the earth, the jurus the archive of the ancestors written in "
            "motion, and the langkah the signature of the path. Clearly "
            "labeled Signature-made, never presented as authentic public "
            "record.")

CIT_DRAEGER = ("Draeger D.F. Weapons and Fighting Arts of Indonesia. "
               "Rutland: Charles E. Tuttle; 1972.")
CIT_MARYONO = ("Maryono O. Pencak Silat in the Indonesian Archipelago. "
               "Yogyakarta: Yayasan Galang; 1998.")
CIT_IPSI = ("Ikatan Pencak Silat Indonesia (IPSI). Peraturan Pertandingan "
            "Pencak Silat: official competition rules. Jakarta: IPSI; "
            "current edition.")
CIT_PERSILAT = ("Persekutuan Pencak Silat Antarbangsa (PERSILAT). "
                "International pencak silat competition regulations. "
                "Jakarta: PERSILAT; current edition.")
CIT_UNESCO = ("UNESCO. Traditions of Pencak Silat: inscribed on the "
              "Representative List of the Intangible Cultural Heritage of "
              "Humanity; 2019.")

ENTRIES = [
    {
        "key": "kuda-kuda",
        "name": "Kuda-Kuda (Stances)",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description":
            "Kuda-kuda are the stances of pencak silat, the root system from "
            "which every punch, kick, sweep, and throw grows. The classical "
            "set includes kuda-kuda depan (front stance), kuda-kuda belakang "
            "(rear stance), kuda-kuda tengah (middle stance), kuda-kuda "
            "samping (side stance), and kuda-kuda silang (crossed stance). "
            "Each stance fixes the height of the body, the distribution of "
            "weight, and the direction power can travel. A front stance "
            "carries about sixty percent of the weight on the lead leg and "
            "drives forward; a middle stance spreads the weight evenly and "
            "anchors against lateral force; the crossed stance coils the "
            "body for turning techniques. Beginners hold each stance for "
            "slow counts while a teacher checks the knees, the back, and "
            "the feet, because every advanced technique in silat is only a "
            "stance that learned to move.",
        "how_it_works":
            "Stand with feet together and the body relaxed. For kuda-kuda "
            "depan, step one foot forward about one and a half shoulder "
            "widths, bend the front knee until it sits above the toes, keep "
            "the rear leg straight with the heel pressed down, and settle "
            "about sixty percent of your weight forward with the hips square. "
            "For kuda-kuda tengah, step sideways about two shoulder widths, "
            "bend both knees equally with the knees tracking over the toes, "
            "keep the back straight and upright, and split the weight "
            "fifty-fifty. For kuda-kuda belakang, shift most of the weight "
            "onto the rear leg with the front foot light on its toes. For "
            "kuda-kuda silang, cross one foot behind the other and sink low "
            "with the knees bent. Hold each stance for a slow count of ten, "
            "breathing steadily, then step through all five in order without "
            "rising up between them.",
        "key_points": [
            "Category: foundations - stances are the root of all silat technique.",
            "Kuda-kuda depan: about sixty percent of weight on the front leg.",
            "Kuda-kuda tengah: weight split evenly, knees tracking over toes.",
            "Kuda-kuda belakang: weight sunk onto the rear leg, front foot light.",
            "Kuda-kuda silang: crossed feet coiling the body for turns.",
            "Knees always track over the toes; the back stays straight.",
            "Step through all five stances without rising between them.",
        ],
        "requirements": [
            "Flat, non-slippery training floor with room to step in all directions.",
            "Bare feet; loose training uniform.",
            "A mirror or teacher to check knee, back, and foot alignment.",
            "Five minutes of leg warm-up before deep stance holding.",
        ],
        "standards": [
            "IPSI basic curriculum stance requirements (kuda-kuda).",
            "Traditional aliran grading: stance-hold endurance at first level.",
        ],
        "citations": [CIT_MARYONO, CIT_IPSI],
        "sig_lens":
            "Through the Signature lens, kuda-kuda is the oath the body "
            "swears to the earth: five stances, five vows, each one a "
            "promise about where the weight will stand when the storm "
            "comes. Every technique in the Signature silat method is signed "
            "first by a stance.",
    },
    {
        "key": "sikap-pasang",
        "name": "Sikap Pasang (Fighting Guard)",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description":
            "Sikap pasang is the ready guard posture of pencak silat, the "
            "position from which all attack and defense begin. The body "
            "settles into a chosen kuda-kuda, the lead hand extends toward "
            "the partner at about chest height with the elbow softly bent, "
            "and the rear hand guards the chin and ribs. The chin tucks "
            "slightly, the eyes stay level and watch the partner's chest, "
            "and the weight stays spring-loaded on the balls of the feet. "
            "Unlike a rigid pose, sikap pasang breathes: the hands float, "
            "the stance shifts with small langkah steps, and the guard "
            "adapts to each aliran's character - some schools hold the "
            "hands high and tight, others extend them low and inviting. "
            "Teachers test a student's sikap pasang by pushing gently at "
            "the shoulders: a true guard absorbs the push through the "
            "stance without toppling.",
        "how_it_works":
            "Settle into kuda-kuda depan with about sixty percent of your "
            "weight forward. Raise the lead hand to chest height, arm "
            "extended about two-thirds with the elbow bent roughly one "
            "hundred twenty degrees and the palm facing inward. Hold the "
            "rear hand beside the chin with the elbow tucked to guard the "
            "ribs. Tuck the chin a finger's width, keep the eyes level on "
            "the partner's chest, and relax the shoulders down away from "
            "the ears. Breathe slowly through the nose. Practice shifting "
            "the guard: extend the lead hand six inches and draw it back, "
            "circle the hands once, then settle again. Have a partner push "
            "gently at your shoulders while you sink slightly deeper into "
            "the stance instead of leaning back.",
        "key_points": [
            "Category: foundations - the guard is the doorway of technique.",
            "Lead hand extended at chest height, elbow softly bent.",
            "Rear hand guards the chin; elbow tucked to the ribs.",
            "Chin tucked, eyes level on the partner's chest.",
            "Weight spring-loaded; the guard breathes and shifts.",
            "Absorb a shoulder push through the stance, never by leaning back.",
            "Each aliran shapes its own sikap pasang character.",
        ],
        "requirements": [
            "Training partner for guard testing and distance drills.",
            "Open floor space for shifting and small steps.",
            "Bare feet; loose training uniform.",
        ],
        "standards": [
            "IPSI basic curriculum guard posture (sikap pasang).",
            "Traditional aliran grading: guard stability under a shoulder push.",
        ],
        "citations": [CIT_MARYONO, CIT_IPSI],
        "sig_lens":
            "Through the Signature lens, sikap pasang is the open door of "
            "the house: inviting, watchful, and rooted. The lead hand is "
            "the greeting, the rear hand the promise, and the stance the "
            "foundation the door hangs on.",
    },
    {
        "key": "langkah",
        "name": "Langkah (Stepping Patterns)",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description":
            "Langkah is the footwork of pencak silat - the stepping patterns "
            "that carry the body into range, out of danger, and around the "
            "partner. Classical langkah includes langkah depan (stepping "
            "forward), langkah belakang (stepping back), langkah samping "
            "(stepping sideways), langkah silang (cross-stepping), and "
            "langkah putar (turning steps). Advanced schools drill pola "
            "langkah, geometric floor patterns - triangles, squares, and "
            "figure-eights - walked for hundreds of repetitions until the "
            "feet draw them without thought. Good langkah keeps the body "
            "level: the head glides at one height instead of bobbing, the "
            "weight transfers smoothly from foot to foot, and every step "
            "lands in a usable kuda-kuda. Masters say the hands only finish "
            "what the feet have already decided, which is why langkah "
            "drills open every traditional training session.",
        "how_it_works":
            "Begin in sikap pasang in kuda-kuda depan. For langkah depan, "
            "slide the rear foot up beside the front foot, then step the "
            "front foot forward one shoulder width, landing in kuda-kuda "
            "depan again with the head at exactly the same height. For "
            "langkah belakang, reverse the sequence. For langkah samping, "
            "step the lead foot sideways and bring the rear foot to meet "
            "it, settling into kuda-kuda tengah. For langkah silang, cross "
            "the rear foot behind the lead foot and pivot into kuda-kuda "
            "silang. For langkah putar, step across and turn the body one "
            "hundred eighty degrees. Walk each pattern ten lengths of the "
            "floor, keeping the head level and landing every step in a "
            "clean stance. Then walk a triangle: three langkah depan, pivot "
            "sixty degrees, and repeat.",
        "key_points": [
            "Category: foundations - footwork decides what the hands can do.",
            "Langkah depan, belakang, samping, silang, and putar form the core set.",
            "Pola langkah drills geometric floor patterns until automatic.",
            "The head glides at one height; no bobbing between steps.",
            "Every step lands in a usable kuda-kuda.",
            "Weight transfers smoothly from foot to foot.",
            "Ten floor lengths per pattern builds the foundation.",
        ],
        "requirements": [
            "Long clear floor lane for walking patterns.",
            "Bare feet; loose training uniform.",
            "Floor markers or tape for triangle and square patterns.",
        ],
        "standards": [
            "IPSI basic curriculum footwork (langkah).",
            "Traditional aliran grading: pola langkah accuracy and flow.",
        ],
        "citations": [CIT_MARYONO, CIT_IPSI],
        "sig_lens":
            "Through the Signature lens, langkah is the signature of the "
            "path: every step a stroke of the pen, every floor pattern a "
            "sentence written with the feet. The hands only finish what the "
            "feet have already decided.",
    },
    {
        "key": "pernapasan",
        "name": "Pernapasan (Breathing Discipline)",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description":
            "Pernapasan is the breathing discipline of pencak silat, the "
            "engine that powers long training sessions and steadies the "
            "body under pressure. Students learn to breathe through the "
            "nose with the diaphragm: the belly expands on the inhale, the "
            "lower abdomen draws gently in on the exhale, and the shoulders "
            "stay down and still. Technique rides the breath - the exhale "
            "carries the punch, the kick, and the throw, while the inhale "
            "recovers the guard. Traditional schools drill counted breathing "
            "in stance: four counts in, two counts held, four counts out, "
            "held while the legs burn in kuda-kuda. Over months the breath "
            "slows the heart, steadies the hands, and teaches the student "
            "to stay calm when the pace quickens. Breath is the first "
            "technique and the last one; everything between is commentary.",
        "how_it_works":
            "Sit or stand tall with the shoulders relaxed and down. Place "
            "one hand on the belly. Inhale slowly through the nose for four "
            "counts, feeling the belly expand against the hand while the "
            "chest stays quiet. Hold for two counts. Exhale through the "
            "nose or pursed lips for four counts, drawing the lower abdomen "
            "gently inward. Repeat for ten full cycles. Next, hold "
            "kuda-kuda tengah and breathe the same 4-2-4 pattern for two "
            "minutes while the stance burns. Then practice technique "
            "breathing: from sikap pasang, exhale sharply through the nose "
            "as you throw a slow pukulan lurus, inhale as the hand returns "
            "to guard. Ten punches, breath matched to every one.",
        "key_points": [
            "Category: foundations - breath is the engine of all technique.",
            "Diaphragm breathing: belly expands on inhale, draws in on exhale.",
            "Shoulders stay down and still throughout.",
            "The exhale carries the technique; the inhale recovers the guard.",
            "Counted pattern: four in, two held, four out.",
            "Two minutes of stance breathing builds endurance and calm.",
            "Match one breath cycle to every technique repetition.",
        ],
        "requirements": [
            "Quiet space for the first seated breathing cycles.",
            "Open floor for stance breathing drills.",
            "A timer or counted cadence for the 4-2-4 pattern.",
        ],
        "standards": [
            "Traditional aliran breathing curriculum (pernapasan).",
            "IPSI warm-up standards: controlled breathing under exertion.",
        ],
        "citations": [CIT_MARYONO],
        "sig_lens":
            "Through the Signature lens, pernapasan is the covenant of "
            "breath: the inhale the promise, the exhale the signature. A "
            "technique thrown on a true exhale carries the whole body "
            "behind it.",
    },
    {
        "key": "pukulan-lurus",
        "name": "Pukulan Lurus (Straight Punch)",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description":
            "Pukulan lurus is the straight punch of pencak silat, the first "
            "hand strike every student learns and the measuring stick for "
            "all hand power. Thrown from sikap pasang, the rear fist travels "
            "the shortest line to the target while the hip snaps forward "
            "and the rear heel drives into the floor. The fist stays "
            "vertical or rotates to horizontal only in the final third of "
            "travel, the elbow stays under the fist, and the non-punching "
            "hand guards the chin until the punching hand returns to take "
            "its place. Power comes from the ground through the stance, the "
            "hip, and the shoulder in one chain - the arm only delivers "
            "what the body has already built. Students drill it in counts "
            "of ten per side, then in flowing combinations, until the "
            "straight line becomes the body's first answer.",
        "how_it_works":
            "Settle into sikap pasang in kuda-kuda depan. Exhale as you "
            "drive the rear fist straight forward at chest height, rotating "
            "the hip of the punching side forward and pressing the rear "
            "heel into the floor. Keep the elbow under the fist and the "
            "shoulder down; rotate the fist to horizontal in the last third "
            "of the punch. At full extension the arm is nearly straight "
            "but the elbow never locks, and the lead hand stays at the chin. "
            "Snap the fist back along the same line to guard as you inhale. "
            "Drill ten slow punches per side checking the line in a mirror, "
            "then ten at full speed with a sharp exhale on each, then "
            "alternate sides without pausing for one minute.",
        "key_points": [
            "Category: strikes - the straight punch is the first hand strike.",
            "Shortest line from guard to target; hip snaps with the punch.",
            "Fist rotates only in the final third of travel.",
            "Elbow stays under the fist; shoulder stays down.",
            "Never lock the elbow at full extension.",
            "The guard hand stays at the chin throughout.",
            "Exhale on the punch; inhale on the return.",
        ],
        "requirements": [
            "Mirror for checking the punch line and hip rotation.",
            "Open floor space; bare feet.",
            "A focus pad or willing partner for later contact drills.",
        ],
        "standards": [
            "IPSI basic curriculum hand strikes (pukulan).",
            "Traditional aliran grading: straight punch form and hip drive.",
        ],
        "citations": [CIT_MARYONO, CIT_IPSI],
        "sig_lens":
            "Through the Signature lens, pukulan lurus is the straight "
            "signature: the shortest line between the oath and its keeping. "
            "The hip signs it, the heel witnesses it, and the exhale seals it.",
    },
    {
        "key": "tendangan-lurus",
        "name": "Tendangan Lurus (Front Push Kick)",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description":
            "Tendangan lurus is the front push kick of pencak silat, driven "
            "straight forward from a raised knee with the ball of the foot "
            "or the heel as the striking surface. From sikap pasang the "
            "kicker chambers the knee high toward the chest, extends the "
            "leg straight into the target while the standing hip drives "
            "forward, and rechambers before the foot returns to the floor. "
            "The supporting foot pivots slightly, the hands stay in guard "
            "with a small counter-swing for balance, and the eyes never "
            "leave the partner. It is both a scoring weapon in tanding and "
            "a distance tool: a firm tendangan lurus stops an advancing "
            "partner cold and resets the range. Beginners practice it "
            "against a wall for balance, then on pads, then in stepping "
            "combinations across the floor.",
        "how_it_works":
            "Stand in sikap pasang. Shift your weight onto the lead leg and "
            "raise the rear knee toward your chest, keeping the foot flexed "
            "and the hands in guard. Extend the leg straight forward, "
            "driving through the ball of the foot or the heel while pushing "
            "the standing hip forward and leaning the torso slightly back "
            "for counterbalance. At full extension the leg is straight but "
            "the knee is not locked. Snap the knee back to the chamber "
            "position, then place the foot down in kuda-kuda. Drill ten "
            "kicks per leg against a wall for balance, then ten per leg on "
            "a pad with a partner holding, exhaling on every extension.",
        "key_points": [
            "Category: strikes - the front kick controls distance.",
            "Chamber the knee high before extending.",
            "Strike with the ball of the foot or the heel.",
            "Standing hip drives forward; torso leans slightly back.",
            "Rechamber before the foot returns to the floor.",
            "Hands stay in guard; eyes never leave the partner.",
            "Wall, then pad, then stepping combinations - in that order.",
        ],
        "requirements": [
            "Wall or rail for balance in early drills.",
            "Kicking pad and a partner for contact practice.",
            "Open floor; bare feet.",
        ],
        "standards": [
            "IPSI basic curriculum kicks (tendangan).",
            "Tanding scoring: a clean front kick scores points.",
        ],
        "citations": [CIT_MARYONO, CIT_IPSI],
        "sig_lens":
            "Through the Signature lens, tendangan lurus is the door pushed "
            "shut with the whole body behind it: chamber the question, "
            "extend the answer, and rechamber before the echo returns.",
    },
    {
        "key": "tangkisan-dalam",
        "name": "Tangkisan Dalam (Inside Block)",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description":
            "Tangkisan dalam is the inside block of pencak silat, the "
            "forearm rising across the body's centerline to meet an "
            "incoming strike. The blocking arm sweeps upward and inward "
            "from the hip, the forearm meets the attack at roughly a "
            "forty-five-degree angle, and the block finishes with the fist "
            "near the opposite shoulder and the elbow guarding the ribs. "
            "The stance drops slightly as the block lands, lending the "
            "body's weight to the deflection, and the free hand stays ready "
            "to catch or counter. Paired with its siblings - tangkisan luar "
            "(outside), tangkisan atas (upper), and tangkisan bawah (lower) "
            "- it forms the four-gate wall every silat student raises "
            "before learning to attack. The block is never a wall to hide "
            "behind; it is a gate that turns the attack aside and opens the "
            "door for the counter.",
        "how_it_works":
            "Stand in sikap pasang. As the partner throws a slow straight "
            "punch at your chest, sweep your lead forearm upward and inward "
            "across your centerline, meeting their forearm with the outside "
            "of yours at about forty-five degrees. Drop your weight an inch "
            "into the stance as contact lands and finish with your fist near "
            "your opposite shoulder, elbow guarding the ribs. Keep the free "
            "hand at your chin. Immediately answer with a slow pukulan lurus "
            "from the free hand. Drill ten blocks per side against slow "
            "punches, then have the partner vary the timing while you keep "
            "the block small and the stance rooted.",
        "key_points": [
            "Category: defenses - the inside block guards the centerline.",
            "Forearm meets the attack at about forty-five degrees.",
            "Block finishes with the fist near the opposite shoulder.",
            "Drop the weight an inch as the block lands.",
            "Free hand stays at the chin, ready to counter.",
            "One of the four gates: dalam, luar, atas, bawah.",
            "Small block, rooted stance; answer with the free hand.",
        ],
        "requirements": [
            "Training partner throwing slow, controlled punches.",
            "Open floor space; bare feet.",
            "Forearm conditioning built gradually over weeks.",
        ],
        "standards": [
            "IPSI basic curriculum blocks (tangkisan).",
            "Traditional aliran grading: four-gate blocking form.",
        ],
        "citations": [CIT_MARYONO, CIT_IPSI],
        "sig_lens":
            "Through the Signature lens, tangkisan dalam is the gate that "
            "turns the storm aside: the forearm the hinge, the stance the "
            "post, and the counter the signature written on the other side "
            "of the door.",
    },
    {
        "key": "elakan",
        "name": "Elakan (Body Evasion)",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description":
            "Elakan is body evasion in pencak silat - moving the target "
            "instead of meeting the attack. The classical evasions are "
            "elakan bawah (ducking under), elakan atas (leaning the torso "
            "back), elakan samping (slipping sideways), and elakan putar "
            "(turning the body away). Each one keeps the feet under the "
            "body and the guard intact: the head moves inches, not feet, "
            "and the evasion ends in a stance ready to answer. Silat "
            "teachers prize elakan above blocking because a missed attack "
            "costs the attacker balance while costing the defender almost "
            "nothing. Students drill it with a partner swinging a padded "
            "stick slowly past the head, learning to let the attack pass "
            "through empty air while the body stays calm and the breath "
            "stays even.",
        "how_it_works":
            "Stand in sikap pasang facing a partner with a padded stick. "
            "For elakan bawah, bend both knees and sink straight down about "
            "eight inches as the stick swings over your head, keeping the "
            "back straight and the guard up. For elakan atas, lean the torso "
            "back from the hips about fifteen degrees with the knees soft, "
            "letting the stick pass before your face. For elakan samping, "
            "take one langkah samping and slip the head six inches offline "
            "while the hands stay in guard. For elakan putar, cross-step and "
            "turn the body ninety degrees. After each evasion, answer with "
            "a slow counter from the new position. Drill five of each per "
            "side at slow speed before the partner adds pace.",
        "key_points": [
            "Category: defenses - evasion moves the target, not the attack.",
            "Four classical evasions: bawah, atas, samping, putar.",
            "The head moves inches; the feet stay under the body.",
            "Every evasion ends in a stance ready to counter.",
            "Guard stays intact throughout the evasion.",
            "A missed attack costs the attacker balance.",
            "Drill with a padded stick at slow speed first.",
        ],
        "requirements": [
            "Partner with a padded stick for slow evasion drills.",
            "Open floor space; bare feet.",
            "Guard discipline: hands never drop during the evasion.",
        ],
        "standards": [
            "IPSI basic curriculum evasions (elakan).",
            "Traditional aliran grading: four-direction evasion form.",
        ],
        "citations": [CIT_MARYONO, CIT_IPSI],
        "sig_lens":
            "Through the Signature lens, elakan is the art of not being "
            "where the storm lands: the body the pen lifted from the page, "
            "the attack a sentence written on empty air.",
    },
    {
        "key": "tepisan",
        "name": "Tepisan (Deflecting Parry)",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description":
            "Tepisan is the deflecting parry of pencak silat, the open hand "
            "brushing an incoming strike aside with timing instead of "
            "force. Where tangkisan meets the attack with the forearm, "
            "tepisan meets it with the palm or the edge of the hand and "
            "redirects it past the body with a short, sharp slap. The "
            "parry travels only a few inches - the hand starts in guard "
            "and returns to guard - and the feet take one small langkah to "
            "sharpen the angle. Because it borrows the attack's own speed, "
            "tepisan costs almost no energy and leaves the parrying hand "
            "free to catch, trap, or strike in the same beat. Students "
            "learn it against slow straight punches first, then against "
            "kicks, discovering that the lighter the touch, the faster the "
            "counter that follows.",
        "how_it_works":
            "Stand in sikap pasang. As the partner throws a slow straight "
            "punch, brush the outside of their wrist with your lead palm, "
            "pushing it six inches past your shoulder while you take one "
            "small langkah samping. The parry is a slap, not a push: contact "
            "lasts a fraction of a second and your hand snaps back to "
            "guard. Against a front kick, brush the ankle aside with the "
            "palm as you step offline. Drill ten parries per side against "
            "slow punches, keeping the motion under six inches of travel, "
            "then add an immediate counter punch from the parrying hand. "
            "The lighter the touch, the sooner the counter lands.",
        "key_points": [
            "Category: defenses - the parry redirects with timing, not force.",
            "Palm or hand-edge brushes the strike a few inches offline.",
            "Contact is a slap; the hand snaps back to guard.",
            "One small langkah sharpens the deflection angle.",
            "Borrows the attack's speed; costs almost no energy.",
            "The parrying hand is free to counter in the same beat.",
            "Slow punches first, then kicks, then faster timing.",
        ],
        "requirements": [
            "Partner throwing slow, controlled punches and kicks.",
            "Open floor space; bare feet.",
            "Discipline to keep the parry small under pressure.",
        ],
        "standards": [
            "IPSI basic curriculum parries (tepisan).",
            "Traditional aliran grading: parry timing and recovery.",
        ],
        "citations": [CIT_MARYONO, CIT_IPSI],
        "sig_lens":
            "Through the Signature lens, tepisan is the lightest signature: "
            "a brushstroke that moves the river aside. The smaller the "
            "parry, the larger the answer it makes room for.",
    },
    {
        "key": "tangkapan",
        "name": "Tangkapan (Catching the Limb)",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description":
            "Tangkapan is the art of catching an attacking limb in pencak "
            "silat - seizing a punch, a kick, or a thrust and holding it "
            "just long enough to answer. The catch is soft: the hands close "
            "around the wrist or ankle at the moment of full extension, "
            "when the limb is slowest, and the body takes one langkah back "
            "or aside to absorb the remaining force. Once caught, the limb "
            "becomes a handle - the catcher can pull the partner off "
            "balance, feed the caught leg into a sapuan sweep, or pin the "
            "arm for a kuncian lock. Timing is everything: reach too early "
            "and the strike slips past; grab too late and it has already "
            "landed. Students practice with a partner throwing slow kicks "
            "that they catch at the ankle, learning to read the chamber "
            "before the kick extends.",
        "how_it_works":
            "Face a partner in sikap pasang. As they throw a slow front "
            "kick, watch the chamber: when the leg extends, step back one "
            "small langkah and close both hands around their ankle at full "
            "extension, thumbs on top. Absorb the push by sinking into your "
            "stance rather than bracing the arms. Hold for one count, then "
            "either push the leg aside and release, or pull gently to test "
            "their balance. Against a slow straight punch, catch the wrist "
            "with your lead hand at extension and guide it past your hip. "
            "Drill ten catches per side at slow speed; speed up only when "
            "every catch lands soft and the stance never breaks.",
        "key_points": [
            "Category: defenses - the catch turns the attack into a handle.",
            "Catch at full extension, when the limb is slowest.",
            "Hands close soft around wrist or ankle; never grab rigidly.",
            "One langkah back or aside absorbs the remaining force.",
            "Read the chamber before the technique extends.",
            "A caught limb feeds sweeps, locks, and off-balancing.",
            "Slow speed first; the stance must never break.",
        ],
        "requirements": [
            "Partner throwing slow, predictable kicks and punches.",
            "Open floor space; bare feet.",
            "A teacher to correct timing before speed increases.",
        ],
        "standards": [
            "IPSI basic curriculum catches (tangkapan).",
            "Traditional aliran grading: catch timing and softness.",
        ],
        "citations": [CIT_MARYONO, CIT_IPSI],
        "sig_lens":
            "Through the Signature lens, tangkapan is catching the pen "
            "mid-sentence: the limb a line of writing, the catch the hand "
            "that holds the page still long enough to read it.",
    },
    {
        "key": "kembangan",
        "name": "Kembangan (Flowing Movement Dance)",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description":
            "Kembangan, the flower dance, is pencak silat's flowing movement "
            "practice - the art performed as dance, with every technique "
            "hidden inside beautiful motion. Practitioners move through "
            "stances, evasions, strikes, and sweeps in continuous flow, "
            "often to the rhythm of traditional gendang drums, turning "
            "combat into choreography without losing its teeth. Kembangan "
            "trains what rigid drilling cannot: transitions, breathing "
            "under continuous motion, balance through turning, and the "
            "relaxed body that makes techniques fast. In competition it is "
            "its own judged category, scored on grace, correctness, and "
            "spirit; in the village it is celebration, wedding "
            "entertainment, and the living archive of the aliran's "
            "character. Every master can be recognized by their kembangan "
            "the way a writer is recognized by handwriting.",
        "how_it_works":
            "Stand relaxed with soft knees. Begin walking a slow circle, "
            "letting the arms float through guard positions. On each drum "
            "beat or counted beat, change: sink into kuda-kuda tengah, rise "
            "through sikap pasang, slip into elakan samping, extend a slow "
            "pukulan lurus, and flow back to walking. Link five techniques "
            "into one unbroken sequence and repeat it for three minutes "
            "without stopping, breathing steadily through the nose. Keep "
            "the shoulders down and the face calm; the moment the flow "
            "breaks, return to the walking circle and begin again. Practice "
            "daily until the transitions disappear and only the river of "
            "motion remains.",
        "key_points": [
            "Category: foundations - flow practice hides technique in beauty.",
            "Continuous motion through stances, evasions, and strikes.",
            "Traditionally performed to gendang drum rhythm.",
            "Trains transitions, turning balance, and relaxed speed.",
            "Judged competition category: grace, correctness, spirit.",
            "Three unbroken minutes builds flow endurance.",
            "A master's kembangan reads like handwriting.",
        ],
        "requirements": [
            "Open floor for continuous circling movement.",
            "Drum recording or counted cadence for rhythm.",
            "Bare feet; loose training uniform.",
        ],
        "standards": [
            "IPSI artistic category: kembangan performance standards.",
            "UNESCO 2019: kembangan as living intangible heritage.",
        ],
        "citations": [CIT_MARYONO, CIT_IPSI, CIT_UNESCO],
        "sig_lens":
            "Through the Signature lens, kembangan is the signature written "
            "in cursive: every technique a letter, every transition the "
            "join between letters, the whole form a name the body writes "
            "in the air.",
    },
    {
        "key": "tendangan-sabit",
        "name": "Tendangan Sabit (Crescent Kick)",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description":
            "Tendangan sabit, the crescent kick, sweeps the leg in a wide "
            "arc like the curve of a sickle - sabit means sickle. From "
            "sikap pasang the kicker swings the leg up and across in a "
            "crescent path, striking with the outer edge of the foot or "
            "the instep, then whips it back along the same arc. Thrown from "
            "the outside it is sabit luar; thrown across the body it is "
            "sabit dalam. The hip opens fully to power the arc, the "
            "supporting foot pivots on the ball, and the hands counter-"
            "swing to keep the torso upright. Because the kick travels "
            "around the guard rather than through it, it is silat's classic "
            "answer to a tight defense - the arc goes where the straight "
            "line cannot. Students master it on pads before ever throwing "
            "it at a partner, because the same arc that scores can sweep "
            "a careless kicker off their own feet.",
        "how_it_works":
            "Stand in sikap pasang. For sabit luar with the rear leg, pivot "
            "the supporting foot about forty-five degrees and swing the "
            "kicking leg up in a wide arc from outside to inside, keeping "
            "the leg nearly straight. Strike through the target line with "
            "the outer edge of the foot, letting the hip open fully to "
            "power the arc. Whip the leg back along the same crescent path "
            "and set it down in kuda-kuda. For sabit dalam, swing the leg "
            "across the body from inside to outside. Keep the hands in "
            "guard with a small counter-swing and the eyes on the partner. "
            "Drill ten arcs per leg per side on a pad, checking that the "
            "supporting foot pivots and the torso stays upright.",
        "key_points": [
            "Category: strikes - the crescent kick arcs around the guard.",
            "Sabit luar swings outside to inside; sabit dalam reverses it.",
            "Strike with the outer edge of the foot or the instep.",
            "Hip opens fully; supporting foot pivots on the ball.",
            "Whip the leg back along the same arc.",
            "Answers a tight defense where straight kicks cannot reach.",
            "Pads before partners; the arc punishes poor balance.",
        ],
        "requirements": [
            "Kicking pad and a partner for arc practice.",
            "Open floor space; bare feet.",
            "Hip flexibility warm-up before full-arc kicking.",
        ],
        "standards": [
            "IPSI curriculum kicks (tendangan sabit).",
            "Tanding scoring: clean crescent kicks score.",
        ],
        "citations": [CIT_MARYONO, CIT_IPSI],
        "sig_lens":
            "Through the Signature lens, tendangan sabit is the sickle "
            "moon drawn with the leg: the arc the signature's flourish, "
            "the hip the hand that writes it, the return the pen lifting "
            "clean from the page.",
    },
    {
        "key": "tendangan-t",
        "name": "Tendangan T (Side Kick)",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description":
            "Tendangan T, the side kick, drives the heel straight sideways "
            "into the target with the body turned edge-on - the leg and "
            "torso forming the shape of the letter T. The kicker chambers "
            "the knee tightly across the body, pivots the supporting foot "
            "fully, and thrusts the heel out while the hip commits its full "
            "weight behind the kick. It is the heaviest kick in the silat "
            "arsenal: every pound of the body travels behind a small heel "
            "surface, which is why tanding referees watch it closely and "
            "why teachers drill its control relentlessly. The chamber is "
            "the whole technique - a tight chamber hides the kick until "
            "the last instant, while a loose chamber warns the partner a "
            "full beat early. Students practice it against a wall for "
            "chamber discipline, then on heavy pads for power, then in "
            "stepping entries.",
        "how_it_works":
            "Stand in sikap pasang. Turn the body edge-on by pivoting the "
            "lead foot and chamber the rear knee tightly across your body, "
            "heel pulled to the opposite hip, hands in guard. Pivot the "
            "supporting foot a full one hundred eighty degrees on the ball "
            "so the heel points at the target. Thrust the heel straight "
            "sideways, driving the hip through and leaning the torso away "
            "for counterbalance. Strike with the heel, leg straight but "
            "knee unlocked. Rechamber tightly along the same line and set "
            "the foot down in stance. Drill ten chambers per leg against a "
            "wall without extending, then ten full kicks on a pad.",
        "key_points": [
            "Category: strikes - the side kick is the heaviest kick.",
            "Chamber the knee tightly across the body; hide the kick.",
            "Supporting foot pivots a full one hundred eighty degrees.",
            "Strike with the heel; hip drives through the target.",
            "Torso leans away for counterbalance.",
            "Rechamber along the same line before setting down.",
            "Wall chambers, then pads, then stepping entries.",
        ],
        "requirements": [
            "Wall for chamber discipline drills.",
            "Heavy pad and a partner for power practice.",
            "Hip and ankle warm-up before full pivots.",
        ],
        "standards": [
            "IPSI curriculum kicks (tendangan T).",
            "Tanding scoring: clean side kicks score; control is judged.",
        ],
        "citations": [CIT_MARYONO, CIT_IPSI],
        "sig_lens":
            "Through the Signature lens, tendangan T is the capital letter "
            "written with the whole body: the chamber the pen raised, the "
            "thrust the stroke, the heel the period at the end of the "
            "sentence.",
    },
    {
        "key": "siku",
        "name": "Siku (Elbow Strikes)",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description":
            "Siku are the elbow strikes of pencak silat, the close-range "
            "weapons that take over where punches run out of room. The "
            "family includes siku depan (horizontal elbow across), siku "
            "atas (rising elbow), siku bawah (downward elbow), siku "
            "belakang (rear elbow), and siku putar (spinning elbow). The "
            "elbow is a short, hard lever driven by hip rotation: the "
            "shoulder whips, the hip snaps, and the point of the elbow "
            "arrives with the body's full turning weight behind a few "
            "square inches. Because elbows work in the clinch and the "
            "crowd, silat pairs every siku with a controlling hand - the "
            "free hand checks, pulls, or frames while the elbow strikes. "
            "Students drill siku on pads at close range, learning the "
            "golden rule of the elbow: never reach with it; let the "
            "langkah bring the target to the elbow.",
        "how_it_works":
            "Stand in sikap pasang at arm's length from a pad. For siku "
            "depan, step in with langkah depan, snap the hip of the "
            "striking side forward, and whip the elbow horizontally across "
            "at chin height, keeping the fist tucked near your own shoulder "
            "and the free hand checking the pad. For siku atas, drop "
            "slightly and drive the elbow upward under the chin line. For "
            "siku bawah, raise the elbow and chop downward. For siku "
            "belakang, turn and thrust the elbow straight back. After each "
            "strike, return instantly to guard. Drill ten of each per side "
            "on the pad, stepping in with the strike and never reaching "
            "past your own balance.",
        "key_points": [
            "Category: strikes - elbows rule the close range.",
            "Five core elbows: depan, atas, bawah, belakang, putar.",
            "Hip rotation drives the strike; the arm only delivers.",
            "Free hand checks, pulls, or frames while the elbow strikes.",
            "Fist tucks near the shoulder; point leads.",
            "Never reach with the elbow; let langkah close the distance.",
            "Pad drills at close range build control first.",
        ],
        "requirements": [
            "Focus pads and a partner for close-range drilling.",
            "Open floor; bare feet.",
            "Controlled contact only; elbows are unforgiving.",
        ],
        "standards": [
            "IPSI curriculum elbow strikes (siku).",
            "Traditional aliran grading: close-range elbow form.",
        ],
        "citations": [CIT_MARYONO, CIT_IPSI],
        "sig_lens":
            "Through the Signature lens, siku is the signature written in "
            "the margin where the pen barely fits: short, sharp, and "
            "impossible to ignore, with the free hand holding the page "
            "steady.",
    },
    {
        "key": "lutut",
        "name": "Lutut (Knee Strikes)",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description":
            "Lutut are the knee strikes of pencak silat, driven upward from "
            "a deep stance with the hip thrusting forward and the hands "
            "pulling the target down to meet the knee. The strike lands "
            "with the bony point of the knee or the upper shin, powered by "
            "the same hip snap that drives the punches, and the supporting "
            "leg rises onto the ball of the foot to add height. Silat "
            "teaches the knee as a clinch weapon: one hand controls the "
            "partner's head or arm, the other guards, and the knee rises "
            "between them. Because the knee is already chambered whenever "
            "the leg lifts, it is the fastest heavy weapon in close - "
            "faster than any kick, heavier than any punch. Students drill "
            "it on pads held at body height, learning to pull with the "
            "hands exactly as the knee rises, so control and strike arrive "
            "as one motion.",
        "how_it_works":
            "Stand in sikap pasang before a pad held at body height. Step "
            "in with langkah depan and grip the pad's sides, pulling it "
            "down and toward you. Drive the rear knee straight up, "
            "thrusting the hip forward and rising onto the ball of the "
            "supporting foot. Strike with the point of the knee, keeping "
            "the foot flexed and hanging. At the top, the thigh is "
            "horizontal and the torso is upright, not leaning back. Lower "
            "the leg back to stance without dropping the hands. Drill ten "
            "knees per leg, pulling the pad down exactly as the knee rises, "
            "then practice the alternate knee from a switch of stance.",
        "key_points": [
            "Category: strikes - the knee is the fastest heavy weapon in close.",
            "Hands pull the target down as the knee rises.",
            "Strike with the point of the knee or upper shin.",
            "Hip thrusts forward; support rises onto the ball of the foot.",
            "Thigh reaches horizontal; torso stays upright.",
            "Foot flexed and hanging, never pointed into the strike.",
            "Pull and strike arrive as one motion.",
        ],
        "requirements": [
            "Body pad and a partner for clinch drilling.",
            "Open floor; bare feet.",
            "Hip flexor warm-up before high knee repetitions.",
        ],
        "standards": [
            "IPSI curriculum knee strikes (lutut).",
            "Traditional aliran grading: clinch knee form and control.",
        ],
        "citations": [CIT_MARYONO, CIT_IPSI],
        "sig_lens":
            "Through the Signature lens, lutut is the exclamation point of "
            "the close range: the hands write the sentence downward and "
            "the knee punctuates it, all in a single breath.",
    },
    {
        "key": "pukulan-bandul",
        "name": "Pukulan Bandul (Swinging Punch)",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description":
            "Pukulan bandul is the swinging punch of pencak silat - bandul "
            "means pendulum - a looping strike that arcs around the "
            "partner's guard like a hook with a longer fuse. The shoulder "
            "swings the arm in a wide curve while the hip and torso rotate "
            "fully into the blow, and the fist arrives from outside the "
            "field of vision with the body's turning weight behind it. "
            "Silat pairs it with langkah putar: the body turns, the arm "
            "follows, and the strike lands as the rotation completes. It "
            "is slower than pukulan lurus but far heavier, and its arc "
            "defeats guards built only for straight attacks. Teachers warn "
            "students of its price: a missed bandul spins the puncher past "
            "the target and opens the back, so it is thrown only when the "
            "feet have already placed the body where the arc will land.",
        "how_it_works":
            "Stand in sikap pasang. Step the lead foot across with langkah "
            "silang and begin turning the hips, letting the rear arm swing "
            "in a wide horizontal arc at chin height. Keep the elbow bent "
            "about ninety degrees and the fist vertical, and rotate the "
            "torso fully so the shoulder, hip, and foot turn as one piece. "
            "The fist lands as the rotation completes; the free hand stays "
            "at the chin throughout. If the punch misses, continue the turn "
            "into elakan putar rather than stopping off balance. Drill ten "
            "slow arcs per side on a pad, checking that the feet, hips, and "
            "shoulder turn together, then add speed only when the arc stays "
            "tight and the guard never drops.",
        "key_points": [
            "Category: strikes - the swinging punch arcs around the guard.",
            "Bandul means pendulum; the arm swings in a wide curve.",
            "Hip, torso, and foot rotate as one piece.",
            "Elbow bent about ninety degrees; fist vertical.",
            "Pairs with langkah putar; the turn powers the blow.",
            "A missed bandul opens the back - feet must be placed first.",
            "Free hand guards the chin through the whole arc.",
        ],
        "requirements": [
            "Heavy pad and a partner for arc practice.",
            "Open floor for turning footwork.",
            "Shoulder warm-up before full-arc repetitions.",
        ],
        "standards": [
            "IPSI curriculum swinging strikes (pukulan bandul).",
            "Traditional aliran grading: turning punch coordination.",
        ],
        "citations": [CIT_MARYONO, CIT_IPSI],
        "sig_lens":
            "Through the Signature lens, pukulan bandul is the pendulum "
            "signature: the whole body the swinging weight, the arc the "
            "curve of the letter, the landing the dot of the exclamation.",
    },
    {
        "key": "sapuan",
        "name": "Sapuan (Sweeping Takedowns)",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description":
            "Sapuan are the sweeping takedowns of pencak silat - sapu means "
            "to sweep - the leg swinging low to hook the partner's "
            "supporting leg while the hands pull or push the upper body the "
            "opposite way. The classical pair is sapu dalam (inside sweep, "
            "hooking the leg from between the partner's feet) and sapu luar "
            "(outside sweep, hooking from outside). Timing is the entire "
            "technique: the sweep lands exactly as the partner's weight "
            "commits to the targeted foot, so a light hook topples a heavy "
            "body. Silat sweeps are famous worldwide because they look like "
            "magic - the partner simply falls while the sweeper barely "
            "moves - but the magic is just physics read one beat early. "
            "Students drill sweeps on crash mats with a cooperative partner, "
            "learning to sweep the leg, never the knee, and to lower the "
            "partner safely every time.",
        "how_it_works":
            "Face a partner in sikap pasang on a mat. As they step forward "
            "with langkah depan, time your sweep to their step: for sapu "
            "dalam, swing your rear leg low across in front of their "
            "advancing shin, hooking just above their ankle with your "
            "instep or calf. Simultaneously push their shoulder gently "
            "backward with your lead hand while you pull with the sweep. "
            "Their weight, already committed to the stepping foot, has "
            "nowhere to go and they sit down onto the mat. Guide them down; "
            "never chop at the knee. Drill ten sweeps per side at walking "
            "speed, then have the partner vary their stepping rhythm while "
            "you wait for the committed step.",
        "key_points": [
            "Category: takedowns - sweeps topple the committed step.",
            "Sapu dalam hooks from inside; sapu luar from outside.",
            "Hook just above the ankle, never at the knee.",
            "Hands push or pull the upper body opposite the sweep.",
            "Timing: sweep lands as weight commits to the foot.",
            "Light hook topples heavy weight when timed right.",
            "Mats required; always guide the partner down safely.",
        ],
        "requirements": [
            "Crash mats for all sweep practice.",
            "Cooperative partner stepping predictably at first.",
            "A teacher to supervise timing before live speed.",
        ],
        "standards": [
            "IPSI curriculum sweeps (sapuan).",
            "Tanding scoring: clean sweeps that drop the opponent score.",
        ],
        "citations": [CIT_MARYONO, CIT_IPSI, CIT_PERSILAT],
        "sig_lens":
            "Through the Signature lens, sapuan is the signature that "
            "erases the line under the feet: a light stroke at exactly the "
            "right beat, and the whole sentence of the stance falls over.",
    },
    {
        "key": "bantingan",
        "name": "Bantingan (Throws)",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description":
            "Bantingan are the throws of pencak silat - banting means to "
            "slam or throw down - techniques that take the partner's "
            "balance, load their weight, and put them on the ground. The "
            "family includes hip throws, shoulder throws, and leg-reap "
            "throws, all built on the same three beats: kuzushi-like "
            "off-balancing (called lepas keseimbangan in Indonesian "
            "instruction), entry with langkah that places the hips below "
            "the partner's center, and the turning lift that completes the "
            "throw. Silat throws favor the low stance: the thrower drops "
            "under the partner's center of gravity and lets the legs do "
            "the lifting. In tanding, a clean throw that drops the opponent "
            "scores the highest points of any technique, which is why every "
            "competition school drills bantingan daily. Students learn on "
            "thick mats with a partner who knows how to fall, because a "
            "throw practiced without safe falling is a promise of injury.",
        "how_it_works":
            "Face a partner on thick mats, both in sikap pasang. For a "
            "basic hip throw: pull their lead arm across as you step in "
            "with langkah silang, turning your back to them and dropping "
            "your hips below theirs. Your feet plant inside their stance, "
            "your hip becomes the fulcrum, and you straighten your legs "
            "while pulling their arm down across your body. They roll over "
            "your hip onto the mat; you stay standing in kuda-kuda. The "
            "partner must know breakfalls before you throw them at any "
            "speed. Drill five throws per side at slow speed with full "
            "cooperation, checking hip depth and foot placement every "
            "repetition, before adding any pace.",
        "key_points": [
            "Category: takedowns - throws load and drop the partner.",
            "Three beats: off-balance, entry, turning lift.",
            "Drop the hips below the partner's center of gravity.",
            "The legs lift; the arms only guide.",
            "Hip becomes the fulcrum; feet plant inside the stance.",
            "Highest-scoring technique in tanding when clean.",
            "Thick mats and breakfall-trained partners are mandatory.",
        ],
        "requirements": [
            "Thick crash mats for all throwing practice.",
            "Partner trained in safe breakfalls.",
            "A teacher supervising every new throw.",
        ],
        "standards": [
            "IPSI curriculum throws (bantingan).",
            "Tanding scoring: clean throws score highest.",
        ],
        "citations": [CIT_MARYONO, CIT_IPSI, CIT_PERSILAT],
        "sig_lens":
            "Through the Signature lens, bantingan is the signature that "
            "lifts the page off the desk: off-balance the ink, entry the "
            "hand beneath, and the turn the flourish that sets it all down "
            "in a new place.",
    },
    {
        "key": "kuncian",
        "name": "Kuncian (Joint Locks)",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description":
            "Kuncian are the joint-locking techniques of pencak silat - "
            "kunci means lock or key - controls applied to the wrist, "
            "elbow, and shoulder that guide the partner to the ground or "
            "to stillness. A lock is a lever: one hand fixes the joint, "
            "the other applies gentle pressure just past the joint's "
            "comfortable range, and the whole body - never just the arms - "
            "supplies the force. Silat teaches locks as control first and "
            "pain never: the partner taps the moment they feel pressure, "
            "and the applier releases instantly, every time, without "
            "exception. Locks flow from tangkapan catches and failed "
            "strikes - the caught wrist becomes a wrist lock, the extended "
            "arm becomes an elbow lock. Students drill them slowly with a "
            "trusted partner, learning the anatomy of each joint and the "
            "sacred rule of the lock: the tap is law.",
        "how_it_works":
            "Face a partner who extends their arm in a slow punch. Catch "
            "the wrist with both hands (tangkapan), step offline with "
            "langkah samping, and fold their arm so their palm turns toward "
            "their own face. Fix their wrist against your chest with one "
            "hand while your other hand presses gently on the back of "
            "their hand, bending the wrist just to the edge of comfort. "
            "Sink your weight to guide them downward; never force the "
            "joint with arm strength. The instant your partner taps your "
            "arm or the mat, release completely. Drill five locks per side "
            "at minimal pressure, trading roles, with the teacher watching "
            "every application.",
        "key_points": [
            "Category: controls - locks are levers, not force.",
            "One hand fixes the joint; the other applies gentle pressure.",
            "The whole body supplies force, never just the arms.",
            "Locks flow from catches and overextended strikes.",
            "The tap is law: release instantly, every time.",
            "Control first; pain is never the goal.",
            "Trusted partner and teacher supervision required.",
        ],
        "requirements": [
            "Trusted, communicative training partner.",
            "Open mat space; bare feet.",
            "Teacher supervision for all locking practice.",
            "Strict tap-and-release discipline from day one.",
        ],
        "standards": [
            "IPSI curriculum joint controls (kuncian).",
            "Traditional aliran safety code: tap means immediate release.",
        ],
        "citations": [CIT_MARYONO, CIT_IPSI],
        "sig_lens":
            "Through the Signature lens, kuncian is the key turned gently "
            "in the lock: the joint the keyhole, the body the hand, and "
            "the tap the moment the door opens - never forced, always "
            "released.",
    },
    {
        "key": "tendangan-belakang",
        "name": "Tendangan Belakang (Back Kick)",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description":
            "Tendangan belakang is the back kick of pencak silat, thrown "
            "over the shoulder line at a partner behind the kicker. The "
            "kicker glances back to find the target, turns the body a full "
            "one hundred eighty degrees while chambering the knee, and "
            "drives the heel straight back with the hip fully committed. "
            "It is silat's answer to pressure from behind and a favorite "
            "counter when a partner crowds past the guard: the turn that "
            "seems like retreat becomes the chamber of the heaviest kick "
            "in the arsenal. The danger is the blind moment mid-turn, so "
            "students learn to spot the target first, turn on a fixed line, "
            "and rechamber before the foot lands - a back kick thrown "
            "without a target is just a spin that donates the back. Drilled "
            "on pads with a partner calling the turn, it becomes one of "
            "the most reliable fight-enders in tanding.",
        "how_it_works":
            "Stand in sikap pasang with a pad held behind your kicking "
            "side. Glance over your kicking-side shoulder to spot the pad. "
            "Turn the body one hundred eighty degrees on the ball of the "
            "supporting foot while chambering the kicking knee tightly to "
            "your chest. Drive the heel straight back into the pad, "
            "thrusting the hip through and keeping the torso pitched "
            "forward over the kick for balance. Strike with the heel, knee "
            "unlocked. Rechamber tightly and turn back to face the pad in "
            "sikap pasang. Drill five turns per side slowly for the footwork, "
            "then ten kicks per side on the pad, spotting the target before "
            "every turn.",
        "key_points": [
            "Category: strikes - the back kick answers pressure from behind.",
            "Spot the target over the shoulder before turning.",
            "Turn a full one hundred eighty degrees on the ball of the foot.",
            "Chamber tightly during the turn; drive the heel straight back.",
            "Hip fully committed; torso pitched forward for balance.",
            "Rechamber before the foot lands; return to guard.",
            "Never throw it blind - no target, no kick.",
        ],
        "requirements": [
            "Pad held by a partner who calls the turn.",
            "Open floor for full turns; bare feet.",
            "Ankle and hip warm-up before turning kicks.",
        ],
        "standards": [
            "IPSI curriculum kicks (tendangan belakang).",
            "Tanding scoring: clean back kicks score heavily.",
        ],
        "citations": [CIT_MARYONO, CIT_IPSI],
        "sig_lens":
            "Through the Signature lens, tendangan belakang is the "
            "signature written over the shoulder: the glance the pen "
            "finding the line, the turn the flourish, the heel the stamp "
            "that lands exactly where the eye promised.",
    },
    {
        "key": "guntingan",
        "name": "Guntingan (Scissors Takedown)",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description":
            "Guntingan, the scissors takedown - gunting means scissors - is "
            "pencak silat's most spectacular technique: the practitioner "
            "drops low, scissors the legs around the partner's leg or "
            "waist, and shears them to the ground. In its classic form the "
            "attacker dives beside the partner's lead leg, one leg hooking "
            "behind the knee while the other sweeps the front, and the two "
            "legs close like blades while the hands pull the upper body "
            "down. It appears in kembangan as a flourish and in tanding as "
            "a high-risk, high-reward takedown, and it demands total "
            "commitment - a half-hearted guntingan leaves the attacker on "
            "the floor beneath the partner. Students learn it last among "
            "the takedowns, on the thickest mats, with a partner who falls "
            "well, because the scissors only close safely when both "
            "practitioners trust the technique completely.",
        "how_it_works":
            "Face a partner on thick mats. As they step forward, drop your "
            "level sharply beside their lead leg: your rear leg shoots "
            "behind their knee while your lead leg sweeps across the front "
            "of their shin. Close the legs like scissors - rear leg "
            "pulling, lead leg pushing - while your hands pull their upper "
            "body toward the swept side. Their leg is sheared from under "
            "them and they fall to the mat; you follow through to a low "
            "kuda-kuda, never landing on top of them uncontrolled. Drill "
            "five per side at slow speed with a fully cooperative partner "
            "who practices falling, and only attempt it at pace under a "
            "teacher's direct supervision.",
        "key_points": [
            "Category: takedowns - the scissors shear the leg from under.",
            "Rear leg hooks behind the knee; lead leg sweeps the shin.",
            "Legs close like blades while hands pull the upper body.",
            "Drop the level sharply; total commitment required.",
            "Follow through to a low stance, never uncontrolled.",
            "Highest-risk takedown; learned last among the sweeps.",
            "Thickest mats, falling-trained partner, teacher present.",
        ],
        "requirements": [
            "Thickest available crash mats.",
            "Partner trained in falling safely.",
            "Teacher's direct supervision at any speed.",
        ],
        "standards": [
            "IPSI curriculum advanced takedowns (guntingan).",
            "Tanding scoring: spectacular clean takedowns score highly.",
        ],
        "citations": [CIT_MARYONO, CIT_IPSI, CIT_PERSILAT],
        "sig_lens":
            "Through the Signature lens, guntingan is the signature that "
            "cuts the page in two: the legs the blades, the timing the "
            "hand, and the fall the clean edge left behind.",
    },
    {
        "key": "jurus-tunggal",
        "name": "Jurus Tunggal (Solo Form)",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description":
            "Jurus tunggal is the solo form of pencak silat - jurus meaning "
            "a set sequence, tunggal meaning single - a choreographed "
            "fight against imaginary opponents that archives the aliran's "
            "entire technique library in motion. A tunggal weaves stances, "
            "strikes, blocks, evasions, sweeps, and locks into one "
            "unbroken sequence, each movement flowing into the next with "
            "precise breathing and full intent. In IPSI competition it is "
            "a judged category with set compulsory forms: athletes perform "
            "the same jurus and are scored on correctness, power, rhythm, "
            "and spirit. For the student, the form is a teacher that never "
            "sleeps - practiced alone at dawn, it ingrains technique until "
            "the body knows what the mind has not yet learned. Every "
            "aliran guards its jurus as its written archive, passed from "
            "teacher to student exactly, because the form is the school.",
        "how_it_works":
            "Learn the form in sections of four movements: the teacher "
            "demonstrates, you mirror slowly, then you repeat the section "
            "ten times before adding the next. Each stance must be exact - "
            "kuda-kuda depth checked - each strike thrown with a sharp "
            "exhale, each transition flowing without pauses. Practice the "
            "full sequence slowly for precision, then at performance tempo "
            "with full power and kiai-like spirit shouts where the form "
            "demands. Time the form: a typical tunggal runs sixty to "
            "ninety seconds. Drill it three full times per session, then "
            "pick the weakest section and repeat it ten more times alone.",
        "key_points": [
            "Category: forms - the solo form archives the school in motion.",
            "Choreographed fight against imaginary opponents.",
            "Learn in four-movement sections; ten repetitions each.",
            "Every stance exact; every strike on an exhale.",
            "IPSI judged category with compulsory set forms.",
            "A full tunggal typically runs sixty to ninety seconds.",
            "The form is a teacher that never sleeps.",
        ],
        "requirements": [
            "A teacher to transmit the form exactly.",
            "Open floor for the full sequence.",
            "Daily solo practice space for dawn repetition.",
        ],
        "standards": [
            "IPSI artistic category: jurus tunggal compulsory forms.",
            "Traditional aliran standard: the form is the school.",
        ],
        "citations": [CIT_MARYONO, CIT_IPSI, CIT_UNESCO],
        "sig_lens":
            "Through the Signature lens, jurus tunggal is the archive "
            "written in motion: every stance a paragraph, every strike a "
            "sentence, the whole form a book the body reads aloud at dawn.",
    },
    {
        "key": "sambutan",
        "name": "Sambutan Berencana (Planned Counters)",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description":
            "Sambutan berencana - the planned reception - is pencak silat's "
            "discipline of the counter: for every attack the student learns "
            "a rehearsed answer, drilled until it arrives without thought. "
            "Sambutan means reception or welcome, and the art treats each "
            "incoming technique as a guest to be received properly: the "
            "straight punch is received with tepisan and an answering "
            "pukulan, the front kick with tangkapan and a sapuan, the swing "
            "with elakan and a siku. Training pairs students in set "
            "exchanges - attacker throws a known technique, defender "
            "answers with the planned counter - then gradually loosens the "
            "script until counters emerge from reading rather than memory. "
            "The advanced student owns dozens of receptions and chains them: "
            "a blocked punch becomes a caught wrist, the caught wrist a "
            "kuncian, the lock a takedown. Sambutan is where the separate "
            "techniques stop being vocabulary and become conversation.",
        "how_it_works":
            "Pair with a partner and agree on the attack: a slow straight "
            "punch. The defender answers with the planned reception - "
            "tepisan with the lead hand, immediate pukulan lurus with the "
            "rear - then both reset. Drill ten exchanges, then swap roles. "
            "Add the second reception: front kick answered by tangkapan at "
            "the ankle and sapu dalam. Drill ten, swap. Then the partner "
            "chooses punch or kick without announcing, and the defender "
            "reads and answers with the correct reception. When both "
            "receptions land cleanly eight times out of ten, add a third: "
            "the swinging punch answered by elakan samping and siku. Chain "
            "practice: defender answers, attacker feeds the next attack "
            "from the defender's answer, for five continuous exchanges.",
        "key_points": [
            "Category: strategy - the planned counter is a rehearsed answer.",
            "Every attack owns a reception: punch, kick, swing each answered.",
            "Set exchanges first; reading replaces memory gradually.",
            "Receptions chain: block to catch to lock to takedown.",
            "Eight clean answers out of ten before adding a new reception.",
            "Counters arrive without thought only after hundreds of reps.",
            "Vocabulary becomes conversation at this rank.",
        ],
        "requirements": [
            "Committed partner for set-exchange drilling.",
            "Open floor; protective gear for faster exchanges.",
            "Teacher to correct the chain before speed rises.",
        ],
        "standards": [
            "IPSI paired-drill curriculum (sambutan).",
            "Traditional aliran grading: counter chains under pressure.",
        ],
        "citations": [CIT_MARYONO, CIT_IPSI],
        "sig_lens":
            "Through the Signature lens, sambutan berencana is the "
            "reception hall of the Signature house: every guest attack "
            "received by name, every answer a signature already practiced "
            "a thousand times before the doorbell rang.",
    },
    {
        "key": "jarak-tempo",
        "name": "Jarak dan Tempo (Distance and Timing)",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description":
            "Jarak dan tempo - distance and timing - is the strategic heart "
            "of pencak silat: the study of exactly how far the body can "
            "reach and exactly when to move. Jarak divides the fight into "
            "zones: jarak jauh (long range, kicks rule), jarak sedang "
            "(middle range, punches rule), and jarak dekat (close range, "
            "elbows, knees, and locks rule). The advanced student measures "
            "their own reach in every stance, knows which techniques live "
            "in which zone, and uses langkah to slide between zones at "
            "will. Tempo is the music of the exchange: the rhythm of the "
            "partner's attacks, the half-beat where their weight commits, "
            "the pause where the counter lives. Silat masters teach that "
            "speed is a poor substitute for timing - the fighter who moves "
            "at the right beat beats the fighter who merely moves fast. "
            "Distance and timing are drilled in sparring games long before "
            "full contact, because they are the art's true weapons.",
        "how_it_works":
            "Mark three zones on the floor with tape: long, middle, and "
            "close, measured from your own reach - extend your kick for "
            "the long line, your punch for the middle line, your elbow for "
            "the close line. With a partner, play the zone game: they move "
            "freely while you use only langkah to keep them exactly at your "
            "long-range line for one minute, then middle for one minute, "
            "then close. Next, tempo drill: the partner throws slow "
            "one-two combinations while you clap on the half-beat between "
            "their strikes, learning to hear the gap. Then answer only in "
            "the gap: evade on their beat, counter on the half-beat. Three "
            "rounds of two minutes, rotating roles.",
        "key_points": [
            "Category: strategy - distance and timing are the true weapons.",
            "Three zones: jauh (kicks), sedang (punches), dekat (elbows/knees/locks).",
            "Measure every zone from your own reach in stance.",
            "Langkah slides the body between zones at will.",
            "The counter lives in the half-beat of the partner's rhythm.",
            "Timing beats speed; the right beat beats the fast beat.",
            "Zone games and tempo drills precede full sparring.",
        ],
        "requirements": [
            "Tape-marked floor for zone measurement.",
            "Partner for zone games and tempo drills.",
            "Timer for two-minute rounds.",
        ],
        "standards": [
            "IPSI sparring strategy curriculum (jarak dan tempo).",
            "Traditional aliran teaching: timing over speed.",
        ],
        "citations": [CIT_MARYONO, CIT_IPSI],
        "sig_lens":
            "Through the Signature lens, jarak dan tempo are the margins "
            "and the meter of the page: distance the margins the pen must "
            "respect, timing the meter every signature keeps, and the "
            "half-beat the space where the Signature signs.",
    },
    {
        "key": "toya",
        "name": "Toya (Staff Heritage)",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description":
            "Toya is the staff of pencak silat heritage - a hardwood pole "
            "traditionally cut to about the practitioner's height, trained "
            "as both weapon and teacher. Staff practice builds everything "
            "empty-hand silat needs: grip strength, hip-driven power, "
            "footwork under a moving weight, and the long-range distance "
            "sense that makes kicks precise. The classical curriculum "
            "covers strikes with both ends, sweeping blocks, thrusts, "
            "spinning transitions, and disarming flows, all performed in "
            "jurus that mirror the empty-hand forms. Heritage schools treat "
            "the toya as the elder sibling of technique: students who can "
            "move a six-foot staff without hitting themselves have learned "
            "body awareness no empty-hand drill can give. Training begins "
            "with a rattan practice staff - light and forgiving - and only "
            "later graduates to hardwood, always with clear space and a "
            "teacher present.",
        "how_it_works":
            "Choose a rattan staff about your own height. Stand in "
            "kuda-kuda tengah holding the staff horizontally at chest "
            "height, hands one-third from each end. Practice the basic "
            "strike: slide the rear hand forward to thrust one end straight "
            "at a target, letting the hip drive the thrust, then pull it "
            "back. Next the sweeping block: swing the staff vertically "
            "across your body to deflect an imaginary strike, stepping "
            "offline with langkah samping. Then the spin transition: roll "
            "the staff around your body, changing grips without stopping "
            "its motion. Drill each movement ten times slowly, checking "
            "that the staff never wobbles and the stance never breaks, "
            "before linking them into a short jurus sequence.",
        "key_points": [
            "Category: heritage weapons - the staff is the elder sibling.",
            "Traditionally cut to about the practitioner's height.",
            "Both ends strike; the staff also blocks and thrusts.",
            "Hip drives every thrust; footwork carries the weight.",
            "Begin with rattan; graduate to hardwood only later.",
            "Staff jurus mirror the empty-hand forms.",
            "Clear space and a teacher present, always.",
        ],
        "requirements": [
            "Rattan practice staff (about practitioner height).",
            "Large clear training space - staff needs room.",
            "A teacher for grip, spin, and safety correction.",
        ],
        "standards": [
            "Traditional aliran weapons curriculum (toya).",
            "Heritage practice: rattan before hardwood, always supervised.",
        ],
        "citations": [CIT_DRAEGER, CIT_MARYONO, CIT_UNESCO],
        "sig_lens":
            "Through the Signature lens, toya is the long signature: a "
            "single stroke the length of the body, written with both "
            "hands, teaching the empty hand everything it knows about "
            "distance.",
    },
    {
        "key": "tanding",
        "name": "Tanding (Sport Match Rules)",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description":
            "Tanding is the sport-match discipline of pencak silat, governed "
            "by IPSI nationally and PERSILAT internationally: two athletes "
            "in protective gear contesting technique on a matted arena "
            "under a referee's eye. Matches run in timed rounds - typically "
            "three rounds of two minutes - and scoring rewards clean, "
            "controlled technique: a valid punch scores one point, a valid "
            "kick two points, and a clean takedown or throw that drops the "
            "opponent three points. Strikes must land with control on "
            "legal targets; sweeps and throws must be executed safely; the "
            "referee stops the bout for fouls, injuries, or lost control. "
            "Tanding is where the art proves its techniques under pressure, "
            "but it is a game with rules, not the whole of silat - the "
            "traditional schools remind athletes that the arena tests the "
            "technique, while the art's heritage lives in the jurus, the "
            "kembangan, and the character of the practitioner.",
        "how_it_works":
            "Prepare for tanding by learning the rulebook first: legal "
            "targets, scoring values, fouls, and the referee's commands in "
            "Indonesian. Gear up in the approved body protector, headguard, "
            "gloves, shin guards, and groin protection. Enter the arena in "
            "sikap pasang and contest three two-minute rounds with one "
            "minute of rest between, scoring with controlled punches (one "
            "point), kicks (two points), and clean takedowns (three "
            "points). Between rounds, your coach adjusts strategy: which "
            "zone you are winning, where the opponent's timing breaks. "
            "After the bout, bow to the opponent, the referee, and the "
            "arena - win or lose, the salute is the technique that matters "
            "most. Train specifically: two-minute intense rounds on pads "
            "build the exact endurance tanding demands.",
        "key_points": [
            "Category: sport - the arena tests technique under pressure.",
            "Governed by IPSI nationally and PERSILAT internationally.",
            "Typically three rounds of two minutes, one minute rest.",
            "Scoring: punch one point, kick two points, clean takedown three.",
            "Full protective gear is mandatory.",
            "Control is judged; fouls stop the bout.",
            "The salute after the bout matters most.",
        ],
        "requirements": [
            "Approved protective gear: body protector, headguard, gloves, shin guards.",
            "Matted arena and a qualified referee for bouts.",
            "Rulebook study: legal targets, fouls, commands.",
            "A coach for corner strategy between rounds.",
        ],
        "standards": [
            "IPSI Peraturan Pertandingan Pencak Silat (current edition).",
            "PERSILAT international competition regulations.",
        ],
        "citations": [CIT_IPSI, CIT_PERSILAT],
        "sig_lens":
            "Through the Signature lens, tanding is the signature tested "
            "under the referee's eye: the same hand, the same oath, now "
            "written at full speed while the clock watches - and the "
            "salute afterward the finest stroke of all.",
    },
    {
        "key": "golok",
        "name": "Golok (Machete Heritage)",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description":
            "The golok is the heavy bladed heritage tool of the Indonesian "
            "archipelago - a machete-like blade traditionally carried for "
            "work in field and forest, and preserved in pencak silat "
            "schools as a heritage weapon of deep cultural meaning. In the "
            "heritage curriculum the golok is studied through form: grip, "
            "cutting angles, flowing transitions, and the respectful "
            "handling rituals passed down with the blade. Training uses "
            "wooden or blunted practice blades exclusively - never a live "
            "edge - and every session opens with safety protocol: clear "
            "space, checked equipment, and a teacher present. The golok "
            "teaches commitment like no empty-hand technique can: the "
            "blade's weight punishes hesitation and rewards the same hip-"
            "driven, whole-body motion that powers the punches. Its place "
            "in silat is cultural heritage first - a link to the ancestors "
            "who carried it daily - and its practice honors that lineage.",
        "how_it_works":
            "Train only with a wooden or blunted practice golok, never a "
            "live blade. Begin each session with the safety check: clear "
            "training space in all directions, practice blade inspected, "
            "teacher present. Learn the grip: firm handshake hold with the "
            "thumb along the spine side, wrist straight. Practice the "
            "fundamental cuts slowly in the air - downward diagonal, upward "
            "diagonal, and horizontal - each powered by hip rotation and "
            "langkah stepping, never by arm alone. Flow between cuts "
            "without stopping, keeping the blade's path always known and "
            "controlled. Drill ten slow cuts per angle, then link them into "
            "a short heritage form. Treat the practice blade with the same "
            "respect as a live one: that discipline is the lesson.",
        "key_points": [
            "Category: heritage weapons - cultural lineage of the blade.",
            "Training uses wooden or blunted practice blades only, never live.",
            "Safety protocol opens every session: space, equipment, teacher.",
            "Fundamental cuts: downward diagonal, upward diagonal, horizontal.",
            "Hip rotation and langkah power the cut, never the arm alone.",
            "The blade's path stays known and controlled at all times.",
            "Respect for the practice blade is itself the lesson.",
        ],
        "requirements": [
            "Wooden or blunted practice golok - never a live edge.",
            "Large clear space; teacher present at every session.",
            "Safety check ritual before any blade handling.",
        ],
        "standards": [
            "Traditional aliran heritage weapons protocol (golok).",
            "Heritage practice: practice blades only, supervised always.",
        ],
        "citations": [CIT_DRAEGER, CIT_MARYONO, CIT_UNESCO],
        "sig_lens":
            "Through the Signature lens, the golok is the heavy signature "
            "of the ancestors: a stroke with weight behind it, written "
            "slowly in practice wood, honoring every hand that held the "
            "blade before.",
    },
    {
        "key": "karambit",
        "name": "Karambit (Curved Blade Heritage)",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description":
            "The karambit is the small curved blade of Minangkabau heritage "
            "in West Sumatra - a claw-shaped knife with a finger ring at "
            "the pommel, originally modeled on the tiger's claw and carried "
            "as a farming tool. In pencak silat heritage it is studied as "
            "a close-range cultural weapon: the ring locks the blade to "
            "the hand so it cannot be dropped, and the curve extends the "
            "natural hooking motions of the empty hand - the same arcs as "
            "siku and tangkapan, now given an edge. Heritage training uses "
            "wooden or blunted trainers exclusively and focuses on flow "
            "drills, grip transitions, and the respectful handling the "
            "blade's lineage demands. The karambit's lesson is precision: "
            "its short reach punishes every wasted motion, teaching the "
            "student that in close range, the smallest correct movement "
            "defeats the largest wild one.",
        "how_it_works":
            "Train only with a wooden or blunted karambit trainer, never a "
            "live blade, with clear space and a teacher present. Learn the "
            "standard grip: index finger through the ring, blade curving "
            "forward from the bottom of the fist. Practice the hooking "
            "flow slowly in the air: small arcs that mirror siku and "
            "tangkapan, the blade extending the hand's natural hooks. "
            "Drill grip transitions - shifting between forward and reverse "
            "holds - ten times per side without rushing. Then practice the "
            "heritage flow form: hooking arcs linked with langkah and "
            "elakan, always slow, always controlled, the trainer's path "
            "known at every instant. End each session by wiping down and "
            "storing the trainer respectfully.",
        "key_points": [
            "Category: heritage weapons - the claw blade of Minangkabau lineage.",
            "Finger ring locks the blade to the hand.",
            "Curve extends the natural hooks of siku and tangkapan.",
            "Trainers only: wooden or blunted, never a live edge.",
            "Grip transitions drilled slowly, ten per side.",
            "Short reach punishes wasted motion; precision is the lesson.",
            "Respectful handling and storage close every session.",
        ],
        "requirements": [
            "Wooden or blunted karambit trainer - never a live blade.",
            "Clear space; teacher present.",
            "Patience: flow before speed, always.",
        ],
        "standards": [
            "Traditional Minangkabau heritage weapons protocol (karambit).",
            "Heritage practice: trainers only, supervised always.",
        ],
        "citations": [CIT_DRAEGER, CIT_MARYONO, CIT_UNESCO],
        "sig_lens":
            "Through the Signature lens, the karambit is the signature's "
            "flourish made steel: the tiger's claw curled around the "
            "finger, teaching that the smallest true stroke outweighs the "
            "wildest swing.",
    },
    {
        "key": "main-bawah",
        "name": "Main Bawah (Ground Fighting)",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description":
            "Main bawah - playing low, the ground game - is pencak silat's "
            "study of fighting from and on the ground. Silat's low stances "
            "already live near the floor, so the art's ground work grows "
            "naturally from its sweeps and throws: the practitioner who "
            "sweeps learns to follow the partner down, control the fall, "
            "and finish with pins, locks, or a safe disengagement. The "
            "curriculum covers breakfalls in every direction, ground "
            "mobility (shrimping, bridging, technical stand-up), positional "
            "control from the dominant positions, and the kuncian locks "
            "adapted for the ground. Defense leads the syllabus: how to "
            "fall without injury, how to protect the head, how to stand "
            "back up safely - because the ground is where the untrained "
            "get hurt. Students drill main bawah on thick mats with "
            "patient partners, learning that the floor is not defeat but "
            "another stance.",
        "how_it_works":
            "Begin on thick mats with breakfalls: back fall, side fall, "
            "and front fall, ten of each, slapping the mat with the arm to "
            "spread the impact and tucking the chin always. Next, ground "
            "mobility: shrimp ten lengths by bridging the hips and sliding "
            "them back, then bridge ten times lifting the hips high. Then "
            "the technical stand-up: from sitting, post one hand behind, "
            "bring one foot to the floor, and rise to kuda-kuda while the "
            "free hand guards - never stand up square to the partner. "
            "Finally, positional drill with a partner: start from the side "
            "control position, hold for a ten-count while they try gently "
            "to escape, then switch. All ground work stays slow and "
            "cooperative until breakfalls are automatic.",
        "key_points": [
            "Category: ground - the floor is another stance.",
            "Breakfalls first: back, side, and front, chin tucked always.",
            "Ground mobility: shrimping, bridging, technical stand-up.",
            "Never stand up square to the partner.",
            "Positional control precedes any lock or finish.",
            "Kuncian locks adapt to the ground from standing study.",
            "Thick mats, patient partners, slow before live.",
        ],
        "requirements": [
            "Thick mats covering the whole training area.",
            "Patient, communicative ground partner.",
            "Teacher supervision for all positional drilling.",
        ],
        "standards": [
            "IPSI extended curriculum groundwork (main bawah).",
            "Traditional aliran safety: breakfalls before ground sparring.",
        ],
        "citations": [CIT_MARYONO, CIT_IPSI],
        "sig_lens":
            "Through the Signature lens, main bawah is the signature "
            "written lying down: the floor the page turned sideways, the "
            "breakfall the pen that never breaks, the stand-up the hand "
            "rising to write again.",
    },
    {
        "key": "keris",
        "name": "Keris (Dagger Heritage)",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description":
            "The keris is the storied wavy-bladed dagger of the Indonesian "
            "archipelago - a weapon, a status symbol, and a spiritual "
            "heirloom, its blade often forged in layered pamor patterns "
            "that smiths read like writing. In pencak silat heritage the "
            "keris is studied with the deepest respect: its curriculum "
            "covers the ceremonial handling, the sheathed and drawn forms, "
            "the close-range thrusting angles, and the cultural protocols "
            "that surround it - how it is worn, presented, and stored. "
            "Training uses wooden or blunted trainers exclusively; the "
            "heritage forms are practiced slowly as moving meditation, "
            "each thrust an exhale, each withdrawal an inhale. The keris "
            "teaches the final lesson of the blade arts: that the weapon "
            "is a responsibility before it is a technique, and that true "
            "mastery is shown in restraint. Its study is as much cultural "
            "education as martial training.",
        "how_it_works":
            "Train only with a wooden or blunted keris trainer, never a "
            "live blade, with a teacher present and clear space. Learn the "
            "ceremonial grip: handshake hold with the thumb braced along "
            "the hilt, blade aligned with the forearm. Practice the "
            "drawing ritual slowly: withdraw the trainer from its sheath "
            "with the edge turned safely away, salute, and return it - ten "
            "repetitions of pure protocol. Then the heritage thrusting "
            "form: step with langkah depan and extend the trainer in a "
            "straight thrust powered by the hip, exhaling, then withdraw "
            "with an inhale. Drill ten slow thrusts per side, the motion "
            "meditative and exact. Study the pamor patterns and wearing "
            "customs with your teacher: the culture is half the curriculum.",
        "key_points": [
            "Category: heritage weapons - the dagger of layered steel and culture.",
            "Wavy blade often forged in pamor patterns read like writing.",
            "Trainers only: wooden or blunted, never a live edge.",
            "Ceremonial handling, drawing ritual, and storage protocols.",
            "Thrusting form practiced slowly as moving meditation.",
            "The weapon is a responsibility before it is a technique.",
            "Cultural education is half the curriculum.",
        ],
        "requirements": [
            "Wooden or blunted keris trainer with sheath.",
            "Teacher of the heritage lineage for protocols.",
            "Quiet, respectful training space.",
        ],
        "standards": [
            "Traditional heritage protocol for keris study.",
            "UNESCO 2019: keris heritage within pencak silat traditions.",
        ],
        "citations": [CIT_DRAEGER, CIT_MARYONO, CIT_UNESCO],
        "sig_lens":
            "Through the Signature lens, the keris is the signature folded "
            "into steel: layered pamor the handwriting of the smith, the "
            "slow thrust the breath of the practitioner, restraint the "
            "finest line ever drawn.",
    },
    {
        "key": "jurus-senjata",
        "name": "Jurus Senjata (Weapon Form)",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description":
            "Jurus senjata is the weapon form of pencak silat - the solo "
            "sequence performed with toya, golok trainer, karambit trainer, "
            "or keris trainer, archiving the weapon's entire technique "
            "library in flowing motion. Like the empty-hand tunggal, the "
            "weapon form weaves strikes, blocks, transitions, and footwork "
            "into one unbroken performance, but the weapon adds unforgiving "
            "feedback: a staff that wobbles, a grip that slips, or a line "
            "that wanders is visible to every watcher. IPSI judges weapon "
            "forms in the artistic categories, scoring correctness, "
            "fluidity, power, and the performer's command of the weapon's "
            "character. For the student, the weapon form is the final "
            "examination of body awareness - the practitioner must know "
            "where every inch of the weapon is at every instant, which "
            "means knowing where every inch of the body is. It is practiced "
            "slowly for years before it is ever performed fast.",
        "how_it_works":
            "Choose one trainer - rattan staff is the traditional first "
            "weapon - and learn the form in four-movement sections as with "
            "the empty-hand tunggal: teacher demonstrates, you mirror "
            "slowly, ten repetitions per section before adding the next. "
            "Check every grip change in a mirror; the weapon must never "
            "wobble or pause mid-transition. Breathe with the form: exhale "
            "on every strike and thrust, inhale on recoveries. Practice the "
            "full sequence slowly for precision, then at performance tempo. "
            "Time it: most weapon forms run sixty to one hundred twenty "
            "seconds. Drill the full form three times per session, then "
            "isolate the weakest transition for ten more repetitions. "
            "Perform for your teacher only when the weapon feels like an "
            "extension of the hands.",
        "key_points": [
            "Category: forms - the weapon's library archived in motion.",
            "Performed with toya, golok, karambit, or keris trainers.",
            "The weapon gives unforgiving feedback on every error.",
            "Learn in four-movement sections; ten reps each.",
            "Every grip change checked; the weapon never wobbles.",
            "IPSI artistic category: correctness, fluidity, power, character.",
            "Slow for years before ever performing fast.",
        ],
        "requirements": [
            "Chosen trainer and ample clear space.",
            "A teacher to transmit the form exactly.",
            "Mirror for checking grip changes and lines.",
        ],
        "standards": [
            "IPSI artistic category: jurus senjata performance standards.",
            "Traditional aliran standard: the weapon as extension of the hand.",
        ],
        "citations": [CIT_DRAEGER, CIT_MARYONO, CIT_IPSI, CIT_UNESCO],
        "sig_lens":
            "Through the Signature lens, jurus senjata is the signature "
            "written with a pen that never lies: every wobble visible, "
            "every true line beautiful, the weapon the honest mirror of "
            "the hand.",
    },
    {
        "key": "patahan",
        "name": "Patahan Terkendali (Controlled Locking Study)",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description":
            "Patahan terkendali - the controlled breaking study - is the "
            "advanced discipline of taking joint locks to their full "
            "mechanical conclusion in theory while practicing them with "
            "absolute control in reality. Patahan means breaking, and the "
            "traditional schools study exactly how each lock in the kuncian "
            "family would complete: which direction the joint travels, "
            "where its structural limit lies, and why control must stop "
            "far short of it. This knowledge is taught only to trusted "
            "advanced students, and only alongside an iron safety ethic: "
            "the study exists so the practitioner understands the "
            "technique's gravity, never to practice injury on a partner. "
            "Every patahan drill ends the instant before pressure becomes "
            "danger, the partner taps, and both practitioners bow. The "
            "lesson of the tenth rank is restraint: to hold the full "
            "knowledge of the lock and choose, every time, to release it.",
        "how_it_works":
            "Study only under a senior teacher with a trusted partner, on "
            "mats, after years of kuncian practice. The teacher demonstrates "
            "a wrist lock's full mechanical path on their own arm first, "
            "naming each degree of travel and marking the safe training "
            "limit far short of the joint's end. Partners then drill the "
            "lock's entry and control phase slowly - never approaching the "
            "limit - with the receiver tapping at the first firm pressure "
            "and the applier releasing instantly. Each session studies one "
            "joint: wrist, then elbow, then shoulder, across many weeks. "
            "The teacher quizzes the student on the joint's anatomy and "
            "the exact safe limit before any new lock is touched. The "
            "drill is complete when the student can name the limit, "
            "demonstrate the control, and release on a whisper of a tap.",
        "key_points": [
            "Category: advanced controls - the full mechanics of the lock.",
            "Studies where each lock's structural limit lies, in theory.",
            "Practice stops far short of any limit, always.",
            "Taught only to trusted advanced students by senior teachers.",
            "The tap - even a whisper - means instant release.",
            "One joint per study block across many weeks.",
            "Restraint is the tenth-rank lesson: hold the knowledge, choose release.",
        ],
        "requirements": [
            "Senior teacher and a deeply trusted partner.",
            "Mats; unhurried, quiet training environment.",
            "Years of kuncian practice as prerequisite.",
            "Anatomy study of each joint before touching it.",
        ],
        "standards": [
            "Traditional aliran advanced safety code (patahan terkendali).",
            "Master-level ethic: knowledge obligates restraint.",
        ],
        "citations": [CIT_MARYONO],
        "sig_lens":
            "Through the Signature lens, patahan terkendali is the "
            "signature the master chooses not to finish: the full stroke "
            "known, the pen lifted deliberately, restraint the most "
            "advanced technique of all.",
    },
    {
        "key": "aliran",
        "name": "Aliran (Style Lineage Study)",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description":
            "Aliran - the stream or flow - is the study of pencak silat's "
            "style lineages: the hundreds of distinct schools across the "
            "Indonesian archipelago and Malaysia, each with its own jurus, "
            "its own kembangan character, and its own philosophy. Cimande "
            "of West Java is famed for its close-range efficiency; "
            "Minangkabau silek for its low, deceptive ground play; Betawi "
            "maen pukulan for its powerful hand work; Perisai Diri, Tapak "
            "Suci, and Merpati Putih among the great modern perguruan with "
            "national followings. The advanced student studies aliran the "
            "way a scholar studies literature: learning the history, the "
            "founders, the signature techniques, and the character of each "
            "stream, then training respectfully within one while honoring "
            "all. Lineage is traced teacher to student, and the student's "
            "duty is to carry the stream forward unpolluted - to add their "
            "own understanding without damming the flow.",
        "how_it_works":
            "Begin the study with your teacher's own lineage: record the "
            "names of your teacher, their teacher, and as many generations "
            "back as are known, with the founding story of the aliran. "
            "Then study three contrasting streams from texts and "
            "documented demonstrations - for example Cimande, Minangkabau "
            "silek, and a modern perguruan - noting each one's signature "
            "stances, favored techniques, and philosophy in a training "
            "journal. Attend a seminar or demonstration of a different "
            "aliran each year, participating respectfully as a guest. "
            "Finally, write your own aliran statement: what your stream "
            "teaches, what it forbids, and what you will carry forward. "
            "The study never ends; the stream keeps flowing.",
        "key_points": [
            "Category: mastery - the streams of the art across the archipelago.",
            "Hundreds of aliran, each with its own jurus and character.",
            "Cimande, Minangkabau silek, Betawi maen pukulan among the famed.",
            "Great modern perguruan include Perisai Diri and Tapak Suci.",
            "Lineage traced teacher to student, generation to generation.",
            "Record your lineage; study three contrasting streams.",
            "Carry the stream forward unpolluted: add, never dam.",
        ],
        "requirements": [
            "A teacher who can name their own lineage.",
            "Training journal for lineage and comparative study.",
            "Access to texts, demonstrations, and seminars.",
        ],
        "standards": [
            "Traditional standard: know your teacher's teacher.",
            "UNESCO 2019: the diversity of aliran as living heritage.",
        ],
        "citations": [CIT_MARYONO, CIT_DRAEGER, CIT_UNESCO],
        "sig_lens":
            "Through the Signature lens, aliran is the river the Signature "
            "swims in: countless streams, one water, and the student's duty "
            "to keep their own stream clear for those who will drink "
            "downstream.",
    },
    {
        "key": "ujian",
        "name": "Ujian Kenaikan Tingkat (Grading and Mastery)",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description":
            "Ujian kenaikan tingkat - the rank advancement examination - is "
            "pencak silat's formal measure of the journey from first stance "
            "to mastery. Candidates demonstrate the full ladder before a "
            "panel of teachers: kuda-kuda held to exhaustion, jurus "
            "performed with precision and spirit, sambutan exchanges "
            "against resisting partners, and the heritage knowledge of "
            "their aliran recited from memory. But the examination "
            "measures character as much as technique: patience with "
            "juniors, respect for opponents, honesty about one's limits, "
            "and the restraint that the patahan study demands. Many schools "
            "mark ranks with colored belts or sashes, yet the masters "
            "insist the true rank is invisible - it shows in how the "
            "practitioner treats the beginner, the defeated, and the art "
            "itself. The tenth rank of this database is therefore not an "
            "ending but a commission: the graduate is charged to teach, "
            "to preserve, and to sign the art forward.",
        "how_it_works":
            "Prepare for grading over months, not weeks: the panel will "
            "test stance endurance (five minutes in kuda-kuda tengah), the "
            "complete jurus tunggal of your level performed twice, "
            "sambutan exchanges against three different partners, and an "
            "oral examination on your aliran's history and safety codes. "
            "Train each component on a schedule: stances daily, jurus three "
            "times per session, exchanges twice weekly, oral study nightly. "
            "In the week before, taper intensity and sleep well - the panel "
            "reads fatigue as poor preparation. On the day, arrive early, "
            "warm up fully, bow to the panel, and perform each requirement "
            "with full spirit whether or not you feel ready. Whatever the "
            "result, thank the panel and return to training the next day: "
            "the grade measures a moment, the art measures a lifetime.",
        "key_points": [
            "Category: mastery - the formal measure of the journey.",
            "Tests technique, heritage knowledge, and character together.",
            "Stance endurance, jurus precision, live exchanges, oral exam.",
            "Prepare over months; taper and rest the final week.",
            "Character counts equally: patience, respect, honesty, restraint.",
            "The true rank is invisible - shown in conduct, not color.",
            "Graduation is a commission: teach, preserve, sign forward.",
        ],
        "requirements": [
            "Months of structured preparation across all components.",
            "A panel of qualified teachers for the examination.",
            "Training journal documenting the preparation.",
        ],
        "standards": [
            "IPSI grading syllabus (ujian kenaikan tingkat).",
            "Traditional perguruan standard: character examined with technique.",
        ],
        "citations": [CIT_IPSI, CIT_MARYONO],
        "sig_lens":
            "Through the Signature lens, ujian kenaikan tingkat is the "
            "Signature witnessed and countersigned: the panel the "
            "witnesses, the candidate's life the document, and the "
            "commission to teach the seal pressed into wax.",
    },
]
