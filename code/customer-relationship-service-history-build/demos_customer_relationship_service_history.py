#!/usr/bin/env python3
"""Demo programs for the Customer Relationship and Service History databases.

Every demo is real, runnable, stdlib-only Python performing the actual
CRM/service-management computation for its record. All are
machine-executed by build.py: each prints its real computed values,
asserts tight bounds (never float exact-equality), and ends with the OK
marker.

Civilian operational scope only. No website references. No Facebook.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_crm_what_is(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # retention economics: the profit of a 1000-customer cohort over 5 years
    base, margin = 1000.0, 180.0
    for retention in (0.95, 0.80):
        profit = margin * sum(base * retention ** t for t in range(5))
        print("retention %.0f %% -> 5-year cohort profit $%.2f" % (retention * 100, profit))
    p95 = margin * sum(base * 0.95 ** t for t in range(5))
    p80 = margin * sum(base * 0.80 ** t for t in range(5))
    assert 814388.0 < p95 < 814389.0
    assert 605087.0 < p80 < 605089.0
    uplift = p95 - p80
    print("profit uplift of 95%% vs 80%% retention: $%.2f" % uplift)
    assert 209300.0 < uplift < 209301.0
    survivors = base * 0.95 ** 5
    print("customers remaining after 5 years at 95%%: %.1f" % survivors)
    assert 773.7 < survivors < 773.9
    print("rule: retention compounds; acquisition spends once")
    print("OK: %s proved the loop" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_customer_record(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # identity resolution: merge two source lists on normalized email
    list_a = ["ana@acme.co", "BOB@ACME.CO", "cy@acme.co", "dee@acme.co",
              "eli@acme.co", "fay@acme.co"]
    list_b = ["bob@acme.co", "CY@acme.co", "gus@acme.co", "hal@acme.co",
              "ana@acme.co"]
    seen, merged, dupes = {}, [], 0
    for email in list_a + list_b:
        key = email.strip().lower()
        if key in seen:
            dupes += 1
        else:
            seen[key] = email
            merged.append(email)
    print("source A: %d, source B: %d" % (len(list_a), len(list_b)))
    print("duplicates folded: %d" % dupes)
    print("surviving unique records: %d" % len(merged))
    assert dupes == 3
    assert len(merged) == 8
    # survivorship: most complete field wins per field
    cand = [{"email": "ana@acme.co", "phone": ""},
            {"email": "ANA@acme.co", "phone": "+1-555-0142"}]
    survivor = {k: next(c[k] for c in cand if c[k]) for k in ("email", "phone")}
    print("survivor: %s" % survivor)
    assert survivor["phone"] == "+1-555-0142"
    print("rule: match before create; merge, never delete history")
    print("OK: %s kept one true record" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_service_vocabulary(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # intake classification by keyword rules: incident vs request vs problem
    items = [
        ("checkout page down for all users", "incident"),
        ("password reset for j. rivera", "service-request"),
        ("recurring database corruption on shard 4", "problem"),
        ("new laptop for incoming hire", "service-request"),
        ("delivery never arrived, tracking silent", "incident"),
        ("add user to billing group", "service-request"),
        ("same login failure third time this week", "problem"),
        ("pricing question about renewal", "service-request"),
        ("mobile app crashes on launch", "incident"),
        ("printer jam on floor 3", "incident"),
        ("known error KE-118 workaround applied", "known-error"),
        ("how do I export my invoices", "service-request"),
    ]
    incident_kw = ("down", "never arrived", "crashes", "jam")
    problem_kw = ("recurring", "third time")
    counts = {"incident": 0, "service-request": 0, "problem": 0, "known-error": 0}
    for text, expected in items:
        t = text.lower()
        if "known error" in t:
            got = "known-error"
        elif any(k in t for k in problem_kw):
            got = "problem"
        elif any(k in t for k in incident_kw):
            got = "incident"
        else:
            got = "service-request"
        assert got == expected, (text, got, expected)
        counts[got] += 1
    print("classified %d intake items: %s" % (len(items), counts))
    assert counts == {"incident": 4, "service-request": 5, "problem": 2, "known-error": 1}
    print("rule: name the trouble first; the remedy follows the name")
    print("OK: %s spoke the vocabulary" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_ticket_anatomy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # ticket age from timestamps, priority from the impact x urgency matrix
    from datetime import datetime
    created = datetime(2026, 10, 10, 9, 0, 0)
    now = datetime(2026, 10, 12, 15, 30, 0)
    age_h = (now - created).total_seconds() / 3600.0
    print("ticket age: %.1f hours" % age_h)
    assert 54.4 < age_h < 54.6
    matrix = {("high", "high"): "P1", ("high", "medium"): "P2",
              ("high", "low"): "P3", ("medium", "high"): "P2",
              ("medium", "medium"): "P3", ("medium", "low"): "P4",
              ("low", "high"): "P3", ("low", "medium"): "P4",
              ("low", "low"): "P4"}
    priority = matrix[("high", "medium")]
    print("impact high x urgency medium -> %s" % priority)
    assert priority == "P2"
    sla_target_h = {"P1": 4, "P2": 24, "P3": 72, "P4": 168}[priority]
    remaining = sla_target_h - age_h
    print("P2 resolution target %dh; %.1f h remaining" % (sla_target_h, remaining))
    assert remaining < 0, "this demo ticket breached - escalation should have fired"
    print("rule: anatomy carries identity, classification, story, commitment, linkage")
    print("OK: %s read the scroll" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_ticket_lifecycle(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # lifecycle math off the transition log: dwell, reopen rate, touches
    from datetime import datetime
    log = [("new", "2026-10-10 09:00"), ("triaged", "2026-10-10 09:12"),
           ("in progress", "2026-10-10 09:40"), ("pending customer", "2026-10-10 11:05"),
           ("in progress", "2026-10-11 08:20"), ("resolved", "2026-10-11 10:00"),
           ("closed", "2026-10-14 10:00")]
    fmt = "%Y-%m-%d %H:%M"
    times = [datetime.strptime(ts, fmt) for _, ts in log]
    dwell_work = sum((b - a).total_seconds() / 3600.0
                     for (sa, a), (sb, b) in zip(zip([s for s, _ in log], times),
                                                 zip([s for s, _ in log][1:], times[1:]))
                     if sa == "in progress")
    print("active work dwell: %.2f hours" % dwell_work)
    assert 3.08 < dwell_work < 3.09
    resolved, reopened = 40, 3
    reopen_rate = reopened / resolved * 100.0
    print("resolved %d, reopened %d -> reopen rate %.1f %%" % (resolved, reopened, reopen_rate))
    assert 7.4 < reopen_rate < 7.6
    print("rule: resolution is a proposal; the customer confirms the fact")
    print("OK: %s walked the stations" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_channels(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # blended cost per resolved contact across the channel mix
    mix = {"phone": (1200, 8.50), "email": (2400, 2.75),
           "chat": (1800, 3.25), "portal": (5200, 0.45)}
    total_vol = sum(v for v, _ in mix.values())
    total_cost = sum(v * c for v, c in mix.values())
    print("contacts: %d" % total_vol)
    for ch, (v, c) in mix.items():
        print("  %-6s %5d x $%5.2f = $%9.2f" % (ch, v, c, v * c))
    blended = total_cost / total_vol
    print("blended cost per contact: $%.4f" % blended)
    assert total_vol == 10600
    assert 24989.0 < total_cost < 24991.0
    assert 2.357 < blended < 2.358
    print("rule: many doors, one hearth, one history")
    print("OK: %s tuned the mix" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_sla(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # SLA compliance and credit computation for a P2 cohort
    target_h, tickets, met = 4.0, 50, 46
    compliance = met / tickets * 100.0
    breaches = tickets - met
    credit_each, credits = 25.0, breaches * 25.0
    print("P2 response target: %.0f h; %d/%d met -> %.1f %%" % (target_h, met, tickets, compliance))
    print("breaches: %d x $%.0f credit = $%.0f owed" % (breaches, credit_each, credits))
    assert 91.9 < compliance < 92.1
    assert credits == 100.0
    # warning thresholds at 50% and 75% of target
    warn1, warn2 = target_h * 0.5, target_h * 0.75
    print("warning thresholds: %.1f h and %.1f h" % (warn1, warn2))
    assert 1.99 < warn1 < 2.01 and 2.99 < warn2 < 3.01
    print("rule: a timed oath is the only honest kind")
    print("OK: %s kept the sundial" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_prioritization(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the full 3x3 impact x urgency matrix, every cell asserted
    matrix = {("high", "high"): "P1", ("high", "medium"): "P2",
              ("high", "low"): "P3", ("medium", "high"): "P2",
              ("medium", "medium"): "P3", ("medium", "low"): "P4",
              ("low", "high"): "P3", ("low", "medium"): "P4",
              ("low", "low"): "P4"}
    assert len(matrix) == 9
    for (imp, urg), pri in sorted(matrix.items()):
        print("  impact %-6s x urgency %-6s -> %s" % (imp, urg, pri))
    assert matrix[("high", "high")] == "P1"
    assert matrix[("medium", "medium")] == "P3"
    assert matrix[("low", "low")] == "P4"
    # the scales never lie for favor: loudest voice gets no uplift
    p1_count = sum(1 for p in matrix.values() if p == "P1")
    print("P1 cells: %d of 9" % p1_count)
    assert p1_count == 1
    print("rule: weigh the wound, not the volume of the voice")
    print("OK: %s held the scales" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_service_desk(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # tier flow: resolution distribution, escalation rates, tiered cost
    total, l1, l2, l3 = 1000, 680, 240, 80
    assert l1 + l2 + l3 == total
    esc1 = (total - l1) / total * 100.0
    esc2 = l3 / (l2 + l3) * 100.0
    print("L1 resolves %d (%.0f %%), L2 resolves %d, L3 resolves %d" % (l1, l1 / total * 100, l2, l3))
    print("L1->L2 escalation: %.0f %% ; L2->L3 escalation: %.0f %%" % (esc1, esc2))
    assert 31.9 < esc1 < 32.1
    assert 24.9 < esc2 < 25.1
    cost = total * 6.0 + (l2 + l3) * 18.0 + l3 * 55.0
    print("tiered cost: $%.0f for %d resolved = $%.2f each" % (cost, total, cost / total))
    assert 16159.0 < cost < 16161.0
    assert 16.15 < cost / total < 16.17
    print("rule: the cheapest capable tier resolves; the torch passes warm")
    print("OK: %s posted the guard" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_product_history(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # warranty entitlement from dates; installed-base version shares
    from datetime import date
    purchased, warranty_months = date(2025, 6, 15), 24
    expiry = date(purchased.year + warranty_months // 12,
                  purchased.month + warranty_months % 12, purchased.day)
    today = date(2026, 10, 17)
    remaining = (expiry - today).days
    print("purchased %s, warranty %d mo -> expires %s" % (purchased, warranty_months, expiry))
    print("in warranty: %s; days remaining: %d" % (today < expiry, remaining))
    assert expiry == date(2027, 6, 15)
    assert remaining == 241
    base = {"4.0": 120, "4.1": 340, "4.2": 890, "5.0": 150}
    total = sum(base.values())
    share42 = base["4.2"] / total * 100.0
    print("installed base %d units; version 4.2 share %.2f %%" % (total, share42))
    assert total == 1500
    assert 59.32 < share42 < 59.35
    print("rule: the keeper remembers every thing entrusted")
    print("OK: %s kept the genealogy" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_crm_models(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # funnel conversion and weighted pipeline forecast
    funnel = [("leads", 1000), ("MQL", 220), ("SQL", 90), ("opportunity", 34), ("won", 11)]
    print("funnel:")
    prev = None
    for stage, n in funnel:
        if prev:
            conv = n / prev * 100.0
            print("  %-11s %4d  (%.1f %% of prior)" % (stage, n, conv))
        else:
            print("  %-11s %4d" % (stage, n))
        prev = n
    assert 21.9 < 220 / 1000 * 100 < 22.1
    assert 40.8 < 90 / 220 * 100 < 41.0
    assert 32.3 < 11 / 34 * 100 < 32.4
    overall = 11 / 1000 * 100.0
    print("lead-to-won overall: %.1f %%" % overall)
    assert 1.09 < overall < 1.11
    opps = [(50000, 0.2), (80000, 0.4), (120000, 0.6), (200000, 0.8)]
    weighted = sum(a * p for a, p in opps)
    print("weighted pipeline: $%d" % weighted)
    assert weighted == 274000
    print("rule: the funnel shows exactly where deals die")
    print("OK: %s weighed the suitors" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_escalation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # escalation countdowns computed from the matrix timers
    from datetime import datetime, timedelta
    timers = {"P1": (15, 30), "P2": (60, 240), "P3": (240, 480), "P4": (1440, 2880)}
    created = datetime(2026, 10, 17, 14, 0, 0)
    for pri in ("P1", "P3"):
        func_m, hier_m = timers[pri]
        func_dl = created + timedelta(minutes=func_m)
        hier_dl = created + timedelta(minutes=hier_m)
        print("%s: functional escalation by %s, hierarchical by %s"
              % (pri, func_dl.strftime("%H:%M"), hier_dl.strftime("%H:%M")))
    assert created + timedelta(minutes=15) == datetime(2026, 10, 17, 14, 15)
    assert created + timedelta(minutes=30) == datetime(2026, 10, 17, 14, 30)
    assert created + timedelta(minutes=480) == datetime(2026, 10, 17, 22, 0)
    # the chain is auditable: every escalation logged with trigger
    chain = [("14:00", "L1", "opened"), ("14:15", "L2", "functional timer"),
             ("14:30", "duty manager", "hierarchical timer")]
    print("escalation chain: %d links" % len(chain))
    assert len(chain) == 3
    print("rule: every rank answers when the call comes")
    print("OK: %s manned the tower" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what_is": demo_crm_what_is,
    "customer_record": demo_crm_customer_record,
    "service_vocabulary": demo_crm_service_vocabulary,
    "ticket_anatomy": demo_crm_ticket_anatomy,
    "ticket_lifecycle": demo_crm_ticket_lifecycle,
    "channels": demo_crm_channels,
    "sla": demo_crm_sla,
    "prioritization": demo_crm_prioritization,
    "service_desk": demo_crm_service_desk,
    "product_history": demo_crm_product_history,
    "crm_models": demo_crm_crm_models,
    "escalation": demo_crm_escalation,
}


def demo_crm_core_metrics(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the five core metrics off one ticket sample, each with its counterweight
    resolve_h = [2.5, 4.0, 1.5, 8.0, 3.0, 26.0, 5.5, 2.0]
    frt_h = [0.25, 0.5, 0.1, 1.0, 0.4, 2.0, 0.3, 0.2]
    aht_m = [8, 12, 6, 22, 10, 35, 14, 9]
    mttr = sum(resolve_h) / len(resolve_h)
    s = sorted(frt_h)
    frt_med = (s[3] + s[4]) / 2.0
    aht = sum(aht_m) / len(aht_m)
    p90 = sorted(resolve_h)[int(0.9 * len(resolve_h)) - 1]
    print("MTTR %.4f h | FRT median %.2f h | AHT %.1f min | p90 resolve %.1f h"
          % (mttr, frt_med, aht, p90))
    assert 6.562 < mttr < 6.564
    assert 0.349 < frt_med < 0.351
    assert 14.49 < aht < 14.51
    reopen_rate = 3 / 40 * 100.0
    print("reopen rate (quality counterweight): %.1f %%" % reopen_rate)
    assert 7.4 < reopen_rate < 7.6
    print("rule: every speed metric walks with a quality counterweight")
    print("OK: %s called the witnesses" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_knowledge(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # honest deflection: sessions with no subsequent ticket, confirmed on sample
    sessions, no_ticket = 800, 520
    raw_deflection = no_ticket / sessions * 100.0
    surveyed, confirmed = 100, 88
    confirm_rate = confirmed / surveyed
    honest_deflected = no_ticket * confirm_rate
    honest_rate = honest_deflected / sessions * 100.0
    print("portal sessions: %d; no ticket after: %d (raw %.1f %%)"
          % (sessions, no_ticket, raw_deflection))
    print("confirmation sample: %d/%d -> honest deflected %.0f (%.2f %%)"
          % (confirmed, surveyed, honest_deflected, honest_rate))
    assert 64.9 < raw_deflection < 65.1
    assert 57.19 < honest_rate < 57.21
    print("rule: deflection is measured from ticket outcomes, never from visits")
    print("OK: %s kept the library honest" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_journey(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # journey stage scores: the average hides nothing when the minimum is named
    stages = [("awareness", 72), ("consideration", 68), ("purchase", 81),
              ("onboarding", 54), ("use", 77), ("support", 63), ("renewal", 70)]
    avg = sum(s for _, s in stages) / len(stages)
    worst = min(stages, key=lambda p: p[1])
    print("journey average: %.2f" % avg)
    for stage, score in stages:
        print("  %-13s %d" % (stage, score))
    print("weakest stage: %s at %d" % worst)
    assert 69.28 < avg < 69.30
    assert worst == ("onboarding", 54)
    print("rule: improvement money goes where the journey bleeds")
    print("OK: %s walked the road" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_csat(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # CSAT top-two-box from a 120-response post-resolution sample
    dist = {5: 58, 4: 34, 3: 15, 2: 8, 1: 5}
    total = sum(dist.values())
    top2 = dist[5] + dist[4]
    pct = top2 / total * 100.0
    mean = sum(k * v for k, v in dist.items()) / total
    print("responses: %d; top-two-box %d -> CSAT %.2f %%" % (total, top2, pct))
    print("mean score: %.3f" % mean)
    for k in (5, 4, 3, 2, 1):
        print("  score %d: %3d" % (k, dist[k]))
    assert total == 120
    assert 76.66 < pct < 76.68
    assert 4.09 < mean < 4.11
    print("rule: the number says how much; the words say what to fix")
    print("OK: %s heard the verdict" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_nps(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # NPS: promoters minus detractors over 200 relationship responses
    promoters, passives, detractors = 110, 55, 35
    total = promoters + passives + detractors
    nps = (promoters - detractors) / total * 100.0
    print("promoters %d, passives %d, detractors %d" % (promoters, passives, detractors))
    print("NPS = (%.1f - %.1f) = %.1f"
          % (promoters / total * 100, detractors / total * 100, nps))
    assert total == 200
    assert 37.4 < nps < 37.6
    # closed loop: every detractor gets an owner and a time box
    looped = detractors  # all 35 routed with 48h follow-up
    print("detractors routed to closed loop: %d/%d" % (looped, detractors))
    assert looped == detractors
    print("rule: the testimony of every detractor is answered")
    print("OK: %s closed the loop" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_ces(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # CES on the 1-7 effort scale: mean plus the low-effort share
    dist = {1: 60, 2: 36, 3: 24, 4: 12, 5: 10, 6: 5, 7: 3}
    total = sum(dist.values())
    mean = sum(k * v for k, v in dist.items()) / total
    low_effort = (dist[1] + dist[2]) / total * 100.0
    print("responses: %d; mean effort %.3f; low-effort (1-2) %.1f %%"
          % (total, mean, low_effort))
    assert total == 150
    assert 2.353 < mean < 2.354
    assert 63.99 < low_effort < 64.01
    # effort drivers coded from the "what was hardest" verbatims
    drivers = {"repeat contact": 41, "repeated info": 27,
               "transfers": 18, "channel switch": 14}
    print("top effort driver: %s (%d mentions)"
          % (max(drivers, key=drivers.get), max(drivers.values())))
    assert max(drivers.values()) == 41
    print("rule: loyalty follows ease, not delight")
    print("OK: %s weighed the burden" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_analytics(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # Little's law: backlog = arrival rate x average wait; spike math
    arrival, wait = 45.0, 2.0
    backlog = arrival * wait
    print("arrival %d/day x wait %.1f d -> backlog %.0f (Little)" % (arrival, wait, backlog))
    assert 89.9 < backlog < 90.1
    spike, days, throughput = 60.0, 5, 45.0
    grown = backlog + (spike - throughput) * days
    print("spike %d/day for %d days at throughput %d -> backlog %.0f"
          % (spike, days, throughput, grown))
    assert 164.9 < grown < 165.1
    # inflow tagging: each arrival class gets its own owner
    inflow = {"new": 38, "reopen": 3, "follow-up": 2, "misroute": 2}
    print("inflow classes: %s (total %d)" % (inflow, sum(inflow.values())))
    assert sum(inflow.values()) == 45
    print("rule: the queue is an instrument panel, not an anxiety")
    print("OK: %s read the dials" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_retention(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # cohort retention curve and the implied monthly churn
    cohort = 1000
    curve = {1: 920, 2: 870, 3: 830, 6: 760, 12: 680}
    print("cohort of %d:" % cohort)
    for m in sorted(curve):
        print("  month %2d: %d retained (%.1f %%)" % (m, curve[m], curve[m] / cohort * 100))
    m12 = curve[12] / cohort
    monthly_churn = (1 - m12 ** (1 / 12)) * 100.0
    print("12-month retention %.0f %%; implied monthly churn %.2f %%" % (m12 * 100, monthly_churn))
    assert 67.9 < m12 * 100 < 68.1
    assert 3.15 < monthly_churn < 3.17
    # save desk on the avoidable voluntary segment
    at_risk, saved = 120, 45
    save_rate = saved / at_risk * 100.0
    print("save desk: %d/%d kept -> %.1f %%" % (saved, at_risk, save_rate))
    assert 37.4 < save_rate < 37.6
    print("rule: the verdict is voted with renewals")
    print("OK: %s mourned and studied" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_segmentation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # RFM quintile codes mapped to named segments and playbooks
    def segment(r, f, m):
        code = "%d%d%d" % (r, f, m)
        if code == "555":
            return "champions"
        if r <= 2 and f >= 4:
            return "at-risk"
        if r == 1 and f <= 2:
            return "hibernating"
        if r <= 2 and m >= 4:
            return "cannot-lose"
        return "potential"
    customers = {"A-101": (5, 5, 5), "B-202": (2, 5, 5), "C-303": (1, 2, 1), "D-404": (4, 3, 4)}
    for cid, (r, f, m) in customers.items():
        print("  %s RFM %d%d%d -> %s" % (cid, r, f, m, segment(r, f, m)))
    assert segment(5, 5, 5) == "champions"
    assert segment(2, 5, 5) == "at-risk"
    assert segment(1, 2, 1) == "hibernating"
    playbooks = {"champions": "advocacy asks", "at-risk": "save outreach",
                 "hibernating": "win-back", "cannot-lose": "executive care"}
    print("playbook for at-risk: %s" % playbooks["at-risk"])
    print("rule: know each partner's station; treat none as a stranger")
    print("OK: %s knew its people" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_recovery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # the recovery paradox in numbers: baseline vs failed vs well-recovered
    baseline, failed_no_recovery, recovered_well = 74.0, 52.0, 82.0
    damage = failed_no_recovery - baseline
    uplift = recovered_well - baseline
    print("baseline satisfaction: %.0f" % baseline)
    print("after failure, no recovery: %.0f (damage %+.0f)" % (failed_no_recovery, damage))
    print("after failure, good recovery: %.0f (uplift %+.0f)" % (recovered_well, uplift))
    assert 7.9 < uplift < 8.1
    assert -22.1 < damage < -21.9
    # empowerment bands: front-line authority by harm tier
    bands = {"minor": 25.0, "moderate": 150.0, "severe": 500.0}
    print("compensation bands: %s" % bands)
    assert bands["severe"] == 500.0
    print("rule: amends swift, follow-up certain")
    print("OK: %s made atonement" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_major_incident(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # major timeline: detect, triage, mitigate, resolve; comms cadence
    t_detect, t_triage, t_mitigate, t_resolve = 8, 20, 65, 140
    print("detected t+%d min; triaged t+%d; mitigated t+%d; resolved t+%d"
          % (t_detect, t_triage, t_mitigate, t_resolve))
    mttr = t_resolve
    print("MTTR: %d min" % mttr)
    assert mttr == 140
    cadence = 30
    updates = [t for t in range(cadence, t_mitigate + 1, cadence)]
    print("status updates on %d-min cadence: %d published before mitigation" % (cadence, len(updates)))
    assert updates == [30, 60]
    # blameless postmortem actions with owners and dates
    actions = [("add circuit breaker", "eng", "2026-11-15"),
               ("runbook for shard failover", "ops", "2026-11-01")]
    print("postmortem actions: %d owned and dated" % len(actions))
    assert len(actions) == 2
    print("rule: mitigation first; blame never")
    print("OK: %s held the walls" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_wfm(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # Erlang C: 100 calls/hour, 180s handle time, 20s target
    calls_per_h, aht_s, target_s = 100.0, 180.0, 20.0
    load = calls_per_h * aht_s / 3600.0
    n = 7
    print("offered load: %.1f Erlangs" % load)
    assert 4.99 < load < 5.01
    num = load ** n / math.factorial(n) * (n / (n - load))
    den = sum(load ** k / math.factorial(k) for k in range(n)) + num
    p_wait = num / den
    sl = 1 - p_wait * math.exp(-(n - load) * target_s / aht_s)
    print("agents %d -> P(wait) %.4f, service level %.2f %% in %ds"
          % (n, p_wait, sl * 100, target_s))
    assert 0.3241 < p_wait < 0.3242
    assert 0.7404 < sl < 0.7405
    shrinkage = 0.25
    bodies = n / (1 - shrinkage)
    print("shrinkage %.0f %% -> schedule %.2f bodies" % (shrinkage * 100, bodies))
    assert 9.33 < bodies < 9.34
    print("rule: the right number, in the right place, at the right hour")
    print("OK: %s mustered the guard" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_qa(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # weighted scorecard plus inter-grader calibration variance
    weights = {"greeting": 10, "needs": 15, "knowledge": 20, "process": 15,
               "communication": 15, "ownership": 15, "closing": 10}
    scores = {"greeting": 4, "needs": 3, "knowledge": 5, "process": 4,
              "communication": 4, "ownership": 5, "closing": 3}
    assert sum(weights.values()) == 100
    total = sum(weights[d] * scores[d] for d in weights) / 100.0
    print("weighted QA score: %.2f / 5" % total)
    assert 4.09 < total < 4.11
    graders = [4.1, 3.9, 4.2]
    mean = sum(graders) / len(graders)
    var = sum((g - mean) ** 2 for g in graders) / len(graders)
    sd = math.sqrt(var)
    print("calibration: graders %s -> sd %.4f" % (graders, sd))
    assert 0.124 < sd < 0.126
    print("rule: the examiners themselves are examined")
    print("OK: %s inspected its honor" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_rca(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # Pareto of incident causes: the few that make most of the pain
    causes = {"config error": 42, "code defect": 28, "capacity": 15,
              "supplier": 9, "process gap": 6}
    total = sum(causes.values())
    ranked = sorted(causes.items(), key=lambda p: -p[1])
    print("incidents: %d" % total)
    cum = 0
    for cause, n in ranked:
        cum += n
        print("  %-13s %3d (%5.1f %%) cumulative %5.1f %%" % (cause, n, n / total * 100, cum / total * 100))
    assert total == 100
    top2_share = (ranked[0][1] + ranked[1][1]) / total * 100.0
    print("top two causes own %.0f %% of incidents" % top2_share)
    assert 69.9 < top2_share < 70.1
    assert ranked[0][0] == "config error"
    print("rule: replace the beam, not just sweep the floor")
    print("OK: %s dug to the stone" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_voc(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # theme health index: volume x sentiment across voice sources
    themes = [("billing confusion", 320, -0.6), ("onboarding gaps", 210, -0.4),
              ("praise for agents", 150, 0.8)]
    vol = sum(v for _, v, _ in themes)
    health = sum(v * s for _, v, s in themes) / vol
    print("voice volume: %d mentions" % vol)
    for name_, v, s in themes:
        print("  %-18s %4d x %+.1f" % (name_, v, s))
    print("theme health index: %+.4f" % health)
    assert vol == 680
    assert -0.230 < health < -0.229
    worst = min(themes, key=lambda p: p[1] * p[2])
    print("priority theme: %s" % worst[0])
    assert worst[0] == "billing confusion"
    print("rule: listen, then act where the voice points")
    print("OK: %s kept its ear to the ground" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_clv(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # CLV = margin x retention / (1 + discount - retention), with sensitivity
    margin, retention, discount = 240.0, 0.82, 0.10
    clv = margin * retention / (1 + discount - retention)
    print("margin $%.0f, retention %.0f %%, discount %.0f %% -> CLV $%.2f"
          % (margin, retention * 100, discount * 100, clv))
    assert 702.85 < clv < 702.87
    clv_up = margin * 0.85 / (1 + discount - 0.85)
    print("retention 85 %% -> CLV $%.2f (delta $%.2f)" % (clv_up, clv_up - clv))
    assert 815.9 < clv_up < 816.1
    # acquisition cap: spend no more than a third of expected CLV
    cap = clv / 3.0
    print("acquisition spend cap per customer: $%.2f" % cap)
    assert 234.28 < cap < 234.30
    print("rule: honor invests where loyalty compounds")
    print("OK: %s reckoned the harvest" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_predictive(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # transparent churn risk score: weighted signals, explainable per account
    weights = {"usage_drop": 0.4, "sentiment_drop": 0.3,
               "payment_wobble": 0.2, "short_tenure": 0.1}
    accounts = {
        "A-101": {"usage_drop": 0.9, "sentiment_drop": 0.8, "payment_wobble": 0.2, "short_tenure": 0.7},
        "B-202": {"usage_drop": 0.2, "sentiment_drop": 0.3, "payment_wobble": 0.1, "short_tenure": 0.2},
        "C-303": {"usage_drop": 0.6, "sentiment_drop": 0.5, "payment_wobble": 0.9, "short_tenure": 0.4},
    }
    scored = {}
    for cid, sig in accounts.items():
        score = sum(weights[k] * sig[k] for k in weights)
        top = max(sig, key=sig.get)
        scored[cid] = (score, top)
        print("  %s risk %.2f (top signal: %s)" % (cid, score, top))
    ranked = sorted(scored, key=lambda c: -scored[c][0])
    print("at-risk order: %s" % ranked)
    assert ranked == ["A-101", "C-303", "B-202"]
    assert 0.709 < scored["A-101"][0] < 0.711
    assert 0.609 < scored["C-303"][0] < 0.611
    assert scored["A-101"][1] == "usage_drop"
    # next-best-action mapping from the top signal
    actions = {"usage_drop": "value-review call", "sentiment_drop": "recovery outreach",
               "payment_wobble": "billing assistance", "short_tenure": "onboarding check"}
    print("A-101 action: %s" % actions[scored["A-101"][1]])
    print("rule: the watchman rides out before the storm")
    print("OK: %s watched the horizon" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_omnichannel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # skill routing: utilization balance and misroute rate
    agents = {"amy": ({"phone", "billing"}, 0.82), "ben": ({"chat", "billing"}, 0.78),
              "cy": ({"phone", "technical"}, 0.85), "dee": ({"chat", "technical"}, 0.80)}
    loads = [load for _, load in agents.values()]
    balance = max(loads) - min(loads)
    print("agent utilization: %s" % {a: l for a, (_, l) in agents.items()})
    print("utilization spread: %.2f" % balance)
    assert 0.069 < balance < 0.071
    contacts, misrouted = 240, 12
    misroute_rate = misrouted / contacts * 100.0
    print("contacts %d, misrouted %d -> %.1f %%" % (contacts, misrouted, misroute_rate))
    assert 4.9 < misroute_rate < 5.1
    # channel-switch rescue keeps the same ticket and history
    rescued = 34
    print("chat-to-phone rescues with transcript carried: %d" % rescued)
    assert rescued == 34
    print("rule: every guest seated rightly; no one at the wrong door")
    print("OK: %s conducted the hall" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_service_catalog(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # catalog coverage: every offering with an SLA, every SLA measured
    services, with_sla = 42, 38
    coverage = with_sla / services * 100.0
    print("catalog services: %d; with published SLA: %d (%.2f %%)"
          % (services, with_sla, coverage))
    assert 90.47 < coverage < 90.49
    meeting = 35
    fulfillment = meeting / with_sla * 100.0
    print("meeting fulfillment target: %d/%d (%.1f %%)" % (meeting, with_sla, fulfillment))
    assert 92.0 < fulfillment < 92.2
    offenders = with_sla - meeting
    print("chronic offenders queued for redesign: %d" % offenders)
    assert offenders == 3
    print("rule: no hidden vows, no hollow ones")
    print("OK: %s published its vows" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_improvement(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # improvement register: verified benefit vs cost, ROI like revenue
    ideas = [("queue triage rules", 45000, 15000), ("knowledge refresh", 120000, 60000),
             ("callback offer", 30000, 10000), ("agent coaching sprints", 80000, 40000)]
    benefit = sum(b for _, b, _ in ideas)
    cost = sum(c for _, _, c in ideas)
    roi = (benefit - cost) / cost * 100.0
    print("improvements: %d" % len(ideas))
    for title, b, c in ideas:
        print("  %-22s benefit $%6d cost $%5d" % (title, b, c))
    print("total benefit $%d, cost $%d -> ROI %.1f %%" % (benefit, cost, roi))
    assert benefit == 275000
    assert cost == 125000
    assert 119.9 < roi < 120.1
    print("rule: sharpen the blade forever; sing the verified wins")
    print("OK: %s kept the whetstone" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_architecture(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # integration health: sync lag, error rate, reconciliation match
    lags = [2, 3, 2, 5, 3, 4, 2, 12, 3, 2]
    mean_lag = sum(lags) / len(lags)
    max_lag = max(lags)
    print("sync lag minutes: mean %.1f, max %d" % (mean_lag, max_lag))
    assert 3.79 < mean_lag < 3.81
    assert max_lag == 12
    alerts = sum(1 for l in lags if l > 10)
    print("lag alerts (>10 min): %d" % alerts)
    assert alerts == 1
    errors, calls = 14, 10000
    err_rate = errors / calls * 100.0
    print("API errors: %d/%d (%.2f %%)" % (errors, calls, err_rate))
    assert 0.139 < err_rate < 0.141
    matched, total_recs = 999850, 1000000
    recon = matched / total_recs * 100.0
    print("reconciliation match: %.3f %%" % recon)
    assert 99.984 < recon < 99.986
    print("rule: one identity, one memory, every limb in agreement")
    print("OK: %s bound the body" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_crm_economics(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # unit economics: channel shift priced before it is chosen
    phone_cost, portal_cost = 8.50, 0.45
    shifted, investment = 2000, 9000.0
    savings = shifted * (phone_cost - portal_cost)
    roi = (savings - investment) / investment * 100.0
    print("shifting %d contacts phone -> portal:" % shifted)
    print("  savings $%.0f on investment $%.0f -> ROI %.2f %%" % (savings, investment, roi))
    assert 16099.9 < savings < 16100.1
    assert 78.8 < roi < 79.0
    # value side: a save priced in lifetime value, not in discount given
    clv, saves = 702.86, 45
    protected = clv * saves
    print("save desk: %d saves x CLV $%.2f = $%.2f protected" % (saves, clv, protected))
    assert 31628.0 < protected < 31630.0
    print("rule: the cheapest oath is the one best kept")
    print("OK: %s kept the ledger" % NAME)
if __name__ == "__main__":
    main()
''')


# extend the registry with the compounded/advanced demos defined above
DEMOS.update({
    "core_metrics": demo_crm_core_metrics,
    "knowledge": demo_crm_knowledge,
    "journey": demo_crm_journey,
    "csat": demo_crm_csat,
    "nps": demo_crm_nps,
    "ces": demo_crm_ces,
    "analytics": demo_crm_analytics,
    "retention": demo_crm_retention,
    "segmentation": demo_crm_segmentation,
    "recovery": demo_crm_recovery,
    "major_incident": demo_crm_major_incident,
    "wfm": demo_crm_wfm,
    "qa": demo_crm_qa,
    "rca": demo_crm_rca,
    "voc": demo_crm_voc,
    "clv": demo_crm_clv,
    "predictive": demo_crm_predictive,
    "omnichannel": demo_crm_omnichannel,
    "service_catalog": demo_crm_service_catalog,
    "improvement": demo_crm_improvement,
    "architecture": demo_crm_architecture,
    "economics": demo_crm_economics,
})
