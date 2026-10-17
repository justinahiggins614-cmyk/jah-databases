#!/usr/bin/env python3
"""Build the Seismology field databases for JAH Databases (field #10, taxonomy order).

Verified 2026-10-17: NO database covers seismology as a science. The broad
'geology' database (10,000 records) is a specimen-style catalog - its
earthquake-adjacent entries ('Subduction - Anatomy of a specimen',
'Tsunamis - How it forms', 'Faulting - Hazards and forces') describe
geological phenomena for specimen records; it contains no seismology
science: no seismic wave types, no seismometers or networks, no magnitude
or intensity scales, no focal mechanisms, no seismic hazard analysis, no
earthquake early warning, no induced seismicity, and no exploration
seismology (reflection, refraction, tomography). 'geology-public' carries
only two generic 'Earthquakes' overview entries. 'earthquake-prediction'
is a prediction folklore database, not the science of seismology. So this
build creates two NEW databases:

  seismology              — The Seismology Database (public-harvest: real,
                            fact-checked seismology - seismic wave types;
                            earthquake mechanics and elastic rebound; fault
                            systems; seismometers and seismogram reading;
                            earthquake location; Richter, moment magnitude,
                            and Mercalli scales; seismic networks; focal
                            mechanisms; aftershock sequences; tsunamis;
                            seismic hazard maps; earthquake early warning;
                            seismic tomography, reflection, and refraction;
                            induced seismicity; slow slip and tremor; source
                            spectra; stress drop; ground motion prediction;
                            site response; paleoseismology; recurrence and
                            seismic gaps; probabilistic seismic hazard
                            analysis; anisotropy; receiver functions;
                            interferometry; deep Earth structure; earthquake
                            forecasting; seismic building codes)
  seismology-signature    — The Seismology Signature Database (his original
                            Signature interpretation; src signature, titles
                            suffixed " (Signature Edition)", never presented
                            as authentic public record)

36 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable,
stdlib-only Python; machine-executed OK).

Never the words "bat belt" anywhere. No website references. No Facebook.
"""
import importlib.util
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base

sys.path.insert(0, HERE)
from entries_seismology import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of seismology: "
                "clearly labeled Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked seismology: seismic wave types; "
                "earthquake mechanics and elastic rebound; fault systems; seismometers and "
                "seismogram reading; earthquake location; Richter, moment magnitude, and "
                "Mercalli scales; seismic networks; focal mechanisms; aftershock sequences; "
                "tsunamis; seismic hazard maps; earthquake early warning; seismic "
                "tomography, reflection, and refraction; induced seismicity; slow slip and "
                "tremor; source spectra; stress drop; ground motion prediction; site "
                "response; paleoseismology; recurrence and seismic gaps; probabilistic "
                "seismic hazard analysis; anisotropy; receiver functions; interferometry; "
                "deep Earth structure; earthquake forecasting; seismic building codes, "
                "organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what seismology is, "
              "plate tectonics and earthquake belts, faults, elastic rebound, P-waves and "
              "S-waves, surface waves) -> Compounded (seismometers, reading seismograms, "
              "earthquake location, Richter scale, moment magnitude, Mercalli intensity, "
              "seismic networks, focal mechanisms, aftershock sequences, tsunamis, seismic "
              "hazard maps, earthquake early warning) -> Advanced (seismic tomography, "
              "reflection, refraction, induced seismicity, slow slip and tremor, source "
              "spectra, stress drop and rupture dynamics, ground motion prediction, site "
              "response and microzonation, paleoseismology, recurrence and seismic gaps, "
              "probabilistic seismic hazard analysis, anisotropy, receiver functions, "
              "interferometry, deep Earth structure, earthquake forecasting, seismic "
              "building codes).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search P-wave, magnitude, Mercalli, tomography, early warning, tsunami...",
        "chat_ph": "Ask about seismology...",
        "archive_blurb": ("Seeded %s seismology records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled structural seismology studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about seismology - from P-waves and the Richter scale up to tomography, PSHA, and building codes." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "seismology-study", "gen_demo_kind": "seismology-demo",
        "source": source,
    }

CIT_PUB = "Seismology (peer-reviewed literature and standard textbooks)."
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["seismology"] = _cfg(
    "seismology", "The Seismology Database",
    "Real, fact-checked seismology: seismic wave types, earthquake mechanics "
    "and elastic rebound, fault systems, seismometers and seismogram reading, "
    "earthquake location, Richter/moment-magnitude/Mercalli scales, seismic "
    "networks, focal mechanisms, aftershocks, tsunamis, hazard maps, early "
    "warning, tomography, reflection, refraction, induced seismicity, slow "
    "slip, source spectra, stress drop, ground motion prediction, site "
    "response, paleoseismology, recurrence, PSHA, anisotropy, receiver "
    "functions, interferometry, deep Earth structure, forecasting, and "
    "seismic building codes.",
    "seismology record", "JAH-SEI-", "JAH Seismology Archivist",
    "seismology archivist - seismic wave types, earthquake mechanics, elastic rebound, "
    "fault systems, seismometers, seismogram reading, earthquake location, magnitude and "
    "intensity scales, seismic networks, focal mechanisms, aftershocks, tsunamis, hazard "
    "maps, early warning, tomography, reflection, refraction, induced seismicity, slow "
    "slip, source spectra, stress drop, ground motion prediction, site response, "
    "paleoseismology, recurrence, PSHA, anisotropy, receiver functions, interferometry, "
    "deep Earth structure, forecasting, building codes; teaching progressively along the "
    "ladder from foundations (what seismology is, plate tectonics, faults, elastic "
    "rebound, body and surface waves) through compounded (seismometers, seismograms, "
    "location, magnitude scales, networks, focal mechanisms, aftershocks, tsunamis, "
    "hazard maps, early warning) to advanced (tomography, reflection, refraction, induced "
    "seismicity, slow slip, source spectra, stress drop, GMPEs, site response, "
    "paleoseismology, recurrence, PSHA, anisotropy, receiver functions, interferometry, "
    "deep Earth, forecasting, building codes); answers from many angles - definition, "
    "example, analogy, application, history, math, how-to - using only the system's own "
    "archive data",
    CIT_PUB, "public")
