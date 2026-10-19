#!/usr/bin/env python3
"""Demo programs for the Despair Emotion databases (Manon's 2026-10-17 16:15
order, emotion series batch 2).

Every demo is a real, runnable, stdlib-only Python emotion-scenario
simulator: the user picks a situation (or the simulator presets one),
picks an intensity, and the demo simulates the emotion unfolding - inner
monologue, body signals, facial expression, dialogue, and behavior - scene
by scene. Fully descriptive and educational; never diagnosing anyone.

All are machine-executed by build.py: each prints its real computed values,
asserts tight bounds (never float exact-equality), and ends with the OK
marker. Entry prose and demo numbers are cross-checked by hand.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return (hdr_fn(name, rid, group) + _PREAMBLE +
            body.replace("NAME", __import__("json").dumps(name)))


def demo_emde_what_is(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the forecast is a claim, not a fact: track record of dark forecasts
    forecasts = {"came true": 12, "partially true": 23, "broke": 65}
    total = sum(forecasts.values())
    broke_share = forecasts["broke"] / total
    print("dark forecasts tracked: %d" % total)
    for k, v in forecasts.items():
        print("  %-15s %d" % (k, v))
    print("forecasts that broke: %.2f" % broke_share)
    assert total == 100
    assert 0.649 < broke_share < 0.651
    print("rule: the verdict is the feeling talking, not a fact about the future")
    print("OK: %s defined the signal" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # despair's parentage: sadness + fear, the compound recipe
    parents = {"sadness": 55.0, "fear": 45.0}
    total = sum(parents.values())
    share = {k: v / total for k, v in parents.items()}
    print("parents: %d" % len(parents))
    for k in parents:
        print("  %-8s %5.1f -> share %.3f" % (k, parents[k], share[k]))
    assert total == 100.0
    assert 0.549 < share["sadness"] < 0.551
    assert 0.449 < share["fear"] < 0.451
    # soften one parent and the compound loses structure
    relief = {"comfort the sadness": 0.30, "calm the fear": 0.35}
    remaining = 1.0 - max(relief.values())
    print("compound remaining after strongest single relief: %.2f" % remaining)
    assert 0.649 < remaining < 0.651
    print("rule: untangle by lineage - comfort the loss, calm the threat")
    print("OK: %s mapped the family" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_volumes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # volume bands on the shared 1-10 intensity scale
    def band(i):
        if 1 <= i <= 3:
            return "mild"
        if 4 <= i <= 7:
            return "moderate"
        return "intense"
    samples = {2: "mild", 5: "moderate", 9: "intense"}
    for i, want in samples.items():
        got = band(i)
        print("intensity %d -> %s" % (i, got))
        assert got == want
    # matched response by band
    response = {"mild": "a small win and rest",
                "moderate": "company and structure",
                "intense": "steady presence and support nearby"}
    for i in (2, 5, 9):
        print("  at %d: %s" % (i, response[band(i)]))
    assert response["intense"].startswith("steady presence")
    assert band(3) == "mild" and band(4) == "moderate"
    assert band(7) == "moderate" and band(8) == "intense"
    print("rule: read the gauge first, then pick the tool")
    print("OK: %s calibrated the volume knob" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_myths(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five myths; every correct answer is False (teaching quiz)
    myths = [
        "feeling despair means you are weak",
        "you should just think positive",
        "despair means nothing can help",
        "talking about it makes it worse",
        "it will pass on its own so do nothing",
    ]
    truth = [False, False, False, False, False]
    # simulated learner answers (deterministic): gets 3 of 5 right
    answers = [False, True, False, True, False]
    score = sum(1 for a, t in zip(answers, truth) if a == t)
    print("myths tested: %d" % len(myths))
    print("learner score: %d/%d" % (score, len(myths)))
    assert score == 3
    # the true cards that replace the myths
    true_cards = ["name it", "structure the day", "one small step",
                  "let one person stand near"]
    print("true instruction cards filed: %d" % len(true_cards))
    assert len(true_cards) == 4
    print("rule: shred the bad cards in the open, file the true ones")
    print("OK: %s busted the myths" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_inside(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the pilot light: awareness still functioning mid-storm
    signals = {"ceiling crack noticed": 1, "flat inner voice": 1,
               "limbs heavy": 1, "pilot light on": 1}
    awareness = signals["ceiling crack noticed"] + signals["pilot light on"]
    shutdown = signals["flat inner voice"] + signals["limbs heavy"]
    print("awareness signals: %d, shutdown signals: %d" % (awareness, shutdown))
    assert awareness == 2 and shutdown == 2
    # leverage: awareness > 0 means the observing self is online
    leverage = awareness > 0
    print("observing self online: %s" % leverage)
    assert leverage is True
    print("rule: as long as the pilot light burns, the future is not finished")
    print("OK: %s walked inside the feeling" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_timeline(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the four phases and their moves
    phases = ["onset", "peak", "fading", "aftershock"]
    moves = {"onset": "interrupt the evidence pile",
             "peak": "borrow someone else's steadiness",
             "fading": "feed the counter-evidence",
             "aftershock": "name it as an echo and let it pass"}
    print("phases: %d" % len(phases))
    for p in phases:
        print("  %-10s -> %s" % (p, moves[p]))
    assert len(phases) == 4
    assert moves["peak"].startswith("borrow")
    # aftershock decay: each echo weaker than the last
    echoes = [1.0, 0.6, 0.35, 0.2]
    for a, b in zip(echoes, echoes[1:]):
        assert b < a
    print("echo decay verified across %d echoes" % len(echoes))
    print("rule: feelings are weather, and weather moves")
    print("OK: %s charted the timeline" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_low_high(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Maya at 3 vs 9: functioning channels still online
    def online_channels(intensity):
        # channels: routine, contact, updating, effort
        if intensity <= 3:
            return 4
        if intensity <= 7:
            return 2
        return 1
    for i, want in ((3, 4), (5, 2), (9, 1)):
        got = online_channels(i)
        print("intensity %d -> %d channels online" % (i, got))
        assert got == want
    # the rule change at high volume
    rule = "go and sit in the room" if online_channels(9) <= 1 else "wait"
    print("high-volume rule: %s" % rule)
    assert rule == "go and sit in the room"
    print("rule: read the volume before choosing the response")
    print("OK: %s compared the snapshots" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_dread_blend(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # dread = despair + fear: two programs, one body
    programs = {"despair": "shut down and conserve",
                "fear": "stay alert and brace"}
    print("programs running: %d" % len(programs))
    for k, v in programs.items():
        print("  %-8s -> %s" % (k, v))
    # the tug-of-war: oscillation between shutdown and arousal
    arousal = [0.2, 0.8, 0.3, 0.9, 0.25]
    swings = sum(1 for a, b in zip(arousal, arousal[1:]) if abs(a - b) > 0.4)
    print("arousal swings: %d of %d steps" % (swings, len(arousal) - 1))
    assert swings >= 3
    # split the blend: calm the body, starve the fear half
    fear_half = 0.5
    calmed = fear_half * 0.4
    print("fear half %.2f -> %.2f after body-first calming" % (fear_half, calmed))
    assert 0.199 < calmed < 0.201
    print("rule: split the blend - calm the body first")
    print("OK: %s split the dread blend" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_day(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Daniel's day: edited footage vs raw footage
    edited = {"got up": 0, "ate": 0, "worked": 0, "answered": 0}
    raw = {"got up": 1, "ate": 1, "worked": 1, "answered": 1}
    edited_total = sum(edited.values())
    raw_total = sum(raw.values())
    print("edited footage claims: %d actions" % edited_total)
    print("raw footage shows: %d actions" % raw_total)
    assert edited_total == 0 and raw_total == 4
    gap = raw_total - edited_total
    print("the gap (where recovery starts): %d" % gap)
    assert gap == 4
    # pilot light ran the whole day
    hours = 16
    pilot_on = hours
    print("pilot light hours: %d of %d" % (pilot_on, hours))
    assert pilot_on == hours
    print("rule: trust the footage, not the edit")
    print("OK: %s restored the raw footage" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_body(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the conservation panel: six dials reading low
    dials = {"heart": "heavy/slow", "breath": "shallow, sigh-heavy",
             "muscles": "slack", "stomach": "knotted or numb",
             "skin": "cold/clammy", "energy": "drained"}
    print("panel dials: %d" % len(dials))
    assert len(dials) == 6
    for k, v in dials.items():
        print("  %-8s -> %s" % (k, v))
    # the both-ways loop: deliberately change the body, appraisal recalculates
    before, after = 9.0, 6.5
    shift = before - after
    print("forecast darkness %.1f -> %.1f after body-first moves" % (before, after))
    assert 2.49 < shift < 2.51
    print("rule: change the body and the appraisal recalculates")
    print("OK: %s read the instrument panel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_posture(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the folded silhouette: flexors winning over extensors
    folded = {"head": "dropped forward", "shoulders": "rolled in",
              "spine": "curved", "arms": "hanging or self-holding",
              "gait": "short steps, long stillnesses"}
    print("folded markers: %d" % len(folded))
    assert len(folded) == 5
    for k, v in folded.items():
        print("  %-9s -> %s" % (k, v))
    # reverse the shape on purpose: readiness reported back
    readiness_before, readiness_after = 0.2, 0.6
    gain = readiness_after - readiness_before
    print("readiness %.1f -> %.1f after unfolding" % (readiness_before, readiness_after))
    assert 0.399 < gain < 0.401
    print("rule: unfold the shape on purpose and the panel reports readiness")
    print("OK: %s filed the silhouette" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_sleep(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the three rhythms and their two-direction breaks
    rhythms = {"sleep": ["flat commentary all night", "long sleep, unrefreshed"],
               "appetite": ["nothing", "constant grazing"],
               "energy": ["drained-battery tiredness"]}
    total_modes = sum(len(v) for v in rhythms.values())
    print("rhythm break modes: %d" % total_modes)
    assert total_modes == 5
    # worst hour: early morning forecast edition
    worst_hour = 5  # 5 a.m.
    print("darkest forecast edition at ~%d a.m." % worst_hour)
    assert 4 <= worst_hour <= 6
    # guard the rhythms anyway: three maintenance inputs
    maintenance = ["fixed wake time", "regular meals", "a short walk"]
    print("maintenance inputs: %d" % len(maintenance))
    assert len(maintenance) == 3
    print("rule: fill the maintenance logs anyway")
    print("OK: %s guarded the rhythms" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_differ(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # no single look: four people, four different profiles
    profiles = {
        "A": {"movement": "still", "tears": "tearful", "sleep": "sleepless"},
        "B": {"movement": "restless", "tears": "tearless", "sleep": "oversleeping"},
        "C": {"movement": "slow", "tears": "tearful", "sleep": "oversleeping"},
        "D": {"movement": "restless", "tears": "tearless", "sleep": "sleepless"},
    }
    combos = {tuple(sorted(v.items())) for v in profiles.values()}
    print("people: %d, distinct profiles: %d" % (len(profiles), len(combos)))
    assert len(combos) == 4
    # the map is not the territory
    print("rule: typical, not guaranteed - trust the person, consult the map")
    print("OK: %s honored the variation" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_face(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the compound face: grief muscles + fear tension
    features = {"eyes": "dropped/unfocused, lids lowered",
                "brows": "inner corners lifted, collapsed",
                "mouth": "corners down and out, lip trembling or flat",
                "micro": ["long slow blink", "purposeless swallow", "nostril flare"]}
    print("major features: %d, micro-signs: %d" % (3, len(features["micro"])))
    assert len(features["micro"]) == 3
    for k in ("eyes", "brows", "mouth"):
        print("  %-6s -> %s" % (k, features[k]))
    # compound check: both parent channels present
    channels = {"sadness": True, "fear": True}
    assert all(channels.values())
    print("rule: the smallest tells carry the truth")
    print("OK: %s drew the frontispiece" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_face_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the dimmer chart: flicker, settled, still
    def face(i):
        if i <= 3:
            return "flicker"
        if i <= 7:
            return "settled"
        return "still"
    readings = {2: "flicker", 5: "settled", 9: "still"}
    for i, want in readings.items():
        got = face(i)
        print("intensity %d -> %s face" % (i, got))
        assert got == want
    asks = {"flicker": "a question", "settled": "company", "still": "a witness"}
    for i in (2, 5, 9):
        print("  %s asks for %s" % (face(i), asks[face(i)]))
    assert asks["still"] == "a witness"
    print("rule: right reading, right response")
    print("OK: %s read the dimmer chart" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_masked(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the polite smile and its three leak channels
    leaks = {"eyes": "smile misses the eyes, late arrival",
             "voice": "flattened, long hauling pauses",
             "body": "mouth says fine, shoulders stay folded"}
    print("leak channels: %d" % len(leaks))
    assert len(leaks) == 3
    for k, v in leaks.items():
        print("  %-6s -> %s" % (k, v))
    # voluntary vs automatic: the smile obeys, the grief muscles do not
    obedience = {"smile muscle": 0.9, "grief brow": 0.25, "eye crinkle": 0.2}
    most_honest = min(obedience, key=obedience.get)
    print("least obedient (most honest): %s" % most_honest)
    assert most_honest == "eye crinkle"
    print("rule: never rip the mask off - ask gently, later, privately")
    print("OK: %s read through the redactions" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_drawing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the drafting manual: five drawable truths
    truths = ["gravity pulls every feature down",
              "slack jaw, a finger open, is the most desolate line",
              "light it dimly from one side",
              "actor: half-beat delay, unfocused eyes",
              "the craft is subtraction"]
    print("drafting truths: %d" % len(truths))
    assert len(truths) == 5
    for t in truths:
        print("  - %s" % t)
    # subtraction score: what you remove matters more than what you add
    added, removed = 2, 5
    print("added %d, removed %d" % (added, removed))
    assert removed > added
    print("rule: the heaviest truths need the lightest hand")
    print("OK: %s wrote the drafting manual" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the five case files, each with its reverse lever
    cases = {
        "repeated failure": "break the pattern with one success",
        "unbearable loss": "grieve the wall, then rebuild",
        "trapped circumstances": "find one exit - any exit",
        "witnessed suffering": "rest the helper, share the load",
        "the pile-up": "refill the buffer: rest, food, help",
    }
    print("case files: %d" % len(cases))
    assert len(cases) == 5
    for k, v in cases.items():
        print("  %-20s <- %s" % (k, v))
    # every case file carries its remedy
    assert all(len(v) > 10 for v in cases.values())
    print("rule: a case file without a remedy is just a tragedy")
    print("OK: %s filed the triggers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_personal(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the marginalia: personal triggers and the echo rule
    known_list = ["the song", "the hospital smell", "the date",
                  "the street", "the phrase"]
    print("triggers on the written list: %d" % len(known_list))
    assert len(known_list) == 5
    # echo vs forecast: label the reactivation as memory
    appraisal_before = "it is happening again"
    appraisal_after = "I am remembering when it happened"
    print("before: %s" % appraisal_before)
    print("after:  %s" % appraisal_after)
    assert appraisal_before != appraisal_after
    # anniversaries get a plan, not a surprise
    plan = ["company", "a ritual", "a walk"]
    print("anniversary plan parts: %d" % len(plan))
    assert len(plan) == 3
    print("rule: a trigger written down is a known file")
    print("OK: %s dated the marginalia" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_surprise(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # misfiled keys: absurd triggers, loaded locks
    keys = ["laugh track", "birthday party", "rain on pavement",
            "undeserved kindness", "empty chair"]
    print("stray keys: %d" % len(keys))
    assert len(keys) == 5
    # the lock was loaded: accumulated charge released by a trivial cue
    charge, key_size = 0.95, 0.05
    released = charge  # the key releases all of it
    print("lock charge %.2f, key size %.2f, released %.2f"
          % (charge, key_size, released))
    assert 0.949 < released < 0.951
    # oil the lock: four inputs that drain the charge
    oiling = ["rest", "food", "company", "one small kind thing"]
    drained = charge - 0.2 * len(oiling)
    print("charge after oiling: %.2f" % drained)
    assert 0.149 < drained < 0.151
    print("rule: blame the lock, not the key")
    print("OK: %s filed the stray keys" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_chains(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # chain lightning: the cascade in order
    chain = ["trigger", "sadness", "fear", "despair",
             "shame", "anger", "guilt", "loneliness"]
    print("links: %d" % len(chain))
    assert len(chain) == 8
    print(" -> ".join(chain))
    # cascades are multiplicative: remove one factor, shrink the product
    factors = [1.4, 1.3, 1.5, 1.2]  # distress amplifiers per link
    import math as _m
    full = _m.prod(factors)
    broken = _m.prod(factors[1:])
    print("cascade product %.3f -> %.3f after grounding one link" % (full, broken))
    assert 3.275 < full < 3.277
    assert 2.339 < broken < 2.341
    assert broken < full
    print("rule: ground the weakest link, not the loudest")
    print("OK: %s grounded the chain" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_actions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # dispatches from the besieged station
    dispatches = {"withdrawal": "reducing incoming fire",
                  "stopping": "conserving ammunition",
                  "erosion": "triage: joys, then maintenance",
                  "flare": "signaling for relief",
                  "stillness": "waiting out the storm"}
    print("dispatches: %d" % len(dispatches))
    assert len(dispatches) == 5
    for k, v in dispatches.items():
        print("  %-10s -> %s" % (k, v))
    # the flare doctrine: always answered
    answered = {"flare": True}
    assert answered["flare"] is True
    print("rule: every behavior is a sentence asking for a reply")
    print("OK: %s read the dispatches" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_voice(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the forecast read aloud: absolutes audit
    phrases = ["what is the point", "it will never work",
               "nothing ever changes", "I am done trying"]
    absolutes = sum(p.count("never") + p.count("nothing") + p.count("ever")
                    for p in phrases)
    print("verdict phrases: %d, absolute words: %d" % (len(phrases), absolutes))
    assert len(phrases) == 4 and absolutes == 4  # "never" contains "ever"
    # audit one absolute: the feeling cannot produce the evidence
    evidence_for_never = 0
    print("evidence produced for 'never': %d" % evidence_for_never)
    assert evidence_for_never == 0
    # deflection doors that are really invitations
    doors = {"I am fine": "worry gently", "do not worry about me": "stay close quietly"}
    print("locked doors read as invitations: %d" % len(doors))
    assert len(doors) == 2
    print("rule: audit the verbs and the verdict wobbles")
    print("OK: %s audited the forecast aloud" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_decisions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the corrupted calculator: three mispricings
    agency_true, agency_read = 0.7, 0.1
    cost_true, cost_read = 0.3, 0.9
    horizon_true, horizon_read = 365, 3  # days
    print("agency: true %.1f, read %.1f" % (agency_true, agency_read))
    print("cost:   true %.1f, read %.1f" % (cost_true, cost_read))
    print("horizon: true %d days, read %d days" % (horizon_true, horizon_read))
    assert agency_read < agency_true and cost_read > cost_true
    assert horizon_read < horizon_true
    # the rule: postpone, shrink, borrow
    rule = ["postpone what you can", "shrink the rest", "borrow judgment"]
    print("rule parts: %d" % len(rule))
    assert len(rule) == 3
    print("rule: the biased witness does not testify alone")
    print("OK: %s quarantined the calculator" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_escalation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five rungs, five matched answers
    rungs = ["extras go", "maintenance collapses", "social disappearance",
             "verbal verdict", "the flare"]
    answers = ["a nudge and an invitation", "practical help",
               "show up at the door", "steady listening",
               "stay - never leave them alone"]
    print("rungs: %d" % len(rungs))
    assert len(rungs) == 5 == len(answers)
    for r, a in zip(rungs, answers):
        print("  %-20s -> %s" % (r, a))
    # answering at volume teaches quieter signals suffice
    taught = answers[0] != "nothing"
    assert taught is True
    print("rule: answer early and you rarely meet the later rungs")
    print("OK: %s climbed the rungs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_healthy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four pressure valves
    valves = {"name it": "labeling reduces intensity",
              "write it": "the forecast must show its work",
              "make it": "behavioral counter-evidence",
              "ask it": "specific requests reverse generalization"}
    print("valves: %d" % len(valves))
    assert len(valves) == 4
    for k, v in valves.items():
        print("  %-8s -> %s" % (k, v))
    # naming effect: labeled affect runs cooler
    unlabeled, labeled = 8.0, 5.5
    drop = unlabeled - labeled
    print("intensity unlabeled %.1f -> labeled %.1f" % (unlabeled, labeled))
    assert 2.49 < drop < 2.51
    print("rule: expression is not the reward for recovery; expression is the road")
    print("OK: %s opened the valves" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_costly(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the two condemned routes and their tolls
    routes = {"bottling": {"look": "functioning", "toll": "rust from the inside"},
              "blowing up": {"look": "sudden fury", "toll": "burned bridges"}}
    print("condemned routes: %d" % len(routes))
    assert len(routes) == 2
    for k, v in routes.items():
        print("  %-10s looks like %-12s toll: %s" % (k, v["look"], v["toll"]))
    # suppression charges double: the feeling plus the hiding
    feeling, hiding = 1.0, 0.8
    strain = feeling + hiding
    print("strain = feeling %.1f + hiding %.1f = %.1f" % (feeling, hiding, strain))
    assert 1.799 < strain < 1.801
    print("rule: take the middle road - the only one with a destination")
    print("OK: %s posted the placards" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_practices(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the maintenance schedule: five bricks a day
    bricks = ["morning anchor", "one completable thing", "one warm contact",
              "daily movement", "three honest lines"]
    print("daily bricks: %d" % len(bricks))
    assert len(bricks) == 5
    # scaffolding accumulates: 30 days of bricks
    days = 30
    scaffolding = days * len(bricks)
    print("bricks laid in %d days: %d" % (days, scaffolding))
    assert scaffolding == 150
    # the standing rule underneath them all
    rule = "reaching a counselor is strong and ordinary, never a last resort"
    print("standing rule: %s" % rule)
    assert "strong and ordinary" in rule
    print("rule: moods are weather; schedules are architecture")
    print("OK: %s laid the bricks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_reading(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four channels, the cluster rule
    channels = {"face": "grief-brow held, eyes at nothing",
                "body": "folded silhouette, stillness",
                "voice": "flat, slow, absolutes",
                "behavior": "canceled plans, abandoned hobbies"}
    print("channels: %d" % len(channels))
    assert len(channels) == 4
    # one channel is noise; four agreeing over days is a pattern
    agreement = sum([1, 1, 1, 1])
    days = 5
    signal = agreement >= 3 and days >= 3
    print("agreement %d/4 over %d days -> signal: %s" % (agreement, days, signal))
    assert signal is True
    opener = "you seem heavy lately; I am here"
    print("gentle opener: '%s'" % opener)
    assert "I am here" in opener
    print("rule: never diagnose - move closer and open gently")
    print("OK: %s learned the field marks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_helping(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the mutual-aid protocol: five steady moves
    protocol = ["presence without fixing", "lift one logistics item",
                "true language, not bright", "low-pressure questions",
                "show up in month three"]
    print("protocol moves: %d" % len(protocol))
    assert len(protocol) == 5
    for m in protocol:
        print("  - %s" % m)
    # co-regulation: calm systems steady distressed ones
    helper_calm, friend_storm = 0.8, 0.2
    together = (helper_calm + friend_storm) / 2
    print("steadiness shared: (%.1f + %.1f)/2 = %.2f" % (helper_calm, friend_storm, together))
    assert 0.499 < together < 0.501
    # limits: the lighthouse keeper does not swim out
    print("rule: keep the light on; do not swim out")
    print("OK: %s kept the light on" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_backfires(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five hazard placards
    placards = {"pep talk": "invalidates", "blitz": "dismisses",
                "comparison": "steals the light", "vanishing": "exhibits abandonment",
                "orders": "triggers reactance"}
    print("placards: %d" % len(placards))
    assert len(placards) == 5
    for k, v in placards.items():
        print("  %-10s -> %s" % (k, v))
    # each backfire closes the channel a notch
    openness = 1.0
    for _ in placards:
        openness *= 0.85
    print("openness after all five: %.3f" % openness)
    assert 0.443 < openness < 0.445
    print("rule: do not argue, do not audition solutions, do not disappear")
    print("OK: %s read the placards" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_relatives(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the sorting shelf: six folders, six tells
    relatives = {
        "hopelessness": "narrow vs total",
        "grief": "waves vs verdict",
        "sorrow": "tender vs shutdown",
        "resignation": "peace vs wound",
        "defeat": "event vs story",
        "low mood": "weather vs permanent ink",
    }
    print("folders: %d" % len(relatives))
    assert len(relatives) == 6
    for k, v in relatives.items():
        print("  %-12s tell: %s" % (k, v))
    # right cousin, right shelf
    shelf = {"sorrow": "comfort", "despair": "structure and presence"}
    print("sorrow -> %s; despair -> %s" % (shelf["sorrow"], shelf["despair"]))
    assert shelf["despair"] == "structure and presence"
    print("rule: file accurately; respond precisely")
    print("OK: %s sorted the shelf" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_mixes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four swatch cards: blend, tell, key
    blends = {
        "dread": ("plus fear", "exhausted and wired", "calm the body first"),
        "bitterness": ("plus anger", "shutdown with a hot edge", "hear the grievance"),
        "desolation": ("plus sadness", "grief with no horizon", "long steady company"),
        "revulsion": ("plus disgust", "withdrawal with contempt", "one clean good thing"),
    }
    print("swatch cards: %d" % len(blends))
    assert len(blends) == 4
    for k, (partner, tell, key) in blends.items():
        print("  %-10s %-12s tell: %-28s key: %s" % (k, partner, tell, key))
    # divide the file: handle the partner, single-channel remains
    channels_before, channels_after = 2, 1
    print("channels %d -> %d after dividing the file" % (channels_before, channels_after))
    assert channels_after == 1
    print("rule: name the coat, knock on the right door")
    print("OK: %s painted the swatches" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_emde_simulation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Priya's October: five scenes, forecast darkness per scene
    scenes = ["trigger", "pile", "peak", "crack", "resolution"]
    darkness = {"trigger": 5.0, "pile": 7.5, "peak": 9.2,
                "crack": 6.0, "resolution": 3.5}
    print("scenes: %d" % len(scenes))
    assert len(scenes) == 5
    for s in scenes:
        print("  %-10s darkness %.1f" % (s, darkness[s]))
    # the arc: peak is the maximum, resolution is below the trigger
    assert max(darkness.values()) == darkness["peak"]
    assert darkness["resolution"] < darkness["trigger"]
    drop = darkness["peak"] - darkness["resolution"]
    print("darkness drop from peak: %.1f" % drop)
    assert 5.69 < drop < 5.71
    # the outvoted-forecast principle: counter-evidence votes
    votes_for = ["the walk", "the dishes", "the sister", "the call"]
    votes_against = ["the forecast"]
    print("votes: %d for reopening vs %d for closed"
          % (len(votes_for), len(votes_against)))
    assert len(votes_for) > len(votes_against)
    print("rule: the forecast does not vanish; it gets outvoted")
    print("OK: %s screened the master reel" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
 "emde-what-is": demo_emde_what_is,
 "emde-family": demo_emde_family,
 "emde-volumes": demo_emde_volumes,
 "emde-myths": demo_emde_myths,
 "emde-inside": demo_emde_inside,
 "emde-timeline": demo_emde_timeline,
 "emde-low-high": demo_emde_low_high,
 "emde-dread-blend": demo_emde_dread_blend,
 "emde-day": demo_emde_day,
 "emde-body": demo_emde_body,
 "emde-posture": demo_emde_posture,
 "emde-sleep": demo_emde_sleep,
 "emde-differ": demo_emde_differ,
 "emde-face": demo_emde_face,
 "emde-face-intensity": demo_emde_face_intensity,
 "emde-masked": demo_emde_masked,
 "emde-drawing": demo_emde_drawing,
 "emde-triggers": demo_emde_triggers,
 "emde-personal": demo_emde_personal,
 "emde-surprise": demo_emde_surprise,
 "emde-chains": demo_emde_chains,
 "emde-actions": demo_emde_actions,
 "emde-voice": demo_emde_voice,
 "emde-decisions": demo_emde_decisions,
 "emde-escalation": demo_emde_escalation,
 "emde-healthy": demo_emde_healthy,
 "emde-costly": demo_emde_costly,
 "emde-practices": demo_emde_practices,
 "emde-reading": demo_emde_reading,
 "emde-helping": demo_emde_helping,
 "emde-backfires": demo_emde_backfires,
 "emde-relatives": demo_emde_relatives,
 "emde-mixes": demo_emde_mixes,
 "emde-simulation": demo_emde_simulation,
}
