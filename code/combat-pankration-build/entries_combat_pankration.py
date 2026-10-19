#!/usr/bin/env python3
"""Entries for the Pankration Combat Database (combat batch 3, 2026-10-17).

Combat orders 2026-10-17, combat batch 3. Ancient Greek pankration: the
all-force art (pan = all, kratos = force), from its Olympic debut in
648 BC through technique (striking from pygme, wrestling from pale) to
the modern revival. Each record is a technique with HOW TO DO IT
(step-by-step body mechanics), ladder-ordered from foundations to
advanced.

34 public records (public-harvest: real, fact-checked pankration
knowledge; standard references: Philostratus Gymnasticus; Pausanias
Description of Greece; Diodorus Siculus Library of History; Miller S.G.
Arete; Poliakoff M.B. Combat Sports in the Ancient World; Gardiner E.N.
Athletics of the Ancient World; World Pankration Athlima Federation
competition rules) + 34 Signature records (his original Signature Combat
Method: every technique a covenant of discipline, the all-force fighter
the armory of the Signature system, pan and kratos the two pillars of
the oath, training the forge and the bout the proof; src signature,
titles suffixed " (Signature Edition)", never presented as authentic
public record).

Ladder: ranks 1-3 foundations -> ranks 4-7 compounded -> ranks 8-10
advanced. The shard index is written in ladder order.

ID prefixes: JAH-CBPK- (public) and JAH-CBPKS- (signature), verified
free in the manifest and in every shard index (zero hits), and the
combat-pankration slugs are absent from the manifest.

Dedupe 2026-10-17: all 68 titles checked against the WHOLE system via
code/dedupe_gate.py before authoring: zero collisions, zero refusals.

Numerical cores: hand-computed 2026-10-17, machine-verified by the demos
(see demos_combat_pankration.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Civilian martial-arts instruction only. Nothing hate-adjacent, profane,
or inappropriate; no religious talk. Nothing on neutralizing or defeating
military or defense-grade systems. Never the words "bat belt" anywhere.
No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Combat Method: "
            "every technique a covenant of discipline, the all-force "
            "fighter the armory of the Signature system, pan (all) and "
            "kratos (force) the two pillars of the oath, training the "
            "forge and the bout the proof. Clearly labeled Signature-made, "
            "never presented as authentic public record.")

CIT_PHILOSTRATUS = ("Philostratus. Gymnasticus (On Athletic Training), "
                    "c. 3rd century AD; treats pankration training, the "
                    "klimax hold, and the pankratiast's preparation.")
CIT_PAUSANIAS = ("Pausanias. Description of Greece, 2nd century AD: 5.8.1 "
                 "(pankration entered the Olympic program); 6.4.6-7 "
                 "(Sostratus of Sicyon); 6.5.1-9 (Polydamas); 8.40.1-2 "
                 "(Arrhichion of Phigalia).")
CIT_DIODORUS = ("Diodorus Siculus. Library of History 17.100-101: the "
                "Athenian pankratiast Dioxippus defeats the armed Macedonian "
                "soldier Coragus.")
CIT_MILLER = ("Miller S.G. Arete: Greek Sports from Ancient Sources. "
              "University of California Press; 2004.")
CIT_POLIAKOFF = ("Poliakoff M.B. Combat Sports in the Ancient World: "
                 "Competition, Violence, and Culture. Yale University "
                 "Press; 1987.")
CIT_GARDINER = ("Gardiner E.N. Athletics of the Ancient World. Oxford "
                "University Press; 1930.")
CIT_WPAF = ("World Pankration Athlima Federation. Pankration Competition "
            "Rules and Technical Regulations; current edition.")

ENTRIES = [
    {
        "key": "allforce",
        "name": "Pankration: The All-Force Art",
        "group": "Origins and Rules",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Pankration is the ancient Greek art of all-force fighting: the "
            "name joins pan (all) with kratos (force, power, mastery), and "
            "the art lives up to it. It blends the two great Greek combat "
            "sports into one contest: pygme, the boxing, and pale, the "
            "wrestling. Striking with fists, feet, elbows, and knees stood "
            "beside throws, trips, joint locks, and strangles in a single "
            "bout. Pankration entered the Olympic program at Olympia in "
            "648 BC, at the 33rd Olympiad, and the boys' division was added "
            "in 200 BC. The ancient rules were famously spare: the only "
            "prohibited acts were biting and gouging the eyes. Everything "
            "else - punching, kicking, throwing, choking, locking joints - "
            "was legal. Bouts continued until one fighter submitted or "
            "could no longer continue. This record frames the whole "
            "database: every later record is one technique of the "
            "all-force art, and the ladder carries you from the first "
            "stance to the complete bout."
        ),
        "how_it_works": (
            "Think of pankration as two arts wearing one belt. Step one is "
            "the pygme half: upright stance, hands up, straight punches and "
            "kicks delivered from the feet, exactly the striking game. "
            "Step two is the pale half: the clinch, the grips, the throws, "
            "the ground struggle, exactly the wrestling game. Step three "
            "is the bridge between them - the moment a strike becomes a "
            "clinch entry, or a blocked kick becomes a catch and a throw. "
            "That bridge is what makes pankration one art instead of two. "
            "To study it, learn each half separately first (that is the "
            "foundations tier), then learn the transitions (the compounded "
            "tier), then learn to chain everything under pressure (the "
            "advanced tier). Every record in this database sits at one of "
            "those three stations."
        ),
        "key_points": [
            "The name is the curriculum: pan (all) plus kratos (force) - no legal technique is excluded except biting and eye-gouging.",
            "Pankration is pygme plus pale: the striking half and the wrestling half, studied separately and then bridged.",
            "Olympic pankration began in 648 BC at the 33rd Olympiad; the boys' event followed in 200 BC.",
            "Bouts ended by submission or incapacitation, not by points - the art rewards finishing, not fencing.",
            "Study order is fixed: stance and the two halves first, transitions second, chained pressure last.",
        ],
        "requirements": [
            "A clear mental picture of the two halves and the bridge between them.",
            "Respect for the ancient ruleset: the sparseness of the rules is the point of the art.",
            "Commitment to learn striking and wrestling together, never one at the expense of the other.",
        ],
        "standards": [
            "Pausanias 5.8.1: pankration's entry into the Olympic program.",
            "Philostratus Gymnasticus: the pankratiast as the complete athlete of boxing and wrestling.",
        ],
        "citations": [CIT_PAUSANIAS, CIT_MILLER, CIT_POLIAKOFF],
        "sig_lens": (
            "The Signature reading of the all-force art: pan and kratos "
            "are the two pillars of the Signature oath. Pan is the "
            "covenant of completeness - no technique refused, no range "
            "feared, striking and wrestling sworn as one art. Kratos is "
            "the covenant of force - every technique executed with the "
            "whole body behind it, never a half-measure. The Signature "
            "pankratiast does not choose between the fist and the throw; "
            "he swears both, and the bout is the proof of the oath."
        ),
    },
    {
        "key": "parastasis",
        "name": "Parastasis: The Pankration Stance",
        "group": "Stance and Movement",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The pankration stance, the parastasis, is the fighting posture "
            "from which both halves of the art launch. It stands more "
            "upright than a pure wrestler's crouch and more square than a "
            "pure boxer's blade, because it must serve strikes and throws "
            "at once. The feet sit about shoulder width apart, lead foot "
            "pointing at the opponent and rear foot turned slightly out, "
            "weight balanced evenly or biased a breath toward the rear. "
            "The knees stay soft and springy, the torso leans forward just "
            "enough to guard against the clinch, the chin tucks, and the "
            "hands rise. From this one posture the fighter can punch, "
            "kick, sprawl against a takedown, or shoot for a grip. Every "
            "technique in the database returns to the stance between "
            "actions, which is why it is taught first and drilled forever."
        ),
        "how_it_works": (
            "Place your lead foot forward, toes toward the opponent, and "
            "your rear foot a comfortable step behind, toes turned out "
            "about 30 degrees. The gap between the feet is roughly one "
            "shoulder width; wider and you cannot move, narrower and you "
            "cannot balance. Bend both knees until the legs feel springy, "
            "like a coiled rope. Settle your weight evenly, or a touch "
            "more on the rear foot so the lead leg is light for kicks and "
            "checks. Lean the torso forward slightly, tuck the chin to the "
            "chest, and raise both hands. Rock gently: forward, back, "
            "side to side. If you can shift weight in any direction "
            "without a preparatory hop, the stance is correct. If you feel "
            "stuck, narrow or widen until the rocking is free."
        ),
        "key_points": [
            "The stance serves two masters: upright enough to strike, grounded enough to wrestle - neither a boxer's blade nor a wrestler's deep crouch.",
            "Soft knees are the suspension: they load strikes, absorb shots, and sprawl against takedowns.",
            "Even weight or a slight rear bias keeps the lead leg light for kicks and the base ready for either half of the art.",
            "Chin tucked and torso inclined protect the jaw and close the distance an opponent needs for the clinch.",
            "The test is movement: free rocking in every direction with no preparatory hop means the stance is right.",
        ],
        "requirements": [
            "Feet about shoulder width apart, lead foot forward, rear foot turned slightly out.",
            "Knees softly bent, weight even or slightly rear, chin tucked.",
            "Ability to step or shift in any direction without a tell or a hop.",
        ],
        "standards": [
            "Philostratus Gymnasticus: the pankratiast's balanced preparation serving both boxing and wrestling.",
            "Poliakoff, Combat Sports in the Ancient World: the upright pankration posture in vase imagery and texts.",
        ],
        "citations": [CIT_PHILOSTRATUS, CIT_POLIAKOFF, CIT_GARDINER],
        "sig_lens": (
            "The Signature reading of the stance: the covenant with the "
            "ground. The Signature pankratiast does not stand on the "
            "earth; he stands with it - feet the twin seals of the oath, "
            "soft knees its living spring. Because the stance must serve "
            "both fist and throw, it teaches the first Signature lesson "
            "of pankration: never build a posture that serves only half "
            "the fight. Every strike and every throw in this database is "
            "already loaded in the parastasis."
        ),
    },
    {
        "key": "cheires",
        "name": "Cheires: The Guard of the Hands",
        "group": "Stance and Movement",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Cheires means hands, and in pankration the hands are the "
            "first wall. The guard holds both fists at cheek height, "
            "elbows tucked to the ribs, forearms vertical like two posts. "
            "The lead hand sits slightly forward to jab, parry, and reach "
            "for the clinch; the rear hand stays home at the chin to guard "
            "the jaw and to launch the heavy cross. Because pankration "
            "allows the clinch and the takedown, the guard also watches "
            "low: the elbows pinch inward to block body shots and to jam "
            "an opponent's reaching arms. The ancient boxers wrapped their "
            "hands in himantes, leather thongs, but the pankratiast fought "
            "bare-handed, so the guard itself had to be the weapon and the "
            "shield at once."
        ),
        "how_it_works": (
            "From the stance, raise both fists to cheek height, knuckles "
            "roughly level with your cheekbones. Tuck the elbows down and "
            "in until the forearms stand vertical and the ribs are "
            "covered. Push the lead fist six inches forward of the face; "
            "keep the rear fist touching the chin. Look between and over "
            "the gloves, never through them - the eyes stay on the "
            "opponent. Breathe behind the guard and bounce it gently: it "
            "should feel like a wall that punches back. Practice the two "
            "jobs separately: first, block by lifting an elbow or turning "
            "a forearm into an incoming strike; second, extend the lead "
            "hand to touch a target, then snap it home. The guard that "
            "cannot punch is a fence; the guard that cannot block is a "
            "flag. Yours must be both."
        ),
        "key_points": [
            "Fists at cheek height, elbows tucked, forearms vertical: the wall that punches back.",
            "The lead hand works forward - jabbing, parrying, reaching for the clinch - while the rear hand guards the chin.",
            "Elbows pinch inward to cover the ribs and to jam an opponent's arms reaching for a grip.",
            "Eyes watch over the gloves, never through them; vision lost is the first defense lost.",
            "The bare-handed pankratiast has no wrapped weapon: the guard itself must strike and shield.",
        ],
        "requirements": [
            "Both fists at cheek height with elbows tucked to the ribs.",
            "Lead hand slightly forward, rear hand anchored at the chin.",
            "Eyes open over the gloves with the chin tucked behind them.",
        ],
        "standards": [
            "Gardiner, Athletics of the Ancient World: the bare-handed guard in pankration vase painting.",
            "Philostratus Gymnasticus: hand position serving both striking and grappling readiness.",
        ],
        "citations": [CIT_GARDINER, CIT_PHILOSTRATUS, CIT_POLIAKOFF],
        "sig_lens": (
            "The Signature reading of the guard: the twin posts of the "
            "oath. The lead hand is pan - reaching to all ranges, open "
            "to every technique. The rear hand is kratos - held in "
            "reserve, the stored force of the covenant. The Signature "
            "pankratiast raises his cheires the way a witness raises a "
            "hand to swear: every block a kept promise, every punch a "
            "promise delivered."
        ),
    },
    {
        "key": "footwork",
        "name": "Footwork and Measure",
        "group": "Stance and Movement",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Footwork is how the pankratiast controls measure - the "
            "distance between the two fighters. All movement starts from "
            "the stance and returns to it: the advance step brings the "
            "lead foot forward and drags the rear foot after it; the "
            "retreat reverses the order; the lateral step slides the whole "
            "base sideways. The feet never cross, because crossed feet "
            "cannot throw and cannot sprawl. Good measure keeps the "
            "fighter exactly one strike or one grip away: close enough to "
            "attack, far enough that the opponent must take a step to "
            "reach. The ancient pankratiasts fought in the skamma, the "
            "sand pit, where every step had to be deliberate - loose "
            "footwork in sand is lost footwork."
        ),
        "how_it_works": (
            "To advance, step the lead foot forward about half a foot "
            "length, then drag the rear foot the same distance so the "
            "stance width is restored. To retreat, step the rear foot back "
            "first, then drag the lead foot. To circle left, step the lead "
            "foot left and follow with the rear; to circle right, lead "
            "with the rear foot and follow with the lead. Keep the knees "
            "soft and the head level - bouncing up and down wastes the "
            "legs and telegraphs movement. Drill the pattern: two steps "
            "forward, one back, circle left, circle right, always ending "
            "in the stance. Then add measure: face a partner and hold the "
            "distance where your extended lead hand just brushes his "
            "shoulder. That is your range. Step in to strike, step out to "
            "breathe, never stand still inside his reach."
        ),
        "key_points": [
            "Every step restores the stance: advance lead-first, retreat rear-first, never cross the feet.",
            "Measure is the true weapon: one strike or one grip away is the only distance that matters.",
            "Head stays level and knees soft; bouncing wastes the legs and announces every move.",
            "Lateral steps open angles for strikes and close the door on the opponent's straight attacks.",
            "Sand-pit discipline: each step deliberate, each stance recovered, no wasted motion.",
        ],
        "requirements": [
            "Step-drag pattern in all four directions without crossing the feet.",
            "Ability to hold striking measure against a moving partner.",
            "Instant stance recovery after every step.",
        ],
        "standards": [
            "Philostratus Gymnasticus: footwork preparation for the combined demands of the bout.",
            "Gardiner, Athletics of the Ancient World: movement in the skamma.",
        ],
        "citations": [CIT_PHILOSTRATUS, CIT_GARDINER],
        "sig_lens": (
            "The Signature reading of footwork: measure is the geography "
            "of the oath. The Signature pankratiast does not chase and "
            "does not flee; he redraws the map with each step, placing "
            "himself exactly where his covenant can be kept - one strike "
            "away, one grip away. Every step-drag is a signature on the "
            "ground: here I stand, here I strike, here I throw."
        ),
    },
    {
        "key": "pygme",
        "name": "Pygme: The Boxing Half",
        "group": "The Two Halves",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Pygme, from pygmachia, is the boxing half of pankration: the "
            "upright striking game of straight punches thrown from the "
            "stance. The foundation punch is the straight lead: the fist "
            "travels in a direct line from the guard to the target, the "
            "shoulder rolls forward to shield the chin, and the rear foot "
            "drives the bodyweight behind it. The cross follows the same "
            "road from the rear hand, with the hips turning to add the "
            "body's mass. Ancient boxers wrapped their fists in himantes, "
            "long leather thongs, to protect the hands; the pankratiast "
            "fought bare-handed, so the pygme half of his training "
            "stressed clean knuckle contact and the guard that snaps "
            "straight back after every punch. Hooks and uppercuts appear "
            "at close range, but the straight punches are the road the "
            "whole striking game travels."
        ),
        "how_it_works": (
            "From the guard, throw the lead straight punch: extend the "
            "lead fist directly at the target, turning the fist so the "
            "knuckles land flat. As the arm extends, drive off the rear "
            "foot and let the lead shoulder roll forward to cover the "
            "chin. The punch ends with the arm nearly straight but the "
            "elbow never locked. Snap it back along the same line to the "
            "guard - the return is half the technique. For the cross, "
            "push off the rear foot, rotate the hips so the rear shoulder "
            "drives forward, and extend the rear fist straight down the "
            "center. The chin stays tucked behind the lead shoulder "
            "throughout. Practice on a heavy bag or pads: lead straight, "
            "cross, lead straight, always returning to the guard. Power "
            "comes from the feet and hips, never from arm-swinging."
        ),
        "key_points": [
            "Straight punches travel the shortest road: guard to target and straight back, no wasted curve.",
            "The shoulder rolls forward to shield the chin with every punch; defense is built into the attack.",
            "Power rises from the rear foot through the hips: the arm delivers force the body generates.",
            "The snap-back to guard is half the punch; a punch that does not return is an invitation.",
            "Bare-handed pankration demands clean knuckle contact: the fist lands flat, the wrist stays straight.",
        ],
        "requirements": [
            "Straight lead and cross thrown from the guard with hip rotation.",
            "Chin tucked and lead shoulder covering it through every punch.",
            "Immediate return to guard after each punch.",
        ],
        "standards": [
            "Poliakoff, Combat Sports in the Ancient World: pygme technique and the himantes.",
            "Gardiner, Athletics of the Ancient World: the straight punch in vase imagery.",
        ],
        "citations": [CIT_POLIAKOFF, CIT_GARDINER, CIT_MILLER],
        "sig_lens": (
            "The Signature reading of pygme: the straight road of the "
            "oath. The Signature pankratiast throws the lead straight the "
            "way a signature is written - direct, committed, no "
            "flourish. The cross is kratos arriving: the whole body sworn "
            "behind one fist. And the snap-back is honor: every strike "
            "accounted for, nothing left hanging in the air."
        ),
    },
    {
        "key": "pale",
        "name": "Pale: The Wrestling Half",
        "group": "The Two Halves",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Pale is the wrestling half of pankration: the standing "
            "grapple, the grips, the throws, and the ground struggle. In "
            "the ancient contest the wrestlers fought upright, each "
            "seeking the grip that would let him throw the other to the "
            "sand. The fundamental grips are the collar tie at the neck, "
            "the underhook beneath the opponent's arm, and the overhook "
            "draped over it - each one a handle on the opponent's balance. "
            "The goal of pale is off-balancing: move the opponent's weight "
            "past the edge of his base and the throw completes itself. "
            "Where pygme strikes from distance, pale works chest to "
            "chest; the pankratiast must be fluent in both, because the "
            "bout flows from one to the other without pause."
        ),
        "how_it_works": (
            "Face a partner in the stance and reach for the collar tie: "
            "cup the back of his neck with your lead hand, elbow down, "
            "and pull his head slightly toward you to break his posture. "
            "With the other hand, swim for the underhook: slide your arm "
            "under his armpit and lace your hand behind his back or "
            "shoulder. From here, feel his balance: push gently and note "
            "which foot carries his weight. To off-balance, step your "
            "lead foot beside his lead foot and pull his head down and "
            "across while driving your underhook upward - his weight tips "
            "over the trapped leg. That tip, that moment his base fails, "
            "is the whole secret of pale. Drill it slowly: grip, feel, "
            "step, tip. Speed comes later; the feel comes first."
        ),
        "key_points": [
            "The grips are handles on balance: collar tie, underhook, overhook - each controls posture and weight.",
            "Off-balancing beats strength: move his weight past his base and the throw does the work.",
            "Head position rules the clinch: the head inside and up wins; the head pulled down loses.",
            "Pale is felt before it is forced: drill the weight-shift slowly until the tip is obvious.",
            "Striking and wrestling share the stance: the bout flows between halves without a pause.",
        ],
        "requirements": [
            "Secure collar tie and underhook from the stance against a resisting partner.",
            "Ability to feel and report the partner's weight distribution.",
            "Off-balance to the point of a controlled tip without muscling.",
        ],
        "standards": [
            "Poliakoff, Combat Sports in the Ancient World: pale grips and the mechanics of the throw.",
            "Philostratus Gymnasticus: wrestling preparation within pankration training.",
        ],
        "citations": [CIT_POLIAKOFF, CIT_PHILOSTRATUS],
        "sig_lens": (
            "The Signature reading of pale: the grip is the handshake of "
            "the covenant. The Signature pankratiast does not grab; he "
            "takes hold - the collar tie the seal on the opponent's "
            "posture, the underhook the sworn claim on his balance. "
            "Off-balancing is the Signature lesson that force obeys "
            "leverage: kratos without pan is just pushing, but kratos "
            "with position is the throw."
        ),
    },
    {
        "key": "prohibitions",
        "name": "The Ancient Prohibitions",
        "group": "Origins and Rules",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The ancient pankration ruleset is famous for what it barely "
            "forbids. According to the ancient accounts, only two acts "
            "were prohibited: biting (daknein) and gouging the eyes or "
            "other soft parts (oruttein, to dig). Everything else was "
            "permitted - punching, kicking, elbowing, kneeing, throwing, "
            "tripping, strangling, and bending joints. A referee, the "
            "hellanodikes, watched the bout and could punish fouls, and "
            "the Spartans were said to train even the forbidden "
            "techniques for real war while observing them in sport. The "
            "sparseness of the rules is the soul of the art: pankration "
            "was the closest the ancient games came to unrestricted "
            "fighting, and its champions were honored as the complete "
            "fighters of their age."
        ),
        "how_it_works": (
            "Learn the ruleset the way the ancients enforced it: as a "
            "short list of absolute lines. First line: no biting - the "
            "teeth are never a weapon in the bout. Second line: no eye "
            "gouging and no digging at soft tissue - the hands strike and "
            "grapple, they do not maim the senses. Everything inside "
            "those two lines is the game: strike any target, throw from "
            "any grip, strangle, lock joints, fight standing and on the "
            "ground. In modern training, add the modern safety lines on "
            "top: tap early and often when caught, respect the tap "
            "instantly, wear protective gear for hard sparring, and stop "
            "the instant a partner signals. The ancient lines teach the "
            "art's character; the modern lines keep the training room "
            "alive to train again tomorrow."
        ),
        "key_points": [
            "Two ancient prohibitions only: biting (daknein) and gouging (oruttein) - everything else was legal.",
            "The hellanodikes refereed the bout; the sparseness of the rules is the identity of the art.",
            "Unrestricted within the lines: strikes, throws, strangles, and joint locks all belong to the bout.",
            "Modern training adds modern safety: tap early, honor the tap, gear up, stop on signal.",
            "The ruleset rewards the complete fighter: no specialist can hide where everything is allowed.",
        ],
        "requirements": [
            "Memorization of the two ancient prohibitions and their meaning.",
            "Modern safety protocol: tap, protective gear, and stop-on-signal discipline.",
            "A training partner agreement honoring both the ancient lines and the modern ones.",
        ],
        "standards": [
            "Poliakoff, Combat Sports in the Ancient World: the pankration ruleset and the hellanodikes.",
            "Miller, Arete: ancient sources on permitted and prohibited acts.",
        ],
        "citations": [CIT_POLIAKOFF, CIT_MILLER],
        "sig_lens": (
            "The Signature reading of the prohibitions: the oath has "
            "edges. The Signature pankratiast swears to all force - pan - "
            "but the oath is sworn within lines, and lines are what make "
            "an oath an oath instead of a brawl. Biting and gouging are "
            "outside the covenant; everything inside it is the art. The "
            "modern safety lines are the same covenant extended to the "
            "training room: train hard, train honest, and bring your "
            "partner home whole."
        ),
    },
    {
        "key": "ptosis",
        "name": "Ptosis: Falling and Rolling",
        "group": "Stance and Movement",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Ptosis is the fall, and learning to fall is the first "
            "wrestling skill of pankration. A fighter who fears the throw "
            "fights stiffly; a fighter who can fall fights freely. The "
            "breakfall spreads the impact of a throw across the broadest "
            "possible surface - the whole side of the body - and across "
            "the longest possible time, by slapping the ground with the "
            "arm and exhaling sharply. The head is the priority: the chin "
            "tucks hard to the chest so the skull never whips into the "
            "sand. The ancient pankratiasts fell on the skamma's sand, "
            "which forgives; the modern student learns on mats, which "
            "forgive more. Either way, the lesson is the same: the ground "
            "is not the enemy, the stiff body is."
        ),
        "how_it_works": (
            "Start sitting on the mat with knees bent. Fall backward, "
            "tucking the chin to the chest, and slap both arms into the "
            "mat at 45-degree angles as your back lands - the slap and "
            "the exhale happen together, one sharp breath out. The arms "
            "absorb and spread the shock; the tucked chin keeps the head "
            "off the ground. Progress to the side fall: from a low "
            "crouch, roll onto one side, slapping the mat with the whole "
            "arm and side of the leg, chin still tucked. Then the forward "
            "roll: tuck the chin, roll over one shoulder diagonally across "
            "the back, and slap out to stand. Drill each fall until it is "
            "boring, then have a partner tip you gently from the clinch "
            "so the fall arrives unannounced. A breakfall you must think "
            "about is a breakfall that arrives too late."
        ),
        "key_points": [
            "Chin tucked is the first law: the head never touches the ground on your fall.",
            "The arm slap spreads impact across time and surface; the exhale braces the body for it.",
            "Learn backward, side, and forward falls in that order: each builds the next.",
            "Drill until the fall is reflex; a considered fall is a late fall.",
            "The fearless fighter is the free fighter: safe falling unlocks committed throwing.",
        ],
        "requirements": [
            "Clean backward, side, and forward breakfalls from a crouch.",
            "Chin tucked and arm slap automatic on every fall.",
            "Calm falling from a partner's gentle throws.",
        ],
        "standards": [
            "Philostratus Gymnasticus: falling practice in the pankratiast's preparation.",
            "World Pankration Athlima Federation rules: safe-fall expectations in modern competition.",
        ],
        "citations": [CIT_PHILOSTRATUS, CIT_WPAF],
        "sig_lens": (
            "The Signature reading of the fall: the oath includes the "
            "ground. The Signature pankratiast swears not only to throw "
            "but to be thrown - the breakfall is the covenant's humility, "
            "the promise that the art will not break its student. Chin "
            "tucked, arm slapping, breath out: that is the Signature "
            "pankratiast signing his name on the mat and rising to sign "
            "it again."
        ),
    },
    {
        "key": "halteres",
        "name": "Halteres: Strength of the Pankratiast",
        "group": "Training and Conditioning",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The halteres were the ancient hand-weights: stone or metal "
            "dumbbells gripped in each fist, swung in training to build "
            "the shoulders, back, and grip of the fighter. The ancient "
            "sources show athletes swinging them in rhythmic drills and "
            "even using them in the standing long jump. For the "
            "pankratiast, the halteres built exactly the strength the art "
            "demands: the pulling power of the clinch, the pushing power "
            "of the strike, and the grip that holds a wrist or an ankle "
            "through the struggle. The principle is progressive: start "
            "with weights you can swing cleanly for many repetitions, add "
            "load or repetitions a little at a time, and let the body "
            "adapt. Strength in pankration is not the display of the "
            "muscle; it is the durability of the technique under fatigue."
        ),
        "how_it_works": (
            "Take a light dumbbell in each hand - the modern halteres. "
            "Stand in the stance and swing both weights forward and up to "
            "shoulder height, letting the hips and legs drive the motion, "
            "then control them back down. That is the basic swing: ten to "
            "fifteen clean repetitions, breathing out on the lift. Next, "
            "the punch press: from the guard, punch straight with each "
            "hand holding a light weight, snapping the fists back to the "
            "chin. Then the grip hold: simply carry heavy dumbbells at "
            "your sides for time, the farmer's walk of the pankratiast. "
            "Train three days a week, adding a small amount of weight or "
            "a few repetitions each week. When the form breaks, the set "
            "is over - the halteres build strength only when the movement "
            "stays clean."
        ),
        "key_points": [
            "Halteres are ancient dumbbells: swung, pressed, and carried to build the fighter's shoulders, back, and grip.",
            "Hip-driven swings teach the body to generate force from the ground, the source of every strike and throw.",
            "Light punch presses groove the straight punch under load; heavy carries forge the clinch grip.",
            "Progression is gradual: small weekly additions of load or reps, never jumps that break form.",
            "Strength serves technique: the set ends when form breaks, because ugly strength is useless strength.",
        ],
        "requirements": [
            "A pair of light and a pair of moderate dumbbells.",
            "Clean swing, punch press, and carry form for the prescribed reps.",
            "A weekly progression log: load and reps recorded, small increases only.",
        ],
        "standards": [
            "Gardiner, Athletics of the Ancient World: the halteres in training and the long jump.",
            "Miller, Arete: ancient sources on weight training for athletes.",
        ],
        "citations": [CIT_GARDINER, CIT_MILLER],
        "sig_lens": (
            "The Signature reading of the halteres: the forge of the "
            "oath. Iron in the hands is the Signature pankratiast's "
            "daily renewal of kratos - force not as a gift but as a "
            "practice, sworn rep by rep. The swing teaches that power "
            "rises from the ground; the carry teaches that the covenant "
            "is held, literally, in the grip. Strength is the oath made "
            "muscle."
        ),
    },
    {
        "key": "skamma",
        "name": "The Skamma: The Training Ground",
        "group": "Training and Conditioning",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The skamma was the dug-up sand pit where the ancient "
            "wrestlers and pankratiasts trained and competed. The sand "
            "gave under the feet, forgave the fall, and punished sloppy "
            "footwork: every step had to be deliberate or the fighter "
            "sank and stumbled. Training in the skamma built the exact "
            "fitness of the bout - the legs for endless stance work, the "
            "lungs for the clinch struggle, the skin toughened by the "
            "sand itself. The modern student rarely has a sand pit, but "
            "the skamma's lessons transfer to any mat: train the feet "
            "deliberately, drill the falls until they are reflex, and do "
            "the hard rounds in the conditions of the fight. The ground "
            "you train on is the ground you fight on."
        ),
        "how_it_works": (
            "Treat your mat as a skamma. First, walk the stance across it: "
            "advance, retreat, circle, every step deliberate, feeling the "
            "surface under the feet the way sand would demand. Second, "
            "drill the falls on it: backward, side, forward, until the "
            "mat feels like an old friend. Third, wrestle on it: clinch "
            "rounds with a partner, two minutes of continuous grip "
            "fighting, then rest one minute, then again - the ancient "
            "rhythm of the pit. Fourth, condition on it: stance holds, "
            "haltere swings, and short sprints across the mat between "
            "rounds. Keep the training ground clean and consistent: same "
            "surface, same discipline, every session. The skamma was not "
            "fancy. It was honest, and honesty is what it taught."
        ),
        "key_points": [
            "The skamma's sand demanded deliberate feet, forgave the fall, and built fight-specific fitness.",
            "Train the surface deliberately: stance walks, falls, clinch rounds, conditioning - all on the same ground.",
            "Clinch rounds of two minutes with one minute rest reproduce the ancient rhythm of the pit.",
            "Consistency of ground builds consistency of fighter: same surface, same discipline, every session.",
            "The ground is a teacher: respect it, learn its lessons, and it returns you ready.",
        ],
        "requirements": [
            "A clean, consistent training surface (mat or sand).",
            "Deliberate stance and fall drills on that surface every session.",
            "Timed clinch rounds with a partner: two minutes on, one minute off.",
        ],
        "standards": [
            "Gardiner, Athletics of the Ancient World: the skamma in ancient training.",
            "Philostratus Gymnasticus: the training ground's role in the athlete's preparation.",
        ],
        "citations": [CIT_GARDINER, CIT_PHILOSTRATUS],
        "sig_lens": (
            "The Signature reading of the skamma: the honest ground. The "
            "Signature pankratiast trains where the fight will be, on "
            "purpose, because the oath is not sworn in comfort. Sand "
            "under the feet is the covenant's witness: every deliberate "
            "step a kept promise, every drilled fall a promise to rise. "
            "The training ground is the first temple of pan and kratos."
        ),
    },
    {
        "key": "breathing",
        "name": "Breathing for the Bout",
        "group": "Training and Conditioning",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Breathing is the engine of pankration: the bout is long, the "
            "clinch is crushing, and the fighter who cannot breathe "
            "cannot fight. The rule is simple and absolute: exhale on "
            "effort, inhale on recovery. Every punch, kick, throw, and "
            "bridge rides out on a sharp breath; every guard, stance "
            "reset, and circling step drinks air back in. Holding the "
            "breath under strain spikes pressure and empties the tank; "
            "panting with the mouth wide open invites the punch that ends "
            "the night. The ancient pankratiasts fought bouts that could "
            "run long, and their training - the runs, the skamma rounds, "
            "the halteres - was breathing training as much as muscle "
            "training. Control the breath and the body follows; lose the "
            "breath and nothing else matters."
        ),
        "how_it_works": (
            "Practice the rhythm away from technique first. Stand in the "
            "stance and breathe in through the nose for two counts, out "
            "through the mouth for two counts, keeping the belly soft and "
            "the shoulders down. Now add effort: throw a straight punch "
            "on each exhale, inhaling as the fist returns. Throw a kick "
            "on the exhale, breathe in on the reset. Bridge on the exhale, "
            "settle on the inhale. The exhale is short and sharp, like "
            "fogging a mirror; the inhale is calm and full. In sparring, "
            "anchor the rhythm to the action: breathe out with every "
            "attack and every escape, breathe in while circling and "
            "guarding. When you feel the breath running away, the answer "
            "is never to hold it - slow the exhale, lengthen it, and let "
            "the rhythm recapture you."
        ),
        "key_points": [
            "Exhale on effort, inhale on recovery: the absolute law of the fighting breath.",
            "The exhale is short and sharp; the inhale is calm and full through the nose.",
            "Never hold the breath under strain: pressure spikes and the tank empties.",
            "Anchor breathing to action: out with attacks and escapes, in with circling and guarding.",
            "Conditioning is breathing training: runs, rounds, and halteres all teach the rhythm.",
        ],
        "requirements": [
            "Two-count nasal inhale and sharp oral exhale maintained in the stance.",
            "Exhale synchronized with every strike, throw, and bridge.",
            "Recovery breathing that restores rhythm within one rest minute.",
        ],
        "standards": [
            "Philostratus Gymnasticus: endurance preparation for the long pankration bout.",
            "World Pankration Athlima Federation rules: round structure demanding breath discipline.",
        ],
        "citations": [CIT_PHILOSTRATUS, CIT_WPAF],
        "sig_lens": (
            "The Signature reading of the breath: the bellows of the "
            "oath. The Signature pankratiast breathes the way the forge "
            "breathes - out with the hammer strike, in with the draw of "
            "the coals. Each exhale delivers the sworn force; each inhale "
            "renews the covenant. The fighter who masters his breath has "
            "mastered the tempo of pan and kratos both."
        ),
    },
    {
        "key": "clinch_tieup",
        "name": "The Clinch Tie-Up",
        "group": "The Two Halves",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The clinch tie-up is the bridge of pankration: the chest-to-"
            "chest grapple where the pygme half ends and the pale half "
            "begins. One fighter reaches for grips - collar tie, underhook, "
            "overhook, body lock - and both wrestle for head position, "
            "hip position, and the underhook that controls the other's "
            "spine. From the tie-up come the knees, the elbows, the trips, "
            "and the throws; losing the tie-up means eating all of them. "
            "The fundamentals are head position (forehead against the "
            "opponent's temple or jaw, never buried in his chest), hip "
            "position (hips back and low, never pressed forward), and hand "
            "fighting (constant small battles for the inside grip). The "
            "clinch is not a rest: it is the busiest room in the fight."
        ),
        "how_it_works": (
            "Step into a partner and tie up: lead hand to the collar tie "
            "behind his neck, rear hand swimming for the underhook under "
            "his armpit. Place your forehead against his temple - head "
            "up, chin tucked - and drop your hips low and back so your "
            "weight sits over your feet, not on him. Now hand-fight: when "
            "he reaches for your neck, swim your arm inside his and "
            "re-take the underhook; when he pushes your head down, circle "
            "it back up and re-seat the forehead. Drill the pummeling "
            "cycle: he takes the underhook, you swim yours back, he "
            "swims, you swim - continuous, breathing steadily, hips "
            "moving. Add the entries: from the tie-up, drop for a knee, "
            "step for a trip, or pull for a throw. The tie-up is a "
            "conversation; make sure you are the one asking the questions."
        ),
        "key_points": [
            "The clinch is the bridge: where striking ends and wrestling begins, and the busiest room in the fight.",
            "Head up and inside wins; hips low and back keep the base under the battle.",
            "Hand-fighting is continuous: swim for the underhook, re-take it, never accept the bad grip.",
            "Every clinch technique - knees, elbows, trips, throws - launches from the tie-up's grips.",
            "The clinch is never a rest: stillness in the tie-up is surrender of the initiative.",
        ],
        "requirements": [
            "Secure collar tie and underhook with correct head and hip position.",
            "Continuous pummeling for the underhook against resistance.",
            "One knee strike and one trip launched from the tie-up.",
        ],
        "standards": [
            "Poliakoff, Combat Sports in the Ancient World: the standing grapple in pankration.",
            "World Pankration Athlima Federation rules: clinch work in modern competition.",
        ],
        "citations": [CIT_POLIAKOFF, CIT_WPAF],
        "sig_lens": (
            "The Signature reading of the clinch: the handshake of the "
            "whole art. In the tie-up the Signature pankratiast holds "
            "both halves of his oath in his hands at once - the striking "
            "half cocked in the elbows, the wrestling half loaded in the "
            "hips. Pan is the clinch's promise: every technique in the "
            "database is reachable from here. Kratos is its price: the "
            "tie-up belongs to whoever works hardest inside it."
        ),
    },
    {
        "key": "laktisma",
        "name": "Laktisma: The Front Kick",
        "group": "Kicking",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Laktisma, the kick, is pankration's longest weapon. The front "
            "kick drives the heel or the ball of the foot straight into "
            "the opponent's midsection or thigh, using the leg's full "
            "length to strike from beyond punching range. The mechanics "
            "are a chamber and a piston: the knee rises high and tight, "
            "then the lower leg extends like a spear, the hips driving "
            "forward behind it. The ancient sources record kicking as a "
            "standard part of the pankration arsenal, and vase paintings "
            "show fighters delivering kicks to the body. The front kick "
            "serves three masters: it damages, it stops an advancing "
            "opponent cold, and it sets the measure for everything that "
            "follows. A fighter who cannot kick cannot keep a wrestler "
            "out; a fighter who can kick chooses when the clinch begins."
        ),
        "how_it_works": (
            "From the stance, shift your weight to the rear leg and raise "
            "the lead knee high, thigh parallel to the ground, shin "
            "hanging - this is the chamber. Drive the hips forward and "
            "extend the lower leg straight at the target, striking with "
            "the heel or the ball of the foot, toes pulled back. The "
            "supporting foot pivots slightly and the torso leans back "
            "just enough to add reach without losing balance. Snap the "
            "leg back along the same path to the chamber, then set the "
            "foot down back into the stance - the kick is not finished "
            "until the stance is recovered. Practice on a heavy bag: "
            "chamber, extend, rechamber, set down. Start with the lead "
            "leg for speed, then drill the rear leg for power, driving "
            "the hip through like a door swinging shut."
        ),
        "key_points": [
            "Chamber high and tight, extend like a piston, rechamber before the foot lands.",
            "Heel or ball of the foot is the weapon; toes pulled back, ankle locked.",
            "Hip drive is the engine: the leg delivers what the hips commit.",
            "The kick controls measure: it damages, stops advances, and decides when the clinch begins.",
            "Stance recovery completes the kick; a kick that strands you is a takedown offered.",
        ],
        "requirements": [
            "Clean chamber-extend-rechamber cycle with both legs on a heavy bag.",
            "Hip drive visible in the extension; torso counter-lean for reach.",
            "Immediate stance recovery after every kick.",
        ],
        "standards": [
            "Poliakoff, Combat Sports in the Ancient World: kicking in the pankration arsenal.",
            "Gardiner, Athletics of the Ancient World: kicks depicted in vase painting.",
        ],
        "citations": [CIT_POLIAKOFF, CIT_GARDINER],
        "sig_lens": (
            "The Signature reading of the front kick: the spear of the "
            "oath. The Signature pankratiast chambers the laktisma the "
            "way an archer draws - pan gathered in the coiled knee - and "
            "releases it as kratos, the whole body sworn behind one "
            "heel. The rechamber is honor: the weapon returns to its "
            "sheath, the stance is restored, and the covenant stands "
            "ready for the next promise."
        ),
    },
    {
        "key": "turning_kick",
        "name": "The Turning Kick",
        "group": "Kicking",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The turning kick - the round kick - is the laktisma thrown "
            "with rotation: the hips turn over completely and the shin or "
            "instep whips around into the opponent's ribs, thigh, or head. "
            "Where the front kick is a piston, the turning kick is a flail: "
            "the standing foot pivots, the hips roll over like a wave, and "
            "the leg follows the body's rotation. It is the heavier of "
            "the two kicks and the more punishing to the opponent's guard, "
            "because the force arrives at an angle the straight guard is "
            "not built to catch. The turning kick also teaches the "
            "pankratiast's most important rotational lesson: power lives "
            "in the hips' turn, a lesson the throws will repeat."
        ),
        "how_it_works": (
            "From the stance, step the lead foot slightly across and pivot "
            "on the ball of the supporting foot, turning it until the toes "
            "point away from the target. As the foot pivots, roll the hips "
            "over - the kicking hip drives forward and down - and let the "
            "leg whip around, striking with the shin or the instep. The "
            "arms swing for balance and protection: the same-side arm "
            "drops to cover the ribs the kick exposes, the opposite arm "
            "stays near the chin. Follow through the target, then bring "
            "the leg back along its arc to the stance. Drill it on the "
            "bag in stages: first the pivot and hip roll without the leg, "
            "then the full kick at half speed, then full power. The kick "
            "is correct when the bag jumps sideways and you land balanced."
        ),
        "key_points": [
            "Pivot the supporting foot fully; the hips must roll over for the kick to carry power.",
            "Shin or instep is the weapon, arriving at an angle the straight guard cannot catch.",
            "The same-side arm guards the exposed ribs; the opposite arm stays home at the chin.",
            "The turning kick teaches rotation: the hips' turn is the engine the throws will borrow.",
            "Follow through the target, then return along the arc: balance at the end proves the kick.",
        ],
        "requirements": [
            "Full pivot and hip roll with shin contact on the bag.",
            "Arm discipline maintained through the kick: ribs covered, chin guarded.",
            "Balanced stance recovery after full-power kicks.",
        ],
        "standards": [
            "Poliakoff, Combat Sports in the Ancient World: kicking technique in pankration.",
            "World Pankration Athlima Federation rules: legal kicking targets in modern competition.",
        ],
        "citations": [CIT_POLIAKOFF, CIT_WPAF],
        "sig_lens": (
            "The Signature reading of the turning kick: the wheel of the "
            "oath. The Signature pankratiast turns his whole body into "
            "the promise - pan in the full rotation, nothing held back - "
            "and delivers kratos at the end of the arc. The pivot foot "
            "is the seal on the ground; the rolling hip is the signature "
            "across the air."
        ),
    },
    {
        "key": "ankon",
        "name": "Ankon: Elbow Strikes",
        "group": "Close Strikes",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Ankon is the elbow, and the elbow is pankration's close-"
            "quarters blade. When the clinch collapses the distance past "
            "punching range, the elbow takes over: short, hard, and "
            "driven by the rotation of the torso rather than the extension "
            "of the arm. The horizontal elbow cuts across the jaw and "
            "temple; the upward elbow spears beneath the chin; the "
            "downward elbow drops like a hammer onto the collarbone and "
            "shoulder. Because the elbow is a short lever of dense bone, "
            "it concentrates the body's rotation into a small, hard "
            "point - which is why elbow strikes cut and stun out of "
            "proportion to their visible wind-up. In the ancient bout, "
            "where the clinch was constant, the elbow was the punctuation "
            "of the tie-up."
        ),
        "how_it_works": (
            "For the horizontal elbow, raise the striking arm so the elbow "
            "points at the target and the forearm lies horizontal, fist "
            "near your own ear. Rotate the torso sharply, driving the "
            "elbow across in a tight arc, and pivot the supporting foot "
            "to feed the rotation. The power is all in the turn - the arm "
            "itself barely moves. For the upward elbow, drop the hand "
            "slightly and drive the elbow up beneath the target, rising "
            "from the legs. For the downward elbow, raise the elbow high "
            "and chop down, letting the bodyweight fall behind it. After "
            "each elbow, the arm returns to the guard or the clinch grip. "
            "Drill on pads held close: the pad holder stands at clinch "
            "distance, and you turn the elbows over in short, heavy arcs. "
            "Short, sharp, and back to the tie-up."
        ),
        "key_points": [
            "The elbow is a short lever of dense bone: torso rotation concentrates into a small, hard point.",
            "Horizontal across the jaw, upward beneath the chin, downward onto the collarbone: three roads, one engine.",
            "Power comes from the torso's turn and the foot's pivot, never from swinging the arm.",
            "Elbows rule the collapsed distance where punches cannot extend: the punctuation of the tie-up.",
            "Return to guard or grip after every elbow; the blade sheaths itself.",
        ],
        "requirements": [
            "Horizontal, upward, and downward elbows with torso rotation on pads.",
            "Supporting-foot pivot feeding each elbow.",
            "Immediate return to guard or clinch grip.",
        ],
        "standards": [
            "Poliakoff, Combat Sports in the Ancient World: close striking in the pankration clinch.",
            "World Pankration Athlima Federation rules: legal elbow use in modern competition.",
        ],
        "citations": [CIT_POLIAKOFF, CIT_WPAF],
        "sig_lens": (
            "The Signature reading of the elbow: the seal of the oath. "
            "The Signature pankratiast throws the ankon the way a seal "
            "is pressed - short, final, and unmistakable. Pan is the "
            "elbow's readiness at every collapsed distance; kratos is "
            "the torso's whole turn behind one hard point. In the clinch "
            "the elbow signs the covenant where the fist cannot reach."
        ),
    },
    {
        "key": "gony",
        "name": "Gony: Knee Strikes",
        "group": "Close Strikes",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Gony is the knee, and the knee is the clinch's cannon. From "
            "the tie-up, the fighter grips the opponent's neck or arms, "
            "pulls him down and forward, and drives the knee up into the "
            "midsection or thigh. The power comes from the pull as much "
            "as the lift: the arms drag the target down onto the rising "
            "knee, doubling the collision. The straight knee spears the "
            "body; the round knee, thrown with a small hip turn, wraps "
            "around the guard into the ribs. Because pankration's clinch "
            "is constant, the knee is among the art's highest-percentage "
            "weapons - it strikes from the position both fighters are "
            "already fighting to hold."
        ),
        "how_it_works": (
            "From the collar tie, grip the back of the partner's neck "
            "with both hands or control one arm. Pull his head down and "
            "toward you as you drive the same-side knee straight up, "
            "hips thrusting forward beneath it. The pull and the knee "
            "meet at the target: your hands drag him down, your knee "
            "rises to greet him. Strike with the point of the knee, "
            "toes pointed down, and snap the leg back to the ground "
            "immediately - standing on one leg in the clinch is borrowed "
            "time. For the round knee, turn the hip over slightly so the "
            "knee travels in a small arc into the ribs. Drill on a heavy "
            "bag or with a partner holding a body pad: pull, knee, reset, "
            "pull, knee, reset. The rhythm is the technique."
        ),
        "key_points": [
            "The knee's power is doubled: the arms pull the target down onto the rising knee.",
            "Straight knee spears the midsection; round knee wraps the guard into the ribs.",
            "Hips thrust forward beneath the knee; toes point down, knee point leads.",
            "Snap the leg back instantly: one-legged time in the clinch is borrowed time.",
            "The knee strikes from the position both fighters already hold - the highest-percentage weapon of the tie-up.",
        ],
        "requirements": [
            "Straight and round knees with the pull-down from the collar tie.",
            "Hip thrust and toe-point discipline on every knee.",
            "Immediate return to two feet and the tie-up.",
        ],
        "standards": [
            "Poliakoff, Combat Sports in the Ancient World: knee strikes from the pankration clinch.",
            "World Pankration Athlima Federation rules: legal knee targets in modern competition.",
        ],
        "citations": [CIT_POLIAKOFF, CIT_WPAF],
        "sig_lens": (
            "The Signature reading of the knee: the hammer of the oath. "
            "The Signature pankratiast drives the gony the way the forge "
            "drives the hammer - the pull of the hands the tongs drawing "
            "the work into place, the rising knee the blow. Pan is the "
            "knee's availability from every tie-up; kratos is the "
            "collision the pull and the lift make together."
        ),
    },
    {
        "key": "rhipsis",
        "name": "Rhipsis: The Art of the Throw",
        "group": "Throws",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Rhipsis, from rhiptein (to throw), is the principle behind "
            "every throw in pankration: off-balance, entry, execution. "
            "First the opponent's weight is moved past the edge of his "
            "base - the off-balance, without which no throw works. Then "
            "the thrower enters, placing his body in the position the "
            "throw requires: hip across, leg behind, shoulder under. Then "
            "the execution: the lever or the wheel that completes what "
            "the off-balance started. The ancient pankratiasts threw from "
            "the standing clinch, and a clean throw onto the skamma's sand "
            "could end the argument outright. Every specific throw in "
            "this database - hip throw, waist lift, trips, counters - is "
            "rhipsis wearing a different grip. Learn the principle and "
            "the throws teach themselves."
        ),
        "how_it_works": (
            "With a partner in the tie-up, practice the three beats "
            "slowly. Beat one, off-balance: pull his head down and across "
            "while stepping your lead foot beside his, until you feel his "
            "weight tip onto the leg nearest you - his base is now a "
            "single foot. Beat two, entry: step your hips across in front "
            "of his hips, back to his chest, knees bent, your body the "
            "wall his tipping weight will fall over. Beat three, "
            "execution: straighten your legs and pull his upper body over "
            "the wall of your hips, guiding him down to the mat. He falls "
            "because his balance was already gone; your body merely "
            "showed him the way down. Drill the three beats as three "
            "separate moves until each is clean, then blend them into one "
            "continuous throw. The throw is not a lift of his weight - "
            "it is the completion of his fall."
        ),
        "key_points": [
            "Every throw has three beats: off-balance, entry, execution - in that order, always.",
            "Off-balance is the throw: move his weight past his base and the rest is guidance.",
            "Entry places your body as the wall or wheel his tipping weight falls over.",
            "Execution completes the fall; it never lifts dead weight - leverage, not muscle.",
            "Rhipsis is one principle in many grips: learn it once, recognize it in every throw.",
        ],
        "requirements": [
            "Demonstrable off-balance of a partner from the tie-up.",
            "Clean entry with hips across and knees bent.",
            "Guided, controlled completion of the throw to the mat.",
        ],
        "standards": [
            "Poliakoff, Combat Sports in the Ancient World: the mechanics of the ancient throw.",
            "Philostratus Gymnasticus: throwing preparation in pankration training.",
        ],
        "citations": [CIT_POLIAKOFF, CIT_PHILOSTRATUS],
        "sig_lens": (
            "The Signature reading of the throw: the completion of the "
            "oath's logic. The Signature pankratiast does not force the "
            "throw; he proves it - beat one the argument (your balance "
            "is mine), beat two the evidence (my body is the wall), beat "
            "three the verdict (down). Pan is the principle's reach "
            "across every grip; kratos is the fall the principle "
            "commands."
        ),
    },
    {
        "key": "hip_throw",
        "name": "The Hip Throw",
        "group": "Throws",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The hip throw is rhipsis in its purest form: the thrower's "
            "hip becomes the fulcrum, the opponent's body the lever, and "
            "the off-balance the force. From the clinch the thrower turns "
            "his back to the opponent's chest, seats his hips low across "
            "the opponent's thighs, and pulls the upper body forward over "
            "the fulcrum while straightening his legs. The opponent, "
            "already tipping, rotates over the hip and lands hard. It is "
            "one of the oldest throws in the wrestling world, and the "
            "ancient pankratiasts - standing wrestlers by training - "
            "threw it as a matter of course. The hip throw rewards the "
            "fighter who enters low and turns fully: a half-turn is a "
            "half-throw, and a half-throw is a gift to the opponent."
        ),
        "how_it_works": (
            "From the tie-up with an underhook, pull the partner forward "
            "until his weight tips onto his toes. Pivot on your lead foot, "
            "turning your back fully to his chest, and drop your hips low "
            "across the front of his thighs - your belt line below his. "
            "Keep the underhook tight and grip his far arm or lat with "
            "your free hand. Now straighten your legs explosively, pull "
            "his upper body down and over your hip, and turn your head to "
            "look where you want him to land. He rotates over the fulcrum "
            "of your hip and falls to the mat; you stay standing, hips "
            "loaded, ready to follow. The keys: enter low (hips below "
            "his), turn fully (back flat to his chest), and pull "
            "continuously. Drill it slowly with a cooperative partner "
            "until the entry is automatic, then add speed."
        ),
        "key_points": [
            "The hip is the fulcrum, the opponent's body the lever, the off-balance the force.",
            "Enter low: your hips must sit below his, or the fulcrum is above the load.",
            "Turn fully: back flat to his chest - a half-turn is a half-throw.",
            "Pull continuously through the execution; the throw fails the moment the pull stops.",
            "Stay standing after the throw: hips loaded, ready to follow to the ground.",
        ],
        "requirements": [
            "Full-turn entry with hips below the partner's against light resistance.",
            "Continuous pull through a controlled completion.",
            "Standing finish with base intact.",
        ],
        "standards": [
            "Poliakoff, Combat Sports in the Ancient World: hip throws in ancient wrestling and pankration.",
            "World Pankration Athlima Federation rules: throwing technique in modern competition.",
        ],
        "citations": [CIT_POLIAKOFF, CIT_WPAF],
        "sig_lens": (
            "The Signature reading of the hip throw: the wheel of the "
            "oath made flesh. The Signature pankratiast turns his back "
            "not in retreat but in promise - the fulcrum sworn, the load "
            "accepted. Pan is the full turn, the whole body committed to "
            "the technique; kratos is the rotation the fulcrum commands. "
            "The opponent does not fall because he was lifted; he falls "
            "because the covenant said so."
        ),
    },
    {
        "key": "mesolabe",
        "name": "Mesolabe: The Waist Grip and Lift",
        "group": "Throws",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The mesolabe - the middle grip - is the ancient waist lock: "
            "both arms encircling the opponent's waist from behind or "
            "from the clinch, hands clasped, the body locked to the body. "
            "From the mesolabe the pankratiast lifts: straightening the "
            "legs, arching the back, raising the opponent clear of the "
            "ground where his base, his balance, and his strength all "
            "cease to exist. A lifted fighter cannot strike, cannot "
            "throw, cannot resist - he can only wait for the ground to "
            "arrive. The ancient sources and vase paintings show the "
            "waist grip as a signature hold of the wrestlers, and in "
            "pankration it bridged the standing fight to the ground "
            "fight in a single dramatic arc."
        ),
        "how_it_works": (
            "Slip behind a partner or turn him in the clinch until his "
            "back is to your chest. Wrap both arms around his waist, "
            "clasp your hands - palm to palm or palm to wrist - and press "
            "your chest tight to his back, your head to one side. Drop "
            "your hips below his, keep your back straight, and "
            "straighten your legs to lift him. Once his feet leave the "
            "ground, he is yours: arch your back slightly and walk or "
            "turn him, then bend the knees and set him down firmly to "
            "the mat, following into the top position. The lift is all "
            "legs - if your back rounds, stop and reset the grip. Drill "
            "with a cooperative partner: grip, drop, lift, carry two "
            "steps, set down. The mesolabe teaches the deepest lesson of "
            "the throws: position first, and the lift is easy."
        ),
        "key_points": [
            "The waist lock from behind or the clinch: both arms around, hands clasped, chest to back.",
            "Lift with the legs, back straight: the legs are the crane, the back is only the frame.",
            "A lifted fighter has no base, no balance, no strength: the air is the loneliest place in the fight.",
            "Carry or turn before the finish: control the descent, then follow to the top position.",
            "Position first, lift second: hips below his makes the heavy weight light.",
        ],
        "requirements": [
            "Secure mesolabe grip with chest-to-back contact.",
            "Straight-backed leg lift of a cooperative partner clear of the ground.",
            "Controlled set-down finishing in the top position.",
        ],
        "standards": [
            "Poliakoff, Combat Sports in the Ancient World: the waist grip in ancient wrestling imagery.",
            "Gardiner, Athletics of the Ancient World: the lift in vase painting.",
        ],
        "citations": [CIT_POLIAKOFF, CIT_GARDINER],
        "sig_lens": (
            "The Signature reading of the mesolabe: the embrace of the "
            "oath. The Signature pankratiast wraps the waist lock the "
            "way the covenant wraps the fighter - complete, inescapable, "
            "sworn. Pan is the grip's totality: the whole opponent held "
            "at once. Kratos is the lift: the legs' honest work raising "
            "what the grip has claimed. To be lifted in the mesolabe is "
            "to learn what the oath weighs."
        ),
    },
    {
        "key": "trips_sweeps",
        "name": "Leg Trips and Foot Sweeps",
        "group": "Throws",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The trip and the sweep are the quiet throws: no big entry, "
            "no dramatic lift - just a foot or leg removing the "
            "opponent's support at the exact moment his weight commits to "
            "it. The inside trip hooks the instep behind his advancing "
            "foot and pulls as the upper body drives forward; the foot "
            "sweep brushes his stepping foot sideways the instant it "
            "touches down, before it can bear weight. Both are throws of "
            "timing rather than strength, which made them favorites of "
            "the ancient pankratiasts: in a long bout, the fighter who "
            "throws with timing instead of muscle is the fighter still "
            "standing at the end. The trip needs the clinch; the sweep "
            "needs only the step. Together they punish every foot the "
            "opponent moves."
        ),
        "how_it_works": (
            "For the inside trip, tie up and wait for the partner to "
            "step his lead foot forward. As his weight commits to the "
            "step, hook your instep behind his ankle, pull his foot "
            "toward you, and drive his upper body forward over it with "
            "your grips - he falls because the leg he trusted is gone. "
            "For the foot sweep, stand at kicking measure and watch his "
            "feet: the instant his lead foot lands from a step, brush it "
            "sideways with the sole of your foot, light and fast, while "
            "your hands push his upper body the other way. The contact "
            "is a brush, not a kick - speed and timing, never force. "
            "Drill the trip from the clinch and the sweep from measure, "
            "alternating, until you feel the rhythm: his step is your "
            "invitation, and you never decline it."
        ),
        "key_points": [
            "Trips and sweeps remove support at the moment of commitment: timing, not strength, is the weapon.",
            "The inside trip hooks the advancing ankle and drives the upper body over the missing leg.",
            "The foot sweep brushes the landing foot sideways before it can bear weight: a brush, never a kick.",
            "The trip wants the clinch; the sweep wants only the step - together they tax every foot moved.",
            "Economy is the point: the timed throw spends nothing and the tired fighter keeps throwing.",
        ],
        "requirements": [
            "Inside trip from the clinch timed to the partner's step.",
            "Foot sweep from measure timed to the footfall.",
            "Brush contact and upper-body direction: no muscling, no kicking.",
        ],
        "standards": [
            "Poliakoff, Combat Sports in the Ancient World: foot techniques in ancient wrestling.",
            "World Pankration Athlima Federation rules: trips and sweeps in modern competition.",
        ],
        "citations": [CIT_POLIAKOFF, CIT_WPAF],
        "sig_lens": (
            "The Signature reading of the trip and sweep: the quiet "
            "verdict. The Signature pankratiast does not announce the "
            "throw; he lets the opponent's own step sign it. Pan is the "
            "patience that watches every foot; kratos is the instant the "
            "support vanishes. The oath kept quietly is still the oath "
            "kept."
        ),
    },
    {
        "key": "apopnixis",
        "name": "Apopnixis: The Strangle",
        "group": "Submissions",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Apopnixis, from apopnigein (to throttle, to choke), is the "
            "strangle: the technique that ends the bout without a single "
            "strike. The forearm, the collar of the arm, or the legs "
            "close around the neck and compress the blood vessels of the "
            "neck until the opponent submits or consciousness fades. The "
            "ancient accounts are explicit: the great Arrhichion died in "
            "a stranglehold even as he won, which tells us the strangle "
            "was a known and feared finish of the ancient bout. The "
            "fundamental strangle is the rear choke: one arm encircles "
            "the neck, the other hand locks behind the head, and the "
            "chest expands to close the hold. It is applied slowly, "
            "released instantly on the tap, and treated with absolute "
            "respect - the strangle is the art's most serious technique "
            "and its most disciplined."
        ),
        "how_it_works": (
            "Take the partner's back in drilling: slide one forearm "
            "across the front of his neck, the crook of the elbow under "
            "his chin, and grip your own opposite biceps. Place your "
            "other hand behind his head, palm open, and draw the elbow "
            "of the choking arm inward while expanding your chest - the "
            "hold closes like a vice, slowly and without jerking. Apply "
            "pressure gradually and watch the partner's hand: the "
            "instant he taps, release completely. Never crank the neck "
            "sideways and never hold after the tap - the strangle is a "
            "sporting technique, and its safety is the whole art's "
            "reputation. Drill the entry (taking the back), the lock "
            "(the figure of the arms), and the release (instant, total) "
            "as three separate skills. In live training, the tap is "
            "sacred: tap early, tap often, and honor every tap you "
            "receive."
        ),
        "key_points": [
            "The strangle compresses the neck's blood vessels: the sporting finish that needs no strike.",
            "The rear choke is the foundation: forearm across the neck, biceps grip, hand behind the head.",
            "Pressure applies slowly and the release is instant: the tap is sacred and absolute.",
            "Never crank the neck and never hold past the tap: the technique's safety is the art's honor.",
            "Tap early and often in training: the strangle rewards the humble student and punishes the proud.",
        ],
        "requirements": [
            "Correct rear-choke figure: forearm, biceps grip, hand behind the head.",
            "Gradual pressure application and instant release on the tap.",
            "A training agreement: taps honored immediately, no exceptions.",
        ],
        "standards": [
            "Pausanias 8.40.1-2: Arrhichion caught in the stranglehold at Olympia.",
            "World Pankration Athlima Federation rules: strangles and tap-out protocol in modern competition.",
        ],
        "citations": [CIT_PAUSANIAS, CIT_WPAF, CIT_POLIAKOFF],
        "sig_lens": (
            "The Signature reading of the strangle: the silent clause of "
            "the oath. The Signature pankratiast applies apopnixis the "
            "way the covenant applies to the conscience - gradually, "
            "inescapably, and released the instant it is acknowledged. "
            "The tap is the opponent's signature on the verdict, and the "
            "Signature fighter honors every signature instantly. That "
            "honor is what separates the art from the assault."
        ),
    },
    {
        "key": "top_position",
        "name": "The Top Position: Ground Control",
        "group": "Ground Fighting",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The top position is the throne of the ground fight: chest-"
            "to-chest control over a prone opponent, the bodyweight "
            "distributed through the chest and hips to pin him flat. From "
            "the top, the pankratiast strikes downward, hunts for "
            "strangles and joint locks, and advances to more dominant "
            "posts - while the fighter beneath spends his strength "
            "merely surviving. The ancient bout went to the ground often, "
            "and the fighter who landed on top usually dictated what "
            "happened next. The keys are weight distribution (heavy "
            "through the chest, not perched on the knees), hip pressure "
            "(the hips pin his hips, killing his bridges), and head "
            "position (forehead heavy on his jaw or chest, never offering "
            "the neck). The top is not a place to rest; it is a place to "
            "work."
        ),
        "how_it_works": (
            "After a throw, follow the partner down: slide your chest "
            "across his chest, your hips heavy on his hips, your knees "
            "wide on the mat for base. Distribute your weight through "
            "your torso onto him - he should feel your chest like a sand-"
            "bag, not your knees like stilts. Place your forehead "
            "against his jaw or chest, keeping your own neck safe. Now "
            "work: with one hand, control his wrist; with the other, "
            "post for base. When he bridges, ride it - let your hips "
            "absorb the surge and settle heavier. When he turns, follow "
            "the turn and re-seat the chest. Drill the maintenance: "
            "partner on the bottom tries to escape for one minute while "
            "you hold the top with weight and hips, striking lightly to "
            "remind him the position has teeth. Heavy chest, killing "
            "hips, working hands."
        ),
        "key_points": [
            "Chest-to-chest with weight through the torso: the top pins with mass, not with muscle.",
            "Hips pin his hips: kill the bridge at its source and the escapes die unborn.",
            "Head heavy on his jaw or chest, your own neck never offered.",
            "The top is a workshop: strikes, strangles, and locks all launch from the pin.",
            "Ride the bridges and follow the turns: maintenance is movement, not stillness.",
        ],
        "requirements": [
            "Stable top hold for one minute against bridging and turning.",
            "Weight distributed through the chest with wide-knee base.",
            "Controlled downward striking and grip transitions from the top.",
        ],
        "standards": [
            "Poliakoff, Combat Sports in the Ancient World: ground fighting in the pankration bout.",
            "World Pankration Athlima Federation rules: ground positions and control in modern competition.",
        ],
        "citations": [CIT_POLIAKOFF, CIT_WPAF],
        "sig_lens": (
            "The Signature reading of the top position: the throne of "
            "the covenant. The Signature pankratiast holds the top the "
            "way the oath holds the fighter - with weight, not with "
            "anger; with presence, not with cruelty. Pan is the "
            "position's completeness: every finish reachable from here. "
            "Kratos is the distribution: the whole body sworn onto the "
            "task of control."
        ),
    },
    {
        "key": "escapes_beneath",
        "name": "Escapes from Beneath",
        "group": "Ground Fighting",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Every fighter visits the bottom; the trained fighter does "
            "not stay there. Escapes from beneath are the ground fight's "
            "emergency exits: the bridge, the hip escape, and the "
            "combinations that chain them. The bridge throws the hips "
            "skyward, bucking the top fighter's weight off its center; "
            "the hip escape - the shrimp - slides the hips out from "
            "under the pin and rebuilds the guard or the stand-up. The "
            "rule of escapes is timing: bridge when he is light, shrimp "
            "when he is heavy, and never waste strength pushing where he "
            "is strongest. The ancient pankratiast, fighting bouts that "
            "went to the ground as a matter of course, lived by these "
            "exits. The bottom is a problem to solve, and these are the "
            "solutions."
        ),
        "how_it_works": (
            "Start under a partner's top hold. For the bridge: plant "
            "both feet flat near your hips, and explode the hips "
            "straight up, throwing his weight toward your head - one "
            "sharp buck, timed for the moment his weight shifts light. "
            "For the hip escape: turn onto one side, plant the top foot, "
            "and shove your hips backward, sliding out from under his "
            "chest, then bring a knee across to rebuild a guard or "
            "stand. Chain them: bridge to create space, shrimp into the "
            "space, repeat. The rhythm is buck-and-slide, buck-and-"
            "slide, never a sustained shove. Drill with the partner "
            "giving half resistance, then three-quarter: escape, "
            "re-establish the guard or the feet, and reset. Two clean "
            "escapes in a row against honest resistance is the standard."
        ),
        "key_points": [
            "The bridge bucks his weight off-center; the hip escape slides your hips out of the pin.",
            "Timing rules: bridge when he is light, shrimp when he is heavy, never push his strength.",
            "Chain them: bridge makes the space, the shrimp takes it - buck-and-slide, repeated.",
            "Escapes are exits, not victories: the goal is the guard or the feet, then the fight resumes.",
            "Calm under the pin: panic spends the strength the escape needs.",
        ],
        "requirements": [
            "Explosive bridge timed to the partner's weight shifts.",
            "Hip escape rebuilding guard or stand-up.",
            "Chained bridge-to-shrimp escape against three-quarter resistance.",
        ],
        "standards": [
            "Poliakoff, Combat Sports in the Ancient World: ground reversals in the ancient bout.",
            "World Pankration Athlima Federation rules: escape and restart conventions.",
        ],
        "citations": [CIT_POLIAKOFF, CIT_WPAF],
        "sig_lens": (
            "The Signature reading of the escape: the oath's resilience. "
            "The Signature pankratiast treats the bottom not as defeat "
            "but as a clause to be answered - the bridge the oath's "
            "refusal to stay down, the shrimp its cleverness finding the "
            "way out. Pan is the calm that sees the exit; kratos is the "
            "explosion that takes it. The covenant is not that you never "
            "fall beneath; it is that you never remain there."
        ),
    },
    {
        "key": "striking_into_clinch",
        "name": "Striking into the Clinch",
        "group": "The Two Halves",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Striking into the clinch is the bridge made into a "
            "technique: punches and kicks thrown not to finish but to "
            "carry the fighter into the tie-up. The jab reaches and "
            "occupies the guard, the cross commits the opponent's "
            "attention, and the fighter steps through the punches into "
            "the collar tie - the strikes are the escort, the clinch is "
            "the destination. The ancient pankratiast needed this bridge "
            "constantly: the pure boxer kept him out with punches, the "
            "pure wrestler shot for his legs, and only the fighter who "
            "could strike his way into the grips could impose his game. "
            "The combinations are short - one-two into the tie, jab-cross-"
            "hook into the underhook - because long combinations belong "
            "to boxing, and this is pankration."
        ),
        "how_it_works": (
            "Face a partner at striking measure. Throw the jab at his "
            "guard - not to hurt, to occupy - and step forward with it. "
            "Throw the cross as the rear foot follows, and let the "
            "momentum of the cross carry your head to the inside as your "
            "lead hand converts to the collar tie behind his neck. You "
            "have struck your way into the clinch: two punches, one step, "
            "one grip. Drill the pattern: jab, cross, tie; jab, cross, "
            "tie. Then vary it: jab to the body (he drops his guard), "
            "cross upstairs, tie; or double jab (he covers high), step "
            "deep, underhook. The strikes must be honest - lazy punches "
            "do not occupy anyone - but they are the escort, not the "
            "mission. The mission is the grip, and the grip is the rest "
            "of the fight."
        ),
        "key_points": [
            "Strikes escort the entry: the jab occupies, the cross commits, the step arrives with the grip.",
            "Combinations stay short: one-two into the tie, jab-cross-hook into the underhook.",
            "The punches must be honest: lazy strikes occupy no one and the bridge collapses.",
            "Vary the road: high-low-high, double jab, body shot - same destination, different escort.",
            "The grip is the mission: every combination ends in the tie-up, never admiring its own work.",
        ],
        "requirements": [
            "Jab-cross-to-collar-tie entry with honest punches.",
            "Two varied entries (high-low, double jab) ending in the tie-up.",
            "No pause between the last punch and the grip: one continuous motion.",
        ],
        "standards": [
            "Poliakoff, Combat Sports in the Ancient World: the striking-to-grappling transition.",
            "World Pankration Athlima Federation rules: entries and clinch initiation.",
        ],
        "citations": [CIT_POLIAKOFF, CIT_WPAF],
        "sig_lens": (
            "The Signature reading of the bridge: the oath crossing "
            "itself. The Signature pankratiast strikes into the clinch "
            "the way the covenant crosses from word to deed - the "
            "punches the declaration, the grip the fulfillment. Pan is "
            "the combination's completeness, both halves in one motion; "
            "kratos is the arrival, the tie-up taken, not asked for."
        ),
    },
    {
        "key": "klimax",
        "name": "Klimax: The Ladder Hold",
        "group": "Submissions",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The klimax - the ladder - is the most famous hold of ancient "
            "pankration, named for the way the limbs interlace like the "
            "rungs of a ladder. Applied from behind or the side, the "
            "attacker's arm threads over the opponent's shoulder and "
            "locks, while the legs scissor around the opponent's body, "
            "rung upon rung, until the whole frame is trapped. Philostratus "
            "discusses the klimax as a signature technique of the "
            "pankratiast: a shoulder lock and control hold that could "
            "force the submission by threatening the joint and the "
            "posture at once. The hold's genius is its completeness - "
            "arms, legs, and body all woven into one structure, so the "
            "opponent fights the ladder, not the man. It is the advanced "
            "submission because it demands total body coordination: every "
            "limb has a rung to hold, and one loose limb is a broken "
            "ladder."
        ),
        "how_it_works": (
            "Take the partner's back standing. Thread your lead arm over "
            "his near shoulder, across his chest, and lock it to your "
            "other arm behind his far shoulder - the arm-rung is set. "
            "Step your near leg across his thigh and hook your far leg "
            "behind his far leg, scissoring your legs around his base - "
            "the leg-rungs are set. Drop your weight slightly and arch "
            "gently backward, drawing his posture with you; the interlaced "
            "frame tightens like a net. Hold the structure, not the "
            "squeeze: the klimax works by the geometry of the rungs, and "
            "muscling collapses the ladder you built. The partner taps "
            "when the shoulder and posture reach their limit - release "
            "instantly, as with every submission. Drill the assembly "
            "slowly: arm-rung, leg-rungs, weight-drop, arch. Four rungs, "
            "one ladder, zero force wasted."
        ),
        "key_points": [
            "The limbs interlace like ladder rungs: arm over the shoulder, legs scissored around the body.",
            "The hold attacks shoulder and posture together: the opponent fights the structure, not the man.",
            "Geometry does the work: hold the frame, do not muscle the squeeze, or the ladder collapses.",
            "Every limb has a rung: one loose limb is a broken ladder and the escape is born.",
            "The tap ends it instantly: the klimax is a sporting hold and its honor is the release.",
        ],
        "requirements": [
            "Correct arm-rung over the shoulder with the lock behind the far shoulder.",
            "Leg-rungs scissored around the partner's base.",
            "Controlled arch with instant release on the tap.",
        ],
        "standards": [
            "Philostratus Gymnasticus: the klimax as the pankratiast's signature hold.",
            "Poliakoff, Combat Sports in the Ancient World: the ladder hold in ancient sources.",
        ],
        "citations": [CIT_PHILOSTRATUS, CIT_POLIAKOFF],
        "sig_lens": (
            "The Signature reading of the klimax: the ladder of the oath "
            "itself. The Signature pankratiast weaves the hold the way "
            "the covenant is woven - rung upon rung, limb upon limb, "
            "until the structure stands on its own geometry. Pan is the "
            "ladder's completeness: every limb sworn to a rung. Kratos "
            "is the quiet of it: no straining, no muscling, the frame "
            "simply true. The opponent climbs down by tapping, and the "
            "Signature fighter lets him down gently."
        ),
    },
    {
        "key": "trachelos",
        "name": "Trachelos: Chokes from Behind",
        "group": "Submissions",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Trachelos is the neck, and chokes from behind are the "
            "crown of the pankration submission game. When the fighter "
            "takes the back - by turning the opponent in the clinch, by "
            "following a throw, or by scrambling from a failed throw - "
            "the neck lies open and the bout can end in seconds. The rear "
            "choke slides the forearm across the throat, the biceps grips "
            "the opposite arm, the free hand posts behind the head, and "
            "the chest expands to close the hold. The ancient bout knew "
            "this finish intimately: Arrhichion himself died in a "
            "stranglehold at Olympia, proof that the back-taken choke was "
            "the ancient game's ultimate argument. The advanced skill is "
            "not the squeeze but the taking of the back: the choke is the "
            "period at the end of a sentence written by positioning."
        ),
        "how_it_works": (
            "From the clinch, when the partner turns away or overcommits "
            "to a throw, slide to his back: chest to his back, one arm "
            "over each shoulder, your feet light. Slip the choking "
            "forearm across the front of his neck, the elbow's crook "
            "under his chin, and grip your own biceps with the choking "
            "hand. Place the free hand behind his head and draw the "
            "choking elbow inward as your chest expands - close the hold "
            "like a book, gradually. Watch his hand for the tap and "
            "release the instant it comes. Drill the sequence in three "
            "parts: taking the back (the entry), setting the figure (the "
            "lock), and the release (the honor). In training, the back "
            "is taken a hundred times and the choke finished rarely - "
            "position first, always, and the finish is a formality."
        ),
        "key_points": [
            "The back taken is the bout nearly won: the neck lies open and the finish is seconds away.",
            "The figure is forearm, biceps grip, hand behind the head, chest expanding: a closing book.",
            "Taking the back is the advanced skill; the squeeze is only the period at the sentence's end.",
            "Pressure closes gradually and the release is instant: the tap is sacred.",
            "Drill the entry a hundred times for every finish: position first, the choke is a formality.",
        ],
        "requirements": [
            "Back-taken position with chest-to-back control and arm figure set.",
            "Gradual closure with the tap watched for and honored instantly.",
            "Three clean back-takes from clinch scrambles without forcing the finish.",
        ],
        "standards": [
            "Pausanias 8.40.1-2: the stranglehold in Arrhichion's final bout.",
            "World Pankration Athlima Federation rules: back control and choke protocol.",
        ],
        "citations": [CIT_PAUSANIAS, CIT_WPAF, CIT_POLIAKOFF],
        "sig_lens": (
            "The Signature reading of the rear choke: the final clause. "
            "The Signature pankratiast takes the back the way the "
            "covenant takes hold of a life - completely, from behind the "
            "struggle, without announcement. Pan is the entry's "
            "patience: a hundred back-takes drilled for one finish. "
            "Kratos is the closure: gradual, inescapable, and released "
            "the instant it is acknowledged. The oath ends fights; it "
            "does not end fighters."
        ),
    },
    {
        "key": "arm_locks",
        "name": "Arm Locks and Joint Control",
        "group": "Submissions",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Arm locks attack the elbow and shoulder as levers: the "
            "joint is isolated, a fulcrum is placed against it, and "
            "controlled pressure extends it toward - never to - its "
            "limit. The straight arm lock pins the opponent's arm between "
            "the attacker's legs or across the body and bridges the hips "
            "to threaten the elbow; the shoulder lock threads the arm "
            "behind the back or across the chest and rotates it. The "
            "ancient pankratiasts bent joints as a matter of course - "
            "Sostratus of Sicyon was nicknamed for his finger locks - and "
            "the joint attack remains the ground game's great equalizer: "
            "leverage defeats strength when the lever is long enough. "
            "Every arm lock is applied with the same discipline as the "
            "strangle: slowly, with the tap watched for, released "
            "instantly, never cranked."
        ),
        "how_it_works": (
            "For the straight arm lock from the top: pin the partner's "
            "wrist to your chest, swing your near leg over his head, and "
            "sit back so his arm lies across your hips, thumb pointing "
            "up. Squeeze your knees tight to his body to isolate the arm, "
            "then bridge your hips upward slowly - the elbow extends over "
            "the fulcrum of your hips. The instant he taps, release and "
            "sit back. For the shoulder lock: from the side, thread his "
            "arm behind his back, grip your own wrist, and lift gently - "
            "the shoulder rotates toward its limit. Apply every lock at "
            "half speed in drilling, watching the partner's free hand "
            "for the tap. The lock is a question - will you concede the "
            "position? - and the tap is the answer. Never ask the "
            "question with a jerk, and never ignore the answer."
        ),
        "key_points": [
            "Joints are levers: isolate the arm, place the fulcrum, extend toward the limit - never to it.",
            "The straight arm lock bridges the hips under the elbow; the shoulder lock rotates the threaded arm.",
            "Leverage is the equalizer: a long lever defeats a strong arm, which is why the small fighter studies locks.",
            "Apply at half speed, watch the free hand, release instantly: the lock is a question, the tap the answer.",
            "Never jerk a lock and never ignore a tap: the joint attack is the art's most disciplined technique.",
        ],
        "requirements": [
            "Straight arm lock with correct fulcrum and isolation from the top.",
            "Shoulder lock with threaded arm and gentle rotation.",
            "Half-speed application with instant release on every tap.",
        ],
        "standards": [
            "Pausanias 6.4.6-7: Sostratus and the joint attacks of the ancient bout.",
            "World Pankration Athlima Federation rules: joint locks and tap protocol.",
        ],
        "citations": [CIT_PAUSANIAS, CIT_WPAF, CIT_POLIAKOFF],
        "sig_lens": (
            "The Signature reading of the arm lock: the lever of the "
            "oath. The Signature pankratiast extends the joint the way "
            "the covenant extends a claim - precisely, to the limit, "
            "never past it. Pan is the lock's geometry: every angle "
            "accounted for, nothing wasted. Kratos is the restraint: "
            "the power to break, sworn never to break. The tap is "
            "honored because the oath is stronger than the break."
        ),
    },
    {
        "key": "counters",
        "name": "Counters: Turning the Throw Against the Thrower",
        "group": "Strategy and History",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The counter is pankration's highest art: using the "
            "opponent's own attack as the raw material of his defeat. "
            "When he reaches for the clinch, the counter-fighter takes "
            "the underhook he offered and throws him with it. When he "
            "drives for the hip throw, the counter-fighter steps around "
            "the entry and takes his back. When he kicks, the counter-"
            "fighter catches the leg and sweeps the standing foot. Every "
            "counter has the same anatomy: read the attack, yield to its "
            "direction, and add your own force to his. The ancient "
            "champions were counter-fighters by necessity - in bouts with "
            "nearly no forbidden techniques, the fighter who answered "
            "force with force broke first, while the fighter who answered "
            "force with geometry lasted. To counter is to let the "
            "opponent write the first half of the sentence and then sign "
            "it yourself."
        ),
        "how_it_works": (
            "Drill the three master counters slowly with a cooperative "
            "partner. One: he reaches for your neck - swim your arm "
            "inside his, take the underhook he gave you, step across, "
            "and throw him with his own entry. Two: he turns for the hip "
            "throw - as his back turns, step your hips back and around, "
            "keep your underhook, and slide to his back as his throw "
            "dies empty. Three: he throws the round kick - catch the "
            "shin under your arm, step deep past his standing leg, and "
            "sweep it as you drive him backward over the missing foot. "
            "Each counter begins with the yield: do not meet his force, "
            "join it, then redirect it. Practice at quarter speed until "
            "the redirection is smooth, then add speed. The counter "
            "punishes commitment: the harder he attacks, the harder he "
            "falls."
        ),
        "key_points": [
            "Every counter shares one anatomy: read the attack, yield to its direction, add your force to his.",
            "His reach becomes your underhook; his turn becomes your back-take; his kick becomes your sweep.",
            "Yield first: meeting force with force breaks the counter-fighter, geometry saves him.",
            "Drill at quarter speed until the redirection is smooth; speed without smoothness is just collision.",
            "The counter punishes commitment: the harder the attack, the harder the fall.",
        ],
        "requirements": [
            "Three master counters (reach, turn, kick) demonstrated at quarter speed.",
            "Visible yield-and-redirect in each: no force-on-force meeting.",
            "Smooth redirection at half speed against honest attacks.",
        ],
        "standards": [
            "Poliakoff, Combat Sports in the Ancient World: counter-technique in ancient wrestling.",
            "Philostratus Gymnasticus: the experienced pankratiast's use of the opponent's motion.",
        ],
        "citations": [CIT_POLIAKOFF, CIT_PHILOSTRATUS],
        "sig_lens": (
            "The Signature reading of the counter: the oath's judo. The "
            "Signature pankratiast does not oppose the attack; he "
            "adopts it - signs his name beneath the opponent's sentence "
            "and makes it his. Pan is the reading: every attack seen "
            "whole, its direction understood. Kratos is the addition: "
            "his force plus yours, arriving where he never intended. "
            "The covenant does not resist the storm; it sails it."
        ),
    },
    {
        "key": "ground_striking",
        "name": "Ground Striking: The Downward Art",
        "group": "Ground Fighting",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Ground striking is what separates pankration's ground game "
            "from pure wrestling's: the top fighter does not merely hold "
            "the pin, he strikes downward through it. Short punches drop "
            "like hammers from the top position, elbows cut in the "
            "scramble, and the fighter beneath must defend the strikes "
            "while escaping the pin - two problems at once, which is the "
            "point. The downward punch is thrown with a short arc, the "
            "bodyweight falling behind it; gravity, useless in the "
            "standing fight, becomes an ally. The ancient bout, fought "
            "to submission or incapacitation, made ground striking a "
            "finishing art: the rain from above broke the guard, and the "
            "submission followed the break."
        ),
        "how_it_works": (
            "From the top position on a partner holding pads, post one "
            "hand on the mat for base and drop short punches with the "
            "other: raise the fist only six inches and let it fall, the "
            "shoulder and bodyweight driving it down, then post and punch "
            "with the other hand. The punches are short, heavy drops - "
            "no wind-up, because the wind-up unseats the base. When the "
            "partner bridges, ride the bridge and keep one punching; "
            "when he turns, follow and re-seat before resuming. Add the "
            "elbow: in the scramble, the short downward elbow drops onto "
            "the guard like a hammer. Drill in rounds: one minute of "
            "controlled ground striking from the top, partner defending, "
            "then switch. The standard is base first, strikes second - "
            "the moment the striking costs you the position, the art is "
            "lost."
        ),
        "key_points": [
            "The top fighter strikes downward: short hammer punches with the bodyweight falling behind them.",
            "Gravity becomes an ally on the ground: the drop does the work the wind-up did standing.",
            "Strikes and pin are one problem for the bottom fighter: defending both at once is the point.",
            "Base first, strikes second: the moment the punches cost the position, the art is lost.",
            "The ancient finish: the rain from above breaks the guard, and the submission follows the break.",
        ],
        "requirements": [
            "Short downward punches from the top with base maintained.",
            "Riding bridges and following turns without losing the position.",
            "One-minute controlled ground-striking round with base intact throughout.",
        ],
        "standards": [
            "Poliakoff, Combat Sports in the Ancient World: striking on the ground in the ancient bout.",
            "World Pankration Athlima Federation rules: ground striking in modern competition.",
        ],
        "citations": [CIT_POLIAKOFF, CIT_WPAF],
        "sig_lens": (
            "The Signature reading of ground striking: the rain of the "
            "oath. The Signature pankratiast strikes downward the way "
            "the covenant settles over a life - not in anger but in "
            "weight, each short punch a kept promise arriving from "
            "above. Pan is the position's completeness: pin and strike "
            "as one problem. Kratos is the drop: gravity sworn as an "
            "ally, the bodyweight delivered like weather."
        ),
    },
    {
        "key": "bout_plan",
        "name": "The Bout Plan: Pankration Strategy",
        "group": "Strategy and History",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The bout plan is the advanced fighter's map: the strategy "
            "that decides which techniques the bout will be fought with "
            "before the first grip. The plan starts with the read - is "
            "the opponent a striker, a wrestler, a counter-fighter? - and "
            "answers with the game: keep the striker at kicking measure "
            "or take him down, keep the wrestler at striking measure or "
            "beat him to the clinch, refuse the counter-fighter the "
            "attacks he wants. The plan paces the effort: the ancient "
            "bout could run long, so the pankratiast spent his strength "
            "in bursts and recovered in the clinch, never emptying the "
            "tank on a single exchange. And the plan has branches: if the "
            "takedown fails, the striking resumes; if the striking "
            "stalls, the clinch answers. The fighter with a plan fights "
            "one bout; the fighter without one fights a hundred "
            "separate accidents."
        ),
        "how_it_works": (
            "Write the plan before you spar, in three lines. Line one, "
            "the read: watch the partner's first minute - does he strike "
            "first, grip first, or wait? Line two, the game: choose your "
            "range and your first three techniques (for example: front "
            "kick to keep measure, jab-cross into the clinch, hip throw "
            "from the underhook). Line three, the branches: if he keeps "
            "you out, the answer is the turning kick and the level "
            "change; if he clinches first, the answer is the underhook "
            "battle and the trip. Spar the plan for one round, then "
            "review: which branch did you visit, and did the plan hold? "
            "Adjust one line and spar again. The plan is not a cage; it "
            "is a compass. The advanced fighter changes the plan between "
            "rounds, and the master changes it mid-round."
        ),
        "key_points": [
            "The plan is three lines: the read, the game, the branches - written before the first grip.",
            "Answer his style with your range: keep the striker out or take him down, beat the wrestler to the punch or the clinch.",
            "Pace in bursts and recover in the clinch: the long bout belongs to the measured fighter.",
            "Branches decide the fight: every plan needs its if-he-does-this answers.",
            "Review and adjust between rounds; the master adjusts mid-round: the plan is a compass, not a cage.",
        ],
        "requirements": [
            "A written three-line bout plan before sparring.",
            "One sparring round fought to the plan with a post-round review.",
            "One adjusted line and one adjusted round: the plan evolving under fire.",
        ],
        "standards": [
            "Philostratus Gymnasticus: the experienced pankratiast's strategic preparation.",
            "World Pankration Athlima Federation rules: round structure shaping modern bout strategy.",
        ],
        "citations": [CIT_PHILOSTRATUS, CIT_WPAF],
        "sig_lens": (
            "The Signature reading of the bout plan: the oath's map. "
            "The Signature pankratiast does not wander into the fight; "
            "he walks a road he drew himself - the read the survey, the "
            "game the sworn route, the branches the alternate roads of "
            "the covenant. Pan is the plan's completeness: every "
            "likely bout accounted for. Kratos is its execution: the "
            "map walked with the whole body. Accidents happen to the "
            "plan-less; the sworn arrive."
        ),
    },
    {
        "key": "arrhichion",
        "name": "The Stand of Arrhichion: The Lesson of 564 BC",
        "group": "Strategy and History",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Arrhichion of Phigalia is pankration's immortal lesson. At "
            "the Olympic Games of 564 BC - the 54th Olympiad, eighty-four "
            "years after pankration entered the program - Arrhichion "
            "reached the final and found himself caught in his opponent's "
            "stranglehold, the apopnixis closing around his neck. Dying, "
            "he did the one thing the hold left him: he wrenched his "
            "opponent's foot or ankle - the ancient accounts say he broke "
            "it - and the opponent, in agony, submitted. Arrhichion died "
            "in the sand and was crowned the victor: the only Olympic "
            "champion, Pausanias records, to win dead. The lesson is not "
            "recklessness - no training honors dying. The lesson is that "
            "the bout is never over while the mind still works: even in "
            "the strangle, even at the end, there is always one more "
            "technique. That is the advanced fighter's creed, and "
            "Arrhichion wrote it in 564 BC."
        ),
        "how_it_works": (
            "Study the lesson as a drill of the mind, not the body. "
            "Spar a round with a single rule: you may not quit any "
            "position until you have attempted two escapes. Caught in "
            "the clinch, you bridge and shrimp; caught on the bottom, "
            "you frame and turn; caught in a submission, you defend the "
            "hands and look for the one counter the hold leaves - the "
            "way Arrhichion found the foot. After the round, review: "
            "where did you stop thinking, and what was the technique you "
            "missed? Drill that missed technique ten times. The exercise "
            "trains the advanced skill the story teaches: the mind that "
            "keeps working when the body is beaten. Arrhichion's "
            "technique was the broken foot; yours will be the escape you "
            "refused to abandon. The bout is never over while the mind "
            "still works - train the mind to keep working."
        ),
        "key_points": [
            "564 BC, the 54th Olympiad: caught in the stranglehold, Arrhichion broke his opponent's foot and was crowned dead.",
            "Pausanias records him as the champion who won after death: the bout's most famous finish.",
            "The lesson is mental, not reckless: the bout is never over while the mind still works.",
            "Every bad position leaves one technique: the advanced fighter's job is to find it, as he found the foot.",
            "Train the never-quit mind with the two-escape rule: no position abandoned before two attempts.",
        ],
        "requirements": [
            "Knowledge of the Arrhichion account: 564 BC, the stranglehold, the broken foot, the crown.",
            "One sparring round under the two-escape rule.",
            "Post-round review identifying the abandoned technique, drilled ten times.",
        ],
        "standards": [
            "Pausanias 8.40.1-2: the full account of Arrhichion's final bout.",
            "Philostratus Gymnasticus: the stranglehold in the ancient bout.",
        ],
        "citations": [CIT_PAUSANIAS, CIT_PHILOSTRATUS],
        "sig_lens": (
            "The Signature reading of Arrhichion: the oath's final "
            "signature. The Signature pankratiast studies 564 BC the way "
            "a witness studies a sworn document - the stranglehold "
            "closing, the mind still working, the one technique found, "
            "the crown given to the dead. Pan is the lesson's "
            "totality: even the last moment holds a technique. Kratos is "
            "the refusal: the covenant does not end when the body ends; "
            "it ends when the mind surrenders, and the Signature mind "
            "does not surrender."
        ),
    },
    {
        "key": "sostratus",
        "name": "Sostratus the Finger-Fighter",
        "group": "Strategy and History",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Sostratus of Sicyon won the Olympic pankration three times - "
            "in 364, 360, and 356 BC, a reign of eight years - and earned "
            "the nickname Akrochersites, the finger-fighter: he was "
            "famous for seizing his opponents' fingers and bending them "
            "until they submitted. Pausanias records the nickname and the "
            "victories. The lesson of Sostratus is the small joint: while "
            "other fighters hunted the big throws and the grand "
            "strangles, he attacked the smallest lever on the body, and "
            "the small lever obeyed the same law as the large - "
            "isolation, fulcrum, pressure. The finger lock is the arm "
            "lock in miniature, and Sostratus proved that mastery of the "
            "small technique wins the large crown. Three Olympics, eight "
            "years, one nickname: the patient hunter of the small joint."
        ),
        "how_it_works": (
            "Study the small joint the way Sostratus did: as a lever "
            "like any other. With a cooperative partner, take his hand "
            "gently and isolate one finger, placing your thumb as the "
            "fulcrum at its base. Apply slow, minimal pressure toward "
            "the back of the hand - a fraction of what the elbow would "
            "take - and stop at the first sign of discomfort: the finger "
            "is fragile, and this is a study of principle, not a "
            "technique for hard sparring. Feel how little force the small "
            "lever needs, and understand the law it shares with the arm "
            "lock: isolate, fulcrum, pressure, tap. Then transfer the "
            "lesson upward: drill the wrist lock the same way - isolate "
            "the wrist, place the fulcrum, bend slowly - and feel the "
            "same law in the larger joint. Sostratus won three Olympics "
            "on the principle. Learn the principle; the crown is "
            "optional."
        ),
        "key_points": [
            "Three Olympic crowns - 364, 360, 356 BC - and the nickname Akrochersites, the finger-fighter.",
            "The small joint obeys the same law as the large: isolation, fulcrum, pressure, tap.",
            "The finger lock is the arm lock in miniature: study it to understand both.",
            "Fingers are fragile: the study is slow, minimal, and stopped at the first discomfort - principle, not sparring.",
            "Mastery of the small technique wins the large crown: patience hunts what power cannot catch.",
        ],
        "requirements": [
            "Knowledge of the Sostratus account: Sicyon, three victories, the nickname.",
            "Slow, minimal finger-isolation study with a cooperative partner.",
            "Transfer drill: the same isolation-fulcrum-pressure law applied to the wrist.",
        ],
        "standards": [
            "Pausanias 6.4.6-7: Sostratus of Sicyon, the Akrochersites.",
            "Poliakoff, Combat Sports in the Ancient World: joint attacks in the ancient bout.",
        ],
        "citations": [CIT_PAUSANIAS, CIT_POLIAKOFF],
        "sig_lens": (
            "The Signature reading of Sostratus: the oath's precision. "
            "The Signature pankratiast studies the finger-fighter the "
            "way the covenant studies the conscience - the smallest "
            "joint, the smallest compromise, given the full attention of "
            "the law. Pan is the eight-year reign: completeness proven "
            "across time. Kratos is the small lever: force so precise "
            "it barely needs to be force. Three crowns for the patient "
            "hunter - the Signature fighter hunts likewise."
        ),
    },
    {
        "key": "dioxippus",
        "name": "Dioxippus Against the Armed Soldier",
        "group": "Strategy and History",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Dioxippus the Athenian, an Olympic pankration champion, "
            "fought the most famous exhibition of the art's history. At "
            "a banquet of Alexander the Great, the Macedonian soldier "
            "Coragus - armed with spear, sword, and full armor - "
            "challenged him. Dioxippus came forward naked and oiled, "
            "carrying only a club, as Diodorus Siculus records. Coragus "
            "threw his javelin; Dioxippus dodged it. Coragus charged "
            "with his long spear; Dioxippus shattered the shaft with his "
            "club. Disarmed and closed with, the soldier was thrown to "
            "the ground, and Dioxippus set his foot on his neck. The "
            "lesson is the complete fighter's answer to the specialist: "
            "the armed man had one range and one plan, while the "
            "pankratiast - trained in all ranges, pan and kratos - "
            "changed the range until the plan broke. All-force beats "
            "single-force when the all-force fighter refuses the "
            "specialist's game."
        ),
        "how_it_works": (
            "Train the lesson as range-changing, not as weapon play. "
            "Spar with a partner given one advantage - longer reach, or "
            "the exclusive right to strike first - and your job is to "
            "refuse his game: change the range until his advantage "
            "vanishes. If he out-reaches you, strike your way into the "
            "clinch the way Dioxippus closed past the spear; if he "
            "rushes, meet him with the timed trip or the underhook "
            "battle. Drill the three range changes: long to clinch "
            "(strike in), clinch to ground (throw), ground to standing "
            "(escape up). After each round, name the range where you won "
            "and the range where you lost - the complete fighter wins in "
            "two ranges and survives the third. Dioxippus did not beat "
            "the spear by being better with the spear. He beat it by "
            "refusing to fight the spear's fight."
        ),
        "key_points": [
            "Diodorus records it: the naked, oiled pankratiast with a club against the fully armed Macedonian.",
            "The javelin dodged, the spear shattered, the soldier thrown and held: range changed until the plan broke.",
            "The complete fighter's answer to the specialist: refuse his game, impose the ranges he cannot fight.",
            "Train range-changing as the skill: long to clinch, clinch to ground, ground to standing.",
            "Win in two ranges, survive the third: that is the all-force fighter's arithmetic.",
        ],
        "requirements": [
            "Knowledge of the Dioxippus account: the banquet, Coragus, the club, the foot on the neck.",
            "Sparring rounds against a partner with a defined single advantage, changing ranges to neutralize it.",
            "Post-round range audit: ranges won, ranges lost, adjustments named.",
        ],
        "standards": [
            "Diodorus Siculus 17.100-101: the full account of Dioxippus and Coragus.",
            "Poliakoff, Combat Sports in the Ancient World: the exhibition bout in context.",
        ],
        "citations": [CIT_DIODORUS, CIT_POLIAKOFF],
        "sig_lens": (
            "The Signature reading of Dioxippus: the oath against the "
            "single weapon. The Signature pankratiast faces the "
            "specialist the way the covenant faces the single argument "
            "- not by meeting it on its ground but by being larger than "
            "it. Pan is the answer: all ranges, all techniques, the "
            "complete fighter. Kratos is the refusal: the spear's fight "
            "declined, the clinch's fight imposed. The oath is all-"
            "force; single-force breaks against it."
        ),
    },
    {
        "key": "modern_revival",
        "name": "The Modern Revival of Pankration",
        "group": "Origins and Rules",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Pankration never fully died - it slept in folk wrestling, "
            "in military training, and in the memory of the games - and "
            "in the twentieth century it woke. Modern pankration is "
            "practiced as an amateur combat sport: striking and grappling "
            "combined, fought in rounds, with protective gear, weight "
            "classes, referees, and a ruleset that preserves the ancient "
            "spirit - all-force fighting - inside modern safety. The "
            "World Pankration Athlima Federation governs international "
            "competition with technical regulations covering legal "
            "techniques, scoring, and conduct. Greece's armed forces "
            "preserve a military pankration tradition as well. The "
            "revival closes the circle this database opened in 648 BC: "
            "the all-force art, taught ladder-wise from stance to "
            "strategy, belongs to the modern fighter exactly as it "
            "belonged to the ancient one. Pan and kratos did not expire; "
            "they were waiting."
        ),
        "how_it_works": (
            "Enter the modern art the way the ancients entered the old: "
            "through the ladder. Begin with a registered club or "
            "federation program and learn the modern ruleset first - "
            "rounds, legal targets, scoring, the referee's commands - "
            "because the modern bout is a sport with a rulebook, not the "
            "ancient near-no-rules contest. Train the foundations of "
            "this database in order: stance, guard, footwork, the two "
            "halves, the falls, the conditioning. Spar lightly with "
            "protective gear, drilling the compounded techniques before "
            "any hard rounds. Compete when your coach agrees you are "
            "ready, starting at the novice level, and treat every bout "
            "as a lesson regardless of the result. The revival is not a "
            "costume: it is the ancient art alive under modern rules, "
            "and it asks the same price the skamma always asked - "
            "deliberate feet, honest effort, and respect for the "
            "opponent."
        ),
        "key_points": [
            "The twentieth-century revival: amateur combat sport, rounds, gear, weight classes, referees.",
            "The World Pankration Athlima Federation governs international competition and technical rules.",
            "Greece's armed forces preserve a military pankration tradition alongside the sport.",
            "Enter through the ladder: ruleset first, foundations in order, light sparring before hard rounds.",
            "The circle closes: the all-force art of 648 BC belongs to the modern fighter under modern rules.",
        ],
        "requirements": [
            "Knowledge of the modern ruleset: rounds, legal targets, scoring, referee commands.",
            "Training under qualified supervision with protective gear.",
            "Foundations mastered in ladder order before hard sparring or competition.",
        ],
        "standards": [
            "World Pankration Athlima Federation: Competition Rules and Technical Regulations, current edition.",
            "Philostratus Gymnasticus: the ancient training ladder the revival preserves.",
        ],
        "citations": [CIT_WPAF, CIT_PHILOSTRATUS, CIT_MILLER],
        "sig_lens": (
            "The Signature reading of the revival: the oath renewed. "
            "The Signature pankratiast sees the modern revival not as a "
            "new art but as the old covenant re-sworn - pan and kratos "
            "spoken again after two thousand years, in gear and under "
            "lights instead of in sand under the sun. The ladder is "
            "unchanged because the oath is unchanged: stance, guard, "
            "two halves, bridge, pressure. What was sworn in 648 BC is "
            "sworn again every time a modern fighter ties up. The art "
            "waited; the waiting is over."
        ),
    },
]
