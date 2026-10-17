#!/usr/bin/env python3
"""Build the Petrophysics field databases for JAH Databases (field #26, taxonomy order).

Verified 2026-10-17 (see entries_petrophysics.py docstring): NO database
covers petrophysics as a specialty discipline. Manifest search (2352
databases): no 'petrophysics' database. Nearest neighbors: 'petrology' /
'petrology-signature' (field #9 - rocks generally, zero petrophysics-topic
hits in their shard indexes) and 'petroleum-refining' /
'petroleum-refining-signature' (field #22 - downstream processing, zero
hits). Whole-system title sweep over all 754 shard indexes ('petrophys',
'archie equation', 'formation evaluation'): ZERO hits anywhere.

So this build creates two NEW databases, 32 ladder-ordered records each,
covering ONLY what the system left uncovered:

  petrophysics             - The Petrophysics Database (public-harvest:
                             real, fact-checked petrophysics; citations
                             Tiab & Donaldson, Archer & Wall, Ellis &
                             Singer, Hearst/Nelson/Paillet, Asquith &
                             Krygowski, Rider, Schlumberger, Doveton,
                             Archie 1942, Darcy 1856, Leverett 1941,
                             Purcell 1949, Brooks & Corey 1964, Wyllie et
                             al. 1956/58, Waxman & Smits 1968, Simandoux
                             1963, Poupon & Leveaux 1971, Timur 1968,
                             Coates & Dumanoir 1973, Morris & Biggs 1967,
                             Kenyon 1997)
  petrophysics-signature   - The Petrophysics Signature Database (his
                             original Signature interpretation; src
                             signature, titles suffixed
                             " (Signature Edition)", never presented as
                             authentic public record)

32 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable,
stdlib-only Python; machine-executed OK). Petrophysics demos: the
petrophysical triangle; core-plug porosity; Darcy linear flow in darcy
units; retort saturations; rock-type classification; Folk-Ward sorting;
API gravity to hydrostatic pressure; radial Darcy well rate; Archie's
equation (Sw = 0.25 canonical); flushed-zone Sxo and movable hydrocarbon;
SP inversion to Rw; GR-to-Vsh transforms compared; Wyllie vs
Raymer-Hunt-Gardner sonic porosity; density porosity (liquid/gas/shale
cases); neutron-density combination and gas crossover; Jurin capillary
pressure and supportable column; Amott-Harvey wettability index; Corey
relative permeability and fractional flow; Vsh shale correction and model
gate; the five-minute quick-look chain; M-N crossplot mineral ID; the
routine core battery with Klinkenberg extrapolation; Simandoux vs Archie;
Brooks-Corey fit; mercury-to-reservoir Pc conversion and J-function;
NMR BVI/FFI split with Timur-Coates permeability; borehole-image dip from
sinusoid geometry; formation-tester spherical-flow permeability;
saturation-height function; Morris-Biggs permeability with flow-zone
indicator; net-pay screening with cutoffs; Monte Carlo Sw uncertainty.

Subtitle disambiguation (fields #13-26 pattern): specialty titles carry
teaching-focused subtitles rather than bare cards, e.g. "Archie's Equation:
The Master Key to Water Saturation".

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
from entries_petrophysics import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of petrophysics: "
                "clearly labeled Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked petrophysics: porosity; permeability and "
                "Darcy's law (linear and radial); saturation; reservoir rock types; pore "
                "geometry; fluid properties; Archie's equation; resistivity logging; the SP "
                "log; gamma ray; sonic, density, and neutron logs; capillary pressure; "
                "wettability; relative permeability; shale volume; quick-look interpretation; "
                "crossplots; routine core analysis; shaly-sand models; special core analysis; "
                "capillary curves and the J-function; NMR logging; borehole imaging; formation "
                "testing; saturation-height functions; permeability from logs; net pay and "
                "cutoffs; deterministic and probabilistic interpretation workflows, organized "
                "in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what petrophysics "
              "is, porosity, permeability, saturation, reservoir rock types, pore geometry, "
              "fluid properties) -> Compounded (Darcy's law in full, Archie's equation, "
              "resistivity/SP/gamma-ray/sonic/density/neutron logging, capillary pressure, "
              "wettability, relative permeability, shale volume, quick-look interpretation, "
              "crossplots, routine core analysis, shaly-sand models) -> Advanced (special "
              "core analysis, capillary curves and J-function, NMR logging, borehole imaging, "
              "formation testing, saturation-height functions, permeability from logs, net "
              "pay and cutoffs, interpretation workflows).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search porosity, Archie, permeability, resistivity, NMR, capillary, saturation, well logs...",
        "chat_ph": "Ask about petrophysics...",
        "archive_blurb": ("Seeded %s petrophysics records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled petrophysics studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about petrophysics - from porosity, permeability, and saturation through Archie's equation, well logging, capillary pressure, wettability, relative permeability, NMR, formation testing, and full reservoir characterization." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "petrophysics-study", "gen_demo_kind": "petrophysics-demo",
        "source": source,
    }

CIT_PUB = ("Petrophysics (standard texts: Tiab & Donaldson 'Petrophysics: Theory and Practice "
           "of Measuring Reservoir Rock and Fluid Transport Properties' 4th ed.; Archer & Wall "
           "'Petroleum Engineering: Principles and Practice'; Ellis & Singer 'Well Logging for "
           "Earth Scientists' 2nd ed.; Hearst, Nelson & Paillet 'Well Logging for Physical "
           "Properties' 2nd ed.; Archie 1942; Darcy 1856; Leverett 1941; Brooks & Corey 1964).")
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["petrophysics"] = _cfg(
    "petrophysics", "The Petrophysics Database",
    "Real, fact-checked petrophysics: from porosity, permeability, saturation, reservoir "
    "rock types, pore geometry, and fluid properties through Darcy's law, Archie's equation, "
    "resistivity/SP/gamma-ray/sonic/density/neutron logging, capillary pressure, wettability, "
    "relative permeability, shale volume, quick-look interpretation, crossplots, core analysis, "
    "shaly-sand models, SCAL, NMR, borehole imaging, formation testing, saturation-height "
    "functions, permeability from logs, net pay, and interpretation workflows - taught "
    "progressively along the ladder.",
    "petrophysics record", "JAH-PPH-", "JAH Petrophysics Archivist",
    "petrophysics archivist - porosity, permeability, Darcy's law, saturation, reservoir "
    "rock types, pore geometry, fluid properties, Archie's equation, resistivity/SP/gamma-"
    "ray/sonic/density/neutron logging, capillary pressure, wettability, relative "
    "permeability, shale volume, quick-look interpretation, crossplots, routine and special "
    "core analysis, shaly-sand models, J-function, NMR logging, borehole imaging, formation "
    "testing, saturation-height functions, permeability from logs, net pay and cutoffs, "
    "deterministic and probabilistic workflows; teaching progressively along the ladder "
    "from foundations through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, math, how-to - using only the "
    "system's own archive data",
    CIT_PUB, "public")
DBCFG["petrophysics-signature"] = _cfg(
    "petrophysics-signature", "The Petrophysics Signature Database",
    "His original Signature interpretation of petrophysics: the full ladder from porosity, "
    "permeability, and saturation through Archie's equation, well logging, capillary "
    "pressure, NMR, formation testing, and reservoir characterization, reframed as "
    "Signature science. Clearly labeled Signature-made, never presented as authentic "
    "public record.",
    "petrophysics record", "JAH-PPS2-", "JAH Petrophysics Archivist (Signature)",
    "petrophysics archivist - Signature editions: his original Signature "
    "interpretation of petrophysics, clearly labeled Signature-made and never "
    "presented as authentic public record; teaches progressively along the ladder "
    "from foundations through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, math, how-to - using only "
    "the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# petrophysical computation for its record. All are machine-executed by main().

_PREAMBLE = (
"import math\n"
)

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_pp_intro(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the petrophysical triangle: rock + fluid + log -> hydrocarbon pore volume
    phi = 0.22        # rock: porosity from the porosity logs
    Sw = 0.30         # fluid ownership: from Archie (resistivity + Rw)
    Rt = 15.0         # log: deep resistivity, the proxy that started it
    Shc = 1.0 - Sw
    hcpv = phi * Shc   # hydrocarbon-filled pore volume per unit bulk volume
    print("rock:  porosity phi = %.2f" % phi)
    print("fluid: Sw = %.2f -> hydrocarbon saturation = %.2f" % (Sw, Shc))
    print("log:   deep resistivity Rt = %.0f ohm-m (the proxy)" % Rt)
    print("HCPV = phi * (1 - Sw) = %.3f per unit bulk volume" % hcpv)
    assert abs(hcpv - 0.154) < 1e-9, hcpv
    assert abs((Sw + Shc) - 1.0) < 1e-12, "saturations must sum to one"
    print("rule: no proxy, no property - every number names its instrument")
    print("OK: %s worked the triangle" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_porosity(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # routine core plug: caliper + dry/saturated weighing -> porosity
    L, D = 7.62, 3.81          # cm (3-inch plug)
    Wdry, Wsat = 195.0, 208.3  # g
    rho_f = 1.0                # g/cc saturating fluid
    Vb = math.pi / 4.0 * D * D * L
    Vp = (Wsat - Wdry) / rho_f
    phi = Vp / Vb
    Vgrain = Vb - Vp
    rho_grain = Wdry / Vgrain
    print("bulk volume = %.2f cc; pore volume = %.1f cc" % (Vb, Vp))
    print("porosity = %.4f (%.1f %%)" % (phi, phi * 100))
    print("grain density = %.3f g/cc %s" % (rho_grain, "<- clean quartz" if abs(rho_grain - 2.65) < 0.05 else ""))
    assert abs(Vb - 86.875) < 0.01, Vb
    assert abs(phi - 0.1531) < 0.002, phi
    assert abs(rho_grain - 2.65) < 0.05, rho_grain
    print("rule: weigh the emptiness first - everything stands on porosity")
    print("OK: %s weighed the plug" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_permeability(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Darcy linear flow in darcy units: k = q*mu*L/(A*dp)
    q, mu, L, A, dp = 0.5, 1.0, 5.0, 11.34, 2.0   # cc/s, cP, cm, cm2, atm
    k_darcy = q * mu * L / (A * dp)
    k_md = k_darcy * 1000.0
    print("q=%.1f cc/s mu=%.0f cP L=%.0f cm A=%.2f cm2 dp=%.0f atm" % (q, mu, L, A, dp))
    print("k = %.4f darcy = %.1f mD" % (k_darcy, k_md))
    if k_md > 100:
        grade = "excellent"
    elif k_md > 10:
        grade = "good"
    elif k_md > 1:
        grade = "tight"
    else:
        grade = "unconventional"
    print("grade: %s reservoir rock" % grade)
    assert abs(k_md - 110.2) < 1.0, k_md
    assert grade == "excellent"
    print("rule: the unit was defined by the experiment - honor the units")
    print("OK: %s ran Darcy's experiment" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_saturation(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Dean-Stark retort: boil it out, trap the water, weigh the oil
    Vp = 18.0     # cc, pore volume from the porosity record
    Vw = 5.4      # cc, water in the graduated trap
    Vo = 12.6     # cc, oil by weight difference
    Sw, So = Vw / Vp, Vo / Vp
    Sg = 1.0 - Sw - So
    print("Vp=%.1f cc: water %.1f -> Sw=%.2f; oil %.1f -> So=%.2f; gas Sg=%.2f" % (Vp, Vw, Sw, Vo, So, Sg))
    print("summation check: Sw + So + Sg = %.4f" % (Sw + So + Sg))
    assert abs(Sw - 0.30) < 1e-9 and abs(So - 0.70) < 1e-9
    assert abs((Sw + So + Sg) - 1.0) < 1e-12, "the iron rule"
    print("hydrocarbon saturation = 1 - Sw = %.2f" % (1.0 - Sw))
    print("rule: the shares always sum to one - anything else is an error, not a discovery")
    print("OK: %s took the retort apart" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_rocktypes(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # four-way rock classification from (phi, k, GR, matrix density)
    def classify(phi, k_md, gr, rho_ma):
        if gr > 75:
            return "shale"
        if abs(rho_ma - 2.65) < 0.04:
            return "sandstone"
        if abs(rho_ma - 2.71) < 0.04:
            return "limestone"
        if abs(rho_ma - 2.87) < 0.06:
            return "dolomite"
        return "unknown"
    samples = [
        ((0.22, 300.0, 30.0, 2.65), "sandstone"),
        ((0.08, 50.0, 25.0, 2.71), "limestone"),
        ((0.12, 80.0, 20.0, 2.87), "dolomite"),
        ((0.25, 0.01, 110.0, 2.68), "shale"),
    ]
    for (phi, k, gr, rho_ma), expect in samples:
        got = classify(phi, k, gr, rho_ma)
        note = ""
        if got == "shale":
            note = " <- 25% porosity, zero flow: rooms with no doors"
        print("phi=%.2f k=%7.2f mD GR=%5.0f -> %-10s%s" % (phi, k, gr, got, note))
        assert got == expect, (got, expect)
    print("rule: name the family first - every transform asks sandstone or carbonate")
    print("OK: %s named the rocks" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_poregeometry(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Folk-and-Ward statistics from grain-size percentiles (phi units)
    p5, p16, p50, p84, p95 = 0.5, 1.2, 2.0, 2.8, 3.5
    sorting = (p84 - p16) / 4.0 + (p95 - p5) / 6.6
    skew = ((p84 + p16 - 2 * p50) / (2 * (p84 - p16)) +
            (p95 + p5 - 2 * p50) / (2 * (p95 - p5)))
    print("percentiles: 5%%=%.1f 16%%=%.1f 50%%=%.1f 84%%=%.1f 95%%=%.1f (phi)" % (p5, p16, p50, p84, p95))
    print("sorting = %.4f phi units -> %s" % (sorting, "well sorted" if sorting < 0.5 else ("moderately sorted" if sorting < 1.0 else "poorly sorted")))
    print("skewness = %+.3f -> %s" % (skew, "symmetrical" if abs(skew) < 0.1 else ("fine-skewed" if skew > 0 else "coarse-skewed")))
    assert abs(sorting - 0.8545) < 0.002, sorting
    assert abs(skew) < 0.01, skew
    assert 0.5 < sorting < 1.0, "moderately sorted: decent throats, some plugging"
    print("rule: the city is its streets - size the throats, not just the rooms")
    print("OK: %s sieved the sand" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_fluids(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # API gravity -> density -> hydrostatic gradient -> column pressure
    api = 35.0
    sg = 141.5 / (131.5 + api)
    rho = sg * 1000.0                       # kg/m3
    grad = 0.433 * sg                       # psi/ft
    depth_ft = 8000.0
    p_bottom = grad * depth_ft
    print("API %.0f -> SG %.4f -> density %.0f kg/m3" % (api, sg, rho))
    print("hydrostatic gradient = %.4f psi/ft" % grad)
    print("at %.0f ft: bottomhole pressure = %.0f psi" % (depth_ft, p_bottom))
    assert abs(sg - 0.8498) < 0.001, sg
    assert abs(p_bottom - 2944.0) < 5.0, p_bottom
    print("rule: convert to common conditions before comparing - fluids shapeshift with depth")
    print("OK: %s weighed the fluid column" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_darcyfull(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # radial Darcy: q = 0.00708*k*h*dp/(mu*B*ln(re/rw)) -> STB/day
    k, h, dp = 100.0, 50.0, 1000.0     # mD, ft, psi
    mu, B = 1.0, 1.2                   # cP, RB/STB
    re, rw = 1000.0, 0.5               # ft
    q = 0.00708 * k * h * dp / (mu * B * math.log(re / rw))
    print("k=%.0f mD h=%.0f ft dp=%.0f psi mu=%.1f B=%.1f re/rw=%.0f" % (k, h, dp, mu, B, re / rw))
    print("ln(re/rw) = %.2f; q = %.0f STB/day" % (math.log(re / rw), q))
    assert 3800.0 < q < 3960.0, q
    # sensitivities: halving k halves q; doubling re barely moves the log
    q_halfk = 0.00708 * (k / 2) * h * dp / (mu * B * math.log(re / rw))
    q_bigre = 0.00708 * k * h * dp / (mu * B * math.log(2 * re / rw))
    print("half the permeability -> %.0f STB/day (halved)" % q_halfk)
    print("double the drainage radius -> %.0f STB/day (log barely moves)" % q_bigre)
    assert abs(q_halfk - q / 2) < 1.0
    assert abs(q_bigre - q) / q < 0.10
    print("rule: the logarithm is merciful to the far field and merciless near the well")
    print("OK: %s produced the well" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_archie(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Archie's equation, the canonical textbook example
    a, m, n = 1.0, 2.0, 2.0
    Rw, phi, Rt = 0.05, 0.20, 20.0     # ohm-m, fraction, ohm-m
    F = a / (phi ** m)
    Ro = F * Rw
    Sw = (a * Rw / ((phi ** m) * Rt)) ** (1.0 / n)
    print("formation factor F = a/phi^m = %.1f; Ro = F*Rw = %.2f ohm-m" % (F, Ro))
    print("Sw = (a*Rw/(phi^m*Rt))^(1/n) = %.4f" % Sw)
    print("hydrocarbon saturation = %.2f" % (1.0 - Sw))
    assert abs(F - 25.0) < 1e-9, F
    assert abs(Ro - 1.25) < 1e-9, Ro
    assert abs(Sw - 0.25) < 1e-9, Sw
    # sensitivity: the fragile input is Rw
    Sw_hi = (a * (Rw * 1.2) / ((phi ** m) * Rt)) ** (1.0 / n)
    print("Rw 20%% high -> Sw = %.3f (the fragile input moves the answer)" % Sw_hi)
    assert Sw_hi > Sw
    print("rule: the rock confesses through its resistance - measure Rw like it matters, it does")
    print("OK: %s turned the master key" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_resistivity(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # invasion profile: flushed zone vs uninvaded -> movable hydrocarbon
    a, m, n = 1.0, 2.0, 2.0
    phi = 0.20
    Rt, Rw = 20.0, 0.05       # deep: uninvaded zone
    Rxo, Rmf = 10.0, 0.20     # shallow: flushed zone, mud filtrate
    Sw = (a * Rw / ((phi ** m) * Rt)) ** (1.0 / n)
    Sxo = (a * Rmf / ((phi ** m) * Rxo)) ** (1.0 / n)
    movable = Sxo - Sw
    print("deep:  Rt=%.0f Rw=%.2f -> Sw  = %.3f" % (Rt, Rw, Sw))
    print("shallow: Rxo=%.0f Rmf=%.2f -> Sxo = %.3f" % (Rxo, Rmf, Sxo))
    print("movable hydrocarbon = Sxo - Sw = %.3f" % movable)
    assert abs(Sw - 0.25) < 1e-9
    assert abs(Sxo - 0.7071) < 0.001, Sxo
    assert 0.45 < movable < 0.47, movable
    assert movable > 0, "positive movable oil: the filtrate pushed oil, so oil was there"
    print("rule: read at three depths - the flushed skin may lie, the deep formation tells")
    print("OK: %s read the invasion" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_sp(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # SP: SSP = -K*log10(Rmf/Rw), then invert a measured deflection back to Rw
    T_F = 200.0
    K = 61.0 + 0.133 * T_F
    Rmf, Rw_true = 0.5, 0.05
    SSP = -K * math.log10(Rmf / Rw_true)
    print("T=%.0f F -> K=%.1f mV; Rmf=%.1f Rw=%.2f" % (T_F, K, Rmf, Rw_true))
    print("static SP = %.1f mV" % SSP)
    assert abs(SSP - (-87.6)) < 0.05, SSP
    # invert: a measured -60 mV deflection -> Rw
    SP_meas = -60.0
    Rw = Rmf / (10.0 ** (-SP_meas / K))
    print("measured SP = %.0f mV -> Rw = %.4f ohm-m" % (SP_meas, Rw))
    assert abs(Rw - 0.1033) < 0.001, Rw
    print("rule: the formation speaks without being asked - listen to the free channels first")
    print("OK: %s inverted the spontaneous potential" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_gr(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # GR -> IGR -> Vsh by four transforms: the interpreter's judgment call
    GR, GRmin, GRmax = 75.0, 20.0, 120.0
    IGR = (GR - GRmin) / (GRmax - GRmin)
    vsh_lin = IGR
    vsh_lar_old = 0.33 * (2.0 ** (2.0 * IGR) - 1.0)
    vsh_stieber = IGR / (3.0 - 2.0 * IGR)
    vsh_lar_tert = 0.083 * (2.0 ** (3.7 * IGR) - 1.0)
    print("GR=%.0f API (anchors %.0f/%.0f) -> IGR=%.2f" % (GR, GRmin, GRmax, IGR))
    print("  linear (max)              Vsh = %.3f" % vsh_lin)
    print("  Larionov older rocks      Vsh = %.3f" % vsh_lar_old)
    print("  Stieber                  Vsh = %.3f" % vsh_stieber)
    print("  Larionov Tertiary        Vsh = %.3f" % vsh_lar_tert)
    assert abs(IGR - 0.55) < 1e-9
    assert abs(vsh_lar_old - 0.3774) < 0.002, vsh_lar_old
    assert vsh_lar_tert < vsh_stieber < vsh_lar_old < vsh_lin, "transform ordering"
    print("spread: %.2f porosity-units of judgment - transform choice moves reserves" % (vsh_lin - vsh_lar_tert))
    print("rule: the shale announces itself; the quiet rock is measured by subtraction")
    print("OK: %s read the shale detector" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_sonic(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Wyllie time-average vs Raymer-Hunt-Gardner, plus compaction correction
    dt, dtma, dtf = 90.0, 55.5, 189.0     # us/ft; sandstone matrix, fluid
    phi_wyllie = (dt - dtma) / (dtf - dtma)
    phi_rhg = (5.0 / 8.0) * (dt - dtma) / dt
    phi_comp = phi_wyllie / 1.3           # unconsolidated-sand compaction correction
    print("dt=%.0f us/ft (ss matrix %.1f, fluid %.0f)" % (dt, dtma, dtf))
    print("  Wyllie time-average      phi = %.4f" % phi_wyllie)
    print("  Raymer-Hunt-Gardner      phi = %.4f" % phi_rhg)
    print("  Wyllie + compaction /1.3 phi = %.4f" % phi_comp)
    assert abs(phi_wyllie - 0.2584) < 0.001, phi_wyllie
    assert abs(phi_rhg - 0.2396) < 0.001, phi_rhg
    assert 0.19 < phi_comp < 0.21
    assert phi_rhg < phi_wyllie, "RHG tempers Wyllie's high-porosity overshoot"
    print("rule: sound cannot lie about its journey - but vugs and gas make it take shortcuts")
    print("OK: %s timed the sound" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_density(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # density porosity: liquid case, gas case, shale-corrected
    rho_b, rho_ma = 2.20, 2.65
    phi_liquid = (rho_ma - rho_b) / (rho_ma - 1.0)
    phi_gas = (rho_ma - rho_b) / (rho_ma - 0.2)
    Vsh, phi_sh = 0.38, 0.05
    phi_corr = phi_liquid - Vsh * phi_sh
    print("rho_b=%.2f rho_ma=%.2f" % (rho_b, rho_ma))
    print("  liquid-filled (rho_f=1.0) phi = %.4f" % phi_liquid)
    print("  gas-filled    (rho_f=0.2) phi = %.4f" % phi_gas)
    print("  shale-corrected           phi = %.4f" % phi_corr)
    assert abs(phi_liquid - 0.2727) < 0.001, phi_liquid
    assert abs(phi_gas - 0.1837) < 0.001, phi_gas
    assert abs(phi_corr - 0.2537) < 0.001, phi_corr
    print("fluid assumption swings the answer %.1f p.u. - never trust density porosity in gas alone" % ((phi_liquid - phi_gas) * 100))
    print("rule: the simplest transform is the most robust - one subtraction, one division")
    print("OK: %s weighed the rock with light" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_neutron(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # neutron-density combination; gas crossover diagnosis
    phi_d, phi_n = 0.27, 0.30
    phi_x = math.sqrt((phi_d ** 2 + phi_n ** 2) / 2.0)
    print("liquid case: phi_d=%.2f phi_n=%.2f -> combined phi = %.4f" % (phi_d, phi_n, phi_x))
    assert abs(phi_x - 0.2854) < 0.002, phi_x
    # gas case: density soars, neutron collapses
    gd, gn = 0.25, 0.10
    sep = gd - gn
    print("gas case:    phi_d=%.2f phi_n=%.2f -> separation %.2f %s" % (gd, gn, sep, "<- CROSSOVER: gas" if gn < gd - 0.05 else ""))
    assert gn < gd - 0.05, "neutron must collapse below density in gas"
    # shale case: both high together, no crossover
    sd, sn = 0.30, 0.33
    print("shale case:  phi_d=%.2f phi_n=%.2f -> both high, no crossover: shale, not gas" % (sd, sn))
    assert not (sn < sd - 0.05)
    print("rule: hunt the hydrogen atom and let the pair diagnose - crossover is gas, twins are shale")
    print("OK: %s hunted hydrogen" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_capillary(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Jurin's law: Pc = 2*sigma*cos(theta)/r -> supportable hydrocarbon column
    sigma, theta = 0.03, 0.0          # N/m, radians (water-wet)
    drho, g = 200.0, 9.80665         # kg/m3 contrast, m/s2
    for r_um in (1.0, 10.0):
        r = r_um * 1e-6
        Pc = 2.0 * sigma * math.cos(theta) / r
        h = Pc / (drho * g)
        print("throat r=%4.0f um: Pc=%7.0f Pa (%4.1f psi) supports h=%6.1f m (%5.0f ft)" % (
            r_um, Pc, Pc / 6894.76, h, h * 3.28084))
        if r_um == 1.0:
            assert abs(Pc - 60000.0) < 1.0, Pc
            assert abs(h - 30.58) < 0.1, h
        else:
            assert abs(h - 3.058) < 0.02, h
    print("ten times the throat, one-tenth the column: tight rock wears a tall transition zone")
    print("rule: the curved interface negotiates - and the negotiation scales as 1/r")
    print("OK: %s curved the interface" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_wettability(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Amott-Harvey index from spontaneous/forced imbibition volumes
    Vosp, Vot = 8.0, 10.0    # water displacing oil: spontaneous / total
    Vo_sp, Vo_t = 1.0, 10.0  # oil displacing water: spontaneous / total
    Iw, Io = Vosp / Vot, Vo_sp / Vo_t
    index = Iw - Io
    if index > 0.3:
        wet = "water-wet"
    elif index < -0.3:
        wet = "oil-wet"
    else:
        wet = "intermediate/mixed-wet"
    print("Iw = %.2f (water imbibes eagerly); Io = %.2f (oil does not)" % (Iw, Io))
    print("Amott-Harvey index = %+.2f -> %s" % (index, wet))
    assert abs(index - 0.70) < 1e-9, index
    assert wet == "water-wet"
    print("consequence: oil sits in pore centers, free to flow; water clings to grains")
    print("rule: ask what every surface is loyal to before predicting any flow")
    print("OK: %s tested the loyalty" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_relperm(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Corey relative permeability + fractional flow at Sw = 0.50
    Swirr, Sor = 0.20, 0.25
    krw0, kro0, nw, no = 0.30, 0.90, 2.0, 2.0
    muw, muo = 0.5, 2.0
    Sw = 0.50
    Swn = (Sw - Swirr) / (1.0 - Swirr - Sor)
    krw = krw0 * Swn ** nw
    kro = kro0 * (1.0 - Swn) ** no
    fw = 1.0 / (1.0 + (kro * muw) / (krw * muo))
    print("Sw=%.2f -> Swn=%.4f" % (Sw, Swn))
    print("krw=%.4f kro=%.4f" % (krw, kro))
    print("fractional flow of water fw = %.4f" % fw)
    assert abs(krw - 0.0893) < 0.001, krw
    assert abs(kro - 0.1860) < 0.001, kro
    assert abs(fw - 0.6575) < 0.005, fw
    # endpoints: only oil flows at Swirr, only water at 1-Sor
    Swn0 = 0.0
    assert krw0 * Swn0 ** nw == 0.0 and kro0 * (1 - Swn0) ** no == kro0
    print("at 50%% water saturation, %.0f%% of production is water: viscosity wins races" % (fw * 100))
    print("rule: two fluids in one rock is a treaty - read the treaty curves")
    print("OK: %s shared the rock" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_vsh(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Vsh in action: shale-correct the porosity, gate the saturation model
    phi_d = 0.2727
    Vsh, phi_sh = 0.38, 0.05
    phi_corr = phi_d - Vsh * phi_sh
    if Vsh < 0.10:
        model = "clean Archie"
    elif Vsh <= 0.40:
        model = "shaly-sand (Simandoux / Waxman-Smits / Indonesia)"
    else:
        model = "not reservoir - no saturation computed"
    print("Vsh=%.2f: phi %.4f -> corrected %.4f" % (Vsh, phi_d, phi_corr))
    print("saturation model gate -> %s" % model)
    assert abs(phi_corr - 0.2537) < 0.001, phi_corr
    assert model.startswith("shaly-sand"), model
    print("a 0.1 Vsh error moves phi, Sw, k, and net pay - weigh the impurity first")
    print("rule: subtract what was never reservoir before believing the reservoir")
    print("OK: %s corrected for clay" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_quicklook(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the five-minute quick-look chain on one zone
    # 1. Vsh from GR (Larionov, older rocks)
    IGR = (60.0 - 20.0) / (120.0 - 20.0)
    Vsh = 0.33 * (2.0 ** (2.0 * IGR) - 1.0)
    # 2. porosity: density (shale-corrected) + sonic, averaged
    phi_d = (2.65 - 2.25) / (2.65 - 1.0) - Vsh * 0.05
    phi_s = (80.0 - 55.5) / (189.0 - 55.5)
    phi = (phi_d + phi_s) / 2.0
    # 3. Rw from SP
    K = 61.0 + 0.133 * 200.0
    Rw = 0.5 / (10.0 ** (70.0 / K))
    # 4. Sw from Archie
    Sw = (1.0 * Rw / ((phi ** 2.0) * 25.0)) ** 0.5
    # 5. cutoffs and verdict
    pay = (phi >= 0.10) and (Vsh <= 0.40) and (Sw <= 0.60)
    hcpv = phi * (1.0 - Sw)
    print("1. Vsh = %.3f | 2. phi = %.3f (d %.3f s %.3f)" % (Vsh, phi, phi_d, phi_s))
    print("3. Rw = %.4f ohm-m | 4. Sw = %.3f" % (Rw, Sw))
    print("5. cutoffs phi/Vsh/Sw: %s -> %s (HCPV %.3f)" % (
        "pass/pass/pass" if pay else "FAIL", "PAY" if pay else "NO PAY", hcpv))
    assert abs(Vsh - 0.2446) < 0.002, Vsh
    assert abs(phi - 0.2069) < 0.002, phi
    assert abs(Rw - 0.0794) < 0.002, Rw
    assert abs(Sw - 0.2724) < 0.003, Sw
    assert pay, "this zone must pay"
    print("IOUs: m=n=2 assumed (repay with core); Vsh transform chosen (repay with XRD); gas unchecked")
    print("rule: triage in five minutes, and write down every debt")
    print("OK: %s did the quick look" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_crossplot(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # M-N crossplot: identify the mineral by nearest fixed point
    dt, rho_b, phiN = 60.0, 2.50, 0.10
    dtf, rho_f, phiNf = 189.0, 1.0, 1.0
    M = (dtf - dt) / (rho_b - rho_f) * 0.01
    N = (phiNf - phiN) / (rho_b - rho_f)
    minerals = {"sandstone": (0.81, 0.64), "limestone": (0.83, 0.59), "dolomite": (0.78, 0.49)}
    print("M = %.3f  N = %.3f" % (M, N))
    best, bestd = None, 1e9
    for mname, (Mm, Nm) in minerals.items():
        d = math.sqrt((M - Mm) ** 2 + (N - Nm) ** 2)
        print("  distance to %-10s (%.2f, %.2f): %.4f" % (mname, Mm, Nm, d))
        if d < bestd:
            best, bestd = mname, d
    print("identified: %s" % best)
    assert abs(M - 0.86) < 0.005 and abs(N - 0.60) < 0.005
    assert best == "limestone", best
    # Pickett check: slope -m on synthetic water-zone data (m = 2)
    import math as _m
    phis = [0.10, 0.15, 0.20, 0.25]
    Rts = [0.05 / (p ** 2) for p in phis]   # water zone: Rt = Rw/phi^m
    slope = (_m.log10(Rts[-1]) - _m.log10(Rts[0])) / (_m.log10(phis[-1]) - _m.log10(phis[0]))
    print("Pickett water-line slope = %.3f -> m = %.2f" % (slope, -slope))
    assert abs(-slope - 2.0) < 0.01
    print("rule: build the plot where the inputs become outputs - let the data confess")
    print("OK: %s crossed the plots" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_routinecore(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the routine core battery: porosity, grain-density check, Klinkenberg
    L, D = 7.62, 3.81
    Wdry, Wsat = 195.0, 208.3
    Vb = math.pi / 4 * D * D * L
    Vp = Wsat - Wdry
    phi = Vp / Vb
    rho_grain = Wdry / (Vb - Vp)
    print("porosity = %.4f; grain density = %.3f g/cc (quartz check)" % (phi, rho_grain))
    assert abs(phi - 0.1531) < 0.002, phi
    assert abs(rho_grain - 2.65) < 0.02, rho_grain
    # Klinkenberg: kg at pm = 1, 2, 4 atm -> extrapolate vs 1/pm
    pm = [1.0, 2.0, 4.0]
    kg = [120.0, 110.0, 105.0]
    x = [1.0 / p for p in pm]
    n = 3
    Sx, Sy = sum(x), sum(kg)
    Sxx = sum(v * v for v in x)
    Sxy = sum(a * b for a, b in zip(x, kg))
    slope = (n * Sxy - Sx * Sy) / (n * Sxx - Sx * Sx)
    k_inf = (Sy - slope * Sx) / n
    print("Klinkenberg: kg vs 1/pm -> k_inf = %.1f mD (gas slip removed)" % k_inf)
    assert abs(k_inf - 100.0) < 1.0, k_inf
    print("rule: honor the witness, cross-examine it - stress, invasion, depth-shift")
    print("OK: %s ran the core battery" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_shalysand(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Simandoux vs clean Archie: the pay that clay was hiding
    a, m, n = 1.0, 2.0, 2.0
    phi, Rt, Rw = 0.25, 8.0, 0.05
    Vsh, Rsh = 0.30, 4.0
    Sw_archie = (a * Rw / ((phi ** m) * Rt)) ** (1.0 / n)
    # Simandoux: 1/Rt = (phi^m*Sw^n)/(a*Rw*(1-Vsh)) + Vsh*Sw/Rsh -> quadratic
    A = (phi ** m) / (a * Rw * (1.0 - Vsh))
    B = Vsh / Rsh
    C = -1.0 / Rt
    Sw_sim = (-B + math.sqrt(B * B - 4 * A * C)) / (2 * A)
    print("clean Archie: Sw = %.4f" % Sw_archie)
    print("Simandoux:    Sw = %.4f" % Sw_sim)
    print("correction: %.1f saturation units of water removed = hidden pay" % ((Sw_archie - Sw_sim) * 100))
    assert abs(Sw_archie - 0.3162) < 0.001, Sw_archie
    assert abs(Sw_sim - 0.2444) < 0.002, Sw_sim
    assert Sw_sim < Sw_archie, "clay conductivity fakes water: correction must lower Sw"
    print("rule: give the clay its term - never let an unmodeled conductor vote in secret")
    print("OK: %s corrected the shaly sand" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_scal(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Brooks-Corey fit from two porous-plate points: Pd and lambda
    Swirr = 0.20
    (Sw1, Pc1), (Sw2, Pc2) = (0.50, 10.0), (0.30, 40.0)   # psi
    Se1 = (Sw1 - Swirr) / (1.0 - Swirr)
    Se2 = (Sw2 - Swirr) / (1.0 - Swirr)
    lam = -math.log(Se2 / Se1) / math.log(Pc2 / Pc1)
    Pd = Pc1 * Se1 ** (1.0 / lam)
    print("Se: %.3f @ %.0f psi; %.3f @ %.0f psi" % (Se1, Pc1, Se2, Pc2))
    print("lambda = %.4f (%s)" % (lam, "uniform throats" if lam > 0.6 else "wide throat distribution"))
    print("Pd = %.2f psi (largest throat's entry pressure)" % Pd)
    assert abs(lam - 0.7925) < 0.005, lam
    assert abs(Pd - 2.90) < 0.1, Pd
    # verify the fit reproduces both points
    for Se, Pc in ((Se1, Pc1), (Se2, Pc2)):
        assert abs(Pd * Se ** (-1.0 / lam) - Pc) < 0.01
    print("rule: patience as an instrument - weeks of equilibration, two reservoir parameters")
    print("OK: %s fitted the drainage curve" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_pccurves(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # mercury-air -> reservoir oil-water conversion; Leverett J-function
    Pc_lab = 100.0   # psi, mercury-air
    num = 30.0 * math.cos(math.radians(30.0))       # oil-water
    den = 480.0 * abs(math.cos(math.radians(140.0)))  # mercury-air
    Pc_res = Pc_lab * num / den
    print("lab Hg-air %.0f psi -> reservoir oil-water %.2f psi" % (Pc_lab, Pc_res))
    assert 7.0 < Pc_res < 7.2, Pc_res
    # J-function: dimensionless and portable
    Pc, sigma, theta, k, phi = 5.0, 30.0, 0.0, 100.0, 0.20
    J = (Pc / (sigma * math.cos(theta))) * math.sqrt(k / phi)
    print("J = (Pc/(sigma*cos th))*sqrt(k/phi) = %.3f (dimensionless)" % J)
    assert abs(J - 3.727) < 0.01, J
    print("one J-curve serves every plug of the rock type: the SCAL-to-model multiplier")
    print("rule: normalize away the size and the truth is one curve")
    print("OK: %s scaled the capillary" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_nmr(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # T2 distribution -> BVI/FFI split -> Timur-Coates permeability
    import math as _m
    T2 = [3.0, 10.0, 30.0, 100.0, 300.0]      # ms bin centers
    amp = [10.0, 20.0, 10.0, 30.0, 30.0]
    cutoff = 33.0
    tot = sum(amp)
    bvi_frac = sum(a for t, a in zip(T2, amp) if t < cutoff) / tot
    ffi_frac = 1.0 - bvi_frac
    phi_nmr = 0.25
    BVI, FFI = bvi_frac * phi_nmr, ffi_frac * phi_nmr
    k = ((phi_nmr * 100.0) / 10.0) ** 4 * (FFI / BVI) ** 2   # Timur-Coates, phi in %
    T2lm = _m.exp(sum(a * _m.log(t) for t, a in zip(T2, amp)) / tot)
    print("T2 cutoff %.0f ms: BVI = %.3f (bound), FFI = %.3f (free/movable)" % (cutoff, BVI, FFI))
    print("Timur-Coates k = %.1f mD; log-mean T2 = %.1f ms" % (k, T2lm))
    assert abs(BVI - 0.10) < 1e-9 and abs(FFI - 0.15) < 1e-9
    assert 80.0 < k < 95.0, k
    assert 50.0 < T2lm < 60.0, T2lm
    print("movable fluid identified with no Archie, no Rw, no resistivity")
    print("rule: measure freedom by how long the signal sings")
    print("OK: %s relaxed the nuclei" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_imaging(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # borehole image: dip from sinusoid geometry; classify the sinusoids
    height, diameter = 0.60, 0.20    # m, peak-to-trough; borehole diameter
    dip = math.degrees(math.atan(height / diameter))
    trough_az = 180.0                # degrees on the unrolled image
    print("sinusoid height %.2f m in %.2f m hole -> dip = %.1f deg, dip azimuth %.0f" % (height, diameter, dip, trough_az))
    assert 71.0 < dip < 72.5, dip
    picks = [
        ("dark continuous full sinusoid", "open fracture - conductive, flowing"),
        ("bright continuous sinusoid", "cemented fracture - resistive, dead"),
        ("faint regular sinusoid set", "bedding - sedimentary layering"),
    ]
    for desc, interp in picks:
        print("  %-32s -> %s" % (desc, interp))
    print("two dark vertical bands 180 deg apart -> breakouts: minimum horizontal stress azimuth")
    print("rule: stop averaging and look - a photograph beats a proxy")
    print("OK: %s photographed the wall" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_formationtest(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # wireline formation tester: spherical-flow k from drawdown
    q, mu = 1e-6, 1e-3        # m3/s, Pa-s
    r_p, dp = 0.01, 1e5       # m probe radius, Pa drawdown
    k_si = q * mu / (4.0 * math.pi * r_p * dp)
    k_md = k_si * 1.01325e15
    mobility = k_md / (mu * 1000.0)   # mD/cP
    print("drawdown: q=%.0e m3/s dp=%.0f kPa -> k = %.2e m2 = %.1f mD" % (q, dp / 1000, k_si, k_md))
    print("mobility k/mu = %.1f mD/cP" % mobility)
    assert 70.0 < k_md < 90.0, k_md
    assert 70.0 < mobility < 90.0, mobility
    # pressure survey reading: gradient break = contact
    grads = [(8000.0, 3500.0), (8100.0, 3543.0), (8200.0, 3575.0)]  # depth ft, pressure psi
    g1 = (grads[1][1] - grads[0][1]) / (grads[1][0] - grads[0][0])
    g2 = (grads[2][1] - grads[1][1]) / (grads[2][0] - grads[1][0])
    print("gradient above %.3f psi/ft, below %.3f psi/ft %s" % (g1, g2, "<- BREAK: fluid contact" if abs(g1 - g2) > 0.05 else ""))
    assert abs(g1 - g2) > 0.05, "the break must show"
    print("rule: take the pulse in many places - pressure is the reservoir's pulse")
    print("OK: %s tested the formation" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_satheight(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # saturation-height function from the Brooks-Corey SCAL fit
    Pd, lam, Swirr = 20000.0, 0.79, 0.20   # Pa, -, -
    drho, g = 200.0, 9.80665
    def height(Sw):
        Se = (Sw - Swirr) / (1.0 - Swirr)
        Pc = Pd * Se ** (-1.0 / lam)
        return Pc / (drho * g)
    h50 = height(0.50)
    h25 = height(0.25)
    print("Sw=0.50 at h = %.1f m above FWL" % h50)
    print("Sw=0.25 at h = %.1f m above FWL" % h25)
    assert 34.0 < h50 < 37.0, h50
    assert h25 > h50, "near-irreducible saturation lives much higher"
    assert h25 > 300.0, h25
    print("transition zone: %.0f m tall - tight throats wear a tall transition" % h25)
    print("rule: draw the beach, never just the waterline")
    print("OK: %s mapped the transition zone" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_permfromlogs(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Morris-Biggs permeability + flow-zone indicator fingerprint
    phi, Swirr = 0.20, 0.25
    k = (100.0 * phi ** 2.25 / Swirr) ** 2
    RQI = 0.0314 * math.sqrt(k / phi)      # microns
    phi_z = phi / (1.0 - phi)
    FZI = RQI / phi_z
    print("Morris-Biggs: k = (100*phi^2.25/Swirr)^2 = %.1f mD" % k)
    print("RQI = %.3f um; FZI = %.3f um (this rock's hydraulic fingerprint)" % (RQI, FZI))
    assert 100.0 < k < 130.0, k
    assert 2.9 < FZI < 3.1, FZI
    print("workflow: cluster core by FZI, fit k-phi per unit, apply by unit in uncored wells")
    print("rule: estimation with its receipt - show the calibration crossplot, always")
    print("OK: %s estimated permeability honestly" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_netpay(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # net-pay screening: three cutoffs, foot by foot
    C_PHI, C_VSH, C_SW = 0.08, 0.40, 0.60
    zones = [  # (thickness ft, phi, Vsh, Sw)
        (10.0, 0.22, 0.10, 0.25),
        (10.0, 0.18, 0.20, 0.35),
        (10.0, 0.06, 0.15, 0.30),
        (10.0, 0.20, 0.50, 0.30),
        (10.0, 0.16, 0.25, 0.70),
    ]
    net, hcpv, gross = 0.0, 0.0, 0.0
    for h, phi, vsh, sw in zones:
        gross += h
        ok = phi >= C_PHI and vsh <= C_VSH and sw <= C_SW
        why = "PAY" if ok else "fails %s" % (
            "porosity" if phi < C_PHI else ("Vsh" if vsh > C_VSH else "Sw"))
        print("h=%4.0f phi=%.2f Vsh=%.2f Sw=%.2f -> %s" % (h, phi, vsh, sw, why))
        if ok:
            net += h
            hcpv += h * phi * (1.0 - sw)
    print("net pay = %.0f ft of %.0f (net-to-gross %.2f); HCPV = %.2f ft of hydrocarbon column" % (net, gross, net / gross, hcpv))
    assert net == 20.0, net
    assert abs(net / gross - 0.40) < 1e-9
    assert abs(hcpv - 2.82) < 0.01, hcpv
    print("rule: name the gates out loud - judgment must be auditable")
    print("OK: %s flagged the pay" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pp_workflows(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Monte Carlo honesty check on the deterministic Archie answer
    import random
    random.seed(42)
    Rw, m, n = 0.05, 2.0, 2.0
    det = (Rw / ((0.20 ** m) * 20.0)) ** (1.0 / n)
    N = 2000
    samples = []
    for _ in range(N):
        phi = random.gauss(0.20, 0.01)
        Rt = random.gauss(20.0, 1.0)
        if phi <= 0 or Rt <= 0:
            continue
        samples.append((Rw / ((phi ** m) * Rt)) ** (1.0 / n))
    samples.sort()
    p10, p50, p90 = samples[int(0.1 * N)], samples[int(0.5 * N)], samples[int(0.9 * N)]
    print("deterministic Sw = %.3f" % det)
    print("Monte Carlo: P10 = %.3f  P50 = %.3f  P90 = %.3f" % (p10, p50, p90))
    assert abs(det - 0.25) < 1e-9
    assert abs(p50 - det) < 0.015, p50
    assert p10 < p50 < p90, "doubt must bracket the answer"
    assert (p90 - p10) > 0.03, "measurement noise alone spreads the answer"
    print("the answer is 0.25, plus-or-minus noise - book the doubt with the number")
    print("rule: uncertainty is not the enemy; hidden uncertainty is")
    print("OK: %s attached the doubt" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "what_is_petrophysics": demo_pp_intro, "porosity": demo_pp_porosity,
    "permeability_intro": demo_pp_permeability, "saturation_intro": demo_pp_saturation,
    "reservoir_rock_types": demo_pp_rocktypes, "pore_geometry": demo_pp_poregeometry,
    "fluid_properties": demo_pp_fluids, "darcy_full": demo_pp_darcyfull,
    "archie": demo_pp_archie, "resistivity_log": demo_pp_resistivity,
    "sp_log": demo_pp_sp, "gamma_ray": demo_pp_gr,
    "sonic_log": demo_pp_sonic, "density_log": demo_pp_density,
    "neutron_log": demo_pp_neutron, "capillary_intro": demo_pp_capillary,
    "wettability": demo_pp_wettability, "relative_perm": demo_pp_relperm,
    "vsh": demo_pp_vsh, "quicklook": demo_pp_quicklook,
    "crossplots": demo_pp_crossplot, "routine_core": demo_pp_routinecore,
    "shaly_sand": demo_pp_shalysand, "scal": demo_pp_scal,
    "pc_curves": demo_pp_pccurves, "nmr": demo_pp_nmr,
    "borehole_imaging": demo_pp_imaging, "formation_testing": demo_pp_formationtest,
    "saturation_height": demo_pp_satheight, "perm_from_logs": demo_pp_permfromlogs,
    "net_pay": demo_pp_netpay, "interpretation_workflows": demo_pp_workflows,
}
assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"


def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_petrophysics.py).
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
    for slug in ("petrophysics", "petrophysics-signature"):
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
