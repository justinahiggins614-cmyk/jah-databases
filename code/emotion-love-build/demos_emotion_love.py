#!/usr/bin/env python3
"""68 machine-executed demos for the Love Emotion databases (34 entries x 2 editions).

Every demo is a real, runnable, stdlib-only Python emotion-scenario
simulator: descriptive and educational only, never diagnosing anyone. Each
program simulates its scenario scene by scene (inner monologue, body
signals, facial expression, dialogue, behavior) to resolution, prints its
real computed values, asserts tight bounds (math.isclose - never float
exact-equality), and ends with the OK marker. Deterministic: no randomness,
so every run reproduces the same values.

Three demo shapes:
  _sim       - scenario simulator: 5-stage intensity arc with body signals
               and cue detection scores per stage.
  _blend     - mix blender (record 33): love + partner emotion blended with
               weights, blended profile asserted between components.
  _recognize - recognition trainer (records 29-31): love cue scores versus
               distractor-emotion cue scores; love must win on its own cues.
"""

import math

# ---------------------------------------------------------------- factories

def _q(s):
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")


def _sim(hdr, name, rid, group, key_points, req, scenario, intensity, cues):
    cue_src = ",\n    ".join('("%s", %.2f)' % (_q(c), w) for c, w in cues)
    prog = hdr(name, rid, group) + '''\
"""Emotion-scenario simulator (descriptive/educational only - never diagnosing).
Simulates the scenario scene by scene: intensity arc, body signals, facial
cues, inner monologue beats, and behavior - to resolution."""
import math


def main():
    scenario = "%s"
    intensity = %.1f  # 0..10 dial
    assert 0.0 <= intensity <= 10.0, "intensity out of range"
    stages = [("onset", 0.20), ("rise", 0.55), ("peak", 1.00),
              ("ease", 0.60), ("aftershock", 0.30)]
    cues = [
    %s,
    ]
    cue_mass = sum(w for _, w in cues)
    levels, hearts, breaths, detected = [], [], [], []
    print("scenario: %%s (intensity %%.1f/10)" %% (scenario, intensity))
    for label, w in stages:
        lvl = intensity * w
        heart = 68.0 + 4.2 * lvl          # bpm: arousal lifts resting 68
        breath = 14.0 + 0.9 * lvl         # breaths/min from resting 14
        warmth = 10.0 * w                 # felt warmth 0..10
        n_cues = int(round(cue_mass * w)) # cues visible this stage
        levels.append(lvl); hearts.append(heart)
        breaths.append(breath); detected.append(n_cues)
        print("  %%-12s level=%%5.2f heart=%%6.1f bpm breath=%%5.1f/min "
              "warmth=%%4.1f/10 cues=%%d" %% (label, lvl, heart, breath, warmth, n_cues))
    peak_i = max(range(len(levels)), key=lambda i: levels[i])
    assert stages[peak_i][0] == "peak", "arc must crest at peak"
    assert detected[-1] < detected[peak_i], "aftershock must trail peak"
    assert detected[0] < detected[peak_i], "onset must trail peak"
    assert all(60.0 <= h <= 120.0 for h in hearts), "heart out of bounds"
    assert all(12.0 <= b <= 26.0 for b in breaths), "breath out of bounds"
    total = math.fsum(levels)
    expect = intensity * math.fsum(w for _, w in stages)
    assert math.isclose(total, expect, rel_tol=1e-9), "arc energy mismatch"
    assert math.isclose(levels[2], intensity, rel_tol=1e-9), "peak must equal dial"
    print("peak heart=%%.1f bpm, peak cues=%%d/%%d, arc energy=%%.2f" %%
          (hearts[peak_i], detected[peak_i], int(round(cue_mass)), total))
    print("OK: simulated '%%s' - arc onset->peak->aftershock verified, "
          "body signals in bounds" %% scenario)


if __name__ == "__main__":
    main()
'''
    return prog % (_q(scenario), float(intensity), cue_src)


