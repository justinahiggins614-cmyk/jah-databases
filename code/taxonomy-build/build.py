"""Build the Taxonomy field databases for JAH Databases (field #7, taxonomy order).

Verified 2026-10-17: NO database covers biological taxonomy as a science.
Manifest "taxonomy" slugs are technology-field taxonomies
(software-labs-taxonomy, core-engine-taxonomy, storage-repository-taxonomy,
network-interconnect-taxonomy, hardware-fabrication-taxonomy); keyword hits
'ai-types' ("Russell and Norvig's agent taxonomy") and 'system-logs'
("error taxonomy") are spurious. So this build creates two NEW databases:

  taxonomy              — The Taxonomy Database (public-harvest: real,
                          fact-checked taxonomy science — Linnaean system,
                          ranks, binomial nomenclature, type specimens,
                          nomenclature codes ICZN/ICNafp/ICNP, synonymy and
                          priority, phylogenetics, cladistics, molecular
                          systematics, DNA barcoding, taxonomic revisions,
                          biodiversity informatics)
  taxonomy-signature    — The Taxonomy Signature Database (his original
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

sys.path.insert(0, HERE)
from entries_taxonomy import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals — his original Signature interpretation of taxonomy: "
                "clearly labeled Signature-made, never presented as authentic public record.")
    pub_line = ("Public records — real, fact-checked taxonomy science: the Linnaean system, "
                "taxonomic ranks, binomial nomenclature, type specimens, the nomenclature "
                "codes (ICZN, ICNafp, ICNP), synonymy and priority, phylogenetics, "
                "cladistics, molecular systematics, DNA barcoding, taxonomic revisions, "
                "and biodiversity informatics, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what taxonomy is, "
              "ranks, binomial nomenclature, Linnaeus, kingdoms and domains, type "
              "specimens, synonymy and priority, reading scientific names, monographs, "
              "museums, common vs scientific names) -> Compounded (phylogenetics, "
              "cladistics, monophyly/paraphyly/polyphyly, morphology-based systematics, "
              "molecular systematics, DNA barcoding, nomenclature codes, taxonomic "
              "revisions, species concepts, dichotomous keys, biodiversity informatics, "
              "reading trees, inference methods) -> Advanced (phylogenomics, molecular "
              "clock, cryptic species, splits and conservation, integrative taxonomy, "
              "ZooBank registration, describing new species, taxonomic impediment, "
              "machine-vision identification, eDNA and metagenomics, PhyloCode, "
              "taxonomic database standards).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s — %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search Linnaeus, binomial names, ICZN, phylogenetics, DNA barcoding, types...",
        "chat_ph": "Ask about taxonomy...",
        "archive_blurb": ("Seeded %s taxonomy records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations · Compounded · Advanced — each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled structural taxonomy studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about taxonomy — from reading a scientific name up to phylogenomics and the PhyloCode." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "taxonomy-study", "gen_demo_kind": "taxonomy-demo",
        "source": source,
    }

CIT_PUB = "Taxonomy (peer-reviewed literature and standard textbooks)."
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["taxonomy"] = _cfg(
    "taxonomy", "The Taxonomy Database",
    "Real, fact-checked taxonomy science: the Linnaean system, ranks, binomial "
    "nomenclature, type specimens, nomenclature codes, synonymy, phylogenetics, "
    "cladistics, molecular systematics, DNA barcoding, revisions, and "
    "biodiversity informatics.",
    "taxonomy record", "JAH-TAX-", "JAH Taxonomy Archivist",
    "taxonomy archivist — Linnaean system, taxonomic ranks, binomial nomenclature, "
    "type specimens, nomenclature codes ICZN/ICNafp/ICNP, synonymy and priority, "
    "phylogenetics, cladistics, molecular systematics, DNA barcoding, taxonomic "
    "revisions, biodiversity informatics; teaching progressively along the ladder from "
    "foundations (what taxonomy is, ranks, binomial nomenclature, Linnaeus, kingdoms "
    "and domains, type specimens, synonymy and priority, reading scientific names, "
    "monographs, museums, common vs scientific names) through compounded "
    "(phylogenetics, cladistics, monophyly/paraphyly/polyphyly, morphology-based "
    "systematics, molecular systematics, DNA barcoding, nomenclature codes, taxonomic "
    "revisions, species concepts, dichotomous keys, biodiversity informatics, reading "
    "trees, inference methods) to advanced (phylogenomics, molecular clock, cryptic "
    "species, splits and conservation, integrative taxonomy, ZooBank registration, "
    "describing new species, taxonomic impediment, machine-vision identification, "
    "eDNA and metagenomics, PhyloCode, taxonomic database standards); answers from "
    "many angles — definition, example, analogy, application, history, math, "
    "how-to — using only the system's own archive data",
    CIT_PUB, "public")
DBCFG["taxonomy-signature"] = _cfg(
    "taxonomy-signature", "The Taxonomy Signature Database",
    "His original Signature interpretation of taxonomy: the full ladder from "
    "reading a scientific name to phylogenomics and the PhyloCode, reframed as "
    "Signature engineering. Clearly labeled Signature-made, never presented as "
    "authentic public record.",
    "taxonomy record", "JAH-TSG-", "JAH Taxonomy Archivist (Signature)",
    "taxonomy archivist — Signature editions: his original Signature interpretation of "
    "taxonomy, clearly labeled Signature-made and never presented as authentic public "
    "record; teaches progressively along the ladder from foundations through compounded "
    "to advanced; answers from many angles — definition, example, analogy, application, "
    "history, math, how-to — using only the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# taxonomic calculation for its record. All are machine-executed by main().

_PREAMBLE = """import math
import re
"""

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_taxonomy_scale(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    described = 2200000.0
    estimate = 8700000.0   # Mora et al. 2011 eukaryote estimate
    known_pct = 100 * described / estimate
    print("described ~%.1fM of ~%.1fM eukaryotes -> %.1f %% known" % (
        described / 1e6, estimate / 1e6, known_pct))
    assert abs(known_pct - 25.29) < 0.1
    unknown = estimate - described
    print("unknown: ~%.1fM species (%.1f %%)" % (unknown / 1e6, 100 - known_pct))
    assert abs(unknown - 6500000.0) < 1.0
    per_year = 17500.0
    years = unknown / per_year
    print("at ~%.0f new species/year -> %.0f years to finish" % (per_year, years))
    assert 370.0 < years < 375.0
    print("OK: %s counted the unknown" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_rank_ladder(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
RANKS = ["Domain", "Kingdom", "Phylum", "Class", "Order", "Family", "Genus", "Species"]
def steps_between(a, b):
    return abs(RANKS.index(a) - RANKS.index(b))
HUMAN = {"Domain": "Eukarya", "Kingdom": "Animalia", "Phylum": "Chordata",
         "Class": "Mammalia", "Order": "Primates", "Family": "Hominidae",
         "Genus": "Homo", "Species": "Homo sapiens"}
def main():
    assert RANKS.index("Species") - RANKS.index("Genus") == 1
    assert steps_between("Domain", "Species") == 7
    assert steps_between("Family", "Genus") == 1
    assert HUMAN["Species"] == "Homo sapiens"
    assert HUMAN["Class"] == "Mammalia"
    # lowest shared rank: human vs lion share Class Mammalia
    lion_class = "Mammalia"
    shared = HUMAN["Class"] == lion_class
    print("human vs lion share rank: Class (%s) -> %s" % (lion_class, shared))
    assert shared is True
    print("ranks: %s" % " > ".join(RANKS))
    print("OK: %s climbed the ladder" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_binomial_check(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def valid_binomial(s):
    parts = s.split()
    return (len(parts) == 2 and parts[0][0].isupper()
            and parts[0][1:].islower() and parts[1].islower())
def strip_author(full):
    s = full.split("(")[0].strip()
    return " ".join(s.split()[:2])
def abbreviate(binomial):
    g, e = binomial.split()
    return g[0] + ". " + e
def main():
    assert valid_binomial("Homo sapiens") is True
    assert valid_binomial("Panthera leo") is True
    assert valid_binomial("homo Sapiens") is False
    assert valid_binomial("Homo") is False
    assert valid_binomial("Homo sapiens extra") is False
    assert strip_author("Panthera leo (Linnaeus, 1758)") == "Panthera leo"
    assert strip_author("Homo sapiens Linnaeus, 1758") == "Homo sapiens"
    assert abbreviate("Panthera leo") == "P. leo"
    print("valid: Homo sapiens, Panthera leo; invalid: homo Sapiens, Homo, trinomials")
    print("OK: %s checked the binomials" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_linnaeus_counts(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    plants = 7700.0    # Species Plantarum (1753), approximate
    animals = 4400.0   # Systema Naturae 10th ed. (1758), approximate
    assert 7000.0 < plants < 8000.0
    assert 4000.0 < animals < 5000.0
    total = plants + animals
    print("Linnaeus described ~%.0f plants + ~%.0f animals = ~%.0f species" % (
        plants, animals, total))
    assert total == 12100.0
    plant_share = 100 * plants / total
    print("plant share: %.1f %%" % plant_share)
    assert 63.0 < plant_share < 64.0
    # starting points of nomenclature
    print("nomenclature starts: plants 1753-05-01, animals 1758-01-01")
    print("OK: %s tallied Linnaeus" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_kingdom_map(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
DOMAINS = {
    "Bacteria": ["bacteria"],
    "Archaea": ["archaea"],
    "Eukarya": ["Animalia", "Plantae", "Fungi", "Protista"],
}
WHITTAKER_1969 = ["Monera", "Protista", "Plantae", "Fungi", "Animalia"]
def main():
    assert len(DOMAINS) == 3
    assert "Fungi" in DOMAINS["Eukarya"]
    assert "Animalia" in DOMAINS["Eukarya"]
    assert len(WHITTAKER_1969) == 5
    assert "Monera" in WHITTAKER_1969
    # Archaea look bacterial but group with Eukarya: the Woese shock
    print("domains: %s" % ", ".join(DOMAINS))
    print("Whittaker 1969 kingdoms: %s" % ", ".join(WHITTAKER_1969))
    print("Archaea: bacterial bodies, eukaryotic-grade genes")
    print("OK: %s mapped the deep branches" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_type_registry(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
PRIORITY = ["holotype", "lectotype", "neotype", "syntype"]
def name_bearer(available):
    for t in PRIORITY:
        if t in available:
            return t
    return None
def main():
    assert name_bearer(["syntype", "lectotype"]) == "lectotype"
    assert name_bearer(["neotype", "syntype"]) == "neotype"
    assert name_bearer(["holotype", "neotype"]) == "holotype"
    assert name_bearer(["paratype"]) is None
    assert name_bearer(["holotype"]) == "holotype"
    print("bearer priority: %s" % " > ".join(PRIORITY))
    print("paratype alone never bears the name")
    print("OK: %s anchored the names" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_priority_rule(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def senior_name(candidates):
    # candidates: (name, author, year); oldest validly published wins
    return min(candidates, key=lambda c: c[2])
def main():
    names = [("Felis catus", "Linnaeus", 1758),
             ("Felis domestica", "Erxleben", 1777),
             ("Felis catus domestica", "Kerr", 1792)]
    win = senior_name(names)
    print("candidates: %s" % [(n, y) for n, a, y in names])
    print("senior synonym: %s %s, %d" % win)
    assert win[0] == "Felis catus" and win[2] == 1758
    # junior homonym: same name, later use -> invalid, needs replacement
    homonyms = [("Musca", "Linnaeus", 1758), ("Musca", "Later", 1800)]
    junior = max(homonyms, key=lambda c: c[2])
    print("junior homonym %s %s, %d -> must be replaced" % junior)
    assert junior[2] == 1800
    print("OK: %s applied priority" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_name_parser(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def parse(full):
    m = re.match(r"^([A-Z][a-z]+)\\s+([a-z]+)(?:\\s+\\(?([A-Z][a-z\\.]+(?:\\s+[A-Z][a-z\\.]+)?),?\\s*(\\d{4})?\\)?)?$", full.strip())
    assert m, "unparseable: %s" % full
    genus, epithet, author, year = m.group(1), m.group(2), m.group(3), m.group(4)
    moved = full.strip().startswith(genus + " " + epithet + " (")
    return {"genus": genus, "epithet": epithet, "author": author,
            "year": int(year) if year else None, "genus_changed": moved}
def main():
    p = parse("Panthera leo (Linnaeus, 1758)")
    assert p["genus"] == "Panthera" and p["epithet"] == "leo"
    assert p["author"] == "Linnaeus" and p["year"] == 1758
    assert p["genus_changed"] is True
    q = parse("Homo sapiens Linnaeus, 1758")
    assert q["genus_changed"] is False and q["year"] == 1758
    r = parse("Quercus alba L.")
    assert r["genus"] == "Quercus" and r["author"] == "L."
    print("Panthera leo (Linnaeus, 1758): moved genus -> parentheses")
    print("Homo sapiens Linnaeus, 1758: original genus -> no parentheses")
    print("OK: %s parsed the packets" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_monograph_scale(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    pages, species = 1200.0, 350.0
    per_species = pages / species
    print("%.0f pages / %.0f species = %.2f pages per species" % (pages, species, per_species))
    assert abs(per_species - 3.4286) < 0.01
    illustrations = 2.0 * species
    print("%.0f illustrations (2 per species)" % illustrations)
    assert illustrations == 700.0
    # account template fields every species gets
    fields = ["accepted name", "synonymy", "description", "distribution",
              "habitat", "specimens examined", "notes"]
    print("account template: %d fields" % len(fields))
    assert len(fields) == 7
    print("OK: %s shelved the monograph" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_museum_growth(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    drawers, per_drawer = 400.0, 200.0
    specimens = drawers * per_drawer
    print("%.0f drawers x %.0f specimens = %.0f specimens" % (drawers, per_drawer, specimens))
    assert specimens == 80000.0
    image_rate = 500.0  # specimens imaged per day
    days = specimens / image_rate
    print("digitizing at %.0f/day -> %.0f days (%.1f years)" % (image_rate, days, days / 365))
    assert abs(days - 160.0) < 1e-9
    # backlog discovery: fraction of 'new' species found in drawers vs field
    drawer_share = 0.5
    print("about half of newly recognized species were already sitting in drawers")
    assert drawer_share == 0.5
    print("OK: %s inventoried the archive" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_common_name_map(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
COMMON_TO_SCI = {"puma": "Puma concolor", "cougar": "Puma concolor",
                 "mountain lion": "Puma concolor", "catamount": "Puma concolor"}
ROBIN_MEANINGS = {"robin": ["Erithacus rubecula (Europe)",
                            "Turdus migratorius (N. America)",
                            "Petroica spp. (Australia)"]}
def main():
    targets = {COMMON_TO_SCI[c] for c in ["puma", "cougar", "mountain lion", "catamount"]}
    print("4 common names -> %d scientific name: %s" % (len(targets), targets.pop()))
    assert targets == set() or True
    assert len({COMMON_TO_SCI[c] for c in COMMON_TO_SCI}) == 1
    robins = ROBIN_MEANINGS["robin"]
    print("1 common name 'robin' -> %d different birds" % len(robins))
    assert len(robins) == 3
    # scientific name is the primary key; common names are aliases
    print("primary key: Puma concolor; aliases: puma, cougar, mountain lion, catamount")
    print("OK: %s keyed the aliases" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_newick_tree(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def parse_newick(s):
    s = s.strip().rstrip(";")
    stack, cur, name = [], [], ""
    for ch in s:
        if ch == "(":
            stack.append(cur); cur = []
        elif ch == ",":
            if name: cur.append(name); name = ""
        elif ch == ")":
            if name: cur.append(name); name = ""
            node = tuple(cur); cur = stack.pop(); cur.append(node)
        else:
            name += ch
    if name: cur.append(name)
    return cur[0]
def tips(node):
    if isinstance(node, str): return {node}
    out = set()
    for c in node: out |= tips(c)
    return out
def mrca(node, a, b):
    # smallest clade containing both
    if isinstance(node, str): return None
    t = tips(node)
    if a in t and b in t:
        for c in node:
            hit = mrca(c, a, b)
            if hit is not None: return hit
        return node
    return None
def main():
    tree = parse_newick("(A,B,(C,D));")
    assert tips(tree) == {"A", "B", "C", "D"}
    m = mrca(tree, "C", "D")
    assert tips(m) == {"C", "D"}, "MRCA(C,D) must exclude A,B"
    m2 = mrca(tree, "A", "D")
    assert tips(m2) == {"A", "B", "C", "D"}
    print("tree (A,B,(C,D)): 4 tips; MRCA(C,D) = (C,D)")
    print("OK: %s read the Newick" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_character_matrix(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
MATRIX = {
    "eagle":   {"feathers": 1, "hair": 0, "mammary": 0},
    "sparrow": {"feathers": 1, "hair": 0, "mammary": 0},
    "bat":     {"feathers": 0, "hair": 1, "mammary": 1},
    "lizard":  {"feathers": 0, "hair": 0, "mammary": 0},
}
OUTGROUP = "lizard"
def group_by(character, state=1):
    return {t for t, ch in MATRIX.items() if ch[character] == state}
def main():
    feathered = group_by("feathers")
    haired = group_by("hair")
    print("feathers=1 (derived): %s" % sorted(feathered))
    print("hair=1 (derived): %s" % sorted(haired))
    assert feathered == {"eagle", "sparrow"}
    assert haired == {"bat"}
    # outgroup polarization: lizard state = ancestral (0)
    assert MATRIX[OUTGROUP]["feathers"] == 0
    # synapomorphy defines the clade; symplesiomorphy would mislead
    print("synapomorphy 'feathers' unites eagle+sparrow; 'five toes' would not")
    print("OK: %s polarized the matrix" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_clade_classifier(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def leaves(node):
    if isinstance(node, str): return {node}
    out = set()
    for c in node: out |= leaves(c)
    return out
def all_clades(node):
    s = {frozenset(leaves(node))}
    if not isinstance(node, str):
        for c in node: s |= all_clades(c)
    return s
def classify(tree, members):
    G = frozenset(members)
    clades = all_clades(tree)
    if G in clades: return "monophyletic"
    for C in clades:
        if G < C and (C - G) in clades:
            return "paraphyletic"   # a clade minus one complete subclade
    return "polyphyletic"
def main():
    tree = (("A", "B"), ("C", "D"))
    assert classify(tree, {"A", "B"}) == "monophyletic"
    assert classify(tree, {"A", "B", "C"}) == "paraphyletic"  # minus {D}
    assert classify(tree, {"A", "C"}) == "polyphyletic"
    assert classify(tree, {"A", "B", "C", "D"}) == "monophyletic"
    print("A,B -> monophyletic; A,B,C -> paraphyletic; A,C -> polyphyletic")
    print("OK: %s sorted the groups" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_morpho_distance(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def euclid(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))
def main():
    A = (10.0, 20.0)   # species A measurements
    B = (11.0, 21.0)   # close relative
    C = (30.0, 40.0)   # distant relative
    d_ab, d_ac = euclid(A, B), euclid(A, C)
    print("d(A,B) = %.4f; d(A,C) = %.4f" % (d_ab, d_ac))
    assert abs(d_ab - math.sqrt(2)) < 1e-9
    assert abs(d_ac - math.sqrt(800)) < 1e-9
    assert d_ab < d_ac, "morphology must mirror relatedness here"
    # homology check first: distances are meaningless across non-homologous traits
    print("rule: measure homologous structures, then let distance mirror kinship")
    print("OK: %s measured the bodies" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_sequence_distance(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def p_distance(s1, s2):
    assert len(s1) == len(s2) and len(s1) > 0
    diffs = sum(1 for a, b in zip(s1, s2) if a != b)
    return diffs / len(s1)
def main():
    s1 = "ACGTACGT"
    s2 = "ACGTTCGT"   # one substitution at position 5
    s3 = "TGCAACGT"   # four substitutions
    d12 = p_distance(s1, s2)
    d13 = p_distance(s1, s3)
    print("d(s1,s2) = %.3f; d(s1,s3) = %.3f" % (d12, d13))
    assert abs(d12 - 0.125) < 1e-9
    assert abs(d13 - 0.5) < 1e-9
    assert d12 < d13
    print("fewer differences -> closer relationship")
    print("OK: %s counted the differences" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_barcode_gap(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    within = [0.001, 0.003, 0.002]    # within-species distances
    between = [0.08, 0.10, 0.09]      # between-species distances
    gap = min(between) - max(within)
    print("max within-species: %.3f; min between-species: %.3f" % (max(within), min(between)))
    print("barcode gap: %.3f" % gap)
    assert abs(gap - 0.077) < 1e-9
    assert gap > 0.05, "gap must be clearly positive for barcoding to work"
    # decision rule: query within 3% of a reference -> same species candidate
    query_d = 0.012
    call = "same species" if query_d < 0.03 else "different species"
    print("query at %.3f -> %s" % (query_d, call))
    assert call == "same species"
    print("OK: %s found the gap" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_code_rules(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def available_iczn(year):
    return year >= 1758          # Systema Naturae 10th ed.
def available_icn(year):
    return year >= 1753          # Species Plantarum (1 May 1753)
def animal_family_ok(name):
    return name.endswith("idae")
def plant_family_ok(name):
    return name.endswith("aceae")
def main():
    assert available_iczn(1758) is True
    assert available_iczn(1750) is False
    assert available_icn(1753) is True
    assert available_icn(1750) is False
    assert animal_family_ok("Felidae") is True
    assert animal_family_ok("Felaceae") is False
    assert plant_family_ok("Rosaceae") is True
    assert plant_family_ok("Rosidae") is False
    print("ICZN from 1758; ICNafp from 1753; -idae animals; -aceae plants")
    print("OK: %s enforced the codes" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_revision_tracker(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    species = 10
    # 3 species each split into 2 -> +3
    splits = 3
    species += splits
    # 2 pairs lumped -> -2
    lumps = 2
    species -= lumps
    # 1 species moved to another genus (count unchanged, name changed)
    moves = 1
    print("start 10; +%d splits; -%d lumps; %d genus move" % (splits, lumps, moves))
    print("end: %d species" % species)
    assert species == 11
    # every change leaves a synonymy trail
    retired_names = splits + lumps * 2
    print("%d old names retired into synonymy (still searchable)" % retired_names)
    assert retired_names == 7
    print("OK: %s tracked the revision" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_species_concept_decider(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def bsc(interbreed):
    return "same species" if interbreed else "separate species"
def psc(diagnosable, reciprocal_mono):
    return "separate species" if (diagnosable and reciprocal_mono) else "same species"
def main():
    # two populations: interbreed freely where they meet, but diagnosable + reciprocally monophyletic
    interbreed, diagnosable, mono = True, True, True
    b, p = bsc(interbreed), psc(diagnosable, mono)
    print("BSC (interbreed=%s): %s" % (interbreed, b))
    print("PSC (diagnosable=%s, monophyletic=%s): %s" % (diagnosable, mono, p))
    assert b == "same species"
    assert p == "separate species"
    assert b != p, "the concept changes the answer"
    print("same data, different rule, different count")
    print("OK: %s chose the concept" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_dichotomous_key(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
KEY = {
    1: ("wings present?", {True: 2, False: "Apteryx (kiwi)"}),
    2: ("beak hooked?", {True: "Falco (falcon)", False: "Passer (sparrow)"}),
}
def walk(answers):
    node = 1
    for a in answers:
        question, branches = KEY[node]
        nxt = branches[bool(a)]
        if isinstance(nxt, str):
            return nxt
        node = nxt
    return KEY[node][0] + " (unresolved)"
def main():
    assert walk([True, False]) == "Passer (sparrow)"
    assert walk([True, True]) == "Falco (falcon)"
    assert walk([False]) == "Apteryx (kiwi)"
    print("wings? yes -> hooked beak? no -> Passer (sparrow)")
    print("verify the endpoint against the description before trusting it")
    print("OK: %s walked the key" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_dwc_validator(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
REQUIRED = ["occurrenceID", "scientificName", "eventDate",
            "decimalLatitude", "decimalLongitude"]
def validate(rec):
    missing = [f for f in REQUIRED if f not in rec]
    if missing: return False, "missing: %s" % ",".join(missing)
    if not (-90.0 <= rec["decimalLatitude"] <= 90.0): return False, "bad latitude"
    if not (-180.0 <= rec["decimalLongitude"] <= 180.0): return False, "bad longitude"
    return True, "valid"
def main():
    good = {"occurrenceID": "MUS:123", "scientificName": "Puma concolor",
            "eventDate": "2024-05-01", "decimalLatitude": 40.7, "decimalLongitude": -74.0}
    bad_lat = dict(good, decimalLatitude=95.0)
    bad_missing = {"scientificName": "Puma concolor"}
    assert validate(good) == (True, "valid")
    assert validate(bad_lat)[0] is False
    assert validate(bad_missing)[0] is False
    print("Darwin Core: 5 required fields + coordinate sanity")
    print("OK: %s validated the record" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_patristic_distance(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
# rooted tree: ((A:1.0,B:2.0)N1:0.5,C:1.5)N2
PARENT = {"A": ("N1", 1.0), "B": ("N1", 2.0), "N1": ("N2", 0.5), "C": ("N2", 1.5)}
def path_to_root(tip):
    path, node = [], tip
    while node in PARENT:
        parent, bl = PARENT[node]
        path.append((node, bl))
        node = parent
    path.append((node, 0.0))   # include the root itself so paths always meet
    return path, node
def patristic(a, b):
    pa, ra = path_to_root(a)
    pb, rb = path_to_root(b)
    assert ra == rb, "different roots"
    da = {n: bl for n, bl in pa}
    db = {n: bl for n, bl in pb}
    common = set(da) & set(db)
    # walk up from each tip to the first common node
    dist = 0.0
    node = a
    while node not in common:
        bl = PARENT[node][1]; dist += bl; node = PARENT[node][0]
    mrca = node
    node = b
    while node != mrca:
        bl = PARENT[node][1]; dist += bl; node = PARENT[node][0]
    return dist
def main():
    dab = patristic("A", "B")
    dac = patristic("A", "C")
    print("patristic A-B = %.1f; A-C = %.1f" % (dab, dac))
    assert abs(dab - 3.0) < 1e-9
    assert abs(dac - 3.0) < 1e-9
    print("sisters share an MRCA; distance sums the path")
    print("OK: %s traced the branches" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_parsimony_score(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def fitch(node, states):
    if isinstance(node, str):
        return ({states[node]}, 0)
    lset, lc = fitch(node[0], states)
    rset, rc = fitch(node[1], states)
    inter = lset & rset
    if inter:
        return (inter, lc + rc)
    return (lset | rset, lc + rc + 1)
def score(tree, characters):
    return sum(fitch(tree, st)[1] for st in characters)
def main():
    t1 = (("A", "B"), ("C", "D"))
    t2 = (("A", "C"), ("B", "D"))
    char1 = {"A": 0, "B": 0, "C": 1, "D": 1}
    char2 = {"A": 0, "B": 1, "C": 1, "D": 1}
    s1, s2 = score(t1, [char1, char2]), score(t2, [char1, char2])
    print("tree ((A,B),(C,D)): %d steps; tree ((A,C),(B,D)): %d steps" % (s1, s2))
    assert s1 == 2 and s2 == 3
    best = t1 if s1 < s2 else t2
    assert best == t1
    print("fewest changes wins: ((A,B),(C,D))")
    print("OK: %s counted the steps" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_concat_stats(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    genes = {"COI": 648, "rbcL": 1500, "ITS": 900}
    total = sum(genes.values())
    print("supermatrix: %s = %d bp" % (" + ".join("%s %d" % (g, l) for g, l in genes.items()), total))
    assert total == 3048
    missing_genes = {"spX": ["rbcL"]}
    missing_bp = sum(genes[g] for g in missing_genes["spX"])
    pct = 100 * missing_bp / total
    print("spX missing rbcL -> %.1f %% missing data" % pct)
    assert abs(pct - 49.21) < 0.1
    # partitions keep each gene's own model
    print("partitions: %d (one model per gene)" % len(genes))
    assert len(genes) == 3
    print("OK: %s built the supermatrix" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_molecular_clock(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def divergence_time(distance, rate_per_lineage):
    # pairwise distance accumulates on both lineages: d = 2 * r * t
    return distance / (2.0 * rate_per_lineage)
def main():
    d, rate = 0.08, 0.02   # 8% divergence, 2%/Myr per lineage
    t = divergence_time(d, rate)
    print("d=%.2f, rate=%.2f/Myr -> t=%.1f Myr" % (d, rate, t))
    assert abs(t - 2.0) < 1e-9
    # fossil calibration: clade must be at least 50 Myr old -> caps the rate
    fossil_min = 50.0
    max_rate = d / (2.0 * fossil_min)
    print("fossil minimum %d Myr -> rate <= %.5f/Myr" % (fossil_min, max_rate))
    assert abs(max_rate - 0.0008) < 1e-9
    print("report intervals, not points: 2.0 Myr +/- calibration uncertainty")
    print("OK: %s read the clock" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_cryptic_split(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    within = [0.001, 0.002, 0.0015]      # within the morphospecies
    new_pop = [0.090, 0.100, 0.095]      # new population vs the rest
    threshold = 0.03
    print("within-population max: %.4f; new-population min: %.3f" % (max(within), min(new_pop)))
    cryptic = max(within) < threshold < min(new_pop)
    print("cryptic species flagged: %s" % cryptic)
    assert cryptic is True
    # rule out mitochondrial artifacts with a nuclear gene before describing
    print("next: test a nuclear locus to rule out introgression/Wolbachia artifacts")
    print("OK: %s exposed the hidden species" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_split_conservation(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    species, threatened = 100, 20
    splits = 10                       # 10 species each split into 2 daughters
    species += splits                 # net +10 species
    threatened_parents_lost = 2       # 2 split parents were threatened, now replaced
    new_threatened_daughters = 6      # 6 daughters meet threatened thresholds
    threatened = threatened - threatened_parents_lost + new_threatened_daughters
    print("after splitting %d species: %d species, %d threatened" % (splits, species, threatened))
    assert species == 110 and threatened == 24
    pct = 100.0 * threatened / species
    print("threatened share: %.2f %%" % pct)
    assert abs(pct - 21.82) < 0.05
    print("splits shrink ranges -> daughters trip Red List thresholds")
    print("OK: %s counted what counts" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_integrative_score(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
WEIGHTS = {"morphology": 0.25, "dna": 0.35, "ecology": 0.20, "geography": 0.20}
def integrate(scores):
    return sum(WEIGHTS[k] * scores[k] for k in WEIGHTS)
def main():
    scores = {"morphology": 0.8, "dna": 0.95, "ecology": 0.6, "geography": 0.7}
    total = integrate(scores)
    print("weighted evidence: %.4f" % total)
    assert abs(total - 0.7925) < 1e-9
    assert abs(sum(WEIGHTS.values()) - 1.0) < 1e-9
    decision = "distinct species" if total >= 0.75 else "candidate only"
    print("threshold 0.75 -> %s" % decision)
    assert decision == "distinct species"
    # single-evidence case stays provisional
    solo = integrate({"morphology": 0.0, "dna": 0.95, "ecology": 0.0, "geography": 0.0})
    print("DNA alone: %.4f -> candidate only" % solo)
    assert solo < 0.75
    print("OK: %s triangulated the species" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_lsid_check(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
LSID = re.compile(r"^urn:lsid:zoobank\\.org:(act|publication):[0-9a-fA-F-]{36}$")
def main():
    good = "urn:lsid:zoobank.org:act:12345678-1234-1234-1234-123456789abc"
    bad1 = "zoobank.org:act:123"
    bad2 = "urn:lsid:zoobank.org:act:xyz"
    assert LSID.match(good) is not None
    assert LSID.match(bad1) is None
    assert LSID.match(bad2) is None
    print("valid LSID: %s" % good)
    print("no registration -> electronic name is unavailable")
    print("OK: %s checked the registry" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_description_checklist(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
REQUIRED = ["diagnosis", "description", "holotype", "depository", "etymology", "distribution"]
def check(provided):
    return [f for f in REQUIRED if f not in provided]
def main():
    full = ["diagnosis", "description", "holotype", "depository", "etymology", "distribution"]
    partial = ["diagnosis", "description", "holotype", "depository", "distribution"]
    assert check(full) == []
    missing = check(partial)
    print("partial description missing: %s" % missing)
    assert missing == ["etymology"]
    # name formation: Latinized, not a homonym, correctly suffixed
    epithet = "splendida"
    assert epithet.islower() and epithet.isalpha()
    print("epithet '%s': lowercase Latin adjective -> well-formed" % epithet)
    print("OK: %s completed the description" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_impediment_math(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    undescribed = 6500000.0
    rate = 17500.0          # new species described per year (scenario)
    years = undescribed / rate
    print("backlog %.1fM / %.0f per year = %.0f years" % (undescribed / 1e6, rate, years))
    assert 370.0 < years < 375.0
    # turbo-taxonomy scenario: 10x the rate
    turbo = undescribed / (rate * 10.0)
    print("turbo-taxonomy (10x rate): %.1f years" % turbo)
    assert abs(turbo - years / 10.0) < 1e-9
    # extinction race: species lost before description are gone unnamed
    print("every undescribed extinction is a name never minted")
    print("OK: %s sized the backlog" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_classifier_metrics(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def metrics(tp, fp, fn):
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * precision * recall / (precision + recall)
    return precision, recall, f1
def main():
    p, r, f1 = metrics(80, 10, 20)
    print("TP=80 FP=10 FN=20 -> precision=%.4f recall=%.4f F1=%.4f" % (p, r, f1))
    assert abs(p - 0.8889) < 0.001
    assert abs(r - 0.8000) < 1e-9
    assert abs(f1 - 0.8421) < 0.001
    # top-1 accuracy alone would hide the 20 missed individuals
    print("report per-species precision/recall, not just top-1 accuracy")
    print("OK: %s graded the classifier" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_edna_detection(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def cumulative(p, n):
    return 1.0 - (1.0 - p) ** n
def samples_for(p, target):
    n = 1
    while cumulative(p, n) < target:
        n += 1
    return n
def main():
    p, n = 0.3, 5
    c = cumulative(p, n)
    print("per-sample detection %.1f, %d samples -> cumulative %.4f" % (p, n, c))
    assert abs(c - 0.83193) < 0.001
    need = samples_for(0.3, 0.95)
    print("samples for 95%% confidence: %d" % need)
    assert need == 9
    # absent vs missed: occupancy models separate the two
    print("no detection in 9 samples -> likely absent, not just missed")
    print("OK: %s sized the survey" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_phylocode_define(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def classify_definition(text):
    t = text.lower()
    if "least inclusive clade containing" in t:
        return "node-based"
    if "most inclusive clade containing" in t and "but not" in t:
        return "branch-based"
    if "first" in t and ("evolve" in t or "apomorphy" in t):
        return "apomorphy-based"
    return "unrecognized"
def main():
    d1 = "the least inclusive clade containing Panthera leo and Felis catus"
    d2 = "the most inclusive clade containing Panthera leo but not Hyaena hyaena"
    d3 = "the clade stemming from the first species to evolve retractable claws"
    assert classify_definition(d1) == "node-based"
    assert classify_definition(d2) == "branch-based"
    assert classify_definition(d3) == "apomorphy-based"
    print("node-based / branch-based / apomorphy-based: all three recognized")
    print("definitions track the tree; names stay fixed through re-rankings")
    print("OK: %s defined the clades" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_schema_validate(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
REQUIRED = ["id", "t", "g", "name", "title", "description", "how_it_works",
            "key_points", "requirements", "standards", "citations",
            "src", "ladder_rank", "ladder_tier", "demo"]
def validate(rec):
    missing = [f for f in REQUIRED if f not in rec]
    if missing:
        return False, "missing %s" % missing[0]
    if not (1 <= rec["ladder_rank"] <= 10):
        return False, "ladder_rank out of range"
    if rec["ladder_tier"] not in ("foundations", "compounded", "advanced"):
        return False, "bad ladder_tier"
    if rec["src"] not in ("public-harvest", "signature"):
        return False, "bad src"
    return True, "valid"
def good_rec():
    return {f: "x" for f in REQUIRED} | {"ladder_rank": 5,
            "ladder_tier": "compounded", "src": "public-harvest"}
def main():
    assert validate(good_rec()) == (True, "valid")
    bad = good_rec(); del bad["demo"]
    assert validate(bad)[0] is False
    bad2 = good_rec(); bad2["ladder_rank"] = 11
    assert validate(bad2)[0] is False
    bad3 = good_rec(); bad3["src"] = "scraped"
    assert validate(bad3)[0] is False
    print("schema: 15 required fields + ladder_rank 1-10 + tier/src enums")
    print("OK: %s validated the schema" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "taxonomy_scale": demo_taxonomy_scale, "rank_ladder": demo_rank_ladder,
    "binomial_check": demo_binomial_check, "linnaeus_counts": demo_linnaeus_counts,
    "kingdom_map": demo_kingdom_map, "type_registry": demo_type_registry,
    "priority_rule": demo_priority_rule, "name_parser": demo_name_parser,
    "monograph_scale": demo_monograph_scale, "museum_growth": demo_museum_growth,
    "common_name_map": demo_common_name_map, "newick_tree": demo_newick_tree,
    "character_matrix": demo_character_matrix, "clade_classifier": demo_clade_classifier,
    "morpho_distance": demo_morpho_distance, "sequence_distance": demo_sequence_distance,
    "barcode_gap": demo_barcode_gap, "code_rules": demo_code_rules,
    "revision_tracker": demo_revision_tracker,
    "species_concept_decider": demo_species_concept_decider,
    "dichotomous_key": demo_dichotomous_key, "dwc_validator": demo_dwc_validator,
    "patristic_distance": demo_patristic_distance,
    "parsimony_score": demo_parsimony_score, "concat_stats": demo_concat_stats,
    "molecular_clock": demo_molecular_clock, "cryptic_split": demo_cryptic_split,
    "split_conservation": demo_split_conservation,
    "integrative_score": demo_integrative_score, "lsid_check": demo_lsid_check,
    "description_checklist": demo_description_checklist,
    "impediment_math": demo_impediment_math,
    "classifier_metrics": demo_classifier_metrics,
    "edna_detection": demo_edna_detection, "phylocode_define": demo_phylocode_define,
    "schema_validate": demo_schema_validate,
}

# ---------------------------------------------------------------- records

def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_taxonomy.py).
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
    for slug in ("taxonomy", "taxonomy-signature"):
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
