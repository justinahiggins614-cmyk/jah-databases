#!/usr/bin/env python3
"""Build the Nanotoxicology field databases for JAH Databases (field #34, taxonomy order).

Verified 2026-10-17 (see entries_nanotoxicology.py docstring): NO database
covers nanotoxicology as a discipline (nanoscale hazard and exposure
science: dose metrics, exposure routes, translocation, oxidative stress,
TiO2, silver, ZnO, quantum dots, nanoplastics, carbon nanotubes, graphene,
protein corona, in vitro screening, assay interference, in vivo testing,
pulmonary clearance, genotoxicity, immune response, dermal and oral
exposure, biomarkers/omics, NIOSH CIB 65, OECD test guidelines, REACH
nanoforms, EPA TSCA, ISO/TS 12901 control banding, safer by design,
surface chemistry, exposure modeling, PPE and engineering controls,
lifecycle thinking, risk assessment, new approach methods).

Manifest search (2368 databases): zero 'nanotox*' slugs, zero 'tox' slugs
at all; nearest neighbors are 'occupational-safety-study' /
'occupational-safety-published' (occupational safety as a study field,
not nanoscale hazard science) and 'nanotech' (general nanotechnology -
no toxicology discipline). Whole-system exact-title sweep: zero
collisions for all 34 planned titles. ZERO full-record discipline
coverage anywhere.

So this build creates two NEW databases, 34 ladder-ordered records each:

  nanotoxicology              - The Nanotoxicology Database
                               (public-harvest: real, fact-checked
                               nanotoxicology; standard references
                               Oberdorster et al. 'Nanotoxicology: An
                               emerging discipline evolving from studies of
                               ultrafine particles' Environ. Health
                               Perspect. 2005; Nel et al. 'Toxic potential
                               of materials at the nanolevel' Science 2006;
                               Donaldson et al. 'Carbon nanotubes: a review
                               of their properties in relation to pulmonary
                               toxicology and workplace safety' Toxicol.
                               Sci. 2006; NIOSH CIB 65 'Occupational
                               Exposure to Carbon Nanotubes and Nanofibers'
                               2013; ISO/TS 12901-2:2014; OECD inhalation
                               test guidelines)
  nanotoxicology-signature    - The Nanotoxicology Signature Database
                               (his original Signature interpretation of
                               nanotoxicology as safety engineering; src
                               signature, titles suffixed
                               " (Signature Edition)", never presented as
                               authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

CONTENT SAFETY: records describe hazards, exposure science, and SAFETY
engineering only. No instructions facilitating harm; every hazard record
pairs with controls and mitigation.

Subtitle disambiguation (fields #13-33 pattern): specialty titles carry
teaching-focused subtitles rather than bare cards.

Numerical cores: all hand-computed 2026-10-17 (one slip caught and fixed
before commit: dose-metric number concentrations were off by 1000x -
recomputed from 1 mg/m3 = 1e-6 kg/m3), machine-verified by the demos.

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
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_nanotoxicology import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of nanotoxicology "
                "as safety engineering: clearly labeled Signature-made, never presented as "
                "authentic public record.")
    pub_line = ("Public records - real, fact-checked nanotoxicology: what nanotoxicology is; "
                "dose metrics (mass, surface area, particle number); exposure routes; "
                "translocation; oxidative stress and ROS; titanium dioxide; silver "
                "nanoparticles; zinc oxide; quantum dots; nanoplastics; carbon nanotubes "
                "and the fiber paradigm; graphene; the protein corona; in vitro screening; "
                "assay interference; in vivo testing; pulmonary clearance; genotoxicity; "
                "immune response; dermal and oral exposure; biomarkers and omics; "
                "NIOSH CIB 65; OECD test guidelines; REACH nanoforms; EPA TSCA; ISO/TS 12901 "
                "control banding; safer by design; surface chemistry; exposure modeling; "
                "PPE and engineering controls; lifecycle thinking; risk assessment; new "
                "approach methods, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what nanotoxicology "
              "is, dose metrics, exposure routes, translocation, oxidative stress, TiO2, "
              "silver, ZnO, quantum dots, nanoplastics) -> Compounded (carbon nanotubes, "
              "graphene, protein corona, in vitro screening, assay interference, in vivo "
              "testing, pulmonary clearance, genotoxicity, immune response, dermal and oral "
              "exposure) -> Advanced (biomarkers and omics, NIOSH CIB 65, OECD guidelines, "
              "REACH, EPA TSCA, ISO/TS 12901, safer by design, surface chemistry, exposure "
              "modeling, PPE and controls, lifecycle, risk assessment, future methods).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search dose metrics, carbon nanotubes, NIOSH CIB 65, safer by design, protein corona, REACH nanoforms...",
        "chat_ph": "Ask about nanotoxicology...",
        "archive_blurb": ("Seeded %s nanotoxicology records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled nanotoxicology studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about nanotoxicology - from what it is through dose metrics, exposure routes, translocation, oxidative stress, titanium dioxide, silver, zinc oxide, quantum dots, and nanoplastics, through carbon nanotubes, graphene, the protein corona, in vitro screening, assay interference, in vivo testing, clearance, genotoxicity, immune response, and dermal and oral exposure, to biomarkers, NIOSH CIB 65, OECD guidelines, REACH, EPA TSCA, control banding, safer by design, surface chemistry, exposure modeling, PPE, lifecycle thinking, risk assessment, and new approach methods." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "nanotoxicology-study", "gen_demo_kind": "nanotoxicology-demo",
        "source": source,
    }

CIT_PUB = ("Nanotoxicology (standard references: Oberdorster et al. 'Nanotoxicology: An "
           "emerging discipline evolving from studies of ultrafine particles' Environ. "
           "Health Perspect. 2005; Nel et al. 'Toxic potential of materials at the "
           "nanolevel' Science 2006; Donaldson et al. 'Carbon nanotubes: a review of "
           "their properties in relation to pulmonary toxicology and workplace safety' "
           "Toxicol. Sci. 2006; Poland et al. 'Carbon nanotubes introduced into the "
           "abdominal cavity of mice show asbestos-like pathogenicity' Nat. Nanotechnol. "
           "2008; NIOSH CIB 65 'Occupational Exposure to Carbon Nanotubes and Nanofibers' "
           "2013; ISO/TS 12901-2:2014; OECD inhalation test guidelines TG 412/413).")
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["nanotoxicology"] = _cfg(
    "nanotoxicology", "The Nanotoxicology Database",
    "Real, fact-checked nanotoxicology: from what nanotoxicology is through dose metrics, "
    "exposure routes, translocation, oxidative stress, titanium dioxide, silver, zinc oxide, "
    "quantum dots, and nanoplastics, through carbon nanotubes, graphene, the protein corona, "
    "in vitro screening, assay interference, in vivo testing, clearance, genotoxicity, immune "
    "response, and dermal and oral exposure, to biomarkers, NIOSH CIB 65, OECD guidelines, "
    "REACH, EPA TSCA, control banding, safer by design, surface chemistry, exposure modeling, "
    "PPE, lifecycle thinking, risk assessment, and new approach methods - taught progressively "
    "along the ladder.",
    "nanotoxicology record", "JAH-NTX-", "JAH Nanotoxicology Archivist",
    "nanotoxicology archivist - nanoscale hazard and exposure science: dose metrics, "
    "exposure routes, translocation, oxidative stress, TiO2, silver, ZnO, quantum dots, "
    "nanoplastics, carbon nanotubes and the fiber paradigm, graphene, protein corona, "
    "in vitro screening, assay interference, in vivo testing, pulmonary clearance, "
    "genotoxicity, immune response, dermal and oral exposure, biomarkers and omics, "
    "NIOSH CIB 65, OECD test guidelines, REACH nanoforms, EPA TSCA, ISO/TS 12901 control "
    "banding, safer by design, surface chemistry, exposure modeling, PPE and engineering "
    "controls, lifecycle thinking, risk assessment, new approach methods; teaching "
    "progressively along the ladder from foundations through compounded to advanced; "
    "answers from many angles - definition, example, analogy, application, history, "
    "math, how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["nanotoxicology-signature"] = _cfg(
    "nanotoxicology-signature", "The Nanotoxicology Signature Database",
    "His original Signature interpretation of nanotoxicology as safety engineering: the full "
    "ladder from hazard and dose metrics through materials, testing, and regulation to "
    "safer-by-design engineering, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "nanotoxicology record", "JAH-NTS-", "JAH Nanotoxicology Archivist (Signature)",
    "nanotoxicology archivist - Signature editions: his original Signature "
    "interpretation of nanotoxicology as safety engineering, clearly labeled "
    "Signature-made and never presented as authentic public record; teaches "
    "progressively along the ladder from foundations through compounded to advanced; "
    "answers from many angles - definition, example, analogy, application, history, "
    "math, how-to - using only archive data from this system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# nanotoxicology computation for its record. All are machine-executed by main().

_PREAMBLE = (
"import math\n"
)

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_nt_what_is(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # specific surface area of TiO2 spheres: SSA = 6/(rho*d), rho=3900 kg/m3
    rho = 3900.0
    ssa20 = 6.0/(rho*20e-9)/1000.0    # m^2/g
    ssa200 = 6.0/(rho*200e-9)/1000.0
    print("20 nm TiO2:  %.2f m^2/g" % ssa20)
    print("200 nm TiO2: %.2f m^2/g" % ssa200)
    print("shrinking 10x multiplies the chemistry-per-gram by %.0f" % (ssa20/ssa200))
    assert 76.92 < ssa20 < 76.93
    assert 7.692 < ssa200 < 7.693
    assert ssa20/ssa200 == 10.0
    print("rule: surface is where the chemistry happens - price it per gram")
    print("OK: %s priced the surface" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_dose_metrics(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 1 mg/m3 TiO2 (rho=3900 kg/m3): number and surface-area concentrations
    rho, C = 3900.0, 1e-6  # kg/m3
    out = {}
    for d in (10e-9, 100e-9):
        mp = rho*math.pi/6.0*d**3
        N = C/mp
        SA = N*math.pi*d**2
        out[d] = (N, SA)
        print("d=%3.0f nm: N=%.3e /m3, SA=%.4f m^2/m3" % (d*1e9, N, SA))
    N10, SA10 = out[10e-9]
    N100, SA100 = out[100e-9]
    print("same milligram: %.0fx the particles, %.0fx the surface" % (N10/N100, SA10/SA100))
    assert 4.897e14 < N10 < 4.898e14
    assert 4.897e11 < N100 < 4.898e11
    assert 0.1538 < SA10 < 0.1539
    assert 0.01538 < SA100 < 0.01539
    assert 999.9 < N10/N100 < 1000.1
    assert 9.99 < SA10/SA100 < 10.01
    print("rule: a milligram is not a milligram - report all three metrics")
    print("OK: %s converted the dose" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_exposure_routes(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # light-work breathing 20 L/min over an 8-h shift
    vol = 20.0*60.0*8.0/1000.0  # m3
    print("air breathed per shift: %.1f m3" % vol)
    for conc_ug, label in ((1.0, "NIOSH CNT REL"), (100.0, "dusty operation")):
        inhaled_ug = conc_ug*vol
        print("%s (%g ug/m3): %.1f ug inhaled" % (label, conc_ug, inhaled_ug))
    assert vol == 9.6
    assert 1.0*vol == 9.6
    assert 100.0*vol == 960.0
    print("rule: control the airborne powder and you control the dominant risk")
    print("OK: %s did the shift arithmetic" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_translocation(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Brownian random walk in air: D = kT/(3*pi*eta*d), x = sqrt(2*D*t)
    kT, eta = 4.114e-21, 1.8e-5
    for d in (10e-9, 100e-9):
        D = kT/(3.0*math.pi*eta*d)
        x = math.sqrt(2.0*D*1.0)
        print("d=%3.0f nm: random walk in 1 s = %.1f um" % (d*1e9, x*1e6))
    x10 = math.sqrt(2.0*(kT/(3.0*math.pi*eta*10e-9)))
    x100 = math.sqrt(2.0*(kT/(3.0*math.pi*eta*100e-9)))
    print("air-blood barrier is ~0.5 um - diffusion delivers particles to it")
    assert 69.64 < x10*1e6 < 69.65
    assert 22.02 < x100*1e6 < 22.03
    print("rule: the lung is a gateway, not a sealed bag - follow the particle")
    print("OK: %s walked the random walk" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_oxidative_stress(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # ROS production vs antioxidant clearance: where the ledger goes red
    ros_per_mg = 5e-9    # mol/s per mg of particles
    clearance = 2e-8     # mol/s the cell can clear
    threshold_mg = clearance/ros_per_mg
    gsh_pool = 1e-6      # mol of glutathione buffer
    drain_s = gsh_pool/(ros_per_mg*1.0)  # at 1 mg dose
    print("threshold dose (production = clearance): %.1f mg" % threshold_mg)
    print("at 1 mg: glutathione buffer drains in %.0f s" % drain_s)
    assert threshold_mg == 4.0
    assert drain_s == 200.0
    print("rule: toxicity is the overdraft - price the ROS against the defense")
    print("OK: %s balanced the ledger" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_tio2(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 8-h shift at the ultrafine TiO2 REL 0.3 mg/m3; P25 SSA 50 m2/g
    vol = 20.0*60.0*8.0/1000.0
    inhaled_mg = 0.3*vol
    sa_m2 = inhaled_mg/1000.0*50.0
    print("inhaled at REL: %.2f mg" % inhaled_mg)
    print("reactive surface delivered: %.3f m^2" % sa_m2)
    print("fine-particle limit 2.4 mg/m3 is %.0fx higher - surface area priced in" % (2.4/0.3))
    assert 2.879 < inhaled_mg < 2.881
    assert 0.1439 < sa_m2 < 0.1441
    assert 2.4/0.3 == 8.0
    print("rule: crystal form + coating + route = the hazard description")
    print("OK: %s read the TiO2 file" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_silver(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # linear dissolution model: 2%/day at 10 nm, 0.4%/day at 50 nm (1/d scaling)
    f10 = 0.02*7.0
    f50 = 0.004*7.0
    print("10 nm Ag: %.1f%% dissolved after 7 days" % (f10*100))
    print("50 nm Ag: %.1f%% dissolved after 7 days" % (f50*100))
    assert 0.139 < f10 < 0.141
    assert 0.0279 < f50 < 0.0281
    assert f10/f50 == 5.0
    print("rule: if the ion control reproduces the toxicity, the particle is a delivery device")
    print("OK: %s timed the ion release" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_zno(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # absorption edge: wavelength(nm) = 1240 / band gap(eV)
    lam_zno = 1240.0/3.37
    lam_tio2 = 1240.0/3.20
    print("ZnO (3.37 eV): absorbs from %.1f nm" % lam_zno)
    print("TiO2 (3.20 eV): absorbs from %.1f nm" % lam_tio2)
    print("both sit in the UVA band that reaches skin")
    assert 367.9 < lam_zno < 368.0
    assert 387.4 < lam_tio2 < 387.6
    print("rule: separate the mechanisms (light vs ions), then engineer each down")
    print("OK: %s found the absorption edge" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_quantum_dots(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Cd inventory of a 4 nm CdSe core (rho 5.82 g/cm3, M 191.37 g/mol)
    V = math.pi/6.0*(4e-9)**3
    atoms = 5820.0*V/0.19137*6.022e23
    Vs = math.pi/6.0*((6e-9)**3-(4e-9)**3)  # 1 nm ZnS shell
    print("4 nm CdSe core holds ~%.0f cadmium atoms" % atoms)
    print("1 nm ZnS shell volume: %.2e m^3 - the whole safety device" % Vs)
    assert 613.0 < atoms < 615.0
    assert 7.958e-26 < Vs < 7.960e-26
    print("rule: count the atoms inside, price the shell in years of integrity")
    print("OK: %s audited the sealed package" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_nanoplastics(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 1 g of plastic (rho 1 g/cm3) fragmented into 100 nm spheres
    d = 1e-5  # cm
    Vp = math.pi/6.0*d**3
    N = 1.0/Vp
    SA = N*math.pi*d**2/1e4  # m^2
    print("particles: %.3e" % N)
    print("new surface: %.1f m^2" % SA)
    assert 1.909e15 < N < 1.911e15
    assert 59.99 < SA < 60.01
    print("rule: fragmentation is a number explosion - choke the source, do not chase particles")
    print("OK: %s counted the uncountable" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_cnt(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # WHO fiber rules: L > 5 um, d < 3 um, aspect > 3
    L, d = 10.0, 0.05  # um
    aspect = L/d
    fiber = (L > 5.0) and (d < 3.0) and (aspect > 3.0)
    print("MWCNT 10 um x 50 nm: aspect ratio %.0f, fiber = %s" % (aspect, fiber))
    sphere = (0.05 > 5.0)
    print("50 nm sphere: fiber = %s" % sphere)
    assert aspect == 200.0
    assert fiber is True
    assert sphere is False
    print("rule: regulate the fiber, not the name")
    print("OK: %s applied the fiber paradigm" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_graphene(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 1 um flakes, areal density 7.7e-7 kg/m2: edge inventory per gram
    m_flake = 7.7e-7*1e-12
    flakes = 1e-3/m_flake
    edge_km = flakes*4e-6/1000.0
    print("flakes per gram: %.3e" % flakes)
    print("total edge per gram: %.3e km" % edge_km)
    assert 1.298e15 < flakes < 1.300e15
    assert 5.194e6 < edge_km < 5.196e6
    print("rule: all surface, no bulk - pacify the edge")
    print("OK: %s inventoried the coastline" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_protein_corona(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Langmuir binding: bound = Bmax*C/(Kd+C), Kd = 0.1 mg/mL
    Kd = 0.1
    f_blood = 1.0*1.0/(Kd+1.0)
    f_dilute = 1.0*0.01/(Kd+0.01)
    print("at 1 mg/mL protein: %.1f%% surface covered" % (f_blood*100))
    print("at 0.01 mg/mL protein: %.1f%% surface covered" % (f_dilute*100))
    assert 0.9090 < f_blood < 0.9092
    assert 0.0908 < f_dilute < 0.0910
    print("rule: cells meet the corona, never the bare particle")
    print("OK: %s dressed the particle" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_in_vitro(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # MTT artifact: true 0.40 OD + 0.15 OD particle absorbance on 1.00 control
    true_od, artifact, control = 0.40, 0.15, 1.00
    measured = (true_od+artifact)/control
    true_viab = true_od/control
    print("true viability: %.0f%%, measured: %.0f%%" % (true_viab*100, measured*100))
    print("error: %.0f points - the cell-free control catches it" % ((measured-true_viab)*100))
    assert 0.549 < measured < 0.551
    assert true_viab == 0.40
    print("rule: a result without interference controls is a rumor")
    print("OK: %s caught the lie" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_assay_interference(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # DCF probe quenched 30% by particles: true 100 RFU reads 70
    true_rfu, quench = 100.0, 0.30
    measured = true_rfu*(1.0-quench)
    correction = 1.0/(1.0-quench)
    print("true %.0f RFU reads %.0f RFU; correction factor %.3f" % (true_rfu, measured, correction))
    assert measured == 70.0
    assert 1.4285 < correction < 1.4287
    print("rule: spike-recovery first, conclusions second")
    print("OK: %s corrected the quench" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_in_vivo(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # rat 6-h exposure at 5 mg/m3: 0.15 L/min, 30% alveolar deposition
    inhaled_m3 = 0.15*360.0/1000.0
    deposited_mg = inhaled_m3*5.0*0.30
    overload_mg = 1.0
    print("deposited: %.3f mg = %.1f%% of the ~1 mg overload line" % (deposited_mg, deposited_mg/overload_mg*100))
    assert 0.0809 < deposited_mg < 0.0811
    assert 8.0 < deposited_mg/overload_mg*100 < 8.2
    print("rule: responsive but not overloaded - or the study measures overload, not the material")
    print("OK: %s designed the dose" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_clearance(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # lung burden after 365 days: normal t1/2 65 d vs overloaded 300 d
    p_normal = math.exp(-math.log(2.0)/65.0*365.0)*100.0
    p_over = math.exp(-math.log(2.0)/300.0*365.0)*100.0
    print("normal clearance: %.2f%% retained after 1 year" % p_normal)
    print("overloaded: %.1f%% retained after 1 year" % p_over)
    assert 2.039 < p_normal < 2.041
    assert 43.02 < p_over < 43.04
    print("rule: overload converts a self-cleaning organ into a reservoir")
    print("OK: %s timed the janitor" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_genotoxicity(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # comet assay tail moment = tail length (um) * fraction of DNA in tail
    tm_exp = 20.0*0.30
    tm_ctrl = 15.0*0.10
    print("exposed tail moment: %.1f; control: %.1f; fold: %.1f" % (tm_exp, tm_ctrl, tm_exp/tm_ctrl))
    assert 5.99 < tm_exp < 6.01
    assert 1.49 < tm_ctrl < 1.51
    assert tm_exp/tm_ctrl == 4.0
    print("rule: genotoxicity is the red line - uncertainty itself becomes the verdict")
    print("OK: %s read the comet tails" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_immune(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Hill dose-response for IL-6: Emax 1000 pg/mL, EC50 50 ug/mL, n 1.5
    Emax, EC50, n = 1000.0, 50.0, 1.5
    def hill(C):
        return Emax*C**n/(EC50**n+C**n)
    print("IL-6 at EC50: %.0f pg/mL" % hill(50.0))
    print("IL-6 at 200 ug/mL: %.1f pg/mL" % hill(200.0))
    assert 499.99 < hill(50.0) < 500.01
    assert 888.88 < hill(200.0) < 888.90
    print("rule: cytokines are the earliest quantitative warning - instrument every variant")
    print("OK: %s fitted the alarm curve" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_dermal(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Franz-cell flux 2.5e-9 mg/cm2/h, 8 h, 100 cm2 of skin
    absorbed_mg = 2.5e-9*8.0*100.0
    print("absorbed: %.1e mg = %.0f ng" % (absorbed_mg, absorbed_mg*1e6))
    assert 1.99e-6 < absorbed_mg < 2.01e-6
    print("rule: intact skin is armor - reassess when it is not intact")
    print("OK: %s audited the armor" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_ingestion(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # oral bioavailability 0.1%: 1 mg ingested
    systemic_mg = 1.0*0.001
    print("1 mg ingested -> %.4f mg systemic (%.0f ug)" % (systemic_mg, systemic_mg*1000))
    print("the rest transits; the gut itself is the question")
    assert 0.00099 < systemic_mg < 0.00101
    print("rule: respect the reluctant gate - prove low uptake per additive")
    print("OK: %s weighed the gut barrier" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_biomarkers(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # log2 fold change: stress gene 50 -> 800 normalized counts
    import math as _m
    l2fc = _m.log2(800.0/50.0)
    print("log2 fold change: %.1f (= %.0fx upregulation)" % (l2fc, 2.0**l2fc))
    assert 3.99 < l2fc < 4.01
    print("rule: file prints by mechanism - let one tested material vouch for its family")
    print("OK: %s read the molecular diary" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_niosh_cib65(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # measured 8 ug/m3 vs REL 1 ug/m3 elemental carbon
    measured, rel = 8.0, 1.0
    exceed = measured/rel
    efficiency = 1.0-1.0/exceed
    print("exceedance: %.0fx over the limit" % exceed)
    print("required control efficiency: %.1f%%" % (efficiency*100))
    assert exceed == 8.0
    assert 0.874 < efficiency < 0.876
    print("rule: work the arithmetic backwards from 1 ug/m3 - open handling cannot comply")
    print("OK: %s enforced the limit" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_oecd(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # TG 413: 10/sex/group x 2 sexes x 4 groups; TG 412: 5/sex/group x 2 x 4
    tg413 = 10*2*4
    tg412 = 5*2*4
    print("TG 413 (90-day): %d rats" % tg413)
    print("TG 412 (28-day): %d rats" % tg412)
    assert tg413 == 80
    assert tg412 == 40
    print("rule: triage in vitro, group nanoforms, run one definitive study instead of three mediocre ones")
    print("OK: %s counted the cost" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_reach(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # tonnage-band decision table
    def annexes(t):
        if t < 1.0:
            return "reduced"
        if t < 10.0:
            return "VII+VIII"
        if t < 100.0:
            return "VII+VIII+IX"
        return "VII+VIII+IX+X"
    for t in (0.5, 5.0, 50.0, 500.0):
        print("%.1f t/yr -> Annex %s" % (t, annexes(t)))
    assert annexes(5.0) == "VII+VIII"
    assert annexes(50.0) == "VII+VIII+IX"
    assert annexes(500.0) == "VII+VIII+IX+X"
    print("rule: each nanoform carries a dossier - consolidate the portfolio before registering")
    print("OK: %s read the tonnage table" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_epa_tsca(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 2017 8(a) rule decision logic
    def reportable(size_nm, solid, engineered, year):
        return solid and engineered and 1.0 <= size_nm <= 100.0 and year >= 2014
    case = reportable(20.0, True, True, 2016)   # 100 kg nanosilver, 2016
    print("20 nm engineered nanosilver, made 2016: reportable = %s" % case)
    assert case is True
    assert reportable(500.0, True, True, 2016) is False
    assert reportable(20.0, True, True, 2010) is False
    print("rule: the regulator asks 'what do you have' - keep the inventory living")
    print("OK: %s filed the census" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_iso12901(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # simplified control-banding matrix: (hazard 1-5, exposure 1-4) -> control level
    def control_level(h, e):
        score = h+e
        if score >= 8:
            return 5  # full containment
        if score >= 6:
            return 4  # containment / LEV+
        if score >= 4:
            return 3  # LEV / fume hood
        return 2      # general ventilation
    h, e = 5, 4  # fibrous biopersistent CNT, dusty kg-scale powder handling
    lvl = control_level(h, e)
    print("hazard band %d x exposure band %d -> control level %d (full containment)" % (h, e, lvl))
    assert lvl == 5
    assert control_level(2, 2) == 3
    print("rule: precaution first, verification always - then measure to prove it")
    print("OK: %s ran the matrix" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_safer_by_design(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # ZnO dissolution: undoped k=0.02/h vs Fe-doped k=0.004/h, 24 h
    f_und = 1.0-math.exp(-0.02*24.0)
    f_dop = 1.0-math.exp(-0.004*24.0)
    print("undoped ZnO dissolved in 24 h: %.1f%%" % (f_und*100))
    print("Fe-doped ZnO dissolved in 24 h: %.1f%%" % (f_dop*100))
    assert 0.3811 < f_und < 0.3813
    assert 0.0914 < f_dop < 0.0916
    print("rule: bend the hazard curve without bending the function curve")
    print("OK: %s doped the lattice" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_surface_chemistry(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 5 nm silica shell on ZnO: effective k 0.002/h vs bare 0.02/h, 24 h
    f_bare = 1.0-math.exp(-0.02*24.0)
    f_shell = 1.0-math.exp(-0.002*24.0)
    print("bare ZnO dissolved: %.1f%%; shelled: %.1f%%" % (f_bare*100, f_shell*100))
    assert 0.3811 < f_bare < 0.3813
    assert 0.0468 < f_shell < 0.0470
    print("rule: the coating is the safety device - warranty it past the product life")
    print("OK: %s sealed the surface" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_exposure_modeling(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # two-box steady state: G = 1 mg/min; near-field 10 m3/min; room 100 m3/min
    G = 1.0  # mg/min
    C_nf = G/10.0*1000.0    # ug/m3
    C_ff = G/100.0*1000.0
    print("breathing zone: %.0f ug/m3; room: %.0f ug/m3" % (C_nf, C_ff))
    print("vs 1 ug/m3 CNT limit: %.0fx over - enclose the process" % (C_nf/1.0))
    assert 99.9 < C_nf < 100.1
    assert 9.99 < C_ff < 10.01
    print("rule: forecast before the first batch runs, verify with a measurement day")
    print("OK: %s modeled the breathing zone" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_ppe(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 50 ug/m3 vs 1 ug/m3 REL: needed reduction 50x; APFs 10 / 50 / 1000
    needed = 50.0/1.0
    apfs = {"half-face P100": 10, "full-face P100": 50, "supplied-air": 1000}
    ok = [k for k, v in apfs.items() if v >= needed]
    print("needed reduction: %.0fx" % needed)
    for k, v in apfs.items():
        print("  %s (APF %d): %s" % (k, v, "adequate" if v >= needed else "insufficient"))
    assert needed == 50.0
    assert ok == ["full-face P100", "supplied-air"]
    print("rule: respirators are the backup that never gets called - enclosures do the work")
    print("OK: %s sized the protection" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_lifecycle(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 100 kg batch: 2% fugitive emission, 99% capture
    produced = 100.0
    fugitive = produced*0.02
    released = fugitive*(1.0-0.99)
    print("fugitive: %.1f kg; released after capture: %.3f kg (%d g)" % (fugitive, released, released*1000))
    assert fugitive == 2.0
    assert 0.0199 < released < 0.0201
    print("rule: place the control where the inventory says the release happens")
    print("OK: %s balanced the mass" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_risk_assessment(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # risk quotients: CNT 0.5 ug/m3 vs REL 1; TiO2 0.05 mg/m3 vs REL 0.3
    rq_cnt = 0.5/1.0
    rq_tio2 = 0.05/0.3
    print("RQ CNT: %.2f (%s)" % (rq_cnt, "acceptable" if rq_cnt < 1 else "manage"))
    print("RQ TiO2: %.3f (%s)" % (rq_tio2, "acceptable" if rq_tio2 < 1 else "manage"))
    assert rq_cnt == 0.5
    assert 0.1666 < rq_tio2 < 0.1668
    print("rule: show every input, price the guesses, re-open when data arrives")
    print("OK: %s closed the ledger" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nt_future(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # NAM battery validation: 5 assays x 20 reference chemicals at 85% concordance
    calls = 5*20
    correct = calls*0.85
    print("validation battery: %d calls, %.0f correct at 85%% concordance" % (calls, correct))
    assert calls == 100
    assert correct == 85.0
    print("rule: map the pathway once, then read it at speed")
    print("OK: %s validated the future" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "what_is": demo_nt_what_is, "dose_metrics": demo_nt_dose_metrics,
    "exposure_routes": demo_nt_exposure_routes,
    "translocation": demo_nt_translocation,
    "oxidative_stress": demo_nt_oxidative_stress, "tio2": demo_nt_tio2,
    "silver": demo_nt_silver, "zno": demo_nt_zno,
    "quantum_dots": demo_nt_quantum_dots,
    "nanoplastics": demo_nt_nanoplastics, "cnt": demo_nt_cnt,
    "graphene": demo_nt_graphene, "protein_corona": demo_nt_protein_corona,
    "in_vitro": demo_nt_in_vitro,
    "assay_interference": demo_nt_assay_interference,
    "in_vivo": demo_nt_in_vivo, "clearance": demo_nt_clearance,
    "genotoxicity": demo_nt_genotoxicity, "immune": demo_nt_immune,
    "dermal": demo_nt_dermal, "ingestion": demo_nt_ingestion,
    "biomarkers": demo_nt_biomarkers, "niosh_cib65": demo_nt_niosh_cib65,
    "oecd_guidelines": demo_nt_oecd, "reach": demo_nt_reach,
    "epa_tsca": demo_nt_epa_tsca, "iso12901": demo_nt_iso12901,
    "safer_by_design": demo_nt_safer_by_design,
    "surface_chemistry": demo_nt_surface_chemistry,
    "exposure_modeling": demo_nt_exposure_modeling, "ppe": demo_nt_ppe,
    "lifecycle": demo_nt_lifecycle,
    "risk_assessment": demo_nt_risk_assessment, "future": demo_nt_future,
}
assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"

def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    ordered = sorted(enumerate(ENTRIES), key=lambda p: (p[1]["ladder_rank"], p[0]))
    recs = []
    for _, e in ordered:
        name = e["name"]
        title = name + " (Signature Edition)" if sig else name
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
    for slug in ("nanotoxicology", "nanotoxicology-signature"):
        source = "signature" if slug.endswith("-signature") else "public"
        built[slug] = build_records(slug, source)

    total = 0
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        assert len(recs) == 34, "expected 34 records in %s, got %d" % (slug, len(recs))
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
