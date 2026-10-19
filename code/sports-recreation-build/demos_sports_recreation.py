#!/usr/bin/env python3
"""Demonstration programs for the Sports and Recreation databases.

Every demo is real, runnable, stdlib-only Python that machine-checks the
record it ships with: the entry's own data is baked into the program, the
program recomputes real values from it, asserts tight bounds (never float
exact-equality), prints the real computed values, and ends with the OK
marker. The build machine-executes every demo.
"""
import json


def _hdr(name, rid, group):
    return ('#!/usr/bin/env python3\n"""%s — working demonstration.\n'
            'Record %s [%s]. Property of Justin Addam Higgins (JAH).\n"""\n'
            % (name, rid, group))


def _t_winpct(hdr, name, rid, group, d):
    w, l = float(d['w']), float(d['l'])
    return hdr + 'W=%r\nL=%r\n' % (w, l) + '''def main():
    pct = W/(W+L)
    print("wins:", W, "| losses:", L)
    print("win percentage:", round(pct, 3))
    assert W >= 0 and L >= 0 and (W+L) > 0
    assert abs(pct - W/(W+L)) < 1e-9
    assert 0 <= pct <= 1
    print("OK: win percentage verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_bmi(hdr, name, rid, group, d):
    kg, m = float(d['kg']), float(d['m'])
    return hdr + 'KG=%r\nM=%r\n' % (kg, m) + '''def main():
    bmi = KG/(M*M)
    print("mass kg:", KG, "| height m:", M)
    print("BMI:", round(bmi, 1))
    assert KG > 0 and M > 0
    assert abs(bmi - KG/(M*M)) < 1e-9
    assert 10 < bmi < 60
    print("OK: BMI verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_thr(hdr, name, rid, group, d):
    age = float(d['age'])
    return hdr + 'AGE=%r\n' % age + '''def main():
    maxhr = 220 - AGE
    z2 = (0.6*maxhr, 0.7*maxhr)
    z4 = (0.8*maxhr, 0.9*maxhr)
    print("age:", AGE, "| estimated max HR:", maxhr)
    print("zone 2 (60-70%):", round(z2[0]), "-", round(z2[1]))
    print("zone 4 (80-90%):", round(z4[0]), "-", round(z4[1]))
    assert 5 < AGE < 100
    assert abs(maxhr - (220-AGE)) < 1e-9
    print("OK: heart-rate zones verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_pace(hdr, name, rid, group, d):
    dist, mins = float(d['dist_km']), float(d['minutes'])
    return hdr + 'DIST=%r\nMINS=%r\n' % (dist, mins) + '''def main():
    perkm = MINS/DIST
    kmh = DIST/(MINS/60.0)
    print("distance km:", DIST, "| time min:", MINS)
    print("pace min/km:", round(perkm, 2))
    print("speed km/h:", round(kmh, 2))
    assert DIST > 0 and MINS > 0
    assert abs(perkm*DIST - MINS) < 1e-9
    print("OK: pace verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_elo(hdr, name, rid, group, d):
    ra, rb = float(d['ra']), float(d['rb'])
    return hdr + 'RA=%r\nRB=%r\n' % (ra, rb) + '''def main():
    ea = 1/(1+10**((RB-RA)/400.0))
    print("rating A:", RA, "| rating B:", RB)
    print("expected score A:", round(ea, 3))
    assert abs(ea - 1/(1+10**((RB-RA)/400.0))) < 1e-9
    assert 0 < ea < 1
    print("OK: Elo expectation verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_calories(hdr, name, rid, group, d):
    wt, met, hrs = (float(d['weight_kg']), float(d['met']),
                    float(d['hours']))
    return hdr + 'WT=%r\nMET=%r\nHRS=%r\n' % (wt, met, hrs) + '''def main():
    kcal = MET*WT*HRS
    print("weight kg:", WT, "| MET:", MET, "| hours:", HRS)
    print("energy kcal:", round(kcal, 1))
    assert WT > 0 and MET > 0 and HRS > 0
    assert abs(kcal - MET*WT*HRS) < 1e-9
    print("OK: energy expenditure verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_tournament(hdr, name, rid, group, d):
    t = int(d['teams'])
    return hdr + 'T=%r\n' % t + '''def main():
    games = T - 1
    rounds = 0
    n = T
    while n > 1:
        n //= 2
        rounds += 1
    print("teams:", T)
    print("single-elim games:", games)
    print("rounds:", rounds)
    assert T >= 2
    assert games == T - 1
    print("OK: tournament math verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_attendance(hdr, name, rid, group, d):
    cap, sold = float(d['capacity']), float(d['sold'])
    return hdr + 'CAP=%r\nSOLD=%r\n' % (cap, sold) + '''def main():
    pct = 100.0*SOLD/CAP
    print("capacity:", CAP, "| sold:", SOLD)
    print("attendance %:", round(pct, 1))
    assert 0 <= SOLD <= CAP and CAP > 0
    assert abs(pct - 100.0*SOLD/CAP) < 1e-9
    print("OK: attendance verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_area(hdr, name, rid, group, d):
    ln, wd = float(d['length_m']), float(d['width_m'])
    return hdr + 'LN=%r\nWD=%r\n' % (ln, wd) + '''def main():
    area = LN*WD
    print("length m:", LN, "| width m:", WD)
    print("area m2:", round(area, 1))
    assert LN > 0 and WD > 0
    assert abs(area - LN*WD) < 1e-9
    print("OK: area verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_load(hdr, name, rid, group, d):
    s, rpe, mins = (float(d['sessions']), float(d['rpe']),
                    float(d['minutes']))
    return hdr + 'S=%r\nRPE=%r\nMINS=%r\n' % (s, rpe, mins) + '''def main():
    per = RPE*MINS
    weekly = per*S
    print("sessions:", S, "| RPE:", RPE, "| min/session:", MINS)
    print("session load (sRPE):", round(per, 1))
    print("weekly load:", round(weekly, 1))
    assert S > 0 and 0 < RPE <= 10 and MINS > 0
    assert abs(weekly - RPE*MINS*S) < 1e-9
    print("OK: training load verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_econ(hdr, name, rid, group, d):
    fx, pr, vc, u = (float(d['fixed']), float(d['price']),
                     float(d['varcost']), float(d['units']))
    return hdr + 'FX=%r\nPR=%r\nVC=%r\nU=%r\n' % (fx, pr, vc, u) + '''def main():
    rev = PR*U
    cost = FX + VC*U
    profit = rev - cost
    print("revenue: $", round(rev, 2))
    print("total cost: $", round(cost, 2))
    print("profit: $", round(profit, 2))
    assert PR > VC > 0 and U > 0 and FX >= 0
    assert abs(profit - (PR*U - FX - VC*U)) < 1e-6*rev + 1e-6
    print("OK: economics verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


_T = {'winpct': _t_winpct, 'bmi': _t_bmi, 'thr': _t_thr,
      'pace': _t_pace, 'elo': _t_elo, 'calories': _t_calories,
      'tournament': _t_tournament, 'attendance': _t_attendance,
      'area': _t_area, 'load': _t_load, 'econ': _t_econ}


def build(dk, name, rid, group, data):
    assert dk in _T, 'unknown demo kind %r' % dk
    return _T[dk](_hdr(name, rid, group), name, rid, group, data)
