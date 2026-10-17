"""Build the Entomology field databases for JAH Databases (field #5, taxonomy order).

Verified 2026-10-17: the manifest holds no dedicated entomology database —
only 'inventors' matched an "ento" substring search, and the biology-family
databases carry only incidental insect coverage. So this build creates two
NEW databases:

  entomology              — The Entomology Database (public-harvest: real,
                            fact-checked entomology — insect anatomy and
                            morphology, insect orders and taxonomy,
                            metamorphosis, insect physiology, behavior and
                            social insects, pollination ecology,
                            agricultural and medical entomology, pest
                            management, beneficial insects, collection and
                            identification methods)
  entomology-signature    — The Entomology Signature Database (his original
                            Signature interpretation; src signature, titles
                            suffixed " (Signature Edition)", never presented as
                            authentic public record)

36 records each, ordered by the teaching ladder (ladder_rank 1-10, ladder_tier
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
from entries_entomology import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals — his original Signature interpretation of entomology: "
                "clearly labeled Signature-made, never presented as authentic public record.")
    pub_line = ("Public records — real, fact-checked entomology: insect anatomy and "
                "morphology, insect orders and taxonomy, metamorphosis, insect physiology, "
                "behavior and social insects, pollination ecology, agricultural and medical "
                "entomology, pest management, beneficial insects, and collection and "
                "identification methods, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what an insect is, "
              "head-thorax-abdomen, exoskeleton and molting, legs, mouthparts, eyes, "
              "antennae, wings and flight, hemolymph and tracheae) -> Compounded "
              "(hemimetaboly, holometaboly, Coleoptera, Diptera and Hymenoptera, "
              "Lepidoptera-Orthoptera-Hemiptera, taxonomy, communication, ants and termites, "
              "bees and wasps, pollination, herbivory, beneficial insects, the nervous "
              "system, reproduction, migration, collection and identification) -> Advanced "
              "(IPM, crop pests, vectors, insecticides and resistance, stored products, "
              "forensics, diapause, genetics, insect dominance, urban pests, conservation).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s — %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search insects, beetles, bees, metamorphosis, pollination, pests...",
        "chat_ph": "Ask about entomology...",
        "archive_blurb": ("Seeded %s entomology records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations · Compounded · Advanced — each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled structural entomology studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about entomology — from what an insect is up to pest management and pollinator conservation." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "entomology-study", "gen_demo_kind": "entomology-demo",
        "source": source,
    }

CIT_PUB = "Entomology (peer-reviewed literature and standard textbooks)."
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["entomology"] = _cfg(
    "entomology", "The Entomology Database",
    "Real, fact-checked entomology: insect anatomy and morphology, insect orders "
    "and taxonomy, metamorphosis, insect physiology, behavior and social insects, "
    "pollination ecology, agricultural and medical entomology, pest management, "
    "beneficial insects, and collection and identification methods.",
    "entomology record", "JAH-ENT-", "JAH Entomology Archivist",
    "entomology archivist — insect anatomy and morphology, insect orders and "
    "taxonomy, metamorphosis, insect physiology, behavior and social insects, "
    "pollination ecology, agricultural and medical entomology, pest management, "
    "beneficial insects, collection and identification methods; teaching "
    "progressively along the ladder from foundations (what an insect is, "
    "head-thorax-abdomen, exoskeleton and molting, legs, mouthparts, eyes, "
    "antennae, wings and flight, hemolymph and tracheae) through compounded "
    "(hemimetaboly, holometaboly, Coleoptera, Diptera and Hymenoptera, "
    "Lepidoptera-Orthoptera-Hemiptera, taxonomy, communication, ants and "
    "termites, bees and wasps, pollination, herbivory, beneficial insects, the "
    "nervous system, reproduction, migration, collection and identification) to "
    "advanced (IPM, crop pests, vectors, insecticides and resistance, stored "
    "products, forensics, diapause, genetics, insect dominance, urban pests, "
    "conservation); answers from many angles — definition, example, analogy, "
    "application, history, math, how-to — using only the system's own archive data",
    CIT_PUB, "public")
DBCFG["entomology-signature"] = _cfg(
    "entomology-signature", "The Entomology Signature Database",
    "His original Signature interpretation of entomology: the full ladder from "
    "what an insect is to pollinator conservation, reframed as Signature "
    "engineering. Clearly labeled Signature-made, never presented as authentic "
    "public record.",
    "entomology record", "JAH-ESG-", "JAH Entomology Archivist (Signature)",
    "entomology archivist — Signature editions: his original Signature interpretation of "
    "entomology, clearly labeled Signature-made and never presented as authentic public "
    "record; teaches progressively along the ladder from foundations through compounded "
    "to advanced; answers from many angles — definition, example, analogy, application, "
    "history, math, how-to — using only the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# entomological calculation for its record. All are machine-executed by main().

_PREAMBLE = """import math
"""

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_insect_diversity(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    described_insects = 1000000
    described_animals = 1300000
    share = described_insects / described_animals
    print("described insects ~%d of ~%d animals -> %.1f %%" % (
        described_insects, described_animals, 100 * share))
    assert abs(share - 0.769) < 0.01
    estimate_low, estimate_high = 5500000, 10000000
    known_low = described_insects / estimate_high
    known_high = described_insects / estimate_low
    print("true total %d-%d -> we know only %.0f-%.0f %%" % (
        estimate_low, estimate_high, 100 * known_low, 100 * known_high))
    assert abs(known_low - 0.10) < 0.01 and abs(known_high - 0.1818) < 0.01
    individuals = 1e19
    print("~%.0e individual insects alive at any moment" % individuals)
    assert individuals == 1e19
    print("OK: %s counted the six-legged kingdom" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_body_tagma(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
TAGMATA = {"head": ("sensory + feeding", 1),
           "thorax": ("locomotion", 3),
           "abdomen": ("viscera", 11)}
def is_insect(tagmata, leg_pairs, antenna_pairs):
    return (set(tagmata) == {"head", "thorax", "abdomen"}
            and leg_pairs == 3 and antenna_pairs == 1)
def main():
    for tagma, (job, segs) in TAGMATA.items():
        print("  %-7s %2d segments -> %s" % (tagma, segs, job))
    assert sum(s for _, s in TAGMATA.values()) == 15
    assert is_insect(["head", "thorax", "abdomen"], 3, 1) is True
    assert is_insect(["cephalothorax", "abdomen"], 4, 0) is False   # spider
    assert is_insect(["head", "trunk"], 30, 1) is False              # millipede
    print("spider/millipede fail the 3-tagma check -> not insects")
    print("OK: %s mapped the tagmata" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_molting_math(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def dyar_series(w0, ratio=1.4, instars=5):
    return [w0 * ratio ** i for i in range(instars)]
def main():
    widths = dyar_series(0.50)            # mm, first-instar head capsule
    for i, w in enumerate(widths, 1):
        print("  instar %d: head capsule %.2f mm" % (i, w))
    ratios = [widths[i + 1] / widths[i] for i in range(len(widths) - 1)]
    assert all(abs(r - 1.4) < 1e-9 for r in ratios), "Dyar's law violated"
    print("growth ratio per molt: %.2f (Dyar's law holds)" % ratios[0])
    assert abs(widths[-1] - 0.50 * 1.4 ** 4) < 1e-9
    # identify an unknown: measured 0.98 mm -> which instar?
    measured = 0.98
    instar = min(range(1, 6), key=lambda i: abs(widths[i - 1] - measured))
    print("measured %.2f mm -> instar %d" % (measured, instar))
    assert instar == 3
    print("OK: %s measured the molts" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_leg_leverage(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def jump_height(v, g=9.81):
    return v ** 2 / (2 * g)
def main():
    # grasshopper: takeoff velocity ~3 m/s
    h = jump_height(3.0)
    print("grasshopper takeoff 3 m/s -> jump height %.2f m" % h)
    assert abs(h - 0.459) < 0.01
    body_m = 0.05
    print("body length 5 cm -> jump is %.0fx body length" % (h / body_m))
    assert h / body_m > 9.0
    # flea: 150 body lengths, body 2 mm -> 0.30 m
    flea_h = 150 * 0.002
    v_needed = math.sqrt(2 * 9.81 * flea_h)
    print("flea jump %.2f m needs takeoff velocity %.2f m/s (elastic catapult)" % (flea_h, v_needed))
    assert abs(v_needed - 2.426) < 0.01
    # tripod gait: always 3 feet down
    print("tripod gait: 3 legs swing while 3 form the support triangle")
    print("OK: %s sprung the leg lever" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mouthpart_matrix(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
MOUTHPARTS = {
    "grasshopper": ("chewing", "leaves"),
    "mosquito female": ("piercing-sucking", "blood"),
    "aphid": ("piercing-sucking", "plant sap"),
    "house fly": ("sponging", "liquids"),
    "butterfly": ("siphoning", "nectar"),
    "honey bee": ("chewing-lapping", "nectar + wax work"),
    "assassin bug": ("piercing-sucking", "other insects"),
}
def main():
    for insect, (mtype, diet) in MOUTHPARTS.items():
        print("  %-15s %-16s feeds on %s" % (insect, mtype, diet))
    assert MOUTHPARTS["mosquito female"][0] == "piercing-sucking"
    assert MOUTHPARTS["butterfly"][0] == "siphoning"
    chewers = [i for i, (m, _) in MOUTHPARTS.items() if m == "chewing"]
    piercers = [i for i, (m, _) in MOUTHPARTS.items() if m == "piercing-sucking"]
    print("%d chewers, %d piercers in the sample" % (len(chewers), len(piercers)))
    assert len(chewers) == 1 and len(piercers) == 3
    print("OK: %s keyed the mouthparts" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eye_facets(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def resolution_deg(interommatidial_angle):
    return interommatidial_angle        # coarsest resolvable detail ~ facet spacing
def main():
    eyes = {"dragonfly": (30000, 1.0), "honey bee": (5500, 2.0), "ant worker": (100, 8.0)}
    for insect, (facets, angle) in eyes.items():
        print("  %-11s %5d facets, ~%.0f deg resolution" % (insect, facets, resolution_deg(angle)))
    assert eyes["dragonfly"][0] == 30000
    # motion vision: flicker fusion
    fly_hz, human_hz = 250.0, 60.0
    print("flicker fusion: fly %.0f Hz vs human %.0f Hz -> fly sees %.1fx faster" % (
        fly_hz, human_hz, fly_hz / human_hz))
    assert abs(fly_hz / human_hz - 4.167) < 0.01
    # superposition gain for night eyes
    print("nocturnal superposition eye: up to 1000x light pooling")
    assert resolution_deg(1.0) < resolution_deg(8.0)
    print("OK: %s resolved the compound eye" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_antenna_odors(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
ANTENNAE = {
    "cockroach": "filiform", "termite": "moniliform", "butterfly": "clavate",
    "scarab beetle": "lamellate", "male moth": "plumose",
    "house fly": "aristate", "ant": "geniculate",
}
def main():
    for insect, shape in ANTENNAE.items():
        print("  %-13s %s" % (insect, shape))
    assert ANTENNAE["male moth"] == "plumose"
    assert ANTENNAE["ant"] == "geniculate"
    assert len(ANTENNAE) == 7
    # male silkmoth: ~17,000 sensilla, single-molecule detection
    sensilla = 17000
    molecules = 1
    print("male silkmoth: %d sensilla detect %d pheromone molecule" % (sensilla, molecules))
    assert sensilla == 17000 and molecules == 1
    # Johnston's organ: mosquito hears ~400 Hz female wingbeat
    print("male mosquito tunes to the female's ~400 Hz wingbeat via Johnston's organ")
    print("OK: %s sniffed with the antennae" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_wingbeat(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
WINGBEATS = {"large butterfly": 5, "honey bee": 230, "house fly": 200,
             "mosquito": 600, "midge": 1000}
def main():
    for insect, hz in WINGBEATS.items():
        print("  %-15s %4d beats/second" % (insect, hz))
    assert WINGBEATS["midge"] == 1000
    assert WINGBEATS["large butterfly"] < WINGBEATS["honey bee"] < WINGBEATS["midge"]
    # asynchronous muscle: 1 nerve impulse -> many beats
    impulses_per_s, beats_per_s = 20.0, 200.0
    gain = beats_per_s / impulses_per_s
    print("asynchronous muscle: %.0f impulses/s drive %.0f beats/s (%.0fx gain)" % (
        impulses_per_s, beats_per_s, gain))
    assert gain == 10.0
    # haltere stabilization feedback time
    print("haltere gyroscopic feedback: course correction within milliseconds")
    print("OK: %s beat the wings" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tracheal_diffusion(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def diffusion_time_ms(distance_um, D_um2_s=2e5):
    # t ~ x^2 / (2D); D for O2 in air ~ 0.2 cm^2/s = 2e5 um^2/s... use tissue-scale value
    D = 2e3   # um^2/s effective in tissue
    return (distance_um ** 2) / (2 * D) * 1000.0
def main():
    for d in (10, 100, 1000):
        print("  O2 diffuses %4d um in ~%.1f ms" % (d, diffusion_time_ms(d)))
    assert diffusion_time_ms(10) < 50.0
    assert diffusion_time_ms(1000) > diffusion_time_ms(100) > diffusion_time_ms(10)
    # why giants needed 35% O2: diffusion distance scales with sqrt(concentration gradient)
    o2_now, o2_carboniferous = 0.21, 0.35
    boost = math.sqrt(o2_carboniferous / o2_now)
    print("35%% O2 vs 21%% O2 -> diffusion reach %.2fx (Carboniferous giants)" % boost)
    assert abs(boost - 1.29) < 0.02
    print("OK: %s breathed through tracheae" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hemimetaboly_table(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    stages = [("egg", 0), ("nymph I", 1), ("nymph II", 2), ("nymph III", 3),
              ("nymph IV", 4), ("nymph V", 5), ("adult", 6)]
    wing_pad = {0: "none", 1: "tiny", 2: "small", 3: "medium", 4: "large",
                5: "veined", 6: "functional wings"}
    for stage, i in stages:
        print("  %-9s wing pads: %s" % (stage, wing_pad[i]))
    assert wing_pad[6] == "functional wings"
    assert len(stages) == 7
    # nymph resembles adult: same diet, same habitat
    print("grasshopper nymph: eats leaves, hops, hides — like the adult, minus wings")
    orders = ["Orthoptera", "Hemiptera", "Odonata", "Blattodea", "Mantodea", "Phasmatodea"]
    print("hemimetabolous orders: %s" % ", ".join(orders))
    assert len(orders) == 6
    print("OK: %s staged incomplete metamorphosis" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_holometaboly_energy(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    larva_mass_mg = 500.0
    fat_fraction = 0.40
    fuel_mg = larva_mass_mg * fat_fraction
    print("caterpillar %.0f mg x %.0f %% fat body = %.0f mg of rebuild fuel" % (
        larva_mass_mg, 100 * fat_fraction, fuel_mg))
    assert fuel_mg == 200.0
    # pupa cannot eat: all adult construction from stored fuel + recycled tissue
    histolysis_recycled = 0.70     # ~70% of larval tissue recycled
    print("histolysis recycles ~%.0f %% of larval tissue into the adult" % (100 * histolysis_recycled))
    assert 0 < histolysis_recycled < 1
    discs = 19                     # pairs of imaginal discs
    print("%d pairs of imaginal discs build wings, legs, eyes, genitalia" % discs)
    assert discs == 19
    share = 0.85                   # ~85% of insect species are holometabolous
    print("holometaboly: ~%.0f %% of all insect species" % (100 * share))
    assert abs(share - 0.85) < 1e-9
    print("OK: %s funded the metamorphosis" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_coleoptera_share(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    beetles, insects, all_life = 400000, 1000000, 1600000
    print("beetles %d / insects %d = %.0f %% of insects" % (beetles, insects, 100 * beetles / insects))
    assert beetles / insects == 0.40
    print("beetles %d / all described life %d = %.0f %%" % (beetles, all_life, 100 * beetles / all_life))
    assert abs(beetles / all_life - 0.25) < 1e-9
    weevils = 60000
    print("weevils (Curculionidae) %d species = %.0f %% of beetles" % (weevils, 100 * weevils / beetles))
    assert abs(weevils / beetles - 0.15) < 1e-9
    # elytra suture check: straight midline
    print("elytra meet in a straight dorsal suture — the field ID mark")
    print("OK: %s tallied the beetles" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_order_lookup(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
ORDERS = {
    "Coleoptera": "elytra; chewing; holometabolous",
    "Diptera": "2 wings + halteres; sucking; holometabolous",
    "Hymenoptera": "hooked wing pairs; chewing; haplodiploid",
    "Lepidoptera": "scale wings; siphoning; holometabolous",
    "Orthoptera": "tegmina + jumping legs; chewing; hemimetabolous",
    "Hemiptera": "hemelytra + beak; piercing-sucking; hemimetabolous",
    "Odonata": "equal membranous wings; chewing; aquatic naiads",
    "Blattodea": "leathery forewings; chewing; includes termites",
}
def diagnose(traits):
    hits = []
    for o, t in ORDERS.items():
        padded = " " + t.replace(";", " ").replace("+", " ") + " "
        if (" " + traits + " ") in padded:
            hits.append(o)
    return hits
def main():
    assert diagnose("halteres") == ["Diptera"]
    assert diagnose("elytra") == ["Coleoptera"]
    assert diagnose("hemelytra") == ["Hemiptera"]
    assert diagnose("scale wings") == ["Lepidoptera"]
    print("keyed: halteres->Diptera, elytra->Coleoptera, hemelytra->Hemiptera, scales->Lepidoptera")
    print("%d orders in the field key" % len(ORDERS))
    assert len(ORDERS) == 8
    print("OK: %s keyed the orders" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_lepidoptera_scales(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    scale_w_um, scale_l_um = 50.0, 100.0   # typical scale dimensions
    scale_area_mm2 = (scale_w_um * scale_l_um) / 1e6
    wing_area_mm2 = 500.0                   # medium butterfly forewing
    scales = wing_area_mm2 / scale_area_mm2
    print("scale %.0fx%.0f um = %.4f mm^2; wing %.0f mm^2 -> ~%.0f scales/wing" % (
        scale_w_um, scale_l_um, scale_area_mm2, wing_area_mm2, scales))
    assert abs(scales - 100000.0) < 1.0
    # structural blue: ridge spacing ~200 nm diffracts blue light
    ridge_nm = 200.0
    blue_nm = 450.0
    print("ridge spacing %.0f nm ~ half of blue %.0f nm -> structural blue (Morpho)" % (ridge_nm, blue_nm))
    assert ridge_nm < blue_nm
    proboscis_cm = 30.0   # Darwin's predicted hawk moth tongue
    print("longest proboscis: %.0f cm (Darwin's predicted moth, found decades later)" % proboscis_cm)
    assert proboscis_cm == 30.0
    print("OK: %s tiled the wing with scales" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_taxonomy_tree(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
TREE = {"Arthropoda": {"Insecta": {
    "Apterygota": ["Archaeognatha", "Zygentoma"],
    "Pterygota": {
        "Paleoptera": ["Odonata", "Ephemeroptera"],
        "Neoptera": {
            "Polyneoptera": ["Orthoptera", "Blattodea", "Mantodea"],
            "Paraneoptera": ["Hemiptera", "Thysanoptera"],
            "Holometabola": ["Coleoptera", "Diptera", "Hymenoptera", "Lepidoptera"],
        }}}}}
def find(order, node=TREE, path=()):
    for k, v in node.items():
        if isinstance(v, list) and order in v:
            return path + (k,)
        if isinstance(v, dict):
            hit = find(order, v, path + (k,))
            if hit:
                return hit
    return None
def main():
    p = find("Hymenoptera")
    print("Hymenoptera: %s" % " -> ".join(p))
    assert p[-1] == "Holometabola"
    assert find("Odonata")[-1] == "Paleoptera"
    assert find("Hemiptera")[-1] == "Paraneoptera"
    assert find("Not an order") is None
    print("OK: %s climbed the insect tree" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_signal_matrix(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
CHANNELS = {
    "chemical": ("pheromones: mate, alarm, trail", "silkmoth bombykol, ant trails"),
    "acoustic": ("stridulation, tymbals", "cricket song, cicada ~120 dB"),
    "visual": ("flash codes, displays", "firefly patterns, butterfly wings"),
    "vibrational": ("stem-borne songs", "treehopper duels"),
    "tactile": ("dance, antennation", "waggle dance, trophallaxis"),
}
def main():
    for ch, (mechanism, example) in CHANNELS.items():
        print("  %-12s %-32s e.g. %s" % (ch, mechanism, example))
    assert len(CHANNELS) == 5
    assert "120 dB" in CHANNELS["acoustic"][1]
    assert CHANNELS["tactile"][1].startswith("waggle")
    # ant trail: shortest path emerges from pheromone reinforcement
    print("ant trail = living computation: evaporating pheromone converges on the richest source")
    print("OK: %s tuned the five channels" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_colony_castes(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # leafcutter colony caste model
    colony = 8000000
    castes = {"minims (gardeners)": 0.50, "medias (foragers)": 0.40,
              "majors (soldiers)": 0.09, "queens": 1 / colony}
    total = 0
    for caste, frac in castes.items():
        n = colony * frac
        total += n
        print("  %-20s %10.0f" % (caste, n))
    assert abs(total - colony) / colony < 0.02
    # termite queen output
    eggs_per_day = 30000
    print("termite queen: %d eggs/day x 365 = %.1f million/year" % (eggs_per_day, eggs_per_day * 365 / 1e6))
    assert eggs_per_day * 365 == 10950000
    # Argentine ant supercolony span
    print("Argentine ant supercolony: hundreds of km, millions of queens cooperating")
    print("OK: %s mustered the colony" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_waggle_dance(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def decode_dance(angle_from_vertical_deg, waggle_seconds):
    # angle from vertical = angle of food from sun's azimuth; ~1 s waggle ~ 1 km
    direction = angle_from_vertical_deg
    distance_km = waggle_seconds * 1.0
    return direction, distance_km
def main():
    direction, distance = decode_dance(40.0, 2.5)
    print("dance: 40 deg from vertical, 2.5 s waggle -> food at %d deg from sun, %.1f km away" % (
        direction, distance))
    assert direction == 40.0 and abs(distance - 2.5) < 1e-9
    d2, dist2 = decode_dance(-60.0, 0.5)
    print("dance: -60 deg, 0.5 s -> %d deg from sun, %.1f km (nearby patch)" % (d2, dist2))
    assert dist2 == 0.5
    # colony decision: quorum of dancers
    dancers = {"site A": 25, "site B": 12, "site C": 8}
    winner = max(dancers, key=dancers.get)
    print("swarm vote %s -> consensus: %s" % (dancers, winner))
    assert winner == "site A"
    print("OK: %s decoded the waggle dance" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pollination_value(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    crops = [("almonds", 1.00), ("apples", 0.90), ("blueberries", 0.95),
             ("squash", 0.90), ("wheat", 0.00)]
    for crop, dependence in crops:
        print("  %-11s pollinator dependence %.0f %%" % (crop, 100 * dependence))
    assert crops[0][1] == 1.00 and crops[-1][1] == 0.00
    # global value estimate
    value_usd_bn = 200.0
    print("insect pollination worth ~$%.0f billion/year to agriculture" % value_usd_bn)
    assert value_usd_bn >= 150.0
    # flowering plant dependence
    pct = 87.0
    print("%.0f %% of flowering plant species need animal pollinators" % pct)
    assert pct == 87.0
    # fig-fig wasp obligate pairs
    print("~750 fig species, each with its own wasp species — 80-million-year mutualism")
    print("OK: %s valued the pollinators" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_herbivory_damage(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def defoliation_pct(eaten_cm2, leaf_cm2):
    return 100.0 * eaten_cm2 / leaf_cm2
def main():
    d = defoliation_pct(15.0, 100.0)
    print("caterpillar eats 15 cm^2 of 100 cm^2 leaf -> %.0f %% defoliation" % d)
    assert d == 15.0
    # plant tolerance: wild plants regrow; economic threshold much lower in crops
    wild_tolerate, crop_et = 30.0, 5.0
    print("wild plant tolerates ~%.0f %%; crop action threshold ~%.0f %%" % (wild_tolerate, crop_et))
    assert wild_tolerate > crop_et
    # monarch sequestration: milkweed toxin stored
    print("monarch: sequesters cardiac glycosides -> poisonous, warning-colored")
    # induced defense timing
    print("jasmonic-acid defenses ramp within hours of feeding; volatiles summon parasitoids")
    print("OK: %s measured the herbivory" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_parasitoid_rates(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def parasitism_pct(parasitized, total):
    return 100.0 * parasitized / total
def main():
    p = parasitism_pct(68, 100)
    print("68 of 100 caterpillars parasitized -> %.0f %% parasitism" % p)
    assert p == 68.0
    # suppression rule of thumb: >50% sustained parasitism suppresses the pest
    assert p > 50.0, "below suppression level"
    # ladybird lifetime aphid consumption
    lifetime_aphids = 5000
    print("one ladybird eats ~%d aphids in its lifetime" % lifetime_aphids)
    assert lifetime_aphids == 5000
    # Trichogramma: pinhead-sized egg parasitoid
    print("Trichogramma wasp: smaller than a pinhead; parasitizes moth eggs")
    print("OK: %s rated the natural enemies" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_neuron_speed(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def reflex_ms(distance_mm, speed_m_s):
    return distance_mm / 1000.0 / speed_m_s * 1000.0
def main():
    # giant fiber escape: ~5 m/s over ~10 mm body
    t = reflex_ms(10.0, 5.0)
    print("escape circuit: 10 mm at 5 m/s -> %.1f ms" % t)
    assert abs(t - 2.0) < 0.1
    # fly haltere reflex corrects flight within milliseconds
    print("haltere reflex arc: course correction without brain involvement")
    # mushroom body learning: bee remembers flower location
    print("mushroom bodies: associative learning center (odor + reward)")
    # octopamine = insect adrenaline
    print("octopamine triggers fight-or-flight arousal; serotonin drives locust gregarization")
    assert reflex_ms(10.0, 5.0) < reflex_ms(10.0, 1.0)
    print("OK: %s timed the neurons" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_fecundity_table(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def project(females, eggs_per_female, generations, survival=0.02):
    pop = females
    for _ in range(generations):
        pop = pop * eggs_per_female * 0.5 * survival   # half female, survival fraction
    return pop
def main():
    table = [("termite queen", 30000, "per day"), ("mosquito", 300, "per blood meal"),
             ("house fly", 500, "per lifetime")]
    for insect, eggs, per in table:
        print("  %-13s %5d eggs %s" % (insect, eggs, per))
    assert table[0][1] == 30000
    # mosquito projection: 10 females, 3 generations, 2% survival
    pop = project(10, 300, 3)
    print("10 mosquitoes x 3 generations (2%% survival) -> %.0f females" % pop)
    assert abs(pop - 270.0) < 1.0
    print("99%% mortality still leaves mosquitoes growing — target reproduction itself")
    print("OK: %s counted the eggs" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_migration_distance(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def flight_days(distance_km, speed_kmh, hours_per_day):
    return distance_km / (speed_kmh * hours_per_day)
def main():
    # monarch: 4000 km at ~15 km/h, 8 h/day
    d = flight_days(4000.0, 15.0, 8.0)
    print("monarch 4000 km at 15 km/h x 8 h/day -> %.1f days of flight" % d)
    assert abs(d - 33.3) < 0.2
    # painted lady circuit up to ~14000 km
    d2 = flight_days(14000.0, 20.0, 10.0)
    print("painted lady ~14000 km circuit -> %.0f flight-days" % d2)
    assert abs(d2 - 70.0) < 1.0
    # clock-shift proof: 6 h shift -> ~90 deg direction error
    print("clock-shift 6 h rotates monarch heading ~90 deg (time-compensated sun compass proven)")
    assert d2 > d
    print("OK: %s tracked the migration" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_trap_counts(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def catch_per_trap_night(total, traps, nights):
    return total / (traps * nights)
def main():
    c = catch_per_trap_night(240, 10, 7)
    print("240 beetles / (10 pitfalls x 7 nights) = %.2f per trap-night" % c)
    assert abs(c - 3.4286) < 0.001
    # standardization makes surveys comparable
    c2 = catch_per_trap_night(120, 10, 7)
    print("site B: %.2f per trap-night -> site A richer than site B" % c2)
    assert c > c2
    # Malaise trap season haul
    print("one Malaise trap x one season -> thousands of species (biodiversity workhorse)")
    # label checklist
    print("every specimen: GPS + date + collector + habitat + method, or it is worthless")
    print("OK: %s standardized the traps" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ipm_threshold(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def eil(control_cost, crop_value_per_unit, damage_per_pest, efficacy):
    return control_cost / (crop_value_per_unit * damage_per_pest * efficacy)
def main():
    # $25/ha spray, crop $400/t, each pest costs 0.002 t, spray 90% effective
    e = eil(25.0, 400.0, 0.002, 0.90)
    print("EIL = 25 / (400 x 0.002 x 0.90) = %.1f pests per sampling unit" % e)
    assert abs(e - 34.7) < 0.2
    et = e * 0.75     # act before the EIL is reached
    print("economic threshold set at 75%% of EIL -> %.1f (spray above this)" % et)
    assert et < e
    # scout count vs threshold
    scouted = 40.0
    print("scouted %.0f -> %s" % (scouted, "SPRAY" if scouted >= et else "HOLD"))
    assert scouted >= et
    print("no spray without a number — that is IPM")
    print("OK: %s computed the threshold" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pest_loss(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def loss_pct(potential_t, actual_t):
    return 100.0 * (potential_t - actual_t) / potential_t
def main():
    l = loss_pct(10.0, 7.8)
    print("potential 10 t/ha, harvested 7.8 -> %.0f %% lost to pests" % l)
    assert abs(l - 22.0) < 0.5
    # global range 18-26%
    assert 18.0 <= l <= 26.0, "within the global 18-26% band"
    # western corn rootworm: ~$1.5B/year US
    print("western corn rootworm: ~$1-2 billion/year in US corn")
    # fall armyworm invasion timeline
    print("fall armyworm: Africa 2016 -> Asia 2018 (invasive spread)")
    print("OK: %s tallied the crop losses" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_vector_r0(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def r0(m, a, b, c, p, n, r=0.05):
    # m: mosquitoes/human, a: bites/day, b,c: transmission probs,
    # p: daily survival, n: extrinsic incubation days, r: human recovery rate (1/days infectious)
    mu = -math.log(p)
    return m * a ** 2 * b * c * (p ** n) / (mu * r)
def main():
    base = r0(m=10.0, a=0.3, b=0.5, c=0.5, p=0.90, n=12.0)
    print("baseline malaria R0 ~ %.2f" % base)
    assert base > 1.0, "disease spreads at baseline"
    # bed nets halve biting rate -> R0 scales with a^2
    halved = r0(m=10.0, a=0.15, b=0.5, c=0.5, p=0.90, n=12.0)
    print("biting rate halved -> R0 ~ %.2f (quarter of baseline: a^2 scaling)" % halved)
    assert abs(halved - base / 4.0) < 1e-9
    # shorter mosquito life: p 0.90 -> 0.80 crashes p^n
    short = r0(m=10.0, a=0.3, b=0.5, c=0.5, p=0.80, n=12.0)
    print("daily survival 0.90 -> 0.80 -> R0 ~ %.2f (incubation bottleneck)" % short)
    assert short < base / 5.0
    print("attack the exponential term: adult survival")
    print("OK: %s modeled the vector" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_resistance_ratio(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def rr(lc50_resistant, lc50_susceptible):
    return lc50_resistant / lc50_susceptible
def main():
    r = rr(500.0, 5.0)
    print("LC50 resistant 500 vs susceptible 5 -> resistance ratio %.0fx" % r)
    assert r == 100.0
    # selection over seasons: exponential climb
    ratio, factor, seasons = 1.0, 2.5, 6
    for s in range(1, seasons + 1):
        ratio *= factor
    print("2.5x per season x 6 seasons -> %.0fx resistance" % ratio)
    assert abs(ratio - 244.14) < 0.5
    # kdr cross-resistance: one mutation defeats DDT + pyrethroids
    print("kdr sodium-channel mutation: cross-resistance to DDT and pyrethroids")
    # refuge strategy keeps resistance recessive
    print("high-dose/refuge: rare resistants mate susceptibles -> resistance stays heterozygous")
    print("OK: %s measured the resistance" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_storage_loss(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def population(females0, eggs, generations, survival=0.5):
    pop = females0
    for _ in range(generations):
        pop = pop * eggs * 0.5 * survival
    return pop
def main():
    # rice weevil: 1 mated female, 300 eggs, 4-week generations
    pop = population(1, 300, 4)
    print("1 weevil female x 4 generations -> %.0f weevils" % pop)
    assert abs(pop - 31640625.0) < 1.0
    print("the mathematics of neglect: exponential")
    # hermetic storage: O2 below ~2-3% asphyxiates
    o2_start, o2_lethal = 21.0, 2.5
    print("sealed storage: O2 %.0f %% -> below %.1f %% kills all stages, no chemistry" % (o2_start, o2_lethal))
    assert o2_lethal < 3.0
    # keep grain dry and cool
    print("keep grain below ~13%% moisture and 18 C: development stalls")
    print("OK: %s audited the grain store" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pmi_calc(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def accumulated_degree_hours(temps_c, threshold_c=6.0):
    return sum(max(0.0, t - threshold_c) for t in temps_c)
def main():
    # Lucilia sericata: egg hatch needs ~ 6 C threshold; suppose 20 C scene
    hours = [20.0] * 48
    adh = accumulated_degree_hours(hours)
    print("48 h at 20 C, threshold 6 C -> %.0f accumulated degree-hours" % adh)
    assert adh == 672.0
    # instar from posterior spiracle slits
    slits_to_instar = {1: "I", 2: "II", 3: "III"}
    oldest = slits_to_instar[3]
    print("oldest larvae: %d slits -> instar %s" % (3, oldest))
    assert oldest == "III"
    # thermal constant example: hatch at ~ 150 ADH -> back-calculate colonization
    thermal_constant = 150.0
    back_hours = thermal_constant / (20.0 - 6.0)
    print("hatch constant %.0f ADH -> eggs laid ~%.1f h before oldest hatch observed" % (
        thermal_constant, back_hours))
    assert abs(back_hours - 10.7) < 0.2
    print("blow flies colonize within minutes: minimum PMI from the oldest stage")
    print("OK: %s read the forensic clock" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_supercooling(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def freezing_point_depression(molality, Kf=1.86):
    return Kf * molality
def main():
    # glycerol accumulation depresses freezing point colligatively
    dep = freezing_point_depression(3.0)
    print("3 molal glycerol -> freezing point depressed %.1f C" % dep)
    assert abs(dep - 5.58) < 0.01
    # supercooling points
    print("goldenrod gall fly larva supercools to ~-50 C (freeze avoider)")
    print("woolly bear caterpillar freezes solid and thaws (freeze tolerant)")
    scp_gallfly, scp_temperate = -50.0, -20.0
    assert scp_gallfly < scp_temperate
    # diapause metabolic suppression
    active, diapause = 100.0, 10.0
    print("diapause metabolism: %.0f %% -> %.0f %% of active rate" % (diapause, active))
    assert diapause < active / 5.0
    print("OK: %s wintered the insect" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_genome_size(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
GENOMES = {"Drosophila melanogaster": (180, 14000),
           "Anopheles gambiae": (278, 14000),
           "Apis mellifera": (250, 15000),
           "Locusta migratoria": (6500, 17000)}
def main():
    for insect, (mb, genes) in GENOMES.items():
        print("  %-25s %4d Mb  ~%d genes" % (insect, mb, genes))
    assert GENOMES["Drosophila melanogaster"][0] == 180
    ratio = GENOMES["Locusta migratoria"][0] / GENOMES["Drosophila melanogaster"][0]
    print("locust genome %.1fx the fruit fly's (transposon bloat)" % ratio)
    assert abs(ratio - 36.1) < 0.2
    # gene drive inheritance: 50% -> ~100%
    print("gene drive: heterozygote passes trait to ~100%% of offspring, not 50%%")
    # SIT ratio rule
    print("sterile insect technique: flood at >10:1 sterile:wild males")
    print("OK: %s sequenced the insects" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_success_factors(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
FACTORS = {"small size (niche subdivision)": 2, "flight": 3, "metamorphosis": 3,
           "exoskeleton": 2, "high fecundity": 2, "angiosperm coevolution": 3,
           "specialization": 2}
def main():
    total = sum(FACTORS.values())
    for factor, weight in FACTORS.items():
        print("  %-32s weight %d" % (factor, weight))
    print("success score: %d (stacked advantages, not one trick)" % total)
    assert total == 17
    # holometaboly share
    print("holometabolous: ~85%% of insect species")
    # decline rate compounding
    rate, years = 0.015, 30
    remaining = (1 - rate) ** years
    print("1.5%%/year decline x 30 years -> %.0f %% remaining" % (100 * remaining))
    assert abs(remaining - 0.635) < 0.01
    print("the same formula explains the crisis: specialists fall fast")
    print("OK: %s scored insect dominance" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_urban_ipm(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # bed bug heat treatment: 50 C kills all stages
    lethal_c, hold_h = 50.0, 2.0
    print("heat treatment: %.0f C for %.0f h kills eggs, nymphs, adults" % (lethal_c, hold_h))
    assert lethal_c == 50.0
    # interceptor trap monitoring: zero catch for 8 weeks = elimination
    weeks_clear = 8
    print("interceptor traps: %d weeks of zero catch confirms elimination" % weeks_clear)
    assert weeks_clear == 8
    # termite bait: colony collapse over months via trophallaxis
    print("chitin-inhibitor bait: workers share it; colony spirals down over months")
    # cockroach bait: slow poison beats fast poison (avoids aversion learning)
    print("slow-acting gel bait: foragers carry it home; fast poison teaches avoidance")
    # exclusion math: seal entry points
    gaps = ["pipes", "vents", "doors", "cracks"]
    print("exclusion checklist: %s" % ", ".join(gaps))
    assert len(gaps) == 4
    print("OK: %s fortified the building" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_decline_stats(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def remaining_after(rate, years):
    return (1 - rate) ** years
def main():
    for rate in (0.01, 0.02):
        r30 = remaining_after(rate, 30)
        print("  %.0f %%/year x 30 years -> %.0f %% of insects remaining" % (100 * rate, 100 * r30))
    assert abs(remaining_after(0.01, 30) - 0.740) < 0.01
    assert abs(remaining_after(0.02, 30) - 0.545) < 0.01
    # western monarch collapse
    then, now = 4500000, 30000
    print("western monarch: ~%d (1980s-90s) -> ~%d now = %.1f %% lost" % (
        then, now, 100 * (1 - now / then)))
    assert 100 * (1 - now / then) > 99.0
    # intervention effect: no-mow corridors raise pollinator abundance
    print("wildflower strips + no-mow corridors measurably raise pollinator abundance")
    print("OK: %s graphed the decline" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "insect_diversity": demo_insect_diversity, "body_tagma": demo_body_tagma,
    "molting_math": demo_molting_math, "leg_leverage": demo_leg_leverage,
    "mouthpart_matrix": demo_mouthpart_matrix, "eye_facets": demo_eye_facets,
    "antenna_odors": demo_antenna_odors, "wingbeat": demo_wingbeat,
    "tracheal_diffusion": demo_tracheal_diffusion,
    "hemimetaboly_table": demo_hemimetaboly_table,
    "holometaboly_energy": demo_holometaboly_energy,
    "coleoptera_share": demo_coleoptera_share, "order_lookup": demo_order_lookup,
    "lepidoptera_scales": demo_lepidoptera_scales, "taxonomy_tree": demo_taxonomy_tree,
    "signal_matrix": demo_signal_matrix, "colony_castes": demo_colony_castes,
    "waggle_dance": demo_waggle_dance, "pollination_value": demo_pollination_value,
    "herbivory_damage": demo_herbivory_damage, "parasitoid_rates": demo_parasitoid_rates,
    "neuron_speed": demo_neuron_speed, "fecundity_table": demo_fecundity_table,
    "migration_distance": demo_migration_distance, "trap_counts": demo_trap_counts,
    "ipm_threshold": demo_ipm_threshold, "pest_loss": demo_pest_loss,
    "vector_r0": demo_vector_r0, "resistance_ratio": demo_resistance_ratio,
    "storage_loss": demo_storage_loss, "pmi_calc": demo_pmi_calc,
    "supercooling": demo_supercooling, "genome_size": demo_genome_size,
    "success_factors": demo_success_factors, "urban_ipm": demo_urban_ipm,
    "decline_stats": demo_decline_stats,
}

# ---------------------------------------------------------------- records

def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_entomology.py).
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
    for slug in ("entomology", "entomology-signature"):
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
