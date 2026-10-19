#!/usr/bin/env python3
"""Demo programs for the Geography Quiz databases (Manon 16:15 orders 2026-10-17).

Every demo is a real, runnable, stdlib-only Python quiz runner. It loads
the same ten questions and answers the record carries (passed in as qa,
straight from entries_quiz_geography.ENTRIES - so record text and demo
output cannot drift apart), simulates a scored run, asserts the exact
score, prints the full answer key, and ends with the OK marker.

All 68 are machine-executed by build.py: each prints its real computed
values, asserts tight bounds (integer score math, never float
exact-equality), and ends with the OK marker.
"""
import json

_QUIZ_BODY = '''\
QA = QA_DATA

def _norm(s):
    return " ".join(str(s).strip().lower().split())

def main():
    total = len(QA)
    print("quiz: " + QUIZNAME)
    print("questions: %d" % total)
    assert total == 10, "a quiz record holds exactly 10 questions"
    # simulated run: even questions answered correctly, odd ones missed
    simulated = [a if (i % 2 == 0) else "I am not sure"
                 for i, (q, a) in enumerate(QA)]
    score = 0
    for i, ((question, answer), given) in enumerate(zip(QA, simulated), start=1):
        assert question.strip(), "blank question at %d" % i
        assert answer.strip(), "blank answer at %d" % i
        correct = _norm(given) == _norm(answer)
        score += 10 if correct else 0
        print("Q%d: %s" % (i, question))
        print("   answered: %s -> %s" % (given, "CORRECT" if correct else "WRONG"))
    print("final score: %d / 100" % score)
    assert 40 < score < 60, "even-index pattern must land at exactly 50"
    assert score == 50
    print("--- ANSWER KEY (at the bottom) ---")
    for i, (question, answer) in enumerate(QA, start=1):
        print("%d. %s" % (i, answer))
    print("grading bands: 90-100 excellent, 70-80 strong pass, 50-60 learning, below 50 retry")
    print("OK: " + QUIZNAME + " ran, scored, and revealed its answers")
if __name__ == "__main__":
    main()
'''


def _quiz_demo(hdr, name, rid, group, points, req, qa):
    body = _QUIZ_BODY.replace("QA_DATA", repr([(q, a) for q, a in qa]))
    body = body.replace("QUIZNAME", json.dumps(name))
    return hdr(name, rid, group) + body


def demo_qzg_continents_oceans(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_world_capitals(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_maps_compass(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_mountains(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_great_rivers(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_deserts_rainforests(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_islands(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_lakes(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_us_states(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_europe(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_asia(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_africa(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_south_america(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_volcanoes(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_climate(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_latlong(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_polar(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_landmarks(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_rivers_americas(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_rivers_africa_asia(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_ocean_currents(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_caves_canyons(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_borders(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_world_records(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_cities(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_europe_rivers(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_map_projections(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_tectonics(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_waterfalls(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_central_asia(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_island_nations(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_border_trivia(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_middle_east(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


def demo_qzg_grand_challenge(hdr, name, rid, group, points, req, qa):
    return _quiz_demo(hdr, name, rid, group, points, req, qa)


DEMOS = {
    "qzg_continents_oceans": demo_qzg_continents_oceans,
    "qzg_world_capitals": demo_qzg_world_capitals,
    "qzg_maps_compass": demo_qzg_maps_compass,
    "qzg_mountains": demo_qzg_mountains,
    "qzg_great_rivers": demo_qzg_great_rivers,
    "qzg_deserts_rainforests": demo_qzg_deserts_rainforests,
    "qzg_islands": demo_qzg_islands,
    "qzg_lakes": demo_qzg_lakes,
    "qzg_us_states": demo_qzg_us_states,
    "qzg_europe": demo_qzg_europe,
    "qzg_asia": demo_qzg_asia,
    "qzg_africa": demo_qzg_africa,
    "qzg_south_america": demo_qzg_south_america,
    "qzg_volcanoes": demo_qzg_volcanoes,
    "qzg_climate": demo_qzg_climate,
    "qzg_latlong": demo_qzg_latlong,
    "qzg_polar": demo_qzg_polar,
    "qzg_landmarks": demo_qzg_landmarks,
    "qzg_rivers_americas": demo_qzg_rivers_americas,
    "qzg_rivers_africa_asia": demo_qzg_rivers_africa_asia,
    "qzg_ocean_currents": demo_qzg_ocean_currents,
    "qzg_caves_canyons": demo_qzg_caves_canyons,
    "qzg_borders": demo_qzg_borders,
    "qzg_world_records": demo_qzg_world_records,
    "qzg_cities": demo_qzg_cities,
    "qzg_europe_rivers": demo_qzg_europe_rivers,
    "qzg_map_projections": demo_qzg_map_projections,
    "qzg_tectonics": demo_qzg_tectonics,
    "qzg_waterfalls": demo_qzg_waterfalls,
    "qzg_central_asia": demo_qzg_central_asia,
    "qzg_island_nations": demo_qzg_island_nations,
    "qzg_border_trivia": demo_qzg_border_trivia,
    "qzg_middle_east": demo_qzg_middle_east,
    "qzg_grand_challenge": demo_qzg_grand_challenge,
}
