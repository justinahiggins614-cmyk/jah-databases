#!/usr/bin/env python3
"""Build the Nanophotonics field databases for JAH Databases (field #30, taxonomy order).

Verified 2026-10-17 (see entries_nanophotonics.py docstring): NO database
covers the nanophotonics discipline. Manifest search (2360 databases):
nearest neighbors are 'optics' (10,002 general-optics records), 'nanotech'
(10,001 general-nanotechnology records), 'photonics-engineers' /
'photonics-technicians' (people/career records), and
'optical-imaging-inspection' (31 inspection records). Whole-system title
sweep over all 759 shard indexes (1,129,517 records): nanophotonics
discipline terms hit exactly 3 records - a quantum-dot computing record and
a holographic-storage data-type record with incidental wording. ZERO
full-record discipline coverage anywhere.

So this build creates two NEW databases, 34 ladder-ordered records each,
covering ONLY what the system left uncovered (nanoscale light-matter
interaction):

  nanophotonics              - The Nanophotonics Database
                               (public-harvest: real, fact-checked
                               nanophotonics; standard references Novotny &
                               Hecht 'Principles of Nano-Optics', Maier
                               'Plasmonics', Prasad 'Nanophotonics',
                               Joannopoulos et al. 'Photonic Crystals')
  nanophotonics-signature    - The Nanophotonics Signature Database
                               (his original Signature interpretation;
                               src signature, titles suffixed
                               " (Signature Edition)", never presented as
                               authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable,
stdlib-only Python; machine-executed OK). Nanophotonics demos: scale ladder;
photon energy; diffraction limit; Drude sign flip; Snell/critical angle;
V-number; SPP dispersion; LSPR Frohlich interpolation; Brus quantum dots;
Bragg period; Bragg-mirror reflectance; slot-waveguide enhancement; optical
antenna scaling; metasurface steering; evanescent depth; Purcell factor;
whispering-gallery FSR/lifetime; plasmonic waveguide length; strong-coupling
race; g2(0); biosensor shift; SERS fourth power; Yablonovitch trapping;
nanolaser threshold gain; negative refraction; silicon ring; graphene
plasmon compression; slow-light delay; SHG/Kerr; SSH bands; HOM dip;
thermal band fraction; grating inverse design; PT-dimer exceptional point.

Subtitle disambiguation (fields #13-29 pattern): specialty titles carry
teaching-focused subtitles rather than bare cards, e.g. "Surface Plasmons:
Light Riding the Skin of a Metal".

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
# main repo (per task). Fields past the gate index were cross-checked
# directly (see docstring) - subtitle disambiguation used throughout.
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_nanophotonics import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of nanophotonics: "
                "clearly labeled Signature-made, never presented as authentic "
                "public record.")
    pub_line = ("Public records - real, fact-checked nanophotonics: what nanophotonics is; "
                "light as wave and photon; the diffraction limit; material response (Drude); "
                "refractive index; waveguides and confinement; surface plasmons; localized "
                "plasmon resonance; quantum dots; photonic crystals; photonic bandgaps; "
                "subwavelength waveguides; optical nano-antennas; metasurfaces; near-field "
                "optics; the Purcell effect; whispering-gallery resonators; plasmonic "
                "waveguides; strong coupling and cavity QED; single-photon sources; "
                "nanophotonic biosensing; surface-enhanced Raman; light trapping for solar; "
                "nanolasers and spasers; negative-index metamaterials; nanoscale silicon "
                "photonics; 2D-material photonics; slow light; nonlinear nanophotonics; "
                "topological photonics; integrated quantum nanophotonics; thermal emission "
                "control; inverse design; non-Hermitian photonics, organized "
                "in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what nanophotonics "
              "is, light as wave and photon, the diffraction limit, material response, "
              "refractive index, confinement) -> Compounded (plasmons, localized plasmon "
              "resonance, quantum dots, photonic crystals, bandgaps, subwavelength "
              "waveguides, nano-antennas, metasurfaces, near-field optics, Purcell effect, "
              "whispering-gallery resonators, plasmonic waveguides) -> Advanced (strong "
              "coupling, single-photon sources, biosensing, SERS, solar light trapping, "
              "nanolasers, negative-index metamaterials, silicon photonics, 2D materials, "
              "slow light, nonlinear, topological, integrated quantum, thermal emission, "
              "inverse design, non-Hermitian photonics).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search plasmons, metasurfaces, Purcell, photonic crystals, quantum dots, nanolasers...",
        "chat_ph": "Ask about nanophotonics...",
        "archive_blurb": ("Seeded %s nanophotonics records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled nanophotonics studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about nanophotonics - from what it is through light as wave and photon, the diffraction limit, material response, refractive index, confinement, plasmons, quantum dots, photonic crystals, nano-antennas, metasurfaces, near-field optics, the Purcell effect, resonators, strong coupling, single photons, biosensing, nanolasers, metamaterials, silicon photonics, 2D materials, slow light, nonlinear and topological photonics, inverse design, and non-Hermitian photonics." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "nanophotonics-study", "gen_demo_kind": "nanophotonics-demo",
        "source": source,
    }

CIT_PUB = ("Nanophotonics (standard texts: Novotny & Hecht 'Principles of Nano-Optics' 2nd ed. "
           "2012; Maier 'Plasmonics: Fundamentals and Applications' 2007; Prasad 'Nanophotonics' "
           "2004; Joannopoulos et al. 'Photonic Crystals: Molding the Flow of Light' 2nd ed. 2008; "
           "Saleh & Teich 'Fundamentals of Photonics' 3rd ed. 2019; Bohren & Huffman 'Absorption "
           "and Scattering of Light by Small Particles' 1983; Kreibig & Vollmer 'Optical "
           "Properties of Metal Clusters' 1995; Raether 'Surface Plasmons' 1988; Loudon 'The "
           "Quantum Theory of Light' 3rd ed. 2000; Walls & Milburn 'Quantum Optics' 2nd ed. 2008; "
           "Boyd 'Nonlinear Optics' 3rd ed. 2008).")
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["nanophotonics"] = _cfg(
    "nanophotonics", "The Nanophotonics Database",
    "Real, fact-checked nanophotonics: from what nanophotonics is through light as wave and "
    "photon, the diffraction limit, material response, refractive index, and confinement, "
    "through plasmons, quantum dots, photonic crystals, nano-antennas, metasurfaces, "
    "near-field optics, the Purcell effect, and resonators, to strong coupling, single-photon "
    "sources, biosensing, nanolasers, metamaterials, silicon photonics, 2D materials, slow "
    "light, nonlinear and topological photonics, inverse design, and non-Hermitian photonics "
    "- taught progressively along the ladder.",
    "nanophotonics record", "JAH-NPH-", "JAH Nanophotonics Archivist",
    "nanophotonics archivist - nanoscale light-matter interaction: diffraction limit, Drude "
    "response, waveguides, plasmons, quantum dots, photonic crystals and bandgaps, "
    "nano-antennas, metasurfaces, near-field optics, Purcell effect, whispering-gallery and "
    "plasmonic resonators, strong coupling / cavity QED, single-photon sources, nanophotonic "
    "biosensing, SERS, solar light trapping, nanolasers, negative-index metamaterials, "
    "silicon photonics, 2D-material photonics, slow light, nonlinear and topological "
    "photonics, integrated quantum nanophotonics, thermal emission control, inverse design, "
    "non-Hermitian photonics; teaching progressively along the ladder from foundations "
    "through compounded to advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only the system's own archive data",
    CIT_PUB, "public")
DBCFG["nanophotonics-signature"] = _cfg(
    "nanophotonics-signature", "The Nanophotonics Signature Database",
    "His original Signature interpretation of nanophotonics: the full ladder from what "
    "nanophotonics is through light, limits, materials, confinement, plasmons, dots, "
    "crystals, antennas, metasurfaces, cavities, quantum light, sensing, lasers, "
    "metamaterials, chips, and the frontiers, reframed as Signature science. Clearly "
    "labeled Signature-made, never presented as authentic public record.",
    "nanophotonics record", "JAH-NPS-", "JAH Nanophotonics Archivist (Signature)",
    "nanophotonics archivist - Signature editions: his original Signature "
    "interpretation of nanophotonics, clearly labeled Signature-made and "
    "never presented as authentic public record; teaches progressively along the "
    "ladder from foundations through compounded to advanced; answers from many "
    "angles - definition, example, analogy, application, history, math, how-to - "
    "using only the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# nanophotonics computation for its record. All are machine-executed by main().

_PREAMBLE = (
"import math\n"
)

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_np_what_is(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the scale ladder: atoms, nanostructures, wavelengths
    atom_d = 0.1                      # nm, typical atomic diameter
    lam = 550.0                       # nm, green light
    atoms_per_wave = lam / atom_d
    nano_lo, nano_hi = 10.0, 500.0    # nm, nanophotonics structure range
    print("one green wavelength spans %.0f atoms" % atoms_per_wave)
    print("nanophotonic structures: %.0f-%-3.0f nm - between the atom and the wave" % (nano_lo, nano_hi))
    print("a 50 nm feature is %.1f%% of the wavelength: the ray picture is dead here" % (50.0 / lam * 100))
    assert atoms_per_wave == 5500.0
    assert 50.0 / lam < 0.10
    print("rule: when the structure is the size of the wave, the wave obeys the structure")
    print("OK: %s walked the scale ladder" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_light_wave(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # E = hc/lambda: the photon energy behind every color
    c = 299792458.0
    h = 6.62607015e-34
    eV = 1.602176634e-19
    for lam_nm, lo, hi in ((400, 3.09, 3.11), (532, 2.32, 2.34), (700, 1.76, 1.78)):
        lam = lam_nm * 1e-9
        f = c / lam
        E_eV = h * f / eV
        print("%d nm: f = %.3e Hz, E = %.3f eV" % (lam_nm, f, E_eV))
        assert lo < E_eV < hi, (lam_nm, E_eV)
    print("rule: 1240/lambda(nm) = eV - memorize it, it never leaves you")
    print("OK: %s weighed the photons" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_diffraction_limit(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Abbe and Rayleigh: the wall every lens hits
    lam, NA = 550.0, 1.4
    d_abbe = lam / (2.0 * NA)
    d_rayleigh = 0.61 * lam / NA
    feature = 50.0
    print("Abbe limit at 550 nm, NA 1.4: %.1f nm" % d_abbe)
    print("Rayleigh limit: %.1f nm" % d_rayleigh)
    print("a 50 nm feature is %.1fx below Abbe: invisible to any lens" % (d_abbe / feature))
    assert abs(d_abbe - 196.43) < 0.1, d_abbe
    assert abs(d_rayleigh - 239.64) < 0.1, d_rayleigh
    print("rule: the limit taxes travelers, not residents - stay in the near field")
    print("OK: %s measured the wall" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_materials_response(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Drude model: epsilon = 1 - (wp/w)^2; the sign flip that makes plasmonics
    c = 299792458.0
    hbar_eVs = 6.582119569e-16          # hbar in eV s
    wp = 9.03 / hbar_eVs                # gold plasma frequency, rad/s
    def re_eps(lam_nm):
        w = 2.0 * math.pi * c / (lam_nm * 1e-9)
        return 1.0 - (wp / w) ** 2
    e532 = re_eps(532.0)
    e137 = re_eps(1240.0 / 9.03)        # the plasma wavelength itself
    e100 = re_eps(100.0)
    print("Re(eps) gold at 532 nm: %.2f (negative: plasmonic)" % e532)
    print("Re(eps) at 137 nm (plasma edge): %.3f (the sign flip)" % e137)
    print("Re(eps) at 100 nm: %.3f (positive: transparent)" % e100)
    assert -14.1 < e532 < -13.9, e532
    assert abs(e137) < 0.02, e137
    assert 0.45 < e100 < 0.49, e100
    print("note: free-electron estimate; interband absorption shifts real gold")
    print("rule: negative epsilon is the visa stamp for plasmon country")
    print("OK: %s flipped the sign" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_refractive_index(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Snell, total internal reflection, Fresnel toll, Brewster
    n1, n2 = 1.5, 1.0
    theta_c = math.degrees(math.asin(n2 / n1))
    R = ((n1 - n2) / (n1 + n2)) ** 2
    theta_b = math.degrees(math.atan(n2 / n1))
    theta2 = math.degrees(math.asin(math.sin(math.radians(45.0)) / n1))
    print("glass->air critical angle: %.2f deg" % theta_c)
    print("normal-incidence toll: %.1f%%" % (R * 100))
    print("Brewster angle: %.2f deg; 45 deg in air -> %.2f deg in glass" % (theta_b, theta2))
    assert abs(theta_c - 41.81) < 0.02, theta_c
    assert abs(R - 0.04) < 1e-9, R
    assert abs(theta_b - 33.69) < 0.02, theta_b
    assert abs(theta2 - 28.13) < 0.02, theta2
    print("rule: every interface charges 4%%; total internal reflection charges nothing")
    print("OK: %s bent the light" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_confinement(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # V-number: single mode below 2.405, a crowd above
    def V(a, lam, NA):
        return (2.0 * math.pi * a / lam) * NA
    v1 = V(4e-6, 1550e-9, 0.14)
    v2 = V(25e-6, 850e-9, 0.22)
    modes = v2 ** 2 / 2.0
    print("4 um core, NA 0.14, 1550 nm: V = %.2f %s" % (v1, "-> SINGLE MODE" if v1 < 2.405 else ""))
    print("25 um core, NA 0.22, 850 nm: V = %.1f -> ~%.0f modes" % (v2, modes))
    assert v1 < 2.405 and abs(v1 - 2.27) < 0.02, v1
    assert 40.0 < v2 < 41.0 and 820.0 < modes < 835.0, (v2, modes)
    print("rule: one mode is a promise; 826 modes are a crowd")
    print("OK: %s counted the modes" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_plasmons(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
import cmath
def main():
    # SPP dispersion on gold at 633 nm: bound, slowed, short-lived
    lam = 633e-9
    eps_m = -11.8 + 1.3j
    eps_d = 1.0
    f = eps_m * eps_d / (eps_m + eps_d)
    n_eff = cmath.sqrt(f)
    k0 = 2.0 * math.pi / lam
    lam_spp = lam / n_eff.real
    L = 1.0 / (2.0 * (k0 * n_eff).imag)
    print("n_eff = %.4f + %.5fi" % (n_eff.real, n_eff.imag))
    print("plasmon wavelength: %.0f nm (light was 633 nm)" % (lam_spp * 1e9))
    print("propagation length: %.1f um - the price of the squeeze" % (L * 1e6))
    assert 1.044 < n_eff.real < 1.046, n_eff
    assert 605.0 < lam_spp * 1e9 < 607.0, lam_spp
    assert 9.0 < L * 1e6 < 10.2, L
    print("rule: tighter than light, briefer than light - the plasmon bargain")
    print("OK: %s rode the metal skin" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_lspr(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Frohlich condition Re(eps) = -2*eps_d: the color follows the medium
    # representative measured-style gold permittivities (lambda nm, Re eps)
    table = [(450, -1.4), (500, -2.7), (520, -4.1), (550, -5.5), (600, -8.0)]
    def resonance(eps_d):
        target = -2.0 * eps_d
        for (l1, e1), (l2, e2) in zip(table, table[1:]):
            if (e1 - target) * (e2 - target) <= 0:
                frac = (target - e1) / (e2 - e1)
                return l1 + frac * (l2 - l1)
        raise ValueError("no bracket")
    lam_water = resonance(1.77)     # water n = 1.33
    lam_air = resonance(1.0)
    print("Au sphere resonance in water: %.1f nm" % lam_water)
    print("Au sphere resonance in air:   %.1f nm" % lam_air)
    print("red shift on wetting: %.1f nm - the whole basis of plasmonic sensing" % (lam_water - lam_air))
    assert abs(lam_water - 512.0) < 0.5, lam_water
    assert abs(lam_air - 473.08) < 0.5, lam_air
    print("rule: the particle's color is the medium's confession")
    print("OK: %s tuned the bell" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_quantum_dots(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Brus equation: size sets the color (CdSe parameters)
    h = 6.62607015e-34
    m0 = 9.10938356e-31
    e = 1.602176634e-19
    eps0 = 8.854187817e-12
    Eg, me, mh, epsr = 1.74, 0.13, 0.45, 10.2
    def emission(R):
        conf = h ** 2 / (8.0 * R ** 2) * (1.0 / (me * m0) + 1.0 / (mh * m0)) / e
        coul = 1.8 * e ** 2 / (4.0 * math.pi * epsr * eps0 * R) / e
        E = Eg + conf - coul
        return E, 1240.0 / E
    E2, l2 = emission(2e-9)
    E3, l3 = emission(3e-9)
    print("R = 2 nm: %.3f eV -> %.0f nm (blue-green)" % (E2, l2))
    print("R = 3 nm: %.3f eV -> %.0f nm (orange)" % (E3, l3))
    assert 2.54 < E2 < 2.55 and 486.0 < l2 < 489.0, (E2, l2)
    assert 2.06 < E3 < 2.08 and 597.0 < l3 < 601.0, (E3, l3)
    print("rule: one chemistry, every color - geometry is the paintbox")
    print("OK: %s sized the rainbow" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_photonic_crystals(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Bragg period and quarter-wave stack thicknesses
    lam1, lam2 = 1550.0, 550.0
    n_eff = 2.0
    L1 = lam1 / (2.0 * n_eff)
    L2 = lam2 / (2.0 * n_eff)
    nH, nL = 2.4, 1.46
    dH = lam1 / (4.0 * nH)
    dL = lam1 / (4.0 * nL)
    print("Bragg period for 1550 nm (n_eff=2): %.1f nm" % L1)
    print("Bragg period for 550 nm: %.1f nm" % L2)
    print("quarter-wave TiO2/SiO2 at 1550 nm: %.1f / %.1f nm" % (dH, dL))
    assert abs(L1 - 387.5) < 0.1 and abs(L2 - 137.5) < 0.1
    assert abs(dH - 161.46) < 0.05 and abs(dL - 265.41) < 0.05
    print("rule: half-wave spacing makes a thousand weak mirrors march as one")
    print("OK: %s stacked the crystal" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_bandgaps(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # quarter-wave Bragg mirror: reflectance from the index ratio alone
    r = 2.4 / 1.46
    def R(N):
        x = r ** (2 * N)
        return ((x - 1.0) / (x + 1.0)) ** 2
    R6, R10 = R(6), R(10)
    print("6 pairs TiO2/SiO2: R = %.4f (%.2f%%)" % (R6, R6 * 100))
    print("10 pairs: R = %.6f (%.4f%%)" % (R10, R10 * 100))
    assert 0.989 < R6 < 0.991, R6
    assert 0.9997 < R10 < 0.9999, R10
    print("rule: no metal, no absorption - just interference, 99.98%% of it")
    print("OK: %s forbade the color" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_subwavelength_waveguides(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # slot waveguide: D-continuity squeezes light into the gap
    n_si = 3.48
    enh_air = (n_si / 1.0) ** 2
    enh_sio2 = (n_si / 1.44) ** 2
    lam, slot = 1550.0, 50.0
    print("air slot field jump: %.1fx; intensity: %.0fx" % (enh_air, enh_air ** 2))
    print("oxide slot field jump: %.2fx; intensity: %.1fx" % (enh_sio2, enh_sio2 ** 2))
    print("50 nm slot at 1550 nm: lambda/%.0f channel carrying the mode" % (lam / slot))
    assert abs(enh_air - 12.11) < 0.02, enh_air
    assert abs(enh_sio2 - 5.84) < 0.02, enh_sio2
    print("rule: the boundary condition focuses better than any lens")
    print("OK: %s squeezed the mode" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_nano_antennas(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # half-wave dipole, plasmonically shortened; radio vs optical
    lam_opt = 800.0
    n_eff = 2.0
    L_opt = lam_opt / (2.0 * n_eff)          # nm
    f_rf = 100e6
    L_rf = 299792458.0 / f_rf / 2.0         # m
    geo = L_opt ** 2
    capture = lam_opt ** 2 / 4.0
    print("800 nm optical dipole: %.0f nm of gold" % L_opt)
    print("100 MHz radio dipole: %.1f m of aluminum" % L_rf)
    print("scale ratio: %.1e - same physics, different universe" % (L_rf / (L_opt * 1e-9)))
    print("capture area %.0f nm^2 vs geometric %.0f nm^2: %.1fx the metal" % (capture, geo, capture / geo))
    assert L_opt == 200.0
    assert abs(L_rf - 1.5) < 0.01
    assert abs(capture / geo - 4.0) < 1e-9
    print("rule: resonance, not size, sets the catch")
    print("OK: %s raised the tower" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_metasurfaces(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # generalized Snell: a phase gradient steers; a phase map focuses
    lam = 800e-9
    period = 2e-6
    dphi_dx = 2.0 * math.pi / period
    sin_t = (lam / (2.0 * math.pi)) * dphi_dx
    theta = math.degrees(math.asin(sin_t))
    f, r = 100e-6, 50e-6
    lam2 = 532e-9
    phi = -(2.0 * math.pi / lam2) * (math.sqrt(r ** 2 + f ** 2) - f)
    phi_wrapped = phi % (2.0 * math.pi)
    print("phase gradient period 2 um bends 800 nm light to %.1f deg" % theta)
    print("metalens (f=100 um) phase at r=50 um: %.2f rad -> %.2f rad wrapped" % (phi, phi_wrapped))
    assert 23.5 < theta < 23.7, theta
    assert -1.3 < (phi_wrapped - 2.0 * math.pi) < -1.0 or -1.3 < phi_wrapped < -1.0, phi_wrapped
    print("rule: the flat sheet decides; the light obeys")
    print("OK: %s printed the lens" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_near_field(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # evanescent penetration depth: the near field's short leash
    n1, n2 = 1.5, 1.0
    theta = math.radians(60.0)
    lam = 500.0
    dp = lam / (2.0 * math.pi * math.sqrt(n1 ** 2 * math.sin(theta) ** 2 - n2 ** 2))
    abbe = lam / (2.0 * 1.4)
    print("penetration depth (glass, 60 deg, 500 nm): %.1f nm" % dp)
    print("NSOM 50 nm aperture beats Abbe %.0f nm by %.1fx" % (abbe, abbe / 50.0))
    assert 95.0 < dp < 97.0, dp
    assert abbe / 50.0 > 3.5
    print("rule: the truth decays in 96 nm - get close or get nothing")
    print("OK: %s read the diary" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_purcell(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Fp = (3/4pi^2)(lambda/n)^3 (Q/V): the cavity hurries the atom
    Q = 1e4
    Fp1 = (3.0 / (4.0 * math.pi ** 2)) * Q        # V = (lambda/n)^3
    Fp10 = Fp1 / 10.0                             # V = 10 (lambda/n)^3
    tau0 = 1e-9
    tau = tau0 / Fp1
    print("Q=1e4, V=(lambda/n)^3: Fp = %.0f" % Fp1)
    print("1 ns emitter -> %.2f ps in the cavity" % (tau * 1e12))
    print("10x larger volume: Fp = %.1f" % Fp10)
    assert 759.0 < Fp1 < 761.0, Fp1
    assert 1.2 < tau * 1e12 < 1.4, tau
    print("rule: the vacuum is engineerable - concentrate it and atoms hurry")
    print("OK: %s hurried the atom" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_wgm(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # whispering gallery: a 50 um bead holding light for 17 metres
    D, n, lam = 50e-6, 1.45, 1550e-9
    c = 299792458.0
    fsr_lam = lam ** 2 / (math.pi * n * D)
    fsr_f = c / (math.pi * n * D)
    m = math.pi * n * D / lam
    Q = 1e8
    omega = 2.0 * math.pi * c / lam
    tau = Q / omega
    path = c * tau / n
    print("FSR: %.2f nm (%.2f THz); mode number ~%.0f" % (fsr_lam * 1e9, fsr_f / 1e12, m))
    print("Q=1e8: photon lives %.1f ns, circles %.1f m" % (tau * 1e9, path))
    assert 10.4 < fsr_lam * 1e9 < 10.7, fsr_lam
    assert 1.31e12 < fsr_f < 1.33e12, fsr_f
    assert 146.0 < m < 148.0, m
    assert 81.0 < tau * 1e9 < 84.0, tau
    assert 16.5 < path < 17.5, path
    print("rule: no mirrors, no ends - the circle is the trap")
    print("OK: %s ran the laps" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_plasmonic_waveguides(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
import cmath
def main():
    # Au SPP at 1550 nm: loosely bound, far-traveling (for a plasmon)
    lam = 1550e-9
    eps_m = -131.9 + 12.65j
    f = eps_m / (eps_m + 1.0)
    n_eff = cmath.sqrt(f)
    k0 = 2.0 * math.pi / lam
    L = 1.0 / (2.0 * (k0 * n_eff).imag)
    print("n_eff = %.5f (barely slower than light: loosely bound)" % n_eff.real)
    print("propagation length: %.0f um" % (L * 1e6))
    assert 1.003 < n_eff.real < 1.005, n_eff
    assert 330.0 < L * 1e6 < 360.0, L
    print("rule: confinement x length is conserved - pick your point on the curve")
    print("OK: %s laid the metal rail" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_strong_coupling(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the race: g vs (kappa+gamma)/2; cooperativity; Rabi splitting
    g, kappa, gamma = 20.0, 30.0, 1.0      # 2pi x GHz
    strong = g > (kappa + gamma) / 2.0
    C = g ** 2 / (kappa * gamma)
    df = 2.0 * g * 1e9                      # Hz splitting
    lam = 900e-9
    dlam = lam ** 2 * df / 299792458.0
    print("g=20 vs (30+1)/2=15.5 GHz: %s" % ("STRONG COUPLING" if strong else "weak"))
    print("cooperativity C = %.1f" % C)
    print("vacuum Rabi splitting: 40 GHz = %.3f nm at 900 nm" % (dlam * 1e9))
    assert strong
    assert 13.0 < C < 14.0, C
    assert 0.10 < dlam * 1e9 < 0.12, dlam
    print("rule: shrink V until g wins - the vacuum does the rest")
    print("OK: %s married atom and photon" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_single_photon(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # g2(0): the beamsplitter never lies about single photons
    side, center, acc = 1000.0, 12.0, 8.0
    g2 = (center - acc) / side
    c_dist, c_ind = 1000.0, 80.0
    V = (c_dist - c_ind) / c_dist
    print("g2(0) = (%.0f-%.0f)/%.0f = %.4f %s" % (center, acc, side, g2, "< 0.5: SINGLE PHOTONS" if g2 < 0.5 else ""))
    print("HOM visibility: %.0f%% indistinguishable" % (V * 100))
    assert abs(g2 - 0.004) < 1e-9, g2
    assert g2 < 0.5
    assert abs(V - 0.92) < 1e-9, V
    print("rule: one excitation, one photon, then dark - antibunching by construction")
    print("OK: %s minted the honest coin" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_biosensing(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Delta_lambda = S * Delta_n: watching molecules land
    S_lspr, S_spr = 200.0, 3000.0           # nm/RIU
    dn = 0.005                               # protein monolayer
    dl_lspr = S_lspr * dn
    dl_spr = S_spr * dn
    resol = 0.02                             # spectrometer resolution, nm
    dn_min = resol / S_lspr
    fom = S_lspr / 80.0                      # / FWHM
    print("protein layer: LSPR shifts %.1f nm, SPR shifts %.0f nm" % (dl_lspr, dl_spr))
    print("detection limit: %.0e RIU" % dn_min)
    print("figure of merit S/FWHM: %.1f" % fom)
    assert abs(dl_lspr - 1.0) < 1e-9 and abs(dl_spr - 15.0) < 1e-9
    assert abs(dn_min - 1e-4) < 1e-12, dn_min
    assert abs(fom - 2.5) < 1e-9, fom
    print("rule: no label, no dye - the molecule confesses by slowing light")
    print("OK: %s weighed the ghosts" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_sers(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # |E/E0|^4: the fourth power that hears single molecules
    ef30 = 30.0 ** 4
    ef100 = 100.0 ** 4
    conc = 1e-9           # mol/L (1 nM)
    vol = 1e-15           # L (femtoliter hotspot)
    NA = 6.02214076e23
    n_mol = conc * vol * NA
    print("30x field -> %.0f x Raman signal" % ef30)
    print("100x field -> %.0e x: single molecules" % ef100)
    print("1 nM in 1 fL: %.2f molecules on average" % n_mol)
    assert ef30 == 810000.0
    assert ef100 == 1e8
    assert 0.60 < n_mol < 0.61, n_mol
    print("rule: two powers in, two powers out - the whisper becomes a shout")
    print("OK: %s built the concert hall" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_solar_trapping(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Yablonovitch 4n^2: geometry drinks what thickness cannot
    n = 3.5
    enh = 4.0 * n ** 2
    alpha = 64.0            # /cm at 1000 nm
    d = 2e-4                # cm
    A1 = 1.0 - math.exp(-alpha * d)
    A2 = 1.0 - math.exp(-alpha * d * enh)
    print("4n^2 path enhancement: %.0fx" % enh)
    print("2 um Si at 1000 nm: %.2f%% single pass -> %.1f%% trapped" % (A1 * 100, A2 * 100))
    print("gain: %.1fx from geometry alone" % (A2 / A1))
    assert enh == 49.0
    assert 0.012 < A1 < 0.014, A1
    assert 0.46 < A2 < 0.47, A2
    assert 36.0 < A2 / A1 < 38.0
    print("rule: teach the photons to swim in circles, not to buy more silicon")
    print("OK: %s trapped the sun" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_nanolasers(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # threshold gain g_th = 2pi n/(lambda Q): the price of tiny
    n, lam, Q = 1.5, 600e-9, 100.0
    g_th = 2.0 * math.pi * n / (lam * Q)     # per metre
    V_spaser = (10e-9) ** 3
    V_diff = (lam / (2.0 * n)) ** 3
    print("threshold gain at Q=100, 600 nm: %.0f /cm of material gain" % (g_th / 100.0))
    print("spaser mode volume: %.0e m^3 vs diffraction %.0e m^3 (%.0fx smaller)" % (V_spaser, V_diff, V_diff / V_spaser))
    assert 1560.0 < g_th / 100.0 < 1585.0, g_th
    assert abs(V_diff / V_spaser - 8000.0) < 1.0
    print("rule: small, fast, hungry - beta->1 and the threshold kink vanishes")
    print("OK: %s lit the speck" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_negative_index(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # n = -sqrt(eps*mu): refraction to the SAME side of the normal
    def refract(n, deg):
        st = math.sin(math.radians(deg)) / n
        return math.degrees(math.asin(st))
    t1 = refract(-1.0, 30.0)
    t2 = refract(-1.5, 20.0)
    print("30 deg onto n=-1: refracts to %.1f deg (same side!)" % t1)
    print("20 deg onto n=-1.5: refracts to %.2f deg" % t2)
    assert abs(t1 + 30.0) < 1e-9, t1
    assert abs(t2 + 13.18) < 0.02, t2
    print("rule: flip both signs and the ray comes home backwards")
    print("OK: %s bent light backwards" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_silicon_photonics(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # microring: FSR, Q, and the 2 dB/cm budget
    R, ng, lam = 10e-6, 4.2, 1550e-9
    fsr = lam ** 2 / (ng * 2.0 * math.pi * R)
    Q = 1550.0 / 0.01
    T = 10.0 ** (-2.0 * 1.0 / 10.0)      # 2 dB/cm over 1 cm
    print("10 um ring at 1550 nm: FSR %.2f nm" % (fsr * 1e9))
    print("0.01 nm linewidth -> Q = %.0f" % Q)
    print("2 dB/cm guide, 1 cm: %.1f%% survives" % (T * 100))
    assert 9.0 < fsr * 1e9 < 9.2, fsr
    assert Q == 155000.0
    assert 0.63 < T < 0.632, T
    print("rule: the ring is a filter, a modulator, and a sensor - pick your coupling")
    print("OK: %s wired the chip" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_graphene(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # graphene plasmon compression: (2*alpha/pi)*(E_F/hbar*w), tunable by gate
    alpha = 1.0 / 137.036
    hbar_w = 0.124                       # eV, 10 um light
    def lam_p(Ef):
        return 10000.0 * (2.0 * alpha / math.pi) * (Ef / hbar_w)
    lp05 = lam_p(0.5)
    lp02, lp08 = lam_p(0.2), lam_p(0.8)
    print("10 um light, E_F=0.5 eV: plasmon %.0f nm (%.0fx compression)" % (lp05, 10000.0 / lp05))
    print("gate to 0.2 eV: %.0f nm; gate to 0.8 eV: %.0f nm" % (lp02, lp08))
    assert 185.0 < lp05 < 190.0, lp05
    assert 73.0 < lp02 < 77.0 and 297.0 < lp08 < 303.0, (lp02, lp08)
    print("rule: one atom thick, and the infrared answers to a volt")
    print("OK: %s tuned flatland" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_slow_light(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # n_g = 20 over 1 mm: the pulse arrives late and dense
    c = 299792458.0
    ng, L = 20.0, 1e-3
    tau = L * ng / c
    vg = c / ng
    pulse = 10e-12
    len_vac, len_slow = c * pulse, vg * pulse
    print("delay over 1 mm at n_g=20: %.1f ps" % (tau * 1e12))
    print("10 ps pulse: %.1f mm in vacuum -> %.0f um slowed (%.0fx denser)" % (len_vac * 1e3, len_slow * 1e6, len_vac / len_slow))
    assert 66.0 < tau * 1e12 < 68.0, tau
    assert abs(len_vac / len_slow - 20.0) < 1e-9
    print("rule: flat bands brake photons; density pays for nonlinearity")
    print("OK: %s braked the photon" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_nonlinear(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # SHG ~ I^2; coherence length; Kerr phase
    pump_gain, shg_gain = 4.0, 4.0 ** 2
    lam, dn = 1e-6, 0.01
    dk = 4.0 * math.pi * dn / lam
    Lc = math.pi / dk
    n2, I, L = 3e-20, 1e13, 1.0
    dphi = (2.0 * math.pi / 1.55e-6) * n2 * I * L
    print("4x pump -> %.0fx second harmonic" % shg_gain)
    print("coherence length at Delta_n=0.01, 1 um: %.0f um" % (Lc * 1e6))
    print("Kerr: 1 GW/cm^2 in silica, 1 m -> %.2f rad nonlinear phase" % dphi)
    assert shg_gain == 16.0
    assert abs(Lc - 25e-6) < 1e-9, Lc
    assert 1.21 < dphi < 1.23, dphi
    print("rule: intense light rewrites the material, then the material rewrites the light")
    print("OK: %s changed the rules" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_topological(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # SSH chain: bands, gap, transition, and the winding number
    def bands(t1, t2, n=400):
        Es = []
        for i in range(n + 1):
            k = math.pi * i / n
            E = math.sqrt(t1 ** 2 + t2 ** 2 + 2.0 * t1 * t2 * math.cos(k))
            Es.append(E)
        return Es
    def winding(t1, t2, n=2000):
        tot = 0.0
        prev = None
        for i in range(n + 1):
            k = 2.0 * math.pi * i / n
            a = math.atan2(t2 * math.sin(k), t1 + t2 * math.cos(k))
            if prev is not None:
                d = a - prev
                while d > math.pi: d -= 2.0 * math.pi
                while d < -math.pi: d += 2.0 * math.pi
                tot += d
            prev = a
        return tot / (2.0 * math.pi)
    E1 = bands(1.0, 2.0)
    gap = 2.0 * min(E1)
    Ecrit = bands(1.5, 1.5)
    w_topo = winding(1.0, 2.0)
    w_triv = winding(2.0, 1.0)
    print("t1=1,t2=2: bands +-1..+-3, gap = %.2f" % gap)
    print("t1=t2=1.5: min |E| = %.4f - the gap CLOSES (transition)" % min(Ecrit))
    print("winding: t1<t2 -> %d (topological), t1>t2 -> %d (trivial)" % (round(w_topo), round(w_triv)))
    assert abs(gap - 2.0) < 0.01, gap
    assert min(Ecrit) < 0.05, min(Ecrit)
    assert round(w_topo) == 1 and round(w_triv) == 0, (w_topo, w_triv)
    print("rule: the integer cannot change without closing the gap - that is the armor")
    print("OK: %s counted the winding" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_quantum_integrated(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # HOM dip and the Mach-Zehnder: the two verbs of linear quantum optics
    V = 0.95
    dip = 1.0 - V
    def T(dphi):
        return math.cos(dphi / 2.0) ** 2
    print("HOM 95%% visibility: coincidences fall to %.0f%% at zero delay" % (dip * 100))
    print("MZI: T(0)=%.2f, T(pi/2)=%.2f, T(pi)=%.2f" % (T(0.0), T(math.pi / 2.0), T(math.pi)))
    assert abs(dip - 0.05) < 1e-9, dip
    assert abs(T(0.0) - 1.0) < 1e-9 and abs(T(math.pi / 2.0) - 0.5) < 1e-9 and abs(T(math.pi)) < 1e-9
    print("rule: identical photons bunch; phases program the circuit")
    print("OK: %s wired the entanglement" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_thermal_emission(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Wien + selective emission: how much 1500 K heat sits in 1-2 um
    lam_sun = 2898.0 / 5800.0
    lam_furn = 2898.0 / 1000.0
    h, c, k = 6.62607015e-34, 299792458.0, 1.380649e-23
    T = 1500.0
    def B(lam):
        x = h * c / (lam * k * T)
        return (2.0 * h * c ** 2 / lam ** 5) / (math.exp(x) - 1.0)
    N = 4000
    a, b = 1e-6, 2e-6
    s = 0.0
    for i in range(N + 1):
        lam = a + (b - a) * i / N
        w = 0.5 if i in (0, N) else 1.0
        s += w * B(lam)
    # B is spectral radiance (per steradian); exitance = pi * integral
    band = math.pi * s * (b - a) / N
    sigma = 5.670374419e-8
    total = sigma * T ** 4
    frac = band / total
    print("Wien: sun %.0f nm, 1000 K furnace %.2f um" % (lam_sun * 1000, lam_furn))
    print("1500 K emitter: %.1f%% of %.0f W/m^2 sits in 1-2 um" % (frac * 100, total))
    assert 495.0 < lam_sun * 1000 < 505.0, lam_sun
    assert abs(lam_furn - 2.898) < 0.01, lam_furn
    assert 0.25 < frac < 0.27, frac
    print("rule: Kirchhoff lets you tax fire - emit only where the cell can eat")
    print("OK: %s edited the glow" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_inverse_design(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # gradient ascent on a binary grating: the computer finds DC = 0.5
    def eta(dc):
        return (math.sin(math.pi * dc) / math.pi) ** 2
    dc, lr, hh = 0.2, 0.5, 1e-5
    for _ in range(200):
        g = (eta(dc + hh) - eta(dc - hh)) / (2.0 * hh)
        dc = min(0.99, max(0.01, dc + lr * g))
    e = eta(dc)
    print("start DC=0.2 -> converged DC=%.4f, eta_1=%.4f (analytic 0.5 / 0.1013)" % (dc, e))
    assert abs(dc - 0.5) < 0.01, dc
    assert abs(e - 0.101321) < 0.002, e
    print("rule: state the goal honestly; let Maxwell draw the shape")
    print("OK: %s sculpted with gradients" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_non_hermitian(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
import cmath
def main():
    # PT dimer [[i*g,k],[k,-i*g]]: real -> EP -> imaginary
    k = 1.0
    def eig(g):
        return cmath.sqrt(k ** 2 - g ** 2)
    e1, e2, e3 = eig(0.5), eig(1.0), eig(1.5)
    print("gamma=0.5: E = +-%.4f (real: PT unbroken)" % e1.real)
    print("gamma=1.0: E = %.1e (EXCEPTIONAL POINT: coalescence)" % abs(e2))
    print("gamma=1.5: E = +-%.4fi (PT broken: one grows, one dies)" % e3.imag)
    assert abs(e1.real - 0.8660254) < 1e-5 and abs(e1.imag) < 1e-9, e1
    assert abs(e2) < 1e-9, e2
    assert abs(e3.imag - 1.1180340) < 1e-5 and abs(e3.real) < 1e-9, e3
    print("rule: at the coalescence the system forgets it was ever two")
    print("OK: %s stood at the exceptional point" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "what_is": demo_np_what_is, "light_wave": demo_np_light_wave,
    "diffraction_limit": demo_np_diffraction_limit,
    "materials_response": demo_np_materials_response,
    "refractive_index": demo_np_refractive_index,
    "confinement": demo_np_confinement, "plasmons": demo_np_plasmons,
    "lspr": demo_np_lspr, "quantum_dots": demo_np_quantum_dots,
    "photonic_crystals": demo_np_photonic_crystals,
    "bandgaps": demo_np_bandgaps,
    "subwavelength_waveguides": demo_np_subwavelength_waveguides,
    "nano_antennas": demo_np_nano_antennas,
    "metasurfaces": demo_np_metasurfaces, "near_field": demo_np_near_field,
    "purcell": demo_np_purcell, "wgm": demo_np_wgm,
    "plasmonic_waveguides": demo_np_plasmonic_waveguides,
    "strong_coupling": demo_np_strong_coupling,
    "single_photon": demo_np_single_photon, "biosensing": demo_np_biosensing,
    "sers": demo_np_sers, "solar_trapping": demo_np_solar_trapping,
    "nanolasers": demo_np_nanolasers,
    "negative_index": demo_np_negative_index,
    "silicon_photonics": demo_np_silicon_photonics,
    "graphene": demo_np_graphene, "slow_light": demo_np_slow_light,
    "nonlinear": demo_np_nonlinear, "topological": demo_np_topological,
    "quantum_integrated": demo_np_quantum_integrated,
    "thermal_emission": demo_np_thermal_emission,
    "inverse_design": demo_np_inverse_design,
    "non_hermitian": demo_np_non_hermitian,
}
assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"


def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_nanophotonics.py).
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
    for slug in ("nanophotonics", "nanophotonics-signature"):
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
