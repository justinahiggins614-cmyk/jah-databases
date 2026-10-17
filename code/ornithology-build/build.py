"""Build the Ornithology field databases for JAH Databases (field #6, taxonomy order).

Verified 2026-10-17: the manifest holds 'public-birds' (60 species-catalog
records: identification, habitat, diet — no science) and 'signature-birds'
(30 original Signature bird concepts). Neither covers ornithology as a
science — no avian anatomy/physiology, flight mechanics, migration,
song/communication, breeding systems, foraging ecology, avian taxonomy,
conservation ornithology, or field methods. So this build creates two NEW
databases:

  ornithology              — The Ornithology Database (public-harvest: real,
                             fact-checked ornithology — avian anatomy and
                             physiology, feathers, flight mechanics,
                             migration and navigation, song and
                             communication, breeding systems, foraging
                             ecology, avian taxonomy, conservation
                             ornithology, field methods)
  ornithology-signature    — The Ornithology Signature Database (his original
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
from entries_ornithology import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals — his original Signature interpretation of ornithology: "
                "clearly labeled Signature-made, never presented as authentic public record.")
    pub_line = ("Public records — real, fact-checked ornithology: avian anatomy and "
                "physiology, feathers, flight mechanics, migration and navigation, "
                "song and communication, breeding systems, foraging ecology, avian "
                "taxonomy, conservation ornithology, and field methods, organized in "
                "the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what ornithology is, "
              "feathers, feather types, skeleton, beaks, feet and legs, respiration, "
              "senses, thermoregulation) -> Compounded (flight physics, wing shapes, "
              "flapping mechanics, soaring, migration I and II, syrinx, song learning, "
              "calls, breeding systems, nests, eggs and incubation, foraging ecology, "
              "taxonomy, molt) -> Advanced (flight energy, high-altitude physiology, "
              "magnetic compass, population ecology, conservation, climate change, "
              "field methods, bioacoustics, cognition, speciation, disease ecology, "
              "conservation genetics).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s — %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search feathers, flight, migration, song, nests, taxonomy, conservation...",
        "chat_ph": "Ask about ornithology...",
        "archive_blurb": ("Seeded %s ornithology records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations · Compounded · Advanced — each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled structural ornithology studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about ornithology — from what a feather is up to migration navigation and bird conservation." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "ornithology-study", "gen_demo_kind": "ornithology-demo",
        "source": source,
    }

CIT_PUB = "Ornithology (peer-reviewed literature and standard textbooks)."
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["ornithology"] = _cfg(
    "ornithology", "The Ornithology Database",
    "Real, fact-checked ornithology: avian anatomy and physiology, feathers, "
    "flight mechanics, migration and navigation, song and communication, "
    "breeding systems, foraging ecology, avian taxonomy, conservation "
    "ornithology, and field methods.",
    "ornithology record", "JAH-ORN-", "JAH Ornithology Archivist",
    "ornithology archivist — avian anatomy and physiology, feathers, flight "
    "mechanics, migration and navigation, song and communication, breeding "
    "systems, foraging ecology, avian taxonomy, conservation ornithology, "
    "field methods; teaching progressively along the ladder from foundations "
    "(what ornithology is, feathers, feather types, skeleton, beaks, feet "
    "and legs, respiration, senses, thermoregulation) through compounded "
    "(flight physics, wing shapes, flapping mechanics, soaring, migration I "
    "and II, syrinx, song learning, calls, breeding systems, nests, eggs "
    "and incubation, foraging ecology, taxonomy, molt) to advanced (flight "
    "energy, high-altitude physiology, magnetic compass, population ecology, "
    "conservation, climate change, field methods, bioacoustics, cognition, "
    "speciation, disease ecology, conservation genetics); answers from many "
    "angles — definition, example, analogy, application, history, math, "
    "how-to — using only the system's own archive data",
    CIT_PUB, "public")
DBCFG["ornithology-signature"] = _cfg(
    "ornithology-signature", "The Ornithology Signature Database",
    "His original Signature interpretation of ornithology: the full ladder from "
    "what a feather is to conservation genetics, reframed as Signature "
    "engineering. Clearly labeled Signature-made, never presented as authentic "
    "public record.",
    "ornithology record", "JAH-OSG-", "JAH Ornithology Archivist (Signature)",
    "ornithology archivist — Signature editions: his original Signature interpretation of "
    "ornithology, clearly labeled Signature-made and never presented as authentic public "
    "record; teaches progressively along the ladder from foundations through compounded "
    "to advanced; answers from many angles — definition, example, analogy, application, "
    "history, math, how-to — using only the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# ornithological calculation for its record. All are machine-executed by main().

_PREAMBLE = """import math
"""

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_bird_diversity(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    described_birds = 11000
    described_animals = 1300000
    share = described_birds / described_animals
    print("described birds %d of %d animals -> %.2f %%" % (
        described_birds, described_animals, 100 * share))
    assert abs(share - 0.0084615) < 0.0001
    estimate_low, estimate_high = 11000, 13000
    known = described_birds / estimate_high
    print("true total %d-%d -> we already know ~%.0f %%" % (
        estimate_low, estimate_high, 100 * known))
    assert abs(known - 0.846) < 0.01
    new_per_year = 4
    print("~%d new bird species described per year (vs ~thousands of new insects)" % new_per_year)
    assert new_per_year < 10
    print("OK: %s counted the birds" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_feather_structure(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    length_cm, barbs_per_cm = 25.0, 50.0
    per_side = length_cm * barbs_per_cm
    total_barbs = 2 * per_side
    print("flight feather %.0f cm x %.0f barbs/cm -> %.0f barbs per side" % (
        length_cm, barbs_per_cm, per_side))
    assert per_side == 1250.0 and total_barbs == 2500.0
    barbules_per_barb = 600.0
    interlocks = total_barbs * barbules_per_barb
    print("%.0f barbs x %.0f barbules -> %.0f interlocking parts per feather" % (
        total_barbs, barbules_per_barb, interlocks))
    assert interlocks == 1500000.0
    # preening re-zips a fraction of disturbed barbules
    disturbed, rezipped = 10000, 9850
    print("preening re-zips %d of %d disturbed barbules (%.1f %%)" % (
        disturbed, rezipped, 100 * rezipped / disturbed))
    assert rezipped / disturbed > 0.95
    print("OK: %s zipped the feather" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_feather_types(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
TYPES = {
    "flight (remiges/rectrices)": ("stiff asymmetric vane", "airfoil"),
    "contour": ("overlapping shingles", "streamlining + weatherproofing"),
    "down": ("loose unhooked barbs", "insulation"),
    "semiplume": ("loose vane, long rachis", "loft + shape"),
    "filoplume": ("hair-like, tufted tip", "feather-position sensor"),
    "bristle": ("stiff rachis, few barbs", "guard / insect net"),
}
def main():
    for ftype, (structure, job) in TYPES.items():
        print("  %-28s %-24s -> %s" % (ftype, structure, job))
    assert len(TYPES) == 6
    assert TYPES["down"][1] == "insulation"
    assert TYPES["filoplume"][1] == "feather-position sensor"
    # wing loading sanity: 100 g bird, 150 cm^2 wing area
    loading = 100.0 / 150.0
    print("wing loading %.2f g/cm^2 (light enough for agile flight)" % loading)
    assert abs(loading - 0.6667) < 0.01
    print("OK: %s sorted the feather wardrobe" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hollow_bone(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # solid rod radius 1 vs hollow tube outer 1.3, wall 0.15
    solid_area = math.pi * 1.0 ** 2
    hollow_area = math.pi * (1.3 ** 2 - 1.15 ** 2)
    ratio = hollow_area / solid_area
    print("hollow tube cross-section is %.1f %% of the solid rod" % (100 * ratio))
    assert abs(ratio - 0.3675) < 0.001
    print("mass saved: %.1f %%" % (100 * (1 - ratio)))
    assert (1 - ratio) > 0.60
    # bending stiffness scales ~ r^4: hollow tube is stiffer AND lighter
    solid_stiff = 1.0 ** 4
    hollow_stiff = 1.3 ** 4 - 1.15 ** 4
    print("bending stiffness: solid %.2f vs hollow %.2f -> hollow wins" % (
        solid_stiff, hollow_stiff))
    assert hollow_stiff > solid_stiff
    # skeleton mass fraction
    print("flying-bird skeleton ~5%% of body mass; flight muscles 15-25%%")
    print("OK: %s lightened the airframe" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_beak_tools(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
BEAKS = {
    "hummingbird": ("slender probe", "flower nectar"),
    "hawk": ("hooked tearer", "meat"),
    "duck": ("lamellate strainer", "seeds + invertebrates from water"),
    "finch": ("deep crusher", "hard seeds"),
    "woodpecker": ("chisel", "wood-boring insects"),
    "heron": ("spear", "fish"),
}
def diagnose(traits):
    hits = []
    for b, t in BEAKS.items():
        padded = " " + t[0].replace("-", " ") + " "
        if (" " + traits + " ") in padded:
            hits.append(b)
    return hits
def main():
    assert diagnose("probe") == ["hummingbird"]
    assert diagnose("crusher") == ["finch"]
    assert diagnose("strainer") == ["duck"]
    assert diagnose("spear") == ["heron"]
    print("keyed: probe->hummingbird, crusher->finch, strainer->duck, spear->heron")
    print("%d beak tools in the kit" % len(BEAKS))
    assert len(BEAKS) == 6
    # Darwin's finches: one ancestor -> many beaks
    print("Galapagos: one finch ancestor radiated into seed/insect/cactus/blood beaks")
    print("OK: %s read the tool heads" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_foot_types(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
FEET = {
    "anisodactyl": ("3 forward, 1 back", "perching songbirds"),
    "zygodactyl": ("2 forward, 2 back", "woodpeckers, parrots: climbing clamp"),
    "palmate": ("3 front toes webbed", "ducks, gulls: paddling"),
    "totipalmate": ("all 4 toes webbed", "pelicans, cormorants"),
    "raptorial": ("curved talons", "hawks, owls: killing grip"),
    "didactyl": ("2 toes", "ostrich: running"),
}
def tendon_lock(crouch_deg):
    # simplified: grip force rises with crouch angle (pulley effect)
    return crouch_deg * 2.5
def main():
    for arrangement, (config, lifestyle) in FEET.items():
        print("  %-12s %-22s %s" % (arrangement, config, lifestyle))
    assert len(FEET) == 6
    assert FEET["anisodactyl"][1].startswith("perching")
    g1, g2 = tendon_lock(10.0), tendon_lock(30.0)
    print("crouch 10 deg -> grip %.0f; crouch 30 deg -> grip %.0f (auto-lock)" % (g1, g2))
    assert g2 > g1 > 0
    print("sleeping percher cannot fall: relaxing tightens the lock")
    print("OK: %s locked the talons" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_air_sac_breathing(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    body_vol, sac_vol = 100.0, 18.0
    print("air sacs %.0f of %.0f body-volume units = %.0f %%" % (
        sac_vol, body_vol, 100 * sac_vol / body_vol))
    assert abs(sac_vol / body_vol - 0.18) < 1e-9
    # fresh-air fraction per breath: tidal vs dead space
    tidal, dead = 10.0, 2.0
    fresh = tidal / (tidal + dead)
    print("tidal %.0f, dead space %.0f -> fresh-air fraction %.1f %%" % (
        tidal, dead, 100 * fresh))
    assert abs(fresh - 0.8333) < 0.001
    # two-breath cycle: lung sees fresh air on BOTH inhale and exhale
    passes = 2
    print("%d-breath cycle: unidirectional flow -> lung always sees fresh air" % passes)
    assert passes == 2
    # cross-current keeps a diffusion gradient along the whole parabronchus
    print("cross-current exchange: blood meets progressively fresher air along the tube")
    print("OK: %s breathed like a bird" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_bird_vision(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    bird_cones, human_cones = 4, 3
    print("cones: bird %d (incl. UV) vs human %d" % (bird_cones, human_cones))
    assert bird_cones == human_cones + 1
    uv_low_nm, uv_high_nm = 300.0, 400.0
    print("UV channel: %.0f-%.0f nm (invisible to us, blazing to mates)" % (uv_low_nm, uv_high_nm))
    assert uv_low_nm < uv_high_nm <= 400.0
    # flicker fusion: finer slices of time
    bird_hz, human_hz = 100.0, 60.0
    print("flicker fusion: bird %.0f Hz vs human %.0f Hz -> %.2fx faster vision" % (
        bird_hz, human_hz, bird_hz / human_hz))
    assert abs(bird_hz / human_hz - 1.6667) < 0.01
    # kestrel sees vole urine in UV
    print("kestrel tracks vole urine trails glowing in UV")
    # two foveae per eye in many birds
    print("dual foveae: sharp forward + sharp lateral vision simultaneously")
    print("OK: %s saw ultraviolet" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_countercurrent(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def heat_recovery(t_arterial_in, t_venous_out, t_ambient):
    return (t_arterial_in - t_venous_out) / (t_arterial_in - t_ambient)
def main():
    rec = heat_recovery(41.0, 25.0, 5.0)
    print("arterial 41 C in, venous 25 C back, ambient 5 C")
    print("heat recovered: %.1f %%" % (100 * rec))
    assert abs(rec - 0.4444) < 0.001
    # foot stays just above freezing while core stays hot
    foot_c = 7.0
    print("foot at %.0f C, core at 41 C — the exchanger pays the difference" % foot_c)
    assert foot_c < 10.0
    # torpor: deliberate set-point drop
    day_temp, torpor_temp = 41.0, 18.0
    print("hummingbird torpor: %.0f C -> %.0f C overnight (%.0f deg drop)" % (
        day_temp, torpor_temp, day_temp - torpor_temp))
    assert day_temp - torpor_temp > 20.0
    print("OK: %s plumbed the heat exchanger" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_lift_eq(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def lift(rho, v, S, CL):
    return 0.5 * rho * v ** 2 * S * CL
def main():
    rho, v, S, CL = 1.225, 10.0, 0.012, 0.5
    L = lift(rho, v, S, CL)
    print("L = 0.5 x %.3f x %.0f^2 x %.3f x %.1f = %.4f N" % (rho, v, S, CL, L))
    assert abs(L - 0.3675) < 1e-9
    W = 0.030 * 9.81
    print("30 g sparrow weighs %.4f N -> lift/weight = %.2f (flies)" % (W, L / W))
    assert abs(W - 0.2943) < 0.001 and L / W > 1.2
    # speed is squared: double speed -> 4x lift
    print("double the speed -> %.1fx the lift (v^2 rules takeoff)" % (lift(rho, 20.0, S, CL) / L))
    assert abs(lift(rho, 20.0, S, CL) / L - 4.0) < 1e-9
    print("OK: %s balanced the four forces" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_wing_shape(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def aspect_ratio(span_m, area_m2):
    return span_m ** 2 / area_m2
def wing_loading(mass_kg, area_m2):
    return mass_kg / area_m2
def main():
    ar_alb = aspect_ratio(3.4, 0.62)
    ar_sparrow = aspect_ratio(0.21, 0.0088)
    print("aspect ratio: albatross %.1f (glider) vs sparrow %.1f (maneuverer)" % (ar_alb, ar_sparrow))
    assert abs(ar_alb - 18.6) < 0.1 and abs(ar_sparrow - 5.0) < 0.1
    wl_alb = wing_loading(9.0, 0.62)
    wl_sparrow = wing_loading(0.030, 0.0088)
    print("wing loading: albatross %.1f kg/m^2 (fast) vs sparrow %.1f kg/m^2 (slow, agile)" % (
        wl_alb, wl_sparrow))
    assert abs(wl_alb - 14.5) < 0.1 and abs(wl_sparrow - 3.4) < 0.1
    # slotted tips split the vortex like airliner winglets
    print("eagle slotted primaries: each finger carries its own small vortex")
    assert ar_alb > ar_sparrow and wl_alb > wl_sparrow
    print("OK: %s read the planforms" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_power_stroke(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def hover_induced_velocity(weight_N, disc_area_m2, rho=1.225):
    return math.sqrt(weight_N / (2 * rho * disc_area_m2))
def main():
    W = 0.004 * 9.81
    A = math.pi * 0.055 ** 2
    vi = hover_induced_velocity(W, A)
    print("hummingbird: weight %.4f N, disc area %.4f m^2" % (W, A))
    print("induced velocity %.3f m/s" % vi)
    assert abs(vi - 1.298) < 0.01
    P_ind = W * vi
    print("induced power = W x vi = %.4f W; with profile drag ~2x -> ~%.2f W" % (P_ind, 2 * P_ind))
    assert abs(P_ind - 0.0509) < 0.002
    # scaling: power ~ W^1.5 / sqrt(disc area) — hovering punishes size
    W2 = 10 * W
    print("10x heavier, same disc -> power %.1fx (W^1.5 scaling)" % ((W2 / W) ** 1.5))
    assert abs((W2 / W) ** 1.5 - 31.6) < 0.1
    print("OK: %s powered the hover" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_glide_polar(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def glide_range(altitude_m, glide_ratio):
    return altitude_m * glide_ratio
def main():
    ratio = 20.0   # albatross best glide
    rng = glide_range(1000.0, ratio)
    print("glide ratio %.0f:1, from 1000 m -> %.0f m of free travel" % (ratio, rng))
    assert rng == 20000.0
    speed = 15.0
    t_min = rng / speed / 60.0
    print("at %.0f m/s -> %.1f minutes aloft without a wingbeat" % (speed, t_min))
    assert abs(t_min - 22.2) < 0.1
    # sink rate at best glide
    sink = speed / ratio
    print("sink rate %.2f m/s — slower than walking down stairs" % sink)
    assert abs(sink - 0.75) < 0.01
    # frigatebird endurance
    print("frigatebirds ride thermals for weeks; juveniles stay aloft for months")
    print("OK: %s rode the free ride" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_migration_math(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def flight_hours(distance_km, speed_kmh):
    return distance_km / speed_kmh
def main():
    h = flight_hours(11000.0, 55.0)
    print("bar-tailed godwit: 11000 km at 55 km/h -> %.0f h = %.1f days nonstop" % (h, h / 24))
    assert abs(h - 200.0) < 1e-9 and abs(h / 24 - 8.33) < 0.01
    # fuel: fat packs ~37 kJ/g
    fat_g, kj_per_g = 160.0, 37.0
    energy = fat_g * kj_per_g
    print("%.0f g fat x %.0f kJ/g = %.0f kJ for the crossing" % (fat_g, kj_per_g, energy))
    assert energy == 5920.0
    per_hour = energy / h
    print("burn rate %.1f kJ/h over %.0f h" % (per_hour, h))
    assert abs(per_hour - 29.6) < 0.1
    # arctic tern annual total
    print("arctic tern: ~70000 km/year pole to pole — the longest migration")
    print("OK: %s fueled the crossing" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_navigation_cues(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
CUES = {
    "sun compass": ("sun azimuth + circadian clock correction", "day migrants"),
    "star compass": ("center of celestial rotation = north", "night migrants"),
    "magnetic compass": ("field inclination angle", "cloudy nights"),
    "landmarks": ("coastlines, rivers, mountains", "experienced adults"),
    "olfaction": ("odor gradients", "tubenoses, homing pigeons"),
}
def main():
    for cue, (mechanism, users) in CUES.items():
        print("  %-16s %-42s %s" % (cue, mechanism, users))
    assert len(CUES) == 5
    # clock-shift proof: 6 h shift -> 90 deg heading error
    shift_h = 6.0
    error_deg = shift_h / 24.0 * 360.0
    print("clock-shift %d h -> heading error %.0f deg (sun compass proven)" % (shift_h, error_deg))
    assert error_deg == 90.0
    # juveniles: clock-and-compass; adults: true navigation
    print("juvenile: fly heading X for Y days; adult: true map-based navigation")
    print("OK: %s fused the compasses" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_syrinx_voices(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    f_left, f_right = 2000.0, 3000.0
    print("syrinx: left bronchus %.0f Hz + right bronchus %.0f Hz simultaneously" % (
        f_left, f_right))
    beat = abs(f_right - f_left)
    print("two-voice beat frequency: %.0f Hz" % beat)
    assert beat == 1000.0
    # mammals: one larynx, one source
    print("mammal larynx: 1 source; bird syrinx: 2 independent sources")
    # rapid side-switching builds syllables no single source could
    switch_ms = 10.0
    print("side-switching every %.0f ms weaves the two voices into one song" % switch_ms)
    assert switch_ms < 50.0
    # brown thrasher repertoire
    print("brown thrasher: 1000+ song types from the double instrument")
    print("OK: %s played both reeds" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_song_learning(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def jaccard(a, b):
    sa, sb = set(a), set(b)
    return len(sa & sb) / len(sa | sb)
def main():
    tutor = ["a", "b", "c", "d"]
    pupil = ["a", "b", "c", "e"]
    j = jaccard(tutor, pupil)
    print("tutor %s vs pupil %s -> syllable similarity %.2f" % (tutor, pupil, j))
    assert abs(j - 0.60) < 1e-9
    # dialect drift: small copying errors accumulate per generation
    err, gens = 0.05, 10
    drift = 1 - (1 - err) ** gens
    print("%.0f %% copying error x %d generations -> %.0f %% dialect drift" % (
        100 * err, gens, 100 * drift))
    assert abs(drift - 0.401) < 0.01
    # repertoires
    print("repertoires: thrasher 1000+, marsh wren 100+, chiffchaff 1")
    # honest signaling: dawn chorus costs energy
    print("dawn chorus: only a male in top condition can afford hours of song")
    print("OK: %s tutored the pupil" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_call_functions(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
CALLS = {
    "seet alarm": ("high, thin, hard to locate", "hawk overhead — freeze"),
    "mobbing call": ("broadband, locatable", "perched owl — come harass"),
    "chick-a-dee": ("graded dee notes", "predator danger dial"),
    "flight call": ("short nocturnal chip", "flock cohesion in the dark"),
    "begging call": ("loud, repetitive", "feed me — honest hunger signal"),
    "contact call": ("individual voice", "mate/flock recognition"),
}
def diagnose(traits):
    hits = []
    for c, t in CALLS.items():
        padded = " " + t[0].replace(",", " ") + " "
        if (" " + traits + " ") in padded:
            hits.append(c)
    return hits
def main():
    assert diagnose("locatable") == ["mobbing call"]
    assert diagnose("graded") == ["chick-a-dee"]
    assert diagnose("nocturnal") == ["flight call"]
    print("keyed: locatable->mobbing, graded->chick-a-dee, nocturnal->flight call")
    print("%d calls in the codebook" % len(CALLS))
    assert len(CALLS) == 6
    # mixed-species eavesdropping
    print("nuthatches eavesdrop on chickadee dees — a shared alarm network")
    print("OK: %s decoded the codebook" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_breeding_payoffs(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # social monogamy share among birds
    mono = 0.90
    print("socially monogamous species: %.0f %% (unmatched in vertebrates)" % (100 * mono))
    assert mono > 0.85
    # the economics: two parents fledge more
    two_parent, one_parent = 4.0, 2.0
    print("chicks fledged: two parents %.0f vs one parent %.0f" % (two_parent, one_parent))
    assert two_parent == 2 * one_parent
    # lek skew: top 10% of males win 80% of matings
    top_frac, win_frac = 0.10, 0.80
    skew = (win_frac / top_frac) / ((1 - win_frac) / (1 - top_frac))
    print("lek skew: top %.0f %% males get %.0f %% matings -> %.0fx the average male" % (
        100 * top_frac, 100 * win_frac, win_frac / top_frac))
    assert abs(win_frac / top_frac - 8.0) < 1e-9
    assert skew > 30.0
    # extra-pair: the social contract vs the genetic ledger
    print("DNA: many 'faithful' nests hold chicks of >1 father (extra-pair mating)")
    print("OK: %s balanced the mating market" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nest_insulation(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def cool_time_min(T0, Ta, T_target, k):
    return math.log((T0 - Ta) / (T_target - Ta)) / k
def main():
    T0, Ta, Tt = 38.0, 10.0, 33.0
    t_open = cool_time_min(T0, Ta, Tt, 0.20)
    t_nest = cool_time_min(T0, Ta, Tt, 0.10)
    print("egg 38 C -> 33 C at 10 C ambient: open %.2f min vs insulated nest %.2f min" % (
        t_open, t_nest))
    assert abs(t_open - 0.98) < 0.02 and abs(t_nest - 1.97) < 0.02
    print("insulation buys %.1fx more foraging time per trip" % (t_nest / t_open))
    assert abs(t_nest / t_open - 2.0) < 0.05
    # megapode mound: microbial heat holds ~34 C
    print("megapode mound: compost heat holds the chamber ~33-35 C; male regulates by beak-thermometer")
    mound, target = 34.0, 34.0
    assert abs(mound - target) < 1.0
    print("OK: %s insulated the nursery" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_egg_math(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def egg_volume_cm3(length_cm, breadth_cm):
    return 0.51 * length_cm * breadth_cm ** 2   # Hoyt's formula
def main():
    v_chicken = egg_volume_cm3(5.8, 4.4)
    print("chicken egg 5.8 x 4.4 cm -> %.1f cm^3 (Hoyt's formula)" % v_chicken)
    assert abs(v_chicken - 57.27) < 0.05
    v_ostrich = egg_volume_cm3(15.0, 13.0)
    print("ostrich egg 15 x 13 cm -> %.0f cm^3 — the largest single cell in nature" % v_ostrich)
    assert abs(v_ostrich - 1292.85) < 0.1
    ratio = v_ostrich / v_chicken
    print("ostrich / chicken volume ratio: %.1fx" % ratio)
    assert abs(ratio - 22.57) < 0.05
    # incubation temperature band
    print("incubation: 36-38 C + regular turning or the embryo sticks")
    print("OK: %s measured the capsule" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_foraging_profit(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def profitability(energy_J, handling_s):
    return energy_J / handling_s
def main():
    prey = {"mussel A": (100.0, 10.0), "mussel B": (250.0, 40.0), "mussel C": (50.0, 2.0)}
    ranked = sorted(prey, key=lambda p: profitability(*prey[p]), reverse=True)
    for p in ranked:
        e, h = prey[p]
        print("  %-9s %.0f J / %.0f s = %.2f J/s" % (p, e, h, profitability(e, h)))
    assert ranked == ["mussel C", "mussel A", "mussel B"]
    assert abs(profitability(50.0, 2.0) - 25.0) < 1e-9
    # marginal value theorem: leave the patch when return drops to habitat average
    habitat_avg = 8.0
    patch_now = 6.5
    print("patch returns %.1f J/s vs habitat %.1f -> %s" % (
        patch_now, habitat_avg, "LEAVE" if patch_now < habitat_avg else "STAY"))
    assert patch_now < habitat_avg
    print("OK: %s optimized the forager" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_bird_orders(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
TREE = {"Palaeognathae": ["Struthioniformes (ostriches)", "Tinamiformes (tinamous)"],
        "Neognathae": {
            "Galloanserae": ["Anseriformes (waterfowl)", "Galliformes (gamebirds)"],
            "Neoaves": {
                "waterbirds": ["Charadriiformes (shorebirds)", "Pelecaniformes (herons, pelicans)"],
                "landbirds": ["Accipitriformes (hawks/eagles)", "Strigiformes (owls)",
                              "Piciformes (woodpeckers)", "Psittaciformes (parrots)",
                              "Apodiformes (swifts/hummingbirds)",
                              "Passeriformes (songbirds, 6000+ species)"],
                "doves": ["Columbiformes (pigeons/doves)"]}}}
def find(order, node=TREE, path=()):
    for k, v in node.items():
        if isinstance(v, list):
            for entry in v:
                if entry.startswith(order):
                    return path + (k,)
        elif isinstance(v, dict):
            hit = find(order, v, path + (k,))
            if hit:
                return hit
    return None
def main():
    p = find("Passeriformes")
    print("Passeriformes: %s" % " -> ".join(p))
    assert p[-1] == "landbirds"
    assert find("Struthioniformes")[0] == "Palaeognathae"
    assert find("Apodiformes")[-1] == "landbirds"
    assert find("Not an order") is None
    # DNA surprise: falcons ally with parrots/songbirds, not hawks
    print("DNA surprise: falcons group with parrots + songbirds, far from hawks")
    print("OK: %s climbed the bird tree" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_molt_score(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def molt_score(primaries):
    # each primary 0 (old) .. 5 (fully grown); 10 primaries -> /50
    assert len(primaries) == 10 and all(0 <= s <= 5 for s in primaries)
    return sum(primaries)
def main():
    left = [5, 5, 5, 4, 3, 2, 1, 0, 0, 0]
    right = [5, 5, 5, 4, 3, 2, 1, 0, 0, 0]
    s = molt_score(left)
    print("primaries %s -> molt score %d/50 (%.0f %%)" % (left, s, 100 * s / 50))
    assert s == 25
    # symmetry: both wings must match or flight unbalances
    assert left == right, "asymmetric molt!"
    print("symmetric: left == right — balanced flight preserved")
    # descendant sequence: inner primaries (P1) molt before outer (P10)
    assert left[0] >= left[-1], "sequence violated"
    print("sequence: inner primaries replaced before outer — descendant order holds")
    print("OK: %s scored the molt" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_flight_cost(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    bmr_multiple = 10.0
    print("flapping flight burns ~%.0fx basal metabolic rate" % bmr_multiple)
    assert 8.0 <= bmr_multiple <= 12.0
    # warbler fuel budget: 3 g fat at 37 kJ/g, burning 30 kJ/h
    fat_g, kj_per_g, burn_kjh = 3.0, 37.0, 30.0
    energy = fat_g * kj_per_g
    hours = energy / burn_kjh
    print("%.0f g fat x %.0f kJ/g = %.0f kJ -> %.1f h of flight" % (fat_g, kj_per_g, energy, hours))
    assert energy == 111.0 and abs(hours - 3.7) < 0.05
    # soaring cheat: gliding ~1.5x BMR
    print("soaring vulture glides at ~1.5x BMR — the free ride")
    # when fat runs out, muscle burns
    print("fat exhausted -> flight muscle itself burns: arrivals are lighter in engine, not just fuel")
    print("OK: %s priced the power curve" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_altitude_oxygen(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def pressure_kpa(alt_m):
    return 101.3 * math.exp(-alt_m / 8400.0)   # barometric formula
def o2_kpa(alt_m):
    return 0.2095 * pressure_kpa(alt_m)
def main():
    p0, p6 = o2_kpa(0.0), o2_kpa(6000.0)
    print("O2 partial pressure: sea level %.1f kPa -> 6000 m %.1f kPa" % (p0, p6))
    assert abs(p0 - 21.2) < 0.1 and abs(p6 - 10.4) < 0.2
    print("ratio: %.3f — every breath carries half the oxygen" % (p6 / p0))
    assert abs(p6 / p0 - 0.4895) < 0.005
    # the goose's upgrades roughly double extraction efficiency
    extraction_mammal, extraction_goose = 0.25, 0.50
    delivered_mammal = p6 * extraction_mammal
    delivered_goose = p6 * extraction_goose
    print("delivered O2: mammal lung %.1f vs goose lung %.1f kPa-equivalent" % (
        delivered_mammal, delivered_goose))
    assert delivered_goose == 2 * delivered_mammal
    print("bar-headed geese cross the Himalayas above 7000 m on this machinery")
    print("OK: %s breathed thin air" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_magnetic_compass(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def dip_angle_deg(mag_lat_deg):
    return math.degrees(math.atan(2 * math.tan(math.radians(mag_lat_deg))))
def main():
    for lat in (0.0, 30.0, 45.0, 60.0):
        print("  magnetic latitude %4.0f deg -> dip angle %5.1f deg" % (lat, dip_angle_deg(lat)))
    assert abs(dip_angle_deg(0.0) - 0.0) < 1e-9
    assert abs(dip_angle_deg(45.0) - 63.43) < 0.01
    assert abs(dip_angle_deg(60.0) - 73.90) < 0.01
    # steep dip = poleward, flat = equatorward: the inclination compass
    print("steep dip -> poleward; flat field -> equatorward (no polarity needed)")
    # light-dependence: the quantum signature
    print("wrong light wavelengths disorient migrants — the radical-pair signature")
    print("OK: %s read the quantum compass" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_banding_stats(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def lincoln_petersen(M, C, R):
    return M * C / R
def main():
    N = lincoln_petersen(200, 150, 30)
    print("banded 200, recatch 150 with 30 banded -> N = 200x150/30 = %.0f" % N)
    assert N == 1000.0
    # assumptions that bias the answer if violated
    print("assumes: closed population, no band loss, equal catchability")
    # encounter history: seen y1, missed y2, seen y3 -> alive in y2 (missed, not dead)
    history = [1, 0, 1, 1]
    alive_y2 = history[0] == 1 and history[2] == 1
    print("history %s -> alive but missed in year 2: %s" % (history, alive_y2))
    assert alive_y2 is True
    # Manx shearwater longevity record
    print("Manx shearwater: banded adult still breeding 50+ years later")
    print("OK: %s estimated the population" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_decline_stats(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def annual_rate(start, end, years):
    return (end / start) ** (1.0 / years) - 1.0
def main():
    then, now = 10.0e9, 7.0e9
    lost = then - now
    print("North America: %.0fB -> %.0fB breeding birds since 1970 (lost %.0fB = %.0f %%)" % (
        then / 1e9, now / 1e9, lost / 1e9, 100 * lost / then))
    assert abs(lost - 3.0e9) < 1e7
    r = annual_rate(then, now, 50)
    print("compounded annual decline: %.2f %%/year" % (100 * -r))
    assert abs(-r - 0.00711) < 0.0005
    # drivers
    print("drivers: habitat loss, pesticides, cats, windows, climate")
    # recoveries prove reversibility
    print("condors: 27 individuals -> 500+; eagles and peregrines rebuilt the same way")
    assert now < then
    print("OK: %s graphed the barometer" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_range_shift(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rate_km_yr, years = 1.5, 30
    shift = rate_km_yr * years
    print("poleward shift %.1f km/yr x %d yr = %.0f km" % (rate_km_yr, years, shift))
    assert shift == 45.0
    # phenology: egg-laying advances ~2 days per decade
    days_per_decade, decades = 2.0, 5
    advance = days_per_decade * decades
    print("laying advances %.0f days/decade x %d decades = %.0f days earlier" % (
        days_per_decade, decades, advance))
    assert advance == 10.0
    # mismatch: caterpillars track temperature, migrants track day length
    print("mismatch: caterpillar peak sprints ahead; day-length-cued migrants arrive late")
    # montane squeeze: habitat area shrinks toward the summit
    print("montane squeeze: each meter uphill loses habitat area — summits are dead ends")
    print("OK: %s tracked the shifting birds" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_point_count(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def density_per_km2(n, radius_m, detection_p):
    per_m2 = n / (math.pi * radius_m ** 2 * detection_p)
    return per_m2 * 1e6
def main():
    d = density_per_km2(8, 100.0, 0.6)
    print("8 birds, 100 m radius, detection p=0.6 -> %.1f birds/km^2" % d)
    assert abs(d - 424.4) < 1.0
    # ignoring detection probability undercounts shy species
    d_naive = density_per_km2(8, 100.0, 1.0)
    print("naive (p=1.0): %.1f — ignoring p undercounts by %.0f %%" % (d_naive, 100 * (1 - d_naive / d)))
    assert d_naive < d
    # mist-net effort standardization
    captures, net_hours = 24, 60.0
    print("mist nets: %d captures / %.0f net-hours = %.2f per net-hour" % (
        captures, net_hours, captures / net_hours))
    assert abs(captures / net_hours - 0.40) < 1e-9
    print("golden rule: record effort (minutes, net-hours, km) or the numbers mean nothing")
    print("OK: %s standardized the count" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_spectrogram_dft(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def dft_magnitudes(x):
    N = len(x)
    mags = []
    for k in range(N):
        re = sum(x[n] * math.cos(2 * math.pi * k * n / N) for n in range(N))
        im = -sum(x[n] * math.sin(2 * math.pi * k * n / N) for n in range(N))
        mags.append(math.hypot(re, im))
    return mags
def main():
    fs, N = 8000.0, 64
    # synthetic two-tone warbler syllable: 2000 Hz + 3000 Hz
    x = [math.sin(2 * math.pi * 2000 * n / fs) + 0.5 * math.sin(2 * math.pi * 3000 * n / fs)
         for n in range(N)]
    mags = dft_magnitudes(x)
    half = mags[1:32]
    top2 = sorted(range(1, 32), key=lambda k: half[k - 1], reverse=True)[:2]
    print("strongest bins: %s -> %.0f Hz and %.0f Hz" % (
        sorted(top2), sorted(top2)[0] * fs / N, sorted(top2)[1] * fs / N))
    assert sorted(top2) == [16, 24]
    assert abs(16 * fs / N - 2000.0) < 1e-9 and abs(24 * fs / N - 3000.0) < 1e-9
    # spectrogram = this DFT, window after window, stacked over time
    print("a spectrogram is this transform repeated every few milliseconds")
    print("OK: %s pictured the song" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nutcracker_memory(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    cached = 30000
    recovered = cached * 2 // 3
    print("Clark's nutcracker caches %d seeds; recovers ~2/3 = %d months later under snow" % (
        cached, recovered))
    assert recovered == 20000
    # landmark-shift experiment proves true spatial maps (not smell)
    normal_recall, shifted_recall = 0.67, 0.25
    print("recall with landmarks intact: %.0f %%; landmarks shifted: %.0f %% -> spatial map proven" % (
        100 * normal_recall, 100 * shifted_recall))
    assert normal_recall > 2 * shifted_recall
    # scrub-jay episodic-like memory: what + where + when
    print("scrub-jays remember what they cached, where, AND when (perishable worms vs nuts)")
    # perspective-taking: re-cache when watched by a thief
    print("watched jays re-cache — they model what the watcher knows")
    print("OK: %s mapped the mind" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_speciation_index(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def ri(hybrid_fitness, parental_fitness):
    return 1.0 - hybrid_fitness / parental_fitness
def main():
    r = ri(0.2, 1.0)
    print("hybrid fitness 0.2 vs parental 1.0 -> RI = %.1f (strong isolation)" % r)
    assert abs(r - 0.8) < 1e-9
    assert abs(ri(1.0, 1.0) - 0.0) < 1e-9, "free interbreeding -> RI 0"
    # ring species: divergence accumulates around the ring
    steps, per_step = 5, 0.15
    accumulated = steps * per_step
    print("greenish warblers: %d steps x %.2f divergence = %.2f accumulated" % (
        steps, per_step, accumulated))
    assert abs(accumulated - 0.75) < 1e-9
    print("ends meet in Siberia as separate species — speciation caught mid-act")
    # song drifts fastest (learned), genes slowest
    print("song diverges first (learned), plumage next, genes last")
    print("OK: %s forked the lineage" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_avian_flu_r0(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def r0(beta, susceptibles, gamma):
    return beta * susceptibles / gamma
def main():
    r = r0(0.0004, 1000.0, 0.2)
    print("duck flock: beta=0.0004, S=1000, gamma=0.2 -> R0 = %.1f (spreads)" % r)
    assert abs(r - 2.0) < 1e-9 and r > 1.0
    # biosecurity cuts transmission by three quarters -> below threshold
    r2 = r0(0.0001, 1000.0, 0.2)
    print("biosecurity cuts transmission 75%% -> R0 = %.1f (%s)" % (
        r2, "dies out" if r2 < 1.0 else "spreads"))
    assert abs(r2 - 0.5) < 1e-9 and r2 < 1.0
    # stopover wetlands mix flyways like airports mix travelers
    print("stopover wetland = international airport during flu season")
    # H5N1 panzootic scale
    print("H5N1 2.3.4.4b: millions of wild birds dead on every continent — incl. Antarctica")
    print("OK: %s modeled the panzootic" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_bottleneck_heterozygosity(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def heterozygosity(h0, ne, generations):
    return h0 * (1 - 1.0 / (2 * ne)) ** generations
def main():
    h = heterozygosity(1.0, 10, 10)
    print("Ne=10, 10 generations: H = %.4f -> %.1f %% of diversity lost" % (h, 100 * (1 - h)))
    assert abs(h - 0.5987) < 0.005
    assert abs((1 - h) - 0.4013) < 0.005
    # per-generation drain
    drain = 1.0 / (2 * 10)
    print("drain per generation: 1/(2x10) = %.1f %%" % (100 * drain))
    assert abs(drain - 0.05) < 1e-9
    # larger Ne bleeds slower
    h_big = heterozygosity(1.0, 100, 10)
    print("Ne=100 keeps %.1f %% vs Ne=10 keeps %.1f %%" % (100 * h_big, 100 * h))
    assert h_big > h
    # condor studbook: minimum-kinship mating from 27 founders
    print("California condor: studbook-managed from 27 founders, 500+ birds today")
    print("OK: %s audited the gene pool" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "bird_diversity": demo_bird_diversity, "feather_structure": demo_feather_structure,
    "feather_types": demo_feather_types, "hollow_bone": demo_hollow_bone,
    "beak_tools": demo_beak_tools, "foot_types": demo_foot_types,
    "air_sac_breathing": demo_air_sac_breathing, "bird_vision": demo_bird_vision,
    "countercurrent": demo_countercurrent, "lift_eq": demo_lift_eq,
    "wing_shape": demo_wing_shape, "power_stroke": demo_power_stroke,
    "glide_polar": demo_glide_polar, "migration_math": demo_migration_math,
    "navigation_cues": demo_navigation_cues, "syrinx_voices": demo_syrinx_voices,
    "song_learning": demo_song_learning, "call_functions": demo_call_functions,
    "breeding_payoffs": demo_breeding_payoffs, "nest_insulation": demo_nest_insulation,
    "egg_math": demo_egg_math, "foraging_profit": demo_foraging_profit,
    "bird_orders": demo_bird_orders, "molt_score": demo_molt_score,
    "flight_cost": demo_flight_cost, "altitude_oxygen": demo_altitude_oxygen,
    "magnetic_compass": demo_magnetic_compass, "banding_stats": demo_banding_stats,
    "decline_stats": demo_decline_stats, "range_shift": demo_range_shift,
    "point_count": demo_point_count, "spectrogram_dft": demo_spectrogram_dft,
    "nutcracker_memory": demo_nutcracker_memory, "speciation_index": demo_speciation_index,
    "avian_flu_r0": demo_avian_flu_r0,
    "bottleneck_heterozygosity": demo_bottleneck_heterozygosity,
}

# ---------------------------------------------------------------- records

def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_ornithology.py).
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
    for slug in ("ornithology", "ornithology-signature"):
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
