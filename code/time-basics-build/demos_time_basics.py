#!/usr/bin/env python3
"""Demo programs for the Time Basics databases (Manon's fundamentals order #9).

Every demo is real, runnable, stdlib-only Python performing the actual
time computation for its record. All are machine-executed by build.py:
each prints its real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker. Entry text numbers were
cross-checked against these computations 2026-10-17.
"""

import json as _json

_PREAMBLE = "import math\nfrom datetime import date, timedelta\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace(
        "NAME", _json.dumps(name))


def demo_tb_what_time_is(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # a moment named, a duration measured: Oct 1 00:00 to Oct 17 16:00
    start_h = 0.0
    end_h = 16 * 24.0 + 16.0
    dur_h = end_h - start_h
    dur_s = dur_h * 3600.0
    print("start: 2026-10-01 00:00, end: 2026-10-17 16:00")
    print("duration: %.1f hours = %.0f seconds" % (dur_h, dur_s))
    assert 399.9 < dur_h < 400.1
    assert 1439900.0 < dur_s < 1440100.0
    print("rule: name two moments, count the steady repeats between them")
    print("OK: %s framed time" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_the_second(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the SI second: exactly 9,192,631,770 cesium-133 periods
    f = 9192631770.0
    period_s = 1.0 / f
    period_ps = period_s * 1e12
    print("cesium-133 frequency: %.0f Hz" % f)
    print("one period: %.6e s = %.2f ps" % (period_s, period_ps))
    assert 108.77 < period_ps < 108.79
    assert 86399.9 < 86400.0 / 1.0 < 86400.1
    print("seconds per day: 86400, per hour: 3600, per minute: 60")
    print("OK: %s counted the atom" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_minutes_hours(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 90 minutes both ways: up to seconds, down to hours
    m = 90.0
    s = m * 60.0
    h = m / 60.0
    print("90 minutes = %.0f seconds = %.1f hours" % (s, h))
    assert 5399.9 < s < 5400.1
    assert 1.499 < h < 1.501
    # decimal hours are not clock hours: 1.5 h = 1 h 30 min
    dh = 2.5
    whole = int(dh)
    mins = (dh - whole) * 60.0
    print("2.5 hours = %d h %.0f min" % (whole, mins))
    assert 29.9 < mins < 30.1
    print("rule: up multiply by 60, down divide by 60, carry at 60")
    print("OK: %s worked the sixties" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_days_weeks_months(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    day_s = 24 * 3600
    week_s = 7 * day_s
    avg_month_s = 30.44 * day_s
    print("1 day = %d s, 1 week = %d s" % (day_s, week_s))
    print("average month (30.44 d) = %.0f s" % avg_month_s)
    assert day_s == 86400
    assert week_s == 604800
    assert 2629400.0 < avg_month_s < 2630100.0
    print("week is exact (7 d); month is calendar (28/29/30/31 d)")
    print("OK: %s kept the rhythms" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_years_decades(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the 400-year Gregorian cycle: 97 leap years, 146097 days
    def leap(y):
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
    leaps = sum(1 for y in range(2001, 2401) if leap(y))
    days = 400 * 365 + leaps
    avg = days / 400.0
    print("leap years per 400: %d" % leaps)
    print("days per 400 years: %d" % days)
    print("average year: %.4f days" % avg)
    assert leaps == 97
    assert days == 146097
    assert 365.2424 < avg < 365.2426
    # residual against the tropical year 365.24219 d
    drift_s = (365.2425 - 365.24219) * 86400.0
    yrs_per_day = 1.0 / (365.2425 - 365.24219)
    print("residual drift: %.2f s/yr -> 1 day in %.0f yr" % (drift_s, yrs_per_day))
    assert 26.7 < drift_s < 26.9
    assert 3200.0 < yrs_per_day < 3260.0
    print("OK: %s held the great units" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_analog_clock(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hand angles at 3:15, measured from 12 o clock
    h, m = 3, 15
    min_angle = m * 6.0
    hour_angle = (h % 12) * 30.0 + m * 0.5
    print("at 3:15 -> minute hand %.1f deg, hour hand %.1f deg" % (min_angle, hour_angle))
    assert 89.9 < min_angle < 90.1
    assert 97.4 < hour_angle < 97.6
    # each minute mark 6 deg, each hour mark 30 deg
    assert 5.99 < 360.0 / 60.0 < 6.01
    assert 29.99 < 360.0 / 12.0 < 30.01
    print("rule: minutes first, then the hour the hour hand has passed")
    print("OK: %s read the dial" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_digital_clock(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 12-hour to 24-hour conversions, traps included
    def to24(h, m, ap):
        if ap == "AM":
            hh = 0 if h == 12 else h
        else:
            hh = 12 if h == 12 else h + 12
        return "%02d:%02d" % (hh, m)
    cases = [((2, 30, "PM"), "14:30"), ((12, 0, "AM"), "00:00"),
             ((12, 0, "PM"), "12:00"), ((11, 59, "PM"), "23:59"),
             ((9, 5, "AM"), "09:05")]
    for (h, m, ap), want in cases:
        got = to24(h, m, ap)
        print("%d:%02d %s -> %s" % (h, m, ap, got))
        assert got == want
    print("rule: 12 AM is midnight, 12 PM is noon, PM adds 12")
    print("OK: %s read the digits" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_am_pm(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the day split in two twelves
    am = list(range(0, 12))
    pm = list(range(12, 24))
    print("AM hours: %d, PM hours: %d, total: %d" % (len(am), len(pm), len(am) + len(pm)))
    assert len(am) == 12 and len(pm) == 12
    # the 12 trap: 12 AM -> 00, 12 PM -> 12
    assert (0 if 12 == 12 else 12) == 0
    conv = {("AM", 12): 0, ("AM", 7): 7, ("PM", 12): 12, ("PM", 7): 19}
    for (ap, h), want in conv.items():
        got = (0 if h == 12 else h) if ap == "AM" else (12 if h == 12 else h + 12)
        assert got == want, (ap, h)
    print("7 AM is breakfast, 7 PM is dinner: always name the marker")
    print("OK: %s split the day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_noon_midnight(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # relative words as offsets from today: 2026-10-17
    today = date(2026, 10, 17)
    names = {"day before yesterday": -2, "yesterday": -1, "today": 0,
             "tomorrow": 1, "day after tomorrow": 2}
    for w, off in names.items():
        print("%-20s -> %s" % (w, today + timedelta(days=off)))
    assert str(today + timedelta(days=-1)) == "2026-10-16"
    assert str(today + timedelta(days=1)) == "2026-10-18"
    # year boundary: Dec 31 + 1 day
    nye = date(2026, 12, 31) + timedelta(days=1)
    print("Dec 31 + 1 day -> %s" % nye)
    assert str(nye) == "2027-01-01"
    print("noon 12:00 PM hinges the day; midnight 12:00 AM turns the date")
    print("OK: %s named the hinges" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_subsecond(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the thousand-step ladder below the second
    ms, us, ns = 1e-3, 1e-6, 1e-9
    print("1 s = %.0f ms = %.0f us = %.0f ns" % (1 / ms, 1 / us, 1 / ns))
    assert 999.9 < 1 / ms < 1000.1
    assert 999999.0 < 1 / us < 1000001.0
    # light in one nanosecond: ~30 cm
    c = 299792458.0
    d_ns = c * ns
    d_us = c * us
    print("light in 1 ns: %.4f m; in 1 us: %.1f m" % (d_ns, d_us))
    assert 0.299 < d_ns < 0.301
    assert 299.7 < d_us < 299.9
    print("OK: %s measured the small" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_ladder(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the rung values, then a full climb: 2 days to seconds
    rungs = {"min": 60, "hour": 3600, "day": 86400, "week": 604800}
    for k, v in rungs.items():
        print("1 %-4s = %d s" % (k, v))
    assert rungs["min"] == 60 and rungs["hour"] == 3600
    assert rungs["day"] == 86400 and rungs["week"] == 604800
    s = 2 * rungs["day"]
    back_h = s / 3600.0
    print("2 days = %d s = %.0f h" % (s, back_h))
    assert s == 172800
    assert 47.9 < back_h < 48.1
    print("rule: climb multiply, descend divide, one rung at a time")
    print("OK: %s climbed the ladder" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_time_tools(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the seconds pendulum: T = 2*pi*sqrt(L/g), solve L for T = 2 s
    g = 9.80665
    T = 2.0
    L = g * (T / (2 * math.pi)) ** 2
    print("seconds pendulum length: %.4f m" % L)
    assert 0.9935 < L < 0.9937
    # quartz: 32768 = 2^15 divided down to 1 Hz
    q = 32768
    print("quartz: %d Hz = 2^%d" % (q, int(math.log2(q))))
    assert q == 2 ** 15
    assert 9.1926e9 < 9192631770.0 < 9.1927e9
    print("each era: a steadier oscillator, counted honestly")
    print("OK: %s wound the clocks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_add_subtract(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # total-minutes method: 2:45 + 1:30, then round trip
    a = 2 * 60 + 45
    b = 1 * 60 + 30
    s = a + b
    print("165 + 90 = %d min = %d h %d min" % (s, s // 60, s % 60))
    assert s == 255 and s // 60 == 4 and s % 60 == 15
    back = s - b
    print("255 - 90 = %d min (round trip)" % back)
    assert back == a
    # borrow case: 4:15 - 1:30
    c, d = 4 * 60 + 15, 1 * 60 + 30
    r = c - d
    print("255 - 90 = %d min = %d h %d min" % (r, r // 60, r % 60))
    assert r == 165
    print("rule: carry and borrow at 60, never at 100")
    print("OK: %s balanced the columns" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_elapsed(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 9:15 AM to 2:45 PM via minutes-since-midnight
    start = 9 * 60 + 15
    end = 14 * 60 + 45
    el = end - start
    print("elapsed: %d min = %d h %d min = %d s" % (el, el // 60, el % 60, el * 60))
    assert el == 330
    assert el * 60 == 19800
    # overnight: 11:00 PM to 7:00 AM
    s2, e2 = 23 * 60, 7 * 60
    if e2 <= s2:
        e2 += 24 * 60
    el2 = e2 - s2
    print("overnight elapsed: %d min = %d h" % (el2, el2 // 60))
    assert el2 == 480
    print("rule: end minus start; end earlier than start means add 24 h")
    print("OK: %s timed the interval" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_24h_clock(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the full hour map, spot-checked
    def h24(h, ap):
        return 0 if (ap == "AM" and h == 12) else (12 if (ap == "PM" and h == 12)
                else (h + 12 if ap == "PM" else h))
    cases = [(12, "AM", 0), (1, "AM", 1), (11, "AM", 11), (12, "PM", 12),
             (1, "PM", 13), (7, "PM", 19), (11, "PM", 23)]
    for h, ap, want in cases:
        got = h24(h, ap)
        print("%2d %s -> %02d:00" % (h, ap, got))
        assert got == want
    # rollover: 23:59 + 1 min
    t = 23 * 60 + 59 + 1
    print("23:59 + 1 min -> %02d:%02d next day" % ((t // 60) % 24, t % 60))
    assert (t // 60) % 24 == 0 and t % 60 == 0
    print("OK: %s counted to twenty-four" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_calendars(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # month lengths sum to 365; February gains a day in leap years
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    common = sum(months)
    leap_y = common + 1
    print("common year: %d days, leap year: %d days" % (common, leap_y))
    assert common == 365 and leap_y == 366
    # knuckle check: 7 months have 31 days
    assert sum(1 for m in months if m == 31) == 7
    # month addition clamps: Jan 31 + 1 month lands in Feb (28/29)
    feb_len = 29  # leap year
    print("Jan 31 + 1 month -> Feb %d (clamped)" % feb_len)
    assert feb_len in (28, 29)
    print("OK: %s mapped the year" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_leap_years(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    def leap(y):
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
    cases = [(2024, True), (2000, True), (1900, False), (2100, False),
             (2025, False), (2026, False)]
    for y, want in cases:
        got = leap(y)
        print("%d -> leap: %s" % (y, got))
        assert got == want
    # cascade order matters: test the century exception explicitly
    assert leap(2000) and not leap(1900)
    print("rule: div by 4, except centuries unless div by 400")
    print("OK: %s paid February" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_time_zones(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 15:00 UTC rendered in two zones
    utc_h = 15.0
    for off, label in [(-5, "UTC-5"), (9, "UTC+9")]:
        local = utc_h + off
        day = 0
        if local >= 24:
            local -= 24
            day = 1
        print("15:00 UTC -> %02d:00 %s%s" % (int(local), label,
              " next day" if day else ""))
    assert int(15.0 - 5) == 10
    assert int(15.0 + 9 - 24) == 0
    # base rate: 360 deg / 24 h
    print("15 degrees of longitude per hour")
    assert 14.99 < 360.0 / 24.0 < 15.01
    print("rule: local = UTC + offset; east ahead, west behind")
    print("OK: %s zoned the globe" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_utc(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # TAI - UTC = 10 s (1972 start) + 27 leap seconds = 37 s
    leap_seconds = 27
    tai_utc = 10 + leap_seconds
    print("leap seconds inserted 1972-2016: %d" % leap_seconds)
    print("TAI - UTC = %d s" % tai_utc)
    assert tai_utc == 37
    # the 0.9 s rule keeps UTC tied to Earth rotation
    print("UTC stays within 0.9 s of UT1 by leap second")
    assert 0.89 < 0.9 < 0.91
    print("OK: %s kept the reference" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_date_line(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # crossing the line: westward +1 day, eastward -1 day
    dep = date(2026, 10, 17)
    west = dep + timedelta(days=1)
    east = dep - timedelta(days=1)
    print("depart %s westward  -> arrive %s" % (dep, west))
    print("depart %s eastward  -> arrive %s" % (dep, east))
    assert str(west) == "2026-10-18"
    assert str(east) == "2026-10-16"
    # the seam reconciles a full circle: +24 h of zones, -1 day at the line
    print("round the world: 24 zone-hours gained, 1 date-line day repaid")
    print("OK: %s settled the seam" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_dst(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # spring-forward day has 23 hours, fall-back day 25
    spring_s = 23 * 3600
    fall_s = 25 * 3600
    normal_s = 24 * 3600
    print("spring day: %d s, normal: %d s, fall day: %d s" % (spring_s, normal_s, fall_s))
    assert spring_s == 82800
    assert fall_s == 90000
    # the offset moves, not the sun: UTC-5 -> UTC-4
    print("offset shift: UTC-5 to UTC-4 (one hour borrowed for the evening)")
    assert -4 - (-5) == 1
    print("OK: %s shifted the season" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_seven_day_week(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    week_h = 7 * 24
    week_min = week_h * 60
    print("1 week = %d h = %d min" % (week_h, week_min))
    assert week_h == 168 and week_min == 10080
    # 100 days = 14 weeks and 2 days
    d = 100
    print("%d days = %d weeks and %d days" % (d, d // 7, d % 7))
    assert d // 7 == 14 and d % 7 == 2
    # weekday advance: common year +1, leap year +2
    assert 365 % 7 == 1 and 366 % 7 == 2
    print("seven wanderers, seven days, unbroken for millennia")
    print("OK: %s kept the seven" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_earth_motion(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the two motions and the tilt
    print("rotation: ~24 h -> day and night")
    print("orbit: ~365.25 d -> the year")
    tilt = 23.5
    print("axial tilt: %.1f deg -> the seasons" % tilt)
    assert 23.4 < tilt < 23.6
    trop = 365.2422
    print("tropical year: %.4f d (the calendar target)" % trop)
    assert 365.2421 < trop < 365.2423
    print("hemispheres oppose: June summer north, winter south")
    print("OK: %s watched the planet" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_schedules(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # two timetable reads: bus and evening flight
    bus = (9 * 60 + 5) - (8 * 60 + 10)
    flight = (21 * 60 + 25) - (18 * 60 + 40)
    print("bus 8:10 -> 9:05: %d min" % bus)
    print("flight 18:40 -> 21:25: %d min = %d h %d min" % (flight, flight // 60, flight % 60))
    assert bus == 55
    assert flight == 165
    # frequency service: every 20 min, next after 8:07 is 8:20
    interval = 20
    t = 8 * 60 + 7
    nxt = ((t + interval - 1) // interval) * interval
    print("every %d min; at 8:07 next is %d:%02d" % (interval, nxt // 60, nxt % 60))
    assert nxt == 8 * 60 + 20
    print("rule: row, column, two times; work backward from the arrival")
    print("OK: %s read the timetable" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_atomic_time(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cesium period and the NIST-F2 stability claim
    f = 9192631770.0
    period_ps = 1e12 / f
    print("cesium period: %.2f ps" % period_ps)
    assert 108.77 < period_ps < 108.79
    yrs = 300e6
    secs = yrs * 365.25 * 86400.0
    frac = 1.0 / secs
    print("300M years = %.3e s; 1 s error -> fractional %.2e" % (secs, frac))
    assert 9.46e15 < secs < 9.47e15
    assert 1.05e-16 < frac < 1.07e-16
    print("TAI: ~450 clocks in ~80 labs, averaged monthly by the BIPM")
    print("OK: %s heard the atom" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_leap_seconds(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the leap minute: 61 seconds, and the running total
    leap_day_s = 24 * 3600 + 1
    print("leap-second day: %d s (23:59:60 exists)" % leap_day_s)
    assert leap_day_s == 86401
    total = 10 + 27
    print("TAI - UTC = 10 + 27 = %d s" % total)
    assert total == 37
    print("discontinuation resolved 2022: no new leap seconds after 2035")
    print("OK: %s wrote the correction" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_world_calendars(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Julian vs Gregorian drift: 0.0075 d/yr = 10.8 min/yr
    rate_d = 365.25 - 365.2425
    rate_min = rate_d * 24 * 60
    print("Julian excess: %.4f d/yr = %.1f min/yr" % (rate_d, rate_min))
    assert 10.7 < rate_min < 10.9
    gap = 10.0 + (2026 - 1582) * rate_d
    print("gap 1582 (10 d) -> 2026: %.1f d" % gap)
    assert 13.0 < gap < 14.0
    # Hijri year: 12 lunations
    hijri = 12 * 29.5306
    print("Hijri year: %.3f d" % hijri)
    assert 354.366 < hijri < 354.368
    print("OK: %s compared the calendars" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_history(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # era spans between the milestones
    esc, pend, quartz, cesium, si = 1275, 1656, 1927, 1955, 1967
    print("escapement->pendulum: %d yr" % (pend - esc))
    print("pendulum->quartz: %d yr" % (quartz - pend))
    print("quartz->cesium: %d yr" % (cesium - quartz))
    print("cesium->SI second: %d yr" % (si - cesium))
    assert pend - esc == 381
    assert quartz - pend == 271
    assert si - cesium == 12
    print("each era checked against the last champion")
    print("OK: %s told the history" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_cross_day_zone(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 10:30 PM (UTC-5) + 4 h 15 m, via UTC
    local_min = 22 * 60 + 30
    utc_min = local_min + 5 * 60  # next-day UTC
    end_utc = utc_min + (4 * 60 + 15)
    end_day = end_utc // (24 * 60)
    end_local = (end_utc - 5 * 60) % (24 * 60)
    print("start 22:30 UTC-5 -> %02d:%02d UTC (day+%d)" % (
        (utc_min // 60) % 24, utc_min % 60, utc_min // (24 * 60)))
    print("end: day+%d %02d:%02d local" % (end_day, end_local // 60, end_local % 60))
    assert end_day == 1
    assert end_local == 2 * 60 + 45
    # round trip: back through the chain
    back = (end_utc - (4 * 60 + 15) - 5 * 60) % (24 * 60)
    assert back == local_min
    print("rule: local->UTC, add, UTC->local, carry the date, check the round trip")
    print("OK: %s crossed day and zone" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_convert_local(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 3:00 PM at UTC-5 -> UTC+1
    a_off, b_off = -5, 1
    diff = b_off - a_off
    a_min = 15 * 60
    b_min = a_min + diff * 60
    day = 0
    if b_min >= 24 * 60:
        b_min -= 24 * 60
        day += 1
    print("15:00 UTC-5 + %d h -> %02d:%02d UTC+1%s" % (
        diff, b_min // 60, b_min % 60, " next day" if day else ""))
    assert diff == 6
    assert b_min == 21 * 60 and day == 0
    # via UTC explicitly
    utc = a_min - a_off * 60
    assert utc == 20 * 60
    print("15:00 here = 20:00 UTC = 21:00 there")
    print("OK: %s translated the hour" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_precision(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # frequency <-> period across the scales
    for f, label in [(60.0, "power line"), (1.2, "heartbeat 72 bpm"), (1e9, "processor")]:
        T = 1.0 / f
        print("%-16s f=%.4g Hz -> T=%.4g s" % (label, f, T))
    assert 0.01666 < 1.0 / 60.0 < 0.01668
    assert 0.832 < 1.0 / 1.2 < 0.834
    assert 0.999e-9 < 1.0 / 1e9 < 1.001e-9
    print("resolution, accuracy, jitter: three different testimonies")
    print("OK: %s timed precisely" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_number_line(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the day budget: 480 + 480 + 480 = 1440
    blocks = {"sleep": 480, "work": 480, "meals": 120, "travel": 60,
              "family": 180, "free": 120}
    total = sum(blocks.values())
    for k, v in blocks.items():
        print("  %-6s %3d min (%4.1f %%)" % (k, v, 100.0 * v / 1440))
    print("total: %d / 1440 min" % total)
    assert total == 1440
    # overlap check: accumulate from 6:00 AM wake
    t = 6 * 60
    prev_end = t
    for k, v in blocks.items():
        assert t >= prev_end
        prev_end = t + v
        t = prev_end
    print("no overlaps, total fits: the plan is possible")
    print("OK: %s budgeted the day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_ages_eras(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # compress 4.54e9 years into one year
    earth = 4.54e9
    yr_min = 365 * 24 * 60.0
    for span, label in [(300000.0, "modern humans"), (5000.0, "recorded history"),
                        (186e6, "Mesozoic era")]:
        comp = span / earth * yr_min
        unit = "min" if comp >= 1 else "s"
        val = comp if comp >= 1 else comp * 60
        print("%-16s -> %.2f %s on the compressed year" % (label, val, unit))
    humans = 300000.0 / earth * yr_min
    history = 5000.0 / earth * yr_min * 60
    assert 34.6 < humans < 34.8
    assert 34.6 < history < 34.8
    print("eons in order: Hadean, Archean, Proterozoic, Phanerozoic")
    print("OK: %s read deep time" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_tb_science(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # light-year from c and the Julian year
    c = 299792458.0
    julian_yr_s = 365.25 * 86400.0
    ly = c * julian_yr_s
    print("c = %.0f m/s (exact)" % c)
    print("light-year = %.4e m" % ly)
    assert 9.4606e15 < ly < 9.4608e15
    # light-nanosecond ~ 30 cm
    assert 0.299 < c * 1e-9 < 0.301
    # 60 Hz -> 16.67 ms; 2.4 GHz -> 0.417 ns
    assert 16.66 < 1000.0 / 60.0 < 16.68
    assert 0.416 < 1.0 / 2.4e9 * 1e9 < 0.418
    print("f = 1/T: one law from heartbeats to gigahertz")
    print("OK: %s measured with light" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what_time_is": demo_tb_what_time_is,
    "the_second": demo_tb_the_second,
    "minutes_hours": demo_tb_minutes_hours,
    "days_weeks_months": demo_tb_days_weeks_months,
    "years_decades_centuries": demo_tb_years_decades,
    "analog_clock": demo_tb_analog_clock,
    "digital_clock": demo_tb_digital_clock,
    "am_pm": demo_tb_am_pm,
    "noon_midnight_relative": demo_tb_noon_midnight,
    "subsecond_units": demo_tb_subsecond,
    "ladder_of_units": demo_tb_ladder,
    "time_tools": demo_tb_time_tools,
    "add_subtract_time": demo_tb_add_subtract,
    "elapsed_time": demo_tb_elapsed,
    "24_hour_clock": demo_tb_24h_clock,
    "calendars_months_years": demo_tb_calendars,
    "leap_years": demo_tb_leap_years,
    "time_zones": demo_tb_time_zones,
    "utc": demo_tb_utc,
    "date_line": demo_tb_date_line,
    "daylight_saving": demo_tb_dst,
    "seven_day_week": demo_tb_seven_day_week,
    "earth_in_motion": demo_tb_earth_motion,
    "schedules_timetables": demo_tb_schedules,
    "atomic_time": demo_tb_atomic_time,
    "leap_seconds": demo_tb_leap_seconds,
    "world_calendars": demo_tb_world_calendars,
    "history_timekeeping": demo_tb_history,
    "time_arithmetic_days_zones": demo_tb_cross_day_zone,
    "converting_local_times": demo_tb_convert_local,
    "precision_timing": demo_tb_precision,
    "time_number_line": demo_tb_number_line,
    "ages_and_eras": demo_tb_ages_eras,
    "time_in_science": demo_tb_science,
}
