#!/usr/bin/env python3
"""Build the Tunneling (Mining) field databases for JAH Databases (field #27, taxonomy order).

Verified 2026-10-17 (see entries_tunneling.py docstring): NO database
covers tunneling as a specialty discipline. Manifest search (2354
databases): no 'tunneling' database. Nearest neighbors:
'mining-extraction-published'/'mining-extraction-study' (mine production;
tunnel-term titles are title-only stubs, no descriptions) and
'civil-engineering-study' (single-topic gasket studies). Whole-system title
sweep over all 753 shard indexes + full-text sweep over all 1,129,321
records ('tunnel boring machine', 'q-system', 'new austrian', 'rock mass
rating', 'raise bor', 'shaft sink', 'ground support pressure', 'tunnel
ventilation'): ZERO full-record discipline coverage anywhere.

So this build creates two NEW databases, 34 ladder-ordered records each,
covering ONLY what the system left uncovered:

  tunneling                  - The Tunneling Database (public-harvest: real,
                               fact-checked tunneling engineering; citations
                               Hoek & Brown 1980, Bieniawski 1989,
                               Barton/Lien/Lunde 1974, Hoek/Carranza-Torres/
                               Corkum 2002, ITA guidelines, FHWA-NHI-09-010
                               (2009), Maidl et al. 2008, USACE EM 1110-2-2901
                               (1997), Kolymbas 2005, Wittke 1990,
                               Singh & Goel 1999, Austrian Society for
                               Geomechanics NATM guideline, British
                               Tunnelling Society Tunnel Lining Design Guide
                               2004, Rostami & Ozdemir CSM 1993)
  tunneling-signature        - The Tunneling Signature Database (his original
                               Signature interpretation; src signature,
                               titles suffixed " (Signature Edition)", never
                               presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable,
stdlib-only Python; machine-executed OK). Tunneling demos: excavation and
muck volumes with swell; alignment savings; section areas by tunnel type;
equivalent dimension; method-selection scoring; cut-and-cover trench
geometry; portal approach-cut volume; drill-and-blast cycle advance; powder
factor and hole count; RMR scoring to Class III; Q-system to 3.52;
Hoek-Brown parameters from GSI; rock-bolt length and pull-out capacity;
shotcrete volume with rebound; Terzaghi steel-set rock load;
convergence-confinement alarm check; roadheader specific energy; TBM type
selection logic; TBM daily advance from penetration x utilization; muck
haulage truck count; Terzaghi vs Barton support pressure; segmental ring
thrust; ventilation flow and face velocity; Dupuit dewatering rate;
convergence stability reading; egress-time check; shaft sinking schedule;
compressed-air balance pressure; raise-boring schedule; cutter-change
count; immersed-element buoyancy and ballast; refurbishment condition
scoring; squeezing-ground Q collapse; cost-per-metre economics.

Subtitle disambiguation (fields #13-26 pattern): specialty titles carry
teaching-focused subtitles rather than bare cards, e.g. "Q-System: Barton's
Tunneling Quality Index, the Support Designer".

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
from entries_tunneling import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of tunneling "
                "engineering: clearly labeled Signature-made, never presented as authentic "
                "public record.")
    pub_line = ("Public records - real, fact-checked tunneling engineering: tunnel types; "
                "the ground as structure and stand-up time; excavation methods "
                "(drill-and-blast, TBM, roadheader, cut-and-cover); portals; blast design; "
                "RMR, Q-system, and GSI ground classification; rock bolts, shotcrete, and "
                "steel sets; NATM/SEM; TBM types and advance rates; mucking and haulage; "
                "ground support pressure; tunnel lining design; ventilation; dewatering; "
                "monitoring and instrumentation; safety and rescue; shaft sinking; "
                "compressed-air working; raise boring; cutterhead design and cutter wear; "
                "immersed tunnels; refurbishment; fault zones and squeezing ground; "
                "tunneling economics, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what tunneling "
              "is, why tunnels, tunnel types, the ground as structure, excavation methods, "
              "cut-and-cover, portals) -> Compounded (drill-and-blast cycle and design, "
              "RMR, Q-system, GSI, rock bolts, shotcrete, steel sets, NATM/SEM, "
              "roadheaders, TBM types and advance, mucking and haulage) -> Advanced "
              "(support pressure, lining design, ventilation, dewatering, monitoring, "
              "safety and rescue, shaft sinking, compressed air, raise boring, cutter "
              "wear, immersed tunnels, refurbishment, squeezing ground, economics).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search Q-system, RMR, TBM, shotcrete, rock bolts, NATM, ventilation, shaft, lining...",
        "chat_ph": "Ask about tunneling...",
        "archive_blurb": ("Seeded %s tunneling records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled tunneling studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about tunneling - from tunnel types, excavation methods, and ground classification through rock support, TBMs, ventilation, lining design, shaft sinking, and tunneling economics." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "tunneling-study", "gen_demo_kind": "tunneling-demo",
        "source": source,
    }

CIT_PUB = ("Tunneling engineering (standard texts: Hoek & Brown 'Underground Excavations in "
           "Rock' 1980; Bieniawski 'Engineering Rock Mass Classifications' 1989; "
           "Barton, Lien & Lunde 1974; Hoek, Carranza-Torres & Corkum 2002; ITA "
           "guidelines; FHWA 'Technical Manual for Design and Construction of Road "
           "Tunnels' FHWA-NHI-09-010, 2009; Maidl et al. 'Hardrock Tunnel Boring "
           "Machines' 2008; USACE 'Tunnels and Shafts in Rock' EM 1110-2-2901, 1997; "
           "Kolymbas 'Tunnelling and Tunnel Mechanics' 2005; Singh & Goel 'Tunnelling "
           "in Weak Rocks' 1999).")
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["tunneling"] = _cfg(
    "tunneling", "The Tunneling Database",
    "Real, fact-checked tunneling engineering: from tunnel types, the ground as "
    "structure, and excavation methods through drill-and-blast design, RMR/Q-system/"
    "GSI classification, rock bolts, shotcrete, steel sets, NATM/SEM, TBM types and "
    "advance, mucking, support pressure, lining design, ventilation, dewatering, "
    "monitoring, safety and rescue, shaft sinking, compressed air, raise boring, "
    "cutter wear, immersed tunnels, refurbishment, squeezing ground, and economics - "
    "taught progressively along the ladder.",
    "tunneling record", "JAH-TUN-", "JAH Tunneling Archivist",
    "tunneling archivist - tunnel types, ground behaviour and stand-up time, "
    "excavation methods, portals, blast design, RMR/Q-system/GSI, rock bolts, "
    "shotcrete, steel sets, NATM/SEM, roadheaders, TBM types and advance rates, "
    "mucking and haulage, support pressure, lining design, ventilation, dewatering, "
    "monitoring, safety and rescue, shaft sinking, compressed-air working, raise "
    "boring, cutter wear, immersed tunnels, refurbishment, squeezing ground, "
    "economics; teaching progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, "
    "analogy, application, history, math, how-to - using only the system's own "
    "archive data",
    CIT_PUB, "public")
DBCFG["tunneling-signature"] = _cfg(
    "tunneling-signature", "The Tunneling Signature Database",
    "His original Signature interpretation of tunneling engineering: the full ladder "
    "from what tunneling is through ground classification, rock support, TBMs, "
    "ventilation, lining design, and economics, reframed as Signature science. "
    "Clearly labeled Signature-made, never presented as authentic public record.",
    "tunneling record", "JAH-TUS-", "JAH Tunneling Archivist (Signature)",
    "tunneling archivist - Signature editions: his original Signature "
    "interpretation of tunneling engineering, clearly labeled Signature-made and "
    "never presented as authentic public record; teaches progressively along the "
    "ladder from foundations through compounded to advanced; answers from many "
    "angles - definition, example, analogy, application, history, math, how-to - "
    "using only the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# tunneling computation for its record. All are machine-executed by main().

_PREAMBLE = (
"import math\n"
)

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_tu_what(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the first tunneling calculation: how much space, how much rock to move
    D, L = 10.0, 2000.0          # m: diameter, length
    swell = 1.4                 # blasted rock occupies ~40% more volume
    V = math.pi * (D / 2.0) ** 2 * L
    muck = V * swell
    print("tunnel: D = %.0f m, L = %.0f m" % (D, L))
    print("underground space created = %.0f m3" % V)
    print("rock to remove (swell %.1f) = %.0f m3" % (swell, muck))
    assert abs(V - 157079.6) < 1.0, V
    assert abs(muck - 219911.5) < 1.0, muck
    print("the void is the product; the muck is the price of the product")
    print("rule: compute the volume first - every later decision is per cubic metre")
    print("OK: %s measured the void" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_why(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # alignment economics: mountain road over vs tunnel through
    road_km, tun_km = 12.0, 6.0
    speed = 80.0                # km/h
    t_road = road_km / speed * 60.0
    t_tun = tun_km / speed * 60.0
    saved_per_trip = t_road - t_tun
    trips_per_day = 2000.0
    saved_per_day_h = saved_per_trip * trips_per_day / 60.0
    print("over the mountain: %.0f km -> %.1f min at %.0f km/h" % (road_km, t_road, speed))
    print("through the mountain: %.0f km -> %.1f min" % (tun_km, t_tun))
    print("saved per trip: %.1f min; per day (%d trips): %.0f hours" % (
        saved_per_trip, trips_per_day, saved_per_day_h))
    assert abs(t_road - 9.0) < 1e-9 and abs(t_tun - 4.5) < 1e-9
    assert abs(saved_per_day_h - 150.0) < 1e-9
    print("150 vehicle-hours saved every day for a century: that is what pays for the tunnel")
    print("rule: the tunnel must earn its per-metre cost in saved distance, land, or capacity")
    print("OK: %s priced the shortcut" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_types(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the cargo fixes the section: typical areas by tunnel type
    sections = [
        ("two-lane road tunnel", 90.0, "lanes + shoulders + ventilation + walkways"),
        ("single-track rail tunnel", 50.0, "loading gauge + aerodynamic clearance"),
        ("water tunnel D=4 m", math.pi * 2.0 ** 2, "hydraulics: area x velocity"),
        ("mine drift 5x4 m", 20.0, "largest truck + ducting + walkway"),
    ]
    for label, area, why in sections:
        print("%-26s %6.1f m2  <- %s" % (label, area, why))
    assert abs(sections[2][1] - 12.566) < 0.001
    # water tunnel flow check: 12.6 m2 at 2 m/s
    flow = sections[2][1] * 2.0
    print("water tunnel at 2 m/s carries %.1f m3/s" % flow)
    assert abs(flow - 25.13) < 0.01
    print("rule: size to the cargo, then let the cargo's rulebook govern the design")
    print("OK: %s sized the sections" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_ground(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # equivalent dimension De = span / ESR: the master sizing number
    cases = [
        ("major road tunnel", 10.0, 1.0),
        ("permanent mine opening", 10.0, 1.6),
        ("temporary mine opening", 10.0, 3.0),
        ("underground power station", 20.0, 1.0),
    ]
    for label, span, esr in cases:
        De = span / esr
        print("%-24s span %4.0f m / ESR %.1f -> De = %.2f" % (label, span, esr, De))
    assert abs(10.0 / 1.0 - 10.0) < 1e-9
    assert abs(10.0 / 1.6 - 6.25) < 1e-9
    # stand-up time shrinks with De and worsening ground (Bieniawski trend)
    print("same 10 m span, temporary use: De drops 10 -> 3.3, support need drops with it")
    print("rule: the ground is the structure - De tells the chart how big the job is")
    print("OK: %s dimensioned the opening" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_methods(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # method-selection scoring: 5 criteria, higher is better
    criteria = ["geology flexibility", "speed", "shape freedom", "low capital", "urban quiet"]
    methods = {
        "drill-and-blast": [5, 2, 5, 4, 1],
        "TBM":              [1, 5, 1, 1, 5],
        "roadheader":        [3, 3, 4, 3, 4],
        "cut-and-cover":     [2, 4, 3, 5, 1],
    }
    scenarios = {
        "variable geology cavern": {"geology flexibility": 3, "shape freedom": 3},
        "long uniform rail tunnel": {"speed": 3, "urban quiet": 2},
        "shallow urban metro": {"low capital": 2, "speed": 2},
    }
    for scen, weights in scenarios.items():
        best, bests = None, -1
        for m, scores in methods.items():
            s = sum(scores[criteria.index(c)] * w for c, w in weights.items())
            if s > bests:
                best, bests = m, s
        print("%-24s -> %s (score %d)" % (scen, best, bests))
    assert True
    print("no method wins everywhere: flexibility vs speed vs capital vs quiet")
    print("rule: let the geology and the constraints choose - never the brochure")
    print("OK: %s scored the methods" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_cutcover(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # open-cut geometry: depth and slopes multiply the excavation fast
    depth, base, slope = 12.0, 20.0, 1.5   # m, m, horizontal:vertical
    top = base + 2.0 * slope * depth
    area = (base + top) / 2.0 * depth
    vol_100m = area * 100.0
    print("depth %.0f m, base %.0f m, slopes 1:%.1f" % (depth, base, slope))
    print("top width = %.0f m; cross-section = %.0f m2" % (top, area))
    print("excavation per 100 m of tunnel = %.0f m3" % vol_100m)
    assert abs(top - 56.0) < 1e-9, top
    assert abs(area - 456.0) < 1e-9, area
    assert abs(vol_100m - 45600.0) < 1e-9
    # depth sensitivity: 6 m deep instead
    top2 = base + 2.0 * slope * 6.0
    area2 = (base + top2) / 2.0 * 6.0
    print("at 6 m deep the section would be only %.0f m2 - depth multiplies cost" % area2)
    assert abs(area2 - 174.0) < 1e-9
    print("rule: cut-and-cover is cheapest shallow; depth kills it faster than length")
    print("OK: %s dug the trench" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_portal(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # portal approach cut: the first excavation, in the worst ground
    depth, base, slope, length = 15.0, 12.0, 1.5, 60.0
    top = base + 2.0 * slope * depth
    area = (base + top) / 2.0 * depth
    vol = area * length
    print("approach cut: %.0f m deep, %.0f m long" % (depth, length))
    print("top width %.0f m, section %.1f m2, volume %.0f m3" % (top, area, vol))
    assert abs(top - 57.0) < 1e-9
    assert abs(area - 517.5) < 1e-9
    assert abs(vol - 31050.0) < 1e-9
    print("stabilize this before tunneling: bolts + shotcrete + drainage on the slopes")
    print("rule: design the portal first - it is built first, in the worst ground, under the most eyes")
    print("OK: %s opened the portal" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_dbcycle(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the drill-and-blast cycle summed to metres per day
    drill, charge, blast_vent, muck, support = 3.0, 1.5, 1.0, 2.0, 2.0
    cycle = drill + charge + blast_vent + muck + support
    rounds_per_day = 24.0 / cycle
    pull = 3.2
    advance = rounds_per_day * pull
    yearly = advance * 300.0
    print("cycle: drill %.1f + charge %.1f + blast/vent %.1f + muck %.1f + support %.1f = %.1f h" % (
        drill, charge, blast_vent, muck, support, cycle))
    print("rounds/day = %.2f; advance = %.2f m/day at %.1f m pull" % (rounds_per_day, advance, pull))
    print("one heading, 300 days: %.0f m/year" % yearly)
    assert abs(cycle - 9.5) < 1e-9
    assert abs(rounds_per_day - 2.5263) < 0.001
    assert abs(advance - 8.08) < 0.01
    assert abs(yearly - 2425.0) < 2.0
    print("two headings (both portals): ~4.8 km/year; four headings with an adit: ~9.7 km/year")
    print("rule: the cycle is the schedule - shorten any step and the metres follow")
    print("OK: %s timed the cycle" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_blastdesign(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # powder factor and pattern from face geometry
    face_area, pull = 20.0, 3.0       # m2, m
    powder_factor = 1.2               # kg/m3
    burden, spacing = 0.8, 0.9        # m
    vol = face_area * pull
    total_kg = vol * powder_factor
    holes = math.ceil(face_area / (burden * spacing))
    per_hole = total_kg / holes
    print("face %.0f m2 x pull %.0f m = %.0f m3/round" % (face_area, pull, vol))
    print("powder factor %.1f kg/m3 -> %.0f kg per round" % (powder_factor, total_kg))
    print("grid %.1f x %.1f m -> %d holes, %.2f kg/hole" % (burden, spacing, holes, per_hole))
    assert abs(vol - 60.0) < 1e-9
    assert abs(total_kg - 72.0) < 1e-9
    assert holes == 28, holes
    assert abs(per_hole - 2.5714) < 0.001
    print("cut holes heaviest, perimeter lightest (smooth blasting)")
    print("rule: exactly enough energy, placed exactly right - break what must go, protect what must stay")
    print("OK: %s designed the round" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_rmr(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Bieniawski RMR scored at the face
    ratings = [
        ("UCS 100 MPa", 7),
        ("RQD 80%", 13),
        ("joint spacing 0.5 m", 10),
        ("slightly rough joints", 20),
        ("damp groundwater", 7),
        ("fair orientation", -5),
    ]
    rmr = sum(r for _, r in ratings)
    for label, r in ratings:
        print("  %-22s %+3d" % (label, r))
    print("RMR = %d" % rmr)
    if rmr >= 81:
        cls = "I (very good)"
    elif rmr >= 61:
        cls = "II (good)"
    elif rmr >= 41:
        cls = "III (fair)"
    elif rmr >= 21:
        cls = "IV (poor)"
    else:
        cls = "V (very poor)"
    print("class %s -> systematic bolts + shotcrete, stand-up counted in days" % cls)
    assert rmr == 52, rmr
    assert cls.startswith("III"), cls
    print("rule: score it at the face in minutes - the number is only useful before stand-up time expires")
    print("OK: %s scored the rock mass" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_qsystem(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Barton Q = (RQD/Jn) x (Jr/Ja) x (Jw/SRF)
    RQD, Jn = 80.0, 9.0        # 80%, three joint sets
    Jr, Ja = 1.5, 1.0          # rough joints, unaltered walls
    Jw, SRF = 0.66, 2.5        # medium inflow, single weakness zone
    block = RQD / Jn
    shear = Jr / Ja
    stress = Jw / SRF
    Q = block * shear * stress
    print("block size  RQD/Jn   = %.2f" % block)
    print("shear       Jr/Ja    = %.2f" % shear)
    print("stress      Jw/SRF   = %.3f" % stress)
    print("Q = %.2f -> fair ground" % Q)
    assert abs(block - 8.8889) < 0.001
    assert abs(shear - 1.5) < 1e-9
    assert abs(stress - 0.264) < 0.001
    assert abs(Q - 3.52) < 0.01, Q
    # bolt length rule: L = 2 + 0.15*B/ESR
    B, ESR = 5.0, 1.6
    L = 2.0 + 0.15 * B / ESR
    print("bolt length L = 2 + 0.15*%.0f/%.1f = %.2f m -> use 2.5 m" % (B, ESR, L))
    assert abs(L - 2.4688) < 0.001
    print("rule: one bad term collapses the product - the weakest term governs, always")
    print("OK: %s computed Q" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_gsi(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # GSI -> Hoek-Brown parameters (2002 edition)
    GSI, mi = 55.0, 10.0
    mb = mi * math.exp((GSI - 100.0) / 28.0)
    s = math.exp((GSI - 100.0) / 9.0)
    a = 0.5 + (math.exp(-GSI / 15.0) - math.exp(-20.0 / 3.0)) / 6.0
    print("GSI = %.0f (blocky, fair surfaces), mi = %.0f" % (GSI, mi))
    print("mb = %.3f" % mb)
    print("s  = %.6f" % s)
    print("a  = %.4f" % a)
    assert abs(mb - 2.0046) < 0.002, mb
    assert abs(s - 0.006738) < 0.00001, s
    assert abs(a - 0.5041) < 0.001, a
    print("these three numbers let the numerical model compute yielding around the tunnel")
    print("rule: quote GSI as a range - false precision is the enemy of a visual index")
    print("OK: %s read the rock character" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_bolts(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # rock-bolt pattern from Q, capacity from bond
    B, ESR = 5.0, 1.6
    L = 2.0 + 0.15 * B / ESR
    spacing = 1.7                      # m, Q-chart for Q=3.5
    d, bond = 0.025, 1.0e6             # m bar diameter, Pa bond strength
    cap = math.pi * d * L * bond / 1000.0   # kN
    print("bolt length L = %.2f m -> install 2.5 m bars at %.1f m spacing" % (L, spacing))
    print("pull-out capacity = pi*%.3f*%.2f*1MPa = %.1f kN" % (d, L, cap))
    assert abs(L - 2.4688) < 0.001
    assert abs(cap - 193.8) < 1.0, cap
    assert cap > 150.0, "must exceed the 100-150 kN working range"
    print("a pattern of these clamps the jointed rock into a reinforced arch")
    print("rule: one bolt is a hope - a pattern is a structure")
    print("OK: %s stitched the ground" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_shotcrete(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # shotcrete quantity: thin shell, big volume
    thick, perim = 0.05, 16.0      # m, m of tunnel perimeter
    per_m = thick * perim
    length = 100.0
    placed = per_m * length
    rebound = 0.15
    order = placed * (1.0 + rebound)
    print("thickness %.0f mm over %.0f m perimeter = %.2f m3 per metre" % (
        thick * 1000, perim, per_m))
    print("100 m of tunnel: place %.0f m3, order %.0f m3 (rebound %.0f%%)" % (
        placed, order, rebound * 100))
    assert abs(per_m - 0.8) < 1e-9
    assert abs(placed - 80.0) < 1e-9
    assert abs(order - 92.0) < 1e-9
    print("no formwork, no gaps, structural in hours - the stand-up-time racer")
    print("rule: spray it minutes after exposure; test panels prove every shift")
    print("OK: %s sprayed the shell" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_steelsets(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Terzaghi rock load for steel-set design in poor ground
    B, Ht = 6.0, 6.0               # m: width, height
    gamma = 25.0                   # kN/m3
    Hp = 0.5 * (B + Ht)            # load height, poor ground
    p = gamma * Hp                 # kPa support pressure
    print("opening %.0f x %.0f m in poor ground" % (B, Ht))
    print("rock load height Hp = 0.5*(%.0f+%.0f) = %.0f m" % (B, Ht, Hp))
    print("support pressure p = %.0f kN/m3 * %.0f m = %.0f kPa" % (gamma, Hp, p))
    assert abs(Hp - 6.0) < 1e-9
    assert abs(p - 150.0) < 1e-9
    spacing = 1.0                  # m between sets
    load_per_set = p * spacing * B
    print("at %.1f m spacing each set carries %.0f kN across the %.0f m span" % (
        spacing, load_per_set, B))
    assert abs(load_per_set - 900.0) < 1e-9
    print("rule: when the ground cannot arch, lend it an arch of steel - blocked tight, encased in shotcrete")
    print("OK: %s set the steel" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_natm(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # convergence-confinement sanity check and alarm logic
    p0, a, G = 5.0e6, 5.0, 2000.0e6   # Pa in-situ stress, m radius, Pa shear modulus
    u_elastic = p0 * a / (2.0 * G)    # m
    u_plastic = 3.0 * u_elastic       # broken ground multiplies ~3x
    alarm = 0.005 * a * 1000.0        # mm: 0.5% of radius
    print("elastic convergence = %.1f mm" % (u_elastic * 1000.0))
    print("plastic estimate    = %.1f mm" % (u_plastic * 1000.0))
    print("alarm threshold     = %.0f mm (0.5%% of radius)" % alarm)
    assert abs(u_elastic * 1000.0 - 6.25) < 0.01
    assert abs(u_plastic * 1000.0 - 18.75) < 0.05
    assert abs(alarm - 25.0) < 1e-9
    # reading a convergence array: flattening = good
    readings = [0.0, 8.0, 14.0, 18.0, 21.0, 22.5, 23.0]   # mm over 6 days
    rates = [readings[i+1] - readings[i] for i in range(len(readings)-1)]
    print("daily rates: %s mm/day -> %s" % (
        ["%.1f" % r for r in rates],
        "FLATTENING: arch formed" if rates[-1] < rates[0] / 3 else "ACCELERATING: escalate"))
    assert rates[-1] < 1.0 and readings[-1] < alarm, "must be stable and under alarm"
    print("rule: allow a little deformation to mobilize the arch - never enough to loosen it")
    print("OK: %s read the convergence" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_roadheader(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # specific energy: the efficiency fingerprint of mechanical cutting
    power_kw, rate_m3h = 300.0, 80.0     # kW cutter head, m3/h in 40 MPa rock
    rate_m3s = rate_m3h / 3600.0
    SE = power_kw / rate_m3s              # kJ/m3
    print("cutter power %.0f kW at %.0f m3/h" % (power_kw, rate_m3h))
    print("specific energy = %.0f kJ/m3 = %.1f MJ/m3" % (SE, SE / 1000.0))
    assert abs(SE - 13500.0) < 1.0, SE
    # harder rock: rate halves, energy doubles
    SE_hard = power_kw / ((rate_m3h / 2.0) / 3600.0)
    print("rock twice as hard (half the rate): SE = %.1f MJ/m3 - energy climbs steeply" % (SE_hard / 1000.0))
    assert abs(SE_hard - 27000.0) < 1.0
    print("rule: sharp picks and right spacing beat raw power - inspect the teeth daily")
    print("OK: %s milled the face" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS_PART1 = {
    "what_is_tunneling": demo_tu_what, "why_tunnels": demo_tu_why,
    "tunnel_types": demo_tu_types, "ground_is_structure": demo_tu_ground,
    "excavation_methods_overview": demo_tu_methods, "cut_and_cover": demo_tu_cutcover,
    "portals": demo_tu_portal, "drill_blast_cycle": demo_tu_dbcycle,
    "blast_design": demo_tu_blastdesign, "rmr": demo_tu_rmr,
    "q_system": demo_tu_qsystem, "gsi": demo_tu_gsi,
    "rock_bolts": demo_tu_bolts, "shotcrete": demo_tu_shotcrete,
    "steel_sets": demo_tu_steelsets, "natm": demo_tu_natm,
    "roadheaders": demo_tu_roadheader,
}

def demo_tu_tbmtypes(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # TBM selection logic: geology answers, the machine follows
    def select(rock, water, strength_mpa):
        if strength_mpa >= 80 and not water and rock == "competent":
            return "open gripper TBM"
        if rock == "fractured" and not water:
            return "single/double shield TBM"
        if rock == "soft cohesive":
            return "EPB TBM"
        if rock == "granular" and water:
            return "slurry TBM"
        return "shielded TBM (default safe)"
    cases = [
        (("competent", False, 150.0), "open gripper TBM"),
        (("fractured", False, 90.0), "single/double shield TBM"),
        (("soft cohesive", True, 5.0), "EPB TBM"),
        (("granular", True, 0.0), "slurry TBM"),
    ]
    for (rock, water, s), expect in cases:
        got = select(rock, water, s)
        print("rock=%-14s water=%-5s UCS~%4.0f MPa -> %s" % (rock, water, s, got))
        assert got == expect, (got, expect)
    print("the geology bet is placed 1-2 years before the machine bores")
    print("rule: the right machine for the ground as it is - never the brochure's promise")
    print("OK: %s chose the machine" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_tbmadvan(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # daily advance = penetration rate x 24 h x utilization
    PR, util = 3.5, 0.35          # m/h, fraction
    daily = PR * 24.0 * util
    monthly = daily * 20.0        # 20 working days
    print("penetration %.1f m/h x 24 h x utilization %.0f%%" % (PR, util * 100))
    print("daily advance   = %.1f m/day" % daily)
    print("monthly advance = %.0f m (20 working days)" % monthly)
    assert abs(daily - 29.4) < 1e-9, daily
    assert abs(monthly - 588.0) < 1e-9
    # utilization is the lever: 0.35 -> 0.70 doubles everything
    print("at 70%% utilization the same machine does %.1f m/day - logistics beats thrust" % (PR * 24.0 * 0.70))
    assert abs(PR * 24.0 * 0.70 - 58.8) < 1e-9
    print("rule: every point of utilization is worth more than a point of penetration")
    print("OK: %s drove the advance" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_muck(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # muck haulage sizing: the circulatory system must keep up with the face
    D, adv = 8.0, 30.0            # m diameter, m/day
    swell, truck = 1.5, 15.0      # -, m3 per truck
    insitu = math.pi * (D / 2.0) ** 2 * adv
    loose = insitu * swell
    loads = math.ceil(loose / truck)
    interval_min = 24.0 * 60.0 / loads
    print("D=%.0f m at %.0f m/day -> %.0f m3 in situ" % (D, adv, insitu))
    print("swell %.1f -> %.0f m3 loose muck per day" % (swell, loose))
    print("at %.0f m3/truck: %d loads/day - one every %.1f min, around the clock" % (
        truck, loads, interval_min))
    assert abs(insitu - 1507.96) < 0.1, insitu
    assert abs(loose - 2261.95) < 0.2, loose
    assert loads == 151, loads
    assert abs(interval_min - 9.5) < 0.1
    print("rule: size the haulage like the excavation - when mucking stops, everything stops")
    print("OK: %s moved the mountain" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_suppress(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # support pressure two ways: Terzaghi (load height) vs Barton (Q correlation)
    # Terzaghi: poor ground, 6x6 m opening
    B, Ht, gamma = 6.0, 6.0, 25.0
    Hp = 0.5 * (B + Ht)
    p_terz = gamma * Hp                       # kPa
    # Barton crown correlation: p = (2/Jr) * Q^(-1/3), in MPa
    Jr, Q = 1.5, 3.52
    p_barton_MPa = (2.0 / Jr) * Q ** (-1.0 / 3.0)
    p_barton = p_barton_MPa * 1000.0           # kPa
    print("Terzaghi: Hp = %.0f m -> p = %.0f kPa" % (Hp, p_terz))
    print("Barton:   (2/%.1f)*%.2f^(-1/3) = %.3f MPa = %.0f kPa" % (Jr, Q, p_barton_MPa, p_barton))
    assert abs(p_terz - 150.0) < 1e-9
    assert abs(p_barton - 876.0) < 2.0, p_barton
    print("Barton is the conservative upper bound here; Terzaghi the working estimate")
    print("design to the envelope, and beat both by supporting early before loosening")
    print("rule: three generations of answers - trust the empirical numbers over the computer")
    print("OK: %s priced the ground load" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_lining(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # segmental ring: thickness rule and the characteristic thrust
    D = 6.0
    t = D / 20.0 / 1.0          # span/20 rule -> m
    p, R = 200.0, D / 2.0       # kPa ground pressure, m radius
    N = p * R                   # kN/m ring thrust
    print("D = %.0f m -> segment thickness ~ D/20 = %.2f m (use 300 mm)" % (D, t))
    print("ring thrust N = p x R = %.0f kPa x %.0f m = %.0f kN per metre" % (p, R, N))
    assert abs(t - 0.30) < 1e-9
    assert abs(N - 600.0) < 1e-9
    # capacity sanity: 300 mm of C40 concrete
    cap = 0.85 * 40.0e3 * t * 1.0   # kN/m (0.85*fck*b*d, d~t)
    print("concrete thrust capacity ~ %.0f kN/m >> %.0f kN/m demand" % (cap, N))
    assert cap > 5.0 * N
    print("joints and gaskets govern - the ring is only as permanent as its weakest seal")
    print("rule: design the ring joint by joint; backfill-grout it to the ground")
    print("OK: %s closed the ring" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_vent(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # construction ventilation sized to the diesel fleet
    diesel_kw = 500.0
    q_per_kw = 0.06              # m3/s per kW
    Q = diesel_kw * q_per_kw
    area = 50.0                  # m2 tunnel section
    v = Q / area
    print("diesel fleet %.0f kW x %.2f m3/s/kW = %.0f m3/s fresh air" % (diesel_kw, q_per_kw, Q))
    print("face velocity in %.0f m2 section = %.2f m/s (minimum 0.30)" % (area, v))
    assert abs(Q - 30.0) < 1e-9
    assert abs(v - 0.60) < 1e-9
    assert v > 0.30, "must exceed the minimum face velocity"
    # fire side: design fire sizes the operational system
    for vehicle, mw in (("car", 5.0), ("truck", 50.0)):
        print("design fire: %-6s ~%.0f MW - this sizes the jet fans and the critical velocity" % (vehicle, mw))
    print("rule: ventilation is life safety wearing an engineering disguise")
    print("OK: %s breathed for the tunnel" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_dewater(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Dupuit well formula: order-of-magnitude dewatering rate
    k = 1.0e-5                 # m/s permeability
    H, h = 20.0, 5.0           # m: natural head, drawn-down head
    R, r = 200.0, 3.0          # m: radius of influence, shaft radius
    Q = math.pi * k * (H ** 2 - h ** 2) / math.log(R / r)   # m3/s
    Q_h = Q * 3600.0
    pump = 15.0                # m3/h installed
    print("k=%.0e m/s, drawdown %.0f->%.0f m" % (k, H, h))
    print("inflow Q = %.4f m3/s = %.1f m3/h" % (Q, Q_h))
    print("installed pump %.0f m3/h -> margin %.1fx" % (pump, pump / Q_h))
    assert abs(Q_h - 10.1) < 0.2, Q_h
    assert pump / Q_h > 1.3, "pump margin required"
    print("but: drawing down settles the ground - in cities, cutoff walls beat pumping")
    print("rule: probe the permeability zone by zone - one open fracture outflows a kilometre of tight rock")
    print("OK: %s dried the heading" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_monitor(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # reading the monitoring: predict, measure, compare, act
    radius = 5.0
    attention, action = 0.005 * radius * 1000.0, 0.01 * radius * 1000.0
    print("radius %.0f m: attention at %.0f mm, action at %.0f mm" % (radius, attention, action))
    assert abs(attention - 25.0) < 1e-9 and abs(action - 50.0) < 1e-9
    conv = [0.0, 8.0, 14.0, 18.0, 21.0, 22.5, 23.0]   # mm
    rates = [round(conv[i+1] - conv[i], 2) for i in range(len(conv) - 1)]
    trend = "FLATTENING - arch formed" if rates[-1] < 1.0 else "ACCELERATING - escalate support"
    print("convergence: %s mm" % conv)
    print("daily rates: %s mm/day -> %s" % (rates, trend))
    assert conv[-1] < attention, "must stay under the attention threshold"
    assert rates[-1] < 1.0
    # extensometer: movement must stay shallow
    anchors = {"2 m": 12.0, "4 m": 6.0, "8 m": 1.5}   # mm at depth
    deep = anchors["8 m"] > 5.0
    print("extensometer: %s -> loosening is %s" % (
        anchors, "DEEPENING - escalate" if deep else "shallow - support working"))
    assert not deep
    print("rule: monitoring without named readers, deciders, and response times is decoration")
    print("OK: %s listened to the ground" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_safety(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # egress check: cross-passage spacing vs the 10-minute tenability criterion
    spacing = 500.0            # m between cross-passages
    walk_speed = 1.0           # m/s, panicked but realistic
    tenability = 10.0 * 60.0   # s
    max_walk = spacing / 2.0
    t_escape = max_walk / walk_speed
    print("cross-passages every %.0f m -> longest walk %.0f m" % (spacing, max_walk))
    print("escape time at %.0f m/s = %.0f s = %.1f min (limit %.0f min)" % (
        walk_speed, t_escape, t_escape / 60.0, tenability / 60.0))
    assert abs(t_escape - 250.0) < 1e-9
    assert t_escape < tenability, "must beat the tenability criterion"
    margin = tenability / t_escape
    print("margin: %.1fx - the design escapes with room to spare" % margin)
    assert abs(margin - 2.4) < 0.01
    print("construction side: self-rescuers give 30-60 min; rescue chambers stand by")
    print("rule: design for the worst day first, the ordinary century second")
    print("OK: %s walked the escape" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_shaft(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # shaft sinking schedule: the vertical tunnel before the horizontal one
    D, depth = 6.0, 300.0      # m
    rate = 1.5                 # m/day, good sinking
    V = math.pi * (D / 2.0) ** 2 * depth
    days = depth / rate
    print("shaft D=%.0f m, depth=%.0f m" % (D, depth))
    print("excavation = %.0f m3" % V)
    print("at %.1f m/day: %.0f days of sinking before lateral work starts" % (rate, days))
    assert abs(V - 8482.3) < 1.0, V
    assert abs(days - 200.0) < 1e-9
    lining = 0.40              # m concrete lining
    conc = math.pi * D * lining * depth
    print("lining %.0f mm: ~%.0f m3 of concrete" % (lining * 1000, conc))
    assert abs(conc - 2261.9) < 1.0, conc
    print("rule: probe the water, seal it or freeze it - never let the bottom outrun the support")
    print("OK: %s sank the shaft" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_air(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # compressed-air balance: hold the water head with air
    head = 30.0                # m of water above the invert
    p = 1000.0 * 9.81 * head / 1000.0   # kPa
    bar = p / 100.0
    print("water head %.0f m -> balance pressure %.0f kPa (~%.1f bar gauge)" % (head, p, bar))
    assert abs(p - 294.3) < 0.1, p
    assert abs(bar - 2.94) < 0.01
    # decompression cost: the human price of the bubble
    print("every entry pays in decompression time - bends injured the unprotected")
    print("modern answer: hyperbaric TBM interventions, or pressure without people")
    # EPB descendant check: same balance with muck pressure, nobody breathes it
    print("EPB holds the same %.0f kPa with conditioned muck - the descendant beats the ancestor" % p)
    print("rule: balance the water, or the water wins - and protect the people inside the bubble")
    print("OK: %s held the pressure" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_raise(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # raise-boring schedule: pilot up, ream down, gravity mucks free
    length = 100.0
    pilot_rate, ream_rate = 15.0, 4.0     # m/day
    t_pilot = length / pilot_rate
    t_ream = length / ream_rate
    total = t_pilot + t_ream
    print("raise length %.0f m" % length)
    print("pilot (%.0f m/day): %.1f days up" % (pilot_rate, t_pilot))
    print("ream  (%.0f m/day): %.1f days down" % (ream_rate, t_ream))
    print("total: %.1f days - a finished shaft nobody blasted under" % total)
    assert abs(t_pilot - 6.667) < 0.01
    assert abs(t_ream - 25.0) < 1e-9
    assert abs(total - 31.67) < 0.01
    print("cuttings fall by gravity to the lower level - the cheapest mucking there is")
    print("rule: a straight pilot makes a straight raise - directional control is the craft")
    print("OK: %s bored the raise" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_cutter(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # cutter-change planning: the wear budget of a hard-rock drive
    drive_m = 2000.0
    life_m = 150.0              # m per full cutter change (abrasive ground)
    changes = math.ceil(drive_m / life_m)
    days_lost = changes * 1.0   # ~1 day per intervention
    print("drive %.0f m, cutter life %.0f m/change" % (drive_m, life_m))
    print("interventions: %d (%.0f days of lost advance)" % (changes, days_lost))
    assert changes == 14, changes
    # soft ground contrast
    life_soft = 1500.0
    print("same drive in soft ground (%.0f m/change): %d interventions" % (
        life_soft, math.ceil(drive_m / life_soft)))
    assert math.ceil(drive_m / life_soft) == 2
    print("measure abrasivity (Cerchar), schedule the changes, never run a dead disc")
    print("rule: the cheapest cutter is the one replaced on time")
    print("OK: %s counted the teeth" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_immersed(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # immersed element: naval architecture of a sinking tunnel
    L, W, H = 150.0, 30.0, 8.0     # m
    disp = L * W * H               # m3 displaced
    buoyancy_t = disp * 1.0        # tonnes (seawater ~1.025, use 1.0)
    weight_t = 30000.0
    floats_by = buoyancy_t - weight_t
    ballast_t = 8000.0
    net = weight_t + ballast_t - buoyancy_t   # >0 means sinks
    print("element %.0fx%.0fx%.0f m displaces %.0f m3 -> %.0f t buoyancy" % (
        L, W, H, disp, buoyancy_t))
    print("weight %.0f t: floats by %.0f t" % (weight_t, floats_by))
    print("ballast %.0f t -> net %.0f t DOWN: a controlled, gentle sink" % (ballast_t, net))
    assert abs(disp - 36000.0) < 1e-9
    assert abs(floats_by - 6000.0) < 1e-9
    assert abs(net - 2000.0) < 1e-9
    assert net > 0 and net < 5000.0, "must sink gently, not plummet"
    print("Gina gasket + dewatered joint: water pressure locks the seal")
    print("rule: sink it like a ship - centimetres per minute, surveyed in 3D")
    print("OK: %s floated the tunnel" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_refurb(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # refurbishment triage: condition scoring per defect family
    defects = [
        ("water ingress at joints", 4),
        ("lining cracks >0.3 mm", 3),
        ("invert deterioration", 2),
        ("outdated fire detection", 4),
        ("spalling at crown", 2),
    ]
    weights = {"water ingress at joints": 3, "lining cracks >0.3 mm": 2,
               "invert deterioration": 2, "outdated fire detection": 3,
               "spalling at crown": 2}
    score = sum(s * weights[d] for d, s in defects)
    maxscore = sum(5 * weights[d] for d, _ in defects)
    index = 100.0 * (1.0 - score / maxscore)
    print("condition index = %.0f/100" % index)
    for d, s in defects:
        print("  %-26s severity %d/5" % (d, s))
    if index >= 80:
        plan = "routine maintenance"
    elif index >= 50:
        plan = "targeted refurbishment (grouting, crack injection, systems upgrade)"
    else:
        plan = "major renewal (relining, drainage rebuild)"
    print("plan: %s" % plan)
    assert abs(index - 36.67) < 0.1, index
    assert plan.startswith("major renewal"), plan
    print("staged in night possessions - the artery operates while it heals")
    print("rule: the alignment is forever; the lining is renewable")
    print("OK: %s surveyed the old bore" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_squeeze(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # squeezing ground collapses Q and inverts the support philosophy
    RQD, Jn, Jr, Ja, Jw = 80.0, 9.0, 1.5, 1.0, 0.66
    for label, SRF in (("normal", 2.5), ("heavy squeezing", 15.0)):
        Q = (RQD / Jn) * (Jr / Ja) * (Jw / SRF)
        p = (2.0 / Jr) * Q ** (-1.0 / 3.0) * 1000.0   # kPa, Barton crown
        print("SRF %4.1f (%-15s): Q = %5.2f -> crown pressure ~%.0f kPa" % (SRF, label, Q, p))
        if label == "normal":
            assert abs(Q - 3.52) < 0.01, Q
        else:
            assert abs(Q - 0.587) < 0.01, Q
            assert p > 1500.0, p
    print("same rock, squeezing stress: support pressure multiplies ~2x and persists for months")
    print("answer: YIELD - sliding steel sets, deformable shotcrete, over-excavation allowance")
    print("rule: never push harder against squeezing ground - yield wisely and let it move through its allowance")
    print("OK: %s faced the squeeze" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tu_econ(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # cost per metre: the unit that rules every tunneling conversation
    parts = [("excavation", 8000.0), ("initial support", 3000.0),
             ("final lining", 4000.0), ("services/logistics", 2000.0)]
    per_m = sum(c for _, c in parts)
    length = 5000.0
    total = per_m * length
    print("cost per metre:")
    for label, c in parts:
        print("  %-18s $%6.0f/m" % (label, c))
    print("  %-18s $%6.0f/m" % ("TOTAL", per_m))
    print("%.0f km x $%.0f/m = $%.0f million" % (length / 1000.0, per_m, total / 1e6))
    assert abs(per_m - 17000.0) < 1e-9
    assert abs(total - 85.0e6) < 1.0
    # learning curve: first km +20%
    first_km = per_m * 1.2 * 1000.0
    print("first kilometre (learning curve +20%%): $%.1fM vs steady $%.1fM" % (
        first_km / 1e6, per_m * 1000.0 / 1e6))
    assert abs(first_km - 20.4e6) < 1.0
    # stalled TBM burns standing cost
    print("a stalled TBM burns six figures a day - advance rate is a financial metric")
    print("rule: price the geology as it is, carry contingency without shame")
    print("OK: %s costed the tunnel" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = dict(DEMOS_PART1)
DEMOS.update({
    "tbm_types": demo_tu_tbmtypes, "tbm_advance": demo_tu_tbmadvan,
    "mucking": demo_tu_muck, "support_pressure": demo_tu_suppress,
    "lining_design": demo_tu_lining, "ventilation": demo_tu_vent,
    "dewatering": demo_tu_dewater, "monitoring": demo_tu_monitor,
    "safety_rescue": demo_tu_safety, "shaft_sinking": demo_tu_shaft,
    "compressed_air": demo_tu_air, "raise_boring": demo_tu_raise,
    "cutter_wear": demo_tu_cutter, "immersed_tunnels": demo_tu_immersed,
    "refurbishment": demo_tu_refurb, "fault_squeezing": demo_tu_squeeze,
    "economics": demo_tu_econ,
})
assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"


def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_tunneling.py).
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
    for slug in ("tunneling", "tunneling-signature"):
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
