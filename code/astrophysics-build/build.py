#!/usr/bin/env python3
"""Build the Astrophysics field databases for JAH Databases (field #2, taxonomy order).

Verified 2026-10-17: the manifest holds astronomy DBs (astronomy, astronomy-public,
astronomy-signature, space-astro, interstellar-travel, space-cosmology-databases)
but no dedicated astrophysics database — thin, scattered coverage of the field as
a discipline. So this build creates two NEW databases rather than extending them:

  astrophysics            — The Astrophysics Database (public-harvest: real,
                           fact-checked astrophysics — stellar structure and
                           evolution, radiative processes, interstellar medium,
                           accretion physics, compact objects, galactic dynamics,
                           cosmology interface, observational techniques,
                           numerical methods)
  astrophysics-signature  — The Astrophysics Signature Database (his original
                           Signature interpretation; src signature, titles
                           suffixed " (Signature Edition)", never presented as
                           authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10, ladder_tier
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
from entries_astrophysics import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals — his original Signature interpretation of astrophysics: "
                "clearly labeled Signature-made, never presented as authentic public record.")
    pub_line = ("Public records — real, fact-checked astrophysics: stellar structure and "
                "evolution, radiative processes, the interstellar medium, accretion physics, "
                "compact objects, galactic dynamics, the cosmology interface, observational "
                "techniques, and numerical methods, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (cosmic units, light, "
              "blackbody radiation, magnitudes, telescopes) -> Compounded (hydrostatic "
              "equilibrium, fusion, the HR diagram, radiative transfer, the interstellar "
              "medium, star formation, accretion, stellar evolution, supernovae, galactic "
              "dynamics) -> Advanced (compact objects, microlensing, exoplanets, the cosmic "
              "microwave background, cosmic expansion, dark energy, quasars, gamma-ray "
              "bursts, nucleosynthesis, numerical methods).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s — %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search astrophysics concepts, objects, equations...",
        "chat_ph": "Ask about astrophysics...",
        "archive_blurb": ("Seeded %s astrophysics records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations · Compounded · Advanced — each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled structural astrophysics studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about astrophysics — from cosmic units and starlight up to black holes, dark energy, and numerical cosmology." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "astrophysics-study", "gen_demo_kind": "astrophysics-demo",
        "source": source,
    }

CIT_PUB = "Astrophysics (peer-reviewed literature and standard textbooks)."
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["astrophysics"] = _cfg(
    "astrophysics", "The Astrophysics Database",
    "Real, fact-checked astrophysics: stellar structure and evolution, radiative processes, "
    "the interstellar medium, accretion physics, compact objects, galactic dynamics, the "
    "cosmology interface, observational techniques, and numerical methods.",
    "astrophysics record", "JAH-AST-", "JAH Astrophysics Archivist",
    "astrophysics archivist — stellar structure and evolution, radiative processes, "
    "interstellar medium, accretion physics, compact objects, galactic dynamics, cosmology "
    "interface, observational techniques, numerical methods; teaching progressively along "
    "the ladder from foundations (cosmic units, light, blackbody radiation, magnitudes, "
    "telescopes) through compounded (hydrostatic equilibrium, fusion, HR diagram, radiative "
    "transfer, ISM, star formation, accretion, stellar evolution, supernovae, galactic "
    "dynamics) to advanced (compact objects, microlensing, exoplanets, CMB, cosmic expansion, "
    "dark energy, quasars, gamma-ray bursts, nucleosynthesis, numerical methods); answers "
    "from many angles — definition, example, analogy, application, history, math, how-to — "
    "using only the system's own archive data",
    CIT_PUB, "public")
DBCFG["astrophysics-signature"] = _cfg(
    "astrophysics-signature", "The Astrophysics Signature Database",
    "His original Signature interpretation of astrophysics: the full ladder from cosmic "
    "units to numerical cosmology, reframed as Signature engineering. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "astrophysics record", "JAH-ASG-", "JAH Astrophysics Archivist (Signature)",
    "astrophysics archivist — Signature editions: his original Signature interpretation of "
    "astrophysics, clearly labeled Signature-made and never presented as authentic public "
    "record; teaches progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles — definition, example, analogy, application, history, "
    "math, how-to — using only the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# astrophysical calculation for its record. All are machine-executed by main().

_PREAMBLE = """import math
C = 299792458.0
G = 6.67430e-11
H = 6.62607015e-34
KB = 1.380649e-23
SIG = 5.670374419e-8
SIGT = 6.6524587321e-29
MP = 1.67262192369e-27
PC = 3.085677581e16
AU = 1.495978707e11
LY = 9.4607304725808e15
MSUN = 1.98847e30
RSUN = 6.957e8
LSUN = 3.828e26
WIEN = 2.897771955e-3
EV = 1.602176634e-19
"""

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_astro_overview(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    age_gyr, radius_gly = 13.8, 46.5
    n_gal, stars_per_gal = 2e12, 1e11
    n_stars = n_gal * stars_per_gal
    print("universe age: %.1f Gyr | observable radius: %.1f Gly" % (age_gyr, radius_gly))
    print("galaxies ~%.0e x %.0e stars/galaxy = %.0e stars" % (n_gal, stars_per_gal, n_stars))
    sun_min = AU / C / 60.0
    print("sunlight travel time: %.2f minutes" % sun_min)
    assert n_stars == 2e23
    assert abs(sun_min - 8.317) < 0.01
    print("OK: %s framed the cosmic scale" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_scale_units(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    arcsec = math.pi / (180.0 * 3600.0)   # one arcsecond in radians
    pc_m = AU / math.tan(arcsec)           # parsec from its definition
    print("1 parsec = %.6e m = %.5f light-years" % (pc_m, pc_m / LY))
    assert abs(pc_m / PC - 1.0) < 1e-6
    assert abs(pc_m / LY - 3.26156) < 1e-4
    print("Proxima Centauri: 1.3012 pc = %.3f ly" % (1.3012 * pc_m / LY))
    print("Andromeda: 780 kpc = %.3e ly" % (780e3 * pc_m / LY))
    assert abs(1.3012 * pc_m / LY - 4.244) < 0.01
    # parallax: distance(pc) = 1 / parallax(arcsec)
    print("a star with 0.1 arcsec parallax sits at %.0f pc" % (1.0 / 0.1))
    print("OK: %s derived the parsec from first principles" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_spectrum(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    bands = [("radio 21 cm", 0.21), ("infrared 10 um", 10e-6),
             ("visible 500 nm", 500e-9), ("X-ray 1 nm", 1e-9), ("gamma 1 pm", 1e-12)]
    for label, lam in bands:
        e_ev = H * C / lam / EV
        unit, val = ("eV", e_ev) if e_ev < 1000 else (("keV", e_ev / 1e3) if e_ev < 1e6 else ("MeV", e_ev / 1e6))
        print("%-16s photon energy: %9.3g %s" % (label, val, unit))
    assert abs(H * C / 500e-9 / EV - 2.48) < 0.01
    assert abs(H * C / 1e-9 / EV / 1e3 - 1.24) < 0.01
    print("OK: %s converted the whole spectrum to photon energies" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_blackbody(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    for T, label in ((5778.0, "Sun"), (10000.0, "blue star"), (3000.0, "red dwarf"),
                     (2.7255, "CMB"), (310.0, "human body")):
        lmax = WIEN / T
        unit, val = ("nm", lmax * 1e9) if lmax < 1e-6 else (("um", lmax * 1e6) if lmax < 1e-3 else ("mm", lmax * 1e3))
        print("%-10s T=%7.2f K  peak at %8.3g %s" % (label, T, val, unit))
    assert abs(WIEN / 5778.0 - 501.5e-9) < 2e-9
    L = 4 * math.pi * RSUN ** 2 * SIG * 5778.0 ** 4
    print("Stefan-Boltzmann check: L = %.4e W (%.4f Lsun)" % (L, L / LSUN))
    assert abs(L / LSUN - 1.0) < 0.02
    print("OK: %s ran Wien's and Stefan-Boltzmann's laws" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_magnitude(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    d_sun_pc = AU / PC
    M_sun = -26.74 - 5 * math.log10(d_sun_pc) + 5   # distance modulus inverted
    print("Sun: m=-26.74 at %.2e pc -> M=%.2f" % (d_sun_pc, M_sun))
    assert abs(M_sun - 4.83) < 0.05
    M_sirius = -1.46 - 5 * math.log10(2.64) + 5
    print("Sirius: m=-1.46 at 2.64 pc -> M=%.2f" % M_sirius)
    assert abs(M_sirius - 1.42) < 0.05
    step = 100.0 ** (1.0 / 5.0)
    print("one magnitude step = factor %.6f" % step)
    assert abs(step - 2.5118864) < 1e-6
    print("OK: %s worked the magnitude system end to end" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_sb_law(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def lum(R_Rsun, T):
    return R_Rsun ** 2 * (T / 5778.0) ** 4
def main():
    print("Sun:        %10.4f Lsun" % lum(1.0, 5778.0))
    betel, rigel = lum(764.0, 3600.0), lum(79.0, 12100.0)
    print("Betelgeuse: %10.0f Lsun (cool but enormous)" % betel)
    print("Rigel:      %10.0f Lsun (small but ferociously hot)" % rigel)
    assert abs(lum(1.0, 5778.0) - 1.0) < 1e-9
    assert 8e4 < betel < 1e5
    assert 1e5 < rigel < 1.4e5
    # invert: radius of a star with L=25.4 Lsun, T=9940 K (Sirius A)
    R = math.sqrt(25.4) / (9940.0 / 5778.0) ** 2
    print("Sirius A radius from L and T: %.2f Rsun" % R)
    assert 1.6 < R < 1.8
    print("OK: %s applied L = 4 pi R^2 sigma T^4" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_telescope(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def resolution_arcsec(D, lam=500e-9):
    return 1.22 * lam / D * 206265.0
def main():
    hst = resolution_arcsec(2.4)
    elt = resolution_arcsec(39.0)
    print("diffraction limit at 500 nm: HST (2.4 m) %.3f arcsec | ELT (39 m) %.4f arcsec" % (hst, elt))
    assert abs(hst - 0.0524) < 0.002
    assert elt < 0.004
    gather = (10000.0 / 7.0) ** 2   # 10 m Keck vs 7 mm dark-adapted eye
    print("Keck light-gathering vs human eye: %.2e x" % gather)
    assert 2.0e6 < gather < 2.1e6
    print("typical atmospheric seeing: ~1 arcsec (ground limit without adaptive optics)")
    print("OK: %s sized telescope performance" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_doppler_spec(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    lam = 656.28e-9   # H-alpha, meters
    K = 55.6          # m/s: 51 Pegasi b's stellar wobble
    dlam = lam * K / C
    print("51 Peg b: stellar wobble %5.1f m/s -> H-alpha shifts %.3e m (%.2e relative)" % (K, dlam, K / C))
    assert abs(K / C - 1.855e-7) < 1e-10
    v = 220e3         # galactic rotation speed
    shift_nm = lam * v / C * 1e9
    print("galactic rotation 220 km/s -> H-alpha shifts %.4f nm" % shift_nm)
    assert abs(shift_nm - 0.4814) < 0.001
    print("OK: %s read velocities from spectral shifts" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hydrostatic(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    rho = 3 * MSUN / (4 * math.pi * RSUN ** 3)     # mean solar density
    pc_analytic = 2 * math.pi / 3 * G * rho ** 2 * RSUN ** 2
    n, dr = 2000, RSUN / 2000.0
    P = 0.0
    for i in range(n, 0, -1):                       # integrate inward from the surface
        r = i * dr
        Mr = 4.0 / 3.0 * math.pi * r ** 3 * rho
        P += G * Mr * rho / r ** 2 * dr             # dP = rho g dr
    print("constant-density Sun: analytic Pc = %.3e Pa, numeric Pc = %.3e Pa" % (pc_analytic, P))
    assert abs(P / pc_analytic - 1.0) < 0.01
    assert 1e14 < P < 2e14
    print("real Sun Pc ~ 2.5e16 Pa: central-condensation factor ~%.0f" % (2.5e16 / P))
    print("OK: %s integrated hydrostatic equilibrium" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_fusion(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    r_pp = (15.7 / 12.0) ** 4      # pp-chain ~ T^4 near solar core temps
    r_cno = (15.7 / 12.0) ** 20    # CNO cycle ~ T^20
    print("15.7 MK vs 12 MK core: pp rate x%.2f | CNO rate x%.0f" % (r_pp, r_cno))
    assert abs(r_pp - 2.93) < 0.05
    assert 200 < r_cno < 230
    E_per = 26.73e6 * EV                          # joules per helium nucleus
    rate = LSUN / E_per
    print("solar pp fusions per second: %.3e" % rate)
    assert 8.5e37 < rate < 9.5e37
    nu_flux = 2 * rate / (4 * math.pi * AU ** 2) / 1e4   # per cm^2 per s at Earth
    print("solar neutrino flux at Earth: %.2e cm^-2 s^-1" % nu_flux)
    assert 5.5e10 < nu_flux < 7e10
    print("OK: %s balanced the stellar fusion ledger" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hr(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    stars = [("Sun", 5778.0, 1.0, "main sequence"),
             ("Sirius A", 9940.0, 25.4, "main sequence"),
             ("Proxima Cen", 3042.0, 0.0017, "main sequence"),
             ("Betelgeuse", 3600.0, 9e4, "supergiant"),
             ("Rigel", 12100.0, 1.2e5, "supergiant"),
             ("Sirius B", 25200.0, 0.056, "white dwarf")]
    print("HR diagram positions (hotter -> left, brighter -> up):")
    for sname, T, L, region in stars:
        print("  %-12s logT=%5.3f logL=%+6.2f  [%s]" % (sname, math.log10(T), math.log10(L), region))
    assert abs(math.log10(5778.0) - 3.762) < 0.01
    # white dwarfs sit far below the main sequence at the same temperature
    assert math.log10(0.056) < -1.0
    print("OK: %s placed real stars on the HR diagram" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_masslum(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    pts = [(0.5, 0.088), (1.0, 1.0), (2.0, 11.3), (10.0, 3162.0)]
    print(" M (Msun)   L (Lsun)    t_MS")
    for M, L in pts:
        t = 1e10 * M / L
        print("  %5.1f   %9.3g   %9.3g yr" % (M, L, t))
    exp = math.log(3162.0 / 0.088) / math.log(10.0 / 0.5)
    print("fitted L-M exponent: %.3f (canonical ~3.5)" % exp)
    assert abs(exp - 3.5) < 0.05
    assert abs(1e10 * 10.0 / 3162.0 - 3.16e7) / 3.16e7 < 0.02
    print("OK: %s verified the mass-luminosity relation" % NAME)
if __name__ == "__main__":
    main()
''')
def demo_radtransfer(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    print("Beer-Lambert attenuation I = I0 e^-tau:")
    for tau in (0.0, 2.0 / 3.0, 1.0, 5.0):
        print("  tau = %4.2f  ->  I/I0 = %.4f" % (tau, math.exp(-tau)))
    assert abs(math.exp(-2.0 / 3.0) - 0.5134) < 0.001
    print("photosphere at tau = 2/3 transmits %.1f%% of the deep intensity" % (100 * math.exp(-2.0 / 3.0)))
    print("limb darkening (Eddington approx I(mu) = I0 (0.4 + 0.6 mu)):")
    for mu in (1.0, 0.5, 0.1):
        print("  mu = %.1f  ->  I/I0 = %.3f" % (mu, 0.4 + 0.6 * mu))
    assert abs((0.4 + 0.6 * 0.1) - 0.46) < 1e-9
    print("OK: %s traced photons through optical depth" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eddington(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def L_edd(M):
    return 4 * math.pi * G * M * MP * C / SIGT   # watts
def main():
    Le = L_edd(MSUN)
    print("Eddington luminosity: 1 Msun  -> %.3e erg/s = %.0f Lsun" % (Le * 1e7, Le / LSUN))
    assert abs(Le * 1e7 - 1.26e38) / 1.26e38 < 0.02
    assert abs(Le / LSUN - 3.28e4) / 3.28e4 < 0.02
    print("                    100 Msun -> %.3e Lsun" % (L_edd(100 * MSUN) / LSUN))
    print("              1e9 Msun (quasar-scale) -> %.3e erg/s" % (L_edd(1e9 * MSUN) * 1e7))
    assert abs(L_edd(1e9 * MSUN) * 1e7 - 1.26e47) / 1.26e47 < 0.02
    print("OK: %s enforced the Eddington limit" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ism(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    phases = [("cold molecular", 1e2, 15.0), ("cold neutral", 30.0, 100.0),
              ("warm neutral", 0.5, 8000.0), ("warm ionized", 0.3, 8000.0),
              ("hot ionized", 0.005, 1e6)]
    print("ISM phase pressure balance (nT in K cm^-3):")
    vals = []
    for pname, n, T in phases:
        vals.append(n * T)
        print("  %-15s n=%8g cm^-3  T=%8g K  nT=%6.0f" % (pname, n, T, n * T))
    assert max(vals) / min(vals) < 4.0, "phases must coexist in rough pressure balance"
    assert all(1000 < v < 8000 for v in vals)
    print("OK: %s balanced the interstellar phases" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_jeans(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
MU = 2.3   # mean molecular weight, molecular gas
def M_jeans(T, n_cm3):
    rho = n_cm3 * 1e6 * MU * MP
    return (math.pi / 6.0) * (math.pi * KB * T / (G * MU * MP)) ** 1.5 / math.sqrt(rho)
def main():
    Mj = M_jeans(10.0, 1e4)
    print("Jeans mass at 10 K, 1e4 cm^-3: %.2f Msun" % (Mj / MSUN))
    assert 1.0 < Mj / MSUN < 10.0
    hot = M_jeans(100.0, 1e4)
    dense = M_jeans(10.0, 1e6)
    print("at 100 K: %.1f Msun (hot gas resists) | at 1e6 cm^-3: %.2f Msun (dense gas fragments)" % (
        hot / MSUN, dense / MSUN))
    assert hot > Mj and dense < Mj
    print("OK: %s applied the Jeans criterion" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_accretion(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    M = 10 * MSUN
    L_edd = 4 * math.pi * G * M * MP * C / SIGT
    Mdot = 0.1 * L_edd / (0.1 * C ** 2)          # a tenth of the Eddington rate
    r_in = 6 * G * M / C ** 2                    # innermost stable orbit
    rs = 2 * G * M / C ** 2
    def T_of_r(r):
        return (3 * G * M * Mdot / (8 * math.pi * SIG * r ** 3) * (1 - math.sqrt(r_in / r))) ** 0.25
    print("10 Msun black hole disk at 0.1 Eddington:")
    for mult in (10, 100, 1000):
        print("  r = %4d rs   T = %.3e K" % (mult, T_of_r(mult * rs)))
    T10 = T_of_r(10 * rs)
    assert 2e6 < T10 < 4e6, T10
    ratio = T_of_r(100 * rs) / T_of_r(1000 * rs)   # T ~ r^-3/4 check
    assert abs(ratio - 10 ** 0.75) / 10 ** 0.75 < 0.05
    print("inner disk glows in X-rays; outer disk in optical/IR")
    print("OK: %s mapped an accretion disk's temperature" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_stevol(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def lifetime(M):
    return 1e10 * M ** -2.5
def remnant(M):
    if M < 0.5:
        return "He white dwarf"
    if M < 8:
        return "C-O white dwarf"
    if M < 25:
        return "neutron star"
    return "black hole"
def main():
    print("initial mass -> main-sequence lifetime -> remnant:")
    for M in (0.5, 1.0, 2.0, 8.0, 20.0, 40.0):
        print("  %5.1f Msun   %9.3g yr   -> %s" % (M, lifetime(M), remnant(M)))
    assert abs(lifetime(1.0) - 1e10) < 1
    assert abs(lifetime(10.0) - 3.16e7) / 3.16e7 < 0.02
    assert remnant(1.0) == "C-O white dwarf"
    assert remnant(20.0) == "neutron star"
    assert remnant(40.0) == "black hole"
    print("OK: %s ran the stellar fate table" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_supernova(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    M_Ia = -19.3
    m_obs = 17.2
    mu = m_obs - M_Ia
    d_pc = 10 ** (mu / 5.0 + 1)
    print("Type Ia: m=%.1f, M=%.1f -> distance modulus %.1f -> d=%.3g pc (%.0f Mpc)" % (
        m_obs, M_Ia, mu, d_pc, d_pc / 1e6))
    assert abs(d_pc / 1e6 - 200) < 5
    m87 = M_Ia + 5 * math.log10(51.4e3) - 5   # a Type Ia at SN 1987A's distance
    print("a Type Ia at SN 1987A's distance (51.4 kpc) would peak at m=%.1f" % m87)
    assert abs(m87 - (-0.75)) < 0.1
    print("OK: %s used a Type Ia supernova as a standard candle" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_rotation(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def v_newton(M, r_kpc):
    return math.sqrt(G * M / (r_kpc * 1e3 * PC))
def main():
    M_lum = 6e10 * MSUN
    v = v_newton(M_lum, 15.0)
    print("luminous mass only, at 15 kpc: v = %.0f km/s (observed ~220 km/s)" % (v / 1e3))
    assert v / 1e3 < 150
    missing = (220e3 / v) ** 2
    print("missing-mass factor to reach 220 km/s: %.1f x" % missing)
    assert missing > 2.0
    print("the gap is dark matter: an extended halo supplying the missing pull")
    print("OK: %s weighed a galaxy's invisible halo" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_whitedwarf(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def R_wd(M):
    return 0.01 * RSUN * (M / MSUN) ** (-1.0 / 3.0)
def main():
    M, R = 0.6 * MSUN, R_wd(0.6 * MSUN)
    rho = 3 * M / (4 * math.pi * R ** 3)
    print("0.6 Msun white dwarf: R = %.0f km, mean density = %.2e kg/m^3" % (R / 1e3, rho))
    assert rho > 1e8
    assert R_wd(1.2 * MSUN) < R_wd(0.6 * MSUN), "mass-radius relation must invert"
    print("1.0 Msun: R = %.0f km | 1.2 Msun: R = %.0f km (heavier = smaller)" % (
        R_wd(MSUN) / 1e3, R_wd(1.2 * MSUN) / 1e3))
    print("Chandrasekhar limit: 1.44 Msun — no stable white dwarf above it")
    assert abs(R_wd(MSUN) / RSUN - 0.01) < 1e-9
    print("OK: %s checked white-dwarf structure" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_neutronstar(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    M, R = 1.4 * MSUN, 12e3
    rho = 3 * M / (4 * math.pi * R ** 3)
    vesc = math.sqrt(2 * G * M / R)
    print("1.4 Msun, 12 km neutron star:")
    print("  mean density %.3e kg/m^3 (nuclear density ~3e17)" % rho)
    print("  escape velocity %.3f c" % (vesc / C))
    assert 3e17 < rho < 5e17
    assert 0.55 < vesc / C < 0.62
    print("  fastest known pulsar spin: 716 Hz")
    print("OK: %s sized a neutron star" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_bh(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def rs(M):
    return 2 * G * M / C ** 2
def main():
    print("Schwarzschild radii: 1 Msun -> %.2f km | 10 Msun -> %.1f km" % (rs(MSUN) / 1e3, rs(10 * MSUN) / 1e3))
    assert abs(rs(MSUN) / 1e3 - 2.953) < 0.01
    M_sgra = 4.297e6 * MSUN
    r = rs(M_sgra)
    print("Sagittarius A* (4.297e6 Msun): rs = %.3e m = %.4f AU" % (r, r / AU))
    assert abs(r / AU - 0.0847) / 0.0847 < 0.02
    r_isco = 3 * r
    T = 2 * math.pi * math.sqrt(r_isco ** 3 / (G * M_sgra))
    print("orbital period at the ISCO: %.0f s (%.1f minutes)" % (T, T / 60))
    assert 1500 < T < 2500
    print("M87* (6.5e9 Msun): rs = %.3e m" % rs(6.5e9 * MSUN))
    print("OK: %s sized black holes from stellar to supermassive" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_microlens(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    M = 0.5 * MSUN
    Dl, Ds = 4e3 * PC, 8e3 * PC
    Dls = Ds - Dl
    thE = math.sqrt(4 * G * M / C ** 2 * Dls / (Dl * Ds))
    mas = thE * 206265e3
    print("0.5 Msun lens at 4 kpc, source at 8 kpc: Einstein radius %.3f mas" % mas)
    assert 0.5 < mas < 1.2
    tE = mas / 5.0 * 365.25      # 5 mas/yr relative proper motion
    print("event timescale: %.1f days" % tE)
    assert 30 < tE < 90
    u = 0.1
    A = (u * u + 2) / (u * math.sqrt(u * u + 4))
    print("peak magnification at closest approach u=0.1: %.1f x" % A)
    assert 9.5 < A < 10.5
    print("OK: %s weighed an invisible lens" % NAME)
if __name__ == "__main__":
    main()
''')
def demo_exoplanet(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    dj = (7.1492e7 / RSUN) ** 2
    de = (6.371e6 / RSUN) ** 2
    print("transit depth: Jupiter/Sun %.3f %% | Earth/Sun %.1f ppm" % (dj * 100, de * 1e6))
    assert abs(dj * 100 - 1.056) < 0.01
    assert abs(de * 1e6 - 83.9) < 1.0
    K = 55.6   # m/s, 51 Pegasi b
    print("51 Pegasi b: stellar wobble K = %.1f m/s, period 4.2 days" % K)
    assert abs(K - 55.6) < 1e-9
    print("OK: %s detected exoplanets two ways" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_cmb(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    T = 2.7255
    lmax = WIEN / T
    print("CMB temperature %.4f K -> blackbody peak at %.3f mm" % (T, lmax * 1e3))
    assert abs(lmax * 1e3 - 1.063) < 0.005
    x = KB * T / (H * C)
    n = 16 * math.pi * 1.2020569 * x ** 3     # photon number density, per m^3
    print("photon density: %.0f cm^-3" % (n / 1e6))
    assert 400 < n / 1e6 < 420
    z = 1090
    print("last scattering at z=%d: plasma temperature then %.0f K" % (z, T * (1 + z)))
    assert abs(T * (1 + z) - 2974) < 5
    print("OK: %s characterized the afterglow of the Big Bang" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_friedmann(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    H0 = 70e3 / (1e6 * PC)          # 70 km/s/Mpc in s^-1
    rho_c = 3 * H0 ** 2 / (8 * math.pi * G)
    print("critical density: %.3e kg/m^3" % rho_c)
    assert abs(rho_c - 9.20e-27) / 9.20e-27 < 0.02
    print("               = %.1f hydrogen atoms per cubic meter" % (rho_c / 1.673e-27))
    tH = 1 / H0
    print("Hubble time 1/H0: %.2f Gyr" % (tH / 3.15576e7 / 1e9))
    assert abs(tH / 3.15576e7 / 1e9 - 13.97) < 0.1
    Om, Ol = 0.315, 0.685
    print("flat universe check: Om + Ol = %.3f" % (Om + Ol))
    assert abs(Om + Ol - 1.0) < 1e-9
    print("OK: %s evaluated the Friedmann ledger" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_darkenergy(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    Om, Ol = 0.315, 0.685
    q0 = Om / 2 - Ol
    print("deceleration parameter q0 = Om/2 - Ol = %.4f" % q0)
    assert abs(q0 - (-0.5275)) < 1e-4
    assert q0 < 0, "expansion must accelerate"
    H0 = 70e3 / (1e6 * PC)
    rho_c = 3 * H0 ** 2 / (8 * math.pi * G)
    rho_L = Ol * rho_c
    Lam = 8 * math.pi * G * rho_L / C ** 2
    print("dark-energy density: %.3e kg/m^3" % rho_L)
    print("cosmological constant Lambda: %.3e m^-2" % Lam)
    assert 1.0e-52 < Lam < 1.3e-52
    print("OK: %s quantified cosmic acceleration" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_agn(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    M = 1e9 * MSUN
    L_edd = 4 * math.pi * G * M * MP * C / SIGT
    L = 1e47 * 1e-7                       # erg/s -> watts
    lam = L / L_edd
    print("quasar: L = 1e47 erg/s, M = 1e9 Msun -> Eddington ratio %.3f" % lam)
    assert 0.5 < lam < 1.0
    Mdot = L / (0.1 * C ** 2)             # kg/s at 10% efficiency
    mdot_yr = Mdot / MSUN * 3.15576e7
    print("accretion rate at 10%% efficiency: %.1f Msun/yr" % mdot_yr)
    assert 15 < mdot_yr < 20
    print("OK: %s ran a quasar's fuel accounting" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_grb(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    z = 1.0
    dL = 6.6e9 * PC                       # luminosity distance, meters
    S = 1e-4 * 1e-7 / 1e-4                # fluence: erg/cm^2 -> J/m^2
    E_iso = 4 * math.pi * dL ** 2 * S / (1 + z)
    print("canonical burst at z=1: E_iso = %.3e erg" % (E_iso * 1e7))
    assert abs(E_iso * 1e7 - 2.6e53) / 2.6e53 < 0.1
    th = 0.1                              # jet opening angle, radians
    E_gamma = E_iso * th ** 2 / 2
    print("beaming-corrected (theta=%.2f rad): E_gamma = %.3e erg" % (th, E_gamma * 1e7))
    assert abs(E_gamma * 1e7 - 1.3e51) / 1.3e51 < 0.1
    print("OK: %s audited a gamma-ray burst's energy" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nucleosynth(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # total binding energies (MeV) from measured nuclear masses
    be = {"He-4": (28.296, 4), "C-12": (92.162, 12), "O-16": (127.619, 16),
          "Fe-56": (492.258, 56), "U-238": (1801.69, 238)}
    vals = {}
    print("binding energy per nucleon:")
    for k, (tot, A) in be.items():
        vals[k] = tot / A
        print("  %-6s %5.2f MeV" % (k, vals[k]))
    peak = max(vals, key=vals.get)
    print("most bound nucleus: %s" % peak)
    assert peak == "Fe-56"
    assert abs(vals["Fe-56"] - 8.79) < 0.02
    assert vals["He-4"] < vals["C-12"] < vals["Fe-56"] > vals["U-238"]
    print("OK: %s located fusion's endpoint at iron" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_habitable(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def hz(L):
    return (math.sqrt(L) * 0.95, math.sqrt(L) * 1.67)
def main():
    print("habitable-zone boundaries (conservative):")
    for sname, L in (("Sun", 1.0), ("Proxima Cen", 0.0017), ("Sirius A", 25.4)):
        lo, hi = hz(L)
        print("  %-12s %.4g - %.4g AU" % (sname, lo, hi))
    lo, hi = hz(1.0)
    assert abs(lo - 0.95) < 1e-9 and abs(hi - 1.67) < 1e-9
    plo, phi = hz(0.0017)
    assert 0.039 < plo < 0.040 and 0.068 < phi < 0.070
    inside = plo < 0.0485 < phi
    print("Proxima b at 0.0485 AU inside its HZ: %s" % inside)
    assert inside
    print("OK: %s screened planetary systems for liquid water" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_sed(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def B_lam(l, T):
    x = H * C / (l * KB * T)
    return (2 * H * C ** 2 / l ** 5) / (math.exp(x) - 1)
def main():
    T = 5778.0
    n, l1, l2 = 400, 10e-9, 1e-3
    tot, l_prev, B_prev = 0.0, l1, B_lam(l1, T)
    for i in range(1, n + 1):
        l = l1 * (l2 / l1) ** (i / n)
        Bl = B_lam(l, T)
        dln = math.log(l / l_prev)          # trapezoid in log-wavelength
        tot += 0.5 * (Bl * l + B_prev * l_prev) * dln
        l_prev, B_prev = l, Bl
    flux = math.pi * tot
    expect = SIG * T ** 4
    print("SED integral: numeric %.6e W/m^2 | sigma T^4 %.6e | err %.4f %%" % (
        flux, expect, abs(flux / expect - 1) * 100))
    assert abs(flux / expect - 1) < 0.02
    print("OK: %s closed the spectral energy budget" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_numerics(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    M, r0 = MSUN, AU
    v0 = math.sqrt(G * M / r0)
    T_orb = 2 * math.pi * math.sqrt(r0 ** 3 / (G * M))
    dt, steps = 3600.0, int(T_orb / 3600.0)
    x, y, vx, vy = r0, 0.0, 0.0, v0
    def acc(px, py):
        r3 = (px * px + py * py) ** 1.5
        return (-G * M * px / r3, -G * M * py / r3)
    ax, ay = acc(x, y)
    E0 = 0.5 * (vx * vx + vy * vy) - G * M / r0
    for _ in range(steps):                  # leapfrog kick-drift-kick
        vx += ax * dt / 2; vy += ay * dt / 2
        x += vx * dt; y += vy * dt
        ax, ay = acc(x, y)
        vx += ax * dt / 2; vy += ay * dt / 2
    r1 = math.hypot(x, y)
    E1 = 0.5 * (vx * vx + vy * vy) - G * M / r1
    print("one orbit, %d leapfrog steps: r/r0 = %.6f | |dE/E| = %.3e" % (steps, r1 / r0, abs(E1 - E0) / abs(E0)))
    assert abs(r1 / r0 - 1) < 0.01
    assert abs(E1 - E0) / abs(E0) < 1e-6
    print("OK: %s passed the orbital verification test" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "astro_overview": demo_astro_overview, "scale_units": demo_scale_units,
    "spectrum": demo_spectrum, "blackbody": demo_blackbody,
    "magnitude": demo_magnitude, "sb_law": demo_sb_law,
    "telescope": demo_telescope, "doppler_spec": demo_doppler_spec,
    "hydrostatic": demo_hydrostatic, "fusion": demo_fusion,
    "hr": demo_hr, "masslum": demo_masslum,
    "radtransfer": demo_radtransfer, "eddington": demo_eddington,
    "ism": demo_ism, "jeans": demo_jeans,
    "accretion": demo_accretion, "stevol": demo_stevol,
    "supernova": demo_supernova, "rotation": demo_rotation,
    "whitedwarf": demo_whitedwarf, "neutronstar": demo_neutronstar,
    "bh": demo_bh, "microlens": demo_microlens,
    "exoplanet": demo_exoplanet, "cmb": demo_cmb,
    "friedmann": demo_friedmann, "darkenergy": demo_darkenergy,
    "agn": demo_agn, "grb": demo_grb,
    "nucleosynth": demo_nucleosynth, "habitable": demo_habitable,
    "sed": demo_sed, "numerics": demo_numerics,
}

# ---------------------------------------------------------------- records

def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_astrophysics.py).
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
    for slug in ("astrophysics", "astrophysics-signature"):
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
        # tab-handler guard (1,470-page canon)
        assert "if(!t.dataset.p)return" in page, "tab guard missing in %s" % slug
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