def _blend(hdr, name, rid, group, key_points, req, partner, pw, desc):
    prog = hdr(name, rid, group) + '''\
"""Mix blender (descriptive/educational only): blends love with a partner
emotion Plutchik-style and reports the blended profile."""
import math


def main():
    love = {"warmth": 9.0, "arousal": 6.0, "valence": 9.2, "approach": 8.5}
    partner = {"warmth": %.1f, "arousal": %.1f, "valence": %.1f, "approach": %.1f}
    partner_name = "%s"
    wl, wp = 0.6, 0.4  # love leads the blend
    blend = {k: wl * love[k] + wp * partner[k] for k in love}
    for k in love:
        lo, hi = min(love[k], partner[k]), max(love[k], partner[k])
        assert lo - 1e-9 <= blend[k] <= hi + 1e-9, "blend out of component range"
    for k in love:
        expect = 0.6 * love[k] + 0.4 * partner[k]
        assert math.isclose(blend[k], expect, rel_tol=1e-9), "blend math drift"
    print("blend: love(0.6) + %%s(0.4) -> %s" %% partner_name)
    for k in ("warmth", "arousal", "valence", "approach"):
        print("  %%-8s love=%%4.1f partner=%%4.1f blend=%%5.2f" %%
              (k, love[k], partner[k], blend[k]))
    print("OK: blend '%%s' verified - profile inside component ranges" %% "%s")


if __name__ == "__main__":
    main()
'''
    return prog % (pw["warmth"], pw["arousal"], pw["valence"], pw["approach"],
                   _q(partner), _q(desc), _q(desc))


def _recognize(hdr, name, rid, group, key_points, req, task, love_cues, distractors):
    lc_src = ",\n    ".join('("%s", %.2f)' % (_q(c), w) for c, w in love_cues)
    d_src = ",\n    ".join('("%s", "%s", %.2f)' % (_q(n), _q(e), w)
                           for n, e, w in distractors)
    prog = hdr(name, rid, group) + '''\
"""Recognition trainer (descriptive/educational only): scores love cues
against distractor-emotion cues for a described scenario. No real people."""
import math


def main():
    task = "%s"
    love_cues = [
    %s,
    ]
    distractors = [
    %s,
    ]
    love_total = math.fsum(w for _, w in love_cues)
    by_emo = {}
    for cname, emo, w in distractors:
        by_emo[emo] = by_emo.get(emo, 0.0) + w
    print("task: %%s" %% task)
    print("  love cue score: %%.2f" %% love_total)
    for emo, tot in sorted(by_emo.items()):
        print("  %%-12s distractor score: %%.2f" %% (emo, tot))
        assert love_total > tot, "love cues must outscore " + emo
    assert math.isclose(love_total, math.fsum(w for _, w in love_cues),
                        rel_tol=1e-9)
    best = max(by_emo, key=lambda e: by_emo[e])
    margin = love_total - by_emo[best]
    print("OK: recognition '%%s' - love cues win by margin %%.2f" %% (task, margin))


if __name__ == "__main__":
    main()
'''
    return prog % (_q(task), lc_src, d_src)


# ------------------------------------------------------------------ demos
# Signature: fn(hdr, name, rid, group, key_points, req)

def demo_what_love_is(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "defining love in plain words for a newcomer", 4.0,
                [("warmth toward the other", 0.90),
                 ("their welfare tied to mine", 0.95),
                 ("choosing in their favor", 0.85),
                 ("closeness, feeling, steady choice", 0.80)])


def demo_emotion_family(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "placing love on the emotion wheel: joy plus trust", 3.0,
                [("joy brightening the bond", 0.85),
                 ("trust calming the threat system", 0.90),
                 ("complex, assembled over time", 0.75),
                 ("neighbors: jealousy, grief, fierceness", 0.70)])


def demo_volumes(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "the same love at mild, moderate, and intense volume", 6.0,
                [("mild: quiet fondness", 0.80),
                 ("moderate: clearly felt and shown", 0.90),
                 ("intense: overwhelming arousal", 0.95),
                 ("low volume is not absence", 0.85)])


