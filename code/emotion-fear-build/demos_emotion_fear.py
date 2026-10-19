#!/usr/bin/env python3
"""Scenario-simulator demos for The Fear Emotion Database.

Each demo is a standalone, runnable Python program: it takes a scenario
(situation + intensity setting), simulates fear unfolding across six
scenes — Trigger, Rise, Peak, Turning Point, Easing, Afterglow — computing
per-scene intensity, heart rate, and breath rate from a deterministic
arousal model, prints the scene-by-scene simulation (inner voice, body,
focus detail), then asserts tight structural bounds (never float
exact-equality) and ends with the OK marker.

The numbers are real computed values from the model, and each scenario is
drawn from its record's content so demo output cross-checks the entry
text: body-signal demos compute the racing heart the entry describes,
cascade demos show the link-by-link chain, blend demos run the mixed
signal, and the showcase demo walks the full six-scene arc.
"""

import json

_TMPL = r'''
import math, json

SITUATION = __SIT__
INTENSITY = __INT__
FOCUS = __FOCUS__
LINES = json.loads(__LINES__)
HR0 = __HR0__

SCENE_NAMES = ["Trigger", "Rise", "Peak", "Turning Point", "Easing", "Afterglow"]

def run(label, intensity):
    peak_set = 0.25 + 0.75 * intensity
    vals = []
    for k in range(6):
        if k <= 2:
            v = peak_set * (k + 1) / 3.0
        else:
            v = peak_set * math.exp(-1.1 * (k - 2))
        vals.append(v)
    hrs = [int(round(HR0 + 95 * v)) for v in vals]
    brs = [int(round(14 + 30 * v)) for v in vals]
    print("RUN: " + label + " (intensity setting %.2f)" % intensity)
    for k in range(6):
        bar = "#" * int(round(vals[k] * 20))
        print("  scene %d %-13s intensity %.3f [%s]" % (k + 1, SCENE_NAMES[k], vals[k], bar))
        print("    inner : " + LINES[k])
        print("    body  : heart %d bpm, breath %d/min" % (hrs[k], brs[k]))
        print("    focus : %s %s" % (FOCUS, "signal rising" if k <= 2 else "signal settling"))
    peak = max(vals)
    auc = sum(vals)
    rec = next(k for k in range(3, 6) if vals[k] < 0.30 * peak)
    assert all(0.0 <= v <= 1.0 for v in vals), "intensity out of range"
    assert 0.50 <= peak <= 1.0, "peak out of bounds"
    assert vals.index(peak) == 2, "peak misplaced"
    assert vals[0] < vals[1] < vals[2], "rise not monotonic"
    assert vals[5] < 0.30 * peak, "no recovery by final scene"
    assert all(50 <= h <= 210 for h in hrs), "heart rate out of bounds"
    assert all(8 <= b <= 60 for b in brs), "breath rate out of bounds"
    assert auc > 1.0, "area under curve too small"
    assert 3 <= rec <= 5, "recovery scene out of range"
    print("  summary: peak=%.3f auc=%.3f recovery_scene=%d max_hr=%d" % (peak, auc, rec + 1, max(hrs)))
    return peak, auc

print("SCENARIO: " + SITUATION)
print("FOCUS: " + FOCUS)
__RUNS__
print("OK: fear scenario simulation complete")
'''


def _prog(situation, intensity, focus, lines, hr0=72, compare=None):
    assert len(lines) == 6, "need 6 scene lines"
    assert 0.35 <= intensity <= 0.95, "intensity out of demo range"
    if compare is None:
        runs = "run(\"main\", INTENSITY)"
    else:
        lo, hi = compare
        runs = ("p_lo, a_lo = run(\"low-volume\", %r)\n"
                "p_hi, a_hi = run(\"high-volume\", %r)\n"
                "assert 0.50 <= p_lo < p_hi <= 1.0, \"volume ordering broken\"\n"
                "assert a_hi > a_lo > 1.0, \"area ordering broken\"\n"
                "print(\"  compare: low peak=%%.3f high peak=%%.3f\" %% (p_lo, p_hi))" % (lo, hi))
    return (_TMPL
            .replace("__SIT__", json.dumps(situation))
            .replace("__INT__", repr(intensity))
            .replace("__FOCUS__", json.dumps(focus))
            .replace("__LINES__", json.dumps(json.dumps(lines)))
            .replace("__HR0__", repr(hr0))
            .replace("__RUNS__", runs))


