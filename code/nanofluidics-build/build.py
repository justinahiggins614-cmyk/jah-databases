#!/usr/bin/env python3
"""Build the Nanofluidics field databases for JAH Databases (field #33, taxonomy order).

Verified 2026-10-17 (see entries_nanofluidics.py docstring): NO database
covers the nanofluidics discipline (fluid behavior at 1-100 nm:
nanochannels, slip flow, electrokinetics, ion selectivity, electrical
double layers, Debye regimes, electro-osmosis, electrophoresis, streaming
potential, concentration polarization, nanofluidic diodes, osmotic power,
nanopore sensing, DNA translocation, nanofluidic transistors, memristors,
desalination, confined water, CNT ultrafast flow, access resistance,
pressure-driven flow, diffusio-osmosis, steric sieving, ionic circuits,
angstrom slits, lab-on-a-chip, biosensors, fouling, design rules, safety).

Manifest search (2366 databases): zero 'nanofluid*' slugs or names;
nearest neighbors are 'nanotech' (10,001 general-nanotechnology records),
'nanomechanics' (34 nanomechanics records - the mechanics of nanoscale
objects, a different discipline), 'nanocomposites' (34 nanocomposites
records - matrix + filler science), 'nanophotonics' (34 records) - all
different disciplines. Whole-system title sweep over all 766 shard
indexes: zero titles contain 'nanofluid*'. ZERO full-record discipline
coverage anywhere.

So this build creates two NEW databases, 34 ladder-ordered records each:

  nanofluidics              - The Nanofluidics Database
                               (public-harvest: real, fact-checked
                               nanofluidics; standard references
                               Bocquet/Charlaix 'Nanofluidics, from bulk to
                               interfaces' Chem. Soc. Rev. 2010;
                               Schoch/Han/Renaud 'Transport phenomena in
                               nanofluidics' Rev. Mod. Phys. 2008;
                               Eijkel/van den Berg 'Nanofluidics: what is it
                               and what can we expect from it?'
                               Microfluid. Nanofluid. 2005;
                               Stein/Kruithof/Dekker 'Surface-charge-
                               governed ion transport in nanofluidic
                               channels' Phys. Rev. Lett. 2004)
  nanofluidics-signature    - The Nanofluidics Signature Database
                               (his original Signature interpretation;
                               src signature, titles suffixed
                               " (Signature Edition)", never presented as
                               authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Subtitle disambiguation (fields #13-32 pattern): specialty titles carry
teaching-focused subtitles rather than bare cards, e.g. "The Debye Length:
The Ruler of Nanofluidic Regimes".

Numerical cores: see entries_nanofluidics.py docstring (all hand-computed
2026-10-17, machine-verified by the demos; 2 hand-arithmetic slips fixed
before commit: access-resistance share 28% -> 44%, Renkin hindrance
0.155 -> 0.102).

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
from entries_nanofluidics import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of nanofluidics: "
                "clearly labeled Signature-made, never presented as authentic "
                "public record.")
    pub_line = ("Public records - real, fact-checked nanofluidics: what nanofluidics is; "
                "the nanoscale advantage; surface charge and the electrical double layer; "
                "the Debye length; slip flow; fabrication; electro-osmosis; electrophoresis; "
                "overlapping double layers and ion selectivity; streaming potential; surface "
                "conductance; ion concentration polarization; nanofluidic diodes; osmotic "
                "power; electrokinetic energy conversion; nanopore sensing; DNA translocation; "
                "nanofluidic transistors; nanofluidic memristors; desalination membranes; "
                "confined water; carbon nanotube ultrafast flow; access resistance; "
                "pressure-driven flow; diffusio-osmosis; steric sieving; ionic circuits; "
                "angstrom slits; lab-on-a-chip; biosensors; fouling; design rules; safety; "
                "the future of the field, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what nanofluidics "
              "is, the nanoscale advantage, double layer, Debye length, slip flow, "
              "fabrication, electro-osmosis, electrophoresis) -> Compounded (ion selectivity, "
              "streaming potential, surface conductance, concentration polarization, diodes, "
              "osmotic power, energy conversion, nanopore sensing, DNA translocation, "
              "transistors, memristors, desalination) -> Advanced (confined water, nanotube "
              "flow, access resistance, pressure-driven flow, diffusio-osmosis, sieving, "
              "ionic circuits, angstrom slits, lab-on-a-chip, biosensors, fouling, design "
              "rules, safety, future).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search Debye length, electro-osmosis, ion selectivity, nanopore, desalination, slip flow...",
        "chat_ph": "Ask about nanofluidics...",
        "archive_blurb": ("Seeded %s nanofluidics records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled nanofluidics studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about nanofluidics - from what it is through the nanoscale advantage, the double layer, the Debye length, slip flow, fabrication, electro-osmosis, and electrophoresis, through ion selectivity, streaming potential, surface conductance, concentration polarization, diodes, osmotic power, energy conversion, nanopore sensing, DNA translocation, transistors, memristors, and desalination, to confined water, nanotube flow, access resistance, pressure-driven flow, diffusio-osmosis, sieving, ionic circuits, angstrom slits, lab-on-a-chip, biosensors, fouling, design rules, safety, and the future of the field." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "nanofluidics-study", "gen_demo_kind": "nanofluidics-demo",
        "source": source,
    }

CIT_PUB = ("Nanofluidics (standard references: Bocquet/Charlaix 'Nanofluidics, from bulk to "
           "interfaces' Chem. Soc. Rev. 2010; Schoch/Han/Renaud 'Transport phenomena in "
           "nanofluidics' Rev. Mod. Phys. 2008; Eijkel/van den Berg 'Nanofluidics: what is "
           "it and what can we expect from it?' Microfluid. Nanofluid. 2005; "
           "Stein/Kruithof/Dekker 'Surface-charge-governed ion transport in nanofluidic "
           "channels' Phys. Rev. Lett. 2004; Bocquet/Tabeling 'Physics and technological "
           "aspects of nanofluidics' Lab Chip 2014; Bocquet 'Nanofluidics coming of age' "
           "Nature Mater. 2020; Daiguji 'Ion transport in nanofluidic channels' Chem. Soc. "
           "Rev. 2010; Israelachvili 'Intermolecular and Surface Forces' 3rd ed. 2011; "
           "Hunter 'Zeta Potential in Colloid Science' 1981; Probstein 'Physicochemical "
           "Hydrodynamics' 2nd ed. 1994; NIOSH CIB 65 'Occupational Exposure to Carbon "
           "Nanotubes and Nanofibers' 2013).")
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["nanofluidics"] = _cfg(
    "nanofluidics", "The Nanofluidics Database",
    "Real, fact-checked nanofluidics: from what nanofluidics is through the nanoscale "
    "advantage, the double layer, the Debye length, slip flow, fabrication, "
    "electro-osmosis, and electrophoresis, through ion selectivity, streaming potential, "
    "surface conductance, concentration polarization, diodes, osmotic power, energy "
    "conversion, nanopore sensing, DNA translocation, transistors, memristors, and "
    "desalination, to confined water, nanotube flow, access resistance, pressure-driven "
    "flow, diffusio-osmosis, sieving, ionic circuits, angstrom slits, lab-on-a-chip, "
    "biosensors, fouling, design rules, safety, and the future of the field - taught "
    "progressively along the ladder.",
    "nanofluidics record", "JAH-NFD-", "JAH Nanofluidics Archivist",
    "nanofluidics archivist - fluid behavior at 1-100 nm: nanochannels, slip flow, "
    "electrokinetics, ion selectivity, electrical double layers, Debye regimes, "
    "electro-osmosis, electrophoresis, streaming potential, concentration polarization, "
    "nanofluidic diodes, osmotic power, nanopore sensing, DNA translocation, nanofluidic "
    "transistors, memristors, desalination, confined water, CNT ultrafast flow, access "
    "resistance, pressure-driven flow, diffusio-osmosis, steric sieving, ionic circuits, "
    "angstrom slits, lab-on-a-chip, biosensors, fouling, design rules, safety; teaching "
    "progressively along the ladder from foundations through compounded to advanced; "
    "answers from many angles - definition, example, analogy, application, history, "
    "math, how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["nanofluidics-signature"] = _cfg(
    "nanofluidics-signature", "The Nanofluidics Signature Database",
    "His original Signature interpretation of nanofluidics: the full ladder from what "
    "nanofluidics is through scale, charge, slip, and fabrication to selectivity, "
    "power, sensing, and ionic circuits, reframed as Signature science. Clearly "
    "labeled Signature-made, never presented as authentic public record.",
    "nanofluidics record", "JAH-NFS-", "JAH Nanofluidics Archivist (Signature)",
    "nanofluidics archivist - Signature editions: his original Signature "
    "interpretation of nanofluidics, clearly labeled Signature-made and "
    "never presented as authentic public record; teaches progressively along the "
    "ladder from foundations through compounded to advanced; answers from many "
    "angles - definition, example, analogy, application, history, math, how-to - "
    "using only archive data from this system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# nanofluidics computation for its record. All are machine-executed by main().

_PREAMBLE = (
"import math\n"
)

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_nf_what_is(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # molecules across the channel + surface-to-volume 2/h: slit vs pipe
    d_water = 0.3e-9
    mol_slit = 50e-9 / d_water
    mol_pipe = 1e-3 / d_water
    sv_slit = 2.0 / 50e-9
    sv_pipe = 2.0 / 1e-3
    print("50 nm slit spanned by ~%.0f water molecules" % mol_slit)
    print("1 mm pipe spanned by ~%.2e water molecules" % mol_pipe)
    print("S/V slit: %.1e /m, pipe: %.0f /m, ratio: %.0e" % (sv_slit, sv_pipe, sv_slit/sv_pipe))
    assert 166.0 < mol_slit < 167.0
    assert 3.33e6 < mol_pipe < 3.34e6
    assert sv_slit/sv_pipe == 20000.0
    print("rule: shrink the channel and the walls become the physics")
    print("OK: %s counted the molecules" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_scale(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # surface-to-volume 2/h across decades; fraction of water within 1 nm of a wall
    for h in (1e-9, 10e-9, 100e-9, 1e-6):
        print("h=%6.0f nm: S/V = %.1e /m" % (h*1e9, 2.0/h))
    for h in (10e-9, 100e-9, 1e-6):
        print("h=%6.0f nm: water within 1 nm of a wall = %.1f%%" % (h*1e9, 200.0*1e-9/h))
    assert 1.999e9 < 2.0/1e-9 < 2.001e9
    assert 1.999e6 < 2.0/1e-6 < 2.001e6
    assert abs(200.0*1e-9/10e-9 - 20.0) < 1e-9
    assert abs(200.0*1e-9/1e-6 - 0.2) < 1e-9
    print("rule: each decade of shrinking multiplies the wall vote by ten")
    print("OK: %s walked the decades" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_double_layer(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Debye length at 25 C: 0.304/sqrt(I[M]) nm
    for I_mM in (1.0, 10.0, 100.0):
        lam = 0.304 / math.sqrt(I_mM/1000.0)
        print("I=%6.1f mM: Debye length = %.2f nm" % (I_mM, lam))
    assert 9.60 < 0.304/math.sqrt(0.001) < 9.62
    assert 3.03 < 0.304/math.sqrt(0.01) < 3.05
    assert 0.95 < 0.304/math.sqrt(0.1) < 0.97
    print("rule: salt screens charge - more salt, thinner double layer")
    print("OK: %s measured the charged skin" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_debye(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # regime ruler: compare h to 2*lambda for a 30 nm channel
    h = 30.0
    for I_mM, expect in ((0.1, "overlapped"), (10.0, "bulk-like")):
        lam = 0.304 / math.sqrt(I_mM/1000.0)
        r = 2.0*lam/h
        regime = "overlapped/selective" if r > 1.0 else ("bulk-like" if r < 0.5 else "transition")
        print("I=%5.1f mM: 2*lambda/h = %.2f -> %s" % (I_mM, r, regime))
    assert 2.02 < 2.0*(0.304/math.sqrt(0.0001))/30.0 < 2.04
    assert 0.20 < 2.0*(0.304/math.sqrt(0.01))/30.0 < 0.21
    print("rule: same channel, different salt - different physics")
    print("OK: %s read the ruler" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_slip(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # slit flow enhancement with slip: 1 + 6b/h
    b, h = 20e-9, 50e-9
    enh = 1.0 + 6.0*b/h
    print("b=20 nm, h=50 nm: Q_slip/Q_no-slip = %.2f" % enh)
    print("hydrophilic wall (b~0): enhancement = %.2f" % (1.0 + 6.0*0.0/h))
    assert 3.39 < enh < 3.41
    print("rule: slip is a fixed length - leverage grows as channels shrink")
    print("OK: %s let go of the wall" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_fabrication(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # plumbing arithmetic: 100 nm x 50 nm x 1 mm trench
    V = 100e-9 * 50e-9 * 1e-3          # m^3
    fL = V * 1000.0 / 1e-15            # litres -> femtolitres
    mol = V * 1000.0 * 55.5 * 6.022e23 # water molecules
    print("channel volume: %.1e m^3 = %.1f fL" % (V, fL))
    print("water molecules inside: %.2e" % mol)
    assert 4.99e-18 < V < 5.01e-18
    assert 4.99 < fL < 5.01
    assert 1.67e11 < mol < 1.68e11
    print("rule: nanofluidic volumes are counted in molecules, not drops")
    print("OK: %s did the plumbing" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_electroosmosis(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Helmholtz-Smoluchowski: v = -eps*zeta*E/eta
    eps = 78.5 * 8.854e-12
    zeta, E, eta = -0.05, 1e4, 1e-3
    v = -eps * zeta * E / eta
    print("zeta=-50 mV, E=100 V/cm: v = %.2e m/s = %.0f um/s" % (v, v*1e6))
    print("1 cm chip crossed in %.1f s" % (0.01/v))
    assert 3.47e-4 < v < 3.48e-4
    print("rule: pull the charged skin and the river follows")
    print("OK: %s pumped with voltage" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_electrophoresis(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Smoluchowski mobility mu = eps*zeta/eta; transit across 1 cm at 100 V/cm
    eps = 78.5 * 8.854e-12
    mu = eps * 0.05 / 1e-3
    t = 0.01 / (mu * 1e4)
    print("mobility: %.2e m^2/(V s)" % mu)
    print("1 cm transit at 100 V/cm: %.2f s" % t)
    assert 3.47e-8 < mu < 3.48e-8
    assert 28.7 < t < 28.8
    print("rule: charge writes the speed limit - subtract electro-osmosis to read it")
    print("OK: %s sorted by charge" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_selectivity(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Donnan: c = c0*exp(-z*e*psi/kT), psi=-80 mV, kT/e=25.7 mV
    psi, kT = -80.0, 25.7
    co = math.exp(-(-1.0)*psi/kT)     # co-ion (z=-1) exclusion factor
    enrich = math.exp(-(1.0)*psi/kT)  # counter-ion (z=+1) enrichment
    print("co-ion kept: %.2f%% -> %.1f%% rejected" % (co*100, (1-co)*100))
    print("counter-ion enriched: %.1fx" % enrich)
    assert 0.044 < co < 0.045
    assert 22.4 < enrich < 22.6
    print("rule: the wall chooses - geometry plus charge, no membrane chemistry")
    print("OK: %s ran the filter" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_streaming(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # streaming potential V = eps*zeta*deltaP/(eta*sigma)
    eps = 78.5 * 8.854e-12
    V = eps * 0.05 * 1e5 / (1e-3 * 0.01)
    print("1 bar, zeta=-50 mV, sigma=0.01 S/m: V_stream = %.3f V" % V)
    assert 0.347 < V < 0.348
    print("rule: pressure in, volts out - electro-osmosis run backwards")
    print("OK: %s harvested pressure" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_conductance(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Dukhin number Du = |sigma_s|/(e*n*h); low-salt plateau conductance
    Du = 0.05 / (1.602e-19 * 6.022e23 * 20e-9)
    mu_K = 7.6e-8
    G_plateau = 2.0 * mu_K * 0.05 * 10e-6 / 1e-3
    print("20 nm channel, 1 mM: Dukhin number = %.1f" % Du)
    print("surface-governed plateau conductance: %.1e S" % G_plateau)
    assert 25.8 < Du < 26.1
    assert 7.5e-11 < G_plateau < 7.7e-11
    print("rule: at low salt the walls carry the current")
    print("OK: %s found the second wire" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_icp(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # depletion front: x = sqrt(D*t), D = 2e-9 m^2/s
    D = 2e-9
    for t in (1.0, 10.0, 100.0):
        print("t=%5.0f s: depletion front at %.0f um" % (t, math.sqrt(D*t)*1e6))
    assert 44.6 < math.sqrt(D*1.0)*1e6 < 44.8
    assert 141.0 < math.sqrt(D*10.0)*1e6 < 142.0
    assert 447.0 < math.sqrt(D*100.0)*1e6 < 448.0
    print("rule: selectivity writes a sharp boundary in salt")
    print("OK: %s polarized the ions" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_diode(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # conical pore: geometric asymmetry (r_base/r_tip)^2; measured rectification ~12
    asym = (100.0/5.0)**2
    print("5 nm tip / 100 nm base: geometric asymmetry = %.0f" % asym)
    print("typical measured rectification ratio at 1 V: ~12")
    assert asym == 400.0
    print("rule: break the symmetry and current learns direction")
    print("OK: %s built the one-way street" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_osmotic_power(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Nernst potential for 0.5 M / 0.01 M; single-pore power; membrane ceiling
    V = 0.0257 * math.log(0.5/0.01)
    P_pore = 1e-9 * V
    P_theory = 1e14 * P_pore
    print("membrane potential: %.3f V" % V)
    print("1 nA per pore -> %.1e W per pore" % P_pore)
    print("1e14 pores/m^2 -> %.1e W/m^2 theoretical ceiling" % P_theory)
    assert 0.100 < V < 0.101
    assert 1.00e-10 < P_pore < 1.01e-10
    assert 1.00e4 < P_theory < 1.01e4
    print("rule: the estuary is a battery - selectivity is the terminal")
    print("OK: %s taxed the meeting of waters" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_ek_energy(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # full chain: I_str, V_str, P_elec (matched load), P_hyd for the demo slit
    eps = 78.5 * 8.854e-12
    w, h, L, dP, sigma = 10e-6, 100e-9, 1e-3, 1e5, 0.01
    I = eps*0.05*(w*h)*dP/(1e-3*L)
    V = eps*0.05*dP/(1e-3*sigma)
    P_e = V*I/4.0
    R_h = 12.0*1e-3*L/(w*h**3)
    P_h = dP*(dP/R_h)
    print("I_stream = %.1f pA, V_stream = %.3f V" % (I*1e12, V))
    print("P_elec = %.2e W, P_hyd = %.2e W, ideal bound = %.1f%%" % (P_e, P_h, 100*P_e/P_h))
    assert 3.47e-12 < I < 3.48e-12
    assert 0.347 < V < 0.348
    assert 3.01e-13 < P_e < 3.03e-13
    assert 8.32e-12 < P_h < 8.34e-12
    print("rule: the ceiling is 3.6%% - right where measured devices land")
    print("OK: %s priced the conversion" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_sensing(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # resistive pulse: (d/D)^3; dwell time for 10 nm pore at 1 mm/s
    dip = (5.0/30.0)**3
    dwell = 10e-9/1e-3
    print("5 nm in 30 nm pore: current dip = %.2f%%" % (dip*100))
    print("dwell time: %.0f us" % (dwell*1e6))
    assert 0.00462 < dip < 0.00464
    assert dwell == 1e-5
    print("rule: every molecule announces itself as a blip")
    print("OK: %s listened for molecules" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_dna(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 10 kbp at 1 us/base, 120 mV
    bases, rate = 10000, 1e-6
    t = bases*rate
    speed = 3.4e-6/t
    print("10 kbp translocation time: %.0f ms" % (t*1e3))
    print("mean speed: %.0f um/s" % (speed*1e6))
    assert t == 0.01
    assert 339.0 < speed*1e6 < 341.0
    print("rule: the pore reads what the field delivers")
    print("OK: %s threaded the code" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_nfet(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # gate sigma_s 0 -> 0.05 C/m^2 at 1 mM, h=20 nm: G ratio = (1+Du)/1
    Du = 0.05/(1.602e-19*6.022e23*20e-9)
    ratio = (1.0+Du)/1.0
    print("Dukhin number gated: 0 -> %.1f" % Du)
    print("conductance on/off ratio: %.1f" % ratio)
    assert 25.8 < Du < 26.1
    assert 26.8 < ratio < 27.1
    print("rule: gate the wall charge and the ions obey")
    print("OK: %s switched the ion transistor" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_memristor(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # accumulation 1.78x / depletion 0.22x conductance -> memory window
    window = 1.78/0.22
    tau = (1e-6)**2/2e-9   # diffusive forgetting, 1 um channel
    print("resistance ratio (memory window): %.1f" % window)
    print("diffusive forgetting time: %.2f ms" % (tau*1e3))
    assert 8.0 < window < 8.2
    assert 4.9e-4 < tau < 5.1e-4
    print("rule: the channel remembers where its ions have been")
    print("OK: %s stored a bit in water" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_desalination(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 250 L/m^2/h/bar; 1 m^2 at 5 bar; household 300 L/day
    daily = 250.0*5.0*24.0
    area = 300.0/daily
    print("1 m^2 at 5 bar: %.0f L/day" % daily)
    print("household membrane: %.2f m^2 (%.0f cm square)" % (area, math.sqrt(area)*100))
    assert daily == 30000.0
    assert 0.009 < area < 0.011
    print("rule: size plus charge in a sub-nm pore beats the sea")
    print("OK: %s made fresh water" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_md_water(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 2 nm slit: layers, confined diffusion, crossing time
    layers = 2.0/0.28
    D = 2.3e-9/10.0
    t = (2e-9)**2/(2.0*D)
    print("water layers in 2 nm: %.1f" % layers)
    print("confined diffusion: %.1e m^2/s; 2 nm crossed in %.1f ns" % (D, t*1e9))
    assert 7.1 < layers < 7.2
    assert 8.6e-9 < t < 8.8e-9
    print("rule: below a few nm, water is countable molecules")
    print("OK: %s watched the molecules" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_slip_cnt(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # tube enhancement 1+4b/R: R=1 nm, b=300 nm, L=1 um, 1 bar
    R, b, L, dP = 1e-9, 300e-9, 1e-6, 1e5
    v_hp = R**2*dP/(8.0*1e-3*L)
    enh = 1.0 + 4.0*b/R
    print("Hagen-Poiseuille velocity: %.1f um/s" % (v_hp*1e6))
    print("enhancement: %.0fx -> %.1f mm/s" % (enh, v_hp*enh*1e3))
    assert 12.4 < v_hp*1e6 < 12.6
    assert 1200.9 < enh < 1201.1
    assert 15.0 < v_hp*enh*1e3 < 15.1
    print("rule: atomic smoothness is infrastructure")
    print("OK: %s rode the water highway" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_access_resistance(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Hall access resistance vs pore resistance: r=5 nm, L=10 nm, sigma=1 S/m
    r, L, sigma = 5e-9, 10e-9, 1.0
    R_acc = 1.0/(4.0*sigma*r)
    R_pore = L/(sigma*math.pi*r**2)
    total = 2.0*R_acc + R_pore
    print("per-mouth access: %.1e ohm; pore: %.1e ohm" % (R_acc, R_pore))
    print("entrances are %.0f%% of total %.1e ohm" % (200.0*R_acc/total, total))
    assert 4.99e7 < R_acc < 5.01e7
    assert 1.27e8 < R_pore < 1.28e8
    assert 43.9 < 200.0*R_acc/total < 44.1
    print("rule: for short pores you are building entrances, not pores")
    print("OK: %s priced the doorway" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_pressure_flow(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # R_h = 12*eta*L/(w*h^3): 1 um x 50 nm x 1 mm; Q at 1 bar
    w, h, L = 1e-6, 50e-9, 1e-3
    R_h = 12.0*1e-3*L/(w*h**3)
    Q = 1e5/R_h
    mol_per_s = Q*1000.0*55.5*6.022e23
    print("R_h = %.1e Pa s/m^3" % R_h)
    print("1 bar -> %.2f fL/s = %.1e molecules/s" % (Q*1e18, mol_per_s))
    assert 9.5e22 < R_h < 9.7e22
    assert 3.4e10 < mol_per_s < 3.5e10
    print("rule: h^3 punishes - microchannels carry, nanochannels work")
    print("OK: %s pushed the plain way" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_diffusioosmosis(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # v = M * grad(ln c): 10x gradient over 1 mm
    v = 5e-10 * 1e4
    print("diffusio-osmotic slip: %.1f um/s" % (v*1e6))
    assert v == 5e-6
    print("rule: imbalance alone moves liquid - no electrodes needed")
    print("OK: %s drifted on salt" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_steric_sieving(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # partition Phi=(1-l)^2 and Renkin hindrance, l = a/r = 0.4
    l = 0.4
    Phi = (1.0-l)**2
    renkin = 1.0 - 2.104*l + 2.09*l**3 - 0.95*l**5
    print("partition coefficient: %.2f" % Phi)
    print("Renkin hindrance factor: %.3f -> total mobility %.3f" % (renkin, Phi*renkin))
    assert Phi == 0.36
    assert 0.282 < renkin < 0.283
    assert 0.101 < Phi*renkin < 0.103
    print("rule: geometry is a filter - the pore as caliper")
    print("OK: %s sieved by size" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_circuits(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # RC limit: R = L/(sigma*w*h), C = eps*A/lambda
    sigma, w, h, L = 0.01, 10e-6, 50e-9, 100e-6
    R = L/(sigma*w*h)
    C = 78.5*8.854e-12*(w*L)/10e-9
    tau = R*C
    print("R = %.1e ohm, C_dl = %.2e F, tau = %.2f s" % (R, C, tau))
    assert 1.99e10 < R < 2.01e10
    assert 6.94e-11 < C < 6.96e-11
    assert 1.38 < tau < 1.40
    print("rule: ionic circuits keep biological time")
    print("OK: %s wired the ions" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_angstrom_slits(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 0.68 nm slit: K+ keeps 1/2 bulk mobility, Al3+ 1/100 -> selectivity 50
    k_frac, al_frac = 0.5, 0.01
    sel = k_frac/al_frac
    print("K+ mobility fraction: %.1f; Al3+ mobility fraction: %.2f" % (k_frac, al_frac))
    print("K+/Al3+ selectivity: %.0f" % sel)
    assert sel == 50.0
    print("rule: at the angstrom scale, dehydration energy is the filter")
    print("OK: %s plumbed one atom high" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_lab_on_chip(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # diffusion clock: t = L^2/D for 100 um; molecules in 1 uL at 1 fM
    t = (100e-6)**2/1e-9
    mol = 1e-15*1e-6*6.022e23
    print("100 um mixes by diffusion in %.0f s - stir, do not wait" % t)
    print("1 uL at 1 fM holds %.0f target molecules" % mol)
    assert t == 10.0
    assert 601.0 < mol < 603.0
    print("rule: preconcentrate first, then detect")
    print("OK: %s built the bench" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_biosensor(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # counting limit: 602 molecules, Poisson noise; wall-meeting time in 50 nm channel
    n = 1e-15*1e-6*6.022e23
    noise = math.sqrt(n)
    t_wall = (50e-9)**2/1e-9
    print("targets: %.0f; Poisson noise: %.1f (%.1f%% floor)" % (n, noise, 100*noise/n))
    print("molecule meets the wall every %.1f us" % (t_wall*1e6))
    assert 601.0 < n < 603.0
    assert 2.4e-6 < t_wall < 2.6e-6
    print("rule: count what can be counted - never average 602 molecules")
    print("OK: %s counted to the limit" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_fouling(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # J = J0*exp(-t/72h): flux at 24 h; half-flux time
    j24 = math.exp(-24.0/72.0)
    t_half = 72.0*math.log(2.0)
    print("flux after 24 h: %.1f%% of fresh" % (j24*100))
    print("half-flux (cleaning interval): %.1f h" % t_half)
    assert 0.716 < j24 < 0.718
    assert 49.9 < t_half < 50.0
    print("rule: design the cleaning before the channel")
    print("OK: %s scheduled the cleaning" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_design_rules(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # network: (1e21 + 2e21) in series, paralleled with 3e21; Q at 1 bar
    R_series = 1e21 + 2e21
    R_total = 1.0/(1.0/R_series + 1.0/3e21)
    Q = 1e5/R_total
    print("R_total = %.1e Pa s/m^3" % R_total)
    print("1 bar -> %.0f aL/s" % (Q*1e21))
    assert R_total == 1.5e21
    assert 66660.0 < Q*1e21 < 66670.0
    print("rule: regime, driver, resistances, walls, measurement, cleaning")
    print("OK: %s ran the checklist" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_safety(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 1 mg powder in 30 m^3 vs NIOSH REL 1 ug/m^3
    conc = (1e-3/30.0)*1e6   # ug/m^3
    print("airborne: %.1f ug/m^3 vs REL 1 ug/m^3 -> %.0fx over" % (conc, conc/1.0))
    assert 33.3 < conc < 33.4
    print("rule: wet work, hooded powders, interlocked kilovolts")
    print("OK: %s did the exposure math" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nf_future(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 1M devices at 250 per 200 mm wafer
    wafers = 1e6/250.0
    print("one million devices: %.0f wafers - a pilot line, not a megafab" % wafers)
    assert wafers == 4000.0
    print("rule: uniformity first, fouling solved, standards shaped")
    print("OK: %s priced the future" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "what_is": demo_nf_what_is, "scale": demo_nf_scale,
    "double_layer": demo_nf_double_layer, "debye": demo_nf_debye,
    "slip": demo_nf_slip, "fabrication": demo_nf_fabrication,
    "electroosmosis": demo_nf_electroosmosis,
    "electrophoresis": demo_nf_electrophoresis,
    "selectivity": demo_nf_selectivity, "streaming": demo_nf_streaming,
    "conductance": demo_nf_conductance, "icp": demo_nf_icp,
    "diode": demo_nf_diode, "osmotic_power": demo_nf_osmotic_power,
    "ek_energy": demo_nf_ek_energy, "sensing": demo_nf_sensing,
    "dna": demo_nf_dna, "nfet": demo_nf_nfet,
    "memristor": demo_nf_memristor, "desalination": demo_nf_desalination,
    "md_water": demo_nf_md_water, "slip_cnt": demo_nf_slip_cnt,
    "access_resistance": demo_nf_access_resistance,
    "pressure_flow": demo_nf_pressure_flow,
    "diffusioosmosis": demo_nf_diffusioosmosis,
    "steric_sieving": demo_nf_steric_sieving, "circuits": demo_nf_circuits,
    "angstrom_slits": demo_nf_angstrom_slits,
    "lab_on_chip": demo_nf_lab_on_chip, "biosensor": demo_nf_biosensor,
    "fouling": demo_nf_fouling, "design_rules": demo_nf_design_rules,
    "safety": demo_nf_safety, "future": demo_nf_future,
}
assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"
def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_nanofluidics.py).
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
    for slug in ("nanofluidics", "nanofluidics-signature"):
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