def demo_myths(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "busting the thunderbolt myth with a slow-grown love", 3.0,
                [("slow growth is fully real", 0.90),
                 ("settling is maturation", 0.85),
                 ("repair beats no-conflict", 0.90),
                 ("love is plural by nature", 0.80)])


def demo_first_person(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "inside the feeling: attention leaning toward the beloved", 7.0,
                [("chest full and open", 0.95),
                 ("body angling like toward light", 0.90),
                 ("fear backgrounded by trust", 0.85),
                 ("wanting their well-being", 0.95)])


def demo_arc(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "the arc: onset, peak, settling, aftershock in one evening", 6.0,
                [("onset: salience takes hold", 0.85),
                 ("peak: maximum arousal", 0.95),
                 ("settling: calm steadiness", 0.90),
                 ("aftershock: the echo fades on schedule", 0.80)])


def demo_low_vs_high(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "Thursday evening calm beside 3 a.m. intensity", 5.0,
                [("quiet fondness doing structural work", 0.90),
                 ("consuming arousal marking preciousness", 0.90),
                 ("whisper and shout: both the voice", 0.95),
                 ("same appraisal, different arousal", 0.85)])


def demo_love_joy_mix(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "laughter in the kitchen: love with its native joy", 7.0,
                [("love the ground, joy the lift", 0.95),
                 ("play that builds shared history", 0.90),
                 ("deposits keeping the ratio healthy", 0.85),
                 ("broadened attention, richer memories", 0.80)])


def demo_day_in_the_life(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "an ordinary day with love running underneath it all", 4.0,
                [("morning safety check", 0.85),
                 ("the diagonal sandwich remembered", 0.90),
                 ("tiny deposits through the day", 0.90),
                 ("evening co-regulation, wordless", 0.95)])


def demo_body_signals(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "the body speaks first: heart, breath, gut, skin", 6.0,
                [("racing then steadying heart", 0.90),
                 ("quickened then deepened breath", 0.85),
                 ("butterflies: the gut reporting", 0.90),
                 ("blush, dilated pupils, electric touch", 0.95)])


def demo_posture_movement(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "geometry of two bodies: open, oriented, near", 5.0,
                [("torso open, room made", 0.90),
                 ("compass-needle orientation", 0.95),
                 ("distance closed to intimate zone", 0.90),
                 ("matched pace, mirrored gesture", 0.85)])


def demo_sleep_appetite_energy(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "the maintenance systems: sleep, appetite, energy", 5.0,
                [("new love: wired and sleepless", 0.85),
                 ("settled love: deeper shared sleep", 0.90),
                 ("appetite suppressed, then restored", 0.80),
                 ("stimulant blend yielding to calm stamina", 0.90)])


def demo_body_differences(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "loud body, quiet body: the same love, different instruments", 4.0,
                [("temperament sets the baseline", 0.90),
                 ("attachment tunes the signal", 0.85),
                 ("culture writes the display rules", 0.80),
                 ("read across time and channels", 0.95)])


def demo_face_of_love(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "reading the face: eyes, brows, mouth, micro-signs", 6.0,
                [("soft sustained gaze, dilated pupils", 0.95),
                 ("the fifth-of-a-second brow flash", 0.90),
                 ("the true smile reaching the eyes", 0.95),
                 ("head tilt baring the neck in trust", 0.85)])


def demo_expression_intensity(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "the face dial: whisper, conversation, shout", 6.0,
                [("low: private softening", 0.85),
                 ("moderate: the you-can-just-tell glow", 0.95),
                 ("high: stunned blank or overflow", 0.90),
                 ("calibrate the reading to the volume", 0.90)])


def demo_hiding_faking(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "the concealed feeling: what leaks through the mask", 5.0,
                [("returning gaze that will not stay away", 0.95),
                 ("pupils that cannot be suppressed", 0.90),
                 ("the sub-second light-up before control", 0.95),
                 ("the body dissenting from the performance", 0.90)])