def _mk(situation, intensity, focus, lines, hr0=72, compare=None):
    def demo(hdr, name, rid, group, key_points, req):
        return hdr(name, rid, group) + _prog(situation, intensity, focus,
                                            lines, hr0, compare)
    return demo


DEMOS = {
"fear-definition": _mk(
    "A sudden loud crash in the night while you are half asleep.", 0.62,
    "the alarm signal itself",
    ["What was that? Something is wrong.",
     "Heart thudding now — the alarm is ringing.",
     "Every sense locked on the dark hallway.",
     "It was the wind. The alarm was doing its job.",
     "Breath slowing; the signal stands down.",
     "Quiet again — the alarm was information, not a flaw."], 74),

"fear-family": _mk(
    "A startling headline that mixes fear with a flash of anger.", 0.55,
    "un-blending the mixture",
    ["That headline hit like a slap.",
     "Afraid of what it means — and angry it happened.",
     "Two feelings shouting at once.",
     "Naming them: fear of the threat, anger at the cause.",
     "Each half quieter once named.",
     "One feeling again — the blend has separated."], 70),

"fear-volumes": _mk(
    "The same strange noise in the house, heard three nights running.", 0.50,
    "estimating the volume",
    ["There it is again — that noise.",
     "Night one it was a 7. Tonight it feels like a 4.",
     "Attention up, but hands steady.",
     "Checking: pipes cooling. A 3, honestly.",
     "The right response for a 3: note it, move on.",
     "Volume estimated, response fitted — the skill working."], 68),

"fear-myths": _mk(
    "Admitting to a friend that you were scared, feeling ashamed of it.", 0.45,
    "the myth dissolving",
    ["I was scared — and I hate saying it.",
     "The shame arrives second, louder than the fear.",
     "Wait: the alarm ringing is not a character flaw.",
     "Saying it out loud: I was afraid. That is all.",
     "The shame has nothing left to stand on.",
     "Just the old scare now — smaller, ordinary, human."], 70),

"fear-firstperson": _mk(
    "Standing at the top of a high staircase, looking down.", 0.70,
    "the inside view",
    ["The drop pulls at my eyes.",
     "Chest tight, hands light — the ancient weather.",
     "Time stretches; one second holds three thoughts.",
     "A small voice doing the math: railing, steps, hold on.",
     "Descending slowly, hand on the rail.",
     "Bottom step. The weather passes — I recognize it now."], 76),

"fear-arc": _mk(
    "A car backfiring outside your window at midnight.", 0.66,
    "the four-act arc",
    ["BANG — upright in bed, heart slamming. (onset)",
     "Frozen, listening — every muscle braced. (rise)",
     "Silence. Just an engine fading. (peak passing)",
     "It was a car. Breath coming back. (fading)",
     "Shaky laugh in the dark.",
     "Hands still trembling a little — the engine cooling. (aftershock)"], 78),

"fear-low-high": _mk(
    "A creak in an empty house — imagined at two volumes.", 0.60,
    "ripple versus wave",
    ["A creak from the hallway.",
     "Low: head turns, one hard heartbeat, listening.",
     "Low: just the house settling — back to the book.",
     "High: BANG at the door — whole body slams alert.",
     "High: breath stopped, hands crushing the chair.",
     "Both pass. Low borrowed a minute; high borrowed the body."],
    72, compare=(0.35, 0.90)),

"fear-anger-blend": _mk(
    "Cornered by an aggressive dog on a narrow path.", 0.78,
    "the run-or-fight argument",
    ["Dog lunging, barking — no room to pass.",
     "Back away slowly — and part of me wants to shout it down.",
     "Cold fear plus hot anger, tangled.",
     "Naming it: afraid AND angry. Two signals, not one.",
     "Fear first: increase distance, steadily.",
     "Anger scheduled second: report the loose dog. Sequenced."], 80),

"fear-day": _mk(
    "The email with the subject line: We need to talk.", 0.52,
    "an ordinary day's visits",
    ["Subject line lands like a stone.",
     "Heart drops before the message even opens.",
     "Opened: it is about the office party. False alarm.",
     "Shaky laugh at my own alarm.",
     "Refund arrives as relief.",
     "Logged: one visit, volume 5, reason none. The pattern shows."], 72),

"fear-body": _mk(
    "Footsteps behind you on a dark street, gaining.", 0.72,
    "the honest reporter",
    ["Footsteps — closer than they should be.",
     "Heart hammering into the ears.",
     "Breath shallow and fast; mouth dry.",
     "Muscles coiled, skin prickling, palms damp.",
     "Crossing to the lit side, pace steady, keys ready.",
     "Footsteps fade past. Body still reporting for a while."], 82),

"fear-posture": _mk(
    "Walking past a group of strangers on a dark street.", 0.60,
    "the silhouette",
    ["Shoulders climbing before I notice.",
     "Chest caving, arms pulled in close.",
     "Feet quick and light, hugging the lit edge.",
     "Head swiveling — the old choreography.",
     "Past them. Deliberately uncurling: drop shoulders, open chest.",
     "The uncurling sends its memo — the alarm eases."], 74),

"fear-sleep": _mk(
    "Lying awake at 2 a.m. replaying the day's scare.", 0.48,
    "the night shift",
    ["Eyes open in the dark, replaying it.",
     "Stomach knotted — dinner sits uneaten in memory.",
     "Shoulders still half-braced against the pillow.",
     "Breath shallow; the bed feels like a watch post.",
     "Slow exhales, one by one. The kitchen can reopen tomorrow.",
     "Drifting at last — the system standing down in waves."], 66),

"fear-differences": _mk(
    "Two friends walking through the same haunted house.", 0.55,
    "same machinery, different calibration",
    ["The first scare: a slam and a scream.",
     "Friend one goes pale and silent, frozen mid-step.",
     "Friend two flushes, laughs too loud, keeps moving.",
     "Same hallway, same machinery — different calibration.",
     "Neither response is the correct one. Both are honest.",
     "Outside, comparing notes without judgment."], 72),

"fear-face": _mk(
    "Catching the threat's reflection in a dark window.", 0.68,
    "the universal mask",
    ["Movement in the glass — someone behind me.",
     "Brows fly up and knit; eyes go wide.",
     "Mouth stretches thin; breath catches.",
     "The mask is on before thought arrives.",
     "Turning: a coat on a hook. The face asked first.",
     "Brow lowering in stages; the mask dismantles."], 76),

"fear-face-intensity": _mk(
    "The same scare shown at a whisper and at a shout.", 0.62,
    "the dimmer switch",
    ["Whisper: inner brows lift a fraction.",
     "Whisper: lids rise a millimeter — concern, not alarm.",
     "Shout: full mask — brows, eyes, stretched mouth.",
     "Shout: jaw drops, nostrils flare.",
     "Fading: the shaky half-smile of relief overlaps.",
     "Same face, different brightness — graded, not toggled."],
    70, compare=(0.35, 0.90)),

"fear-hidden": _mk(
    "Trying to look calm in a job interview after receiving bad news.", 0.58,
    "what leaks through",
    ["Sitting up straight, face arranged neutral.",
     "The mouth obeys. The brows do not.",
     "A quarter-second brow flash — there, gone.",
     "Blinking faster; voice climbing half a step.",
     "Pressing on, kindly pretending not to notice myself.",
     "After: the mask drops in the elevator. The leak was honest."], 74),

"fear-artist": _mk(
    "An actor rehearsing the fear face alone in a mirror.", 0.50,
    "crafting the signal",
    ["Neutral face. Now: brows up AND knitted.",
     "Eyes widened, lower lids tense, gaze fixed.",
     "Mouth stretched horizontally, corners back.",
     "Head pulls back a fraction, chin tucks.",
     "Not surprise — surprise is smooth. This is knitted.",
     "Holding it: the stomach believes it before the mind does."], 68),

"fear-triggers": _mk(
    "A balloon popping at a quiet party.", 0.64,
    "the classic key in the lock",
    ["Silence, chatter — then BANG.",
     "Whole body jumps before thought.",
     "Heart slamming at a balloon. The price of sensitivity.",
     "Laughter rippling — the room's all-clear.",
     "Checking: no smoke, no screams. False alarm.",
     "Logged kindly: of course it startled me. It startles everyone."], 78),

"fear-personal-triggers": _mk(
    "Hearing the song that was playing on that bad day.", 0.60,
    "the private logbook",
    ["Three notes in — the room tilts.",
     "It is just a song. The body disagrees.",
     "The whole memory arrives with the melody.",
     "Naming it: this is the association, not the event.",
     "Staying through the chorus, breathing. Nothing bad happens.",
     "One safe repetition logged — the wiring loosens a notch."], 72),

"fear-surprise-triggers": _mk(
    "Catching your own reflection in a dark window.", 0.62,
    "speed, not philosophy",
    ["A face in the glass where no face should be.",
     "Jump first — the machinery does speed, not philosophy.",
     "Understanding arrives second: it is me.",
     "The laugh comes, a little shaky.",
     "Noting the state: tired, already on edge. Of course.",
     "Calibrated, not embarrassed — the hair trigger logged."], 76),

"fear-cascade": _mk(
    "A strange noise at night that will not resolve.", 0.70,
    "breaking the chain",
    ["A creak with no explanation. (link one)",
     "The news story surfaces. (link two)",
     "What if someone is downstairs? (link three)",
     "Heart hammering — proof, it feels like. (link four)",
     "Every sound now a suspect. (link five)",
     "Light on. Checking. One broken link collapses the chain."], 76),

"fear-actions": _mk(
    "Deciding whether to enter the dark basement.", 0.66,
    "the ancient software",
    ["Hand on the door, feet not moving.",
     "Freeze first — the oldest move, buying assessment.",
     "Flight in slow motion suggests: skip it, go back upstairs.",
     "Fight has no target here. Affiliate: call someone down.",
     "Asking the question: is this working, or just avoiding?",
     "Graded step: light on, three steps down, pause. Negotiated."], 74),

"fear-words": _mk(
    "Calling a friend right after the scare.", 0.56,
    "the frightened voice",
    ["Dialing with shaking hands.",
     "What was that? Are you sure? What if — questions tumbling.",
     "Voice half an octave high, sentences short.",
     "Friend: short sentences, low and steady. Facts with edges.",
     "Repeating the reassurance until it lands.",
     "My voice settling as the alarm settles. The script loosens."], 74),

"fear-decisions": _mk(
    "Deciding whether to cancel the trip after the scare.", 0.60,
    "the risk officer's meeting",
    ["The urge votes: cancel everything, now.",
     "Fear overweights the worst case; the upside hides.",
     "Slowing down: sleeping on it, writing the real odds.",
     "The friend-test: what would I advise her?",
     "A reversible first step: postpone, not cancel.",
     "Fear got its vote — it read the risk section. Not the only chair."], 70),

"fear-escalation": _mk(
    "The alarm climbing rung by rung during heavy turbulence.", 0.80,
    "meeting each rung",
    ["Rung one: checking the seatbelt, planning. Strategic.",
     "Rung two: gripping armrests, snapping at the drink cart. Urgent.",
     "Rung three: breath stopped, hands shaking. Primitive.",
     "No debate at the top — just ride, breathe, wait.",
     "The drop eases. Rung two. Rung one.",
     "Every rung came back down. Holding that fact."], 84),

"fear-healthy": _mk(
    "Naming the fear out loud to a trusted friend.", 0.50,
    "letting it move",
    ["The sentence forming: I am afraid of...",
     "Saying it. The fog becomes an object.",
     "Spoken fear shrinks — secrecy was feeding it.",
     "A walk together; the arousal gets lawful motion.",
     "Slow exhales on the way home.",
     "Moved, not stored. The valve worked."], 68),

"fear-unhealthy": _mk(
    "Bottling it all day until the car ride home.", 0.74,
    "the invoices",
    ["Smiling through it all day. Fine, fine, fine.",
     "Jaw aching by evening; shoulders like stone.",
     "Snapping at nothing on the drive — the leak.",
     "Tears in the parked car. The bottle's limit reached.",
     "Noticing the pattern without judgment.",
     "One honest sentence tomorrow. The valve opens a crack."], 78),

"fear-practices": _mk(
    "One month of keeping the fear log.", 0.45,
    "the maintenance schedule",
    ["Day one: trigger, volume, what helped. Three lines.",
     "Week one: the 3 a.m. pattern emerges.",
     "Week two: pre-meeting spike, planned for now.",
     "Week three: graded step taken — the phone call made.",
     "Week four: fewer false alarms, faster recoveries.",
     "The instrument kept, not silenced. Maintenance logged."], 66),

"fear-reading": _mk(
    "Noticing a friend's laugh pitched half a step too high.", 0.52,
    "the four channels",
    ["The laugh does not match the eyes.",
     "Channel one: brows flicker up and knit.",
     "Channel two: shoulders hunched, hand checking the door.",
     "Channel three: voice bright and too fast.",
     "Two, three channels together — a reliable read.",
     "Adjusting: slowing down, softening, making room."], 70),

"fear-support": _mk(
    "Sitting with a frightened child during a thunderstorm.", 0.62,
    "the lighthouse",
    ["The thunder cracks; small hands clutch.",
     "Getting low, getting warm. I am here.",
     "Concrete facts: the house is strong; the storm passes.",
     "That was a big scary noise — believed, not argued.",
     "Breathing together, slow.",
     "Small shoulders dropping. Safety, proven by presence."], 72),

"fear-mistakes": _mk(
    "The gotcha prank that went wrong.", 0.68,
    "friendly fire",
    ["The jump-scare lands — too well.",
     "Laughter from us; tears from them. The receipt kept.",
     "Mockery would add shame to fear. Not doing that.",
     "Apologizing plainly, staying close.",
     "No logic lecture — one fact, then quiet company.",
     "Logged as friendly fire: never spend trust for a laugh."], 76),

"fear-map": _mk(
    "Placing tonight's uneasy feeling on the emotion map.", 0.50,
    "naming the street",
    ["The feeling is foggy. Checking the neighbors.",
     "Present or future? Future — anxiety's street, not fear's.",
     "Scheduled? No — dread needs a date. This is free-floating.",
     "Intensity: mild. Nervousness, then — fear's quiet neighbor.",
     "Destination chosen: calm, via the far side.",
     "Named precisely. The handling follows the name."], 68),

"fear-blends": _mk(
    "The roller coaster cresting its highest hill.", 0.70,
    "the compound signal",
    ["The climb, the click-click-click.",
     "Fear's arousal plus joy's delight — thrill.",
     "Same pounding heart as the alley. Different meaning.",
     "Hands up — the body celebrating the alarm.",
     "The drop: screaming laughter.",
     "Context wrote the meaning. The machinery is neutral."], 82),

"fear-simulation": _mk(
    "Power outage on a stormy night, home alone.", 0.82,
    "the full drill",
    ["Lights die with a pop. Breath catches. (trigger)",
     "Crash downstairs — cascade begins: memory, imagination, hammering heart. (rise)",
     "Another bang — the wave crests, thoughts narrow to check or hide. (peak)",
     "Naming it: I am afraid, and I will check one room at a time. (turning)",
     "Rooms cleared, branch found, friend texted. The laugh comes shaky. (easing)",
     "Candlelight, blanket, trembling hands cooling. Fear completed. (afterglow)"],
    84),
}

assert len(DEMOS) == 34, "need 34 demos"
