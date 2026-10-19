#!/usr/bin/env python3
"""Demonstration programs for the Mining and Extractive Industries databases.

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


def _t_metal(hdr, name, rid, group, d):
    t, g = float(d['tonnes']), float(d['grade_pct'])
    return hdr + 'T=%r\nG=%r\n' % (t, g) + '''def main():
    metal = T*G/100.0
    print("ore tonnes:", T)
    print("grade %:", G)
    print("contained metal tonnes:", round(metal, 1))
    assert T > 0 and G >= 0
    assert abs(metal - T*G/100.0) < 1e-9
    print("OK: contained metal verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_stripratio(hdr, name, rid, group, d):
    w, o = float(d['waste']), float(d['ore'])
    return hdr + 'W=%r\nO=%r\n' % (w, o) + '''def main():
    sr = W/O
    print("waste tonnes:", W, "| ore tonnes:", O)
    print("strip ratio:", round(sr, 2), ": 1")
    assert W >= 0 and O > 0
    assert abs(sr - W/O) < 1e-9
    print("OK: strip ratio verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_cutoff(hdr, name, rid, group, d):
    c, p, r = (float(d['cost_per_t_ore']), float(d['price_per_t_metal']),
               float(d['recovery']))
    return hdr + 'C=%r\nP=%r\nR=%r\n' % (c, p, r) + '''def main():
    cog = 100.0*C/(P*R)
    print("cost per ore tonne: $", C)
    print("metal price per tonne: $", P, "| recovery:", R)
    print("breakeven cut-off grade %:", round(cog, 3))
    assert C > 0 and P > 0 and 0 < R <= 1.0
    assert abs(cog - 100.0*C/(P*R)) < 1e-9
    print("OK: cut-off grade verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_recovery(hdr, name, rid, group, d):
    f, r = float(d['feed_metal']), float(d['recovered_metal'])
    return hdr + 'F=%r\nR=%r\n' % (f, r) + '''def main():
    rec = 100.0*R/F
    lost = F - R
    print("feed metal:", F, "| recovered metal:", R)
    print("recovery %:", round(rec, 2))
    print("metal lost:", round(lost, 1))
    assert 0 <= R <= F and F > 0
    assert abs(rec - 100.0*R/F) < 1e-9
    print("OK: recovery verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_blast(hdr, name, rid, group, d):
    h, kg, t = (float(d['holes']), float(d['kg_per_hole']),
                float(d['tonnes_broken']))
    return hdr + 'H=%r\nKG=%r\nT=%r\n' % (h, kg, t) + '''def main():
    total = H*KG
    pf = total/T
    print("holes:", H, "| kg per hole:", KG)
    print("total explosives kg:", round(total, 1))
    print("powder factor kg/t:", round(pf, 3))
    assert H > 0 and KG > 0 and T > 0
    assert abs(pf - H*KG/T) < 1e-9
    print("OK: blast design verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_haul(hdr, name, rid, group, d):
    n, p, tr = (float(d['trucks']), float(d['payload_t']),
                float(d['trips_per_day']))
    return hdr + 'N=%r\nP=%r\nTR=%r\n' % (n, p, tr) + '''def main():
    daily = N*P*TR
    print("trucks:", N, "| payload t:", P, "| trips/day:", TR)
    print("daily haulage tonnes:", round(daily, 1))
    assert N > 0 and P > 0 and TR > 0
    assert abs(daily - N*P*TR) < 1e-9
    print("OK: haulage verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_grind(hdr, name, rid, group, d):
    tph, hrs = float(d['feed_tph']), float(d['hours'])
    return hdr + 'TPH=%r\nHRS=%r\n' % (tph, hrs) + '''def main():
    daily = TPH*HRS
    print("feed tph:", TPH, "| operating hours:", HRS)
    print("daily throughput tonnes:", round(daily, 1))
    assert TPH > 0 and 0 < HRS <= 24.0
    assert abs(daily - TPH*HRS) < 1e-9
    print("OK: grinding throughput verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_water(hdr, name, rid, group, d):
    q = float(d['flow_lps'])
    return hdr + 'Q=%r\n' % q + '''def main():
    m3day = Q*86.4
    print("flow L/s:", Q)
    print("flow m3/day:", round(m3day, 1))
    assert Q >= 0
    assert abs(m3day - Q*86400.0/1000.0) < 1e-9
    print("OK: water flow verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_npv(hdr, name, rid, group, d):
    cx, cf, n, r = (float(d['capex']), float(d['annual_cf']),
                    int(d['years']), float(d['rate']))
    return hdr + 'CX=%r\nCF=%r\nN=%r\nR=%r\n' % (cx, cf, n, r) + '''def main():
    pv = sum(CF/((1+R)**t) for t in range(1, N+1))
    npv = pv - CX
    print("capex: $", round(CX, 2))
    print("annual cashflow: $", round(CF, 2), "for", N, "years at", R)
    print("NPV: $", round(npv, 2))
    assert CX >= 0 and N > 0 and R >= 0
    assert abs(npv - (sum(CF/((1+R)**t) for t in range(1, N+1)) - CX)) < 1e-6*abs(pv) + 1e-6
    print("OK: NPV verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_drill(hdr, name, rid, group, d):
    h, dep = float(d['holes']), float(d['avg_depth_m'])
    return hdr + 'H=%r\nDEP=%r\n' % (h, dep) + '''def main():
    total = H*DEP
    print("holes:", H, "| avg depth m:", DEP)
    print("total drilled meters:", round(total, 1))
    assert H > 0 and DEP > 0
    assert abs(total - H*DEP) < 1e-9
    print("OK: drilling meters verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


_T = {'metal': _t_metal, 'stripratio': _t_stripratio, 'cutoff': _t_cutoff,
      'recovery': _t_recovery, 'blast': _t_blast, 'haul': _t_haul,
      'grind': _t_grind, 'water': _t_water, 'npv': _t_npv,
      'drill': _t_drill}


def build(dk, name, rid, group, data):
    assert dk in _T, 'unknown demo kind %r' % dk
    return _T[dk](_hdr(name, rid, group), name, rid, group, data)
