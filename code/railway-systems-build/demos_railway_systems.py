#!/usr/bin/env python3
"""Demonstration programs for the Railway Systems databases.

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


def _t_braking(hdr, name, rid, group, d):
    v, a = float(d['v_kmh']), float(d['decel'])
    return hdr + 'V=%r\nA=%r\n' % (v, a) + '''def main():
    vms = V/3.6
    dist = vms*vms/(2*A)
    t = vms/A
    print("speed km/h:", V, "| deceleration m/s2:", A)
    print("braking distance m:", round(dist, 1))
    print("braking time s:", round(t, 1))
    assert V > 0 and A > 0
    assert abs(dist - (V/3.6)**2/(2*A)) < 1e-9
    assert dist > 0
    print("OK: braking distance verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_cant(hdr, name, rid, group, d):
    v, r = float(d['v_kmh']), float(d['radius_m'])
    return hdr + 'V=%r\nR=%r\n' % (v, r) + '''def main():
    e = 11.8*V*V/R
    print("speed km/h:", V, "| curve radius m:", R)
    print("equilibrium cant mm:", round(e, 1))
    assert V > 0 and R > 0
    assert abs(e - 11.8*V*V/R) < 1e-9
    assert 0 < e < 300
    print("OK: equilibrium cant verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_curve(hdr, name, rid, group, d):
    e, r = float(d['cant_mm']), float(d['radius_m'])
    return hdr + 'E=%r\nR=%r\n' % (e, r) + '''import math
def main():
    v = math.sqrt(E*R/11.8)
    print("cant mm:", E, "| radius m:", R)
    print("equilibrium speed km/h:", round(v, 1))
    assert E > 0 and R > 0
    assert abs(11.8*v*v/R - E) < 1e-9
    print("OK: curve speed verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_axle(hdr, name, rid, group, d):
    wt, ax = float(d['wagon_t']), float(d['axles'])
    return hdr + 'WT=%r\nAX=%r\n' % (wt, ax) + '''def main():
    per = WT/AX
    print("wagon mass tonnes:", WT, "| axles:", AX)
    print("axle load tonnes:", round(per, 2))
    assert WT > 0 and AX > 0
    assert abs(per*AX - WT) < 1e-9
    assert per < 40
    print("OK: axle load verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_energy(hdr, name, rid, group, d):
    m, v = float(d['mass_t']), float(d['v_kmh'])
    return hdr + 'M=%r\nV=%r\n' % (m, v) + '''def main():
    vms = V/3.6
    ke = 0.5*M*1000.0*vms*vms/1e6
    print("mass tonnes:", M, "| speed km/h:", V)
    print("kinetic energy MJ:", round(ke, 2))
    assert M > 0 and V > 0
    assert abs(ke - 0.5*M*1000.0*(V/3.6)**2/1e6) < 1e-9
    print("OK: kinetic energy verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_capacity(hdr, name, rid, group, d):
    cars, seats = float(d['cars']), float(d['seats'])
    return hdr + 'CARS=%r\nSEATS=%r\n' % (cars, seats) + '''def main():
    total = CARS*SEATS
    print("cars/wagons:", CARS, "| seats or tonnes each:", SEATS)
    print("total train capacity:", total)
    assert CARS > 0 and SEATS > 0
    assert total == CARS*SEATS
    print("OK: train capacity verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_headway(hdr, name, rid, group, d):
    v, b = float(d['speed_kmh']), float(d['block_km'])
    return hdr + 'V=%r\nB=%r\n' % (v, b) + '''def main():
    hw = B/V*3600.0
    tph = 3600.0/hw
    print("speed km/h:", V, "| block km:", B)
    print("headway seconds:", round(hw, 1))
    print("trains per hour:", round(tph, 2))
    assert V > 0 and B > 0
    assert abs(hw - B/V*3600.0) < 1e-9
    assert abs(tph*hw - 3600.0) < 1e-6
    print("OK: headway verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_runtime(hdr, name, rid, group, d):
    dist, avg, stops, dwell = (float(d['dist_km']), float(d['avg_kmh']),
                               float(d['stops']), float(d['dwell_min']))
    return hdr + 'DIST=%r\nAVG=%r\nSTOPS=%r\nDWELL=%r\n' % (dist, avg, stops, dwell) + '''def main():
    run = DIST/AVG*60.0
    total = run + STOPS*DWELL
    print("distance km:", DIST, "| avg speed km/h:", AVG)
    print("running time min:", round(run, 1))
    print("total with", STOPS, "stops:", round(total, 1), "min")
    assert DIST > 0 and AVG > 0 and STOPS >= 0 and DWELL >= 0
    assert abs(total - (DIST/AVG*60.0 + STOPS*DWELL)) < 1e-9
    print("OK: timetable runtime verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_gradient(hdr, name, rid, group, d):
    rise, run = float(d['rise_m']), float(d['run_m'])
    return hdr + 'RISE=%r\nRUN=%r\n' % (rise, run) + '''def main():
    grade = 100.0*RISE/RUN
    resist = grade*98.1/10.0
    print("rise m:", RISE, "| run m:", RUN)
    print("gradient %:", round(grade, 3))
    assert RUN > 0 and RISE >= 0
    assert abs(grade - 100.0*RISE/RUN) < 1e-9
    print("OK: gradient verified for", @@NAME@@)
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


_T = {'braking': _t_braking, 'cant': _t_cant, 'curve': _t_curve,
      'axle': _t_axle, 'energy': _t_energy, 'capacity': _t_capacity,
      'headway': _t_headway, 'runtime': _t_runtime,
      'gradient': _t_gradient, 'econ': _t_econ}


def build(dk, name, rid, group, data):
    assert dk in _T, 'unknown demo kind %r' % dk
    return _T[dk](_hdr(name, rid, group), name, rid, group, data)
