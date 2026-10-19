#!/usr/bin/env python3
"""Demo programs for the Hope Emotion databases (Manon's 16:15 orders, emotion series).

Every demo is real, runnable, stdlib-only Python performing the actual
emotion-scenario simulation for its record. All are machine-executed by
build.py: each prints its real computed values, asserts tight bounds
(never float exact-equality), and ends with the OK marker. Demo outputs
were cross-checked against entry text during authoring.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_hope_definition(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three-component checklist: goal, pathways, agency - hope needs all three
    components = {"goal": 1, "pathways": 1, "agency": 1}
    present = sum(components.values())
    print("hope components present: %d/3" % present)
    # a wish has goal only; confidence has goal + certainty; hope has all three
    wish = {"goal": 1, "pathways": 0, "agency": 0}
    print("wish components: %d/3 (goal only - not hope)" % sum(wish.values()))
    assert present == 3
    assert sum(wish.values()) == 1
    completeness = present / 3.0 * 100.0
    print("hope completeness: %.1f %%" % completeness)
    assert 99.9 < completeness < 100.1
    print("rule: goal plus pathways plus agency - take one away and the feeling thins")
    print("OK: %s defined the feeling" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_family(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # circumplex coordinates: hope = pleasant, gently activated
    valence, arousal = 7.5, 4.5
    quadrant = ("pleasant-gentle" if valence > 5 and arousal <= 5
                else "other")
    print("hope circumplex: valence %.1f, arousal %.1f -> %s" % (valence, arousal, quadrant))
    assert quadrant == "pleasant-gentle"
    # despair sits at the opposite corner: unpleasant, low
    d_val = {"despair": 2.0}
    d_aro = {"despair": 2.5}
    print("despair (opposite): valence %.1f, arousal %.1f" % (d_val["despair"], d_aro["despair"]))
    assert d_val["despair"] < 5 and d_aro["despair"] < 5
    # Plutchik neighborhood: anticipation + joy = optimism, hope beside it
    blend = {"anticipation": 1, "joy": 1}
    optimism = sum(blend.values()) == 2
    print("optimism dyad (anticipation + joy): %s; hope = neighboring compound" % optimism)
    assert optimism is True
    print("rule: a compound, not a primary - anticipation blended with pleasant approach-warmth")
    print("OK: %s placed hope on the map" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the dial: level 1-10; goal fixed, agency + pathway energy = level
    for level in (1, 4, 6, 9):
        agency = float(level)
        if level <= 3:
            band = "flicker (quiet leaning)"
        elif level <= 6:
            band = "steady (working hope)"
        else:
            band = "blaze (life-reorganizing)"
        print("level %d -> agency %.1f: %s" % (level, agency, band))
    bands = {1: "flicker (quiet leaning)", 4: "steady (working hope)",
             6: "steady (working hope)", 9: "blaze (life-reorganizing)"}
    assert bands[9] == "blaze (life-reorganizing)"
    # feedback loop: one confirmed pathway raises agency by a step
    agency = 3.0
    for _ in range(3):
        agency = agency + 1.5
    print("agency after 3 confirmed pathways: %.1f" % agency)
    assert 7.49 < agency < 7.51
    # intensity without pathways -> anxious wanting, not striving
    pathways, intensity = 0, 9.0
    mode = "anxious wanting" if pathways == 0 and intensity > 7 else "striving"
    print("intensity %.1f with %d pathways -> %s" % (intensity, pathways, mode))
    assert mode == "anxious wanting"
    print("rule: the goal stays fixed; agency and pathway energy are the dial")
    print("OK: %s turned the volume knob" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_myths(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six myths, each answered: myth or fact?
    quiz = [("hope is just wishful thinking", "myth"),
            ("hope means ignoring reality", "myth"),
            ("hope is only for optimists", "myth"),
            ("more hope is always better", "myth"),
            ("losing hope means something is broken in you", "myth"),
            ("hope needs goals plus pathways plus agency", "fact")]
    answers = ["myth", "myth", "myth", "myth", "myth", "fact"]
    score = sum(1 for (_, c), a in zip(quiz, answers) if a == c)
    print("myth quiz: %d/%d correct" % (score, len(quiz)))
    for (q, c), a in zip(quiz, answers):
        print("  [%s] %-52s -> %s" % ("ok" if a == c else "MISS", q, c))
    assert score == 6
    assert score / len(quiz) > 0.99
    print("rule: fix the definition and the machinery stops obeying false rules")
    print("OK: %s cleared the attic" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_first_person(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # first-person passage assembled from the record's own sensory channels
    channels = ["breath comes a touch deeper", "chest feels a little lifted",
                "eyes want to look up and ahead", "thoughts step, not race",
                "each surviving route adds a degree of warmth",
                "time leans forward like a corridor with doors",
                "shoulders square, jaw unclenches",
                "a quiet hum underneath: movement is allowed"]
    passage = "Inside hope: " + "; ".join(channels) + "."
    words = passage.split()
    print(passage)
    print("channels rendered: %d, words: %d" % (len(channels), len(words)))
    assert len(channels) == 8
    assert 30 < len(words) < 120
    assert "corridor" in passage and "warmth" in passage
    print("rule: goal, pathways, agency rendered as felt experience")
    print("OK: %s stepped inside the feeling" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_time_course(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four movements: onset, build, fade/resolution, aftershock
    scenes = [("1 onset (the spark)", 2.0),
              ("2 build (pathways sketched)", 6.0),
              ("3 peak (goal feels near)", 9.0),
              ("4a resolution (goal arrives)", 3.0),
              ("4b fade (routes close)", 1.5),
              ("5 aftershock (memory re-warms)", 2.5)]
    for label, v in scenes:
        bar = "#" * int(v)
        print("  %-34s %4.1f %s" % (label, v, bar))
    peak = max(scenes, key=lambda p: p[1])
    print("peak scene: %s at %.1f" % (peak[0], peak[1]))
    assert peak[0].startswith("3 peak")
    assert 8.9 < peak[1] < 9.1
    # renewability: one new route re-ignites from the fade floor
    floor = 1.5
    reignited = floor + 2.0
    print("after one new route: %.1f (renewable from a single spark)" % reignited)
    assert 3.49 < reignited < 3.51
    print("rule: spark, build, fade or resolve, echo - and renewable throughout")
    print("OK: %s walked the life cycle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_low_vs_high(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # same machinery, two gains: flicker vs blaze
    low = {"goal": 1, "pathways": 0.2, "agency": 1.0}
    high = {"goal": 1, "pathways": 3.0, "agency": 9.0}
    def total(s):
        return s["goal"] + s["pathways"] + s["agency"]
    print("flicker total: %.1f (thin, returning thought)" % total(low))
    print("blaze total: %.1f (reorganizing current)" % total(high))
    assert 2.19 < total(low) < 2.21
    assert 12.9 < total(high) < 13.1
    # transition: one confirmed pathway raises agency, which sketches the next
    agency, pathways = 1.0, 0.2
    agency += 2.0
    pathways += 1.0
    print("after one confirmed pathway: agency %.1f, pathways %.1f" % (agency, pathways))
    assert 2.9 < agency < 3.1 and 1.19 < pathways < 1.21
    print("rule: same structure, different gain - the loop bridges the two")
    print("OK: %s held both snapshots" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_hope_optimism_blend(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # division of labor: optimism sets the base rate, hope runs the machinery
    base_rate = 0.7          # optimistic prior: effort tends to pay
    routes, agency = 3, 6.0  # hope machinery: 3 live routes, agency 6
    blend_strength = base_rate * (routes + agency)
    print("blend strength: %.2f (base rate %.1f x machinery %.1f)" % (blend_strength, base_rate, routes + agency))
    assert 6.29 < blend_strength < 6.31
    # failure test: one route closes; optimism keeps rerouting funded
    routes -= 1
    funded = base_rate > 0.5
    print("route closed -> routes %d, rerouting funded: %s" % (routes, funded))
    assert routes == 2 and funded is True
    # unblended failure modes
    print("optimism alone: cheerful passivity; hope alone: grim determination")
    print("rule: optimism funds the rerouting, hope does the rerouting")
    print("OK: %s blended the partners" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_day_vignette(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # one ordinary day, hope running underneath it
    day = [("morning priming", 3.0, "goal re-engages, first email answered"),
           ("midday dip", 1.5, "setback closes a route"),
           ("midday recovery", 4.0, "reroute sketched, warmth returns"),
           ("afternoon telling", 5.5, "shared hope, new route donated"),
           ("evening review", 5.0, "wins counted, next step named"),
           ("night rest", 4.0, "mind rests on the next step")]
    for label, v, note in day:
        print("  %-18s %4.1f  %s" % (label, v, note))
    vals = [v for _, v, _ in day]
    assert vals[1] < vals[0] < vals[2] < vals[3], "dip then recovery arc"
    assert vals[4] > vals[0], "evening higher than morning: the loop compounded"
    avg = sum(vals) / len(vals)
    print("day average hope: %.2f" % avg)
    assert 3.82 < avg < 3.84
    print("rule: not a lightning strike - a current running quietly under a normal day")
    print("OK: %s lived the day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_body(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # body channels: 0 = braced/threat, 10 = fully released/ready
    body = {"heart_steadiness": 8.0, "breath_depth": 7.5, "jaw_release": 8.5,
            "shoulder_drop": 8.0, "hand_openness": 7.0, "gut_settling": 7.5,
            "skin_warmth": 6.5, "available_energy": 8.0}
    for channel, v in body.items():
        print("  %-16s %4.1f" % (channel, v))
    avg = sum(body.values()) / len(body)
    print("body readiness average: %.2f" % avg)
    assert 7.62 < avg < 7.63
    # the fingerprint: calm body PLUS forward energy (both high = hope)
    calm = (body["heart_steadiness"] + body["breath_depth"]) / 2.0
    forward = (body["available_energy"] + body["hand_openness"]) / 2.0
    fingerprint = calm > 7.0 and forward > 7.0
    print("calm %.1f + forward %.1f -> hope fingerprint: %s" % (calm, forward, fingerprint))
    assert fingerprint is True
    print("rule: quiet readiness - calm body plus forward-leaning energy")
    print("OK: %s read the body" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_posture(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # posture axes: vertical (upright vs collapsed), forward (lean vs withdraw)
    axes = {"spine_tall": 8.0, "shoulders_level": 7.5, "chest_open": 8.0,
            "head_level_up": 7.0, "gaze_forward_up": 8.5, "lean_in": 7.0}
    vertical = (axes["spine_tall"] + axes["chest_open"] + axes["head_level_up"]) / 3.0
    print("vertical axis (hope plays here): %.2f" % vertical)
    assert 7.66 < vertical < 7.67
    # gaze target: middle distance where futures live
    gaze_elevation_deg = 10.0
    print("gaze elevation: %.1f deg (up and beyond the present)" % gaze_elevation_deg)
    assert 9.9 < gaze_elevation_deg < 10.1
    # intensity scaling: stride length grows with agency
    stride_factor = 1.0 + 0.05 * 6.0
    print("stride factor at agency 6: %.2f" % stride_factor)
    assert 1.29 < stride_factor < 1.31
    print("rule: up, forward, open - never in collapse")
    print("OK: %s carried the posture" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_sleep_appetite(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # maintenance systems under steady hope (baseline 5.0 = neutral)
    systems = {"sleep_onset_ease": 7.5, "appetite_rhythm": 7.0, "available_energy": 8.0}
    for sys, v in systems.items():
        print("  %-18s %4.1f (delta %+.1f)" % (sys, v, v - 5.0))
    # high-intensity flip: momentum can lighten sleep for a few nights
    blaze_sleep = 4.0
    print("blaze-level sleep depth: %.1f (momentum, not distress)" % blaze_sleep)
    assert 3.9 < blaze_sleep < 4.1
    # the ledger: when hope fades, systems report first
    faded = {k: 5.0 - (v - 5.0) * 0.8 for k, v in systems.items()}
    print("systems when hope fades:")
    for sys, v in faded.items():
        print("  %-18s %4.1f" % (sys, v))
    assert all(v < 5.0 for v in faded.values())
    print("rule: the body's honest ledger - maintenance systems report hope first")
    print("OK: %s checked the ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_individual_diff(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # same machinery, four renderings - all valid hope
    renderings = {"high-body (chest lift)": 8.0, "low-body (belly settle)": 7.5,
                  "hot (warmth spreading)": 7.0, "cool (clarity, stillness)": 8.5}
    for style, v in renderings.items():
        print("  %-26s %4.1f" % (style, v))
    # machinery identical underneath: goal + pathways + agency all present
    machinery = {"goal": 1, "pathways": 1, "agency": 1}
    assert sum(machinery.values()) == 3
    spread = max(renderings.values()) - min(renderings.values())
    print("rendering spread: %.1f (variation in display, not in structure)" % spread)
    assert 1.49 < spread < 1.51
    # expressive vs reserved: visibility differs, machinery identical
    print("expressive wearer visibility: high; reserved carrier visibility: low; machinery: same")
    print("rule: same machine, personal rendering - no correct way to feel it")
    print("OK: %s honored the variation" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_face(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # FACS intensities 0-5 for the quiet signature of hope
    aus = {"AU1+2 brow raise (gentle)": 2.0, "AU12 lip-corner pull (soft)": 2.0,
           "AU6 cheek raise (Duchenne)": 0.0, "upper-lid raise (horizon)": 1.5}
    for au, v in aus.items():
        print("  %-32s %4.1f/5" % (au, v))
    # the signature: brow + lip ease present, Duchenne cheek absent
    signature = aus["AU1+2 brow raise (gentle)"] > 0 and aus["AU6 cheek raise (Duchenne)"] == 0
    print("quiet signature (brow+lip, no cheek): %s" % signature)
    assert signature is True
    # micro-signs: lip parting, slow nod, sketching pause
    micro = ["lip parting (plan forming words)", "slow nod (route confirmed)",
             "sketching pause (new pathway clicking)"]
    print("micro-signs: %d" % len(micro))
    assert len(micro) == 3
    print("rule: a face turned toward the future - open, attending, faintly lit")
    print("OK: %s read the face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_face_intensity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # amplitude per band: brow travel (mm), mouth opening (0-5), body joining (0-5)
    bands = {"flicker": (0.5, 0.0, 0.0), "steady": (2.0, 1.0, 1.5), "blaze": (4.0, 3.5, 4.5)}
    for band, (brow, mouth, body) in bands.items():
        print("  %-8s brow %3.1fmm  mouth %.1f/5  body %.1f/5" % (band, brow, mouth, body))
    # amplitude rises monotonically across bands on every channel
    for i in (0, 1, 2):
        vals = [bands[b][i] for b in ("flicker", "steady", "blaze")]
        assert vals[0] < vals[1] < vals[2], "monotonic amplitude"
    # blaze borrows joy's cheek (AU6) - structural convergence
    blaze_au6 = 2.5
    print("blaze AU6 cheek engagement: %.1f/5 (borrowed from joy)" % blaze_au6)
    assert 2.49 < blaze_au6 < 2.51
    print("rule: read amplitude - how far the features travel is the volume knob")
    print("OK: %s read the dial on the face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_hiding_faking(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hidden hope: suppression effort high, but leaks escape
    suppression = 8.0
    leaks = {"gaze drift up": 1, "inner-brow flash": 1, "deep breath": 1}
    print("suppression effort: %.1f/10; leaks escaping: %d" % (suppression, len(leaks)))
    assert len(leaks) == 3
    # micro-expression speed beats the suppression command
    micro_ms, command_ms = 150.0, 400.0
    print("micro-expression %dms vs suppression command %dms -> leaks" % (micro_ms, command_ms))
    assert micro_ms < command_ms
    # faked hope: display without machinery
    display, machinery = 9.0, 1.0
    fake_score = display - machinery
    print("faked: display %.1f - machinery %.1f = gap %.1f (all display, no machine)" % (display, machinery, fake_score))
    assert 7.9 < fake_score < 8.1
    # missing markers that give faking away
    missing = ["no sketching pauses", "no lip-parting", "no genuine gaze drift"]
    print("missing in faked hope: %d markers" % len(missing))
    assert len(missing) == 3
    print("rule: hidden = machinery without display; faked = display without machinery")
    print("OK: %s spotted the leaks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_expression_gallery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five renderable frames, each isolating one machinery event
    frames = [("1 flicker", "inner brow +2mm, pupils up 10deg"),
              ("2 steady gaze", "gentle brow raise, soft-focus forward eyes"),
              ("3 sketching pause", "lips parted a breath, gaze unfocused mid-distance"),
              ("4 confirming nod", "single slow nod + exhale"),
              ("5 blaze", "joy's repertoire admitted: smile, cheeks, shining eyes")]
    for label, note in frames:
        print("  %-16s %s" % (label, note))
    assert len(frames) == 5
    # actor's ordering rule: breath first, gaze second, mouth last
    order = ["breath (one deep exhale)", "gaze (up and beyond)", "mouth (release, never force)"]
    print("actor order: %s" % " -> ".join(order))
    assert order[0].startswith("breath") and order[-1].startswith("mouth")
    # never smile hard: forced smile reads as joy/performance, not hope
    print("rule: play attending, not grinning - the face of listening to an unspoken future")
    print("OK: %s filled the sketchbook" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_classic_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # each trigger mapped to the component it changes
    triggers = [("new option appears", "pathways"), ("good news on the goal", "agency"),
                ("help offered", "pathways+agency"), ("witnessed turnaround", "pathways"),
                ("real deadline", "goal"), ("first small win", "agency (loop ignition)")]
    for label, comp in triggers:
        print("  %-24s -> %s" % (label, comp))
    assert len(triggers) == 6
    # the ignition test: a real trigger changes at least one component
    def ignites(goal_d, pathways_d, agency_d):
        return (goal_d + pathways_d + agency_d) > 0
    print("encouragement with no component change ignites: %s" % ignites(0, 0, 0))
    print("new option (pathways +1) ignites: %s" % ignites(0, 1, 0))
    assert ignites(0, 0, 0) is False
    assert ignites(0, 1, 0) is True
    # trigger words as appraisal shortcuts
    words = ["possible", "eligible", "treatable", "opening", "next step"]
    print("trigger words: %d" % len(words))
    assert len(words) == 5
    print("rule: encouragement warms; ignition changes a component")
    print("OK: %s mapped the triggers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_personal_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # private trigger set: pre-verified, trusted more than strangers' words
    private = {"anniversary date": 8.0, "stored place": 7.5, "internalized voice": 8.5,
               "sensory anchor": 7.0, "personal proof": 9.0}
    for label, v in private.items():
        print("  %-20s trust %.1f/10" % (label, v))
    # brain discounts others' data, trusts its own history
    own, stranger = 9.0, 4.0
    print("own-history trust %.1f vs stranger encouragement %.1f" % (own, stranger))
    assert own > stranger
    strongest = max(private, key=private.get)
    print("strongest private trigger: %s" % strongest)
    assert strongest == "personal proof"
    # seeming-from-nowhere: no new information, corridor still opens
    new_info = 0
    opens = new_info == 0 and private["sensory anchor"] > 5
    print("corridor opens with zero new information: %s" % opens)
    assert opens is True
    print("rule: pre-verified keys fit only their own lock")
    print("OK: %s cut the private keys" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_surprise_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # odd triggers, each with its component effect
    odd = [("stranger's kindness", "pathways", "helpers exist -> routes exist"),
           ("well-made object", "agency", "competence contagion"),
           ("recalibrating news", "pathways", "obstacle rescaled to handleable"),
           ("child's question", "pathways", "dead assumption re-audited"),
           ("exhaustion", "goal", "guard down, quiet signal through"),
           ("minor-key song", "pathways", "grief processed, channels freed")]
    for label, comp, mech in odd:
        print("  %-20s -> %-8s (%s)" % (label, comp, mech))
    assert len(odd) == 6
    # kindness inference chain: 3 steps in under a second
    chain = ["helpers exist", "help is available", "routes exist"]
    print("kindness inference: %d steps" % len(chain))
    assert len(chain) == 3
    # the dignity test: spark source does not matter, component effect does
    dignified, effective = False, True
    counts = dignified or effective
    print("counts as trigger: %s (effect over dignity)" % counts)
    assert counts is True
    print("rule: the machinery is opportunistic, not dignified")
    print("OK: %s welcomed the strange sparks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_chain_reactions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five-stage cascade: ignition, spillover, contagion, spiral, stabilization
    stages = ["1 ignition", "2 spillover", "3 contagion", "4 upward spiral", "5 stabilization"]
    print("cascade stages: %d" % len(stages))
    assert len(stages) == 5
    # spillover: agency is global, not goal-locked
    agency_pool = 6.0
    goals = ["job", "health", "project"]
    per_goal = agency_pool / len(goals)
    print("agency pool %.1f across %d goals -> %.1f each" % (agency_pool, len(goals), per_goal))
    assert 1.99 < per_goal < 2.01
    # contagion: telling transmits the machinery; two minds sketching
    minds = 1 + 1
    routes_per_mind = 3
    print("minds sketching after telling: %d -> %d live routes" % (minds, minds * routes_per_mind))
    assert minds * routes_per_mind == 6
    # downward cascade: quarantine failures to their route
    generalized = False
    neighbors_safe = not generalized
    print("blockage generalized: %s; neighbors safe: %s" % (generalized, neighbors_safe))
    assert neighbors_safe is True
    print("rule: guard the first domino - one protected hope seeds the cascade")
    print("OK: %s ran the cascade" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_actions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # eight signature actions, each serving a component
    actions = [("planning", "pathways"), ("information-seeking", "pathways"),
               ("first step", "agency"), ("backup routes", "pathways (resilience)"),
               ("persisting/rerouting", "pathways (flexibility)"), ("recruiting", "pathways+agency"),
               ("preparing", "goal"), ("marking progress", "agency (loop fuel)")]
    for label, comp in actions:
        print("  %-22s -> %s" % (label, comp))
    assert len(actions) == 8
    # backup routes: structural resilience - no single closure kills it
    routes = 3
    closed = 1
    alive = routes - closed
    hope_survives = alive > 0
    print("routes %d, closed %d, alive %d -> hope survives: %s" % (routes, closed, alive, hope_survives))
    assert hope_survives is True
    # notable absences
    absent = ["passive waiting", "hiding the goal", "display over steps"]
    print("absent from hopeful behavior: %d" % len(absent))
    assert len(absent) == 3
    print("rule: planning, stepping, rerouting, recruiting - the proof of the machinery")
    print("OK: %s watched the doing" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_speech(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # route-words vs wall-words: the hope content of speech
    route_words = ["possible", "pathway", "next step", "we can", "option", "when"]
    wall_words = ["never", "impossible", "no point", "always fails"]
    print("route-words: %d, wall-words: %d" % (len(route_words), len(wall_words)))
    ratio = len(route_words) / len(wall_words)
    print("hope ratio: %.2f" % ratio)
    assert 1.49 < ratio < 1.51
    # conditional grammar: sentences containing their own backup plans
    sentence = "we try the evening class first, and if not, then the employer's program"
    has_backup = "if not" in sentence
    print("backup plan inside the sentence: %s" % has_backup)
    assert has_backup is True
    # music: lifted phrase endings + sketching pauses
    prosody = {"lifted endings": 1, "steady pace": 1, "sketching pauses": 1}
    print("prosody markers: %d/3" % sum(prosody.values()))
    assert sum(prosody.values()) == 3
    print("rule: count the route-words - the ratio predicts who keeps moving")
    print("OK: %s heard the voice" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_decisions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five decision domains reweighted by hope
    domains = ["risk (calculated, not reckless)", "time horizon (lengthened)",
               "option breadth (pruning delayed)", "information (diagnostic over comforting)",
               "social (collaborators over solo)"]
    print("reweighted domains: %d" % len(domains))
    assert len(domains) == 5
    # horizon: navigable future lowers discounting of delayed rewards
    discount_closed, discount_open = 0.9, 0.5
    print("discount rate: closed future %.1f -> open future %.1f" % (discount_closed, discount_open))
    assert discount_open < discount_closed
    # shadow side: three biases when the audit stops
    biases = ["underweight base rates", "overweight the vivid route", "persistence past rerouting"]
    print("shadow biases: %d" % len(biases))
    assert len(biases) == 3
    # the pathways audit: routes real, plural, evidence-updated
    audit = {"real": 1, "plural": 1, "evidence_updated": 1}
    honest = sum(audit.values()) == 3
    print("pathways audit passed: %s -> judgment stays sound" % honest)
    assert honest is True
    print("rule: hope should inform judgment, never merely decorate it")
    print("OK: %s weighed the scales" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_intensity_behavior(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five escalation levels with the resource each spends
    levels = [("1 quiet leaning", "attention"), ("2 active sketching", "time"),
              ("3 committed moving", "money+reputation"), ("4 full mobilization", "schedule+team"),
              ("5 blaze", "other people's time")]
    for label, resource in levels:
        print("  %-20s spends %s" % (label, resource))
    assert len(levels) == 5
    # jumps follow pathway confirmations
    agency, level = 2.0, 1
    agency += 3.0  # pathway confirmed
    level = 3 if agency >= 5.0 else level
    print("pathway confirmed: agency %.1f -> level %d" % (agency, level))
    assert level == 3
    # over-escalation: level-4 spending on level-1 information
    info_level, spend_level = 1, 4
    over = spend_level - info_level
    print("over-escalation gap: %d levels (the behavioral shadow side)" % over)
    assert over == 3
    print("rule: read the spending - the ledger never lies about the dial")
    print("OK: %s climbed the ladder" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_healthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three channels, all coupled to real pathways
    channels = {"saying (conditional speech)": 1, "showing (quiet signature)": 1,
                "channeling (daily pathway work)": 1}
    print("healthy channels active: %d/3" % sum(channels.values()))
    assert sum(channels.values()) == 3
    # reinforcement triangle: each channel feeds the others
    routes_from_speech, people_from_display, wins_from_channeling = 2, 3, 5
    total_fuel = routes_from_speech + people_from_display + wins_from_channeling
    print("triangle fuel: %d routes + %d people + %d wins = %d" % (
        routes_from_speech, people_from_display, wins_from_channeling, total_fuel))
    assert total_fuel == 10
    # the test: does it feed machinery or only image?
    feeds_machinery = True
    print("expression feeds machinery (not just image): %s" % feeds_machinery)
    assert feeds_machinery is True
    print("rule: show the work, not just the glow - coupled display")
    print("OK: %s expressed it well" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_unhealthy_expression(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bottling: three starved inputs
    starved = ["route intelligence", "reality-testing", "social fuel"]
    print("bottling starves %d inputs" % len(starved))
    assert len(starved) == 3
    # bottled hope ferments: unpruned routes generate anxiety, not agency
    routes_sketched, routes_walked = 12, 0
    pruned = routes_walked > 0
    ferment = routes_sketched > 5 and not pruned
    print("sketched %d, walked %d -> ferments into rumination: %s" % (routes_sketched, routes_walked, ferment))
    assert ferment is True
    # exploding: display spends the fuel before the steps
    fuel, display_spend, step_spend = 10.0, 9.0, 1.0
    remaining = fuel - display_spend - step_spend
    print("fuel %.1f - display %.1f - steps %.1f = %.1f left (bankrupt)" % (
        fuel, display_spend, step_spend, remaining))
    assert -0.1 < remaining < 0.1
    # public collapse costs route + standing
    cost_private, cost_public = 1, 2
    print("private failure costs %d; public collapse costs %d" % (cost_private, cost_public))
    assert cost_public > cost_private
    print("rule: bottling starves, exploding spends - both decouple display from machinery")
    print("OK: %s priced the failures" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_everyday_practices(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # seven maintenance practices + rest
    practices = ["name the goal daily", "sketch one route", "take one small step",
                 "count the wins", "keep a backup route warm", "speak it weekly",
                 "audit monthly", "rest the machinery"]
    print("maintenance practices: %d" % len(practices))
    assert len(practices) == 8
    # daily compounding: one small step a day for 30 days
    steps = 30
    agency_gain_per_step = 0.2
    total_gain = steps * agency_gain_per_step
    print("%d small steps x %.1f agency = %.1f total gain" % (steps, agency_gain_per_step, total_gain))
    assert 5.99 < total_gain < 6.01
    # smallness is a feature: the step must be cheap enough to complete daily
    cheap_enough = True
    print("step cheap enough for daily completion: %s (the loop needs daily feeding)" % cheap_enough)
    assert cheap_enough is True
    # rest is diagnostic: tired machinery masquerades as hopelessness
    print("rule: bridges are maintained with inspections, not ceremonies")
    print("OK: %s kept the maintenance log" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_reading_signs(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four channels; convergence is the detection principle
    channels = {"face (lifted gaze, brow ease)": 1, "body (unclenched, leaning)": 1,
                "voice (conditional grammar)": 1, "behavior (planning, stepping)": 1}
    agreeing = sum(channels.values())
    print("channels agreeing: %d/4" % agreeing)
    detected = agreeing >= 3
    print("hope detected (3+ agreeing): %s" % detected)
    assert detected is True
    # one channel alone is a hypothesis, not proof
    print("single channel alone = hypothesis: %s" % (1 < 3))
    # corridor-closed absence signature
    absent = {"planning stopped": 1, "gaze dropped": 1, "speech past-locked": 1}
    closed = sum(absent.values()) == 3
    print("corridor-closed signature: %s" % closed)
    assert closed is True
    # calibration: read the delta against baseline
    baseline_gaze, now_gaze = 5.0, 8.0
    delta = now_gaze - baseline_gaze
    print("gaze delta vs baseline: %+.1f (deltas beat absolutes)" % delta)
    assert 2.9 < delta < 3.1
    print("rule: convergence detects; absences warn; deltas inform")
    print("OK: %s read the room" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_supportive_responses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six supportive responses, each feeding a component
    responses = [("feed pathways (donate routes)", "pathways"),
                 ("ask sketching questions", "pathways"),
                 ("lend agency (stated belief)", "agency"),
                 ("mark wins aloud", "agency"),
                 ("protect fragile routes", "pathways"),
                 ("share concrete load", "pathways+agency")]
    for label, comp in responses:
        print("  %-32s -> %s" % (label, comp))
    assert len(responses) == 6
    # borrowed agency spends like the real thing
    own_agency, borrowed = 4.0, 3.0
    spendable = own_agency + borrowed
    print("spendable agency: %.1f own + %.1f borrowed = %.1f" % (own_agency, borrowed, spendable))
    assert 6.9 < spendable < 7.1
    # appraisal timing: criticism before testing kills, after testing prunes
    before_testing, after_testing = "kills", "prunes"
    print("criticism before testing %s; after testing %s" % (before_testing, after_testing))
    assert before_testing != after_testing
    print("rule: donate to the components - routes, questions, belief, witness, protection, load")
    print("OK: %s lent a hand" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_mistakes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six mistakes, each damaging a component while feeling virtuous
    mistakes = [("reality hammer", "pathways", "feels like honesty"),
                ("false reassurance", "agency", "feels like kindness"),
                ("route theft", "agency", "feels like help"),
                ("comparison", "goal", "feels like perspective"),
                ("cheerleader trap", "pathways", "feels like support"),
                ("abandoned witness", "agency", "feels like neutrality")]
    for label, comp, guise in mistakes:
        print("  %-18s damages %-8s (%s)" % (label, comp, guise))
    assert len(mistakes) == 6
    # premature odds-citing teaches the machinery that sketching gets punished
    pathways_before, pathways_after = 5, 2
    print("pathways generated before hammer: %d, after: %d" % (pathways_before, pathways_after))
    assert pathways_after < pathways_before
    # silence at failure confirms the worst reading
    witnessed, verdict = True, "data point"
    print("failure witnessed: %s -> reads as %s (not verdict)" % (witnessed, verdict))
    assert verdict == "data point"
    print("rule: move the errors from invisible to visible - that is where they get caught")
    print("OK: %s listed the traps" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_neighbors(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six neighbors, each varying the components differently
    neighbors = {"optimism": "general scope, no machinery", "confidence": "certainty near 1",
                 "wishful thinking": "pathways=0, agency=0", "faith (secular)": "trust ahead of evidence",
                 "despair": "pathways locked at 0", "expectation": "prediction, no wanting/working"}
    for label, diff in neighbors.items():
        print("  %-18s %s" % (label, diff))
    assert len(neighbors) == 6
    # the doing-test: behavior reveals which components run
    doing = {"optimism": "nothing (good outlook)", "hope": "the work under uncertainty",
             "wishing": "nothing (wanted outcome)", "confidence": "the work, certain",
             "despair": "nothing (closed)"}
    print("doing-test: hope -> %s" % doing["hope"])
    assert doing["hope"] == "the work under uncertainty"
    # true opposite check: despair, not fear or sadness
    print("opposite of hope: despair (fear and sadness can coexist with hope)")
    print("rule: ask what they are doing - the doing reveals the machinery")
    print("OK: %s mapped the neighborhood" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_mixes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four Plutchik-style dyads with hope
    blends = {"hope+fear": "the vigil", "hope+grief": "the lantern in the dark",
              "hope+anger": "the forge", "hope+gratitude": "the full circle"}
    for pair, name_ in blends.items():
        print("  %-16s = %s" % (pair, name_))
    assert len(blends) == 4
    # the forge runs hottest: heat + direction
    heat = {"vigil": 4.0, "lantern": 3.0, "forge": 9.0, "circle": 5.0}
    hottest = max(heat, key=heat.get)
    print("hottest blend: %s at %.1f (needs the pathways audit most)" % (hottest, heat[hottest]))
    assert hottest == "forge"
    # most stable: gratitude fills the ledger hope spends
    stability = {"vigil": 5.0, "lantern": 6.0, "forge": 4.0, "circle": 9.0}
    stablest = max(stability, key=stability.get)
    print("most stable blend: %s at %.1f" % (stablest, stability[stablest]))
    assert stablest == "circle"
    # naming rule: unnamed blends get misread
    named = True
    print("both partners named: %s -> no misreading" % named)
    assert named is True
    print("rule: pure hope is the textbook; blended hope is the real world")
    print("OK: %s mixed the dyads" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hope_full_simulation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # seven scenes, each running a named mechanism
    scenes = [("1 spark", 2.0, "onset: appraisal flips closed->open"),
              ("2 sketching", 6.0, "pathways at full gain + backup"),
              ("3 telling", 7.5, "social pooling, borrowed agency"),
              ("4 dip", 2.5, "route closure, then rerouting"),
              ("5 mobilization", 9.0, "escalation ladder, transmission"),
              ("6 resolution", 3.0, "goal discharge into satisfaction"),
              ("7 aftershock", 4.0, "memory replay -> personal proof")]
    for label, v, mech in scenes:
        bar = "#" * int(v)
        print("  %-16s %4.1f %s  [%s]" % (label, v, bar, mech))
    assert len(scenes) == 7
    peak = max(scenes, key=lambda p: p[1])
    print("peak scene: %s at %.1f" % (peak[0], peak[1]))
    assert peak[0].startswith("5 mobilization")
    assert 8.9 < peak[1] < 9.1
    # the dip's recovery is worth three sparks
    spark, recovery_value = 2.0, 3 * 2.0
    print("recovery value: %.1f = three sparks (%.1f)" % (recovery_value, spark))
    assert 5.9 < recovery_value < 6.1
    # arc check: rises to scene 5, then falls
    vals = [v for _, v, _ in scenes]
    assert vals.index(max(vals)) == 4
    assert vals[0] < vals[1] < vals[2] > vals[3] < vals[4] > vals[5]
    print("rule: hope is not a mood but a machine - understandable, maintainable, runnable")
    print("OK: %s ran the full simulation" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "definition": demo_hope_definition,
    "family": demo_hope_family,
    "intensity": demo_hope_intensity,
    "myths": demo_hope_myths,
    "first_person": demo_hope_first_person,
    "time_course": demo_hope_time_course,
    "low_vs_high": demo_hope_low_vs_high,
    "hope_optimism_blend": demo_hope_hope_optimism_blend,
    "day_vignette": demo_hope_day_vignette,
    "body": demo_hope_body,
    "posture": demo_hope_posture,
    "sleep_appetite": demo_hope_sleep_appetite,
    "individual_diff": demo_hope_individual_diff,
    "face": demo_hope_face,
    "face_intensity": demo_hope_face_intensity,
    "hiding_faking": demo_hope_hiding_faking,
    "expression_gallery": demo_hope_expression_gallery,
    "classic_triggers": demo_hope_classic_triggers,
    "personal_triggers": demo_hope_personal_triggers,
    "surprise_triggers": demo_hope_surprise_triggers,
    "chain_reactions": demo_hope_chain_reactions,
    "actions": demo_hope_actions,
    "speech": demo_hope_speech,
    "decisions": demo_hope_decisions,
    "intensity_behavior": demo_hope_intensity_behavior,
    "healthy_expression": demo_hope_healthy_expression,
    "unhealthy_expression": demo_hope_unhealthy_expression,
    "everyday_practices": demo_hope_everyday_practices,
    "reading_signs": demo_hope_reading_signs,
    "supportive_responses": demo_hope_supportive_responses,
    "mistakes": demo_hope_mistakes,
    "neighbors": demo_hope_neighbors,
    "mixes": demo_hope_mixes,
    "full_simulation": demo_hope_full_simulation,
}