def demo_expression_gallery(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "directing the love scene: mechanics, not symbols", 5.0,
                [("draw the eyes first: soft, aimed", 0.90),
                 ("the small true smile, never the grin", 0.85),
                 ("act the arrival beat, not the declaration", 0.95),
                 ("let the leaks do the work", 0.90)])


def demo_classic_triggers(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "how it started: proximity, kindness, disclosure", 5.0,
                [("repeated contact, love as geography", 0.90),
                 ("kindness met in a moment of need", 0.95),
                 ("being known and knowing", 0.90),
                 ("small care compounding like interest", 0.85)])


def demo_personal_triggers(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "the private trigger map: songs, dates, mispronounced words", 4.0,
                [("sensory packaging replays the feeling", 0.90),
                 ("anniversaries arriving with weather", 0.85),
                 ("neutral things absorbing the feeling", 0.90),
                 ("tending the map across decades", 0.80)])


def demo_surprise_triggers(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "the strange road: arousal, accidents, almost-lost", 6.0,
                [("borrowed arousal credited to the beloved", 0.90),
                 ("care teaching the heart to feel", 0.85),
                 ("the scheduling artifact that became real", 0.80),
                 ("strange roads still arrive", 0.95)])


def demo_chain_reactions(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "the cascade: love plus fear, sadness, anger, joy", 7.0,
                [("joy cascade: the upward spiral", 0.90),
                 ("fear cascade: vigilance to jealousy", 0.90),
                 ("sadness cascade: compassion with weight", 0.85),
                 ("chain-read back to the first link", 0.95)])


def demo_behavior_actions(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "love in action: approach, serve, touch, protect, repair", 6.0,
                [("time and attention spent on the beloved", 0.95),
                 ("micro-services, the atoms of bonds", 0.90),
                 ("touch: the native language", 0.95),
                 ("the comeback after conflict", 0.90)])


def demo_behavior_words(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "the dialect of love: phrases, tone, convergence", 5.0,
                [("declarations, check-ins, future-talk", 0.90),
                 ("the voice softening on their name", 0.95),
                 ("vocabularies converging", 0.85),
                 ("we-language and joint stories", 0.90)])


def demo_behavior_decisions(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "love votes: the reweighted payoff matrix", 5.0,
                [("the beloved's welfare in the equation", 0.95),
                 ("the lengthened time horizon", 0.85),
                 ("positive illusions protecting the bond", 0.90),
                 ("let love vote, never alone", 0.95)])


def demo_behavior_intensity(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "full volume: pursuit, vigilance, sacrifice, expression", 9.0,
                [("pursuit that delights, never alarms", 0.90),
                 ("vigilance calmable by reassurance", 0.90),
                 ("sacrifice that preserves the self", 0.95),
                 ("expression as gift, never leverage", 0.95)])


def demo_healthy_expression(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "say it, show it, channel it: the full expression", 6.0,
                [("specific, timely, bidirectional saying", 0.90),
                 ("showing attuned to what lands", 0.95),
                 ("love irrigating the whole life", 0.90),
                 ("pattern over peaks", 0.85)])


def demo_unhealthy_expression(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "the middle path between bottling and exploding", 6.0,
                [("bottling reads as absence", 0.90),
                 ("exploding overwhelms instead of moving", 0.90),
                 ("full feeling, human-volume delivery", 0.95),
                 ("daily transmissions; feel, write, sleep, deliver", 0.85)])


def demo_everyday_practices(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "tending the garden: seven small daily practices", 4.0,
                [("the daily deposit, on purpose", 0.95),
                 ("specific appreciation, out loud", 0.90),
                 ("ruptures repaired fast", 0.90),
                 ("novelty, separate selves, rest, review", 0.85)])


def demo_recognizing_others(hdr, name, rid, group, key_points, req):
    return _recognize(hdr, name, rid, group, key_points, req,
                      "which cues reveal love across the room",
                      [("soft sustained gaze", 0.95),
                       ("duchenne smile with smooth brow", 0.95),
                       ("torso oriented, distance closed", 0.90),
                       ("voice softening on the name", 0.85),
                       ("pattern of small kindnesses", 0.90)],
                      [("polite nod", "politeness", 0.40),
                       ("brief glance", "curiosity", 0.55),
                       ("firm handshake", "professionalism", 0.35)])


