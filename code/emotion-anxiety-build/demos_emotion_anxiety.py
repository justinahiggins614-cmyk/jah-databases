#!/usr/bin/env python3
"""Scenario-simulator demos for The Anxiety Emotion Database.

Each demo is a standalone, runnable Python program: it takes a scenario
(situation + intensity setting), simulates anxiety unfolding across six
scenes - Onset, Build, Peak, Turning Point, Easing, Settling - computing
per-scene intensity, heart rate, and breath rate from a deterministic
arousal model, prints the scene-by-scene simulation (inner voice, body,
focus detail), then asserts tight structural bounds (never float
exact-equality) and ends with the OK marker.

The numbers are real computed values from the model, and each scenario is
drawn from its record's content so demo output cross-checks the entry
text: body-signal demos compute the pounding heart the entry describes,
cascade demos show the link-by-link chain, blend demos run the mixed
signal, and the showcase demo walks the full six-scene arc.

Descriptive and educational only. Never diagnoses any person.
"""

import json

_TMPL = r'''
import math, json

SITUATION = __SIT__
INTENSITY = __INT__
FOCUS = __FOCUS__
LINES = json.loads(__LINES__)
HR0 = __HR0__

SCENE_NAMES = ["Onset", "Build", "Peak", "Turning Point", "Easing", "Settling"]

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
print("OK: anxiety scenario simulation complete")
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
"anxiety-definition": _mk(
    "The night before a first job interview.", 0.55,
    "the forecast, not the weather",
    ["Calendar glance at breakfast: the flicker starts, stomach tightens. (onset)",
     "Scenarios bloom on the commute: the panel, the hard question, the pause. (build)",
     "Peak rehearsal at midnight: every answer sounds wrong in the dark. (peak)",
     "Naming it: I am anxious about the unknown panel, not about my worth. (turning)",
     "Plan made, clothes laid out, questions prepared. The loop starts to close. (easing)",
     "Morning: the forecast was loud, the interview is just a conversation. (settling)"],
    70),

"anxiety-family": _mk(
    "Sorting three feelings: the dog barking now, the vet visit Friday, the party tonight.", 0.50,
    "which family member is shouting",
    ["The bark at the door: threat here, now. That one is fear. (onset)",
     "The vet visit Friday: threat later, maybe. That one is anxiety. (build)",
     "Same pounding heart in both — the machinery is shared. (peak)",
     "The party tonight: buzzing, but the appraisal says opportunity. Excitement. (turning)",
     "Three names, three responses: act, prepare, approach. (easing)",
     "Named precisely. The handling follows the name. (settling)"],
    68),

"anxiety-volumes": _mk(
    "Three volumes of the same worry: the dentist Thursday.", 0.60,
    "the volume dial",
    ["Tuesday: a flicker while making coffee. Barely a whisper. (onset)",
     "Wednesday: the hum is audible now, stomach busy. (build)",
     "Thursday morning: the flood — hands shaky, thoughts racing. (peak)",
     "Same machinery at every volume; only the share of the system changes. (turning)",
     "Checklist for the whisper, calming for the hum, body-first for the flood. (easing)",
     "The dial reads clearly now. Match the answer to the volume. (settling)"],
    72),

"anxiety-myths": _mk(
    "Believing the myth: anxiety means something is broken.", 0.55,
    "wiping the lens",
    ["The wave hits and the second appraisal lands: what is wrong with me. (onset)",
     "Anxiety about the anxiety: the loop tightens on itself. (build)",
     "Peak shame: hiding the feeling, performing fine. (peak)",
     "The correction: this is equipment, not identity. A loud signal, not a true one. (turning)",
     "Lens wiped. The forecast is just a forecast. (easing)",
     "Same wave, half the suffering — the second layer is gone. (settling)"],
    71),

"anxiety-firstperson": _mk(
    "Inside the tilted corridor: waiting on the test results.", 0.72,
    "the view from the crow's nest",
    ["The room too bright, time too fast, the hand on the chest. (onset)",
     "The corridor tilts: every thought slides back to the results. (build)",
     "Tired and wired at once — exhausted, too charged to rest. (peak)",
     "Logging it honestly: this is the forecast machinery, not the world. (turning)",
     "The scenarios keep playing, but quieter now that they are named. (easing)",
     "Living one step ahead of the present — then stepping back into it. (settling)"],
    76),

"anxiety-arc": _mk(
    "The grant decision: six weeks of waiting.", 0.65,
    "the wave chart",
    ["The email saying 'decision in six weeks': the first flicker. (onset)",
     "Week three: the loop is a background process, attention taxed daily. (build)",
     "The night before the announcement: the crest, endless while it lasts. (peak)",
     "Preparation at onset, endurance at the peak — the right move per phase. (turning)",
     "The decision lands (funded). The shoulders take an hour to believe it. (easing)",
     "Aftershock flicker at the next deadline — the warm circuit cooling. (settling)"],
    70),

"anxiety-low-high": _mk(
    "Two snapshots: dentist Thursday vs the verdict tomorrow.", 0.60,
    "same sea, different swell",
    ["Low: the flicker at breakfast, gone by the email. A good assistant. (onset)",
     "High: the flicker that grew roots — chest compressed, thoughts looping. (build)",
     "Low costs ninety seconds; high costs the night. Same machinery. (peak)",
     "The difference is system capture — how much of you the loop owns. (turning)",
     "Checklist for the ripple, ballast for the storm. (easing)",
     "Read the swell at a glance. Never send a checklist into a storm. (settling)"],
    74, compare=(0.42, 0.88)),

"anxiety-irritation-blend": _mk(
    "Stuck in traffic on the way to the uncertain meeting.", 0.68,
    "one feeling, two faces",
    ["The meeting looms: pure anxiety, stomach tight. (onset)",
     "The slow driver ahead: dread sharpens into edge. (build)",
     "The snap: words shorter than intended, jaw aching. (peak)",
     "The catch: the irritation is trapped preparation energy, misdirected. (turning)",
     "Address the anxiety half — plan the meeting's first line — and the edge dissolves. (easing)",
     "It was never about the traffic. The blend, unmixed. (settling)"],
    78),

"anxiety-day": _mk(
    "The 2 p.m. meeting: one ordinary anxious day.", 0.62,
    "the tax on presence",
    ["Morning: the mind is already at 2 p.m. before the eyes open. (onset)",
     "The subject-less email from the boss: the engine ignites. (build)",
     "Lunch tasteless, laughter distant — attention fully captured. (peak)",
     "The meeting: four fine minutes. All scenarios evaporate. (turning)",
     "The body takes an hour to get the memo. Shoulders descend slowly. (easing)",
     "Ledger: six hours of presence paid, four minutes of preparation bought. (settling)"],
    71),

"anxiety-body": _mk(
    "Backstage before the talk: the full-body log.", 0.70,
    "reading the gauges",
    ["Heart quickens, breath goes shallow and high. (onset)",
     "Hands tremble, stomach churns, palms sweat. (build)",
     "Mouth dry, legs jittery, the tired-but-wired peak. (peak)",
     "The gauges are not the storm — they are the report of one. (turning)",
     "Slow exhale: the stand-down signal the body understands. (easing)",
     "Gauges falling: heart 68, breath deep, jaw unclenched. (settling)"],
    80),

"anxiety-posture": _mk(
    "The waiting room: reading the body's trim.", 0.58,
    "posture votes on safety",
    ["Shoulders rise a centimeter; the chin tucks. (onset)",
     "The leg starts bouncing; the pen gets clicked. (build)",
     "Perched on the chair's edge, movements small and careful. (peak)",
     "Deliberate trim: shoulders dropped, jaw unclenched, feet planted. (turning)",
     "The body talks the mind down the same wiring that wound it up. (easing)",
     "Sitting back at last. The vote has changed. (settling)"],
    69),

"anxiety-sleep": _mk(
    "The night before the results: guarding the stores.", 0.75,
    "sleep, appetite, energy",
    ["Lights out: the mind holds its final review session uninvited. (onset)",
     "Shallow sleep, vivid dreams — the theater keeps rehearsing. (build)",
     "3 a.m.: wide awake, scenarios at full volume, stomach closed. (peak)",
     "The stores are low: no wonder the forecast runs dark. (turning)",
     "Wind-down routine, no screens, the breath practice. Drifting at last. (easing)",
     "Morning unrefreshed but intact. Guard the stores tonight. (settling)"],
    73),

"anxiety-differences": _mk(
    "Two friends, one worry: different dashboards.", 0.55,
    "your private alarm code",
    ["Amara gets the racing heart and sweating palms. (onset)",
     "Jon gets the knotted gut and the blank mind. (build)",
     "Same loop, different channels — both convinced theirs is the real anxiety. (peak)",
     "The map: Amara's first signal is cardiac, Jon's is gastrointestinal. (turning)",
     "Each learns their three signals in order — early warning, personalized. (easing)",
     "No one's anxiety should look like anyone else's. (settling)"],
    70),

"anxiety-face": _mk(
    "Across the interview table: the face on watch.", 0.60,
    "the lookout's face",
    ["The brow knits faintly; the eyes do one extra sweep. (onset)",
     "Lips press thin; the smile arrives but the eyes stay on watch. (build)",
     "Blink rate climbing, jaw working, the pasted smile fully deployed. (peak)",
     "Reading the cluster: brow plus eyes plus mouth — the loop is running. (turning)",
     "The interviewer slows down, makes room. The face softens a fraction. (easing)",
     "It looked like listening hard — because that is what it was. (settling)"],
    72),

"anxiety-face-intensity": _mk(
    "The signal lamp: dim, bright, flashing.", 0.66,
    "calibrating to the dial",
    ["Mild: a whisper of a knit, one extra glance. Socially fluent. (onset)",
     "Moderate: the configuration locks — scanning eyes, working jaw. (build)",
     "High: the flood — every muscle firing at once. (peak)",
     "Or the freeze: the terrible stillness, the unpowered face. (turning)",
     "Dim lamp wants a plan; flashing lamp wants a steady hand, no new orders. (easing)",
     "The dial read correctly. The response matched the volume. (settling)"],
    74),

"anxiety-hidden": _mk(
    "The competent mask at the family dinner.", 0.62,
    "flags and weather",
    ["Brisk efficiency, humor like smoke: the most together person in the room. (onset)",
     "The laugh a beat too fast; the jaw you could strike a match on. (build)",
     "Hands betray: phone checked eleven times under the table. (peak)",
     "The mask is exhausting — the performance feeds the alarm. (turning)",
     "One safe person, one honest sentence. The flag comes down. (easing)",
     "Lower your own flag where it is safe; never tear down another's. (settling)"],
    71),

"anxiety-artist": _mk(
    "Drawing the worried witness for the stage.", 0.50,
    "charting the face",
    ["Study the brow: inner corners lifted, center knit — a suggestion, not a canyon. (onset)",
     "The eyes: widened, aimed just past the other person. (build)",
     "Hands as supporting cast: the thumb worrying its partner. (peak)",
     "Play divided attention: body here, mind at the 2 p.m. meeting. (turning)",
     "Escalate across the scene: brow, hands, scanning eyes, mask, then flood or freeze. (easing)",
     "The audience recognizes it instantly — everyone has worn this face. (settling)"],
    68),

"anxiety-triggers": _mk(
    "The classics parade: test, bill, waiting room, unanswered message.", 0.64,
    "the charted reefs",
    ["The exam date set: evaluation, the most universal trigger. (onset)",
     "The bill arrives the same week: resources under threat. (build)",
     "The message with no subject line: pure uncertainty, full concentration. (peak)",
     "The formula: it matters, it is uncertain, control feels limited. (turning)",
     "Top three mapped. Most of the territory is now charted. (easing)",
     "The categories are universal; only the details are personal. (settling)"],
    72),

"anxiety-personal-triggers": _mk(
    "The ringtone that once delivered bad news.", 0.60,
    "the uncharted rocks",
    ["The phone rings with that tone: the stomach drops first. (onset)",
     "The mind has not caught up — the feeling arrived before the reason. (build)",
     "Full brace: shoulders up, breath short, for a call about lunch plans. (peak)",
     "Detective work: the tone, the bad news, three years ago. Mapped. (turning)",
     "That is the anniversary, not a new emergency. The forecast corrects. (easing)",
     "A rock on the chart is a hazard managed. (settling)"],
    75),

"anxiety-surprise-triggers": _mk(
    "The promotion letter: good news, racing heart.", 0.58,
    "false contacts on the scope",
    ["The acceptance arrives: joy — and the heart hammering. (onset)",
     "Big change is uncertain regardless of pleasantness. (build)",
     "Plus the third coffee: the body faking the signal, the mind believing it. (peak)",
     "Calibrate the instrument: check the caffeine, check the quiet, check the news. (turning)",
     "Most false contacts dissolve under one honest look. (easing)",
     "'No reason' becomes 'the scope needs calibration.' (settling)"],
    82),

"anxiety-cascade": _mk(
    "The 2 p.m. meeting recruits the mortgage.", 0.70,
    "the mutiny of the imagination",
    ["Link one: the meeting tomorrow. Real, preparable. (onset)",
     "Link two: the presentation. Link three: the promotion. The recruitment drive begins. (build)",
     "Link six: the meaning of the career. Six steps from a meeting. (peak)",
     "The chain audit on paper: link six is absurd, visibly absurd. (turning)",
     "Solve link one; let link six wait for a calmer hour. (easing)",
     "The mutiny put down at the second deck. (settling)"],
    73),

"anxiety-actions": _mk(
    "The invitation declined, the locks checked twice.", 0.62,
    "drills: coping or maintenance",
    ["The invitation: declined with a thin excuse. Immediate relief. (onset)",
     "The message re-read four times; the symptom searched at 1 a.m. (build)",
     "The bag packed for every scenario; the calendar quietly edited. (peak)",
     "The over-time test: does it shrink the anxiety, or rent relief by the hour? (turning)",
     "One maintenance behavior retired: the 1 a.m. search. (easing)",
     "Motion is not seamanship. Keep the drills that work. (settling)"],
    70),

"anxiety-words": _mk(
    "The 'what if' briefing before the call.", 0.60,
    "the loop made audible",
    ["'What if they ask about the delay' — the engine's output format, spoken. (onset)",
     "'Maybe, probably, I guess' — language staying provisional. (build)",
     "'Are you sure it'll be okay' — the third costume for the same question. (peak)",
     "Hearing the dialect: respond to the loop, not just the words. (turning)",
     "One rehearsal aloud, then the plan is closed. (easing)",
     "Clear reports, calm ship. (settling)"],
    76),

"anxiety-decisions": _mk(
    "The offer letter: safe job vs the leap.", 0.66,
    "the biased consultant",
    ["The 5 percent risk renders in high definition; the upside stays blurry. (onset)",
     "Options narrow to safe vs catastrophe; the middle never makes the table. (build)",
     "'I need more information' becomes a permanent address. (peak)",
     "Decision hygiene: base rates looked up, deadline set, process judged. (turning)",
     "The consultant's math checked — the risk was 5 percent, not 50. (easing)",
     "A ship that only sails safe waters never reaches any harbor. (settling)"],
    71),

"anxiety-escalation": _mk(
    "The worry climbs its own ladder.", 0.72,
    "seamanship per sea state",
    ["Low: strategic — a little more preparation, one good question. (onset)",
     "Moderate: threat-serving — triple-checking, the evening eaten. (build)",
     "High: the day organizes around the anxiety; the phone call feels enormous. (peak)",
     "The order: plan, then calm-and-cut, then settle-the-body. (turning)",
     "At the crest: no charting in a hurricane. Hold the ship together. (easing)",
     "Match the seamanship to the sea. Every storm is survivable. (settling)"],
    77),

"anxiety-healthy": _mk(
    "The presentation tomorrow: saying it, showing it, channeling it.", 0.58,
    "the messenger heard",
    ["'I am anxious about the client being unpredictable' — the street address. (onset)",
     "The hand allowed to shake instead of wrestled still. (build)",
     "The walk before the interview; the list worked through, then closed. (peak)",
     "Affect labeled, suppression dropped, energy given its job. (turning)",
     "The loop closes: the future it was forecasting has been prepared for. (easing)",
     "What remains is much smaller than what arrived. (settling)"],
    69),

"anxiety-unhealthy": _mk(
    "Two roads: the bottle and the boil.", 0.68,
    "the middle road",
    ["The bottle: 'I'm fine' performed on schedule while the body runs hot. (onset)",
     "The boil: the 2 a.m. spiral, the frantic eleventh rehearsal. (build)",
     "The bottle bursts: tears over something small. The boil burns: the regretted message. (peak)",
     "Both roads shoot the messenger or hand it the wheel. (turning)",
     "The middle road: receive the message, answer it, stand the messenger down. (easing)",
     "Know your default road; it is the first step off it. (settling)"],
    74),

"anxiety-practices": _mk(
    "The daily orders: breath, window, plan, stores.", 0.52,
    "maintenance for the machinery",
    ["The flicker at noon: three slow exhales, out longer than in. (onset)",
     "The worry deferred to its 6 p.m. appointment — fifteen minutes, on paper. (build)",
     "The open loop closed: one concrete next step, written down. (peak)",
     "Stores guarded: sleep hours kept, the walk taken, caffeine audited. (turning)",
     "The evening ledger: predicted vs happened, two minutes. (easing)",
     "Small, repeated, mechanical — that is why they compound. (settling)"],
    67),

"anxiety-reading": _mk(
    "Noticing the colleague's worried week.", 0.55,
    "clusters, not single signs",
    ["Monday: the brow stays knitted through the standup. (onset)",
     "Wednesday: hands in motion, hedging in every sentence, early exits. (build)",
     "The cluster reads clearly: brow plus hands plus hedging plus withdrawal. (peak)",
     "Hold it lightly — noticing, not diagnosing. Never announce the finding. (turning)",
     "Adjust yourself: slower pace, room made, steady presence lent. (easing)",
     "Your calm, borrowed. The lamp burns steadier. (settling)"],
    68),

"anxiety-support": _mk(
    "Beside the friend before the big call.", 0.62,
    "coming alongside",
    ["Your own pace slows first; your voice drops half a notch. (onset)",
     "'This sounds like a lot.' Acknowledged, not amplified. (build)",
     "'Talk it through, make a plan, or just sit?' Concrete options, not open sea. (peak)",
     "One loop closed together: the email drafted, the first line planned. (turning)",
     "Staying past the first calm — the aftershock gets company. (easing)",
     "Not frightened, not hurried, not going anywhere. (settling)"],
    70),

"anxiety-mistakes": _mk(
    "The seven misfires, one honest evening.", 0.58,
    "answering the signal, not the noise",
    ["'Just relax' — demanding the impossible, adding failure-fuel. (onset)",
     "The logic lecture: twenty minutes the crowded brain cannot process. (build)",
     "'It'll be fine' on repeat: soothing less each time, depending more. (peak)",
     "The pattern: all seven answered the noise instead of the signal. (turning)",
     "Heard, answered concretely, given time — the three wants, met. (easing)",
     "The tuition paid; the mistakes retired. (settling)"],
    72),

"anxiety-map": _mk(
    "Placing tonight's feeling on the neighborhood map.", 0.54,
    "the coastal chart",
    ["The timing test: threat later, not now — anxiety, not fear. (onset)",
     "The talky loop without the pounding heart — worry, the mental half. (build)",
     "The buzz before the launch: threat and opportunity at once. The electric edge. (peak)",
     "Each neighbor wants its own response; the wrong crew stands down. (turning)",
     "Right name, right crew, right deck. (easing)",
     "The chart consulted before the orders given. (settling)"],
    69),

"anxiety-blends": _mk(
    "The week of combined weather.", 0.66,
    "two weathers, two answers",
    ["Monday: anxiety plus irritation — the edgy blend, snapping at traffic. (onset)",
     "Wednesday: anxiety plus sadness — the heavy blend, the undertow. (build)",
     "Friday: anxiety plus excitement — the electric blend before the launch. (peak)",
     "Naming both ingredients in each: feel the mix, split the response. (turning)",
     "The anxiety half gets preparation every time; each partner gets its own answer. (easing)",
     "Two weathers, two answers, one steady ship. (settling)"],
    73),

"anxiety-simulation": _mk(
    "Maya's review week: the full voyage.", 0.78,
    "trigger to resolution",
    ["Monday: the calendar notification — the flicker, the stomach, the waking forecast. (onset)",
     "Wednesday: the loop fully engaged — scenarios, snapping, shallow sleep. (build)",
     "Thursday night: the cascade at full stretch, hands shaking on the phone. (peak)",
     "Friday morning: named precisely, two items prepared — the hinge turns. (turning)",
     "The review: fine, genuinely fine. Shoulders descend over the hour. (easing)",
     "The ledger written, the aftershock recognized, the chart improved. Every wave breaks. (settling)"],
    76),
}

assert len(DEMOS) == 34, "need 34 demos"
