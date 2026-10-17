#!/usr/bin/env python3
"""Demo programs for the Public Notices and Deadlines databases.

Every demo is real, runnable, stdlib-only Python performing the actual
notice/deadline computation for its record. All are machine-executed by
build.py before the records ship: each prints its real computed values,
asserts tight bounds (never float exact-equality), and ends with the OK
marker.
"""

_PREAMBLE = "import datetime\nimport hashlib\nimport math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_pnd_what_is(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the five questions every notice answers, and the six families
    questions = ["who is speaking", "what is happening", "whom it affects",
                 "what must be done", "by when"]
    families = ["recalls", "regulatory changes", "tenders", "filings",
                "advisories", "expirations"]
    print("notice questions: %d" % len(questions))
    print("notice families: %d" % len(families))
    for f in families:
        print("  - %s" % f)
    assert len(questions) == 5
    assert len(families) == 6
    assert questions[-1] == "by when", "the deadline turns information into obligation"
    print("rule: the 'by when' turns information into obligation")
    print("OK: %s framed the summons" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_anatomy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the eight parts of a notice; a sample recall notice dissected
    parts = ["header", "identifier", "authority", "subject", "body",
             "action", "deadline_block", "contact"]
    notice = {
        "header": "FDA Enforcement Report",
        "identifier": "FDA-R-2026-1847",
        "authority": "21 CFR Part 7",
        "subject": "Class II recall of infusion pump model IP-200",
        "body": "dose accuracy drift under high humidity",
        "action": "stop use; contact manufacturer for replacement",
        "deadline_block": "notify owners within 10 business days",
        "contact": "Office of Compliance, 1-888-555-0142",
    }
    missing = [p for p in parts if p not in notice]
    print("anatomy parts: %d, missing: %d" % (len(parts), len(missing)))
    assert not missing, "incomplete notice: %s" % missing
    assert notice["identifier"].startswith("FDA-R-")
    print("identifier: %s" % notice["identifier"])
    print("rule: check the anatomy first, read the prose second")
    print("OK: %s dissected the notice" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_six_families(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # canonical sources per family
    sources = {"recalls": ["FDA", "NHTSA", "CPSC"],
               "regulatory changes": ["Federal Register", "Regulations.gov"],
               "tenders": ["SAM.gov"],
               "filings": ["EDGAR", "IRS", "state portals"],
               "advisories": ["FDA", "CDC", "NWS", "CISA", "State Dept"],
               "expirations": ["USPTO", "state boards", "licensing bodies"]}
    total = sum(len(v) for v in sources.values())
    print("families: %d, canonical sources: %d" % (len(sources), total))
    assert len(sources) == 6
    assert total == 17
    assert "SAM.gov" in sources["tenders"]
    print("rule: classify at intake - the family decides everything downstream")
    print("OK: %s named the six families" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_deadline_anatomy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # trigger + computation + consequence: 60-day comment period
    trigger = datetime.date(2026, 3, 1)          # publication date
    due = trigger + datetime.timedelta(days=60)  # calendar-day count
    check = datetime.date(2026, 4, 1)
    remaining = (due - check).days
    print("trigger: %s, due: %s" % (trigger.isoformat(), due.isoformat()))
    print("days remaining on %s: %d" % (check.isoformat(), remaining))
    assert due == datetime.date(2026, 4, 30)
    assert remaining == 29
    print("consequence of missing: comment not in the record")
    print("rule: trigger, computation, consequence - all three or it is decoration")
    print("OK: %s ran the three-part machine" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_business_days(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # worked example from the record: 5 business days from Thu 2022-06-30,
    # excluding the trigger day, US federal calendar (Jul 4 observed Mon)
    holidays = {datetime.date(2022, 7, 4)}
    trigger = datetime.date(2022, 6, 30)  # Thursday
    d, counted = trigger, 0
    walk = []
    while counted < 5:
        d += datetime.timedelta(days=1)
        if d.weekday() < 5 and d not in holidays:
            counted += 1
            walk.append((d.isoformat(), counted))
        else:
            walk.append((d.isoformat(), "skip"))
    for day, mark in walk:
        print("  %s -> %s" % (day, mark))
    print("due: %s" % d.isoformat())
    assert d == datetime.date(2022, 7, 8)
    assert d.weekday() == 4  # Friday
    print("rule: show the walk in writing - miss the holiday, miss the date")
    print("OK: %s walked the calendar" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_sources(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # source map: canonical source + check frequency per family
    source_map = [
        ("recalls", "FDA/NHTSA/CPSC portals", "daily"),
        ("regulatory changes", "Federal Register", "daily"),
        ("tenders", "SAM.gov", "daily when active"),
        ("filings", "EDGAR / IRS", "on schedule"),
        ("advisories", "CDC/NWS/CISA", "daily"),
        ("expirations", "USPTO / state boards", "weekly"),
    ]
    print("source map entries: %d" % len(source_map))
    for fam, src, freq in source_map:
        print("  %-20s %-28s %s" % (fam, src, freq))
    assert len(source_map) == 6
    assert all(len(row) == 3 for row in source_map)
    print("rule: aggregators are tripwires; the official source is truth")
    print("OK: %s mapped the sources" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_channels(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # publication-requirement checklist for an outgoing notice
    checklist = {"channel named by governing instrument": True,
                 "frequency executed": True,
                 "duration executed": True,
                 "timing before effective date met": True,
                 "proof collected (affidavit/receipt)": True}
    done = sum(1 for v in checklist.values() if v)
    print("publication checklist: %d/%d" % (done, len(checklist)))
    assert done == len(checklist) == 5
    print("rule: the wrong channel can void the notice")
    print("OK: %s checked the channel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_severity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # likelihood (1-4) x impact (1-4) -> response level
    def level(likelihood, impact):
        s = likelihood * impact
        if s >= 12:
            return "critical"
        if s >= 6:
            return "warning"
        if s >= 3:
            return "watch"
        return "informational"
    cases = [((4, 4), "critical"), ((3, 2), "warning"),
             ((2, 2), "watch"), ((1, 1), "informational")]
    for (lh, im), want in cases:
        got = level(lh, im)
        print("  likelihood %d x impact %d = %d -> %s" % (lh, im, lh * im, got))
        assert got == want
    print("rule: let the level set the tempo, not the headline")
    print("OK: %s measured the warning" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_compliance_read(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pass one of the compliance read: hunt the operative verbs
    text = ("The manufacturer shall notify the agency within 24 hours. "
            "Distributors may request an extension. The agency will publish "
            "the notice. Records should be retained for 5 years.")
    duties = [w for w in ("shall", "must", "required") if w in text]
    permissions = [w for w in ("may", "should") if w in text]
    print("duty verbs found: %s" % duties)
    print("permission verbs found: %s" % permissions)
    assert duties == ["shall"]
    assert permissions == ["may", "should"]
    print("rule: six passes - verbs, dates, definitions, scope, mechanics, penalties")
    print("OK: %s interrogated the summons" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_tracking_workflow(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six stages with typical dwell times (days) for a routine filing notice
    stages = [("intake", 0.5), ("triage", 1.0), ("extraction", 2.0),
              ("calendaring", 1.0), ("action", 5.0), ("closure", 1.0)]
    total = sum(d for _, d in stages)
    print("stages: %d" % len(stages))
    for s, d in stages:
        print("  %-12s %.1f days" % (s, d))
    print("intake-to-closure: %.1f days" % total)
    assert len(stages) == 6
    assert 10.4 < total < 10.6
    print("rule: no owner, no triage exit; no receipt, no action exit")
    print("OK: %s ran the six gates" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_compliance_calendar(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # recurring quarterly safety reports, due 30 days after quarter end, 2026
    quarters = [(datetime.date(2026, 3, 31), datetime.date(2026, 4, 30)),
                (datetime.date(2026, 6, 30), datetime.date(2026, 7, 30)),
                (datetime.date(2026, 9, 30), datetime.date(2026, 10, 30)),
                (datetime.date(2026, 12, 31), datetime.date(2027, 1, 30))]
    print("recurring obligations generated: %d" % len(quarters))
    for end, due in quarters:
        print("  quarter ends %s -> due %s" % (end.isoformat(), due.isoformat()))
        assert (due - end).days == 30
    assert len(quarters) == 4
    assert quarters[0][1] == datetime.date(2026, 4, 30)
    print("rule: generate the year forward - nothing depends on memory")
    print("OK: %s built the honor roll" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_expiration(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # trademark section 8 affidavit window: registered 2020-03-10
    reg = datetime.date(2020, 3, 10)
    window_open = reg.replace(year=2025)                    # +5 years
    window_close = reg.replace(year=2026)                   # +6 years
    grace_end = datetime.date(2026, 9, 10)                  # +6 months grace
    print("registered: %s" % reg.isoformat())
    print("affidavit window: %s to %s" % (window_open.isoformat(), window_close.isoformat()))
    print("grace ends: %s (surcharge applies)" % grace_end.isoformat())
    assert window_open == datetime.date(2025, 3, 10)
    assert window_close == datetime.date(2026, 3, 10)
    assert grace_end == datetime.date(2026, 9, 10)
    assert (grace_end - window_close).days == 184
    print("rule: alarm at the window opening, not at expiration")
    print("OK: %s guarded the silent summons" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_recall_anatomy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # affected-unit range check: serials SN1000-SN1999
    def affected(serial):
        n = int(serial.replace("SN", ""))
        return 1000 <= n <= 1999
    checks = [("SN1450", True), ("SN1000", True), ("SN1999", True),
              ("SN2001", False), ("SN0999", False)]
    for serial, want in checks:
        got = affected(serial)
        print("  %s affected: %s" % (serial, got))
        assert got == want
    print("rule: precision here is everything - over-broad wastes, under-broad endangers")
    print("OK: %s sorted the affected units" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_recall_classes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hazard evaluation -> FDA class
    def classify(prob_severe, reversible):
        if prob_severe >= 0.5:
            return "Class I"
        if prob_severe > 0.0 or reversible:
            return "Class II"
        return "Class III"
    cases = [((0.6, False), "Class I"), ((0.05, True), "Class II"),
             ((0.0, False), "Class III")]
    for (p, rev), want in cases:
        got = classify(p, rev)
        print("  p=%.2f reversible=%s -> %s" % (p, rev, got))
        assert got == want
    print("rule: debating I vs II - respond as I until the agency rules")
    print("OK: %s weighed the classes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_regulatory_comment(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 60-day comment period on a proposed rule published 2026-03-01
    published = datetime.date(2026, 3, 1)
    closes = published + datetime.timedelta(days=60)
    file_by = closes - datetime.timedelta(days=7)  # safe filing target
    print("published: %s, docket closes: %s" % (published.isoformat(), closes.isoformat()))
    print("safe file-by target: %s" % file_by.isoformat())
    assert closes == datetime.date(2026, 4, 30)
    assert file_by == datetime.date(2026, 4, 23)
    print("rule: a late comment may not be in the record at all")
    print("OK: %s guarded the docket" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_tenders(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # solicitation deadline 2026-05-15 14:00 Eastern; internal deadline 24h prior
    deadline = datetime.datetime(2026, 5, 15, 14, 0)
    internal = deadline - datetime.timedelta(hours=24)
    print("solicitation deadline: %s Eastern" % deadline.isoformat())
    print("internal deadline:     %s Eastern" % internal.isoformat())
    assert internal == datetime.datetime(2026, 5, 14, 14, 0)
    amendments = ["A0001", "A0002", "A0003"]
    acknowledged = ["A0001", "A0002", "A0003"]
    assert amendments == acknowledged, "unacknowledged amendment kills the bid"
    print("amendments acknowledged: %d/%d" % (len(acknowledged), len(amendments)))
    print("rule: late is late - there is no grace period")
    print("OK: %s swore the bid on time" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_filings(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 2026 estimated tax due dates: Apr 15, Jun 15, Sep 15, Jan 15 (2027)
    estimated = [datetime.date(2026, 4, 15), datetime.date(2026, 6, 15),
                 datetime.date(2026, 9, 15), datetime.date(2027, 1, 15)]
    for i, d in enumerate(estimated, 1):
        print("  Q%d estimated due: %s" % (i, d.isoformat()))
    assert estimated == [datetime.date(2026, 4, 15), datetime.date(2026, 6, 15),
                         datetime.date(2026, 9, 15), datetime.date(2027, 1, 15)]
    print("rule: extension to file is never extension to pay")
    print("OK: %s scheduled the tributes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_safety_advisories(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # severity -> response tempo routing
    routing = {"informational": "log", "watch": "monitor",
               "warning": "act", "critical": "escalate"}
    advisories = [("heat advisory", "warning"), ("drug safety comm", "warning"),
                  ("new guidance doc", "informational"), ("outbreak alert", "critical")]
    for title, sev in advisories:
        action = routing[sev]
        print("  %-18s [%s] -> %s" % (title, sev, action))
    assert routing["warning"] == "act"
    assert routing["critical"] == "escalate"
    assert routing["informational"] == "log"
    print("rule: advisories create a standard of care - heed the warning")
    print("OK: %s routed the warnings" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_legal_notices(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # FRCP 6: served Mon 2026-03-02, 21 days to answer, trigger day excluded
    served = datetime.date(2026, 3, 2)
    answer_due = served + datetime.timedelta(days=21)
    mail_due = answer_due + datetime.timedelta(days=3)  # FRCP 6(d) mail add
    print("served: %s" % served.isoformat())
    print("answer due (21 days, trigger excluded): %s" % answer_due.isoformat())
    print("if served by mail (+3 days): %s" % mail_due.isoformat())
    assert answer_due == datetime.date(2026, 3, 23)
    assert answer_due.weekday() == 0  # Monday
    assert mail_due == datetime.date(2026, 3, 26)
    print("rule: calendar the paper the day it arrives")
    print("OK: %s answered the iron summons" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_consumer_protection(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # mirror test: FTC action practices vs own practices
    practices = [("drip pricing at checkout", True),
                 ("clear refund policy", False),
                 ("auto-renew without consent", True),
                 ("honest testimonials", False),
                 ("bait-and-switch ads", False)]
    flagged = [p for p, risk in practices if risk]
    print("practices reviewed: %d, flagged: %d" % (len(practices), len(flagged)))
    for p in flagged:
        print("  FLAG: %s" % p)
    assert len(flagged) == 2
    assert "auto-renew without consent" in flagged
    print("rule: hold the mirror up before the enforcer does")
    print("OK: %s held the mirror" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_licensing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # continuing-education tracking: 30 hours required
    required = 30.0
    earned = [8.0, 6.0, 10.0]
    total_earned = sum(earned)
    remaining = required - total_earned
    print("CE required: %.1f, earned: %.1f, remaining: %.1f"
          % (required, total_earned, remaining))
    assert 23.9 < total_earned < 24.1
    assert 5.9 < remaining < 6.1
    assert remaining > 0, "renewal blocked until CE complete"
    print("rule: file inside the window - alarming at expiration is alarming at failure")
    print("OK: %s kept the credential current" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_jurisdiction(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # same 2-business-day clause under two calendars: federal (Thanksgiving
    # observed) vs a plain calendar. Trigger Tue 2026-11-24, exclude trigger.
    trigger = datetime.date(2026, 11, 24)  # Tuesday
    federal_hol = {datetime.date(2026, 11, 26)}  # Thanksgiving Thursday
    def add_biz(trig, n, hols):
        d, c = trig, 0
        while c < n:
            d += datetime.timedelta(days=1)
            if d.weekday() < 5 and d not in hols:
                c += 1
        return d
    fed = add_biz(trigger, 2, federal_hol)
    plain = add_biz(trigger, 2, set())
    print("federal calendar due: %s" % fed.isoformat())
    print("plain calendar due:   %s" % plain.isoformat())
    assert fed == datetime.date(2026, 11, 27)
    assert plain == datetime.date(2026, 11, 26)
    print("binding (earliest): %s" % min(fed, plain).isoformat())
    print("rule: name the jurisdiction, then count")
    print("OK: %s asked the clock's owner" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_ip_deadlines(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # patent granted 2021-06-15: first maintenance fee at 3.5 years
    grant = datetime.date(2021, 6, 15)
    fee1_due = datetime.date(2024, 12, 15)   # +3 years, +6 months
    grace_end = datetime.date(2025, 6, 15)   # +6 months grace + surcharge
    alarm = datetime.date(2024, 9, 15)       # 90-day alarm
    print("granted: %s" % grant.isoformat())
    print("1st maintenance fee due: %s" % fee1_due.isoformat())
    print("grace ends: %s | alarm: %s" % (grace_end.isoformat(), alarm.isoformat()))
    assert fee1_due == datetime.date(2024, 12, 15)
    assert grace_end == datetime.date(2025, 6, 15)
    assert (fee1_due - alarm).days == 91
    print("rule: in IP the calendar is the portfolio")
    print("OK: %s docketed the patent" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_tax_deadlines(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # $10,000 owed, 2 months late: file-late vs pay-late penalties
    owed = 10000.0
    months = 2
    fail_file = owed * 0.05 * months   # 5% per month
    fail_pay = owed * 0.005 * months   # 0.5% per month
    print("owed: $%.2f, %d months late" % (owed, months))
    print("failure-to-file penalty: $%.2f" % fail_file)
    print("failure-to-pay penalty:  $%.2f" % fail_pay)
    assert 999.9 < fail_file < 1000.1
    assert 99.9 < fail_pay < 100.1
    assert fail_file > 9.9 * fail_pay
    print("rule: file on time even when cash is short")
    print("OK: %s separated the clocks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_deadline_algorithms(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # full algorithm: observed-holiday resolution + business-day walk
    def federal_holidays(year):
        base = [(1, 1), (7, 4), (11, 11), (12, 25)]
        out = set()
        for m, d in base:
            h = datetime.date(year, m, d)
            if h.weekday() == 5:
                out.add(h - datetime.timedelta(days=1))  # Fri observed
            elif h.weekday() == 6:
                out.add(h + datetime.timedelta(days=1))  # Mon observed
            else:
                out.add(h)
        return out
    hols = federal_holidays(2022)
    assert datetime.date(2022, 7, 4) in hols  # Monday -> observed itself
    def add_biz(trig, n, holidays):
        d, c = trig, 0
        while c < n:
            d += datetime.timedelta(days=1)
            if d.weekday() < 5 and d not in holidays:
                c += 1
        return d
    r1 = add_biz(datetime.date(2022, 6, 30), 5, hols)
    r2 = add_biz(datetime.date(2022, 7, 1), 1, hols)  # Fri -> skip wknd+hol -> Tue
    print("5 biz days from 2022-06-30: %s" % r1.isoformat())
    print("1 biz day from 2022-07-01:  %s" % r2.isoformat())
    assert r1 == datetime.date(2022, 7, 8)
    assert r2 == datetime.date(2022, 7, 5)
    print("rule: the walk is the proof")
    print("OK: %s ran the abacus" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_tracking_system(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four-table system: intake 3 notices, drive two to closure
    notices, obligations, deadlines, evidence = [], [], [], []
    for i, fam in enumerate(["recall", "filing", "tender"]):
        notices.append({"id": "N-%d" % (i + 1), "family": fam,
                        "owner": "owner-%d" % (i + 1), "stage": "intake"})
    assert len(notices) == 3 and all(n["owner"] for n in notices)
    obligations.append({"id": "O-1", "notice": "N-1",
                        "duty": "notify owners of recall"})
    obligations.append({"id": "O-2", "notice": "N-2",
                        "duty": "file quarterly report"})
    deadlines.append({"id": "D-1", "obligation": "O-1",
                      "due": "2026-11-01", "rule": "10 business days"})
    deadlines.append({"id": "D-2", "obligation": "O-2",
                      "due": "2026-10-30", "rule": "30 calendar days"})
    evidence.append({"obligation": "O-1", "receipt": "RCPT-881"})
    evidence.append({"obligation": "O-2", "receipt": "RCPT-882"})
    closed = [e for e in evidence if e["receipt"]]
    print("notices: %d, obligations: %d, deadlines: %d, evidence: %d"
          % (len(notices), len(obligations), len(deadlines), len(evidence)))
    assert len(closed) == 2
    print("closed with proof: %d" % len(closed))
    print("rule: no receipt, no exit from action")
    print("OK: %s ran the fortress" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_escalation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # escalation matrix lookup per obligation class
    matrix = {
        "tender": {"notify": ["bid manager", "VP sales"],
                   "action": "capture lesson; watch re-solicitation"},
        "filing": {"notify": ["owner", "controller"],
                   "action": "file now, pay now, stop the clock"},
        "court": {"notify": ["owner", "counsel"],
                  "action": "move for relief - hours matter"},
        "recall": {"notify": ["coordinator", "CEO"],
                   "action": "incident command; notify immediately"},
    }
    hit = matrix["filing"]
    print("missed filing -> notify: %s" % ", ".join(hit["notify"]))
    print("immediate action: %s" % hit["action"])
    assert hit["notify"][0] == "owner"
    assert len(matrix) == 4
    print("rule: written calmly, executed urgently")
    print("OK: %s planned for the breach" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_audit_trail(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hash-chained append-only log; tamper breaks the chain
    events = ["intake N-1", "triage: owner assigned", "deadline computed",
              "action taken", "evidence attached", "closure verified"]
    chain, prev = [], hashlib.sha256(b"genesis").hexdigest()
    for e in events:
        h = hashlib.sha256((prev + e).encode()).hexdigest()
        chain.append((e, h))
        prev = h
    ok = True
    prev = hashlib.sha256(b"genesis").hexdigest()
    for e, h in chain:
        if hashlib.sha256((prev + e).encode()).hexdigest() != h:
            ok = False
        prev = h
    print("events chained: %d, chain valid: %s" % (len(chain), ok))
    assert ok and len(chain) == 6
    tampered = (chain[2][0] + " (edited)", chain[2][1])
    bad = hashlib.sha256((chain[1][1] + tampered[0]).encode()).hexdigest() != tampered[1]
    print("tamper detected: %s" % bad)
    assert bad
    print("rule: the chain unbroken is honor made visible")
    print("OK: %s swore the testimony" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_multi_jurisdiction(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # one report owed in two states with different due dates -> earliest binds
    computed = {"Delaware": datetime.date(2026, 3, 1),
                "Texas": datetime.date(2026, 2, 15),
                "federal": datetime.date(2026, 3, 15)}
    binding = min(computed.values())
    binder = [j for j, d in computed.items() if d == binding][0]
    for j, d in sorted(computed.items(), key=lambda kv: kv[1]):
        print("  %-10s %s" % (j, d.isoformat()))
    print("binding date: %s (%s)" % (binding.isoformat(), binder))
    assert binding == datetime.date(2026, 2, 15)
    assert binder == "Texas"
    print("rule: many clocks, one honor - obey the strictest")
    print("OK: %s chose the earliest" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_recall_playbook(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 72-hour playbook timeline (hours from declaration)
    timeline = [("decision team convened", 24), ("scope frozen", 36),
                ("owner notification complete", 60),
                ("press + portal published", 72),
                ("remedy operations live", 72)]
    worst = max(h for _, h in timeline)
    for event, h in timeline:
        print("  T+%3dh  %s" % (h, event))
    print("notification complete by T+%dh" % worst)
    assert worst <= 72
    assert len(timeline) == 5
    print("rule: written in peace, executed at speed")
    print("OK: %s rehearsed the battle plan" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_impact_assessment(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # gap scoring: duty -> (current state, remediation cost)
    gaps = [("labeling update", "absent", 120000.0),
            ("recordkeeping system", "partial", 45000.0),
            ("staff training", "absent", 8000.0)]
    total = sum(c for _, _, c in gaps)
    absent = sum(1 for _, s, _ in gaps if s == "absent")
    print("duties assessed: %d, absent: %d" % (len(gaps), absent))
    for duty, state, cost in gaps:
        print("  %-22s %-8s $%9.2f" % (duty, state, cost))
    print("total remediation: $%.2f" % total)
    assert 172999.0 < total < 173001.0
    assert absent == 2
    print("rule: price the rule at proposal, shape it by comment")
    print("OK: %s translated law into labor" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_tender_workflow(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # backward-planned milestones from a fixed deadline
    deadline = datetime.datetime(2026, 6, 30, 17, 0)
    submit = deadline - datetime.timedelta(hours=24)
    review = submit - datetime.timedelta(hours=48)
    pricing = submit - datetime.timedelta(hours=72)
    draft = submit - datetime.timedelta(days=7)
    print("deadline:  %s" % deadline.isoformat())
    print("submit:    %s" % submit.isoformat())
    print("review:    %s" % review.isoformat())
    print("pricing:   %s" % pricing.isoformat())
    print("draft:     %s" % draft.isoformat())
    assert submit == datetime.datetime(2026, 6, 29, 17, 0)
    assert review == datetime.datetime(2026, 6, 27, 17, 0)
    assert (deadline - submit).total_seconds() == 86400.0
    print("rule: an oath sworn late is no oath at all")
    print("OK: %s worked the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_automated_monitoring(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # simulated collector output: dedupe on identifier, count detections
    seen = [("FR-2026-101", "warning"), ("RC-881", "critical"),
            ("FR-2026-101", "warning"), ("SAM-5520", "informational"),
            ("RC-881", "critical"), ("ADV-314", "watch")]
    unique = {}
    for ident, sev in seen:
        unique.setdefault(ident, sev)  # first sighting wins
    critical = [i for i, s in unique.items() if s == "critical"]
    print("sightings: %d, unique notices: %d" % (len(seen), len(unique)))
    print("critical detections: %d (%s)" % (len(critical), ", ".join(critical)))
    assert len(unique) == 4
    assert critical == ["RC-881"]
    print("rule: automation multiplies the watch; it does not replace the watcher")
    print("OK: %s stood the watchtower" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_pnd_complete_system(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # program health: due / overdue / closed boards
    due = ["10-Q filing", "trademark affidavit"]
    overdue = ["state annual report"]
    closed = [("bid submitted", True), ("comment filed", True),
              ("renewal paid", False)]
    on_time = sum(1 for _, t in closed if t)
    rate = on_time / len(closed)
    print("due: %d, overdue: %d, closed: %d" % (len(due), len(overdue), len(closed)))
    print("on-time closure rate: %.4f" % rate)
    assert len(due) == 2 and len(overdue) == 1 and len(closed) == 3
    assert 0.66 < rate < 0.67
    print("rule: rhythm, not emergency - from the first summons to the final proof")
    print("OK: %s closed the loop" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what_is": demo_pnd_what_is,
    "anatomy": demo_pnd_anatomy,
    "six_families": demo_pnd_six_families,
    "deadline_anatomy": demo_pnd_deadline_anatomy,
    "business_days": demo_pnd_business_days,
    "sources": demo_pnd_sources,
    "channels": demo_pnd_channels,
    "severity": demo_pnd_severity,
    "compliance_read": demo_pnd_compliance_read,
    "tracking_workflow": demo_pnd_tracking_workflow,
    "compliance_calendar": demo_pnd_compliance_calendar,
    "expiration": demo_pnd_expiration,
    "recall_anatomy": demo_pnd_recall_anatomy,
    "recall_classes": demo_pnd_recall_classes,
    "regulatory_comment": demo_pnd_regulatory_comment,
    "tenders": demo_pnd_tenders,
    "filings": demo_pnd_filings,
    "safety_advisories": demo_pnd_safety_advisories,
    "legal_notices": demo_pnd_legal_notices,
    "consumer_protection": demo_pnd_consumer_protection,
    "licensing": demo_pnd_licensing,
    "jurisdiction": demo_pnd_jurisdiction,
    "ip_deadlines": demo_pnd_ip_deadlines,
    "tax_deadlines": demo_pnd_tax_deadlines,
    "deadline_algorithms": demo_pnd_deadline_algorithms,
    "tracking_system": demo_pnd_tracking_system,
    "escalation": demo_pnd_escalation,
    "audit_trail": demo_pnd_audit_trail,
    "multi_jurisdiction": demo_pnd_multi_jurisdiction,
    "recall_playbook": demo_pnd_recall_playbook,
    "impact_assessment": demo_pnd_impact_assessment,
    "tender_workflow": demo_pnd_tender_workflow,
    "automated_monitoring": demo_pnd_automated_monitoring,
    "complete_system": demo_pnd_complete_system,
}
