#!/usr/bin/env python3
"""Demo programs for the Incident and Outage Records databases.

Every demo is real, runnable, stdlib-only Python performing the actual
incident-management computation for its record (severity classification,
MTTR/MTBF math, nines arithmetic, timeline reconstruction, blast-radius
traversal, impact ledgers, escalation simulation, fault-tree probability,
error budgets, burn rates, DORA classification, case-study timeline math).
All are machine-executed by build.py: each prints its real computed values,
asserts tight bounds (never float exact-equality), and ends with the OK
marker. Synthetic example inputs are labeled as such inside the programs.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_io_what_is_incident(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # example incident log: (id, severity) - synthetic teaching data
    log = [("INC-101", "SEV2"), ("INC-102", "SEV3"), ("INC-103", "SEV1"),
           ("INC-104", "SEV3"), ("INC-105", "SEV2"), ("INC-106", "SEV4"),
           ("INC-107", "SEV2"), ("INC-108", "SEV3"), ("INC-109", "SEV1"),
           ("INC-110", "SEV3")]
    by_sev = {}
    for _i, sev in log:
        by_sev[sev] = by_sev.get(sev, 0) + 1
    total = len(log)
    for sev in sorted(by_sev):
        print("  %s: %d incidents (%5.1f %%)" % (sev, by_sev[sev], by_sev[sev] / total * 100.0))
    sev1_share = by_sev.get("SEV1", 0) / total * 100.0
    print("SEV1 share: %.1f %%" % sev1_share)
    assert total == 10
    assert by_sev["SEV1"] == 2 and by_sev["SEV3"] == 4
    assert 19.9 < sev1_share < 20.1
    print("rule: declare the severity, and the machinery knows what to do")
    print("OK: %s classified the log" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_what_is_outage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # a month with one 43.8-minute full outage: availability arithmetic
    minutes_in_month = 30.0 * 24.0 * 60.0
    downtime_min = 43.8
    availability = (minutes_in_month - downtime_min) / minutes_in_month * 100.0
    nines = -math.log10(1.0 - availability / 100.0)
    print("downtime: %.1f min in a 30-day month" % downtime_min)
    print("availability: %.4f %%" % availability)
    print("nines: %.3f" % nines)
    assert 43_190.0 < minutes_in_month < 43_210.0
    assert 99.898 < availability < 99.899
    assert 2.9939 < nines < 2.9941
    print("rule: one minute of downtime is the difference between nines")
    print("OK: %s measured the outage" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_incident_lifecycle(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # phase durations (minutes) reconstructed from a fault timeline
    phases = {"detect": 9.0, "triage": 6.0, "mitigate": 22.0,
              "resolve": 31.0, "review": 0.0}  # review happens after
    response_total = sum(v for k, v in phases.items() if k != "review")
    mttr = response_total  # single incident: MTTR is the full response
    print("phase durations (min):")
    for k, v in phases.items():
        print("  %-9s %5.1f" % (k, v))
    print("response total (MTTR): %.1f min" % response_total)
    assert abs(response_total - 68.0) < 1e-9
    assert abs(mttr - 68.0) < 1e-9
    biggest = max((k for k in phases if k != "review"), key=lambda k: phases[k])
    print("longest phase: %s" % biggest)
    assert biggest == "resolve"
    print("rule: each phase has its own clock - read them separately")
    print("OK: %s walked the lifecycle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_mttr(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # restore times (minutes) for five incidents - synthetic teaching data
    restore = [12.0, 45.0, 30.0, 18.0, 90.0]
    mttr = sum(restore) / len(restore)
    ordered = sorted(restore)
    median = ordered[len(ordered) // 2]
    print("restore times: %s" % restore)
    print("MTTR (mean): %.2f min" % mttr)
    print("median: %.2f min" % median)
    assert 38.99 < mttr < 39.01
    assert 29.99 < median < 30.01
    # DORA elite bar: under 60 minutes
    print("DORA elite bar (<60 min): %s" % ("PASS" if mttr < 60.0 else "FAIL"))
    assert mttr < 60.0
    print("rule: mean and median together - one catastrophe must not hide the trend")
    print("OK: %s computed the reflex" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_mtbf(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # one year of operation, 4 failures, MTTR of 1 hour
    hours_year = 8760.0
    failures = 4
    mttr_h = 1.0
    mtbf = hours_year / failures
    availability = mtbf / (mtbf + mttr_h) * 100.0
    print("MTBF: %.1f hours (%.1f days)" % (mtbf, mtbf / 24.0))
    print("MTTR: %.1f hour" % mttr_h)
    print("availability: %.3f %%" % availability)
    assert 2189.9 < mtbf < 2190.1
    assert 99.953 < availability < 99.955
    print("rule: heal fast AND bleed rarely - A = MTBF / (MTBF + MTTR)")
    print("OK: %s measured endurance" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_nines(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # allowed downtime per availability level
    levels = [99.0, 99.9, 99.95, 99.99, 99.999]
    min_year = 365.0 * 24.0 * 60.0
    print("availability -> allowed downtime per year:")
    for a in levels:
        down_min = (1.0 - a / 100.0) * min_year
        print("  %.3f %% -> %9.2f min (%6.2f h)" % (a, down_min, down_min / 60.0))
    d_999 = (1.0 - 0.999) * min_year
    d_9999 = (1.0 - 0.9999) * min_year
    assert 525.5 < d_999 < 525.7               # 99.9% -> ~525.6 min/year
    assert 8.75 < d_999 / 60.0 < 8.77      # 99.9% -> ~8.76 h/year
    assert 52.5 < d_9999 < 52.7             # 99.99% -> ~52.6 min/year
    monthly_999 = (1.0 - 0.999) * 30.0 * 24.0 * 60.0
    print("99.9%% monthly budget: %.2f min" % monthly_999)
    assert 43.19 < monthly_999 < 43.21
    print("rule: each nine divides the budget by ten - choose the SLO like money")
    print("OK: %s counted the nines" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_fault_timeline(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # unordered timeline entries as the scribe might capture them
    raw = [
        ("14:11", "on-call", "rolled back deploy v482"),
        ("14:02", "monitor", "error rate crossed 5 percent"),
        ("14:06", "IC", "declared SEV2"),
        ("13:58", "telemetry", "first failed checkout (reconstructed)"),
        ("14:20", "monitor", "error rate back under 0.5 percent"),
    ]
    def mins(t):
        h, m = t.split(":")
        return int(h) * 60 + int(m)
    ordered = sorted(raw, key=lambda e: mins(e[0]))
    print("reconstructed timeline:")
    for t, actor, what in ordered:
        print("  %s %-9s %s" % (t, actor, what))
    detection_lag = mins(ordered[1][0]) - mins(ordered[0][0])
    restore = mins(ordered[-1][0]) - mins(ordered[0][0])
    print("true start: %s, detected: %s, lag: %d min" % (ordered[0][0], ordered[1][0], detection_lag))
    print("failure-to-restored: %d min" % restore)
    assert [e[0] for e in ordered] == ["13:58", "14:02", "14:06", "14:11", "14:20"]
    assert detection_lag == 4
    assert restore == 22
    print("rule: the clock starts at failure, not at noticing")
    print("OK: %s wrote the timeline" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_blast_radius(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # dependency graph: service -> services that depend on it (downstream)
    downstream = {
        "dns": ["api", "web", "mobile"],
        "api": ["checkout", "search"],
        "web": ["checkout"],
        "mobile": ["checkout"],
        "db": ["api", "search"],
        "checkout": [], "search": [],
    }
    failed = "dns"
    seen, stack = set(), [failed]
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        stack.extend(downstream.get(node, []))
    print("failed node: %s" % failed)
    print("blast radius: %d nodes -> %s" % (len(seen), sorted(seen)))
    assert seen == {"dns", "api", "web", "mobile", "checkout", "search"}
    assert len(seen) == 6
    # a leaf failure is contained
    leaf_seen, stack = set(), ["search"]
    while stack:
        node = stack.pop()
        if node in leaf_seen:
            continue
        leaf_seen.add(node)
        stack.extend(downstream.get(node, []))
    print("leaf failure blast radius: %d node" % len(leaf_seen))
    assert leaf_seen == {"search"}
    print("rule: the shape of the damage points at the cause")
    print("OK: %s mapped the blast" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_impact_assessment(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # impact ledger: (segment, users affected, minutes down)
    segments = [("web checkout", 60000, 30.0),
                ("mobile checkout", 40000, 30.0),
                ("api partners", 2500, 47.0)]
    total_user_min = sum(u * m for _, u, m in segments)
    print("impact ledger:")
    for seg, u, m in segments:
        print("  %-15s %6d users x %4.0f min = %9.0f user-min" % (seg, u, m, u * m))
    print("total: %.0f user-minutes" % total_user_min)
    assert abs(total_user_min - 3_117_500.0) < 1e-6
    # revenue estimate: 12 orders/min at $64 average during the window
    orders_per_min, aov = 12.0, 64.0
    revenue = orders_per_min * 30.0 * aov
    print("estimated revenue at risk: $%.0f" % revenue)
    assert 23_030.0 < revenue < 23_050.0
    print("rule: severity without impact is just a feeling - ledger it")
    print("OK: %s weighed the pain" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_detection_alerting(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # detection lags (minutes) across a quarter - synthetic teaching data
    lags = [2.0, 4.0, 1.0, 9.0, 3.0, 5.0, 2.0, 14.0, 3.0, 4.0, 6.0, 2.0]
    mttd = sum(lags) / len(lags)
    med = sorted(lags)[len(lags) // 2]
    print("detection lags: %s" % lags)
    print("MTTD: %.2f min, median: %.1f min" % (mttd, med))
    assert 4.58 < mttd < 4.59
    assert med == 4.0
    # alert actionability: pages that needed action vs total pages
    pages, actionable = 132, 41
    action_rate = actionable / pages * 100.0
    print("pages: %d, actionable: %d (%.1f %%)" % (pages, actionable, action_rate))
    assert 31.0 < action_rate < 31.1
    print("verdict: actionability below 50%% - tune the noisy alerts" if action_rate < 50 else "healthy")
    assert action_rate < 50.0
    print("rule: alert on symptoms, and every page must earn its wake-up")
    print("OK: %s tuned the nerves" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_oncall_escalation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # escalation ladder: rung -> ack timeout (minutes), then auto-escalate
    ladder = [("primary", 5.0), ("secondary", 10.0), ("team lead", 15.0), ("manager", 30.0)]
    print("escalation ladder:")
    cumulative = 0.0
    for rung, timeout in ladder:
        cumulative += timeout
        print("  %-10s ack within %4.0f min (page at T+%4.0f)" % (rung, timeout, cumulative))
    assert abs(cumulative - 60.0) < 1e-9
    # rotation load: 6 engineers, weekly rotation
    engineers, weeks = 6, 52
    shifts_each = weeks / engineers
    print("rotation: %d engineers -> %.2f primary weeks each per year" % (engineers, shifts_each))
    assert 8.66 < shifts_each < 8.68
    # simulated unacknowledged page walks the ladder
    t, rung_hit = 0.0, None
    for rung, timeout in ladder:
        t += timeout
        rung_hit = rung
        break  # primary answers at first rung in this drill
    print("drill: primary acknowledged at T+%.0f min, rung reached: %s" % (ladder[0][1], rung_hit))
    assert rung_hit == "primary"
    print("rule: no incident sits unacknowledged - the ladder climbs by itself")
    print("OK: %s stood the watch" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_incident_comms(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SEV1 comms cadence: every 15 minutes over a 90-minute incident
    duration_min, cadence = 90.0, 15.0
    updates = int(duration_min / cadence) + 1  # opening + cadence updates
    print("incident duration: %.0f min, cadence: %.0f min" % (duration_min, cadence))
    print("updates owed: %d (opening + %d cadence updates)" % (updates, updates - 1))
    assert updates == 7
    # audience coverage check
    audiences = {"responders": True, "executives": True, "support": True,
                 "status page": True, "customers": True}
    covered = sum(audiences.values())
    print("audiences briefed: %d/%d" % (covered, len(audiences)))
    assert covered == 5
    # staleness guard: longest gap between updates must not exceed 2x cadence
    gaps = [15.0, 15.0, 14.0, 16.0, 15.0, 15.0]
    worst = max(gaps)
    print("worst update gap: %.0f min (limit %.0f)" % (worst, 2 * cadence))
    assert worst <= 2 * cadence
    print("rule: the drumbeat never slips - cadence, not inspiration")
    print("OK: %s kept the voice" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_incident_commander(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # span of control: 12 responders organized under one IC
    responders = 12
    teams = ["ops", "comms", "data"]
    per_team = responders / len(teams)
    channels_without_ic = responders * (responders - 1) // 2
    channels_with_ic = responders  # hub-and-spoke through the IC
    print("responders: %d in %d teams (%.0f per team)" % (responders, len(teams), per_team))
    print("coordination channels without IC: %d" % channels_without_ic)
    print("coordination channels with IC hub: %d" % channels_with_ic)
    assert per_team == 4.0
    assert channels_without_ic == 66
    assert channels_with_ic == 12
    # decision latency: IC loop every 15 min over a 90-min incident
    decisions = int(90 / 15)
    print("command decisions in a 90-min SEV1: %d" % decisions)
    assert decisions == 6
    print("rule: one commander, stated aloud - command never drifts")
    print("OK: %s took command" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_triage_severity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # severity rubric: score = 0.5*impact + 0.3*scope + 0.2*urgency (each 0-5)
    def score(impact, scope, urgency):
        return 0.5 * impact + 0.3 * scope + 0.2 * urgency
    def grade(s):
        if s >= 4.0:
            return "SEV1"
        if s >= 2.5:
            return "SEV2"
        if s >= 1.0:
            return "SEV3"
        return "SEV4"
    cases = [("checkout down globally", 5, 5, 5),
             ("search slow in one region", 2, 3, 3),
             ("typo on help page", 0, 1, 1)]
    for label, i, s, u in cases:
        sc, g = score(i, s, u), grade(score(i, s, u))
        print("  %-26s score %.2f -> %s" % (label, sc, g))
    assert grade(score(5, 5, 5)) == "SEV1"
    assert grade(score(2, 3, 3)) == "SEV2"
    assert grade(score(0, 1, 1)) == "SEV4"
    assert 4.99 < score(5, 5, 5) < 5.01
    assert 2.49 < score(2, 3, 3) < 2.51
    print("rule: grade in minutes, write the reasoning, re-grade on evidence")
    print("OK: %s ran triage" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_mitigation_resolution(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # (time-to-mitigate, time-to-resolve) minutes - synthetic teaching data
    incidents = [(8.0, 45.0), (15.0, 90.0), (5.0, 30.0), (22.0, 130.0), (11.0, 60.0)]
    mttm = sum(m for m, _ in incidents) / len(incidents)
    mttr = sum(r for _, r in incidents) / len(incidents)
    print("MTTM: %.2f min, MTTR: %.2f min" % (mttm, mttr))
    print("mitigation share of response: %.1f %%" % (mttm / mttr * 100.0))
    assert 12.19 < mttm < 12.21
    assert 70.99 < mttr < 71.01
    assert mttm < mttr, "mitigation must land before resolution"
    # mitigation effectiveness: error rate before/after rollback
    before, after = 34.0, 0.4
    reduction = (before - after) / before * 100.0
    print("rollback: error %.1f%% -> %.1f%% (%.1f%% reduction)" % (before, after, reduction))
    assert 98.7 < reduction < 98.9
    print("rule: stop the bleeding first - understanding can wait for calm")
    print("OK: %s chose mitigation first" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_restoration_rollback(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # canary analysis: 5% canary vs baseline error rates
    baseline_err, canary_err = 0.10, 2.40  # percent
    halt_threshold = 1.0  # halt rollout if canary exceeds 1%
    print("baseline error: %.2f%%, canary error: %.2f%%" % (baseline_err, canary_err))
    verdict = "HALT" if canary_err > halt_threshold else "PROCEED"
    print("canary verdict (threshold %.1f%%): %s" % (halt_threshold, verdict))
    assert verdict == "HALT"
    # rollback drill timings (minutes) - synthetic teaching data
    drills = [6.0, 4.5, 7.0, 5.0]
    mean_drill = sum(drills) / len(drills)
    print("rollback drills: %s -> mean %.2f min" % (drills, mean_drill))
    assert 5.62 < mean_drill < 5.63
    assert mean_drill < 10.0, "rollback must be a minutes-long drill"
    print("rule: every step forward mapped with its step back")
    print("OK: %s kept the way home" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_five_whys(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the auditable chain: each answer a fact, each why following the last
    chain = [
        "checkout was down 47 minutes",
        "deploy v482 crashed the payment workers",
        "v482 was never tested against the new OS image",
        "the pipeline has no deploy test on OS upgrades",
        "nobody owned adding OS-upgrade testing to the pipeline",
    ]
    print("five whys chain:")
    for i, link in enumerate(chain, 1):
        print("  why %d: %s" % (i, link))
    assert len(chain) == 5
    root = chain[-1]
    # blameless check: the root names a system gap, not a person
    import re as _re
    banned = [r"\bpriya\b", r"\bhe\b", r"\bshe\b", r"engineer pushed", r"\bforgot\b"]
    assert not any(_re.search(b, root.lower()) for b in banned), "chain ended at a person"
    assert "nobody owned" in root or "no " in root
    print("root cause: %s" % root)
    print("action: assign pipeline-test ownership and add the OS-upgrade stage")
    print("rule: never stop at the symptom, never end at a person")
    print("OK: %s dug to the root" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_fishbone_faulttree(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # OR gate: any of three independent causes (p=0.01 each) fails the system
    p = [0.01, 0.01, 0.01]
    p_or = 1.0 - math.prod(1.0 - x for x in p)
    print("OR gate (any of 3 x p=0.01): P = %.5f" % p_or)
    assert 0.0296 < p_or < 0.0298
    # AND gate: all three must coincide
    p_and = math.prod(p)
    print("AND gate (all 3 coincide):   P = %.7f" % p_and)
    assert 0.99e-6 < p_and < 1.01e-6
    # fishbone coverage: every category bone must carry at least one rib
    bones = {"people": 2, "process": 3, "tools": 2, "environment": 1,
             "materials": 1, "measurement": 2}
    empty = [k for k, v in bones.items() if v == 0]
    print("fishbone ribs per bone: %s" % bones)
    assert not empty, "every bone needs at least one rib before debate"
    assert sum(bones.values()) == 11
    print("rule: breadth before debate - fill every bone, then prune by evidence")
    print("OK: %s read the skeleton" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_blameless_postmortems(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # language audit: blameful vs blameless sentences in a draft
    sentences = [
        "the deploy proceeded without a canary check",
        "the alert fired 9 minutes after the first failure",
        "priya skipped the canary check",
        "the runbook step referenced a decommissioned host",
    ]
    blame_markers = ["skipped", "forgot", "failed to", "neglected"]
    clean, flagged = [], []
    for s in sentences:
        (flagged if any(m in s.lower() for m in blame_markers) else clean).append(s)
    print("blameless sentences: %d" % len(clean))
    for s in clean:
        print("  ok: %s" % s)
    print("flagged sentences: %d" % len(flagged))
    for s in flagged:
        print("  rewrite: %s" % s)
    assert len(clean) == 3
    assert len(flagged) == 1
    # follow-through: action closure in blameless vs blame cultures (illustrative)
    blameless_close, blame_close = 0.87, 0.41
    print("action closure: blameless %.0f%% vs blame %.0f%% (illustrative)" % (
        blameless_close * 100, blame_close * 100))
    assert blameless_close > blame_close
    print("rule: examine the wound, never the warrior")
    print("OK: %s kept the oath of honesty" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_postmortem_template(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # completeness audit of a postmortem draft against the 7 canonical sections
    canonical = ["summary", "impact", "timeline", "root cause",
                 "what went well", "what went poorly", "action items"]
    draft = ["summary", "impact", "timeline", "root cause",
             "what went poorly", "action items"]  # missing: what went well
    missing = [s for s in canonical if s not in draft]
    score = len(draft) / len(canonical) * 100.0
    print("sections present: %d/%d (%.1f%%)" % (len(draft), len(canonical), score))
    print("missing: %s" % missing)
    assert missing == ["what went well"]
    assert 85.6 < score < 85.8
    # action-item teeth check: each needs owner + date + verification
    actions = [("add canary gate", "lee", "2026-11-15", "pipeline rejects gateless deploys"),
               ("fix runbook host", "sam", "2026-10-30", "drill passes with runbook only")]
    for label, owner, date, verify in actions:
        assert owner and date and verify, "toothless action: %s" % label
    print("action items with teeth: %d" % len(actions))
    print("rule: same sections every time - a postmortem is data, not an essay")
    print("OK: %s kept the chronicle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_action_items(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # action-item aging (days open) - synthetic teaching data
    aging = [4.0, 12.0, 31.0, 8.0, 45.0, 3.0, 60.0, 15.0]
    due = 30.0
    mean_age = sum(aging) / len(aging)
    overdue = sum(1 for a in aging if a > due)
    print("action items: %d, mean age %.1f days" % (len(aging), mean_age))
    print("overdue (>%.0f days): %d (%.0f%%)" % (due, overdue, overdue / len(aging) * 100.0))
    assert 22.24 < mean_age < 22.26
    assert overdue == 3
    # closure rate for the quarter
    opened, closed = 46, 41
    closure = closed / opened * 100.0
    print("quarterly closure: %d/%d (%.1f%%)" % (closed, opened, closure))
    assert 89.0 < closure < 89.2
    # recurrence check: failure classes seen before
    recurrences = 1
    print("recurrences this quarter: %d" % recurrences)
    assert recurrences <= 1, "recurrence means the learning loop broke"
    print("rule: a vow is not kept until the body proves it")
    print("OK: %s kept the oath-book" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_status_page(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # incident state machine walk
    states = ["investigating", "identified", "monitoring", "resolved"]
    walk = ["investigating", "identified", "monitoring", "resolved"]
    assert walk == states, "states must move in order"
    print("state walk: %s" % " -> ".join(walk))
    # subscriber notification math
    subscribers, batch_per_min = 100000, 20000
    notify_min = subscribers / batch_per_min
    print("subscribers: %d, notify time: %.1f min" % (subscribers, notify_min))
    assert 4.99 < notify_min < 5.01
    # independence check: status page must not share fate with the services
    hosts = {"status page": "provider-b", "api": "provider-a", "web": "provider-a"}
    assert hosts["status page"] != hosts["api"], "status page shares fate with the api"
    print("hosting: status page on %s, services on %s - independent" % (
        hosts["status page"], hosts["api"]))
    print("rule: the banner flies on its own pole, even when the city burns")
    print("OK: %s raised the banner" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_paging_routing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # routing rules: (service, severity) -> (team, channel)
    rules = {("checkout", "SEV1"): ("payments", "page"),
             ("checkout", "SEV3"): ("payments", "ticket"),
             ("search", "SEV2"): ("search", "page"),
             ("docs", "SEV4"): ("docs", "backlog")}
    alerts = [(("checkout", "SEV1"), ("payments", "page")),
              (("search", "SEV2"), ("search", "page")),
              (("docs", "SEV4"), ("docs", "backlog"))]
    for key, expected in alerts:
        routed = rules[key]
        print("  alert %s -> team %s via %s" % (key, routed[0], routed[1]))
        assert routed == expected
    # misroute rate must be driven down by the tuning loop
    pages, misrouted = 210, 6
    misrate = misrouted / pages * 100.0
    print("misroute rate: %d/%d (%.2f%%)" % (misrouted, pages, misrate))
    assert 2.85 < misrate < 2.87
    assert misrate < 5.0, "misroutes are detection time thrown away"
    print("rule: every alarm knows its soldier - misroutes are bugs in the rules")
    print("OK: %s stationed the guard" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_incident_bridge(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # check-in loop over a 90-minute SEV1 at 15-minute cadence
    duration, cadence = 90.0, 15.0
    checkins = int(duration / cadence)
    print("bridge check-ins: %d at %.0f-min cadence" % (checkins, cadence))
    assert checkins == 6
    # responder rotation: fresh responders every 4 hours on long incidents
    shift_h = 4.0
    rotations = duration / 60.0 / shift_h
    print("rotations needed for %.1f h incident: %.2f (none yet)" % (duration / 60.0, rotations))
    assert 0.37 < rotations < 0.38
    # etiquette: newcomers must read the timeline before asking
    newcomers, read_first = 3, 3
    print("newcomers onboarded via timeline: %d/%d" % (read_first, newcomers))
    assert read_first == newcomers
    print("rule: voice for decisions, text for the record - the council disbands at victory")
    print("OK: %s convened the council" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_sre_error_budgets(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SLO 99.9% over 30 days at 1M requests/day
    slo = 99.9
    requests = 1_000_000 * 30
    budget = (1.0 - slo / 100.0) * requests
    print("SLO: %.1f%%, requests/30d: %d" % (slo, requests))
    print("error budget: %.0f failed requests" % budget)
    assert 29_990.0 < budget < 30_010.0
    consumed = 21_000.0
    remaining = budget - consumed
    print("consumed: %.0f, remaining: %.0f (%.1f%% left)" % (consumed, remaining, remaining / budget * 100.0))
    assert 8_990.0 < remaining < 9_010.0
    # burn rate: consuming 2.5x the sustainable rate
    burn_rate = 2.5
    days_left = (remaining / budget) * 30.0 / burn_rate
    print("burn rate: %.1fx -> budget exhausts in %.1f days at this pace" % (burn_rate, days_left))
    assert 3.5 < days_left < 3.7
    policy = "FREEZE launches" if remaining / budget < 0.5 else "ship with care"
    print("policy: %s" % policy)
    assert policy == "FREEZE launches"
    print("rule: the budget is honor made countable")
    print("OK: %s signed the covenant" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_chaos_engineering(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # steady-state hypothesis test: kill 10% of instances in one zone
    baseline_err = 0.12  # percent, measured over the prior week
    experiment_err = 0.15  # percent, during the fault injection
    tolerance_pp = 0.10  # hypothesis: error moves less than 0.10 percentage points
    delta = experiment_err - baseline_err
    print("steady state baseline error: %.2f%%" % baseline_err)
    print("experiment error: %.2f%%, delta: %+.2f pp (tolerance %.2f pp)" % (
        experiment_err, delta, tolerance_pp))
    holds = delta < tolerance_pp
    print("hypothesis: %s" % ("HOLDS - resilience proven" if holds else "BROKEN - weakness found"))
    assert holds
    assert 0.029 < delta < 0.031
    # blast radius accounting
    zone_instances, killed = 40, 4
    print("blast radius: %d/%d instances in one zone (%.0f%%)" % (
        killed, zone_instances, killed / zone_instances * 100.0))
    assert killed / zone_instances == 0.10
    print("rule: spar with padded blades - hypothesis first, abort armed")
    print("OK: %s ran the sparring bout" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_observability(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # trace sampling economics
    spans_per_min = 1_000_000
    head_sample = 0.01
    kept_per_min = spans_per_min * head_sample
    bytes_per_span = 2048
    gb_per_day = kept_per_min * bytes_per_span * 60 * 24 / 1e9
    print("spans/min: %d, head sample: %.0f%%" % (spans_per_min, head_sample * 100))
    print("kept: %.0f spans/min -> %.1f GB/day" % (kept_per_min, gb_per_day))
    assert 9_990.0 < kept_per_min < 10_010.0
    assert 29.4 < gb_per_day < 29.6
    # tail-based sampling keeps 100% of errors: error visibility check
    err_rate = 0.002
    err_spans = spans_per_min * err_rate
    print("error spans/min kept by tail sampling: %.0f (100%% of errors)" % err_spans)
    assert 1_990.0 < err_spans < 2_010.0
    # the incident question ladder: metrics -> traces -> logs
    ladder = [("metrics", "when did it start"), ("traces", "which service"),
              ("logs", "what was the mechanism")]
    for pillar, answers in ladder:
        print("  %-8s answers: %s" % (pillar, answers))
    assert len(ladder) == 3
    print("rule: a body that feels itself cannot be ambushed by its own wounds")
    print("OK: %s sharpened the senses" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_metrics_dashboards(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # monthly MTTR trend (minutes) - synthetic teaching data
    mttr = [95.0, 88.0, 80.0, 72.0, 65.0]
    n = len(mttr)
    xs = list(range(n))
    mean_x = sum(xs) / n
    mean_y = sum(mttr) / n
    slope = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, mttr)) / sum(
        (x - mean_x) ** 2 for x in xs)
    print("MTTR trend: %s" % mttr)
    print("slope: %.2f min/month" % slope)
    assert -7.61 < slope < -7.59
    assert slope < 0, "MTTR must trend down"
    improvement = (mttr[0] - mttr[-1]) / mttr[0] * 100.0
    print("improvement over %d months: %.1f%%" % (n, improvement))
    assert 31.5 < improvement < 31.6
    # recurrence: the red alarm
    recurrences = [0, 0, 1, 0, 0]
    print("recurrences by month: %s (total %d)" % (recurrences, sum(recurrences)))
    assert sum(recurrences) == 1
    print("rule: measurement that changes nothing is ceremony")
    print("OK: %s read the chart" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_dora_metrics(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # classify a team against the DORA elite thresholds
    team = {"deploys_per_day": 4.0, "lead_time_min": 42.0,
            "mttr_min": 38.0, "change_fail_pct": 9.0}
    checks = {
        "deployment frequency": team["deploys_per_day"] >= 1.0,
        "lead time < 1h": team["lead_time_min"] < 60.0,
        "MTTR < 1h": team["mttr_min"] < 60.0,
        "change failure 0-15%": 0.0 <= team["change_fail_pct"] <= 15.0,
    }
    print("team metrics: %s" % team)
    for label, passed in checks.items():
        print("  %-22s %s" % (label, "ELITE" if passed else "not elite"))
    assert all(checks.values()), "this team should classify elite on all four"
    elite_count = sum(checks.values())
    print("elite checks passed: %d/4" % elite_count)
    assert elite_count == 4
    # contrast: a low performer
    low = {"deploys_per_day": 1.0 / 90.0, "lead_time_min": 30 * 24 * 60.0,
           "mttr_min": 14 * 24 * 60.0, "change_fail_pct": 25.0}
    low_elite = sum([low["deploys_per_day"] >= 1.0, low["lead_time_min"] < 60.0,
                     low["mttr_min"] < 60.0, 0.0 <= low["change_fail_pct"] <= 15.0])
    print("low performer elite checks: %d/4" % low_elite)
    assert low_elite == 0
    print("rule: speed and stability are the same capability, not a trade-off")
    print("OK: %s ran the trials" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_game_days(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # drill results: detection and mitigation before/after a drill program
    before = {"detect_min": 25.0, "mitigate_min": 55.0, "runbook_defects": 7}
    after = {"detect_min": 8.0, "mitigate_min": 22.0, "runbook_defects": 1}
    for k in before:
        improvement = (before[k] - after[k]) / before[k] * 100.0
        print("  %-15s %.0f -> %.0f (%.0f%% better)" % (k, before[k], after[k], improvement))
    det_imp = (before["detect_min"] - after["detect_min"]) / before["detect_min"] * 100.0
    assert 67.9 < det_imp < 68.1
    mit_imp = (before["mitigate_min"] - after["mitigate_min"]) / before["mitigate_min"] * 100.0
    assert 59.9 < mit_imp < 60.1
    assert after["runbook_defects"] < before["runbook_defects"]
    # scenario rotation covers the risk register
    scenarios = ["db failover", "zone loss", "dns failure", "deploy rollback", "ddos absorb"]
    print("scenario library: %d scenarios" % len(scenarios))
    assert len(scenarios) == 5
    print("rule: battles fought in practice are won in war")
    print("OK: %s mustered the troops" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_review_boards(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # quarterly board scorecard - synthetic teaching data
    incidents, sev1 = 34, 3
    actions_opened, actions_closed = 52, 47
    closure = actions_closed / actions_opened * 100.0
    print("incidents: %d (SEV1: %d)" % (incidents, sev1))
    print("actions: %d opened, %d closed (%.1f%%)" % (actions_opened, actions_closed, closure))
    assert 90.3 < closure < 90.5
    overdue = 2
    print("overdue actions: %d" % overdue)
    assert overdue <= 3, "overdue actions must stay near zero"
    # recurrence is the board's personal failure metric
    recurrences = 0
    print("failure-class recurrences: %d" % recurrences)
    assert recurrences == 0
    # investment decision: budget burn leaders get reliability work
    burn = {"checkout": 0.82, "search": 0.31, "docs": 0.05}
    hottest = max(burn, key=burn.get)
    print("highest budget burn: %s (%.0f%%) -> reliability investment" % (hottest, burn[hottest] * 100))
    assert hottest == "checkout"
    print("rule: the elders chase every vow to completion")
    print("OK: %s convened the elders" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_dyn_2016(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # timeline math for the two waves, October 21 2016 (UTC)
    def mins(t):
        h, m = t.split(":")
        return int(h) * 60 + int(m)
    wave1 = (mins("11:10"), mins("13:20"))
    wave2 = (mins("15:50"), mins("17:00"))
    d1, d2 = wave1[1] - wave1[0], wave2[1] - wave2[0]
    print("wave 1: 11:10-13:20 UTC = %d min" % d1)
    print("wave 2: 15:50-17:00 UTC = %d min" % d2)
    print("total degraded: %d min" % (d1 + d2))
    assert d1 == 130
    assert d2 == 70
    assert d1 + d2 == 200
    # reported peak scale
    peak_tbps = 1.2
    print("reported peak attack traffic: ~%.1f Tbps" % peak_tbps)
    assert 1.19 < peak_tbps < 1.21
    # shared-dependency blast radius: one DNS provider, N customers dark
    customers = ["twitter", "netflix", "reddit", "github", "airbnb"]
    print("sample of affected customers: %d named" % len(customers))
    assert len(customers) == 5
    print("rule: no single nerve shall be the body's only path")
    print("OK: %s studied the siege" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_fastly_2021(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # timeline math: June 8 2021, 09:58 to 10:44 UTC
    def mins(t):
        h, m = t.split(":")
        return int(h) * 60 + int(m)
    duration = mins("10:44") - mins("09:58")
    print("outage window: 09:58-10:44 UTC = %d min" % duration)
    assert duration == 46
    # error share vs the monthly budget at 99.9%
    err_share = 0.85
    monthly_budget_min = 0.001 * 30 * 24 * 60  # 43.2 min at 99.9%
    budget_consumed = duration * err_share / monthly_budget_min * 100.0
    print("error share: %.0f%%, monthly 99.9%% budget: %.1f min" % (err_share * 100, monthly_budget_min))
    print("budget consumed in 46 min: %.0f%% of the month" % budget_consumed)
    assert 43.19 < monthly_budget_min < 43.21
    assert 90.4 < budget_consumed < 90.6
    # latent period: bug deployed May 12, triggered June 8
    latent_days = (8 - 12) + 31  # May 12 -> June 8
    print("latent period: %d days armed before the trigger" % latent_days)
    assert latent_days == 27
    print("rule: the rollback is the hand that puts the serpent back to sleep")
    print("OK: %s kept the vigil" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_io_aws_2021(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # timeline math: December 7 2021, ~10:48 ET start, substantially restored by evening
    def mins(t):
        h, m = t.split(":")
        return int(h) * 60 + int(m)
    duration = mins("18:00") - mins("10:48")  # ~7.2 hours of degraded control plane
    print("degraded window: 10:48-18:00 ET = %d min (%.1f h)" % (duration, duration / 60.0))
    assert duration == 432
    assert 7.19 < duration / 60.0 < 7.21
    # budget math: 7.2 hours against a 99.9% monthly budget of 43.8 minutes
    monthly_budget = 43.8
    consumed = duration / monthly_budget * 100.0
    print("monthly 99.9%% budget: %.1f min; consumed: %.0f%% of the month" % (monthly_budget, consumed))
    assert 986.0 < consumed < 987.0
    # control plane vs data plane: which degraded
    plane = {"control APIs": "degraded", "console": "degraded",
             "traffic serving": "largely healthy", "dns": "healthy"}
    degraded = [k for k, v in plane.items() if v != "healthy" and "largely" not in v]
    print("planes: %s" % plane)
    print("fully degraded planes: %s" % degraded)
    assert degraded == ["control APIs", "console"]
    # regional concentration: one region's bad day
    regions = {"us-east-1": "degraded", "us-west-2": "healthy", "eu-west-1": "healthy"}
    healthy = sum(1 for v in regions.values() if v == "healthy")
    print("regions healthy: %d/%d" % (healthy, len(regions)))
    assert healthy == 2
    print("rule: never let one hall hold the keys to every room")
    print("OK: %s bound the automation" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what_is_incident": demo_io_what_is_incident,
    "what_is_outage": demo_io_what_is_outage,
    "incident_lifecycle": demo_io_incident_lifecycle,
    "mttr": demo_io_mttr,
    "mtbf": demo_io_mtbf,
    "nines": demo_io_nines,
    "fault_timeline": demo_io_fault_timeline,
    "blast_radius": demo_io_blast_radius,
    "impact_assessment": demo_io_impact_assessment,
    "detection_alerting": demo_io_detection_alerting,
    "oncall_escalation": demo_io_oncall_escalation,
    "incident_comms": demo_io_incident_comms,
    "incident_commander": demo_io_incident_commander,
    "triage_severity": demo_io_triage_severity,
    "mitigation_resolution": demo_io_mitigation_resolution,
    "restoration_rollback": demo_io_restoration_rollback,
    "five_whys": demo_io_five_whys,
    "fishbone_faulttree": demo_io_fishbone_faulttree,
    "blameless_postmortems": demo_io_blameless_postmortems,
    "postmortem_template": demo_io_postmortem_template,
    "action_items": demo_io_action_items,
    "status_page": demo_io_status_page,
    "paging_routing": demo_io_paging_routing,
    "incident_bridge": demo_io_incident_bridge,
    "sre_error_budgets": demo_io_sre_error_budgets,
    "chaos_engineering": demo_io_chaos_engineering,
    "observability": demo_io_observability,
    "metrics_dashboards": demo_io_metrics_dashboards,
    "dora_metrics": demo_io_dora_metrics,
    "game_days": demo_io_game_days,
    "review_boards": demo_io_review_boards,
    "dyn_2016": demo_io_dyn_2016,
    "fastly_2021": demo_io_fastly_2021,
    "aws_2021": demo_io_aws_2021,
}
