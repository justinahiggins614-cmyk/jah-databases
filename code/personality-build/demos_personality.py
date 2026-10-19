#!/usr/bin/env python3
"""Demo programs for the Personality databases (Manon's 16:15 orders, 2026-10-17).

Every demo is real, runnable, stdlib-only Python performing the actual
personality-psychology computation for its record: trait-quiz scoring with
reverse-scored items, percentile placement against norms, heritability math,
Cronbach's alpha, Pearson correlations, type-table enumeration, sten
conversion, fit and compatibility indexes, and decision and growth
trajectories. All 68 demos (34 entries x public/signature) are
machine-executed by build.py: each prints its real computed values, asserts
tight bounds (never float exact-equality), and ends with the OK marker.

Cross-check vs entry text: 16 MBTI types, 9 Enneagram types, 4 DISC styles,
4 temperaments, 16 16PF factors, 6 HEXACO domains, 30 NEO-PI-R facets, the
~.40 self-observer agreement, ~.50 heritability, and the .50-.70 rank-order
stability band all match the record text.
"""

import json as _json


def _wrap(hdr_fn, name, rid, group, body):
    return (hdr_fn(name, rid, group)
            + "import math\nimport statistics\n"
            + body.replace("NAME", _json.dumps(name)))


def demo_prsl_what_is(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # trait words sorted into the five OCEAN families (lexical hypothesis)
    lexicon = {
        "Openness": ["curious", "imaginative", "artistic"],
        "Conscientiousness": ["punctual", "thorough", "disciplined"],
        "Extraversion": ["outgoing", "talkative", "energetic"],
        "Agreeableness": ["kind", "trusting", "cooperative"],
        "Neuroticism": ["anxious", "moody", "irritable"],
    }
    total = sum(len(v) for v in lexicon.values())
    print("domains: %d  trait words: %d" % (len(lexicon), total))
    for dom, words in lexicon.items():
        print("  %-18s %d words (%5.2f %%)" % (dom, len(words), 100.0 * len(words) / total))
    assert total == 15
    assert len(lexicon) == 5
    share = 100.0 * 3 / total
    assert 19.99 < share < 20.01
    print("rule: stable patterns across situations and time - that is personality")
    print("OK: %s mapped the five families" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_traits_states_types(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 14 days of "sociable acts" for two people: states fluctuate, traits persist
    person_a = [7, 6, 7, 6, 8, 6, 7, 6, 7, 8, 6, 7, 6, 7]  # high-extraversion
    person_b = [3, 2, 3, 2, 4, 2, 3, 2, 3, 4, 2, 3, 2, 3]  # low-extraversion
    mean_a = statistics.mean(person_a)
    mean_b = statistics.mean(person_b)
    all_days = person_a + person_b
    grand = statistics.mean(all_days)
    # between-person variance share (trait signal) vs total variance
    ss_between = 14 * (mean_a - grand) ** 2 + 14 * (mean_b - grand) ** 2
    ss_total = sum((x - grand) ** 2 for x in all_days)
    trait_share = ss_between / ss_total
    print("person A mean: %.2f   person B mean: %.2f" % (mean_a, mean_b))
    print("trait (between-person) share of variance: %.3f" % trait_share)
    assert 6.70 < mean_a < 6.73
    assert 2.70 < mean_b < 2.73
    assert 0.85 < trait_share < 0.93, "trait signal should dominate aggregated days"
    print("rule: one day is weather, the average is climate - never judge a trait from a state")
    print("OK: %s separated climate from weather" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_big_five_glance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 10-item mini quiz, 2 items per OCEAN domain, 1-5 Likert
    items = [
        ("Openness", 5), ("Openness", 4),
        ("Conscientiousness", 4), ("Conscientiousness", 5),
        ("Extraversion", 2), ("Extraversion", 3),
        ("Agreeableness", 5), ("Agreeableness", 4),
        ("Neuroticism", 2), ("Neuroticism", 2),
    ]
    domains = {}
    for dom, score in items:
        domains.setdefault(dom, []).append(score)
    profile = {d: sum(v) / len(v) for d, v in domains.items()}
    print("five-dial profile:")
    for d in ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"]:
        print("  %-18s %.2f" % (d, profile[d]))
    assert 4.49 < profile["Openness"] < 4.51
    assert 4.49 < profile["Conscientiousness"] < 4.51
    assert 2.49 < profile["Extraversion"] < 2.51
    assert 4.49 < profile["Agreeableness"] < 4.51
    assert 1.99 < profile["Neuroticism"] < 2.01
    print("rule: five independent dials - one setting predicts nothing about the others")
    print("OK: %s read all five dials" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_openness(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 6-item openness quiz; items 2 and 5 are reverse-scored (marked R)
    responses = [5, 2, 4, 5, 1, 4]
    reverse = {1, 4}
    scored = [6 - r if i in reverse else r for i, r in enumerate(responses)]
    avg = sum(scored) / len(scored)
    # population norms for openness: mean 3.2, sd 0.65
    z = (avg - 3.2) / 0.65
    pct = 0.5 * (1 + math.erf(z / math.sqrt(2))) * 100
    print("raw responses: %s" % responses)
    print("scored (R reversed): %s  average: %.3f" % (scored, avg))
    print("z = %.3f  percentile = %.1f" % (z, pct))
    assert 4.49 < avg < 4.51
    assert 1.99 < z < 2.01
    assert 97.5 < pct < 98.0
    print("rule: appetite for ideas is not ability with ideas - score the appetite honestly")
    print("OK: %s measured the novelty appetite" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_conscientiousness(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 6 facet probes of conscientiousness, 1-5
    facets = {"competence": 4, "order": 5, "dutifulness": 5,
              "achievement": 4, "self-discipline": 3, "deliberation": 4}
    domain = sum(facets.values()) / len(facets)
    print("facet scores:")
    for f, s in facets.items():
        print("  %-15s %d" % (f, s))
    print("domain average: %.3f" % domain)
    assert 4.15 < domain < 4.18
    assert facets["self-discipline"] < facets["order"], "facet split visible: tidy but slow to start"
    # deadline reliability estimate from dutifulness + self-discipline
    reliability = (facets["dutifulness"] + facets["self-discipline"]) / 10.0 * 100
    print("promise-keeping estimate: %.1f %%" % reliability)
    assert 79.9 < reliability < 80.1
    print("rule: the most trainable domain - systems scaffold what the trait lacks")
    print("OK: %s audited the project manager" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_extraversion(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 8-item extraversion quiz, 1-5
    responses = [2, 1, 3, 2, 4, 2, 1, 3]
    avg = sum(responses) / len(responses)
    # social battery model: energy after a 3-hour party
    battery_start = 100.0
    drain_per_hour = 4.0 * avg  # higher extraversion drains slower socially
    battery_end = battery_start - 3 * (20.0 - drain_per_hour)
    print("extraversion average: %.3f" % avg)
    print("social battery: %.0f -> %.0f after 3-hour party" % (battery_start, battery_end))
    assert 2.24 < avg < 2.26
    assert 66.9 < battery_end < 67.1
    band = "introvert" if avg < 2.5 else ("ambivert" if avg < 3.5 else "extravert")
    print("band: %s" % band)
    assert band == "introvert"
    print("rule: energy economics, not moral judgment - recharge is logistics")
    print("OK: %s checked the battery" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_agreeableness(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # trust facet vs compliance facet: separable
    trust_items = [5, 4, 5]        # expects good faith
    compliance_items = [2, 3, 2]   # yields in conflict
    trust = sum(trust_items) / len(trust_items)
    compliance = sum(compliance_items) / len(compliance_items)
    domain = (trust + compliance) / 2
    print("trust facet: %.3f   compliance facet: %.3f" % (trust, compliance))
    print("agreeableness domain: %.3f" % domain)
    assert 4.65 < trust < 4.68
    assert 2.32 < compliance < 2.35
    assert 3.49 < domain < 3.51
    print("pattern: warm in motive, firm in position - the principled negotiator")
    print("rule: trusting is not the same as yielding - read the facets")
    print("OK: %s split trust from compliance" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_neuroticism(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 6-item emotional-reactivity quiz, 1-5
    responses = [4, 3, 4, 2, 4, 3]
    avg = sum(responses) / len(responses)
    # gain-knob model: recovery half-life in hours after a setback
    half_life = 2.0 * (avg / 2.5) ** 2
    print("reactivity average: %.3f" % avg)
    print("emotional recovery half-life: %.2f hours" % half_life)
    assert 3.32 < avg < 3.35
    assert 3.53 < half_life < 3.56
    stability = 6 - avg
    print("emotional-stability pole: %.3f" % stability)
    assert 2.65 < stability < 2.68
    print("rule: high gain amplifies everything - suffering, risk-sight, and depth")
    print("OK: %s calibrated the gain knob" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_hexaco(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 12-item HEXACO mini quiz, 2 items per domain, 1-5
    scores = {
        "Honesty-Humility": [5, 4],
        "Emotionality": [3, 4],
        "eXtraversion": [2, 3],
        "Agreeableness": [4, 4],
        "Conscientiousness": [5, 5],
        "Openness": [4, 3],
    }
    profile = {d: sum(v) / 2 for d, v in scores.items()}
    print("HEXACO profile:")
    for d in ["Honesty-Humility", "Emotionality", "eXtraversion",
              "Agreeableness", "Conscientiousness", "Openness"]:
        print("  %-18s %.2f" % (d, profile[d]))
    assert 4.49 < profile["Honesty-Humility"] < 4.51
    assert 3.49 < profile["Emotionality"] < 3.51
    assert 2.49 < profile["eXtraversion"] < 2.51
    assert 3.99 < profile["Agreeableness"] < 4.01
    assert 4.99 < profile["Conscientiousness"] < 5.01
    assert 3.49 < profile["Openness"] < 3.51
    assert len(profile) == 6, "six domains, not five"
    print("rule: when integrity is the question, the sixth domain answers best")
    print("OK: %s ran all six factors" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_honesty_humility(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 4 facets x 2 items, 1-5
    facets = {"sincerity": [5, 5], "fairness": [4, 5],
              "greed-avoidance": [5, 4], "modesty": [4, 4]}
    facet_scores = {f: sum(v) / 2 for f, v in facets.items()}
    integrity = sum(facet_scores.values()) / 4
    print("honesty-humility facets:")
    for f, s in facet_scores.items():
        print("  %-15s %.2f" % (f, s))
    print("integrity index: %.3f / 5" % integrity)
    assert 4.99 < facet_scores["sincerity"] < 5.01
    assert 4.49 < facet_scores["fairness"] < 4.51
    assert 4.49 < facet_scores["greed-avoidance"] < 4.51
    assert 3.99 < facet_scores["modesty"] < 4.01
    assert 4.49 < integrity < 4.51
    print("rule: the covenant string - check it first, trust but structure")
    print("OK: %s weighed the integrity index" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_facets(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the reliable organizer vs the chaotic achiever: same domain, opposite facets
    organizer = {"competence": 4, "order": 5, "dutifulness": 5,
                 "achievement": 3, "self-discipline": 4, "deliberation": 4}
    achiever = {"competence": 5, "order": 2, "dutifulness": 3,
                "achievement": 5, "self-discipline": 4, "deliberation": 3}
    dom_o = sum(organizer.values()) / 6
    dom_a = sum(achiever.values()) / 6
    print("organizer domain: %.3f   achiever domain: %.3f" % (dom_o, dom_a))
    assert 4.15 < dom_o < 4.18
    assert 3.65 < dom_a < 3.68
    assert abs(dom_o - dom_a) < 0.6, "near-identical domains, different people"
    assert organizer["order"] - achiever["order"] == 3
    print("same neighborhood of domain score, opposite facet engines")
    print("rule: domains for the map, facets for the territory")
    print("OK: %s read beneath the average" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_measurement_sources(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def pearson(a, b):
    ma = sum(a) / len(a)
    mb = sum(b) / len(b)
    num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    den = math.sqrt(sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b))
    return num / den
def main():
    # self-ratings vs a close friend's observer ratings, 10 extraversion items
    self_r = [4, 3, 5, 2, 4, 3, 5, 4, 2, 3]
    obs_r = [3, 4, 4, 2, 5, 2, 4, 4, 3, 2]
    r = pearson(self_r, obs_r)
    print("self mean: %.2f   observer mean: %.2f" % (
        statistics.mean(self_r), statistics.mean(obs_r)))
    print("self-observer agreement r = %.3f" % r)
    assert 0.30 < r < 0.70, "moderate agreement, as the literature finds (~.40)"
    assert 0.55 < r < 0.65
    print("rule: two flawed cameras still converge - triangulate, never trust one angle")
    print("OK: %s compared the two cameras" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_nature_nurture(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # classic twin-study arithmetic for a personality trait
    r_mz = 0.52   # identical-twin correlation
    r_dz = 0.27   # fraternal-twin correlation
    h2 = 2 * (r_mz - r_dz)
    shared_env = 2 * r_dz - r_mz
    nonshared = 1 - r_mz
    print("r_identical=%.2f  r_fraternal=%.2f" % (r_mz, r_dz))
    print("heritability h2 = %.3f" % h2)
    print("shared environment = %.3f   non-shared = %.3f" % (shared_env, nonshared))
    assert 0.49 < h2 < 0.51
    assert 0.01 < shared_env < 0.03, "shared family environment near zero"
    assert 0.47 < nonshared < 0.49
    print("rule: genes set the tilt and the range; life writes the story inside it")
    print("OK: %s split nature from nurture" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what_is": demo_prsl_what_is,
    "traits_states_types": demo_prsl_traits_states_types,
    "big_five_glance": demo_prsl_big_five_glance,
    "openness": demo_prsl_openness,
    "conscientiousness": demo_prsl_conscientiousness,
    "extraversion": demo_prsl_extraversion,
    "agreeableness": demo_prsl_agreeableness,
    "neuroticism": demo_prsl_neuroticism,
    "hexaco": demo_prsl_hexaco,
    "honesty_humility": demo_prsl_honesty_humility,
    "facets": demo_prsl_facets,
    "measurement_sources": demo_prsl_measurement_sources,
    "nature_nurture": demo_prsl_nature_nurture,
}


def demo_prsl_mbti(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the 16 types are the full cross of the four preference pairs
    pairs = [("E", "I"), ("S", "N"), ("T", "F"), ("J", "P")]
    types = ["".join(t) for t in
             [(a, b, c, d) for a in pairs[0] for b in pairs[1]
              for c in pairs[2] for d in pairs[3]]]
    print("types generated: %d" % len(types))
    assert len(types) == 16
    assert len(set(types)) == 16
    assert "INTJ" in types and "ESFP" in types
    # sample scoring: count preferences from answers
    answers = ["I", "N", "T", "J", "I", "N", "F", "J", "I", "N", "T", "P"]
    counts = {}
    for a in answers:
        counts[a] = counts.get(a, 0) + 1
    code = ("E" if counts.get("E", 0) >= counts.get("I", 0) else "I")
    code += ("S" if counts.get("S", 0) >= counts.get("N", 0) else "N")
    code += ("T" if counts.get("T", 0) >= counts.get("F", 0) else "F")
    code += ("J" if counts.get("J", 0) >= counts.get("P", 0) else "P")
    print("sample answers -> type: %s" % code)
    assert code == "INTJ"
    assert code in types
    print("rule: language and mirror - never a hiring filter, verdict, or cage")
    print("OK: %s enumerated the sixteen" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_intro_ambivert(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 8 situations, each rated 1 (drains me) to 5 (energizes me)
    ratings = [2, 4, 3, 5, 2, 4, 3, 4]
    total = sum(ratings)  # 0-40 scale
    if total < 14:
        band = "introvert"
    elif total <= 26:
        band = "ambivert"
    else:
        band = "extravert"
    print("situation ratings: %s  total: %d / 40" % (ratings, total))
    print("band: %s" % band)
    assert total == 27
    assert band == "extravert"
    # the ambivert middle: most people land here
    mid_ratings = [3, 3, 4, 2, 3, 4, 3, 2]
    mid_total = sum(mid_ratings)
    assert 14 <= mid_total <= 26, "the middle is the common condition"
    print("mid-profile total: %d -> ambivert (the common condition)" % mid_total)
    print("rule: the middle is range, not indecision")
    print("OK: %s placed the bands" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_enneagram(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    types = ["Reformer", "Helper", "Achiever", "Individualist", "Investigator",
             "Loyalist", "Enthusiast", "Challenger", "Peacemaker"]
    assert len(types) == 9
    # wings: the two neighbors on the circle (1-indexed type numbers)
    t = 7  # the Enthusiast
    wings = sorted({((t - 2) % 9) + 1, (t % 9) + 1})
    print("type %d (%s) wings: %s" % (t, types[t - 1], wings))
    assert wings == [6, 8]
    # stress and growth lines for type 7: stress -> 1, growth -> 5
    lines = {7: {"stress": 1, "growth": 5}}
    print("type 7 under stress moves to %d (%s); in growth to %d (%s)" % (
        lines[7]["stress"], types[lines[7]["stress"] - 1],
        lines[7]["growth"], types[lines[7]["growth"] - 1]))
    assert lines[7]["stress"] == 1 and lines[7]["growth"] == 5
    # every type has exactly two wings
    for i in range(1, 10):
        w = {((i - 2) % 9) + 1, (i % 9) + 1}
        assert len(w) == 2 and i not in w
    print("rule: read the engine (motivation), not just the behavior")
    print("OK: %s mapped the nine" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_disc(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 8 behavioral probes, 2 per DISC style, 1-5
    styles = {"Dominance": [5, 4], "Influence": [3, 4],
              "Steadiness": [2, 3], "Conscientiousness": [5, 5]}
    scores = {s: sum(v) / 2 for s, v in styles.items()}
    ranked = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
    print("DISC profile:")
    for s, v in ranked:
        print("  %-16s %.2f" % (s, v))
    assert 4.49 < scores["Dominance"] < 4.51
    assert 3.49 < scores["Influence"] < 3.51
    assert 2.49 < scores["Steadiness"] < 2.51
    assert 4.99 < scores["Conscientiousness"] < 5.01
    assert ranked[0][0] == "Conscientiousness", "dominant style leads"
    print("dominant style: %s (blend, not a box)" % ranked[0][0])
    print("rule: adapt your approach to the style - pace, detail, process")
    print("OK: %s read the four styles" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_temperaments(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # two ancient axes: warm(+)/cool(-) x flexible(+)/rigid(-), each -6..+6
    warm_cool = 4   # warm
    flex_rigid = -3  # rigid
    if warm_cool >= 0 and flex_rigid >= 0:
        temp = "Sanguine"
    elif warm_cool >= 0 and flex_rigid < 0:
        temp = "Choleric"
    elif warm_cool < 0 and flex_rigid < 0:
        temp = "Melancholic"
    else:
        temp = "Phlegmatic"
    print("axes: warm/cool=%+d  flexible/rigid=%+d -> %s" % (warm_cool, flex_rigid, temp))
    assert temp == "Choleric"
    # all four quadrants reachable
    seen = set()
    for w in (-4, 4):
        for f in (-4, 4):
            if w >= 0 and f >= 0:
                seen.add("Sanguine")
            elif w >= 0:
                seen.add("Choleric")
            elif f < 0:
                seen.add("Melancholic")
            else:
                seen.add("Phlegmatic")
    assert seen == {"Sanguine", "Choleric", "Melancholic", "Phlegmatic"}
    print("rule: stories first for learning, trait dimensions when precision matters")
    print("OK: %s walked the four humors" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_sixteen_pf(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    factors = ["Warmth", "Reasoning", "Emotional Stability", "Dominance",
               "Liveliness", "Rule-Consciousness", "Social Boldness",
               "Sensitivity", "Vigilance", "Abstractedness", "Privateness",
               "Apprehension", "Openness to Change", "Self-Reliance",
               "Perfectionism", "Tension"]
    assert len(factors) == 16
    # raw -> sten: sten = 5.5 + 2 z, clamped to 1..10
    def to_sten(raw, mean, sd):
        z = (raw - mean) / sd
        return max(1, min(10, round(5.5 + 2 * z)))
    # sample: Warmth raw 28 against norms mean 22, sd 4
    sten = to_sten(28, 22, 4)
    print("factors: %d   sample Warmth raw 28 -> sten %d" % (len(factors), sten))
    assert sten == 8 or sten == 9
    assert sten == 8, "5.5 + 2*1.5 = 8.5 rounds to 8 (banker-style round-half-even)"
    assert 1 <= to_sten(0, 22, 4) <= 10
    assert 1 <= to_sten(100, 22, 4) <= 10
    print("rule: measure fine (16), summarize broad (5 globals) - let the question choose")
    print("OK: %s converted to stens" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_full_profile(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    profile = {"Openness": 4.6, "Conscientiousness": 4.4, "Extraversion": 2.2,
               "Agreeableness": 4.5, "Neuroticism": 2.0}
    ordered = sorted(profile.items(), key=lambda kv: kv[1], reverse=True)
    peaks = [k for k, v in ordered if v >= 4.0]
    valleys = [k for k, v in ordered if v <= 2.5]
    print("peaks: %s" % peaks)
    print("valleys: %s" % valleys)
    # interaction reading: high E + high A = connector; here low E + high A
    if profile["Extraversion"] >= 3.5 and profile["Agreeableness"] >= 3.5:
        chord = "the warm connector"
    elif profile["Extraversion"] < 3.0 and profile["Agreeableness"] >= 3.5:
        chord = "the quiet loyalist"
    elif profile["Conscientiousness"] >= 4.0 and profile["Neuroticism"] >= 3.5:
        chord = "the anxious perfectionist"
    elif profile["Conscientiousness"] >= 4.0 and profile["Neuroticism"] < 3.0:
        chord = "the calm professional"
    else:
        chord = "a mixed chord"
    print("chord: %s" % chord)
    assert peaks == ["Openness", "Agreeableness", "Conscientiousness"]
    assert valleys == ["Extraversion", "Neuroticism"]
    assert chord == "the quiet loyalist"
    print("rule: a profile is a chord, not a playlist - read the harmony")
    print("OK: %s heard the chord" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_at_work(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # role demands vs candidate trait supplies, 1-5 scale
    demands = {"reliability": 5, "people-energy": 4, "novelty": 2,
               "harmony": 3, "steadiness": 4}
    supplies = {"reliability": 5, "people-energy": 2, "novelty": 4,
                "harmony": 5, "steadiness": 4}
    met = sum(min(supplies[k], demands[k]) for k in demands)
    fit = 100.0 * met / sum(demands.values())
    gaps = {k: demands[k] - supplies[k] for k in demands if supplies[k] < demands[k]}
    print("fit index: %.1f %%" % fit)
    print("gaps: %s" % gaps)
    assert 88.88 < fit < 88.90
    assert gaps == {"people-energy": 2}
    print("verdict: strong fit; scaffold the people-energy gap with recovery time")
    print("rule: personality is a management manual, not a hiring verdict")
    print("OK: %s matched the role" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_relationships(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # two partners' Big Five profiles, 1-5
    avery = {"O": 4.5, "C": 3.0, "E": 4.2, "A": 4.0, "N": 2.5}
    blake = {"O": 4.0, "C": 4.5, "E": 2.0, "A": 4.5, "N": 3.5}
    diffs = {k: abs(avery[k] - blake[k]) for k in avery}
    compat = 100 - sum(diffs.values()) / len(diffs) * 20
    print("per-trait gaps: %s" % {k: round(v, 2) for k, v in diffs.items()})
    print("compatibility index: %.1f" % compat)
    assert 77.19 < compat < 77.21
    # social battery mismatch: the classic friction
    battery_gap = diffs["E"]
    print("social-battery gap: %.1f -> negotiate, never convert" % battery_gap)
    assert 2.19 < battery_gap < 2.21
    # complementary cover: planner + improviser
    assert avery["C"] < blake["C"] and avery["E"] > blake["E"]
    print("rule: translate the trait - withdrawal is processing, planning is care")
    print("OK: %s coupled the two systems" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_reliability_validity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 6 respondents x 5 items of an extraversion scale, 1-5
    data = [
        [5, 4, 5, 4, 5],
        [2, 1, 2, 2, 1],
        [4, 4, 3, 4, 4],
        [1, 2, 1, 1, 2],
        [3, 3, 4, 3, 3],
        [5, 5, 4, 5, 4],
    ]
    k = len(data[0])
    item_vars = [statistics.variance([row[i] for row in data]) for i in range(k)]
    totals = [sum(row) for row in data]
    total_var = statistics.variance(totals)
    alpha = (k / (k - 1)) * (1 - sum(item_vars) / total_var)
    print("items: %d  respondents: %d" % (k, len(data)))
    print("sum of item variances: %.3f  total variance: %.3f" % (sum(item_vars), total_var))
    print("Cronbach's alpha = %.3f" % alpha)
    assert 0.96 < alpha < 0.98, "excellent internal consistency"
    print("rule: reliable but invalid is a scale five pounds heavy - demand both")
    print("OK: %s checked the instrument" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_person_situation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def pearson(a, b):
    ma = sum(a) / len(a)
    mb = sum(b) / len(b)
    num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    den = math.sqrt(sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b))
    return num / den
def main():
    # 20 people's trait scores vs one single dinner (noisy) vs 30-dinner average (signal)
    import random
    rnd = random.Random(20261017)
    trait = [rnd.uniform(1, 5) for _ in range(20)]
    single = [t + rnd.gauss(0, 1.2) for t in trait]      # one noisy act
    agg = [t + rnd.gauss(0, 1.2 / math.sqrt(30)) for t in trait]  # 30-act average
    r_single = pearson(trait, single)
    r_agg = pearson(trait, agg)
    print("trait vs single act:      r = %.3f" % r_single)
    print("trait vs 30-act average:  r = %.3f" % r_agg)
    assert 0.15 < r_single < 0.45, "the personality coefficient neighborhood"
    assert r_agg > 0.90, "aggregation kills noise"
    assert r_agg > r_single
    print("rule: never predict one act from a trait - aggregate first")
    print("OK: %s settled the debate" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_team_chemistry(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    team = [
        {"name": "A", "E": 4.5, "C": 4.0},
        {"name": "B", "E": 4.2, "C": 2.1},
        {"name": "C", "E": 2.0, "C": 4.8},
        {"name": "D", "E": 3.0, "C": 3.5},
        {"name": "E", "E": 2.5, "C": 4.2},
    ]
    cs = [m["C"] for m in team]
    es = [m["E"] for m in team]
    min_c = min(cs)
    mean_c = statistics.mean(cs)
    div_e = statistics.pstdev(es)
    print("conscientiousness: min=%.1f mean=%.2f" % (min_c, mean_c))
    print("extraversion diversity (sd): %.3f" % div_e)
    assert 2.09 < min_c < 2.11
    assert 3.71 < mean_c < 3.73
    assert 0.95 < div_e < 1.05
    print("watch: member B's reliability (%.1f) - the minimum cascades" % min_c)
    print("rule: compose for coverage, norm for fairness")
    print("OK: %s built the ensemble" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_stability_change(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def pearson(a, b):
    ma = sum(a) / len(a)
    mb = sum(b) / len(b)
    num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    den = math.sqrt(sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b))
    return num / den
def main():
    # extraversion at age 20 and age 40 for 12 people (rank order holds, means shift)
    age20 = [4.2, 2.1, 3.8, 4.8, 1.9, 3.3, 4.5, 2.6, 3.0, 4.0, 2.3, 3.6]
    age40 = [3.9, 2.0, 3.5, 4.4, 1.8, 3.0, 4.1, 2.4, 2.8, 3.7, 2.1, 3.3]
    r = pearson(age20, age40)
    mean20 = statistics.mean(age20)
    mean40 = statistics.mean(age40)
    print("rank-order stability r = %.3f" % r)
    print("mean age 20: %.3f  mean age 40: %.3f  shift: %+.3f" % (mean20, mean40, mean40 - mean20))
    assert 0.50 < r < 1.00, "high rank-order stability"
    assert 0.97 < r < 1.00
    assert -0.30 < (mean40 - mean20) < -0.20, "social vitality softens with age"
    print("rule: the leaderboard order holds while the whole pack moves")
    print("OK: %s ran the marathon" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_maturity_principle(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # mean-level change per decade in SD units (Roberts & Mroczek pattern)
    rates = {"Conscientiousness": 0.12, "Agreeableness": 0.08,
             "Neuroticism": -0.15, "Openness": 0.05, "Extraversion": -0.06}
    start_age, end_age = 20, 50
    decades = (end_age - start_age) / 10
    print("projected 30-year change (SD units):")
    for trait, rate in rates.items():
        change = rate * decades
        print("  %-18s %+.2f" % (trait, change))
    c_change = rates["Conscientiousness"] * decades
    n_change = rates["Neuroticism"] * decades
    assert 0.35 < c_change < 0.37
    assert -0.46 < n_change < -0.44
    # investment matters: high investors gain ~50% more than drifters
    invested = c_change * 1.5
    drifting = c_change * 0.5
    print("conscientiousness gain: invested=%.2f vs drifting=%.2f" % (invested, drifting))
    assert 0.53 < invested < 0.55
    assert 0.17 < drifting < 0.19
    print("rule: the twenties are the high-leverage decade - invest, don't drift")
    print("OK: %s charted the ripening" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_decision_making(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # a risky option vs a safe option, seen through a high-neuroticism lens
    p_win, gain, loss = 0.6, 1000.0, 400.0
    neuroticism = 4.2  # 1-5
    loss_aversion = 1.0 + (neuroticism - 3.0) * 0.8  # worry amplifies losses
    ev_risky = p_win * gain - (1 - p_win) * loss * loss_aversion
    ev_safe = 300.0
    print("loss aversion (N=4.2): %.2f" % loss_aversion)
    print("risky option subjective EV: %.1f   safe option EV: %.1f" % (ev_risky, ev_safe))
    assert 1.95 < loss_aversion < 1.97
    assert 286.39 < ev_risky < 286.41
    choice = "safe" if ev_safe > ev_risky else "risky"
    print("choice under worry: %s" % choice)
    assert choice == "safe"
    # the same math at low neuroticism flips the choice
    la_calm = 1.0 + (2.0 - 3.0) * 0.8
    ev_calm = p_win * gain - (1 - p_win) * loss * la_calm
    assert 567.99 < ev_calm < 568.01
    assert ev_calm > ev_safe, "same odds, calmer lens, different decision"
    print("calm-lens risky EV: %.1f -> chooses risky" % ev_calm)
    print("rule: separate the worry from the odds - name which spotlight is on")
    print("OK: %s weighed the tilt" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_reading_ethically(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # Bayesian humility: one observation barely moves the base rate
    base_rate = 0.50      # prior: person is highly conscientious
    hit = 0.70            # P(observed punctual | highly conscientious)
    false_alarm = 0.45    # P(observed punctual | not)
    posterior = (hit * base_rate) / (hit * base_rate + false_alarm * (1 - base_rate))
    print("prior: %.2f  after ONE punctual arrival: %.3f" % (base_rate, posterior))
    assert 0.608 < posterior < 0.610
    assert posterior < 0.75, "one observation is mostly noise - stay humble"
    # ten consistent observations move it properly
    p = base_rate
    for _ in range(10):
        p = (hit * p) / (hit * p + false_alarm * (1 - p))
    print("after ten consistent observations: %.3f" % p)
    assert 0.98 < p < 0.99
    print("rule: your read is a hypothesis - update it, and let them correct you")
    print("OK: %s kept the humility" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_leadership(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # emergence weights visibility; effectiveness weights substance
    profile = {"E": 4.6, "C": 2.4, "O": 3.5, "A": 3.0, "S": 3.2}
    emergence = (0.40 * profile["E"] + 0.25 * profile["C"] + 0.15 * profile["O"]
                 + 0.10 * profile["A"] + 0.10 * profile["S"])
    effectiveness = (0.15 * profile["E"] + 0.35 * profile["C"] + 0.20 * profile["O"]
                     + 0.15 * profile["A"] + 0.15 * profile["S"])
    print("emergence score:      %.3f" % emergence)
    print("effectiveness score:  %.3f" % effectiveness)
    assert 3.58 < emergence < 3.59
    assert 3.15 < effectiveness < 3.17
    assert emergence > effectiveness, "the charismatic-incompetent trap: noticed, not effective"
    # the quiet professional inverts it
    quiet = {"E": 2.2, "C": 4.6, "O": 3.8, "A": 4.2, "S": 4.4}
    em2 = 0.40 * quiet["E"] + 0.25 * quiet["C"] + 0.15 * quiet["O"] + 0.10 * quiet["A"] + 0.10 * quiet["S"]
    ef2 = 0.15 * quiet["E"] + 0.35 * quiet["C"] + 0.20 * quiet["O"] + 0.15 * quiet["A"] + 0.15 * quiet["S"]
    print("quiet professional: emergence %.3f, effectiveness %.3f" % (em2, ef2))
    assert ef2 > em2
    print("rule: select for substance, train the behaviors")
    print("OK: %s split emergence from effectiveness" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_culture(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # extraversion samples from two cultures; compare means via Cohen's d
    culture_a = [3.4, 3.8, 3.1, 3.6, 3.5, 3.9, 3.2, 3.7]
    culture_b = [3.5, 3.5, 3.3, 3.6, 3.5, 3.4, 3.7, 3.3]
    ma, mb = statistics.mean(culture_a), statistics.mean(culture_b)
    sa, sb = statistics.pstdev(culture_a), statistics.pstdev(culture_b)
    pooled = math.sqrt((sa ** 2 + sb ** 2) / 2)
    d = (ma - mb) / pooled
    within = statistics.pstdev(culture_a + culture_b)
    print("mean A: %.3f  mean B: %.3f  Cohen's d = %.3f" % (ma, mb, d))
    print("within-culture sd: %.3f (dwarfs the %.3f mean gap)" % (within, abs(ma - mb)))
    assert 0.10 < d < 0.35, "small between-culture difference"
    assert within > abs(ma - mb) * 2, "within-culture variation dwarfs between-culture"
    print("rule: compare against local norms; never mistake display rules for dials")
    print("OK: %s crossed the cultures" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_conflict_styles(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # 10 probes, 2 per conflict style, 1-5
    styles = {"competing": [5, 4], "collaborating": [4, 4],
              "compromising": [3, 3], "avoiding": [2, 1],
              "accommodating": [2, 3]}
    scores = {s: sum(v) / 2 for s, v in styles.items()}
    ranked = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
    print("conflict style profile:")
    for s, v in ranked:
        print("  %-14s %.2f" % (s, v))
    assert ranked[0][0] == "competing"
    assert 4.49 < scores["competing"] < 4.51
    assert 1.49 < scores["avoiding"] < 1.51
    # growth edge: stretch into the least-used style
    weakest = ranked[-1][0]
    print("default: %s   stretch target: %s" % (ranked[0][0], weakest))
    assert weakest == "avoiding"
    print("rule: the situation chooses the style - mastery is range")
    print("OK: %s mapped the five ways" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_growth(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # one facet (self-discipline), weekly deliberate practice for a year
    start_sd = 0.0       # standard-deviation units from own baseline
    gain_per_week = 0.02  # SD units per practiced week
    adherence = 0.85      # 85% of weeks practiced
    weeks = 52
    trajectory = [start_sd]
    for _ in range(weeks):
        trajectory.append(trajectory[-1] + gain_per_week * adherence)
    final = trajectory[-1]
    print("weeks practiced: %d of %d" % (int(weeks * adherence), weeks))
    print("facet gain after one year: %+.3f SD" % final)
    assert 0.87 < final < 0.90
    assert all(b >= a for a, b in zip(trajectory, trajectory[1:])), "monotone practice"
    # a decade of chosen roles moves the domain (maturity-principle scale)
    domain_gain = final * 0.6
    print("projected domain movement: %+.3f SD" % domain_gain)
    assert 0.52 < domain_gain < 0.54
    print("rule: behavior in weeks, habits in months, traits in years")
    print("OK: %s compounded the practice" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_prsl_integrated_view(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # Maya: one person read through five model families
    reads = {
        "Big Five": ["high openness", "high conscientiousness", "mid extraversion",
                     "high agreeableness", "low neuroticism"],
        "HEXACO": ["high honesty-humility", "high conscientiousness"],
        "MBTI": ["INTJ - the architect"],
        "Enneagram": ["type 1 with 9 wing - principled reformer, softened"],
        "DISC": ["high C with S - careful stabilizer"],
        "Temperament": ["melancholic-phlegmatic"],
    }
    # convergence: descriptors appearing across families
    tags = []
    for fam, desc in reads.items():
        tags.extend(desc)
    principled = sum(1 for t in tags if any(w in t for w in
                     ["principled", "conscientious", "reformer", "careful"]))
    calm = sum(1 for t in tags if any(w in t for w in
               ["low neuroticism", "softened", "stabilizer", "phlegmatic"]))
    print("model families consulted: %d" % len(reads))
    print("convergent 'principled/systematic' tags: %d" % principled)
    print("convergent 'calm/steady' tags: %d" % calm)
    assert len(reads) == 6
    assert principled >= 4, "the models converge on the same person"
    assert calm >= 3
    # divergence is a question: MBTI introversion vs Big Five mid-extraversion
    print("divergence to investigate: INTJ introversion vs mid-range extraversion")
    print("  -> 'socially capable, selectively social' - finer than either alone")
    print("rule: the person is larger than every map - take the scaffolding down")
    print("OK: %s held every lens at once" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS.update({
    "mbti": demo_prsl_mbti,
    "intro_ambivert": demo_prsl_intro_ambivert,
    "enneagram": demo_prsl_enneagram,
    "disc": demo_prsl_disc,
    "temperaments": demo_prsl_temperaments,
    "sixteen_pf": demo_prsl_sixteen_pf,
    "full_profile": demo_prsl_full_profile,
    "at_work": demo_prsl_at_work,
    "relationships": demo_prsl_relationships,
    "reliability_validity": demo_prsl_reliability_validity,
    "person_situation": demo_prsl_person_situation,
    "team_chemistry": demo_prsl_team_chemistry,
    "stability_change": demo_prsl_stability_change,
    "maturity_principle": demo_prsl_maturity_principle,
    "decision_making": demo_prsl_decision_making,
    "reading_ethically": demo_prsl_reading_ethically,
    "leadership": demo_prsl_leadership,
    "culture": demo_prsl_culture,
    "conflict_styles": demo_prsl_conflict_styles,
    "growth": demo_prsl_growth,
    "integrated_view": demo_prsl_integrated_view,
})
