#!/usr/bin/env python3
"""PHASE L — catalog pastes 1-4 (400 entries, master index to 500).

Cross-check: 14 entries file as full canon records into 15 existing
covering databases (oral-histories-public, scientific-instruments-public,
algorithms, anatomy, signature-math-discoveries, volcanoes,
public-dream-records, cryptocurrency, sign-language, public-cartography,
pharma-drugs, terraforming, space-elevator, antimatter).

New: 70 databases grouped by the pastes' domain groups — 30
public+signature pairs for pastes 1-3 (public = fact-checked real records,
src=public-harvest; signature = his original catalog designs,
src=signature, " (Signature Edition)" titles) and 10 signature-only
databases for paste 4 (ultra-advanced/cosmic, Signature-original, clearly
labeled).

Whole-system dedupe via code/dedupe_gate.py. Canon page/chunk/index
pattern from code/phone-compound-build. No website references, no
Facebook, no banned phrases. Safety: scholarly/factual tone; defensive or
descriptive documentation only — no weapons content, no operational
tradecraft, no medical advice.
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

sys.path.insert(0, os.path.join(HERE))
sys.path.insert(0, os.path.join(REPO, "code"))
from entries_l import ENTRIES, PUB
import build as B

GATE = B.GATE
GROUP = "catalog-pastes"

# ============================================================ new DB config
# (cat, slug, name, tagline, record_kind, prefix, ai_name, role, citation, sig_only)

NEWCATS = [
    # ---- Paste 1 ----
    ("biodiv", "biological-diversity-databases",
     "The Biological Diversity and Ecology Databases Database",
     "Database catalogs for life on Earth: endangered species, pollinators, forests, microbiomes, and reefs.",
     "biodiversity catalog record", "JAH-BIOD-", "JAH Biodiversity Catalog Archivist",
     "biodiversity catalog archivist — species and ecosystem catalogs",
     "Conservation biology (standard IUCN and ecological literature).", False),
    ("earthsci", "earth-sciences-databases",
     "The Earth Sciences and Planetary Health Databases Database",
     "Database catalogs for the living planet: glaciers, aquifers, volcanoes, climate, soils, and seismic systems.",
     "earth science catalog record", "JAH-EARS-", "JAH Earth Sciences Catalog Archivist",
     "earth sciences catalog archivist — planetary health catalogs",
     "Earth science (standard geological and climate literature).", False),
    ("culther", "cultural-heritage-databases",
     "The Cultural Heritage, Language and Arts Databases Database",
     "Database catalogs for human culture: languages, crafts, music, monuments, texts, film, food, and textiles.",
     "cultural heritage catalog record", "JAH-CULH-", "JAH Cultural Heritage Catalog Archivist",
     "cultural heritage catalog archivist — language and arts catalogs",
     "Cultural heritage (standard UNESCO and ethnographic literature).", False),
    ("scimath", "science-math-tech-databases",
     "The Science, Mathematics and Technology Databases Database",
     "Database catalogs for knowledge itself: constants, elements, hardware, units, medicines, and energy.",
     "science catalog record", "JAH-SMT-", "JAH Science Catalog Archivist",
     "science catalog archivist — math and technology catalogs",
     "Science and metrology (standard scientific literature).", False),
    ("spacecos", "space-cosmology-databases",
     "The Space, Astronomy and Cosmology Databases Database",
     "Database catalogs for the universe: asteroids, exoplanets, stars, galaxies, debris, probes, and worlds.",
     "space catalog record", "JAH-SPC-", "JAH Space Catalog Archivist",
     "space catalog archivist — astronomy and cosmology catalogs",
     "Astronomy (standard astrophysical literature).", False),
    ("histconf", "history-conflict-databases",
     "The History, Conflict and Social Structure Databases Database",
     "Database catalogs for the human past: treaties, rights, money, maps, plagues, movements, wrecks, and emblems.",
     "history catalog record", "JAH-HISTC-", "JAH History Catalog Archivist",
     "history catalog archivist — conflict and society catalogs",
     "History (standard historical literature).", False),
    ("phileth", "philosophy-ethics-databases",
     "The Philosophy, Ethics and Human Thought Databases Database",
     "Database catalogs for human thought: ethics, fallacies, religions, rites, utopias, aesthetics, and justice.",
     "philosophy catalog record", "JAH-PHIL-", "JAH Philosophy Catalog Archivist",
     "philosophy catalog archivist — ethics and thought catalogs",
     "Philosophy (standard philosophical literature).", False),
    ("matcult", "material-culture-databases",
     "The Material Culture, Design and Industry Databases Database",
     "Database catalogs for made things: design milestones, materials, vehicles, packaging, type, toys, and locks.",
     "material culture catalog record", "JAH-MATC-", "JAH Material Culture Catalog Archivist",
     "material culture catalog archivist — design and industry catalogs",
     "Material culture (standard design-history literature).", False),
    ("humanexp", "human-experience-databases",
     "The Human Experience, Health and Psychology Databases Database",
     "Database catalogs for inner life: dreams, emotion, archetypes, senses, memory, grief, humor, and art.",
     "human experience catalog record", "JAH-HUMX-", "JAH Human Experience Catalog Archivist",
     "human experience catalog archivist — psychology and health catalogs",
     "Psychology (standard psychological literature).", False),
    ("ephfut", "ephemera-futures-databases",
     "The Ephemera, Futures and Speculation Databases Database",
     "Database catalogs for the fleeting and the future: time capsules, ruins, conlangs, street art, and meta-indexes.",
     "ephemera catalog record", "JAH-EPHF-", "JAH Ephemera Catalog Archivist",
     "ephemera catalog archivist — futures and speculation catalogs",
     "Future studies (standard archival and speculative literature).", False),
    # ---- Paste 2 ----
    ("deeptime", "deep-time-geodynamics-databases",
     "The Deep Time, Geodynamics and Material Science Databases Database",
     "Database catalogs for deep Earth: core samples, minerals, caves, impacts, soils, vents, and geothermal heat.",
     "deep-time catalog record", "JAH-DTG-", "JAH Deep Time Catalog Archivist",
     "deep time catalog archivist — geodynamics and materials catalogs",
     "Earth science (standard geological literature).", False),
    ("infra", "infrastructure-databases",
     "The Infrastructure, Networks and Built Environment Databases Database",
     "Database catalogs for built systems: cables, waterworks, rails, utilities, lighthouses, grids, and bridges.",
     "infrastructure catalog record", "JAH-INFR-", "JAH Infrastructure Catalog Archivist",
     "infrastructure catalog archivist — networks and built environment catalogs",
     "Infrastructure (standard engineering literature).", False),
    ("langsym", "language-symbols-databases",
     "The Language, Symbols and Information System Databases Database",
     "Database catalogs for human codes: scripts, whistled speech, ciphers, isolates, shorthand, and symbology.",
     "language catalog record", "JAH-LANG-", "JAH Language Catalog Archivist",
     "language catalog archivist — symbols and information catalogs",
     "Linguistics (standard linguistic literature).", False),
    ("mathcomp", "math-computation-databases",
     "The Mathematics, Computation and Logical System Databases Database",
     "Database catalogs for formal systems: primes, automata, complexity, geometries, codes, and game theory.",
     "mathematics catalog record", "JAH-MATHC-", "JAH Mathematics Catalog Archivist",
     "mathematics catalog archivist — computation and logic catalogs",
     "Mathematics (standard mathematical literature).", False),
    ("biogen", "biology-genetics-databases",
     "The Biology, Genetics and Medical Knowledge Databases Database",
     "Database catalogs for life's code: paleogenomes, HLA, venoms, microbiomes, vectors, and blood groups.",
     "genetics catalog record", "JAH-BIOG-", "JAH Genetics Catalog Archivist",
     "genetics catalog archivist — biology and medical catalogs",
     "Biology (standard genetic and medical literature).", False),
    ("agrifood", "agriculture-food-databases",
     "The Agriculture, Food System and Toolmaking Databases Database",
     "Database catalogs for feeding humanity: landraces, foraging, preservation, tools, breeds, dyes, and mills.",
     "agriculture catalog record", "JAH-AGRI-", "JAH Agriculture Catalog Archivist",
     "agriculture catalog archivist — food and toolmaking catalogs",
     "Agriculture (standard agronomic literature).", False),
    ("musicac", "music-acoustics-databases",
     "The Music, Acoustics and Sensory Phenomena Databases Database",
     "Database catalogs for sound and sense: hall acoustics, tunings, sky sounds, pigments, scents, and illusions.",
     "acoustics catalog record", "JAH-MUSA-", "JAH Acoustics Catalog Archivist",
     "acoustics catalog archivist — music and sensory catalogs",
     "Acoustics (standard musicological literature).", False),
    ("govecon", "governance-economics-databases",
     "The Governance, Economics and Human Organization Databases Database",
     "Database catalogs for organizing society: currencies, commons, taxes, guilds, co-ops, voting, and response.",
     "governance catalog record", "JAH-GOVE-", "JAH Governance Catalog Archivist",
     "governance catalog archivist — economics and organization catalogs",
     "Economics (standard institutional literature).", False),
    ("maravi", "maritime-aviation-databases",
     "The Maritime, Aviation and Transportation History Databases Database",
     "Database catalogs for movement: watercraft, wayfinding, aircraft, trade winds, locomotives, and logbooks.",
     "transport history catalog record", "JAH-MAVA-", "JAH Transport History Catalog Archivist",
     "transport history catalog archivist — maritime and aviation catalogs",
     "Transport history (standard nautical and aviation literature).", False),
    ("margin", "marginalia-lost-knowledge-databases",
     "The Marginalia, Micro-History and Lost Knowledge Databases Database",
     "Database catalogs for the overlooked: marginalia, mysteries, phantom islands, zines, ruins, and web relics.",
     "lost knowledge catalog record", "JAH-MARG-", "JAH Lost Knowledge Catalog Archivist",
     "lost knowledge catalog archivist — marginalia and micro-history catalogs",
     "Micro-history (standard archival literature).", False),
    # ---- Paste 3 ----
    ("submicro", "submicroscopic-phenomena-databases",
     "The Sub-Microscopic, Physical and Chemical Phenomena Databases Database",
     "Database catalogs for the very small: polymorphs, phase boundaries, superconductors, catalysts, and nanomaterials.",
     "sub-microscopic catalog record", "JAH-SUBM-", "JAH Sub-Microscopic Catalog Archivist",
     "sub-microscopic catalog archivist — physical and chemical catalogs",
     "Physics and chemistry (standard condensed-matter literature).", False),
    ("survival", "extreme-survival-databases",
     "The Extreme Survival, Wilderness and Frontier Knowledge Databases Database",
     "Database catalogs for staying alive: fire, water, fungi, shelter, knots, navigation, tracking, and triage.",
     "survival catalog record", "JAH-EXSV-", "JAH Survival Knowledge Catalog Archivist",
     "survival knowledge catalog archivist — wilderness and frontier catalogs",
     "Survival skills (standard bushcraft and wilderness literature).", False),
    ("failures", "system-failures-databases",
     "The System Failure, Safety and Forensics Databases Database",
     "Database catalogs for hard lessons: collapses, disasters, crashes, blackouts, forensics, and near-misses.",
     "failure analysis catalog record", "JAH-SYFA-", "JAH Failure Analysis Catalog Archivist",
     "failure analysis catalog archivist — safety and forensics catalogs",
     "Forensic engineering (standard failure literature).", False),
    ("crafts", "niche-crafts-databases",
     "The Niche Craft, Material Processing and Artisan Skill Databases Database",
     "Database catalogs for hand skill: glass, paper, clocks, books, smelting, stone, barrels, kilns, and baskets.",
     "craft catalog record", "JAH-NICR-", "JAH Craft Catalog Archivist",
     "craft catalog archivist — artisan skill catalogs",
     "Craft technology (standard artisan literature).", False),
    ("cognit", "cognition-learning-databases",
     "The Cognition, Learning and Psychological Framework Databases Database",
     "Database catalogs for minds: heuristics, pedagogy, consciousness, therapy, memory, and neurodiversity.",
     "cognition catalog record", "JAH-COGL-", "JAH Cognition Catalog Archivist",
     "cognition catalog archivist — learning and psychology catalogs",
     "Cognitive science (standard psychological literature).", False),
    ("biosig", "biological-signaling-databases",
     "The Biological Signaling, Communication and Sense Databases Database",
     "Database catalogs for living signals: plant chemistry, pheromones, magnetoreception, song, and quorum sensing.",
     "biological signaling catalog record", "JAH-BIOS-", "JAH Biological Signaling Catalog Archivist",
     "biological signaling catalog archivist — communication and sense catalogs",
     "Biology (standard signaling literature).", False),
    ("archtyp", "architectural-typologies-databases",
     "The Architectural Typology and Spatial Engineering Databases Database",
     "Database catalogs for built form: vernacular, acoustics, forts, trusses, vaults, alignments, and shelters.",
     "architectural catalog record", "JAH-ARCT-", "JAH Architectural Catalog Archivist",
     "architectural catalog archivist — typology and spatial catalogs",
     "Architecture (standard building literature).", False),
    ("metrol", "metrology-measurement-databases",
     "The Specialized Data, Measurement and Metrology Databases Database",
     "Database catalogs for measuring: atomic clocks, benchmarks, spectra, color, noise, hardness, and threads.",
     "metrology catalog record", "JAH-METR-", "JAH Metrology Catalog Archivist",
     "metrology catalog archivist — measurement and standards catalogs",
     "Metrology (standard measurement-science literature).", False),
    ("socrit", "sociology-rituals-databases",
     "The Sociology, Group Dynamic and Ritual Databases Database",
     "Database catalogs for groups: de-escalation, crowds, taboos, gift economies, subcultures, and councils.",
     "sociology catalog record", "JAH-SOCR-", "JAH Sociology Catalog Archivist",
     "sociology catalog archivist — group and ritual catalogs",
     "Sociology (standard sociological literature).", False),
    ("metaknow", "metaknowledge-preservation-databases",
     "The Metaknowledge, Preservation and Future Archiving Databases Database",
     "Database catalogs for memory itself: media durability, warnings, primers, vaults, schemas, and error taxonomies.",
     "metaknowledge catalog record", "JAH-METK-", "JAH Metaknowledge Catalog Archivist",
     "metaknowledge catalog archivist — preservation and archiving catalogs",
     "Archival science (standard preservation literature).", False),
    # ---- Paste 4 (signature-only) ----
    ("quantft", "quantum-field-theory-databases-signature",
     "The Quantum Field Theory Signature Database",
     "Signature-original design catalogs for frontier physics: topological qubits, Casimir effects, exotic matter, QCD phases, and Hawking radiation. Theoretical documentation, clearly labeled.",
     "quantum frontier catalog record", "JAH-QFTG-", "JAH Quantum Frontier Catalog Archivist (Signature)",
     "quantum frontier catalog archivist — signature theoretical physics catalogs",
     "Theoretical physics (standard literature). Signature-original designs.", True),
    ("postbio", "postbiological-cognition-databases-signature",
     "The Post-Biological Cognition Signature Database",
     "Signature-original design catalogs for mind futures: connectomes, mind-transfer validation, qualia, brain-to-brain protocols, and AGI alignment. Theoretical documentation, clearly labeled.",
     "post-biological cognition catalog record", "JAH-PBCG-", "JAH Post-Biological Cognition Archivist (Signature)",
     "post-biological cognition archivist — signature mind-future catalogs",
     "Consciousness and AI safety (standard literature). Signature-original designs.", True),
    ("astroeng", "astroengineering-megastructures-databases-signature",
     "The Astroengineering and Megastructures Signature Database",
     "Signature-original design catalogs for cosmic engineering: Dyson swarms, stellar lifting, Matrioshka brains, habitats, sails, and beacons. Theoretical documentation, clearly labeled.",
     "astroengineering catalog record", "JAH-ASTMG-", "JAH Astroengineering Catalog Archivist (Signature)",
     "astroengineering catalog archivist — signature megastructure catalogs",
     "Astroengineering (standard speculative literature). Signature-original designs.", True),
    ("synbio", "synthetic-biology-nanotech-databases-signature",
     "The Synthetic Biology and Nanotech Signature Database",
     "Signature-original design catalogs for engineered life: molecular assemblers, XNA, de novo proteins, nanobots, gene drives, and DNA storage. Theoretical documentation, clearly labeled.",
     "synthetic biology catalog record", "JAH-SBNG-", "JAH Synthetic Biology Catalog Archivist (Signature)",
     "synthetic biology catalog archivist — signature bioengineering catalogs",
     "Synthetic biology (standard literature). Signature-original designs.", True),
    ("advcomp", "advanced-computation-databases-signature",
     "The Advanced Computation Signature Database",
     "Signature-original design catalogs for future computing: reversible logic, photonic chips, neuromorphic hardware, self-rewriting verifiers, and spacetime simulation. Theoretical documentation, clearly labeled.",
     "advanced computation catalog record", "JAH-ADVCG-", "JAH Advanced Computation Archivist (Signature)",
     "advanced computation catalog archivist — signature computing catalogs",
     "Computer architecture (standard literature). Signature-original designs.", True),
    ("deepspace", "deep-space-navigation-databases-signature",
     "The Deep Space Navigation Signature Database",
     "Signature-original design catalogs for navigating the void: pulsar grids, gravitational lenses, biosignatures, dust erosion, and ocean-world drills. Theoretical documentation, clearly labeled.",
     "deep-space navigation catalog record", "JAH-DSNG-", "JAH Deep Space Navigation Archivist (Signature)",
     "deep space navigation archivist — signature navigation catalogs",
     "Space navigation (standard literature). Signature-original designs.", True),
    ("postscar", "postscarcity-economics-databases-signature",
     "The Post-Scarcity Economics Signature Database",
     "Signature-original design catalogs for abundance economics: zero-g refining, closed-loop life support, sequestration, transmutation, and automated supply webs. Theoretical documentation, clearly labeled.",
     "post-scarcity economics catalog record", "JAH-PSCG-", "JAH Post-Scarcity Economics Archivist (Signature)",
     "post-scarcity economics archivist — signature abundance catalogs",
     "Economics and life support (standard literature). Signature-original designs.", True),
    ("metaphys", "metaphysics-ontology-databases-signature",
     "The Metaphysics and Ontology Signature Database",
     "Signature-original design catalogs for ultimate questions: holographic bounds, causal loops, Solomonoff limits, IIT, fine-tuning, and simulation signatures. Theoretical documentation, clearly labeled.",
     "metaphysics catalog record", "JAH-METPG-", "JAH Metaphysics Catalog Archivist (Signature)",
     "metaphysics catalog archivist — signature ontology catalogs",
     "Philosophy of physics (standard literature). Signature-original designs.", True),
    ("cosmicth", "cosmic-threats-defense-databases-signature",
     "The Cosmic Threats and Planetary Defense Signature Database",
     "Signature-original design catalogs for cosmic risk: deflection, super-flares, GRBs, vacuum decay, Kessler clearing, and pandemic countermeasures. Defensive documentation, clearly labeled.",
     "cosmic threat catalog record", "JAH-CTDG-", "JAH Cosmic Threat Catalog Archivist (Signature)",
     "cosmic threat catalog archivist — signature planetary defense catalogs",
     "Planetary defense (standard literature). Signature-original defensive designs.", True),
    ("deeptime2", "deeptime-archiving-databases-signature",
     "The Deep-Time Archiving Signature Database",
     "Signature-original design catalogs for eternity: nuclear clocks, first-contact primers, granite vaults, beacons, genetic re-boot packages, and the Grand Unified Catalog. Theoretical documentation, clearly labeled.",
     "deep-time archiving catalog record", "JAH-DTAG-", "JAH Deep-Time Archiving Catalog Archivist (Signature)",
     "deep-time archiving catalog archivist — signature legacy catalogs",
     "Archival science (standard literature). Signature-original designs.", True),
]

SIG_PREFIX = {
    "biodiv": "JAH-BIODG-", "earthsci": "JAH-EARSG-", "culther": "JAH-CULHG-",
    "scimath": "JAH-SMTG-", "spacecos": "JAH-SPCG-", "histconf": "JAH-HISTCG-",
    "phileth": "JAH-PHILG-", "matcult": "JAH-MATCG-", "humanexp": "JAH-HUMXG-",
    "ephfut": "JAH-EPHFG-", "deeptime": "JAH-DTGG-", "infra": "JAH-INFRG-",
    "langsym": "JAH-LANGG-", "mathcomp": "JAH-MATHCG-", "biogen": "JAH-BIOGG-",
    "agrifood": "JAH-AGRIG-", "musicac": "JAH-MUSAG-", "govecon": "JAH-GOVEG-",
    "maravi": "JAH-MAVAG-", "margin": "JAH-MARGG-", "submicro": "JAH-SUBMG-",
    "survival": "JAH-EXSVG-", "failures": "JAH-SYFAG-", "crafts": "JAH-NICRG-",
    "cognit": "JAH-COGLG-", "biosig": "JAH-BIOSG-", "archtyp": "JAH-ARCTG-",
    "metrol": "JAH-METRG-", "socrit": "JAH-SOCRG-", "metaknow": "JAH-METKG-",
}


def _cfg(cat, slug, name, tagline, record_kind, prefix, ai, role, citation,
         source, sig_only=False):
    sig = source == "signature"
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": ("%s — %s Every record carries the full entry: description, how it works, "
                   "key points, requirements, standards, citations, and a working demonstration program."
                   % (tagline,
                      "Signature originals — original Signature catalog designs."
                      if sig else
                      "Public records — real-world catalogs documented factually.")),
        "sig_type": ("Signature originals organized in the Signature system"
                     if sig else "Public records organized in the Signature system"),
        "search_ph": "Search %s..." % record_kind,
        "chat_ph": "Ask about %s..." % record_kind,
        "archive_blurb": "Seeded %s %s, marching toward one million records." % (
            "Signature-original" if sig else "public-record", record_kind),
        "schema": "id, t, g, name, title, description, how_it_works, key_points, requirements, standards, citations, src, demo",
        "fields": "catalog-paste archives",
        "gen_desc": ("Generate clearly-labeled structural sample records. Seeded archive records are the authoritative entries."),
        "greet": "I am the %s. Ask me about %s." % (ai, record_kind),
        "gen_fields": ["catalog-paste archives"], "gen_kind": slug,
        "gen_demo_kind": "python", "source": source,
    }


DBCFG = {}
CIT = {}
for (cat, slug, name, tagline, rk, prefix, ai, role, citation, sig_only) in NEWCATS:
    if sig_only:
        DBCFG[slug] = _cfg(cat, slug, name, tagline, rk, prefix, ai, role,
                           citation, "signature", sig_only=True)
        CIT[slug] = citation
    else:
        DBCFG[slug] = _cfg(cat, slug, name, tagline, rk, prefix, ai, role,
                           citation, "public")
        CIT[slug] = citation
        sslug = slug + "-signature"
        DBCFG[sslug] = _cfg(cat, sslug,
                            name.replace(" Databases Database",
                                         " Signature Databases Database"),
                            tagline, rk, SIG_PREFIX[cat], ai + " (Signature)",
                            role + " — Signature editions", citation,
                            "signature")
        CIT[sslug] = citation + " Signature editions are original Signature catalog designs."

SIG_ONLY_CATS = {cat for (cat, _s, _n, _t, _rk, _p, _a, _r, _c, so) in NEWCATS if so}

# filed entries written as Signature originals (speculative/cosmic topics +
# the math-proofs record filed into his Signature math discoveries DB)
SIG_FILED_KEYS = {"math-proofs", "terraforming", "space-elevator", "antimatter"}


def filed_src(key, cat):
    return "signature" if key in SIG_FILED_KEYS else "public-harvest"


# ============================================================ filing

def file_records():
    manifest = json.load(open(os.path.join(REPO, "data", "manifest.json")))
    api = json.load(open(os.path.join(REPO, "api.json")))
    m_idx = {d["slug"]: d for d in manifest["databases"]}
    a_idx = {d["slug"]: d for d in api["databases"]}
    filed = []
    progs = []
    for (key, cat, title, desc, points, req, standards, citations, demo_kind,
         target) in ENTRIES:
        if not target:
            continue
        src = filed_src(key, cat)
        ftitle = title + " (Signature Edition)" if src == "signature" else title
        if [h for h in GATE.check(target, ftitle) if h[0] != target]:
            print("  gate refused (cross-db dupe): %s" % ftitle, flush=True)
            continue
        entry = m_idx[target]
        prefix = entry["id_prefix"]
        try:
            root = B.shard_root_for(target, entry)
        except ValueError:
            root = os.path.join(REPO, "data", target)
        idx_path = os.path.join(root, "index.jsonl.gz")
        rows = B.gz_jsonl_rows(idx_path)
        if any(r.get("t") == ftitle for r in rows):
            print("  skip (already filed): %s -> %s" % (ftitle, target), flush=True)
            continue
        rid = B.next_id(prefix, rows[-1]["id"])
        rec = B.build_record(title, title, GROUP, desc, points, req, standards,
                             citations, src, demo_kind, rid)
        assert rec["t"] == ftitle, "title mismatch %r vs %r" % (rec["t"], ftitle)
        B.check_record(rec)
        light = {"id": rid, "t": rec["t"], "g": GROUP}
        for k in rows[-1]:
            if k not in light:
                light[k] = rows[-1][k]
        page = os.path.join(REPO, "db", target, "index.html")
        html = open(page, encoding="utf-8").read() if os.path.exists(page) else ""
        chunks_dir = os.path.join(root, "chunks")
        chunk_files = sorted(f for f in os.listdir(chunks_dir) if f.endswith(".jsonl.gz"))
        if "Math.floor(idx/100)" in html:
            chunk_no = len(rows) // 100
            cname = "chunk-%04d.jsonl.gz" % chunk_no
            cpath = os.path.join(chunks_dir, cname)
            crows = B.gz_jsonl_rows(cpath) if os.path.exists(cpath) else []
            if len(crows) >= 100:
                chunk_no += 1
                cname = "chunk-%04d.jsonl.gz" % chunk_no
                cpath = os.path.join(chunks_dir, cname)
                crows = []
            if "c" in light:
                del light["c"]
        else:
            def cnum(fn):
                mm = re.search(r"chunk-(\d+)\.jsonl\.gz", fn)
                return int(mm.group(1)) if mm else 0
            nums = [cnum(f) for f in chunk_files]
            last_no = max(nums)
            cpath = os.path.join(chunks_dir, "chunk-%04d.jsonl.gz" % last_no)
            crows = B.gz_jsonl_rows(cpath)
            if len(crows) >= 100:
                last_no += 1
                cpath = os.path.join(chunks_dir, "chunk-%04d.jsonl.gz" % last_no)
                crows = []
            light["c"] = last_no
        crows.append(rec)
        B.write_gz_jsonl(cpath, crows)
        rows.append(light)
        B.write_gz_jsonl(idx_path, rows)
        entry["record_count"] = entry.get("record_count", 0) + 1
        if target in a_idx:
            a_idx[target]["record_count"] = a_idx[target].get("record_count", 0) + 1
        GATE.admit(target, ftitle, rid)
        filed.append((target, rid, ftitle))
        progs.append((rid, rec["demo"]["program"]))
        print("  filed %-44s %s -> %s" % (ftitle[:44], target, rid), flush=True)
    with open(os.path.join(REPO, "data", "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=1, ensure_ascii=False)
        f.write("\n")
    with open(os.path.join(REPO, "api.json"), "w", encoding="utf-8") as f:
        json.dump(api, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("filed %d records into %d databases"
          % (len(filed), len({t for t, _, _ in filed})), flush=True)
    return filed, progs


# ============================================================ new DBs

def build_new_records():
    built = {}
    for (cat, slug, _n, _t, _rk, _p, _a, _r, _c, sig_only) in NEWCATS:
        vers = ("signature",) if sig_only else ("public", "signature")
        for ver in vers:
            s = slug if ver == "public" else (slug if sig_only else slug + "-signature")
            cfg = DBCFG[s]
            recs = []
            for (key, ecat, title, desc, points, req, standards, citations,
                 demo_kind, target) in ENTRIES:
                if ecat != cat or target:
                    continue
                if ver == "public":
                    p = PUB[key]
                    (ptitle, pdesc, ppoints, preq, pstandards, pcit, pdemo) = p
                    src = "public-harvest"
                    rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
                    rec = B.build_record(ptitle, ptitle, key, pdesc, ppoints,
                                         preq, pstandards, pcit, src, pdemo,
                                         rid)
                    gate_title = ptitle
                else:
                    src = "signature"
                    rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
                    rec = B.build_record(title, title, key, desc, points, req,
                                         standards, CIT[s], src, demo_kind,
                                         rid)
                    gate_title = rec["t"]
                B.check_record(rec)
                if [h for h in GATE.check(s, gate_title) if h[0] != s]:
                    print("  gate refused (cross-db dupe): %s" % gate_title, flush=True)
                    continue
                GATE.admit(s, gate_title, rid)
                recs.append(rec)
            assert recs, "empty db " + s
            built[s] = recs
    return built


def write_shard_db(slug, recs):
    base = os.path.join(SHARD, "data", slug)
    light = [{"id": r["id"], "t": r["t"], "g": r["g"]} for r in recs]
    B.write_gz_jsonl(os.path.join(base, "index.jsonl.gz"), light)
    for ci in range(0, len(recs), 100):
        B.write_gz_jsonl(os.path.join(base, "chunks", "chunk-%04d.jsonl.gz" % (ci // 100)),
                         recs[ci:ci + 100])
    return len(recs)


def update_json_list(path, entries):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    data = json.loads(raw)
    have = {d["slug"] for d in data["databases"]}
    for e in entries:
        if e["slug"] not in have:
            data["databases"].append(e)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        if raw.endswith("\n"):
            f.write("\n")


def manifest_entry(slug, n):
    c = DBCFG[slug]
    return {"slug": slug, "name": c["name"], "tagline": c["tagline"],
            "record_kind": c["record_kind"], "id_prefix": c["prefix"],
            "ai_name": c["ai"], "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "record_count": n, "status": "live", "full_records": n,
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": c["source"]}


def api_entry(slug, n):
    c = DBCFG[slug]
    return {"slug": slug, "name": c["name"], "tagline": c["tagline"],
            "record_kind": c["record_kind"], "record_count": n, "status": "live",
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"}


MARKERS = {"report": "INFO = {", "sqlite": "sqlite3.connect", "jsondoc": "def get_path(",
           "ledger": "def post(entries)", "ticks": "vwap", "hashchain": "block_hash(",
           "ehr": "ENCOUNTER_REQUIRED", "dicom": "REQUIRED_TAGS", "genome": "GC=",
           "geo": "point_in_polygon", "stats": "statistics.median",
           "simhw": "SIMULATED DEVICE INTERFACE", "rss": "ElementTree",
           "text": "most_common(5)", "pipeline": "def clean(rec)",
           "fileops": "TemporaryDirectory",
           "socket": "parse_ipv4_header", "algo": "def bfs(", "vision": "edge_metric",
           "secret": "gen_world(", "dsp": "dft_mag", "sensors": "pearson(",
           "spike": "integrate-and-fire", "dna": "quaternary-encoded",
           "tda": "persistence pairs", "poincare": "acosh(",
           "multivector": "geometric product", "riemann": "line element",
           "lattice": "Babai", "fhe": "homomorphic addition",
           "qkd": "BB84", "hologram": "interference grating",
           "plasmonic": "plasmonic waveguide", "skyrmion": "topological charge",
           "memgraph": "episodic memory", "selfimprove": "NodeTransformer",
           "neurosym": "logical inference"}


def run_demo(rid, prog, done):
    for k, m in MARKERS.items():
        if k not in done and m in prog:
            done.add(k)
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=60)
            assert p.returncode == 0, "demo failed %s: %s" % (rid, p.stderr[-500:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % rid
            print("demo ok: %-12s %s" % (k, rid), flush=True)


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

    # ---- step 1: file 14 entries into existing databases
    filed, filed_progs = file_records()
    assert len(filed) == 14, "expected 14 filed, got %d" % len(filed)

    # ---- step 2: build 70 new databases (30 pairs + 10 signature-only)
    built = build_new_records()
    assert len(built) == 70, "expected 70 dbs, got %d" % len(built)
    total = 0
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        total += len(recs)
        n = write_shard_db(slug, recs)
        print("shard: %-46s %d records" % (slug, n), flush=True)
    assert total == 675, "expected 675 seed records, got %d" % total

    # ---- step 3: execute every demo (filed + new), one run per archetype
    done = set()
    for rid, prog in filed_progs:
        run_demo(rid, prog, done)
    for slug, recs in built.items():
        for r in recs:
            run_demo(r["id"], r["demo"]["program"], done)
    for k in sorted(set(MARKERS) - done):
        prog = B.DEMOS[k]("Sample %s demo" % k, "TEST-000001", "test", ["p1"], "req")
        compile(prog, "TEST-000001", "exec")
        p = subprocess.run([sys.executable, "-c", prog],
                           capture_output=True, text=True, timeout=60)
        assert p.returncode == 0, "demo failed (direct) %s: %s" % (k, p.stderr[-500:])
        assert "OK:" in p.stdout, "demo no OK marker (direct) %s" % k
        done.add(k)
        print("demo ok: %-12s (direct)" % k, flush=True)
    assert len(done) == len(MARKERS), "not all archetypes executed: %s" % (set(MARKERS) - done)
    print("demo execution: %d archetypes ran OK" % len(done), flush=True)

    # ---- step 4: pages + generators
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
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ",".join(notes)), flush=True)

    entries_m = [manifest_entry(s, len(built[s])) for s in built]
    update_json_list(os.path.join(REPO, "data", "manifest.json"), entries_m)
    entries_a = [api_entry(s, len(built[s])) for s in built]
    update_json_list(os.path.join(REPO, "api.json"), entries_a)
    print("manifest + api.json: appended %d databases, %d records" % (len(built), total))
    print("filed records: %d" % len(filed))
    print("NEXT: run python3 code/restamp_counts.py, then commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
