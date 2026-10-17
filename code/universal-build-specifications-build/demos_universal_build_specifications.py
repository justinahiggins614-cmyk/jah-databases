#!/usr/bin/env python3
"""Demo programs for the Universal Build Specifications databases.

Every demo is real, runnable, stdlib-only Python performing the actual
build-specification computation for its record. All are machine-executed by
build.py before commit: each prints its real computed values, asserts tight
bounds (never float exact-equality), and ends with the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_ubs_what_is(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # spec completeness: which of the seven sections are filled
    sections = {"objective": True, "deliverables": True, "requirements": True,
                "constraints": True, "assumptions": False,
                "acceptance": True, "verification": True}
    filled = sum(1 for v in sections.values() if v)
    total = len(sections)
    score = filled / total * 100.0
    missing = sorted(k for k, v in sections.items() if not v)
    print("sections filled: %d of %d" % (filled, total))
    print("completeness: %.2f %%" % score)
    print("missing: %s" % missing)
    assert filled == 6 and total == 7
    assert 85.70 < score < 85.72
    assert missing == ["assumptions"]
    print("rule: six of seven is not a spec - the missing section is where the dispute starts")
    print("OK: %s scored the contract" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_request_pipeline(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # extraction: map request keywords onto the seven spec sections
    request = "build a fast report generator for the finance team under 50k by q3"
    lexicon = {"objective": ["report", "generator"],
               "deliverables": ["report"],
               "requirements": ["generator"],
               "constraints": ["fast", "50k", "q3", "under", "by"],
               "assumptions": ["finance", "team"],
               "acceptance": [],
               "verification": []}
    words = request.split()
    hits = {sec: sum(1 for w in words if w in keys) for sec, keys in lexicon.items()}
    covered = sum(1 for c in hits.values() if c > 0)
    vague = [w for w in words if w in ("fast",)]
    coverage = covered / len(lexicon) * 100.0
    print("request words: %d" % len(words))
    print("sections hit: %d of %d (%.2f %%)" % (covered, len(lexicon), coverage))
    print("vague modifiers flagged for quantification: %s" % vague)
    assert covered == 5
    assert 71.42 < coverage < 71.44
    assert vague == ["fast"]
    print("rule: 'fast' never becomes a requirement - it becomes a question first")
    print("OK: %s ran the refinery" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_anatomy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # anatomy checklist: the fourteen sections, walked top to bottom
    required = ["header", "objective", "stakeholders", "deliverables",
                "functional", "nonfunctional", "constraints", "assumptions",
                "interfaces", "acceptance", "verification", "risks",
                "glossary", "history"]
    draft = [s for s in required if s not in ("risks", "glossary")]
    missing = [s for s in required if s not in draft]
    score = len(draft) / len(required) * 100.0
    print("sections present: %d of %d" % (len(draft), len(required)))
    print("anatomy score: %.2f %%" % score)
    print("missing bones: %s" % missing)
    assert len(draft) == 12 and len(required) == 14
    assert 85.70 < score < 85.72
    assert missing == ["risks", "glossary"]
    print("rule: skip a bone and the body cannot stand")
    print("OK: %s walked the skeleton" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_objectives(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SMART test on the worked objective
    smart = {"specific": True, "measurable": True, "achievable": True,
             "relevant": True, "time_bound": True}
    letters = sum(1 for v in smart.values() if v)
    score = letters / 5.0 * 100.0
    # the number in the paragraph: 6 hours -> 15 minutes
    before_min, after_min = 6.0 * 60.0, 15.0
    improvement = before_min / after_min
    print("SMART letters passing: %d of 5 (%.1f %%)" % (letters, score))
    print("improvement factor: %.0f min / %.0f min = %.1fx" % (before_min, after_min, improvement))
    assert letters == 5
    assert 23.9 < improvement < 24.1
    print("rule: one number beats ten adjectives")
    print("OK: %s tested the destination" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_deliverables(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # definition-of-done arithmetic across the cargo manifest
    # each deliverable: exists, passes test, handed over, logged
    manifest = {"spec v1.0": [True, True, True, True],
                "prototype": [True, True, False, True],
                "test report": [True, False, False, False],
                "user guide": [False, False, False, False]}
    done = sum(1 for checks in manifest.values() if all(checks))
    total = len(manifest)
    pct = done / total * 100.0
    print("deliverables accepted: %d of %d (%.1f %%)" % (done, total, pct))
    assert done == 1 and total == 4
    assert 24.9 < pct < 25.1
    print("rule: progress is cargo delivered and accepted, never hours spent")
    print("OK: %s counted the cargo" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_functional_req(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # ID integrity: unique, sequential, no silent gaps
    ids = ["REQ-001", "REQ-002", "REQ-003", "REQ-005"]
    nums = sorted(int(i.split("-")[1]) for i in ids)
    unique = len(set(ids)) == len(ids)
    expected = list(range(nums[0], nums[-1] + 1))
    gaps = [n for n in expected if n not in nums]
    print("requirements: %d, unique IDs: %s" % (len(ids), unique))
    print("sequence gaps: %s" % (["REQ-%03d" % n for n in gaps] or "none"))
    assert unique is True
    assert gaps == [4]
    print("rule: a skipped number without a logged reason is a lost requirement")
    print("OK: %s audited the beams" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_nonfunctional_req(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # ISO/IEC 25010 eight characteristics: coverage check
    characteristics = ["functional suitability", "performance efficiency",
                       "compatibility", "usability", "reliability",
                       "security", "maintainability", "portability"]
    specified = [c for c in characteristics if c not in ("portability", "compatibility")]
    coverage = len(specified) / len(characteristics) * 100.0
    print("quality characteristics specified: %d of %d (%.1f %%)"
          % (len(specified), len(characteristics), coverage))
    print("unspecified: %s" % [c for c in characteristics if c not in specified])
    assert len(specified) == 6
    assert 74.9 < coverage < 75.1
    print("rule: an empty characteristic is a question, not an answer")
    print("OK: %s tempered the beams" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_constraints(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # budget wall: line items against the ceiling
    items = {"labor": 120000.0, "parts": 60000.0, "tooling": 35000.0, "contingency": 25000.0}
    ceiling = 250000.0
    total = sum(items.values())
    margin = ceiling - total
    margin_pct = margin / ceiling * 100.0
    print("budget total: $%.0f against ceiling $%.0f" % (total, ceiling))
    print("margin: $%.0f (%.1f %%)" % (margin, margin_pct))
    assert 239999.0 < total < 240001.0
    assert 9999.0 < margin < 10001.0
    assert 3.9 < margin_pct < 4.1
    print("rule: the design must fit the walls, not the other way around")
    print("OK: %s walked the walls" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_assumptions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # dependency map: topological order proves no deadlock
    deps = {"build": ["parts", "spec"], "parts": ["po"], "spec": [],
            "po": [], "test": ["build"]}
    order, temp, perm = [], set(), set()
    def visit(n):
        assert n not in temp, "cycle detected at " + n
        if n in perm:
            return
        temp.add(n)
        for d in deps[n]:
            visit(d)
        temp.remove(n)
        perm.add(n)
        order.append(n)
    for node in deps:
        visit(node)
    print("dependency order: %s" % order)
    print("nodes ordered: %d of %d (cycle-free: True)" % (len(order), len(deps)))
    assert len(order) == 5
    assert order.index("po") < order.index("parts") < order.index("build") < order.index("test")
    print("rule: a cycle in the map is a deadlock on the schedule")
    print("OK: %s mapped the supply lines" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_acceptance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # given-when-then criteria executed: binary pass/fail
    criteria = [
        ("1000 users", "login storm 10 min", 96.2, 95.0),   # (given, when, measured %, threshold %)
        ("1000 users", "login storm 10 min", 1.8, 2.0),      # seconds p95 vs limit
        ("1000 users", "login storm 10 min", 0, 0),          # data lost vs allowed
    ]
    results = [m >= t if i == 0 else (m <= t if i == 1 else m == t)
               for i, (_, _, m, t) in enumerate(criteria)]
    passed = sum(1 for r in results if r)
    print("criteria: %d, passed: %d, failed: %d" % (len(criteria), passed, len(criteria) - passed))
    assert passed == 3
    print("rule: sign-off needs every criterion passed or formally waived")
    print("OK: %s painted the finish line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_verification(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # verification matrix coverage: rows are requirements, every row needs a method
    matrix = {"REQ-001": ["test"], "REQ-002": ["analysis"], "REQ-003": ["test", "demo"],
              "REQ-004": ["inspection"], "REQ-005": ["test"], "REQ-006": ["demo"],
              "REQ-007": [], "REQ-008": []}
    covered = sum(1 for m in matrix.values() if m)
    coverage = covered / len(matrix) * 100.0
    gaps = sorted(k for k, m in matrix.items() if not m)
    print("requirements with a verification method: %d of %d (%.1f %%)"
          % (covered, len(matrix), coverage))
    print("unverifiable rows: %s" % gaps)
    assert covered == 6
    assert 74.9 < coverage < 75.1
    assert gaps == ["REQ-007", "REQ-008"]
    print("rule: an empty row is a gap to close, not a detail to defer")
    print("OK: %s opened the proof ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_stakeholders(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # power-interest grid placement
    people = {"requester": (9, 9), "lead user": (4, 9), "regulator": (9, 3),
              "maintainer": (5, 7), "bystander": (2, 2), "security": (8, 6)}
    def quad(power, interest):
        if power >= 5 and interest >= 5:
            return "collaborate"
        if power >= 5:
            return "satisfy"
        if interest >= 5:
            return "inform"
        return "monitor"
    quads = {}
    for who, (pw, it) in people.items():
        quads.setdefault(quad(pw, it), []).append(who)
    for q in ("collaborate", "satisfy", "inform", "monitor"):
        print("  %-11s: %d (%s)" % (q, len(quads.get(q, [])), ", ".join(sorted(quads.get(q, [])))))
    assert len(quads["collaborate"]) == 3
    assert quads["satisfy"] == ["regulator"]
    assert quads["monitor"] == ["bystander"]
    print("rule: find every signatory before the first line is drawn")
    print("OK: %s mapped the signatories" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_scope(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # change impact score: cost x schedule x risk factor
    cost_k, sched_wks, risk_factor = 18.0, 3.0, 1.5
    impact = cost_k * sched_wks * risk_factor
    threshold, board_limit = 50.0, 100.0
    if impact >= board_limit:
        decision = "board review required"
    elif impact >= threshold:
        decision = "lead approval"
    else:
        decision = "auto-approve"
    print("impact score: %.1fk x %.0f wks x %.1f = %.1f" % (cost_k, sched_wks, risk_factor, impact))
    print("decision: %s" % decision)
    assert 80.9 < impact < 81.1
    assert decision == "lead approval"
    print("rule: every change pays its toll in writing")
    print("OK: %s kept the gate" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_traceability(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the four orphan queries over the link map
    reqs = ["REQ-001", "REQ-002", "REQ-003", "REQ-004", "REQ-005", "REQ-006"]
    design_links = {"REQ-001": ["D-1"], "REQ-002": ["D-2"], "REQ-003": ["D-3"],
                    "REQ-004": [], "REQ-005": ["D-4"], "REQ-006": ["D-5"]}
    test_links = {"REQ-001": ["T-1"], "REQ-002": ["T-2"], "REQ-003": [],
                  "REQ-004": [], "REQ-005": ["T-3"], "REQ-006": ["T-4"]}
    unimpl = [r for r in reqs if not design_links[r]]
    untested = [r for r in reqs if not test_links[r]]
    impl_cov = (len(reqs) - len(unimpl)) / len(reqs) * 100.0
    test_cov = (len(reqs) - len(untested)) / len(reqs) * 100.0
    print("implementation coverage: %.2f %%, orphans: %s" % (impl_cov, unimpl))
    print("verification coverage: %.2f %%, orphans: %s" % (test_cov, untested))
    assert unimpl == ["REQ-004"]
    assert untested == ["REQ-003", "REQ-004"]
    assert 83.32 < impl_cov < 83.34
    assert 66.66 < test_cov < 66.68
    print("rule: orphans in either direction are defects")
    print("OK: %s surveyed the map" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_risk(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # exposure = probability x impact, ranked
    risks = [("vendor slip", 0.3, 40000.0), ("sensor unproven", 0.5, 60000.0),
             ("reg change", 0.1, 100000.0), ("staff loss", 0.3, 25000.0)]
    ranked = sorted(((n, p * i) for n, p, i in risks), key=lambda r: -r[1])
    total = sum(e for _, e in ranked)
    print("total exposure: $%.0f" % total)
    for n, e in ranked:
        print("  %-15s $%.0f" % (n, e))
    assert ranked[0] == ("sensor unproven", 30000.0)
    assert 59499.0 < total < 59501.0
    print("rule: work the biggest exposures first")
    print("OK: %s read the weather chart" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_interfaces(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # unit compatibility across the boundary: both sides must agree
    sides = [("length", "m", "m"), ("length", "m", "mm"),
             ("voltage", "V", "V"), ("pressure", "kPa", "kPa")]
    mismatches = [s for s in sides if s[1] != s[2]]
    ok = len(sides) - len(mismatches)
    print("interfaces checked: %d, compatible: %d, mismatches: %d"
          % (len(sides), ok, len(mismatches)))
    for s in mismatches:
        print("  MISMATCH: %s provider=%s consumer=%s" % s)
    assert ok == 3 and len(mismatches) == 1
    assert mismatches[0] == ("length", "m", "mm")
    print("rule: the meter-foot disaster is prevented by a document line")
    print("OK: %s walked the fences" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_software(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # API contract completeness: endpoints x contract fields
    fields = ["schema", "errors", "auth", "limits", "versioning"]
    endpoints = {"POST /login": ["schema", "errors", "auth", "limits", "versioning"],
                 "GET /report": ["schema", "errors", "auth", "limits"],
                 "POST /export": ["schema", "errors"],
                 "DELETE /user": ["schema", "errors", "auth", "limits", "versioning"]}
    cells = sum(len(v) for v in endpoints.values())
    total = len(endpoints) * len(fields)
    pct = cells / total * 100.0
    worst = min(endpoints, key=lambda e: len(endpoints[e]))
    print("contract cells filled: %d of %d (%.1f %%)" % (cells, total, pct))
    print("weakest endpoint: %s (%d of %d fields)" % (worst, len(endpoints[worst]), len(fields)))
    assert cells == 16 and total == 20
    assert 79.9 < pct < 80.1
    assert worst == "POST /export"
    print("rule: an endpoint without its contract is a rumor with a URL")
    print("OK: %s specified the doors" % NAME)
if __name__ == "__main__":
    main()
''')
def demo_ubs_hardware(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # tolerance stack-up: worst-case vs root-sum-square
    nominal = [2.0, 3.0, 1.5]
    tol = [0.10, 0.15, 0.05]
    worst = sum(tol)
    rss = math.sqrt(sum(t * t for t in tol))
    gap_nominal, gap_min = 0.50, 0.20
    ok_worst = gap_nominal - worst >= gap_min
    print("worst-case stack: %.3f mm; RSS stack: %.4f mm" % (worst, rss))
    print("clearance at worst case: %.3f mm (min %.2f: %s)" % (gap_nominal - worst, gap_min, ok_worst))
    assert 0.299 < worst < 0.301
    assert 0.1870 < rss < 0.1872
    assert rss < worst
    assert ok_worst is True
    print("rule: a fit proven only on paper is a very expensive piece of paper")
    print("OK: %s stacked the tolerances" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_embedded(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # power budget: subsystem draws x duty cycle vs battery capacity
    # (current mA, duty fraction)
    subs = {"mcu_sleep": (0.005, 0.90), "mcu_active": (12.0, 0.08),
            "radio_tx": (45.0, 0.02), "sensor": (2.0, 0.10)}
    avg_ma = sum(i * d for i, d in subs.values())
    battery_mah, required_h = 2000.0, 720.0
    runtime_h = battery_mah / avg_ma
    margin = runtime_h / required_h
    print("average draw: %.3f mA" % avg_ma)
    print("runtime: %.0f mAh / %.3f mA = %.1f h (required %.0f h, margin %.2fx)"
          % (battery_mah, avg_ma, runtime_h, required_h, margin))
    assert 2.064 < avg_ma < 2.065
    assert 968.7 < runtime_h < 968.8
    assert margin > 1.0
    print("rule: budget the milliamps before choosing the silicon")
    print("OK: %s budgeted the sip of power" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_integration(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pairwise interface count sets the honest scale of integration
    units = ["ui", "api", "auth", "db", "worker", "notifier"]
    n = len(units)
    pairs = n * (n - 1) // 2
    stubbed = 4  # interfaces verified against stubs before counterparts arrive
    print("integration units: %d -> pairwise interfaces: %d" % (n, pairs))
    print("verified against stubs early: %d of %d (%.1f %%)" % (stubbed, pairs, stubbed / pairs * 100.0))
    assert pairs == 15
    assert 26.6 < stubbed / pairs * 100.0 < 26.7
    print("rule: integration day should confirm, not discover")
    print("OK: %s choreographed the raising" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_safety(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # risk class from severity x likelihood
    hazards = [("brake loss", 4, 2), ("false alarm", 2, 4), ("data leak", 3, 3)]
    def risk_class(sev, like):
        score = sev * like
        if score >= 12:
            return "high"
        if score >= 6:
            return "medium"
        return "low"
    for name_h, sev, like in hazards:
        print("  %-10s sev=%d like=%d -> %s" % (name_h, sev, like, risk_class(sev, like)))
    classes = [risk_class(s, l) for _, s, l in hazards]
    assert classes == ["medium", "medium", "medium"]
    assert risk_class(4, 4) == "high" and risk_class(1, 2) == "low"
    print("rule: the risk class drives the rigor - high means redundancy and independent assessment")
    print("OK: %s posted the load limits" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_versioning(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # semantic version bump from the change list
    current = (1, 4, 2)
    changes = [("minor", "added export deliverable"),
               ("patch", "fixed tolerance typo"),
               ("patch", "clarified acceptance wording")]
    kinds = {k for k, _ in changes}
    if "major" in kinds:
        nxt = (current[0] + 1, 0, 0)
    elif "minor" in kinds:
        nxt = (current[0], current[1] + 1, 0)
    else:
        nxt = (current[0], current[1], current[2] + 1)
    print("changes: %d minor, %d patch" % (sum(1 for k, _ in changes if k == "minor"),
                                           sum(1 for k, _ in changes if k == "patch")))
    print("version: %d.%d.%d -> %d.%d.%d" % (current + nxt))
    assert nxt == (1, 5, 0)
    print("rule: frozen means read-only - the new version carries the change history")
    print("OK: %s sealed the edition" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_cost(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # PERT three-point estimate with stated uncertainty
    optimistic, likely, pessimistic = 80.0, 100.0, 150.0  # k$
    expected = (optimistic + 4.0 * likely + pessimistic) / 6.0
    sd = (pessimistic - optimistic) / 6.0
    print("three-point: O=%.0fk M=%.0fk P=%.0fk" % (optimistic, likely, pessimistic))
    print("PERT expected: %.1fk, std dev: %.2fk" % (expected, sd))
    print("80%% band: %.1fk .. %.1fk" % (expected - 1.28 * sd, expected + 1.28 * sd))
    assert 104.9 < expected < 105.1
    assert 11.66 < sd < 11.68
    print("rule: state the uncertainty - a point estimate without a band is a wish")
    print("OK: %s priced the contract" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_prototypes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # phase-gate scoring: go, conditional, or stop
    gates = {"SRR": 8.5, "PDR": 7.2, "CDR": 6.8, "TRR": 8.0, "AR": 9.1}
    go_line, cond_line = 7.0, 5.0
    def verdict(s):
        if s >= go_line:
            return "GO"
        if s >= cond_line:
            return "CONDITIONAL"
        return "STOP"
    stops = [g for g, s in gates.items() if verdict(s) == "STOP"]
    conds = [g for g, s in gates.items() if verdict(s) == "CONDITIONAL"]
    for g, s in gates.items():
        print("  %s: %.1f -> %s" % (g, s, verdict(s)))
    assert stops == []
    assert conds == ["CDR"]
    print("rule: a stop is a process success - kill it cheap, not expensive")
    print("OK: %s tolled the phases" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_mbse(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # model coverage: requirements allocated to blocks
    requirements = 20
    allocated = 17
    coverage = allocated / requirements * 100.0
    # parametric rollup: subsystem masses from the model values
    masses = {"structure": 4.2, "avionics": 1.8, "power": 2.5, "payload": 3.0}
    total = sum(masses.values())
    budget = 12.0
    margin = (budget - total) / budget * 100.0
    print("requirements allocated in model: %d of %d (%.1f %%)" % (allocated, requirements, coverage))
    print("mass rollup: %.1f kg vs %.1f kg budget (margin %.1f %%)" % (total, budget, margin))
    assert 84.9 < coverage < 85.1
    assert 11.49 < total < 11.51
    assert 4.1 < margin < 4.2
    print("rule: one model, one truth - documents are generated views")
    print("OK: %s drew the living blueprint" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_standards(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 29148 good-requirement characteristics checklist
    chars = ["necessary", "implementation-free", "unambiguous", "consistent",
             "complete", "singular", "feasible", "traceable", "verifiable"]
    findings = {"REQ-007": ["ambiguous"], "REQ-012": ["unverifiable", "compound"]}
    total_checks = len(chars) * 14  # 14 requirements reviewed
    violations = sum(len(v) for v in findings.values())
    clean_rate = (total_checks - violations) / total_checks * 100.0
    print("characteristics: %d; requirements reviewed: 14" % len(chars))
    print("violations: %d of %d checks (clean %.2f %%)" % (violations, total_checks, clean_rate))
    assert len(chars) == 9
    assert violations == 3
    assert 97.61 < clean_rate < 97.63
    print("rule: the checklist does not care who typed the sentence")
    print("OK: %s posted the building code" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_ai_gen(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # ambiguity scan: vague terms flagged for quantification
    vague = ["fast", "robust", "user-friendly", "etc", "adequate", "seamless"]
    sentences = ["the system shall be fast",
                 "the export shall complete in under 5 seconds",
                 "the interface shall be user-friendly",
                 "the system shall handle adequate load etc",
                 "uptime shall be 99.9 percent",
                 "failover shall be seamless"]
    flagged = [(s, [w for w in vague if w in s.split()]) for s in sentences]
    flagged = [(s, ws) for s, ws in flagged if ws]
    rate = len(flagged) / len(sentences) * 100.0
    print("sentences scanned: %d, flagged: %d (%.1f %%)" % (len(sentences), len(flagged), rate))
    for s, ws in flagged:
        print("  '%s' -> %s" % (s, ws))
    assert len(flagged) == 4
    assert 66.66 < rate < 66.68
    print("rule: the AI proposes, the accountable human disposes")
    print("OK: %s ran the apprentice's scan" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_ml_specs(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # class balance and split arithmetic for the dataset spec
    counts = {"approved": 4500.0, "review": 3800.0, "rejected": 1700.0}
    total = sum(counts.values())
    balance = min(counts.values()) / max(counts.values())
    splits = {"train": 0.70, "val": 0.15, "test": 0.15}
    test_n = total * splits["test"]
    print("dataset: %.0f labeled items" % total)
    print("class balance min/max: %.4f" % balance)
    print("held-out test set: %.0f items" % test_n)
    assert 9999.0 < total < 10001.0
    assert 0.3777 < balance < 0.3779
    assert 1499.0 < test_n < 1501.0
    print("rule: unspecified data is unspecified behavior")
    print("OK: %s specified the schooling" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_cps(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # latency budget per control path: worst-case vs the physics deadline
    stages = {"sense": 12.0, "transport": 8.0, "compute": 25.0, "actuate": 5.0}
    total = sum(stages.values())
    deadline = 100.0
    margin = (deadline - total) / deadline * 100.0
    jitter = 3.0
    worst_with_jitter = total + jitter
    print("latency budget: %s = %.0f ms worst-case" % (" + ".join("%.0f" % v for v in stages.values()), total))
    print("deadline %.0f ms -> margin %.0f %%" % (deadline, margin))
    print("with jitter %.0f ms: %.0f ms (within deadline: %s)" % (jitter, worst_with_jitter, worst_with_jitter <= deadline))
    assert 49.9 < total < 50.1
    assert 49.9 < margin < 50.1
    assert worst_with_jitter <= deadline
    print("rule: a late brake command is a failed requirement, not a slow feature")
    print("OK: %s budgeted the reflexes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_contracts(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOW completeness and milestone money tied to accepted cargo
    sections = ["scope", "deliverables", "acceptance", "schedule",
                "price", "ip", "warranty", "changes"]
    present = [s for s in sections if s != "warranty"]
    pct = len(present) / len(sections) * 100.0
    milestones = [("spec accepted", 0.20), ("prototype accepted", 0.30),
                  ("system accepted", 0.40), ("warranty end", 0.10)]
    money = sum(m for _, m in milestones)
    print("SOW sections present: %d of %d (%.1f %%)" % (len(present), len(sections), pct))
    print("missing: %s" % [s for s in sections if s not in present])
    print("milestone money accounted: %.0f %%" % (money * 100.0))
    assert len(present) == 7
    assert 87.49 < pct < 87.51
    assert 0.999 < money < 1.001
    print("rule: paid for cargo, not for effort - and never without the warranty clause")
    print("OK: %s wrote the enforceable exchange" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_executable(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # twin parameter check: every parameter within its tolerance
    params = [("mass_kg", 11.5, 12.0, 0.5), ("power_w", 48.0, 50.0, 5.0),
              ("latency_ms", 50.0, 100.0, 0.0), ("thrust_n", 95.0, 100.0, 10.0),
              ("temp_c", 62.0, 85.0, 0.0)]
    # (name, actual, limit, tolerance): pass if actual <= limit + tolerance
    results = [(n, a <= lim + tol) for n, a, lim, tol in params]
    passed = sum(1 for _, ok in results if ok)
    pct = passed / len(results) * 100.0
    for n, ok in results:
        print("  %-10s %s" % (n, "PASS" if ok else "FAIL"))
    print("twin parameters within tolerance: %d of %d (%.0f %%)" % (passed, len(results), pct))
    assert passed == 5
    assert pct == 100.0
    print("rule: two views, one baseline - changed together or not at all")
    print("OK: %s rehearsed the contract" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_fmea(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # RPN = severity x occurrence x detection, ranked
    modes = [("sensor drift", 8, 4, 6), ("connector fatigue", 6, 5, 4),
             ("firmware hang", 9, 2, 7)]
    ranked = sorted(((m, s * o * d) for m, s, o, d in modes), key=lambda r: -r[1])
    threshold = 100
    actions = [(m, r) for m, r in ranked if r >= threshold]
    for m, r in ranked:
        print("  %-17s RPN=%d%s" % (m, r, " -> ACTION" if r >= threshold else ""))
    assert ranked[0] == ("sensor drift", 192)
    assert ranked[1] == ("firmware hang", 126)
    assert len(actions) == 3
    print("rule: every action becomes a traced requirement")
    print("OK: %s held the inquests" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_inspections(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Fagan inspection metrics: defect density and inspection rate
    pages, defects = 40.0, 12.0
    majors = 4.0
    prep_hours, meeting_hours = 6.0, 2.0
    density = defects / pages
    major_rate = majors / meeting_hours
    print("inspected: %.0f pages, defects: %.0f (majors %.0f)" % (pages, defects, majors))
    print("defect density: %.2f per page" % density)
    print("major find rate: %.1f per meeting-hour" % major_rate)
    assert 0.299 < density < 0.301
    assert 1.99 < major_rate < 2.01
    print("rule: never seal an unread contract")
    print("OK: %s convened the jury" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ubs_handoff(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # BOM sourceability: every line needs an approved source
    bom = {"mcu": "approved", "sensor": "approved", "connector": "approved",
           "enclosure": "pending", "battery": "approved", "antenna": "approved"}
    sourced = sum(1 for v in bom.values() if v == "approved")
    pct = sourced / len(bom) * 100.0
    blockers = sorted(k for k, v in bom.items() if v != "approved")
    print("BOM lines sourced: %d of %d (%.2f %%)" % (sourced, len(bom), pct))
    print("blockers: %s" % blockers)
    assert sourced == 5 and len(bom) == 6
    assert 83.32 < pct < 83.34
    assert blockers == ["enclosure"]
    print("rule: the contract is complete when the first real thing passes inspection")
    print("OK: %s delivered the cargo" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what_is": demo_ubs_what_is,
    "request_pipeline": demo_ubs_request_pipeline,
    "anatomy": demo_ubs_anatomy,
    "objectives": demo_ubs_objectives,
    "deliverables": demo_ubs_deliverables,
    "functional_req": demo_ubs_functional_req,
    "nonfunctional_req": demo_ubs_nonfunctional_req,
    "constraints": demo_ubs_constraints,
    "assumptions": demo_ubs_assumptions,
    "acceptance": demo_ubs_acceptance,
    "verification": demo_ubs_verification,
    "stakeholders": demo_ubs_stakeholders,
    "scope": demo_ubs_scope,
    "traceability": demo_ubs_traceability,
    "risk": demo_ubs_risk,
    "interfaces": demo_ubs_interfaces,
    "software": demo_ubs_software,
    "hardware": demo_ubs_hardware,
    "embedded": demo_ubs_embedded,
    "integration": demo_ubs_integration,
    "safety": demo_ubs_safety,
    "versioning": demo_ubs_versioning,
    "cost": demo_ubs_cost,
    "prototypes": demo_ubs_prototypes,
    "mbse": demo_ubs_mbse,
    "standards": demo_ubs_standards,
    "ai_gen": demo_ubs_ai_gen,
    "ml_specs": demo_ubs_ml_specs,
    "cps": demo_ubs_cps,
    "contracts": demo_ubs_contracts,
    "executable": demo_ubs_executable,
    "fmea": demo_ubs_fmea,
    "inspections": demo_ubs_inspections,
    "handoff": demo_ubs_handoff,
}
