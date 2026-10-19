#!/usr/bin/env python3
"""Parametric, machine-verified demo builders for the decades databases.

Every demo is real, runnable, stdlib-only Python. Expected values are
computed at build time and embedded as literals; the build executes every
demo and requires the OK marker.
"""
from datetime import date

REF = date(2026, 10, 18)


def _hdr(name, rid, group):
    return ('#!/usr/bin/env python3\n"""%s -- working demonstration.\n'
            'Record %s [%s]. Property of Justin Addam Higgins (JAH).\n"""\n'
            % (name, rid, group))


def demo_event(name, rid, group, dd):
    """Date-math demo for a dated history record. dd: dict(y,m,d[,rank])."""
    ev = date(dd["y"], dd["m"], dd["d"])
    dow = ev.strftime("%A")
    days = (REF - ev).days
    years = REF.year - ev.year - ((REF.month, REF.day) < (ev.month, ev.day))
    iso = ev.isoformat()
    sig = bool(dd.get("signature"))
    body = _hdr(name, rid, group)
    body += "from datetime import date\n\n\ndef main():\n"
    body += "    event = date(%d, %d, %d)\n" % (ev.year, ev.month, ev.day)
    body += "    ref = date(2026, 10, 18)\n"
    body += "    # 1. day of the week of the anchor date\n"
    body += "    dow = event.strftime(\"%A\")\n"
    body += "    assert dow == %r, dow\n" % dow
    body += "    # 2. days elapsed to the reference date\n"
    body += "    days = (ref - event).days\n"
    body += "    assert days == %d, days\n" % days
    body += "    assert days > 0, 'anchor must precede the reference date'\n"
    body += "    # 3. full years elapsed\n"
    body += ("    years = ref.year - event.year - "
             "((ref.month, ref.day) < (event.month, event.day))\n")
    body += "    assert years == %d, years\n" % years
    if sig:
        rank = int(dd.get("rank", 1))
        lev = round(years * rank / 34.0, 2)
        body += "    # 4. lesson leverage index: hindsight years x ladder depth\n"
        body += "    leverage = round(years * %d / 34.0, 2)\n" % rank
        body += "    assert leverage == %r, leverage\n" % lev
        body += "    print(\"lesson leverage index (years x rank / 34): %s\" % leverage)\n"
    body += "    print(\"event: %s\")\n" % name.replace('"', "'")
    body += "    print(\"anchor date: %s (a %s)\")\n" % (iso, dow)
    body += "    print(\"days to 2026-10-18: %d\")\n" % days
    body += "    print(\"full years elapsed: %d\")\n" % years
    body += "    print(\"OK: %s %s\")\n" % (rid, name.replace('"', "'"))
    body += "\n\nif __name__ == \"__main__\":\n    main()\n"
    return body


DEMOS = {"event": demo_event}
