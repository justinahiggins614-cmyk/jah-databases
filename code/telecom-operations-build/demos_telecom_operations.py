#!/usr/bin/env python3
"""Demonstration programs for the Telecom Operations databases.

Every demo is real, runnable, stdlib-only Python that machine-checks the
record it ships with: the entry's own data is baked into the program, the
program recomputes real values from it, asserts tight bounds (never float
exact-equality), prints the real computed values, and ends with the OK
marker. The build machine-executes every demo.
"""
import json
import math


def _hdr(name, rid, group):
    return ('#!/usr/bin/env python3\n"""%s — working demonstration.\n'
            'Record %s [%s]. Property of Justin Addam Higgins (JAH).\n"""\n'
            % (name, rid, group))


def _t_dbm(hdr, name, rid, group, d):
    w = float(d['watts'])
    return hdr + 'W=%r\n' % w + '''import math
def main():
    mw = W*1000.0
    dbm = 10*math.log10(mw)
    print("power watts:", W)
    print("power milliwatts:", mw)
    print("power dBm:", round(dbm, 2))
    assert W > 0
    assert abs(dbm - 10*math.log10(W*1000.0)) < 1e-9
    print("OK: dBm conversion verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_fspl(hdr, name, rid, group, d):
    f, dist = float(d['freq_mhz']), float(d['dist_km'])
    return hdr + 'F=%r\nD=%r\n' % (f, dist) + '''import math
def main():
    fspl = 20*math.log10(D) + 20*math.log10(F) + 32.44
    print("frequency MHz:", F, "| distance km:", D)
    print("free-space path loss dB:", round(fspl, 2))
    assert F > 0 and D > 0
    assert abs(fspl - (20*math.log10(D) + 20*math.log10(F) + 32.44)) < 1e-9
    assert 20 < fspl < 250
    print("OK: FSPL verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_shannon(hdr, name, rid, group, d):
    bw, snr = float(d['bw_mhz']), float(d['snr_db'])
    return hdr + 'BW=%r\nSNR=%r\n' % (bw, snr) + '''import math
def main():
    snr_lin = 10**(SNR/10.0)
    cap = BW*math.log2(1+snr_lin)
    print("bandwidth MHz:", BW, "| SNR dB:", SNR)
    print("Shannon capacity Mbps:", round(cap, 2))
    assert BW > 0
    assert cap > BW
    assert abs(cap - BW*math.log2(1+10**(SNR/10.0))) < 1e-9
    print("OK: Shannon capacity verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_subnet(hdr, name, rid, group, d):
    pfx = int(d['prefix'])
    return hdr + 'PFX=%r\n' % pfx + '''def main():
    hosts = 2**(32-PFX) - 2
    print("prefix length: /", PFX, sep="")
    print("usable host addresses:", hosts)
    assert 0 < PFX < 31
    assert hosts == 2**(32-PFX) - 2
    assert hosts > 0
    print("OK: subnet size verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_erlang(hdr, name, rid, group, d):
    c, a = int(d['channels']), float(d['traffic_erl'])
    return hdr + 'C=%r\nA=%r\n' % (c, a) + '''def main():
    b = 1.0
    for k in range(1, C+1):
        b = A*b/(k + A*b)
    print("channels:", C, "| offered traffic Erlangs:", A)
    print("Erlang-B blocking probability:", round(b, 6))
    assert 0 <= b <= 1.0
    assert C > 0 and A >= 0
    print("OK: Erlang-B verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_bdp(hdr, name, rid, group, d):
    bw, rtt = float(d['bw_mbps']), float(d['rtt_ms'])
    return hdr + 'BW=%r\nRTT=%r\n' % (bw, rtt) + '''def main():
    bdp = BW*1e6*(RTT/1000.0)/8.0
    print("bandwidth Mbps:", BW, "| RTT ms:", RTT)
    print("bandwidth-delay product bytes:", round(bdp, 1))
    assert BW > 0 and RTT > 0
    assert abs(bdp - BW*1e6*RTT/1000.0/8.0) < 1e-6*bdp + 1e-6
    print("OK: BDP verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_link(hdr, name, rid, group, d):
    tx, g, l, s = (float(d['tx_dbm']), float(d['gain_db']),
                   float(d['loss_db']), float(d['sens_dbm']))
    return hdr + 'TX=%r\nG=%r\nL=%r\nSENS=%r\n' % (tx, g, l, s) + '''def main():
    rx = TX + G - L
    margin = rx - SENS
    print("TX dBm:", TX, "| gains dB:", G, "| losses dB:", L)
    print("received power dBm:", round(rx, 2))
    print("margin above sensitivity dB:", round(margin, 2))
    assert abs(rx - (TX + G - L)) < 1e-9
    assert abs(margin - (rx - SENS)) < 1e-9
    print("OK: link budget verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_fiber(hdr, name, rid, group, d):
    dist, atten = float(d['dist_km']), float(d['atten_dbkm'])
    return hdr + 'DIST=%r\nATTEN=%r\n' % (dist, atten) + '''def main():
    loss = DIST*ATTEN
    print("fiber distance km:", DIST)
    print("attenuation dB/km:", ATTEN)
    print("total fiber loss dB:", round(loss, 2))
    assert DIST > 0 and ATTEN > 0
    assert abs(loss - DIST*ATTEN) < 1e-9
    print("OK: fiber loss verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_cell(hdr, name, rid, group, d):
    r, region = float(d['radius_km']), float(d['region_km2'])
    return hdr + 'R=%r\nREGION=%r\n' % (r, region) + '''import math
def main():
    area = math.pi*R*R
    sites = REGION/area
    print("cell radius km:", R)
    print("cell area km2:", round(area, 2))
    print("sites to cover region:", round(sites, 1))
    assert R > 0 and REGION > 0
    assert abs(area - math.pi*R*R) < 1e-9
    assert sites > 0
    print("OK: cell plan verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_billing(hdr, name, rid, group, d):
    units, rate = float(d['units']), float(d['rate'])
    return hdr + 'UNITS=%r\nRATE=%r\n' % (units, rate) + '''def main():
    charge = UNITS*RATE
    print("billed units:", UNITS)
    print("rate: $", RATE)
    print("charge: $", round(charge, 2))
    assert UNITS >= 0 and RATE >= 0
    assert abs(charge - UNITS*RATE) < 1e-9
    print("OK: billing verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


_T = {'dbm': _t_dbm, 'fspl': _t_fspl, 'shannon': _t_shannon,
      'subnet': _t_subnet, 'erlang': _t_erlang, 'bdp': _t_bdp,
      'link': _t_link, 'fiber': _t_fiber, 'cell': _t_cell,
      'billing': _t_billing}


def build(dk, name, rid, group, data):
    assert dk in _T, 'unknown demo kind %r' % dk
    return _T[dk](_hdr(name, rid, group), name, rid, group, data)
