#!/usr/bin/env python3
"""Entries for the Eskrima Kali Arnis Combat Database (combat batch 2).

Verified 2026-10-17 (combat batch 2): RAW SWEEP over the full manifest plus
every shard index title in jah-databases-data-1: zero 'combat-eskrima*'
slugs/names; zero title collisions on all 34 public titles and all 34
Signature-suffixed titles (dedupe_gate check over the whole system before
authoring, 0 refusals). Civilian training scope only: stick, blade, and
empty-hand technique instruction with body mechanics; nothing on
neutralizing or defeating military or defense-grade systems.

This build creates two NEW databases, 34 ladder-ordered records each:

  combat-eskrima-kali-arnis            - The Eskrima Kali Arnis Combat
                                        Database (public-harvest: real,
                                        fact-checked Filipino martial arts
                                        knowledge - single and double stick,
                                        blade work, empty-hand translation,
                                        disarms, triangle footwork - every
                                        record carrying how-to body
                                        mechanics, real Filipino terminology
                                        with translations, and working
                                        training calculators; standard
                                        references Wiley Filipino Martial
                                        Culture 1997, Wiley Filipino Fighting
                                        Arts 2000, Inosanto The Filipino
                                        Martial Arts 1980, Presas Modern
                                        Arnis 1983, Sulite Masters of Arnis
                                        Kali and Eskrima 1994, Galang
                                        Complete Sinawali 2000)
  combat-eskrima-kali-arnis-signature - The Eskrima Kali Arnis Combat
                                        Signature Database
                                        (his original Signature Combat
                                        Method: the weapon as the teacher,
                                        the angle as the lesson, the
                                        triangle as the path; src signature,
                                        titles suffixed " (Signature
                                        Edition)", never presented as
                                        authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBEKA- (public) and JAH-CBEKAS- (signature), verified free
in the manifest id_prefix values and in every shard index (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_eskrima_kali_arnis.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Combat Method: the "
            "weapon as the teacher, the angle as the lesson, the triangle as "
            "the path. Clearly labeled Signature-made, never presented as "
            "authentic public record.")

CIT_WILEY97 = ("Wiley MV. Filipino Martial Culture. Charles E. Tuttle "
               "Company; 1997.")
CIT_WILEY00 = ("Wiley MV. Filipino Fighting Arts: Theory and Practice. "
               "Unique Publications; 2000.")
CIT_INOSANTO = ("Inosanto D. The Filipino Martial Arts. Know Now "
                "Publishing; 1980.")
CIT_PRESAS = ("Presas R. Modern Arnis: The Filipino Art of Stick Fighting. "
              "Black Belt Books; 1983.")
CIT_SULITE = ("Sulite EG. Masters of Arnis, Kali and Eskrima. Paladin "
              "Press; 1994.")
CIT_GALANG = ("Galang R. Complete Sinawali: Filipino Double Weapon "
              "Fighting. Charles E. Tuttle Company; 2000.")

STD_SAFETY = ("Training safety: protective equipment for any partner "
              "contact; controlled contact only in sparring; blade work "
              "begins with trainers, never live edges.")
STD_WEAPON_FIRST = ("Weapon-first pedagogy: the weapon teaches the angle, "
                    "the angle translates to the empty hand; empty-hand "
                    "technique derives from weapon technique, never the "
                    "reverse.")
STD_ANGLES = ("Angle discipline: every strike and block is named by its "
              "angle number; partner drills synchronize on the shared "
              "numbered system.")
STD_FOOTWORK = ("Footwork first: the feet deliver the weapon; no strike "
                "lands without the step that carries it.")

ENTRIES = [
    {
        "key": "what_is",
        "name": "What Eskrima, Kali, and Arnis Are",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "sig_lens": ("Through the Signature lens, the three names are one "
                     "covenant of motion: the weapon as the teacher, the "
                     "angle as the lesson, the triangle as the path. The "
                     "Signature practitioner studies the stick first because "
                     "the stick is honest - it reaches where the hand cannot "
                     "and it forgives the beginner. Every later record in "
                     "this archive is one branch of that covenant."),
        "description": (
            "Eskrima, Kali, and Arnis are the blade-rooted martial arts of "
            "the Philippines, taught weapon-first where most arts begin with "
            "the empty hand. The names carry history: Eskrima comes from the "
            "Spanish esgrima, fencing, and Arnis from arnes, harness or "
            "armor; Kali is the older indigenous name many Filipino masters "
            "use for the pre-colonial art. The core idea is weapon "
            "translation: a stick stands in for the sword, the angles that "
            "work with the stick work with the blade, and the angles that "
            "work with the blade work with the empty hand. So the art "
            "teaches one numbered angle system - twelve basic striking "
            "angles - and reuses it across the stick, the knife, the sword, "
            "and the hands. Footwork runs on triangles: forward, retreat, "
            "and sidestepping patterns that move the fighter off the line "
            "of attack while loading the next strike. Partner drills such "
            "as sinawali, hubud-lubud, and sombrada build timing and "
            "sensitivity instead of memorizing hundreds of fixed forms. "
            "Major lineages include Doce Pares Eskrima, Modern Arnis, and "
            "the Inosanto blending of Filipino arts. This record frames "
            "the whole database: weapon, angle, triangle, drill."
        ),
        "how_it_works": (
            "Training works by stacking four layers in order. First comes "
            "the weapon: the beginner holds a rattan stick and learns to "
            "move it without hurting the training partner. Second comes "
            "the angle: twelve numbered strikes and their defenses, drilled "
            "slowly until the numbers become reflex. Third comes the "
            "footwork: triangle stepping patterns that carry the weapon "
            "into range and carry the fighter out of danger. Fourth comes "
            "the drill: partner patterns that feed attacks and defenses in "
            "a loop, building the sensitivity to feel an opening instead "
            "of thinking about it. Empty-hand technique is translated last, "
            "because the weapon has already taught the angles and the "
            "timing. A training session opens with solo angle repetitions, "
            "adds footwork to the angles, then pairs up for a flow drill, "
            "and finishes with controlled sparring when the student is "
            "ready. Everything is numbered and repeatable, so two "
            "practitioners who have never met can flow together from the "
            "numbers alone."
        ),
        "key_points": [
            "One art, three names: Eskrima (from esgrima, fencing), Arnis (from arnes, harness), and Kali (the older indigenous name) describe the same Filipino weapon-first family.",
            "Weapon translation is the heart of the system: learn the twelve angles with the stick and they carry to the blade and then to the empty hand.",
            "Angles replace memorized forms: numbered strikes and blocks synchronize partners and scale to any weapon.",
            "Triangle footwork moves the fighter off the attack line while loading the next strike - the feet deliver the weapon.",
            "Partner flow drills (sinawali, hubud-lubud, sombrada) build timing and sensitivity; control always comes before contact.",
        ],
        "requirements": [
            "An open training space with clear floor and room to swing a stick without hitting walls or partners.",
            "One rattan training stick per student, 26 to 30 inches long, plus tape for marking and repair.",
            "A training partner once the basic angles are known; solo work comes first.",
            "Protective equipment before any partner contact: headgear, hand protection, and body padding.",
            "Respect for the weapon: sticks and especially blades are training tools, never toys.",
        ],
        "standards": [STD_WEAPON_FIRST, STD_SAFETY, STD_ANGLES],
        "citations": [CIT_WILEY97, CIT_WILEY00, CIT_INOSANTO],
    },
    {
        "key": "the_stick",
        "name": "The Stick: Baston, Yantok, and Rattan",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "sig_lens": ("Through the Signature lens, the stick is the first "
                     "covenant: a length of rattan that stands in for the "
                     "sword and keeps the beginner safe while the angles "
                     "sink in. The Signature practitioner chooses one stick "
                     "and trains it like an oath - same length, same weight, "
                     "until the hand forgets the stick and remembers only "
                     "the line."),
        "description": (
            "The baston - also called olisi in Cebuano and yantok when it "
            "is rattan - is the training weapon of Eskrima, Kali, and "
            "Arnis. Rattan is the traditional material because it is light, "
            "flexible, and honest: it bruises before it breaks, and when it "
            "does break it splinters into fibers instead of shattering into "
            "sharp shards the way hardwood can. A training stick runs 26 "
            "to 30 inches long with a diameter near one inch, light enough "
            "to swing fast for hundreds of repetitions yet heavy enough to "
            "teach the wrist to snap. Hardwoods like kamagong exist for "
            "advanced and demonstration work, but beginners train rattan "
            "because partner drills demand a forgiving material. The stick "
            "is a stand-in: in the old training it represents the sword "
            "(espada), so every angle learned with the stick is an angle "
            "already learned for the blade. Care matters: wipe the stick "
            "down, oil rattan lightly to slow drying, tape splits early, "
            "and retire a stick that has cracked through. Two matched "
            "sticks open the double-stick work later in the ladder."
        ),
        "how_it_works": (
            "The stick works as an extension of the forearm, adding reach "
            "and leverage to the same angles the empty hand will later use. "
            "A 28-inch stick plus a 28-inch arm puts the striking tip about "
            "four and a half feet from the shoulder, which is why the art "
            "trains distance management as seriously as striking. In partner "
            "work the stick is the safe surrogate: two practitioners can "
            "trade full-speed angles with rattan and protective gear, "
            "something no one can do with live blades. The material science "
            "is practical: rattan fibers compress on impact and spring "
            "back, spreading the strike over a slightly longer moment and "
            "reducing peak force on the partner compared with rigid wood. "
            "The punyo, the butt end of the stick, doubles as a close-range "
            "weapon for hammering and hooking once the grip is learned. "
            "Choosing a stick is choosing a training partner for the hand: "
            "match the length to the arm, keep the pair matched, and let "
            "the stick teach the angle through repetition."
        ),
        "key_points": [
            "Rattan (yantok) is the standard training wood: light, flexible, and it splinters instead of shattering, which keeps partner drills safe.",
            "The stick is the sword in disguise: 26 to 30 inches of rattan teaches blade angles without blade consequences.",
            "Length plus arm equals reach: a 28-inch stick on a 28-inch arm puts the tip about four and a half feet from the shoulder.",
            "The punyo, the butt end, is a second weapon for close hammering, hooking, and disarms.",
            "Maintain the stick: oil lightly, tape splits early, retire cracked sticks, keep double-stick pairs matched.",
        ],
        "requirements": [
            "Two rattan sticks, 26 to 30 inches long, matched in length and weight for double-stick work.",
            "Athletic tape for marking grips and repairing early splits.",
            "Light oil (coconut or mineral) to slow rattan drying and cracking.",
            "A storage spot out of direct sun and damp, standing or lying flat.",
            "A retired-stick bin: cracked sticks leave the training floor, never return to partner drills.",
        ],
        "standards": [STD_SAFETY, STD_WEAPON_FIRST],
        "citations": [CIT_PRESAS, CIT_INOSANTO, CIT_WILEY00],
    },
    {
        "key": "the_grip",
        "name": "The Grip: Holding the Stick Right",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "sig_lens": ("Through the Signature lens, the grip is the oath of "
                     "the hand: firm enough to command, loose enough to "
                     "listen. The Signature practitioner grips at the "
                     "moment of impact and releases between strikes, "
                     "because a clenched hand is a deaf hand, and the stick "
                     "must whisper its warnings back through the palm."),
        "description": (
            "The grip is the first technique and the last one: every angle, "
            "block, and disarm begins and ends in the hand. The standard "
            "grip is a firm handshake hold with the thumb braced along or "
            "across the stick, the wrist straight, and the stick seated in "
            "the fingers rather than buried in the palm. Power rule: grip "
            "loosely while the stick travels and tighten only at the moment "
            "of impact. A constant death grip tires the forearm in minutes, "
            "slows the wrist snap that generates speed, and makes the stick "
            "easy to strip because a rigid hand cannot adjust. The loose "
            "travel also protects the partner: a relaxed swing can be "
            "checked mid-flight, a white-knuckle swing cannot. Grip length "
            "matters: choke up for close work and disarms, slide to the "
            "end for maximum reach. The thumb position decides the punyo: "
            "with the thumb clear, the butt end protrudes for hammering "
            "and hooking. Beginners should expect forearm burn in the first "
            "weeks; that burn is the wrist extensors waking up, and it "
            "fades as the grip learns to breathe."
        ),
        "how_it_works": (
            "The grip works as a clutch, not a clamp. During the swing the "
            "fingers hold just enough that centrifugal force seats the "
            "stick against the palm; the wrist stays supple so the snap at "
            "the end of the strike adds tip speed that muscle alone cannot "
            "produce. At impact the fingers close for a fraction of a "
            "second, making the hand, stick, and forearm one rigid lever "
            "that transfers energy into the target instead of rattling the "
            "wrist. Then the hand opens back to its traveling grip. This "
            "cycle - loose, snap, tighten, release - repeats hundreds of "
            "times in a session and is drilled deliberately: ten strikes "
            "gripped correctly beat a hundred muscled through a locked "
            "fist. Against disarms, the living grip wins: because the hand "
            "is already adjusting pressure hundreds of times a minute, it "
            "feels the strip beginning and can re-seat the stick before the "
            "lever completes. Train it with slow-motion shadow strikes, "
            "watching the fingers open and close, until the clutch runs on "
            "its own."
        ),
        "key_points": [
            "Hold the stick like a handshake: thumb braced, wrist straight, stick seated in the fingers.",
            "Loose on the travel, tight at impact: the clutch cycle generates snap and protects the wrist.",
            "A death grip is a slow grip: constant tension tires the forearm, kills wrist speed, and invites disarms.",
            "Grip length is range control: choke up for close work, slide to the end for maximum reach.",
            "The living grip resists strips because a hand already adjusting pressure feels the disarm beginning.",
        ],
        "requirements": [
            "One rattan stick and a mirror or video camera to check thumb and wrist alignment.",
            "Ten minutes of slow shadow striking daily for the first month: speed hides grip faults.",
            "A partner drill at quarter speed once the clutch feels automatic.",
            "Forearm and wrist conditioning: the extensors need the first weeks of burn to adapt.",
            "Patience: the grip is re-checked at every ladder rank; it is never finished.",
        ],
        "standards": [STD_WEAPON_FIRST, STD_SAFETY],
        "citations": [CIT_PRESAS, CIT_INOSANTO],
    },
    {
        "key": "stance_handa",
        "name": "Stance and the Ready Position (Handa)",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "sig_lens": ("Through the Signature lens, handa is the still point "
                     "of the covenant: knees soft, breath low, weapon ready "
                     "but not eager. The Signature practitioner stands ready "
                     "the way a door stands ready - closed but not locked, "
                     "able to open in any direction the moment the angle "
                     "demands it."),
        "description": (
            "Handa means ready, and the ready position is the stance every "
            "technique launches from and returns to. The feet sit about "
            "shoulder width apart, one foot leading on the weapon side, "
            "knees soft and bent, weight settled low with roughly sixty "
            "percent on the rear leg and forty on the lead. The weapon hand "
            "extends toward the opponent at about chest height, the live "
            "hand - the empty hand - rides up near the chin or the weapon "
            "forearm, ready to check, parry, or grab. The chin tucks, the "
            "shoulders relax, and the eyes watch the opponent's chest and "
            "shoulders rather than the weapon, because the body telegraphs "
            "before the stick moves. The low center of gravity does three "
            "jobs: it anchors strikes so the hips can rotate into them, it "
            "lets the fighter explode forward or slip back without a "
            "preparatory bounce, and it keeps the fighter upright when a "
            "block lands hard. Beginners stand too tall and too square; "
            "the correction is always the same: sink an inch, blade the "
            "body, bring the live hand home."
        ),
        "how_it_works": (
            "The stance works as a loaded spring pointed at the opponent. "
            "With the knees bent and the weight back, the rear leg can "
            "drive the hips forward into a strike - the famous hip "
            "rotation that puts body weight behind the stick - while the "
            "lead leg is already light enough to step. The extended weapon "
            "hand measures distance: if the tip cannot reach, the feet "
            "must move first, which enforces the footwork-first habit. The "
            "live hand position is functional, not decorative: held high "
            "it can slap down an incoming strike (a check), held near the "
            "weapon arm it can brace a block, and from either place it is "
            "one motion from grabbing the opponent's wrist. Returning to "
            "handa after every strike is drilled as strictly as the "
            "strikes themselves, because the fighter is most vulnerable in "
            "the half-second after attacking. The stance is checked by a "
            "partner's push: a correct handa absorbs a shove at the "
            "shoulder without stepping; a tall stance topples."
        ),
        "key_points": [
            "Handa means ready: feet shoulder width, weapon-side foot leading, knees bent, weight about 60 percent rear and 40 percent lead.",
            "The weapon hand extends to measure distance; the live hand rides high to check, parry, or grab.",
            "Watch the chest and shoulders, not the stick: the body telegraphs before the weapon moves.",
            "A low stance anchors hip rotation into strikes and lets the fighter explode in any direction without telegraphing.",
            "Return to handa after every strike: the half-second after attacking is the most dangerous moment.",
        ],
        "requirements": [
            "A flat floor and a mirror or partner to check posture.",
            "Five minutes of static handa holds daily to build the leg endurance the stance demands.",
            "A stick for the weapon-hand position; the live hand stays empty.",
            "A partner push test weekly: absorb a shoulder shove without stepping.",
            "Comfortable flat shoes or bare feet; no raised heels, which pitch the weight forward.",
        ],
        "standards": [STD_FOOTWORK, STD_SAFETY],
        "citations": [CIT_PRESAS, CIT_WILEY00, CIT_SULITE],
    },
    {
        "key": "angles_1_5",
        "name": "The Five Basic Angles (Numerado 1-5)",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "sig_lens": ("Through the Signature lens, the first five angles "
                     "are the first five letters of the covenant: diagonal "
                     "down, diagonal back, horizontal across, horizontal "
                     "return, and the thrust that writes the final line. "
                     "The Signature practitioner drills them until the "
                     "numbers vanish and only the lines remain."),
        "description": (
            "Numerado is the numbered angle system, and angles one through "
            "five are the alphabet of the art. Angle 1 is the forehand "
            "diagonal strike downward, from the weapon-side shoulder toward "
            "the opposite hip - the most natural swing a beginner owns. "
            "Angle 2 is its mirror: the backhand diagonal downward from the "
            "opposite shoulder to the weapon-side hip. Angle 3 is the "
            "forehand horizontal strike across the body at chest height. "
            "Angle 4 is the backhand horizontal return at the same height. "
            "Angle 5 is the thrust, the stick driven straight forward like "
            "a spear, usually aimed at the face, throat, or solar plexus. "
            "These five are drilled first because they cover the four "
            "quadrants of the target plus the centerline, and because every "
            "partner drill in the system feeds and answers in these "
            "numbers. Each angle names both an attack and the defense "
            "against it: knowing angle 1 means knowing how it is thrown and "
            "how it is blocked. Targets are taught by line: the diagonals "
            "fall on the head, collarbone, and ribs; the horizontals on the "
            "temple, neck, and ribs; the thrust on the face and torso."
        ),
        "how_it_works": (
            "The angles work by giving every strike a number, a line, and "
            "a partner answer. The beginner stands in handa, steps with the "
            "strike, and throws angle 1 by rotating the hips and snapping "
            "the wrist so the stick travels from high on the weapon side to "
            "low on the far side in one clean diagonal. The return stroke - "
            "angle 2 - chambers naturally at the end of angle 1, which is "
            "why the art drills them in pairs: every strike loads its "
            "opposite. Angles 3 and 4 teach the horizontal plane and the "
            "wrist roll that keeps the stick flat through the swing. Angle "
            "5, the thrust, teaches the lunge: the rear leg drives, the "
            "body drops slightly, and the stick extends in a straight line "
            "with the thumb on top guiding the point. In partner work the "
            "feeder calls or simply throws angle 1 and the defender "
            "answers with the angle-1 block, so both sides learn the same "
            "geometry. Ten clean repetitions of each angle per side, "
            "returning to handa between strikes, builds the foundation "
            "everything later stands on."
        ),
        "key_points": [
            "Angles 1 and 2 are the diagonal pair: forehand down from the weapon shoulder, backhand down from the far shoulder.",
            "Angles 3 and 4 are the horizontal pair at chest height: forehand across, backhand return.",
            "Angle 5 is the thrust: a straight spear-line to the face or torso, driven by the rear leg.",
            "Every angle is both an attack and a defense: learn the number and you learn its answer.",
            "Step with the strike and return to handa between repetitions: the feet and the guard are part of the angle.",
        ],
        "requirements": [
            "Solid handa stance and grip; the angles are built on both.",
            "One rattan stick; a mirror or video to check the diagonal lines.",
            "A training partner once the solo lines are clean, starting at quarter speed.",
            "Ten repetitions per angle per session minimum; the alphabet needs daily writing.",
            "Tape marks on a heavy bag or tire stack for target lines once solo form is clean.",
        ],
        "standards": [STD_ANGLES, STD_FOOTWORK, STD_SAFETY],
        "citations": [CIT_PRESAS, CIT_INOSANTO, CIT_GALANG],
    },
    {
        "key": "angles_6_12",
        "name": "Angles Six Through Twelve",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "sig_lens": ("Through the Signature lens, angles six through twelve "
                     "complete the covenant of the circle: the rising cuts, "
                     "the falling cuts, the low lines, and the overhead that "
                     "closes the book. The Signature practitioner treats "
                     "the full twelve as one wheel - no angle is exotic, "
                     "every angle is a spoke, and the wheel turns the same "
                     "in either hand."),
        "description": (
            "Angles six through twelve complete the numerado, the full "
            "twelve-angle circle that covers the target from every line. "
            "The commonly taught continuation runs: angle 6, the upward "
            "diagonal from the low backhand side; angle 7, the upward "
            "diagonal from the low forehand side - the rising cuts that "
            "answer low attacks. Angle 8, the downward vertical on the "
            "backhand side; angle 9, the downward vertical on the forehand "
            "side - the falling chops. Angle 10, the forehand strike to the "
            "low line, and angle 11, its backhand mirror, targeting the "
            "knee, shin, and ankle. Angle 12 is the straight overhead "
            "strike, the crown cut. Numbering varies between systems and "
            "lineages - some schools order the low and rising cuts "
            "differently - which is why partners always confirm the "
            "numbering before drilling. Together the twelve divide the "
            "space around the target into roughly thirty-degree sectors, "
            "so any incoming line has a name and a numbered answer. The "
            "low angles teach a vital lesson: drop the level by bending "
            "the knees, never by bowing the head toward the strike."
        ),
        "how_it_works": (
            "The upper angles work by completing the defensive circle. "
            "Where angles 1 through 5 cover the high and middle lines, the "
            "rising cuts of 6 and 7 intercept low-line attacks by meeting "
            "them from below with the strong part of the stick, and the "
            "low strikes of 10 and 11 teach the fighter to attack the "
            "legs that carry the opponent. The verticals, 8 and 9, are "
            "drilled with a dropping step: the fighter sinks the weight as "
            "the stick falls, adding body mass to the chop. Angle 12, the "
            "overhead, is the commitment strike - powerful, but it opens "
            "the body, so it is drilled with an immediate return to guard "
            "or a follow-up angle. In partner flow the feeder walks through "
            "all twelve in order while the defender answers each with its "
            "numbered block, which builds the complete vocabulary: after "
            "this drill there is no line of attack the defender has never "
            "seen. The full twelve are then drilled in broken rhythm - the "
            "feeder calling numbers out of order - so the answers become "
            "recognition rather than sequence memory."
        ),
        "key_points": [
            "Angles 6 and 7 are the rising cuts: upward diagonals that intercept low-line attacks.",
            "Angles 8 and 9 are the falling verticals: drilled with a dropping step that adds body mass to the chop.",
            "Angles 10 and 11 attack the low line - knee, shin, ankle - by bending the knees, never bowing the head.",
            "Angle 12 is the straight overhead: powerful but committing, always followed by an immediate guard return.",
            "Confirm numbering with any new partner: lineage variations exist, and the numbers must match before drilling.",
        ],
        "requirements": [
            "Clean angles 1 through 5; the upper angles layer onto the alphabet, they do not replace it.",
            "One rattan stick and a partner who has confirmed the same numbering.",
            "Knee mobility for the level drops; warm the knees and hips before low-line work.",
            "A heavy bag or tire stack for the overhead and vertical chops at full power.",
            "Protective gear before any partner feeding above half speed.",
        ],
        "standards": [STD_ANGLES, STD_SAFETY, STD_FOOTWORK],
        "citations": [CIT_PRESAS, CIT_INOSANTO, CIT_SULITE],
    },
    {
        "key": "footwork_sulong",
        "name": "Footwork I: The Forward Triangle (Sulong)",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "sig_lens": ("Through the Signature lens, the forward triangle is "
                     "the first path of the covenant: two steps that close "
                     "distance while stepping off the line of the enemy "
                     "blade. The Signature practitioner walks the triangle "
                     "until the feet move before the thought, because the "
                     "weapon is useless if the feet arrive late."),
        "description": (
            "Sulong means to advance, and the forward triangle is the "
            "footwork pattern that carries the fighter into range without "
            "walking into the attack. Picture a triangle on the floor with "
            "its point facing the opponent. The fighter stands at the rear "
            "base, steps to the left point or the right point, and from "
            "there can step to the front point - closing distance while "
            "moving off the centerline. This is the male triangle, point "
            "forward. The genius of the pattern is that the stepping foot "
            "never crosses the centerline blindly: each step lands outside "
            "the opponent's lead, so the advance is also an evasion. The "
            "triangle is walked slowly at first - step, settle, check "
            "balance - then paired with angle 1 and angle 2, so the strike "
            "lands exactly as the stepping foot plants. Filipino masters "
            "insist the feet are trained before the hands are trusted: a "
            "perfect strike thrown from dead feet arrives late and "
            "underpowered. Chalk or tape triangles on the floor make the "
            "pattern visible; the goal is to wear the pattern into the "
            "legs until the advance is automatic."
        ),
        "how_it_works": (
            "The forward triangle works by splitting the advance into two "
            "angled steps instead of one straight one. A straight step "
            "forward walks directly into the opponent's power line; the "
            "triangle's first step moves diagonally to the outside, "
            "slipping the opponent's lead weapon, and the second step "
            "drives to the front point with the hips already loaded for "
            "the strike. Body mechanics: the rear leg pushes, the weight "
            "transfers in a straight line between the triangle points, the "
            "knees stay bent so the head does not bob up into a target, "
            "and the stepping foot lands heel-toe quietly - a slapping "
            "step telegraphs. Paired with striking, the timing rule is "
            "step-then-strike or strike-with-step, never strike-then-step: "
            "the foot must be planted to anchor the hip rotation. In "
            "partner work the feeder holds a stick extended and the "
            "advancer practices stepping to each point of the triangle "
            "without touching it, learning to judge distance by the body "
            "instead of the eyes. Three sets of ten triangles per side, "
            "then triangles with angles 1 through 5, is the classic "
            "progression."
        ),
        "key_points": [
            "The male triangle points at the opponent: base at the rear, front point as the destination.",
            "Two angled steps replace one straight step: the advance is also an evasion off the centerline.",
            "Step to the outside of the opponent's lead: never cross the power line blindly.",
            "Strike with the step or just after it lands: the planted foot anchors the hip rotation.",
            "Chalk the triangle on the floor and walk it until the legs know it without the eyes.",
        ],
        "requirements": [
            "A clear floor and chalk or tape to mark a triangle about two feet per side.",
            "Flat shoes or bare feet; bent knees throughout - the drill fails if the legs straighten.",
            "Solid handa stance; the triangle launches from and returns to the ready position.",
            "One stick once footwork is clean; feet first, then feet plus angles.",
            "A patient partner to hold the distance stick for range judgment.",
        ],
        "standards": [STD_FOOTWORK, STD_SAFETY],
        "citations": [CIT_WILEY00, CIT_INOSANTO, CIT_PRESAS],
    },
    {
        "key": "labtik",
        "name": "The Twelve Basic Strikes (Labtik)",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "sig_lens": ("Through the Signature lens, labtik is the covenant "
                     "made loud: twelve lines written on the air until the "
                     "body can write them in the dark. The Signature "
                     "practitioner strikes the tire stack the way a writer "
                     "fills pages - daily, completely, and without "
                     "apology - because power that is not practiced is "
                     "only a rumor."),
        "description": (
            "Labtik means to strike, and the twelve basic strikes are the "
            "numerado angles thrown with full body mechanics at real "
            "targets. Knowing the angle lines is geometry; labtik is "
            "physics: hip rotation, weight transfer, wrist snap, and "
            "follow-through combining into strikes that can break a grip, "
            "deaden a limb, or stop an advance. The targets follow the "
            "lines: the diagonals fall on the head, collarbone, elbow, and "
            "ribs; the horizontals on the temple, neck, and floating ribs; "
            "the thrust on the face and solar plexus; the low angles on "
            "the knee and ankle. The art's signature target is the weapon "
            "hand itself - defanging the snake - striking the hand that "
            "holds the weapon so the threat ends without needing to reach "
            "the body. Strikes are thrown through the target, not at it: "
            "the stick continues six inches past the contact line, which "
            "keeps the power from dying at the surface. Power comes from "
            "the ground up: rear foot drives, hips rotate, shoulder "
            "follows, elbow extends, wrist snaps. The arm alone is the "
            "weakest link in that chain."
        ),
        "how_it_works": (
            "A full-power strike works as a kinetic chain. The rear leg "
            "drives against the floor, the hips rotate toward the target, "
            "the torso follows, the shoulder whips, the elbow extends, and "
            "the wrist snaps in the final inches - each link adding speed "
            "that the next link multiplies. At the contact instant the "
            "grip tightens, making hand, stick, and forearm a single lever, "
            "then releases as the stick follows through. The fighter steps "
            "with the strike so the body mass travels into the target; a "
            "strike thrown from planted, dead feet is all arm and no "
            "weight. Training runs in three modes: shadow striking for "
            "form, bag or tire work for power, and partner feeding for "
            "timing. On the tire stack the student learns the sound of a "
            "correct strike - a sharp crack rather than a dull thud - and "
            "the feel of the stick rebounding cleanly instead of jarring "
            "the wrist. The defanging strike is drilled as a precise "
            "angle-1 or angle-3 to the partner's extended stick hand at "
            "controlled speed, building the accuracy that makes the "
            "technique humane: ending the fight by removing the weapon, "
            "not by reaching the body."
        ),
        "key_points": [
            "Power is a chain: rear foot to hips to torso to shoulder to elbow to wrist snap; the arm alone is the weakest link.",
            "Strike through the target, not at it: follow six inches past the contact line.",
            "Defang the snake: the weapon hand is the primary target - remove the weapon and the threat ends.",
            "Step with the strike: body mass must travel into the target; dead feet make arm-only strikes.",
            "Three training modes: shadow for form, tires or bags for power, partner feeding for timing.",
        ],
        "requirements": [
            "Clean twelve angles; power layered onto bad lines only builds bad habits faster.",
            "A tire stack or heavy bag for full-power work - never full power on a partner.",
            "Wrist and forearm conditioning; the snap loads the wrist extensors heavily.",
            "Protective gear and a controlled partner for defanging accuracy drills.",
            "A training log: count strikes per session and watch the crack replace the thud.",
        ],
        "standards": [STD_ANGLES, STD_SAFETY, STD_FOOTWORK],
        "citations": [CIT_PRESAS, CIT_SULITE, CIT_WILEY00],
    },
    {
        "key": "footwork_atras",
        "name": "Footwork II: The Retreat Triangle (Atras)",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "sig_lens": ("Through the Signature lens, the retreat triangle is "
                     "the covenant kept wisely: stepping back is not "
                     "surrender, it is reloading. The Signature practitioner "
                     "retreats on the triangle the way a wave retreats - "
                     "gathering itself for the return - and the opponent "
                     "who chases the wave meets the rock."),
        "description": (
            "Atras means to retreat, and the retreat triangle is the "
            "footwork that carries the fighter out of danger without "
            "giving up structure. It is the female triangle: the point "
            "faces backward, and the fighter steps from the front point "
            "back to the left or right rear points. The cardinal rule is "
            "never retreat in a straight line: backing straight up keeps "
            "the fighter on the opponent's power line and usually ends "
            "with a stumble over the trailing foot. The triangle's angled "
            "steps slip the fighter off the line while creating the "
            "distance a block or counter needs. The retreat is active, not "
            "panicked: the weapon stays between the fighter and the "
            "threat, the eyes stay on the opponent, and the rearward step "
            "loads the hips for the counter that follows - the classic "
            "draw, where the fighter invites the chase and answers it. "
            "Retreating on the triangle also protects the knees: angled "
            "steps keep the joints stacked under the hips, while straight "
            "backward scrambling twists them. Drilled with a partner "
            "advancing on the forward triangle, the two triangles lock "
            "together like gears: one advances, one retreats, and the "
            "distance between the fighters stays constant."
        ),
        "how_it_works": (
            "The retreat triangle works by converting backward motion into "
            "an angle. As the opponent advances, the fighter steps the "
            "lead foot back and out to one rear point of the triangle, "
            "the body blading slightly, the weapon hand checking the "
            "centerline. The second step brings the rear foot to the other "
            "rear point, re-squaring the stance at the new distance. "
            "Because each step moves diagonally, the fighter leaves the "
            "attack's line while staying balanced enough to block, and "
            "because the steps are short the fighter never crosses the "
            "feet - the classic cause of retreat falls. The counter is "
            "built into the pattern: the rearward step that loads the "
            "hips becomes the forward drive of the answering strike, so "
            "retreat and counter are one motion, not two. In partner "
            "drilling the advancer walks the forward triangle throwing "
            "slow angles while the retreater walks the retreat triangle "
            "answering with blocks, keeping a constant two-stick distance. "
            "Speed comes last: first the pattern, then the pattern with "
            "blocks, then the pattern with the counter that punishes the "
            "chase."
        ),
        "key_points": [
            "The female triangle points backward: angled steps replace the dangerous straight-line retreat.",
            "Never cross the feet and never back straight up: both habits end in a fall.",
            "The weapon stays between fighter and threat; the eyes never leave the opponent.",
            "The retreat loads the counter: the backward step becomes the forward drive of the answer.",
            "Drill it geared with a partner's forward triangle: advance and retreat keeping constant distance.",
        ],
        "requirements": [
            "Clean forward triangle; the retreat mirrors it and is learned second.",
            "Chalk or tape female triangle on the floor, point facing away.",
            "A partner to advance slowly while the student retreats with blocks.",
            "Knee-friendly footwear and a smooth floor; the angled steps must glide, not stick.",
            "Protective gear before the counter-strike phase of the drill.",
        ],
        "standards": [STD_FOOTWORK, STD_SAFETY],
        "citations": [CIT_WILEY00, CIT_INOSANTO],
    },
]

ENTRIES.extend([
    {
        "key": "defensa",
        "name": "Blocking: The Four Basic Defenses (Defensa)",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "sig_lens": ("Through the Signature lens, the block is the "
                     "covenant of the shield: the stick rises not to stop "
                     "the storm but to turn it aside. The Signature "
                     "practitioner defends the way water defends against a "
                     "stone - yielding at the angle that sends the force "
                     "past, never meeting it head-on."),
        "description": (
            "Defensa is the blocking system, and the four basic defenses "
            "answer the four families of incoming angles. The outside "
            "block (sangga) meets forehand strikes with the stick held "
            "vertical on the outside of the body. The inside block answers "
            "backhand strikes with the stick vertical on the inside. The "
            "roof or umbrella block (payong, meaning umbrella) raises the "
            "stick horizontal above the head against overhead and diagonal "
            "attacks. The cross-block crosses stick and live hand before "
            "the body against thrusts and close strikes. The governing "
            "principle is deflection over interception: the block meets "
            "the incoming stick at an angle and slides it offline, because "
            "meeting force head-on with a one-inch stick is a contest the "
            "block usually loses. Blocks are thrown with the body, not the "
            "arm: the hips rotate into the block, the step carries the "
            "fighter slightly offline, and the live hand braces or checks "
            "to support the stick. Every block ends loaded for the "
            "counter - the blocking motion chambers the answering strike, "
            "so defense and offense are one continuous movement."
        ),
        "how_it_works": (
            "A block works by redirecting energy, not absorbing it. The "
            "defender reads the incoming angle from the attacker's "
            "shoulder and hip, steps slightly offline on the triangle, and "
            "presents the stick so the incoming weapon strikes its strong "
            "third - the section nearest the hand - at roughly a "
            "forty-five-degree meeting angle. At that angle the attack "
            "slides off instead of driving through, and the defender's "
            "wrist survives the impact. The live hand supports by checking "
            "the attacker's weapon arm or bracing the blocking stick, "
            "adding a second point of structure. Timing decides "
            "everything: block too early and the attacker redirects around "
            "it; block too late and the strike is already home. Training "
            "runs feeder-and-answer: the partner throws angle 1 at quarter "
            "speed and the student answers with the outside block, then "
            "the speed climbs in stages. The payong is drilled against "
            "overhead feeds until raising the roof is reflexive. The final "
            "test is the counter: every block in the drill must flow "
            "immediately into its answering strike, because a block that "
            "does not produce a counter only postpones the problem."
        ),
        "key_points": [
            "Four defenses answer four angle families: outside block, inside block, roof block (payong), and cross-block.",
            "Deflect, do not catch: meet the incoming stick at an angle and slide it offline.",
            "Block with the body: hips rotate, the step moves slightly offline, the live hand braces or checks.",
            "Meet force with the strong third of the stick, the section nearest the hand.",
            "Every block chambers its counter: defense that does not produce offense only postpones the problem.",
        ],
        "requirements": [
            "Clean angles 1 through 5 on both sides; the blocks mirror the strikes.",
            "A patient feeder partner; blocking cannot be learned solo.",
            "Protective gear: headgear and hand protection before any feeding above quarter speed.",
            "One rattan stick each; the feeder uses controlled, committed feeds, never wild swings.",
            "Footwork basics: the block steps offline, so the triangles must be walking already.",
        ],
        "standards": [STD_ANGLES, STD_SAFETY, STD_FOOTWORK],
        "citations": [CIT_PRESAS, CIT_INOSANTO, CIT_SULITE],
    },
    {
        "key": "abaniko",
        "name": "The Abaniko: The Fan Strike",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "sig_lens": ("Through the Signature lens, the abaniko is the "
                     "covenant of the wrist: a fan of strikes that opens "
                     "and closes like a breath. The Signature practitioner "
                     "fans the stick at close range where long swings die, "
                     "because the wrist is the last weapon to tire and the "
                     "first to arrive."),
        "description": (
            "Abaniko means fan, and the fan strike is the wrist-driven "
            "strike that fans the stick back and forth in a tight arc. "
            "Where the twelve angles are arm-and-hip strikes for medium "
            "range, the abaniko is the close-range answer: when the "
            "opponent crowds in and long swings have no room, the wrist "
            "takes over. The basic abaniko runs horizontally, the stick "
            "snapping from forehand to backhand and back in a fanning "
            "motion powered almost entirely by wrist rotation. The short "
            "abaniko (abaniko corto) works in a tight arc for "
            "chest-to-chest distance; the long abaniko (abaniko largo) "
            "opens the arc for the edge of close range. Targets are the "
            "temple, the side of the neck, the ribs, and the weapon hand - "
            "places where even a short-arc strike lands with meaning. The "
            "technique demands a conditioned wrist: beginners feel the "
            "extensors complain within a minute, and the conditioning is "
            "built gradually with short daily sets. The fan is also a "
            "defensive tool: fanned continuously, the stick becomes a "
            "moving wall that is hard to enter."
        ),
        "how_it_works": (
            "The abaniko works by replacing the arm swing with wrist "
            "rotation. The elbow stays nearly fixed near the ribs, the "
            "forearm acts as the fan's handle, and the wrist rotates "
            "rapidly so the stick tip sweeps a wide arc while the hand "
            "barely moves. Because the moving mass is small - just the "
            "hand and stick - the direction can reverse in a fraction of "
            "a second, producing the characteristic back-and-forth fanning "
            "that can land two or three strikes in the time of one full "
            "swing. The power comes from the snap at each end of the arc "
            "and from the slight body drop that adds weight; it will not "
            "match a full angle-1 for raw force, but at trapping distance "
            "there is no room for a full angle 1 anyway. Training starts "
            "with slow, wide fans to groove the wrist path, then narrows "
            "and quickens the arc. The wall drill - fanning continuously "
            "while a partner probes with slow feeds - teaches the "
            "defensive fan: the moving stick intercepts the probing weapon "
            "before it reaches the body. Ten thirty-second sets daily "
            "build the wrist within a month."
        ),
        "key_points": [
            "The abaniko is wrist-powered: the elbow stays near the ribs while the wrist fans the stick back and forth.",
            "Close-range answer: where long swings have no room, the fan still strikes.",
            "Short abaniko for chest-to-chest distance; long abaniko for the edge of close range.",
            "The continuous fan is also a moving wall: hard to enter, dangerous to grab.",
            "Condition gradually: short daily sets build the wrist extensors; rushing causes strain.",
        ],
        "requirements": [
            "A conditioned grip; the fan loads the wrist far more than the twelve angles.",
            "One rattan stick; no partner needed for the first two weeks of wall-and-mirror work.",
            "A mirror to check the arc stays tight and the elbow stays home.",
            "Thirty-second sets with full rest between; stop at sharp wrist pain, never push through it.",
            "Protective hand gear before any partner probing against the fan.",
        ],
        "standards": [STD_SAFETY, STD_WEAPON_FIRST],
        "citations": [CIT_INOSANTO, CIT_WILEY00],
    },
    {
        "key": "solo_drills",
        "name": "Solo Baston Drills: Shadow Striking",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "sig_lens": ("Through the Signature lens, shadow striking is the "
                     "covenant kept in solitude: the practitioner faces the "
                     "invisible opponent and fights honestly, because the "
                     "shadow never flatters. The Signature practitioner "
                     "shadows daily, and the empty air becomes the most "
                     "honest training partner of all."),
        "description": (
            "Solo baston drills - shadow striking with the stick - are the "
            "daily practice that turns the angles from knowledge into "
            "reflex. The practitioner faces an imagined opponent and "
            "throws the twelve angles in sequence, in broken order, and in "
            "combination, always with footwork: every strike steps, every "
            "combination moves. The value of solo work is honesty: no "
            "partner compensates for a dropped guard, a lazy wrist, or "
            "dead feet, so the mirror or the video camera becomes the "
            "teacher. A standard session runs the twelve angles ten times "
            "each, then the five basic blocks against imagined feeds, then "
            "free combinations - angle 1 into angle 2 into abaniko into "
            "thrust - while walking the triangles. Advanced solo work adds "
            "the sinawali patterns shadowed with two sticks and footwork "
            "spirals: figure-eight stepping that turns the fighter while "
            "striking. The old masters say the art is learned in the "
            "hours no one watches; the solo drill is where the angles "
            "become the practitioner's own instead of the teacher's. Ten "
            "focused minutes daily beats one sloppy hour weekly."
        ),
        "how_it_works": (
            "Shadow striking works by grooving the complete strike "
            "package - stance, step, hip, snap, guard return - without the "
            "timing pressure of a partner. The brain learns the sequence "
            "as one chunk instead of five separate instructions, which is "
            "why the drill always includes the footwork and the return to "
            "handa: the chunk must contain the whole technique. Broken "
            "rhythm is the key progression: once the twelve flow in order, "
            "the practitioner calls numbers at random - 7, 3, 11, 5 - and "
            "throws each instantly, converting sequence memory into true "
            "recognition. Combination shadowing adds realism: no real "
            "exchange is one strike, so the drill chains three to five "
            "angles with direction changes, forcing the feet to keep "
            "delivering. Video review closes the loop: the practitioner "
            "films a session weekly and checks the lines against the "
            "angle chart, catching the drift that daily practice "
            "otherwise hides. The session ends with slow-motion "
            "repetitions - three perfect slow strikes per angle - which "
            "lock in the corrected form."
        ),
        "key_points": [
            "Shadow striking grooves the whole package - stance, step, hip, snap, guard return - as one chunk.",
            "The mirror and the camera are the teachers: solo work exposes what partners hide.",
            "Broken rhythm converts sequence memory into recognition: call numbers at random and throw instantly.",
            "Chain combinations with direction changes: real exchanges are never one strike.",
            "Finish slow: three perfect slow-motion strikes per angle lock in the corrected form.",
        ],
        "requirements": [
            "One rattan stick and enough clear space to swing fully in all directions.",
            "A mirror or a phone camera for form checks; film weekly at minimum.",
            "Clean twelve angles and triangle footwork; solo drills polish, they do not invent.",
            "A timer: ten focused minutes daily, structured as angles, blocks, combinations, slow finish.",
            "A training log noting which angles drifted and what the video showed.",
        ],
        "standards": [STD_ANGLES, STD_FOOTWORK],
        "citations": [CIT_PRESAS, CIT_WILEY00],
    },
    {
        "key": "sinawali",
        "name": "Sinawali: The Double-Stick Weave",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "sig_lens": ("Through the Signature lens, sinawali is the covenant "
                     "of two hands: the weave that teaches the left what "
                     "the right has always known. The Signature practitioner "
                     "weaves daily, because a fighter with two trained hands "
                     "has no weak side for the enemy to find."),
        "description": (
            "Sinawali means to weave, and the double-stick weave is the "
            "signature partner drill of the Filipino arts. Two "
            "practitioners face each other, each holding a stick in each "
            "hand, and trade strikes in a looping six-count pattern: right "
            "high forehand, left high backhand, right low, left low, right "
            "high backhand, left high forehand - each strike answered by "
            "the partner's matching block, the pattern flowing continuously "
            "like a weave on a loom. The drill develops what single-stick "
            "work cannot: both hands striking and defending independently, "
            "rhythm under pressure, and the peripheral awareness to track "
            "two weapons at once. It is traditionally the doorway to "
            "double-weapon fighting and to the empty-hand translations, "
            "because the coordination it builds transfers everywhere. "
            "Variations multiply from the base: heaven sinawali weaves "
            "overhead, low sinawali works the leg lines, and advanced "
            "players break the pattern into free exchanges. The cardinal "
            "rule is control: the sticks strike the partner's stick, never "
            "the partner, and the rhythm is a promise both sides keep."
        ),
        "how_it_works": (
            "Sinawali works by overloading the coordination system in a "
            "safe, predictable loop. The six-count pattern alternates "
            "hands and heights in a fixed cycle, so the beginner can "
            "memorize the sequence and then let the body run it while the "
            "mind watches - the classic drill state where learning "
            "happens fastest. The left hand, untrained in most people, "
            "catches up to the right through sheer repetition: hundreds of "
            "cycles per session. The partner's sticks provide moving "
            "targets and incoming timing, so the drill trains distance "
            "and rhythm, not just choreography. The teaching progression "
            "is strict: first shadow the pattern solo with two sticks, "
            "then walk it with a partner at slow speed counting aloud, "
            "then drop the counting, then add speed in stages, then add "
            "footwork - stepping the triangle while weaving. Breaking the "
            "pattern is the graduation: on a signal, one partner feeds a "
            "random angle and the other must answer from the weave, which "
            "converts the memorized loop into live recognition. Sticks "
            "must be matched in length and weight, or the rhythm stutters."
        ),
        "key_points": [
            "The six-count weave alternates hands and heights in a fixed loop: right high, left high, right low, left low, right backhand high, left forehand high.",
            "Both hands learn to strike and defend independently; the weak hand catches up through repetition.",
            "Sticks strike the partner's stick, never the partner: the rhythm is a promise both sides keep.",
            "Progression: solo shadow, slow counted partner work, uncounted flow, speed stages, footwork, pattern breaks.",
            "Sinawali is the doorway to double weapons and empty-hand translation: the coordination transfers everywhere.",
        ],
        "requirements": [
            "Two matched rattan sticks per practitioner; mismatched sticks break the rhythm.",
            "Clean single-stick angles 1 through 4; the weave is built from them.",
            "A partner of similar level; the drill is a duet, not a contest.",
            "Protective hand gear once speed rises above half.",
            "A large enough floor to add triangle stepping in the later stages.",
        ],
        "standards": [STD_SAFETY, STD_ANGLES, STD_WEAPON_FIRST],
        "citations": [CIT_GALANG, CIT_INOSANTO, CIT_WILEY00],
    },
    {
        "key": "heaven_six",
        "name": "Heaven Six Sinawali",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "sig_lens": ("Through the Signature lens, heaven six is the "
                     "covenant written overhead: the weave that guards the "
                     "crown while the hands learn to cross like swords "
                     "saluting. The Signature practitioner weaves the "
                     "heaven pattern until the head is the safest place on "
                     "the battlefield - because it is the best defended."),
        "description": (
            "Heaven six is the overhead sinawali pattern, named for the "
            "way the sticks weave across the sky above the practitioners' "
            "heads. Where the basic six-count works the high and low lines "
            "in front of the body, heaven six keeps the exchange in the "
            "upper zone: both partners trade looping overhead strikes - "
            "angle 1 and angle 2 descending, crossed and recrossed - in a "
            "continuous six-count that looks like a double helix turning "
            "above them. The pattern teaches the roof defense as a living "
            "thing: instead of one static payong block, the practitioner "
            "learns to keep a moving roof of steel - or rattan - over the "
            "head at all times. It also trains the crossing lines that "
            "appear in blade work, where overhead exchanges are common and "
            "a dropped guard is instantly punished. Footwork is added "
            "early in heaven six because the overhead zone invites "
            "circling: partners weave while stepping the triangle, "
            "learning to keep the roof intact while moving. The pattern "
            "demands relaxed shoulders - tension climbs into the neck when "
            "the arms stay overhead - so breathing and shoulder drops are "
            "coached explicitly."
        ),
        "how_it_works": (
            "Heaven six works by making the overhead zone a practiced "
            "neighborhood instead of a panic zone. The six-count cycles "
            "both sticks through descending diagonals that cross above "
            "the head; each strike is met by the partner's stick rising "
            "to meet it, so both practitioners are always simultaneously "
            "attacking and roofing. The crossing geometry trains the "
            "eyes to track two weapons converging overhead without "
            "flinching - the flinch is what drops the guard in real "
            "exchanges. The wrists do the fine work: small rotations at "
            "the top of each loop redirect the sticks into the next "
            "strike, keeping the pattern tight and fast. Shoulders must "
            "stay down and the breath steady; the drill is often practiced "
            "to a count or a song rhythm to enforce the breathing. The "
            "progression mirrors basic sinawali: solo shadow first, then "
            "slow counted partner weaving, then speed, then triangle "
            "footwork while weaving, then pattern breaks where one partner "
            "feeds a random overhead angle and the other answers from the "
            "flow. A clean heaven six at speed is one of the art's "
            "beautiful sights - and its most practical overhead defense."
        ),
        "key_points": [
            "Heaven six keeps the weave in the overhead zone: looping descending diagonals crossing above the head.",
            "It trains a moving roof instead of a static block: continuous overhead coverage.",
            "The crossing lines prepare for blade work, where overhead exchanges punish a dropped guard instantly.",
            "Relaxed shoulders and steady breath are coached explicitly; tension climbs into the neck overhead.",
            "Add triangle footwork while weaving: keep the roof intact while moving.",
        ],
        "requirements": [
            "Clean basic sinawali six-count; heaven six is its overhead sibling.",
            "Two matched sticks per practitioner and a partner.",
            "Shoulder warm-up and mobility work before every heaven session.",
            "High ceilings or outdoor space: the pattern needs overhead clearance.",
            "Headgear once speed rises; overhead exchanges deserve respect.",
        ],
        "standards": [STD_SAFETY, STD_ANGLES],
        "citations": [CIT_GALANG, CIT_INOSANTO],
    },
    {
        "key": "redonda",
        "name": "Redonda: The Circular Strike",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "sig_lens": ("Through the Signature lens, redonda is the covenant "
                     "of the circle: the strike that never stops, rolling "
                     "from one angle into the next like a wheel that "
                     "refuses the ground. The Signature practitioner turns "
                     "the redonda until stopping feels unnatural - because "
                     "a weapon in motion is a weapon that cannot be "
                     "caught."),
        "description": (
            "Redonda means round or circular, and the redonda is the "
            "continuous circular strike that never stops moving. Instead "
            "of the strike-recover-strike rhythm of the basic angles, the "
            "redonda rolls one strike into the next: a descending diagonal "
            "flows into a rising cut on the return, the wrist rolls, and "
            "the stick is already striking again without ever chambering. "
            "The classic redonda is thrown overhead and to the sides in a "
            "flattened circle, but the principle applies to any plane: "
            "keep the weapon in motion and let each strike's ending become "
            "the next strike's beginning. The technique builds the "
            "transition skill that separates beginners from fighters - "
            "most people can throw one good strike, but chaining five "
            "without a pause requires the wrist rolls and hip shifts the "
            "redonda drills. It is also a conditioning tool: two minutes "
            "of continuous redonda exhausts the shoulders and forearms "
            "faster than any other basic drill, which is exactly the "
            "stamina real exchanges demand. The double-stick redonda, both "
            "hands circling in opposite directions, is the graduation "
            "exercise."
        ),
        "how_it_works": (
            "The redonda works on momentum conservation. A normal strike "
            "spends its energy at the target and must be re-chambered; the "
            "redonda redirects the follow-through into the next strike's "
            "backswing, so the stick's motion is never wasted. The wrist "
            "is the steering wheel: a quarter-roll at the end of each arc "
            "turns the stick for the return cut, and the hips shift weight "
            "side to side to feed the circle. The practitioner starts with "
            "slow, wide circles on one side, feeling the moment the strike "
            "wants to stop and learning to roll through it instead. Speed "
            "builds in stages, and the circle tightens as control grows - "
            "a tight fast redonda is far more dangerous than a wide slow "
            "one, because the weapon is always near the target line. The "
            "partner drill feeds a slow angle and the student answers "
            "with a three-strike redonda instead of a single counter, "
            "learning to keep striking while the feeder resets. Breathing "
            "is rhythmic: exhale on each downward pass, never hold the "
            "breath during the spin."
        ),
        "key_points": [
            "The redonda never stops: each strike's follow-through becomes the next strike's backswing.",
            "The wrist roll steers the circle; the hips shift weight side to side to feed it.",
            "Transitions are the skill: chaining five strikes without pause separates fighters from beginners.",
            "Tight and fast beats wide and slow: keep the weapon near the target line.",
            "Double-stick redonda - both hands circling in opposition - is the graduation exercise.",
        ],
        "requirements": [
            "Clean twelve angles and a conditioned wrist; the circle loads both heavily.",
            "One rattan stick to start; two for the graduation double redonda.",
            "Open space with clearance on both sides; the circle is wide at first.",
            "Shoulder and wrist warm-up; two minutes of redonda is serious conditioning.",
            "A partner for the answer-with-redonda drill once the solo circle is stable.",
        ],
        "standards": [STD_ANGLES, STD_SAFETY],
        "citations": [CIT_INOSANTO, CIT_WILEY00, CIT_GALANG],
    },
    {
        "key": "hubud",
        "name": "Hubud-Lubud: Tie and Untie",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "sig_lens": ("Through the Signature lens, hubud-lubud is the "
                     "covenant of the knot: tie the opponent's arm, untie "
                     "your own, and never be the one who is bound. The "
                     "Signature practitioner ties and unties until the "
                     "hands think in knots - because the fighter who "
                     "controls the tie controls the fight."),
        "description": (
            "Hubud-lubud means tie and untie, and it is the sensitivity "
            "drill at the heart of close-range Filipino fighting. Two "
            "partners face each other: one feeds a straight punch or a "
            "slow angle-5 thrust, the other parries it across the body, "
            "traps it with the checking hand - the tie - and then unwraps, "
            "passing the arm aside and flowing into a counter - the untie. "
            "The cycle repeats, roles swapping, building the tactile "
            "sensitivity to feel an arm's pressure and direction instead "
            "of watching it. Where sinawali trains the eyes and the "
            "rhythm, hubud trains the hands: the light touch that reads "
            "intention through contact. The drill is the foundation of "
            "trapping - the momentary immobilization of the opponent's "
            "limb that opens the counter - and it translates directly to "
            "panantukan, gunting, and the empty-hand game. It is practiced "
            "soft: the feed is honest but controlled, the trap is a touch, "
            "not a yank, and the counter stops at the touch. Speed is "
            "earned over months; rushing hubud produces arm-wrestling, "
            "not sensitivity."
        ),
        "how_it_works": (
            "Hubud works by training the contact reflex. When the feeder's "
            "arm touches the defender's parry, the defender's hand reads "
            "pressure, angle, and commitment through the skin - "
            "information that arrives faster than vision. The tie is a "
            "light trap: the checking hand presses the feeding arm just "
            "enough to pin it for a beat while the other hand chambers the "
            "counter. The untie is the release: the trapped arm is passed "
            "aside along its weakest line - across the body, never into "
            "strength - and the counter flows into the opening. The "
            "sensitivity develops because the drill is continuous: feed, "
            "parry, tie, untie, counter, reset - hundreds of cycles per "
            "session, each one a small lesson in pressure. The teaching "
            "order is fixed: first the empty-hand pattern walked slowly "
            "with a cooperative feeder, then the same pattern with the "
            "feeder adding slight resistance, then the stick version where "
            "the feed is a slow thrust, then speed in careful stages. The "
            "test is the broken feed: the feeder occasionally throws the "
            "wrong attack, and the defender's hands must feel the change "
            "and adapt without thinking."
        ),
        "key_points": [
            "Hubud-lubud trains the hands, not the eyes: sensitivity to pressure and direction through contact.",
            "The tie is a light trap that pins the feeding arm for a beat; the untie passes it aside and counters.",
            "Pass along the weak line: across the body, never into the opponent's strength.",
            "Practice soft: honest feeds, touching traps, counters that stop at contact; rushing builds arm-wrestling, not sensitivity.",
            "The drill is the foundation of all trapping and translates directly to panantukan and gunting.",
        ],
        "requirements": [
            "A cooperative partner; hubud cannot be learned against resistance at first.",
            "Clean angle-5 defense and basic parrying; the tie builds on the parry.",
            "Empty hands to start; sticks enter only in the later stages.",
            "Patience measured in months: sensitivity is slow-cooked, never microwaved.",
            "A calm floor: frustration makes the hands heavy, and heavy hands learn nothing.",
        ],
        "standards": [STD_SAFETY, STD_WEAPON_FIRST],
        "citations": [CIT_INOSANTO, CIT_WILEY00],
    },
    {
        "key": "sombrada",
        "name": "Sombrada: Counter for Counter",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "sig_lens": ("Through the Signature lens, sombrada is the covenant "
                     "of the answer: every strike deserves a reply, and "
                     "every reply deserves a reply in turn. The Signature "
                     "practitioner counters the counter until the chain has "
                     "no end - because the fighter who owns the last "
                     "answer owns the exchange."),
        "description": (
            "Sombrada means countering, shade against shade, and it is the "
            "counter-for-counter drill that teaches the fighter to think "
            "one move ahead. The pattern is simple and deep: partner A "
            "feeds angle 1, partner B blocks and counters with angle 1, "
            "partner A blocks the counter and counters in turn, and the "
            "chain continues - strike, block, counter, block, counter - "
            "until someone chooses to break it. Unlike the fixed loops of "
            "sinawali, sombrada is conversational: each counter can change "
            "the angle, the target, or the rhythm, and the partner must "
            "read and answer in real time. The drill builds the two skills "
            "that decide real exchanges: reading intention - seeing the "
            "counter forming before it launches - and chaining offense "
            "from defense without a pause. Beginners run a fixed "
            "three-exchange chain; intermediate players vary the angles; "
            "advanced players break the pattern entirely, feeding fakes "
            "and drawing the counter they want. Control is sacred: the "
            "counters stop at the touch, and the drill resets the instant "
            "control slips."
        ),
        "how_it_works": (
            "Sombrada works by compressing the decision cycle. In a real "
            "exchange the fighter must perceive the attack, choose the "
            "block, and launch the counter in under half a second; "
            "sombrada rehearses exactly that loop hundreds of times per "
            "session. The fixed opening - always the same feed - lets the "
            "beginner automate the first block-and-counter, freeing "
            "attention for what comes next. As the chain extends, the "
            "fighter learns to read the partner's chamber: the slight hip "
            "shift or shoulder lift that announces which angle is coming. "
            "The advanced game is pattern-breaking: feed a convincing "
            "angle 1, read the partner's committed block, and answer with "
            "angle 3 to the newly opened line - the counter to the "
            "counter's counter. Teaching runs in stages: fixed three-count "
            "chains at slow speed, then variable angles within the chain, "
            "then free chains with agreed targets, then fakes and draws. "
            "The safety rule never changes: every counter is pulled at the "
            "touch, and anyone can call a reset by dropping the sticks to "
            "guard."
        ),
        "key_points": [
            "Sombrada is conversational: strike, block, counter, block, counter - each answer can change the angle or rhythm.",
            "It compresses the decision cycle: perceive, block, and counter in under half a second, rehearsed hundreds of times.",
            "Read the chamber: the hip shift and shoulder lift announce the coming angle before it launches.",
            "The advanced game is pattern-breaking: draw the counter you want, then answer the opened line.",
            "Counters stop at the touch; anyone can call a reset by dropping to guard.",
        ],
        "requirements": [
            "Clean blocks and counters from the defensa work; sombrada chains them.",
            "A trusted partner at matched level; the drill is only as safe as the wilder participant.",
            "Full protective gear: headgear, hands, body - counters fly at real speed.",
            "One rattan stick each; matched length keeps the geometry honest.",
            "An agreed stop signal and the discipline to honor it instantly.",
        ],
        "standards": [STD_SAFETY, STD_ANGLES],
        "citations": [CIT_INOSANTO, CIT_SULITE, CIT_WILEY00],
    },
    {
        "key": "tapi_tapi",
        "name": "Tapi-Tapi: Tapping and Clearing",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "sig_lens": ("Through the Signature lens, tapi-tapi is the "
                     "covenant of control: tap the enemy weapon aside "
                     "before writing your own line. The Signature "
                     "practitioner clears the path first and strikes "
                     "second, because a strike thrown into a guarded line "
                     "is a gift to the opponent."),
        "description": (
            "Tapi-tapi means tapping, and it is the art of controlling "
            "the opponent's weapon before striking. The core motion is "
            "small: as the opponent chambers or extends, the practitioner's "
            "stick taps the opponent's stick or weapon hand offline - a "
            "light, precise deflection - clearing a lane for the real "
            "strike that follows instantly. It is the difference between "
            "hitting a guarded target and hitting an open one. The tap is "
            "thrown with the wrist and the live hand working together: "
            "the stick taps high while the live hand checks low, or the "
            "reverse, so the opponent's weapon is managed on two lines at "
            "once. Tapi-tapi appears everywhere in the advanced game: in "
            "espada y daga the short weapon taps while the long weapon "
            "strikes, in blade work the tap keeps the edge off the "
            "centerline, and in empty-hand translation the tap becomes the "
            "parry that precedes the punch. The technique demands "
            "precision over power - a hard tap is just a block, and a "
            "missed tap is an invitation. Drilled against a partner's "
            "slow feeds, the tap must land in the window between the "
            "chamber and the launch."
        ),
        "how_it_works": (
            "Tapi-tapi works by attacking the opponent's timing instead of "
            "the opponent. A strike needs a clean launch line; the tap "
            "disrupts that line in the fraction of a second before launch, "
            "when the weapon is committed to its path but has not yet "
            "generated speed. The mechanics are minimal: a short wrist "
            "flick that contacts the opponent's stick near its tip - the "
            "weakest point of the lever - and pushes it a few inches "
            "offline. Those few inches are everything: the opponent must "
            "re-chamber or redirect, and in that beat the practitioner's "
            "real strike is already traveling. The live hand multiplies "
            "the effect by checking the opponent's weapon arm, pinning it "
            "for the instant the tap needs. Training starts with the "
            "partner feeding slow, predictable angles while the student "
            "practices tapping the tip offline and striking through the "
            "opened lane - tap-strike as one beat, not two. The advanced "
            "drill randomizes the feed and shortens the window until the "
            "tap becomes a reflex that fires on the chamber, not on the "
            "conscious decision."
        ),
        "key_points": [
            "Tapi-tapi controls the weapon before striking: tap it offline, then strike through the opened lane.",
            "Tap the tip, the weakest point of the lever: a few inches of deflection is enough.",
            "The window is the chamber: tap between commitment and launch, when the weapon cannot redirect.",
            "The live hand checks the weapon arm while the stick taps: two-line control.",
            "Tap-strike is one beat, not two: precision over power, reflex over decision.",
        ],
        "requirements": [
            "Clean basic angles and blocks; the tap is a refinement of the parry.",
            "A cooperative feeder starting slow; the timing window is small and must be learned gently.",
            "One rattan stick each and hand protection; tips get tapped near the hands.",
            "A mirror or video to check the tap stays a wrist flick, not an arm swing.",
            "Protective gear before the randomized-feed stage.",
        ],
        "standards": [STD_SAFETY, STD_ANGLES],
        "citations": [CIT_INOSANTO, CIT_WILEY00],
    },
])

ENTRIES.extend([
    {
        "key": "espada_y_daga",
        "name": "Espada y Daga: Stick and Knife",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "sig_lens": ("Through the Signature lens, espada y daga is the "
                     "covenant of the pair: the long weapon writes the "
                     "lines while the short weapon guards the margins. The "
                     "Signature practitioner wields the pair the way a "
                     "writer holds pen and ruler - one to create, one to "
                     "measure - and the live hand is never idle again."),
        "description": (
            "Espada y daga means sword and dagger, and in training it is "
            "practiced as stick and knife: the long weapon in the dominant "
            "hand, the short weapon - a training dagger - in the live "
            "hand. The pairing transforms the live hand from a checker "
            "into a weapon: the dagger parries, hooks, traps, and strikes "
            "at close range while the stick commands the longer lines. "
            "The classic coordination has the weapons working in "
            "opposition - when the stick strikes high, the dagger guards "
            "low - so the fighter is never open on both lines at once. "
            "The dagger's jobs are checking the opponent's weapon arm, "
            "hooking the opponent's stick to control it, and finishing at "
            "close range where the stick is too long to work. Footwork "
            "becomes more angular in espada y daga: the fighter closes to "
            "the dagger's range behind the stick's cover, strikes with "
            "both, and exits on the triangle. Training daggers are wood, "
            "aluminum, or rubber - never live steel until the far advanced "
            "stages, and many schools never use live steel in paired "
            "work at all. The drill foundation is the espada y daga "
            "sinawali: the same six-count weave, now with long and short "
            "weapons trading roles."
        ),
        "how_it_works": (
            "Espada y daga works by dividing the fight into two ranges "
            "managed simultaneously. The stick owns the long range: it "
            "strikes, blocks, and measures distance. The dagger owns the "
            "close range: it checks, hooks, and traps. The coordination "
            "rule is simple - the weapons never do the same job at the "
            "same time - which the practitioner learns through the paired "
            "sinawali: stick strikes angle 1 while the dagger checks low, "
            "then the roles trade. The dagger's hook is its signature "
            "move: catching the opponent's stick or wrist in the crook of "
            "the dagger arm and pulling it offline, which the stick then "
            "punishes. Entries are drilled as three-beat patterns: stick "
            "covers with a strike, step closes on the triangle, dagger "
            "checks and the stick follows through. The danger is fixation "
            "on the long weapon: beginners wave the stick and forget the "
            "dagger, so teachers run dagger-only rounds where the stick "
            "hand stays chambered. The graduation is the free exchange: "
            "both weapons live, both ranges open, the fighter switching "
            "jobs between hands without a pause."
        ),
        "key_points": [
            "The stick owns long range, the dagger owns close range; the weapons never do the same job at the same time.",
            "The dagger checks, hooks, and traps: it turns the live hand from a checker into a weapon.",
            "The hook is the signature move: catch the opponent's weapon in the dagger arm's crook and pull it offline.",
            "Entries run in three beats: stick covers, step closes on the triangle, dagger checks and the stick finishes.",
            "Train with wood, aluminum, or rubber daggers; live steel stays out of paired work.",
        ],
        "requirements": [
            "Clean single-stick angles and basic sinawali; the pairing layers onto both.",
            "One rattan stick and one training dagger (wood, aluminum, or rubber).",
            "A partner and full protective gear; two weapons double the contact points.",
            "Triangle footwork at walking speed with the pair before any speed.",
            "Dagger-only rounds to cure the beginner's fixation on the long weapon.",
        ],
        "standards": [STD_SAFETY, STD_WEAPON_FIRST, STD_FOOTWORK],
        "citations": [CIT_INOSANTO, CIT_WILEY00, CIT_SULITE],
    },
    {
        "key": "footwork_iii",
        "name": "Footwork III: Sidestepping and the Female Triangle",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "sig_lens": ("Through the Signature lens, the sidestep is the "
                     "covenant of the angle: refuse the straight road and "
                     "the enemy's strength passes by like weather. The "
                     "Signature practitioner steps to the dead side until "
                     "the opponent's power is always somewhere else - "
                     "because the fight is won by position before it is "
                     "won by strikes."),
        "description": (
            "The third footwork stage adds lateral movement: sidestepping "
            "triangles and the female triangle, the pattern whose point "
            "faces sideways or backward. Where the forward triangle closes "
            "and the retreat triangle escapes, the sidestep triangle "
            "repositions - moving the fighter to the opponent's dead side, "
            "the flank where the opponent's weapon cannot easily reach. "
            "The core drill is the sidestep-and-strike: as the partner "
            "feeds angle 1, the fighter steps diagonally left-forward to "
            "the outside of the attack, letting the strike pass, and "
            "answers with angle 2 into the newly exposed ribs. The female "
            "triangle extends the idea: stepping patterns that circle and "
            "pivot, keeping the fighter mobile in all directions instead "
            "of only forward and back. Zoning is the tactical payoff: by "
            "stepping to the outside of the opponent's lead, the fighter "
            "puts the opponent's own body between the opponent's rear "
            "weapons and the target. The footwork is drilled with the "
            "stick chambered first - pure stepping - then with the "
            "sidestep-strike, then in free flow where the feeder attacks "
            "from random angles and the student must step to the correct "
            "side every time."
        ),
        "how_it_works": (
            "Sidestepping works by changing the angle of the fight instead "
            "of contesting its force. A strike travels down a line; moving "
            "eighteen inches to the side removes the target from that "
            "line entirely, which costs less energy and less risk than any "
            "block. The mechanics: the step pushes from the inside foot, "
            "the body stays low and bladed, the head stays off the "
            "centerline, and the stick stays chambered until the new "
            "position is set - stepping while swinging is how fighters "
            "fall into counters. The dead side is the geometric goal: "
            "stepping to the outside of the opponent's weapon-side "
            "shoulder puts the fighter where the opponent must turn the "
            "whole body to re-aim, while the fighter's own weapon is "
            "already lined up. The female triangle patterns train the "
            "pivot: the fighter learns to rotate around the opponent's "
            "lead foot like a door around a hinge, which is the footwork "
            "behind many disarms. In free-flow drilling the feeder calls "
            "nothing; the student reads the incoming angle and steps to "
            "its outside, and the teacher corrects the side until the "
            "choice is instant."
        ),
        "key_points": [
            "Sidestepping changes the angle instead of contesting the force: eighteen inches sideways beats any block.",
            "Step to the dead side: outside the opponent's weapon shoulder, where re-aiming costs a full body turn.",
            "Push from the inside foot, stay low and bladed, keep the stick chambered until the step lands.",
            "The female triangle trains the pivot: rotate around the opponent's lead foot like a door around a hinge.",
            "Drill progression: pure stepping, sidestep-strike, then free flow against random feeds.",
        ],
        "requirements": [
            "Clean forward and retreat triangles; the sidestep is the third direction.",
            "Chalk triangles including lateral points; mark the dead-side positions.",
            "A feeder partner throwing slow, honest angles from the front.",
            "Flat, grippy footwear; the push step needs traction without sticking.",
            "Protective gear before the free-flow stage.",
        ],
        "standards": [STD_FOOTWORK, STD_SAFETY],
        "citations": [CIT_WILEY00, CIT_INOSANTO],
    },
    {
        "key": "panantukan",
        "name": "Panantukan: Empty-Hand Boxing",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "sig_lens": ("Through the Signature lens, panantukan is the "
                     "covenant fulfilled: the weapon dissolves and the "
                     "hand remembers everything it taught. The Signature "
                     "practitioner boxes with the angles still living in "
                     "the fists - because the stick was never the art, it "
                     "was only the teacher, and the lesson was always the "
                     "body."),
        "description": (
            "Panantukan - from suntok, to punch - is Filipino empty-hand "
            "boxing, the translation of the weapon angles into the fists, "
            "elbows, knees, and head. The principle is direct: angle 1 "
            "with the stick becomes the overhand or the elbow slash, "
            "angle 3 becomes the hook, angle 5 becomes the jab and the "
            "cross, the low angles become knees and kicks. Because the "
            "practitioner has already drilled these lines thousands of "
            "times with the stick, the empty-hand versions arrive with "
            "timing and targeting pre-installed - this is the famous "
            "weapon-first payoff. Panantukan is dirty by design: it "
            "includes the slap, the backfist, the elbow, the headbutt, and "
            "the limb destructions that target the opponent's attacking "
            "arms, all woven with the same trapping and checking the "
            "weapon game taught. The stance lowers and shortens: without "
            "the stick's reach, distance collapses and the triangle "
            "footwork works at half the scale. Training runs the same "
            "ladder as the weapons: solo shadowboxing the translated "
            "angles, partner hubud with punches instead of thrusts, "
            "sombrada with empty hands, and finally controlled sparring."
        ),
        "how_it_works": (
            "Panantukan works because the nervous system does not care "
            "what is in the hand - it cares about lines and timing. The "
            "translation drill makes this explicit: the student throws "
            "angle 1 with the stick, drops the stick, and throws the same "
            "angle as an overhand punch, feeling the identical hip "
            "rotation and step. The twelve angles become twelve "
            "empty-hand strikes, and the blocks become parries, covers, "
            "and destructions - striking the incoming limb instead of "
            "just deflecting it. The hubud pattern translates whole: the "
            "feeder throws a slow jab-cross, the defender parries, ties, "
            "unties, and counters with the elbow or the slap. Limb "
            "destruction is the signature tactic: when the opponent jabs, "
            "the defender's forearm or elbow meets the incoming arm with "
            "a short, hard strike - the gunting principle - damaging the "
            "weapon instead of blocking it. Sparring is introduced with "
            "the same control ladder as stick sparring: technique-only "
            "rounds, then light contact with gear, always with the "
            "translation mindset - every combination must trace back to "
            "an angle."
        ),
        "key_points": [
            "Panantukan translates the twelve angles into fists, elbows, knees, and head: the lines are identical, only the tool changes.",
            "Weapon-first payoff: thousands of stick repetitions pre-install the timing the empty hand needs.",
            "Limb destruction targets the attacking arm itself: damage the weapon instead of just blocking it.",
            "The hubud and sombrada patterns translate whole: feed punches instead of thrusts and the drills still work.",
            "Every combination must trace back to an angle: the translation stays honest.",
        ],
        "requirements": [
            "Clean twelve angles with the stick; the translation needs something to translate.",
            "Boxing gloves or bag gloves for partner work; hand wraps for bag rounds.",
            "A heavy bag for the translated strikes at full power.",
            "A partner for hubud-with-punches and empty-hand sombrada.",
            "Mouthguard and headgear before any contact sparring.",
        ],
        "standards": [STD_WEAPON_FIRST, STD_SAFETY],
        "citations": [CIT_INOSANTO, CIT_WILEY00, CIT_SULITE],
    },
    {
        "key": "gunting",
        "name": "Gunting: The Scissor Trap",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "sig_lens": ("Through the Signature lens, gunting is the covenant "
                     "of the scissors: two limbs closing on one, and the "
                     "opponent's strength becomes the blade that cuts the "
                     "opponent. The Signature practitioner scissors the "
                     "attacking arm until the enemy learns what every "
                     "Fighter of the art learns - the weapon you reach with "
                     "is the weapon you risk."),
        "description": (
            "Gunting means scissors, and the scissor trap is the technique "
            "of wedging the opponent's attacking limb between two of the "
            "defender's limbs and clamping down. The classic gunting "
            "meets the opponent's punch with the defender's forearm "
            "rising inside it while the other hand presses down on top of "
            "it - the arm caught like paper in scissors - often with a "
            "short destructive strike to the biceps or the elbow joint at "
            "the moment of the trap. It is the empty-hand expression of "
            "defanging the snake: instead of blocking the punch, the "
            "defender attacks the punching arm. The wedge multiplies "
            "force: a shallow scissor angle turns moderate arm strength "
            "into serious clamping pressure on the trapped limb, and the "
            "destruction strike lands on nerves and tendons that do not "
            "toughen with training. Gunting flows from hubud: the tie "
            "becomes the scissor, the untie becomes the destruction and "
            "the counter. With the stick, the same geometry appears as "
            "the stick-and-forearm trap; with the blade, the scissor "
            "guides the edge. It is drilled slowly and with great control, "
            "because the technique targets joints."
        ),
        "how_it_works": (
            "The gunting works as a wedge and a lever. As the punch "
            "arrives, the defender's lead forearm rises at a shallow angle "
            "across the punching arm's path - not meeting it head-on but "
            "sliding along it - while the rear hand comes down on top of "
            "the arm near the elbow. The two limbs form a V, and as the V "
            "closes, the mechanical advantage multiplies the clamping "
            "force: a twenty-degree wedge gives roughly five-to-one "
            "leverage, so the trapped arm is immobilized far beyond what "
            "the defender's raw strength could do. In that pinned instant "
            "the defender's forearm bone or elbow drives a short strike "
            "into the biceps, the inner elbow, or the wrist - the "
            "destruction - and then the trap opens into the counter. The "
            "drill progression is strict: first the wedge shape against a "
            "static extended arm, then the wedge against slow feeds, then "
            "the wedge with the destruction touch, then hubud flow with "
            "gunting inserted on signal. Joint safety is absolute: the "
            "clamp is practiced as pressure, never as a jerk, and the "
            "destruction is always a touch in drilling."
        ),
        "key_points": [
            "The gunting wedges the attacking arm between two of the defender's limbs like paper in scissors.",
            "The wedge multiplies force: a shallow scissor angle gives roughly five-to-one clamping leverage.",
            "It is defanging with the hands: attack the punching arm instead of merely blocking it.",
            "The destruction strike lands on the biceps, inner elbow, or wrist at the moment of the trap.",
            "Drill it as pressure, never as a jerk: the technique targets joints and demands absolute control.",
        ],
        "requirements": [
            "Clean hubud-lubud; the gunting grows out of the tie.",
            "A cooperative partner; the wedge is learned on a static arm first.",
            "Empty hands; the geometry is pure body mechanics.",
            "Joint-safety briefing before the first session: pressure, never jerks.",
            "Patience: the wedge angle is felt, not forced, and takes weeks to find.",
        ],
        "standards": [STD_SAFETY, STD_WEAPON_FIRST],
        "citations": [CIT_INOSANTO, CIT_WILEY00],
    },
    {
        "key": "daga_i",
        "name": "Knife Work I: Daga Grips and Angles",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "sig_lens": ("Through the Signature lens, the daga is the covenant "
                     "made sharp: the same twelve angles, now with "
                     "consequences that cannot be taped over. The Signature "
                     "practitioner takes up the trainer blade with clean "
                     "hands and a quiet mind - because the knife teaches "
                     "respect faster than any teacher, and respect is the "
                     "first technique."),
        "description": (
            "Daga is the knife, and the first knife record covers grips, "
            "angles, and edge awareness with training blades. Three grips "
            "rule the art: the hammer grip, blade extending from the "
            "thumb side like a hammer, the all-purpose grip for slashing "
            "and thrusting; the pakal or icepick grip, blade extending "
            "from the pinky side, point down, for close hooking and "
            "raking; and the fencer's grip, thumb along the spine for "
            "precise thrusting. The twelve angles transfer directly: "
            "angle 1 with a knife is a diagonal slash, angle 5 is the "
            "thrust, the low angles are leg cuts. But the blade changes "
            "the geometry: the edge has an orientation, and a slash thrown "
            "with the flat does nothing, so every angle is drilled with "
            "edge alignment checked. Range collapses to arm's length, "
            "which makes the triangle footwork even more critical - the "
            "knife fighter lives or dies by the step. All early work uses "
            "trainers: wood, aluminum, or rubber. The safety covenant is "
            "absolute: trainers are inspected before every session, live "
            "blades never enter partner drills, and the techniques are "
            "taught as civilian self-defense knowledge with the gravity "
            "the tool deserves."
        ),
        "how_it_works": (
            "Knife work functions as angle work with edge discipline. The "
            "student first learns the grips statically: shifting between "
            "hammer, pakal, and fencer without looking, because grip "
            "changes happen by feel in the dark of a real exchange. Then "
            "the twelve angles are shadowed with the trainer, checking "
            "after each cut that the edge - marked with tape on the "
            "trainer - faced the target through the whole arc. The "
            "transfer drill pairs stick and knife: throw angle 3 with the "
            "stick, then immediately with the trainer, feeling how the "
            "shorter weapon demands a deeper step. Partner work begins "
            "with the feeder offering slow angle-5 thrusts while the "
            "student practices the four defenses adapted to the blade - "
            "deflecting the weapon arm, never catching the edge. The "
            "tapi-tapi tap becomes essential: tapping the knife hand "
            "offline is far safer than blocking the blade. Every session "
            "ends with the respect drill: slow, deliberate angle work "
            "with full attention on edge alignment, because casual hands "
            "and sharp tools are a bad pairing."
        ),
        "key_points": [
            "Three grips: hammer for slashing and thrusting, pakal (icepick) for close hooking, fencer's grip for precise thrusts.",
            "The twelve angles transfer directly, but the edge must face the target through the whole arc.",
            "Train with wood, aluminum, or rubber trainers; live blades never enter partner drills.",
            "Deflect the weapon arm, never catch the edge: tapi-tapi tapping is the core knife defense.",
            "Shift grips without looking: grip changes happen by feel, and the feel is drilled.",
        ],
        "requirements": [
            "Clean twelve angles with the stick; the knife is a translation, not a new alphabet.",
            "One training dagger (wood, aluminum, or rubber) with the edge marked in tape.",
            "A partner and protective gear including eye protection before any partner blade work.",
            "Blade-safety briefing and trainer inspection before every session.",
            "A sober training covenant: no horseplay, no live steel, full attention always.",
        ],
        "standards": [STD_SAFETY, STD_WEAPON_FIRST, STD_ANGLES],
        "citations": [CIT_INOSANTO, CIT_WILEY00, CIT_SULITE],
    },
    {
        "key": "agaw_i",
        "name": "Disarming I: Snaking the Stick Away (Agaw Sandata)",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "sig_lens": ("Through the Signature lens, the snaking disarm is "
                     "the covenant of the serpent: wrap, squeeze, and take "
                     "- never wrestling strength against strength. The "
                     "Signature practitioner snakes the weapon away the "
                     "way water takes a stone from a child's hand: "
                     "patiently, inevitably, and without a contest."),
        "description": (
            "Agaw sandata means seizing the weapon, and the snaking disarm "
            "is the first and most characteristic Filipino disarm. The "
            "defender meets the opponent's strike with a block, then wraps "
            "the defending stick around the opponent's wrist and weapon - "
            "snaking over and under - and levers the stick out of the "
            "grip with a short twist. The technique exploits leverage, "
            "not strength: the defender's whole stick becomes a lever "
            "against the opponent's fingers, and the mechanical advantage "
            "runs roughly twelve to one, so a modest pull defeats even a "
            "strong grip. The classic entry is against angle 1: block with "
            "the outside defense, snake the stick over the attacker's "
            "wrist, trap it against the defender's own forearm, and twist "
            "down and out. Timing is everything: the snake must begin in "
            "the instant the strike is blocked, while the attacker's arm "
            "is extended and committed. It is drilled in stages - the wrap "
            "shape on a static held stick, then against slow feeds, then "
            "in sombrada flow on signal - and always with the counter in "
            "mind: the disarm ends with the defender holding both weapons "
            "and the attacker disarmed and covered."
        ),
        "how_it_works": (
            "The snaking disarm works as a lever against the fingers. The "
            "opponent's grip is strong along the stick's axis but weak "
            "against rotation: fingers wrap the stick, and a twisting "
            "force pries them open. The defender's stick, wrapped around "
            "the opponent's wrist, applies that twist with the full "
            "length of the lever - the contact point near the defender's "
            "hand versus the opponent's grip near the defender's stick "
            "tip gives the twelve-to-one advantage. The body adds the "
            "force: the defender steps on the triangle and drops the "
            "weight as the twist fires, so body mass, not arm strength, "
            "drives the lever. The trap matters as much as the twist: "
            "snaking the stick against the defender's own forearm pins "
            "the opponent's wrist so it cannot follow the twist and "
            "re-grip. The drill teaches the feel of the committed arm - "
            "the snake only works on an extended, committed strike, which "
            "is why it is practiced inside sombrada flow, where the "
            "feeds are honest. Against a retracted or uncommitted arm, "
            "the defender does not force it: the disarm is an "
            "opportunity, never a wrestling match."
        ),
        "key_points": [
            "Agaw sandata means seizing the weapon; the snake wraps the defender's stick around the attacker's wrist and levers it out.",
            "Leverage beats strength: roughly twelve-to-one mechanical advantage against the gripping fingers.",
            "The snake fires on the committed arm: block the strike, wrap in the same beat, twist with the body drop.",
            "Trap the wrist against your own forearm so it cannot follow the twist and re-grip.",
            "A disarm is an opportunity, never a wrestling match: if the arm is not committed, do not force it.",
        ],
        "requirements": [
            "Clean blocks and sombrada flow; the disarm lives inside honest feeds.",
            "A cooperative partner starting with a static held stick, progressing to slow feeds.",
            "One rattan stick each; the defender needs a stick to snake with.",
            "Wrist and finger safety: the twist is applied smoothly, never jerked.",
            "Protective gear before the flow-insertion stage.",
        ],
        "standards": [STD_SAFETY, STD_ANGLES],
        "citations": [CIT_INOSANTO, CIT_SULITE, CIT_WILEY00],
    },
    {
        "key": "agaw_ii",
        "name": "Disarming II: Strips and Punyo Work",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "sig_lens": ("Through the Signature lens, the strip is the covenant "
                     "completed: first loosen with the punyo, then take "
                     "with the hands. The Signature practitioner strikes "
                     "the gripping hand to remind it of its mortality, then "
                     "accepts the surrendered weapon - because the hand "
                     "that has been hit cannot hold, and the fighter who "
                     "knows this never has to wrestle."),
        "description": (
            "The second disarming record covers strips - taking the weapon "
            "with the hands and body - and punyo work, the butt-end "
            "strikes that loosen the grip first. The punyo is the "
            "setup: a short hammering strike with the butt of the stick "
            "to the opponent's weapon hand, wrist, or forearm. Even a "
            "light punyo strike stings the gripping hand badly, and a "
            "stung hand cannot hold - the strip that follows meets little "
            "resistance. The basic two-count is punyo to the hand, then "
            "the live hand strips the weapon: grabbing the opponent's "
            "stick near its tip while the defender's stick controls the "
            "wrist, then levering it out with a body turn. Variations "
            "include the two-on-one strip, both hands on the opponent's "
            "weapon while the defender's stick pins the arm, and the "
            "strike-strip, where a defanging strike to the hand flows "
            "directly into the take. The safety rule is strict: punyo "
            "strikes in drilling are touches to padded hands, and the "
            "strip is applied with smooth leverage, never a wrenching "
            "jerk that could injure the wrist."
        ),
        "how_it_works": (
            "Strips work by combining pain compliance with leverage. The "
            "punyo strike to the back of the gripping hand triggers an "
            "involuntary loosening - the hand's grip reflex breaks for a "
            "fraction of a second under sharp impact - and the strip "
            "exploits exactly that window. The live hand grabs the "
            "opponent's stick near the tip, the far end of the lever, "
            "while the defender's own stick or forearm pins the "
            "opponent's wrist; a short rotation of the defender's body "
            "then pries the weapon out along the line the fingers open "
            "most easily, which is a twist toward the thumb side. The "
            "two-on-one variation doubles the control: both of the "
            "defender's hands on the weapon, the defender's stick "
            "trapping the arm, the body drop supplying the force. Drilling "
            "runs in three stages: punyo touch-and-strip on a static "
            "held stick, the same against slow feeds, and insertion into "
            "sombrada flow where the feeder's committed strike invites "
            "the punyo. The counter-threat is always honored: the strip "
            "ends with the defender covered and the taken weapon "
            "controlled, because a half-completed disarm leaves the "
            "defender holding the dangerous end."
        ),
        "key_points": [
            "Punyo first, strip second: the butt-end strike to the gripping hand breaks the grip reflex for the window the strip needs.",
            "Grab near the tip: the far end of the lever gives maximum prying advantage.",
            "Twist toward the thumb side: fingers open most easily along that line.",
            "The two-on-one strip doubles control: both hands on the weapon, the stick pinning the arm, the body drop supplying force.",
            "Drill with touches and smooth leverage: punyo strikes are touches in practice, strips are never jerked.",
        ],
        "requirements": [
            "Clean snaking disarm; the strip is its close-range sibling.",
            "Padded hand protection for the partner receiving punyo touches.",
            "One rattan stick each; the defender's stick does the pinning.",
            "A cooperative partner progressing from static holds to slow feeds.",
            "Wrist-safety briefing: smooth leverage only, zero jerking.",
        ],
        "standards": [STD_SAFETY, STD_ANGLES],
        "citations": [CIT_INOSANTO, CIT_SULITE],
    },
])

ENTRIES.extend([
    {
        "key": "daga_ii",
        "name": "Knife Work II: Live-Blade Awareness and Tapping",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "sig_lens": ("Through the Signature lens, the live blade is the "
                     "covenant's final examiner: it does not forgive, so "
                     "the practitioner learns to never need forgiveness. "
                     "The Signature practitioner taps the blade aside with "
                     "the calm of long practice - because panic is the "
                     "only cut that cannot be trained away."),
        "description": (
            "The second knife record builds live-blade awareness: the "
            "understanding that a blade punishes every error the stick "
            "forgives. The core defensive skill is tapping with control - "
            "using the stick or the checking hand to tap the knife hand "
            "offline, never the blade itself - combined with the triangle "
            "footwork that keeps the body off the cutting lines. Blade "
            "sparring with trainers introduces the psychological shift: "
            "even a wooden knife changes how partners move, and the "
            "student learns to manage the adrenaline that makes beginners "
            "freeze or flail. The largo mano blade game - long-range knife "
            "fencing with slashes at the extended arm - teaches the "
            "defanging principle at its most serious: the knife hand is "
            "the target, because reaching the body means walking into the "
            "edge. Targeting discipline is drilled relentlessly: the "
            "trainer work maps the body's vital lines - neck, inner arm, "
            "torso, inner leg - so the practitioner understands what is "
            "at stake and why avoidance and control outrank engagement. "
            "The record closes with the standing rule of the art: the "
            "knife is a tool of last resort, trained for understanding "
            "and defense, and the skilled practitioner de-escalates and "
            "leaves whenever leaving is possible."
        ),
        "how_it_works": (
            "Live-blade awareness works by replacing the stick-trained "
            "instinct to block with the blade-trained instinct to evade "
            "and control. The numbers are sobering: a committed knife "
            "thrust crosses arm's length in about two-tenths of a second, "
            "faster than conscious reaction, so the defense must be "
            "pre-positioned - the checking hand already up, the body "
            "already angled - not launched on sight. The tapping defense "
            "exploits the knife hand as the nearest target: a short tap "
            "to the wrist or forearm with the stick redirects the whole "
            "weapon, because the hand steers the blade. Footwork does the "
            "heavy lifting: the sidestep triangle moves the body off the "
            "thrust line while the tap clears the hand, a two-part "
            "defense that drilling fuses into one beat. Trainer sparring "
            "runs in short rounds with full protective gear including eye "
            "protection, and every exchange is reviewed: where was the "
            "checking hand, did the feet move first, was the tap on the "
            "hand or dangerously near the blade. The psychological "
            "training is explicit - breathing drills between rounds, "
            "verbal de-escalation practice - because the blade demands a "
            "calm mind more than fast hands."
        ),
        "key_points": [
            "A committed thrust crosses arm's length in about 0.2 seconds: the defense must be pre-positioned, not launched on sight.",
            "Tap the knife hand, never the blade: the hand steers the edge, and the hand is the nearest target.",
            "Footwork does the heavy lifting: sidestep off the thrust line while the tap clears the hand, fused into one beat.",
            "Trainer sparring builds the psychological shift: manage the adrenaline that makes beginners freeze or flail.",
            "The standing rule: de-escalate and leave whenever leaving is possible; the blade is a last resort.",
        ],
        "requirements": [
            "Clean knife grips, angles, and edge alignment from Knife Work I.",
            "Training daggers only; the live-blade in the title means awareness, not live steel in drills.",
            "Full protective gear including eye protection for any trainer sparring.",
            "A calm, experienced partner; blade psychology work needs trust.",
            "Breathing and de-escalation practice alongside the physical drills.",
        ],
        "standards": [STD_SAFETY, STD_WEAPON_FIRST, STD_FOOTWORK],
        "citations": [CIT_INOSANTO, CIT_WILEY00, CIT_SULITE],
    },
    {
        "key": "cadena",
        "name": "Cadena de Mano: The Chain of Hands",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "sig_lens": ("Through the Signature lens, cadena de mano is the "
                     "covenant unbroken: hand follows hand follows hand, "
                     "and the chain has no first link and no last. The "
                     "Signature practitioner chains at close range until "
                     "the opponent feels not strikes but weather - "
                     "continuous, inescapable, and already past."),
        "description": (
            "Cadena de mano means chain of the hand, and it is the "
            "close-range empty-hand system of chained strikes, traps, and "
            "limb destructions. Where panantukan boxes at arm's length, "
            "cadena works chest-to-chest: the practitioner's hands flow "
            "from strike to trap to destruction to strike without "
            "chambering, each motion feeding the next. The core vocabulary "
            "is small - the slap, the backfist, the elbow, the gunting "
            "wedge, the hubud tie - but the chaining is endless: five "
            "core moves chain into sixty ordered three-move sequences, "
            "and the practitioner learns to improvise within that space. "
            "Sensitivity is everything at this range: the hands read the "
            "opponent's arms through constant light contact, feeling the "
            "chamber before the strike launches. Cadena is traditionally "
            "taught after the weapon work because every chain traces back "
            "to a stick angle - the elbow is angle 1 shortened, the "
            "backfist is angle 4 without the stick. Training is "
            "partner-heavy: the chain cannot be learned on a bag, because "
            "the bag does not push back, trap, or change the rhythm. "
            "Control is the price of admission: at this range a lost "
            "temper lands an elbow, so cadena is taught to calm students "
            "first."
        ),
        "how_it_works": (
            "Cadena works by eliminating the gaps between techniques. A "
            "normal combination has seams - strike, recover, strike - "
            "and the seams are where counters live; cadena removes them "
            "by making every motion end in the chamber of the next. The "
            "elbow strike finishes with the hand already positioned for "
            "the backfist; the backfist's return becomes the gunting "
            "wedge against the opponent's answering arm; the wedge opens "
            "into the slap. The hands maintain constant reference contact "
            "with the opponent's arms - the checking touch from hubud, "
            "now permanent - so the chain reacts to pressure changes "
            "instead of visual cues, which is faster at this range. The "
            "drill ladder is fixed: first the five core moves solo, then "
            "two-move chains with a partner feeding slow punches, then "
            "three-move chains, then the flow drill where the partner "
            "feeds random close attacks and the student must chain three "
            "unbroken moves before resetting. The graduation test is the "
            "continuous minute: sixty seconds of unbroken chaining against "
            "a resisting partner, with control held throughout - no "
            "chambering, no backing up, no lost temper."
        ),
        "key_points": [
            "Cadena chains strike to trap to destruction to strike with no seams: every motion ends in the next motion's chamber.",
            "Five core moves - slap, backfist, elbow, gunting wedge, hubud tie - chain into sixty ordered three-move sequences.",
            "Constant reference contact: the hands read pressure changes faster than the eyes read motion.",
            "Every chain traces back to a stick angle: the elbow is angle 1 shortened, the backfist is angle 4 unarmed.",
            "Control is the price of admission: at chest-to-chest range a lost temper lands an elbow.",
        ],
        "requirements": [
            "Clean panantukan, hubud, and gunting; cadena chains them all.",
            "A trusted partner; the chain cannot be learned on a bag.",
            "Empty hands and a calm floor; protective headgear for the flow stages.",
            "Demonstrated emotional control: the teacher gates this record on temperament.",
            "Short daily sessions; sensitivity fatigues faster than muscle.",
        ],
        "standards": [STD_SAFETY, STD_WEAPON_FIRST],
        "citations": [CIT_INOSANTO, CIT_WILEY00],
    },
    {
        "key": "dumog",
        "name": "Dumog: Filipino Grappling and Wrestling",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "sig_lens": ("Through the Signature lens, dumog is the covenant "
                     "of the ground: when the weapons are gone and the "
                     "hands are tied, the body still knows the way down. "
                     "The Signature practitioner wrestles the way the art "
                     "strikes - with angles, leverage, and the triangle "
                     "under the feet - because the fall is only another "
                     "angle, written vertically."),
        "description": (
            "Dumog is the Filipino wrestling art: clinch fighting, throws, "
            "takedowns, and ground control, practiced as the grappling "
            "half of the complete fighter. The standing game centers on "
            "the clinch - head control, the neck tie, the over-under - "
            "where the practitioner fights for the inside position that "
            "the weapon arts call the close range. Signature techniques "
            "include the head-and-arm throws, hip tosses driven by the "
            "same hip rotation as the stick strikes, leg reaps that sweep "
            "the supporting leg, and the standing joint locks that flow "
            "from the disarming work. On the ground dumog emphasizes "
            "position and the quick finish: control the head, control the "
            "hips, apply the lock or the pin, and disengage - the art "
            "assumes the street has friends and hard floors, so prolonged "
            "ground wrestling is discouraged. The connection to the "
            "weapon art runs deep: the triangle footwork becomes the "
            "throwing footwork, the hubud sensitivity becomes clinch "
            "sensitivity, and the disarm entries become standing locks. "
            "Training is done on mats with a partner, always with "
            "tapping honored instantly."
        ),
        "how_it_works": (
            "Dumog works on leverage and positional hierarchy. The clinch "
            "is a battle for head position: whoever controls the head "
            "controls the spine, and whoever controls the spine decides "
            "where the bodies go. The hip throw demonstrates the "
            "physics: the practitioner steps the triangle to get the hips "
            "under the opponent's center, loads by bending the knees, and "
            "rotates - the opponent's seventy-five kilograms lifted a "
            "foot off the ground costs the thrower a fraction of that in "
            "effort because the hips, not the arms, do the lifting. The "
            "leg reap attacks the base instead of the body: sweeping the "
            "supporting leg while pushing the upper body the other way, "
            "the classic two-direction takedown. Ground control follows "
            "the positional ladder - side control over guard, mount over "
            "side control - with the locks applied from dominant "
            "positions only. Training runs technique lines: partners "
            "drill one throw for ten minutes, alternating roles, then "
            "flow between three throws, then add the standing locks from "
            "the disarm entries. Randori - free grappling - starts with "
            "position-only rounds and graduates to full rounds with "
            "instant tap honor."
        ),
        "key_points": [
            "The clinch is a battle for head position: control the head, control the spine, decide where the bodies go.",
            "Throws use the hips, not the arms: triangle footwork gets the hips under the opponent's center.",
            "The leg reap attacks the base: sweep the supporting leg while pushing the upper body the other way.",
            "Ground rule: position first, finish quick, disengage - the street has friends and hard floors.",
            "Tap is sacred: honor it instantly, every time, no exceptions, no ego.",
        ],
        "requirements": [
            "Mats: dumog is not learned on hard floors.",
            "A trained partner; throws require a partner who knows how to fall.",
            "Breakfall training first: the ability to be thrown safely precedes throwing.",
            "Clean triangle footwork and hubud sensitivity; both transfer directly.",
            "A mouthguard and the tap covenant agreed before the first round.",
        ],
        "standards": [STD_SAFETY, STD_FOOTWORK],
        "citations": [CIT_WILEY97, CIT_WILEY00, CIT_SULITE],
    },
    {
        "key": "live_hand",
        "name": "The Live Hand: Kamot as Second Weapon",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "sig_lens": ("Through the Signature lens, the live hand is the "
                     "covenant's silent partner: the hand that never held "
                     "the weapon but always decided the fight. The "
                     "Signature practitioner wakes the live hand until it "
                     "checks, traps, and disarms on its own - because the "
                     "weapon is only half the fighter, and the empty hand "
                     "is the half that thinks."),
        "description": (
            "The live hand - kamot, the empty hand - is the advanced "
            "study of everything the non-weapon hand does: checking, "
            "parrying, trapping, grabbing, disarming, and striking. "
            "Beginners park the live hand near the chin and forget it; "
            "advanced practitioners make it the busiest hand in the "
            "fight. The checking family: the hand presses or slaps the "
            "opponent's weapon arm offline, buying the beat the stick "
            "needs. The parrying family: open-hand deflections that work "
            "the same angles as the stick blocks. The trapping family: "
            "from hubud, the live hand pins the opponent's limb while the "
            "weapon strikes. The grabbing family: seizing the opponent's "
            "wrist, elbow, or weapon to feed the disarms. And the "
            "striking family: the live hand punches, slaps, and elbows "
            "at close range where the stick cannot chamber. The advanced "
            "principle is independence: the live hand acts on its own "
            "read of the fight, not as the stick's assistant. Drills "
            "isolate it - live-hand-only sparring rounds, checking-only "
            "exchanges - until it stops waiting for permission. The "
            "master's tell is the live hand's position: always between "
            "the fighter and the threat, always moving, never dropped."
        ),
        "how_it_works": (
            "The live hand works by multiplying the fighter's defensive "
            "and offensive bandwidth. A single stick can only be in one "
            "place; the live hand covers the second line, which is why "
            "espada y daga simply weaponizes what the live hand was "
            "already doing. The check is the foundation: as the "
            "opponent's strike launches, the live hand meets the weapon "
            "arm - not the weapon - with a short pressing parry, "
            "deflecting the whole attack by its steering. The trap "
            "builds on the check: the pressing hand stays on the arm, "
            "pinning it for the beat the stick's counter needs. The grab "
            "is the trap extended: the hand closes on the wrist and "
            "pulls it into the disarm entries. Training isolates each "
            "family: checking drills against slow feeds with the stick "
            "hand chambered, trapping flow from hubud with the stick "
            "removed, and finally the integration rounds where both hands "
            "are live and the teacher scores live-hand actions. The "
            "independence test is the blind round: the student spars "
            "light with the stick hand restricted to blocking, forcing "
            "the live hand to create every opening."
        ),
        "key_points": [
            "The live hand is the second weapon: checking, parrying, trapping, grabbing, disarming, striking.",
            "Check the weapon arm, not the weapon: deflect the steering and the whole attack follows.",
            "The advanced principle is independence: the live hand acts on its own read, not as the stick's assistant.",
            "Isolate it in training: live-hand-only rounds and checking-only exchanges wake it up.",
            "The master's tell: the live hand is always between the fighter and the threat, always moving, never dropped.",
        ],
        "requirements": [
            "Clean hubud, tapi-tapi, and disarm entries; the live hand's jobs come from them.",
            "A partner for the checking and trapping isolation drills.",
            "Empty live hand and one stick; the drill restricts the stick hand by design.",
            "Protective gear for the integration rounds.",
            "Video review: the live hand's laziness is invisible to its owner.",
        ],
        "standards": [STD_SAFETY, STD_WEAPON_FIRST],
        "citations": [CIT_INOSANTO, CIT_WILEY00],
    },
    {
        "key": "espada_y_daga_ii",
        "name": "Espada y Daga II: Advanced Live-Hand Control",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "sig_lens": ("Through the Signature lens, the advanced pair is "
                     "the covenant in full voice: long and short speaking "
                     "together, the dagger writing between the stick's "
                     "lines. The Signature practitioner passes, checks, "
                     "and clears with the short weapon until the pair "
                     "moves like one mind in two hands - because the "
                     "master of two weapons is the master of no weak "
                     "range."),
        "description": (
            "The advanced espada y daga record covers the close-range "
            "integration: passing, checking, and clearing with the short "
            "weapon while the long weapon commands. Passing is the core "
            "skill: as the opponent's weapon comes in, the dagger hand "
            "meets it and passes it across the body to the stick side, "
            "where the stick traps or punishes - the two weapons handing "
            "the threat back and forth like a ball. Checking becomes "
            "continuous: the dagger never leaves contact with the "
            "opponent's weapon arm, riding it through the exchange and "
            "killing every chamber before it launches. Clearing is the "
            "entry system: the dagger clears the opponent's guard high "
            "while the stick strikes low, or hooks the weapon down while "
            "the stick takes the head - the classic high-low that the "
            "single stick cannot produce alone. The corto game - close "
            "range - is where the pair shines: the stick shortens to "
            "punyo work and the dagger does the cutting and trapping, "
            "the fighter chest-to-chest and fully armed. Free-flow "
            "paired sparring with trainers is the graduation, run in "
            "short controlled rounds with full gear."
        ),
        "how_it_works": (
            "Advanced espada y daga works on the passing triangle: dagger "
            "receives, stick traps, dagger finishes - or any rotation of "
            "that circuit. The mechanics of the pass: the dagger hand "
            "contacts the incoming weapon arm on its outside, guides it "
            "across the defender's centerline with a short pull, and the "
            "stick is already waiting on the far side to pin it; the "
            "opponent's weapon ends up controlled by both of the "
            "defender's weapons at once. The continuous check is a "
            "sensitivity skill from hubud, scaled up: the dagger hand "
            "rests lightly on the opponent's forearm and reads the "
            "chamber through the skin, pressing in the instant before "
            "launch. The high-low clearing exploits divided attention: "
            "the human guard can only strongly cover one line, so the "
            "dagger threatens high - drawing the guard up - while the "
            "stick takes the exposed low line, or the reverse. Training "
            "runs the passing circuit as a drill: feeder throws slow "
            "angles, student passes every one to the stick side, then the "
            "feeder varies the angles, then the speed rises, then the "
            "free-flow rounds begin. The dagger hand must stay relaxed: "
            "a tense checking hand is slow, and slow checks get hit."
        ),
        "key_points": [
            "Passing is the core: the dagger receives the incoming weapon and hands it across to the waiting stick.",
            "The continuous check rides the opponent's weapon arm, killing every chamber before it launches.",
            "Clearing runs the high-low: the dagger threatens one line and draws the guard while the stick takes the other.",
            "The corto game shines chest-to-chest: stick shortens to punyo work while the dagger traps and finishes.",
            "Keep the dagger hand relaxed: a tense checking hand is slow, and slow checks get hit.",
        ],
        "requirements": [
            "Clean basic espada y daga; the advanced record is its close-range integration.",
            "One rattan stick and one training dagger; matched and inspected.",
            "A skilled partner; passing drills need honest, controlled feeds.",
            "Full protective gear including eye protection for the free-flow rounds.",
            "Hubud sensitivity; the continuous check is hubud with a dagger in hand.",
        ],
        "standards": [STD_SAFETY, STD_WEAPON_FIRST],
        "citations": [CIT_INOSANTO, CIT_SULITE, CIT_WILEY00],
    },
    {
        "key": "laban_laro",
        "name": "Sparring I: Protected Contact (Laban Laro)",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "sig_lens": ("Through the Signature lens, laban laro is the "
                     "covenant tested kindly: play the fight so the fight "
                     "does not have to be real. The Signature practitioner "
                     "spars the way a musician rehearses - with protection, "
                     "with partners, with joy - because the play that is "
                     "honest teaches what the drill cannot."),
        "description": (
            "Laban laro means play fight, and protected-contact sparring "
            "is where the drills meet a resisting opponent for the first "
            "time. The gear is the covenant: headgear with face "
            "protection, padded gloves or stick mitts, body armor, groin "
            "protection, and for blade-trainer rounds, eye protection. The "
            "rules of engagement are agreed before the first round: "
            "which targets are legal, what contact level is allowed, how "
            "a round is stopped, and the absolute authority of the stop "
            "call. Rounds run short - two minutes with a minute's rest is "
            "the classic - because fatigue destroys technique and the "
            "goal is learning, not surviving. The beginner's sparring "
            "curriculum is staged: first technique-only rounds where only "
            "agreed angles are thrown, then limited-target rounds, then "
            "open rounds at controlled contact. The teacher watches for "
            "the three beginner failures: the frozen guard that stops "
            "moving, the wild swing that abandons the angles, and the "
            "chasing feet that forget the triangles. Every round ends "
            "with the review: what worked, what broke down, which drill "
            "needs repeating."
        ),
        "how_it_works": (
            "Protected sparring works by adding the one ingredient drills "
            "lack: an opponent who does not cooperate. The first rounds "
            "are deliberately constrained - both partners may only throw "
            "angles 1 and 2 at half speed - so the student experiences "
            "timing pressure without technical chaos. As control is "
            "proven, constraints lift one at a time: more angles, more "
            "speed, footwork freedom, then counters. The protective gear "
            "changes the psychology: beginners swing wildly when they "
            "feel safe, so the teacher enforces the contact ladder "
            "ruthlessly - anyone who cannot control power at half speed "
            "does not advance to full speed. The round structure teaches "
            "energy management: three two-minute rounds with one-minute "
            "rests demand pacing, and the student learns that the "
            "fighter who breathes wins the third round. Between rounds "
            "the teacher gives exactly one correction - the single "
            "biggest leak - because five corrections between rounds "
            "produce zero improvements in the next one. The graduation "
            "metric is composure: the student who keeps the guard, the "
            "angles, and the footwork under pressure is ready for "
            "free-flow."
        ),
        "key_points": [
            "Gear is the covenant: headgear, hand protection, body armor, groin protection - agreed before the first round.",
            "Constraints lift one at a time: agreed angles first, then speed, then footwork, then counters.",
            "The contact ladder is enforced: no control at half speed means no full speed, ever.",
            "Three two-minute rounds teach pacing: the fighter who breathes wins the third round.",
            "One correction between rounds: the single biggest leak, because five corrections produce zero improvements.",
        ],
        "requirements": [
            "Complete protective gear, inspected before every session.",
            "Clean angles, blocks, and footwork; sparring tests the foundation, it does not build it.",
            "A supervised environment with an agreed stop call honored instantly.",
            "A partner at matched level and temperament; sparring is a duet, not a grudge.",
            "A teacher or experienced observer for the first twenty rounds minimum.",
        ],
        "standards": [STD_SAFETY],
        "citations": [CIT_PRESAS, CIT_SULITE, CIT_WILEY00],
    },
    {
        "key": "free_flow",
        "name": "Free-Flow Sparring: The Switching Game",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "sig_lens": ("Through the Signature lens, free-flow is the "
                     "covenant unleashed: all ranges, all weapons, no "
                     "script - only the angles, the triangles, and the "
                     "calm. The Signature practitioner flows through largo, "
                     "medio, and corto like water through rapids - never "
                     "fighting the current, always choosing the line - "
                     "because the master does not win exchanges, the "
                     "master dissolves them."),
        "description": (
            "Free-flow sparring is the open game: both partners move "
            "through all three ranges - largo (long), medio (medium), and "
            "corto (close) - switching weapons, angles, and tactics "
            "without a script. The switching game is the heart of it: the "
            "fighter who controls the range controls the fight, so "
            "practitioners drill the transitions deliberately - closing "
            "from largo to corto behind a covering strike, or disengaging "
            "from corto to largo on the retreat triangle when the "
            "close game turns bad. Six transitions connect the three "
            "ranges, and the advanced student owns all six in both "
            "directions. Weapon switching joins the game: dropping from "
            "double stick to single stick plus live hand, or picking up "
            "the disarmed opponent's weapon mid-exchange. The mental game "
            "separates the advanced from the intermediate: fakes that draw "
            "the block and punish the opening, rhythm breaks that disrupt "
            "the opponent's timing, and the patience to wait for the real "
            "opening instead of manufacturing a bad one. Rounds stay "
            "short and the gear stays on; free does not mean reckless. "
            "The teacher's eye is on the transitions: anyone can brawl in "
            "one range, but the fighter moves between them like weather."
        ),
        "how_it_works": (
            "Free-flow works by making range a decision instead of an "
            "accident. The transition matrix is drilled explicitly: largo "
            "to medio (step in behind angle 1), medio to corto (crash "
            "behind the check), corto to medio (push off on the triangle), "
            "and the three reverse moves - six transitions, each with a "
            "covering technique so the move itself is protected. The "
            "switching drill runs as a game: the teacher calls a range "
            "every ten seconds and both fighters must be fighting in it "
            "by the call's end, which builds the transition reflex under "
            "pressure. Weapon switching is layered next: on the teacher's "
            "signal one fighter drops a stick and must immediately "
            "reorganize into single-stick-plus-live-hand, learning that "
            "the system degrades gracefully. The mental layer is coached "
            "through constrained games: fake-only rounds where no strike "
            "may land without a preceding fake, or counter-only rounds "
            "where the first strike is forbidden. Video review is "
            "essential at this stage: fighters cannot feel their own "
            "rhythm breaks and range accidents, but the camera shows "
            "them plainly."
        ),
        "key_points": [
            "Three ranges - largo, medio, corto - connected by six transitions, each with a covering technique.",
            "Range is a decision: drill the transitions until switching ranges is as natural as switching angles.",
            "The system degrades gracefully: losing a stick reorganizes into single-stick-plus-live-hand without panic.",
            "Constrained games build the mental layer: fake-only rounds, counter-only rounds, called-range rounds.",
            "Video review is essential: the camera shows the rhythm breaks and range accidents the fighter cannot feel.",
        ],
        "requirements": [
            "Composure in protected sparring; free-flow demands the calm laban laro built.",
            "Full protective gear; the ranges and weapons multiply the contact points.",
            "One or two rattan sticks; trainers for any blade-switching games.",
            "A teacher to run the constrained games and review the video.",
            "An agreed intensity ladder; free-flow at full power is reserved for the proven.",
        ],
        "standards": [STD_SAFETY, STD_FOOTWORK],
        "citations": [CIT_INOSANTO, CIT_SULITE, CIT_WILEY00],
    },
    {
        "key": "multiple",
        "name": "Multiple Opponents: Moving the Line",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "sig_lens": ("Through the Signature lens, the multiple-opponent "
                     "game is the covenant's hardest truth: you cannot "
                     "fight two people, so you must arrange to fight one "
                     "person twice. The Signature practitioner moves the "
                     "line until the many become a queue - because geometry "
                     "is the only ally that never tires."),
        "description": (
            "The multiple-opponent record teaches the geometry of "
            "surviving more than one attacker: the core insight is that "
            "two attackers can only hurt the defender if they can both "
            "reach at once, so the defender's whole job is to keep them "
            "stacked - one behind the other - and never stand between "
            "them. The footwork is constant: the fighter circles on the "
            "triangles, always moving to put the nearer attacker between "
            "the defender and the farther one, turning two-on-one into a "
            "series of one-on-one moments. The angles serve double duty: "
            "a strike that defangs the near attacker's hand also threatens "
            "the far attacker, and wide redonda-style arcs keep both at "
            "bay while the feet reposition. Targeting prioritizes mobility "
            "kills: the low angles to knees and ankles slow a chaser, "
            "which matters more than any head strike when the goal is "
            "escape. And escape is the goal: the record's standing rule is "
            "that the win against multiple attackers is the exit, and "
            "every technique here serves breaking contact and leaving. "
            "Training uses two patient feeders and starts at walking "
            "speed - the geometry must be walked before it is run."
        ),
        "how_it_works": (
            "Stacking works on lines of attack. With two attackers three "
            "meters apart, the defender needs roughly eight and a half "
            "meters of distance to narrow the angle between them under "
            "twenty degrees - the point where the far attacker must go "
            "around the near one. Since that distance rarely exists, the "
            "defender manufactures it with movement: circling so the "
            "attackers' lines converge, using the near attacker as a "
            "shield while addressing the far one with long strikes. The "
            "footwork pattern is the continuous triangle walk - never "
            "planting, never backing straight - with the stick kept in "
            "wide, threatening arcs that discourage the rush. The "
            "defanging priority is tactical: a hurt hand drops a weapon, "
            "and an unarmed attacker is a grappler the defender can "
            "shove into the partner. The exit is drilled as the finish of "
            "every sequence: create the stack, strike the near attacker's "
            "mobility, and sprint the opened line - the drill ends with "
            "the defender ten meters away, not with a posed victory. "
            "Two-feeder drills progress from walking-speed geometry to "
            "half-speed pressure, and the teacher stops the drill the "
            "instant the defender plants between the feeders: that "
            "position is the failure the whole record exists to prevent."
        ),
        "key_points": [
            "Never stand between two attackers: keep them stacked, one behind the other, and fight a series of one-on-one moments.",
            "Circle on the triangles: use the near attacker as a shield while the long strikes address the far one.",
            "Prioritize mobility kills: low angles to knees and ankles slow a chaser better than any head strike.",
            "Wide threatening arcs discourage the rush while the feet manufacture the stacking geometry.",
            "The win is the exit: every sequence ends with the defender ten meters away, not a posed victory.",
        ],
        "requirements": [
            "Complete footwork mastery: the stacking game is pure triangles at speed.",
            "Two patient feeder partners; the drill needs two bodies to teach the geometry.",
            "One rattan stick and full protective gear for all three participants.",
            "A large clear space; stacking needs room to circle.",
            "The escape mindset briefed first: this record serves leaving, not winning.",
        ],
        "standards": [STD_SAFETY, STD_FOOTWORK],
        "citations": [CIT_WILEY00, CIT_SULITE],
    },
    {
        "key": "mastery",
        "name": "Mastery: Free-Flow Play",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "sig_lens": ("Through the Signature lens, mastery is the covenant "
                     "kept so long it becomes the keeper: the angles live "
                     "in the hands, the triangles live in the feet, and "
                     "the practitioner finally understands the first "
                     "lesson. The Signature master plays - laban laro to "
                     "the end - because the art was never about the "
                     "fight. It was about the person the practice builds, "
                     "one honest repetition at a time."),
        "description": (
            "Mastery is not a technique but the integration of all "
            "thirty-three records into free-flow play: the practitioner "
            "moves through every range, every weapon, and the empty hand "
            "without choosing, the right answer arriving before the "
            "question is finished. The traditional measure is humble and "
            "numerical: roughly a thousand honest repetitions per "
            "technique - thirty-four thousand strikes, blocks, and steps - "
            "which at two hundred repetitions a day is about six months "
            "of daily practice to lay the foundation, and years to refine "
            "it. The master's game is play: laban laro at full "
            "understanding, where the exchange is joyful, creative, and "
            "completely controlled - the hardest sparring to do well, "
            "because it demands everything with nothing at stake. Teaching "
            "becomes part of the practice: the art is passed on the way "
            "it was received, one student at a time, and the master "
            "learns the angles anew through every beginner's questions. "
            "The record closes the ladder where it began: the weapon as "
            "the teacher, the angle as the lesson, the triangle as the "
            "path. The complete practitioner keeps the covenant of "
            "control - the skills are real, so the responsibility is real - "
            "trains daily, plays often, and never stops being a student."
        ),
        "how_it_works": (
            "Mastery works through integration and teaching. Integration "
            "is trained in the open mat: long free-flow sessions where "
            "the practitioner cycles through single stick, double stick, "
            "espada y daga, blade trainers, and empty hand against "
            "changing partners, with the teacher watching for the seams - "
            "the hesitations where one subsystem hands off to another - "
            "and prescribing the drills that smooth them. The "
            "thirty-four-thousand repetition foundation is tracked simply: "
            "a training log with daily counts per technique family, "
            "reviewed monthly, because what gets counted gets completed. "
            "Teaching accelerates the final stage: explaining the snaking "
            "disarm to a beginner forces the master to articulate the "
            "leverage the hands have known for years, and the "
            "articulation deepens the knowing. The play standard is the "
            "true test: the master spars with beginners safely and "
            "joyfully, giving them the exact resistance that teaches - "
            "never crushing, never patronizing. And the practice never "
            "ends: the daily solo session - angles, triangles, sinawali "
            "shadow - continues for life, because the art is a moving "
            "meditation and the covenant is kept one repetition at a time."
        ),
        "key_points": [
            "Mastery is integration: all ranges, all weapons, and the empty hand flowing without seams or hesitation.",
            "The traditional foundation is about a thousand honest repetitions per technique: count them in a training log.",
            "Teaching deepens the knowing: explaining a technique articulates what the hands have known for years.",
            "The play standard is the true test: spar with beginners safely and joyfully, at exactly the resistance that teaches.",
            "The practice never ends: daily solo work continues for life, one honest repetition at a time.",
        ],
        "requirements": [
            "The full ladder behind: every record practiced, not just read.",
            "A training log with daily counts per technique family, reviewed monthly.",
            "Training partners of all levels, including beginners to teach.",
            "A teacher or peer group for the open-mat integration sessions.",
            "The covenant of control: real skill means real responsibility, kept daily.",
        ],
        "standards": [STD_SAFETY, STD_WEAPON_FIRST, STD_FOOTWORK, STD_ANGLES],
        "citations": [CIT_WILEY97, CIT_WILEY00, CIT_INOSANTO, CIT_PRESAS, CIT_SULITE, CIT_GALANG],
    },
])
