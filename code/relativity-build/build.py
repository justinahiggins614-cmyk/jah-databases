#!/usr/bin/env python3
"""Build the Relativity field databases for JAH Databases (field #1, taxonomy order).

Verified 2026-10-17: the manifest's `everything-physics` database holds only 12
records with a single relativity keyword hit — thin, not substantial coverage.
So this build creates two NEW databases rather than extending it:

  relativity            — The Relativity Database (public-harvest: real, fact-checked
                         relativity physics, special + general)
  relativity-signature  — The Relativity Signature Database (his original Signature
                         interpretation; src signature, titles suffixed
                         " (Signature Edition)", never presented as authentic
                         public record)

32 records each, ordered by the teaching ladder (ladder_rank 1-10, ladder_tier
foundations/compounded/advanced); the shard index is written in ladder order so
pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements + standards
+ citations + working demonstration code (real, runnable, stdlib-only Python;
machine-executed OK).

Never the words "bat belt" anywhere. No website references. No Facebook.
"""
import importlib.util
import json
import os
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
from entries_relativity import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals — his original Signature interpretation of relativity: "
                "clearly labeled Signature-made, never presented as authentic public record.")
    pub_line = ("Public records — real, fact-checked relativity physics: special relativity, "
                "general relativity, and their experimental tests, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (reference frames, "
              "postulates, time dilation) -> Compounded (Lorentz transforms, mass-energy, "
              "spacetime intervals, equivalence) -> Advanced (field equations, black holes, "
              "gravitational waves, cosmology).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s — %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search relativity concepts, effects, experiments...",
        "chat_ph": "Ask about relativity...",
        "archive_blurb": ("Seeded %s relativity records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations · Compounded · Advanced — each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled structural relativity studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about relativity — from the two postulates up to black holes and gravitational waves." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "relativity-study", "gen_demo_kind": "relativity-demo",
        "source": source,
    }

CIT_PUB = "Relativity physics (peer-reviewed literature and standard textbooks)."
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["relativity"] = _cfg(
    "relativity", "The Relativity Database",
    "Real, fact-checked relativity: special relativity (time dilation, length contraction, "
    "Lorentz transforms, mass-energy equivalence) and general relativity (spacetime curvature, "
    "field equations, black holes, gravitational waves, cosmology).",
    "relativity record", "JAH-REL-", "JAH Relativity Archivist",
    "relativity archivist — special and general relativity, teaching progressively along the "
    "ladder from foundations (reference frames, postulates, time dilation) through compounded "
    "(Lorentz transforms, mass-energy, spacetime intervals, equivalence) to advanced (field "
    "equations, black holes, gravitational waves, cosmology); answers from many angles — "
    "definition, example, analogy, application, history, math, how-to — using only the "
    "system's own archive data",
    CIT_PUB, "public")
DBCFG["relativity-signature"] = _cfg(
    "relativity-signature", "The Relativity Signature Database",
    "His original Signature interpretation of relativity: the full ladder from reference "
    "frames to cosmology, reframed as Signature engineering. Clearly labeled Signature-made, "
    "never presented as authentic public record.",
    "relativity record", "JAH-REG-", "JAH Relativity Archivist (Signature)",
    "relativity archivist — Signature editions: his original Signature interpretation of "
    "relativity, clearly labeled Signature-made and never presented as authentic public "
    "record; teaches progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles — definition, example, analogy, application, history, "
    "math, how-to — using only the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# relativistic calculation for its record. All are machine-executed by main().

C_SNIPPET = "C = 299792458.0  # m/s, exact by SI definition\n"

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + C_SNIPPET + body.replace("NAME", json.dumps(name)))

def demo_galilean(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
import math
def main():
    v_train = 30.0  # m/s
    v_ball = 10.0   # m/s, thrown forward on the train
    v_ground = v_train + v_ball  # Galilean velocity addition
    print("ball speed: train frame %.1f m/s, ground frame %.1f m/s" % (v_ball, v_ground))
    beta = v_ground / C
    gamma = 1.0 / math.sqrt(1 - beta * beta)
    print("relativistic correction at %.0f m/s: gamma - 1 = %.3e" % (v_ground, gamma - 1))
    assert abs(v_ground - 40.0) < 1e-9
    assert gamma - 1 < 1e-12, "relativity must be negligible at everyday speeds"
    print("OK: %s combined everyday speeds; relativistic correction is negligible" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_lightclock(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
import math
def main():
    L = 1.0          # mirror separation, meters
    v = 0.6 * C
    T0 = 2 * L / C   # rest tick period
    gamma = 1.0 / math.sqrt(1 - (v / C) ** 2)
    T = gamma * T0   # moving tick period, seen from the ground
    print("rest tick period:      %.4e s" % T0)
    print("moving tick period:    %.4e s (gamma = %.4f)" % (T, gamma))
    print("ticks per ground second: rest %.3e, moving %.3e" % (1 / T0, 1 / T))
    assert abs(gamma - 1.25) < 1e-9
    assert T > T0, "moving clock must tick slower"
    print("OK: %s showed the moving light clock ticking slower by gamma" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_timedil(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
import math
def main():
    tau = 2.197e-6      # muon proper lifetime, s
    v = 0.998 * C
    gamma = 1.0 / math.sqrt(1 - (v / C) ** 2)
    t_lab = gamma * tau            # lifetime seen from Earth
    dist = v * t_lab / 1000.0      # km the muon travels
    dist_newton = v * tau / 1000.0 # km without relativity
    print("muon gamma at 0.998c: %.2f" % gamma)
    print("lab-frame lifetime: %.2e s (proper %.2e s)" % (t_lab, tau))
    print("travel distance: %.2f km with relativity, %.2f km without" % (dist, dist_newton))
    assert 10.0 < dist < 11.0, "muons must reach the ground (~10 km)"
    assert dist_newton < 1.0, "Newtonian muons would decay in under a kilometer"
    print("OK: %s showed time dilation letting muons reach the ground" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_gamma(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
import math
def gamma_of(beta):
    return 1.0 / math.sqrt(1 - beta * beta)
def main():
    print(" beta (v/c)      gamma")
    for beta in (0.0, 0.1, 0.5, 0.9, 0.99, 0.999):
        print("  %-12.3f  %10.4f" % (beta, gamma_of(beta)))
    assert abs(gamma_of(0.0) - 1.0) < 1e-12
    assert abs(gamma_of(0.99) - 7.0888) < 0.001
    assert gamma_of(0.999) > 20.0
    print("OK: %s tabulated the Lorentz factor from rest to 0.999c" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_lencontract(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
import math
def main():
    L0 = 100.0   # proper length, meters
    v = 0.8 * C
    gamma = 1.0 / math.sqrt(1 - (v / C) ** 2)
    L = L0 / gamma
    print("proper length: %.1f m" % L0)
    print("length at 0.8c: %.4f m (gamma = %.4f)" % (L, gamma))
    assert abs(L - 60.0) < 1e-9
    print("OK: %s contracted the moving rod to %.1f m" % (NAME, L))
if __name__ == "__main__":
    main()
''')

def demo_simultaneity(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
import math
def main():
    L = 100.0    # train length, meters
    v = 0.8 * C
    gamma = 1.0 / math.sqrt(1 - (v / C) ** 2)
    # events simultaneous in the embankment frame, separated by L along motion:
    dt_train = gamma * v * L / C ** 2
    print("embankment frame: strikes simultaneous, %.0f m apart" % L)
    print("train frame: front strike leads by %.3e s (%.1f ns)" % (dt_train, dt_train * 1e9))
    assert 4.4e-7 < dt_train < 4.5e-7
    print("OK: %s showed simultaneity is relative" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_lorentz(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
import math
def main():
    x, t = 100.0, 1e-6     # event in the ground frame
    v = 0.6 * C
    gamma = 1.0 / math.sqrt(1 - (v / C) ** 2)
    xp = gamma * (x - v * t)
    tp = gamma * (t - v * x / C ** 2)
    print("ground frame: x = %.2f m, t = %.3e s" % (x, t))
    print("moving frame: x' = %.2f m, t' = %.3e s" % (xp, tp))
    # inverse transform must round-trip exactly
    x2 = gamma * (xp + v * tp)
    t2 = gamma * (tp + v * xp / C ** 2)
    assert abs(x2 - x) < 1e-6 and abs(t2 - t) < 1e-12, "inverse transform failed"
    print("inverse transform returns x = %.6f m, t = %.6e s" % (x2, t2))
    print("OK: %s transformed an event and round-tripped it" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_veladd(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def add(u_prime, v):
    return (u_prime + v) / (1 + u_prime * v)   # speeds as fractions of c
def main():
    u1 = add(0.5, 0.5)
    u2 = add(0.9, 0.9)
    u3 = add(1.0, 0.9)   # photon from a moving source
    print("0.5c + 0.5c = %.4fc" % u1)
    print("0.9c + 0.9c = %.6fc" % u2)
    print("c + 0.9c    = %.4fc" % u3)
    assert abs(u1 - 0.8) < 1e-9
    assert u2 < 1.0, "must stay subluminal"
    assert abs(u3 - 1.0) < 1e-12, "light speed must be invariant"
    print("OK: %s combined relativistic speeds without reaching c" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_emc2(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    E_1kg = 1.0 * C ** 2
    megatons = E_1kg / 4.184e15
    m_e = 9.1093837e-31
    eV = m_e * C ** 2 / 1.602176634e-19
    L_sun = 3.828e26                    # watts
    dm_dt = L_sun / C ** 2              # kg/s converted to energy
    print("1 kg  -> %.4e J = %.2f megatons of TNT" % (E_1kg, megatons))
    print("electron rest energy: %.1f keV" % (eV / 1000.0))
    print("Sun converts %.3e kg of mass to energy per second" % dm_dt)
    assert 21.0 < megatons < 22.0
    assert abs(eV / 1000.0 - 511.0) < 1.0
    assert 4.2e9 < dm_dt < 4.3e9
    print("OK: %s balanced the mass-energy books" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_relmom(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
import math
def main():
    m, v = 1.0, 0.9 * C
    gamma = 1.0 / math.sqrt(1 - (v / C) ** 2)
    p = gamma * m * v
    E = gamma * m * C ** 2
    lhs = E ** 2
    rhs = (p * C) ** 2 + (m * C ** 2) ** 2
    print("p = %.4e kg m/s (Newton would say %.4e)" % (p, m * v))
    print("E = %.4e J" % E)
    print("E^2 - (pc)^2 = %.4e  vs  (mc^2)^2 = %.4e" % (lhs - (p * C) ** 2, (m * C ** 2) ** 2))
    assert abs(lhs - rhs) / lhs < 1e-9, "energy-momentum invariant violated"
    print("OK: %s verified the energy-momentum invariant" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_interval(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
import math
def s2(t, x):
    return -(C * t) ** 2 + x ** 2
def main():
    t, x = 5e-6, 1200.0          # events A=(0,0), B in the ground frame
    v = 0.5 * C
    gamma = 1.0 / math.sqrt(1 - (v / C) ** 2)
    tp = gamma * (t - v * x / C ** 2)
    xp = gamma * (x - v * t)
    a, b = s2(t, x), s2(tp, xp)
    print("ground frame: s^2 = %.3e m^2" % a)
    print("moving frame: s^2 = %.3e m^2" % b)
    print("classification: %s (causal contact possible)" % ("timelike" if a < 0 else "other"))
    assert a < 0, "these events must be timelike separated"
    assert abs(a - b) / abs(a) < 1e-6, "interval must be invariant"
    print("OK: %s showed the spacetime interval is frame-independent" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_twin(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
import math
def main():
    v = 0.8 * C
    D_ly = 4.0                       # light-years each way
    gamma = 1.0 / math.sqrt(1 - (v / C) ** 2)
    t_earth = 2 * D_ly / 0.8         # years, Earth frame
    t_traveler = t_earth / gamma     # years, traveler proper time
    print("Earth waits:    %.1f years" % t_earth)
    print("Traveler ages:  %.1f years" % t_traveler)
    assert abs(t_earth - 10.0) < 1e-9
    assert abs(t_traveler - 6.0) < 1e-9
    assert t_traveler < t_earth
    print("OK: %s resolved the twin paradox: bent worldline ages less" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_doppler(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
import math
def main():
    beta = 0.5                       # receding at half light speed
    ratio = math.sqrt((1 + beta) / (1 - beta))
    z = ratio - 1
    lam_emit = 656.28e-9             # H-alpha, meters
    lam_obs = lam_emit * ratio
    print("wavelength ratio (observed/emitted): %.5f" % ratio)
    print("redshift z = %.5f" % z)
    print("H-alpha 656.3 nm -> %.1f nm" % (lam_obs * 1e9))
    assert 0.73 < z < 0.74
    print("OK: %s computed the relativistic redshift" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_propertime(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
import math
def main():
    # events A=(0,0), B=(10 yr, 0): inertial twin vs traveling twin (0.8c out and back)
    t_inertial = 10.0
    gamma = 1.0 / math.sqrt(1 - 0.8 ** 2)
    t_leg = 5.0
    t_traveler = 2 * t_leg / gamma
    print("inertial worldline proper time:  %.1f yr" % t_inertial)
    print("accelerated worldline proper time: %.1f yr" % t_traveler)
    assert abs(t_traveler - 6.0) < 1e-9
    assert t_traveler < t_inertial, "straight worldline must maximize proper time"
    print("OK: %s showed straight worldlines age the most" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_michelson(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    L = 11.0            # effective arm length, meters
    lam = 500e-9        # light wavelength, meters
    v = 30000.0         # Earth's orbital speed, m/s
    expected = 2 * L / lam * (v / C) ** 2   # classical ether prediction
    observed = 0.0                        # what Michelson and Morley found
    print("classical ether prediction: %.2f fringe shift" % expected)
    print("observed shift: < 0.01 fringes (consistent with zero)")
    assert 0.43 < expected < 0.45
    print("OK: %s reproduced the null result that killed the ether" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_equiv(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
import math
def main():
    h, g = 10.0, 9.80665
    t = math.sqrt(2 * h / g)   # fall time: mass cancels out
    print("1 kg mass falls %.3f s" % t)
    print("1000 kg mass falls %.3f s" % t)
    assert abs(t - 1.428) < 0.001
    print("OK: %s showed all masses fall together" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_curvature(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
import math
def main():
    # octant triangle on a unit sphere: three right angles
    angles = [math.pi / 2, math.pi / 2, math.pi / 2]
    total = sum(angles)
    excess = total - math.pi
    R = 1.0
    area = 4 * math.pi * R ** 2 / 8.0
    print("angle sum: %.1f deg (Euclid says 180)" % math.degrees(total))
    print("spherical excess: %.4f rad; area/R^2 = %.4f" % (excess, area / R ** 2))
    assert abs(excess - area / R ** 2) < 1e-12, "Girard's theorem failed"
    print("OK: %s measured curvature as excess angle" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_perihelion(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
import math
G = 6.67430e-11
M_SUN = 1.98847e30
def main():
    a, e = 5.7909e10, 0.2056          # Mercury: semi-major axis (m), eccentricity
    dphi = 6 * math.pi * G * M_SUN / (a * (1 - e ** 2) * C ** 2)  # rad per orbit
    orbits_per_century = 36525.0 / 87.9691
    arcsec = dphi * orbits_per_century * 206265.0
    print("GR perihelion shift: %.2f arcseconds per century" % arcsec)
    assert 42.0 < arcsec < 44.0, "must match the famous 43 arcseconds"
    print("OK: %s reproduced Mercury's 43 arcseconds per century" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_grtimedil(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
import math
G = 6.67430e-11
M_EARTH = 5.97237e24
def main():
    rs = 2 * G * M_EARTH / C ** 2
    r_earth, r_gps = 6371000.0, 26571000.0
    gr = rs / 2 * (1 / r_earth - 1 / r_gps) * 86400.0 * 1e6   # us/day fast
    v = 3874.0
    sr = (v ** 2 / (2 * C ** 2)) * 86400.0 * 1e6               # us/day slow
    net = gr - sr
    km = net * 1e-6 * C / 1000.0
    print("Schwarzschild radius of Earth: %.2f mm" % (rs * 1000))
    print("GPS clock: GR +%0.1f us/day, SR -%.1f us/day, net %+.1f us/day" % (gr, sr, net))
    print("uncorrected position drift: %.1f km/day" % km)
    assert 38.0 < net < 39.5
    assert 11.0 < km < 12.0
    print("OK: %s combined both relativistic GPS corrections" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_geodesic(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
import math
def haversine_km(lat1, lon1, lat2, lon2):
    R = 6371.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * R * math.asin(math.sqrt(a))
def main():
    nyc = (40.7128, -74.0060)
    lon = (51.5074, -0.1278)
    gc = haversine_km(*nyc, *lon)          # great-circle: the geodesic
    dlat = math.radians(lon[0] - nyc[0])
    dlon = math.radians(lon[1] - nyc[1])
    latm = math.radians((nyc[0] + lon[0]) / 2)
    flat = 6371.0 * math.hypot(dlat, dlon * math.cos(latm))  # flat-map straight line
    print("great-circle (geodesic): %.0f km" % gc)
    print("flat-map straight line:  %.0f km" % flat)
    assert 5500 < gc < 5650
    assert gc < flat, "geodesic must be the shortest surface path"
    print("OK: %s showed the geodesic beats the flat-map line" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_schwarz(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
G = 6.67430e-11
M_SUN = 1.98847e30
AU = 1.496e11
def rs(m):
    return 2 * G * m / C ** 2
def main():
    r_sun = rs(M_SUN)
    r_earth = rs(5.97237e24)
    r_10 = rs(10 * M_SUN)
    r_sgra = rs(4.297e6 * M_SUN)
    print("Schwarzschild radii: Sun %.2f km | Earth %.2f mm | 10 suns %.1f km" % (
        r_sun / 1000, r_earth * 1000, r_10 / 1000))
    print("Sagittarius A* (4.3M suns): %.3e m = %.3f AU" % (r_sgra, r_sgra / AU))
    assert abs(r_sun / 1000 - 2.953) < 0.01
    assert abs(r_earth * 1000 - 8.87) < 0.05
    print("OK: %s sized black holes from Earth to Sagittarius A*" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_gw(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
G = 6.67430e-11
M_SUN = 1.98847e30
MPC = 3.085677581e22
def main():
    # order-of-magnitude strain for a GW150914-like merger: h ~ (G/c^4)(M v^2/r)
    M = 60 * M_SUN
    v = 0.5 * C
    r = 410 * MPC
    h = (G / C ** 4) * (M * v ** 2) / r
    print("estimated strain h ~ %.2e" % h)
    print("over 4 km of arm: %.2e m (far below a proton width)" % (h * 4000))
    assert 1e-22 < h < 1e-20, "must be order 10^-21 like GW150914"
    print("OK: %s estimated a LIGO-scale gravitational-wave strain" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hubble(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    H0 = 70.0               # km/s per Mpc
    c_kms = C / 1000.0
    for z in (0.01, 0.1):
        v = z * c_kms       # recession speed, km/s (low-z approximation)
        d = v / H0           # Mpc
        print("z = %.2f -> v = %7.0f km/s -> d = %6.1f Mpc" % (z, v, d))
    assert abs((0.1 * c_kms) / H0 - 428.3) < 1.0
    print("OK: %s applied Hubble's law" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_framedrag(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
import math
G = 6.67430e-11
M_EARTH = 5.97237e24
R_EARTH = 6371000.0
MAS_PER_RAD = 206264806.0
YR = 31557600.0
def main():
    a = 7027400.0                        # Gravity Probe B orbit radius, m
    I = 0.3307 * M_EARTH * R_EARTH ** 2  # Earth's moment of inertia
    J = I * 7.2921159e-5                 # Earth's angular momentum
    # geodetic precession: (3/2)(GM/c^2 a) n
    n = math.sqrt(G * M_EARTH / a ** 3)
    geo = 1.5 * (G * M_EARTH / (C ** 2 * a)) * n * YR * MAS_PER_RAD
    # Lense-Thirring nodal rate: 2 G J / (c^2 a^3)
    lt = 2 * G * J / (C ** 2 * a ** 3) * YR * MAS_PER_RAD
    print("geodetic precession:   %7.0f mas/yr (GP-B measured 6601.8, predicted 6606.1)" % geo)
    print("Lense-Thirring nodal:  %7.1f mas/yr" % lt)
    print("GP-B frame-dragging drift: predicted 39.2, measured 37.2 +/- 7.2 mas/yr")
    assert 6590 < geo < 6620, "geodetic precession must match Gravity Probe B"
    assert lt > 100, "frame dragging must be non-negligible at this precision"
    print("OK: %s computed both relativistic precessions" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_lensing(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
import math
G = 6.67430e-11
M_SUN = 1.98847e30
R_SUN = 6.957e8
MPC = 3.085677581e22
def main():
    alpha = 4 * G * M_SUN / (C ** 2 * R_SUN)   # radians, at the solar limb
    arcsec = alpha * 206265.0
    print("solar limb deflection: %.4f arcseconds" % arcsec)
    # Einstein ring: 10^12 solar-mass lens, 1 Gpc away, source at 2 Gpc
    M = 1e12 * M_SUN
    Dl, Ds, Dls = 1 * MPC * 1000, 2 * MPC * 1000, 1 * MPC * 1000
    theta_E = math.sqrt(4 * G * M / C ** 2 * Dls / (Dl * Ds))
    print("galaxy-lens Einstein ring radius: %.2f arcseconds" % (theta_E * 206265.0))
    assert 1.74 < arcsec < 1.76, "must match the famous 1.75 arcseconds"
    print("OK: %s bent starlight by the book value" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_lambda(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
import math
G = 6.67430e-11
def main():
    H0 = 70e3 / 3.085677581e22          # 70 km/s/Mpc in 1/s
    rho_c = 3 * H0 ** 2 / (8 * math.pi * G)   # critical density, kg/m^3
    rho_L = 0.69 * rho_c                       # dark energy density
    Lambda = 8 * math.pi * G * rho_L / C ** 2  # cosmological constant, 1/m^2
    print("critical density:      %.3e kg/m^3" % rho_c)
    print("dark energy density:   %.3e kg/m^3" % rho_L)
    print("cosmological constant: %.3e m^-2" % Lambda)
    assert 1.1e-52 < Lambda < 1.3e-52
    print("OK: %s measured the weight of empty space" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_deflection(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
G = 6.67430e-11
M_SUN = 1.98847e30
R_SUN = 6.957e8
def main():
    for b_radii, label in ((1.0, "solar limb"), (2.0, "two solar radii")):
        b = b_radii * R_SUN
        alpha = 4 * G * M_SUN / (C ** 2 * b)
        print("deflection at %s: %.4f arcseconds" % (label, alpha * 206265.0))
    limb = 4 * G * M_SUN / (C ** 2 * R_SUN) * 206265.0
    assert 1.74 < limb < 1.76
    print("OK: %s verified the light-bending test of GR" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_gps(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
import math
G = 6.67430e-11
M_EARTH = 5.97237e24
def main():
    rs = 2 * G * M_EARTH / C ** 2
    gr = rs / 2 * (1 / 6371000.0 - 1 / 26571000.0) * 86400.0 * 1e6
    sr = (3874.0 ** 2 / (2 * C ** 2)) * 86400.0 * 1e6
    net = gr - sr
    f0 = 10.23e6
    f_orbit = f0 * (1 - net * 1e-6 / 86400.0)
    err_km = net * 1e-6 * C / 1000.0
    print("relativistic offset: %+.2f us/day" % net)
    print("factory clock setting: %.11f MHz (launched slow, ticks right in orbit)" % (f_orbit / 1e6))
    print("position error if ignored: %.1f km/day" % err_km)
    assert 38.0 < net < 39.5
    assert abs(f_orbit / 1e6 - 10.22999999) < 1e-6
    print("OK: %s showed GPS runs on relativity" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "galilean": demo_galilean, "lightclock": demo_lightclock, "timedil": demo_timedil,
    "gamma": demo_gamma, "lencontract": demo_lencontract, "simultaneity": demo_simultaneity,
    "lorentz": demo_lorentz, "veladd": demo_veladd, "emc2": demo_emc2,
    "relmom": demo_relmom, "interval": demo_interval, "twin": demo_twin,
    "doppler": demo_doppler, "propertime": demo_propertime, "michelson": demo_michelson,
    "equiv": demo_equiv, "curvature": demo_curvature, "perihelion": demo_perihelion,
    "grtimedil": demo_grtimedil, "geodesic": demo_geodesic, "schwarz": demo_schwarz,
    "gw": demo_gw, "hubble": demo_hubble, "framedrag": demo_framedrag,
    "lensing": demo_lensing, "lambda": demo_lambda, "deflection": demo_deflection,
    "gps": demo_gps,
}

# ---------------------------------------------------------------- records

def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_relativity.py).
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
    for slug in ("relativity", "relativity-signature"):
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
        # Exhaustive pill + red All Database Merger button ride along in the template
        assert 'id="qex"' in page and 'id="qmerge"' in page, "merger pattern missing in %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        changed, notes = sweep.process_page(ppath)
        topics = {}
        for r in recs:
            topics.setdefault(r["g"], []).append("%s — %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ",".join(notes)), flush=True)

    entries_m = [base.manifest_entry(s, len(built[s])) for s in built]
    base.update_json_list(os.path.join(REPO, "data", "manifest.json"), entries_m)
    entries_a = [base.api_entry(s, len(built[s])) for s in built]
    base.update_json_list(os.path.join(REPO, "api.json"), entries_a)
    print("manifest + api.json: appended %d databases, %d records" % (len(built), total))
    print("NEXT: run python3 code/restamp_counts.py, then commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
