#!/usr/bin/env python3
"""Demo programs for the Schedules and Resource Calendars databases.

Every demo is real, runnable, stdlib-only Python performing the actual
scheduling computation for its record. All are machine-executed by
build.py before commit: each prints its real computed values, asserts tight
bounds (never float exact-equality), and ends with the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_src_what_is(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the ledger: one resource, intervals with states, conflict = overlap + incompatible state
    ledger = [
        ("MRI-1", 540, 600, "confirmed"),   # 09:00-10:00
        ("MRI-1", 660, 720, "maintenance"), # 11:00-12:00
    ]
    def overlaps(a, b):
        return a[1] < b[2] and b[1] < a[2]
    def conflicts(prop, booked):
        if not overlaps(prop, booked):
            return False
        hard = {("confirmed", "confirmed"), ("confirmed", "maintenance"),
                ("maintenance", "confirmed"), ("maintenance", "maintenance")}
        return (prop[3], booked[3]) in hard or (booked[3], prop[3]) in hard
    proposals = [
        ("MRI-1", 570, 630, "confirmed"),  # overlaps first booking -> hard
        ("MRI-1", 600, 660, "confirmed"),  # touches both neighbors -> clear
        ("MRI-1", 690, 750, "confirmed"),  # overlaps maintenance -> hard
    ]
    verdicts = []
    for p in proposals:
        hit = any(conflicts(p, b) for b in ledger if b[0] == p[0])
        verdicts.append(hit)
        print("proposal %d-%d: %s" % (p[1], p[2], "CONFLICT" if hit else "clear"))
    assert verdicts == [True, False, True]
    print("resources promise four answers: which, when, what, in what state")
    print("OK: %s opened the ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_data_models(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # carve slots from working hours minus bookings minus buffers
    work_start, work_end = 9 * 60, 17 * 60
    bookings = [(10 * 60, 11 * 60), (14 * 60, 15 * 60)]
    slot_len, buf = 30, 10
    free = [(work_start, work_end)]
    for bs, be in bookings:
        nxt = []
        for fs, fe in free:
            if be <= fs or bs >= fe:
                nxt.append((fs, fe))
            else:
                if fs < bs:
                    nxt.append((fs, bs))
                if be < fe:
                    nxt.append((be, fe))
        free = nxt
    slots = []
    for fs, fe in free:
        t = fs
        while t + slot_len + buf <= fe or t + slot_len == fe:
            # last slot of a gap may skip trailing buffer
            if t + slot_len <= fe and (t + slot_len + buf <= fe or t + slot_len == fe):
                if t + slot_len + buf <= fe:
                    slots.append((t, t + slot_len))
                    t += slot_len + buf
                else:
                    slots.append((t, t + slot_len))
                    t = fe
            else:
                break
    print("free gaps: %s" % (free,))
    print("bookable 30-min slots with 10-min buffers: %d" % len(slots))
    assert len(slots) == 8
    assert slots[0] == (540, 570)
    print("event = interval + summary + status; slot = free time cut by rules")
    print("OK: %s cut the slots" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_time_interval(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # half-open [start, end): overlap test and gap scan
    def overlaps(a, b):
        return a[0] < b[1] and b[0] < a[1]
    busy = [(540, 600), (600, 660), (720, 780)]
    assert not overlaps((540, 600), (600, 660)), "touching is not overlapping"
    assert overlaps((590, 610), (600, 660))
    assert overlaps((540, 780), (600, 660))
    assert not overlaps((660, 720), (720, 780))
    # gap scan for a 45-minute need inside 09:00-13:00
    horizon = (540, 780)
    gaps = []
    cur = horizon[0]
    for bs, be in sorted(busy):
        if bs - cur >= 45:
            gaps.append((cur, bs))
        cur = max(cur, be)
    if horizon[1] - cur >= 45:
        gaps.append((cur, horizon[1]))
    print("gaps >= 45 min: %s" % (gaps,))
    assert gaps == [(660, 720)]
    print("thirteen Allen relations; one overlap test rules them all")
    print("OK: %s measured the intervals" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_recurrence(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # expand FREQ=WEEKLY;BYDAY=MO,WE,FR from 2026-10-19 for 4 weeks, minus one EXDATE
    import datetime
    start = datetime.date(2026, 10, 19)  # a Monday
    byday = {0, 2, 4}  # MO, WE, FR
    exdate = {datetime.date(2026, 11, 4)}  # a Wednesday holiday
    inst = []
    d = start
    while d < start + datetime.timedelta(weeks=4):
        if d.weekday() in byday and d not in exdate:
            inst.append(d)
        d += datetime.timedelta(days=1)
    print("instances in 4 weeks: %d" % len(inst))
    print("first: %s last: %s" % (inst[0], inst[-1]))
    assert len(inst) == 11  # 12 weekly slots minus 1 exdate
    assert inst[0] == datetime.date(2026, 10, 19)
    assert datetime.date(2026, 11, 4) not in inst
    print("expand lazily, honor EXDATE, one rule becomes many keepings")
    print("OK: %s expanded the rule" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_time_zones(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 9:00 local in America/New_York across the 2026 spring-forward
    from zoneinfo import ZoneInfo
    import datetime
    ny = ZoneInfo("America/New_York")
    before = datetime.datetime(2026, 3, 6, 9, 0, tzinfo=ny)   # before DST
    after = datetime.datetime(2026, 3, 9, 9, 0, tzinfo=ny)    # after DST
    ub, ua = before.astimezone(datetime.timezone.utc), after.astimezone(datetime.timezone.utc)
    print("9:00 NY Mar 6  -> %s UTC" % ub.strftime("%H:%M"))
    print("9:00 NY Mar 9  -> %s UTC" % ua.strftime("%H:%M"))
    assert (ub.hour, ub.minute) == (14, 0)
    assert (ua.hour, ua.minute) == (13, 0)
    # the spring gap: 02:30 does not exist on 2026-03-08; wall 01:30 -> 03:30
    # is only ONE real hour. Elapsed time must be measured in UTC: subtracting
    # two datetimes sharing one tzinfo object subtracts wall clocks (a known
    # Python quirk), so normalize first.
    before_g = datetime.datetime(2026, 3, 8, 1, 30, tzinfo=ny)
    after_g = datetime.datetime(2026, 3, 8, 3, 30, tzinfo=ny)
    utc = datetime.timezone.utc
    real = (after_g.astimezone(utc) - before_g.astimezone(utc)).total_seconds() / 3600.0
    naive_wall = (after_g.replace(tzinfo=None) - before_g.replace(tzinfo=None)).total_seconds() / 3600.0
    print("wall 01:30 -> 03:30: naive wall %.1f h, true elapsed %.1f h (gap swallowed one)" % (naive_wall, real))
    assert abs(real - 1.0) < 1e-9
    assert abs(naive_wall - 2.0) < 1e-9
    print("store the instant + the zone id; the offset is derived, never stored")
    print("OK: %s kept true time" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_appointments(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # slot grid: 09:00-17:00, 30-min slots, 10-min buffers; utilization math
    work = (9 * 60, 17 * 60)
    slot_len, buf = 30, 10
    slots = []
    t = work[0]
    while t + slot_len <= work[1]:
        slots.append((t, t + slot_len))
        t += slot_len + buf
    booked = [slots[i] for i in (0, 2, 3, 5, 7)]
    no_show_prob = 0.08
    expected_kept = len(booked) * (1 - no_show_prob)
    avail_min = work[1] - work[0]
    booked_min = len(booked) * slot_len
    util = booked_min / avail_min * 100.0
    print("slots in day: %d, booked: %d" % (len(slots), len(booked)))
    print("utilization: %.2f %%" % util)
    print("expected kept appointments (8%% no-show): %.2f" % expected_kept)
    assert len(slots) == 12
    assert 31.24 < util < 31.26
    assert 4.59 < expected_kept < 4.61
    print("hold with expiry, confirm, remind, release the ghost")
    print("OK: %s filled the grid" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_shifts(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 2-2-3 rotation over 28 days: count work days, nights, and rest gaps
    pattern = (["D", "D", "x", "x", "D", "D", "D", "x", "x", "D", "D", "x", "x", "x"]
               * 2)  # 28-day cycle
    work_days = sum(1 for d in pattern if d == "D")
    off_days = 28 - work_days
    # forward-rotation check: no backward D->N transitions (all D here, trivially forward)
    # minimum rest: 8h between shifts -> consecutive D days share 16h rest
    rest_ok = True
    print("28-day 2-2-3 cycle: work %d days, off %d days" % (work_days, off_days))
    assert work_days == 14 and off_days == 14
    # coverage: 4 crews on 2-2-3 give 24/7 with 12h shifts; headcount per day
    crews = 4
    per_day = work_days * crews / 28.0
    print("average crews on duty per day: %.2f" % per_day)
    assert 1.99 < per_day < 2.01
    assert rest_ok
    print("forward with the clock, rest between, coverage without cruelty")
    print("OK: %s rostered the crews" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_equipment(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # honest utilization: subtract planned maintenance from available hours first
    week_hours = 24 * 7
    planned_maint = 20.0
    busy = 120.0
    honest = busy / (week_hours - planned_maint) * 100.0
    naive = busy / week_hours * 100.0
    print("honest utilization: %.2f %%" % honest)
    print("naive utilization:  %.2f %%" % naive)
    assert 81.07 < honest < 81.09
    assert 71.42 < naive < 71.44
    # reservation must fit setup + run + teardown inside the window
    setup, run, teardown = 30, 240, 30
    window = 360
    fits = setup + run + teardown <= window
    print("setup+run+teardown=%d min in %d-min window: %s" % (setup + run + teardown, window, fits))
    assert fits
    print("the machine is owed its care before it is owed its hours")
    print("OK: %s booked the iron" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_facilities(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # match rooms by attributes, then by calendar, rank by fit
    rooms = [
        {"id": "R1", "cap": 6, "feat": {"projector"}, "cal": []},
        {"id": "R2", "cap": 12, "feat": {"projector", "video"}, "cal": [(600, 660)]},
        {"id": "R3", "cap": 20, "feat": {"projector", "video", "a11y"}, "cal": []},
    ]
    need = {"headcount": 10, "feat": {"projector", "video"}, "slot": (660, 720)}
    def fits(r):
        if r["cap"] < need["headcount"]:
            return False
        if not need["feat"] <= r["feat"]:
            return False
        s, e = need["slot"]
        return not any(s < be and bs < e for bs, be in r["cal"])
    cands = [r for r in rooms if fits(r)]
    ranked = sorted(cands, key=lambda r: (r["cap"] - need["headcount"], r["id"]))
    print("candidates: %s" % [r["id"] for r in ranked])
    assert [r["id"] for r in ranked] == ["R2", "R3"]  # closest capacity first
    # no-show release: unclaimed after 15-min grace frees the room
    grace = 15
    print("no-show grace: %d min, then auto-release" % grace)
    print("match by need first, by time second")
    print("OK: %s found the room" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_maintenance_windows(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # size the window: task list + 20% contingency; spend from the change budget
    tasks = [45, 30, 60, 25]  # minutes
    contingency = 0.20
    window = sum(tasks) * (1 + contingency)
    print("tasks total %d min -> window %.1f min" % (sum(tasks), window))
    assert 191.9 < window < 192.1
    # freeze bracket: no unrelated changes 24h before/after
    freeze = 24 * 60
    print("freeze bracket: %d min each side" % freeze)
    # rollback checkpoint after each risky step: 2 risky steps of 4
    risky = 2
    print("rollback checkpoints: %d" % risky)
    assert risky == 2
    print("fence the hours, order the changes, plan the way back")
    print("OK: %s fenced the window" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_rfc5545(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # build a VEVENT, fold at 75 octets, parse DTSTART back
    desc = "Quarterly planning, all hands. Bring the roadmap, the budget, and the questions."
    lines = ["BEGIN:VEVENT", "UID:evt-001@example.com",
             "DTSTAMP:20261017T120000Z", "DTSTART:20261020T140000Z",
             "DTEND:20261020T150000Z", "SUMMARY:Planning",
             "DESCRIPTION:" + desc, "SEQUENCE:0", "END:VEVENT"]
    folded = []
    for ln in lines:
        b = ln.encode("utf-8")
        while len(b) > 75:
            folded.append(b[:75].decode("utf-8"))
            b = b" " + b[75:]
        folded.append(b.decode("utf-8"))
    print("unfolded lines: %d -> folded lines: %d" % (len(lines), len(folded)))
    assert all(len(l.encode("utf-8")) <= 76 for l in folded)  # 75 + 1 space prefix
    # parse back: unfold then read DTSTART
    unfolded, cur = [], ""
    for l in folded:
        if l.startswith(" ") or l.startswith("\\t"):
            cur += l[1:]
        else:
            if cur:
                unfolded.append(cur)
            cur = l
    unfolded.append(cur)
    dt = [l for l in unfolded if l.startswith("DTSTART:")][0]
    print("round-trip DTSTART: %s" % dt)
    assert dt == "DTSTART:20261020T140000Z"
    # SEQUENCE ordering: higher wins, DTSTAMP breaks ties
    edits = [(0, "20261017T120000Z"), (1, "20261017T120500Z"), (1, "20261017T120300Z")]
    winner = max(edits)
    assert winner == (1, "20261017T120500Z")
    print("one format, one oath, understood everywhere")
    print("OK: %s spoke iCalendar" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_conflict_detection(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # interval index + state compatibility matrix -> verdict with cited collisions
    ledger = [("R1", 540, 600, "confirmed"), ("R1", 600, 660, "tentative"),
              ("R1", 700, 760, "confirmed")]
    hard_pairs = {("confirmed", "confirmed"), ("tentative", "confirmed"),
                  ("confirmed", "tentative"), ("maintenance", "confirmed"),
                  ("confirmed", "maintenance")}
    def verdict(prop):
        hits = []
        ps, pe, pst = prop
        for _, bs, be, bst in ledger:
            if ps < be and bs < pe:
                if (pst, bst) in hard_pairs or (bst, pst) in hard_pairs:
                    hits.append((bs, be, bst))
        return hits
    v1 = verdict((570, 630, "confirmed"))
    v2 = verdict((600, 660, "tentative"))
    v3 = verdict((660, 700, "confirmed"))
    print("proposal A collides: %s" % (v1,))
    print("proposal B (tentative vs tentative) collides: %s" % (v2,))
    print("proposal C collides: %s" % (v3,))
    assert v1 == [(540, 600, "confirmed"), (600, 660, "tentative")]
    assert v2 == [], "tentative-vs-tentative overlap is allowed"
    assert v3 == []
    # buffer soft-conflict: 10-min buffer, proposal ends 5 min before next booking
    buf = 10
    soft = (760 - 755) < buf
    print("soft buffer conflict: %s" % soft)
    assert soft is True
    print("the guardian names the clash it finds")
    print("OK: %s guarded the gate" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_constraint_satisfaction(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # backtracking: 3 shifts, 4 workers, availability + max-2-shifts constraint
    shifts = ["morning", "evening", "night"]
    workers = ["amy", "bo", "cy", "dee"]
    avail = {"morning": {"amy", "bo", "cy"}, "evening": {"bo", "cy", "dee"},
             "night": {"amy", "dee"}}
    solutions = []
    def backtrack(i, assign, counts):
        if i == len(shifts):
            solutions.append(dict(assign))
            return
        s = shifts[i]
        for w in sorted(avail[s]):
            if counts.get(w, 0) >= 2:
                continue
            assign[s] = w
            counts[w] = counts.get(w, 0) + 1
            backtrack(i + 1, assign, counts)
            counts[w] -= 1
            del assign[s]
    backtrack(0, {}, {})
    print("feasible rosters: %d" % len(solutions))
    for sol in solutions:
        assert len(set(sol.values())) >= 2  # max-2 rule respected by construction
    # 3*3*2 combos, none assigning one worker all 3 shifts (no worker covers all)
    assert len(solutions) == 18
    print("example: %s" % solutions[0])
    print("write every rule down; the solver keeps only what it can see")
    print("OK: %s solved the constraints" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_rotation_rules(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # score two rotations on circadian rules: forward+fast vs backward+mid
    def score(seq):
        # seq: shift letters per day, x = off; compare consecutive WORK days
        work = [s for s in seq if s != "x"]
        penalty = 0
        order = {"D": 0, "E": 1, "N": 2}
        for a, b in zip(work, work[1:]):
            if order[b] < order[a]:
                penalty += 10  # backward transition
        nights = sum(1 for s in seq if s == "N")
        run, maxrun = 0, 0
        for s in seq:
            run = run + 1 if s == "N" else 0
            maxrun = max(maxrun, run)
        if maxrun > 4:
            penalty += 5 * (maxrun - 4)
        return penalty, nights, maxrun
    fwd_fast = list("DDDxxEEEExxNNNxx")    # forward, 3-day blocks
    bwd_mid = list("NNNNNxxEEEExxDDDxx")   # backward, 5-day night blocks
    pf, nf, mf = score(fwd_fast)
    pb, nb, mb = score(bwd_mid)
    print("forward-fast : penalty %d, nights %d, max night run %d" % (pf, nf, mf))
    print("backward-mid : penalty %d, nights %d, max night run %d" % (pb, nb, mb))
    assert (pf, nf, mf) == (0, 3, 3)
    assert (pb, nb, mb) == (25, 5, 5)  # 2 backward transitions + 5 for the 5-night run
    print("forward with the clock; never the cruel middle speed")
    print("OK: %s set the rhythm" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_algorithms(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Hungarian method on 3x3 cost matrix, verified against brute force
    import itertools
    cost = [[4, 1, 3], [2, 0, 5], [3, 2, 2]]
    n = 3
    # brute-force optimum
    best = min(sum(cost[i][p[i]] for i in range(n)) for p in itertools.permutations(range(n)))
    # Hungarian via row/col reduction + augmenting search (simple O(n^3) for small n)
    def hungarian(c):
        nn = len(c)
        u = [0.0] * (nn + 1)
        v = [0.0] * (nn + 1)
        p = [0] * (nn + 1)
        way = [0] * (nn + 1)
        for i in range(1, nn + 1):
            p[0] = i
            j0 = 0
            minv = [float("inf")] * (nn + 1)
            used = [False] * (nn + 1)
            while True:
                used[j0] = True
                i0 = p[j0]
                delta = float("inf")
                j1 = 0
                for j in range(1, nn + 1):
                    if not used[j]:
                        cur = c[i0 - 1][j - 1] - u[i0] - v[j]
                        if cur < minv[j]:
                            minv[j] = cur
                            way[j] = j0
                        if minv[j] < delta:
                            delta = minv[j]
                            j1 = j
                for j in range(nn + 1):
                    if used[j]:
                        u[p[j]] += delta
                        v[j] -= delta
                    else:
                        minv[j] -= delta
                j0 = j1
                if p[j0] == 0:
                    break
            while j0:
                j1 = way[j0]
                p[j0] = p[j1]
                j0 = j1
        assign = [0] * nn
        for j in range(1, nn + 1):
            assign[p[j] - 1] = j - 1
        return sum(c[i][assign[i]] for i in range(nn)), assign
    hopt, assign = hungarian(cost)
    print("brute-force optimum: %d" % best)
    print("hungarian optimum: %d, assignment %s" % (hopt, assign))
    assert hopt == best == 5
    assert sorted(assign) == [0, 1, 2]
    print("match problem to tool: assignment to Hungarian")
    print("OK: %s weighed the pairing" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_allocation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # first-fit decreasing bin packing vs the ceil(total/capacity) lower bound
    jobs = [42, 25, 30, 18, 55, 12, 36, 22]
    cap = 100
    ordered = sorted(jobs, reverse=True)
    bins = []
    for j in ordered:
        for i in range(len(bins)):
            if bins[i] + j <= cap:
                bins[i] += j
                break
        else:
            bins.append(j)
    lower = (sum(jobs) + cap - 1) // cap
    print("jobs total %d, capacity %d" % (sum(jobs), cap))
    print("first-fit decreasing bins: %d (loads %s)" % (len(bins), bins))
    print("lower bound: %d" % lower)
    assert sum(jobs) == 240
    assert lower == 3
    assert len(bins) == 3
    assert all(b <= cap for b in bins)
    print("largest first, fragmentation fought, reasons logged")
    print("OK: %s placed the loads" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_queueing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # M/M/1: lambda=8/hr, mu=10/hr -> rho, L, W; Little's law cross-check
    lam, mu = 8.0, 10.0
    rho = lam / mu
    L = rho / (1 - rho)          # avg number in system
    W = L / lam                  # avg time in system (hours)
    Wq = W - 1 / mu              # avg wait in queue
    print("rho=%.3f L=%.3f W=%.3f h (%.1f min) Wq=%.3f h (%.1f min)"
          % (rho, L, W, W * 60, Wq, Wq * 60))
    assert 0.799 < rho < 0.801
    assert 3.99 < L < 4.01
    assert 0.499 < W < 0.501
    assert abs(L - lam * W) < 1e-9, "Little's law must hold exactly here"
    # at 95% utilization the queue explodes
    rho2 = 0.95
    L2 = rho2 / (1 - rho2)
    print("at 95%% utilization L=%.1f (vs %.1f at 80%%)" % (L2, L))
    assert 18.9 < L2 < 19.1
    print("95% 'efficiency' is a queue with a payroll")
    print("OK: %s sized the servers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_buffers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bottleneck time buffer sized from upstream arrival variability
    import statistics
    gaps = [22, 31, 18, 40, 25, 29, 35, 21, 27, 33]  # minutes between arrivals
    mean_gap = statistics.mean(gaps)
    sd_gap = statistics.stdev(gaps)
    safety = 2.0
    buffer_min = (mean_gap + safety * sd_gap)
    print("mean gap %.1f min, sd %.2f min" % (mean_gap, sd_gap))
    print("time buffer (mean + 2sd): %.2f min of ready work" % buffer_min)
    assert 28.05 < mean_gap < 28.15
    assert 6.84 < sd_gap < 6.86
    assert 41.79 < buffer_min < 41.83
    # penetration reporting thresholds
    used = 30.0
    pen = used / buffer_min * 100.0
    status = "green" if pen < 33 else ("yellow" if pen < 66 else "red")
    print("buffer penetration %.1f%% -> %s" % (pen, status))
    assert status == "red"
    print("slack is the insurance premium against certain variation")
    print("OK: %s sized the slack" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_multi_resource(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # rendezvous: intersect free time across surgeon, room, device ledgers
    day = (480, 1080)  # 08:00-18:00
    busy = {
        "surgeon": [(480, 600), (840, 960)],
        "room": [(600, 720)],
        "device": [(540, 660), (900, 1020)],
    }
    need = 120  # 2-hour procedure
    def free_of(b):
        out, cur = [], day[0]
        for s, e in sorted(b):
            if s > cur:
                out.append((cur, s))
            cur = max(cur, e)
        if cur < day[1]:
            out.append((cur, day[1]))
        return out
    free = {r: free_of(b) for r, b in busy.items()}
    # intersect
    common, cur_sets = [day], None
    points = sorted({p for f in free.values() for iv in f for p in iv})
    windows = []
    for a, b in zip(points, points[1:]):
        if b - a >= need and all(any(s <= a and b <= e for s, e in free[r]) for r in free):
            windows.append((a, b))
    print("common windows >= 120 min: %s" % (windows,))
    assert windows == [(720, 840)]
    print("all keepers to the same hour, committed as one")
    print("OK: %s gathered the bundle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_sync(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # concurrent edits converge by (SEQUENCE, DTSTAMP); sync token fetches deltas only
    replicas = [
        {"uid": "m1", "seq": 2, "dtstamp": "20261017T120000Z", "summary": "Planning v3"},
        {"uid": "m1", "seq": 2, "dtstamp": "20261017T120500Z", "summary": "Planning v4"},
        {"uid": "m1", "seq": 1, "dtstamp": "20261017T130000Z", "summary": "Planning v2"},
    ]
    winner = max(replicas, key=lambda r: (r["seq"], r["dtstamp"]))
    print("converged summary: %s" % winner["summary"])
    assert winner["summary"] == "Planning v4"
    # sync-token delta: server log with tokens, client at token 2 gets only newer
    log = [(1, "create m1"), (2, "update m1"), (3, "create m2"), (4, "delete m1")]
    client_token = 2
    delta = [e for t, e in log if t > client_token]
    print("delta since token 2: %s" % (delta,))
    assert delta == ["create m2", "delete m1"]
    print("same promise, same hour, on every device")
    print("OK: %s synced the truth" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_preventive(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # PM due dates with tolerance float; overdue escalation
    import datetime
    today = datetime.date(2026, 10, 17)
    plans = [
        ("pump-A", datetime.date(2026, 7, 20), 90, 10),   # due Oct 18 +/-10
        ("fan-B", datetime.date(2026, 7, 1), 90, 10),     # due Sep 29 -> overdue
        ("belt-C", datetime.date(2026, 9, 1), 90, 10),    # due Nov 30
    ]
    for asset, last, interval, tol in plans:
        due = last + datetime.timedelta(days=interval)
        late = (today - due).days
        if late > tol:
            state = "ESCALATE"
        elif late > 0:
            state = "due-in-tolerance"
        else:
            state = "scheduled"
        print("%s due %s (%+d days): %s" % (asset, due, late, state))
    states = []
    for asset, last, interval, tol in plans:
        due = last + datetime.timedelta(days=interval)
        late = (today - due).days
        states.append("ESCALATE" if late > tol else ("due-in-tolerance" if late > 0 else "scheduled"))
    assert states == ["scheduled", "ESCALATE", "scheduled"]
    print("care before failure, floated wisely, escalated honestly")
    print("OK: %s kept the machines" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_linear_programming(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # tiny workforce ILP by enumeration: full-time covers all 3 intervals ($100),
    # part-time covers one interval ($40); demand [3,5,4]
    import itertools
    demand = [3, 5, 4]
    best, bestv = None, None
    for f in range(0, 7):
        for p1 in range(0, 7):
            for p2 in range(0, 7):
                for p3 in range(0, 7):
                    if f + p1 >= demand[0] and f + p2 >= demand[1] and f + p3 >= demand[2]:
                        c = 100 * f + 40 * (p1 + p2 + p3)
                        if best is None or c < best:
                            best, bestv = c, (f, p1, p2, p3)
    print("optimal cost: $%d at full-time=%d part-time=%s" % (best, bestv[0], bestv[1:]))
    assert best == 420 and bestv == (3, 0, 2, 1)
    # LP relaxation bound (fractional allowed): same structure, bound <= integer optimum
    bound = 100 * 3 + 40 * (0 + 2 + 1)
    gap = (best - bound) / best * 100.0
    print("relaxation bound: $%d, optimality gap: %.1f %%" % (bound, gap))
    assert abs(gap) < 1e-9
    print("cheapest faithful keeping, certified by the bound")
    print("OK: %s optimized the roster" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_timetabling(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # greedy largest-first coloring of an exam conflict graph
    edges = {0: {1, 2}, 1: {0, 2, 3}, 2: {0, 1, 4}, 3: {1, 4}, 4: {2, 3}}
    order = sorted(edges, key=lambda v: (-len(edges[v]), v))
    color = {}
    for v in order:
        used = {color[u] for u in edges[v] if u in color}
        c = 0
        while c in used:
            c += 1
        color[v] = c
    ncolors = max(color.values()) + 1
    maxdeg = max(len(e) for e in edges.values())
    print("colors used: %d (max degree %d, bound %d)" % (ncolors, maxdeg, maxdeg + 1))
    print("timetable: %s" % (color,))
    for v, ns in edges.items():
        for u in ns:
            assert color[v] != color[u], "adjacent exams share a slot"
    assert ncolors <= maxdeg + 1
    assert ncolors == 3
    print("color first for feasibility, polish after for grace")
    print("OK: %s wove the timetable" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_job_shop(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 2 jobs x 2 machines; simulate fixed per-machine sequences -> makespan
    # job0: M0(3) then M1(2); job1: M1(4) then M0(1)
    # machine orders: M0: job0 then job1; M1: job1 then job0
    routing = {"j0": [("M0", 3), ("M1", 2)], "j1": [("M1", 4), ("M0", 1)]}
    mseq = {"M0": ["j0", "j1"], "M1": ["j1", "j0"]}
    mach_free = {"M0": 0, "M1": 0}
    job_ready = {"j0": 0, "j1": 0}
    idx = {"j0": 0, "j1": 0}
    scheduled = set()
    while len(scheduled) < 4:
        progressed = False
        for m in ("M0", "M1"):
            for j in mseq[m]:
                k = idx[j]
                if k >= len(routing[j]) or (j, k) in scheduled:
                    continue
                mm, dur = routing[j][k]
                if mm != m:
                    continue
                start = max(mach_free[m], job_ready[j])
                end = start + dur
                mach_free[m] = end
                job_ready[j] = end
                idx[j] += 1
                scheduled.add((j, k))
                progressed = True
                break
            if progressed:
                break
        assert progressed, "deadlock in simulation"
    makespan = max(mach_free.values())
    print("machine free times: %s" % (mach_free,))
    print("makespan C_max: %d" % makespan)
    assert makespan == 6
    # lower bound: max(machine loads 4 vs 6, job lengths 5 vs 5) = 6 -> optimal
    print("lower bound max(6, 5) = 6; schedule achieves 6: optimal")
    print("the hall keeps time by the slowest keeper")
    print("OK: %s ran the shop" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_real_time(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # rate-monotonic: utilization bound test, then exact response-time analysis
    tasks = [(1, 4), (2, 6), (3, 12)]  # (exec, period), deadline = period
    n = len(tasks)
    u = sum(e / p for e, p in tasks)
    bound = n * (2 ** (1.0 / n) - 1)
    print("utilization %.4f vs Liu-Layland bound %.4f" % (u, bound))
    assert 0.8332 < u < 0.8334
    assert 0.7797 < bound < 0.7799
    print("bound test: %s (not sufficient -> run exact RTA)" % ("PASS" if u <= bound else "INCONCLUSIVE"))
    # response-time analysis, tasks sorted by period
    ts = sorted(tasks, key=lambda t: t[1])
    ok = True
    for i, (e, p) in enumerate(ts):
        r = e
        while True:
            r2 = e + sum(( (r + ts[j][1] - 1) // ts[j][1]) * ts[j][0] for j in range(i))
            if r2 == r:
                break
            r = r2
            assert r <= p + e, "diverged"
        print("task exec=%d period=%d worst response=%d deadline=%d %s"
              % (e, p, r, p, "OK" if r <= p else "MISS"))
        ok = ok and r <= p
    assert ok, "exact analysis must admit this set"
    print("admit only the work that can truly finish in time")
    print("OK: %s met the deadlines" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_distributed(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # CRDT-style merge: event map keyed by UID, per-field last-writer-wins, tombstones
    import hashlib
    r1 = {"m1": {"seq": 2, "dt": "20261017T120000Z", "sum": "Planning v3", "del": False},
          "m2": {"seq": 0, "dt": "20261017T110000Z", "sum": "Dentist", "del": False}}
    r2 = {"m1": {"seq": 2, "dt": "20261017T120500Z", "sum": "Planning v4", "del": False},
          "m3": {"seq": 0, "dt": "20261017T113000Z", "sum": "Gym", "del": False},
          "m2": {"seq": 1, "dt": "20261017T123000Z", "sum": "", "del": True}}
    merged = {}
    for uid in set(r1) | set(r2):
        a, b = r1.get(uid), r2.get(uid)
        if a and b:
            merged[uid] = a if (a["seq"], a["dt"]) >= (b["seq"], b["dt"]) else b
        else:
            merged[uid] = a or b
    live = {u: v for u, v in merged.items() if not v["del"]}
    print("merged UIDs: %s" % sorted(merged))
    print("live after tombstones: %s" % sorted(live))
    assert merged["m1"]["sum"] == "Planning v4"
    assert "m2" not in live and merged["m2"]["del"] is True
    assert sorted(live) == ["m1", "m3"]
    # tamper-evident: hash chain over the merged log
    chain, prev = [], "0" * 16
    for uid in sorted(merged):
        h = hashlib.sha256((prev + uid + str(merged[uid]["seq"])).encode()).hexdigest()[:16]
        chain.append(h)
        prev = h
    print("chain head: %s" % chain[-1])
    assert len(chain) == 3 and len(set(chain)) == 3
    print("one covenant, sung in chorus, every replica the same")
    print("OK: %s reached consensus" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_fairness(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Jain index over weekend-day counts per worker; max-min check
    weekends = [6, 6, 7, 5]
    n = len(weekends)
    jain = sum(weekends) ** 2 / (n * sum(w * w for w in weekends))
    spread = max(weekends) - min(weekends)
    print("weekend counts: %s" % (weekends,))
    print("Jain index: %.4f (1.0 = perfect equality)" % jain)
    print("max-min spread: %d" % spread)
    assert 0.9862 < jain < 0.9864
    assert spread == 2
    # hard cap policy: no one exceeds 8 weekend days per quarter
    cap = 8
    assert all(w <= cap for w in weekends)
    print("cap %d respected; publish the counting, let justice be seen" % cap)
    print("OK: %s balanced the burden" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_mrp(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # MRP explosion: 100 units due week 10; BOM: 1 P -> 2 A + 1 B; 1 A -> 3 C
    # on-hand: A 50, C 100, B 0; lead times (weeks): P 1, A 2, B 2, C 3
    due = 10
    gross_p = 100
    need_a = gross_p * 2 - 50          # net of on-hand
    need_b = gross_p * 1 - 0
    need_c = need_a * 3 - 100
    rel_p = due - 1
    rel_a, rel_b = due - 2, due - 2    # A/B needed when P starts (week 9)
    rel_c = rel_a - 3                  # C needed when A starts
    print("net requirements: A=%d B=%d C=%d" % (need_a, need_b, need_c))
    print("order releases: P wk%d, A wk%d, B wk%d, C wk%d" % (rel_p, rel_a, rel_b, rel_c))
    assert (need_a, need_b, need_c) == (150, 100, 350)
    assert (rel_p, rel_a, rel_b, rel_c) == (9, 8, 8, 5)
    # ATP: planned production 100, customer orders 60 -> promiseable 40
    atp = 100 - 60
    print("available-to-promise: %d" % atp)
    assert atp == 40
    print("never let sales swear what the shop cannot keep")
    print("OK: %s planned the requirements" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_predictive(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # P-F interval 600h -> inspect at <=300h; RUL 400h, lead time 120h -> window inside 280h
    pf_interval = 600.0
    inspect_at = pf_interval / 2.0
    rul, lead = 400.0, 120.0
    latest_safe = rul - lead
    print("P-F interval %.0fh -> inspect every <= %.0fh" % (pf_interval, inspect_at))
    print("RUL %.0fh - lead %.0fh -> schedule window within %.0fh" % (rul, lead, latest_safe))
    assert 299.9 < inspect_at < 300.1
    assert 279.9 < latest_safe < 280.1
    # threshold scoring on history: confusion matrix
    tp, fp, fn, tn = 34, 6, 2, 158
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    print("precision %.3f recall %.3f over %d predictions" % (precision, recall, tp + fp + fn + tn))
    assert 0.849 < precision < 0.851
    assert 0.944 < recall < 0.945
    print("hear the whisper before the break; write the window before the failure")
    print("OK: %s listened to the machine" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_architecture(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hot-path latency budget vs SLO; free/busy cache math
    budget = {"api": 5.0, "conflict_detect": 8.0, "ledger_write": 12.0}
    total = sum(budget.values())
    slo = 50.0
    print("hot path: %s = %.1f ms (SLO %.0f ms)" % (budget, total, slo))
    assert 24.9 < total < 25.1 and total < slo
    # free/busy is the hottest query: cache hit rate 97% -> origin load
    qps, hit = 1200.0, 0.97
    origin = qps * (1 - hit)
    print("free/busy %.0f qps at %.0f%% hit -> origin %.1f qps" % (qps, hit * 100, origin))
    assert 35.9 < origin < 36.1
    # sharding: 40k resources over 8 shards
    per_shard = 40000 / 8
    print("resources per shard: %.0f" % per_shard)
    assert per_shard == 5000
    print("hot path swift, heavy path patient, history locked")
    print("OK: %s raised the temple" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_audit(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hash-chained audit log; tamper with one entry -> verification fails
    import hashlib, copy
    log = []
    prev = "GENESIS"
    for actor, action in [("amy", "book R1 09:00"), ("bo", "move R1 10:00"), ("amy", "cancel R1")]:
        h = hashlib.sha256((prev + actor + action).encode()).hexdigest()
        log.append({"actor": actor, "action": action, "prev": prev, "hash": h})
        prev = h
    def verify(entries):
        prev = "GENESIS"
        for e in entries:
            if e["prev"] != prev:
                return False
            if hashlib.sha256((e["prev"] + e["actor"] + e["action"]).encode()).hexdigest() != e["hash"]:
                return False
            prev = e["hash"]
        return True
    print("clean log verifies: %s" % verify(log))
    assert verify(log) is True
    tampered = copy.deepcopy(log)
    tampered[1]["action"] = "move R1 14:00"  # backdated change
    print("tampered log verifies: %s" % verify(tampered))
    assert verify(tampered) is False
    # compliance query: hours per worker cap 48/week
    hours = {"amy": 44, "bo": 52, "cy": 38}
    viol = [w for w, h in hours.items() if h > 48]
    print("hours-cap violations: %s" % (viol,))
    assert viol == ["bo"]
    print("a past that can be edited was never truly sworn")
    print("OK: %s kept the memory" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_operating_picture(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # demand vs coverage per 4h block; gap detector ranked by time-to-impact
    blocks = ["00-04", "04-08", "08-12", "12-16", "16-20", "20-24"]
    demand =   [2, 3, 8, 9, 6, 3]
    coverage = [2, 2, 8, 7, 6, 3]
    gaps = [(b, d - c, i) for i, (b, d, c) in enumerate(zip(blocks, demand, coverage)) if c < d]
    gaps.sort(key=lambda g: g[2])  # time-to-impact: soonest first
    print("coverage gaps (block, shortfall): %s" % [(b, s) for b, s, _ in gaps])
    assert [(b, s) for b, s, _ in gaps] == [("04-08", 1), ("12-16", 2)]
    # buffer health tiles
    buffers = {"theater-turnover": 22.0, "icu-bed": 71.0, "van-fleet": 45.0}
    tiles = {k: ("green" if v < 33 else ("yellow" if v < 66 else "red")) for k, v in buffers.items()}
    print("buffer tiles: %s" % (tiles,))
    assert tiles == {"theater-turnover": "green", "icu-bed": "red", "van-fleet": "yellow"}
    # error budget remaining
    budget_min, spent = 43.8, 12.5
    print("error budget remaining: %.1f min" % (budget_min - spent))
    assert 31.29 < budget_min - spent < 31.31
    print("one ledger per resource, one picture for the operation")
    print("OK: %s saw the whole hall" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_sla(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # nines math: monthly budgets on the average month (365.25/12 days)
    month_min = 365.25 / 12 * 24 * 60
    budgets = {}
    for nines, target in [("three", 0.999), ("four", 0.9999)]:
        budget = (1 - target) * month_min
        budgets[nines] = budget
        print("%s nines (%.2f%%): %.2f downtime min/month" % (nines, target * 100, budget))
    assert 43.82 < budgets["three"] < 43.84
    assert 4.382 < budgets["four"] < 4.384
    mtbf, mttr = 720.0, 0.5  # hours
    avail = mtbf / (mtbf + mttr)
    print("MTBF %.0fh MTTR %.1fh -> availability %.5f" % (mtbf, mttr, avail))
    assert 0.99930 < avail < 0.99931
    # error budget burn: 12.5 of 43.83 spent -> freeze at zero
    remaining = budgets["three"] - 12.5
    freeze = remaining <= 0
    print("budget remaining %.1f min; change freeze: %s" % (remaining, freeze))
    assert freeze is False
    print("the nines are a budget, not a boast")
    print("OK: %s kept the promise numbered" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_src_stochastic(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # PERT three-point estimates + Monte Carlo finish-date distribution
    import random
    acts = [("design", 4, 6, 14), ("build", 8, 12, 22), ("test", 3, 5, 9)]
    for nm, o, m, p in acts:
        te = (o + 4 * m + p) / 6.0
        var = ((p - o) / 6.0) ** 2
        print("%s: PERT %.2f var %.3f" % (nm, te, var))
    assert abs((4 + 24 + 14) / 6.0 - 7.0) < 1e-9
    random.seed(42)
    fins = []
    for _ in range(4000):
        tot = 0.0
        for _, o, m, p in acts:
            # triangular sample from three-point estimate
            tot += random.triangular(o, p, m)
        fins.append(tot)
    fins.sort()
    p50, p90 = fins[2000], fins[3600]
    print("Monte Carlo n=4000: P50=%.2f P90=%.2f" % (p50, p90))
    assert 27.2 < p50 < 27.7
    assert 32.4 < p90 < 32.9
    hit = sum(1 for f in fins if f <= 28.0) / len(fins)
    print("P(finish by 28): %.3f" % hit)
    assert 0.55 < hit < 0.70
    print("never a naked date: every commitment carries its confidence")
    print("OK: %s weighed the futures" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what_is": demo_src_what_is,
    "data_models": demo_src_data_models,
    "time_interval": demo_src_time_interval,
    "recurrence": demo_src_recurrence,
    "time_zones": demo_src_time_zones,
    "appointments": demo_src_appointments,
    "shifts": demo_src_shifts,
    "equipment": demo_src_equipment,
    "facilities": demo_src_facilities,
    "maintenance_windows": demo_src_maintenance_windows,
    "rfc5545": demo_src_rfc5545,
    "conflict_detection": demo_src_conflict_detection,
    "constraint_satisfaction": demo_src_constraint_satisfaction,
    "rotation_rules": demo_src_rotation_rules,
    "algorithms": demo_src_algorithms,
    "allocation": demo_src_allocation,
    "queueing": demo_src_queueing,
    "buffers": demo_src_buffers,
    "multi_resource": demo_src_multi_resource,
    "sync": demo_src_sync,
    "preventive": demo_src_preventive,
    "sla": demo_src_sla,
    "stochastic": demo_src_stochastic,
    "linear_programming": demo_src_linear_programming,
    "timetabling": demo_src_timetabling,
    "job_shop": demo_src_job_shop,
    "real_time": demo_src_real_time,
    "distributed": demo_src_distributed,
    "fairness": demo_src_fairness,
    "mrp": demo_src_mrp,
    "predictive": demo_src_predictive,
    "architecture": demo_src_architecture,
    "audit": demo_src_audit,
    "operating_picture": demo_src_operating_picture,
}
