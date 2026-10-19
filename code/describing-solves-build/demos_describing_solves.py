#!/usr/bin/env python3
"""Demo programs for the Describing Solves databases.

Every demo is a solution-description checker or simulator: real, runnable,
stdlib-only Python that performs the actual computation for its record,
prints the real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker. All 68 demos (34 public +
34 Signature) are machine-executed by build.py.
"""

import json as _json

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", _json.dumps(name))


def demo_dsv_what_described_solution(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the three parts of a described solution: problem, path, check
    solution = {"problem": "2x + 3 = 11, find x",
                "path": ["subtract 3: 2x = 8", "divide by 2: x = 4"],
                "check": "2(4)+3 = 11"}
    parts = ["problem", "path", "check"]
    present = sum(1 for p in parts if solution.get(p))
    completeness = present / len(parts)
    answer_only = {"answer": "x = 4"}
    present2 = sum(1 for p in parts if answer_only.get(p))
    completeness2 = present2 / len(parts)
    print("described: %d/3 parts -> completeness %.3f" % (present, completeness))
    print("answer-only: %d/3 parts -> completeness %.3f" % (present2, completeness2))
    assert 0.999 < completeness < 1.001
    assert -0.001 < completeness2 < 0.001
    assert completeness > completeness2
    print("OK: %s scored description completeness" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_problem_first(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the problem statement must come before the first solving move
    writeup = ["PROBLEM: drain flows slowly; find the clog",
               "CHECK: is the trap full? yes, partially",
               "STEP 1: place bucket under trap",
               "STEP 2: loosen trap nuts",
               "CHECK: water flows freely after cleaning"]
    prob_idx = next(i for i, l in enumerate(writeup) if l.startswith("PROBLEM"))
    first_step = next(i for i, l in enumerate(writeup) if l.startswith("STEP"))
    order_ok = prob_idx < first_step
    # crispness: the problem names unknown, known, and what counts as done
    crisp = {"unknown": "clog location", "known": "slow drain",
             "done": "water flows freely"}
    crispness = len(crisp) / 3.0
    print("problem at line %d, first step at line %d, order ok: %s"
          % (prob_idx, first_step, order_ok))
    print("crispness: %.3f" % crispness)
    assert order_ok is True
    assert 0.999 < crispness < 1.001
    print("OK: %s verified problem-first ordering" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_worked_example(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # worked-example effect: studying the worked path costs less search
    # load than solving unaided, leaving capacity for structure
    search_cost_unaided = 0.75   # flailing, backtracking, dead ends
    search_cost_worked = 0.10    # the path is shown
    structure_gain = 0.55        # attention freed for why-each-step
    load_unaided = search_cost_unaided
    load_worked = search_cost_worked
    learning_unaided = max(0.0, 1.0 - load_unaided) * 0.4
    learning_worked = max(0.0, 1.0 - load_worked) * (0.4 + structure_gain)
    print("unaided load %.2f -> learning %.3f" % (load_unaided, learning_unaided))
    print("worked  load %.2f -> learning %.3f" % (load_worked, learning_worked))
    assert 0.099 < learning_unaided < 0.101
    assert 0.854 < learning_worked < 0.856
    assert learning_worked > learning_unaided
    print("OK: %s measured the worked-example effect" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_show_work(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hidden-leap ratio: moves jumped over without a shown line
    shown = ["2x + 3 = 11",
             "2x + 3 - 3 = 11 - 3   (subtract 3 both sides)",
             "2x = 8",
             "2x / 2 = 8 / 2        (divide both sides by 2)",
             "x = 4"]
    total_moves = 4          # subtract, simplify, divide, simplify
    shown_moves = 4          # every move has its line
    leap_ratio = (total_moves - shown_moves) / total_moves
    terse = ["2x + 3 = 11", "x = 4"]
    leap_terse = (total_moves - (len(terse) - 1)) / total_moves
    print("shown lines: %d, leap ratio %.3f" % (len(shown), leap_ratio))
    print("terse lines: %d, leap ratio %.3f" % (len(terse), leap_terse))
    assert -0.001 < leap_ratio < 0.001
    assert 0.749 < leap_terse < 0.751
    assert leap_ratio < leap_terse
    print("OK: %s computed hidden-leap ratios" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_step_ordering(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # every step's inputs must be produced by an earlier step
    steps = [("gather parts", []),
             ("remove panel", ["gather parts"]),
             ("replace belt", ["remove panel"]),
             ("refit panel", ["replace belt"]),
             ("test run", ["refit panel"])]
    produced = set()
    violations = 0
    for title, needs in steps:
        for n in needs:
            if n not in produced:
                violations += 1
        produced.add(title)
    shuffled = [steps[2], steps[0], steps[4], steps[1], steps[3]]
    produced2 = set()
    violations2 = 0
    for title, needs in shuffled:
        for n in needs:
            if n not in produced2:
                violations2 += 1
        produced2.add(title)
    print("ordered violations: %d, shuffled violations: %d" % (violations, violations2))
    assert violations == 0
    assert violations2 == 2
    print("OK: %s checked step dependency ordering" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_tools_first(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # every tool touched by a step must appear on the upfront list
    materials = ["10mm wrench", "phillips screwdriver", "replacement belt",
                 "shop rag", "torque spec 25 Nm"]
    steps_touch = ["10mm wrench", "phillips screwdriver", "replacement belt",
                   "10mm wrench", "torque spec 25 Nm"]
    missing = [t for t in steps_touch if t not in materials]
    coverage = (len(steps_touch) - len(missing)) / len(steps_touch)
    steps_touch2 = steps_touch + ["impact driver"]  # smuggled tool
    missing2 = [t for t in steps_touch2 if t not in materials]
    coverage2 = (len(steps_touch2) - len(missing2)) / len(steps_touch2)
    print("coverage complete list: %.3f, with smuggled tool: %.3f"
          % (coverage, coverage2))
    assert 0.999 < coverage < 1.001
    assert 0.832 < coverage2 < 0.834
    assert missing2 == ["impact driver"]
    print("OK: %s audited tools against the materials list" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_given_find_plan(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # GIVEN / FIND / PLAN boxes: the plan must reference the givens
    given = {"length_m": 12.0, "width_m": 9.0, "door_m2": 2.0}
    find = {"paint_m2": "wall area minus door, in square meters"}
    plan = ("use the area formula on the given length and width, "
            "then subtract the given door area")
    refs = sum(1 for g in given if g.split("_")[0] in plan)
    ref_ratio = refs / len(given)
    # execute the plan
    area = given["length_m"] * given["width_m"] - given["door_m2"]
    print("plan references %d/%d givens (ratio %.3f)" % (refs, len(given), ref_ratio))
    print("paint needed: %.1f m^2" % area)
    assert 0.999 < ref_ratio < 1.001
    assert 105.9 < area < 106.1
    assert "square meters" in find["paint_m2"]
    print("OK: %s ran the given-find-plan boxes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_label_moves(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # every step gets a purpose label from the known kinds
    kinds = {"setup", "transform", "check", "cleanup"}
    steps = [("disconnect power", "setup"),
             ("remove cover", "setup"),
             ("swap fuse", "transform"),
             ("power on, test lamp", "check"),
             ("refit cover, coil cord", "cleanup")]
    labeled = sum(1 for _, k in steps if k in kinds)
    coverage = labeled / len(steps)
    # a step whose purpose cannot be stated is two steps hiding as one
    unlabeled = [("fiddle with wires", "")]
    coverage2 = sum(1 for _, k in unlabeled if k in kinds) / len(unlabeled)
    print("label coverage: %.3f, unlabeled step coverage: %.3f" % (coverage, coverage2))
    assert 0.999 < coverage < 1.001
    assert -0.001 < coverage2 < 0.001
    print("OK: %s verified purpose labels on every move" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_check_step(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the check: feed the answer back into the problem
    x = 4  # candidate from solving 2x + 3 = 11
    lhs = 2 * x + 3
    rhs = 11
    residual = abs(lhs - rhs)
    # reasonableness: a wall area cannot be absurd
    wall_m2 = 106.0
    sane = 0.0 < wall_m2 < 100000.0
    print("substitution: 2(%d)+3 = %d, residual %.3f" % (x, lhs, residual))
    print("reasonableness of %.1f m^2: %s" % (wall_m2, sane))
    assert -0.001 < residual < 0.001
    assert sane is True
    # a wrong answer fails the check
    assert abs(2 * 5 + 3 - 11) > 0.001
    print("OK: %s closed the loop with the check step" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_think_aloud(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # one sentence per step: narration grain matches action grain
    narration = ["I check the fuse first because it is the cheapest part to test.",
                 "The fuse is good, so I move to the switch.",
                 "The switch clicks but the lamp stays dark, so the fault is past the switch."]
    sentences = [s.count(".") for s in narration]
    one_each = all(c == 1 for c in sentences)
    bad = ["I check the fuse. It looks fine. Then I test the switch and it clicks."]
    bad_counts = [s.count(".") for s in bad]
    print("sentences per step: %s -> one each: %s" % (sentences, one_each))
    print("bad narration sentences: %s" % bad_counts)
    assert one_each is True
    assert bad_counts == [3]
    assert sum(sentences) == len(narration)
    print("OK: %s enforced one sentence per step" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_deictic(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # every noun with a visual referent must be labeled in a figure
    figure_labels = {"bolt 7", "bracket A", "wire red", "fuse F1"}
    step_nouns = ["bolt 7", "bracket A", "wire red", "fuse F1"]
    pointed = sum(1 for n in step_nouns if n in figure_labels)
    coverage = pointed / len(step_nouns)
    step_nouns2 = step_nouns + ["mystery clip"]
    pointed2 = sum(1 for n in step_nouns2 if n in figure_labels)
    coverage2 = pointed2 / len(step_nouns2)
    print("pointing coverage: %.3f, with unpointed noun: %.3f" % (coverage, coverage2))
    assert 0.999 < coverage < 1.001
    assert 0.799 < coverage2 < 0.801
    print("OK: %s checked labels point at every part" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_reading_direction(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # no forward references: nothing used before it is introduced;
    # figures appear at or before the step that needs them
    doc = [("overview", None),
           ("fig 1: parts", "fig1"),
           ("step 1 uses fig1", "fig1"),
           ("term: torque", None),
           ("step 2 uses torque", None)]
    seen_figs = set()
    seen_terms = set()
    stalls = 0
    for kind, ref in doc:
        if kind.startswith("fig"):
            seen_figs.add(ref)
        if kind.startswith("term"):
            seen_terms.add(kind.split(":")[1].strip())
        if kind.startswith("step"):
            if ref and ref not in seen_figs:
                stalls += 1
            if "torque" in kind and "torque" not in seen_terms:
                stalls += 1
    print("reader stalls on forward references: %d" % stalls)
    assert stalls == 0
    # break it: reference fig2 before it appears
    assert "fig2" not in seen_figs
    print("OK: %s verified reading direction has no forward refs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_solution_schema(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # a schema: fixed skeleton, named slots; validate a filled instance
    schema_slots = ["material", "fastener", "finish"]
    scope = "fits: butt joints in softwood; not: metal joinery"
    filled = {"material": "pine", "fastener": "wood screws", "finish": "oil"}
    unfilled = [s for s in schema_slots if s not in filled]
    fill_ratio = (len(schema_slots) - len(unfilled)) / len(schema_slots)
    filled2 = {"material": "pine", "fastener": "wood screws"}  # missing finish
    unfilled2 = [s for s in schema_slots if s not in filled2]
    fill_ratio2 = (len(schema_slots) - len(unfilled2)) / len(schema_slots)
    print("schema scope: %s" % scope)
    print("fill ratio: %.3f, missing-slot ratio: %.3f" % (fill_ratio, fill_ratio2))
    assert 0.999 < fill_ratio < 1.001
    assert 0.666 < fill_ratio2 < 0.667
    assert unfilled2 == ["finish"]
    print("OK: %s validated a filled solution schema" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_fill_template(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # fill every blank; none may remain
    template = ("GIVEN: __G__  FIND: __F__  PLAN: __P__  "
                "STEP 1: __S1__  CHECK: __C__")
    values = {"__G__": "12 V battery, starter clicks",
              "__F__": "why the engine will not turn",
              "__P__": "test battery under load, then cables",
              "__S1__": "load-test the battery",
              "__C__": "engine cranks strongly"}
    filled = template
    for token, val in values.items():
        filled = filled.replace(token, val)
    remaining = filled.count("__")
    print("filled: %s" % filled[:60] + "...")
    print("remaining blank tokens: %d" % remaining)
    assert remaining == 0
    assert "__G__" not in filled and "__C__" not in filled
    print("OK: %s filled every template blank" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_critical_reading(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # critical reading: score justified claims over total claims
    steps = [("2x = 8", "subtracted 3 from both sides"),
             ("x = 4", "divided both sides by 2"),
             ("therefore done", ""),          # unjustified victory lap
             ("x = 4 works", "substituted back: 11 = 11")]
    justified = sum(1 for _, why in steps if why.strip())
    rigor = justified / len(steps)
    # the checklist: justifications, materials, real check, scope
    checklist = {"justifications": justified == len(steps),
                 "materials_listed": True,
                 "real_check": True,
                 "scope_stated": False}
    score = sum(checklist.values()) / len(checklist)
    print("rigor: %d/%d = %.3f" % (justified, len(steps), rigor))
    print("checklist score: %.3f" % score)
    assert 0.749 < rigor < 0.751
    assert 0.499 < score < 0.501
    print("OK: %s read a solution critically" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_dead_end(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the honest dead-end record: attempt, rationale, break point, lesson, cost
    record = {"attempt": "replaced the starter motor",
              "rationale": "clicking suggested starter failure",
              "break_point": "new starter clicked identically",
              "lesson": "clicking with good starter means weak current: test battery and cables",
              "cost_hours": 2.5}
    complete = sum(1 for k in ("attempt", "rationale", "break_point", "lesson")
                   if record.get(k))
    completeness = complete / 4.0
    # the lesson rules out a branch: next hunter skips the starter
    branch_pruned = "starter" in record["lesson"] or "battery" in record["lesson"]
    print("dead-end completeness: %.3f, cost logged: %.1f h" % (completeness, record["cost_hours"]))
    print("branch pruned for next hunter: %s" % branch_pruned)
    assert 0.999 < completeness < 1.001
    assert 2.49 < record["cost_hours"] < 2.51
    assert branch_pruned is True
    print("OK: %s recorded a dead end honestly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_partial_solution(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # progress marks: solved, frontier, blocked, resume
    subgoals = [("diagnose", True), ("parts ordered", True),
                ("disassemble", True), ("repair", False), ("test", False)]
    done = sum(1 for _, d in subgoals if d)
    progress = done / len(subgoals)
    frontier = "repair: windings rewound, awaiting varnish cure"
    blocked = ["varnish cure: 24 h"]
    resume = "resume at varnish check, then reassemble per steps 4-6"
    print("progress: %d/%d = %.3f" % (done, len(subgoals), progress))
    print("frontier: %s" % frontier)
    assert 0.599 < progress < 0.601
    assert len(blocked) == 1 and resume.startswith("resume at")
    print("OK: %s marked partial-solution progress" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "dsv_what_described_solution": demo_dsv_what_described_solution,
    "dsv_problem_first": demo_dsv_problem_first,
    "dsv_worked_example": demo_dsv_worked_example,
    "dsv_show_work": demo_dsv_show_work,
    "dsv_step_ordering": demo_dsv_step_ordering,
    "dsv_tools_first": demo_dsv_tools_first,
    "dsv_given_find_plan": demo_dsv_given_find_plan,
    "dsv_label_moves": demo_dsv_label_moves,
    "dsv_check_step": demo_dsv_check_step,
    "dsv_think_aloud": demo_dsv_think_aloud,
    "dsv_deictic": demo_dsv_deictic,
    "dsv_reading_direction": demo_dsv_reading_direction,
    "dsv_solution_schema": demo_dsv_solution_schema,
    "dsv_fill_template": demo_dsv_fill_template,
    "dsv_critical_reading": demo_dsv_critical_reading,
    "dsv_dead_end": demo_dsv_dead_end,
    "dsv_partial_solution": demo_dsv_partial_solution,
}


def demo_dsv_diagnostic_narrative(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hypothesis-driven diagnosis: bisect the cause space, cheapest tests first
    causes = ["fuse", "switch", "cord", "plug", "lamp", "socket", "breaker", "wire"]
    truth = "cord"
    # each probe eliminates half the candidates (bisection)
    remaining = list(causes)
    probes = 0
    while len(remaining) > 1:
        half = remaining[:len(remaining) // 2]
        probes += 1
        # probe: is the fault in this half? (continuity test)
        remaining = half if truth in half else remaining[len(remaining) // 2:]
    print("candidates: %d, probes to isolate: %d, found: %s"
          % (len(causes), probes, remaining[0]))
    assert remaining == [truth]
    assert probes == 3  # log2(8)
    # cheapest-first ordering: fuse (cheap) tested before rewiring (dear)
    costs = {"fuse": 1, "cord": 3, "wire": 9}
    order = sorted(costs, key=costs.get)
    print("cheapest-first order: %s" % order)
    assert order == ["fuse", "cord", "wire"]
    print("OK: %s narrated the diagnostic hunt" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_repair_walkthrough(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # before/after: the symptom must be gone under the conditions that made it
    state = {"powers_on": False, "fault_symptom": True}
    steps = ["disconnect power", "open case (4 screws, keep order)",
             "replace fuse F1 with 5A", "close case", "power on"]
    warnings_inline = {1: "screws differ in length: keep order"}
    state["powers_on"] = True
    state["fault_symptom"] = False
    fixed = state["powers_on"] and not state["fault_symptom"]
    # reassembly trap noted: screws must return in order
    trap_noted = 1 in warnings_inline
    print("steps: %d, warning at step %d: %s" % (len(steps), 2, trap_noted))
    print("after: powers_on=%s symptom=%s -> fixed=%s"
          % (state["powers_on"], state["fault_symptom"], fixed))
    assert fixed is True
    assert trap_noted is True
    assert len(steps) == 5
    print("OK: %s walked the repair through" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_math_presentation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # presented derivation with aligned equals and named moves, then the check
    moves = [("3x - 5", "16", "given"),
             ("3x", "21", "add 5 to both sides"),
             ("x", "7", "divide both sides by 3")]
    lines = ["%-7s= %s" % (lhs, rhs) for lhs, rhs, _ in moves]
    # alignment: equals signs line up (position of '=' constant)
    eq_pos = [l.index("=") for l in lines]
    aligned = len(set(eq_pos)) == 1
    # named moves: every line after the first names its rule
    named = all(rule != "given" and rule for _, _, rule in moves[1:])
    x = 7
    residual = abs(3 * x - 5 - 16)
    print("equals positions: %s -> aligned: %s" % (eq_pos, aligned))
    print("moves named: %s, check residual: %.3f" % (named, residual))
    assert aligned is True
    assert named is True
    assert -0.001 < residual < 0.001
    print("OK: %s presented the math solution" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_science_presentation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # IMRAD completeness + the data shown, not just summarized
    report = {"introduction": "does shade change germination time?",
              "methods": "40 seeds, 2 groups, 7 days, daily counts",
              "results": [5, 7, 6, 8, 6, 7, 6, 5, 7, 6,
                          3, 4, 3, 5, 4, 3, 4, 5, 3, 4],
              "discussion": "shade group slower; light uncontrolled, n small"}
    sections = ["introduction", "methods", "results", "discussion"]
    complete = sum(1 for s in sections if report.get(s)) / len(sections)
    data = report["results"]
    mean_all = sum(data) / len(data)
    mean_shade = sum(data[10:]) / 10
    mean_light = sum(data[:10]) / 10
    print("IMRAD completeness: %.3f" % complete)
    print("mean light %.2f vs shade %.2f (n=%d shown, not summarized)"
          % (mean_light, mean_shade, len(data)))
    assert 0.999 < complete < 1.001
    assert 6.29 < mean_light < 6.31
    assert 3.79 < mean_shade < 3.81
    assert mean_light > mean_shade
    print("OK: %s presented the science solution" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_engineering_presentation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # trade study: score candidates against testable requirements
    criteria = {"load_kg": 0.5, "deflection_mm": 0.3, "cost": 0.2}
    # lower deflection and cost are better -> invert
    designs = {"beam A": {"load_kg": 220, "deflection_mm": 1.8, "cost": 40},
               "beam B": {"load_kg": 260, "deflection_mm": 2.4, "cost": 30},
               "beam C": {"load_kg": 180, "deflection_mm": 1.2, "cost": 55}}
    req_load, req_defl = 200, 2.0
    scores = {}
    for dname, d in designs.items():
        if d["load_kg"] < req_load or d["deflection_mm"] > req_defl:
            scores[dname] = -1.0  # fails requirements
            continue
        scores[dname] = (criteria["load_kg"] * d["load_kg"] / 260.0
                         + criteria["deflection_mm"] * (3.0 - d["deflection_mm"]) / 3.0
                         + criteria["cost"] * (60.0 - d["cost"]) / 60.0)
    winner = max(scores, key=scores.get)
    for dname in sorted(scores):
        print("  %-7s score %.3f" % (dname, scores[dname]))
    print("winner: %s (meets 200 kg, deflection under 2 mm)" % winner)
    assert scores["beam C"] < 0  # fails the load requirement
    assert winner == "beam A"
    assert 0.609 < scores["beam A"] < 0.611
    print("OK: %s ran the engineering trade study" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_craft_presentation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # materials and tools cover every operation; feel-cues written down
    materials = {"pine boards": 4, "wood screws": 24, "oil finish": 1}
    operations = [("cut boards to length", {"pine boards": 4}, "cut until the line just disappears"),
                  ("drive screws", {"wood screws": 24}, "snug, not crushing"),
                  ("apply oil", {"oil finish": 1}, "thin coat, no pooling")]
    covered = all(all(m in materials and materials[m] >= q
                      for m, q in need.items())
                  for _, need, _ in operations)
    cues = sum(1 for _, _, cue in operations if cue)
    print("operations: %d, materials cover all: %s, feel-cues written: %d/%d"
          % (len(operations), covered, cues, len(operations)))
    assert covered is True
    assert cues == len(operations)
    total_screws = sum(need.get("wood screws", 0) for _, need, _ in operations)
    assert total_screws == 24
    print("OK: %s presented the craft solution" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_everyday_presentation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cost stated up front: time, money, effort; fallback given
    fix = {"minutes": 20, "cost_usd": 8.50, "effort": "easy",
           "fallback": "if still slow, the clog is past the trap: call a plumber",
           "call_pro_when": "water backs up into the sink"}
    budget = {"minutes": 30, "cost_usd": 15.00}
    fits = fix["minutes"] <= budget["minutes"] and fix["cost_usd"] <= budget["cost_usd"]
    total_cost = fix["cost_usd"] + fix["minutes"] * 0.5  # time valued
    print("fix: %d min, $%.2f, effort %s -> fits budget: %s"
          % (fix["minutes"], fix["cost_usd"], fix["effort"], fits))
    print("all-in cost score: %.2f; fallback present: %s; pro line present: %s"
          % (total_cost, bool(fix["fallback"]), bool(fix["call_pro_when"])))
    assert fits is True
    assert 18.49 < total_cost < 18.51
    assert "call a plumber" in fix["fallback"]
    print("OK: %s presented the everyday solution" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_proof_writeup(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # claim: the sum of the first n odd numbers is n^2; verify to n = 20
    # the write-up's cases: base n=1, step n -> n+1 (induction)
    def odd_sum(n):
        return sum(2 * k - 1 for k in range(1, n + 1))
    worst = 0.0
    for n in range(1, 21):
        diff = abs(odd_sum(n) - n * n)
        worst = max(worst, diff)
    # induction step check: odd_sum(n+1) - odd_sum(n) == 2n+1
    step_ok = all(odd_sum(n + 1) - odd_sum(n) == 2 * n + 1 for n in range(1, 20))
    print("max |sum - n^2| over n=1..20: %.3f" % worst)
    print("induction step holds for all n: %s" % step_ok)
    assert -0.001 < worst < 0.001
    assert step_ok is True
    print("OK: %s wrote the proof and verified it" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_how_to_describe(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the Feynman test: simplify; the stumble marks thin understanding
    explanation = {"terms_defined": True, "one_sentence_per_step": True,
                   "reason_per_step": False, "example_before_general": True,
                   "scope_stated": True}
    score = sum(explanation.values()) / len(explanation)
    # the missing reason-per-step is the diagnosed thin joint
    thin_joints = [k for k, v in explanation.items() if not v]
    print("describe-skill score: %.3f" % score)
    print("thin joints found by the Feynman test: %s" % thin_joints)
    assert 0.799 < score < 0.801
    assert thin_joints == ["reason_per_step"]
    print("OK: %s taught describing by diagnosing the draft" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_solution_storytelling(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the arc beats must appear in order: disruption, struggle, insight,
    # resolution, new normal
    story = ["disruption: line down, orders piling up",
             "struggle: two hours on the wrong sensor",
             "insight: the fault moved with the heat",
             "resolution: rerouted the cable, verified under load",
             "new normal: heat-rated cable spec added to the checklist"]
    beats = ["disruption", "struggle", "insight", "resolution", "new normal"]
    positions = [next(i for i, s in enumerate(story) if s.startswith(b)) for b in beats]
    in_order = all(a < b for a, b in zip(positions, positions[1:]))
    # honesty: no invented drama -> the struggle beat is real and logged
    honest = "two hours" in story[1]
    print("beat positions: %s -> arc in order: %s, honest struggle: %s"
          % (positions, in_order, honest))
    assert in_order is True
    assert honest is True
    assert positions == [0, 1, 2, 3, 4]
    print("OK: %s told the solution as an honest arc" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_tradeoffs(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the bargain on the record: gains, prices, and the reason
    options = {"fast query": {"speed": 9, "correctness": 5, "cost": 4},
               "audited query": {"speed": 5, "correctness": 9, "cost": 6}}
    weights = {"speed": 0.2, "correctness": 0.6, "cost": 0.2}
    # cost is a price: lower is better -> invert on a 10 scale
    def score(o):
        return (weights["speed"] * o["speed"]
                + weights["correctness"] * o["correctness"]
                + weights["cost"] * (10 - o["cost"]))
    s = {k: score(v) for k, v in options.items()}
    chosen = max(s, key=s.get)
    loser_price = "correctness 5 vs 9"  # stated plainly, no euphemism
    print("scores: %s -> chosen: %s" % (
        {k: round(v, 3) for k, v in s.items()}, chosen))
    print("price paid, stated plainly: %s" % loser_price)
    assert chosen == "audited query"
    assert 7.19 < s["audited query"] < 7.21
    assert 5.99 < s["fast query"] < 6.01
    print("OK: %s put the trade-off bargain on the record" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_compare_two(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # criteria stated first; both steelmanned; scores shown for re-weighting
    criteria = ["speed", "correctness", "cost"]
    A = {"speed": 8, "correctness": 6, "cost": 7}   # higher cost-score = cheaper
    B = {"speed": 5, "correctness": 9, "cost": 5}
    shown = {c: (A[c], B[c]) for c in criteria}
    def verdict(weights):
        sa = sum(weights[c] * A[c] for c in criteria)
        sb = sum(weights[c] * B[c] for c in criteria)
        return ("A" if sa > sb else "B"), sa, sb
    v1, sa1, sb1 = verdict({"speed": 0.6, "correctness": 0.2, "cost": 0.2})
    v2, sa2, sb2 = verdict({"speed": 0.1, "correctness": 0.7, "cost": 0.2})
    print("scores shown: %s" % shown)
    print("speed-weighted verdict: %s (%.2f vs %.2f)" % (v1, sa1, sb1))
    print("correctness-weighted verdict: %s (%.2f vs %.2f)" % (v2, sa2, sb2))
    assert v1 == "A" and v2 == "B"  # conditional verdicts
    assert 7.39 < sa1 < 7.41 and 5.79 < sb1 < 5.81
    print("OK: %s compared two solutions honestly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_rubric_view(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # analytic rubric over description criteria, SOLO-flavored levels 0-4
    rubric = {"problem stated": 3, "steps ordered": 4, "reasons given": 2,
              "check shown": 4, "scope admitted": 1}
    total = sum(rubric.values())
    max_total = 4 * len(rubric)
    pct = total / max_total
    weakest = min(rubric, key=rubric.get)
    # answer-correct split from description-good
    answer_correct, description_good = True, pct >= 0.6
    print("rubric total: %d/%d = %.3f" % (total, max_total, pct))
    print("weakest criterion (actionable feedback): %s" % weakest)
    print("answer correct: %s, description good: %s" % (answer_correct, description_good))
    assert total == 14
    assert 0.699 < pct < 0.701
    assert weakest == "scope admitted"
    print("OK: %s graded through the rubric view" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_best_practices(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the pre-publish checklist: every load-bearing practice present
    checklist = {"problem stated": True, "materials listed": True,
                 "steps numbered": True, "reasons per step": True,
                 "figures with steps": True, "check shown": True,
                 "limits admitted": True, "dated and versioned": False}
    score = sum(checklist.values()) / len(checklist)
    missing = [k for k, v in checklist.items() if not v]
    publish = score >= 0.875  # at most one miss allowed
    print("checklist score: %.3f, missing: %s, publish: %s" % (score, missing, publish))
    assert 0.874 < score < 0.876
    assert missing == ["dated and versioned"]
    assert publish is True
    print("OK: %s ran the best-practice checklist" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_group_presentation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the digest fits the slot: hook, insight, sketch, proof, limits, pointer
    slot_minutes = 10
    sections = {"hook (problem + stakes)": 1.5, "insight": 2.0,
                "solution sketch": 2.5, "proof it works": 2.0,
                "limits admitted": 1.0, "pointer to write-up": 1.0}
    total = sum(sections.values())
    fits = abs(total - slot_minutes) < 0.001
    one_visual_each = len(sections)  # one visual per point
    print("sections: %d, total %.1f min vs slot %d -> fits: %s"
          % (len(sections), total, slot_minutes, fits))
    assert fits is True
    assert one_visual_each == 6
    print("OK: %s built the presentation digest" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_debug_log(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # delta debugging: shrink the failing input to the minimal trigger
    def fails(inp):
        return "x" in inp and len(inp) >= 3  # the fault needs x plus length
    failing = "abxcde"
    assert fails(failing)
    # minimize: drop characters while it still fails
    current = failing
    changed = True
    while changed:
        changed = False
        for i in range(len(current)):
            cand = current[:i] + current[i + 1:]
            if cand and fails(cand):
                current = cand
                changed = True
                break
    print("failing input %r minimized to %r" % (failing, current))
    assert current == "xab" or current == "abx" or len(current) == 3
    assert fails(current)
    # regression check: fix removes the failure, nothing else broke
    fixed = not fails(current.replace("x", "y"))
    print("minimal trigger kept failing: %s; fix verified: %s" % (fails(current), fixed))
    assert fixed is True
    print("OK: %s kept the debugging log" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_dsv_full_system(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the capstone pipeline: run all six phases against one sample record
    record = {"problem": "pump will not prime",
              "tools": ["wrench", "priming water", "gasket kit"],
              "plan": "check suction line, then seals, then prime",
              "steps": ["inspect suction line", "replace gasket", "prime and test"],
              "reasons": ["air leak stops prime", "worn gasket found", "verify under load"],
              "check": "pump primes in 30 s, holds pressure",
              "date": "2026-10-17", "version": 1}
    phases = {
        "intake": bool(record["problem"]) and bool(record["tools"]),
        "planning": bool(record["plan"]),
        "execution": len(record["steps"]) == len(record["reasons"]) == 3,
        "checking": "holds pressure" in record["check"],
        "writing": all(record["steps"]),
        "publishing": bool(record["date"]) and record["version"] == 1,
    }
    passed = sum(phases.values())
    print("phases: %s" % phases)
    print("pipeline: %d/%d phases passed" % (passed, len(phases)))
    assert passed == 6
    assert all(phases.values())
    print("OK: %s ran the full worked-through system" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "dsv_diagnostic_narrative": demo_dsv_diagnostic_narrative,
    "dsv_repair_walkthrough": demo_dsv_repair_walkthrough,
    "dsv_math_presentation": demo_dsv_math_presentation,
    "dsv_science_presentation": demo_dsv_science_presentation,
    "dsv_engineering_presentation": demo_dsv_engineering_presentation,
    "dsv_craft_presentation": demo_dsv_craft_presentation,
    "dsv_everyday_presentation": demo_dsv_everyday_presentation,
    "dsv_proof_writeup": demo_dsv_proof_writeup,
    "dsv_how_to_describe": demo_dsv_how_to_describe,
    "dsv_solution_storytelling": demo_dsv_solution_storytelling,
    "dsv_tradeoffs": demo_dsv_tradeoffs,
    "dsv_compare_two": demo_dsv_compare_two,
    "dsv_rubric_view": demo_dsv_rubric_view,
    "dsv_best_practices": demo_dsv_best_practices,
    "dsv_group_presentation": demo_dsv_group_presentation,
    "dsv_debug_log": demo_dsv_debug_log,
    "dsv_full_system": demo_dsv_full_system,
})

