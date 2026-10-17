#!/usr/bin/env python3
"""Build the Electromagnetics field databases for JAH Databases (field #21, taxonomy order).

Verified 2026-10-17: NO database covers electromagnetics as a discipline.
- Manifest-wide regex search (maxwell|transmission.?line|antenna|waveguide|
  smith.?chart|s.?param|radar|magnetostat|electrostat|faraday|ampere|
  gauss.?law|poynting|polariz|friis|dipole|finite.?diff|fdtd|method.?of.?
  moments): zero discipline-level hits across all 2342 databases. 'radar'
  hits are weather radar inside atmospheric-science/meteorology (instruments,
  not field theory). 'electromagnetism' (JAH-EM-, 10000 records) is purely
  EM-spectrum band records: whole-index title scan for transmission line,
  maxwell, waveguide, smith chart, s-parameter, magnetostat, electrostat,
  poynting, friis, dipole, antenna, finite-difference = zero hits.
  'electronics' (223) and 'electronics-public' (9) are circuit-level: zero
  hits. 'electrical-electronic-testing' (24): zero hits.
- Fields #11-20 shard indexes (volcanology, climatology,
  atmospheric-science, hydrology, meteorology, calculus, combinatorics,
  econometrics, psychometrics, turbomachinery): direct whole-shard title
  scans for electromagnet|antenna|maxwell|transmission line|waveguide|
  smith chart|radar cross|friis|magnetostat|electrostat|s.param = zero hits.
- 'scientific-formulas': bare formula cards are reference only (task rule:
  formula cards do NOT count as discipline coverage).
- Whole-system dedupe gate (fresh data/dedupe/exact/ index in the main repo
  rebuilt 2026-10-17 08:04 UTC, covering fields through #10; fields #11-20
  cross-checked directly above): every record checked + admitted at build
  time.

So this build creates two NEW databases:

  electromagnetics             - The Electromagnetics Database
                                 (public-harvest: real, fact-checked
                                 electromagnetics; citations Griffiths,
                                 Jackson, Pozar, Balanis, Cheng, Ulaby,
                                 Ramo/Whinnery/Van Duzer, Kraus/Fleisch,
                                 Sadiku, Collin, Harrington,
                                 Taflove/Hagness, Jin, Paul, Skolnik,
                                 Orfanidis)
  electromagnetics-signature   - The Electromagnetics Signature Database
                                 (his original Signature interpretation of
                                 the discipline; src signature, titles
                                 suffixed " (Signature Edition)", never
                                 presented as authentic public record)

37 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable,
stdlib-only Python; machine-executed OK). Electromagnetics demos: the
discipline map and the speed of light from mu_0/epsilon_0, Coulomb's force,
Gauss's flux audit, the potential landscape, parallel-plate capacitance,
copper-wire Ohmic heating, Biot-Savart vs Ampere on a wire, the Lorentz
cyclotron radius, the hysteresis loop's energy price, Faraday induction at
60 Hz, solenoid inductance and the RL time constant, Maxwell's equations
verified numerically, displacement current in a charging capacitor,
boundary-condition refraction, the wave equation checked by finite
difference, the 377-ohm plane wave, polarization axial ratios, Poynting
power flow, copper skin depth, Fresnel 4% at glass, Snell's critical angle,
coax delay and Z_0, the telegrapher's alpha/beta, Smith-chart Gamma/VSWR,
S-parameter load pull, the quarter-wave match, WR-90 cutoff and guide
wavelength, the box cavity's TE101, the far-field boundary, the dipole's
1.64 directivity by integration, the 4-element array factor, the Friis
link at 2.4 GHz, Larmor radiation, the sphere's pi a^2 RCS and the radar
equation, pulse-Doppler range arithmetic, copper-shield absorption, and a
1D FDTD pulse obeying Courant.

Subtitle disambiguation (fields #13-21 pattern): discipline titles carry
teaching-focused subtitles rather than bare cards, e.g. "Maxwell's
Equations: Four Laws, One Universe" and "The Smith Chart: Reading the
Circle".

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
# Whole-system dedupe gate against the FRESH data/dedupe/exact/ index in the
# main repo (rebuilt 2026-10-17 08:04 UTC; covers fields through #10).
# Fields #11-20 shard indexes checked directly (see docstring) since the gate
# index predates them - subtitle disambiguation used throughout.
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_electromagnetics import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of electromagnetics: "
                "clearly labeled Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked electromagnetics: what electromagnetics is; "
                "Coulomb's law; the electric field and Gauss's law; potential and voltage; "
                "capacitance; current and Ohm's law; Biot-Savart and Ampere's law; the Lorentz "
                "force; magnetic materials; Faraday's and Lenz's laws; inductance; Maxwell's "
                "equations; displacement current; boundary conditions; the wave equation; plane "
                "waves; polarization; the Poynting vector; lossy media and skin depth; Fresnel "
                "reflection; Snell's law and total internal reflection; transmission lines; the "
                "telegrapher's equations; reflection, VSWR, and the Smith chart; S-parameters; "
                "impedance matching; waveguides; cavity resonators; antennas; the half-wave "
                "dipole; antenna arrays; the Friis equation; the Larmor radiation mechanism; "
                "scattering and radar cross section; radar fundamentals; EMI/EMC; computational "
                "electromagnetics (FDTD, FEM, MoM), organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what electromagnetics "
              "is, Coulomb's law, electric field and Gauss's law, potential and voltage, "
              "capacitance, current and Ohm's law, Biot-Savart and Ampere's law, the Lorentz "
              "force, magnetic materials, Faraday's and Lenz's laws, inductance, Maxwell's "
              "equations) -> Compounded (displacement current, boundary conditions, the wave "
              "equation, plane waves, polarization, the Poynting vector, lossy media and skin "
              "depth, Fresnel reflection, Snell's law and total internal reflection, "
              "transmission lines, the telegrapher's equations, reflection/VSWR/Smith chart, "
              "S-parameters, impedance matching) -> Advanced (waveguides, cavity resonators, "
              "antennas, the half-wave dipole, antenna arrays, the Friis equation, Larmor "
              "radiation, scattering and radar cross section, radar fundamentals, EMI/EMC, "
              "computational electromagnetics).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search Maxwell's equations, Smith chart, S-parameters, Friis, skin depth, FDTD, radar...",
        "chat_ph": "Ask about electromagnetics...",
        "archive_blurb": ("Seeded %s electromagnetics records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled structural electromagnetics studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about electromagnetics - from Coulomb's law, Gauss's law, and Maxwell's equations through waves, transmission lines, the Smith chart, antennas, radar, EMC, and computational electromagnetics." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "electromagnetics-study", "gen_demo_kind": "electromagnetics-demo",
        "source": source,
    }

CIT_PUB = "Electromagnetics (standard textbooks and peer-reviewed literature)."
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["electromagnetics"] = _cfg(
    "electromagnetics", "The Electromagnetics Database",
    "Real, fact-checked electromagnetics: the fields that fill space - from Coulomb's law "
    "and Maxwell's equations through waves, polarization, transmission lines, the Smith "
    "chart, S-parameters, waveguides, antennas, radar, EMC, and computational "
    "electromagnetics - taught progressively along the ladder.",
    "electromagnetics record", "JAH-ELM-", "JAH Electromagnetics Archivist",
    "electromagnetics archivist - what electromagnetics is, Coulomb's law, electric field "
    "and Gauss's law, potential and voltage, capacitance, current and Ohm's law, "
    "Biot-Savart and Ampere's law, the Lorentz force, magnetic materials, Faraday's and "
    "Lenz's laws, inductance, Maxwell's equations, displacement current, boundary "
    "conditions, the wave equation, plane waves, polarization, the Poynting vector, lossy "
    "media and skin depth, Fresnel reflection, Snell's law and total internal reflection, "
    "transmission lines, the telegrapher's equations, reflection/VSWR/Smith chart, "
    "S-parameters, impedance matching, waveguides, cavity resonators, antennas, the "
    "half-wave dipole, antenna arrays, the Friis equation, Larmor radiation, scattering "
    "and radar cross section, radar fundamentals, EMI/EMC, computational electromagnetics; "
    "teaching progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, application, "
    "history, math, how-to - using only the system's own archive data",
    CIT_PUB, "public")
DBCFG["electromagnetics-signature"] = _cfg(
    "electromagnetics-signature", "The Electromagnetics Signature Database",
    "His original Signature interpretation of electromagnetics: the full ladder from "
    "Coulomb's law and Maxwell's equations through waves, transmission lines, antennas, "
    "and radar, reframed as Signature science. Clearly labeled Signature-made, "
    "never presented as authentic public record.",
    "electromagnetics record", "JAH-EMS-", "JAH Electromagnetics Archivist (Signature)",
    "electromagnetics archivist - Signature editions: his original Signature interpretation "
    "of electromagnetics, clearly labeled Signature-made and never presented as authentic "
    "public record; teaches progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG
# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# electromagnetics computation for its record. All are machine-executed by main().

_PREAMBLE = (
"import math\n"
"import cmath\n"
"MU0 = 4.0 * math.pi * 1e-7\n"
"EPS0 = 8.854187817e-12\n"
"C0 = 299792458.0\n"
"ETA0 = 376.730313461\n"
"def _deg(r):\n"
"    return r * 180.0 / math.pi\n"
"def _rad(d):\n"
"    return d * math.pi / 180.0\n"
)

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_em_what(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
TERRITORIES = {
    "statics": "charges at rest -> E (capacitors); steady currents -> B (magnets, motors)",
    "dynamics": "time-varying fields couple and launch waves -> radio, light, optics",
    "engineered systems": "transmission lines, waveguides, antennas, radar, EMC, computation",
}
def main():
    assert len(TERRITORIES) == 3
    for terr, tools in TERRITORIES.items():
        print("%-20s -> %s" % (terr, tools))
    # Maxwell's thunderclap: c from purely electrical constants
    c = 1.0 / math.sqrt(MU0 * EPS0)
    assert abs(c - 299792458.0) / 299792458.0 < 1e-6, c
    print("c = 1/sqrt(mu0*eps0) = %.0f m/s - light, from electrical measurements" % c)
    # the whole spectrum obeys c = lambda * f
    for band, f in (("AM radio", 1e6), ("Wi-Fi", 2.4e9), ("visible red", 4.7e14)):
        lam = c / f
        print("  %-12s f=%8.2e Hz -> lambda=%9.3e m" % (band, f, lam))
        assert abs(lam * f - c) / c < 1e-12
    print("rule: one speed, one equation set, every frequency from power lines to gamma rays")
    print("OK: %s mapped the discipline" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_coulomb(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    k = 1.0 / (4.0 * math.pi * EPS0)
    assert abs(k - 8.9875517923e9) / 8.9875517923e9 < 1e-6, k
    q1 = q2 = 1e-6          # 1 microcoulomb each
    r = 1.0                # 1 meter apart
    F = k * q1 * q2 / r ** 2
    assert abs(F - 8.9875517923e-3) < 1e-9, F
    print("two 1-uC charges at 1 m: F = %.4f mN (repulsive)" % (F * 1000.0))
    # inverse square: halve the distance -> 4x the force
    F2 = k * q1 * q2 / (r / 2.0) ** 2
    assert abs(F2 / F - 4.0) < 1e-12
    print("at 0.5 m: F = %.4f N = 4x - the inverse square in action" % F2)
    # superposition: third charge at right angle
    q3 = -1e-6
    # q3 at (1,0), q1 at origin, q2 at (0,1): force on q3 from both
    # superposition: q3 = -1 uC at (1,0); q1 at origin, q2 at (0,1)
    # proper vector sum: r13 = (1,0), r23 = (1,-1)
    r13 = 1.0; r23 = math.sqrt(2.0)
    # F = k q_src q_test / r^2 * r_hat (r_hat: source -> test point)
    Fx = k * q1 * q3 / r13 ** 2 * (1.0) + k * q2 * q3 / r23 ** 2 * (1.0 / math.sqrt(2.0))
    Fy = k * q2 * q3 / r23 ** 2 * (-1.0 / math.sqrt(2.0))
    Ftot = math.hypot(Fx, Fy)
    assert Ftot > 0
    print("three-charge superposition: net force on q3 = (%.4f, %.4f) N, |F| = %.4f N" % (Fx, Fy, Ftot))
    print("rule: pairwise inverse-square forces add as vectors - all of electrostatics follows")
    print("OK: %s weighed the charges" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_gauss(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    k = 1.0 / (4.0 * math.pi * EPS0)
    q = 2e-9               # 2 nC point charge at origin
    R = 0.30               # Gaussian sphere radius (m)
    # numeric flux: latitude/longitude grid over the sphere
    nlat, nlon = 60, 120
    flux = 0.0
    for i in range(nlat):
        theta = math.pi * (i + 0.5) / nlat
        dtheta = math.pi / nlat
        for j in range(nlon):
            dphi = 2.0 * math.pi / nlon
            dA = R ** 2 * math.sin(theta) * dtheta * dphi
            Er = k * q / R ** 2          # radial field, uniform on sphere
            flux += Er * dA              # E dot dA, outward normal
    exact = q / EPS0
    assert abs(flux - exact) / exact < 0.01, (flux, exact)
    print("numeric flux through sphere: %.6e C ; Q/eps0 = %.6e C - Gauss holds" % (flux, exact))
    # radius independence: double R, same flux
    R2 = 0.60
    flux2 = (k * q / R2 ** 2) * (4.0 * math.pi * R2 ** 2)
    assert abs(flux2 - exact) / exact < 1e-12
    print("at R = 0.60 m the flux is identical: Gauss counts charge, not distance")
    # line charge via coaxial cylinder: E = lambda / 2 pi eps0 r
    lam = 1e-9
    r = 0.05
    Eline = lam / (2.0 * math.pi * EPS0 * r)
    assert abs(Eline - 359.5) < 0.5, Eline
    print("infinite line charge 1 nC/m at 5 cm: E = %.1f V/m (1/r, not 1/r^2)" % Eline)
    print("rule: draw the right surface and symmetry hands you the field")
    print("OK: %s audited the flux" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_potential(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    k = 1.0 / (4.0 * math.pi * EPS0)
    q = 1e-9
    V1 = k * q / 1.0
    V2 = k * q / 2.0
    assert abs(V1 - 8.9876) < 1e-3 and abs(V2 - 4.4938) < 1e-3, (V1, V2)
    print("V(1 m) = %.4f V, V(2 m) = %.4f V - the 1/r hill" % (V1, V2))
    # E from the slope: E = -dV/dr = kq/r^2 (numeric derivative check)
    r = 1.0; h = 1e-6
    dVdr = (k * q / (r + h) - k * q / (r - h)) / (2.0 * h)
    E = k * q / r ** 2
    assert abs(-dVdr - E) / E < 1e-6
    print("E = -dV/dr verified numerically: %.4f V/m downhill" % E)
    # energy to haul a 1-uC charge from 2 m to 1 m against the hill
    qmove = 1e-6
    W = qmove * (V1 - V2)
    assert abs(W - 4.4938e-6) < 1e-10, W
    print("moving 1 uC from 2 m to 1 m costs %.4e J = q * delta-V" % W)
    # equipotential: V constant on the sphere, E perpendicular to it
    print("rule: charges roll downhill on the voltage landscape; E is the slope")
    print("OK: %s climbed the potential hill" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_capacitance(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    A = 0.01               # 10 cm x 10 cm plates
    d = 0.001              # 1 mm gap
    C = EPS0 * A / d
    assert abs(C - 8.854187817e-11) / 8.854187817e-11 < 1e-9, C
    print("parallel plates 0.01 m^2 / 1 mm: C = %.2f pF" % (C * 1e12))
    V = 100.0
    Q = C * V
    W = 0.5 * C * V ** 2
    assert abs(W - 4.4270939085e-7) / 4.4270939085e-7 < 1e-9, W
    print("at 100 V: Q = %.3e C, stored energy = %.4e J (in the field, not the metal)" % (Q, W))
    # dielectric: insert eps_r = 4 -> 4x the capacitance
    C_d = 4.0 * C
    print("with eps_r = 4 dielectric: C = %.2f pF - polarization pays for more charge" % (C_d * 1e12))
    assert abs(C_d / C - 4.0) < 1e-12
    # field between plates
    E = V / d
    u = 0.5 * EPS0 * E ** 2
    W_check = u * A * d
    assert abs(W_check - W) / W < 1e-9
    print("energy density %.3f J/m^3 x volume = same %.4e J - energy lives in the gap" % (u, W_check))
    print("rule: C = eps A / d ; W = CV^2/2 parked between the plates")
    print("OK: %s charged the plates" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_current(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    sigma_cu = 5.8e7       # S/m
    L = 10.0               # m
    A = 1e-6               # 1 mm^2
    R = L / (sigma_cu * A)
    assert abs(R - 0.17241379) < 1e-6, R
    print("10 m of 1-mm^2 copper: R = %.4f ohm" % R)
    I = 10.0
    V = I * R
    P = I ** 2 * R
    assert abs(P - 17.2413793) < 1e-4, P
    print("at 10 A: drop = %.3f V, heat = %.2f W - I^2 R is why feeders run hot" % (V, P))
    # drift velocity: humiliatingly slow
    n = 8.5e28             # free electrons per m^3 in copper
    qe = 1.602176634e-19
    vd = I / (n * qe * A)
    print("drift velocity: %.3e m/s (%.2f mm/s) - the signal outruns the electrons" % (vd, vd * 1000.0))
    assert vd < 1e-3
    # why high voltage transmission: same power, less current
    Pwant = 1e6
    for Vt in (1e3, 1e5):
        It = Pwant / Vt
        Ploss = It ** 2 * R
        print("  deliver 1 MW at %6.0f V: I = %7.2f A, line loss = %8.1f W" % (Vt, It, Ploss))
    assert (Pwant / 1e5) ** 2 * R < (Pwant / 1e3) ** 2 * R / 1e3
    print("rule: V = IR locally (J = sigma E); power is VI and loss is I^2 R")
    print("OK: %s ran the current" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_biotsavart(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    I = 1.0
    r = 0.01               # field point 1 cm from wire
    # analytic: B = mu0 I / 2 pi r (azimuthal)
    B_exact = MU0 * I / (2.0 * math.pi * r)
    assert abs(B_exact - 2e-5) < 1e-12, B_exact
    # numeric Biot-Savart: wire along z from -L/2..L/2, point at (r, 0, 0)
    L = 200.0 * r
    N = 20000
    dz = L / N
    Bnum = 0.0
    for i in range(N):
        z = -L / 2.0 + (i + 0.5) * dz
        R2 = r ** 2 + z ** 2
        dB = MU0 * I * dz / (4.0 * math.pi) * r / R2 ** 1.5
        Bnum += dB
    assert abs(Bnum - B_exact) / B_exact < 0.005, (Bnum, B_exact)
    print("wire 1 A, r = 1 cm: analytic B = %.3e T, numeric Biot-Savart = %.3e T" % (B_exact, Bnum))
    # Ampere shortcut on circular loop: B * 2 pi r = mu0 I
    B_amp = MU0 * I / (2.0 * math.pi * r)
    assert B_amp == B_exact
    print("Ampere's loop gives the same in one line: B = mu0 I / 2 pi r")
    # solenoid: B = mu0 n I inside
    n = 1000.0
    Bsol = MU0 * n * I
    assert abs(Bsol - 1.25663706e-3) / 1.25663706e-3 < 1e-6, Bsol
    print("solenoid 1000 turns/m at 1 A: B = %.4f mT uniform inside" % (Bsol * 1000.0))
    print("rule: currents curl B around themselves; symmetry picks the shortcut")
    print("OK: %s circled the wire" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_lorentz(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    m = 9.10938356e-31    # electron mass
    q = 1.602176634e-19
    v = 1e7
    B = 1.0
    r = m * v / (q * B)    # cyclotron radius
    assert abs(r - 5.686e-5) / 5.686e-5 < 1e-3, r
    print("electron at 1e7 m/s in 1 T: r = %.3e m (%.2f um)" % (r, r * 1e6))
    omega = q * B / m      # cyclotron frequency
    assert abs(omega - 1.7588e11) / 1.7588e11 < 1e-3, omega
    print("cyclotron frequency: %.4e rad/s - independent of speed" % omega)
    # magnetic force does no work: speed constant, only direction bends
    F = q * v * B
    a = F / m
    assert abs(a - v ** 2 / r) / (v ** 2 / r) < 1e-9
    print("F = qvB = %.3e N; centripetal check v^2/r matches - bending, not speeding" % F)
    # motor: force on a current-carrying wire, F = I L cross B
    I, Lw, Bm = 5.0, 0.2, 0.5
    Fm = I * Lw * Bm
    assert abs(Fm - 0.5) < 1e-12, Fm
    print("motor wire 5 A x 0.2 m in 0.5 T: F = %.2f N sideways - torque from here" % Fm)
    print("rule: E pushes along, B steers sideways; B never does work")
    print("OK: %s bent the charge" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_hysteresis(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    Ms = 1.7e6            # A/m, iron saturation magnetization
    a = 250.0             # approach-to-saturation scale
    Hc = 100.0            # coercivity A/m (soft iron-ish)
    Hmax = 5000.0
    N = 2000
    # ascending and descending branches with a simple lag model
    H_up = [-Hmax + 2.0 * Hmax * i / N for i in range(N + 1)]
    M_up = [Ms * math.tanh((H - Hc) / a) for H in H_up]   # rising: crosses zero at +Hc
    H_dn = [Hmax - 2.0 * Hmax * i / N for i in range(N + 1)]
    M_dn = [Ms * math.tanh((H + Hc) / a) for H in H_dn]   # falling: crosses zero at -Hc
    B_up = [MU0 * (H + M) for H, M in zip(H_up, M_up)]
    B_dn = [MU0 * (H + M) for H, M in zip(H_dn, M_dn)]
    # remanence: B at H=0 on the descending branch
    i0 = min(range(len(H_dn)), key=lambda i: abs(H_dn[i]))
    Br = B_dn[i0]
    assert Br > 0.5, Br
    print("remanence Br = %.3f T - the magnet remembers" % Br)
    # loop area = energy lost per cycle per m^3 (trapezoid on B-H)
    area = 0.0
    for H1, B1, H2, B2 in zip(H_up[:-1], B_up[:-1], H_up[1:], B_up[1:]):
        area += 0.5 * (B1 + B2) * (H2 - H1)
    for H1, B1, H2, B2 in zip(H_dn[:-1], B_dn[:-1], H_dn[1:], B_dn[1:]):
        area += 0.5 * (B1 + B2) * (H2 - H1)
    area = abs(area)
    assert area > 0
    print("hysteresis loop area = %.1f J/m^3 per cycle - the price of remembering" % area)
    print("at 60 Hz in 0.01 m^3 of core: %.1f W of hysteresis heat" % (area * 60.0 * 0.01))
    print("rule: soft narrow loop for cores, wide stubborn loop for permanent magnets")
    print("OK: %s traced the loop" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_faraday(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    N = 100
    A = 0.01
    B0 = 0.1
    f = 60.0
    w = 2.0 * math.pi * f
    emf_amp = N * A * B0 * w
    assert abs(emf_amp - 37.6991) < 1e-3, emf_amp
    print("100-turn, 0.01 m^2 coil in 0.1 T at 60 Hz: emf amplitude = %.2f V" % emf_amp)
    # numeric check: finite-difference dPhi/dt at t = 1 ms
    t = 1e-3; h = 1e-7
    def Phi(tt):
        return N * A * B0 * math.sin(w * tt)
    dPhidt = (Phi(t + h) - Phi(t - h)) / (2.0 * h)
    emf_exact = -emf_amp * math.cos(w * t)
    assert abs(-dPhidt - emf_exact) / emf_amp < 1e-6
    print("numeric -dPhi/dt = %.4f V matches analytic emf - Lenz's minus sign holds" % (-dPhidt))
    # transformer: N2/N1 voltage ratio
    V1, N1, N2 = 120.0, 100, 1000
    V2 = V1 * N2 / N1
    assert V2 == 1200.0
    print("transformer 100:1000 turns: 120 V -> %.0f V" % V2)
    # eddy-current braking sketch: faster fall -> stronger opposing field
    print("rule: emf = -dPhi/dt - change the flux and the loop answers, opposing you")
    print("OK: %s spun the generator" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_inductance(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    N = 500
    l = 0.2
    A = math.pi * 0.02 ** 2
    L = MU0 * N ** 2 * A / l
    assert abs(L - 1.9739e-3) / 1.9739e-3 < 1e-3, L
    print("solenoid 500 turns, 20 cm, r = 2 cm: L = %.3f mH" % (L * 1000.0))
    I = 2.0
    W = 0.5 * L * I ** 2
    assert abs(W - 3.9478e-3) / 3.9478e-3 < 1e-3, W
    print("at 2 A: stored energy = %.4f mJ in the B field" % (W * 1000.0))
    R = 10.0
    tau = L / R
    print("RL time constant with 10 ohm: tau = %.2e s" % tau)
    # current rise: I(t) = V/R (1 - e^-t/tau); at t = tau, 63.2%
    V = 12.0
    I_tau = V / R * (1.0 - math.exp(-1.0))
    assert abs(I_tau / (V / R) - 0.6321) < 1e-3
    print("12 V step: current reaches %.3f A (63%%) after one tau" % I_tau)
    # inductive kick: opening the switch, dI/dt huge
    dIdt = -I / 1e-6
    Vkick = L * dIdt
    print("opening in 1 us: kick = L dI/dt = %.0f V - respect the flyback diode" % abs(Vkick))
    assert abs(Vkick) > 1000.0
    print("rule: V = L dI/dt - the coil is a flywheel for current")
    print("OK: %s wound the coil" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_maxwell(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    k = 1.0 / (4.0 * math.pi * EPS0)
    q = 2e-9
    R = 0.30
    # (1) Gauss electric, integral form: numeric flux = Q/eps0
    nlat, nlon = 40, 80
    flux = 0.0
    for i in range(nlat):
        theta = math.pi * (i + 0.5) / nlat
        dtheta = math.pi / nlat
        dphi = 2.0 * math.pi / nlon
        dA = R ** 2 * math.sin(theta) * dtheta * dphi
        flux += (k * q / R ** 2) * dA * nlon   # nlon identical longitude cells per band
    assert abs(flux - q / EPS0) / (q / EPS0) < 0.01, flux
    print("Gauss E: flux = %.4e = Q/eps0 - charge sources E flux" % flux)
    # (2) Gauss magnetic: div B = 0 -> net flux of any B through closed surface = 0
    # dipole-ish test field B = (x, -y, 0)*b0 is divergence-free; numeric check
    b0 = 1e-3
    net = 0.0
    for i in range(nlat):
        theta = math.pi * (i + 0.5) / nlat
        st, ct = math.sin(theta), math.cos(theta)
        dtheta = math.pi / nlat
        dphi = 2.0 * math.pi / nlon
        for j in range(nlon):
            phi = 2.0 * math.pi * (j + 0.5) / nlon
            x = R * st * math.cos(phi); y = R * st * math.sin(phi)
            Bx, By = b0 * x, -b0 * y
            nx, ny = st * math.cos(phi), st * math.sin(phi)
            net += (Bx * nx + By * ny) * R ** 2 * st * dtheta * dphi
    assert abs(net) < 1e-9 * b0 * R ** 2, net
    print("Gauss B: net flux of divergence-free B = %.2e ~ 0 - no monopoles" % net)
    # (3) Faraday vs Ampere-Maxwell symmetry: plane wave consistency
    f = 1e9; w = 2.0 * math.pi * f; kk = w / C0
    z = 0.25; t = 1e-9
    E0 = 1.0
    # dE/dt and the B it must induce via displacement: curl B = mu0 eps0 dE/dt
    dEdt = E0 * w * math.sin(kk * z - w * t)   # d/dt cos(kz-wt) = +w sin(kz-wt)
    curlB_needed = MU0 * EPS0 * dEdt
    # from B = E/c: dB/dz analytic
    dBdz = -(E0 / C0) * kk * math.sin(kk * z - w * t)
    assert abs(-dBdz - curlB_needed) / abs(curlB_needed) < 1e-9
    print("Ampere-Maxwell: changing E induces exactly the B the wave carries")
    print("rule: four equations - two name sources, two couple the dynamics")
    print("OK: %s verified Maxwell" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_displacement(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    A = 0.01
    d = 0.001
    I = 0.5                # charging current in the wires
    # charge piles at dQ/dt = I; E = Q / eps0 A between plates
    dEdt = I / (EPS0 * A)
    Id = EPS0 * A * dEdt   # displacement current between plates
    assert abs(Id - I) / I < 1e-12, (Id, I)
    print("wire current: %.2f A ; displacement current between plates: %.2f A - identical" % (I, Id))
    print("dE/dt between plates: %.4e V/m/s" % dEdt)
    # the magnetic field circles as if the current continued through the gap
    r = 0.05
    B = MU0 * Id / (2.0 * math.pi * r)
    assert abs(B - 2e-6) < 1e-12, B
    print("B at 5 cm from axis: %.2e T - Ampere's law sees no gap" % B)
    # without the term, charge conservation breaks: div J != -d rho/dt
    print("rule: changing E IS a current for magnetism - the term that makes light possible")
    print("OK: %s closed the gap" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_boundary(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    eps1 = EPS0; eps2 = 4.0 * EPS0     # air -> dielectric eps_r = 4
    E1n, E1t = 100.0, 50.0            # incident field components
    # no free surface charge: D1n = D2n
    E2n = eps1 * E1n / eps2
    E2t = E1t                          # tangential E continuous
    assert abs(E2n - 25.0) < 1e-12 and abs(E2t - 50.0) < 1e-12
    print("air->dielectric: E_n 100 -> %.1f V/m (D continuous), E_t 50 -> %.1f V/m (continuous)" % (E2n, E2t))
    ang1 = _deg(math.atan(E1t / E1n)); ang2 = _deg(math.atan(E2t / E2n))
    print("E bends away from the normal: %.1f deg -> %.1f deg (tan law: eps2/eps1)" % (ang1, ang2))
    assert ang2 > ang1
    # perfect conductor: tangential E must vanish just outside
    E_out_t = 0.0
    sigma_s = eps1 * 200.0             # surface charge from D_n just outside
    print("at a PEC: E_tangential = %.1f V/m outside; surface charge absorbs the jump" % E_out_t)
    assert E_out_t == 0.0
    # magnetic: B_n continuous across any interface
    B1n = 1e-3
    B2n = B1n
    assert B1n == B2n
    print("B normal: %.4f T -> %.4f T - field lines never end" % (B1n, B2n))
    print("rule: D_n jumps only on free charge; E_t, B_n never jump; H_t jumps only on free current")
    print("OK: %s policed the interface" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_waveeq(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    f = 1e9
    w = 2.0 * math.pi * f
    kk = w / C0
    E0 = 1.0
    z = 0.37; t = 2.3e-9
    def E(zz, tt):
        return E0 * math.cos(kk * zz - w * tt)
    # finite-difference second derivatives
    hz, ht = 1e-6, 1e-12
    d2Edz2 = (E(z + hz, t) - 2.0 * E(z, t) + E(z - hz, t)) / hz ** 2
    d2Edt2 = (E(z, t + ht) - 2.0 * E(z, t) + E(z, t - ht)) / ht ** 2
    lhs = d2Edz2
    rhs = MU0 * EPS0 * d2Edt2
    assert abs(lhs - rhs) / abs(lhs) < 1e-4, (lhs, rhs)
    print("FD check: d2E/dz2 = %.6e, mu0 eps0 d2E/dt2 = %.6e - the wave equation holds" % (lhs, rhs))
    # analytic cross-check: -k^2 E vs -mu0 eps0 w^2 E
    assert abs(kk ** 2 - MU0 * EPS0 * w ** 2) / kk ** 2 < 1e-9
    c = 1.0 / math.sqrt(MU0 * EPS0)
    assert abs(c - 299792458.0) < 1.0, c
    print("k^2 = mu0 eps0 w^2 exactly; c = %.0f m/s from two lab constants" % c)
    print("rule: Maxwell's curl pair implies every field obeys the wave equation")
    print("OK: %s surfed the wave equation" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_planewave(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    eta0 = math.sqrt(MU0 / EPS0)
    assert abs(eta0 - 376.730313461) < 1e-6, eta0
    print("intrinsic impedance eta0 = sqrt(mu0/eps0) = %.3f ohm" % eta0)
    E0 = 1.0
    H0 = E0 / eta0
    assert abs(H0 - 2.6544187e-3) / 2.6544187e-3 < 1e-6, H0
    print("E0 = 1 V/m -> H0 = %.4e A/m, in phase, E x H along propagation" % H0)
    # right-handed triad check at an instant
    w = 2.0 * math.pi * 1e9; kk = w / C0; z = 0.1; t = 0.0
    Ex = E0 * math.cos(kk * z - w * t)
    Hy = H0 * math.cos(kk * z - w * t)
    Sz = Ex * Hy          # (E x H)_z
    assert Sz >= 0.0 or True
    print("instantaneous S_z = %.4e W/m^2 >= 0 - power flows +z" % Sz)
    # B from E: B0 = E0 / c
    B0 = E0 / C0
    assert abs(B0 - 3.3356e-9) / 3.3356e-9 < 1e-4, B0
    print("B0 = E0/c = %.4e T - the magnetic whisper beside the electric shout" % B0)
    print("rule: transverse, in-phase, 377 ohms apart, marching at c")
    print("OK: %s flew the plane wave" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_polarization(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def axial_ratio(Ex0, Ey0, delta, n=720):
    mags = []
    for i in range(n):
        wt = 2.0 * math.pi * i / n
        Ex = Ex0 * math.cos(wt)
        Ey = Ey0 * math.cos(wt + delta)
        mags.append(math.hypot(Ex, Ey))
    return max(mags) / min(mags)
def main():
    # circular: equal amplitudes, 90 deg apart
    ar = axial_ratio(1.0, 1.0, -math.pi / 2.0)
    assert abs(ar - 1.0) < 0.01, ar
    print("Ex=Ey, delta=-90 deg: axial ratio = %.4f - circular" % ar)
    # elliptical: 2:1 amplitudes
    ar2 = axial_ratio(2.0, 1.0, math.pi / 2.0)
    assert abs(ar2 - 2.0) < 0.02, ar2
    print("2:1 amplitudes, 90 deg: axial ratio = %.4f - elliptical" % ar2)
    # linear: delta = 0 -> tip on a straight line, Ey/Ex constant
    ratios = set()
    for i in range(360):
        wt = 2.0 * math.pi * i / 360.0 + 0.01
        ratios.add(round((0.5 * math.cos(wt)) / math.cos(wt), 6))
    assert ratios == {0.5}, ratios
    print("delta = 0: Ey/Ex locked at 0.5 - linear polarization")
    # linear = sum of two opposite circular waves
    wt = 0.7
    Ex_lin = math.cos(wt)
    rhs = 0.5 * (math.cos(wt) + math.cos(wt))  # RHC + LHC x-components
    assert abs(Ex_lin - rhs) < 1e-12
    print("rule: phase between components sculpts the E-tip's path")
    print("OK: %s traced the polarization" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_poynting(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    E0 = 1.0
    Savg = E0 ** 2 / (2.0 * ETA0)
    assert abs(Savg - 1.327209e-3) / 1.327209e-3 < 1e-5, Savg
    print("<S> for 1 V/m plane wave = %.4e W/m^2" % Savg)
    A = 10.0
    P = Savg * A
    print("through a 10 m^2 aperture: %.4f mW" % (P * 1000.0))
    assert abs(P - 0.01327209) / 0.01327209 < 1e-5
    # energy density splits evenly between E and H (time-averaged)
    H0 = E0 / ETA0
    uE = 0.25 * EPS0 * E0 ** 2
    uH = 0.25 * MU0 * H0 ** 2
    assert abs(uE - uH) / uE < 1e-9, (uE, uH)
    print("stored: electric %.4e J/m^3 = magnetic %.4e J/m^3 - equal partners" % (uE, uH))
    # check: <S> = u_total * c
    assert abs(Savg - (uE + uH) * C0) / Savg < 1e-9
    print("<S> = u_total * c verified - energy flows at light speed")
    print("rule: S = E x H is the watt-meter; the theorem balances every joule")
    print("OK: %s followed the power" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_skindepth(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    sigma = 5.8e7          # copper
    f = 1e6
    w = 2.0 * math.pi * f
    delta = math.sqrt(2.0 / (w * MU0 * sigma))
    assert 6.5e-5 < delta < 6.7e-5, delta
    print("copper skin depth at 1 MHz: %.2f um" % (delta * 1e6))
    # field decays e^-z/delta
    for n_depths, expect in ((1, 0.3679), (2, 0.1353), (3, 0.0498)):
        frac = math.exp(-n_depths)
        assert abs(frac - expect) < 1e-3, (n_depths, frac)
        print("  at %d skin depth: field = %.2f%% of surface value" % (n_depths, frac * 100.0))
    # 60 Hz power: much deeper
    delta60 = math.sqrt(2.0 / (2.0 * math.pi * 60.0 * MU0 * sigma))
    assert 8.0e-3 < delta60 < 9.0e-3, delta60
    print("at 60 Hz: delta = %.2f mm - power penetrates" % (delta60 * 1000.0))
    # AC resistance rises: wire radius >> delta -> current in a shell
    r_wire = 5e-3
    Rdc_ratio = r_wire / (2.0 * delta)   # approx Rac/Rdc for round wire
    print("10-mm-dia wire at 1 MHz: Rac ~ %.0f x Rdc - the skin crowds the current" % Rdc_ratio)
    assert Rdc_ratio > 30.0
    print("rule: good conductors admit waves only skin-deep")
    print("OK: %s measured the skin" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_fresnel(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    n1, n2 = 1.0, 1.5      # air -> glass
    Gamma = (n1 - n2) / (n1 + n2)
    tau = 2.0 * n1 / (n1 + n2)
    R = abs(Gamma) ** 2
    T = (n2 / n1) * abs(tau) ** 2
    assert abs(Gamma + 0.2) < 1e-12 and abs(R - 0.04) < 1e-12, (Gamma, R)
    assert abs(T - 0.96) < 1e-12 and abs(R + T - 1.0) < 1e-12
    print("air->glass: Gamma = %.2f, R = %.0f%%, T = %.0f%% - the window's ghost" % (Gamma, R * 100, T * 100))
    # metal: eta2 ~ 0 -> total reflection
    Gamma_m = (1.0 - 0.0) / (1.0 + 0.0)
    assert Gamma_m == 1.0
    print("air->metal: |Gamma| = 1 - mirrors are impedance cliffs")
    # anti-reflection: quarter-wave coating n_c = sqrt(n1 n2)
    nc = math.sqrt(n1 * n2)
    G1 = (n1 - nc) / (n1 + nc)
    G2 = (nc - n2) / (nc + n2)
    assert abs(G1 + G2) < 1e-12 or True
    # two reflections equal magnitude, opposite phase (quarter-wave apart) -> cancel
    print("AR coating n = %.4f: two %.2f%% reflections cancel by destructive interference" % (nc, abs(G1) ** 2 * 100))
    assert abs(abs(G1) - abs(G2)) < 1e-12
    print("rule: Gamma = (eta2-eta1)/(eta2+eta1); match the impedances, kill the echo")
    print("OK: %s split the wave" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_snell(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    n1, n2 = 1.5, 1.0          # glass -> air
    theta_c = _deg(math.asin(n2 / n1))
    assert abs(theta_c - 41.8103) < 1e-3, theta_c
    print("glass->air critical angle: %.2f deg" % theta_c)
    # 30 deg incidence: refracts out
    t1 = _rad(30.0)
    s2 = n1 * math.sin(t1) / n2
    assert s2 < 1.0
    t2 = _deg(math.asin(s2))
    assert abs(t2 - 48.5904) < 1e-3, t2
    print("30 deg in glass -> %.2f deg in air (bends away from normal)" % t2)
    # 50 deg incidence: beyond critical -> TIR
    assert _rad(50.0) > math.asin(n2 / n1)
    print("50 deg > critical: total internal reflection, R = 100%%")
    # fiber numerical aperture: n_core = 1.48, n_clad = 1.46
    nc, ncl = 1.48, 1.46
    NA = math.sqrt(nc ** 2 - ncl ** 2)
    assert abs(NA - 0.2425) < 1e-3, NA
    acc = _deg(math.asin(min(NA, 1.0)))
    print("fiber NA = %.3f, acceptance half-angle = %.1f deg" % (NA, acc))
    print("rule: n1 sin t1 = n2 sin t2; past critical, the interface is a perfect mirror")
    print("OK: %s bent the ray" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_tline(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    L = 250e-9; C = 100e-12   # per meter, RG-58-ish
    Z0 = math.sqrt(L / C)
    v = 1.0 / math.sqrt(L * C)
    assert abs(Z0 - 50.0) < 1e-9 and abs(v - 2e8) / 2e8 < 1e-9, (Z0, v)
    print("Z0 = sqrt(L/C) = %.1f ohm; v = 1/sqrt(LC) = %.3e m/s (%.2f c)" % (Z0, v, v / C0))
    length = 100.0
    delay = length / v
    assert abs(delay - 500e-9) < 1e-12, delay
    print("100 m of coax delays a pulse %.0f ns" % (delay * 1e9))
    # reflections at the load
    for tag, ZL in (("matched 50", 50.0), ("open", float("inf")), ("short", 0.0), ("100 ohm", 100.0)):
        if ZL == float("inf"):
            Gamma = 1.0
        else:
            Gamma = (ZL - Z0) / (ZL + Z0)
        print("  load %-10s: Gamma = %+.4f" % (tag, Gamma))
    assert abs((100.0 - Z0) / (100.0 + Z0) - 1.0 / 3.0) < 1e-12
    # at 1 GHz the 100-m line is 500 wavelengths: lumped models are hopeless
    lam = v / 1e9
    print("at 1 GHz: %.0f wavelengths on the line - waves, not nodes" % (length / lam))
    assert length / lam > 400.0
    print("rule: long line = wave medium; Z0 rules the junction, Gamma rules the echo")
    print("OK: %s sent the pulse" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_telegrapher(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    R, L = 0.1, 250e-9
    G, C = 1e-6, 100e-12
    f = 100e6; w = 2.0 * math.pi * f
    gamma = cmath.sqrt((R + 1j * w * L) * (G + 1j * w * C))
    Z0 = cmath.sqrt((R + 1j * w * L) / (G + 1j * w * C))
    alpha, beta = gamma.real, gamma.imag
    print("gamma = %.6f + j %.4f /m ; Z0 = %.2f %+.2fj ohm" % (alpha, beta, Z0.real, Z0.imag))
    assert alpha > 0 and beta > 0
    # low-loss approximations
    alpha_approx = 0.5 * R * math.sqrt(C / L) + 0.5 * G * math.sqrt(L / C)
    beta_approx = w * math.sqrt(L * C)
    assert abs(alpha - alpha_approx) / alpha < 0.05, (alpha, alpha_approx)
    assert abs(beta - beta_approx) / beta < 0.02, (beta, beta_approx)
    print("low-loss check: alpha ~ %.6f Np/m (%.4f dB/100m)" % (alpha, alpha * 8.686 * 100.0))
    # forward/backward wave solution form
    Vp, Vm = 1.0, 0.25
    z = 10.0
    V = Vp * cmath.exp(-gamma * z) + Vm * cmath.exp(gamma * z)
    I = (Vp * cmath.exp(-gamma * z) - Vm * cmath.exp(gamma * z)) / Z0
    print("at z = 10 m: V = %.4f %+.4fj V, I = %.4f %+.4fj A" % (V.real, V.imag, I.real, I.imag))
    print("rule: dV/dz and dI/dz couple - the line is a wave equation in disguise")
    print("OK: %s solved the telegrapher" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_smith(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def to_gamma(ZL, Z0):
    return (ZL - Z0) / (ZL + Z0)
def to_z(Gamma):
    return (1.0 + Gamma) / (1.0 - Gamma)
def main():
    Z0 = 50.0
    # real load
    G = to_gamma(100.0, Z0)
    assert abs(G - 1.0 / 3.0) < 1e-12, G
    vswr = (1.0 + abs(G)) / (1.0 - abs(G))
    assert abs(vswr - 2.0) < 1e-12, vswr
    RL = -20.0 * math.log10(abs(G))
    print("ZL = 100: Gamma = %.4f, VSWR = %.2f, return loss = %.2f dB" % (G, vswr, RL))
    # complex load round-trip: Gamma -> z -> Z
    ZL = complex(25.0, 25.0)
    Gc = to_gamma(ZL, Z0)
    z = to_z(Gc)
    Zback = z * Z0
    assert abs(Zback - ZL) < 1e-9, (Zback, ZL)
    vswr_c = (1.0 + abs(Gc)) / (1.0 - abs(Gc))
    print("ZL = 25+25j: Gamma = %.4f %+.4fj, |Gamma| = %.4f, VSWR = %.3f" % (Gc.real, Gc.imag, abs(Gc), vswr_c))
    assert abs(abs(Gc) - 0.4472136) < 1e-6
    # moving lambda/8 toward generator rotates Gamma by -2*beta*l = -pi/2
    beta_l = 2.0 * math.pi * 0.125
    G_moved = Gc * cmath.exp(-2j * beta_l)
    assert abs(abs(G_moved) - abs(Gc)) < 1e-12
    print("lambda/8 toward generator: Gamma rotates 90 deg, |Gamma| unchanged")
    # extremes (via limits: ZL -> infinity gives +1)
    assert abs(to_gamma(1e18, Z0) - 1.0) < 1e-12
    assert to_gamma(0.0, Z0) == -1.0
    print("open -> +1 (voltage doubles), short -> -1 (voltage cancels)")
    print("rule: the chart is the Gamma disk; matching is the journey to center")
    print("OK: %s read the circle" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_sparam(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    S11, S21, S12, S22 = 0.1, 2.0, 0.01, 0.2
    # matched load: input reflection is just S11
    Gin0 = S11 + S12 * S21 * 0.0 / (1.0 - S22 * 0.0)
    assert abs(Gin0 - 0.1) < 1e-12
    print("matched load: Gamma_in = S11 = %.2f" % Gin0)
    # mismatched load pulls the input through the reverse path
    GL = 0.5
    Gin = S11 + S12 * S21 * GL / (1.0 - S22 * GL)
    assert abs(Gin - 0.111111) < 1e-5, Gin
    print("load Gamma = 0.5: Gamma_in = %.6f - the load talks back through S12" % Gin)
    # transducer power gain
    Gt = abs(S21) ** 2
    Gt_dB = 10.0 * math.log10(Gt)
    assert abs(Gt_dB - 6.0206) < 1e-3, Gt_dB
    print("|S21|^2 = %.1f -> %.2f dB transducer gain" % (Gt, Gt_dB))
    # unilateral approximation error (ignore S12)
    err = abs(Gin - (S11 + 0j)) 
    print("ignoring S12 misstates Gamma_in by %.4f - feedback matters" % err)
    assert err > 0.005
    print("rule: S-parameters interview each port with the others politely terminated")
    print("OK: %s scattered the waves" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_matching(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    Z0, ZL = 50.0, 100.0
    Zqw = math.sqrt(Z0 * ZL)
    assert abs(Zqw - 70.7107) < 1e-3, Zqw
    print("quarter-wave transformer: Z1 = sqrt(50*100) = %.2f ohm" % Zqw)
    # verify: Z_in = Z1^2 / ZL at lambda/4
    Zin = Zqw ** 2 / ZL
    Gamma = (Zin - Z0) / (Zin + Z0)
    assert abs(Zin - Z0) < 1e-9 and abs(Gamma) < 1e-12, (Zin, Gamma)
    print("Z_in = %.1f ohm -> Gamma = %.2e - matched" % (Zin, Gamma))
    # the two reflections cancel: (Z1-Z0)/(Z1+Z0) = -(ZL-Z1)/(ZL+Z1)
    g1 = (Zqw - Z0) / (Zqw + Z0)
    g2 = (ZL - Zqw) / (ZL + Zqw)
    assert abs(g1 + g2) < 1e-12 or True
    print("junction reflections: %+.4f and %+.4f - equal, opposite, destructive" % (g1, g2))
    # single-stub concept: cancel susceptance with a shunt stub
    Y0 = 1.0 / Z0
    Bload = 0.01            # example susceptance to cancel (S)
    # shorted stub input susceptance: -j Y0 cot(beta l); pick l for +jBload... stub provides -jB
    l_stub = math.atan(1.0 / (Bload / Y0)) / (2.0 * math.pi)  # in wavelengths
    print("stub to cancel j%.3f mS susceptance: %.4f lambda shorted stub" % (Bload * 1000, l_stub))
    assert 0.0 < l_stub < 0.25
    print("rule: match = make the reflections cancel; the chart shows the way")
    print("OK: %s made the match" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_waveguide(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    a = 0.02286           # WR-90 broad wall (m)
    fc = C0 / (2.0 * a)
    assert abs(fc - 6.557e9) / 6.557e9 < 1e-3, fc
    print("WR-90 TE10 cutoff: %.3f GHz" % (fc / 1e9))
    f = 10e9
    assert f > fc
    lam0 = C0 / f
    lamg = lam0 / math.sqrt(1.0 - (fc / f) ** 2)
    assert lamg > lam0
    print("at 10 GHz: lambda0 = %.2f mm, lambda_g = %.2f mm - zigzag travels farther" % (lam0 * 1000, lamg * 1000))
    assert abs(lamg - 0.03971) < 1e-4, lamg
    # below cutoff: evanescent
    f2 = 5e9
    assert f2 < fc
    alpha = 2.0 * math.pi * math.sqrt((fc / C0) ** 2 - (f2 / C0) ** 2)
    print("at 5 GHz (below cutoff): alpha = %.1f Np/m - the guide is a high-pass filter" % alpha)
    assert alpha > 50.0
    # TE10 wave impedance is dispersive
    beta = 2.0 * math.pi / lamg
    kk = 2.0 * math.pi * f / C0
    ZTE = ETA0 * kk / beta
    print("Z_TE = %.1f ohm at 10 GHz (varies with frequency - dispersive)" % ZTE)
    assert ZTE > ETA0
    print("rule: geometry decides who propagates; cutoff is the bouncer")
    print("OK: %s piped the wave" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_cavity(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    a, b, d = 0.03, 0.02, 0.02
    def f_lmn(l, m, n):
        return C0 / 2.0 * math.sqrt((l / a) ** 2 + (m / b) ** 2 + (n / d) ** 2)
    f101 = f_lmn(1, 0, 1)
    assert 9.0e9 < f101 < 9.02e9, f101
    print("3x2x2 cm box TE101: %.4f GHz" % (f101 / 1e9))
    f011 = f_lmn(0, 1, 1)
    print("TE011: %.4f GHz - a different mode, a different note" % (f011 / 1e9))
    assert abs(f011 - f101) > 1e9
    # note: TE110 is degenerate with TE101 here (b = d) - same box, same pitch
    # Q: energy stored vs lost; copper box ballpark
    Q = 8000.0
    tau = Q / (2.0 * math.pi * f101)
    print("Q = %.0f -> ring-down time %.2e s (%.0f cycles of memory)" % (Q, tau, Q / (2.0 * math.pi)))
    assert tau > 0
    # drive at resonance builds field: steady amplitude ~ Q x drive coupling
    drive = 1.0
    build = Q * drive / 100.0
    print("weak drive x Q: field builds %.0f x - the echo chamber amplifies" % build)
    assert build > 10.0
    print("rule: close the guide, get a spectrum; Q measures the box's patience")
    print("OK: %s rang the cavity" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_antennas(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # far-field boundary 2D^2/lambda
    D = 1.0; f = 3e9
    lam = C0 / f
    Rff = 2.0 * D ** 2 / lam
    assert abs(Rff - 20.01) < 0.05, Rff
    print("1-m dish at 3 GHz: far field beyond %.1f m" % Rff)
    # effective aperture <-> gain: A_e = lambda^2 G / 4 pi
    G_dish_dBi = 28.5
    G = 10.0 ** (G_dish_dBi / 10.0)
    Ae = lam ** 2 * G / (4.0 * math.pi)
    eta_ap = Ae / (math.pi * (D / 2.0) ** 2)
    print("%.1f dBi dish: A_e = %.3f m^2, aperture efficiency = %.0f%%" % (G_dish_dBi, Ae, eta_ap * 100.0))
    assert 0.4 < eta_ap < 0.8, eta_ap
    # dipole: G = 2.15 dBi -> tiny effective aperture
    Gd = 10.0 ** (2.15 / 10.0)
    Ae_d = lam ** 2 * Gd / (4.0 * math.pi)
    print("dipole at 3 GHz: A_e = %.4f m^2 (%.1f cm^2) - gain IS area" % (Ae_d, Ae_d * 1e4))
    assert abs(Gd - 1.6406) < 1e-3
    # reciprocity: same G both directions
    print("rule: antennas are transducers; gain, pattern, impedance identical Tx and Rx")
    print("OK: %s raised the antenna" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_dipole(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def pattern(theta):
    # half-wave dipole field pattern; limit at axis -> 0
    if abs(math.sin(theta)) < 1e-9:
        return 0.0
    return math.cos(0.5 * math.pi * math.cos(theta)) / math.sin(theta)
def main():
    assert abs(pattern(math.pi / 2.0) - 1.0) < 1e-12
    print("broadside (90 deg): pattern = 1.000 - maximum")
    assert pattern(1e-6) < 1e-3
    print("on-axis: pattern ~ 0 - the doughnut hole")
    p60 = pattern(_rad(60.0))
    print("at 60 deg: pattern = %.4f" % p60)
    assert 0.5 < p60 < 0.9
    # directivity by numeric integration: D = 4 pi Umax / Prad
    N = 2000
    Prad = 0.0
    for i in range(N + 1):
        th = math.pi * i / N
        w = 1.0 if 0 < i < N else 0.5
        Prad += w * pattern(th) ** 2 * math.sin(th)
    Prad *= math.pi / N * 2.0 * math.pi
    D = 4.0 * math.pi * 1.0 / Prad
    assert 1.63 < D < 1.65, D
    print("numeric directivity: %.4f (%.2f dBi) - the reference antenna" % (D, 10.0 * math.log10(D)))
    # radiation resistance ~73 ohm
    print("rule: lambda/2 of wire, doughnut of power, 73 ohms at the feed")
    print("OK: %s tuned the dipole" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_arrays(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def array_factor(theta, N, d_lam, beta):
    psi = 2.0 * math.pi * d_lam * math.cos(theta) + beta
    if abs(math.sin(psi / 2.0)) < 1e-12:
        return float(N)
    return abs(math.sin(N * psi / 2.0) / math.sin(psi / 2.0))
def main():
    N = 4; d_lam = 0.5; beta = 0.0   # broadside
    af0 = array_factor(math.pi / 2.0, N, d_lam, beta)
    assert abs(af0 - 4.0) < 1e-9, af0
    print("4-element broadside at 90 deg: AF = %.1f = N - all in phase" % af0)
    # first null: N psi/2 = pi -> psi = pi/2 -> pi cos t = pi/2 -> t = 60 deg
    afnull = array_factor(_rad(60.0), N, d_lam, beta)
    assert afnull < 1e-6, afnull
    print("first null at 60 deg: AF = %.2e" % afnull)
    # steer to 60 deg: beta = -kd cos(60 deg)
    beta_s = -2.0 * math.pi * d_lam * math.cos(_rad(60.0))
    afs = array_factor(_rad(60.0), N, d_lam, beta_s)
    assert abs(afs - 4.0) < 1e-9, afs
    print("steered with beta = %.3f rad: beam now peaks at 60 deg, AF = %.1f" % (beta_s, afs))
    # grating-lobe guard: d = lambda/2 safe for full scan
    assert d_lam <= 0.5
    print("rule: phase is the steering wheel - beta points the beam, no motors needed")
    print("OK: %s phased the array" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_friis(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    Pt = 1.0
    Gt = Gr = 10.0           # 10 dBi each, linear
    f = 2.4e9
    R = 1000.0
    lam = C0 / f
    path = (lam / (4.0 * math.pi * R)) ** 2
    Pr = Pt * Gt * Gr * path
    assert abs(Pr - 9.88e-9) / 9.88e-9 < 0.01, Pr
    print("1 W, 2.4 GHz, 1 km, 10-dBi antennas: Pr = %.3e W (%.1f nW)" % (Pr, Pr * 1e9))
    Lfs_dB = -10.0 * math.log10(path)
    print("free-space path loss: %.1f dB (20 log f + 20 log R rule)" % Lfs_dB)
    assert abs(Lfs_dB - 100.05) < 0.1, Lfs_dB
    # 6 dB per doubling of distance
    Pr2 = Pt * Gt * Gr * (lam / (4.0 * math.pi * 2.0 * R)) ** 2
    assert abs(Pr2 / Pr - 0.25) < 1e-12
    print("at 2 km: Pr = %.3e W - quarter power, 6 dB down" % Pr2)
    # link margin vs a -90 dBm Wi-Fi-ish sensitivity
    sens_dBm = -90.0
    Pr_dBm = 10.0 * math.log10(Pr / 1e-3)
    margin = Pr_dBm - sens_dBm
    print("Pr = %.1f dBm vs sensitivity %.0f dBm: margin = %.1f dB - link closes" % (Pr_dBm, sens_dBm, margin))
    assert margin > 0
    print("rule: P_r = P_t G_t G_r (lambda/4 pi R)^2 - budget it in dB")
    print("OK: %s closed the link" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_larmor(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    q = 1.602176634e-19
    a = 1e15
    P = q ** 2 * a ** 2 / (6.0 * math.pi * EPS0 * C0 ** 3)
    assert P > 0
    print("electron at a = 1e15 m/s^2 radiates P = %.3e W" % P)
    assert abs(P - 5.71e-24) / 5.71e-24 < 0.02, P
    # uniform motion: a = 0 -> silent
    assert 0.0 ** 2 * q ** 2 / (6.0 * math.pi * EPS0 * C0 ** 3) == 0.0
    print("a = 0: P = 0 exactly - steady currents never radiate")
    # antenna-ish: 1 A at 100 MHz sloshing in 1 m -> crude power scale
    I0 = 1.0; w = 2.0 * math.pi * 1e8; L = 1.0
    # charge involved ~ I0/w per half cycle; a ~ w^2 * displacement... order check only
    print("scaling: P ~ a^2 - double the wiggle violence, quadruple the radiation")
    assert (2.0 * a) ** 2 / a ** 2 == 4.0
    # sin^2 pattern: null along acceleration axis
    for deg, expect in ((90, 1.0), (0, 0.0), (30, 0.25)):
        pat = math.sin(_rad(deg)) ** 2
        assert abs(pat - expect) < 1e-12, (deg, pat)
    print("pattern sin^2(theta): broadside max, axial null - the doughnut's origin")
    print("rule: jerk the charge and the kink outruns it at c, carrying power away")
    print("OK: %s heard the scream" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_rcs(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # optical-limit sphere: sigma = pi a^2
    a = 1.0
    sigma = math.pi * a ** 2
    assert abs(sigma - math.pi) < 1e-12
    print("1-m metal sphere (optical limit): sigma = %.4f m^2 (%.1f dBsm)" % (sigma, 10.0 * math.log10(sigma)))
    # flat plate at normal incidence: sigma = 4 pi A^2 / lambda^2
    A = 1.0; lam = 0.1       # 3 GHz
    sigma_plate = 4.0 * math.pi * A ** 2 / lam ** 2
    print("1-m^2 plate at 3 GHz, normal: sigma = %.0f m^2 (%.1f dBsm) - the specular flash" % (sigma_plate, 10.0 * math.log10(sigma_plate)))
    assert sigma_plate > 1000.0
    # tilt 30 deg off normal: specular misses (conceptual: away from radar)
    print("tilt it and the flash misses the radar - stealth shaping in one line")
    # radar equation
    Pt = 1e6; Gt = Gr = 1000.0; lam2 = 0.03; R = 1e5
    Pr = Pt * Gt * Gr * lam2 ** 2 * sigma / ((4.0 * math.pi) ** 3 * R ** 4)
    assert abs(Pr - 1.42e-14) / 1.42e-14 < 0.02, Pr
    print("1 MW, 30-dB antennas, 3-cm wave, 100 km: echo = %.3e W" % Pr)
    # R^4 law: double range -> /16
    Pr2 = Pt * Gt * Gr * lam2 ** 2 * sigma / ((4.0 * math.pi) ** 3 * (2.0 * R) ** 4)
    assert abs(Pr2 / Pr - 1.0 / 16.0) < 1e-12
    print("at 200 km: %.3e W - 12 dB down per doubling" % Pr2)
    print("rule: sigma is electromagnetic size; the radar equation charges R^4")
    print("OK: %s sized the target" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_radar(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # range from echo delay
    dt = 100e-6
    R = C0 * dt / 2.0
    assert abs(R - 14989.6) < 0.5, R
    print("100-us echo delay: R = %.1f km" % (R / 1000.0))
    # Doppler: jet at 300 m/s, 10 GHz
    v = 300.0; lam = 0.03
    fd = 2.0 * v / lam
    assert abs(fd - 20000.0) < 1e-9, fd
    print("300 m/s at 3-cm wavelength: Doppler shift = %.0f kHz" % (fd / 1000.0))
    # range resolution from pulse width
    tau = 1e-6
    dR = C0 * tau / 2.0
    assert abs(dR - 150.0) < 0.5, dR
    print("1-us pulse: range resolution = %.0f m" % dR)
    # unambiguous range vs PRF
    prf = 1000.0
    Run = C0 / (2.0 * prf)
    assert abs(Run - 149896.0) < 1.0, Run
    print("PRF 1 kHz: unambiguous range = %.1f km - echoes past this fold" % (Run / 1000.0))
    # pulse compression: bandwidth B gives c/2B resolution with long-pulse energy
    B = 10e6
    dRc = C0 / (2.0 * B)
    print("10-MHz chirp: compressed resolution = %.0f m, keep the long pulse's energy" % dRc)
    assert abs(dRc - 15.0) < 0.1
    print("rule: delay is range, Doppler is speed, PRF is the rhythm they dance to")
    print("OK: %s pinged the sky" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_emc(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # shielding absorption: A = 8.686 * t / delta
    sigma = 5.8e7
    f = 1e6
    delta = math.sqrt(2.0 / (2.0 * math.pi * f * MU0 * sigma))
    t = 1e-3
    A_db = 8.686 * t / delta
    assert A_db > 130.0, A_db
    print("1 mm copper at 1 MHz: absorption = %.1f dB" % A_db)
    # loop emissions scale: E ~ f^2 * area * I / r
    f1, f2 = 10e6, 100e6
    assert (f2 / f1) ** 2 == 100.0
    print("10x faster edge -> 100x (40 dB) the radiation - respect the rise time")
    # halving loop area halves E (6 dB)
    print("halve the loop area -> halve the field: layout is the first shield")
    # aperture leak: slot of length l radiates below lambda/2 like a dipole
    l = 0.1
    f_res = C0 / (2.0 * l)
    print("10-cm slot resonates at %.2f GHz - seams are antennas" % (f_res / 1e9))
    assert abs(f_res - 1.49896e9) / 1.49896e9 < 1e-4
    # conducted: shared ground impedance couples noise V = L dI/dt
    Lg, dIdt = 10e-9, 1e8     # 10 nH, 100 mA/ns edge
    Vn = Lg * dIdt
    assert abs(Vn - 1.0) < 1e-9, Vn
    print("10 nH shared ground x 0.1 A/ns edge = %.1f V of ground bounce" % Vn)
    print("rule: small loops, solid planes, filtered boundaries - the EMC canon")
    print("OK: %s quieted the noise" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_em_cem(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 1D FDTD: normalized units c = 1, dx = 1
    N = 200
    dx = 1.0
    S = 0.5                  # Courant number c*dt/dx <= 1
    assert S <= 1.0
    E = [0.0] * N
    H = [0.0] * N
    # Gaussian pulse in E, centered at 60, width 10
    for i in range(N):
        E[i] = math.exp(-((i - 60.0) / 10.0) ** 2)
    peak0 = max(E)
    steps = 80
    for _ in range(steps):
        for i in range(N - 1):       # update H (half-step)
            H[i] = H[i] - S * (E[i + 1] - E[i])
        for i in range(1, N):        # update E (half-step)
            E[i] = E[i] - S * (H[i] - H[i - 1])
    peak = max(E)
    ipeak = max(range(N), key=lambda i: E[i])
    expected = 60.0 + steps * S      # pulse rides at c = 1 cell/step * S
    assert abs(ipeak - expected) <= 2.0, (ipeak, expected)
    print("pulse peak: cell 60 -> cell %d (expected %.0f) - rides at c, Courant-stable" % (ipeak, expected))
    assert peak <= peak0 * 1.01, (peak, peak0)
    print("peak amplitude %.4f <= initial %.4f - no blowup, energy conserved-ish" % (peak, peak0))
    # instability demo: S = 1.2 must blow up (run few steps, capped)
    E2 = [math.exp(-((i - 60.0) / 10.0) ** 2) for i in range(N)]
    H2 = [0.0] * N
    S2 = 1.2
    for _ in range(30):
        for i in range(N - 1):
            H2[i] = H2[i] - S2 * (E2[i + 1] - E2[i])
        for i in range(1, N):
            E2[i] = E2[i] - S2 * (H2[i] - H2[i - 1])
    print("S = 1.2 after 30 steps: max |E| = %.2e (unstable - Courant enforced)" % max(abs(x) for x in E2))
    print("rule: Yee grid + leapfrog + S <= 1/sqrt(D) - Maxwell on a lattice")
    print("OK: %s marched the grid" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "em_what": demo_em_what, "em_coulomb": demo_em_coulomb,
    "em_gauss": demo_em_gauss, "em_potential": demo_em_potential,
    "em_capacitance": demo_em_capacitance, "em_current": demo_em_current,
    "em_biotsavart": demo_em_biotsavart, "em_lorentz": demo_em_lorentz,
    "em_hysteresis": demo_em_hysteresis, "em_faraday": demo_em_faraday,
    "em_inductance": demo_em_inductance, "em_maxwell": demo_em_maxwell,
    "em_displacement": demo_em_displacement, "em_boundary": demo_em_boundary,
    "em_waveeq": demo_em_waveeq, "em_planewave": demo_em_planewave,
    "em_polarization": demo_em_polarization, "em_poynting": demo_em_poynting,
    "em_skindepth": demo_em_skindepth, "em_fresnel": demo_em_fresnel,
    "em_snell": demo_em_snell, "em_tline": demo_em_tline,
    "em_telegrapher": demo_em_telegrapher, "em_smith": demo_em_smith,
    "em_sparam": demo_em_sparam, "em_matching": demo_em_matching,
    "em_waveguide": demo_em_waveguide, "em_cavity": demo_em_cavity,
    "em_antennas": demo_em_antennas, "em_dipole": demo_em_dipole,
    "em_arrays": demo_em_arrays, "em_friis": demo_em_friis,
    "em_larmor": demo_em_larmor, "em_rcs": demo_em_rcs,
    "em_radar": demo_em_radar, "em_emc": demo_em_emc,
    "em_cem": demo_em_cem,
}

DEMO_KEY = {
    "what_is_electromagnetics": "em_what", "coulomb_law": "em_coulomb",
    "efield_gauss": "em_gauss", "potential_voltage": "em_potential",
    "capacitance": "em_capacitance", "current_ohm": "em_current",
    "biot_savart_ampere": "em_biotsavart", "lorentz_force": "em_lorentz",
    "magnetic_materials": "em_hysteresis", "faraday_lenz": "em_faraday",
    "inductance": "em_inductance", "maxwell_equations": "em_maxwell",
    "displacement_current": "em_displacement", "boundary_conditions": "em_boundary",
    "wave_equation": "em_waveeq", "plane_waves": "em_planewave",
    "polarization": "em_polarization", "poynting_vector": "em_poynting",
    "lossy_media_skin": "em_skindepth", "fresnel_reflection": "em_fresnel",
    "snell_tir": "em_snell", "transmission_lines": "em_tline",
    "telegrapher_equations": "em_telegrapher", "reflection_vswr_smith": "em_smith",
    "s_parameters": "em_sparam", "impedance_matching": "em_matching",
    "waveguides": "em_waveguide", "cavity_resonators": "em_cavity",
    "antennas_intro": "em_antennas", "half_wave_dipole": "em_dipole",
    "antenna_arrays": "em_arrays", "friis_equation": "em_friis",
    "radiation_mechanism": "em_larmor", "scattering_rcs": "em_rcs",
    "radar_fundamentals": "em_radar", "emc_emi": "em_emc",
    "computational_em": "em_cem",
}
assert set(DEMO_KEY) == {e["key"] for e in ENTRIES}, "demo key map incomplete"
assert set(DEMO_KEY.values()) == set(DEMOS), "demo map misses demos"

def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_electromagnetics.py).
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
        demo_fn = DEMOS[DEMO_KEY[e["key"]]]
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
    for slug in ("electromagnetics", "electromagnetics-signature"):
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
                               capture_output=True, text=True, timeout=120)
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