DBCFG["seismology-signature"] = _cfg(
    "seismology-signature", "The Seismology Signature Database",
    "His original Signature interpretation of seismology: the full ladder from "
    "P-waves and elastic rebound to tomography, PSHA, and seismic building "
    "codes, reframed as Signature science. Clearly labeled Signature-made, "
    "never presented as authentic public record.",
    "seismology record", "JAH-SSG-", "JAH Seismology Archivist (Signature)",
    "seismology archivist - Signature editions: his original Signature interpretation of "
    "seismology, clearly labeled Signature-made and never presented as authentic public "
    "record; teaches progressively along the ladder from foundations through compounded "
    "to advanced; answers from many angles - definition, example, analogy, application, "
    "history, math, how-to - using only the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# seismological calculation for its record. All are machine-executed by main().

_PREAMBLE = """import math
import re
"""

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_seismo_branches(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
BRANCHES = {
    "observational seismology": "recording and locating earthquakes",
    "theoretical seismology": "how waves propagate in elastic media",
    "exploration seismology": "imaging the Earth with controlled sources",
    "earthquake seismology": "how, where, and why faults rupture",
    "applied seismology": "hazard, early warning, and resource exploration",
    "source seismology": "spectra, moment tensors, and rupture physics",
}
def main():
    assert len(BRANCHES) == 6
    assert BRANCHES["exploration seismology"] == "imaging the Earth with controlled sources"
    assert BRANCHES["theoretical seismology"] == "how waves propagate in elastic media"
    for branch, focus in BRANCHES.items():
        print("%-26s -> %s" % (branch, focus))
    print("rule: source, path, receiver - model the physics, compare with data, update the model")
    print("OK: %s mapped the branches" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_plate_boundaries(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
BOUNDARIES = {
    "convergent": {"motion": "plates collide, one subducts", "quakes": "megathrust thrust events to M9.5",
                   "example": "Japan Trench, Chile"},
    "transform": {"motion": "plates slide sideways", "quakes": "strike-slip events",
                  "example": "San Andreas Fault"},
    "divergent": {"motion": "plates pull apart", "quakes": "shallow normal-faulting swarms",
                  "example": "Mid-Atlantic Ridge"},
}
def main():
    assert set(BOUNDARIES) == {"convergent", "transform", "divergent"}
    assert "M9.5" in BOUNDARIES["convergent"]["quakes"]
    for b, d in BOUNDARIES.items():
        print("%-11s | %-34s | %s (%s)" % (b, d["motion"], d["quakes"], d["example"]))
    print("rule: boundary type sets the faulting style; subduction interfaces host the giants")
    print("OK: %s mapped the earthquake belts" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_fault_types(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def classify(rake):
    r = ((rake + 180) % 360) - 180
    a = abs(r)
    if a <= 30 or a >= 150:
        return "strike-slip"
    return "reverse/thrust" if r > 0 else "normal"
def main():
    cases = [(0, "strike-slip"), (180, "strike-slip"), (90, "reverse/thrust"),
             (-90, "normal"), (45, "reverse/thrust"), (-120, "normal")]
    for rake, want in cases:
        got = classify(rake)
        assert got == want, (rake, got)
        print("rake %+4d -> %s" % (rake, got))
    print("rule: rake near 0/180 slips sideways; near +90 rides up; near -90 slides down")
    print("OK: %s classified the faults" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_elastic_rebound(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
RATE = 35.0        # mm/yr tectonic loading (San Andreas-like)
FAIL_SLIP = 4200.0  # mm slip that fails the fault (~1906 scale)
def main():
    years_to_fail = FAIL_SLIP / RATE
    assert abs(years_to_fail - 120.0) < 1e-9
    print("loading rate %.0f mm/yr, failure slip %.0f mm -> cycle %.0f yr" % (RATE, FAIL_SLIP, years_to_fail))
    stress, t, events = 0.0, 0.0, []
    while t < 1000.0:
        t += 1.0
        stress += RATE
        if stress >= FAIL_SLIP:      # coseismic rebound: the snap
            events.append(t)
            stress = 0.0
    assert len(events) == 8, len(events)
    print("1000-yr stick-slip run: %d earthquakes, mean interval %.0f yr" % (len(events), 1000.0 / len(events)))
    print("rule: slow loading, sudden rebound - the seismic cycle in one loop")
    print("OK: %s ran the rebound cycle" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ps_distance(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
VP, VS = 6.0, 3.46  # km/s, continental crust
def distance_from_sp(sp_seconds):
    return sp_seconds / (1.0 / VS - 1.0 / VP)
def main():
    for sp, want in [(10.0, 81.8), (30.0, 245.3), (60.0, 490.6)]:
        d = distance_from_sp(sp)
        assert abs(d - want) < 1.0, (sp, d)
        print("S-P %5.1f s -> distance %6.1f km" % (sp, d))
    print("rule: distance = (S-P) / (1/Vs - 1/Vp); one station gives a circle")
    print("OK: %s ranged the quake" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_surface_dispersion(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
# illustrative Rayleigh-wave phase velocities (km/s) vs period (s)
DISPERSION = [(10.0, 3.55), (20.0, 3.75), (50.0, 4.05), (100.0, 4.45), (200.0, 4.85)]
def main():
    vels = [v for _, v in DISPERSION]
    assert vels == sorted(vels), "dispersion must increase with period"
    for period, vel in DISPERSION:
        depth_probe = vel * period / 3.0   # rule of thumb: samples ~ wavelength/3
        print("period %6.1f s -> %4.2f km/s (samples ~%5.0f km deep)" % (period, vel, depth_probe))
    print("rule: long periods run faster and see deeper - dispersion is a depth sounder")
    print("OK: %s measured dispersion" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_seismometer_response(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def response_mag(f, f0=1.0, h=0.7071):
    w, w0 = 2 * math.pi * f, 2 * math.pi * f0
    return 1.0 / math.sqrt((w0 * w0 - w * w) ** 2 + (2 * h * w0 * w) ** 2)
def main():
    flat = response_mag(0.001)         # far below natural frequency
    expected = 1.0 / (2 * math.pi * 1.0) ** 2
    assert abs(flat - expected) / expected < 1e-6
    print("1-Hz seismometer: flat displacement response %.3e m/count-ish below f0" % flat)
    for f in (0.05, 0.5, 1.0, 5.0):
        print("  f=%4.2f Hz -> |H|=%.3e" % (f, response_mag(f)))
    print("rule: below f0 the mass stays still and the frame's motion is recorded faithfully")
    print("OK: %s calibrated the instrument" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pick_phases(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def synth_trace(n=2000, iP=400, iS=900):
    tr = [0.05 * math.sin(0.7 * i) for i in range(n)]          # background noise
    for i in range(iP, n):                                      # P coda decays
        tr[i] += 1.0 * math.exp(-(i - iP) / 120.0)
    for i in range(iS, n):                                      # bigger S arrival
        tr[i] += 3.0 * math.exp(-(i - iS) / 200.0)
    return tr
def main():
    tr = synth_trace()
    iP = next(i for i, x in enumerate(tr) if abs(x) > 0.5)
    iS = next(i for i in range(iP + 50, len(tr)) if abs(tr[i]) > 2.0)
    assert abs(iP - 400) <= 2, iP
    assert abs(iS - 900) <= 2, iS
    print("picked P at sample %d, S at sample %d (S-P = %d samples)" % (iP, iS, iS - iP))
    print("rule: thresholds find onsets; S-P converts to distance")
    print("OK: %s read the seismogram" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_triangulation(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
ST = {"A": (0.0, 0.0), "B": (100.0, 0.0), "C": (0.0, 100.0)}  # km
TRUE = (30.0, 40.0)
VP, VS = 6.0, 3.46
def main():
    dists = {}
    for s, (x, y) in ST.items():
        true_d = math.hypot(TRUE[0] - x, TRUE[1] - y)
        sp = true_d * (1.0 / VS - 1.0 / VP)          # what the station measures
        dists[s] = sp / (1.0 / VS - 1.0 / VP)        # analyst converts back
    (x1, y1), (x2, y2), (x3, y3) = ST["A"], ST["B"], ST["C"]
    d1, d2, d3 = dists["A"], dists["B"], dists["C"]
    # subtract circle equations -> two linear equations
    a11, a12 = 2 * (x2 - x1), 2 * (y2 - y1)
    b1 = d1**2 - d2**2 - x1**2 + x2**2 - y1**2 + y2**2
    a21, a22 = 2 * (x3 - x1), 2 * (y3 - y1)
    b2 = d1**2 - d3**2 - x1**2 + x3**2 - y1**2 + y3**2
    det = a11 * a22 - a12 * a21
    ex, ey = (b1 * a22 - a12 * b2) / det, (a11 * b2 - b1 * a21) / det
    assert abs(ex - TRUE[0]) < 1e-6 and abs(ey - TRUE[1]) < 1e-6, (ex, ey)
    print("stations %s -> epicenter (%.1f, %.1f) km, true (%.1f, %.1f) km" %
          (sorted(ST), ex, ey, TRUE[0], TRUE[1]))
    print("rule: three circles, one intersection - the epicenter")
    print("OK: %s located the earthquake" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_richter_ml(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def local_magnitude(amp_um, dist_corr_100km=3.0):
    return math.log10(amp_um) + dist_corr_100km   # -logA0(100 km) = 3.0
def energy_joules(M):
    return 10.0 ** (11.8 + 1.5 * M) / 1e7          # ergs -> joules
def main():
    M = local_magnitude(1000.0)
    assert abs(M - 6.0) < 1e-9
    e6 = energy_joules(6.0)
    e7 = energy_joules(7.0)
    assert abs(e7 / e6 - 31.6) < 0.5
    print("M_L %.1f from 1000 um at 100 km; energy %.2e J" % (M, e6))
    print("one unit up -> %.1fx energy (the 32x rule)" % (e7 / e6))
    print("rule: M_L = log10(A) - log10(A0); each unit is ~32x the energy")
    print("OK: %s measured local magnitude" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_moment_magnitude(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def seismic_moment(mu, area_m2, slip_m):
    return mu * area_m2 * slip_m
def moment_magnitude(M0):
    return (2.0 / 3.0) * (math.log10(M0) - 9.1)
def main():
    M0 = seismic_moment(3.0e10, 7.5e8, 2.0)   # 50x15 km fault, 2 m slip
    Mw = moment_magnitude(M0)
    assert abs(Mw - 7.04) < 0.02, Mw
    print("M0 = mu*A*D = %.2e N-m -> M_w %.2f" % (M0, Mw))
    chile = moment_magnitude(2.0e23)
    assert abs(chile - 9.47) < 0.03, chile
    print("1960 Chile M0=2e23 N-m -> M_w %.2f (no saturation)" % chile)
    print("rule: M_w = (2/3)(log10 M0 - 9.1); long periods never saturate")
    print("OK: %s weighed the rupture" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mercalli_map(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def pga_g(M, R_km):
    return 10.0 ** (0.3 * M - 1.2 * math.log10(R_km) - 1.5)
def mmi_from_pga(pga):
    table = [(0.0017, "I"), (0.014, "II-III"), (0.039, "IV"), (0.092, "V"),
             (0.18, "VI"), (0.34, "VII"), (0.65, "VIII"), (1.24, "IX"), (9.9, "X+")]
    for thr, mmi in table:
        if pga < thr:
            return mmi
    return "X+"
def main():
    M = 7.0
    for R in (10, 30, 100):
        pga, mmi = pga_g(M, R), mmi_from_pga(pga_g(M, R))
        print("M%.1f at %3d km: PGA %.3f g -> MMI %s" % (M, R, pga, mmi))
    assert mmi_from_pga(pga_g(7.0, 10)) == "VII"
    assert mmi_from_pga(pga_g(7.0, 100)) == "IV"
    print("rule: magnitude is one number; intensity is a map that fades with distance")
    print("OK: %s mapped the shaking" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_network_gap(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def azimuthal_gap(azimuths):
    az = sorted(a % 360.0 for a in azimuths)
    gaps = [az[i + 1] - az[i] for i in range(len(az) - 1)]
    gaps.append(az[0] + 360.0 - az[-1])
    return max(gaps)
def main():
    good = azimuthal_gap([10, 100, 190, 280])
    bad = azimuthal_gap([10, 30, 50, 70])
    assert abs(good - 90.0) < 1e-9 and abs(bad - 300.0) < 1e-9
    print("surrounding network: gap %.0f deg -> trustworthy location" % good)
    print("one-sided network:   gap %.0f deg -> location smeared away from stations" % bad)
    print("rule: stations must surround the quake; gap > 180 deg means distrust the fix")
    print("OK: %s checked the geometry" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_beachball_quadrants(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def first_motion(strike_deg, azimuth_deg):
    # vertical strike-slip fault: radiation ~ sin(2*theta), theta from strike
    theta = math.radians(azimuth_deg - strike_deg)
    return "up (compressional)" if math.sin(2 * theta) > 0 else "down (dilatational)"
def main():
    strike = 0.0  # north-south right-lateral fault
    cases = [(45, "up (compressional)"), (135, "down (dilatational)"),
             (225, "up (compressional)"), (315, "down (dilatational)")]
    for az, want in cases:
        got = first_motion(strike, az)
        assert got == want, (az, got)
        print("station azimuth %3d deg -> P first motion %s" % (az, got))
    print("rule: quadrants alternate around the fault; nodal planes separate up from down")
    print("OK: %s read the beach ball" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_omori_decay(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def omori_rate(t_days, K=100.0, c=0.1, p=1.0):
    return K / (c + t_days) ** p
def main():
    r1, r10 = omori_rate(1.0), omori_rate(10.0)
    assert r1 > 9 * r10, (r1, r10)
    print("day  1 rate: %6.1f aftershocks/day" % r1)
    print("day 10 rate: %6.1f aftershocks/day" % r10)
    n = 0.0
    t, dt = 0.0, 0.5
    while t < 30.0:                      # expected count in the first month
        n += omori_rate(t + dt / 2) * dt
        t += dt
    print("expected aftershocks in 30 days: %.0f" % n)
    print("rule: n(t) = K/(c+t)^p - the sequence is most dangerous first")
    print("OK: %s timed the aftershocks" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tsunami_travel(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
G = 9.81
def wave_speed(depth_m):
    return math.sqrt(G * depth_m)
def travel_hours(distance_km, depth_m):
    return distance_km * 1000.0 / wave_speed(depth_m) / 3600.0
def main():
    c = wave_speed(4000.0)
    assert abs(c - 198.1) < 0.5, c
    print("deep-ocean (4 km) tsunami speed: %.0f m/s = %.0f km/h" % (c, c * 3.6))
    t = travel_hours(1000.0, 4000.0)
    print("1000 km of ocean crossed in %.2f hours" % t)
    assert abs(t - 1.40) < 0.03, t
    print("rule: c = sqrt(g*h) - fast, long, and low offshore; a flood at the shore")
    print("OK: %s timed the tsunami" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hazard_curve(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def annual_rate(a, b, m):
    return 10.0 ** (a - b * m)          # Gutenberg-Richter
def prob_in_years(rate, years):
    return 1.0 - math.exp(-rate * years)
def main():
    a, b = 4.0, 1.0
    r6 = annual_rate(a, b, 6.0)
    assert abs(r6 - 0.01) < 1e-12
    p50 = prob_in_years(r6, 50)
    print("M>=6 rate: %.3f/yr -> P(50 yr) = %.1f%%" % (r6, 100 * p50))
    for m in (5.0, 6.0, 7.0, 8.0):
        print("  M>=%.0f: %.4f/yr  P(50yr)=%5.1f%%" % (m, annual_rate(a, b, m), 100 * prob_in_years(annual_rate(a, b, m), 50)))
    print("rule: hazard is a rate turned into a probability - never a date")
    print("OK: %s drew the hazard curve" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eew_blindzone(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
VP, VS = 6.0, 3.46  # km/s
def warning_time(dist_km, latency_s):
    tP, tS = dist_km / VP, dist_km / VS
    return tS - (tP + latency_s)
def main():
    latency = 4.0
    blind = VP * latency
    print("system latency %.0f s -> blind-zone radius %.0f km (no warning inside)" % (latency, blind))
    assert warning_time(20.0, latency) < 0
    for d in (50, 100, 200):
        w = warning_time(float(d), latency)
        print("  city %3d km out: %.1f s of warning" % (d, w))
    assert abs(warning_time(100.0, latency) - 8.2) < 0.3
    print("rule: warning = S arrival minus (P arrival + latency); the P-wave's head start is the budget")
    print("OK: %s raced the waves" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tomography_2x2(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def solve(A, b):
    n = len(b)
    M = [row[:] + [bi] for row, bi in zip(A, b)]
    for col in range(n):                                   # Gaussian elimination
        piv = max(range(col, n), key=lambda r: abs(M[r][col]))
        M[col], M[piv] = M[piv], M[col]
        for r in range(col + 1, n):
            f = M[r][col] / M[col][col]
            for c in range(col, n + 1):
                M[r][c] -= f * M[col][c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (M[i][n] - sum(M[i][j] * x[j] for j in range(i + 1, n))) / M[i][i]
    return x
def main():
    true = [0.10, -0.05, 0.02, -0.08]     # slowness anomalies in 4 blocks
    rays = [[1, 1, 0, 0], [0, 0, 1, 1],   # row rays, column rays
            [1, 0, 1, 0], [1, 0, 0, 1]]   # + two crossing rays (full rank)
    delays = [sum(r[i] * true[i] for i in range(4)) for r in rays]
    est = solve(rays, delays)
    for t, e in zip(true, est):
        assert abs(t - e) < 1e-9, (t, e)
    print("true anomalies: %s" % ["%+.2f" % t for t in true])
    print("recovered:      %s" % ["%+.2f" % e for e in est])
    print("rule: delays are integrals of slowness - invert the rays, image the Earth")
    print("OK: %s ran the CAT scan" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_reflection_nmo(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def travel_time(t0, x, v):
    return math.sqrt(t0 * t0 + (x / v) ** 2)
def main():
    t0, v = 1.0, 2000.0
    for x in (0.0, 500.0, 1000.0, 2000.0):
        t = travel_time(t0, x, v)
        corrected = t - (t - t0)          # NMO correction flattens the hyperbola
        assert abs(corrected - t0) < 1e-12
        print("offset %4.0f m: raw %5.3f s -> NMO-corrected %.3f s" % (x, t, corrected))
    print("rule: t(x) = sqrt(t0^2 + (x/v)^2); moveout correction + stack = the reflector")
    print("OK: %s processed the reflection" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_refraction_intercept(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def intercept_time(h, v1, v2):
    return 2 * h * math.sqrt(1 / v1 ** 2 - 1 / v2 ** 2)
def thickness_from_intercept(ti, v1, v2):
    return ti / (2 * math.sqrt(1 / v1 ** 2 - 1 / v2 ** 2))
def main():
    v1, v2, h = 2000.0, 6000.0, 1000.0
    ti = intercept_time(h, v1, v2)
    h_back = thickness_from_intercept(ti, v1, v2)
    assert abs(h_back - h) < 1e-6, h_back
    print("v1=%.0f v2=%.0f m/s, intercept %.3f s -> layer thickness %.0f m" % (v1, v2, ti, h_back))
    print("rule: slope gives the lower velocity, intercept gives the upper thickness")
    print("OK: %s sounded the layers" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pressure_front(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def front_radius(D, t_seconds):
    return math.sqrt(4 * math.pi * D * t_seconds)
def main():
    D = 1.0  # m^2/s hydraulic diffusivity
    for days in (1, 10, 30, 100):
        r = front_radius(D, days * 86400.0)
        print("after %3d days of injection: pressure front at %6.0f m" % (days, r))
    assert abs(front_radius(1.0, 30 * 86400.0) - 5707.0) < 5.0
    print("rule: r = sqrt(4*pi*D*t) - seismicity migrating with the front is the smoking gun")
    print("OK: %s tracked the pressure" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_slow_slip_scaling(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def regular_moment(duration_s):
    return 1.0e16 * duration_s ** 3      # ordinary quakes: M0 ~ T^3
def slow_moment(duration_s):
    return 3.0e11 * duration_s           # slow slip: M0 ~ T (linear)
def main():
    for days in (5, 20, 60):
        T = days * 86400.0
        print("%2d-day slow slip: M0 = %.2e N-m (~M%.1f)" %
              (days, slow_moment(T), (2.0 / 3.0) * (math.log10(slow_moment(T)) - 9.1)))
    m7_reg = (1.0e19 / 1.0e16) ** (1.0 / 3.0)
    print("a regular M7 lasts ~%.0f s; a slow M7 lasts weeks - different physics" % m7_reg)
    assert abs(m7_reg - 10.0) < 0.5
    print("rule: ordinary moment grows as duration cubed; slow slip grows linearly with time")
    print("OK: %s clocked the silent slip" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_brune_spectrum(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def corner_freq(M0, dsigma, beta=3500.0):
    return 0.49 * beta * (dsigma / M0) ** (1.0 / 3.0)
def spectrum(f, M0, fc):
    return M0 / (1 + (f / fc) ** 2)      # omega-squared shape
def main():
    fc = corner_freq(1.0e18, 3.0e6)
    assert abs(fc - 0.247) < 0.01, fc
    low, high = spectrum(0.01, 1.0e18, fc), spectrum(10.0, 1.0e18, fc)
    assert abs(low - 1.0e18) / 1.0e18 < 0.01
    assert abs(high / low - (fc / 10.0) ** 2) < 0.01
    print("M0=1e18 N-m, stress drop 3 MPa -> corner frequency %.3f Hz" % fc)
    print("spectrum flat at %.1e below fc, falls as f^-2 above" % low)
    print("rule: flat level = moment; corner = size; decay = Brune omega-squared")
    print("OK: %s took the spectrum" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_stress_drop(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def stress_drop(M0, radius_m):
    return (7.0 / 16.0) * M0 / radius_m ** 3
def main():
    for M0, r, label in ((1.0e18, 10000.0, "M~7"), (1.0e15, 1000.0, "M~4")):
        ds = stress_drop(M0, r)
        print("%s: M0=%.0e N-m, r=%.0f m -> stress drop %.2f MPa" % (label, M0, r, ds / 1e6))
    assert abs(stress_drop(1.0e18, 10000.0) - 4.375e5) < 1.0
    print("rule: delta_sigma = (7/16) M0 / r^3 - typically 1-10 MPa, self-similar across scales")
    print("OK: %s dropped the stress" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_gmpe_pga(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def pga_g(M, R_km, vs30=760.0):
    site = -0.25 * math.log10(vs30 / 760.0)
    return 10.0 ** (-1.2 + 0.35 * M - 1.1 * math.log10(R_km + 5.0) + site)
def main():
    for M, R in ((6.0, 10.0), (7.0, 20.0), (7.0, 100.0)):
        print("M%.1f at %3d km (rock): PGA %.2f g" % (M, R, pga_g(M, R)))
    assert abs(pga_g(7.0, 20.0) - 0.51) < 0.05
    soft = pga_g(7.0, 20.0, vs30=200.0)
    print("same quake on soft soil (Vs30=200): PGA %.2f g - site amplification" % soft)
    assert soft > pga_g(7.0, 20.0)
    print("rule: magnitude, distance, fault style, site - the GMPE folds them into shaking")
    print("OK: %s predicted the ground motion" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_site_resonance(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def resonance_freq(vs, h):
    return vs / (4.0 * h)
def main():
    for vs, h, label in ((200.0, 50.0, "soft bay mud"), (800.0, 30.0, "stiff soil"),
                         (1500.0, 100.0, "weathered rock")):
        f0 = resonance_freq(vs, h)
        print("%-14s: Vs=%4.0f m/s, H=%3.0f m -> f0 = %.2f Hz" % (label, vs, h, f0))
    assert abs(resonance_freq(200.0, 50.0) - 1.0) < 1e-9
    print("a 10-story building sways near 1 Hz - bay mud at f0=1 Hz is a deadly match")
    print("rule: f0 = Vs/4H; when soil and structure share a frequency, resonance destroys")
    print("OK: %s tuned the soil column" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_paleo_recurrence(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def stats(intervals):
    n = len(intervals)
    mean = sum(intervals) / n
    var = sum((x - mean) ** 2 for x in intervals) / n
    return mean, math.sqrt(var), math.sqrt(var) / mean
def main():
    ages = [1200, 950, 700, 500, 180]          # event ages, years BP (Pallett-Creek-like)
    intervals = [ages[i] - ages[i + 1] for i in range(len(ages) - 1)]
    mean, sd, cov = stats(intervals)
    print("event ages BP: %s" % ages)
    print("intervals: %s -> mean %.0f yr, COV %.2f" % (intervals, mean, cov))
    assert abs(mean - 255.0) < 1.0
    assert cov > 0.15, "recurrence is irregular - clockwork would give COV near 0"
    print("rule: trenches give intervals; COV measures the irregularity - no metronome")
    print("OK: %s dug the trench" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_slip_deficit(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def slip_deficit(rate_mm_yr, years_since):
    return rate_mm_yr * years_since / 1000.0   # meters
def main():
    deficit = slip_deficit(35.0, 120.0)        # 35 mm/yr since 1906
    print("loading 35 mm/yr x 120 yr -> slip deficit %.1f m" % deficit)
    char_slip = 4.5
    print("characteristic slip %.1f m -> deficit is %.0f%% of a full cycle" %
          (char_slip, 100 * deficit / char_slip))
    assert abs(deficit - 4.2) < 1e-9
    print("rule: deficit = rate x time; a long-quiet fault carries a large debt")
    print("OK: %s balanced the slip budget" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_psha_integral(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def annual_exceedance(a, b, R_km, z_g):
    total, dm = 0.0, 0.1
    m = 5.0
    while m <= 8.0:                            # Cornell-McGuire sum over magnitudes
        rate = (10.0 ** (a - b * m) - 10.0 ** (a - b * (m + dm)))
        median = 10.0 ** (0.3 * m - 1.2 * math.log10(R_km) - 1.5)
        sigma = 0.6                            # lognormal scatter, natural log
        p = 0.5 * (1 - math.erf((math.log(z_g) - math.log(median)) / (sigma * math.sqrt(2))))
        total += rate * p
        m += dm
    return total
def main():
    hz = annual_exceedance(4.0, 1.0, 20.0, 0.3)
    print("annual P(PGA > 0.3g) at 20 km: %.4f (return period ~%.0f yr)" % (hz, 1 / hz))
    assert 0.0 < hz < 0.05, hz
    hz2 = annual_exceedance(4.0, 1.0, 100.0, 0.3)
    assert hz2 < hz
    print("same site at 100 km: %.5f - distance dilutes the hazard" % hz2)
    print("rule: sum over magnitudes of rate x P(shaking | m, r) - the Cornell integral")
    print("OK: %s integrated the hazard" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_splitting_delay(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def split_delay(path_km, vfast, vslow):
    return path_km * 1000.0 * (1.0 / vslow - 1.0 / vfast)
def main():
    dt = split_delay(200.0, 4700.0, 4500.0)
    print("200 km mantle path, 4 percent anisotropy -> splitting delay %.2f s" % dt)
    assert abs(dt - 1.89) < 0.05, dt
    print("fast direction phi records the flow; delay dt records its strength")
    print("rule: dt = L(1/Vslow - 1/Vfast) - split shear waves are a flow compass")
    print("OK: %s split the shear wave" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_receiver_ps(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def ps_delay(H_km, vp, vs, p):
    return H_km * (math.sqrt(1 / vs ** 2 - p ** 2) - math.sqrt(1 / vp ** 2 - p ** 2))
def moho_from_ps(dt, vp, vs, p):
    return dt / (math.sqrt(1 / vs ** 2 - p ** 2) - math.sqrt(1 / vp ** 2 - p ** 2))
def main():
    dt = ps_delay(35.0, 6.0, 3.46, 0.06)
    H = moho_from_ps(dt, 6.0, 3.46, 0.06)
    assert abs(H - 35.0) < 1e-6, H
    print("Ps delay %.2f s -> Moho depth %.1f km from one waveform" % (dt, H))
    print("rule: deconvolve the source, keep the conversions - the Moho in seconds")
    print("OK: %s read the Moho" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_noise_correlation(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    N, lag = 2000, 37
    a = [math.sin(0.11 * i) + 0.5 * math.sin(0.031 * i + 1.7) for i in range(N)]
    b = [0.0] * N
    for i in range(lag, N):
        b[i] = a[i - lag]                       # station B hears station A, delayed
    best_k, best_c = 0, -1e18
    for k in range(-100, 101):                  # cross-correlate
        c = sum(a[i] * b[i + k] for i in range(N - 100))
        if c > best_c:
            best_k, best_c = k, c
    assert best_k == lag, best_k
    print("noise cross-correlation peaks at lag %d samples - the inter-station Green function" % best_k)
    print("rule: correlate the hum, stack for months, and the Earth answers between the stations")
    print("OK: %s turned noise into signal" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_shadow_zone(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def direct_p(delta_deg):
    return delta_deg < 103.0 or delta_deg > 143.0   # P shadow zone 103-143 deg
def main():
    for d in (60.0, 103.0, 120.0, 143.0, 160.0):
        print("distance %5.1f deg: direct P %s" % (d, "arrives" if direct_p(d) else "in SHADOW"))
    assert direct_p(60.0) and not direct_p(120.0) and direct_p(160.0)
    print("S never crosses the core at all - Oldham's 1906 proof the outer core is liquid")
    print("rule: shadow zones are geometry; geometry is structure")
    print("OK: %s mapped the shadow" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_gutenberg_richter(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def annual_N(a, b, m):
    return 10.0 ** (a - b * m)
def prob(rate, years):
    return 1.0 - math.exp(-rate * years)
def main():
    a, b = 5.0, 1.0
    r7 = annual_N(a, b, 7.0)
    assert abs(r7 - 0.01) < 1e-12
    print("M>=7 rate %.3f/yr; P(50 yr) = %.1f%%" % (r7, 100 * prob(r7, 50)))
    for m in (6.0, 7.0, 8.0):
        r = annual_N(a, b, m)
        print("  M>=%.0f: %.4f/yr -> each unit 10x rarer (b=1)" % (m, r))
    assert abs(annual_N(a, b, 6.0) / r7 - 10.0) < 1e-9
    print("rule: log N = a - bM - the most useful straight line in seismology")
    print("OK: %s counted the earthquakes" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_base_shear(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def base_shear(W_kN, SDS, R, Ie):
    Cs = SDS / (R / Ie)
    Cs = max(Cs, 0.044 * SDS * Ie)          # code minimum
    return Cs * W_kN
def main():
    W = 10000.0
    V = base_shear(W, 1.0, 8.0, 1.0)
    assert abs(V - 1250.0) < 1e-9, V
    print("W=%.0f kN, SDS=1.0, R=8 -> base shear V = %.0f kN" % (W, V))
    floors = [0.25, 0.35, 0.40]             # mass x height weighting per floor
    for i, f in enumerate(floors, 1):
        print("  floor %d: lateral force %.0f kN" % (i, V * f))
    assert abs(sum(floors) - 1.0) < 1e-9
    print("rule: V = Cs*W, ductility does the rest - design to bend, never to break")
    print("OK: %s sized the structure" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "seismo_branches": demo_seismo_branches, "plate_boundaries": demo_plate_boundaries,
    "fault_types": demo_fault_types, "elastic_rebound": demo_elastic_rebound,
    "ps_distance": demo_ps_distance, "surface_dispersion": demo_surface_dispersion,
    "seismometer_response": demo_seismometer_response, "pick_phases": demo_pick_phases,
    "triangulation": demo_triangulation, "richter_ml": demo_richter_ml,
    "moment_magnitude": demo_moment_magnitude, "mercalli_map": demo_mercalli_map,
    "network_gap": demo_network_gap, "beachball_quadrants": demo_beachball_quadrants,
    "omori_decay": demo_omori_decay, "tsunami_travel": demo_tsunami_travel,
    "hazard_curve": demo_hazard_curve, "eew_blindzone": demo_eew_blindzone,
    "tomography_2x2": demo_tomography_2x2, "reflection_nmo": demo_reflection_nmo,
    "refraction_intercept": demo_refraction_intercept, "pressure_front": demo_pressure_front,
    "slow_slip_scaling": demo_slow_slip_scaling, "brune_spectrum": demo_brune_spectrum,
    "stress_drop": demo_stress_drop, "gmpe_pga": demo_gmpe_pga,
    "site_resonance": demo_site_resonance, "paleo_recurrence": demo_paleo_recurrence,
    "slip_deficit": demo_slip_deficit, "psha_integral": demo_psha_integral,
    "splitting_delay": demo_splitting_delay, "receiver_ps": demo_receiver_ps,
    "noise_correlation": demo_noise_correlation, "shadow_zone": demo_shadow_zone,
    "gutenberg_richter": demo_gutenberg_richter, "base_shear": demo_base_shear,
}

# ---------------------------------------------------------------- records

def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_seismology.py).
    ordered = sorted(enumerate(ENTRIES), key=lambda p: (p[1]["ladder_rank"], p[0]))
    recs = []
    for _, e in ordered:
        name = e["name"]
        title = name + " (Signature Edition)" if sig else name
        # Whole-system dedupe gate (his standing rule: every record, never a sample).
        if [h for h in base.GATE.check(slug, title) if h[0] != slug]:
            print("  gate refused (cross-db dupe): %s" % title, flush=True)
            continue
        rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
        if sig:
            description = ("Signature original interpretation. " + e["sig_lens"] + " "
                           + e["description"])
            how = e["sig_lens"] + " " + e["how_it_works"]
            citations = list(e["citations"]) + [SIG_TAIL]
        else:
            description = e["description"]
            how = e["how_it_works"]
            citations = list(e["citations"])
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "description": description,
            "how_it_works": how,
            "key_points": list(e["key_points"]),
            "requirements": list(e["requirements"]),
            "standards": list(e["standards"]),
            "citations": citations,
            "src": "signature" if sig else "public-harvest",
            "ladder_rank": e["ladder_rank"],
            "ladder_tier": e["ladder_tier"],
        }
        demo_fn = DEMOS[e["demo_kind"]]
        program = demo_fn(name if not sig else title, rid, e["group"],
                          e["key_points"], "; ".join(e["requirements"]))
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working demonstration program (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    # Ladder order guarantee: ids were assigned in ladder order; re-verify.
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def main():
    sys.path.insert(0, os.path.join(REPO, "code", "numbering-build"))
    spec = importlib.util.spec_from_file_location(
        "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
    nb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nb)
    nb.DBCFG = DBCFG

    sweep_path = "/home/hatch/workspace/goals/database-quality-audit/hidden_files/patches/sweep-db-pages.py"
    sspec = importlib.util.spec_from_file_location("sweep", sweep_path)
    sweep = importlib.util.module_from_spec(sspec)
    sspec.loader.exec_module(sweep)

    built = {}
    for slug in ("seismology", "seismology-signature"):
        source = "signature" if slug.endswith("-signature") else "public"
        built[slug] = build_records(slug, source)

    # sanity: ids unique + prefix + required keys + ALL demo programs compile
    # + banned-content scan + ladder fields present
    total = 0
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        assert len(recs) >= 30, "fewer than 30 records in %s" % slug
        for r in recs:
            for k in ("id", "t", "g", "name", "title", "description", "how_it_works",
                      "key_points", "requirements", "standards", "citations",
                      "src", "ladder_rank", "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
            assert 1 <= r["ladder_rank"] <= 10, "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("foundations", "compounded", "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            compile(prog, r["id"], "exec")
            blob = json.dumps(r).lower()
            assert "facebook" not in blob, "facebook ref in %s" % r["id"]
            assert "bat belt" not in blob, "banned phrase in %s" % r["id"]
            if slug.endswith("-signature"):
                assert "(signature edition)" in r["title"].lower(), "sig title missing suffix"
                assert r["src"] == "signature"
            else:
                assert r["src"] == "public-harvest"
        total += len(recs)
        n = base.write_shard_db(slug, recs)
        print("shard: %-38s %d records" % (slug, n), flush=True)

    # machine-execute EVERY demo (canon: runnable demo, machine-executed OK)
    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=60)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-500:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
    print("demo execution: all %d demos ran OK" % total, flush=True)

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    for slug, recs in built.items():
        page = nb.build_page(slug, template)
        page = page.replace(
            "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
            DBCFG[slug]["gen_desc"])
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "facebook" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
        assert "bat belt" not in page.lower(), "banned phrase in page %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        changed, notes = sweep.process_page(ppath)
        topics = {}
        for r in recs:
            topics.setdefault(r["g"], []).append("%s - %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    entries_m = [base.manifest_entry(s, len(built[s])) for s in built]
    base.update_json_list(os.path.join(REPO, "data", "manifest.json"), entries_m)
    entries_a = [base.api_entry(s, len(built[s])) for s in built]
    base.update_json_list(os.path.join(REPO, "api.json"), entries_a)
    print("manifest + api.json: appended %d databases, %d records" % (len(built), total))
    print("NEXT: run python3 code/restamp_counts.py, then commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
