#!/usr/bin/env python3
"""Entries for the Wing Chun Combat databases (combat batch 3, 2026-10-17).

Verified 2026-10-17: RAW SWEEP over the full manifest (2,442 databases)
PLUS every shard index title in jah-databases-data-1 (id/t/g rows):
zero 'combat-wing-chun' slugs/names; zero 'wing chun' title collisions.
The combat-* sibling family (boxing, brazilian-jiu-jitsu, capoeira, judo,
karate, kickboxing, lethwei, muay-thai, savate, taekwondo) covers other
arts - none covers Wing Chun's centerline theory, chi sao, wooden dummy
form, or Cantonese hand-technique system, so BUILD NEW is the verdict
under the paste's rule (name/purpose/record schema/capabilities).

So this build creates two NEW databases, 34 ladder-ordered records each:

  combat-wing-chun              - Wing Chun Combat Database (public-harvest:
                                  real, fact-checked Wing Chun martial-arts
                                  knowledge - centerline theory, stances,
                                  hand techniques, footwork, the three empty-
                                  hand forms, chi sao, the wooden dummy, and
                                  the traditional weapons - every record a
                                  technique with step-by-step body mechanics
                                  for HOW TO DO IT; standard references Chu,
                                  Ritchie and Wu, Complete Wing Chun (Tuttle,
                                  1998); Belonoha, The Wing Chun Compendium
                                  vols 1-2 (Blue Snake Books, 2009, 2013);
                                  Yip Chun, 116 Wing Tsun Dummy Techniques
                                  (1981); Leung Ting, Wing Tsun Kuen (1981);
                                  Yimm Lee, Wing Chun Kung Fu (Ohara, 1972))
  combat-wing-chun-signature    - Wing Chun Combat Signature Database
                                  (his original Signature Combat Method: the
                                  centerline as the Signature line, every
                                  technique a covenant of structure, the
                                  dummy the iron training partner, chi sao
                                  the listening bridge; src signature,
                                  titles suffixed " (Signature Edition)",
                                  never presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBWC- (public) and JAH-CBWCS- (signature), verified free
in the manifest id_prefix values and in every shard index (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_wing_chun.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Civilian traditional-art scope only: forms, drills, conditioning, and
self-defense instruction. Nothing on neutralizing military or
defense-grade systems. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Combat Method: the "
            "centerline is the Signature line every technique is measured "
            "from, each technique a covenant of structure, the wooden dummy "
            "the iron training partner, chi sao the listening bridge, and "
            "forward pressure the oath. Clearly labeled Signature-made, "
            "never presented as authentic public record.")

CIT_COMPLETE = ("Chu R, Ritchie R, Wu Y. Complete Wing Chun: The Definitive "
                "Guide to Wing Chun's History and Traditions. Tuttle "
                "Publishing; 1998.")
CIT_COMPENDIUM = ("Belonoha W. The Wing Chun Compendium, Volumes 1 and 2. "
                  "Blue Snake Books; 2009, 2013.")
CIT_DUMMY116 = ("Yip Chun. 116 Wing Tsun Dummy Techniques. Hong Kong; 1981.")
CIT_WINGTSUN = ("Leung Ting. Wing Tsun Kuen. Hong Kong; 1981.")
CIT_YIMM = ("Yimm Lee J. Wing Chun Kung Fu. Ohara Publications; 1972.")

ENTRIES = [
    {
        "key": "centerline",
        "name": "The Centerline Theory (Jung Sin)",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The centerline (Jung Sin, literally the central thread) is the "
            "single idea the whole art hangs from: an imaginary vertical "
            "plane running from the crown of the head through the nose, "
            "throat, solar plexus, and groin, dividing the body into left "
            "and right halves. Everything vital sits on this line, so Wing "
            "Chun does two things with it: guard your own centerline and "
            "attack the opponent's. The geometry is unforgiving and simple. "
            "If two fighters stand 1.50 meters apart, the straight centerline "
            "attack travels exactly 1.50 meters, while a circular hook around "
            "the outside travels a semicircular arc of about 2.36 meters - "
            "the straight line saves roughly 0.86 meters, about 36 percent "
            "of the distance, and arrives first every time the timing is "
            "equal. That is why Wing Chun punches travel straight down the "
            "middle instead of looping, why the guard sits between the "
            "fighter and the opponent rather than out at the sides, and why "
            "footwork aims to occupy the opponent's centerline while turning "
            "your own away. The theory also defines defense: any attack that "
            "does not threaten your centerline can be ignored, which keeps "
            "the fighter from chasing hands and wasting motion."
        ),
        "how_it_works": (
            "Stand facing a partner at arm's length and have them hold one "
            "fist on the vertical line between your eyes and your belt "
            "buckle - that is your centerline, and their fist is sitting on "
            "it. Now hold your own guard: both hands live on or near that "
            "line, elbows sunk and pointing down the line, so any straight "
            "attack must pass through your hands to reach you. To attack, "
            "extend the vertical punch straight along the line from wherever "
            "your hand already is; do not pull it back, do not swing it "
            "wide. To defend, meet the incoming arm with a hand that stays "
            "on the line and deflects the attack just far enough that it "
            "misses the line - a few centimeters of deflection at the bridge "
            "is a complete miss at the body. Footwork serves the same "
            "master: step to place your centerline facing the opponent's "
            "while your turning takes your own centerline off their line of "
            "attack. Every drill in the system is scored against this "
            "standard: did the technique protect your line and threaten "
            "theirs, or did it wander."
        ),
        "key_points": [
            "The centerline is the vertical plane through the body's vital targets; guarding it and attacking along it is the whole strategy in one sentence.",
            "The straight line is the shortest path: a 1.50 meter centerline attack beats a 2.36 meter circular attack by about 36 percent of the distance, so equal timing always favors the straight punch.",
            "The guard lives on the centerline - hands between you and the opponent, elbows sunk - so every straight attack must pass through your hands first.",
            "Defense means deflecting attacks just off the line; an attack that does not threaten your centerline is ignored, which stops the fighter from chasing hands.",
            "Footwork serves the line: step to face the opponent's centerline while turning yours away, and every technique is judged by whether it protected your line and threatened theirs.",
        ],
        "requirements": [
            "A clear mental picture of the vertical line from crown to groin, checked in a mirror until the guard sits on it without looking.",
            "A guard with both hands on or near the line and elbows pointing down it, held without shoulder tension.",
            "Punches that travel straight along the line from wherever the hand starts, with no wind-up and no wide swing.",
            "Deflections that move the incoming arm just centimeters off the line at the bridge point.",
            "Footwork that re-faces the opponent's centerline after every step and turn.",
        ],
        "standards": [
            "Every technique in every drill is measured against the centerline standard: protect yours, threaten theirs.",
            "Straight-line attacks are drilled before any circular technique, so the shortest path becomes the default.",
            "Partner drills use light, controlled contact on the line, with a qualified instructor supervising alignment.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_YIMM],
        "sig_lens": (
            "The Signature read: the centerline is the Signature line - the "
            "axis every technique is measured from. Where public instruction "
            "draws a line on the body, the Signature Combat Method treats it "
            "as a covenant: nothing you do may abandon the line, and "
            "everything you do must arrive along it. Guard the line and the "
            "line guards you."
        ),
    },
    {
        "key": "stance",
        "name": "Yee Jee Kim Yeung Ma: The Basic Stance",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Yee Jee Kim Yeung Ma - the character-two goat-clamping stance, "
            "named for the way the written character for 'two' looks like "
            "the feet and for the adduction that feels like gripping a goat "
            "between the knees - is the foundation every Wing Chun technique "
            "stands on. The feet sit about shoulder width apart, roughly "
            "0.45 meters for an average adult, toes turned inward, knees "
            "bent and pressed gently inward, pelvis tucked, spine straight, "
            "head up. The weight splits exactly 50/50: a 70 kilogram "
            "practitioner carries 35 kilograms on each foot, which keeps "
            "either leg free to kick without shifting weight first. The "
            "stance is trained statically in the first form until the legs "
            "shake and then stop shaking - that burning phase builds the "
            "tendon strength and root that make every later technique "
            "possible. A rooted stance is a stable platform: with the center "
            "of mass about 0.95 meters high and a half-base of 0.225 meters, "
            "the body can tip about 13.3 degrees before the weight leaves "
            "the base, which is the margin a punch or a push has to "
            "overcome. Everything in Wing Chun - every punch, deflection, "
            "and step - is practiced from this stance first, because power "
            "that does not come from the ground is arm power, and arm power "
            "is the first thing the art discards."
        ),
        "how_it_works": (
            "Stand with feet shoulder width apart and turn the toes inward "
            "until the feet form a shallow V pointing at each other. Sink "
            "by bending the knees and pushing them gently inward as if "
            "gripping a ball between them, tuck the pelvis under, straighten "
            "the lower back, and let the weight settle evenly - rock "
            "slightly forward and back until neither foot feels heavier. "
            "The knees track over the toes; the shoulders stay relaxed and "
            "down; the head floats up as if suspended by a string. Hold "
            "this while practicing the first form's hand techniques: the "
            "stance must not rise, shift, or wobble when the arms move, "
            "which teaches the separation of upper and lower body that "
            "makes the punches fast - the arms fire while the platform stays "
            "still. When the legs burn, stay a little longer; when they go "
            "numb, shake out and reset. Train it daily, a few minutes at a "
            "time, and the stance becomes the place the body returns to "
            "without thinking."
        ),
        "key_points": [
            "Yee Jee Kim Yeung Ma is the goat-clamping stance: feet shoulder width apart, toes in, knees bent and pressed inward, pelvis tucked, weight 50/50.",
            "The even weight split - 35 kilograms per foot for a 70 kilogram practitioner - keeps either leg free to kick with no preparatory shift.",
            "Static stance training builds the tendon strength and root that every punch, deflection, and step depends on.",
            "The geometry gives real stability: the body can tip about 13.3 degrees before leaving its base, a measurable margin against pushes.",
            "All hand techniques are learned in this stance first, so the arms learn to fire while the platform stays perfectly still.",
        ],
        "requirements": [
            "Feet about shoulder width apart with toes turned inward and knees bent and adducted.",
            "Weight distributed exactly evenly between the feet, verified by rocking until neither foot feels heavier.",
            "An upright spine with tucked pelvis and relaxed shoulders, held without leaning.",
            "The ability to hold the stance through the first form's hand movements without rising or wobbling.",
            "Daily static practice, increasing duration gradually as the legs adapt.",
        ],
        "standards": [
            "The stance is trained before any stepping: static root first, mobile root later.",
            "Knees track over the toes at all times; knee pain is a stop signal, never trained through.",
            "A qualified instructor checks alignment - toe angle, knee tracking, pelvic tuck - before long holds are assigned.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_WINGTSUN],
        "sig_lens": (
            "The Signature read: the stance is the oath of the ground. "
            "Where public instruction counts kilograms per foot, the "
            "Signature Combat Method treats the 50/50 split as a covenant "
            "with the earth - neither leg favored, neither leg burdened, "
            "both ready. Root first; everything thrown from an unrooted "
            "body is a promise the ground will not keep."
        ),
    },
    {
        "key": "guard",
        "name": "Man Sau and Wu Sau: The Guard",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The Wing Chun guard is two hands with two jobs. The Man Sau, "
            "the asking hand, extends forward along the centerline with the "
            "palm open and relaxed, roughly a forearm's length from the "
            "chest - it 'asks' the opponent's intentions by making the first "
            "bridge contact, feeling pressure the instant an attack begins. "
            "The Wu Sau, the protecting hand, sits back near the chest or "
            "throat, elbow sunk on the centerline, guarding the line the "
            "asking hand cannot cover. Together they divide the frontal arc: "
            "the forward hand commands about 60 degrees of the space ahead, "
            "the rear hand about 40 degrees, with roughly 15 degrees of "
            "overlap - about 85 degrees of a 180-degree frontal arc, or "
            "47.2 percent, under direct hand coverage, and the rest managed "
            "by footwork and turning. The guard is alive, not frozen: the "
            "asking hand extends and withdraws, the protecting hand fills "
            "whatever gap opens, and neither hand ever drops below the "
            "elbows' guard of the ribs. Beginners learn the guard as a shape; "
            "intermediate students learn it as a conversation, with the "
            "asking hand constantly probing and the protecting hand "
            "constantly answering."
        ),
        "how_it_works": (
            "From the basic stance, extend your lead hand forward along the "
            "centerline to about a forearm's length, palm facing the "
            "opponent, fingers relaxed and slightly up - this is the Man "
            "Sau, and it should feel like reaching to shake hands with "
            "someone's attack. Hold your rear hand back, palm facing your "
            "own chest, elbow dropped onto the centerline - this is the Wu "
            "Sau, the last wall before your throat. Keep the elbows down and "
            "in; flared elbows open the ribs and abandon the line. As the "
            "partner moves, let the asking hand ride their lead arm with "
            "light contact, feeling for pressure changes, while the "
            "protecting hand shadows the centerline behind it. When their "
            "arm presses, the asking hand becomes a deflection - Tan Sau, "
            "Pak Sau, Bong Sau - and the protecting hand instantly takes "
            "the asking hand's place on the line. Drill it slowly: one "
            "partner feeds straight punches, the other keeps the guard's "
            "shape while deflecting, never letting either hand leave the "
            "centerline unguarded."
        ),
        "key_points": [
            "The Man Sau (asking hand) extends forward to make first bridge contact and feel the attack coming; the Wu Sau (protecting hand) guards the centerline behind it.",
            "The two hands divide the frontal space - about 60 degrees forward and 40 degrees rear with overlap - so the centerline is never uncovered.",
            "Elbows stay down and in; flared elbows open the ribs and abandon the guard's geometry.",
            "The guard is active: the asking hand probes and deflects while the protecting hand continuously refills the line.",
            "Beginners learn the shape; intermediate students learn the conversation between the two hands.",
        ],
        "requirements": [
            "A lead hand extended along the centerline at a forearm's length, palm open and relaxed.",
            "A rear hand held back guarding the throat and chest with the elbow sunk on the line.",
            "Elbows down and in at all times, protecting the ribs.",
            "Light, sensitive bridge contact through the asking hand, reading pressure rather than pushing.",
            "Instant refill: whenever one hand leaves the line to deflect, the other takes its place.",
        ],
        "standards": [
            "Guard drills begin with slow, cooperative straight punches and only accelerate when the shape holds.",
            "Contact stays light and controlled; the guard is a sensing tool, not a pushing tool.",
            "A qualified instructor verifies that neither hand abandons the centerline during deflections.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_YIMM],
        "sig_lens": (
            "The Signature read: two hands, one covenant. The asking hand "
            "goes out as the Signature's question and the protecting hand "
            "stays as its answer - the line is never left alone. Where "
            "public instruction stations two guards, the Signature Combat "
            "Method stations a conversation: ask, listen, answer, and never "
            "let the centerline stand undefended."
        ),
    },
    {
        "key": "punch",
        "name": "Yat Jee Chung Kuen: The Vertical Punch",
        "group": "Hand Techniques",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Yat Jee Chung Kuen - the character-sun thrusting punch, named "
            "for the shape of the written character for 'sun' - is the "
            "primary strike of Wing Chun and one of the most analyzed "
            "punches in martial arts. The fist is vertical, knuckles stacked "
            "vertically, wrist straight, elbow pointing down along the "
            "centerline; it travels the shortest path from wherever the "
            "hand starts straight to the target, usually the opponent's "
            "centerline at solar plexus or nose height. The numbers explain "
            "its reputation: the fist covers about 0.55 meters in roughly "
            "0.12 seconds, reaching about 4.58 meters per second, and with "
            "an effective body mass of about 4 kilograms behind it the "
            "punch carries roughly 42 joules of kinetic energy and 18.3 "
            "kilogram-meters per second of momentum - delivered without any "
            "wind-up, from the guard, along the centerline. The elbow-down "
            "structure protects the ribs during the punch and lets the "
            "punch retract along the same line it traveled, so the hand "
            "returns to guard in the same 0.12 seconds. Because the punch "
            "starts from the centerline and returns to it, it chains "
            "naturally - one punch chambers the next, which is the basis "
            "of the famous chain punching."
        ),
        "how_it_works": (
            "From the guard, pick a target on the partner's centerline - a "
            "focus mitt held at solar plexus height works best. Without "
            "pulling the hand back, drive the fist straight forward along "
            "the line, rotating the forearm only enough to bring the fist "
            "vertical, knuckles stacked, wrist locked straight. The elbow "
            "stays down and travels behind the fist on the centerline; the "
            "shoulder stays down and relaxed; the power comes from the "
            "ground through the stance, a small hip rotation, and the "
            "triceps snapping the arm straight at the end. Strike with the "
            "fist's face and snap it back along the exact same path - the "
            "retraction is as fast as the punch, which is what makes the "
            "next punch possible. Drill it first in the air for form, then "
            "on a wall bag for impact, then on mitts for accuracy: fifty "
            "slow perfect punches beat five hundred sloppy ones. Keep the "
            "non-punching hand guarding the line - the punch never costs "
            "you your defense."
        ),
        "key_points": [
            "The vertical fist travels straight along the centerline from wherever the hand starts, with no wind-up and no telegraph.",
            "Real measured dynamics: about 0.55 meters in 0.12 seconds gives 4.58 meters per second, about 42 joules, and 18.3 kilogram-meters per second of momentum.",
            "The elbow stays down on the centerline behind the fist, protecting the ribs and keeping the structure intact.",
            "The punch retracts along the same line it traveled, at the same speed, which chambers the next punch automatically.",
            "Power comes from the ground through the stance and hip, not from the shoulder - the arm is the delivery system, not the engine.",
        ],
        "requirements": [
            "A vertical fist with stacked knuckles and a straight, locked wrist at impact.",
            "An elbow that travels down the centerline behind the fist, never flaring out.",
            "A straight-line path from guard to target and back, with no pull-back before the punch.",
            "Relaxed shoulders and power driven from the stance and hip rotation.",
            "The non-punching hand holding the guard on the centerline throughout.",
        ],
        "standards": [
            "Form is drilled in the air before any impact work; impact begins on a wall bag, then mitts.",
            "Wrist alignment is checked by an instructor before power is added - a bent wrist under load is an injury.",
            "Partner mitt work uses controlled power with headgear available when targeting head height.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_WINGTSUN, CIT_YIMM],
        "sig_lens": (
            "The Signature read: the punch is the Signature's exclamation "
            "mark - straight, vertical, and already on the line before it "
            "is thrown. Where public instruction measures joules, the "
            "Signature Combat Method measures honesty: the punch that "
            "travels the shortest path cannot lie about its intention, and "
            "the fist that returns along the same line keeps every promise "
            "the guard made."
        ),
    },
    {
        "key": "chain_punch",
        "name": "Lin Wan Kuen: Chain Punching",
        "group": "Hand Techniques",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Lin Wan Kuen, chain punching - literally 'continuous circling "
            "fists' - is Wing Chun's signature offensive: a stream of "
            "vertical punches fired straight down the centerline, each "
            "punch retracting as the next fires, so the opponent faces an "
            "unbroken wall of fists. The mechanics are what make it "
            "possible: because each punch starts on the centerline and "
            "returns to it, no punch interferes with the next, and the "
            "retraction of one arm chambers the other. The output is "
            "remarkable for a human striking system: a trained practitioner "
            "fires about 8 punches in 1.2 seconds, roughly 6.67 punches per "
            "second or 400 punches per minute, each carrying about 42 "
            "joules - a sustained delivery of about 336 joules at roughly "
            "280 watts of striking power. Chain punching is not wild "
            "flailing; it is disciplined forward pressure. The practitioner "
            "steps in behind the punches, each punch occupying the "
            "centerline the opponent needs to counter through, so the "
            "defense and the offense are the same action: the punches "
            "themselves jam the opponent's attempts to punch back."
        ),
        "how_it_works": (
            "Start in the guard with a partner holding two focus mitts on "
            "their centerline. Fire the lead punch straight down the line, "
            "and the instant it lands, snap it back while the rear hand "
            "fires past it - the hands pass each other on the centerline "
            "like pistons. Keep the elbows down, the shoulders relaxed, and "
            "the rhythm even: the most common error is starting fast and "
            "decaying, so train with a metronome or a count, holding a "
            "steady cadence for the full burst. Step forward as you punch, "
            "one small step per two punches, driving the whole wall of "
            "fists into the opponent's space - the feet and the fists move "
            "as one unit. Breathe out in short bursts with the punches, "
            "never holding the breath. Drill in sets: 8-punch bursts with "
            "full recovery between them, then 15-second sustained rounds, "
            "then 30 seconds. Stop the set the moment the elbows flare or "
            "the punches start looping - chain punching is only chain "
            "punching while every punch stays on the line."
        ),
        "key_points": [
            "Chain punching fires continuous vertical punches down the centerline, each punch's retraction chambering the next like pistons.",
            "Measured output runs about 8 punches in 1.2 seconds - 6.67 per second, 400 per minute - delivering roughly 336 joules at about 280 watts.",
            "The punches themselves are the defense: occupying the centerline jams the opponent's ability to punch back through it.",
            "Forward stepping behind the punches turns a hand technique into whole-body pressure.",
            "The drill is only valid while every punch stays straight on the line - looping punches mean the set is over.",
        ],
        "requirements": [
            "A clean vertical punch that starts and returns on the centerline, so consecutive punches never interfere.",
            "Alternating piston rhythm with even cadence, trained to a count or metronome.",
            "Forward stepping coordinated with the punches - about one small step per two punches.",
            "Relaxed shoulders and short exhaled breaths; no breath-holding under the burst.",
            "An immediate stop when form decays: flared elbows or looping punches end the set.",
        ],
        "standards": [
            "Chain punching is drilled on mitts and bags before any partner application, with protective gear for contact rounds.",
            "Burst length increases only while every punch holds the centerline; volume never outruns form.",
            "Partner drills cap contact power and require headgear at head height.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_WINGTSUN],
        "sig_lens": (
            "The Signature read: chain punching is the Signature's drumbeat "
            "- one line, struck again and again, never leaving the line it "
            "strikes along. Where public instruction counts punches per "
            "minute, the Signature Combat Method hears a promise kept at "
            "speed: every punch guards the line it attacks along, so the "
            "offense never borrows from the defense."
        ),
    },
    {
        "key": "tan_sau",
        "name": "Tan Sau: The Dispersing Hand",
        "group": "Hand Techniques",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Tan Sau, the dispersing hand - the name evokes spreading or "
            "opening, like parting a curtain - is the first deflection every "
            "Wing Chun student learns and the purest expression of the "
            "art's defensive idea: do not block force, disperse it. The "
            "hand is palm-up, fingers pointing forward along the centerline, "
            "elbow sunk and anchored on the centerline about a fist's "
            "distance from the body. When a straight punch arrives, the Tan "
            "Sau meets it from underneath and slightly to the side, "
            "redirecting it off the line rather than stopping it. The "
            "physics favor the defender: an incoming punch of 100 newtons "
            "arriving 30 degrees off the defender's centerline needs only "
            "to be turned 60 degrees off its path, leaving just 50 newtons "
            "still traveling toward the original target while 86.6 newtons "
            "of its force is shunted sideways into empty space. The elbow "
            "never leaves the centerline - that immovable elbow is what "
            "makes Tan Sau a structure instead of a slap. Tan Sau appears "
            "in the first form, in single-hand sticking, and as half of the "
            "Kwan Sau combination, making it the most drilled hand in the "
            "system."
        ),
        "how_it_works": (
            "From the guard, let the partner throw a slow straight punch at "
            "your chest. As it arrives, turn your lead hand palm-up and "
            "slide it forward and slightly outward along the centerline, "
            "meeting their forearm from underneath with the outer edge of "
            "your hand and wrist. The elbow stays pinned on the centerline - "
            "imagine it nailed to a point a fist's width in front of your "
            "solar plexus - and the whole motion is a small forward wedge, "
            "not a big sideways sweep. Contact the punch early, near their "
            "wrist, where the leverage favors you, and let their own forward "
            "energy carry their fist past your shoulder while your hand "
            "continues to their centerline as a punch. The instant the "
            "deflection is complete, the Tan Sau is already becoming your "
            "attack - deflection and counter are one motion. Drill it from "
            "Dan Chi Sao first, then against slow straight punches, then "
            "against faster ones, always checking that the elbow never "
            "drifted off the line."
        ),
        "key_points": [
            "Tan Sau disperses rather than blocks: the palm-up hand wedges the incoming punch off the centerline and lets its own energy carry it past.",
            "The force math favors deflection - a 100 newton punch turned 60 degrees off path leaves only 50 newtons on target while 86.6 newtons go sideways.",
            "The elbow stays anchored on the centerline; that immovable elbow is what turns the hand from a slap into a structure.",
            "Contact happens early, near the opponent's wrist, where leverage favors the defender.",
            "Deflection and counter are one motion: the dispersing hand continues forward as the attack.",
        ],
        "requirements": [
            "A palm-up hand with fingers forward along the centerline and the elbow sunk a fist's width from the body.",
            "An elbow that never leaves the centerline during the deflection.",
            "Early contact near the opponent's wrist with a small forward wedge motion, not a wide sweep.",
            "Forward pressure maintained through the deflection so the hand arrives as a counter.",
            "Relaxed shoulders - tension in the shoulder collapses the elbow's structure.",
        ],
        "standards": [
            "Tan Sau is drilled first in single-hand sticking, then against slow straight punches, then at speed.",
            "Partner contact stays light; the deflection is practiced as redirection, never as a strike to the partner's arm.",
            "An instructor verifies the elbow's position on the centerline before speed is added.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_WINGTSUN, CIT_DUMMY116],
        "sig_lens": (
            "The Signature read: Tan Sau is the Signature's open palm - it "
            "does not meet force with force but shows force the door. Where "
            "public instruction teaches a deflection, the Signature Combat "
            "Method teaches a courtesy with geometry: the elbow keeps its "
            "covenant with the line, and the attack, politely redirected, "
            "defeats itself."
        ),
    },
    {
        "key": "bong_sau",
        "name": "Bong Sau: The Wing Arm",
        "group": "Hand Techniques",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Bong Sau, the wing arm - named for the way the bent arm "
            "resembles a wing - is Wing Chun's emergency deflection, the "
            "technique that saves the fighter when a punch has gotten too "
            "close and too far inside for Tan Sau. The elbow rises and the "
            "forearm rolls over the incoming arm like a wing folding, with "
            "the elbow higher than the hand and the forearm angled across "
            "the centerline. It is a recovery position with real structure: "
            "with the elbow as the pivot, an 80 newton punch landing 0.28 "
            "meters out on the forearm is balanced by the upper arm and "
            "shoulder working at a 0.10 meter lever - about 224 newtons of "
            "muscle force, well within what the shoulder girdle produces, "
            "which is why the wing holds against punches that would blow "
            "through a weaker shape. Bong Sau is never a destination; it is "
            "a bridge. Held too long it collapses, but rolled through - "
            "Bong Sau turning into Tan Sau as the pressure passes - it "
            "converts a losing position into an attack. It appears in the "
            "first form's third section, in double-hand rolling, and as "
            "half of Kwan Sau, and students drill the Bong-to-Tan roll "
            "until it happens faster than thought."
        ),
        "how_it_works": (
            "Have the partner press a slow straight punch deep toward your "
            "chest, inside your Tan Sau's range. Let your elbow rise and "
            "roll the forearm over their arm, elbow high, wrist low, the "
            "forearm lying across their punch like a wing over it - the "
            "contact rolls their force up and over your shoulder instead of "
            "into your chest. Keep the shoulder down even as the elbow "
            "rises; a shrugged shoulder disconnects the structure from the "
            "body. The instant their pressure slides off, roll the wing "
            "down and forward into Tan Sau and punch with the same hand - "
            "Bong Sau, Tan Sau, punch is one continuous roll, drilled as a "
            "single breath. Common faults: holding the wing statically "
            "until it collapses, letting the elbow drift out past the "
            "shoulder line, and muscling the roll with the shoulder instead "
            "of letting the forearm's rotation do the work. Drill it in Luk "
            "Sao rolling first, where the Bong appears naturally in the "
            "cycle, then against a partner who deliberately punches too "
            "deep, so the emergency feels familiar when it arrives for real."
        ),
        "key_points": [
            "Bong Sau is the emergency deflection for punches that get too close and too far inside for Tan Sau - the elbow rises and the forearm rolls over the attack like a wing.",
            "The lever math works: an 80 newton punch at 0.28 meters from the elbow pivot is held by about 224 newtons of shoulder force at a 0.10 meter lever.",
            "Bong Sau is a bridge, never a destination - held statically it collapses; rolled through into Tan Sau it becomes an attack.",
            "The shoulder stays down while the elbow rises; shrugging disconnects the wing from the body's structure.",
            "The Bong-to-Tan roll is drilled until it fires faster than thought, appearing in the first form, in rolling hands, and in Kwan Sau.",
        ],
        "requirements": [
            "An elbow that rises above the hand with the forearm angled across the centerline, rolling over the incoming arm.",
            "A shoulder that stays down and connected while the elbow lifts.",
            "An immediate roll-through: Bong Sau converts to Tan Sau and then to a punch as one continuous motion.",
            "Contact that guides the punch up and over the shoulder rather than stopping it dead.",
            "No static holding - the wing exists only in motion.",
        ],
        "standards": [
            "Bong Sau is learned inside Luk Sao rolling before it is drilled as an isolated emergency.",
            "Partners feed deep, slow punches first; speed rises only when the roll-through stays continuous.",
            "An instructor watches for the two classic faults: the static wing and the shrugged shoulder.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_WINGTSUN],
        "sig_lens": (
            "The Signature read: Bong Sau is the Signature's folding wing - "
            "the covenant that no lost position stays lost. Where public "
            "instruction teaches an emergency shape, the Signature Combat "
            "Method teaches a promise: the wing rises, the pressure passes "
            "over, and the roll carries the fighter from defense to attack "
            "without ever abandoning the line."
        ),
    },
    {
        "key": "fook_sau",
        "name": "Fook Sau: The Controlling Hand",
        "group": "Hand Techniques",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Fook Sau, the controlling or subduing hand - the character "
            "carries the sense of lying over and covering - is the palm-down "
            "hand that rests on top of the opponent's bridge and controls "
            "it. Where Tan Sau disperses from underneath, Fook Sau pins from "
            "above: the hand lies palm-down across the opponent's forearm, "
            "elbow sunk on the centerline, wrist relaxed, using the natural "
            "weight of the arm plus a small downward intention to keep the "
            "opponent's arm trapped. The control is economical rather than "
            "muscular: a forearm of about 1.6 kilograms plus 20 newtons of "
            "applied downward pressure delivers about 35.7 newtons of "
            "pinning force onto the bridge - against an opponent's arm that "
            "can lift perhaps 25 newtons from that angle, the net pin of "
            "about 10.7 newtons is enough to smother the arm's attempts to "
            "rise or punch. Fook Sau is the resting state of chi sao: in "
            "double-hand rolling, each hand spends half its time as Fook "
            "Sau, lying on the partner's arm, feeling for the instant the "
            "pressure changes and the arm can be struck through. Students "
            "learn it in the first form, then live in it during months of "
            "sticking-hands practice."
        ),
        "how_it_works": (
            "From the guard, lay your lead hand palm-down across the "
            "partner's extended forearm, wrist relaxed, fingers pointing "
            "along their arm toward their elbow. Sink your elbow onto the "
            "centerline and let the arm's weight settle onto their bridge - "
            "do not press with the shoulder; the control comes from "
            "structure and a small downward intention, not from pushing. "
            "Your hand should feel heavy to them and light to you. As they "
            "try to lift, circle, or punch, maintain the contact and follow "
            "their motion without losing the top position: if they press "
            "up, sink slightly and let their force run into your elbow's "
            "structure; if they withdraw, follow forward and punch. The "
            "classic drill is Dan Chi Sao, where Fook Sau alternates with "
            "Tan Sau in a continuous cycle, teaching the hand to control "
            "without grabbing - the moment you grab, you commit your hand "
            "and lose the sensitivity. Check constantly: can you lift your "
            "fingers off their arm without your elbow moving? If yes, the "
            "structure is carrying the control, not your muscles."
        ),
        "key_points": [
            "Fook Sau is the palm-down controlling hand that lies over the opponent's bridge, pinning from above where Tan Sau disperses from below.",
            "The pin is economical: about 1.6 kilograms of forearm plus 20 newtons of intention gives 35.7 newtons of control against roughly 25 newtons of lift - a net pin of 10.7 newtons.",
            "Control comes from structure and weight, never from grabbing or shoulder-pressing; grabbing commits the hand and kills sensitivity.",
            "Fook Sau is the resting state of chi sao - each hand spends half the rolling cycle lying on the partner's arm, listening for the opening.",
            "The test of correct Fook Sau: the fingers can lift off the bridge without the elbow moving, proving structure carries the control.",
        ],
        "requirements": [
            "A palm-down hand lying across the opponent's forearm with a relaxed wrist and fingers pointing toward their elbow.",
            "An elbow sunk on the centerline carrying the control through structure, not muscle.",
            "Downward intention without shoulder pressure - heavy to the opponent, light to you.",
            "Continuous following contact: the hand stays on top through lifts, circles, and withdrawals.",
            "No grabbing - the hand controls by position and weight, staying free to strike.",
        ],
        "standards": [
            "Fook Sau is built in Dan Chi Sao before it is trusted in free rolling or sparring.",
            "Partners keep the bridge pressure honest but light; leaning body weight onto the control is a fault.",
            "Instructors check the finger-lift test regularly to keep the control structural, not muscular.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_WINGTSUN],
        "sig_lens": (
            "The Signature read: Fook Sau is the Signature's resting hand - "
            "control without grasping, presence without force. Where public "
            "instruction teaches a pin, the Signature Combat Method teaches "
            "a covenant of weight: the hand lies on the bridge and keeps "
            "its word, feeling everything and holding nothing, free to "
            "become a punch the instant the bridge speaks."
        ),
    },
    {
        "key": "pak_sau",
        "name": "Pak Sau: The Slapping Hand",
        "group": "Hand Techniques",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Pak Sau, the slapping hand, is Wing Chun's line-clearer: a "
            "short, sharp slap with the palm that knocks the opponent's "
            "arm off the centerline and opens the road for the punch that "
            "follows in the same beat. Unlike Tan Sau's wedge or Fook Sau's "
            "pin, Pak Sau is percussive - it meets the incoming or guarding "
            "arm with a crisp redirecting slap, usually from outside to "
            "inside, clearing the centerline for a fraction of a second "
            "that is all the punch needs. The timing math shows why it "
            "works: a 0.5 kilogram hand traveling 0.25 meters in 0.08 "
            "seconds reaches 3.125 meters per second, carrying 1.56 "
            "kilogram-meters per second of momentum - against an "
            "opponent's 3 kilogram arm drifting at 1 meter per second, the "
            "slap redirects the arm by about 27.5 degrees, more than enough "
            "to clear the line for the punch arriving behind it. Pak Sau "
            "pairs with the punch in the classic one-two of Lop Sao "
            "drills: slap the arm aside, punch through the gap, and the "
            "two actions land as a single beat. It is drilled in the first "
            "form, in Dan Chi Sao, and in every entry drill in the system."
        ),
        "how_it_works": (
            "Face the partner in guard with their lead hand on your "
            "centerline. Slap the back of their wrist with your palm, a "
            "short chopping motion from your centerline outward-in, "
            "knocking their arm across and off your line - the power comes "
            "from a snap of the elbow and a small body turn, not from a "
            "big arm swing. The instant their arm clears, fire the vertical "
            "punch straight down the opened line with the same hand or the "
            "other: Pak, punch - one beat, not two. The slap must be short; "
            "a long swing is a telegraph and leaves your own line open. "
            "Drill it first against a static guard arm, then against a "
            "partner who tries to keep their arm on your line, then inside "
            "the Lop Sao cycle where the Pak follows a pull. Keep the "
            "non-slapping hand guarding throughout - clearing their line "
            "must never cost you yours. The sound of a good Pak Sau is a "
            "sharp crack; the feeling is of the arm simply not being there "
            "anymore."
        ),
        "key_points": [
            "Pak Sau is the percussive line-clearer: a short palm slap that knocks the opponent's arm off the centerline for the punch behind it.",
            "The momentum math works - a 0.5 kilogram hand at 3.125 meters per second redirects a 3 kilogram guarding arm by about 27.5 degrees, clearing the line.",
            "Pak and punch land as one beat, not two; the slap exists only to open the road the punch travels.",
            "The slap is short and elbow-driven; a long swing telegraphs and abandons your own guard.",
            "It pairs with the punch in every entry drill in the system, from Dan Chi Sao to the Lop Sao cycle.",
        ],
        "requirements": [
            "A short, sharp palm slap from the centerline, powered by elbow snap and a small body turn.",
            "Contact on the opponent's wrist or forearm that redirects the arm across and off your line.",
            "An immediate punch down the cleared line, landing as the same beat as the slap.",
            "No long swing - the hand travels the minimum distance to clear the arm.",
            "The other hand holding the guard on your own centerline throughout.",
        ],
        "standards": [
            "Pak Sau is drilled against static arms before moving guards, and against cooperative partners before resisting ones.",
            "Slap contact to a partner's arm stays controlled; the drill trains redirection, not punishment.",
            "Instructors check that the punch truly follows in the same beat - a delayed punch is a failed Pak Sau.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_YIMM],
        "sig_lens": (
            "The Signature read: Pak Sau is the Signature's knock on the "
            "door - one sharp note that moves the obstacle aside. Where "
            "public instruction teaches a slap, the Signature Combat Method "
            "teaches a courtesy of timing: clear the line in the same beat "
            "the punch claims it, and never leave your own door unguarded "
            "while you knock on theirs."
        ),
    },
    {
        "key": "advance",
        "name": "Seung Ma and Tui Ma: Advancing and Retreating",
        "group": "Footwork",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Seung Ma (advancing step) and Tui Ma (retreating step) are Wing "
            "Chun's straight-line footwork: the whole stance glides forward "
            "or backward as a single unit, weight staying 50/50, the "
            "centerline facing the opponent at all times. The step is small "
            "and economical - about 0.5 meters - and quick: at a drill "
            "cadence of 2 steps per second the practitioner closes at 1.0 "
            "meter per second, crossing a 1.5 meter gap in 1.5 seconds, "
            "three steps, without ever abandoning the stance's structure. "
            "The key discipline is that the upper body does not bob, lean, "
            "or telegraph: the head stays level, the guard stays on the "
            "line, and the step is felt by the opponent only when the "
            "distance has already changed. Beginners learn the step as a "
            "slide - the feet skim the floor - because lifting the feet "
            "high breaks the root and signals the movement. Advancing "
            "footwork carries the chain punching forward; retreating "
            "footwork yields ground without yielding structure, drawing the "
            "attacker onto the defender's counter. Both are drilled in "
            "straight lines first, then with turns, then against a moving "
            "partner."
        ),
        "how_it_works": (
            "From the basic stance, slide the front foot forward about 0.5 "
            "meters, skimming the floor, and let the rear foot follow to "
            "restore the stance - the feet move one at a time but the body "
            "glides as one piece, head level, guard untouched. For the "
            "retreat, reverse it: rear foot slides back first, front foot "
            "follows. Keep the weight 50/50 throughout; the most common "
            "fault is leaning into the step, which loads the front leg and "
            "kills the ability to kick or turn. Drill it on a line on the "
            "floor: advance three steps, retreat three steps, keeping the "
            "stance width and toe angle identical at every stop - have a "
            "partner watch your head against a wall mark to prove it never "
            "bobs. Then add the hands: advance behind chain punching, "
            "retreat behind Tan Sau deflections, so the feet and hands learn "
            "their partnership. Finally, drill against a partner who "
            "advances on you: hold your ground with the guard, then retreat "
            "one step and counter as their momentum carries them onto your "
            "punch."
        ),
        "key_points": [
            "Seung Ma and Tui Ma move the whole stance as one unit forward or back, weight staying 50/50 and the centerline always facing the opponent.",
            "The step is small and fast: 0.5 meter steps at 2 per second close distance at 1.0 meter per second - a 1.5 meter gap falls in 1.5 seconds.",
            "The head stays level and the guard stays on the line; the opponent should feel the distance change, not see the step coming.",
            "Feet skim the floor in a slide; lifting high breaks the root and telegraphs.",
            "Advancing carries the attack forward; retreating yields ground without yielding structure, drawing the attacker onto the counter.",
        ],
        "requirements": [
            "A stance that moves as a single gliding unit, front foot then rear foot on the advance, rear then front on the retreat.",
            "Weight held 50/50 through every step, with no leaning into the direction of travel.",
            "A level head and an undisturbed guard - the upper body must not bob or telegraph.",
            "Feet skimming the floor, stance width and toe angle identical after each step.",
            "Coordination with the hands: stepping behind punches on the advance, behind deflections on the retreat.",
        ],
        "standards": [
            "Straight-line stepping is mastered before any turning or angled footwork is introduced.",
            "Head-bob is checked against a fixed reference until the glide is level.",
            "Partner footwork drills use agreed cadences and stop instantly on loss of stance structure.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_WINGTSUN],
        "sig_lens": (
            "The Signature read: the step is the Signature's quiet promise - "
            "the ground changes beneath the fighter while nothing above "
            "the waist admits it. Where public instruction teaches advance "
            "and retreat, the Signature Combat Method teaches a single "
            "glide that keeps its covenant with the stance: the line "
            "faces the opponent at every instant of the journey."
        ),
    },
    {
        "key": "turn",
        "name": "Juen Ma: Turning the Stance",
        "group": "Footwork",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Juen Ma, turning the stance, is how Wing Chun changes facing "
            "without changing structure: the practitioner pivots on the "
            "heels, rotating the whole stance - typically 45 degrees - "
            "while the hands stay on the centerline and the weight stays "
            "50/50. The turn does three jobs at once: it takes your "
            "centerline off the opponent's line of attack, it brings your "
            "centerline to face a new angle on the opponent, and it loads "
            "the hips to power the hands. The rotation is compact and fast: "
            "a 45 degree turn swings the hips through an arc of about 0.196 "
            "meters at a 0.25 meter hip radius, completed in roughly 0.25 "
            "seconds - an angular speed of about 3.14 radians per second, "
            "which is where turning punches get their whip. The discipline "
            "is that the turn comes from the stance, not the shoulders: "
            "beginners swing their arms and leave their feet behind, which "
            "abandons both the root and the line. Drilled correctly, the "
            "feet, hips, and hands arrive together, the guard never leaving "
            "the centerline during the rotation. Juen Ma is the footwork of "
            "Chum Kiu's second form and the engine of every angled counter "
            "in the system."
        ),
        "how_it_works": (
            "From the basic stance, pivot on the heels and rotate the "
            "entire stance 45 degrees to the side - the toes swing around, "
            "the knees track over the toes, the hips turn as one piece, and "
            "the hands stay exactly where they were relative to your chest, "
            "still guarding the centerline. The most common fault is turning "
            "the shoulders without the feet; fix it by having a partner hold "
            "your shoulders while you turn - only the stance should move. "
            "Drill the turn empty-handed first: 45 degrees left, back to "
            "center, 45 degrees right, keeping the stance width constant - "
            "mark the floor with tape and land on the marks. Then add the "
            "hands: turn with Tan Sau to deflect a punch from the new "
            "angle, turn with the punch to strike around the opponent's "
            "guard. Then drill against a partner who steps to your flank: "
            "turn to re-face their centerline while your hands answer their "
            "attack, so the turn and the defense are one motion. Speed comes "
            "last; the pivot must stay rooted before it gets fast."
        ),
        "key_points": [
            "Juen Ma pivots the whole stance on the heels, typically 45 degrees, while the hands stay on the centerline and the weight stays 50/50.",
            "One turn does three jobs: it removes your centerline from the attack line, re-faces the opponent's centerline, and loads the hips for power.",
            "The rotation is compact and fast - about 0.196 meters of hip arc in 0.25 seconds, roughly 3.14 radians per second - which whips the hands.",
            "The turn comes from the stance, not the shoulders; feet, hips, and hands must arrive together.",
            "It is the footwork of the second form and the engine of every angled counter in the system.",
        ],
        "requirements": [
            "A heel pivot rotating the entire stance as one piece, knees tracking over the toes.",
            "Hands that hold their position relative to the chest, never leaving the centerline during the rotation.",
            "Weight remaining 50/50 with the stance width unchanged - verified against floor marks.",
            "Feet, hips, and hands arriving together, with no shoulder-first swinging.",
            "Root before speed: the pivot stays stable and only then gets fast.",
        ],
        "standards": [
            "Empty-hand turning on floor marks is mastered before hand techniques are added to the turn.",
            "Knee tracking is monitored; any knee pain or inward collapse stops the drill for alignment correction.",
            "Partner angle drills start slow, with the turn and the defense required to land as one motion.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_WINGTSUN],
        "sig_lens": (
            "The Signature read: the turn is the Signature's pivot of "
            "fate - the line leaves the attack's path and finds the "
            "attacker's flank in a single rotation. Where public instruction "
            "teaches a 45 degree pivot, the Signature Combat Method teaches "
            "a covenant of arrival: feet, hips, and hands keep one "
            "appointment, and the guard never once leaves the line to keep it."
        ),
    },
    {
        "key": "siu_nim_tau",
        "name": "Siu Nim Tau: The First Form",
        "group": "Forms",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Siu Nim Tau - 'little idea' or 'little imagination' - is the "
            "first empty-hand form of Wing Chun and the foundation of the "
            "entire system. Performed entirely in the Yee Jee Kim Yeung Ma "
            "stance with no stepping, it teaches the alphabet of the art: "
            "the stance itself, the centerline, the guard, and the core "
            "hand techniques - Tan Sau, Fook Sau, Bong Sau, Pak Sau, the "
            "vertical punch - each drilled in slow, deliberate isolation. "
            "The form has three sections: the first trains stillness, "
            "structure, and the basic hand shapes with deep breathing; the "
            "second adds simultaneous hand actions and releases of energy; "
            "the third trains the Bong Sau roll and the punch. The scale of "
            "the training is serious: about 108 distinct hand movements "
            "performed over roughly 20 minutes of slow practice - about "
            "11.1 seconds per movement - with some 200 slow breath cycles "
            "at 6 seconds each, which is why the form builds tendon "
            "strength, relaxation under load, and the elbow discipline "
            "everything else depends on. Ip Man's Hong Kong students "
            "practiced it daily for years before advancing; the form is "
            "never truly finished, only deepened."
        ),
        "how_it_works": (
            "Stand in Yee Jee Kim Yeung Ma, settle the weight 50/50, and "
            "begin the first section at a glacial pace: each hand "
            "technique - the opening cross of the arms, the Tan Sau, the "
            "punch - is extended slowly, held, and withdrawn, while the "
            "stance never rises and the breathing stays deep and even. "
            "Resist the urge to rush; the slowness is the training, forcing "
            "the small stabilizing muscles and the tendons to carry loads "
            "the big muscles would otherwise steal. Move to the second "
            "section's paired hand actions and the third section's Bong "
            "Sau rolls and punches only when the first section's shapes "
            "hold without wobble. Practice daily, ideally in the morning: "
            "one slow pass of 20 minutes for structure, and later a second "
            "pass at natural speed for flow. Film yourself monthly from the "
            "front and side - the camera catches the rising stance, the "
            "drifting elbow, and the held breath that the mirror misses. "
            "Every fault found in the form is a fault that would appear in "
            "sparring, so the form is where faults go to be corrected."
        ),
        "key_points": [
            "Siu Nim Tau ('little idea') is the first form: the entire alphabet of Wing Chun - stance, centerline, guard, and core hand techniques - performed without stepping.",
            "Three sections train stillness and structure, simultaneous hand actions with energy release, and the Bong Sau roll with the punch.",
            "The training volume is real: about 108 movements over 20 slow minutes - 11.1 seconds per movement - with roughly 200 deep breath cycles.",
            "The slowness is the method: slow practice forces tendons and stabilizers to carry loads the big muscles would steal, building relaxation under load.",
            "The form is never finished, only deepened - every fault visible in the form would appear in sparring, so it is where faults are corrected.",
        ],
        "requirements": [
            "The Yee Jee Kim Yeung Ma stance held without rising, shifting, or wobbling through all three sections.",
            "Glacial pacing on the first section: each technique extended, held, and withdrawn with deep even breathing.",
            "Correct hand shapes - Tan, Fook, Bong, Pak, vertical punch - with elbows on the centerline.",
            "Daily practice: one slow structural pass, later plus one natural-speed pass for flow.",
            "Monthly self-review on video from front and side to catch stance, elbow, and breathing faults.",
        ],
        "standards": [
            "The form is learned section by section from a qualified instructor; the full sequence is earned, not rushed.",
            "Speed is added only after the slow form holds its structure; rushing the form trains rushing, not Wing Chun.",
            "Training is daily and patient - Ip Man's students spent years on this form before advancing.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_WINGTSUN, CIT_YIMM],
        "sig_lens": (
            "The Signature read: the first form is the Signature's quiet "
            "room - no stepping, no opponent, only the stance, the line, "
            "and the hands learning their alphabet at 11 seconds a letter. "
            "Where public instruction teaches a sequence, the Signature "
            "Combat Method teaches a covenant of patience: the fighter who "
            "can hold stillness correctly has already learned everything "
            "speed will later try to teach."
        ),
    },
    {
        "key": "lap_sau",
        "name": "Lap Sau: The Pulling Hand",
        "group": "Hand Techniques",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Lap Sau, the pulling or grabbing hand, is Wing Chun's way of "
            "stealing the opponent's balance and structure with a short, "
            "violent yank. The hand grabs the opponent's wrist or forearm - "
            "typically as they punch - and pulls it sharply down and across "
            "their own centerline while the other hand punches straight "
            "into the opening the pull creates. It is the compounded "
            "technique par excellence because it fuses offense and defense "
            "into a single beat: the pull IS the defense, clearing the line "
            "and dragging the opponent's structure with it, and the punch "
            "IS the offense, arriving before the opponent can recover. The "
            "work math is modest but the effect is outsized: a 60 newton "
            "pull applied over 0.2 meters does 12 joules of work, displacing "
            "the opponent's arm 0.2 meters in about 0.15 seconds - 1.33 "
            "meters per second of forced movement, faster than the "
            "opponent's structure can follow, which drags their shoulder "
            "forward and their weight onto their front foot. Lap Sau is the "
            "heart of the Lop Sao drill cycle, appears throughout the "
            "wooden dummy form, and is one of the first techniques students "
            "test in controlled sparring because its timing - pull as they "
            "commit - teaches the whole art of interception."
        ),
        "how_it_works": (
            "As the partner punches, catch their wrist with your lead hand "
            "- the grab is a hook of the fingers, not a death grip - and "
            "yank it sharply down and across toward their opposite hip, "
            "stepping slightly and turning your stance to add body weight "
            "to the pull. The pull must be sudden: a slow pull lets them "
            "brace, while a sharp 0.15 second yank moves their arm faster "
            "than their balance can answer. Simultaneously - the same beat, "
            "not after - drive the rear hand's vertical punch straight down "
            "the centerline their pulled arm just vacated. The two hands "
            "work as a team: puller and puncher, with the puller's elbow "
            "dropping to keep your own structure. Drill it in the Lop Sao "
            "cycle first: partner punches, you Lap and punch, they Pak your "
            "punch and punch back, cycling continuously. Then drill the "
            "timing against a partner who varies the punch speed - the Lap "
            "must catch the punch as it commits, neither reaching early nor "
            "chasing late. Keep the grab brief: hold too long and you are "
            "grappling, which is not Wing Chun's game."
        ),
        "key_points": [
            "Lap Sau grabs the opponent's punching arm and yanks it down and across their centerline while the other hand punches the opened line - pull and punch land as one beat.",
            "The yank is sudden, not strong: 60 newtons over 0.2 meters moves the arm at 1.33 meters per second, faster than the opponent's balance can follow.",
            "The pull IS the defense and the punch IS the offense; the technique fuses both into a single interception.",
            "Timing is everything: the Lap catches the punch as it commits - reaching early or chasing late both fail.",
            "The grab is brief by design; holding on turns the technique into grappling, which abandons Wing Chun's striking game.",
        ],
        "requirements": [
            "A hooking finger-grab on the wrist or forearm, caught as the punch commits.",
            "A sharp downward-across pull powered by a small stance turn, completed in about 0.15 seconds.",
            "A simultaneous vertical punch down the vacated centerline - same beat, not after.",
            "The pulling elbow dropping to preserve your own structure during the yank.",
            "An instant release: the hand lets go as the punch lands, never holding on.",
        ],
        "standards": [
            "Lap Sau is drilled first in the cooperative Lop Sao cycle, then against varied punch timing.",
            "The grabbing hand uses a hook grip, never a crushing grip; partner wrists are treated with care.",
            "Sparring application waits until the pull-punch lands as a true single beat in drills.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_DUMMY116],
        "sig_lens": (
            "The Signature read: Lap Sau is the Signature's sudden answer - "
            "the opponent's committed punch becomes the handle by which "
            "their balance is borrowed. Where public instruction teaches a "
            "pull and a punch, the Signature Combat Method teaches one "
            "covenant of timing: the yank and the strike keep a single "
            "appointment, and the line the pull vacates is the line the "
            "punch was always owed."
        ),
    },
    {
        "key": "jut_sau",
        "name": "Jut Sau: The Jerking Hand",
        "group": "Hand Techniques",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Jut Sau, the jerking hand, is Lap Sau's sharper, shorter "
            "cousin: instead of grabbing and pulling the arm across, the "
            "hand chops down onto the opponent's forearm with a sudden "
            "jerking shock that collapses the arm downward. The motion is "
            "small - a few centimeters of downward snap driven by the elbow "
            "and a tiny stance sink - but the impulse is real: jerking a "
            "3 kilogram arm downward at 8 meters per second squared applies "
            "24 newtons, and delivered in 0.1 seconds that is an impulse of "
            "2.4 newton-seconds, changing the arm's velocity by 0.8 meters "
            "per second downward - enough to smash a punch into the floor "
            "of its own trajectory and leave the centerline undefended. Jut "
            "Sau shines against committed straight punches and against "
            "opponents who press forward heavily onto your bridge: their "
            "own forward pressure plus your downward jerk folds their "
            "structure. It appears in the second form, in the dummy form's "
            "low sections, and throughout chi sao as the answer to a "
            "partner who leans on your hands. Students learn it after Lap "
            "Sau because the timing is identical - catch the commitment - "
            "but the tool is a shock rather than a pull."
        ),
        "how_it_works": (
            "As the partner's punch commits, meet their forearm from above "
            "with the edge of your hand and snap it downward in a short, "
            "violent jerk - the power comes from dropping the elbow and "
            "sinking the stance a fraction, not from swinging the arm. The "
            "contact is a shock, not a push: think of cracking a whip "
            "downward onto their arm rather than pressing it down. The "
            "instant their arm collapses, punch straight over it down the "
            "centerline - Jut, punch, one beat. The most common fault is "
            "turning the jerk into a long downward press, which commits "
            "your hand and your weight; the jerk must be over in a tenth "
            "of a second, with your hand already recovering as their arm "
            "falls. Drill it against a partner who punches and deliberately "
            "leans forward onto your bridge, so you feel how their pressure "
            "feeds the technique. Then drill the choice: partner punches "
            "with varied energy, and you answer light punches with Tan Sau "
            "and heavy committed ones with Jut Sau, training the judgment "
            "of which tool the pressure calls for."
        ),
        "key_points": [
            "Jut Sau is a sudden downward jerking shock onto the opponent's forearm that collapses a committed punch - Lap Sau's sharper, shorter cousin.",
            "The impulse is real: 24 newtons over 0.1 seconds changes a 3 kilogram arm's velocity by 0.8 meters per second downward.",
            "The motion is tiny - a few centimeters of elbow-driven snap plus a fractional stance sink - never a long pressing push.",
            "It feeds on the opponent's pressure: the harder they lean onto your bridge, the harder the jerk folds them.",
            "Students learn the judgment alongside the technique: light punches get Tan Sau, heavy committed ones get Jut Sau.",
        ],
        "requirements": [
            "Contact from above on the opponent's forearm with the hand's edge, timed to the punch's commitment.",
            "A short downward snap driven by the dropping elbow and a small stance sink, completed in about 0.1 seconds.",
            "A shock, not a press - the hand recovers as the opponent's arm falls.",
            "An immediate punch over the collapsed arm down the centerline, one beat.",
            "Reading the pressure: heavy forward energy calls for Jut Sau, light energy for Tan Sau.",
        ],
        "standards": [
            "Jut Sau is drilled against cooperative committed punches before any speed or resistance is added.",
            "The downward shock targets the forearm, never the elbow joint; joint safety is absolute.",
            "Instructors verify the jerk stays short - a long press is corrected back to a snap.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_DUMMY116],
        "sig_lens": (
            "The Signature read: Jut Sau is the Signature's thunderclap - a "
            "tenth of a second that the opponent's arm never recovers from. "
            "Where public instruction teaches a downward jerk, the Signature "
            "Combat Method teaches a covenant of shock: meet commitment "
            "with suddenness, let their own pressure dig their grave, and "
            "have the punch already traveling before their arm finishes falling."
        ),
    },
    {
        "key": "kwan_sau",
        "name": "Kwan Sau: The Rotating Hand",
        "group": "Hand Techniques",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Kwan Sau, the rotating hand, is the compounded technique that "
            "answers two problems at once: one hand performs Tan Sau while "
            "the other performs Bong Sau, and the pair rotates - Tan "
            "becoming Bong, Bong becoming Tan - rolling around the "
            "opponent's pressure like a wheel. It is the answer to the "
            "fighter who attacks high and low together, or who presses "
            "with changing angles that a single deflection cannot track. "
            "The rotation is continuous and fast: the hands turn through 90 "
            "degrees in about 0.15 seconds, an angular velocity of roughly "
            "10.47 radians per second, which puts the rolling hand at "
            "about 2.93 meters per second at a 0.28 meter radius - fast "
            "enough to stay ahead of combination punching. Kwan Sau appears "
            "in the first form's third section, where the Bong-to-Tan roll "
            "is first isolated, and it is the signature motion of advanced "
            "chi sao, where both partners' hands roll through Kwan Sau "
            "continuously while hunting for the opening to strike. Students "
            "find it awkward for months - the two hands want to do the same "
            "thing - and then one day the rotation becomes automatic, which "
            "is the moment their chi sao becomes dangerous."
        ),
        "how_it_works": (
            "Hold both hands forward: the lower hand in Tan Sau, palm up on "
            "the centerline, and the upper hand in Bong Sau, elbow high, "
            "forearm across. Now rotate: the Tan hand rises and rolls over "
            "into Bong while the Bong hand drops and rolls under into Tan - "
            "the hands circle around each other without ever leaving the "
            "centerline's corridor, like two pistons in a rotary engine. "
            "Have the partner feed alternating high and low straight "
            "punches: the upper hand's Bong catches the high punch and "
            "rolls it into Tan as the lower hand's Tan catches the low "
            "punch and rolls it into Bong, the rotation never stopping. "
            "Keep the elbows anchored - the rotation happens at the "
            "forearms, not by waving the elbows around - and keep the "
            "shoulders down. Drill it first in the air for the coordination, "
            "then in Luk Sao rolling where it occurs naturally, then "
            "against the partner's combinations. The breakthrough drill: "
            "partner attacks continuously while you may ONLY use Kwan Sau - "
            "no punching back - until the rotation holds under pressure."
        ),
        "key_points": [
            "Kwan Sau pairs Tan Sau and Bong Sau in one structure and rotates them continuously - Tan becoming Bong, Bong becoming Tan - to track changing attack angles.",
            "The rotation runs about 90 degrees in 0.15 seconds (10.47 radians per second), putting the rolling hand near 2.93 meters per second - fast enough to stay ahead of combinations.",
            "It answers high-low simultaneous attacks that a single deflection cannot cover.",
            "The rotation happens at the forearms with anchored elbows; waving the elbows destroys the structure.",
            "It is the signature motion of advanced chi sao, drilled until the two hands rotate automatically and independently.",
        ],
        "requirements": [
            "One hand in Tan Sau and the other in Bong Sau, both on the centerline's corridor.",
            "Continuous rotation exchanging the two shapes without pausing or leaving the line.",
            "Anchored elbows and down shoulders - the forearms rotate, the frame does not wave.",
            "Tracking of high and low attacks simultaneously, each met by the appropriate rolling hand.",
            "Automatic, thought-free rotation under combination pressure.",
        ],
        "standards": [
            "Kwan Sau is learned in the air and in Luk Sao rolling before it faces combination attacks.",
            "The defense-only pressure drill (no punching back) proves the rotation before offense is added.",
            "Instructors watch for elbow drift - the classic fault that collapses the wheel.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_WINGTSUN],
        "sig_lens": (
            "The Signature read: Kwan Sau is the Signature's wheel - two "
            "hands keeping one covenant as they turn through each other's "
            "shapes. Where public instruction teaches a rotating double "
            "deflection, the Signature Combat Method teaches perpetual "
            "motion with a still center: the hands may turn at ten radians "
            "a second, but the elbows keep their oath to the line, and no "
            "attack finds the axis undefended."
        ),
    },
    {
        "key": "gaun_sau",
        "name": "Gaun Sau: The Splitting Hand",
        "group": "Hand Techniques",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Gaun Sau, the splitting hand - sometimes translated as the "
            "cultivating or plowing hand in its low form - is the wedge "
            "that splits the opponent's attack in two. Both hands chop "
            "downward and outward simultaneously, palms facing down and out, "
            "driving between the opponent's arms like an axe splitting a "
            "log, forcing their guard apart and opening the centerline. "
            "The wedge geometry multiplies the force: an 80 newton downward "
            "drive split at 45 degrees to each side delivers about 56.6 "
            "newtons of lateral force per side - 113.1 newtons of total "
            "spreading force - from a single downward motion, which is why "
            "a committed Gaun Sau bursts through guards that would stop a "
            "straight punch. It is the answer to the opponent who shells "
            "up, crosses their arms, or clinches: instead of going around "
            "the guard, Gaun Sau goes through it by splitting it. The "
            "technique appears in the second form's low sections and "
            "throughout the dummy form, where the dummy's arms are split "
            "again and again. Students learn it after the single-hand "
            "deflections because it demands what they teach: both hands "
            "firing as one coordinated wedge while the stance drops its "
            "weight behind them."
        ),
        "how_it_works": (
            "Have the partner hold both forearms crossed in front of their "
            "chest in a tight shell. Place your hands together above their "
            "guard, then chop both hands down and outward simultaneously, "
            "palms down, elbows driving down the centerline - the hands "
            "split apart as they descend, wedging between their forearms "
            "and forcing them apart. The power comes from a small sink of "
            "the stance at the moment of the split: drop your weight an "
            "inch and let it drive the wedge. The instant their guard "
            "splits, punch straight through the middle with either hand - "
            "Gaun, punch, one motion. The most common fault is splitting "
            "with the arms while the body stays tall, which makes a weak "
            "pushing motion; the stance must drop behind the hands. Drill "
            "it against the wooden dummy's crossed arms first, feeling the "
            "wedge find the seam, then against a partner's shell guard, "
            "then as the entry in sparring against opponents who cover up. "
            "Keep your own elbows in during the split - wide elbows open "
            "your ribs to the counter."
        ),
        "key_points": [
            "Gaun Sau is a simultaneous two-hand downward-outward wedge that splits the opponent's guard apart like an axe splitting a log.",
            "The wedge multiplies force: an 80 newton drive at 45 degrees per side yields about 56.6 newtons of lateral force each - 113.1 newtons of spreading force.",
            "It answers the shell guard, crossed arms, and clinch by going through the guard rather than around it.",
            "Power comes from the stance dropping behind the hands; arm-only splitting is a weak push.",
            "The split is instantly followed by a punch through the opened middle - wedge and strike are one entry.",
        ],
        "requirements": [
            "Both hands chopping down and outward simultaneously, palms down, splitting from a single point.",
            "A small stance sink timed to the split, dropping body weight behind the wedge.",
            "Elbows driving down the centerline and staying in - no wide flaring that opens the ribs.",
            "Contact that finds the seam between the opponent's arms and forces them apart.",
            "An immediate punch through the opened centerline as the split lands.",
        ],
        "standards": [
            "Gaun Sau is drilled first on the wooden dummy's arms, then against cooperative shell guards.",
            "The stance sink is verified before power is added - tall splitting is corrected immediately.",
            "Partner drills use controlled force; the wedge targets the arms, never the head or neck.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_DUMMY116],
        "sig_lens": (
            "The Signature read: Gaun Sau is the Signature's axe - one "
            "downward covenant that the guard cannot keep closed. Where "
            "public instruction teaches a splitting wedge, the Signature "
            "Combat Method teaches the arithmetic of the seam: a single "
            "drive, honestly angled, becomes twice the force, and the "
            "punch that follows walks through a door the wedge opened."
        ),
    },
    {
        "key": "huen_sau",
        "name": "Huen Sau: The Circling Hand",
        "group": "Hand Techniques",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Huen Sau, the circling hand, is Wing Chun's answer to the grab: "
            "when the opponent seizes your wrist, your hand traces a small, "
            "fast circle that rolls their grip off and frees the hand to "
            "strike. The circle is tight - about 0.15 meters in radius, a "
            "circumference of roughly 0.94 meters - and quick: at a hand "
            "speed of 2 meters per second one full circle takes about 0.471 "
            "seconds, and the standard drill chains four circles in about "
            "1.885 seconds, which is why a grab that feels secure simply "
            "evaporates. The mechanics exploit the hand's anatomy: the "
            "circle rolls the opponent's grip toward the thumb - the "
            "weakest point of any grip - and the rotation tightens your "
            "own wrist structure as it turns. Huen Sau appears in all three "
            "empty-hand forms and constantly in chi sao, where partners "
            "seize each other's wrists specifically to invite the circle. "
            "Beyond escapes, the circling motion is the basis of several "
            "dummy techniques and the wrist conditioning that makes the "
            "whole hand system work. Students drill it thousands of times "
            "because the circle must fire before the thinking starts - a "
            "grab answered late is a grab that has already become a pull."
        ),
        "how_it_works": (
            "Have the partner grab your lead wrist firmly with one hand. "
            "Without pulling back against the grip - pulling feeds it - "
            "circle your hand in a tight loop: drop the elbow slightly, "
            "roll the wrist, and trace the circle so your hand spirals "
            "toward their thumb, the weak point of the grip. The circle's "
            "rotation peels their fingers open; the instant the grip "
            "breaks, the circling hand continues into a punch or a Pak Sau - "
            "escape and counter are one motion. Keep the circle small and "
            "fast: a big slow loop gives them time to re-grip, and pulling "
            "straight back just tests their grip strength against yours. "
            "Drill both directions, both hands, then have the partner grab "
            "with either hand at random so the circle fires on recognition "
            "rather than anticipation. Advance the drill: partner grabs and "
            "immediately pulls, and your circle must break the grip while "
            "their pull is still developing - this is the timing that "
            "matters, because real grabs always come with a yank."
        ),
        "key_points": [
            "Huen Sau answers any wrist grab with a small fast circle that rolls the grip toward the thumb - the grip's weakest point - and frees the hand.",
            "The circle is tight and quick: 0.15 meter radius, 0.94 meter circumference, about 0.471 seconds per circle at 2 meters per second.",
            "Never pull straight back against a grab; pulling feeds the grip while circling defeats it.",
            "Escape and counter are one motion: the freed hand continues directly into a punch or Pak Sau.",
            "The circle must fire on recognition, not anticipation - drilled against random grabs until it precedes thought.",
        ],
        "requirements": [
            "A tight circle of about 0.15 meter radius, spiraling toward the opponent's thumb.",
            "No backward pulling - the hand circles while the elbow drops slightly.",
            "Speed over strength: the circle completes before the grab can become a pull.",
            "An immediate continuation into punch or Pak Sau as the grip breaks.",
            "Both hands, both circle directions, against random unannounced grabs.",
        ],
        "standards": [
            "Grab drills begin with announced, cooperative grabs and progress to random grabs with a pull.",
            "Partners grip the wrist firmly but never torque the joint; wrist safety governs the drill speed.",
            "Instructors verify the circle stays small - big loops are corrected back to tight spirals.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_WINGTSUN],
        "sig_lens": (
            "The Signature read: Huen Sau is the Signature's untying - no "
            "knot the opponent ties survives the circle. Where public "
            "instruction teaches a wrist escape, the Signature Combat "
            "Method teaches a covenant of motion: never fight the grip's "
            "strength, only its geometry, and let the freed hand keep the "
            "appointment the circle already made with the centerline."
        ),
    },
    {
        "key": "gan_sau",
        "name": "Gan Sau: The Low Plowing Hand",
        "group": "Hand Techniques",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Gan Sau, the low plowing hand - the name carries the image of "
            "a plow turning the earth - is the low-line deflection that "
            "meets kicks, low punches, and grabbing hands aimed at the "
            "legs and lower body. The hand chops downward and outward at a "
            "low angle, palm down, the arm forming a plowshare that "
            "redirects the incoming limb down and away from the stance. It "
            "is the low counterpart to Tan Sau's high line: where Tan "
            "disperses punches at chest height, Gan plows everything below "
            "the waist off the line. The deflection math is unforgiving to "
            "the kicker: a 12 kilogram leg traveling at 3 meters per second "
            "carries 36 kilogram-meters per second of momentum, and "
            "deflecting it 45 degrees off its path shunts 25.5 of those "
            "units sideways while leaving only 25.5 still traveling at the "
            "defender - the kick's threat is more than quartered by a "
            "single plowing hand. Gan Sau appears in the second form's "
            "kicking sections, in the dummy form's low gates, and in chi "
            "gerk leg drills. Students learn it after the high-line hands "
            "because it demands the same elbow discipline pointed downward: "
            "the most common fault is chopping with a straight arm, which "
            "abandons all structure."
        ),
        "how_it_works": (
            "Have the partner throw a slow low front kick at your lead leg. "
            "As it arrives, chop your lead hand down and outward across the "
            "kick's path, palm down, arm angled like a plowshare - contact "
            "their shin with the outer edge of your forearm and redirect "
            "the kick down and past your leg, not into it. The elbow stays "
            "bent and anchored toward the centerline; a straight-arm chop "
            "has no structure and the kick will go through it. Sink the "
            "stance slightly into the deflection to add body weight behind "
            "the plow. The instant the kick is redirected, counter: step in "
            "with a punch while their kicking leg is still recovering - Gan, "
            "punch, one beat. Drill it first against slow low kicks, then "
            "against low punches and grabbing hands, then inside chi gerk "
            "where the hands and legs defend together. Always protect the "
            "groin line with the motion: the plow's angle must carry the "
            "attack away from the body, never across it."
        ),
        "key_points": [
            "Gan Sau is the low-line plow: a downward-outward chop that redirects kicks, low punches, and leg grabs away from the stance.",
            "The deflection math guts the kick: 36 kilogram-meters per second of leg momentum deflected 45 degrees leaves only 25.5 still on target.",
            "The elbow stays bent and anchored toward the centerline - a straight-arm chop has no structure and the kick goes through it.",
            "The stance sinks slightly into the deflection, adding body weight behind the plow.",
            "Counter immediately: Gan Sau and the punch are one beat, striking while the kicking leg is still recovering.",
        ],
        "requirements": [
            "A downward-outward chop, palm down, angled like a plowshare across the low attack's path.",
            "A bent elbow anchored toward the centerline throughout the deflection.",
            "Contact with the outer forearm that redirects the limb down and away, never across the body.",
            "A small stance sink timed to the plow, adding weight behind it.",
            "An immediate punch counter down the centerline as the low attack is cleared.",
        ],
        "standards": [
            "Gan Sau is drilled first against slow, controlled low kicks with shin guards worn by both partners.",
            "The deflection targets the shin and forearm, never the knee joint; joint targeting is forbidden in drills.",
            "Instructors correct the straight-arm chop on sight - structure first, then speed.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_DUMMY116],
        "sig_lens": (
            "The Signature read: Gan Sau is the Signature's plow - what "
            "comes low is turned into the earth it came from. Where public "
            "instruction teaches a low deflection, the Signature Combat "
            "Method teaches a covenant with gravity: the elbow keeps its "
            "bend, the stance lends its weight, and the kick that sought "
            "the leg finds only the ground."
        ),
    },
    {
        "key": "biu_sau",
        "name": "Biu Sau: The Thrusting Hand",
        "group": "Hand Techniques",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Biu Sau, the thrusting or darting hand, is the spear of the "
            "Wing Chun hand system: the fingers thrust forward together "
            "like a dart, striking with the fingertips along the "
            "centerline. In training it is practiced as a precise, "
            "whipping thrust to the eyes and throat - the traditional "
            "targets - but its everyday value is as the longest, fastest "
            "hand in the system, a probing attack that outranges the punch "
            "and punishes anyone who leans in. The fingertip mechanics are "
            "striking: a 50 newton thrust delivered through four fingertips "
            "over about 4 square centimeters of contact - 0.0004 square "
            "meters - produces roughly 125,000 pascals, 125 kilopascals of "
            "pressure, which is why even a controlled thrust demands "
            "respect and why the technique is drilled against pads rather "
            "than partners. Biu Sau appears in the first form's later "
            "sections, dominates the third form Biu Jee, and is the thrust "
            "half of the Biu Ma footwork's name. Students learn it after "
            "the punch because it requires what the punch teaches - "
            "relaxation, straight-line delivery, instant retraction - with "
            "the added discipline of finger conditioning and absolute "
            "accuracy, since a thrust that misses the line is a gift of an "
            "extended arm."
        ),
        "how_it_works": (
            "From the guard, thrust the lead hand forward with the fingers "
            "together and extended, palm facing down or sideways, the arm "
            "whipping out along the centerline and snapping back the "
            "instant it reaches full extension - the motion is a dart, not "
            "a push. Keep the wrist straight and the fingers rigid at the "
            "moment of contact but relaxed in flight; tension during the "
            "flight slows the thrust and telegraphs it. Aim at a small "
            "target - a coin taped to a wall pad - because Biu Sau lives or "
            "dies on accuracy: drill until the thrust lands on the coin "
            "nine times out of ten. Condition the fingers gradually: begin "
            "with thrusts into a bean bag, progress to a sand bag over "
            "months, never striking hard surfaces, and stop at any sharp "
            "finger pain. In application the thrust is a probe and a "
            "punish: dart it at the eyes to make the opponent blink and "
            "cover, then punch through the reaction - Biu, punch, one "
            "combination. Never thrust at a partner's face in drills; pads "
            "and wall targets only."
        ),
        "key_points": [
            "Biu Sau is the darting fingertip thrust along the centerline - the longest, fastest hand in the system, traditionally aimed at the eyes and throat.",
            "The pressure math commands respect: 50 newtons through 4 square centimeters is about 125 kilopascals, so the thrust is drilled on pads, never on partners.",
            "The motion is a whip - relaxed in flight, rigid at contact, snapping back instantly - never a push.",
            "Accuracy is the technique: training aims at coin-sized targets until the thrust lands true nearly every time.",
            "In combination it is a probe and a punish - dart at the eyes to draw the flinch, then punch through the reaction.",
        ],
        "requirements": [
            "Fingers together and extended, thrust straight along the centerline with a whipping arm.",
            "Relaxation in flight and rigidity only at the instant of contact, with instant retraction.",
            "A small, precise target - accuracy drilled to near-perfection on pads and wall targets.",
            "Gradual finger conditioning on soft bags over months, stopping at any sharp pain.",
            "Never thrust at a partner's face in drills - pads and targets only, absolutely.",
        ],
        "standards": [
            "Biu Sau is drilled exclusively against pads, bags, and wall targets; partner face-targeting is forbidden.",
            "Finger conditioning progresses over months from soft to firm bags; hard surfaces are never used.",
            "Instructors verify the whipping relaxation before any power is added - a tense thrust is a slow thrust.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_WINGTSUN],
        "sig_lens": (
            "The Signature read: Biu Sau is the Signature's dart - the "
            "longest word the hand can speak, written on the centerline. "
            "Where public instruction teaches a fingertip thrust, the "
            "Signature Combat Method teaches a covenant of precision: the "
            "hand travels relaxed, arrives rigid, and returns before the "
            "thought of it has finished - and it is never, ever loosed at "
            "a partner in play."
        ),
    },
    {
        "key": "chum_kiu",
        "name": "Chum Kiu: The Second Form",
        "group": "Forms",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Chum Kiu - 'seeking the bridge' - is the second empty-hand "
            "form and the moment Wing Chun starts to move. Where Siu Nim "
            "Tau trains the fighter standing still, Chum Kiu adds turning "
            "the stance, stepping, and kicking: the practitioner learns to "
            "seek the bridge - to make arm contact with the opponent - and "
            "to cross the gap between fighters. The form teaches the "
            "turning punch, the step-and-punch, the Bong Sau with turning, "
            "the three kicks, and the coordinated whole-body power that "
            "comes from the stance rotating behind the hands. The bridging "
            "numbers show the shift: each turning step covers about 0.75 "
            "meters, so three turning advances cross 2.25 meters in roughly "
            "1.2 seconds - a bridging speed of about 1.875 meters per "
            "second, fast enough to collapse the gap before a retreating "
            "opponent can reset. Chum Kiu is also the form of the second "
            "line of defense: when the first line - the hands - is "
            "beaten, the turn and the step carry the fighter to a new "
            "angle instead of a desperate block. Students typically spend "
            "a year or more on the first form before Chum Kiu is taught, "
            "because every movement in the second form assumes the first "
            "form's structure is already automatic."
        ),
        "how_it_works": (
            "Learn Chum Kiu section by section from a qualified instructor, "
            "practicing each new turning or stepping movement in isolation "
            "before linking it into the sequence. The key checkpoints: the "
            "stance must not narrow or rise during turns - mark the floor "
            "and land on the marks; the hands must stay on the centerline "
            "while the body turns beneath them; the kicks must chamber and "
            "fire without the stance wobbling. Practice the form at three "
            "speeds: slow for structure, natural for flow, and fast for "
            "power, but never let the fast pass degrade the shapes the slow "
            "pass built. Drill the applications with a partner: have them "
            "hold a pad at successive angles while you turn and punch, "
            "step and punch, turn with Bong Sau - the form's movements must "
            "each have a living partner application, or they are just "
            "dance. Common faults: turning the shoulders without the "
            "stance, stepping with the weight already committed forward, "
            "and rushing the kicks. Correct them in the slow pass, where "
            "there is nowhere to hide."
        ),
        "key_points": [
            "Chum Kiu ('seeking the bridge') is the second form: it adds stance turning, stepping, and kicking to the first form's stationary alphabet.",
            "The form teaches bridging the gap - three turning advances cross 2.25 meters in about 1.2 seconds, a closing speed near 1.875 meters per second.",
            "It introduces the turning punch, step-and-punch, turning Bong Sau, and the three kicks, all powered by the rotating stance.",
            "It is the second line of defense: when the hands are beaten, the turn and step carry the fighter to a new angle.",
            "Every movement assumes the first form's structure is automatic - the second form is earned, typically after a year or more.",
        ],
        "requirements": [
            "A stance that holds its width and depth through every turn and step, verified against floor marks.",
            "Hands that stay on the centerline while the body turns beneath them.",
            "Section-by-section learning from a qualified instructor, each movement isolated before linking.",
            "Three practice speeds - slow for structure, natural for flow, fast for power - with the fast never degrading the slow.",
            "A living partner application for every movement; nothing in the form may be mere dance.",
        ],
        "standards": [
            "Chum Kiu is taught only after the first form's structure is automatic, typically a year or more in.",
            "The slow pass is the court of correction - faults are fixed there before speed is permitted.",
            "Kicking sections are drilled with the stance's stability as the pass-fail criterion.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_WINGTSUN, CIT_YIMM],
        "sig_lens": (
            "The Signature read: the second form is the Signature's first "
            "journey - the stance that learned stillness now learns to "
            "travel without forgetting it. Where public instruction teaches "
            "turning and stepping, the Signature Combat Method teaches a "
            "covenant of motion: the bridge is sought, the gap is crossed "
            "at nearly two meters a second, and the centerline arrives "
            "before the opponent has finished leaving."
        ),
    },
    {
        "key": "kicks",
        "name": "Wing Chun Kicks: Front and Side Kicks",
        "group": "Footwork",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Wing Chun's kicking is economical and low: the front kick and "
            "the side kick, delivered at knee and shin height, chambered "
            "tightly and fired without shifting the weight first. The art "
            "deliberately avoids high kicks - a high kick abandons the "
            "stance, telegraphs for a full beat, and offers the leg to be "
            "caught - and instead treats the kick as a long punch: fast, "
            "direct, and instantly recoverable. The numbers justify the "
            "doctrine: a 12 kilogram leg extending at 6 meters per second "
            "carries 72 kilogram-meters per second of momentum and about "
            "216 joules of kinetic energy - more than five times the "
            "punch's energy - chambered and extended in roughly 0.18 "
            "seconds, with a reach of about 0.95 meters against the hand's "
            "0.70 meters, a 0.25 meter advantage that lets the kick strike "
            "from outside punching range. The supporting leg stays rooted "
            "in a bent-stance guard throughout, the hands never drop to "
            "'help' the kick, and the kicking leg returns along the same "
            "path it traveled. Students learn the kicks in Chum Kiu's "
            "kicking section and drill them on pads, on the dummy's leg, "
            "and in chi gerk leg sparring."
        ),
        "how_it_works": (
            "From the stance, chamber the knee tightly upward - the knee "
            "rises first, the foot follows - then snap the leg out along "
            "the centerline for the front kick, striking with the heel or "
            "the ball of the foot, or pivot the support foot and thrust "
            "sideways for the side kick, striking with the heel's edge. "
            "Keep the hands in guard throughout; the moment the hands drop, "
            "the kick has cost more than it gains. Strike low: the knee, "
            "the shin, the thigh - targets that stop movement rather than "
            "targets that impress spectators. Retract along the same path "
            "at the same speed and set the foot back down in stance without "
            "stamping or stumbling. Drill the chamber-to-extension slowly "
            "first - 0.18 seconds is the goal, not the starting point - "
            "then on a heavy pad for impact, then on the dummy's leg for "
            "angle, then in chi gerk against a partner's legs with shin "
            "guards. The pass-fail test: kick at full speed and have a "
            "partner check that your guard never moved and your stance "
            "never wobbled."
        ),
        "key_points": [
            "Wing Chun kicks low and economically: front and side kicks at knee and shin height, chambered tight, fired without a weight shift.",
            "The leg's numbers dwarf the punch: 12 kilograms at 6 meters per second gives 72 kilogram-meters per second and about 216 joules - five times the punch.",
            "Reach advantage is real: about 0.95 meters for the kick versus 0.70 for the hand, striking from outside punching range.",
            "High kicks are rejected by doctrine: they abandon the stance, telegraph, and offer the leg to be caught.",
            "The hands never drop during the kick and the leg retracts along its own path - the kick must cost nothing defensively.",
        ],
        "requirements": [
            "A tight chamber - knee rising first, foot following - with no preparatory weight shift.",
            "Low targets only: knee, shin, thigh - strikes that stop movement.",
            "Hands held in guard throughout the kick, never dropping to assist.",
            "Full-speed retraction along the same path, foot resetting into stance without stumbling.",
            "A rooted supporting leg in a bent-stance guard for the entire technique.",
        ],
        "standards": [
            "Kicks are learned in Chum Kiu's kicking section and drilled slowly before any speed or impact.",
            "Pad and dummy-leg work precedes partner leg drills; partner drills require shin guards.",
            "The guard-and-stance stability test is the gate to full-speed kicking.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_WINGTSUN],
        "sig_lens": (
            "The Signature read: the kick is the Signature's long punch - "
            "five times the energy, none of the vanity. Where public "
            "instruction teaches front and side kicks, the Signature Combat "
            "Method teaches a covenant of economy: strike low, chamber "
            "tight, keep the hands on the line, and let the leg return "
            "home before the opponent has priced what it cost them."
        ),
    },
    {
        "key": "dan_chi_sau",
        "name": "Dan Chi Sao: Single-Hand Sticking",
        "group": "Chi Sao",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Dan Chi Sao, single-hand sticking, is the doorway to Wing "
            "Chun's famous sensitivity training: two partners each extend "
            "one arm, maintain light forearm-to-forearm bridge contact, "
            "and cycle continuously through Tan Sau, Fook Sau, punch, Pak "
            "Sau, and back again. One partner's Tan becomes the other's "
            "Fook; the punch is answered by Pak; the cycle rolls without "
            "stopping, and through the rolling each student learns the "
            "three skills chi sao exists to teach: sensitivity (feeling "
            "pressure changes through the bridge), forward pressure "
            "(maintaining constant gentle intent toward the opponent's "
            "center), and automatic technique (the right hand shape "
            "appearing without decision). The drill's volume builds the "
            "skill: at a relaxed cycle of 2.0 seconds, one minute of "
            "continuous Dan Chi Sao runs 30 full cycles - 60 Tan Sau, 60 "
            "Fook Sau, 30 punches, 30 Pak Sau per hand - thousands of "
            "correct repetitions per month of regular practice. Dan Chi Sao "
            "is deliberately cooperative at first; the partners feed each "
            "other the cycle so both can polish the shapes. Competition "
            "comes later, in Gor Sao. Students typically begin Dan Chi Sao "
            "after the first form's hand techniques are stable, and many "
            "teachers consider a year of it the minimum before double-hand "
            "rolling."
        ),
        "how_it_works": (
            "Face your partner in stance, each extending the right arm to "
            "touch forearms - light contact, about the pressure of a "
            "handshake. Partner A holds Tan Sau while Partner B holds Fook "
            "Sau lying on top; on a silent count, A punches straight down "
            "the line while B answers with Pak Sau, then B's hand becomes "
            "Tan as A's becomes Fook, and the cycle continues: Tan, Fook, "
            "punch, Pak, Tan, Fook, punch, Pak. Keep the bridge contact "
            "unbroken and the pressure light and constant - if the contact "
            "goes heavy, both partners are pushing instead of listening. "
            "Start painfully slowly, checking each shape: Tan palm-up with "
            "elbow on the line, Fook palm-down controlling from above, the "
            "punch straight, the Pak short and crisp. When the shapes hold, "
            "let the cycle find its rhythm at about 2 seconds per round and "
            "run it for minutes, then switch arms. The advanced practice: "
            "one partner deliberately varies the pressure - pressing, "
            "yielding, speeding - and the other maintains the cycle "
            "without breaking shape, learning to feel rather than see."
        ),
        "key_points": [
            "Dan Chi Sao cycles two partners through Tan Sau, Fook Sau, punch, and Pak Sau with unbroken light bridge contact - the doorway to sensitivity training.",
            "The drill teaches three skills: feeling pressure through the bridge, maintaining forward pressure, and producing the right hand shape without deciding.",
            "Volume builds the skill: 2-second cycles give 30 rounds per minute - 60 Tan, 60 Fook, 30 punches, 30 Pak per hand, thousands of reps monthly.",
            "The drill is cooperative first: partners feed each other the cycle to polish shapes; competition waits for Gor Sao.",
            "Bridge pressure stays light and constant - heavy contact means both partners are pushing instead of listening.",
        ],
        "requirements": [
            "Unbroken forearm-to-forearm bridge contact at light, constant, handshake-like pressure.",
            "Correct cycling shapes: palm-up Tan with elbow on the line, palm-down controlling Fook, straight punch, short Pak.",
            "A slow start with shape checks, progressing to a steady 2-second rhythm for minutes at a time.",
            "Both arms trained equally, switching sides regularly.",
            "Forward pressure maintained through the whole cycle - never pulling back, never shoving.",
        ],
        "standards": [
            "Dan Chi Sao begins only after the first form's hand shapes are stable.",
            "Partners keep contact light and cooperative; muscling the cycle is corrected immediately.",
            "A qualified instructor checks the shapes and the pressure before the rhythm is allowed to quicken.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_WINGTSUN, CIT_YIMM],
        "sig_lens": (
            "The Signature read: single-hand sticking is the Signature's "
            "first conversation - one bridge, two listeners, and the "
            "shapes of Tan, Fook, punch, and Pak taking turns speaking. "
            "Where public instruction teaches a drill cycle, the Signature "
            "Combat Method teaches the covenant of the bridge: stay light, "
            "stay forward, stay in contact, and let the hands learn what "
            "the eyes can never be fast enough to see."
        ),
    },
    {
        "key": "luk_sao",
        "name": "Luk Sao: Double-Hand Rolling",
        "group": "Chi Sao",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Luk Sao - 'rolling hands,' also called Poon Sao - is "
            "double-hand sticking: both partners roll both arms "
            "continuously through Tan Sau, Fook Sau, and Bong Sau in a "
            "flowing cycle, maintaining two bridges of light contact while "
            "each hand takes turns controlling from above and dispersing "
            "from below. It is the platform on which all advanced chi sao "
            "is built: every attack in Gor Sao free sticking launches from "
            "the roll, and every defense returns to it. The rolling volume "
            "is what rewires the reflexes: at a relaxed 1.5 seconds per "
            "full roll, three minutes of continuous Luk Sao produces 120 "
            "rolls, and with three hand shapes cycling per roll that is 360 "
            "shape changes per hand - nearly three-quarters of a thousand "
            "sensitivity decisions in a single three-minute round. The "
            "roll teaches what no solo drill can: continuous forward "
            "pressure against a live, resisting, thinking arm; the feeling "
            "of an opponent's intention a fraction of a second before it "
            "becomes motion; and the discipline of never breaking contact "
            "to chase - the hands stay on the bridges and let the openings "
            "come to them. Students graduate to Luk Sao after Dan Chi Sao, "
            "and the roll itself becomes a lifelong practice."
        ),
        "how_it_works": (
            "Face your partner, both in stance, and cross forearms so each "
            "of your hands contacts one of theirs - right to right, left "
            "to left - with light, even pressure. Begin the roll: your "
            "right hand cycles Fook to Tan to Bong while your left cycles "
            "the complementary shapes, the hands rolling around each "
            "other's forearms in a continuous flowing loop, elbows staying "
            "low and on the centerline's corridor. Neither partner leads; "
            "the roll finds a shared rhythm at about 1.5 seconds per "
            "cycle, and both maintain gentle forward intent - pressing "
            "toward the partner's center without shoving. When the roll is "
            "smooth, add the first attacks: on a felt opening, one partner "
            "punches straight from the roll while the other answers with "
            "Pak or Tan and the roll resumes - attack and return, never "
            "chasing. Common faults: breaking contact to punch wide, "
            "pressing so hard the roll becomes a shoving match, and letting "
            "the elbows float up and out. Drill in three-minute rounds with "
            "a minute's rest, like sparring rounds, because that is what "
            "the roll is preparing you for."
        ),
        "key_points": [
            "Luk Sao rolls both partners' hands continuously through Tan, Fook, and Bong with two bridges of light contact - the platform all advanced chi sao is built on.",
            "The volume rewires reflexes: 1.5-second rolls give 120 rolls in three minutes, 360 shape changes per hand - hundreds of sensitivity decisions per round.",
            "It teaches continuous forward pressure against a live resisting arm and the feeling of intention just before it becomes motion.",
            "Every attack launches from the roll and every defense returns to it; the hands never break contact to chase.",
            "The discipline is staying on the bridges and letting openings come, rather than abandoning the roll to hunt.",
        ],
        "requirements": [
            "Two unbroken bridges of light, even contact with gentle forward intent - pressing toward center, never shoving.",
            "Continuous cycling through Tan, Fook, and Bong with elbows low in the centerline's corridor.",
            "A shared rhythm of about 1.5 seconds per roll, sustained for full three-minute rounds.",
            "Attacks that launch from the roll and defenses that return to it, with contact never broken to chase.",
            "Complementary coordination: each hand cycles opposite shapes so the pair stays balanced.",
        ],
        "standards": [
            "Luk Sao follows Dan Chi Sao; the single-hand cycle's shapes and pressure must be stable first.",
            "Rolling is cooperative until the shapes hold under rhythm, then attacks are introduced by agreement.",
            "Rounds are timed with rest intervals; exhausted rolling trains sloppy bridges and is stopped.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_WINGTSUN],
        "sig_lens": (
            "The Signature read: rolling hands is the Signature's endless "
            "river - two bridges that never break, carrying Tan, Fook, and "
            "Bong around each other in an unbroken covenant. Where public "
            "instruction teaches a drill, the Signature Combat Method "
            "teaches a listening post: stay on the bridges, keep the "
            "forward oath, and let the opponent's intention arrive at your "
            "hands before it has finished leaving their mind."
        ),
    },
    {
        "key": "lop_sao",
        "name": "Lop Sao Drills: Attack and Defense Cycles",
        "group": "Chi Sao",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The Lop Sao cycle is Wing Chun's core attack-and-defense "
            "drill: from the rolling bridge, one partner grabs the other's "
            "wrist (Lop), pulls it down and across (Lap Sau), and punches "
            "straight through; the defender answers with Pak Sau and "
            "punches back; the first partner answers that punch the same "
            "way - and the cycle rolls continuously, attack becoming "
            "defense becoming attack. It is the drill where chi sao's "
            "sensitivity becomes fighting timing: the pull must catch the "
            "punch as it commits, the Pak must clear the line in the same "
            "beat, and neither partner may break the rhythm to think. The "
            "cadence is demanding: the standard four-beat cycle (Lop, "
            "punch, Pak, punch) run at 120 beats per minute turns every "
            "2.0 seconds, so 50 continuous cycles take 100 seconds and "
            "deliver 100 punches per partner - a hundred interceptions "
            "practiced in under two minutes. Variations build the full "
            "fighter: the cycle run with stepping, with the defender "
            "allowed any answer (Tan, Bong, Jut, Gaun), with the attacker "
            "feinting the Lop, and finally with both partners free to break "
            "the cycle - which is the doorway to Gor Sao. Students drill "
            "the Lop Sao cycle for months because it is the closest "
            "cooperative drill to actual fighting."
        ),
        "how_it_works": (
            "Begin in Luk Sao rolling with your partner. On an agreed "
            "signal, Partner A hooks B's wrist, pulls it down and across "
            "in Lap Sau, and punches straight down the opened line; B "
            "slaps the punch aside with Pak Sau and punches back straight; "
            "A Pak Sau's that punch and punches again - and the cycle "
            "continues: Lop, punch, Pak, punch, Lop, punch, Pak, punch. "
            "Start at half speed with a spoken count - 'one, two, three, "
            "four' - until every pull catches cleanly and every Pak lands "
            "in the same beat as its punch. Then bring the cadence up to "
            "120 beats per minute and run 50-cycle sets, keeping the "
            "bridge contact light between beats. Add the variations in "
            "order: first stepping with the cycle, then freeing the "
            "defender's choice of answer, then allowing the attacker to "
            "feint. The safety rules never change: controlled contact, "
            "headgear when punches target head height, and an instant stop "
            "if either partner starts muscling through the technique "
            "instead of timing it."
        ),
        "key_points": [
            "The Lop Sao cycle chains Lop-pull, punch, Pak Sau, and counter-punch into a continuous attack-defense-attack loop - the closest cooperative drill to fighting.",
            "At 120 beats per minute the four-beat cycle turns every 2.0 seconds: 50 cycles in 100 seconds deliver 100 interceptions per partner.",
            "The pull must catch the punch as it commits and the Pak must land in the same beat - timing, not strength, runs the cycle.",
            "Ordered variations build the fighter: stepping, free choice of defensive answer, feinted entries, then breaking the cycle into Gor Sao.",
            "It is where chi sao's sensitivity becomes fighting timing, drilled for months as the bridge to free practice.",
        ],
        "requirements": [
            "A clean Lop-pull that catches the punching wrist as it commits, dragging it down and across.",
            "A straight punch down the opened line in the same beat as the pull.",
            "A Pak Sau that clears each incoming punch in the same beat, with an instant counter-punch.",
            "Unbroken cadence at 120 beats per minute for 50-cycle sets, with light bridge contact between beats.",
            "Progressive variations: stepping, free defensive choice, feints, then breaking into free rolling.",
        ],
        "standards": [
            "The cycle is learned at half speed with a spoken count; full cadence is earned by clean timing.",
            "Contact stays controlled throughout; headgear is required when punches target head height.",
            "Muscling through the technique instead of timing it stops the drill for correction.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_DUMMY116],
        "sig_lens": (
            "The Signature read: the Lop Sao cycle is the Signature's "
            "sparring heartbeat - pull, punch, slap, punch, a hundred "
            "interceptions in a hundred seconds. Where public instruction "
            "teaches a drill, the Signature Combat Method teaches a "
            "covenant of rhythm: catch the commitment, clear the line, "
            "answer in the same beat, and never let the thinking interrupt "
            "the hands' appointment with the centerline."
        ),
    },
    {
        "key": "dummy",
        "name": "Mook Yan Jong: The Wooden Dummy Form",
        "group": "Wooden Dummy",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The Mook Yan Jong, the wooden dummy - 'wooden man post' - is "
            "Wing Chun's iron training partner: a wooden trunk with two "
            "upper arms set at angles, one lower bent arm, and a leg, "
            "mounted on a frame that gives slightly under impact. The dummy "
            "form trains what no human partner can: striking full power "
            "into solid resistance, practicing angles and footwork around "
            "an unyielding opponent, and conditioning the arms and legs "
            "against hardwood. The traditional Ip Man dummy form is "
            "commonly counted as 108 movements across its sections - Yip "
            "Chun's book catalogs 116 distinct dummy techniques - and the "
            "training volume is honest work: at about 3 seconds per "
            "movement one full pass takes roughly 324 seconds, 5.4 minutes, "
            "so three focused passes run about 16.2 minutes of continuous "
            "angle stepping, Pak Sau, Lap Sau, Bong Sau, kicks, and elbows "
            "against resistance. The dummy teaches positioning above all: "
            "its arms punish every wrong angle, forcing the student to "
            "step to the blind side, to enter at the correct distance, and "
            "to keep the centerline while moving around a solid object. "
            "Students begin dummy training after the second form, and the "
            "dummy form is traditionally taught in sections over a year or "
            "more, because each section's lessons have to be earned in the "
            "arms before the next is given."
        ),
        "how_it_works": (
            "Learn the dummy form in sections from a qualified instructor, "
            "never the whole sequence at once. Begin each section slowly "
            "and without power, walking the footwork around the dummy and "
            "placing each hand technique on the wooden arms - Pak Sau on "
            "the upper arms, Lap Sau pulling the arm down, Bong Sau rolling "
            "under - checking that every technique lands at the correct "
            "angle and distance. Only when the footwork is automatic do you "
            "add power: strike the arms and trunk with committed Pak Sau, "
            "punches, and elbows, conditioning the forearms gradually - "
            "start with light contact and build over months, never striking "
            "through pain. Train the leg techniques against the dummy's "
            "leg: front kicks, side kicks, and sweeps, always from the "
            "correct flanking angle. Run full passes for conditioning - "
            "three passes, about 16 minutes - and isolated sections for "
            "technique, filming yourself to check that the centerline holds "
            "while circling. Pad the dummy's arms if your forearms bruise "
            "excessively; conditioning is gradual adaptation, not injury. "
            "The dummy never moves, so it never lies: if your angle is "
            "wrong, the wooden arm tells you immediately."
        ),
        "key_points": [
            "The Mook Yan Jong is the wooden dummy: trunk, two upper arms, a lower bent arm, and a leg on a live frame - the partner that lets you strike full power into solid resistance.",
            "The form runs about 108 movements (116 techniques cataloged in Yip Chun's book); at 3 seconds each, one pass takes 5.4 minutes and three passes about 16.2 minutes.",
            "The dummy's supreme lesson is positioning: its arms punish wrong angles, forcing correct distance, blind-side stepping, and centerline discipline.",
            "It conditions the arms and legs against hardwood gradually - light contact building over months, never through pain.",
            "The form is taught in sections over a year or more after the second form; each section's lessons are earned before the next is given.",
        ],
        "requirements": [
            "Section-by-section learning from a qualified instructor, footwork walked slowly before any power is added.",
            "Correct angles and distances on every technique - Pak, Lap, Bong, kicks, elbows - against the wooden arms.",
            "Gradual arm and leg conditioning over months, starting light and never training through pain.",
            "Full passes for conditioning (about three passes, 16 minutes) plus isolated sections for technique.",
            "A centerline that holds while circling the dummy, verified on video.",
        ],
        "standards": [
            "Dummy training begins after the second form; the empty-hand structure must be automatic first.",
            "Conditioning progresses gradually - bruising that does not resolve between sessions means the intensity is too high.",
            "Instructors verify angles before power: striking the dummy wrongly at full power injures the student, not the wood.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_DUMMY116, CIT_WINGTSUN],
        "sig_lens": (
            "The Signature read: the dummy is the Signature's iron partner - "
            "it never moves, never lies, and never forgives a wrong angle. "
            "Where public instruction teaches 108 movements, the Signature "
            "Combat Method teaches a covenant of honesty: the wooden arms "
            "report every fault instantly, and the student who listens for "
            "a year earns what no compliant partner can give - technique "
            "that has been argued with and won."
        ),
    },
    {
        "key": "dummy_footwork",
        "name": "Biu Ma: Dummy Footwork and Angles",
        "group": "Wooden Dummy",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Biu Ma, the darting step, is the footwork that makes the "
            "wooden dummy form work: a sharp 45 degree angled step that "
            "carries the fighter to the dummy's blind side - outside the "
            "wooden arms' reach - while the hands strike from the new "
            "angle. It is the physical expression of Wing Chun's angling "
            "doctrine: never meet force head-on when a step can put you "
            "where the force is not. The geometry is tight and practical: "
            "a Biu Ma step covers about 0.4 meters at 45 degrees, and "
            "flanking a quarter-circle of 0.6 meter radius around the "
            "dummy - an arc of about 0.943 meters - takes 3 such steps, "
            "each one re-facing the centerline on the target while the "
            "body travels around it. The step is always paired with hand "
            "technique: step with Pak Sau, step with the punch, step with "
            "the kick - the feet deliver the hands to the angle where they "
            "work. Students drill Biu Ma around the dummy until the "
            "flanking becomes instinctive, then discover the same steps "
            "working against human partners: the dummy's blind side and "
            "the human's blind side are found the same way. The discipline "
            "is that the stance never narrows during the dart - a narrow "
            "stance at the new angle is a fallen fighter waiting to happen."
        ),
        "how_it_works": (
            "Stand before the dummy in stance. Dart the lead foot 45 "
            "degrees to the outside at about 0.4 meters, let the rear foot "
            "follow to restore the stance, and strike with Pak Sau or the "
            "punch as the step lands - the hand and the foot arrive "
            "together, the strike powered by the step's momentum. Circle "
            "the dummy in quarter arcs: three Biu Ma steps carry you 90 "
            "degrees around, and at each stop your centerline must face "
            "the dummy's center while your body stands at its flank. Have "
            "a partner check your stance width at every stop - mark the "
            "floor and land on the marks - because the step's speed "
            "tempts the feet to come together. Drill the step-hand pairs: "
            "Biu Ma with Pak Sau, with Lap Sau and punch, with the front "
            "kick, each pair landing as one beat. Then take it to a human "
            "partner: as they punch, Biu Ma to their outside and answer "
            "with the punch - the same blind-side geometry the dummy "
            "taught. Speed comes last; a fast narrow step is just a fast "
            "way to fall."
        ),
        "key_points": [
            "Biu Ma is the 45 degree darting step that carries the fighter to the blind side - outside the arms' reach - while the hands strike from the new angle.",
            "The geometry is practical: 0.4 meter steps, three of them to flank a 90 degree arc of 0.943 meters around the dummy.",
            "It embodies the angling doctrine: never meet force head-on when a step puts you where the force is not.",
            "Every step pairs with a hand technique - Pak, Lap and punch, kick - arriving as one beat, the step powering the strike.",
            "The stance must never narrow during the dart; footwork drilled on floor marks keeps the width honest.",
        ],
        "requirements": [
            "A 45 degree darting step of about 0.4 meters, rear foot following to restore full stance width.",
            "Hand technique arriving with the step as one beat - the step delivers the strike.",
            "The centerline re-facing the target at every stop while the body flanks it.",
            "Stance width preserved through the dart, verified against floor marks.",
            "Application against human partners: darting to the outside of a punch and answering from the blind side.",
        ],
        "standards": [
            "Biu Ma is drilled around the dummy before it is used against human partners.",
            "Stance width is checked at every stop until the step holds its structure at speed.",
            "Partner angling drills use controlled contact; the blind-side punch is pulled to touch.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_DUMMY116],
        "sig_lens": (
            "The Signature read: Biu Ma is the Signature's sidestep of "
            "fate - the force is met not where it is but where it is not. "
            "Where public instruction teaches a 45 degree step, the "
            "Signature Combat Method teaches a covenant of angles: three "
            "darts to own the flank, the stance never narrowing, the hands "
            "arriving with the feet, and the opponent's strength left "
            "guarding an empty center."
        ),
    },
    {
        "key": "biu_jee",
        "name": "Biu Jee: The Third Form",
        "group": "Forms",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Biu Jee - 'darting' or 'thrusting fingers' - is the third and "
            "final empty-hand form, and it is Wing Chun's emergency "
            "manual: the techniques for when everything has gone wrong. "
            "Where Siu Nim Tau trains the ideal structure and Chum Kiu "
            "trains bridging the gap, Biu Jee trains recovery - the elbow "
            "strikes for when the arms are trapped, the darting fingers "
            "for when the line is lost, the long-range thrusts for when "
            "the opponent is out of punching reach, and the emergency "
            "footwork for when the stance is compromised. The form's "
            "energy is different: short, whipping, explosive releases of "
            "power, like the 180 degree elbow recovery that snaps through "
            "in about 0.2 seconds - an angular velocity near 15.71 radians "
            "per second, putting the fingertips at roughly 8.64 meters per "
            "second at a 0.55 meter radius. Biu Jee is traditionally taught "
            "only to advanced students, often after years of training, "
            "because its techniques assume the first two forms' structure "
            "is unshakable - emergency techniques used without foundation "
            "are just flailing. The form also contains the system's "
            "philosophy in miniature: Wing Chun does not plan to lose, but "
            "it plans for losing, and the plan is to recover the centerline "
            "by any means and immediately resume the attack."
        ),
        "how_it_works": (
            "Learn Biu Jee only when your teacher judges the first two "
            "forms solid - the form's whipping energy will destroy a weak "
            "stance rather than build it. Practice each emergency "
            "technique in isolation first: the elbow recoveries snapped "
            "from trapped positions, the darting finger thrusts at wall "
            "targets, the long-range stepping thrusts, each drilled slowly "
            "until the structure holds, then at the form's explosive speed. "
            "The key checkpoint is recovery: after every whipping motion, "
            "the body must land back in stance with the guard on the "
            "centerline - Biu Jee techniques that leave you off-balance are "
            "failed techniques. Drill the applications as scenarios: "
            "partner traps your arms against your body and you elbow your "
            "way out; partner grabs from behind and the form's turn-and-"
            "thrust answers; partner retreats out of range and the darting "
            "step closes it. Train the finger thrusts on pads only, with "
            "the same conditioning discipline as Biu Sau. The form is "
            "short but intense - practice it after the body is warm, never "
            "cold, because the explosive releases punish cold tendons."
        ),
        "key_points": [
            "Biu Jee ('darting fingers') is the third form: the emergency manual for when structure is lost - trapped arms, lost line, out-of-range opponents, compromised stance.",
            "Its energy is short and whipping: a 180 degree elbow recovery snaps through in about 0.2 seconds, near 15.71 radians per second, fingertips near 8.64 meters per second.",
            "It is taught only to advanced students after years, because emergency techniques without foundation are just flailing.",
            "Every technique must end in recovered stance with the guard on the line - a Biu Jee motion that leaves you off-balance is a failed technique.",
            "The form's philosophy: Wing Chun does not plan to lose, but it plans for losing - recover the centerline by any means and resume the attack.",
        ],
        "requirements": [
            "Solid first and second forms as judged by a qualified teacher before Biu Jee is taught.",
            "Isolated drilling of each emergency technique - elbow recoveries, darting thrusts, long-range steps - slowly before explosively.",
            "Recovery to stance with the guard on the centerline after every whipping motion.",
            "Scenario drilling: trapped arms, grabs from behind, out-of-range opponents.",
            "A warmed-up body before practice; the explosive releases are never trained cold.",
        ],
        "standards": [
            "Biu Jee is reserved for advanced students; premature teaching is a recognized fault in traditional schools.",
            "Finger thrusts are drilled on pads only, with progressive conditioning and no partner face-targeting.",
            "Instructors verify the recovery-to-stance after every technique before speed is permitted.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_WINGTSUN],
        "sig_lens": (
            "The Signature read: the third form is the Signature's "
            "contingency - the covenant kept even when everything else is "
            "broken. Where public instruction teaches emergency "
            "techniques, the Signature Combat Method teaches a promise to "
            "the centerline: lose it if you must, but recover it by any "
            "means, at fifteen radians a second if need be, and be already "
            "attacking when you arrive."
        ),
    },
    {
        "key": "chi_gerk",
        "name": "Chi Gerk: Sticky Legs",
        "group": "Chi Sao",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Chi Gerk, sticky legs, is chi sao for the lower body: two "
            "partners maintain light leg-to-leg bridge contact - shin to "
            "shin, foot to foot - and practice sensing, deflecting, "
            "sweeping, and countering with the legs while the hands guard "
            "or work independently. It trains the sensitivity the hands "
            "learned in chi sao, but in the legs, where most fighters are "
            "blind: the ability to feel a kick chambering through a few "
            "newtons of pressure change, to deflect it with a small leg "
            "motion, and to answer with sweeps and counters. The leg "
            "mechanics are heavy: a sweeping leg of about 12 kilograms "
            "traveling at 2.5 meters per second carries 30 "
            "kilogram-meters per second of momentum, and stopping it in "
            "0.1 seconds of contact demands an average force near 300 "
            "newtons - which is why chi gerk emphasizes deflection over "
            "blocking, angling the sweep away rather than meeting it "
            "dead-on. Sensitivity is the real curriculum: partners learn to "
            "detect pressure changes as small as 5 newtons through the "
            "leg bridge, the lower-body equivalent of the hand's listening "
            "skill. Chi gerk is traditionally taught late, after the "
            "hands' chi sao is mature, because leg sensitivity without hand "
            "control leaves the upper body undefended."
        ),
        "how_it_works": (
            "Face your partner in stance with lead legs touching lightly, "
            "shin to shin. Maintain the leg bridge with gentle forward "
            "pressure - the same listening intent as the hand bridges - "
            "while both partners' hands hold guard. Begin the basic cycle: "
            "one partner sweeps slowly at the other's lead leg, the other "
            "lifts and angles the leg to deflect the sweep past, then "
            "answers with a slow sweep of their own. Keep every motion "
            "slow and controlled at first; the legs are heavy and clumsy "
            "compared to the hands, and fast leg sparring without control "
            "injures knees. As sensitivity develops, quicken the exchanges "
            "and add the hand techniques: sweep low while Pak Sau clears "
            "high, deflect the kick with Gan Sau while the leg counters. "
            "Wear shin guards for all partner leg contact, and agree the "
            "targets in advance - knees are never targeted in drills. The "
            "advanced practice is free chi gerk: both partners move freely, "
            "legs and hands working, each trying to sweep or unbalance the "
            "other while staying rooted - the closest Wing Chun comes to "
            "wrestling, and the drill that completes the fighter's "
            "sensitivity from head to toe."
        ),
        "key_points": [
            "Chi Gerk is sticky legs: light leg-to-leg bridge contact training the lower body's sensitivity, deflection, sweeps, and counters.",
            "Leg mechanics are heavy - a 12 kilogram sweep at 2.5 meters per second needs about 300 newtons to stop in 0.1 seconds - so deflection beats blocking.",
            "Sensitivity is the curriculum: detecting pressure changes as small as 5 newtons through the leg bridge, the lower-body equivalent of hand listening.",
            "It is taught late, after hand chi sao matures, because leg sensitivity without hand control leaves the upper body open.",
            "Free chi gerk - both partners moving freely, sweeping and unbalancing - completes the fighter's sensitivity from head to toe.",
        ],
        "requirements": [
            "A light leg bridge - shin to shin - with gentle forward pressure and continuous listening intent.",
            "Slow, controlled sweeps and deflections first; speed only after control is proven.",
            "Hands holding guard throughout, integrating with the legs as sensitivity grows.",
            "Shin guards for all partner leg contact, with targets agreed in advance.",
            "An absolute ban on knee targeting in drills.",
        ],
        "standards": [
            "Chi gerk follows mature hand chi sao; the upper-body guard must be automatic first.",
            "All partner leg contact requires shin guards and pre-agreed targets.",
            "Knee joints are never targeted; any drill violating this stops immediately.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM],
        "sig_lens": (
            "The Signature read: sticky legs is the Signature's listening "
            "extended downward - the covenant of the bridge kept by the "
            "shins as faithfully as the forearms. Where public instruction "
            "teaches leg drills, the Signature Combat Method teaches "
            "wholeness: the fighter who can hear five newtons through a "
            "shin has no blind half, and the sweep that comes is already "
            "answered before it arrives."
        ),
    },
    {
        "key": "knives",
        "name": "Bart Cham Dao: The Eight-Cut Knives",
        "group": "Weapons",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The Bart Cham Dao, the eight-cut knives - a pair of short, "
            "broad butterfly swords - are Wing Chun's close-range weapons, "
            "traditionally taught only to the most advanced students. The "
            "'eight cuts' are eight fundamental slashing and stabbing "
            "motions that combine into the complete knife form, and their "
            "geometry is total: eight cuts spaced 45 degrees apart cover "
            "the full 360 degrees around the fighter, leaving no angle "
            "unaddressed. The knives extend the empty-hand system rather "
            "than replacing it: the footwork is the same, the centerline "
            "is the same, and the cuts are the hand techniques - Pak Sau, "
            "Tan Sau, Bong Sau - given edges. The reach math shows the "
            "weapon's domain: a 0.35 meter blade on a 0.65 meter arm gives "
            "about 1.0 meter of reach, commanding a circle of roughly 3.14 "
            "square meters around the fighter - close range, personal, "
            "decisive. Training uses wooden or blunt aluminum replicas; "
            "live blades are never used for partner drills. The knife form "
            "is short but dense, and its lessons feed directly back into "
            "the empty hands: students consistently report that their "
            "Bong Sau and their footwork improve after knife training, "
            "because the weapon punishes every lazy angle the empty hands "
            "had been getting away with."
        ),
        "how_it_works": (
            "Learn the eight cuts individually with wooden training knives "
            "before attempting the form: each cut - the downward chop, the "
            "rising slash, the horizontal cuts inside and out, the thrusts - "
            "is drilled slowly against the air, checking that the edge "
            "alignment, the wrist position, and the footwork match the "
            "empty-hand technique it extends. Link the cuts into the form "
            "only when each one is clean, practicing with the same stance "
            "discipline as the empty-hand forms - the knives do not excuse "
            "a narrow stance or a dropped guard. Drill the applications "
            "with a partner using wooden knives and protective gear: one "
            "attacks with a committed cut, the other answers with the "
            "form's deflection and counter, at slow speed with full "
            "protective equipment. Never train partner drills with live "
            "blades, and never practice the form's thrusts toward a "
            "partner. The advanced training is the knife form against the "
            "dummy's arms, which teaches the cuts' angles against "
            "resistance. Throughout, keep the empty-hand connection "
            "explicit: after each knife session, shadow the same motions "
            "empty-handed and feel how the weapon's demands have sharpened "
            "the hands."
        ),
        "key_points": [
            "The Bart Cham Dao are the eight-cut knives - paired butterfly swords, the close-range weapons, taught traditionally only to advanced students.",
            "Eight cuts at 45 degrees cover the full 360 degrees: no angle around the fighter is unaddressed.",
            "The knives extend the empty-hand system: same footwork, same centerline, the hand techniques given edges.",
            "Reach is about 1.0 meter (0.35 meter blade plus 0.65 meter arm), commanding roughly 3.14 square meters - close, personal, decisive.",
            "Knife training feeds back into the empty hands: the weapon punishes lazy angles the hands had been getting away with.",
        ],
        "requirements": [
            "The eight cuts learned individually with wooden training knives before the form is attempted.",
            "Edge alignment, wrist position, and footwork matching the empty-hand technique each cut extends.",
            "The full stance and guard discipline of the empty-hand forms - the weapons excuse nothing.",
            "Partner drills with wooden knives and full protective gear only; live blades never used with partners.",
            "Explicit empty-hand shadowing after knife sessions to transfer the weapon's lessons to the hands.",
        ],
        "standards": [
            "The knives are taught only to advanced students with mature empty-hand structure.",
            "All partner drills use wooden or blunt aluminum trainers with protective gear; live blades are for solo form only.",
            "Thrusts are never directed at a partner, even with trainers.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_WINGTSUN],
        "sig_lens": (
            "The Signature read: the eight-cut knives are the Signature's "
            "edged covenant - the hand techniques keeping their promises "
            "in steel. Where public instruction teaches a weapons form, "
            "the Signature Combat Method teaches completion: eight cuts, "
            "forty-five degrees apart, no angle unguarded - and the empty "
            "hands return from the blades sharper than they went, because "
            "the knives accept no lazy angle."
        ),
    },
    {
        "key": "pole",
        "name": "Luk Dim Boon Kwan: The Six-and-a-Half-Point Pole",
        "group": "Weapons",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The Luk Dim Boon Kwan, the six-and-a-half-point pole - a long "
            "wooden staff of about 2.6 meters - is Wing Chun's long weapon "
            "and its power developer. The form contains six and a half "
            "techniques: the thrust, the sweeping strikes, the defensive "
            "circles, and the 'half point' - a short, devastating upward "
            "jerk - and training it builds the whole-body power that "
            "feeds back into every punch. The lever math explains the "
            "pole's fearsome reputation: with the hands gripping about "
            "0.5 meters apart, a rear hand driving at 2 meters per second "
            "whips the tip at about 10.4 meters per second, and with an "
            "effective mass near 1.5 kilograms the tip strike carries "
            "roughly 81 joules - delivered at nearly three meters of "
            "reach, long before any hand technique can answer. The pole is "
            "traditionally taught alongside or after the knives to advanced "
            "students, and its training is famously demanding: the long "
            "form is practiced until the practitioner's forearms, grip, and "
            "stance can manage the staff's leverage without strain. The "
            "pole's deeper lesson is power generation - the coordinated "
            "snap of stance, waist, and arms that the pole magnifies is "
            "exactly the coordination behind the one-inch punch's "
            "reputation, which is why pole training visibly improves the "
            "empty-hand striking of everyone who completes it."
        ),
        "how_it_works": (
            "Begin with a rattan or waxwood pole of about 2.6 meters, "
            "learning the grip - hands about 0.5 meters apart, lead hand "
            "guiding, rear hand driving - and the basic thrust against the "
            "air, checking that the tip travels straight along the "
            "centerline and the stance stays rooted against the pole's "
            "leverage. Drill the six and a half techniques individually: "
            "the straight thrust, the low and high sweeps, the circling "
            "deflections, and the half-point upward jerk, each practiced "
            "slowly until the pole feels like an extension of the arms "
            "rather than a separate object. Link them into the form and "
            "practice it daily - the pole form is the system's strength "
            "training, and skipping days shows immediately in the tip's "
            "speed. Drill applications with a partner at safe distance "
            "using padded poles: one thrusts, the other deflects with the "
            "circling techniques, both wearing eye protection. Never spar "
            "with hardwood poles. After each pole session, practice the "
            "empty-hand punches and feel for the transfer: the stance-"
            "waist-arm snap the pole demanded is now available to the "
            "fist, which is the whole point of the weapon."
        ),
        "key_points": [
            "The Luk Dim Boon Kwan is the six-and-a-half-point pole: a 2.6 meter staff, the long weapon and the system's power developer, taught to advanced students.",
            "Lever math makes it fearsome: a 2 meter per second rear hand with 0.5 meter grip spacing whips the tip to about 10.4 meters per second - roughly 81 joules at nearly three meters of reach.",
            "The form's six and a half techniques - thrusts, sweeps, circling deflections, the half-point upward jerk - are drilled until the pole feels like an extension of the arms.",
            "Pole training is strength training: daily form practice builds the forearms, grip, and stance the leverage demands.",
            "The deeper lesson is power generation - the stance-waist-arm snap the pole magnifies transfers directly to the empty-hand punch.",
        ],
        "requirements": [
            "A pole of about 2.6 meters with a 0.5 meter grip spacing, lead hand guiding and rear hand driving.",
            "The six and a half techniques drilled individually until the pole moves as an arm extension.",
            "Daily form practice as strength training, with the tip's speed as the progress measure.",
            "Partner applications with padded poles and eye protection only; hardwood sparring forbidden.",
            "Explicit transfer practice: empty-hand punching after pole sessions to carry the power generation across.",
        ],
        "standards": [
            "The pole is taught to advanced students; the leverage punishes weak structure, so the stance must be mature first.",
            "All partner pole work uses padded poles with eye protection; hardwood poles are for solo form only.",
            "Training volume builds gradually - the pole's leverage strains wrists and shoulders that are rushed.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_WINGTSUN],
        "sig_lens": (
            "The Signature read: the long pole is the Signature's lever of "
            "truth - two meters of wood that multiplies an honest stance "
            "into eighty joules. Where public instruction teaches a staff "
            "form, the Signature Combat Method teaches a covenant of "
            "power: the tip can only be fast if the root is true, and the "
            "snap the pole demands is the same snap the fist has owed the "
            "centerline all along."
        ),
    },
    {
        "key": "lin_siu_dai_da",
        "name": "Lin Siu Dai Da: Simultaneous Attack and Defense",
        "group": "Hand Techniques",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Lin Siu Dai Da - 'simultaneous defense and attack' - is the "
            "principle that separates Wing Chun from block-then-punch "
            "systems: the same motion that deflects the incoming attack "
            "delivers the counterattack, in a single beat. The Tan Sau "
            "that disperses the punch continues forward as the punch; the "
            "Pak Sau that clears the arm arrives with the punch behind it; "
            "the Lap Sau's pull and the punch are one action. The timing "
            "advantage is decisive: a simultaneous defense-attack completes "
            "in about 0.25 seconds - one beat - while a block-then-punch "
            "needs about 0.5 seconds - two beats - so the Wing Chun "
            "fighter lands twice as many actions in the same time, firing "
            "8 techniques in 2 seconds against the two-beat fighter's 4. "
            "The principle is not just speed but structure: because the "
            "defending hand never leaves the centerline to 'block' and "
            "return, the guard is never abandoned, and the opponent faces "
            "the demoralizing reality that every attack they launch is "
            "answered by a punch arriving with their own attack's timing. "
            "Students spend years approaching the ideal - most beginners "
            "still defend and then attack in two beats under pressure - "
            "and the Lop Sao cycle, chi sao, and sparring are the drills "
            "that compress the two beats into one."
        ),
        "how_it_works": (
            "Have the partner throw slow straight punches. Answer each "
            "with Tan Sau - and let the Tan hand keep traveling forward "
            "into the punch without any pause or chambering: the deflection "
            "and the strike are one continuous extension. The most common "
            "fault is the hesitation beat - deflect, pause, then punch - "
            "which is just block-then-punch with better PR; have the "
            "partner call out the pause until it disappears. Drill the "
            "principle through every technique: Pak Sau arriving with the "
            "punch behind it in the same beat, Lap Sau's pull landing with "
            "the punch, Bong Sau rolling into Tan into the punch without "
            "stopping. Then test it in the Lop Sao cycle at full cadence: "
            "the cycle only works at 120 beats per minute if every defense "
            "carries its own attack, which makes the drill a ruthless "
            "auditor of the principle. Finally, spar with the single "
            "constraint that you may not throw a punch that did not begin "
            "as a deflection - this forces the simultaneity under pressure "
            "and reveals exactly where the two-beat habit still hides."
        ),
        "key_points": [
            "Lin Siu Dai Da is simultaneous attack and defense: the deflecting motion continues into the counterattack in a single beat - the Tan Sau becomes the punch.",
            "The timing advantage is decisive: one beat (0.25 seconds) versus two beats (0.5 seconds) means 8 actions to the two-beat fighter's 4 in the same 2 seconds.",
            "The guard is never abandoned, because the defending hand never leaves the line to block and return - defense and offense are the same motion.",
            "The hesitation beat - deflect, pause, punch - is the classic fault; it is just block-then-punch wearing the principle's name.",
            "Years of Lop Sao, chi sao, and constrained sparring compress the two beats into one under pressure.",
        ],
        "requirements": [
            "Every deflection continuing forward into the counterattack with no pause or chambering.",
            "The defending hand staying on the centerline throughout - no blocking excursions that abandon the guard.",
            "The principle applied through all techniques: Tan, Pak, Lap, Bong each carrying its own punch.",
            "Elimination of the hesitation beat, verified by a partner calling out any pause.",
            "Pressure testing in the Lop Sao cycle and constrained sparring where every punch must begin as a deflection.",
        ],
        "standards": [
            "Simultaneity is drilled first in slow cooperative exchanges; the single beat is earned before speed.",
            "The Lop Sao cycle at full cadence is the auditor - it fails audibly when the two-beat habit appears.",
            "Constrained sparring uses full protective gear and controlled contact.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_WINGTSUN],
        "sig_lens": (
            "The Signature read: simultaneity is the Signature's single "
            "heartbeat - the hand that turns the attack aside is already "
            "the fist that answers it. Where public instruction teaches a "
            "principle, the Signature Combat Method teaches a covenant of "
            "the beat: one motion, a quarter of a second, defense and "
            "attack keeping the same appointment - and the guard, never "
            "once abandoned, keeps its oath to the line."
        ),
    },
    {
        "key": "lat_sao",
        "name": "Lat Sau Jik Chung: Free Sparring",
        "group": "Chi Sao",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Lat Sau Jik Chung - 'free hand, straight thrust' - is Wing "
            "Chun's free sparring: two practitioners in protective gear "
            "fighting with the system's techniques at controlled contact, "
            "testing whether the forms, the drills, and the chi sao survive "
            "contact with a resisting opponent. It is the examination the "
            "whole curriculum points toward: the centerline theory under "
            "pressure, the stance when someone is trying to move it, chain "
            "punching against a guard that hits back, deflections timed "
            "against punches that do not cooperate. A standard session "
            "runs three 2-minute rounds - 360 seconds of work - with a "
            "minute's rest between, about 8 minutes total; at a working "
            "output near 300 punches per minute that is roughly 1,800 "
            "punches thrown per session, each one audited by the opponent's "
            "resistance. The rules are strict and traditional: controlled "
            "contact, headgear and gloves, no strikes to forbidden targets, "
            "and a supervising instructor with absolute stop authority. "
            "Students discover in sparring what the drills cannot teach: "
            "that techniques shrink under adrenaline, that the guard drops "
            "when the lungs burn, and that the fighter who keeps the "
            "centerline when exhausted is the one the years of forms were "
            "building. Sparring is introduced gradually - positional rounds, "
            "then light continuous, then full - and it never replaces the "
            "forms; it verifies them."
        ),
        "how_it_works": (
            "Begin sparring only when your instructor clears you - "
            "typically after solid chi sao and drill fundamentals. Gear up "
            "fully: headgear, mouthguard, gloves, groin protection, and "
            "shin guards if kicks are included. Start with positional "
            "rounds: one partner attacks only with straight punches while "
            "the other defends only with the hand techniques, then swap - "
            "this isolates the skills before chaos. Progress to light "
            "continuous sparring at agreed contact levels, with the "
            "explicit goal of using Wing Chun techniques rather than "
            "brawling: the instructor stops the round the moment either "
            "fighter abandons the system for wild swinging. Run the "
            "standard structure - three 2-minute rounds with minute rests - "
            "and debrief after every session: which techniques appeared "
            "under pressure, which vanished, and what the forms need to "
            "fix. Keep a sparring journal noting the same. The golden rule: "
            "sparring is a laboratory, not a contest - the win is a "
            "technique that worked, not a partner who was hurt. Anyone "
            "using sparring to punish a partner is removed from sparring."
        ),
        "key_points": [
            "Lat Sau Jik Chung is Wing Chun's free sparring: protective gear, controlled contact, the whole curriculum tested against a resisting opponent.",
            "A standard session is three 2-minute rounds with minute rests - about 8 minutes, roughly 1,800 punches at a working output of 300 per minute.",
            "It is the examination the curriculum points toward: centerline, stance, chain punching, and deflections all audited by resistance.",
            "Introduction is gradual: positional rounds, then light continuous, then full - sparring verifies the forms, never replaces them.",
            "Sparring is a laboratory, not a contest: the win is a technique that worked, and anyone punishing a partner is removed.",
        ],
        "requirements": [
            "Instructor clearance based on solid chi sao and drill fundamentals before free sparring begins.",
            "Full protective gear: headgear, mouthguard, gloves, groin protection, shin guards where kicks are included.",
            "Graduated introduction: positional rounds first, then light continuous, then full sparring.",
            "A supervising instructor with absolute stop authority and pre-agreed contact levels and forbidden targets.",
            "A debrief and journal after every session: what worked under pressure, what vanished, what the forms must fix.",
        ],
        "standards": [
            "No sparring without instructor clearance and supervision; the supervisor's stop is absolute and instant.",
            "Contact is controlled at agreed levels; forbidden targets are briefed before every session.",
            "Using sparring to punish a partner ends the practitioner's sparring privileges.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM],
        "sig_lens": (
            "The Signature read: free sparring is the Signature's final "
            "examination - the resisting opponent auditing every covenant "
            "the forms made. Where public instruction teaches a sparring "
            "format, the Signature Combat Method teaches the truth of the "
            "laboratory: eighteen hundred punches per session, each one "
            "asking whether the centerline held when the lungs burned - "
            "and the fighter who kept it is the one the years were building."
        ),
    },
    {
        "key": "gor_sao",
        "name": "Gor Sao: Free Sticking Hands",
        "group": "Chi Sao",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Gor Sao - 'crossing hands' - is free chi sao: both partners "
            "roll in Luk Sao and either may attack at any moment with any "
            "technique, defending, countering, and returning to the roll "
            "in continuous improvisation. It is the closest Wing Chun "
            "comes to fighting without protective gear, and the drill "
            "where sensitivity becomes art: the practitioner feels the "
            "attack forming in the bridge and answers before it is thrown, "
            "turns the partner's pressure into openings, and chains Lap "
            "Sau, Pak Sau, punches, and kicks in flowing combinations. The "
            "exchange rate in skilled Gor Sao is blistering: with attacks "
            "launching roughly every 1.5 seconds, five minutes of free "
            "sticking produces about 200 exchanges - 400 techniques "
            "thrown, defended, and countered, each one decided by feel "
            "rather than sight. Gor Sao has its own etiquette, strictly "
            "observed: controlled contact, no muscling through technique "
            "with size and strength, an instant stop if either partner is "
            "hurt or overwhelmed, and the senior partner's duty to teach "
            "rather than dominate. It is traditionally introduced after "
            "years of structured chi sao, because free sticking without "
            "the roll's discipline degenerates into shoving and brawling - "
            "the roll is the grammar, and Gor Sao is the poetry spoken in it."
        ),
        "how_it_works": (
            "Begin in Luk Sao rolling with an experienced partner - Gor "
            "Sao is never a beginner's drill. Roll cooperatively for the "
            "first minute to establish the shared rhythm and trust; then, "
            "by prior agreement, open the round: either partner may break "
            "the roll with an attack - a punch from the bridge, a Lap Sau "
            "entry, a low kick - and the other answers with any defense "
            "and counter, both returning to the roll between exchanges. "
            "Keep the contact controlled and the pressure honest but not "
            "brutal: the goal is clean technique at speed, and muscling "
            "through with strength is a fault the senior partner corrects "
            "immediately. The defender's job is to feel the attack in the "
            "bridge before it launches; the attacker's job is to disguise "
            "intention until the last instant - this mutual sharpening is "
            "the drill's engine. Run timed rounds of 3 to 5 minutes with "
            "rests, and rotate partners: different bodies teach different "
            "lessons, and the practitioner who can only stick with one "
            "partner has learned a partner, not the art. End every session "
            "with cooperative rolling to close the practice cleanly."
        ),
        "key_points": [
            "Gor Sao ('crossing hands') is free chi sao: both partners roll in Luk Sao and either may attack at any moment, improvising continuously.",
            "Skilled exchanges run about one attack per 1.5 seconds - 200 exchanges, 400 techniques, in five minutes - all decided by feel rather than sight.",
            "It is sensitivity become art: feeling the attack forming in the bridge and answering before it is thrown.",
            "Strict etiquette governs it: controlled contact, no muscling with size, instant stops, and the senior partner's duty to teach rather than dominate.",
            "It requires years of structured chi sao first - free sticking without the roll's discipline degenerates into shoving; the roll is the grammar, Gor Sao the poetry.",
        ],
        "requirements": [
            "A mature Luk Sao roll as the platform - attacks launch from it and defenses return to it.",
            "An experienced partner and prior agreement on contact levels before any round opens.",
            "Attacks disguised until the last instant; defenses felt in the bridge before they launch.",
            "Controlled contact throughout, with muscling corrected as a fault, not rewarded.",
            "Timed 3 to 5 minute rounds with rests, rotating partners, closing with cooperative rolling.",
        ],
        "standards": [
            "Gor Sao is introduced only after years of structured chi sao; premature free sticking is forbidden.",
            "Either partner may stop the round instantly for pain, overwhelm, or loss of control - no questions asked.",
            "Senior partners teach; dominating a junior in Gor Sao is a breach of etiquette.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM, CIT_WINGTSUN],
        "sig_lens": (
            "The Signature read: free sticking is the Signature's poetry - "
            "the grammar of the roll spoken at speed, two hundred "
            "exchanges in five minutes, every one decided by touch. Where "
            "public instruction teaches a free drill, the Signature Combat "
            "Method teaches the covenant fulfilled: the bridge that was "
            "listened to for years now speaks first, and the hands answer "
            "before the attack has finished being thought."
        ),
    },
    {
        "key": "application",
        "name": "Wing Chun Self-Defense: The Application Framework",
        "group": "Hand Techniques",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The application framework is how Wing Chun's techniques "
            "become self-defense: the principles for recognizing danger, "
            "managing distance, de-escalating, and - only when necessary - "
            "applying the art's tools lawfully and proportionally. The "
            "framework starts before any technique: awareness of "
            "surroundings, recognition of pre-attack indicators, and the "
            "standing order that the best fight is the one avoided - "
            "de-escalation, apology, and departure are the advanced "
            "techniques. The distance math sets the doctrine: with average "
            "human reaction time near 0.25 seconds and an attacker's punch "
            "traveling about 5 meters per second, the punch covers 1.25 "
            "meters before the defender can even begin to respond - so the "
            "framework holds a safe distance near 1.5 meters, hands "
            "already in a non-threatening guard, and treats any closer "
            "approach by an aggressor as the trigger for the guard to "
            "become Man Sau and Wu Sau. If violence becomes unavoidable, "
            "the response is the art itself - simultaneous defense and "
            "attack down the centerline - applied only until the threat "
            "stops, and stopped the instant it does. The framework closes "
            "with the legal and ethical boundaries every student is taught: "
            "force must be lawful, necessary, and proportional; the "
            "techniques are for defense of self and others, never for "
            "aggression, intimidation, or settling disputes."
        ),
        "how_it_works": (
            "Train the framework as a decision ladder, not just techniques. "
            "First, practice awareness drills: walking a route and noting "
            "exits, blind spots, and the behavior of people around you - "
            "the habit of noticing is the first technique. Second, drill "
            "verbal de-escalation with a partner playing the aggressor: "
            "calm voice, open hands, creating distance while talking, and "
            "leaving at the first opportunity - score these drills like "
            "sparring rounds, because they are. Third, practice the "
            "trigger: partner steps aggressively inside 1.5 meters and your "
            "hands come up into the guard while you continue talking and "
            "moving offline - the guard appears without any strike, which "
            "is legally and tactically the correct first move. Fourth, "
            "only against a fully committed attack in protective gear, "
            "apply the physical techniques - simultaneous defense and "
            "attack - and practice the stop: the instant the partner "
            "signals or disengages, all offense ceases immediately. "
            "Rehearse the stop as seriously as the strike; the ability to "
            "turn the techniques off is what separates self-defense from "
            "assault. Review your jurisdiction's self-defense law with a "
            "qualified instructor's guidance and understand it before you "
            "ever need it."
        ),
        "key_points": [
            "The framework is a decision ladder: awareness first, de-escalation second, guard without striking third, physical technique only against committed attack - and the stop the instant the threat ends.",
            "Distance doctrine comes from reaction math: a 5 meter per second punch covers 1.25 meters in the 0.25 second reaction time, so the safe line is held near 1.5 meters.",
            "The best fight is the one avoided: de-escalation, apology, and departure are taught and scored as the advanced techniques.",
            "Physical response is the art itself - simultaneous defense and attack down the centerline - applied only until the threat stops.",
            "Force must be lawful, necessary, and proportional; the techniques defend self and others, never aggress, intimidate, or settle disputes.",
        ],
        "requirements": [
            "Daily awareness habits: noting exits, blind spots, and pre-attack indicators as a trained reflex.",
            "Drilled verbal de-escalation with distance creation, scored as seriously as sparring rounds.",
            "The guard trigger: hands rising to Man Sau and Wu Sau without striking when an aggressor closes inside 1.5 meters.",
            "Physical techniques reserved for committed attacks, practiced in protective gear with a rehearsed immediate stop.",
            "Working knowledge of the jurisdiction's self-defense law before the skills are ever needed.",
        ],
        "standards": [
            "De-escalation and avoidance are taught before physical techniques and tested alongside them.",
            "The immediate stop on threat cessation is drilled as a core skill, not an afterthought.",
            "Instructors teach the legal and ethical boundaries explicitly; techniques are never presented as tools of aggression.",
        ],
        "citations": [CIT_COMPLETE, CIT_COMPENDIUM],
        "sig_lens": (
            "The Signature read: the framework is the Signature's final "
            "covenant - the art's power leashed by its conscience. Where "
            "public instruction teaches self-defense, the Signature Combat "
            "Method teaches the whole ladder: see first, speak second, "
            "guard third, strike only when the committed attack leaves no "
            "other answer - and stop the instant the threat stops, because "
            "the line the Signature guards is drawn around the innocent, "
            "not around the fighter's pride."
        ),
    },
]