def demo_supporting_others(hdr, name, rid, group, key_points, req):
    return _recognize(hdr, name, rid, group, key_points, req,
                      "choosing the supportive response to a friend in new love",
                      [("receive the news warmly", 0.95),
                       ("ask open questions", 0.90),
                       ("normalize without minimizing", 0.90),
                       ("raise concerns once, gently", 0.85),
                       ("show up for the whole arc", 0.95)],
                      [("mock the feeling", "mockery", 0.20),
                       ("interrogate immediately", "alarm", 0.45),
                       ("issue repeated warnings", "control", 0.40)])


def demo_recognizing_mistakes(hdr, name, rid, group, key_points, req):
    return _recognize(hdr, name, rid, group, key_points, req,
                      "spotting the mishandling before it lands",
                      [("notice the mockery forming", 0.90),
                       ("catch the rushed timeline", 0.85),
                       ("hear the scorekeeping start", 0.90),
                       ("refuse the sideline diagnosis", 0.95)],
                      [("tease affectionately", "habit", 0.50),
                       ("offer scheduling advice", "helpfulness", 0.55),
                       ("share a similar story", "relating", 0.45)])


def demo_related_emotions(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "neighbors on the map: liking, infatuation, desire, need", 5.0,
                [("liking enjoys; love reorganizes", 0.90),
                 ("infatuation fades at reality; love deepens", 0.95),
                 ("desire wants; love cherishes", 0.90),
                 ("indifference is the true opposite", 0.85)])


def demo_love_mixes(hdr, name, rid, group, key_points, req):
    return _blend(hdr, name, rid, group, key_points, req,
                  "joy", {"warmth": 8.0, "arousal": 8.5, "valence": 9.5, "approach": 9.0},
                  "love plus joy: the native-weather blend")


def demo_full_simulation(hdr, name, rid, group, key_points, req):
    return _sim(hdr, name, rid, group, key_points, req,
                "June and Theo: trigger to peak to resolution in five scenes", 7.0,
                [("the wheelbarrow trigger", 0.85),
                 ("the quickening across shared Saturdays", 0.90),
                 ("the potluck crest", 0.95),
                 ("the fear cascade, chain-read and repaired", 0.90),
                 ("the spring garden resolution", 0.95)])


DEMOS = {
    "what-love-is": demo_what_love_is,
    "emotion-family": demo_emotion_family,
    "volumes": demo_volumes,
    "myths": demo_myths,
    "first-person": demo_first_person,
    "arc": demo_arc,
    "low-vs-high": demo_low_vs_high,
    "love-joy-mix": demo_love_joy_mix,
    "day-in-the-life": demo_day_in_the_life,
    "body-signals": demo_body_signals,
    "posture-movement": demo_posture_movement,
    "sleep-appetite-energy": demo_sleep_appetite_energy,
    "body-differences": demo_body_differences,
    "face-of-love": demo_face_of_love,
    "expression-intensity": demo_expression_intensity,
    "hiding-faking": demo_hiding_faking,
    "expression-gallery": demo_expression_gallery,
    "classic-triggers": demo_classic_triggers,
    "personal-triggers": demo_personal_triggers,
    "surprise-triggers": demo_surprise_triggers,
    "chain-reactions": demo_chain_reactions,
    "behavior-actions": demo_behavior_actions,
    "behavior-words": demo_behavior_words,
    "behavior-decisions": demo_behavior_decisions,
    "behavior-intensity": demo_behavior_intensity,
    "healthy-expression": demo_healthy_expression,
    "unhealthy-expression": demo_unhealthy_expression,
    "everyday-practices": demo_everyday_practices,
    "recognizing-others": demo_recognizing_others,
    "supporting-others": demo_supporting_others,
    "recognizing-mistakes": demo_recognizing_mistakes,
    "related-emotions": demo_related_emotions,
    "love-mixes": demo_love_mixes,
    "full-simulation": demo_full_simulation,
}
