#!/usr/bin/env python3
"""Entries for the Sumo Combat databases (combat batch 2, 2026-10-17).

Verified 2026-10-17: RAW SWEEP over the full manifest plus every shard
index title in jah-databases-data-1 plus the main-repo data dir: zero
'combat-sumo*' slugs/names; zero title collisions for all 68 titles
(34 public + 34 " (Signature Edition)") checked through the whole-system
dedupe gate BEFORE authoring: zero refusals. Near-hit check: existing
combat/martial-arts databases cover karate forms, green-beret material,
and self-defense knowledge; none teaches Japanese sumo fundamentals,
shiko training, or the 82 kimarite winning techniques with step-by-step
body mechanics, so BUILD NEW is the verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  combat-sumo                  - The Sumo Combat Database
                                 (public-harvest: real, fact-checked Japanese
                                 sumo: shiko and basic training, stance and
                                 footwork, and the 82 kimarite winning
                                 techniques - pushes, throws, leg trips - each
                                 record carrying step-by-step body mechanics;
                                 standard references: the Nihon Sumo Kyokai
                                 official kimarite list, dohyo dimensions and
                                 bout rules, and stable training practices)
  combat-sumo-signature        - The Sumo Combat Signature Database
                                 (his original Signature Sumo Method: the
                                 dohyo the field of work, the tachiai the
                                 oath of engagement, each kimarite a signed
                                 technique of balance taken and balance
                                 kept; src signature, titles suffixed
                                 " (Signature Edition)", never presented as
                                 authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBSUM- (public) and JAH-CBSUMS- (signature), verified free
in the manifest id_prefix values and in every shard index (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_combat_sumo.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Sumo Method: the "
            "dohyo the field of work, the tachiai the oath of engagement, "
            "each kimarite a signed technique of balance taken and balance "
            "kept. Clearly labeled Signature-made, never presented as "
            "authentic public record.")

CIT_KIMARITE = ("Nihon Sumo Kyokai (Japan Sumo Association). The 82 kimarite "
                "(decisive winning techniques) as codified by the Association: "
                "kihonwaza (fundamental techniques), nagewaza (throwing "
                "techniques), kakewaza (tripping techniques), hineriwaza "
                "(twisting techniques), soritewaza (lifting techniques), and "
                "tokushuwaza (special techniques).")
CIT_DOHYO = ("Nihon Sumo Kyokai. The dohyo (raised clay ring): a circle 4.55 "
             "meters (15 shaku) in diameter, bounded by the tawara (rice-straw "
             "bales). A bout is lost by stepping or being forced outside the "
             "tawara, or by touching the ground with any part of the body "
             "other than the soles of the feet.")
CIT_TRAINING = ("Standard professional sumo training practices: asageiko "
                "(morning practice), shiko (leg-stomping exercise), teppo "
                "(striking the wooden post), butsukari-geiko (impact "
                "practice), and moshiai-geiko (practice bouts), as conducted "
                "in sumo stables (heya) under the Japan Sumo Association.")
CIT_HISTORY = ("Sumo history: origins in Shinto ritual and the Kojiki "
               "chronicles (712 CE); professional sumo organized from the "
               "Edo period; the modern six-tournament honbasho system "
               "administered by the Japan Sumo Association.")

ENTRIES = [
    {
        "key": "kamae",
        "name": "Kamae: The Sumo Stance",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Kamae is the fundamental sumo stance, the posture every "
            "technique stands on. The wrestler crouches low with feet wider "
            "than shoulder width, toes angled slightly outward, knees bent "
            "deeply over the feet, back straight and leaning slightly "
            "forward, arms held ready in front of the body. The center of "
            "gravity drops low between the feet, which makes the stance "
            "resistant to pushes from the front, the side, and the rear. A "
            "wrestler who cannot hold kamae cannot do sumo: every shiko "
            "stomp, every suri-ashi slide, and every kimarite starts from "
            "this low, wide, balanced base. Beginners hold kamae against a "
            "wall or in front of a mirror for timed sets, building the "
            "quadriceps and hip endurance that sumo demands, until the low "
            "stance becomes the body's natural home."
        ),
        "how_it_works": (
            "Step one: place the feet about one and a half shoulder widths "
            "apart, toes pointing slightly outward, weight spread evenly "
            "across both soles. Step two: bend the knees until the thighs "
            "are near parallel to the ground, keeping the knees tracking "
            "over the toes and never collapsing inward. Step three: tilt "
            "the torso slightly forward from the hips, keeping the back "
            "flat and the head up with eyes forward, which places the "
            "center of mass low and slightly ahead of the feet. Step four: "
            "raise the arms in front of the body, elbows slightly bent and "
            "hands open, ready to meet the opponent. Step five: breathe "
            "deeply and settle; the stance is held by the legs, not braced "
            "by holding the breath. To test the stance, have a partner push "
            "lightly at the shoulders from several directions: a correct "
            "kamae rocks slightly and settles back to center, while a weak "
            "kamae steps or tips. Training sets run from thirty seconds up "
            "to several minutes as leg strength grows."
        ),
        "key_points": [
            "The stance is low and wide: feet beyond shoulder width, knees bent deep, torso leaning slightly forward, center of gravity dropped between the feet.",
            "Weight stays balanced across both soles; a kamae that leans to one side is already half-beaten.",
            "Knees track over the toes and never cave inward; the back stays flat and the head stays up.",
            "Arms stay ready in front of the body, not hanging at the sides, so the wrestler meets contact instead of receiving it.",
            "Every sumo technique starts from kamae: the stance is the root, and a shallow root topples in the first exchange.",
        ],
        "requirements": [
            "Flat, firm footing with enough space to widen the feet to about one and a half shoulder widths.",
            "Quadriceps and hip flexibility sufficient to hold a deep knee bend for at least thirty seconds.",
            "A wall or mirror for posture checks, or a training partner to test balance with light pushes.",
        ],
        "standards": [
            "Training follows standard stable practice: stance holds lengthen gradually, never jumped to full minutes on the first day.",
            "Balance checks use light partner pushes only; full-contact testing belongs to later training stages.",
        ],
        "citations": [CIT_TRAINING],
        "sig_lens": (
            "The Signature read: kamae is the signed stance of the worker - "
            "low, wide, rooted, ready from every direction. The Signature "
            "Sumo Method treats balance as the first covenant: before any "
            "technique is learned, the body signs its agreement with the "
            "ground, and the ground countersigns by holding it up."
        ),
    },
    {
        "key": "shiko",
        "name": "Shiko: The Leg Stomp Exercise",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Shiko is the signature exercise of sumo: the leg stomp performed "
            "at the start of every training session and every tournament "
            "day. From the low kamae stance, the wrestler lifts one leg high "
            "to the side, raising the foot well above waist level, then "
            "drives it down hard onto the clay, slapping the foot flat "
            "against the ground. The exercise builds hip flexibility, leg "
            "strength, and balance on the standing leg, and it opens the "
            "hips so the wrestler can drop low in a bout. Beginners start "
            "with a handful of slow, controlled stomps per side and work "
            "toward sets of fifty or a hundred per leg, alternating sides. "
            "The stomp is the heartbeat of sumo training: everything else - "
            "footwork, throws, trips - draws on the hips and balance that "
            "shiko forges."
        ),
        "how_it_works": (
            "Step one: settle into kamae, weight even, arms relaxed at the "
            "sides or lightly on the thighs. Step two: shift the weight "
            "fully onto one leg, rooting that foot into the ground. Step "
            "three: lift the opposite leg out to the side, keeping it as "
            "straight as balance allows, and raise the foot high - "
            "experienced wrestlers raise the foot above the head, beginners "
            "aim for waist height or wherever the hips allow. Step four: "
            "stomp the lifted foot straight down onto the ground with a "
            "firm flat slap, landing back into kamae without rocking or "
            "stepping. Step five: immediately repeat on the other side, "
            "keeping an even rhythm. The standing leg does the real work: "
            "it holds the whole body steady while the other leg moves. "
            "Common faults are leaning the torso toward the lifted leg, "
            "rushing the rhythm, and landing on the toes instead of the "
            "flat foot. A standard set is one hundred stomps, fifty per "
            "leg; a daily total in a stable runs to several hundred."
        ),
        "key_points": [
            "Shiko is performed from kamae: the stance is the platform, the stomp is the exercise.",
            "The lifted leg goes high to the side and comes down in a firm flat-footed slap; the torso stays upright throughout.",
            "The standing leg carries the training load: single-leg balance under full body weight builds the stability sumo needs.",
            "Rhythm stays even and unhurried; speed is added only after form is clean on both sides.",
            "Hip flexibility is the long prize: regular shiko opens the hips so the wrestler can fight lower and move wider.",
        ],
        "requirements": [
            "A solid kamae base that can hold single-leg balance for several seconds.",
            "Enough floor space to lift a leg high to the side without striking anything.",
            "A flat, forgiving surface; the stomp lands with real force, so thin floors or bare concrete are avoided.",
        ],
        "standards": [
            "Stables count shiko in sets of one hundred (fifty per leg); beginners build up in sets of twenty.",
            "The stomp lands flat-footed; toe-first landings are corrected as a form fault.",
        ],
        "citations": [CIT_TRAINING],
        "sig_lens": (
            "The Signature read: shiko is the stomp that signs the day - "
            "each leg lifted high and driven down is a signature struck on "
            "the ground. The Signature Sumo Method reads the hundred stomps "
            "as a hundred renewals of the balance covenant, hips opened, "
            "roots driven deeper with every count."
        ),
    },
    {
        "key": "suriashi",
        "name": "Suri-Ashi: Sliding Footwork",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Suri-ashi is sumo's sliding footwork: the wrestler moves "
            "without lifting the feet, gliding the soles across the clay "
            "in small smooth steps. The feet stay in contact with the "
            "ground, the knees stay bent, and the body stays low, so the "
            "wrestler is balanced and ready to push, pull, or turn at every "
            "instant. Lifting the feet would break the base and invite a "
            "trip; sliding keeps the center of gravity constant and the "
            "stance intact. Training runs the wrestler up and down the "
            "training hall in suri-ashi lanes, forward and backward, then "
            "sideways, until the glide is silent and effortless. In a bout, "
            "suri-ashi is how a pusher advances without giving up balance, "
            "and how a defender retreats without being chased down."
        ),
        "how_it_works": (
            "Step one: sink into kamae and fix the height of the hips - "
            "they must not bob up and down while moving. Step two: slide "
            "one foot forward a short distance, keeping the sole flat "
            "against the ground, feeling the floor the whole way. Step "
            "three: shift the weight onto the advanced foot and slide the "
            "trailing foot up to recover the stance width. Step four: "
            "repeat, maintaining an even rhythm, the head still and the "
            "eyes level. For backward movement the sequence reverses: the "
            "rear foot slides back first, then the front foot follows. For "
            "sideways movement the lead-side foot steps out first. The "
            "critical detail is that the moving foot never leaves the "
            "ground - the sole drags lightly, which keeps the body "
            "connected to the floor and ready. A ten-meter lane forward "
            "and back is one rep; beginners do a few lanes, wrestlers in "
            "training do dozens, and the glide should be quiet enough that "
            "the feet barely whisper."
        ),
        "key_points": [
            "The feet never leave the ground: sliding preserves the stance and keeps the wrestler trip-proof while moving.",
            "Hip height stays constant; bobbing up wastes energy and breaks the low base.",
            "The head stays still and level, eyes forward, so movement never costs awareness of the opponent.",
            "Forward, backward, and sideways glides are all trained; a wrestler who can only move forward is half a wrestler.",
            "Quiet feet are correct feet: noise means lifting, dragging, or stomping, all of which betray lost contact.",
        ],
        "requirements": [
            "A smooth, low-friction surface for sliding: packed clay, polished wood, or mats.",
            "A straight lane of at least ten meters for continuous forward and backward reps.",
            "A stable kamae that holds while the weight shifts foot to foot.",
        ],
        "standards": [
            "Suri-ashi lanes are a standard stable drill, done at the start of practice before contact work.",
            "The sole stays in floor contact throughout; stepping or hopping is corrected as a form fault.",
        ],
        "citations": [CIT_TRAINING],
        "sig_lens": (
            "The Signature read: suri-ashi is the signed glide - movement "
            "without leaving the ground, the Signature Sumo Method's image "
            "of progress that never breaks its base. The wrestler advances, "
            "retreats, and circles, and every inch is signed in the clay by "
            "a sole that never lifts."
        ),
    },
    {
        "key": "teppo",
        "name": "Teppo: Striking Post Training",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Teppo is the striking drill: the wrestler strikes a thick "
            "wooden post with open-handed slaps, alternating arms, driving "
            "each blow from the hips and the low stance. The post does not "
            "move, so every strike teaches the body to deliver force "
            "through a solid base, and the hands and forearms toughen with "
            "repetition. Teppo builds the arm strength and striking "
            "technique behind the thrusting attacks (tsuki) used in real "
            "bouts, and it conditions the striking surfaces so contact in "
            "a match does not injure the attacker. Sets run in the dozens "
            "per arm, struck with a sharp exhale, the wrestler resetting "
            "to kamae between strikes. The rhythm of teppo - strike, "
            "settle, strike - is the rhythm of every pushing attack in "
            "sumo."
        ),
        "how_it_works": (
            "Step one: face the post from about an arm's length away, feet "
            "in kamae, one foot slightly forward. Step two: raise the "
            "striking arm with the hand open, fingers together, palm facing "
            "the post. Step three: drive the strike from the legs and hips, "
            "rotating the torso into the blow, and slap the post with the "
            "heel of the palm and the fingers together - the arm extends "
            "fully but the elbow does not lock painfully. Step four: snap "
            "the hand back to guard immediately after contact; the strike "
            "is a whip, not a lean. Step five: exhale sharply on each "
            "strike and settle back into kamae before the next blow. "
            "Alternate arms evenly, fifty strikes per arm to a set. The "
            "common faults are striking with the arm alone (no hip drive), "
            "leaning the chest into the post after contact, and letting the "
            "guard hand drop. Over weeks the palms and forearms harden, "
            "the hip drive deepens, and the strike becomes a whole-body "
            "event."
        ),
        "key_points": [
            "The strike is driven from the hips and legs, not the arm: teppo teaches whole-body striking, not arm slapping.",
            "The striking surface is the open hand, fingers together; the snap-back is as important as the contact.",
            "Each strike ends back in kamae; the wrestler is never left leaning on the post.",
            "Both arms are trained equally, in even alternating sets, so the wrestler thrusts from either side.",
            "Repetition conditions the hands and forearms gradually; pain is a signal to check form, not to push through.",
        ],
        "requirements": [
            "A sturdy vertical post (traditionally wood) fixed firmly enough to take repeated full-force strikes.",
            "A solid kamae base to drive from; teppo without the stance is just arm work.",
            "Rest days or lighter volume when the hands are sore; conditioning is built over weeks, not forced in days.",
        ],
        "standards": [
            "Teppo sets are traditionally counted in the dozens per arm; form faults are corrected before volume is added.",
            "Striking is open-handed; closed-fist punching is not part of teppo or of sumo.",
        ],
        "citations": [CIT_TRAINING],
        "sig_lens": (
            "The Signature read: teppo is the signed strike - each slap on "
            "the post a signature driven through hip and leg into wood. "
            "The Signature Sumo Method treats the post as the unmoving "
            "problem: the wrestler does not move the post, the wrestler "
            "signs the post, and the signed strike becomes the thrust that "
            "moves opponents."
        ),
    },
    {
        "key": "matawari",
        "name": "Matawari: The Splits Stretch",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Matawari is the splits stretch, the flexibility exercise that "
            "opens the hips and inner thighs. The wrestler sits with legs "
            "spread wide, then leans the chest forward and down between "
            "the legs, pressing the torso toward the floor, and holds the "
            "deep stretch. Advanced wrestlers press the chest flat to the "
            "ground between fully split legs. Hip flexibility is what lets "
            "a wrestler drop into a deep kamae, spread wide against a "
            "push, and recover balance at extreme angles - without it, the "
            "stance stays high and every technique loses leverage. "
            "Matawari is done daily, held in long slow stretches rather "
            "than bounced, and progress is measured in centimeters over "
            "months. It is the quiet foundation beneath every dramatic "
            "throw: the flexible wrestler reaches positions the stiff "
            "wrestler cannot."
        ),
        "how_it_works": (
            "Step one: sit on the floor and spread the legs as wide as "
            "comfortable, toes pointing up, knees straight but not forced. "
            "Step two: sit tall for a few breaths, then hinge forward from "
            "the hips, reaching the chest toward the floor between the "
            "legs. Step three: when the forward stretch meets resistance, "
            "hold the position and breathe deeply for thirty seconds to a "
            "minute, letting the muscles release a little further with "
            "each exhale. Step four: walk the hands forward between the "
            "legs as the torso descends, aiming over weeks and months to "
            "bring the chest to the floor. Step five: ease out of the "
            "stretch slowly, shake the legs loose, and repeat for two or "
            "three holds. Never bounce: ballistic stretching in matawari "
            "risks the groin and hamstring attachments. Progress is "
            "patient - a few degrees of extra split per month is normal - "
            "and the stretch is done after the body is warm, never cold."
        ),
        "key_points": [
            "Matawari opens the hips and inner thighs; hip range is what lets a wrestler fight low and wide.",
            "The stretch is held long and breathed into, never bounced; patience is the method.",
            "Knees stay straight and toes stay up; forcing the knees down with the hands is a fault.",
            "Daily practice beats occasional marathon sessions: a little every day opens the hips over months.",
            "Flexibility is trained warm, after shiko and footwork, when the muscles are ready to lengthen.",
        ],
        "requirements": [
            "A clean floor or mat with room to spread the legs fully wide.",
            "A warmed-up body: matawari follows the active drills, never opens the session.",
            "Patience measured in months; anyone chasing the full split in weeks will injure something.",
        ],
        "standards": [
            "Stable practice treats matawari as daily maintenance, held in long static stretches.",
            "Stretching is never forced through sharp pain; the signal to stop is pain, the signal to continue is mild tension.",
        ],
        "citations": [CIT_TRAINING],
        "sig_lens": (
            "The Signature read: matawari is the signed opening - the "
            "wrestler signs wider and wider across the floor, and the "
            "Signature Sumo Method reads each new centimeter of split as "
            "range claimed. The low stance is bought with hip range, and "
            "hip range is bought one patient stretch at a time."
        ),
    },
    {
        "key": "tachiai",
        "name": "Tachiai: The Initial Charge",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The tachiai is the initial charge: the explosive collision "
            "that opens every bout. Both wrestlers crouch at their starting "
            "lines, touch the ground with both fists, and at the agreed "
            "moment launch forward, meeting chest to chest (or hand to "
            "chest) in the center of the ring. A good tachiai is low, fast, "
            "and driving - the wrestler hits with the whole body behind "
            "the contact and keeps the feet driving forward through the "
            "collision. A bad tachiai is high, hesitant, or off-balance, "
            "and it loses the bout in the first second. Wrestlers drill "
            "the tachiai endlessly: the timing of the launch, the angle of "
            "the hit, the immediate follow-up. Matches are often decided "
            "at the tachiai, which is why it is trained like a technique "
            "of its own."
        ),
        "how_it_works": (
            "Step one: crouch at the starting line (shikiri-sen), both "
            "fists touching the ground, eyes on the opponent, weight "
            "coiled in the legs. Step two: read the opponent's rhythm - "
            "the charge begins when both wrestlers agree the moment is "
            "right, and jumping the start is a false start. Step three: "
            "explode forward and slightly upward from the crouch, driving "
            "with the legs, leading with the chest and the hands. Step "
            "four: meet the opponent with the chest or the palms, striking "
            "into their upper body while the feet keep driving - the "
            "collision is not the end of the charge, it is the middle of "
            "it. Step five: on contact, immediately transition into the "
            "planned technique: drive for the push, secure the belt grip "
            "for the throw, or set the feet for the counter. The keys are "
            "staying low (a high tachiai gets lifted), keeping the head "
            "up (a dropped head gets slapped down), and never stopping the "
            "feet at the moment of impact."
        ),
        "key_points": [
            "The tachiai is a full-body charge, not a shove: legs drive, chest meets, feet keep moving through contact.",
            "Staying low is decisive; the lower wrestler at the collision usually controls what happens next.",
            "Both fists must touch the ground before the charge; a jumped start is a false start and the bout restarts.",
            "The charge continues through the collision: stopping the feet at impact surrenders all momentum.",
            "Every tachiai has a plan: the charge sets up the push, the grip, or the counter that follows.",
        ],
        "requirements": [
            "A proper crouch start with both fists down and eyes on the opponent.",
            "Explosive leg drive trained through shiko, stance holds, and short sprints.",
            "A training partner or pad to collide with; the tachiai cannot be drilled solo at full intent.",
        ],
        "standards": [
            "Bouts begin from the crouched position with both fists touching the ground, per Association rules.",
            "False starts are restarted; repeated false starts draw warnings from the referee.",
        ],
        "citations": [CIT_TRAINING, CIT_DOHYO],
        "sig_lens": (
            "The Signature read: the tachiai is the oath of engagement - "
            "the moment the wrestler signs the bout with the whole body. "
            "The Signature Sumo Method treats the charge as the first "
            "signature on the match: low, committed, and already carrying "
            "the plan for what the contact becomes."
        ),
    },
    {
        "key": "butsukari",
        "name": "Butsukari-Geiko: Impact Training",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Butsukari-geiko is impact training: one wrestler charges and "
            "drives into a partner who braces and absorbs the collision, "
            "then the driver keeps pushing the partner across the ring. "
            "The exercise trains both sides of contact - the attacker "
            "learns to hit low and keep driving through resistance, and "
            "the receiver learns to absorb force without breaking stance "
            "or stepping back. Repeated impacts condition the chest, "
            "shoulders, and arms to the collisions of real bouts, and the "
            "driving phase builds the sustained pushing power behind every "
            "oshiwaza technique. Butsukari is done in sets across the "
            "training hall, roles alternating, and it is one of the most "
            "physically demanding drills in the stable. It teaches the "
            "body what the tachiai feels like a hundred times over."
        ),
        "how_it_works": (
            "Step one: the receiver sets a deep kamae facing the driver, "
            "arms up to receive, chest braced. Step two: the driver takes "
            "a short run-up or starts from a crouch and charges into the "
            "receiver's chest and arms, hitting low with the whole body. "
            "Step three: on contact the receiver absorbs the hit by "
            "sinking slightly and letting the legs take the force, keeping "
            "the feet planted and the stance intact. Step four: the driver "
            "keeps the feet driving and pushes the receiver steadily "
            "across the floor, maintaining chest contact and a low "
            "posture. Step five: at the far wall or the set distance, both "
            "wrestlers reset, swap roles, and go again. The driver must "
            "not hit high (the receiver's chin and throat are never the "
            "target) and must not stop driving at the moment of contact. "
            "The receiver must not step back or brace with locked knees. "
            "Sets run to the length of the hall and back; both wrestlers "
            "are thoroughly worked by the end."
        ),
        "key_points": [
            "Both roles are trained: the driver learns the charge and the sustained push; the receiver learns to absorb without breaking.",
            "Contact is low and full-bodied; high hits and head contact are never the drill.",
            "The driver keeps driving through the collision; the receiver sinks and holds, never steps back.",
            "Repeated impacts condition the torso and arms to real bout collisions over weeks of practice.",
            "Butsukari is the bridge between the tachiai and the pushing techniques: charge, absorb, drive.",
        ],
        "requirements": [
            "Two trained partners of reasonably matched size, or a senior wrestler receiving for a junior.",
            "A long clear lane of mats or clay for the driving phase.",
            "Solid kamae from both wrestlers before contact begins; tired stances make for sloppy impacts.",
        ],
        "standards": [
            "Butsukari-geiko is standard stable practice, done in the contact portion of morning training.",
            "Head and throat contact is prohibited in the drill; the target is the chest and arms.",
        ],
        "citations": [CIT_TRAINING],
        "sig_lens": (
            "The Signature read: butsukari is the signed collision - hit "
            "and hold, drive and absorb, each role signing the other's "
            "training. The Signature Sumo Method treats the drill as the "
            "covenant of contact: the driver signs with force, the "
            "receiver countersigns by standing, and both leave stronger."
        ),
    },
    {
        "key": "yotsu",
        "name": "Yotsu Stances: Hidari-Yotsu and Migi-Yotsu",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The yotsu stances are the two belt-grip fighting postures, "
            "and most sumo is fought from one of them. In hidari-yotsu "
            "(left-hand inside), the wrestler's left hand grips inside the "
            "opponent's belt at the front while the right hand grips the "
            "outside of the belt; in migi-yotsu (right-hand inside) the "
            "hands reverse. The inside hand controls the opponent's center "
            "and sets up the great belt throws; the outside hand controls "
            "the hip and the turn. Wrestlers have a favored side, drilled "
            "until the grip is automatic, and entire bouts are contests to "
            "secure one's own yotsu while denying the opponent's. The grip "
            "is taken on the mawashi (the heavy belt), deep and tight, "
            "with the body low and the head positioned to avoid the "
            "opponent's inside arm."
        ),
        "how_it_works": (
            "Step one: from the tachiai or the clinch, work one hand "
            "inside to the front of the opponent's mawashi, gripping deep "
            "with the fingers and thumb locked around the belt. Step two: "
            "bring the other hand to the outside of the belt at the hip, "
            "gripping firmly. Step three: drop the hips low, tuck the head "
            "to the side of the opponent's inside arm so it cannot swim "
            "inside, and pull the opponent's body tight against your own - "
            "there should be no space between the two torsos. Step four: "
            "establish which yotsu you hold: left hand inside is "
            "hidari-yotsu, right hand inside is migi-yotsu, and your "
            "technique selection follows your grip. Step five: from the "
            "locked yotsu, attack: the inside hand lifts and turns for the "
            "throws, the hips drive for the force-out, the body twists for "
            "the trips. Losing the inside grip usually means losing the "
            "exchange, so wrestlers fight constantly to keep their hand "
            "inside and strip the opponent's."
        ),
        "key_points": [
            "Hidari-yotsu is left hand inside, right hand outside; migi-yotsu reverses the hands; every wrestler has a favored side.",
            "The inside hand is the weapon hand: it controls the center and sets up the throws.",
            "The grip is deep and tight on the mawashi, bodies pressed together with no space between.",
            "The head tucks to block the opponent's inside arm; head position is part of the grip fight.",
            "Losing the inside grip usually loses the exchange, so grip fighting is continuous.",
        ],
        "requirements": [
            "A mawashi (belt) worn correctly and tied tight; grip work is impossible on a loose belt.",
            "A partner to clinch with; the yotsu stances are trained in live grip exchanges.",
            "Forearm and grip strength built through teppo, shiko, and dedicated grip work.",
        ],
        "standards": [
            "Grips are taken on the mawashi; grabbing the opponent's throat, hair, or the belt knot area improperly is penalized.",
            "Yotsu fighting is the core of belt sumo and is drilled daily in stables.",
        ],
        "citations": [CIT_TRAINING, CIT_KIMARITE],
        "sig_lens": (
            "The Signature read: the yotsu grip is the signed hold - the "
            "inside hand signs its claim on the opponent's center. The "
            "Signature Sumo Method treats grip fighting as the negotiation "
            "before the technique: whoever holds the inside hand holds the "
            "pen, and the throw is just the signature being written."
        ),
    },
]
ENTRIES += [
    {
        "key": "oshidashi",
        "name": "Oshi-Dashi: The Frontal Push Out",
        "group": "Pushing Techniques",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Oshi-dashi is the frontal push out, the most fundamental of "
            "the 82 kimarite: the wrestler drives the opponent straight "
            "backward and out of the ring with sustained pushing, without "
            "grabbing the belt. The hands press against the opponent's "
            "chest, shoulders, or upper arms, the legs drive in suri-ashi, "
            "and the body stays low behind the push. It is the purest "
            "expression of pushing sumo (oshi-zumo): no grips, no throws, "
            "just continuous forward pressure until the opponent's heels "
            "cross the straw bales. Oshi-dashi decides more bouts than any "
            "other technique, because the tachiai itself is a push, and "
            "the wrestler who wins the first push usually finishes with "
            "this one. Training is butsukari-geiko made purposeful: hit "
            "low, keep the feet moving, and never let the push stall."
        ),
        "how_it_works": (
            "Step one: from the tachiai, plant both palms on the "
            "opponent's upper body - chest, shoulders, or the fronts of "
            "the arms - with the elbows slightly bent, never locked. Step "
            "two: drop the hips and drive forward with the legs, keeping "
            "the back straight and the head up; the power comes from the "
            "legs, the hands only transmit it. Step three: advance in "
            "suri-ashi, short sliding steps, maintaining constant pressure "
            "so the opponent never gets a moment to reset their feet. Step "
            "four: steer the opponent toward the ring's edge by angling "
            "the push slightly, keeping your own body between the opponent "
            "and the center of the ring. Step five: as the opponent's "
            "heels reach the tawara, give the final drive and follow "
            "through - but stay balanced, because a desperate opponent "
            "may sidestep, and the pusher who overcommits can be pulled "
            "down. The common faults are pushing with the arms alone, "
            "standing up during the drive, and pausing mid-push to "
            "re-grip, each of which hands the initiative back."
        ),
        "key_points": [
            "Oshi-dashi is the most common kimarite: a frontal push out with no belt grip, decided by continuous forward pressure.",
            "Power comes from the legs driving in suri-ashi; the arms transmit force, they do not generate it.",
            "Constant pressure is the method: any pause lets the opponent reset their feet and counter.",
            "The pusher steers toward the edge while staying between the opponent and the ring's center.",
            "Overcommitment is the danger: the final drive must stay balanced against the sidestep and pull-down counters.",
        ],
        "requirements": [
            "A driving tachiai and sustained leg drive trained through butsukari-geiko.",
            "Open-handed pushing on the chest, shoulders, or arms; grabbing the throat or hair is prohibited.",
            "Balance through the finish: the pusher must be able to stop or turn if the opponent sidesteps.",
        ],
        "standards": [
            "Oshi-dashi is classified among the kihonwaza (fundamental techniques) in the official kimarite list.",
            "The bout is won when the opponent steps outside the tawara or touches down; the pusher must remain inside and upright.",
        ],
        "citations": [CIT_KIMARITE, CIT_DOHYO],
        "sig_lens": (
            "The Signature read: oshi-dashi is the signed advance - "
            "pressure that never pauses, the Signature Sumo Method's image "
            "of steady work. No grip, no trick: the wrestler signs the "
            "opponent out of the ring one sliding step at a time, and the "
            "signature is legible in the unbroken line of the drive."
        ),
    },
    {
        "key": "oshitaoshi",
        "name": "Oshi-Taoshi: The Frontal Push Down",
        "group": "Pushing Techniques",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Oshi-taoshi is the frontal push down: like oshi-dashi, the "
            "wrestler pushes from the front without a belt grip, but "
            "instead of driving the opponent out of the ring, the push is "
            "angled downward so the opponent topples forward onto the "
            "clay. The technique punishes the opponent who leans too far "
            "forward resisting a push, or who is caught high and off "
            "balance: a sharp downward shove at the shoulders or upper "
            "chest sends them face-first to the ground. Where oshi-dashi "
            "is sustained pressure, oshi-taoshi is pressure with a "
            "downward finish - the same leg drive, the same hand position, "
            "but the final vector points at the clay instead of the edge. "
            "It is a kihonwaza fundamental, and it teaches the essential "
            "lesson that a push has a direction, and direction can be "
            "changed at the last instant."
        ),
        "how_it_works": (
            "Step one: establish the frontal push exactly as for "
            "oshi-dashi - palms on the upper body, hips low, legs driving. "
            "Step two: read the opponent's posture; oshi-taoshi works "
            "when the opponent is leaning forward into the push or has "
            "risen high, their weight already committed ahead of their "
            "feet. Step three: instead of continuing to drive horizontally, "
            "drop your own weight slightly and redirect the push downward, "
            "pressing the opponent's shoulders or upper chest toward the "
            "ground. Step four: keep the hands on the opponent through "
            "the fall, following them down just enough to complete the "
            "technique without falling yourself. Step five: recover to "
            "kamae the instant the opponent's body (other than the soles "
            "of the feet) touches the clay - the bout ends there. The "
            "timing is everything: push down too early and the opponent "
            "steps back; too late and they have already recovered. The "
            "downward finish must be decisive, a single committed "
            "redirection of the existing push."
        ),
        "key_points": [
            "Oshi-taoshi is the frontal push with a downward finish: the opponent topples forward onto the clay instead of being driven out.",
            "It punishes the leaning opponent: anyone pushing back too hard with the chest forward is already half toppled.",
            "The setup is identical to oshi-dashi; only the final vector changes, which makes it hard to read.",
            "Hands stay on the opponent through the fall to complete the technique without falling as well.",
            "Timing decides it: the downward redirection must land while the opponent's weight is committed forward.",
        ],
        "requirements": [
            "A working frontal push (oshi-dashi mechanics) as the entry; oshi-taoshi is a finish, not a standalone attack.",
            "An opponent leaning forward or caught high; pushing down a balanced, low opponent rarely works.",
            "Controlled follow-through: the attacker must not dive onto the clay with the opponent.",
        ],
        "standards": [
            "Oshi-taoshi is classified among the kihonwaza (fundamental techniques) in the official kimarite list.",
            "The bout is lost by touching the ground with any body part other than the soles of the feet.",
        ],
        "citations": [CIT_KIMARITE, CIT_DOHYO],
        "sig_lens": (
            "The Signature read: oshi-taoshi is the signed redirection - "
            "the same push, finished downward. The Signature Sumo Method "
            "treats it as the lesson of the adjustable plan: commit to the "
            "drive, but keep the finishing direction unsigned until the "
            "opponent's posture tells you where to sign."
        ),
    },
    {
        "key": "tsukidashi",
        "name": "Tsuki-Dashi: The Thrust Out",
        "group": "Pushing Techniques",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Tsuki-dashi is the thrust out: the wrestler drives the "
            "opponent out of the ring with a rapid series of open-handed "
            "thrusts to the chest and face, rather than one sustained "
            "push. Each thrust snaps out from the shoulder, lands with the "
            "palm heel, and retracts instantly, and the blows rain down in "
            "a continuous barrage that walks the opponent backward. The "
            "technique belongs to the thrusting specialists (tsuki-oshi "
            "wrestlers), whose teppo training gives them the arm speed and "
            "conditioning to keep the barrage going. Where oshi-dashi is a "
            "river, tsuki-dashi is a hailstorm: many sharp impacts instead "
            "of one long pressure. The defense is to slip inside the "
            "thrusts and take a belt grip, which is why thrusting wrestlers "
            "train to keep the barrage too fast to slip."
        ),
        "how_it_works": (
            "Step one: from the tachiai, establish range - close enough "
            "to land the thrusts, far enough that the opponent cannot "
            "easily grab the belt. Step two: fire the first thrust with "
            "the lead hand, palm heel to the opponent's chest or face, "
            "driven from the hip and shoulder exactly as drilled in "
            "teppo. Step three: snap the hand back instantly and fire the "
            "next thrust with the other hand, establishing an alternating "
            "rhythm of three to five thrusts per second. Step four: step "
            "forward with each pair of thrusts, advancing in short "
            "driving steps so the barrage walks the opponent backward. "
            "Step five: maintain the rhythm all the way to the edge; the "
            "moment the thrusts pause, the opponent will slip inside, so "
            "the final thrusts are the fastest. Guard the body during the "
            "barrage: the non-striking hand stays up, because a slipped "
            "thrust invites the belt grip that ends the attacker's night."
        ),
        "key_points": [
            "Tsuki-dashi is a barrage of alternating open-handed thrusts that walks the opponent out; many sharp impacts, not one long push.",
            "Each thrust is a teppo strike: hip-driven, palm-heel contact, instant snap-back.",
            "Range is the lifeline: too close and the opponent takes the belt; too far and the thrusts lose force.",
            "The rhythm must not pause; a gap in the barrage is the invitation to slip inside.",
            "Advance with the thrusts in short driving steps, steering the opponent toward the tawara.",
        ],
        "requirements": [
            "Teppo-conditioned hands, shoulders, and arms capable of sustaining a high-speed thrusting barrage.",
            "The discipline to keep range; thrusting wrestlers who crowd in get gripped and thrown.",
            "Footwork that advances with the hands; thrusts without forward steps push no one out.",
        ],
        "standards": [
            "Tsuki-dashi is classified among the kihonwaza (fundamental techniques) in the official kimarite list.",
            "Strikes are open-handed; closed-fist punching is prohibited in sumo.",
        ],
        "citations": [CIT_KIMARITE, CIT_TRAINING],
        "sig_lens": (
            "The Signature read: tsuki-dashi is the signed barrage - "
            "strike after strike, each one a signature on the opponent's "
            "retreat. The Signature Sumo Method reads the thrusting rhythm "
            "as relentless output: no single blow decides it, the "
            "unbroken sequence does."
        ),
    },
    {
        "key": "tsukitaoshi",
        "name": "Tsuki-Taoshi: The Thrust Down",
        "group": "Pushing Techniques",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Tsuki-taoshi is the thrust down: the thrusting barrage of "
            "tsuki-dashi, finished with a downward vector so the opponent "
            "collapses to the clay instead of stepping out. As the "
            "opponent retreats before the thrusts, leaning back or "
            "flinching away from the blows to the face, the attacker drops "
            "the final thrusts downward onto the shoulders and upper "
            "chest, driving the opponent straight down. It is the "
            "thrusting wrestler's answer to the opponent who refuses to "
            "be walked out: if they will not go back, they will go down. "
            "The technique demands the same arm speed and conditioning as "
            "tsuki-dashi, plus the judgment to read when the opponent's "
            "balance has shifted from retreating to toppling."
        ),
        "how_it_works": (
            "Step one: establish the thrusting barrage exactly as for "
            "tsuki-dashi, walking the opponent backward with alternating "
            "palm-heel thrusts. Step two: watch the opponent's head and "
            "shoulders; when they start leaning back away from the blows "
            "or their steps become short and choppy, their balance is "
            "ripe. Step three: drop your own hips slightly and redirect "
            "the next thrusts downward, striking down onto the shoulders "
            "and upper chest instead of straight into them. Step four: "
            "follow the downward thrusts with your body weight, pressing "
            "through the opponent's guard until their knees buckle or "
            "their hands touch the clay. Step five: stay on your feet and "
            "recover to kamae; the bout ends the instant any part of the "
            "opponent besides the soles touches down. The fault to avoid "
            "is telegraphing the downward shift too early, which lets the "
            "opponent duck under the high thrusts and take the belt."
        ),
        "key_points": [
            "Tsuki-taoshi finishes the thrusting barrage downward: the retreating opponent collapses to the clay.",
            "It punishes the backward lean: an opponent flinching away from face thrusts is already falling.",
            "The read is in the head and shoulders; when they tip back, the downward finish is on.",
            "The attacker follows through with body weight but stays on the feet.",
            "Telegraphing the shift too early lets the opponent duck under and take the belt.",
        ],
        "requirements": [
            "A working thrusting barrage (tsuki-dashi mechanics) as the entry.",
            "An opponent retreating or leaning back under the thrusts; the downward finish needs a ripe target.",
            "The conditioning to keep the barrage fast through the final downward thrusts.",
        ],
        "standards": [
            "Tsuki-taoshi is classified among the kihonwaza (fundamental techniques) in the official kimarite list.",
            "Thrusts are open-handed; the bout ends when any part of the opponent besides the soles touches the clay.",
        ],
        "citations": [CIT_KIMARITE, CIT_DOHYO],
        "sig_lens": (
            "The Signature read: tsuki-taoshi is the signed change of "
            "direction - the barrage that was walking the opponent back "
            "suddenly signs downward. The Signature Sumo Method treats it "
            "as reading the opponent's answer and overwriting it: they "
            "chose retreat, the wrestler signs the fall."
        ),
    },
    {
        "key": "okuridashi",
        "name": "Okuri-Dashi: The Rear Push Out",
        "group": "Pushing Techniques",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Okuri-dashi is the rear push out: the wrestler gets behind "
            "the opponent and pushes them out of the ring from the back. "
            "It is the technique of the turned bout - the opponent has "
            "been spun, has turned to escape, or has overcommitted to an "
            "attack, and now their back is exposed. The attacker presses "
            "both hands into the opponent's back or sides and drives them "
            "forward and out, staying behind them so they cannot turn "
            "back. Okuri-dashi rewards the wrestler who keeps moving when "
            "the opponent turns: where others pause at the spin, the "
            "okuri-dashi wrestler is already behind, already pushing. It "
            "is a kihonwaza fundamental, and it teaches that a bout is "
            "never over at the turn - the turn is often where it is won."
        ),
        "how_it_works": (
            "Step one: recognize the turn - the opponent spins away from "
            "a throw attempt, turns to flee a push, or overrotates on "
            "their own attack. Step two: stay close and get behind, "
            "placing both hands on the opponent's back or flanks before "
            "they can square up again. Step three: drive forward with the "
            "legs in suri-ashi, pushing through the opponent's back, "
            "keeping your chest close so they cannot turn into you. Step "
            "four: steer them toward the nearest edge, adjusting the push "
            "angle as they stumble to stay behind them. Step five: finish "
            "with a final drive as they cross the tawara, then check your "
            "own balance - the most common failure is the attacker "
            "stumbling out after the opponent in the excitement of the "
            "chase. The push must be controlled: wild shoving from behind "
            "risks both wrestlers going out together, and the bout goes "
            "to whoever touches down or steps out first."
        ),
        "key_points": [
            "Okuri-dashi is won at the turn: the opponent's back is exposed, and the wrestler who is already behind wins.",
            "Both hands press the back or flanks; the attacker stays glued behind so the opponent cannot square up.",
            "The drive is the familiar leg-powered push in suri-ashi, steered toward the nearest edge.",
            "Control beats wildness: shoving from behind can carry both wrestlers out, and order of exit decides the bout.",
            "The turn is not the end of the bout; for the okuri-dashi wrestler, it is the beginning of the win.",
        ],
        "requirements": [
            "The awareness to keep moving when the opponent turns, instead of pausing at the spin.",
            "Position behind the opponent with hands on the back or flanks before they square up.",
            "Balance through the finish; chasing the opponent out after them loses the bout.",
        ],
        "standards": [
            "Okuri-dashi is classified among the kihonwaza (fundamental techniques) in the official kimarite list.",
            "Pushing is open-handed on the back and sides; strikes to the back of the head are prohibited.",
        ],
        "citations": [CIT_KIMARITE, CIT_DOHYO],
        "sig_lens": (
            "The Signature read: okuri-dashi is the signed follow-through "
            "- the wrestler does not stop at the opponent's turn but signs "
            "past it. The Signature Sumo Method treats the turned back as "
            "an unsigned opportunity: be already behind it, already "
            "pushing, and the bout signs itself."
        ),
    },
    {
        "key": "okuritaoshi",
        "name": "Okuri-Taoshi: The Rear Push Down",
        "group": "Pushing Techniques",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Okuri-taoshi is the rear push down: from behind the turned "
            "opponent, the wrestler drives them down to the clay instead "
            "of pushing them out. The hands press down on the opponent's "
            "back, shoulders, or the back of the belt, and the attacker's "
            "weight follows the push downward until the opponent's knees "
            "or hands touch. It is the close-quarters cousin of "
            "okuri-dashi, used when the opponent is too close to the "
            "center to be pushed out, or when they stumble and their "
            "upper body is already falling forward. The technique is "
            "decisive and abrupt: one moment the opponent is turning, the "
            "next they are on the clay. Like all rear techniques it "
            "demands control, because the attacker is pressing down on a "
            "falling body and must not follow it to the ground."
        ),
        "how_it_works": (
            "Step one: secure the rear position exactly as for "
            "okuri-dashi, hands on the opponent's back, flanks, or the "
            "back of the belt. Step two: read the fall - okuri-taoshi is "
            "on when the opponent's upper body is tipping forward, their "
            "steps are stumbling, or they are too central for the push "
            "out. Step three: press downward with both hands while "
            "dropping your own hips, driving the opponent's shoulders "
            "toward the clay. Step four: keep the pressure on through the "
            "descent, following just far enough to complete the technique; "
            "the instant a knee, hand, or any other body part touches, "
            "the bout is over. Step five: arrest your own downward "
            "momentum and stand clear in kamae - falling onto or with the "
            "opponent risks a disputed call or an injury to both. The "
            "downward press must be committed but measured: enough to "
            "finish a stumbling opponent, controlled enough to stay on "
            "your feet."
        ),
        "key_points": [
            "Okuri-taoshi is the rear attack finished downward: the turned, stumbling opponent is pressed to the clay.",
            "It is chosen when the opponent is too central to push out or already falling forward.",
            "The press is downward through the back and shoulders, with the attacker's hips dropping behind it.",
            "The attacker must arrest the follow-through and stay on the feet; falling with the opponent is the fault.",
            "The read is in the stumble: upper body tipping forward means the downward finish is available.",
        ],
        "requirements": [
            "The rear position secured before the opponent squares up, as for okuri-dashi.",
            "A stumbling or forward-tipping opponent; pressing down a balanced opponent from behind rarely works.",
            "The body control to press down hard and stop, staying upright while the opponent goes down.",
        ],
        "standards": [
            "Okuri-taoshi is classified among the kihonwaza (fundamental techniques) in the official kimarite list.",
            "The bout ends when any part of the opponent besides the soles touches the clay.",
        ],
        "citations": [CIT_KIMARITE, CIT_DOHYO],
        "sig_lens": (
            "The Signature read: okuri-taoshi is the signed descent - the "
            "rear attack that finishes the stumble instead of chasing it. "
            "The Signature Sumo Method treats the falling opponent as a "
            "sentence already half-written: press it to the clay, sign it, "
            "and stand clear."
        ),
    },
    {
        "key": "hatakikomi",
        "name": "Hatakikomi: The Slap Down",
        "group": "Pulling and Slap Techniques",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Hatakikomi is the slap down: as the opponent charges or "
            "pushes forward, the wrestler slaps down hard on their "
            "shoulder, upper arm, or the side of the head, redirecting "
            "their forward momentum into the clay. It is the classic "
            "counter to the reckless charge - the harder the opponent "
            "comes in, the harder they fall, because their own drive "
            "becomes the force that topples them. The slap is open-handed "
            "and downward, timed to land exactly as the opponent's weight "
            "commits past their feet, and the wrestler sidesteps slightly "
            "so the falling body does not take them down too. Hatakikomi "
            "is a hineriwaza (twisting technique) in the official "
            "classification, and it is the first great lesson in using "
            "the opponent's force: never meet a charge head-on when you "
            "can slap it into the ground."
        ),
        "how_it_works": (
            "Step one: as the opponent charges or drives forward, hold "
            "your ground in kamae and let them commit - hatakikomi needs "
            "their momentum, so patience is the setup. Step two: at the "
            "instant their weight shifts past their lead foot, swing your "
            "arm down in a hard open-handed slap onto their shoulder, "
            "upper arm, or the side of the head and neck. Step three: "
            "step slightly to the side as you slap, clearing your body "
            "from the path of the falling opponent. Step four: follow the "
            "slap through downward, adding your body weight to their "
            "momentum, driving them face-first toward the clay. Step "
            "five: stay on your feet and recover to kamae as they touch "
            "down. The timing window is narrow: slap too early and they "
            "adjust; too late and they run through you. The slap must be "
            "downward, not across - a sideways slap spins the opponent "
            "instead of dropping them, which is a different technique "
            "entirely."
        ),
        "key_points": [
            "Hatakikomi turns the opponent's charge against them: their forward momentum becomes the force of their fall.",
            "The slap is open-handed and downward, onto the shoulder, upper arm, or side of the head, timed to the weight commitment.",
            "The wrestler sidesteps as they slap, clearing the falling body's path.",
            "Patience is the setup: the technique needs the opponent's committed momentum, so it cannot be forced early.",
            "It is the first lesson in not meeting force with force: redirect the charge into the clay.",
        ],
        "requirements": [
            "A charging or heavily forward-committed opponent; hatakikomi has nothing to work with against a cautious one.",
            "Precise timing: the slap must land as the opponent's weight passes their lead foot.",
            "The sidestep and balance to stay upright while the opponent falls past.",
        ],
        "standards": [
            "Hatakikomi is classified among the hineriwaza (twisting techniques) in the official kimarite list.",
            "The slap is open-handed; striking with a closed fist is prohibited.",
        ],
        "citations": [CIT_KIMARITE],
        "sig_lens": (
            "The Signature read: hatakikomi is the signed redirection of "
            "recklessness - the harder they charge, the harder the "
            "signature lands. The Signature Sumo Method treats the "
            "opponent's momentum as ink: let them supply it, then sign it "
            "downward into the clay."
        ),
    },
    {
        "key": "hikiotoshi",
        "name": "Hiki-Otoshi: The Hand Pull Down",
        "group": "Pulling and Slap Techniques",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Hiki-otoshi is the hand pull down: the wrestler grips the "
            "opponent's arm, wrist, or mawashi and yanks them sharply "
            "downward and forward, using their forward lean and momentum "
            "to drop them to the clay. Like hatakikomi it feeds on the "
            "opponent's aggression, but where the slap down is a strike, "
            "the hand pull down is a grip technique - the attacker holds "
            "on and pulls the opponent's committed weight straight down. "
            "It is devastating against the opponent who overreaches with "
            "a push or a grab: the extended arm becomes a handle, and one "
            "sharp downward pull folds them. Hiki-otoshi is classified "
            "among the hineriwaza, and it teaches the grip-fighter's "
            "version of the counterattacker's creed: let them reach, then "
            "pull the reach into the ground."
        ),
        "how_it_works": (
            "Step one: secure a grip on the opponent's wrist, forearm, or "
            "the front of their mawashi as they push or reach toward you. "
            "Step two: wait for - or invite - their forward commitment: "
            "the pull works when their weight is moving toward you or "
            "leaning over their lead foot. Step three: drop your hips and "
            "yank the gripped arm sharply down and slightly toward you, "
            "rotating your torso into the pull for full-body power. Step "
            "four: keep pulling through the descent, guiding the "
            "opponent's head and shoulders toward the clay while you stay "
            "low and balanced. Step five: release or control the grip as "
            "they touch down, and recover to kamae without being dragged "
            "forward yourself. The pull is sudden and total - a hesitant "
            "half-pull just warns the opponent. And the attacker must keep "
            "the hips below the pull: pulling from a high stance pulls "
            "the attacker off balance instead."
        ),
        "key_points": [
            "Hiki-otoshi is a grip counter: hold the reaching arm or belt and yank the committed weight down.",
            "It feeds on overreach: the extended arm becomes the handle for the opponent's own fall.",
            "The pull is sudden, downward, and full-bodied - hips drop, torso rotates, no hesitation.",
            "The attacker stays low and balanced; a high pull drags the attacker down instead.",
            "Control the grip through the fall and recover without being pulled forward.",
        ],
        "requirements": [
            "A grip on the wrist, forearm, or front of the mawashi, secured as the opponent reaches or pushes.",
            "A forward-committed opponent; the pull needs their momentum or lean to work with.",
            "The hip drop and torso rotation that make the pull a whole-body technique, not an arm yank.",
        ],
        "standards": [
            "Hiki-otoshi is classified among the hineriwaza (twisting techniques) in the official kimarite list.",
            "Grips on the mawashi and arms are legal; pulling hair or the throat is prohibited.",
        ],
        "citations": [CIT_KIMARITE],
        "sig_lens": (
            "The Signature read: hiki-otoshi is the signed answer to "
            "overreach - the opponent extends a handle, and the Signature "
            "Sumo Method signs the pull that folds them. Let them reach: "
            "every reach is an unsigned line, and the pull is the "
            "signature that completes it downward."
        ),
    },
    {
        "key": "sukuinage",
        "name": "Sukuinage: The Beltless Arm Throw",
        "group": "Throwing Techniques",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Sukuinage is the beltless arm throw: without taking a belt "
            "grip, the wrestler scoops the opponent's arm and body with "
            "both arms and throws them forward and down. The attacker "
            "slides one arm under the opponent's armpit and across the "
            "back or chest, locks it with the other arm, then lifts and "
            "twists, dumping the opponent to the clay in front. It is the "
            "bridge between pushing sumo and belt sumo - no mawashi grip "
            "required, just the scoop, the lift, and the turn. Sukuinage "
            "is classified among the nagewaza (throwing techniques), and "
            "it is often the first throw a pushing wrestler learns, "
            "because it starts from the same chest-to-chest contact as "
            "the push. The keys are getting the scooping arm deep under "
            "the armpit and committing the hips to the lift."
        ),
        "how_it_works": (
            "Step one: from chest-to-chest contact, slide your lead arm "
            "deep under the opponent's armpit, reaching across their back "
            "or chest, and lock it against your own body with your other "
            "arm. Step two: drop your hips below the opponent's center "
            "and pull their upper body tight against yours - the scoop "
            "must be snug, with no space for them to slip out. Step three: "
            "lift with the legs while twisting your torso, turning your "
            "back partially toward the direction of the throw. Step four: "
            "as the opponent's feet lighten, complete the twist and dump "
            "them forward and down to the clay in front of you. Step five: "
            "stay on your feet through the throw, releasing the lock as "
            "they go down, and recover to kamae. The common faults are a "
            "shallow scoop (the arm slides out), lifting with the back "
            "instead of the legs, and failing to commit to the twist, "
            "which leaves the opponent draped over you instead of thrown."
        ),
        "key_points": [
            "Sukuinage needs no belt grip: scoop under the armpit, lock the arms, lift and twist the opponent down.",
            "The scooping arm must go deep; a shallow scoop lets the opponent slide out.",
            "The lift comes from the legs with the hips below the opponent's center; the back stays straight.",
            "The twist completes the throw: lift without turning just holds the opponent up.",
            "It is the pushing wrestler's first throw, launched from the same contact as the push.",
        ],
        "requirements": [
            "Chest-to-chest contact with the opponent's armpit accessible for the scoop.",
            "The leg strength to lift a resisting opponent's weight briefly, trained through shiko and stance work.",
            "Commitment to the twist; a half-hearted sukuinage ends with the opponent on top.",
        ],
        "standards": [
            "Sukuinage is classified among the nagewaza (throwing techniques) in the official kimarite list.",
            "The throw is completed without a belt grip; the arms control the opponent's upper body throughout.",
        ],
        "citations": [CIT_KIMARITE],
        "sig_lens": (
            "The Signature read: sukuinage is the signed scoop - no belt, "
            "no handle but the body itself. The Signature Sumo Method "
            "treats it as the technique of working with what is at hand: "
            "slide under, lock on, lift with the legs, and sign the turn "
            "that puts them down."
        ),
    },
    {
        "key": "uwatenage",
        "name": "Uwate-Nage: The Overarm Throw",
        "group": "Throwing Techniques",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Uwate-nage is the overarm throw: from the belt grip, the "
            "wrestler's outside arm - the uwate, thrown over the "
            "opponent's arm - pulls down and around in a great arc, "
            "throwing the opponent over and down to the clay. It is one "
            "of the signature techniques of sumo, the throw the crowd "
            "rises for: the attacker locks the overarm grip deep on the "
            "belt, turns the hips, and wheels the opponent around the "
            "body like a door swinging on a hinge. The overarm grip gives "
            "tremendous leverage, because the arm comes over the top and "
            "the whole torso rotates behind it. Uwate-nage is classified "
            "among the nagewaza, and mastering it is a rite of passage: "
            "the wrestler who can throw with the overarm can throw anyone "
            "they can grip."
        ),
        "how_it_works": (
            "Step one: secure the belt with the outside arm thrown over "
            "the opponent's arm, gripping the mawashi deep at the back or "
            "side - this is the uwate grip, and it must be deep, not a "
            "fingertip hold. Step two: pull the opponent tight against "
            "your side, eliminating all space, and set your hips below "
            "theirs. Step three: step across and turn your hips sharply, "
            "rotating your body so your back turns toward the throwing "
            "direction. Step four: pull the overarm down and around in a "
            "wide arc, using the hip turn to wheel the opponent's body "
            "over and down - the arm describes the circle, the hips "
            "supply the force. Step five: follow through until the "
            "opponent lands on the clay, then release and recover to "
            "kamae on your feet. The grip depth decides everything: a "
            "shallow uwate slips off mid-throw. The turn must be total - "
            "a partial turn leaves the opponent standing beside you, "
            "which is the worst place to be."
        ),
        "key_points": [
            "Uwate-nage is the overarm belt throw: the outside arm arcs down and around, wheeling the opponent over.",
            "The uwate grip must be deep on the mawashi; a shallow grip slips off mid-throw.",
            "The hips turn fully and supply the force; the arm describes the arc, the body powers it.",
            "Pull the opponent tight with no space before the turn; space is where throws die.",
            "Commit to the full turn: a partial rotation strands the attacker beside an unthrown opponent.",
        ],
        "requirements": [
            "A deep overarm (uwate) grip on the opponent's mawashi, secured in the grip fight.",
            "The hip mobility and core rotation to turn fully under load, built through shiko and matawari.",
            "A partner trained to take the fall; the overarm throw lands hard and is never drilled on the unwilling.",
        ],
        "standards": [
            "Uwate-nage is classified among the nagewaza (throwing techniques) in the official kimarite list.",
            "The grip is on the mawashi; the throw is completed with the attacker remaining on the feet.",
        ],
        "citations": [CIT_KIMARITE],
        "sig_lens": (
            "The Signature read: uwate-nage is the signed arc - the "
            "overarm describing a great circle and the opponent wheeled "
            "along it. The Signature Sumo Method treats the deep grip as "
            "the pen grip and the hip turn as the hand: hold deep, turn "
            "fully, and the throw signs itself across the clay."
        ),
    },
    {
        "key": "shitatenage",
        "name": "Shitate-Nage: The Underarm Throw",
        "group": "Throwing Techniques",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Shitate-nage is the underarm throw: the inside belt hand - "
            "the shitate, threaded under the opponent's arm - lifts and "
            "turns the opponent over and down. Where uwate-nage wheels "
            "the opponent around with the overarm, shitate-nage upends "
            "them with the underarm, the inside hand acting as the pivot "
            "around which the opponent's body rotates. The inside grip is "
            "the most fought-over position in sumo precisely because it "
            "enables this throw: the hand is already at the opponent's "
            "center, and a sharp lift-and-turn folds them over it. "
            "Shitate-nage is classified among the nagewaza, and it is the "
            "yotsu wrestler's bread and butter - the reward for winning "
            "the inside grip in the clinch."
        ),
        "how_it_works": (
            "Step one: win the inside position - your hand threaded under "
            "the opponent's arm, gripping the front of their mawashi "
            "deep. This is the shitate grip, and the whole technique "
            "depends on holding it. Step two: pull the opponent's body "
            "tight to yours and drop your hips, loading your legs like a "
            "spring. Step three: lift sharply with the inside hand while "
            "turning your torso, pivoting the opponent's body up and over "
            "the gripping hand. Step four: continue the turn, guiding the "
            "opponent's rotation until they land on the clay beside or in "
            "front of you. Step five: stay on your feet, control the "
            "landing, and recover to kamae. The lift must be explosive - "
            "a slow lift lets the opponent widen their base and kill the "
            "throw. The turn must be committed - the inside hand is the "
            "pivot, and the body rotates around it. Lose the inside grip "
            "mid-throw and the technique collapses, which is why grip "
            "strength is the hidden requirement."
        ),
        "key_points": [
            "Shitate-nage is the underarm belt throw: the inside hand lifts and the opponent pivots over it.",
            "The inside (shitate) grip is the prize of the clinch; this throw is its reward.",
            "The lift is explosive and the turn is committed; slow or partial execution kills the throw.",
            "Hips drop below the opponent's center before the lift; the legs spring the body upward.",
            "Grip strength is the hidden requirement: the throw dies the instant the inside hand slips.",
        ],
        "requirements": [
            "The inside hand position won and held: threaded under the opponent's arm, deep on the front of the mawashi.",
            "Explosive hip and leg drive to lift a resisting opponent's weight.",
            "Grip endurance to hold the shitate through the full rotation.",
        ],
        "standards": [
            "Shitate-nage is classified among the nagewaza (throwing techniques) in the official kimarite list.",
            "The throw pivots on the inside grip; the attacker remains on the feet through the completion.",
        ],
        "citations": [CIT_KIMARITE],
        "sig_lens": (
            "The Signature read: shitate-nage is the signed pivot - the "
            "inside hand the fixed point, the opponent's body the line "
            "that turns around it. The Signature Sumo Method treats the "
            "won inside grip as the signed claim: hold the center, lift "
            "it, and turn the claim into the throw."
        ),
    },
    {
        "key": "kotenage",
        "name": "Kote-Nage: The Armlock Throw",
        "group": "Throwing Techniques",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Kote-nage is the armlock throw: the wrestler traps the "
            "opponent's arm across their own body, locks it with both "
            "hands, and twists it into a throw that spins the opponent "
            "down to the clay. The locked arm becomes a lever: by "
            "controlling the wrist and elbow and turning the body, the "
            "attacker rotates the opponent's whole frame around the "
            "trapped arm. It is one of the most technical throws in the "
            "kimarite list, demanding precise arm control rather than raw "
            "power, and it punishes the opponent who reaches in with a "
            "loose arm. Kote-nage is classified among the nagewaza, and it "
            "is drilled slowly and carefully, because a locked arm under "
            "full force is unforgiving - control in practice is what "
            "makes the technique usable in a bout."
        ),
        "how_it_works": (
            "Step one: as the opponent reaches in or extends an arm, wrap "
            "it: slide your arm over theirs and lock their wrist and "
            "forearm against your chest or side with both hands. Step two: "
            "secure the lock - their elbow is controlled, their wrist is "
            "held, and the arm cannot pull free. Step three: step across "
            "and turn your body sharply, using the trapped arm as the "
            "lever to rotate their whole frame. Step four: continue the "
            "turn, guiding them down to the clay in a spiral; the lock "
            "converts your rotation into their fall. Step five: release "
            "the lock the moment they are going down - never crank a "
            "trapped arm past the fall - and recover to kamae. In "
            "practice the throw is drilled at walking speed with a "
            "cooperative partner, and the lock is released early and "
            "often. The technique's danger is also its discipline: the "
            "wrestler who masters the release masters the throw."
        ),
        "key_points": [
            "Kote-nage traps the opponent's arm and uses it as a lever, twisting the whole body down in a spiral.",
            "It punishes the loose reaching arm; a tucked, controlled arm gives the throw nothing to trap.",
            "The lock controls wrist and elbow against the attacker's body; the turn supplies the throwing force.",
            "Drilled slowly with a cooperative partner; the locked arm is unforgiving at full force.",
            "The lock is released as the opponent falls; cranking past the fall is never part of the technique.",
        ],
        "requirements": [
            "Precise arm control and the timing to trap a reaching arm before it retracts.",
            "A cooperative, trained partner for drilling; the armlock is never practiced at speed on the unwilling.",
            "The discipline to release the lock the instant the throw is decided.",
        ],
        "standards": [
            "Kote-nage is classified among the nagewaza (throwing techniques) in the official kimarite list.",
            "Training practice requires controlled drilling with early release; joint safety governs the drill.",
        ],
        "citations": [CIT_KIMARITE],
        "sig_lens": (
            "The Signature read: kote-nage is the signed lever - the "
            "trapped arm the handle, the turn the signature. The "
            "Signature Sumo Method treats it as precision over power: the "
            "technique is signed not with force but with control, and the "
            "release is part of the signature."
        ),
    },
    {
        "key": "kubinage",
        "name": "Kubi-Nage: The Head Pivot Throw",
        "group": "Throwing Techniques",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Kubi-nage is the head pivot throw: the wrestler wraps an arm "
            "around the opponent's head and neck, locks it against the "
            "body, and pivots the opponent over and down around that "
            "point. The head becomes the fulcrum: with the neck controlled "
            "and the body turning, the opponent's frame rotates around "
            "the held head until they land on the clay. It is a close, "
            "physical technique, used in the grinding clinch when the belt "
            "grips are stalemated and the head is the available handle. "
            "Kubi-nage is classified among the nagewaza, and like the "
            "armlock throw it is drilled with care, because the neck is "
            "involved - the throw pivots the body around the head, it "
            "never cranks the neck itself."
        ),
        "how_it_works": (
            "Step one: in the close clinch, slide your arm around the "
            "opponent's head and neck, cupping the head and locking your "
            "hands together or against your own body so the hold is snug "
            "but not a choke. Step two: pull the opponent's upper body "
            "tight and drop your hips, setting the pivot. Step three: "
            "turn your body sharply, pivoting the opponent's frame around "
            "the held head - their body rotates, their feet leave their "
            "base, and the throw develops. Step four: guide the rotation "
            "down to the clay, controlling the fall so the opponent lands "
            "on their side or back, not on the head or neck. Step five: "
            "release the headlock as they land and recover to kamae. The "
            "critical safety rule: the technique throws the body around "
            "the head; it never twists or cranks the neck. In drilling, "
            "the partner taps or the throw is walked through slowly, and "
            "any neck discomfort stops the drill immediately."
        ),
        "key_points": [
            "Kubi-nage pivots the opponent's body around the controlled head; the head is the fulcrum, not the target.",
            "It is the clinch throw for stalemated belt grips: when the belt is denied, the head is the handle.",
            "The body rotates and the feet lose their base; the turn, not arm strength, throws the opponent.",
            "The fall is guided to the side or back; the opponent must never land on the head or neck.",
            "Safety governs the drill: the neck is never cranked, and any discomfort stops the practice immediately.",
        ],
        "requirements": [
            "A close clinch with the opponent's head accessible and the belt grips stalemated.",
            "A snug but safe head control: locked against the body, never a choke, never a neck crank.",
            "A trained partner and a mat; the throw is walked through slowly before any speed is added.",
        ],
        "standards": [
            "Kubi-nage is classified among the nagewaza (throwing techniques) in the official kimarite list.",
            "Training follows joint-and-neck safety practice: controlled drilling, early release, immediate stop on discomfort.",
        ],
        "citations": [CIT_KIMARITE],
        "sig_lens": (
            "The Signature read: kubi-nage is the signed fulcrum - the "
            "held head the fixed point around which the bout turns. The "
            "Signature Sumo Method treats it as the technique of the "
            "stalemate broken: when the belt is denied, sign the pivot "
            "around what remains, and sign it with care."
        ),
    },
    {
        "key": "sotogake",
        "name": "Sotogake: The Outer Leg Trip",
        "group": "Leg Trips",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Sotogake is the outer leg trip: the wrestler hooks their leg "
            "around the outside of the opponent's leg and sweeps or "
            "reaps it, toppling the opponent while driving or twisting "
            "their upper body. The leg hook removes the opponent's base "
            "on one side at exactly the moment the upper-body technique "
            "pushes their weight onto that side - the combination is what "
            "makes the trip work, because a leg hook alone against a "
            "balanced opponent just gets stepped out of. Sotogake is "
            "classified among the kakewaza (tripping techniques), and it "
            "is the first leg trip most wrestlers learn, often paired "
            "with a push or a twist. The hooking leg stays bent and "
            "controlled; a wild straight-legged kick is a foul risk and a "
            "balance risk."
        ),
        "how_it_works": (
            "Step one: engage the opponent's upper body with a push, grip, "
            "or twist, committing their weight onto the leg you intend to "
            "hook. Step two: swing your leg around the outside of their "
            "leg, hooking your calf or ankle behind their calf or ankle - "
            "the hook is a cradle, not a kick. Step three: at the same "
            "instant, drive or twist their upper body toward the hooked "
            "side, so their weight falls onto the leg that is being "
            "removed. Step four: reap the hooked leg through, sweeping it "
            "out from under them as their upper body goes over. Step five: "
            "stay balanced on your supporting leg through the reap and "
            "recover to kamae as they touch down. Timing is the whole "
            "technique: hook while their weight is on the leg, and finish "
            "the upper-body drive in the same beat. Hook a leg with no "
            "weight on it and the opponent simply steps free and counters."
        ),
        "key_points": [
            "Sotogake hooks the outside of the opponent's leg and reaps it while the upper body drives their weight onto it.",
            "The trip needs the opponent's weight on the hooked leg; an unweighted hook is stepped out of.",
            "Upper-body technique and leg hook land in the same beat; the combination is the technique.",
            "The hooking leg is bent and controlled; wild straight-legged kicks are fouls and balance risks.",
            "The attacker stays balanced on the supporting leg through the reap.",
        ],
        "requirements": [
            "An upper-body engagement (push, grip, or twist) that commits the opponent's weight to one leg.",
            "The timing to hook exactly as the weight lands; drilled first in slow motion with a partner.",
            "A bent, controlled hooking leg; kicking at the opponent's leg is prohibited.",
        ],
        "standards": [
            "Sotogake is classified among the kakewaza (tripping techniques) in the official kimarite list.",
            "Leg techniques hook and reap; striking or kicking the opponent's legs is a foul.",
        ],
        "citations": [CIT_KIMARITE],
        "sig_lens": (
            "The Signature read: sotogake is the signed removal - the "
            "base taken out from under the weight in a single beat. The "
            "Signature Sumo Method treats it as the technique of combined "
            "action: the hands sign the direction, the leg signs the "
            "removal, and both signatures land together."
        ),
    },
    {
        "key": "uchigake",
        "name": "Uchigake: The Inner Leg Trip",
        "group": "Leg Trips",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Uchigake is the inner leg trip: instead of hooking around "
            "the outside, the wrestler's leg threads between the "
            "opponent's legs and hooks the inside of the far leg, "
            "reaping it inward while the upper body drives or twists. "
            "The inner entry is stealthier than the outer hook - the "
            "opponent feels the upper-body attack and does not see the "
            "leg coming until the base is gone. It demands closer range "
            "and finer timing than sotogake, because the hooking leg "
            "must travel between the opponent's legs without getting "
            "trapped. Uchigake is classified among the kakewaza, and it "
            "is an advanced trip precisely because the entry is "
            "dangerous: a mistimed inner hook can be caught, countered, "
            "and turned into the attacker's own fall."
        ),
        "how_it_works": (
            "Step one: close the range with an upper-body attack - a "
            "push, a pull, or a twist - that occupies the opponent's "
            "attention and commits their weight. Step two: slide your "
            "hooking leg between their legs, keeping it bent and close "
            "to your own body, and hook the inside of their far leg at "
            "the calf or ankle. Step three: in the same beat, drive or "
            "twist their upper body toward the hooked side while reaping "
            "the hooked leg inward and through. Step four: follow the "
            "reap with your body, staying upright on the supporting leg, "
            "as the opponent's base collapses inward. Step five: recover "
            "to kamae as they touch down, watching for the counter - a "
            "failed uchigake often leaves the attacker's leg caught, and "
            "the recovery must be immediate. The entry must be quick and "
            "the leg must stay bent; a straight leg threaded between the "
            "opponent's legs is easily trapped."
        ),
        "key_points": [
            "Uchigake hooks the inside of the far leg, entering between the opponent's legs for a stealthier trip.",
            "The inner entry demands closer range and finer timing than the outer hook.",
            "The hooking leg stays bent and close; a straight leg threaded through is easily trapped and countered.",
            "Upper-body attack and inner reap land in the same beat, as with all leg trips.",
            "A failed uchigake leaves the attacker's leg caught; the recovery must be immediate.",
        ],
        "requirements": [
            "Close range and an upper-body attack that occupies the opponent while the leg enters.",
            "The speed and precision to thread the hooking leg between the opponent's legs without it being caught.",
            "Drilling at slow speed first; the inner entry is only attempted live after the mechanics are clean.",
        ],
        "standards": [
            "Uchigake is classified among the kakewaza (tripping techniques) in the official kimarite list.",
            "Leg techniques hook and reap; striking or kicking the opponent's legs is a foul.",
        ],
        "citations": [CIT_KIMARITE],
        "sig_lens": (
            "The Signature read: uchigake is the signed inside line - the "
            "trip that enters where the opponent is not looking. The "
            "Signature Sumo Method treats it as the advanced lesson of "
            "the leg trips: the bolder the entry, the cleaner the "
            "mechanics must be, because the inside line punishes sloppiness."
        ),
    },
    {
        "key": "kirikaeshi",
        "name": "Kirikaeshi: The Twisting Knee Trip",
        "group": "Leg Trips",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Kirikaeshi is the twisting knee trip: the wrestler twists "
            "the opponent's body while sweeping or blocking at the knee, "
            "so the upper body turns one way and the leg is stopped the "
            "other way, and the opponent spirals down. The technique "
            "combines a sharp body twist - usually from a belt grip or an "
            "arm control - with a leg action at the knee that prevents the "
            "opponent's base from following the twist. It is one of the "
            "most visually dramatic kimarite: the opponent corkscrews to "
            "the clay. Kirikaeshi is classified among the kakewaza, and it "
            "sits at the advanced tier because the twist and the leg "
            "block must be perfectly synchronized - the twist without the "
            "block just turns the opponent, and the block without the "
            "twist just trips a step."
        ),
        "how_it_works": (
            "Step one: secure upper-body control - a belt grip, an arm "
            "lock, or a tight clinch - that lets you twist the "
            "opponent's torso. Step two: begin the sharp twist, rotating "
            "their upper body hard to one side with your hips and arms. "
            "Step three: in the same instant, sweep or block at their knee "
            "or lower leg on the side of the twist, stopping their base "
            "from following the rotation. Step four: the opposing forces "
            "- torso turning, leg stopped - spiral the opponent down to "
            "the clay; guide the fall so they land on their side. Step "
            "five: stay on your feet through the spiral and recover to "
            "kamae. The synchronization is everything: the leg action "
            "must land exactly as the twist peaks. Drill it slowly with a "
            "partner who knows the fall, because the spiral lands hard "
            "and the knee contact must be a sweep or block, never a "
            "strike."
        ),
        "key_points": [
            "Kirikaeshi twists the torso one way while stopping the leg the other way; the opposition spirals the opponent down.",
            "The twist and the leg block must synchronize exactly; either one alone fails.",
            "Upper-body control (belt grip, arm control, or tight clinch) is the prerequisite for the twist.",
            "The leg action is a sweep or block at the knee, never a strike.",
            "The fall is guided to the side; the spiral lands hard and is drilled slowly with a trained partner.",
        ],
        "requirements": [
            "Secure upper-body control that can rotate the opponent's torso sharply.",
            "The timing to land the knee block exactly at the peak of the twist.",
            "A trained partner and mats for drilling; the spiral throw is walked through before any speed.",
        ],
        "standards": [
            "Kirikaeshi is classified among the kakewaza (tripping techniques) in the official kimarite list.",
            "Leg contact is a sweep or block; striking the knee or leg is prohibited.",
        ],
        "citations": [CIT_KIMARITE],
        "sig_lens": (
            "The Signature read: kirikaeshi is the signed spiral - two "
            "opposite signatures, torso one way and leg the other, meeting "
            "in the fall. The Signature Sumo Method treats it as the "
            "technique of opposition harnessed: turn and stop, signed in "
            "the same instant, and the spiral writes itself."
        ),
    },
    {
        "key": "watashikomi",
        "name": "Watashikomi: The Thigh-Grabbing Push Down",
        "group": "Leg Trips",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Watashikomi is the thigh-grabbing push down: the wrestler "
            "grabs the opponent's thigh or the inside of the leg with one "
            "hand while pushing their upper body down and forward with "
            "the other, folding them to the clay. The thigh grip gives "
            "control of the opponent's base directly - lifting or "
            "blocking the leg while the upper body is driven down leaves "
            "the opponent with no post to catch themselves. It is an "
            "unusual and advanced kimarite, rarely seen, because securing "
            "a thigh grip against a resisting wrestler demands deep "
            "penetration and perfect timing. Watashikomi is classified "
            "among the kakewaza, and it rewards the wrestler who fights "
            "low: the lower you are, the closer the thigh grip, and the "
            "more natural the folding finish."
        ),
        "how_it_works": (
            "Step one: penetrate low - drop under the opponent's upper-"
            "body defense and secure a grip on their thigh or the inside "
            "of their leg with one hand, fingers firm. Step two: with the "
            "other hand, press or push their upper body - shoulder, chest, "
            "or head - down and forward. Step three: combine the two "
            "actions: lift or block the gripped leg while driving the "
            "upper body down, folding the opponent at the waist. Step "
            "four: follow the fold to the clay, keeping the thigh grip "
            "until the opponent's body (other than the soles) touches. "
            "Step five: release the leg grip as they land and recover to "
            "kamae on your feet. The penetration is the hard part: "
            "reaching for the thigh from too high gets the arm trapped, "
            "and the grip must be secured before the push begins, or the "
            "opponent simply steps back out of range."
        ),
        "key_points": [
            "Watashikomi grips the thigh or inner leg with one hand while the other hand drives the upper body down.",
            "Controlling the leg directly removes the opponent's post; the fold leaves them nothing to catch themselves with.",
            "Deep low penetration is the prerequisite; reaching from high gets the arm trapped.",
            "The grip must be secured before the push begins, or the opponent steps out of range.",
            "The wrestler who fights lowest finds the thigh grip most naturally.",
        ],
        "requirements": [
            "The ability to penetrate low under the opponent's upper-body defense.",
            "A firm grip on the thigh or inner leg, secured before the upper-body drive starts.",
            "Drilling with a cooperative partner; the folding finish is practiced slowly first.",
        ],
        "standards": [
            "Watashikomi is classified among the kakewaza (tripping techniques) in the official kimarite list.",
            "Grips on the leg are legal; the finish must not involve striking.",
        ],
        "citations": [CIT_KIMARITE],
        "sig_lens": (
            "The Signature read: watashikomi is the signed fold - the leg "
            "held, the upper body pressed, the opponent folded like a "
            "signed page. The Signature Sumo Method treats it as the "
            "reward of fighting low: drop beneath the defense, take hold "
            "of the base itself, and sign the fold."
        ),
    },
]
ENTRIES += [
    {
        "key": "yorikiri",
        "name": "Yori-Kiri: The Force Out",
        "group": "Force-Out Techniques",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Yori-kiri is the force out: from the belt grip, the wrestler "
            "walks the opponent out of the ring with relentless "
            "chest-to-chest pressure, the classic technique of the belt-"
            "fighting yotsu wrestler. Both wrestlers are locked on the "
            "mawashi, bodies pressed together, and the attacker simply "
            "out-drives the defender - step by step, refusing to be "
            "stopped, turning the bout into a contest of legs, lungs, and "
            "will. It is the most grinding of the kimarite: no flash, no "
            "trick, just the slow march to the edge. Yori-kiri is "
            "classified among the kihonwaza, and it is the technique that "
            "separates the strong from the merely skilled - the wrestler "
            "who can force out a resisting opponent from the belt has "
            "mastered the foundation of all sumo."
        ),
        "how_it_works": (
            "Step one: secure the belt grip - your favored yotsu, inside "
            "hand deep - and pull the opponent's body tight against yours "
            "with no space between. Step two: drop the hips low and begin "
            "driving forward with short powerful steps, keeping the chest "
            "pressed into the opponent so every step moves them. Step "
            "three: maintain the march - the defender will try to circle, "
            "drop weight, or twist free, and each attempt is answered with "
            "steady forward pressure, never a pause. Step four: as the "
            "tawara nears, shorten the steps and increase the drive, "
            "finishing with a final surge that carries the opponent out. "
            "Step five: stop your own momentum at the edge - the most "
            "humiliating loss in sumo is forcing the opponent out and "
            "stumbling out after them. The keys are the locked grip, the "
            "low hips, and inexhaustible legs: yori-kiri is won in the "
            "third and fourth steps, when the defender's legs start to "
            "fail and the attacker's do not."
        ),
        "key_points": [
            "Yori-kiri is the belt-grip force out: chest-to-chest, locked on the mawashi, marching the opponent out step by step.",
            "It is a contest of legs, lungs, and will; the wrestler whose drive outlasts the defense wins.",
            "The bodies stay pressed together with no space; space is where the defender escapes.",
            "The defender's counters - circling, dropping weight, twisting - are all answered with steady forward pressure.",
            "The attacker must stop at the edge; following the opponent out after them loses the bout.",
        ],
        "requirements": [
            "A secured belt grip (favored yotsu) held tight through the entire march.",
            "The leg endurance for a sustained drive, built through butsukari-geiko and stance work.",
            "The balance and awareness to halt at the tawara after the final surge.",
        ],
        "standards": [
            "Yori-kiri is classified among the kihonwaza (fundamental techniques) in the official kimarite list.",
            "The bout is won when the opponent steps outside the tawara; order of exit decides close finishes.",
        ],
        "citations": [CIT_KIMARITE, CIT_DOHYO],
        "sig_lens": (
            "The Signature read: yori-kiri is the signed march - no trick, "
            "no flash, just the unbroken line of forward pressure. The "
            "Signature Sumo Method treats it as the technique of "
            "outlasting: lock on, stay low, keep stepping, and let the "
            "signature be the distance covered."
        ),
    },
    {
        "key": "yoritaoshi",
        "name": "Yori-Taoshi: The Force Out and Down",
        "group": "Force-Out Techniques",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Yori-taoshi is the force out and down: the belt-grip drive "
            "of yori-kiri, finished by crushing the opponent down to the "
            "clay instead of marching them out. As the defender resists "
            "the forward march - dropping their weight, bracing their "
            "legs, refusing to step back - the attacker changes the "
            "vector, driving down through the locked grip and folding "
            "the opponent to the ground. It is the answer to the "
            "immovable defender: if they will not go back, they will go "
            "down. Yori-taoshi is classified among the kihonwaza, and it "
            "completes the yotsu wrestler's education - the force out "
            "marches them to the edge, the force out and down drops them "
            "where they stand."
        ),
        "how_it_works": (
            "Step one: establish the belt-grip drive exactly as for "
            "yori-kiri - locked yotsu, bodies tight, hips low, marching "
            "forward. Step two: read the resistance; yori-taoshi is on "
            "when the defender has braced hard against the drive, weight "
            "dropped, legs set, refusing to retreat. Step three: change "
            "the vector - instead of driving horizontally, drop your own "
            "weight and drive down through the grip, pressing the "
            "opponent's upper body toward the clay. Step four: keep the "
            "belt grip locked through the descent, following the "
            "opponent down just far enough to complete the technique. "
            "Step five: the instant any part of the opponent besides the "
            "soles touches, the bout is over; release the drive and "
            "recover to kamae on your feet. The danger is mistiming the "
            "vector change: shifting down too early lets the braced "
            "defender shove you back, and the attacker must be ready to "
            "return to the horizontal march if the downward finish is "
            "not there."
        ),
        "key_points": [
            "Yori-taoshi is the belt-grip drive finished downward: the braced defender who will not retreat is folded to the clay.",
            "It answers the immovable defense; the vector change punishes the dropped weight.",
            "The setup is identical to yori-kiri; only the finishing vector changes.",
            "The belt grip stays locked through the descent to control the fall.",
            "Mistiming the shift lets the defender shove back; the attacker must be ready to resume the march.",
        ],
        "requirements": [
            "A working belt-grip drive (yori-kiri mechanics) as the entry.",
            "A defender braced hard against the march, weight dropped and refusing to step back.",
            "The judgment to change vectors at the right instant and the control to stay on the feet.",
        ],
        "standards": [
            "Yori-taoshi is classified among the kihonwaza (fundamental techniques) in the official kimarite list.",
            "The bout ends when any part of the opponent besides the soles touches the clay.",
        ],
        "citations": [CIT_KIMARITE, CIT_DOHYO],
        "sig_lens": (
            "The Signature read: yori-taoshi is the signed answer to the "
            "immovable - the march that becomes the descent. The "
            "Signature Sumo Method treats the braced defender as a wall "
            "that has signed its own position: drive down through it, and "
            "the wall becomes the floor."
        ),
    },
    {
        "key": "uwatedashinage",
        "name": "Uwatedashi-Nage: The Pulling Overarm Throw",
        "group": "Advanced Throws",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Uwatedashi-nage is the pulling overarm throw: the overarm "
            "belt grip of uwate-nage, but instead of wheeling the "
            "opponent around the body, the attacker pulls them sharply "
            "forward and down over the hip. The overarm hand yanks the "
            "belt toward and past the attacker's own body while the hips "
            "block and turn, sending the opponent tumbling over the "
            "leading hip to the clay. It is the close-quarters, "
            "pulling variant of the great overarm throw - less arc, more "
            "snap, the opponent folded over the hip rather than wheeled "
            "around it. Uwatedashi-nage is classified among the nagewaza, "
            "and it is the advanced answer to the opponent who defends "
            "the standard overarm wheel by staying tight: pull them over "
            "instead of around."
        ),
        "how_it_works": (
            "Step one: secure the deep overarm (uwate) grip on the "
            "mawashi, exactly as for uwate-nage. Step two: pull the "
            "opponent tight and set the near hip as the block, dropping "
            "low. Step three: instead of turning for the wheel, yank the "
            "overarm sharply down and across your own body, pulling the "
            "opponent's weight forward over your blocking hip. Step four: "
            "turn the hips into the pull, folding the opponent over the "
            "hip and down to the clay in front. Step five: stay on your "
            "feet through the snap, release the grip as they land, and "
            "recover to kamae. The pull must be sudden and the hip must "
            "be set - a slow pull lets the opponent step around, and a "
            "high hip lets them stay upright. The technique is chosen "
            "when the opponent crowds in to deny the wheeling arc; the "
            "pulling variant needs that closeness."
        ),
        "key_points": [
            "Uwatedashi-nage pulls the overarm grip down and across, folding the opponent over the attacker's hip.",
            "It is the pulling variant of uwate-nage: less arc, more snap, used when the opponent crowds in.",
            "The near hip is set as the block; the opponent's weight is yanked forward over it.",
            "The pull is sudden; a slow pull lets the opponent step around the hip.",
            "The deep overarm grip is the prerequisite; without it there is nothing to pull with.",
        ],
        "requirements": [
            "A deep overarm (uwate) grip on the mawashi, secured in the grip fight.",
            "A close, crowding opponent; the pulling variant needs the tight range.",
            "The hip set and the sudden pull coordinated in one beat; drilled slowly first.",
        ],
        "standards": [
            "Uwatedashi-nage is classified among the nagewaza (throwing techniques) in the official kimarite list.",
            "The throw is completed over the hip with the attacker remaining on the feet.",
        ],
        "citations": [CIT_KIMARITE],
        "sig_lens": (
            "The Signature read: uwatedashi-nage is the signed snap - the "
            "great arc folded into a single sharp pull over the hip. The "
            "Signature Sumo Method treats it as the technique of "
            "closeness used: when the opponent crowds to deny the wheel, "
            "sign the shorter line and fold them over it."
        ),
    },
    {
        "key": "shitatedashinage",
        "name": "Shitatedashi-Nage: The Pulling Underarm Throw",
        "group": "Advanced Throws",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Shitatedashi-nage is the pulling underarm throw: the inside "
            "belt grip of shitate-nage, finished with a sharp forward "
            "pull instead of the lifting pivot. The inside hand yanks the "
            "mawashi down and across while the attacker's body turns and "
            "drops, dragging the opponent forward and down over the "
            "leading side. Where shitate-nage lifts the opponent up and "
            "over the inside hand, the pulling variant drags them down "
            "and past it - quicker, lower, and harder to escape once the "
            "pull starts. Shitatedashi-nage is classified among the "
            "nagewaza, and it is the inside-grip wrestler's snap finish: "
            "the same prized hand position, the same sudden commitment, "
            "but the opponent goes down in front instead of over the "
            "top."
        ),
        "how_it_works": (
            "Step one: win and hold the inside (shitate) grip, threaded "
            "under the opponent's arm and deep on the front of the "
            "mawashi. Step two: pull the opponent tight and drop the "
            "hips, loading for the pull rather than the lift. Step three: "
            "yank the inside hand sharply down and across your body while "
            "turning and dropping your weight, dragging the opponent's "
            "center forward and down past your leading side. Step four: "
            "continue the pull through their fall, guiding them to the "
            "clay in front of you. Step five: stay on your feet, release "
            "as they land, and recover to kamae. The pull must be "
            "explosive and the body must drop with it - pulling from a "
            "high stance just drags the attacker forward. The inside grip "
            "must hold through the snap; if it slips, the pull becomes a "
            "stumble. Choose the pulling variant when the opponent is "
            "heavy on their feet and hard to lift; drag them instead."
        ),
        "key_points": [
            "Shitatedashi-nage yanks the inside grip down and across, dragging the opponent down in front.",
            "It is the pulling variant of shitate-nage: quicker and lower than the lifting pivot.",
            "The attacker's body drops with the pull; pulling from high drags the attacker forward instead.",
            "The inside grip must hold through the snap; the throw dies if the hand slips.",
            "It is chosen when the opponent is too heavy to lift; drag what cannot be lifted.",
        ],
        "requirements": [
            "The inside (shitate) grip won and held deep on the front of the mawashi.",
            "An explosive pull coordinated with a full body drop.",
            "The judgment to choose the drag over the lift against heavy, well-based opponents.",
        ],
        "standards": [
            "Shitatedashi-nage is classified among the nagewaza (throwing techniques) in the official kimarite list.",
            "The throw finishes with the opponent down in front and the attacker on the feet.",
        ],
        "citations": [CIT_KIMARITE],
        "sig_lens": (
            "The Signature read: shitatedashi-nage is the signed drag - "
            "the prized inside hand signing downward instead of lifting. "
            "The Signature Sumo Method treats it as the pragmatist's "
            "finish: what cannot be lifted can be dragged, and the "
            "signature is the same hand either way."
        ),
    },
    {
        "key": "katasukashi",
        "name": "Katasukashi: The Under-Shoulder Swing Down",
        "group": "Advanced Throws",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Katasukashi is the under-shoulder swing down: as the "
            "opponent pushes or reaches over the attacker's shoulder, "
            "the attacker ducks under the arm, swings it down and across "
            "the body, and drops the opponent forward to the clay. The "
            "technique turns the opponent's own reaching arm into the "
            "handle of their fall - they extend over the shoulder, and "
            "the attacker simply removes the support beneath while "
            "swinging the arm down. It is one of the most elegant "
            "kimarite, a pure redirection that needs almost no strength "
            "once the timing is right. Katasukashi is classified among "
            "the hineriwaza (twisting techniques), and it is the advanced "
            "lesson in letting the opponent supply everything: the "
            "reach, the weight, and the fall."
        ),
        "how_it_works": (
            "Step one: invite or await the opponent's overreaching push - "
            "their arm extending over your shoulder or across your upper "
            "back. Step two: at the moment of their commitment, duck "
            "slightly and slip your shoulder under their arm, taking "
            "control of the arm at the wrist or forearm. Step three: "
            "swing their arm down and across your body in a sharp arc "
            "while dropping your own weight, removing the support their "
            "push was leaning on. Step four: guide their falling upper "
            "body down to the clay in front of you, following just far "
            "enough to complete the technique. Step five: release the "
            "arm as they land and recover to kamae on your feet. The "
            "duck must be timed to their commitment - too early and "
            "they pull the arm back, too late and their weight runs over "
            "you. The swing is down and across, never up; lifting the "
            "arm gives the opponent their balance back."
        ),
        "key_points": [
            "Katasukashi ducks under the opponent's reaching arm and swings it down and across, dropping them forward.",
            "The opponent's own reach becomes the handle of their fall; the technique needs their commitment.",
            "The duck is timed to the commitment: early lets them retract, late lets them run over you.",
            "The swing is down and across, never up; lifting returns their balance.",
            "It is the purest redirection in the kimarite: almost no strength required once the timing is right.",
        ],
        "requirements": [
            "An opponent reaching or pushing over the shoulder; the technique cannot be forced without the reach.",
            "The timing to duck under exactly as the weight commits.",
            "Arm control at the wrist or forearm through the swing, released as the opponent lands.",
        ],
        "standards": [
            "Katasukashi is classified among the hineriwaza (twisting techniques) in the official kimarite list.",
            "The technique redirects the opponent's arm and weight; striking is not part of it.",
        ],
        "citations": [CIT_KIMARITE],
        "sig_lens": (
            "The Signature read: katasukashi is the signed disappearance "
            "- the support removed, the reach swung down, the opponent "
            "falling through where the wrestler was. The Signature Sumo "
            "Method treats it as the ultimate economy: let them supply "
            "the reach, the weight, and the fall, and sign only the "
            "redirection."
        ),
    },
    {
        "key": "utchari",
        "name": "Utchari: The Ring Edge Throw",
        "group": "Advanced Throws",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Utchari is the ring edge throw: the legendary last-instant "
            "reversal, thrown when the wrestler is at the very edge of "
            "the ring, heels at the straw, apparently beaten. As the "
            "opponent drives in for the finish, the wrestler pivots on "
            "the edge, twists the body, and throws the attacker past and "
            "down - winning from the brink. It is the most dramatic "
            "kimarite in sumo, the throw that brings the crowd to its "
            "feet, and it demands total commitment: the pivot, the "
            "twist, and the throw must happen in a single motion at the "
            "exact edge, because there is no second chance and no room "
            "for a step. Utchari is classified among the nagewaza, and "
            "every wrestler drills it for the day they need it - the day "
            "the bout is lost everywhere except in the throw."
        ),
        "how_it_works": (
            "Step one: at the ring's edge, heels near or on the tawara, "
            "absorb the opponent's final drive without stepping out - "
            "the feet must hold the edge. Step two: as the opponent "
            "commits their weight into the finishing push, pivot on the "
            "balls of the feet, turning the body sideways along the "
            "edge. Step three: in the same motion, grip or hook the "
            "opponent's body - belt, arm, or torso - and twist violently, "
            "throwing their committed weight past you and down. Step "
            "four: let their momentum carry them out or down while you "
            "complete the pivot and stay inside the ring. Step five: "
            "recover to kamae - the bout is yours the instant they touch "
            "down or step out first. The margin is measured in "
            "centimeters: pivot too shallow and you step out; throw too "
            "late and they drive you out; hesitate and the moment is "
            "gone. Utchari is drilled at the edge with a trusted partner, "
            "at increasing speed, until the pivot-throw is a single "
            "reflex."
        ),
        "key_points": [
            "Utchari is the last-instant reversal at the ring's edge: pivot, twist, and throw the finisher past you.",
            "The feet must hold the edge; the technique is won or lost in centimeters at the tawara.",
            "The opponent's committed finishing drive supplies the throwing force; the pivot redirects it.",
            "Pivot, twist, and throw are a single motion - hesitation or staging loses the instant.",
            "It is drilled at the edge with a trusted partner until the reversal is a single reflex.",
        ],
        "requirements": [
            "Position at the ring's edge with the feet able to pivot without stepping out.",
            "An opponent fully committed to the finishing drive; the throw needs their momentum.",
            "A trusted drilling partner and a safe edge; the full-speed reversal is only attempted live after slow mastery.",
        ],
        "standards": [
            "Utchari is classified among the nagewaza (throwing techniques) in the official kimarite list.",
            "The bout is decided by who touches down or steps out first; the edge pivot must keep the thrower inside.",
        ],
        "citations": [CIT_KIMARITE, CIT_DOHYO],
        "sig_lens": (
            "The Signature read: utchari is the signed reversal - defeat "
            "at the edge, signed over into victory in a single pivot. The "
            "Signature Sumo Method treats the brink as the finest place to "
            "sign: nowhere to step, no time to think, only the pivot, the "
            "twist, and the throw."
        ),
    },
    {
        "key": "tsuriotoshi",
        "name": "Tsuri-Otoshi: The Lifting Body Drop",
        "group": "Advanced Throws",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Tsuri-otoshi is the lifting body drop: the wrestler grips "
            "the opponent's mawashi with both hands, lifts their entire "
            "body clear off the clay, and drops them. It is the ultimate "
            "demonstration of sumo strength - the opponent, all hundred-"
            "plus kilograms of them, hoisted into the air and set down "
            "hard. The lift comes from the legs with the back straight, "
            "the opponent's weight hanging from the belt grips, and the "
            "drop is guided so they land on the clay while the lifter "
            "stays on the feet. Tsuri-otoshi is classified among the "
            "soritewaza (lifting techniques), and it is vanishingly rare "
            "in top-division sumo, because lifting a resisting elite "
            "wrestler requires extraordinary power - which is exactly why "
            "the crowd roars when it happens."
        ),
        "how_it_works": (
            "Step one: secure a two-handed grip on the opponent's mawashi, "
            "deep and even, front or sides. Step two: drop the hips well "
            "below the opponent's center of gravity and pull their body "
            "tight against yours. Step three: drive up explosively with "
            "the legs - back straight, head up - lifting the opponent's "
            "feet clear off the clay; their weight hangs from your grips. "
            "Step four: at the top of the lift, guide their body down to "
            "the clay in front or to the side, controlling the descent so "
            "they land on their side or back. Step five: stay on your "
            "feet through the drop, release the grips as they land, and "
            "recover to kamae. The lift must be decisive: a half-lift "
            "leaves a heavy opponent draped on you, which is the worst "
            "position in sumo. This is a strength technique for the "
            "exceptionally powerful, drilled with lighter partners and "
            "never attempted beyond the lifter's proven capacity."
        ),
        "key_points": [
            "Tsuri-otoshi lifts the opponent's whole body off the clay with a two-handed belt grip and drops them.",
            "The lift is leg-driven with a straight back; the opponent's weight hangs from the grips.",
            "Hips must drop well below the opponent's center before the explosive drive up.",
            "A half-lift is catastrophic: the technique demands decisive, proven lifting power.",
            "It is among the rarest kimarite at the elite level, which is why it electrifies the crowd.",
        ],
        "requirements": [
            "Extraordinary leg and back strength, proven in training before any live attempt.",
            "A deep, even two-handed grip on the mawashi that will not slip under full load.",
            "Drilling with lighter partners first; the full lift is never attempted beyond proven capacity.",
        ],
        "standards": [
            "Tsuri-otoshi is classified among the soritewaza (lifting techniques) in the official kimarite list.",
            "The lifter remains on the feet; the drop is guided, never a spike.",
        ],
        "citations": [CIT_KIMARITE],
        "sig_lens": (
            "The Signature read: tsuri-otoshi is the signed lift - the "
            "whole opponent raised and set down like a signature pressed "
            "into the page. The Signature Sumo Method treats it as "
            "strength made legible: the legs sign what the arms merely "
            "hold, and the clay receives the mark."
        ),
    },
    {
        "key": "kawazugake",
        "name": "Kawazugake: The Hooking Backward Counter Throw",
        "group": "Advanced Throws",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Kawazugake is the hooking backward counter throw: as the "
            "opponent attacks, the wrestler hooks their leg around the "
            "opponent's leg from the inside, locks the upper body, and "
            "throws backward, countering the attack with a spectacular "
            "reverse fall. The technique is a counter in the purest "
            "sense - it does not initiate, it answers, turning the "
            "attacker's own forward drive into a backward throw. "
            "Kawazugake is classified among the tokushuwaza (special "
            "techniques), and it is one of the rarest kimarite ever "
            "recorded, because the timing window is a fraction of a "
            "second and the backward fall is dangerous for both "
            "wrestlers. It is drilled only by advanced practitioners with "
            "full safety awareness, and in competition it appears once in "
            "a generation - which is why every occurrence is remembered."
        ),
        "how_it_works": (
            "Step one: as the opponent commits to a forward attack - a "
            "drive, a push, a throw entry - hold your ground and let "
            "their weight come to you. Step two: in the instant of their "
            "commitment, hook your leg around the inside of their leg, "
            "locking the lower bodies together. Step three: lock your "
            "upper body against theirs - chest to chest, arms controlling "
            "- so the two bodies move as one. Step four: throw your own "
            "weight backward, using the hooked leg as the pivot, carrying "
            "the opponent over and down behind you. Step five: control "
            "the backward fall absolutely - tuck the chin, guide the "
            "opponent's landing, and be prepared for the hard landing "
            "yourself. The timing is everything and the margin is nil: "
            "hook too early and they adjust, too late and they run "
            "through. Because both wrestlers fall backward, the technique "
            "is practiced only with expert partners, full mats, and a "
            "coach watching."
        ),
        "key_points": [
            "Kawazugake is the purest counter: hook the inside leg, lock the bodies, and throw backward off the attacker's drive.",
            "It answers rather than initiates; without the opponent's committed attack there is nothing to counter.",
            "The timing window is a fraction of a second; early or late both fail.",
            "Both wrestlers fall backward, so fall control and mats are non-negotiable.",
            "It is among the rarest kimarite ever recorded; every competitive occurrence is remembered.",
        ],
        "requirements": [
            "An opponent fully committed to a forward attack; the counter needs their drive.",
            "Advanced timing and the courage to throw backward off a live attack.",
            "Expert drilling partners, full mats, and coaching supervision; never practiced casually.",
        ],
        "standards": [
            "Kawazugake is classified among the tokushuwaza (special techniques) in the official kimarite list.",
            "Training follows strict safety practice: expert partners, mats, supervision, and absolute fall control.",
        ],
        "citations": [CIT_KIMARITE],
        "sig_lens": (
            "The Signature read: kawazugake is the signed answer - the "
            "attack received, hooked, and signed backward. The Signature "
            "Sumo Method treats it as the rarest signature of all: written "
            "in a fraction of a second, off the opponent's own ink, and "
            "remembered for a generation."
        ),
    },
    {
        "key": "izori",
        "name": "Izori: The Backward Body Drop",
        "group": "Advanced Throws",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Izori is the backward body drop: the wrestler ducks under "
            "the opponent's attack, gets the head and shoulders beneath "
            "their center, and throws them backward over the body to the "
            "clay behind. The attacker disappears under the opponent's "
            "drive and reappears as the fulcrum of their fall - the "
            "opponent charges forward and finds the ground coming up to "
            "meet them from below. Izori is classified among the "
            "tokushuwaza (special techniques), and like kawazugake it is "
            "vanishingly rare, demanding perfect depth, perfect timing, "
            "and the nerve to go under a charging wrestler. It is the "
            "final record of this database because it is the final lesson "
            "of sumo technique: the lowest wrestler, at the perfect "
            "instant, can move anyone."
        ),
        "how_it_works": (
            "Step one: as the opponent drives forward, drop lower than "
            "their center - deep kamae, head up, eyes on the target. Step "
            "two: penetrate under their upper body, getting your head "
            "and shoulders beneath their chest or armpits. Step three: "
            "lock on - arms around the torso or belt - and set your body "
            "as the fulcrum. Step four: in one motion, extend the legs "
            "and arch back, throwing the opponent's committed weight up "
            "and over backward behind you. Step five: control the "
            "backward throw absolutely, guiding them to land on their "
            "back on the clay while you stay low and balanced. The "
            "penetration must be deep and the timing exact: going under "
            "too shallow leaves you crushed under the drive, and the "
            "throw must be committed totally once started. Drilled only "
            "by advanced wrestlers with expert partners and full safety "
            "measures, walked through slowly long before any speed."
        ),
        "key_points": [
            "Izori ducks under the opponent's drive and throws them backward over the body.",
            "The wrestler becomes the fulcrum: head and shoulders set beneath the opponent's center.",
            "Depth and timing must be perfect; shallow penetration gets crushed under the drive.",
            "The throw is committed totally once started; there is no halfway in going under.",
            "It is the final lesson: the lowest wrestler, at the perfect instant, can move anyone.",
        ],
        "requirements": [
            "A driving, forward-committed opponent; the technique needs their momentum to throw.",
            "The depth to get fully under a charging wrestler's center and the nerve to do it.",
            "Advanced drilling only: expert partners, walked through slowly, full safety measures.",
        ],
        "standards": [
            "Izori is classified among the tokushuwaza (special techniques) in the official kimarite list.",
            "Training follows strict safety practice: advanced practitioners only, expert partners, controlled drilling.",
        ],
        "citations": [CIT_KIMARITE],
        "sig_lens": (
            "The Signature read: izori is the signed depth - the wrestler "
            "who goes lowest signs the greatest throw. The Signature Sumo "
            "Method closes the ladder here: from the stance to the "
            "backward body drop, every technique was balance taken and "
            "balance kept, and the deepest signature moves anyone."
        ),
    },
]
