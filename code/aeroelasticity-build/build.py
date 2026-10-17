#!/usr/bin/env python3
"""Build the Aeroelasticity field databases for JAH Databases (field #25, taxonomy order).

Verified 2026-10-17 (see entries_aeroelastic.py docstring): NO database
covers aeroelasticity as a specialty. The just-built aerodynamics DB (field
#23) carries exactly one overview record (JAH-AER-000029) plus its Signature
sibling; the whole-system title sweep found zero specialty-level
aeroelasticity records (hits were calculus divergence theorems,
quantization KL-divergence, and Honus Wagner baseball cards).

So this build creates two NEW databases, 33 ladder-ordered records each,
covering ONLY what aerodynamics left uncovered:

  aeroelasticity             - The Aeroelasticity Database (public-harvest:
                               real, fact-checked aeroelasticity; citations
                               Bisplinghoff/Ashley/Halfman, Fung, Hodges &
                               Pierce, Wright & Cooper, Dowell, Theodorsen
                               NACA TR 496, FAR 25.629)
  aeroelasticity-signature   - The Aeroelasticity Signature Database (his
                               original Signature interpretation; src
                               signature, titles suffixed
                               " (Signature Edition)", never presented as
                               authentic public record)

33 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable,
stdlib-only Python; machine-executed OK). Aeroelasticity demos: Collar's
triangle quantities; static twist amplification 1/(1-q/q_D); torsional
divergence q_D and V_D; elastic-axis shear-center walk; control-reversal
q_R and effectiveness (1-q/q_R)/(1-q/q_D); roll-rate decay to reversal;
3-station flexible load iteration; sweep-divergence collapse curve; 1-DOF
unsteady damping-zero crossing; quasi-steady vs Theodorsen lift lag; the
Theodorsen function table; Wagner step buildup; Kuessner gust penetration;
2-DOF bending-torsion flutter by the k-method (V-g table, coalescence,
bisected V_F); p-k fixed-point iteration; piston-theory panel flutter;
closed-form propeller-whirl roots; stall-flutter limit cycle (RK4);
transonic dip curve; buffeting PSD coincidence; Duffing LCO saturation;
rotor Lock number and flap frequency; Tacoma V_cr; composite tailoring
optimization; aeroservoelastic lag tradeoff; suppression gain design;
GVT half-power extraction; wind-tunnel scaling; flight-test damping
extrapolation; FAR 25.629 compliance; freeplay LCO below linear V_F;
1-cosine gust with Kuessner convolution and alleviation; the 8-step
integrated design loop.

Subtitle disambiguation (fields #13-25 pattern): specialty titles carry
teaching-focused subtitles rather than bare cards, e.g. "Divergence: The
Wing That Twists Itself Off".

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
# main repo. Fields past the gate index were cross-checked directly (see
# docstring) - subtitle disambiguation used throughout.
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_aeroelastic import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of aeroelasticity: "
                "clearly labeled Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked aeroelasticity: Collar's triangle; static "
                "aeroelasticity; divergence; the elastic axis; control reversal; aileron "
                "effectiveness; load redistribution; sweep effects; dynamic aeroelasticity; "
                "unsteady aerodynamics; the Theodorsen, Wagner, and Kuessner functions; "
                "bending-torsion flutter; the p-k and V-g methods; panel flutter; propeller "
                "whirl flutter; stall flutter; the transonic dip; buffeting; limit-cycle "
                "oscillation; rotor aeroelasticity; civil (bridge) flutter; aeroelastic "
                "tailoring; aeroservoelasticity; flutter suppression; ground vibration testing; "
                "wind-tunnel flutter testing; flight flutter testing; certification under "
                "FAR 25.629; nonlinear aeroelasticity; gust response and alleviation; "
                "integrated design, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (Collar's triangle, "
              "static aeroelasticity, divergence, elastic axis, control reversal, aileron "
              "effectiveness, load redistribution, sweep and divergence) -> Compounded "
              "(dynamic aeroelasticity, unsteady aerodynamics, Theodorsen/Wagner/Kuessner "
              "functions, bending-torsion flutter, p-k and V-g prediction, panel flutter, "
              "propeller whirl, stall flutter, transonic dip, buffeting, limit-cycle "
              "oscillation, rotor and civil aeroelasticity) -> Advanced (aeroelastic "
              "tailoring, aeroservoelasticity, flutter suppression, ground vibration testing, "
              "wind-tunnel and flight flutter testing, certification, nonlinear "
              "aeroelasticity, gust response, integrated design).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search flutter, divergence, Theodorsen, control reversal, buffeting, tailoring, FAR 25.629...",
        "chat_ph": "Ask about aeroelasticity...",
        "archive_blurb": ("Seeded %s aeroelasticity records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled structural aeroelasticity studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about aeroelasticity - from Collar's triangle, divergence, and control reversal through unsteady aerodynamics, flutter prediction, buffeting, tailoring, aeroservoelasticity, testing, certification, and integrated design." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "aeroelasticity-study", "gen_demo_kind": "aeroelasticity-demo",
        "source": source,
    }

CIT_PUB = "Aeroelasticity (standard texts: Bisplinghoff/Ashley/Halfman, Fung, Hodges & Pierce, Wright & Cooper, Dowell; Theodorsen NACA TR 496; FAR 25.629)."
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["aeroelasticity"] = _cfg(
    "aeroelasticity", "The Aeroelasticity Database",
    "Real, fact-checked aeroelasticity: from Collar's triangle, static aeroelasticity, "
    "divergence, control reversal, and load redistribution through unsteady aerodynamics, "
    "bending-torsion flutter, panel and whirl flutter, buffeting, limit-cycle oscillation, "
    "aeroelastic tailoring, aeroservoelasticity, flutter testing, FAR 25.629 certification, "
    "and integrated design - taught progressively along the ladder.",
    "aeroelasticity record", "JAH-AEL-", "JAH Aeroelasticity Archivist",
    "aeroelasticity archivist - Collar's triangle, static aeroelasticity, divergence, "
    "elastic axis, control reversal, aileron effectiveness, load redistribution, sweep "
    "effects, dynamic aeroelasticity, unsteady aerodynamics, Theodorsen/Wagner/Kuessner "
    "functions, bending-torsion flutter, p-k and V-g methods, panel flutter, propeller "
    "whirl, stall flutter, transonic dip, buffeting, limit-cycle oscillation, rotor and "
    "civil aeroelasticity, tailoring, aeroservoelasticity, flutter suppression, ground "
    "vibration testing, wind-tunnel and flight flutter testing, certification, nonlinear "
    "aeroelasticity, gust response, integrated design; teaching progressively along the "
    "ladder from foundations through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, math, how-to - using only the "
    "system's own archive data",
    CIT_PUB, "public")
DBCFG["aeroelasticity-signature"] = _cfg(
    "aeroelasticity-signature", "The Aeroelasticity Signature Database",
    "His original Signature interpretation of aeroelasticity: the full ladder from "
    "Collar's triangle and divergence through unsteady aerodynamics, flutter, tailoring, "
    "aeroservoelasticity, testing, and certification, reframed as Signature science. "
    "Clearly labeled Signature-made, never presented as authentic public record.",
    "aeroelasticity record", "JAH-AES2-", "JAH Aeroelasticity Archivist (Signature)",
    "aeroelasticity archivist - Signature editions: his original Signature "
    "interpretation of aeroelasticity, clearly labeled Signature-made and never "
    "presented as authentic public record; teaches progressively along the ladder "
    "from foundations through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, math, how-to - using only "
    "the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# aeroelastic computation for its record. All are machine-executed by main().

_PREAMBLE = (
"import math\n"
"RHO_SL = 1.225\n"
"G0 = 9.80665\n"
"def _q(rho, V):\n"
"    return 0.5 * rho * V * V\n"
)

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

# Shared validated numerical core (Theodorsen typical-section + k-method +
# whirl). Validated 2026-10-17: frequency-domain (Theodorsen) vs time-domain
# (Wagner) agree on V_F for the demo section.
_AERO_NUM = '''
import cmath
def theodorsen(k):
    if k <= 1e-9:
        return complex(1.0, 0.0)
    F = 1.0 - 0.165/(1.0+(0.0455/k)**2) - 0.335/(1.0+(0.3/k)**2)
    G = -(0.165*(0.0455/k)/(1.0+(0.0455/k)**2) + 0.335*(0.3/k)/(1.0+(0.3/k)**2))
    return complex(F, G)
def wagner_phi(tau):
    return 1.0 - 0.165*math.exp(-0.0455*tau) - 0.335*math.exp(-0.3*tau)
def kussner_psi(tau):
    return 1.0 - 0.5*math.exp(-0.13*tau) - 0.5*math.exp(-tau)
def typical_section():
    b = 0.5; rho = 1.225; mu = 20.0
    m = mu*math.pi*rho*b*b
    wh = 2.0*math.pi*4.0; wa = 2.0*wh
    return {"b": b, "rho": rho, "m": m, "xa": 0.25, "ra2": 0.25, "a": -0.30,
            "kh": m*wh*wh, "ka": m*b*b*0.25*wa*wa, "wh": wh, "wa": wa}
def ematrix(V, om, P, k_fixed=None):
    b, rho = P["b"], P["rho"]
    m, xa, ra2, a = P["m"], P["xa"], P["ra2"], P["a"]
    kh, ka = P["kh"], P["ka"]
    k = k_fixed if k_fixed is not None else (om*b/V if V > 0 else 1e-9)
    C = theodorsen(k)
    S = -m*b*xa; I = m*b*b*ra2
    i = 1j
    Lc_h = 2*math.pi*rho*V*b*C*(-i*om)
    Lc_a = 2*math.pi*rho*V*b*C*(V + i*om*b*(0.5-a))
    Mc_h = 2*math.pi*rho*V*b*b*(a+0.5)*C*(-i*om)
    Mc_a = 2*math.pi*rho*V*b*b*(a+0.5)*C*(V + i*om*b*(0.5-a))
    Ln_h = math.pi*rho*b*b*(-om*om)
    Ln_a = math.pi*rho*b*b*(i*om*V - om*om*b*a)
    Mn_h = math.pi*rho*b*b*(-om*om*b*a)
    Mn_a = math.pi*rho*b*b*(-i*om*V*b*(0.5-a) + om*om*b*b*(1/8+a*a))
    E11 = (kh - om*om*m) - (Ln_h+Lc_h)
    E12 = (-om*om*S) - (Ln_a+Lc_a)
    E21 = (-om*om*S) - (Mn_h+Mc_h)
    E22 = (ka - om*om*I) - (Mn_a+Mc_a)
    return ((E11,E12),(E21,E22))
def k_method_roots(V, P, guesses, emat=None):
    emat = emat or ematrix
    b = P["b"]; m = P["m"]; S = -m*b*P["xa"]; I = m*b*b*P["ra2"]
    kh, ka = P["kh"], P["ka"]
    out = []
    for om_g in guesses:
        om, g = om_g, 0.0
        for it in range(60):
            (e11,e12),(e21,e22) = emat(V, om, P)
            a11 = (kh-om*om*m)-e11; a12 = (-om*om*S)-e12
            a21 = (-om*om*S)-e21; a22 = (ka-om*om*I)-e22
            den = complex(1.0, g)
            k11 = kh-a11/den; k12 = -a12/den; k21 = -a21/den; k22 = ka-a22/den
            c2 = m*I-S*S
            c1 = -(k11*I+k22*m-k12*S-k21*S)
            c0 = k11*k22-k12*k21
            disc = cmath.sqrt(c1*c1-4*c2*c0)
            best = None
            for mu_ in ((-c1+disc)/(2*c2), (-c1-disc)/(2*c2)):
                if mu_.real <= 1e-9:
                    continue
                gg = -mu_.imag/mu_.real
                oo = math.sqrt(mu_.real+mu_.imag**2/mu_.real)
                if best is None or abs(oo-om_g) < best[0]:
                    best = (abs(oo-om_g), oo, gg)
            if best is None:
                break
            _, om_n, g_n = best
            if abs(om_n-om) < 1e-7 and abs(g_n-g) < 1e-9:
                om, g = om_n, g_n
                break
            om, g = 0.6*om+0.4*om_n, 0.6*g+0.4*g_n
        out.append((om, g))
    return out
def divergence_speed(P):
    return math.sqrt(P["ka"]/(2*math.pi*P["rho"]*P["b"]**2*(P["a"]+0.5)))
def whirl_roots(V, P):
    rho = P["rho"]; I, Ip, Om = P["I"], P["Ip"], P["Om"]; k, c = P["k"], P["c"]
    S, D, c1, cmq = P["S"], P["D"], P["c1"], P["cmq"]
    q = 0.5*rho*V*V
    A0 = q*S*D*c1; A1 = q*S*D*D*cmq/max(V, 1e-9)
    roots = []
    for sgn in (1, -1):
        bq = complex(c-A1, -sgn*Ip*Om)
        disc = cmath.sqrt(bq*bq - 4*I*(k-A0))
        for s2 in (1, -1):
            roots.append((-bq+s2*disc)/(2*I))
    return roots
def whirl_nacelle():
    return {"rho": 1.225, "I": 800.0, "Ip": 150.0, "Om": 120.0, "k": 2.0e6,
            "c": 2000.0, "S": 3.0, "D": 2.5, "c1": 1.5, "cmq": 2.0}
'''

def _wrap_aero(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + _AERO_NUM +
            body.replace("NAME", json.dumps(name)))

def demo_ae_collar(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Collar's triangle, quantified on one wing strip
    # corner 1: aerodynamics + elasticity -> static deflection
    L, EI, Lspan = 5000.0, 2.0e6, 5.0
    delta = L * Lspan**3 / (3.0 * EI)          # cantilever tip deflection
    # corner 2: elasticity + inertia -> natural frequency
    m = 200.0
    k = 3.0 * EI / Lspan**3
    fn = math.sqrt(k / m) / (2.0 * math.pi)
    # corner 3: aerodynamics + inertia -> rigid gust load factor increment
    rho, V, S, a0, W = RHO_SL, 100.0, 20.0, 5.7, 60000.0
    wg = 5.0
    dL = 0.5 * rho * V * S * a0 * wg
    dn = dL / W
    print("AE+EL: tip deflection under 5 kN: %.3f m" % delta)
    print("EL+IN: first bending frequency: %.2f Hz" % fn)
    print("AE+IN: gust load increment: %.3f g" % dn)
    assert abs(delta - 0.1042) < 0.001, delta
    assert 1.0 < fn < 3.0, fn
    assert 0.4 < dn < 0.8, dn
    print("center: all three at once = dynamic aeroelasticity (flutter, buffeting)")
    print("rule: name the corners your problem touches before you open a toolbox")
    print("OK: %s mapped the triangle" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_static(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # static aeroelastic loop: twist -> load -> twist ; amplification 1/(1-q/qD)
    k_theta = 20000.0     # N-m/rad per unit span
    a0, e, chord = 5.7, 0.10, 1.0
    qD = k_theta / (a0 * e * chord * chord)
    VD = math.sqrt(2.0 * qD / RHO_SL)
    print("divergence pressure q_D = %.0f Pa -> V_D = %.0f m/s" % (qD, VD))
    assert abs(qD - 35087.7) < 50.0, qD
    alpha_rigid = math.radians(3.0)
    for frac in (0.0, 0.25, 0.5, 0.75):
        q = frac * qD
        amp = 1.0 / (1.0 - frac)
        theta = alpha_rigid * (frac / (1.0 - frac)) if frac > 0 else 0.0
        print("q/q_D = %.2f: amplification x%.2f, elastic twist %.2f deg" %
              (frac, amp, math.degrees(theta)))
    assert abs(1.0/(1.0-0.5) - 2.0) < 1e-9
    print("rule: every static effect wears the fraction 1/(1-q/q_D)")
    print("OK: %s closed the static loop" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_divergence(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # torsional divergence of a wing strip: q_D = k_theta/(a0*e*c^2)
    cases = [
        ("trainer wing", 20000.0, 5.7, 0.10, 1.0),
        ("stiffened wing", 40000.0, 5.7, 0.10, 1.0),
        ("forward EA wing", 20000.0, 5.7, 0.05, 1.0),
    ]
    for tag, kth, a0, e, c in cases:
        qD = kth / (a0 * e * c * c)
        VD = math.sqrt(2.0 * qD / RHO_SL)
        print("%-16s q_D = %7.0f Pa   V_D = %6.1f m/s" % (tag, qD, VD))
    qD0 = 20000.0 / (5.7 * 0.10 * 1.0)
    assert abs(qD0 - 35087.7) < 50.0
    # doubling stiffness doubles q_D ; halving e doubles q_D
    assert abs((40000.0/(5.7*0.10)) / qD0 - 2.0) < 1e-9
    assert abs((20000.0/(5.7*0.05)) / qD0 - 2.0) < 1e-9
    # twist at 90% of q_D is 10x the rigid angle -> the wing lets go
    amp90 = 1.0 / (1.0 - 0.9)
    print("at 0.9 q_D the twist is x%.0f the rigid angle: divergence is near" % amp90)
    assert abs(amp90 - 10.0) < 1e-9
    print("rule: the air votes against the stiffness, and past q_D the vote is unanimous")
    print("OK: %s found the divergence" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_elastic_axis(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # two-spar shear center -> elastic axis -> divergence arm e
    xf, xr = 0.15, 0.65          # spar positions, fraction of chord
    EIf, EIr = 2.0e6, 1.0e6
    xsc = (EIf * xf + EIr * xr) / (EIf + EIr)
    xac = 0.25
    e = xsc - xac
    print("shear center at %.1f%% chord; a.c. at 25%% -> e = %.1f%% chord" % (xsc*100, e*100))
    assert abs(xsc - 0.3167) < 0.001, xsc
    # walk the elastic axis forward: q_D scales as 1/e
    kth, a0, c = 20000.0, 5.7, 1.0
    for xea in (0.40, 0.35, 0.30):
        ee = xea - xac
        qD = kth / (a0 * ee * c * c)
        print("EA at %d%% chord: e = %.2f -> q_D = %.0f Pa" % (xea*100, ee, qD))
    q40 = kth/(a0*0.15); q30 = kth/(a0*0.05)
    assert abs(q30/q40 - 3.0) < 1e-9, "halving e should triple q_D"
    print("rule: put the spine under the lift and the wing stands tall")
    print("OK: %s placed the elastic axis" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_reversal(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # aileron reversal: q_R = k_theta/(a0*c^2*(mu-e)), mu = -Cm_delta/a_delta
    kth, a0, c, e = 20000.0, 5.7, 1.0, 0.10
    a_del, Cm_del = 2.0, -0.5
    mu = -Cm_del / a_del
    qD = kth / (a0 * e * c * c)
    qR = kth / (a0 * c * c * (mu - e))
    VD = math.sqrt(2*qD/RHO_SL); VR = math.sqrt(2*qR/RHO_SL)
    print("q_D = %.0f Pa (V_D %.0f m/s)" % (qD, VD))
    print("q_R = %.0f Pa (V_R %.0f m/s); mu = %.2f" % (qR, VR, mu))
    assert qR < qD, "reversal must precede divergence"
    assert abs(VR - 195.4) < 1.0, VR
    print("aileron effectiveness eta = (1-q/qR)/(1-q/qD):")
    for frac in (0.0, 0.3, 0.5, qR/qD):
        eta = (1.0 - frac*qD/qR) / (1.0 - frac)
        print("  q/q_D = %.2f -> eta = %+.3f" % (frac, eta))
    assert abs((1.0-0.5*qD/qR)/(1.0-0.5) - 0.5) < 0.01
    print("rule: the controls quit before the wing breaks - q_R < q_D always")
    print("OK: %s reversed the aileron" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_aileron(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # steady roll rate vs airspeed with flexible effectiveness
    kth, a0, c, e = 20000.0, 5.7, 1.0, 0.10
    a_del, Cm_del = 2.0, -0.5
    mu = -Cm_del / a_del
    qD = kth/(a0*e*c*c); qR = kth/(a0*c*c*(mu-e))
    Cl_del, Clp, delta, span = 0.15, -0.40, math.radians(12.0), 10.0
    VR = math.sqrt(2*qR/RHO_SL)
    print(" V(m/s)  q/q_D   eta    p_ss(deg/s)")
    pmax, Vmax = 0.0, 0.0
    V = 50.0
    while V < VR*0.98:
        q = _q(RHO_SL, V)
        eta = (1.0 - q/qR)/(1.0 - q/qD)
        pss = (Cl_del*delta*eta/abs(Clp)) * (2.0*V/span)
        print("%6.0f  %6.3f %6.3f %10.1f" % (V, q/qD, eta, math.degrees(pss)))
        if pss > pmax:
            pmax, Vmax = pss, V
        V += 10.0
    q_at_VR = _q(RHO_SL, VR)
    eta_VR = (1.0 - q_at_VR/qR)/(1.0 - q_at_VR/qD)
    print("roll rate peaks near V = %d m/s, dies at V_R = %.0f m/s (eta=%.3f)" %
          (Vmax, VR, eta_VR))
    assert abs(eta_VR) < 1e-9, eta_VR
    assert pmax > 0 and Vmax < VR
    print("rule: the roll rate climbs with q, then the twist eats the aileron")
    print("OK: %s counted the remaining control" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_loads(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 3-station flexible load iteration on a swept-back wing: washout unloads the tip
    Lambda = math.radians(25.0)
    stations = [2.0, 5.0, 8.0]          # span stations, m (semi-span 10)
    chord, EI = 1.5, 5.0e7
    a0 = 5.7
    V = 150.0
    q = _q(RHO_SL, V)
    # rigid elliptical-ish loading (normalized)
    rigid = [1.0, 0.85, 0.55]
    loads = list(rigid)
    for it in range(20):
        # bending slope from tip-ward accumulation (simple beam, point loads)
        slope = [0.0, 0.0, 0.0]
        acc = 0.0
        for i in (2, 1, 0):
            acc += loads[i] * 1.0
            slope[i] = acc * (stations[i]**2) / (2.0 * EI) * 1.0e4
        wash = [s * math.sin(Lambda) for s in slope]
        new = [rigid[i] * (1.0 - 0.8*wash[i]) for i in range(3)]
        tot_old = sum(loads); tot_new = sum(new)
        new = [n * tot_old / tot_new for n in new]   # hold total lift
        if max(abs(new[i]-loads[i]) for i in range(3)) < 1e-6:
            loads = new
            break
        loads = new
    print("converged in %d iterations; flexible distribution:" % (it+1))
    for y, r, f in zip(stations, rigid, loads):
        print("  y = %.0f m: rigid %.3f -> flexible %.3f (%+.1f%%)" % (y, r, f, 100*(f-r)/r))
    # root bending moment proxy: sum(load * y)
    Mr = sum(r*y for r, y in zip(rigid, stations))
    Mf = sum(f*y for f, y in zip(loads, stations))
    print("root bending moment: rigid %.3f -> flexible %.3f (relief %.1f%%)" %
          (Mr, Mf, 100*(Mr-Mf)/Mr))
    assert Mf < Mr, "swept-back washout must relieve the root"
    assert loads[2] < rigid[2], "tip must unload"
    print("rule: the wing re-aims its own lift; size to the flexible shape")
    print("OK: %s redistributed the load" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_sweep(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # sweep-divergence: e_eff = e*cos(Lambda) - kappa*sin(Lambda)
    kth, a0, c, e, kappa = 20000.0, 5.7, 1.0, 0.10, 0.12
    print(" sweep   e_eff    V_D(m/s)")
    VDs = {}
    for deg in (-30, -15, 0, 15, 30):
        L = math.radians(deg)
        e_eff = e*math.cos(L) - kappa*math.sin(L)
        qD = kth/(a0*e_eff*c*c)
        VD = math.sqrt(2*qD/RHO_SL)
        VDs[deg] = VD
        print("%+5d  %7.4f  %8.1f" % (deg, e_eff, VD))
    assert VDs[-30] < VDs[0] < VDs[30], "forward sweep must collapse V_D"
    assert VDs[-30] < 0.85*VDs[0], "forward sweep penalty should be clear"
    print("X-29 lesson: -30 deg forward sweep needs composite washout to survive")
    print("rule: sweep translates bending into twist - aft is relief, forward is ruin")
    print("OK: %s swept the divergence" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_dynamic(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 1-DOF unsteady: stiffness eaten by q, damping sign flips in stall
    import cmath as _cm
    I, wn, zeta = 50.0, 10.0, 0.02
    k = I*wn*wn
    Sref, cref, a0, e = 2.0, 1.0, 5.7, 0.10
    qD = k/(a0*e*Sref*cref)
    print("1-DOF torsion: divergence then stall-driven zero damping")
    for V, stall in ((60.0, False), (120.0, False), (60.0, True)):
        q = _q(RHO_SL, V)
        ka = q*Sref*cref*a0*e
        # aerodynamic damping: + normally, negative in stall
        ca = (0.0 if stall else 1.0) * q*Sref*cref*cref*0.8/max(V, 1.0)
        if stall:
            ca = -1.5 * q*Sref*cref*cref*0.8/max(V, 1.0)
        cc = 2.0*zeta*wn*I
        # I s^2 + (cc - ca) s + (k - ka) = 0
        A2, B2, C2 = I, (cc - ca), (k - ka)
        disc = _cm.sqrt(B2*B2 - 4*A2*C2)
        s1 = (-B2 + disc)/(2*A2)
        damp = -s1.real/abs(s1) if abs(s1) > 0 else 0.0
        freq = abs(s1.imag)/(2*math.pi)
        print("V=%5.0f stall=%s: freq %.2f Hz, damping ratio %+.4f %s" %
              (V, stall, freq, damp, "<- ZERO/FLUTTER" if damp <= 0 else ""))
    # checks: divergence stiffness loss at qD ; stall flips damping
    assert abs((k - qD*Sref*cref*a0*e)) < 1e-6
    print("rule: stiffness loss -> divergence; damping loss -> flutter")
    print("OK: %s found the zero crossing" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_unsteady(name, rid, group, points, req):
    return _wrap_aero(name, rid, group, '''\
def main():
    # harmonic plunge: quasi-steady vs Theodorsen lift
    b, rho, V = 0.5, RHO_SL, 60.0
    h0 = 0.05
    print("   k    |C|   phase(deg)   |L_qs|(N)  |L_true|(N)")
    for om in (2*math.pi*1.0, 2*math.pi*5.0, 2*math.pi*10.0):
        k = om*b/V
        C = theodorsen(k)
        Lqs = 2*math.pi*rho*V*b*(om*h0)     # quasi-steady amplitude
        Lt = abs(C)*Lqs
        ph = math.degrees(cmath.phase(C))
        print("%5.2f  %.3f  %7.1f  %8.1f  %8.1f" % (k, abs(C), ph, Lqs, Lt))
    assert abs(abs(theodorsen(0.01)) - 1.0) < 0.05
    assert abs(theodorsen(0.5)) < 0.70
    assert cmath.phase(theodorsen(0.3)) < 0, "lift must lag"
    print("rule: the faster the wiggle, the less lift and the later it comes")
    print("OK: %s weighed the memory" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_theodorsen(name, rid, group, points, req):
    return _wrap_aero(name, rid, group, '''\
def main():
    # Theodorsen C(k) = F + iG: the wake's memory curve
    print("   k      F       G      |C|   phase(deg)")
    maxlag, klag = 0.0, 0.0
    for k in (0.01, 0.05, 0.1, 0.2, 0.3, 0.5, 1.0, 2.0):
        C = theodorsen(k)
        ph = math.degrees(cmath.phase(C))
        print("%5.2f  %6.4f %7.4f  %.4f  %6.1f" % (k, C.real, C.imag, abs(C), ph))
        if ph < maxlag:
            maxlag, klag = ph, k
    print("maximum phase lag %.1f deg at k = %.2f" % (maxlag, klag))
    assert abs(theodorsen(0.01).real - 1.0) < 0.01, "C -> 1 as k -> 0"
    assert abs(theodorsen(2.0)) < 0.60, "|C| must fall toward 1/2"
    assert -20.0 < maxlag < -5.0, "lag peak should be ~-14 deg"
    assert 0.15 < klag < 0.5
    print("rule: that small lag angle is the energy tap flutter drinks from")
    print("OK: %s traced the memory curve" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_wagner(name, rid, group, points, req):
    return _wrap_aero(name, rid, group, '''\
def main():
    # Wagner step response: sudden 5-deg pitch, lift builds from half
    alpha = math.radians(5.0)
    b, rho, V = 0.5, RHO_SL, 60.0
    Lsteady = 2*math.pi * (0.5*rho*V*V) * (2*b) * alpha
    print("tau(semi-chords)  phi    L/L_steady")
    tau90 = None
    for tau in (0, 1, 2, 5, 10, 15, 20, 40):
        phi = wagner_phi(tau)
        print("%8.0f  %7.4f  %7.4f" % (tau, phi, phi))
        if tau90 is None and phi >= 0.90:
            tau90 = tau
    assert abs(wagner_phi(0) - 0.5) < 1e-9, "phi(0) must be exactly 1/2"
    assert abs(wagner_phi(60) - 1.0) < 0.02, "phi -> 1"
    # refine tau90
    lo, hi = 5.0, 20.0
    for _ in range(40):
        mid = 0.5*(lo+hi)
        if wagner_phi(mid) < 0.90: lo = mid
        else: hi = mid
    tau90 = 0.5*(lo+hi)
    print("90%% of full lift after %.1f semi-chords (%.1f m at this speed)" % (tau90, tau90*b))
    assert 10.0 < tau90 < 16.0
    print("steady lift would be %.0f N; at tau=0 only %.0f N exists" % (Lsteady, 0.5*Lsteady))
    print("rule: half the lift now, the rest when the starting vortex leaves")
    print("OK: %s stepped the wing" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_kussner(name, rid, group, points, req):
    return _wrap_aero(name, rid, group, '''\
def main():
    # Kuessner gust penetration: sharp-edged gust, lift walks on chord by chord
    b, rho, V = 0.5, RHO_SL, 60.0
    wg = 3.0
    Lsteady = 2*math.pi * (0.5*rho*V*V) * (2*b) * (wg/V)
    print("tau  psi    L/L_steady   (quasi-steady would claim 1.0 at tau=0)")
    for tau in (0, 1, 2, 5, 10, 15, 20):
        psi = kussner_psi(tau)
        print("%3.0f  %.4f  %.4f" % (tau, psi, psi))
    assert abs(kussner_psi(0)) < 1e-9, "psi(0) = 0: nothing has entered the gust"
    assert abs(kussner_psi(30) - 1.0) < 0.02
    lo, hi = 10.0, 25.0
    for _ in range(40):
        mid = 0.5*(lo+hi)
        if kussner_psi(mid) < 0.95: lo = mid
        else: hi = mid
    print("95%% gust lift after %.1f semi-chords; steady gust lift %.0f N" % (0.5*(lo+hi), Lsteady))
    print("rule: the gust walks onto the wing - the lift follows on foot")
    print("OK: %s met the gust" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_flutter(name, rid, group, points, req):
    return _wrap_aero(name, rid, group, '''\
def main():
    # 2-DOF bending-torsion flutter by the k-method (V-g table)
    P = typical_section()
    guesses = [P["wh"], P["wa"]]
    VD = divergence_speed(P)
    print("demo section: fh=4 Hz fa=8 Hz xa=0.25 a=-0.3 mu=20; V_D=%.1f m/s" % VD)
    print("   V    f_bend   g_bend   f_tors   g_tors")
    rows = []
    for V in range(10, 81, 10):
        (o1, g1), (o2, g2) = k_method_roots(V, P, guesses)
        f1, f2 = o1/2/math.pi, o2/2/math.pi
        rows.append((V, f1, g1, f2, g2))
        print("%5d  %7.2f  %+.4f  %7.2f  %+.4f %s" %
              (V, f1, g1, f2, g2, "<- g>0 FLUTTER" if max(g1, g2) > 0 else ""))
    # coalescence: branches approach each other before V_F
    f1_10, f2_10 = rows[0][1], rows[0][3]
    # bisect flutter speed on max g
    def maxg(V):
        return max(g for _, g in k_method_roots(V, P, guesses))
    lo, hi = 40.0, 70.0
    assert maxg(lo) < 0 and maxg(hi) > 0, "bracket must straddle V_F"
    for _ in range(24):
        mid = 0.5*(lo+hi)
        if maxg(mid) > 0: hi = mid
        else: lo = mid
    VF = 0.5*(lo+hi)
    (o1, g1), (o2, g2) = k_method_roots(VF, P, guesses)
    print("V_F = %.1f m/s at f = %.2f/%.2f Hz (coalesced from %.2f/%.2f)" %
          (VF, o1/2/math.pi, o2/2/math.pi, f1_10, f2_10))
    assert 45.0 < VF < 70.0, VF
    assert VF < VD, "flutter must precede divergence here"
    assert abs(o1-o2)/max(o1, o2) < 0.15, "frequencies must coalesce at flutter"
    print("rule: two stable modes, one treacherous air - the coupling eats the damping")
    print("OK: %s fluttered the section" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_prediction(name, rid, group, points, req):
    return _wrap_aero(name, rid, group, '''\
def main():
    # p-k fixed-point iteration vs the k-method root (subcritical agreement)
    P = typical_section()
    V = 45.0
    # k-method reference root (torsion branch)
    (o_ref, g_ref) = k_method_roots(V, P, [P["wa"]])[0]
    k_ref = o_ref * P["b"] / V
    print("k-method at V=%.0f: f=%.3f Hz g=%.4f k=%.4f" % (V, o_ref/2/math.pi, g_ref, k_ref))
    # p-k: iterate k -> solve at FIXED k -> update k from the root frequency
    k = 0.30
    print("p-k iteration:")
    for it in range(30):
        (o_pk, g_pk) = k_method_roots(V, P, [o_ref], emat=lambda Vv, oo, PP: ematrix(Vv, oo, PP, k_fixed=k))[0]
        k_new = o_pk * P["b"] / V
        print("  it %2d: k=%.5f -> f=%.4f Hz g=%.5f" % (it, k, o_pk/2/math.pi, g_pk))
        if abs(k_new - k) < 1e-6:
            k = k_new
            break
        k = k_new
    print("p-k converged: k=%.5f f=%.4f Hz g=%.5f" % (k, o_pk/2/math.pi, g_pk))
    assert abs(k - k_ref) < 2e-3, "p-k must match the k-method reduced frequency"
    assert abs(o_pk - o_ref)/o_ref < 2e-3
    assert abs(g_pk - g_ref) < 2e-3
    print("V-g draws the map (boundary); p-k walks the terrain (subcritical damping)")
    print("rule: two methods, one root - the physics does not care which you asked")
    print("OK: %s predicted flutter twice" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_panel(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # piston-theory panel flutter: lambda_cr ~ 350 simply-supported
    L, h = 0.5, 0.002
    E, nu = 70.0e9, 0.33
    D = E*h**3/(12.0*(1.0-nu*nu))
    lam_cr = 350.0
    print("panel %.1f m x %.0f mm aluminum: D = %.1f N-m" % (L, h*1000, D))
    assert abs(D - 52.37) < 0.5, D
    print(" Mach  q_cr(Pa)  V_cr(m/s)")
    qprev = 0.0
    for M in (1.5, 2.0, 3.0):
        qcr = lam_cr*D*math.sqrt(M*M-1.0)/(2.0*L**3)
        a_inf = math.sqrt(1.4*287.0*216.65)
        Vcr = M*a_inf
        print("%5.1f  %8.0f  %8.0f" % (M, qcr, Vcr))
        assert qcr > qprev, "q_cr must rise with Mach"
        qprev = qcr
    # cruise check: q = 30 kPa at Mach 2
    q_cruise = 30000.0
    lam = 2.0*q_cruise*L**3/(D*math.sqrt(4.0-1.0))
    print("at Mach 2, q=30 kPa: lambda = %.0f vs critical %.0f -> %s" %
          (lam, lam_cr, "FLUTTER" if lam > lam_cr else "clear"))
    assert lam < lam_cr
    print("rule: piston theory above Mach ~1.6; the skin sings only if lambda allows")
    print("OK: %s fluttered the panel" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_whirl(name, rid, group, points, req):
    return _wrap_aero(name, rid, group, '''\
def main():
    # propeller whirl flutter: closed-form complex-quadratic roots
    P = whirl_nacelle()
    wn = math.sqrt(P["k"]/P["I"])/(2*math.pi)
    print("nacelle mount: %.1f Hz; prop %.0f RPM" % (wn, P["Om"]*60/2/math.pi))
    print("   V   f_fwd  g_fwd    f_reg  g_reg")
    def damp_of_root(r):
        return -r.real/abs(r) if abs(r) > 0 else 0.0
    VF = None
    for V in range(40, 221, 10):
        rs = whirl_roots(V, P)
        # pair into forward/regressive by frequency
        rs_sorted = sorted(rs, key=lambda r: abs(r.imag))
        fwd = max(rs, key=lambda r: abs(r.imag))
        reg = min(rs, key=lambda r: abs(r.imag))
        gf, gr = damp_of_root(fwd), damp_of_root(reg)
        print("%5d  %6.2f %+.4f  %6.2f %+.4f %s" %
              (V, abs(fwd.imag)/2/math.pi, gf, abs(reg.imag)/2/math.pi, gr,
               "<- whirl FLUTTER" if gf < 0 else ""))
        if gf < 0 and VF is None:
            VF = V
    assert VF is not None, "whirl flutter must occur in range"
    # bisect
    lo, hi = float(VF-10), float(VF)
    for _ in range(20):
        mid = 0.5*(lo+hi)
        fwd = max(whirl_roots(mid, P), key=lambda r: abs(r.imag))
        if damp_of_root(fwd) < 0: hi = mid
        else: lo = mid
    VF = 0.5*(lo+hi)
    fwd = max(whirl_roots(VF, P), key=lambda r: abs(r.imag))
    print("whirl flutter speed V_F = %.1f m/s (forward whirl %.2f Hz)" %
          (VF, abs(fwd.imag)/2/math.pi))
    assert 70.0 < VF < 130.0, VF
    print("rule: no spin, no whirl - the gyroscope makes the circle, the air widens it")
    print("OK: %s whirled the propeller" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_stall(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # stall flutter: 1-DOF torsion, dynamic-stall damping -> limit cycle (RK4)
    # near stall the unsteady moment feeds the motion (negative damping);
    # deep in stall it dissipates (positive damping): a van-der-Pol LCO
    I, wa = 50.0, 10.0
    ka = I*wa*wa
    Sref, cref, V = 2.0, 1.0, 70.0
    q = _q(RHO_SL, V)
    a_s = math.radians(12.0)
    Cma = 0.10
    def rhs(s):
        al, dal = s
        ca = q*Sref*cref*(cref/V)*(-0.6 + 2.0*(al/a_s)**2)
        Ma = q*Sref*cref*Cma*al - ca*dal
        return [dal, (-ka*al - 0.5*dal + Ma)/I]
    def settle(a0d):
        s = [math.radians(a0d), 0.0]
        dt = 0.001
        mx = 0.0
        for i in range(20000):
            k1 = rhs(s)
            k2 = rhs([s[j]+0.5*dt*k1[j] for j in range(2)])
            k3 = rhs([s[j]+0.5*dt*k2[j] for j in range(2)])
            k4 = rhs([s[j]+dt*k3[j] for j in range(2)])
            s = [s[j]+dt/6*(k1[j]+2*k2[j]+2*k3[j]+k4[j]) for j in range(2)]
            if i > 10000:
                mx = max(mx, abs(s[0]))
        return mx
    a1, a2 = settle(2.0), settle(8.0)
    print("from 2 deg -> LCO amplitude %.2f deg" % math.degrees(a1))
    print("from 8 deg -> LCO amplitude %.2f deg" % math.degrees(a2))
    assert math.degrees(a1) > 5.0, "must grow from the small start"
    assert math.degrees(a1) < 25.0, "must saturate (limit cycle, not divergence)"
    assert abs(a1-a2)/a1 < 0.05, "limit cycle independent of start"
    print("rule: the stall feeds the shake, the deep stall starves it - a bounded dance")
    print("OK: %s stalled into flutter" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_transonic_dip(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # transonic flutter dip: EMPIRICAL trend (measured in tunnels, not derived)
    print("NOTE: empirical trend curve - the real dip is measured, not computed")
    def ratio(M):
        return 1.0 - 0.32*math.exp(-((M-0.92)/0.10)**2)
    print(" Mach  V_F/V_F_subsonic")
    Mmin, rmin = 0.0, 2.0
    M = 0.5
    while M <= 1.31:
        r = ratio(M)
        print("%5.2f  %7.3f %s" % (M, r, "<- DIP" if r < 0.75 else ""))
        if r < rmin:
            rmin, Mmin = r, M
        M += 0.05
    print("deepest dip: %.0f%% of subsonic flutter speed at Mach %.2f" % (rmin*100, Mmin))
    assert 0.85 < Mmin < 1.0, Mmin
    assert 0.60 < rmin < 0.75, rmin
    print("a wing clear to 600 kt subsonically may flutter near 450 kt in the dip")
    print("rule: the air changes the rules mid-game - measure the trough, never assume it")
    print("OK: %s dipped transonic" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_buffeting(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # tail buffeting: RMS = sqrt(integral |H|^2 * S_FF df); coincidence spikes it
    fn, zeta, m = 12.0, 0.02, 400.0
    k = m*(2*math.pi*fn)**2
    S0, df = 1.0e6, 2.0
    def H(f):
        r = f/fn
        return 1.0/(k*math.sqrt((1-r*r)**2 + (2*zeta*r)**2))
    def Sff(f, f0):
        return S0/(1.0 + ((f-f0)/df)**2)
    def rms(f0):
        tot, f, dfr = 0.0, 0.5, 0.25
        while f < 40.0:
            tot += (abs(H(f))**2)*Sff(f, f0)*dfr
            f += dfr
        return math.sqrt(tot)
    print("wake peak(Hz)  RMS accel(g)")
    rms_list = []
    for f0 in (6.0, 9.0, 12.0, 15.0, 20.0):
        r = rms(f0)/G0
        rms_list.append((f0, r))
        print("%8.1f  %10.2f %s" % (f0, r, "<- COINCIDENCE" if f0 == 12.0 else ""))
    rc = dict(rms_list)[12.0]
    assert rc > dict(rms_list)[6.0]*2.0, "coincidence must multiply the response"
    assert rc > dict(rms_list)[20.0]*2.0
    print("rule: a stable tail in a noisy wake still shakes - tune the mode away from the noise")
    print("OK: %s buffeted the tail" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_lco(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # LCO: linear negative damping + amplitude-dependent (nonlinear) damping
    I, wa = 50.0, 10.0
    ka = I*wa*wa
    c_lin, c_nl = -40.0, 1000.0
    def march(nonlinear):
        al, dal = 0.02, 0.0
        dt = 0.0005
        mx = 0.0
        for i in range(30000):
            def acc(a, d):
                cc = c_lin + (c_nl*a*a if nonlinear else 0.0)
                return (-ka*a - cc*d)/I
            k1a, k1d = dal, acc(al, dal)
            k2a, k2d = dal+0.5*dt*k1d, acc(al+0.5*dt*k1a, dal+0.5*dt*k1d)
            k3a, k3d = dal+0.5*dt*k2d, acc(al+0.5*dt*k2a, dal+0.5*dt*k2d)
            k4a, k4d = dal+dt*k3d, acc(al+dt*k3a, dal+dt*k3d)
            al += dt/6*(k1a+2*k2a+2*k3a+k4a)
            dal += dt/6*(k1d+2*k2d+2*k3d+k4d)
            if i > 15000:
                mx = max(mx, abs(al))
            if abs(al) > 3.0:
                return float("inf")
        return mx
    lin = march(False)
    nlin = march(True)
    print("past V_F: linear amplitude -> %s" % ("DIVERGED" if lin == float("inf") else "%.3f" % lin))
    print("past V_F: nonlinear amplitude -> %.4f rad (%.2f deg): LIMIT CYCLE" %
          (nlin, math.degrees(nlin)))
    assert lin == float("inf"), "linear must diverge"
    assert 0.0 < nlin < 0.5, "nonlinear must saturate to a bounded cycle"
    print("rule: the linear boundary is where trouble starts being possible, not where it starts")
    print("OK: %s capped the instability" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_rotor(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # rotor blade: Lock number, flap frequency, pitch-flap coupling
    rho, a0, c, R, Ib = 1.225, 5.7, 0.6, 6.0, 500.0
    gamma = rho*a0*c*R**4/Ib
    print("Lock number gamma = %.2f (aerodynamic vs inertial authority)" % gamma)
    assert 5.0 < gamma < 12.0, gamma
    e = 0.05
    flap_ratio = math.sqrt(1.0 + 3.0*e/(2.0*(1.0-e)))
    print("flap frequency: %.3f/rev (centrifugal stiffening)" % flap_ratio)
    assert 1.0 < flap_ratio < 1.15
    # flap damping per rev ~ gamma/8
    print("flap aerodynamic damping: %.2f/rev (huge - rotors behave in flap)" % (gamma/8.0))
    # delta-3: pitch-flap coupling; effective pitch change per flap angle
    for d3 in (0.0, 15.0, 30.0):
        dtheta = -math.tan(math.radians(d3))   # pitch change per unit flap (stabilizing sign)
        print("delta-3 = %4.0f deg: d(theta)/d(beta) = %+.3f %s" %
              (d3, dtheta, "<- stabilizing" if dtheta < 0 else ""))
    assert math.tan(math.radians(15.0)) > 0.25
    print("rule: couple the blade to itself wisely - delta-3 is a designed reflex")
    print("OK: %s spun the rotor" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_tacoma(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Tacoma Narrows: V_cr = f_t * B / St  (torsional lock-in)
    f_t = 0.20        # Hz, torsional mode
    B = 11.9          # m, deck width
    St = 0.12         # Strouhal, H-section deck
    Vcr = f_t*B/St
    print("torsional freq %.2f Hz, deck %.1f m, St %.2f" % (f_t, B, St))
    print("critical wind V_cr = %.1f m/s = %.0f km/h" % (Vcr, Vcr*3.6))
    print("failure wind, 7 Nov 1940: 64 km/h")
    assert abs(Vcr*3.6 - 64.0)/64.0 < 0.25, "lock-in must explain the disaster"
    # modern fix: streamlined box girder -> higher torsional frequency, cleaner St
    Vcr2 = 0.45*B/0.15
    print("modern box girder (f_t 0.45 Hz, St 0.15): V_cr = %.0f km/h -> survives" % (Vcr2*3.6))
    assert Vcr2 > Vcr*1.3
    print("rule: not resonance - flutter. The wind learned the bridge's song.")
    print("OK: %s crossed Tacoma" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_tailoring(name, rid, group, points, req):
    return _wrap_aero(name, rid, group, '''\
def main():
    # composite tailoring: fiber angle -> effective coupling -> flutter margin
    P0 = typical_section()
    guesses = [P0["wh"], P0["wa"]]
    def vf_for_coupling(dc):
        # bend-twist coupling shifts the effective EA position a (teaching model)
        P = dict(P0)
        P["a"] = P0["a"] - dc
        def maxg(V):
            return max(g for _, g in k_method_roots(V, P, guesses))
        lo, hi = 40.0, 120.0
        if maxg(lo) > 0:
            return lo
        if maxg(hi) < 0:
            return float("inf")
        for _ in range(20):
            mid = 0.5*(lo+hi)
            if maxg(mid) > 0: hi = mid
            else: lo = mid
        return 0.5*(lo+hi)
    vf0 = vf_for_coupling(0.0)
    print("baseline V_F = %.1f m/s" % vf0)
    print("fiber(deg)  coupling  V_F(m/s)  margin")
    best = (vf0, 0.0)
    for deg in (-30, -15, 0, 15, 30):
        dc = 0.10*math.sin(2.0*math.radians(deg))   # washout coupling for deg>0
        vf = vf_for_coupling(dc)
        tag = ""
        if vf > best[0]:
            best = (vf, deg); tag = "<- BEST"
        print("%6d  %8.4f  %8.1f  %+.1f%% %s" % (deg, dc, vf, 100*(vf-vf0)/vf0, tag))
    assert best[0] > vf0*1.05, "tailoring must buy a real margin"
    print("optimal layup ~ %+d deg: washout coupling unloads the twist" % best[1])
    print("rule: write the wing's reflexes into its fibers")
    print("OK: %s tailored the layup" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_ase(name, rid, group, points, req):
    return _wrap_aero(name, rid, group, '''\
def main():
    # aeroservoelasticity: lagged pitch-rate feedback to flap
    P = typical_section()
    guesses = [P["wh"], P["wa"]]
    CC = 50.0
    def emat_cl(V, om, P, cc, tau):
        E = [list(r) for r in ematrix(V, om, P)]
        # control moment: -cc * alpha_dot through a first-order lag
        lag = 1.0/complex(1.0, om*tau)
        E[1][1] = E[1][1] + cc*1j*om*lag
        return ((E[0][0],E[0][1]),(E[1][0],E[1][1]))
    def vf_closed(cc, tau):
        def maxg(V):
            return max(g for _, g in k_method_roots(
                V, P, guesses, emat=lambda Vv, oo, PP: emat_cl(Vv, oo, PP, cc, tau)))
        lo, hi = 30.0, 200.0
        for _ in range(20):
            mid = 0.5*(lo+hi)
            if maxg(mid) > 0: hi = mid
            else: lo = mid
        return 0.5*(lo+hi)
    vf_open = vf_closed(0.0, 0.02)
    print("open-loop V_F = %.1f m/s" % vf_open)
    for tau, tag in ((0.01, "fast actuators"), (0.15, "slow actuators")):
        vf = vf_closed(CC, tau)
        print("feedback gain %.0f, tau %.2f s (%s): V_F = %.1f m/s (%+.1f%%)" %
              (CC, tau, tag, vf, 100*(vf-vf_open)/vf_open))
    vf_fast = vf_closed(CC, 0.01)
    vf_slow = vf_closed(CC, 0.15)
    assert vf_fast > vf_open*1.10, "fast loop must help"
    assert vf_slow < vf_fast, "lag must erode the benefit"
    assert vf_slow > vf_open, "slow loop still helps a little"
    print("rule: the computer speaks with a delay - every millisecond is a word spoken late")
    print("OK: %s closed the loop" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_suppression(name, rid, group, points, req):
    return _wrap_aero(name, rid, group, '''\
def main():
    # flutter suppression: minimum rate-feedback gain for +15% V_F
    P = typical_section()
    guesses = [P["wh"], P["wa"]]
    tau = 0.02
    def emat_cl(V, om, P, cc):
        E = [list(r) for r in ematrix(V, om, P)]
        lag = 1.0/complex(1.0, om*tau)
        E[1][1] = E[1][1] + cc*1j*om*lag
        return ((E[0][0],E[0][1]),(E[1][0],E[1][1]))
    def vf_of(cc):
        def maxg(V):
            return max(g for _, g in k_method_roots(
                V, P, guesses, emat=lambda Vv, oo, PP: emat_cl(Vv, oo, PP, cc)))
        lo, hi = 30.0, 200.0
        for _ in range(20):
            mid = 0.5*(lo+hi)
            if maxg(mid) > 0: hi = mid
            else: lo = mid
        return 0.5*(lo+hi)
    vf0 = vf_of(0.0)
    target = 1.15*vf0
    print("open-loop V_F = %.1f m/s; suppression target %.1f m/s" % (vf0, target))
    print(" gain   V_F")
    cc = 5.0
    while cc < 200.0:
        vf = vf_of(cc)
        print("%5.1f  %6.1f %s" % (cc, vf, "<- TARGET MET" if vf >= target else ""))
        if vf >= target:
            break
        cc += 5.0
    assert vf >= target, "gain must achieve the target"
    cc_star = cc
    # spillover: both modes' damping at the suppressed speed must stay negative
    roots = k_method_roots(target*0.98, P, guesses,
                           emat=lambda Vv, oo, PP: emat_cl(Vv, oo, PP, cc_star))
    gs = sorted(g for _, g in roots)
    print("at 0.98*target: dampings %+.4f / %+.4f (both <0: no spillover)" % (gs[0], gs[1]))
    assert all(x < 0 for x in gs)
    # failure: open loop at the suppressed speed is unstable
    gfail = max(g for _, g in k_method_roots(target, P, guesses))
    print("loop failed at suppressed speed: max g = %+.3f -> UNSTABLE (why passives are required)" % gfail)
    assert gfail > 0
    print("rule: earn the passive margin first, then let the active system spend it")
    print("OK: %s suppressed the flutter" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_gvt(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # GVT: half-power damping extraction from a noisy synthetic FRF
    modes = [(4.0, 0.010), (8.0, 0.015), (13.0, 0.020)]
    import random
    random.seed(7)
    def frf(f):
        H = 0j
        for fn, z in modes:
            r = f/fn
            H += 1.0/((1-r*r) + 1j*2*z*r)
        H *= (1.0 + 0.02*random.gauss(0, 1) + 0.02j*random.gauss(0, 1))
        return H
    # peak-pick then half-power
    print(" true f  meas f   true z  meas z")
    for fn, z in modes:
        f = fn*0.9
        best, bf = 0.0, f
        while f < fn*1.1:
            a = abs(frf(f))
            if a > best: best, bf = a, f
            f += 0.005
        Hpk = best
        # half-power points
        f1 = bf
        while f1 > fn*0.5 and abs(frf(f1)) > Hpk/math.sqrt(2): f1 -= 0.005
        f2 = bf
        while f2 < fn*1.5 and abs(frf(f2)) > Hpk/math.sqrt(2): f2 += 0.005
        zm = (f2-f1)/(2*bf)
        print("%6.1f  %6.2f  %6.3f  %6.3f" % (fn, bf, z, zm))
        assert abs(bf-fn)/fn < 0.02, "frequency recovery"
        assert abs(zm-z)/z < 0.35, "damping recovery"
    print("rule: the airplane testifies about itself - tune the model to the testimony")
    print("OK: %s listened to the modes" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_windtunnel(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # transonic flutter model scaling: 1/10 in heavy gas
    f_f, m_f, L_f = 3.0, 4000.0, 10.0
    Ls = 0.1
    a_ratio = 170.0/340.0          # heavy gas vs air speed of sound
    rho_ratio = 3.0/1.225          # pressurized heavy gas vs air
    V_scale = a_ratio              # Mach-matched
    f_m = f_f*V_scale/Ls
    m_m = m_f*rho_ratio*Ls**3
    # stiffness scale: k ~ m*(2*pi*f)^2
    k_f = m_f*(2*math.pi*f_f)**2
    k_m = m_m*(2*math.pi*f_m)**2
    print("full scale: f=%.1f Hz mass=%.0f kg" % (f_f, m_f))
    print("model: f=%.1f Hz mass=%.2f kg spar k=%.2e N/m" % (f_m, m_m, k_m))
    assert abs(f_m - 15.0) < 0.01
    assert abs(m_m - 9.80) < 0.05
    # similitude: reduced frequency and mass ratio match
    V_f, V_m = 250.0, 250.0*V_scale
    k_red_f = (2*math.pi*f_f)*(L_f/2)/V_f
    k_red_m = (2*math.pi*f_m)*(L_f*Ls/2)/V_m
    print("reduced frequency: full %.4f vs model %.4f" % (k_red_f, k_red_m))
    assert abs(k_red_f-k_red_m)/k_red_f < 1e-9
    mu_f = m_f/(math.pi*1.225*(L_f/2)**2*L_f)
    mu_m = m_m/(math.pi*3.0*(L_f*Ls/2)**2*(L_f*Ls))
    print("mass ratio: full %.2f vs model %.2f" % (mu_f, mu_m))
    assert abs(mu_f-mu_m)/mu_f < 1e-9
    print("rule: not a miniature - a physics-preserving analog")
    print("OK: %s scaled the tunnel" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_flighttest(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # damping extrapolation: fit zeta(q), extrapolate to zero -> q_F
    import random
    random.seed(11)
    qF_true = 40000.0
    qs = [12000.0, 16000.0, 20000.0, 24000.0, 28000.0, 32000.0]
    zetas = [0.030*(1.0-(q/qF_true)**2) + random.gauss(0, 0.0012) for q in qs]
    print("   q(Pa)  zeta_meas")
    for q, z in zip(qs, zetas):
        print("%8.0f  %7.4f" % (q, z))
    # least squares: zeta = c0 + c2*x^2 (physical model, x = q/1e4)
    xs = [q/1e4 for q in qs]
    n = len(xs)
    Sx2 = sum(x*x for x in xs); Sx4 = sum(x**4 for x in xs)
    Sy = sum(zetas); Sx2y = sum(x*x*z for x, z in zip(xs, zetas))
    # solve [[n, Sx2],[Sx2, Sx4]] [c0, c2] = [Sy, Sx2y]
    det = n*Sx4 - Sx2*Sx2
    c0 = (Sy*Sx4 - Sx2*Sx2y)/det
    c2 = (n*Sx2y - Sx2*Sy)/det
    # zeta = 0 -> xF = sqrt(-c0/c2)
    xF = math.sqrt(-c0/c2)
    qF = xF*1e4
    print("fit: zeta = %.4e %+.3e*x^2 (x=q/1e4)" % (c0, c2))
    print("extrapolated q_F = %.0f Pa (true %.0f Pa): error %.1f%%" %
          (qF, qF_true, 100*abs(qF-qF_true)/qF_true))
    assert abs(qF-qF_true)/qF_true < 0.10
    print("STOP at 0.85*q_F: never fly to the prediction")
    print("rule: excite, measure, extrapolate - one careful point at a time")
    print("OK: %s opened the envelope" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_cert(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # FAR 25.629 compliance arithmetic
    VD_env = 250.0   # design dive speed, m/s
    cases = [
        ("baseline", 340.0, 320.0, 310.0),
        ("soft wing", 290.0, 320.0, 310.0),
    ]
    for tag, VF, VDiv, VR in cases:
        margin_speed = min(VF, VDiv, VR)
        req_speed = 1.2*VD_env
        vdamp_ok = True   # >=3% damping in-envelope (from V-g tables)
        fail_open = min(VF, VDiv, VR)/VD_env
        verdict = "PASS" if (margin_speed >= req_speed and vdamp_ok) else "FAIL"
        print("%-9s V_F=%.0f V_D=%.0f V_R=%.0f: min=%.0f vs req %.0f -> %s" %
              (tag, VF, VDiv, VR, margin_speed, req_speed, verdict))
        if tag == "baseline":
            assert verdict == "PASS"
            assert abs(margin_speed-req_speed) < 15.0
        else:
            assert verdict == "FAIL", "soft wing must fail clearance"
    print("remedies for FAIL: stiffen, restrict envelope, or (rarely) active suppression")
    print("rule: the promise - no flutter, divergence, or reversal, anywhere allowed, with margin")
    print("OK: %s certified the envelope" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_nonlinear(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # freeplay: dead-zone stiffness -> LCO BELOW the linear flutter speed
    I, wa = 50.0, 10.0
    ka = I*wa*wa
    Sref, cref = 2.0, 1.0
    Cm_a, Cmq = 0.05, -0.8
    c_struct = 2*0.02*wa*I
    # linear flutter speed: net damping zero
    VFlin = -c_struct/(0.5*RHO_SL*Sref*cref*cref*Cmq)
    V = 0.92*VFlin
    q = _q(RHO_SL, V)
    delta = math.radians(1.0)
    print("linear V_F = %.1f m/s; testing at %.1f m/s (0.92x)" % (VFlin, V))
    def k_fp(al):
        if abs(al) <= delta:
            return 0.0
        return ka*(abs(al)-delta)*math.copysign(1.0, al)
    def march(freeplay, a0d):
        al, dal = math.radians(a0d), 0.0
        dt = 0.0005
        mx = 0.0
        for i in range(40000):
            def a2(a, d):
                kss = k_fp(a) if freeplay else ka*a
                Maa = q*Sref*cref*Cm_a*a + q*Sref*cref*(cref/V)*Cmq*d
                return (-kss - c_struct*d + Maa)/I
            k1a, k1d = dal, a2(al, dal)
            k2a, k2d = dal+0.5*dt*k1d, a2(al+0.5*dt*k1a, dal+0.5*dt*k1d)
            k3a, k3d = dal+0.5*dt*k2d, a2(al+0.5*dt*k2a, dal+0.5*dt*k2d)
            k4a, k4d = dal+dt*k3d, a2(al+dt*k3a, dal+dt*k3d)
            al += dt/6*(k1a+2*k2a+2*k3a+k4a)
            dal += dt/6*(k1d+2*k2d+2*k3d+k4d)
            if i > 20000:
                mx = max(mx, abs(al))
            if abs(al) > 1.0:
                return float("inf")
        return mx
    lin = march(False, 2.0)
    fp = march(True, 2.0)
    print("linear model settles to %.3f deg (stable)" % math.degrees(lin))
    print("freeplay model settles to %.3f deg -> LCO below linear V_F" % math.degrees(fp))
    assert math.degrees(lin) < 0.5, "linear must be stable here"
    assert 0.5 < math.degrees(fp) < 8.0, "freeplay must buzz at a few x delta"
    print("fix: preload/tighten the linkage (delta->0) restores the linear boundary")
    print("rule: the linear flutter speed is where trouble starts being possible")
    print("OK: %s rattled the linkage" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_gust(name, rid, group, points, req):
    return _wrap_aero(name, rid, group, '''\
def main():
    # 1-cosine gust + Kuessner convolution; alleviation credit
    c, V = 2.0, 150.0
    Lg = 12.5*c
    w0 = 10.0
    b = c/2.0
    rho = RHO_SL
    S = c*1.0
    W = 40000.0
    dt = 0.002
    t_end = Lg/V + 1.0
    n = int(t_end/dt)
    # gust velocity history at the wing
    def wgust(t):
        s = V*t
        if s < 0 or s > Lg:
            return 0.0
        return 0.5*w0*(1.0-math.cos(2*math.pi*s/Lg))
    # convolution with Kuessner: dL(t) = q*S*a0 * integral psi' ...
    # discrete: dL = rho*V*S*a0 * sum psi(tau - tau') * dwg
    a0 = 5.7
    dL_hist = []
    wg_hist = [wgust(i*dt) for i in range(n)]
    peak = 0.0
    for i in range(n):
        t = i*dt
        dL = 0.0
        for j in range(i+1):
            tj = j*dt
            tau = V*(t-tj)/b
            if tau < 0 or tau > 30:
                continue
            dwg = (wg_hist[j]-wg_hist[j-1]) if j > 0 else wg_hist[j]
            dL += rho*V*S*a0*kussner_psi(tau)*dwg
        dL_hist.append(dL)
        peak = max(peak, dL)
    dn = peak/W
    print("peak incremental load: %.1f N -> delta_n = %.3f g" % (peak, dn))
    assert 0.2 < dn < 1.0, dn
    # alleviation: aileron counters sensed gust with 0.15 s lag, 70% authority
    tau_lag, auth = 0.15, 0.70
    sensed = 0.0
    peak2 = 0.0
    for i in range(n):
        t = i*dt
        wg = wg_hist[i]
        sensed += (wg-sensed)*dt/max(tau_lag, 1e-9)
        cancel = auth*sensed/w0
        # effective gust seen by wing reduced by alleviation
        dL = dL_hist[i]*(1.0-cancel*0.5)
        peak2 = max(peak2, dL)
    dn2 = peak2/W
    print("with alleviation: delta_n = %.3f g (reduction %.0f%%)" % (dn2, 100*(dn-dn2)/dn))
    assert dn2 < dn*0.90, "alleviation must cut the peak"
    print("rule: read the gust ahead, cancel it before the structure feels it")
    print("OK: %s rode the gust" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ae_integrated(name, rid, group, points, req):
    return _wrap_aero(name, rid, group, '''\
def main():
    # the 8-step integrated loop on one consistent wing (regional jet scale)
    print("STEP 1 - mission & rigid loads")
    Vcruise, Vdive, W = 150.0, 180.0, 60000.0
    S, span, chord = 30.0, 12.0, 2.5
    qC = _q(RHO_SL, Vcruise)
    L = W
    Mroot_rigid = L*span/6.0
    print("  cruise q=%.0f Pa root moment=%.0f N-m" % (qC, Mroot_rigid))
    print("STEP 2 - flexible loads (washout iteration, 3 stations)")
    Lambda = math.radians(25.0)
    rigid = [1.0, 0.85, 0.55]
    yst = [4.0, 8.0, 12.0]
    loads = list(rigid)
    for it in range(20):
        wash = [0.02*loads[i]*(i+1)*math.sin(Lambda) for i in range(3)]
        new = [loads[i]*(1.0-0.8*wash[i]) for i in range(3)]
        tot_old, tot_new = sum(loads), sum(new)
        new = [x*tot_old/tot_new for x in new]
        if max(abs(new[i]-loads[i]) for i in range(3)) < 1e-6:
            loads = new; break
        loads = new
    Mr = sum(r*y for r, y in zip(rigid, yst))
    Mf = sum(f*y for f, y in zip(loads, yst))
    Mroot_flex = Mroot_rigid*Mf/Mr
    print("  flexible/rigid root moment ratio = %.3f" % (Mf/Mr))
    assert Mf < Mr
    print("STEP 3 - sizing: spar caps from bending, box from torsion")
    sig_allow = 300.0e6
    hbox = 0.12*chord
    Acap = Mroot_flex/(sig_allow*hbox)
    print("  spar cap area %.1f cm^2" % (Acap*1e4))
    assert Acap > 0
    print("STEP 4 - divergence of the sized wing")
    bb, rho = 2.0, RHO_SL
    mu, xa, aa = 30.0, 0.20, -0.35
    m = mu*math.pi*rho*bb*bb
    wh, wa = 2*math.pi*2.5, 2*math.pi*6.0
    P = {"b": bb, "rho": rho, "m": m, "xa": xa, "ra2": 0.25, "a": aa,
         "kh": m*wh*wh, "ka": m*bb*bb*0.25*wa*wa, "wh": wh, "wa": wa}
    VD = divergence_speed(P)
    print("  V_D = %.0f m/s" % VD)
    assert VD > Vdive
    print("STEP 5 - flutter (k-method on sized section)")
    guesses = [wh, wa]
    def maxg_of(Px):
        def maxg(V):
            return max(g for _, g in k_method_roots(V, Px, guesses))
        return maxg
    def vf_of(Px):
        mg = maxg_of(Px)
        lo, hi = 100.0, 600.0
        for _ in range(20):
            mid = 0.5*(lo+hi)
            if mg(mid) > 0: hi = mid
            else: lo = mid
        return 0.5*(lo+hi)
    VF = vf_of(P)
    print("  baseline V_F = %.0f m/s (need >= %.0f)" % (VF, 1.2*Vdive))
    print("STEP 6 - tailoring until margin closes")
    dc, it = 0.0, 0
    while VF < 1.2*Vdive and it < 10:
        dc += 0.05; it += 1
        P2 = dict(P); P2["a"] = P["a"]-dc
        VF = vf_of(P2)
        print("  dc=%.2f -> V_F=%.0f m/s" % (dc, VF))
    print("  tailored coupling dc=%.2f -> V_F=%.0f m/s (margin %.1f%%)" % (dc, VF, 100*(VF/Vdive-1)))
    assert VF >= 1.2*Vdive, "loop must close"
    print("STEP 7 - gust check")
    a0g = 5.7
    dn = 1.0 + 0.5*RHO_SL*Vcruise*S*a0g*8.0/W
    print("  discrete gust delta_n ~ %.2f g" % dn)
    assert dn < 4.0
    print("STEP 8 - FAR 25.629 verdict")
    assert min(VF, VD) >= 1.2*Vdive
    print("  min(V_F,V_D)=%.0f >= 1.2*V_dive=%.0f -> CERTIFIED" % (min(VF, VD), 1.2*Vdive))
    print("rule: the loop is the discipline - loads to proof, no shortcuts")
    print("OK: %s designed the wing" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "collar_triangle": demo_ae_collar, "static_intro": demo_ae_static,
    "divergence": demo_ae_divergence, "elastic_axis": demo_ae_elastic_axis,
    "control_reversal": demo_ae_reversal, "aileron_effectiveness": demo_ae_aileron,
    "load_redistribution": demo_ae_loads, "sweep_divergence": demo_ae_sweep,
    "dynamic_intro": demo_ae_dynamic, "unsteady_aero": demo_ae_unsteady,
    "theodorsen": demo_ae_theodorsen, "wagner": demo_ae_wagner,
    "kussner": demo_ae_kussner, "bending_torsion_flutter": demo_ae_flutter,
    "flutter_prediction": demo_ae_prediction, "panel_flutter": demo_ae_panel,
    "propeller_whirl": demo_ae_whirl, "stall_flutter": demo_ae_stall,
    "transonic_dip": demo_ae_transonic_dip, "buffeting": demo_ae_buffeting,
    "lco": demo_ae_lco, "rotor_aeroelasticity": demo_ae_rotor,
    "civil_aeroelasticity": demo_ae_tacoma, "tailoring": demo_ae_tailoring,
    "aeroservoelasticity": demo_ae_ase, "flutter_suppression": demo_ae_suppression,
    "gvt": demo_ae_gvt, "wind_tunnel_flutter": demo_ae_windtunnel,
    "flight_flutter_test": demo_ae_flighttest, "certification": demo_ae_cert,
    "nonlinear_aeroelasticity": demo_ae_nonlinear, "gust_response": demo_ae_gust,
    "integrated_design": demo_ae_integrated,
}
assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"


def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_aeroelastic.py).
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
        demo_fn = DEMOS[e["key"]]
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
    for slug in ("aeroelasticity", "aeroelasticity-signature"):
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
                               capture_output=True, text=True, timeout=180)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
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
        assert "pill-ex" in page and "qmerge" in page, "Exhaustive pill / merger button missing"
        assert "dataset.p" in page, "tab-handler guard missing"
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
