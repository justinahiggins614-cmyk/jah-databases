#!/usr/bin/env python3
"""Entries for the Snake Kung Fu Combat databases (combat batch 4).

Shequan (snake fist) - one of the five animal styles of Chinese kung fu -
imitates the serpent: finger strikes like a striking head, coiling
evasions, low stances, whipping waist power, and classical vital-point
(dianxue) theory taught as educational anatomy. This build creates two
NEW databases, 34 ladder-ordered records each:

  combat-snake-kung-fu             - Snake Kung Fu Combat Database
                                     (public-harvest: real, fact-checked
                                     snake style - She Quan - snake hand
                                     and finger strikes, coiling evasions,
                                     low stances, vital-point striking
                                     theory in educational anatomy context,
                                     snake forms in sequence, chi
                                     development exercises, applications;
                                     every record a full technique with
                                     step-by-step how-to; standard
                                     references Shahar The Shaolin
                                     Monastery 2008; Wong Kiew Kit The Art
                                     of Shaolin Kung Fu 2002; Yang
                                     Jwing-Ming Shaolin Long Fist Kung Fu
                                     2008 and The Root of Chinese Qigong
                                     1997; Chow and Spangler Kung Fu 1982;
                                     Smith Chinese Boxing 1974; Clark
                                     Pressure Point Fighting 2001; Reid
                                     and Croucher The Way of the Warrior
                                     1983)
  combat-snake-kung-fu-signature  - Snake Kung Fu Combat Signature
                                     Database
                                     (his original Signature Serpent
                                     Method: every coil a signed circuit,
                                     every strike a signature written in
                                     motion, the serpent the seal of the
                                     system; src signature, titles suffixed
                                     " (Signature Edition)", never
                                     presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written
in ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CBSNK- (public) and JAH-CBSNKS- (signature), verified
free in the manifest id_prefix values and across every shard index of
jah-databases-data-1 (zero hits for "JAH-CBSNK"). Slugs
combat-snake-kung-fu and combat-snake-kung-fu-signature verified absent
from the manifest. Dedupe gate passes: no dedicated snake kung fu
database exists anywhere in the system (the Shaolin database mentions
snake once as one of the five animals only).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_snake_kung_fu.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Civilian traditional-art scope: traditional snake style instruction for
practice, sport, and study. Vital-point theory is educational anatomy
only; all partner drills are no-contact. No religious talk. Never the
words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Serpent Method: "
            "every coil a signed circuit, every strike a signature written "
            "in motion, the serpent the seal of the system. Clearly "
            "labeled Signature-made, never presented as authentic public "
            "record.")

CIT_SHAHAR = ("Shahar M. The Shaolin Monastery: History, Religion, and the "
              "Chinese Martial Arts. University of Hawaii Press; 2008.")
CIT_WONG = ("Wong Kiew Kit. The Art of Shaolin Kung Fu. Tuttle Publishing; "
            "2002.")
CIT_YANG = ("Yang Jwing-Ming. Shaolin Long Fist Kung Fu. YMAA Publication "
            "Center; 2008.")
CIT_YANG_QIGONG = ("Yang Jwing-Ming. The Root of Chinese Qigong: Secrets "
                   "for Health, Longevity, and Enlightenment. YMAA "
                   "Publication Center; 1997.")
CIT_CHOW = ("Chow D, Spangler R. Kung Fu: History, Philosophy, and "
            "Technique. Unique Publications; 1982.")
CIT_SMITH = ("Smith RW. Chinese Boxing: Masters and Methods. Kodansha "
             "International; 1974.")
CIT_CLARK = ("Clark R. Pressure Point Fighting: A Guide to the Secret "
             "Heart of Asian Martial Arts. Tuttle Publishing; 2001.")
CIT_REID = ("Reid H, Croucher M. The Way of the Warrior: The Paradox of "
            "the Martial Arts. Overlook Press; 1983.")

ENTRIES = [
    {
        "key": "salute",
        "name": "The Snake Salute (She Quan Li)",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Every snake style session opens the way a serpent greets the "
            "morning sun: still, low, and attentive. The she quan li, the "
            "snake salute, is the bow that frames all snake training. The "
            "practitioner stands with feet together, raises both hands to "
            "chest height - the right hand shaped into the snake head, the "
            "left palm covering it like scales over the body - and bows "
            "the head and waist about fifteen degrees. Shequan, the snake "
            "fist, is one of the five animal styles of Chinese kung fu, "
            "practiced in both northern and southern schools and "
            "popularized worldwide by the 1978 film Snake in the Eagles "
            "Shadow. Its signature is imitation of the serpent: finger "
            "strikes that dart like a striking head, a body that coils "
            "and uncoils, footwork that glides, and attacks aimed with "
            "precision rather than force. The salute teaches the first "
            "lesson of the style - the snake never wastes motion - and it "
            "takes about two and a half seconds: raise the hands together, "
            "hold a half beat, bow, hold, rise, repeated three times at "
            "the opening and closing of practice."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: stand with feet together, weight even, "
            "spine tall, arms relaxed. Step 2: raise both hands to chest "
            "height at the same time - shape the right hand into the "
            "snake head (fingers together and slightly cupped, thumb "
            "tucked) and lay the open left palm over it. Step 3: hold the "
            "joined hands one fist-width from the chest for a half beat, "
            "eyes forward, breathing steady. Step 4: bow the head and "
            "upper body forward about fifteen degrees while the hands "
            "stay fixed at chest height. Step 5: hold the bow for one "
            "full breath. Step 6: rise back to the joined-hands position, "
            "then lower the hands to the sides. The common errors are "
            "separating the finger shapes so the snake head collapses, "
            "bowing only the neck instead of the waist, and rushing so "
            "the salute becomes a nod. Practice three unhurried salutes "
            "at the start and end of every session until the hands meet "
            "in exactly the same place every time."
        ),
        "key_points": [
            "The snake salute frames every session: right hand in snake head shape, left palm covering it, at chest height.",
            "Shequan is one of the five animal styles; its signature is finger strikes, coiling, gliding footwork, and precision over force.",
            "The full gesture - raise, hold, bow fifteen degrees, hold one breath, rise - takes about two and a half seconds.",
            "Three unhurried salutes open and close practice, teaching the first lesson: the snake never wastes motion.",
            "Precision matters more than speed: the hands must meet in exactly the same place every time.",
        ],
        "requirements": [
            "A clear floor space and a settled standing posture with feet together before the hands move.",
            "Right hand shaped into the snake head: fingers together, slightly cupped, thumb tucked against the palm.",
            "Left palm open with fingers together, laid over the right hand like scales over the body.",
            "A bow of about fifteen degrees from the head and upper body, hands unmoving at chest height.",
            "Three slow repetitions at the opening and closing of each training session.",
        ],
        "standards": [
            "The snake head hand shape stays crisp through the whole salute, never collapsing into a loose fist.",
            "The bow comes from the waist, not the neck alone, and the hands do not drift up or down.",
            "Each salute matches the last: same hand position, same timing, same depth of bow.",
        ],
        "citations": [CIT_SHAHAR, CIT_WONG, CIT_REID],
        "sig_lens": (
            "The Signature read: the salute is the serpent signing its "
            "name before it writes anything with force. Where public "
            "teaching files etiquette, the Signature method files a "
            "covenant - stillness first, motion second, waste never."
        ),
    },
    {
        "key": "rest",
        "name": "Snake Resting Posture (She Xi Zhuang)",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Before the snake strikes it rests - coiled, low, breathing "
            "slowly, every muscle available but none spent. The she xi "
            "zhuang, the snake resting posture, is the standing "
            "meditation of snake style: feet shoulder-width apart, knees "
            "softly bent, the torso settled low as if draped over the "
            "legs, arms hanging with the hands in loose snake shapes. "
            "The student holds the posture for three to five minutes, "
            "breathing on a quiet cadence - in for four counts, a brief "
            "pause, out for six - which gives a twelve-second cycle and "
            "twenty-five complete cycles in five minutes. The resting "
            "posture trains the two foundations every later snake "
            "technique depends on: a low, rooted base that can uncoil "
            "instantly, and the calm that lets the body move without "
            "tension. Watch a real snake and the lesson is plain: "
            "stillness is not the absence of readiness, it is readiness "
            "at its most efficient."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: place the feet shoulder-width apart "
            "with the toes pointing slightly outward, and settle the "
            "weight evenly across both feet. Step 2: bend the knees "
            "softly and sink the hips until the thighs take the weight - "
            "low enough to feel the legs working, high enough to stand "
            "for minutes. Step 3: let the torso drape naturally, chest "
            "relaxed, the crown of the head drawn gently upward so the "
            "spine stays long. Step 4: drop the shoulders and let the "
            "arms hang with the hands in loose snake shapes, fingers "
            "together and relaxed. Step 5: begin the breath cadence - "
            "breathe in through the nose for four slow counts, pause for "
            "two, breathe out through the nose for six counts, feeling "
            "the belly rise and fall. Step 6: hold for three minutes at "
            "first, adding a minute each week, keeping the gaze soft and "
            "forward. If the legs tremble, breathe into the trembling "
            "and settle deeper rather than rising up."
        ),
        "key_points": [
            "Feet shoulder-width, knees softly bent, hips sunk: a low rooted base that can uncoil instantly.",
            "The breath cadence is in for four counts, pause for two, out for six: a twelve-second cycle.",
            "Five minutes of resting posture gives twenty-five complete breath cycles.",
            "Stillness is trained as efficiency, not passivity: every muscle available, none spent.",
            "Build from three minutes toward ten; trembling legs are met with breath, not with standing up.",
        ],
        "requirements": [
            "A clear floor space and footwear that lets the feet grip, or bare feet on a safe surface.",
            "Knees tracking over the toes, never caving inward, while the hips sink.",
            "Shoulders dropped away from the ears and the chest relaxed, not puffed.",
            "The four-two-six breath cadence counted silently, never forced or gasped.",
            "Three minutes minimum at first, lengthening one minute per week of steady practice.",
        ],
        "standards": [
            "The spine stays long and the head level through the whole hold - no craning forward.",
            "The breath never breaks cadence to accommodate discomfort; discomfort is breathed through.",
            "Each session matches the last in depth of stance and evenness of breath.",
        ],
        "citations": [CIT_WONG, CIT_YANG_QIGONG],
        "sig_lens": (
            "The Signature read: the resting posture is the coil before "
            "the signature is written. Public teaching calls it standing "
            "meditation; the Signature method calls it charging the "
            "circuit - the lower the coil, the faster the release."
        ),
    },
    {
        "key": "tongue-hand",
        "name": "Snake Tongue Hand Formation (She She Shou)",
        "group": "Hand Forms",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The most famous hand of snake style is the she she shou, "
            "the snake tongue hand: the index and middle fingers extended "
            "together like a serpents flicking tongue, the remaining "
            "fingers folded tight, the thumb pressed over them for "
            "support. In classical snake theory these two fingers dart "
            "like a tongue to precise targets - the eyes, the throat "
            "hollow, the soft points of the face - which is why the "
            "formation is drilled for precision before it is ever drilled "
            "for speed. The striking surface is narrow, about four "
            "centimeters across two trained fingers, so alignment is "
            "everything: the two fingers must extend on exactly the "
            "same line as the forearm, or the wrist takes the shock "
            "instead of the target. Students first learn the shape "
            "statically, then hold it against light resistance - ten "
            "seconds per hold, six holds per hand, both hands, two "
            "minutes of formation drilling - until the fingers hold "
            "their line without shaking."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: open the hand and extend the index "
            "and middle fingers together, pressing them side by side so "
            "no gap shows between them. Step 2: fold the ring and little "
            "fingers tightly into the palm and press the thumb firmly "
            "over them, locking the folded fingers down. Step 3: align "
            "the two extended fingers with the bones of the forearm - "
            "sight down the arm and adjust until fingers, wrist, and "
            "forearm form one straight line with no bend at the wrist. "
            "Step 4: tense the fingers just enough to hold the line, "
            "then release halfway: the shape must be firm, not rigid. "
            "Step 5: practice the formation drill - press the fingertips "
            "lightly against a wall, hold ten seconds keeping the line "
            "straight, rest, and repeat six times per hand, both hands. "
            "Step 6: check the shape in a mirror from the side; any "
            "wrist bend or finger separation means the formation is not "
            "ready for striking drills. The common errors are letting "
            "the two fingers split apart, bending the wrist upward, and "
            "clenching the whole hand white-knuckle tight."
        ),
        "key_points": [
            "Index and middle fingers extended together like a flicking tongue; ring and little fingers folded, thumb locking them.",
            "The striking surface is narrow - about four centimeters - so finger-forearm alignment is everything.",
            "Classical theory aims the tongue hand at precise soft targets, which is why precision is drilled before speed.",
            "Formation drill: ten-second wall presses, six holds per hand, both hands, two minutes total.",
            "A bent wrist or separated fingers means the formation is not ready for striking work.",
        ],
        "requirements": [
            "Healthy fingers and wrists with no current injury before any resistance drilling.",
            "The two extended fingers pressed together with no visible gap between them.",
            "Thumb pressed firmly over the folded fingers to lock the formation.",
            "A straight finger-to-forearm line verified in a mirror from the side.",
            "Ten-second holds, six per hand, practiced slowly before any speed is added.",
        ],
        "standards": [
            "The two fingers hold their line without shaking through the full ten-second hold.",
            "No wrist bend in any direction during the press; the shock path runs straight through the forearm.",
            "Both hands match: the formation looks identical left and right.",
        ],
        "citations": [CIT_WONG, CIT_CHOW, CIT_SMITH],
        "sig_lens": (
            "The Signature read: two fingers are a finer pen than five. "
            "Where the fist signs in broad strokes, the tongue hand "
            "signs in fine print - and the Signature method trains the "
            "fine print first, because precision is the harder signature "
            "to forge."
        ),
    },
    {
        "key": "snake-head-palm",
        "name": "Snake Head Palm (She Tou Zhang)",
        "group": "Hand Forms",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "If the tongue hand is the serpents darting tongue, the she "
            "tou zhang, the snake head palm, is the serpents head: the "
            "hand held open with the fingers together and slightly "
            "cupped, the wrist cocked back so the edge and heel of the "
            "hand lead, shaped like a cobras flared hood. The snake "
            "head palm strikes with a whipping snap of the wrist - the "
            "forearm delivers, the wrist flicks through the last forty-"
            "five degrees, and the hand lands like the head of a "
            "striking snake. It is the broader tool beside the tongue "
            "hand: where the two fingers pick a point, the snake head "
            "palm covers an area, used for deflecting incoming limbs and "
            "for striking with the outer edge of the hand. The formation "
            "drill is twelve slow wrist snaps per hand, twenty-four "
            "total, each snap traveling the full forty-five degrees - "
            "one thousand and eighty degrees of whip in a single round - "
            "practiced in the air with no target until the snap is "
            "crisp and the wrist stays pain-free."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: open the hand with the fingers "
            "together and slightly cupped, as if holding a small ball, "
            "thumb relaxed against the side of the hand. Step 2: cock "
            "the wrist back about forty-five degrees so the heel of the "
            "palm and the outer edge lead. Step 3: extend the arm toward "
            "the target line with the elbow soft, the forearm doing the "
            "carrying. Step 4: at the last instant, snap the wrist "
            "forward through its forty-five degrees so the hand whips "
            "like a striking head - the power comes from the snap, not "
            "from arm muscle. Step 5: return instantly along the same "
            "path, the hand recoiling like a serpent withdrawing. Step "
            "6: drill twelve slow snaps per hand in the air, watching "
            "that the wrist tracks straight with no sideways wobble. "
            "The common errors are muscling the strike with the shoulder "
            "so the wrist snap disappears, over-cocking the wrist past "
            "comfort, and leaving the hand out after the strike instead "
            "of recoiling."
        ),
        "key_points": [
            "Open hand, fingers together and slightly cupped, wrist cocked back: the shape of a striking serpent head.",
            "Power comes from the last forty-five degrees of wrist snap, not from shoulder muscle.",
            "The broader tool beside the tongue hand: covers an area, deflects limbs, strikes with the hand edge.",
            "Drill: twelve slow snaps per hand, twenty-four total, one thousand eighty degrees of whip per round.",
            "The hand recoils instantly along its path, like a serpent withdrawing after the strike.",
        ],
        "requirements": [
            "Healthy wrists with full pain-free range of motion before snap drilling.",
            "Fingers together and slightly cupped through the whole motion, never splaying.",
            "The wrist cocked back about forty-five degrees at the ready, no further.",
            "Air-only practice until the snap is crisp and the wrist stays comfortable.",
            "Twelve controlled snaps per hand per round, both hands trained equally.",
        ],
        "standards": [
            "The wrist tracks straight through the snap with no sideways wobble.",
            "The recoil is as fast as the strike - the hand never lingers at full extension.",
            "No shoulder muscling: the arm carries, the wrist delivers.",
        ],
        "citations": [CIT_WONG, CIT_CHOW],
        "sig_lens": (
            "The Signature read: the palm is the serpents hood, flared "
            "to be seen. Public teaching uses it to cover area; the "
            "Signature method uses it to sign broadly first, so the "
            "fine print of the tongue hand lands inside a signature "
            "already written."
        ),
    },
    {
        "key": "waist-coils",
        "name": "Serpent Waist Warmup (She Yao)",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "A snakes power lives in its coils, and a snake stylists "
            "power lives in the waist. The she yao, the serpent waist "
            "warmup, is the daily loosening of the bodys coiling engine: "
            "standing in a comfortable stance, the practitioner circles "
            "the waist through its full range - forward, side, back, "
            "side - as if drawing rings with the navel. Nine full "
            "rotations in each direction, eighteen rotations totaling "
            "six thousand four hundred eighty degrees of waist travel, "
            "take about seventy-two seconds at four seconds per circle. "
            "The drill teaches the core mechanic of the entire style: "
            "the waist leads and the limbs follow. Punches, deflections, "
            "and evasions in snake style all begin as a turn of the "
            "waist, the way a serpents strike begins as a ripple through "
            "its coils. Stiff waists make stiff snake stylists; the "
            "warmup is never skipped, because every technique in this "
            "database is waist-driven."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: stand with feet a comfortable width "
            "apart, knees soft, hands resting lightly on the hips. Step "
            "2: begin circling the waist slowly - push the hips forward, "
            "roll them to the right side, draw them back, roll them to "
            "the left side, and return forward: one full ring drawn with "
            "the navel. Step 3: keep the shoulders level and the head "
            "still; the movement belongs to the waist alone, not a "
            "leaning of the torso. Step 4: complete nine slow rotations "
            "clockwise, about four seconds per circle, breathing "
            "naturally. Step 5: reverse and complete nine rotations "
            "counterclockwise. Step 6: finish by standing still for three "
            "breaths, feeling the warmth and looseness in the waist and "
            "lower back. The common errors are rushing the circles so "
            "they become hip wiggles, leaning the shoulders with the "
            "turn, and holding the breath. If the lower back complains, "
            "make the circles smaller, never force the range."
        ),
        "key_points": [
            "Nine rotations each direction, eighteen total, six thousand four hundred eighty degrees of waist travel.",
            "Four seconds per circle: the full warmup takes about seventy-two seconds.",
            "The waist leads and the limbs follow - the core mechanic of the entire snake style.",
            "Shoulders stay level and the head still; the rings are drawn by the waist alone.",
            "A snakes power lives in its coils; a snake stylists power lives in the waist.",
        ],
        "requirements": [
            "A healthy lower back; any sharp pain means smaller circles or stopping.",
            "Feet planted and knees soft so the waist can move freely above a stable base.",
            "Hands resting lightly on the hips to feel the rings the waist is drawing.",
            "Nine slow rotations per direction, about four seconds each, breathing naturally.",
            "Shoulders level throughout - no leaning the torso with the turn.",
        ],
        "standards": [
            "Each rotation is a full smooth ring with no hitches or flat spots.",
            "The head stays still and level; only the waist draws the circles.",
            "Both directions feel equally smooth - no favored side.",
        ],
        "citations": [CIT_WONG, CIT_YANG_QIGONG],
        "sig_lens": (
            "The Signature read: the waist is the hinge of the "
            "signature. Public teaching warms it up; the Signature "
            "method winds it up - eighteen rings wound tight, so that "
            "every later technique is simply the coil being allowed to "
            "spring."
        ),
    },
    {
        "key": "finger-conditioning",
        "name": "Finger Conditioning Basics (Zhi Gong)",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Snake style strikes with the fingers, so snake style must "
            "build the fingers. The zhi gong, finger conditioning "
            "basics, is the entry-level strengthening every snake "
            "stylist completes before striking anything harder than air: "
            "fingertip pushups on the knees, finger extensions against a "
            "wall, and grip-and-release drills that teach the hand to "
            "snap between soft and hard. The beginner ladder runs six "
            "weeks: five fingertip pushups per hand in week one, then "
            "eight, ten, twelve, fifteen, and twenty - seventy pushups "
            "per hand across the ladder, each week consolidating before "
            "the next begins. Conditioning is patient work measured in "
            "months, not sessions, and the iron rule is pain-free "
            "progress: dull effort is training, sharp pain is damage, "
            "and the two are never confused. Rushed fingers break; "
            "patient fingers become the striking tools the style "
            "requires."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: kneel and place the fingertips of "
            "one hand on the floor, fingers spread, wrist straight, "
            "weight shared with the knees - this is the start position "
            "for fingertip pushups. Step 2: lower the chest toward the "
            "floor by bending the arms, keeping the fingers straight "
            "and the wrist unbent, then press back up: one fingertip "
            "pushup. Step 3: perform the weeks quota - five per hand in "
            "week one - resting fully between hands. Step 4: add the "
            "wall drill: press the fingertips against a wall at chest "
            "height, lean in until the fingers take firm load, hold ten "
            "seconds, release; repeat five times. Step 5: finish with "
            "grip-and-release: squeeze the hand into a tight fist for "
            "three seconds, then snap it open with fingers spread wide; "
            "ten repetitions. Step 6: each week add the next rung - "
            "eight, ten, twelve, fifteen, twenty - only if the previous "
            "week was completed with zero sharp pain. The common errors "
            "are bending the wrists during pushups, skipping weeks to "
            "chase numbers, and training through sharp pain."
        ),
        "key_points": [
            "Six-week ladder: five, eight, ten, twelve, fifteen, twenty fingertip pushups per hand - seventy total.",
            "Wall presses, grip-and-release snaps, and fingertip pushups form the basic conditioning trio.",
            "Dull effort is training; sharp pain is damage - the two are never confused.",
            "A new rung is earned only by a pain-free week on the current rung.",
            "Rushed fingers break; patient fingers become the tools the style requires.",
        ],
        "requirements": [
            "Healthy fingers, wrists, and elbows with no current injury.",
            "A floor surface that will not slip under the fingertips.",
            "Fingertips placed with fingers spread and wrists straight during pushups.",
            "The weekly quota completed with zero sharp pain before advancing.",
            "Rest days between hard sessions - conditioning grows during recovery.",
        ],
        "standards": [
            "Every pushup keeps the fingers straight and the wrist unbent from start to finish.",
            "No rung is skipped and no week is repeated under pain.",
            "Both hands advance together - no favored hand in conditioning.",
        ],
        "citations": [CIT_YANG, CIT_CHOW],
        "sig_lens": (
            "The Signature read: conditioning is the slow signing of "
            "the contract between will and bone. Public teaching "
            "counts pushups; the Signature method counts promises kept "
            "- seventy per hand, each one a line of the signature "
            "written into the fingers themselves."
        ),
    },
    {
        "key": "snake-step",
        "name": "Snake Step Gliding Footwork (She Xing Bu)",
        "group": "Stances and Steps",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "A snake does not march; it flows. The she xing bu, the "
            "snake step, is the gliding footwork of the style: the feet "
            "stay low and close to the floor, each step sliding forward "
            "about half a meter with the weight transferring smoothly, "
            "no bobbing of the head, no stomping of the heel. Forty "
            "gliding steps cover twenty meters of floor in about sixty "
            "seconds - slow, silent, level practice that teaches the "
            "legs to move without disturbing the bodys aim. In "
            "application the glide lets the stylist close distance "
            "without telegraphing: the upper body stays perfectly still "
            "while the feet flow underneath, so a strike seems to arrive "
            "from nowhere. Beginners practice in straight lines; the "
            "glide later curves, weaves, and circles, but the rule never "
            "changes - the head must ride at one height, like a snakes "
            "head gliding over grass."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: settle into a medium snake stance, "
            "weight even, head level. Step 2: slide the front foot "
            "forward about half a meter, keeping the sole close to the "
            "floor - imagine pushing a sheet of paper along the ground "
            "without wrinkling it. Step 3: transfer the weight smoothly "
            "onto the front foot as it lands, the head staying at "
            "exactly the same height. Step 4: draw the rear foot up "
            "behind, sliding rather than stepping, until the stance is "
            "restored. Step 5: repeat down the length of the floor: "
            "forty steps, twenty meters, about sixty seconds, silent. "
            "Step 6: turn and glide back, then practice the retreat - "
            "the same glide in reverse. The common errors are lifting "
            "the feet high like marching, letting the head bob with "
            "each step, and stomping the landing. A useful check: "
            "balance a light book on the head for the first ten steps; "
            "if it falls, the glide is not level."
        ),
        "key_points": [
            "Feet stay low and close to the floor; each step slides about half a meter.",
            "Forty gliding steps cover twenty meters in about sixty seconds of silent practice.",
            "The head rides at one constant height - no bobbing, like a snakes head over grass.",
            "The upper body stays still while the feet flow, so distance closes without telegraphing.",
            "Straight-line glides come first; curves, weaves, and circles come later.",
        ],
        "requirements": [
            "A smooth floor at least ten meters long for the glide line.",
            "Footwear with flat soles, or bare feet on a safe surface.",
            "A settled medium stance before the first step - no starting from standing.",
            "Forty steps per round, twenty meters, practiced at slow silent speed.",
            "A light book balanced on the head for the first ten steps as a level check.",
        ],
        "standards": [
            "The head height does not vary through the whole forty steps.",
            "No foot lifts higher than a sheets thickness off the floor.",
            "The glide is silent - stomping or scuffing means the weight transfer is abrupt.",
        ],
        "citations": [CIT_WONG, CIT_SMITH],
        "sig_lens": (
            "The Signature read: the glide is the signature written "
            "without lifting the pen. Public teaching practices "
            "footwork; the Signature method practices invisibility - "
            "twenty meters crossed, and the stillness of the upper "
            "body denies that any distance was traveled at all."
        ),
    },
    {
        "key": "coil-deflect",
        "name": "Coiling Forearm Deflection (Chan Rao Shou)",
        "group": "Coiling and Evasion",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The snake does not meet force with force; it slides around "
            "it. The chan rao shou, the coiling forearm deflection, is "
            "snake styles first defensive answer: as an attack travels "
            "down its line, the forearm spirals around the incoming limb "
            "and guides it past the body, turning a ninety-degree "
            "incoming angle into a thirty-degree miss - sixty degrees "
            "of redirection bought with a turn of the wrist, not a "
            "shove of the shoulder. The contact is brief and sliding, "
            "like a snake slipping past a branch: stick, spiral, "
            "release. Beginners drill the motion in the air, then with "
            "a partner offering slow straight pushes, three sets of ten "
            "per side - thirty deflections a round - learning that the "
            "deflection succeeds when the incoming force is borrowed "
            "and returned to empty space, never when it is stopped "
            "head-on."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: stand in a medium snake stance with "
            "the lead forearm raised across the centerline, elbow soft. "
            "Step 2: as the incoming limb travels toward you, meet it "
            "with the outside of the forearm - light contact, never a "
            "hard block. Step 3: spiral the forearm around the incoming "
            "limb, turning the wrist so the arm rolls over and around, "
            "guiding the attack past your shoulder. Step 4: let the "
            "waist turn with the spiral, adding the bodys rotation to "
            "the redirection - a ninety-degree attack leaves at thirty "
            "degrees, sixty degrees of redirection. Step 5: release "
            "contact the instant the attack passes; do not grab, do not "
            "chase. Step 6: drill three sets of ten per side, first in "
            "the air, then against slow partner pushes with no force. "
            "The common errors are meeting the attack with a rigid arm, "
            "pushing instead of spiraling, and holding onto the "
            "partners arm after the deflection."
        ),
        "key_points": [
            "A ninety-degree incoming attack is guided into a thirty-degree miss: sixty degrees of redirection.",
            "Contact is brief and sliding - stick, spiral, release - never a hard block or a grab.",
            "The waist turns with the spiral; the deflection is waist-driven, not shoulder-driven.",
            "Drill: three sets of ten per side, thirty deflections a round, air first then slow partner pushes.",
            "Success means the force is borrowed and returned to empty space, never stopped head-on.",
        ],
        "requirements": [
            "A cooperative partner for the contact phase, working at slow speed with no force.",
            "A settled medium stance so the waist can turn without losing balance.",
            "Light forearm contact only - no grabbing the partners limb.",
            "Three sets of ten deflections per side per round.",
            "Immediate release of contact once the attack passes the shoulder.",
        ],
        "standards": [
            "The forearm spirals; it never stiffens into a rigid block.",
            "The waist visibly turns with every deflection - arm-only spirals are incomplete.",
            "The partner feels guided, not pushed or struck, at slow speed.",
        ],
        "citations": [CIT_WONG, CIT_CHOW, CIT_REID],
        "sig_lens": (
            "The Signature read: deflection is editing someone elses "
            "sentence. Public teaching redirects force; the Signature "
            "method rewrites the attacks direction mid-flight - sixty "
            "degrees of revision, signed with a spiral."
        ),
    },
    {
        "key": "low-stance",
        "name": "Low Snake Stance (She Pan Bu)",
        "group": "Stances and Steps",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The coiled serpent sits low, and so does the snake stylist. "
            "The she pan bu, the low snake stance - sometimes called the "
            "coiled stance - drops the body until the thighs burn: one "
            "leg folded deeply beneath, the other extended to the side, "
            "the torso upright over the coiled leg like a serpent reared "
            "from its coils. It is the styles signature posture for "
            "evasion and for springing attacks: from the coil the body "
            "can drop lower to slip under an attack or uncoil upward "
            "into a strike. Beginners build the stance on a hold ladder "
            "- thirty seconds, forty-five, sixty, ninety, then one "
            "hundred twenty seconds, three hundred forty-five seconds "
            "of coil time across the ladder - because the stance is "
            "useless if the legs quit after ten seconds. The low snake "
            "stance is where snake stylists learn that stillness at "
            "depth is a weapon."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: from a standing position, step one "
            "foot out to the side about one and a half shoulder-widths. "
            "Step 2: bend the stepping leg deeply, sinking the hips "
            "until the thigh is near horizontal, while the other leg "
            "extends straight to the side with the foot flat. Step 3: "
            "keep the torso upright over the bent leg - the spine does "
            "not lean, the chest does not collapse. Step 4: let the arms "
            "take a loose snake guard, hands in relaxed snake shapes at "
            "chest height. Step 5: hold for the rungs time - thirty "
            "seconds at first - breathing steadily, knees tracking over "
            "the toes of the bent leg. Step 6: rise smoothly, shake out "
            "the legs, and repeat on the other side. The common errors "
            "are letting the knee of the bent leg cave inward, leaning "
            "the torso over the thigh to cheat the depth, and lifting "
            "the heel of the extended leg. Advance one rung only when "
            "the current hold is steady and pain-free."
        ),
        "key_points": [
            "One leg folded deep beneath, the other extended: the coiled posture of the style.",
            "Hold ladder: thirty, forty-five, sixty, ninety, one hundred twenty seconds - three hundred forty-five seconds total.",
            "From the coil the body can drop to evade or uncoil upward to strike.",
            "The torso stays upright over the bent leg; depth is never bought by leaning.",
            "Stillness at depth is a weapon - the stance is useless if the legs quit in ten seconds.",
        ],
        "requirements": [
            "Healthy knees and ankles with no current injury.",
            "A non-slip floor, since the extended leg carries load at an angle.",
            "The bent knees tracking over the toes, never caving inward.",
            "An upright torso with the chest open through the whole hold.",
            "Both sides trained equally, advancing one rung at a time.",
        ],
        "standards": [
            "The thigh of the bent leg reaches near horizontal at full depth.",
            "The extended legs foot stays flat and the heel stays down.",
            "The hold is steady - no bouncing, no shifting, no leaning - for the full rung time.",
        ],
        "citations": [CIT_YANG, CIT_WONG],
        "sig_lens": (
            "The Signature read: the low stance is the coil wound to "
            "its limit. Public teaching builds leg strength; the "
            "Signature method builds the spring - three hundred "
            "forty-five seconds of winding, so the release needs no "
            "decision, only permission."
        ),
    },
]
ENTRIES.extend([
    {
        "key": "double-tongue",
        "name": "Double Snake Tongue Strike (Shuang She Tu Xin)",
        "group": "Strikes",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "One tongue flicks; two tongues flick in rhythm. The shuang "
            "she tu xin, the double snake tongue strike, pairs the two "
            "hands so they dart alternately like a serpent testing the "
            "air: left tongue, right tongue, left, right, each strike "
            "returning along its own path while the other extends. The "
            "drill runs in a one-point-two-second cycle - two strikes "
            "per cycle - so a minute of steady practice lands one "
            "hundred precise tongue strikes, each aimed at a soft "
            "target zone on the training dummy or marked pad. The "
            "alternation teaches the styles core rhythm: never commit "
            "both hands at once, never leave a strike unrecoiled. In "
            "classical theory the double tongue overwhelms a guards "
            "timing - the defender answers the first flick while the "
            "second is already arriving - and the drill builds that "
            "timing into the nervous system one hundred strikes at a "
            "time."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: take a medium snake stance facing the "
            "pad or dummy, both hands in tongue hand formation at chest "
            "height. Step 2: extend the left tongue hand straight to the "
            "target zone, fingers aligned with the forearm, striking "
            "with a short darting motion from the elbow. Step 3: the "
            "instant the left hand begins its recoil, extend the right "
            "tongue hand to its target zone - the hands pass each other "
            "mid-path. Step 4: continue alternating, left-right-left-"
            "right, keeping the rhythm even: two strikes every one-point-"
            "two seconds. Step 5: keep each strike short - the fingers "
            "travel no more than a forearms length - and recoil fully "
            "before the next extension. Step 6: drill for one minute, "
            "counting to one hundred strikes, then rest and repeat. The "
            "common errors are overextending so the shoulder commits, "
            "letting the rhythm collapse into flurries and pauses, and "
            "dropping the guard hand while the striking hand works."
        ),
        "key_points": [
            "Hands dart alternately - left, right, left, right - like a serpent testing the air.",
            "Two strikes per one-point-two-second cycle: one hundred precise strikes per minute of drilling.",
            "Never commit both hands at once; never leave a strike unrecoiled.",
            "Each strike travels no more than a forearms length, darting from the elbow.",
            "The alternation builds timing that overwhelms a guards rhythm: the second flick arrives as the first is answered.",
        ],
        "requirements": [
            "A marked pad or training dummy with clear soft target zones.",
            "Both hands in correct tongue hand formation before the first strike.",
            "A medium snake stance that stays stable through the full minute.",
            "Short darting strikes only - no lunging, no shoulder commitment.",
            "One full minute per round, counting toward one hundred strikes.",
        ],
        "standards": [
            "The rhythm stays even through the whole minute - no flurries, no pauses.",
            "Every strike recoils fully along its own path before the next extends.",
            "Both hands strike with equal speed and equal precision.",
        ],
        "citations": [CIT_WONG, CIT_SMITH],
        "sig_lens": (
            "The Signature read: two tongues write in stereo. Public "
            "teaching drills alternation; the Signature method drills "
            "the conversation - each flick a question, each recoil an "
            "answer, one hundred exchanges a minute until the rhythm "
            "signs itself."
        ),
    },
    {
        "key": "whips-tail",
        "name": "Snake Whips Its Tail (She Wei Bian)",
        "group": "Strikes",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "When the serpents head is busy, its tail is already moving. "
            "The she wei bian, the snake whips its tail, is the styles "
            "backfist: the arm sweeps in a one-hundred-eighty-degree arc "
            "with the back of the hand leading, the waist whipping the "
            "arm around like the lash of a tail. Twenty sweeps per side, "
            "forty total, trace seven thousand two hundred degrees of "
            "arc in a single round - and every degree is waist-driven, "
            "the arm loose until the moment of the whip. The technique "
            "answers the flank: when an opponent circles past the "
            "tongue hands reach, the tail is already there. Beginners "
            "drill it in the air against an imaginary circling opponent, "
            "learning that the power arrives from the sudden turn of "
            "the waist, not from swinging the arm like a club."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: stand in a medium snake stance, lead "
            "hand forward in a snake guard, rear hand chambered at the "
            "hip. Step 2: turn the waist sharply toward the rear side, "
            "letting the rear arm swing out and around in a one-hundred-"
            "eighty-degree arc, the back of the hand leading. Step 3: "
            "keep the arm relaxed through the sweep - the waist does the "
            "work, the arm is the lash. Step 4: at the arcs end, snap "
            "the wrist so the back of the hand cracks like a whip tip, "
            "then recoil the arm immediately. Step 5: reset the stance "
            "and repeat - twenty sweeps per side, forty total, each arc "
            "a full one hundred eighty degrees. Step 6: practice the "
            "footwork pairing: as the waist whips, the feet pivot so the "
            "body faces the new line. The common errors are swinging "
            "with a stiff arm powered by the shoulder, cutting the arc "
            "short, and leaving the arm extended after the whip instead "
            "of recoiling."
        ),
        "key_points": [
            "A one-hundred-eighty-degree backfist arc, the back of the hand leading like a lashing tail.",
            "Twenty sweeps per side, forty total: seven thousand two hundred degrees of arc per round.",
            "Power comes from the sudden turn of the waist; the arm stays loose until the whip.",
            "Answers the flank: when the tongue hands cannot reach, the tail is already moving.",
            "The wrist snaps at the arcs end and the arm recoils instantly - no lingering.",
        ],
        "requirements": [
            "A clear training area with no obstacles in the full arc path.",
            "A settled stance that lets the waist turn freely without losing balance.",
            "A relaxed arm through the sweep - tension only at the whip instant.",
            "Twenty full-arc sweeps per side per round.",
            "Foot pivots paired with the waist turn so the body faces the new line.",
        ],
        "standards": [
            "Every sweep traces the full one hundred eighty degrees - no shortened arcs.",
            "The waist visibly leads; the arm follows like a lash, never like a club.",
            "The recoil is immediate - the hand never hangs at the arcs end.",
        ],
        "citations": [CIT_WONG, CIT_CHOW],
        "sig_lens": (
            "The Signature read: the tail is the signature written "
            "behind the back. Public teaching covers the flank; the "
            "Signature method signs the space the opponent thought was "
            "empty - seven thousand two hundred degrees of proof per "
            "round that nothing behind the serpent is safe."
        ),
    },
    {
        "key": "eye-flicks",
        "name": "Precision Eye Flicks (Dian Mu Xun Lian)",
        "group": "Strikes",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The snake strikes the eye because the eye cannot be "
            "armored. The dian mu xun lian, precision eye flick "
            "training, is the styles accuracy school: five target "
            "rings hung at head height, shrinking from ten centimeters "
            "down to four, and the tongue hand must flick through each "
            "ring - ten clean flicks per ring, fifty strikes per round - "
            "without touching the ring itself. The drill is practiced "
            "on rings and pads only, never on a partner, and it teaches "
            "the defining snake skill: hitting a chosen point at speed. "
            "Classical snake theory holds that precision defeats power - "
            "a flick that lands exactly where it is aimed needs no "
            "force behind it - and the shrinking rings make that theory "
            "physical. When all five rings are cleared ten times each "
            "without a touch, the students eyes and fingers have learned "
            "to agree."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: hang five rings at head height in a "
            "line, sized ten, eight, six, five, and four centimeters, "
            "each at a comfortable striking distance. Step 2: take a "
            "medium snake stance and form the tongue hand. Step 3: flick "
            "the tongue hand through the ten-centimeter ring - a short "
            "dart from the elbow, fingers passing cleanly through the "
            "opening. Step 4: complete ten clean passes through the "
            "largest ring, then move to the eight-centimeter ring, and "
            "so on down to four centimeters: fifty strikes per round. "
            "Step 5: any touch of the ring restarts that rings count - "
            "the standard is ten consecutive clean passes. Step 6: "
            "drill at half speed until the largest three rings are "
            "clean, then add speed gradually. The common errors are "
            "lunging the body at small rings instead of trusting the "
            "arm, tensing the fingers so the hand wobbles, and rushing "
            "to small rings before the large ones are clean."
        ),
        "key_points": [
            "Five rings, ten to four centimeters, ten clean flicks each: fifty strikes per round.",
            "A touched ring restarts its count - the standard is ten consecutive clean passes.",
            "Trained on rings and pads only, never on a partner.",
            "Classical theory: precision defeats power - a flick that lands exactly needs no force.",
            "Half speed first; speed is earned ring by ring.",
        ],
        "requirements": [
            "Five rings or marked circles sized ten, eight, six, five, and four centimeters, hung at head height.",
            "A stable stance at a distance where the largest ring is reached without lunging.",
            "Correct tongue hand formation verified before the first flick.",
            "Ten consecutive clean passes per ring before advancing to the next.",
            "No partner targets - rings and pads only for this drill.",
        ],
        "standards": [
            "The fingers pass through each ring without touching it, ten times consecutively.",
            "The body does not lunge; the strike is an arm dart from a stable base.",
            "All five rings cleared in one round before the drill is considered complete.",
        ],
        "citations": [CIT_WONG, CIT_SMITH, CIT_REID],
        "sig_lens": (
            "The Signature read: the rings are the fine print of the "
            "signature. Public teaching drills accuracy; the Signature "
            "method drills agreement - eye and finger signing the same "
            "contract, fifty witnesses per round, until the hand cannot "
            "miss what the eye has chosen."
        ),
    },
    {
        "key": "coiling-strike",
        "name": "Coiling Arm Snake Strike (Chan Rao Ji)",
        "group": "Strikes",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "First the arm coils, then it strikes - the two motions are "
            "one. The chan rao ji, the coiling arm snake strike, winds "
            "the striking arm through a two-hundred-seventy-degree "
            "spiral around the guard or the incoming limb, then releases "
            "the coil into a tongue hand strike along the line the "
            "spiral opened. Three sets of eight, twenty-four strikes "
            "per round, each one practicing the styles signature "
            "combination: defense and attack as a single coiling "
            "motion, the spiral clearing the path that the strike then "
            "travels. In classical application the coil wraps an "
            "opponents guarding arm and the strike darts through the "
            "gap before the guard can recover - the snake does not "
            "push the branch aside, it winds around it and bites from "
            "the other side."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: face the dummy or pad in a medium "
            "snake stance, lead arm raised in a coiling guard. Step 2: "
            "begin the spiral - roll the forearm over and around in a "
            "two-hundred-seventy-degree wind, the elbow dropping and "
            "the wrist turning, as if winding around an incoming limb. "
            "Step 3: at the spirals completion, let the coil release: "
            "the arm unwinds and the hand shapes into the tongue hand "
            "mid-extension. Step 4: dart the tongue hand along the line "
            "the spiral opened, a short precise strike, then recoil. "
            "Step 5: reset to the coiling guard and repeat - three sets "
            "of eight, twenty-four strikes per round, alternating lead "
            "hands each set. Step 6: check that the spiral always "
            "precedes the strike; if the strike fires without the wind, "
            "the technique has collapsed into an ordinary punch. The "
            "common errors are striking without coiling first, winding "
            "with the shoulder instead of the forearm, and pausing "
            "between the coil and the strike so the two motions "
            "separate."
        ),
        "key_points": [
            "The arm winds a two-hundred-seventy-degree spiral, then releases the coil into a tongue hand strike.",
            "Three sets of eight, twenty-four strikes per round: defense and attack as one coiling motion.",
            "The spiral clears the path - winding around the guard - that the strike then travels.",
            "The hand shapes into the tongue hand mid-extension as the coil releases.",
            "A strike without the preceding wind is not this technique; the coil is the technique.",
        ],
        "requirements": [
            "A training dummy or pad to receive the released strikes.",
            "A fluid forearm spiral - the elbow drops and the wrist turns through the full wind.",
            "The tongue hand formed during the unwinding, not before.",
            "Three sets of eight strikes per round, alternating lead hands.",
            "No pause between coil and strike - one continuous motion.",
        ],
        "standards": [
            "Every strike is preceded by the full two-hundred-seventy-degree wind.",
            "The coil and the release flow as one motion with no visible seam.",
            "Both lead hands perform the technique equally well.",
        ],
        "citations": [CIT_WONG, CIT_CHOW],
        "sig_lens": (
            "The Signature read: the spiral is the signature being "
            "written in the air, the strike is the dot on the mark. "
            "Public teaching combines defense and attack; the Signature "
            "method refuses to separate them - one coil, one release, "
            "twenty-four signatures per round."
        ),
    },
    {
        "key": "creeps-down",
        "name": "Snake Creeps Down Transitions (She Xing Xia Shi)",
        "group": "Stances and Steps",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The serpent drops without warning. The she xing xia shi, "
            "the snake creeps down transitions, trains the sudden "
            "level change from standing to the low snake stance and "
            "back: the body sinks in one-point-five seconds from full "
            "height to the coiled depth, holds, and rises again - ten "
            "transitions per round, fifteen seconds of controlled "
            "dropping. In application the creep-down slips under a high "
            "attack while loading the legs like a compressed spring; "
            "the rise that follows can carry a strike upward along the "
            "opening the drop created. The drill teaches the legs to "
            "accept the drop without the knees buckling and the torso "
            "to stay upright while the floor rushes up - the head must "
            "not dive forward, the spine must not fold. A snake "
            "stylist who can change levels in a breath and a half owns "
            "the vertical dimension of the exchange."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: stand in a medium snake stance, guard "
            "up, weight even. Step 2: sink - bend both knees and drop "
            "the hips straight down into the low snake stance, one leg "
            "folding deep, the other extending, the torso staying "
            "upright. The full drop takes about one-point-five seconds: "
            "fast, but never a collapse. Step 3: settle for one breath "
            "in the coil, feeling the legs loaded. Step 4: rise smoothly "
            "back to the medium stance, driving up through the legs, "
            "guard intact the whole way. Step 5: repeat ten times - ten "
            "drops, fifteen seconds of sinking - then rest the legs. "
            "Step 6: alternate which leg folds deep each repetition so "
            "both sides learn the coil. The common errors are dropping "
            "with the torso leaning forward, letting the knees cave "
            "inward under the sudden load, and bouncing at the bottom "
            "instead of settling."
        ),
        "key_points": [
            "Full height to coiled depth in one-point-five seconds: ten transitions, fifteen seconds of dropping per round.",
            "The drop slips under high attacks while loading the legs like a compressed spring.",
            "The torso stays upright while the floor rushes up - no diving forward, no folding.",
            "Both legs alternate as the folding leg so both sides learn the coil.",
            "Level changes in a breath and a half give the stylist the vertical dimension.",
        ],
        "requirements": [
            "Healthy knees and ankles, warmed up before the first drop.",
            "A non-slip floor - the drop loads the legs suddenly.",
            "An upright torso through the entire descent and rise.",
            "Knees tracking over the toes with no inward cave.",
            "Ten full transitions per round, alternating the folding leg.",
        ],
        "standards": [
            "Each drop completes in about one-point-five seconds - controlled, never a collapse.",
            "The head height changes but the head never dives forward of the knees.",
            "The rise is as smooth as the drop; no pushing off the floor with the hands.",
        ],
        "citations": [CIT_YANG, CIT_WONG],
        "sig_lens": (
            "The Signature read: the drop is the signature ducking "
            "under the line to sign beneath it. Public teaching "
            "trains evasion; the Signature method trains the spring - "
            "fifteen seconds of winding per round, and every rise is "
            "already a strike that has not been named yet."
        ),
    },
    {
        "key": "darting-head",
        "name": "Darting Head Strike (She Tou Ji)",
        "group": "Strikes",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "This is the strike the style is named for: the whole body "
            "becomes the serpent and the hand becomes its head. The she "
            "tou ji, the darting head strike, lunges the body forward "
            "one-point-two meters while the tongue hand darts to the "
            "target - the lunge and the strike landing as one event, "
            "the way a snakes strike is body and head together. Twelve "
            "repetitions carry the stylist fourteen-point-four meters "
            "down the floor, each lunge a complete commitment of "
            "distance closed and precision delivered. Southern kung fu "
            "schools, where snake style runs deepest, teach this as "
            "the answer to retreating opponents: the glide becomes a "
            "dart, and the distance the opponent bought by stepping "
            "back is spent in a single lunge. The drill is practiced "
            "on the dummy or pads, and the rule is absolute - the "
            "strike must arrive with the lunge, never after it."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: take a medium snake stance at "
            "lunge distance from the dummy, about one-point-two meters "
            "out. Step 2: coil slightly - sink a breath lower, hands in "
            "tongue formation. Step 3: lunge - drive off the rear leg, "
            "let the body dart forward the full one-point-two meters, "
            "and extend the tongue hand so hand and body arrive "
            "together. Step 4: the strike lands as the front foot "
            "lands: one event, not two. Step 5: recoil instantly - snap "
            "the hand back and recover the stance, ready to dart again. "
            "Step 6: repeat twelve times down the floor, fourteen-point-"
            "four meters of darting, then walk back and repeat. The "
            "common errors are striking after the lunge lands instead "
            "of with it, over-lunging so balance is lost on arrival, "
            "and dropping the rear guard hand during the dart."
        ),
        "key_points": [
            "Body and hand arrive as one event: the lunge is one-point-two meters, the strike lands with the front foot.",
            "Twelve repetitions carry the stylist fourteen-point-four meters down the floor.",
            "The southern answer to retreating opponents: the glide becomes a dart.",
            "The strike must arrive with the lunge, never after it - one event, not two.",
            "Instant recoil after every dart; the serpent never lingers at full extension.",
        ],
        "requirements": [
            "A clear floor lane at least fifteen meters long for the darting line.",
            "A training dummy or pads at the far end to receive the strikes.",
            "Correct tongue hand formation held through the lunge.",
            "The full one-point-two-meter lunge driven from the rear leg.",
            "Twelve complete dart-and-recover repetitions per round.",
        ],
        "standards": [
            "Hand and front foot land together on every repetition - the timing is the technique.",
            "Balance is intact on arrival; no stumbling past the target.",
            "The rear guard hand stays up through the entire dart.",
        ],
        "citations": [CIT_WONG, CIT_CHOW, CIT_SMITH],
        "sig_lens": (
            "The Signature read: the dart is the whole serpent signing "
            "at once. Public teaching closes distance; the Signature "
            "method erases it - one-point-two meters of floor denied, "
            "fourteen-point-four meters of proof per round that the "
            "signature arrives with the body behind it."
        ),
    },
    {
        "key": "entwines-branch",
        "name": "Snake Entwines the Branch (Arm Entanglement)",
        "group": "Applications",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The serpent does not block the branch; it wraps it. This "
            "application takes the coiling deflection into partner work: "
            "as the partners arm extends in a slow straight strike, the "
            "stylist spirals the forearm around it, slides to the "
            "outside, and lets the coil settle into a controlling wrap - "
            "four movements in sequence, five slow repetitions per "
            "round, twenty entanglements practiced with a cooperative "
            "partner at walking speed and zero force. The sequence is "
            "stick, spiral, slide, settle: contact the incoming arm, "
            "wind around it, glide to the outside line, and let the "
            "wrap rest in a position of control. Nothing is grabbed, "
            "nothing is wrenched; the entanglement works because the "
            "spiral geometry leaves the partners arm with nowhere to "
            "go, not because of strength. All partner work in this "
            "database is no-contact and cooperative - the entanglement "
            "is a study in positioning, practiced slowly enough that "
            "both partners can talk through it."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: the partner extends a slow straight "
            "arm toward the stylists chest at walking speed; the "
            "stylist meets it with the outside of the lead forearm - "
            "stick, light contact. Step 2: spiral - roll the forearm "
            "over and around the partners arm in the coiling wind, the "
            "waist turning with it. Step 3: slide - glide the body to "
            "the outside line as the spiral completes, so the partners "
            "arm is guided past the center. Step 4: settle - let the "
            "coiled arm rest in a wrapping position that controls the "
            "partners elbow line, both partners freezing to check the "
            "geometry. Step 5: release cleanly, reset, and repeat - "
            "five repetitions per round, twenty total across the four "
            "movements, then swap roles. Step 6: talk through each "
            "repetition: the partner reports what they feel, and any "
            "force or discomfort means the speed was too high. The "
            "common errors are gripping instead of wrapping, muscling "
            "the partners arm, and practicing faster than the geometry "
            "is understood."
        ),
        "key_points": [
            "Four movements in sequence: stick, spiral, slide, settle - twenty entanglements per round.",
            "Practiced with a cooperative partner at walking speed and zero force.",
            "The wrap controls by spiral geometry, not by strength, gripping, or wrenching.",
            "Both partners freeze to check the position, then release cleanly.",
            "Any force or discomfort means the speed was too high - slow down and talk it through.",
        ],
        "requirements": [
            "A cooperative partner briefed on the zero-force, walking-speed rule.",
            "A clear mat or floor area with room to slide to the outside line.",
            "Light forearm contact only - no gripping the partners arm or wrist.",
            "Five slow repetitions per round per person, then swapping roles.",
            "Verbal check-ins: the partner reports what they feel on every repetition.",
        ],
        "standards": [
            "The partners arm is guided, never grabbed or wrenched, through all four movements.",
            "The waist turns with the spiral - arm-only wraps are incomplete.",
            "Both partners can explain the geometry of the settled position.",
        ],
        "citations": [CIT_WONG, CIT_REID],
        "sig_lens": (
            "The Signature read: entanglement is the signature wrapping "
            "the page it is written on. Public teaching studies "
            "positioning; the Signature method studies inevitability - "
            "four movements, twenty repetitions, and the geometry does "
            "the signing while strength watches."
        ),
    },
])
ENTRIES.extend([
    {
        "key": "rising-serpent",
        "name": "Rising Serpent Level Change (She Sheng)",
        "group": "Coiling and Evasion",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Down is only half the serpents range; up is the other. The "
            "she sheng, the rising serpent, is the upward level change: "
            "from the low coiled stance the body uncoils in about one "
            "second, rising one-point-one meters from coil to full "
            "height with the hands traveling upward in a double tongue "
            "guard - eight rises per round, eight seconds of uncoiling. "
            "Where the creep-down slips under attacks, the rising "
            "serpent answers low attacks and grappling pressure by "
            "leaving the low line entirely, the body ascending along a "
            "spiral path that is difficult to follow or hold. Classical "
            "snake forms pair the two constantly: creep down, rise up, "
            "the serpent writing vertical waves through the exchange. "
            "The drill teaches the legs to uncoil without pushing off "
            "the hands and the spine to stay long through the whole "
            "ascent - a serpent rises along its own length, it does not "
            "climb with its arms."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: settle into the low snake stance, one "
            "leg folded deep, torso upright, hands in a low guard. Step "
            "2: begin the uncoil - drive through the folded leg, letting "
            "the hips rise straight up, the extending leg drawing in "
            "beneath you. Step 3: let the body spiral slightly as it "
            "rises, the waist turning a quarter turn, hands traveling "
            "upward in a double tongue guard that covers the centerline. "
            "Step 4: arrive at full standing height in about one second, "
            "one-point-one meters of ascent, weight even, guard intact. "
            "Step 5: hold one breath at the top, then sink back to the "
            "coil to begin the next rise - eight rises per round. Step "
            "6: breathe out on the rise, in on the sink; never hold the "
            "breath through the uncoiling. The common errors are pushing "
            "off the floor with the hands, letting the torso tip forward "
            "on the way up, and rushing so the spiral becomes a "
            "straight pop-up."
        ),
        "key_points": [
            "From coiled depth to full height in about one second: one-point-one meters of ascent.",
            "Eight rises per round, eight seconds of uncoiling, hands traveling up in a double tongue guard.",
            "Answers low attacks by leaving the low line entirely along a spiraling path.",
            "The legs uncoil the body; the hands never push off the floor.",
            "Paired with the creep-down in classical forms: the serpent writes vertical waves.",
        ],
        "requirements": [
            "Healthy knees and a warmed-up lower body before the first rise.",
            "A stable low snake stance as the starting coil for every repetition.",
            "The full one-point-one-meter ascent driven by the legs alone.",
            "A quarter-turn waist spiral through the rise, guard covering the centerline.",
            "Eight complete rise-and-sink cycles per round, breathing out on the rise.",
        ],
        "standards": [
            "The spine stays long through the whole ascent - no tipping forward.",
            "Each rise completes in about one second with the spiral intact.",
            "The hands guard the centerline for the entire one-point-one meters.",
        ],
        "citations": [CIT_YANG, CIT_WONG],
        "sig_lens": (
            "The Signature read: the rise is the signature ascending "
            "off the page it was written under. Public teaching trains "
            "the upward escape; the Signature method trains the return "
            "- eight seconds of uncoiling per round, and every ascent "
            "is the coil reloading in plain sight."
        ),
    },
    {
        "key": "vital-theory-1",
        "name": "Vital-Point Theory I: The Educational Anatomy Map",
        "group": "Vital-Point Theory",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Snake style aims at points, so snake students study the "
            "map. This record is educational anatomy, not combat "
            "instruction: the classical dianxue, vital-point theory, "
            "taught as a study of human structure. Twelve primary "
            "points are mapped in this first study - the temple region, "
            "the hollow of the throat, the sides of the neck where the "
            "great vessels run, the solar plexus, the floating ribs, "
            "and the soft points of the face - each located by "
            "anatomical landmarks, each understood for what lies "
            "beneath: bone, vessel, nerve, airway. The student learns "
            "the map the way a medical student learns anatomy: by "
            "naming structures, understanding vulnerability as a "
            "property of the body, and completing a twelve-question "
            "study quiz with ten correct required to advance. Nothing "
            "in this study is practiced on people. The knowledge "
            "exists so the stylist understands why snake style "
            "values precision, and why the art pairs its study of "
            "points with a strict ethic of restraint."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: obtain an anatomy reference - a "
            "textbook or anatomical chart - and locate the twelve "
            "primary points by their landmarks: the temple at the "
            "thinnest part of the skull, the throat hollow above the "
            "sternum, the neck vessels beside the windpipe, the solar "
            "plexus below the sternum, the floating ribs at the lower "
            "rib cage, and the soft points around the eyes, nose, and "
            "jaw. Step 2: for each point, write down what lies beneath "
            "it - bone, blood vessel, nerve cluster, or airway - in "
            "your own words. Step 3: study the points in pairs, quizzing "
            "yourself on landmark and underlying structure until all "
            "twelve are named without hesitation. Step 4: take the "
            "twelve-question study quiz - name the landmark, name the "
            "structure beneath - requiring ten correct to advance. Step "
            "5: review the misses with the reference open, correcting "
            "the map, not memorizing the error. Step 6: revisit the map "
            "monthly; anatomy fades without review. The common errors "
            "are memorizing names without understanding the structures, "
            "treating the map as targeting practice, and skipping the "
            "written step - writing the structures down is what makes "
            "the knowledge stay."
        ),
        "key_points": [
            "Twelve primary points mapped by anatomical landmark and underlying structure: bone, vessel, nerve, airway.",
            "Educational anatomy only: studied like a medical student studies structure, never practiced on people.",
            "A twelve-question study quiz requires ten correct answers to advance.",
            "The map explains why the style values precision - and why it pairs precision with restraint.",
            "Writing each point's structures in your own words is what makes the knowledge stay.",
        ],
        "requirements": [
            "An anatomy textbook or anatomical chart as the study reference.",
            "A written study journal for the twelve points and their underlying structures.",
            "The twelve-question quiz completed with at least ten correct.",
            "Monthly review of the map - anatomy fades without it.",
            "A clear understanding: this is study material, never practiced on people.",
        ],
        "standards": [
            "Every point is located by landmark and explained by structure, not just named.",
            "Ten of twelve quiz questions correct before advancing to the second theory study.",
            "The written journal is complete and in the students own words.",
        ],
        "citations": [CIT_CLARK, CIT_YANG_QIGONG],
        "sig_lens": (
            "The Signature read: the map is the legend of the "
            "signature - it explains what every stroke means. Public "
            "teaching maps the points; the Signature method maps the "
            "responsibility, twelve points and twelve promises that "
            "precision will always be paired with restraint."
        ),
    },
    {
        "key": "form-one",
        "name": "Snake Form One: The Coiling Serpent (She Quan Yi Lu)",
        "group": "Forms",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Forms are where the style stores its knowledge, and the "
            "first snake form stores the coil. The she quan yi lu, snake "
            "form one - the coiling serpent - is a short sequence of "
            "eighteen movements practiced in order: salute, sink to the "
            "coil, tongue hand drills in four directions, the coiling "
            "deflection, the tail whip, the creep-down and rise, and "
            "the closing salute. At three seconds per movement the form "
            "runs fifty-four seconds; three rounds total one hundred "
            "sixty-two seconds of continuous snake movement. The form "
            "is the students first long memorization - eighteen "
            "movements in exact sequence - and it is practiced slowly "
            "until the order is automatic, then at full speed until the "
            "transitions disappear. Every later form in this database "
            "builds on form one: its movements are the alphabet, and "
            "the longer forms are sentences."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: learn the eighteen movements in "
            "three groups of six - first the salute, sink, and four "
            "directional tongue drills; then the deflection, the tail "
            "whip, and the directional changes; then the creep-down, "
            "the rise, and the closing salute. Step 2: practice each "
            "group slowly until its six movements flow without pausing "
            "to remember. Step 3: join the groups in order and walk "
            "the full eighteen movements at half speed, about three "
            "seconds per movement, fifty-four seconds per round. Step "
            "4: repeat for three rounds - one hundred sixty-two seconds "
            "total - resting between rounds. Step 5: when the sequence "
            "is automatic, practice at full speed, letting the "
            "transitions between movements disappear. Step 6: film or "
            "mirror-check the form monthly, comparing the shapes to "
            "the foundations: every tongue hand crisp, every stance at "
            "depth. The common errors are rushing the memorization so "
            "the order scrambles under speed, pausing between "
            "movements, and letting the stances rise as fatigue sets "
            "in."
        ),
        "key_points": [
            "Eighteen movements in exact sequence: the alphabet of the snake style.",
            "Three seconds per movement: fifty-four seconds per round, one hundred sixty-two seconds for three rounds.",
            "Learned in three groups of six, joined only when each group flows.",
            "Slow until automatic, then full speed until the transitions disappear.",
            "Every later form builds on form one; its movements are the foundation vocabulary.",
        ],
        "requirements": [
            "Mastery of the foundations first: salute, resting posture, tongue hand, snake step, low stance.",
            "A floor space large enough for four-directional movement.",
            "The eighteen movements learned in three groups of six before joining.",
            "Three full rounds per practice session at the students working speed.",
            "A mirror or recording for monthly shape checks against the foundations.",
        ],
        "standards": [
            "The eighteen movements run in exact order with no pauses to remember.",
            "Stances stay at depth through all three rounds - no rising with fatigue.",
            "Every tongue hand and snake head palm in the form holds its crisp shape.",
        ],
        "citations": [CIT_WONG, CIT_SHAHAR],
        "sig_lens": (
            "The Signature read: form one is the signature practiced "
            "until the hand cannot forget it. Public teaching "
            "memorizes a sequence; the Signature method internalizes "
            "an alphabet - eighteen letters, one hundred sixty-two "
            "seconds per writing, until the coil writes itself."
        ),
    },
    {
        "key": "snake-breathing",
        "name": "Chi Development: Snake Breathing (She Xi)",
        "group": "Chi Development",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The serpent breathes slowly even in the strike. The she "
            "xi, snake breathing, is the styles foundational qigong: a "
            "seated or standing breath practice that trains the deep, "
            "slow respiration classical theory associates with steady "
            "energy and calm nerves. The cycle is eighteen seconds - "
            "breathe in for six counts, hold gently for three, breathe "
            "out for nine - and ten minutes of practice gives thirty-"
            "three complete cycles, each one slower and deeper than "
            "ordinary breathing. The long exhale is the point: nine "
            "counts out against six in teaches the nervous system that "
            "exertion ends in release, so the body learns to stay calm "
            "inside effort. Students practice snake breathing before "
            "forms and after hard conditioning, and the classical texts "
            "on qigong describe this kind of regulated breathing as the "
            "root of all energy training - the breath first, everything "
            "else after."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: sit or stand comfortably with the "
            "spine long, hands resting, eyes softly closed or lowered. "
            "Step 2: breathe in through the nose for six slow counts, "
            "feeling the belly expand and the lower ribs widen - the "
            "chest stays quiet. Step 3: hold gently for three counts, "
            "neither clenching nor gasping, the air simply resting. "
            "Step 4: breathe out through the nose for nine slow counts, "
            "letting the belly draw in naturally, emptying completely "
            "but without forcing. Step 5: continue for ten minutes - "
            "thirty-three eighteen-second cycles - keeping the count "
            "honest even as the breath wants to quicken. Step 6: end "
            "with three natural breaths, then sit quietly for a minute "
            "before standing. The common errors are forcing the belly "
            "instead of letting it move, gasping on the hold, and "
            "cutting the exhale short - the nine counts out are the "
            "whole lesson. Practice daily; the calm compounds."
        ),
        "key_points": [
            "Eighteen-second cycle: in for six, hold for three, out for nine - ten minutes gives thirty-three cycles.",
            "The long exhale teaches the nervous system that exertion ends in release.",
            "Belly breathing: the belly expands and the lower ribs widen while the chest stays quiet.",
            "Practiced before forms and after hard conditioning, daily - the calm compounds.",
            "Classical qigong theory treats regulated breathing as the root of all energy training.",
        ],
        "requirements": [
            "A quiet space and ten uninterrupted minutes.",
            "A seated or standing posture with the spine long.",
            "The six-three-nine count kept honest through all thirty-three cycles.",
            "Nasal breathing throughout - no mouth breathing.",
            "Daily practice; a single weekly session does not build the habit.",
        ],
        "standards": [
            "The exhale reaches the full nine counts on every cycle, never cut short.",
            "The belly moves and the chest stays quiet - no chest heaving.",
            "Ten minutes completed without breaking the count to check the time.",
        ],
        "citations": [CIT_YANG_QIGONG, CIT_WONG],
        "sig_lens": (
            "The Signature read: the breath is the ink of the "
            "signature - without it the pen is dry. Public teaching "
            "practices qigong; the Signature method practices the "
            "signature beneath the technique: thirty-three slow "
            "strokes per session, each one signing calm into the "
            "nervous system."
        ),
    },
    {
        "key": "coiling-evasion",
        "name": "Coiling Body Evasion (She Shen Shan)",
        "group": "Coiling and Evasion",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The serpent is never where the strike lands. The she shen "
            "shan, the coiling body evasion, moves the whole torso off "
            "the attack line in a spiraling displacement: the waist "
            "coils, the body slides zero-point-six meters to the side, "
            "and the head travels a curved path that no straight attack "
            "can follow. Three directions - left, right, and the drop-"
            "coil - drilled four times each, twelve evasions per round, "
            "seven-point-two meters of total displacement, teach the "
            "body that evasion is a relocation, not a retreat. The "
            "hands stay in guard through every coil; the evasion that "
            "drops the guard has traded one danger for another. In "
            "classical snake theory the evasion is already the next "
            "attack: the coil that carries the body aside loads the "
            "waist for the return strike, so defense and offense share "
            "a single spiraling motion."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: stand in a medium snake stance "
            "facing the imaginary attack line, hands in guard. Step 2: "
            "coil left - turn the waist sharply, slide the body zero-"
            "point-six meters to the left along a curved path, head "
            "traveling the spiral, guard intact. Step 3: return to "
            "center and coil right - the same zero-point-six-meter "
            "spiral displacement to the right. Step 4: drop-coil - sink "
            "into the low snake stance while turning the waist, the "
            "body disappearing below the high line. Step 5: drill four "
            "repetitions of each direction - twelve evasions, seven-"
            "point-two meters of displacement - keeping every coil "
            "smooth and every guard up. Step 6: add the return: after "
            "each evasion, let the uncoiling waist carry a tongue hand "
            "back along the vacated line. The common errors are "
            "stepping straight back instead of spiraling, dropping the "
            "hands during the coil, and evading so far that the return "
            "strike cannot reach."
        ),
        "key_points": [
            "Three evasions - coil left, coil right, drop-coil - four repetitions each, twelve per round.",
            "Each coil displaces the body zero-point-six meters along a curved path: seven-point-two meters total.",
            "Evasion is relocation, not retreat: the body moves aside, never straight back.",
            "The guard stays up through every coil - trading guard for evasion trades one danger for another.",
            "The coil that evades loads the waist for the return strike: one spiral, two purposes.",
        ],
        "requirements": [
            "A clear floor area with at least two meters of lateral space.",
            "A settled medium stance before each coil - no evading from standing.",
            "The full zero-point-six-meter spiral displacement per evasion.",
            "Hands in guard through the entire motion, every repetition.",
            "Four repetitions per direction per round, both sides equal.",
        ],
        "standards": [
            "The head travels a curved path on every evasion - no straight-line retreats.",
            "The guard never drops, even at the deepest point of the drop-coil.",
            "Each evasion flows into a return strike without resetting the feet.",
        ],
        "citations": [CIT_WONG, CIT_CHOW],
        "sig_lens": (
            "The Signature read: evasion is the signature stepping "
            "aside to let the attack sign empty air. Public teaching "
            "dodges; the Signature method relocates - twelve coils per "
            "round, seven-point-two meters of denial, and the spiral "
            "always keeps a return stroke loaded."
        ),
    },
    {
        "key": "double-headed",
        "name": "Double-Headed Snake: Strike and Guard (Shuang Tou She)",
        "group": "Strikes",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The mythical double-headed serpent strikes in two "
            "directions at once - and the drill named for it teaches "
            "the hands to work independently. The shuang tou she, the "
            "double-headed snake, pairs a tongue hand strike with a "
            "simultaneous guarding deflection: one hand darts while "
            "the other coils, the body serving two purposes in a "
            "single beat. Twenty-five strike-and-guard pairs in thirty "
            "seconds - one pair every one-point-two seconds - train "
            "the independence that beginners lack: the striking hand "
            "must not drag the guarding hand with it, and the guarding "
            "hand must not freeze the striking hand. Classical snake "
            "masters describe this as the moment the style matures - "
            "when one hand can attack and the other defend without "
            "either consulting the other, the practitioner has two "
            "serpents instead of one."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: face the dummy in a medium snake "
            "stance, left hand forward in tongue formation, right hand "
            "in a coiling guard. Step 2: dart the left tongue hand to "
            "its target while the right hand simultaneously performs a "
            "coiling deflection in the air beside you - strike and "
            "guard in one beat. Step 3: recoil the left hand as the "
            "right hand settles back to guard; the two motions are "
            "independent but synchronized. Step 4: swap roles - right "
            "hand strikes while the left hand coils in guard. Step 5: "
            "continue alternating for thirty seconds, aiming for "
            "twenty-five complete pairs, one every one-point-two "
            "seconds. Step 6: check the independence: have a partner "
            "call strike or guard at random, and let only the named "
            "hand move. The common errors are letting the guarding "
            "hand mirror the striking hand, freezing the guard while "
            "the strike extends, and losing the rhythm so the pairs "
            "collapse into alternating single motions."
        ),
        "key_points": [
            "One hand strikes while the other guards: twenty-five pairs in thirty seconds, one every one-point-two seconds.",
            "The hands work independently - the strike must not drag the guard, the guard must not freeze the strike.",
            "Strike and guard land in a single beat, then both reset together.",
            "Trained on the dummy for the strike hand and in the air for the guard hand.",
            "Two serpents instead of one: the moment the style matures.",
        ],
        "requirements": [
            "A training dummy or pad for the striking hand; the guard hand works in the air.",
            "Established tongue hand formation and coiling deflection before combining them.",
            "A stable stance that does not shift as the hands work independently.",
            "Thirty-second rounds aiming for twenty-five complete pairs.",
            "Random-call checks with a partner to verify true hand independence.",
        ],
        "standards": [
            "The guarding hand never mirrors the striking hand - the motions stay independent.",
            "Every pair completes within the one-point-two-second beat.",
            "Both hands perform both roles equally: strike-left, strike-right, twenty-five pairs each way over time.",
        ],
        "citations": [CIT_WONG, CIT_SMITH],
        "sig_lens": (
            "The Signature read: two heads, one signature. Public "
            "teaching coordinates the hands; the Signature method "
            "liberates them - twenty-five pairs per round until each "
            "hand signs its own half of the technique without asking "
            "the other for permission."
        ),
    },
    {
        "key": "form-two",
        "name": "Snake Form Two: Serpent Crosses the River (She Quan Er Lu)",
        "group": "Forms",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The second form teaches the serpent to travel. The she "
            "quan er lu, snake form two - the serpent crosses the "
            "river - is twenty-four movements that carry the "
            "practitioner across the floor and back: advancing tongue "
            "strikes, the double-headed pairs, coiling evasions in all "
            "three directions, the tail whip on the turn, and the "
            "creep-down beneath an imaginary high line. At three-point-"
            "five seconds per movement the form runs eighty-four "
            "seconds; two rounds total one hundred sixty-eight seconds "
            "of traveling snake work. Where form one stays near its "
            "starting point, form two insists on covering ground - the "
            "glide, the dart, and the coil all appear in their "
            "traveling versions. Students learn it only after form one "
            "is automatic, because form two assumes the alphabet: it "
            "is the first sentence written while walking."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: confirm form one runs cleanly at "
            "speed - form two is not started until it does. Step 2: "
            "learn the twenty-four movements in four groups of six: "
            "the advance (glide plus tongue strikes), the double-"
            "headed pairs, the three-directional evasions, and the "
            "turn with the tail whip plus the creep-down and closing. "
            "Step 3: walk each group slowly until its six movements "
            "flow, then join the groups in order. Step 4: perform the "
            "full form at three-point-five seconds per movement - "
            "eighty-four seconds - keeping the traveling footwork "
            "smooth and level. Step 5: complete two rounds per "
            "session, one hundred sixty-eight seconds total, resting "
            "between rounds. Step 6: practice the form in both "
            "directions across the floor so the turn and the "
            "directional evasions are trained symmetrically. The "
            "common errors are starting form two with form one still "
            "shaky, letting the traveling stances rise, and rushing "
            "the turn so the tail whip is skipped."
        ),
        "key_points": [
            "Twenty-four movements that travel across the floor and back: the first sentence written while walking.",
            "Three-point-five seconds per movement: eighty-four seconds per round, one hundred sixty-eight for two.",
            "Contains the glide, the dart, the coil, the double-headed pairs, and the tail whip in traveling form.",
            "Form one must run cleanly at speed before form two begins - the alphabet before the sentence.",
            "Practiced in both directions so turns and evasions train symmetrically.",
        ],
        "requirements": [
            "Form one performed cleanly at full speed as the prerequisite.",
            "A floor lane long enough for the full traveling sequence in both directions.",
            "The twenty-four movements learned in four groups of six before joining.",
            "Two complete rounds per session at the students working speed.",
            "Mirror or recording checks to confirm the traveling stances stay at depth.",
        ],
        "standards": [
            "The twenty-four movements run in exact order with no pauses and no skipped transitions.",
            "The form genuinely travels - the start and end points differ by the full lane.",
            "Both directions performed with equal smoothness and equal depth.",
        ],
        "citations": [CIT_WONG, CIT_SHAHAR],
        "sig_lens": (
            "The Signature read: form two is the signature learning "
            "to walk. Public teaching adds movements; the Signature "
            "method adds ground - twenty-four strokes, one hundred "
            "sixty-eight seconds, and the coil proves it can sign "
            "while traveling."
        ),
    },
    {
        "key": "vital-theory-2",
        "name": "Vital-Point Theory II: Meridians and Pressure Points",
        "group": "Vital-Point Theory",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The map gains its rivers. This second theory study adds "
            "the classical meridian system - the jingluo, the channels "
            "along which traditional Chinese medicine maps the bodys "
            "energy and along which the classical martial texts place "
            "their pressure points. Twelve meridians are studied, five "
            "noted points on each, sixty points total, each one "
            "located on the students own body by anatomical landmark "
            "and understood through the same educational lens as the "
            "first study: what structure lies beneath, and why the "
            "classical texts marked it. The study is book-and-body "
            "work, never partner work - points are located with a "
            "fingertip on ones own forearm, wrist, or hand, with light "
            "touch only, as a geography lesson. Classical snake "
            "theory claims the styles precision comes from this "
            "knowledge; the modern student takes from it a deep "
            "respect for the bodys complexity and a reinforced ethic: "
            "the more precisely you understand vulnerability, the more "
            "restraint the art demands."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: obtain a meridian chart from a "
            "traditional Chinese medicine reference and identify the "
            "twelve primary meridians by name and general pathway. Step "
            "2: for each meridian, select five noted points and locate "
            "each on your own body by its anatomical landmark - "
            "light fingertip touch on your own forearm, wrist, or hand "
            "only, never pressing hard. Step 3: for each of the sixty "
            "points, write the landmark and the underlying structure "
            "in your study journal, in your own words. Step 4: study "
            "the meridians two at a time, quizzing yourself until each "
            "pathway and its five points are recalled without the "
            "chart. Step 5: complete the written review - name all "
            "twelve meridians and their pathways from memory, then "
            "check against the reference. Step 6: revisit the full "
            "sixty-point map monthly alongside the twelve primary "
            "points from the first study. The common errors are "
            "treating the chart as mystical rather than anatomical, "
            "pressing points hard on oneself, and memorizing point "
            "names without learning the meridian pathways."
        ),
        "key_points": [
            "Twelve meridians studied, five noted points each: sixty points total, located by anatomical landmark.",
            "Book-and-body study only: light fingertip touch on ones own body, never partner work, never hard pressure.",
            "Each point recorded with its landmark and underlying structure, in the students own words.",
            "The meridians are the rivers of the classical map; the points are the marked crossings.",
            "Greater understanding of vulnerability demands greater restraint - the ethics scale with the knowledge.",
        ],
        "requirements": [
            "A traditional Chinese medicine meridian chart as the reference.",
            "The completed first theory study - twelve primary points - as prerequisite.",
            "A study journal holding all sixty points with landmarks and structures.",
            "Light self-touch only for location; no hard pressure, no partner practice.",
            "Monthly review of the full map alongside the first studys twelve points.",
        ],
        "standards": [
            "All twelve meridians named with their pathways recalled without the chart.",
            "Sixty points located by landmark, each with its underlying structure written down.",
            "Zero partner or hard-pressure practice - the study stays educational throughout.",
        ],
        "citations": [CIT_CLARK, CIT_YANG_QIGONG],
        "sig_lens": (
            "The Signature read: the meridians are the ruled lines "
            "beneath the signature. Public teaching charts the "
            "channels; the Signature method reads the whole page - "
            "sixty crossings, twelve rivers, and the standing rule "
            "that the finer the knowledge, the heavier the restraint "
            "it signs."
        ),
    },
    {
        "key": "snake-vs-crane",
        "name": "Snake Against the Crane: Application Principles",
        "group": "Applications",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Every animal style is measured against the others, and "
            "the classic pairing is snake against crane: the low, "
            "coiling, precise serpent versus the tall, evasive, "
            "winged crane. This record studies the principles of that "
            "matchup as pure theory - five principles, three slow "
            "drills each, fifteen drills per round, all practiced "
            "solo or with a cooperative partner at walking speed. The "
            "principles: stay low where the crane wants height; coil "
            "around the long wing strikes rather than meeting them; "
            "answer evasion with the dart, closing the distance the "
            "crane tries to keep; guard the eyes, which both styles "
            "prize; and never chase - let the cranes movement spend "
            "itself against the coils patience. The southern schools "
            "that preserve both animals teach this pairing as a "
            "lesson in opposites: the student learns the snake by "
            "studying what it is not."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: learn the five principles by "
            "heart - low against high, coil around the wings, dart "
            "against evasion, guard the eyes, never chase. Step 2: "
            "for each principle, practice its three drills solo: for "
            "example, for low-against-high, drill the creep-down, the "
            "low coil hold, and the rising serpent as the answers to "
            "an imaginary high guard. Step 3: perform all fifteen "
            "drills in sequence - five principles times three drills - "
            "at slow, precise speed. Step 4: with a cooperative "
            "partner playing slow, stylized crane movements at walking "
            "speed, apply each principle in turn, freezing to check "
            "positions. Step 5: after each partner round, discuss what "
            "worked: the partner reports whether the principle "
            "genuinely neutralized their movement. Step 6: rotate "
            "roles so both partners study both animals. The common "
            "errors are speeding up before the principles are "
            "understood, treating the partner like an opponent, and "
            "memorizing the drills without grasping the principle "
            "each one demonstrates."
        ),
        "key_points": [
            "Five principles of the classic snake-versus-crane pairing, three slow drills each: fifteen drills per round.",
            "Low against high, coil around the wings, dart against evasion, guard the eyes, never chase.",
            "All partner work at walking speed with a cooperative partner - theory, not sparring.",
            "The student learns the snake by studying what it is not: the lesson of opposites.",
            "Every drill demonstrates its principle; memorized drills without understood principles are empty.",
        ],
        "requirements": [
            "A cooperative partner willing to play slow, stylized crane movements.",
            "The five principles memorized before the first partner round.",
            "Walking speed for all partner work, with freezes to check positions.",
            "All fifteen drills performed per round, three per principle.",
            "Post-round discussion: the partner reports what genuinely worked.",
        ],
        "standards": [
            "Each drill is traceable to its principle - the student can say which principle it demonstrates.",
            "Partner speed never exceeds a walk; no competitive energy enters the drill.",
            "Both partners study both roles over time.",
        ],
        "citations": [CIT_WONG, CIT_REID, CIT_CHOW],
        "sig_lens": (
            "The Signature read: the crane is the signature read "
            "backwards - every stroke the snake makes, reversed. "
            "Public teaching compares the animals; the Signature "
            "method signs the contrast: fifteen drills per round "
            "until the student can write the serpent precisely "
            "because they have studied the wing."
        ),
    },
])
ENTRIES.extend([
    {
        "key": "form-three",
        "name": "Snake Form Three: The Python Sequence (She Quan San Lu)",
        "group": "Forms",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The third form is where the serpent grows heavy. The she "
            "quan san lu, snake form three - the python sequence - is "
            "thirty-six movements of constricting, close-range snake "
            "work: the entanglement entries, the coiling arm strikes, "
            "the drop-coils and rises, and the double-headed pairs, all "
            "performed at close distance to the dummy as if wrapped "
            "around it. At four seconds per movement the form runs one "
            "hundred forty-four seconds; two rounds total two hundred "
            "eighty-eight seconds of continuous constriction. The "
            "python sequence teaches what the earlier forms only "
            "implied: the snake does not only dart, it holds. Students "
            "begin form three only when form two travels cleanly, and "
            "they practice it slowly for months - the close-range "
            "geometry punishes rushing, and every entanglement in the "
            "sequence must be understood before it is performed at "
            "speed."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: confirm form two travels cleanly at "
            "speed - form three is not started until it does. Step 2: "
            "learn the thirty-six movements in six groups of six: the "
            "close entry, the entanglement set, the coiling strikes, "
            "the drop-coils and rises, the double-headed pairs, and "
            "the constricting close with the salute. Step 3: practice "
            "each group at close distance to the dummy, slowly, until "
            "the geometry of every entanglement is understood. Step 4: "
            "join the groups and walk the full form at four seconds "
            "per movement - one hundred forty-four seconds per round. "
            "Step 5: complete two rounds per session, two hundred "
            "eighty-eight seconds total, resting between rounds. Step "
            "6: keep a form journal: note which movements blur at "
            "speed and drill those movements separately. The common "
            "errors are starting form three with form two still "
            "unsteady, practicing the entanglements fast before their "
            "geometry is understood, and drifting away from the dummy "
            "so the close-range work becomes long-range waving."
        ),
        "key_points": [
            "Thirty-six movements of close-range constricting work, performed near the dummy as if wrapped around it.",
            "Four seconds per movement: one hundred forty-four seconds per round, two hundred eighty-eight for two.",
            "The python sequence teaches the lesson the earlier forms implied: the snake does not only dart, it holds.",
            "Form two must travel cleanly before form three begins; entanglements are understood before they are sped up.",
            "A form journal tracks which movements blur at speed for separate drilling.",
        ],
        "requirements": [
            "Form two performed cleanly at full speed as the prerequisite.",
            "A training dummy for the close-range entanglement geometry.",
            "The thirty-six movements learned in six groups of six before joining.",
            "Two complete rounds per session at the students working speed.",
            "A form journal recording the movements that need separate drilling.",
        ],
        "standards": [
            "The thirty-six movements run in exact order with the close distance maintained throughout.",
            "Every entanglement shows correct geometry at slow speed before any speed is added.",
            "The form stays constricting - no drifting to long range.",
        ],
        "citations": [CIT_WONG, CIT_SHAHAR],
        "sig_lens": (
            "The Signature read: form three is the signature wrapping "
            "the page instead of writing on it. Public teaching adds "
            "a longer sequence; the Signature method adds weight - "
            "thirty-six strokes, two hundred eighty-eight seconds, "
            "and the constriction proves the serpent can sign by "
            "holding as well as by striking."
        ),
    },
    {
        "key": "iron-finger",
        "name": "Iron Finger Conditioning (Tie Zhi Gong)",
        "group": "Chi Development",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The advanced hand is built, not born. The tie zhi gong, "
            "iron finger conditioning, is the traditional hardening of "
            "the striking fingers against the canvas bag: the tongue "
            "hand and spear hand thrust into a bag of beans or coarse "
            "sand, starting gently and building over months until the "
            "fingers strike with the solidity the style demands. The "
            "weekly ladder runs fifty thrusts per hand in week one, "
            "then seventy-five, one hundred, and one hundred twenty-"
            "five - three hundred fifty thrusts per hand across the "
            "four-week cycle, each week consolidated before the next. "
            "The work is always followed by recovery: warm water "
            "soaking, gentle massage of the fingers, and rest days "
            "between hard sessions, because conditioning grows during "
            "recovery, not during impact. The iron rule from the "
            "basics still governs, sharpened: any sharp pain, any "
            "swelling that does not fade overnight, any numbness - "
            "stop, rest, and resume lighter. Iron fingers are earned "
            "in seasons, and the impatient inherit injuries."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: prepare the bag - canvas filled "
            "with mung beans for beginners, the traditional starting "
            "medium, hung or set at chest height. Step 2: form the "
            "tongue hand and thrust the fingertips into the bag with "
            "short, controlled penetrations - the wrist straight, the "
            "power from the arm, never a bent-wrist stab. Step 3: "
            "perform the weeks quota - fifty thrusts per hand in week "
            "one - at a steady rhythm, alternating hands. Step 4: "
            "repeat with the spear hand formation for half the quota, "
            "building the full-hand thrust alongside the two fingers. "
            "Step 5: after every session, soak the hands in warm water "
            "for ten minutes and massage each finger gently from base "
            "to tip. Step 6: advance one rung per week - seventy-five, "
            "one hundred, one hundred twenty-five - only with zero "
            "sharp pain, zero lingering swelling, zero numbness. The "
            "common errors are starting on sand instead of beans, "
            "thrusting with a bent wrist, skipping the soak and "
            "massage, and training daily without rest days."
        ),
        "key_points": [
            "Four-week ladder: fifty, seventy-five, one hundred, one hundred twenty-five thrusts per hand - three hundred fifty total.",
            "Canvas bag of mung beans first; the traditional starting medium, never sand at the start.",
            "Every session ends with a ten-minute warm soak and gentle finger massage.",
            "Sharp pain, lingering swelling, or numbness means stop, rest, and resume lighter.",
            "Conditioning grows during recovery: rest days between hard sessions are mandatory.",
        ],
        "requirements": [
            "A canvas conditioning bag filled with mung beans, hung or set at chest height.",
            "Completed finger conditioning basics - the six-week fingertip ladder - as prerequisite.",
            "Straight wrists on every thrust; the power comes from the arm, never a bent-wrist stab.",
            "Warm water soak and finger massage after every session without exception.",
            "Rest days between hard sessions; zero sharp pain before advancing a rung.",
        ],
        "standards": [
            "No rung is advanced with any sharp pain, lingering swelling, or numbness present.",
            "The weekly quota is completed per hand, both hands advancing together.",
            "The soak-and-massage recovery is performed after every session, logged in the training journal.",
        ],
        "citations": [CIT_YANG, CIT_CHOW, CIT_YANG_QIGONG],
        "sig_lens": (
            "The Signature read: iron finger is the signature pressed "
            "into steel - the hand becoming the seal it stamps. Public "
            "teaching hardens the fingers; the Signature method tempers "
            "the patience: three hundred fifty thrusts per hand per "
            "cycle, each one a hammer blow on the impatience that "
            "would have broken them."
        ),
    },
    {
        "key": "silk-energy",
        "name": "Chi Development: Coiling Silk Energy (Chan Si Jin)",
        "group": "Chi Development",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Power that spirals cannot be stopped head-on. The chan si "
            "jin, coiling silk energy, is the advanced energy practice "
            "of the coiling arts: the practitioner draws continuous "
            "spirals with the hands and waist - reeling the silk, as "
            "the classical image has it, drawing a single thread from "
            "a cocoon without breaking it - training force to travel "
            "in curves rather than straight lines. Ten minutes of "
            "practice at four seconds per spiral circle gives one "
            "hundred fifty continuous coils, each one smooth, each one "
            "unbroken, the hands never stopping and never jerking. "
            "The classical theory holds that spiraling force penetrates "
            "where straight force is blocked, the way a drill enters "
            "wood that would split a nail; the modern student "
            "experiences it as whole-body coordination, the waist, "
            "shoulders, elbows, and wrists turning as one threaded "
            "system. The silk must never break: any jerk or stop "
            "restarts the count for that minute."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: stand in a medium snake stance, "
            "arms rounded in front as if embracing a large ball. Step "
            "2: begin drawing a horizontal spiral with both hands - "
            "outward and around, the waist turning with the hands, "
            "the whole body participating in the coil. Step 3: keep "
            "the motion continuous and smooth, about four seconds per "
            "full circle, imagining a silk thread paying out from the "
            "hands that must never snap. Step 4: after five minutes, "
            "reverse the spiral direction without stopping, and "
            "continue for five more minutes - one hundred fifty coils "
            "total in ten minutes. Step 5: if the motion jerks or "
            "stops, restart the count for that minute; the unbroken "
            "thread is the standard. Step 6: finish by standing still "
            "for a minute, hands resting, feeling the spiraling "
            "sensation continue in the body. The common errors are "
            "moving only the hands while the waist stays still, "
            "rushing the circles so the thread would snap, and "
            "holding the breath instead of breathing with the coils."
        ),
        "key_points": [
            "Continuous spirals drawn with hands and waist: one hundred fifty unbroken coils in ten minutes.",
            "Four seconds per circle; the motion never jerks and never stops - the silk must not break.",
            "Classical theory: spiraling force penetrates where straight force is blocked, like a drill versus a nail.",
            "The whole body coils as one threaded system: waist, shoulders, elbows, wrists together.",
            "A jerk or stop restarts the count for that minute - continuity is the standard.",
        ],
        "requirements": [
            "Established snake breathing practice as the prerequisite calm.",
            "A clear space allowing full arm spirals without striking anything.",
            "The waist turning with the hands on every coil - no hands-only spiraling.",
            "Ten continuous minutes, five per direction, at about four seconds per circle.",
            "Breathing synchronized with the coils, never held.",
        ],
        "standards": [
            "One hundred fifty coils completed with no jerks and no stops.",
            "The waist visibly drives every spiral; the arms follow the bodys coil.",
            "The thread image held throughout - smooth, continuous, unbroken.",
        ],
        "citations": [CIT_YANG_QIGONG, CIT_WONG],
        "sig_lens": (
            "The Signature read: the silk is the signature drawn "
            "without lifting the pen for ten minutes. Public teaching "
            "practices spiraling energy; the Signature method practices "
            "the unbroken line - one hundred fifty coils, and the "
            "proof of mastery is that the thread never snapped."
        ),
    },
    {
        "key": "spear-hand",
        "name": "Snake Spear Hand Penetration (She Mao Shou)",
        "group": "Strikes",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Two fingers pick a point; five fingers drive through it. "
            "The she mao shou, the snake spear hand, joins all five "
            "fingers into a single rigid spear - fingers together, "
            "thumb pressed tight, the hand a blade - and thrusts it "
            "with the full body behind it, the classical penetrating "
            "strike of the advanced snake stylist. The southern "
            "schools teach the spear as the tongue hands elder "
            "brother: where the two fingers dart, the five fingers "
            "drive, and the conditioning of the iron finger ladder is "
            "its prerequisite. The drill is one hundred thrusts per "
            "session against the bean bag, each thrust a short "
            "penetration with the body falling forward behind it, the "
            "depth of penetration marked on the bag in four stages - "
            "two, three, four, five centimeters - as the months pass. "
            "The spear hand is never practiced on people or on hard "
            "surfaces; it is a bag-and-dummy technique, and the "
            "advanced student treats it with the gravity its power "
            "demands."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: confirm the iron finger ladder is "
            "complete - the spear hand is not attempted without "
            "conditioned fingers. Step 2: form the spear - all five "
            "fingers extended together and pressed tight, thumb folded "
            "hard against the index finger, wrist locked straight. "
            "Step 3: face the bean bag in a medium stance, spear hand "
            "chambered at the hip. Step 4: thrust - drive the spear "
            "forward with a short penetration, the body falling "
            "forward behind the hand, the wrist absolutely straight, "
            "then withdraw instantly. Step 5: repeat for one hundred "
            "thrusts per session, alternating hands, marking the "
            "penetration depth on the bag: two centimeters at first, "
            "advancing to three, four, and five over the months. Step "
            "6: soak and massage the hands after every session, exactly "
            "as in the iron finger practice. The common errors are "
            "attempting the spear without completing the conditioning "
            "ladder, bending the wrist on impact, and thrusting at "
            "anything harder than the bean bag."
        ),
        "key_points": [
            "All five fingers joined into a single spear: the tongue hands elder brother, the penetrating strike.",
            "One hundred thrusts per session against the bean bag, penetration marked at two, three, four, five centimeters.",
            "The iron finger conditioning ladder is the absolute prerequisite - no exceptions.",
            "The wrist stays absolutely straight; the body falls forward behind the thrust.",
            "Bag and dummy only, never people, never hard surfaces - treated with the gravity its power demands.",
        ],
        "requirements": [
            "The completed iron finger ladder - conditioned fingers verified before the first spear thrust.",
            "A canvas bean bag at chest height; no harder target, ever.",
            "The five-finger spear formation with the thumb locked tight and the wrist straight.",
            "One hundred thrusts per session, alternating hands, with depth marked on the bag.",
            "The full soak-and-massage recovery after every session.",
        ],
        "standards": [
            "Every thrust shows a straight wrist from chamber to withdrawal - no bending on impact.",
            "Penetration depth advances one centimeter at a time, only after the current depth is consistent.",
            "Zero practice on people or hard surfaces, without exception.",
        ],
        "citations": [CIT_WONG, CIT_CHOW, CIT_SMITH],
        "sig_lens": (
            "The Signature read: the spear is the signature written "
            "with the whole hand at once. Public teaching penetrates; "
            "the Signature method commits - one hundred thrusts per "
            "session, five centimeters of proof, and the iron rule "
            "that the hand which can write this deeply must be the "
            "hand most careful where it writes."
        ),
    },
    {
        "key": "strikes-water",
        "name": "Serpent Strikes the Water: Diving Application (She Ru Shui)",
        "group": "Applications",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The serpent dives and the surface barely ripples. The she "
            "ru shui, the serpent strikes the water, is the advanced "
            "diving application: from standing, the body drops, glides "
            "low, and rises through the target line in a single "
            "flowing sequence - six phases, two seconds each, twelve "
            "seconds per repetition, five repetitions per round, sixty "
            "seconds of diving serpent. The application chains "
            "everything the ladder built: the creep-down becomes the "
            "dive, the glide becomes the underwater travel, the rising "
            "serpent becomes the breach, and the tongue hand strikes as "
            "the body surfaces. It is practiced on the dummy and in "
            "the air, and it is the styles answer to the question of "
            "how low the snake is willing to go: all the way down, "
            "and back up through the opening the dive created. The "
            "sequence must flow as one water-smooth motion; any phase "
            "performed as a separate technique breaks the dive."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: stand at medium distance from the "
            "dummy in a snake stance, guard up. Step 2: phase one and "
            "two - sink into the creep-down (two seconds), then glide "
            "low past the dummys line (two seconds), the body near the "
            "floor. Step 3: phases three and four - coil at the low "
            "point (two seconds), then begin the rising serpent breach "
            "(two seconds), the body ascending along its spiral. Step "
            "4: phases five and six - as the body surfaces, the tongue "
            "hand strikes along the opened line (two seconds), then "
            "recoil and settle to guard (two seconds). Step 5: the "
            "full twelve-second sequence must flow without pauses "
            "between phases - one water-smooth motion. Step 6: repeat "
            "five times per round, sixty seconds of diving, then rest "
            "and review which phase broke the flow. The common errors "
            "are pausing between phases, rising straight up instead of "
            "along the spiral, and striking before the body has "
            "surfaced - the strike belongs to the breach, not the "
            "dive."
        ),
        "key_points": [
            "Six phases, two seconds each: twelve seconds per repetition, five repetitions, sixty seconds per round.",
            "Chains the ladder: creep-down as the dive, glide as underwater travel, rising serpent as the breach.",
            "The tongue hand strikes as the body surfaces - the strike belongs to the breach, not the dive.",
            "Practiced on the dummy and in the air; the sequence must flow as one water-smooth motion.",
            "The styles answer to how low the snake will go: all the way down, and up through the opening.",
        ],
        "requirements": [
            "Mastery of the creep-down, the glide, the rising serpent, and the tongue hand as prerequisites.",
            "A training dummy marking the target line for the breach.",
            "A clear floor allowing the full low glide without obstruction.",
            "All six phases performed at two seconds each with no pauses between them.",
            "Five complete repetitions per round with a flow review after each.",
        ],
        "standards": [
            "The twelve-second sequence runs with no pauses between phases - one continuous motion.",
            "The ascent follows the spiral path, never a straight pop-up.",
            "The strike lands with the surfacing, not before and not after.",
        ],
        "citations": [CIT_WONG, CIT_CHOW],
        "sig_lens": (
            "The Signature read: the dive is the signature written "
            "underwater - invisible until it surfaces. Public teaching "
            "chains techniques; the Signature method pours them: six "
            "phases, sixty seconds, and the proof of the pour is that "
            "no seam shows between the waters."
        ),
    },
    {
        "key": "vital-applications",
        "name": "Vital-Point Training Drills (Partner-Safe)",
        "group": "Vital-Point Theory",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Knowledge of points is completed by discipline with "
            "points. This record contains the eight partner-safe "
            "training drills that apply the vital-point studies without "
            "any contact to vulnerable areas: locating points on ones "
            "own body by landmark, guiding a partners hand to a safe "
            "landmark like the forearm, practicing the tongue hands "
            "accuracy on marked pads placed over safe zones, rehearsing "
            "the ethics responses - when to stop, when to refuse, when "
            "to walk away - and drilling the restraint forms that end "
            "every application at the point of control rather than "
            "harm. The contact flag for every drill in this record is "
            "zero: no drill makes contact with any vulnerable point on "
            "any person, ever, and any partner may stop any drill at "
            "any moment for any reason. The classical texts pair point "
            "knowledge with the heaviest ethical weight in the art; "
            "this record makes that pairing physical. Eight drills, "
            "zero contact, one ethic: the deeper the knowledge, the "
            "lighter the hand."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: review the twelve primary points and "
            "the sixty meridian points from the two theory studies - "
            "this record is not started until both are complete. Step "
            "2: drill one - locate each point on your own body by "
            "landmark with light touch, naming the structure beneath. "
            "Step 3: drills two and three - with a partner, guide their "
            "hand to safe landmarks on the forearm, practicing precise "
            "location with zero pressure. Step 4: drills four and five "
            "- tongue hand accuracy on marked pads worn over safe "
            "training zones, ten clean strikes per pad. Step 5: drills "
            "six through eight - the ethics rehearsals: practice "
            "stopping mid-technique on a partners stop word, refusing "
            "an unsafe drill clearly, and ending every application "
            "sequence at control. Step 6: log all eight drills in the "
            "training journal with the contact flag marked zero for "
            "each. The common errors are treating the ethics drills "
            "as less important than the location drills, applying "
            "pressure during location practice, and skipping the stop-"
            "word rehearsal."
        ),
        "key_points": [
            "Eight partner-safe drills applying the point studies with zero contact to vulnerable areas - contact flag zero.",
            "Location by landmark on ones own body; guided location on safe zones like the forearm, zero pressure.",
            "Tongue hand accuracy drilled on marked pads over safe training zones.",
            "Ethics rehearsals: stopping on the stop word, refusing unsafe drills, ending at control.",
            "Any partner may stop any drill at any moment for any reason - the rule is absolute.",
        ],
        "requirements": [
            "Both vital-point theory studies completed as the prerequisite.",
            "A cooperative partner briefed on the stop word and the absolute stop rule.",
            "Marked pads for the accuracy drills, worn over safe training zones.",
            "A training journal logging all eight drills with the contact flag at zero.",
            "Zero pressure during all location practice - landmarks, not targets.",
        ],
        "standards": [
            "The contact flag reads zero for every drill, every session, without exception.",
            "The stop word is rehearsed and honored instantly in every partner drill.",
            "Every application sequence in the students practice ends at control, never past it.",
        ],
        "citations": [CIT_CLARK, CIT_REID],
        "sig_lens": (
            "The Signature read: these drills are the signature "
            "practicing restraint as a technique. Public teaching "
            "guards safety; the Signature method signs the heaviest "
            "line in the whole database - eight drills, zero contact, "
            "and the proof of the serpent is the hand it never "
            "closes."
        ),
    },
    {
        "key": "python-coils",
        "name": "Python Coils: Entrapment Applications (She Chan Ying Yong)",
        "group": "Applications",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The constrictor does not strike to kill; it wraps to "
            "hold. The she chan ying yong, the python coils "
            "entrapment applications, are the advanced close-range "
            "studies of the constricting principle: three wraps with "
            "two arms - six control points - applied in a five-step "
            "sequence against a cooperative partners slow extended "
            "guard, practiced at walking speed with zero force. The "
            "steps: enter inside the guard line, coil the first wrap "
            "around the partners arm, settle the second wrap across "
            "the elbow line, rest the third wrap in a controlling "
            "hold, and freeze while both partners verify the geometry. "
            "Nothing is squeezed, nothing is wrenched; the entrapment "
            "is a study in positional control, and the partners "
            "comfort is the continuous gauge - any discomfort ends the "
            "repetition immediately. The python teaches the final "
            "lesson of the close range: control is a position, not a "
            "pressure."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: the partner extends a slow guard "
            "at walking speed; the stylist glides inside the guard "
            "line - enter, step one. Step 2: coil the lead arm around "
            "the partners arm in the wrapping spiral - the first wrap, "
            "light contact, no gripping. Step 3: settle the second arm "
            "across the partners elbow line, completing the second "
            "wrap - six control points now in place across three wraps "
            "and two arms. Step 4: rest the third wrap into a holding "
            "position that controls the partners movement options, "
            "then freeze - both partners check the geometry and the "
            "partners comfort. Step 5: release cleanly on the partners "
            "word, reset, and repeat the five-step sequence - then "
            "swap roles so both partners study the coils. Step 6: "
            "log the session, noting any repetition stopped for "
            "discomfort and what caused it. The common errors are "
            "gripping instead of wrapping, applying pressure to "
            "prove the hold, moving faster than the geometry is "
            "understood, and skipping the role swap."
        ),
        "key_points": [
            "Three wraps with two arms: six control points in a five-step sequence, practiced at walking speed, zero force.",
            "Enter, coil, settle, rest, freeze-and-verify: control is a position, not a pressure.",
            "Nothing squeezed, nothing wrenched; the partners comfort is the continuous gauge.",
            "Any discomfort ends the repetition immediately - the rule is absolute.",
            "Both partners study both roles; the coils are understood from inside and outside.",
        ],
        "requirements": [
            "A cooperative partner briefed on the zero-force rule and the absolute stop rule.",
            "Mastery of the entanglement entries and form three as prerequisites.",
            "A clear mat area with room to enter inside the guard line safely.",
            "Light wrapping contact only - no gripping, no squeezing, no wrenching.",
            "A session log noting every stopped repetition and its cause.",
        ],
        "standards": [
            "All six control points placed by wrapping geometry, never by force.",
            "The partner reports comfort at the freeze on every repetition.",
            "Roles swapped every round; no one only coils and no one is only coiled.",
        ],
        "citations": [CIT_WONG, CIT_REID],
        "sig_lens": (
            "The Signature read: the python signs by holding the page "
            "still. Public teaching studies entrapment; the Signature "
            "method studies the gentlest signature in the database - "
            "six control points, zero force, and the proof written "
            "in the partners ease."
        ),
    },
    {
        "key": "form-four",
        "name": "Snake Form Four: Nine-Bend Serpent (Jiu Qu She)",
        "group": "Forms",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The serpent that cannot bend cannot survive. The jiu qu "
            "she, the nine-bend serpent, is the fourth and most "
            "demanding snake form: nine bends - nine full directional "
            "changes - with four movements at each bend, thirty-six "
            "movements total, the practitioner weaving across the "
            "floor like a serpent through grass. At four seconds per "
            "movement the form runs one hundred forty-four seconds of "
            "continuous directional change, and every bend must keep "
            "the coil: the low stance, the spiraling waist, the guard "
            "that never drops through the turn. The nine bends test "
            "everything the ladder built - footwork that glides "
            "without bobbing, a waist that coils under load, hands "
            "that hold their shapes while the body changes direction, "
            "and a memory that keeps thirty-six movements in order "
            "while the floor spins. Students perform form four only "
            "after form three is steady, and they perform it for "
            "years: the bends deepen as the stylist does."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: confirm form three runs steadily - "
            "form four is not started until it does. Step 2: learn the "
            "nine bends as nine stations: at each station, four "
            "movements - arrive in the coil, strike or deflect, coil "
            "the turn, depart along the new line. Step 3: practice the "
            "stations one at a time, slowly, until each bend keeps the "
            "low stance and the guard through the directional change. "
            "Step 4: join the stations in order and walk the full "
            "thirty-six movements at four seconds each - one hundred "
            "forty-four seconds - keeping every bend coiled. Step 5: "
            "perform the form facing different starting directions so "
            "no bend becomes a favored turn. Step 6: review monthly "
            "against the foundations: the glide still level, the "
            "tongue hands still crisp, the nine bends still nine. The "
            "common errors are straightening up through the bends, "
            "dropping the guard during directional changes, losing "
            "count of the bends, and rushing the form before the "
            "stations are steady."
        ),
        "key_points": [
            "Nine bends, four movements each: thirty-six movements of continuous directional change.",
            "Four seconds per movement: one hundred forty-four seconds of weaving serpent.",
            "Every bend keeps the coil - low stance, spiraling waist, guard never dropping through the turn.",
            "Form three must run steadily before form four begins; the bends deepen as the stylist does.",
            "Practiced from different starting directions so no bend becomes a favored turn.",
        ],
        "requirements": [
            "Form three performed steadily as the prerequisite.",
            "A large floor area allowing nine full directional changes with travel.",
            "The nine stations learned one at a time before joining.",
            "One hundred forty-four seconds per full performance at the students working speed.",
            "Monthly review against the foundations: glide, hand shapes, stance depth.",
        ],
        "standards": [
            "All nine bends completed with the coil intact - no straightening through the turns.",
            "The thirty-six movements run in exact order from any starting direction.",
            "The guard stays up through every directional change without exception.",
        ],
        "citations": [CIT_WONG, CIT_SHAHAR],
        "sig_lens": (
            "The Signature read: nine bends are the signature proving "
            "it can be read from any angle. Public teaching performs "
            "a long form; the Signature method weaves a seal - thirty-"
            "six strokes, one hundred forty-four seconds, and the "
            "serpent that bends nine times without breaking is the "
            "signature that cannot be forged."
        ),
    },
    {
        "key": "master-sequence",
        "name": "The Master Sequence: Full Snake System Synthesis",
        "group": "Applications",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "At the end of the ladder the serpent looks back at the "
            "whole path. The master sequence is the synthesis "
            "performance of the complete snake system: all four forms "
            "performed in order - eighteen, twenty-four, thirty-six, "
            "and thirty-six movements, one hundred fourteen movements "
            "total - at an average of three-point-five seconds each, "
            "about three hundred ninety-nine seconds of continuous "
            "snake kung fu, nearly seven minutes without stopping. The "
            "sequence is not a test of memory but of integration: the "
            "salute that opens form one must carry the same precision "
            "as the final bend of form four, the breathing learned in "
            "the chi studies must sustain the whole performance, and "
            "the restraint studied in the vital-point drills must be "
            "present in every strike. Students attempt the master "
            "sequence only when all four forms run cleanly on their "
            "own; most perform it monthly as a measure of the system "
            "living in the body. One hundred fourteen movements, one "
            "serpent, one signature."
        ),
        "how_it_works": (
            "HOW TO DO IT. Step 1: confirm all four forms run cleanly "
            "at speed on their own - the sequence is not attempted "
            "until they do. Step 2: perform form one (eighteen "
            "movements), rest one minute, perform form two (twenty-"
            "four), rest one minute, perform form three (thirty-six), "
            "rest one minute, perform form four (thirty-six) - one "
            "hundred fourteen movements, about three hundred ninety-"
            "nine seconds of performance plus rests. Step 3: keep the "
            "snake breathing rhythm through the rests - in six, hold "
            "three, out nine - so the body recovers without cooling. "
            "Step 4: after the sequence, sit quietly for five minutes, "
            "then write the session in the training journal: which "
            "form wavered, which transitions blurred, what the breath "
            "did at minute five. Step 5: drill the weak points "
            "separately in the following weeks training. Step 6: "
            "repeat the master sequence monthly, comparing each "
            "performance to the last - the measure is integration, "
            "not speed. The common errors are attempting the sequence "
            "with a form still unsteady, skipping the rests and "
            "collapsing at form three, and treating the sequence as a "
            "finish line instead of a monthly measure."
        ),
        "key_points": [
            "All four forms in order: eighteen plus twenty-four plus thirty-six plus thirty-six - one hundred fourteen movements.",
            "About three hundred ninety-nine seconds of performance: nearly seven minutes without stopping.",
            "A test of integration, not memory: precision, breathing, and restraint sustained across the whole sequence.",
            "Snake breathing through the rests keeps the body recovering without cooling.",
            "Performed monthly as the measure of the system living in the body.",
        ],
        "requirements": [
            "All four forms performed cleanly at speed as the prerequisite.",
            "A large clear space and thirty minutes of uninterrupted time.",
            "One-minute breathing rests between forms, kept to the six-three-nine rhythm.",
            "A training journal entry after every sequence: weak forms, blurred transitions, breath behavior.",
            "Separate drilling of the weak points in the following weeks.",
        ],
        "standards": [
            "One hundred fourteen movements in exact order across the four forms.",
            "The first salute and the final bend show equal precision - no fading.",
            "The sequence is repeated monthly, each performance compared to the last.",
        ],
        "citations": [CIT_WONG, CIT_SHAHAR, CIT_YANG_QIGONG],
        "sig_lens": (
            "The Signature read: the master sequence is the complete "
            "signature, written end to end without lifting the pen. "
            "Public teaching synthesizes a curriculum; the Signature "
            "method signs the whole system at once - one hundred "
            "fourteen strokes, three hundred ninety-nine seconds, one "
            "serpent, and the page is finally, fully signed."
        ),
    },
])
