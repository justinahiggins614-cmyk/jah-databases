#!/usr/bin/env python3
"""Build the Virology field databases for JAH Databases (field #3, taxonomy order).

Verified 2026-10-17: the manifest holds microbiology/immunology/epidemiologists
DBs but no dedicated virology database — virus coverage is thin taxonomy/traits
records, not the discipline. So this build creates two NEW databases:

  virology              — The Virology Database (public-harvest: real,
                         fact-checked virology — virus structure and
                         classification (Baltimore), replication cycles,
                         bacteriophages, plant/animal/human viruses, emerging
                         viruses, vaccines/antivirals, diagnostic methods,
                         epidemiology of viral disease, lab techniques)
  virology-signature    — The Virology Signature Database (his original
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
from entries_virology import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals — his original Signature interpretation of virology: "
                "clearly labeled Signature-made, never presented as authentic public record.")
    pub_line = ("Public records — real, fact-checked virology: virus structure and "
                "classification (Baltimore), replication cycles, bacteriophages, "
                "plant/animal/human viruses, emerging viruses, vaccines and antivirals, "
                "diagnostic methods, epidemiology of viral disease, and lab techniques, "
                "organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what a virus is, "
              "structure, genomes, Baltimore classification, microscopy, taxonomy, tropism, "
              "transmission, lytic/lysogenic cycles, entry) -> Compounded (replication "
              "strategies, reverse transcription, RdRp, assembly, bacteriophages, plant "
              "viruses, animal viruses, respiratory viruses, emerging viruses, evolution, "
              "latency, oncogenic viruses) -> Advanced (diagnostics, vaccines, antivirals, "
              "epidemiology, lab techniques, viral vectors, giant viruses, endogenous "
              "retroviruses, metagenomics, pandemic preparedness).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s — %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search viruses, Baltimore classes, vaccines, techniques...",
        "chat_ph": "Ask about virology...",
        "archive_blurb": ("Seeded %s virology records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations · Compounded · Advanced — each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled structural virology studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about virology — from what a virus is up to vaccines, pandemics, and gene therapy." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "virology-study", "gen_demo_kind": "virology-demo",
        "source": source,
    }

CIT_PUB = "Virology (peer-reviewed literature and standard textbooks)."
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["virology"] = _cfg(
    "virology", "The Virology Database",
    "Real, fact-checked virology: virus structure and classification (Baltimore), "
    "replication cycles, bacteriophages, plant/animal/human viruses, emerging viruses, "
    "vaccines and antivirals, diagnostic methods, epidemiology of viral disease, and "
    "lab techniques.",
    "virology record", "JAH-VIR-", "JAH Virology Archivist",
    "virology archivist — virus structure and classification (Baltimore), replication "
    "cycles, bacteriophages, plant/animal/human viruses, emerging viruses, "
    "vaccines/antivirals, diagnostic methods, epidemiology of viral disease, lab "
    "techniques; teaching progressively along the ladder from foundations (what a "
    "virus is, structure, genomes, Baltimore classes, microscopy, taxonomy, tropism, "
    "transmission, lytic/lysogenic cycles, entry) through compounded (replication "
    "strategies, reverse transcription, RdRp, assembly, phages, plant/animal/ "
    "respiratory viruses, emerging viruses, evolution, latency, oncogenic viruses) to "
    "advanced (diagnostics, vaccines, antivirals, epidemiology, lab techniques, viral "
    "vectors, giant viruses, endogenous retroviruses, metagenomics, pandemic "
    "preparedness); answers from many angles — definition, example, analogy, "
    "application, history, math, how-to — using only the system's own archive data",
    CIT_PUB, "public")
DBCFG["virology-signature"] = _cfg(
    "virology-signature", "The Virology Signature Database",
    "His original Signature interpretation of virology: the full ladder from what a "
    "virus is to pandemic preparedness, reframed as Signature engineering. Clearly "
    "labeled Signature-made, never presented as authentic public record.",
    "virology record", "JAH-VSG-", "JAH Virology Archivist (Signature)",
    "virology archivist — Signature editions: his original Signature interpretation of "
    "virology, clearly labeled Signature-made and never presented as authentic public "
    "record; teaches progressively along the ladder from foundations through compounded "
    "to advanced; answers from many angles — definition, example, analogy, application, "
    "history, math, how-to — using only the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# virological calculation for its record. All are machine-executed by main().

_PREAMBLE = """import math
"""

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_virus_scale(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    n_particles = 1e31                      # estimated virus particles on Earth
    virion_mass = 1e-18                     # kg, typical order of magnitude
    total_kg = n_particles * virion_mass
    print("estimated virus particles on Earth: %.0e" % n_particles)
    print("at ~%.0e kg each -> total viral mass ~%.0e kg" % (virion_mass, total_kg))
    assert total_kg == 1e13
    human_biomass = 4e11                    # kg, order of magnitude
    print("human biomass ~%.0e kg: viruses outweigh humanity ~%.0f-fold" % (
        human_biomass, total_kg / human_biomass))
    assert total_kg / human_biomass > 10
    print("OK: %s weighed the virosphere" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_capsid_geometry(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def subunits(T):
    return 60 * T
def main():
    print("icosahedral capsid subunits = 60 x T:")
    for T, example in ((1, "small phage"), (3, "poliovirus-like"), (4, "hepatitis B-like")):
        print("  T=%d -> %d subunits  (%s)" % (T, subunits(T), example))
    assert subunits(1) == 60
    assert subunits(3) == 180
    assert subunits(4) == 240
    assert subunits(7) == 420
    print("OK: %s tiled the icosahedron" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_size_filter(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    pore_nm = 220.0   # 0.22-micron bacteria-proof filter
    agents = [("parvovirus", 25.0), ("poliovirus", 30.0), ("SARS-CoV-2", 100.0),
              ("influenza A", 120.0), ("tobacco mosaic virus", 18.0),
              ("E. coli", 2000.0)]
    print("0.22-micron filter (pore %.0f nm):" % pore_nm)
    for aname, size in agents:
        verdict = "PASSES (virus-sized)" if size < pore_nm else "RETAINED (cell-sized)"
        print("  %-20s %6.0f nm  %s" % (aname, size, verdict))
    assert all(s < pore_nm for _, s in agents if _ != "E. coli")
    assert 2000.0 > pore_nm
    print("OK: %s proved filterability separates viruses from bacteria" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_genome_stats(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def gc_content(seq):
    seq = seq.upper()
    return (seq.count("G") + seq.count("C")) / len(seq)
def main():
    seq = "ATGC" * 25                      # synthetic 100-letter genome
    L = len(seq)
    gc = gc_content(seq)
    print("synthetic genome: %d letters, GC content %.1f %%" % (L, gc * 100))
    assert L == 100
    assert abs(gc - 0.50) < 1e-9
    real = {"parvovirus (ssDNA)": 5100, "influenza (8 segments)": 13500,
            "SARS-CoV-2 (+ssRNA)": 29900, "mimivirus (dsDNA)": 1180000,
            "pandoravirus (dsDNA)": 2500000}
    print("real genome lengths span %.0e-fold:" % (max(real.values()) / min(real.values())))
    for vname, ln in real.items():
        print("  %-24s %8d nt" % (vname, ln))
    assert abs(max(real.values()) / min(real.values()) - 490.2) < 1.0
    print("OK: %s measured genomes from 5 kb to 2.5 Mb" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_baltimore_lookup(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
CLASSES = {
    "I":   ("dsDNA",  "herpes simplex virus"),
    "II":  ("ssDNA",  "parvovirus"),
    "III": ("dsRNA",  "rotavirus"),
    "IV":  ("+ssRNA", "SARS-CoV-2"),
    "V":   ("-ssRNA", "influenza A"),
    "VI":  ("ssRNA-RT", "HIV"),
    "VII": ("dsDNA-RT", "hepatitis B virus"),
}
def main():
    print("Baltimore classes:")
    for cls in ("I", "II", "III", "IV", "V", "VI", "VII"):
        genome, example = CLASSES[cls]
        print("  class %-4s %-9s e.g. %s" % (cls, genome, example))
    assert len(CLASSES) == 7
    assert CLASSES["IV"][1] == "SARS-CoV-2"
    assert CLASSES["VI"][0] == "ssRNA-RT"
    assert CLASSES["V"][1] == "influenza A"
    rt_classes = [c for c, (g, _) in CLASSES.items() if "RT" in g]
    assert rt_classes == ["VI", "VII"]
    print("OK: %s classified all seven Baltimore classes" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_microscope_resolution(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def abbe(lam_nm, NA):
    return lam_nm / (2 * NA)
def main():
    d_light = abbe(550.0, 1.4)
    print("light microscope (550 nm, NA 1.4): resolution ~%.0f nm" % d_light)
    assert abs(d_light - 196.4) < 1.0
    d_em = abbe(0.004, 1.4)
    print("electron microscope (0.004 nm electrons): resolution ~%.4f nm" % d_em)
    assert d_em < 0.01
    polio = 30.0
    print("poliovirus (%g nm) vs light limit (%g nm): %s" % (
        polio, d_light, "INVISIBLE to light" if polio < d_light else "visible"))
    assert polio < d_light < 400.0
    print("OK: %s derived why viruses needed the electron microscope" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_taxonomy_tree(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
TREE = {
    "Nidovirales": {"Coronaviridae": ["SARS-CoV-2", "MERS-CoV"],
                    "Arteriviridae": ["PRRSV"]},
    "Herpesvirales": {"Herpesviridae": ["herpes simplex virus 1", "varicella-zoster virus"]},
    "Mononegavirales": {"Filoviridae": ["Ebola virus"],
                        "Paramyxoviridae": ["measles virus"],
                        "Rhabdoviridae": ["rabies virus"]},
    "Picornavirales": {"Picornaviridae": ["poliovirus", "rhinovirus"]},
}
def find(virus):
    for order, fams in TREE.items():
        for fam, members in fams.items():
            if virus in members:
                return order, fam
    return None
def main():
    for v in ("SARS-CoV-2", "Ebola virus", "measles virus", "poliovirus"):
        order, fam = find(v)
        print("  %-22s order %-15s family %s" % (v, order, fam))
    assert find("SARS-CoV-2") == ("Nidovirales", "Coronaviridae")
    assert find("Ebola virus") == ("Mononegavirales", "Filoviridae")
    assert find("rabies virus") == ("Mononegavirales", "Rhabdoviridae")
    assert find("not a virus") is None
    print("OK: %s navigated the ICTV tree" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_binding_affinity(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def frac_bound(L_nM, Kd_nM):
    return L_nM / (Kd_nM + L_nM)
def main():
    Kd = 10.0   # nM, spike-receptor dissociation constant
    print("Kd = %.0f nM:" % Kd)
    for L in (1.0, 10.0, 90.0):
        print("  receptor %.0f nM -> %.1f %% of spikes bound" % (L, 100 * frac_bound(L, Kd)))
    assert abs(frac_bound(10.0, Kd) - 0.5) < 1e-9
    assert abs(frac_bound(90.0, Kd) - 0.9) < 1e-9
    tight = frac_bound(10.0, 1.0)
    print("a 10x tighter binder (Kd=1 nM) at 10 nM receptor: %.1f %% bound" % (100 * tight))
    assert abs(tight - 10.0 / 11.0) < 1e-9
    print("OK: %s quantified the receptor handshake" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_transmission_routes(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
ROUTES = {
    "respiratory": ["influenza A", "SARS-CoV-2", "rhinovirus"],
    "fecal-oral": ["norovirus", "poliovirus", "hepatitis A virus"],
    "blood-borne": ["HIV", "hepatitis B virus", "hepatitis C virus"],
    "sexual": ["HIV", "herpes simplex virus 2", "human papillomavirus"],
    "vector-borne": ["Zika virus", "dengue virus", "yellow fever virus"],
    "vertical": ["rubella virus", "Zika virus", "HIV"],
}
CONTROLS = {
    "respiratory": "masks, ventilation",
    "fecal-oral": "safe water, handwashing",
    "blood-borne": "screen blood, safe needles",
    "sexual": "condoms",
    "vector-borne": "bed nets, mosquito control",
    "vertical": "maternal screening, treatment",
}
def main():
    for route, viruses in ROUTES.items():
        print("  %-12s %-28s breaks: %s" % (route, ", ".join(viruses[:2]), CONTROLS[route]))
    assert len(ROUTES) == 6
    assert all(len(v) >= 2 for v in ROUTES.values())
    assert "SARS-CoV-2" in ROUTES["respiratory"]
    assert "HIV" in ROUTES["blood-borne"] and "HIV" in ROUTES["sexual"]
    print("OK: %s mapped every transmission route to its breaker" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_lytic_burst(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    N0, burst, cycles = 1, 150, 4
    N = N0 * burst ** cycles
    print("one virion, burst size %d, %d lytic cycles -> %d virions" % (burst, cycles, N))
    assert N == 506250000
    t4_burst, t4_min = 150, 25.0
    per_hour = 60.0 / t4_min
    print("phage T4: ~%d progeny per %g min -> %.1f doublings/hour of infected cells" % (
        t4_burst, t4_min, per_hour * math.log2(t4_burst)))
    assert abs(per_hour * math.log2(t4_burst) - 17.4) < 0.2
    print("OK: %s compounded the lytic burst" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_lysogeny_switch(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def decide(cI_high, dna_damage):
    # lambda genetic switch: cI maintains lysogeny; DNA damage flips to lysis
    if dna_damage:
        return "lytic"
    return "lysogenic" if cI_high else "lytic"
def main():
    cases = [("healthy lysogen", True, False), ("UV-damaged lysogen", True, True),
             ("fresh infection, Cro wins", False, False)]
    for label, cI, dmg in cases:
        print("  %-24s -> %s" % (label, decide(cI, dmg)))
    assert decide(True, False) == "lysogenic"
    assert decide(True, True) == "lytic"
    assert decide(False, False) == "lytic"
    print("prophage genes carried silently; toxin genes can ride along (cholera, diphtheria)")
    print("OK: %s flipped the lambda switch" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_entry_kinetics(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def bound_frac(k_per_min, t_min):
    return 1 - math.exp(-k_per_min * t_min)
def main():
    k = 0.5
    print("attachment rate k = %.1f /min:" % k)
    for t in (1.0, 5.0, 10.0):
        print("  t = %4.1f min -> %.1f %% bound" % (t, 100 * bound_frac(k, t)))
    assert abs(bound_frac(0.5, 5.0) - 0.917915) < 1e-4
    assert bound_frac(0.5, 10.0) > 0.99
    # fusion is effectively irreversible once triggered: bound -> fused fraction
    fused = bound_frac(k, 5.0) * 0.8
    print("with 80%% fusion efficiency at 5 min: %.1f %% entered" % (100 * fused))
    assert abs(fused - 0.734332) < 1e-4
    print("OK: %s timed viral entry" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_replication_playbook(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
PLAYBOOK = {
    "I":   ["genome to nucleus", "cell transcribes mRNA", "cell replicates DNA"],
    "II":  ["ssDNA -> dsDNA", "genome to nucleus", "cell transcribes mRNA"],
    "III": ["carried RdRp transcribes mRNA inside particle", "translate polymerase", "copy dsRNA"],
    "IV":  ["genome IS mRNA: translate immediately", "make RdRp", "copy via -RNA intermediate"],
    "V":   ["carried RdRp transcribes mRNA from -RNA", "translate proteins", "copy genome"],
    "VI":  ["reverse transcriptase: RNA -> dsDNA", "integrate provirus", "cell transcribes mRNA"],
    "VII": ["DNA transcribed to RNA", "reverse transcribe RNA -> DNA", "package DNA"],
}
def main():
    for cls in ("I", "IV", "V", "VI"):
        print("  class %s: %s" % (cls, " -> ".join(PLAYBOOK[cls])))
    assert len(PLAYBOOK) == 7
    assert PLAYBOOK["IV"][0].startswith("genome IS mRNA")
    assert "carried RdRp" in PLAYBOOK["V"][0]
    assert "reverse transcriptase" in PLAYBOOK["VI"][0]
    assert "integrate provirus" in PLAYBOOK["VI"]
    print("OK: %s ran all seven replication playbooks" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_revtranscribe(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
COMP_RNA = {"A": "T", "U": "A", "G": "C", "C": "G"}
COMP_DNA = {"A": "T", "T": "A", "G": "C", "C": "G"}
def rna_to_dna(rna):
    return "".join(COMP_RNA[b] for b in rna.upper())
def main():
    rna = "AUGCUU"
    dna = rna_to_dna(rna)
    print("HIV-like RNA template %s -> DNA copy %s" % (rna, dna))
    assert dna == "TACGAA"
    assert rna_to_dna("UUUU") == "AAAA"
    assert rna_to_dna("GCGC") == "CGCG"
    # second strand: complement of the first DNA strand
    comp2 = "".join(COMP_DNA[b] for b in dna)
    print("second DNA strand: %s (dsDNA ready to integrate)" % comp2)
    assert comp2 == "ATGCTT"
    print("OK: %s ran reverse transcription" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_rdrp_errors(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def mutations_per_genome(mu, L):
    return mu * L
def main():
    mu = 1e-4   # per base per replication, typical RdRp without proofreading
    for vname, L in (("poliovirus", 7500), ("influenza segment avg", 1700),
                     ("SARS-CoV-2", 29900)):
        print("  %-22s L=%5d -> ~%.2f mutations per genome copy" % (vname, L, mutations_per_genome(mu, L)))
    assert abs(mutations_per_genome(1e-4, 29900) - 2.99) < 1e-9
    assert abs(mutations_per_genome(1e-4, 10000) - 1.0) < 1e-9
    # coronavirus proofreading lowers the effective rate ~10-fold
    print("with proofreading (CoV, ~10x lower): %.2f per genome" % mutations_per_genome(1e-5, 29900))
    assert abs(mutations_per_genome(1e-5, 29900) - 0.299) < 1e-9
    print("OK: %s counted RdRp's typos" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_assembly_kinetics(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    r, K, V, dt, steps = 0.5, 1000.0, 10.0, 0.1, 400
    for _ in range(steps):          # logistic self-assembly: nucleation then growth
        V += r * V * (1 - V / K) * dt
    print("self-assembly: %d subunits available -> %.0f assembled (carrying capacity %g)" % (K, V, K))
    assert 990.0 < V < 1000.0
    # nucleation lag: early growth is slow, then explosive
    V2, early = 10.0, None
    for i in range(400):
        V2 += r * V2 * (1 - V2 / K) * dt
        if i == 20:
            early = V2
    print("after 2 time units only %.1f assembled (nucleation lag), then runaway growth" % early)
    assert early < 50.0
    print("OK: %s watched capsids self-assemble" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_phage_moi(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def p_zero(moi):
    return math.exp(-moi)
def main():
    for moi in (0.1, 1.0, 5.0):
        infected = 1 - p_zero(moi)
        print("  MOI %.1f -> %.1f %% of bacteria infected" % (moi, 100 * infected))
    assert abs(p_zero(5.0) - 0.0067379) < 1e-6
    assert abs((1 - p_zero(1.0)) - 0.6321206) < 1e-6
    # therapy dosing: 1e9 bacteria at MOI 10 needs 1e10 phages
    bacteria, moi = 1e9, 10.0
    print("therapy dose for %.0e bacteria at MOI %.0f: %.0e phages" % (bacteria, moi, bacteria * moi))
    assert bacteria * moi == 1e10
    print("OK: %s dosed phage therapy by MOI" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tmv_packing(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    proteins, nt = 2130, 6395
    per = proteins / nt
    print("TMV: %d coat proteins wrap %d nucleotides" % (proteins, nt))
    print("  proteins per nucleotide: %.4f (≈ 1 per 3)" % per)
    print("  nucleotides per protein: %.3f" % (nt / proteins))
    assert abs(per - 1.0 / 3.0) < 0.001
    assert abs(nt / proteins - 3.002) < 0.01
    length_nm, diam_nm = 300.0, 18.0
    print("rod %g x %g nm: aspect ratio %.1f" % (length_nm, diam_nm, length_nm / diam_nm))
    assert abs(length_nm / diam_nm - 16.67) < 0.01
    print("OK: %s audited TMV's bill of materials" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_host_matrix(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
HOSTS = {
    "tobacco mosaic virus": ["tobacco", "tomato", "pepper"],
    "rabies virus": ["dogs", "bats", "humans", "raccoons"],
    "bacteriophage T4": ["E. coli"],
    "African swine fever virus": ["pigs", "warthogs"],
    "canine parvovirus": ["dogs"],
}
def main():
    for v, hosts in HOSTS.items():
        print("  %-24s -> %s" % (v, ", ".join(hosts)))
    assert "humans" in HOSTS["rabies virus"]
    assert "humans" not in HOSTS["tobacco mosaic virus"]
    assert HOSTS["bacteriophage T4"] == ["E. coli"]
    zoonotic = [v for v, h in HOSTS.items() if "humans" in h]
    print("zoonotic in this set: %s" % ", ".join(zoonotic))
    assert zoonotic == ["rabies virus"]
    print("OK: %s mapped the host matrix" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_r0_compare(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def herd_threshold(R0):
    return 1 - 1 / R0
def main():
    table = [("measles", 15.0), ("smallpox", 6.0), ("SARS-CoV-2 ancestral", 2.8),
             ("seasonal influenza", 1.3)]
    print("  virus                    R0    herd threshold")
    for vname, R0 in table:
        print("  %-24s %4.1f   %5.1f %%" % (vname, R0, 100 * herd_threshold(R0)))
    assert abs(herd_threshold(15.0) - 0.93333) < 1e-4
    assert abs(herd_threshold(1.3) - 0.23077) < 1e-4
    assert herd_threshold(15.0) > herd_threshold(2.8) > herd_threshold(1.3)
    print("OK: %s ranked viruses by R0" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_spillover_score(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def score(profile):
    # EDUCATIONAL toy triage model, not a real risk assessment.
    w = {"rna_genome": 2, "mammal_reservoir": 2, "respiratory_route": 3,
         "broad_host_range": 2, "human_receptor_match": 3}
    return sum(w[k] for k, v in profile.items() if v)
def main():
    high = {"rna_genome": True, "mammal_reservoir": True, "respiratory_route": True,
            "broad_host_range": True, "human_receptor_match": True}
    low = {"rna_genome": False, "mammal_reservoir": False, "respiratory_route": False,
           "broad_host_range": False, "human_receptor_match": False}
    mid = {"rna_genome": True, "mammal_reservoir": True, "respiratory_route": False,
           "broad_host_range": False, "human_receptor_match": False}
    print("toy spillover triage scores (educational only): high=%d mid=%d low=%d" % (
        score(high), score(mid), score(low)))
    assert score(high) == 12 and score(mid) == 4 and score(low) == 0
    assert score(high) > score(mid) > score(low)
    print("OK: %s triaged spillover risk (toy model)" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_quasispecies_sim(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def run(mu, seed=42, gens=12, L=24, pop=200):
    import random
    rng = random.Random(seed)
    bases = "ACGU"
    seq = [rng.choice(bases) for _ in range(L)]
    cloud = {"".join(seq)}
    cur = ["".join(seq)] * pop
    for _ in range(gens):
        nxt = []
        for s in cur:
            s = "".join(b if rng.random() > mu else rng.choice(bases) for b in s)
            nxt.append(s)
        cur = nxt
        cloud.update(cur)
    return len(cloud)
def main():
    d_low = run(0.001)
    d_high = run(0.05)
    print("distinct genomes after 12 generations: low error -> %d, high error -> %d" % (d_low, d_high))
    assert run(0.05) == d_high, "simulation must be deterministic"
    assert d_high > d_low >= 1
    print("selection would now act on the cloud, not on one genome")
    print("OK: %s grew a quasispecies cloud" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_latency_markov(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # latent -> reactivated with p=0.01/yr; reactivated -> latent with p=0.30/yr
    p_lr, p_rl = 0.01, 0.30
    latent, react = 1.0, 0.0
    for _ in range(2000):
        latent, react = latent * (1 - p_lr) + react * p_rl, latent * p_lr + react * (1 - p_rl)
    print("steady state: %.2f %% latent, %.2f %% reactivated" % (100 * latent, 100 * react))
    expect_react = p_lr / (p_lr + p_rl)
    assert abs(react - expect_react) < 1e-6
    assert abs(react - 0.032258) < 1e-4
    assert latent > 0.95, "herpesviruses spend life overwhelmingly latent"
    print("OK: %s found latency's steady state" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_onco_table(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
ONCO = {
    "human papillomavirus 16/18": "cervical, anal, throat cancers",
    "hepatitis B virus": "liver cancer",
    "hepatitis C virus": "liver cancer",
    "Epstein-Barr virus": "Burkitt lymphoma, nasopharyngeal carcinoma",
    "HTLV-1": "adult T-cell leukemia",
    "Kaposi sarcoma herpesvirus": "Kaposi sarcoma",
    "Merkel cell polyomavirus": "Merkel cell carcinoma",
}
VACCINE_PREVENTABLE = {"human papillomavirus 16/18", "hepatitis B virus"}
def main():
    for v, cancers in ONCO.items():
        tag = " [VACCINE-PREVENTABLE]" if v in VACCINE_PREVENTABLE else ""
        print("  %-32s -> %s%s" % (v, cancers, tag))
    assert len(ONCO) == 7
    assert ONCO["human papillomavirus 16/18"].startswith("cervical")
    assert "Burkitt" in ONCO["Epstein-Barr virus"]
    assert len(VACCINE_PREVENTABLE) == 2
    print("OK: %s listed the oncogenic viruses" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pcr_amplification(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def copies(n_cycles, efficiency=1.0):
    return (1 + efficiency) ** n_cycles
def main():
    for n in (20, 25, 30, 35):
        print("  %d cycles -> %.3g copies" % (n, copies(n)))
    assert copies(30) == 2 ** 30 == 1073741824
    assert copies(20) == 1048576
    # Ct: ~3.32 cycles per 10-fold change
    ct_shift = math.log(10) / math.log(2)
    print("one 10-fold dilution shifts Ct by %.2f cycles" % ct_shift)
    assert abs(ct_shift - 3.3219) < 1e-3
    print("low Ct (18) = abundant virus; high Ct (35) = scarce virus")
    print("OK: %s amplified by PCR" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_vaccine_efficacy(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def efficacy(attack_vax, attack_unvax):
    return 1 - attack_vax / attack_unvax
def main():
    trials = [("measles MMR", 0.001, 0.10), ("HPV", 0.002, 0.05), ("COVID mRNA", 0.01, 0.20)]
    for tname, av, au in trials:
        print("  %-12s attack vax %.1f %% vs unvax %.0f %% -> VE %.0f %%" % (
            tname, 100 * av, 100 * au, 100 * efficacy(av, au)))
    assert abs(efficacy(0.01, 0.20) - 0.95) < 1e-9
    assert abs(efficacy(0.001, 0.10) - 0.99) < 1e-9
    assert abs(efficacy(0.002, 0.05) - 0.96) < 1e-9
    print("OK: %s computed vaccine efficacy" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_antiviral_dose_response(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def inhibition(dose, ic50, n=1.0):
    return 1 / (1 + (ic50 / dose) ** n)
def main():
    ic50 = 50.0   # nM
    print("IC50 = %.0f nM (Hill n=1):" % ic50)
    for dose in (5.0, 50.0, 450.0):
        print("  dose %6.0f nM -> %.1f %% inhibition" % (dose, 100 * inhibition(dose, ic50)))
    assert abs(inhibition(ic50, ic50) - 0.5) < 1e-9
    assert abs(inhibition(450.0, ic50) - 0.9) < 1e-9
    assert abs(inhibition(5.0, ic50) - 1.0 / 11.0) < 1e-9
    # steeper curve with Hill n=2
    assert inhibition(950.0, ic50, n=2.0) > 0.99
    print("OK: %s plotted the antiviral dose-response" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_sir_model(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def run(R0, days=200):
    N, gamma = 1000.0, 0.2
    beta = R0 * gamma / N
    S, I, R = N - 1.0, 1.0, 0.0
    peak, dt = I, 0.5
    for _ in range(int(days / dt)):
        dS = -beta * S * I * dt
        dR = gamma * I * dt
        S += dS; I += -dS - dR; R += dR
        peak = max(peak, I)
    return S, I, R, peak
def main():
    for R0 in (1.3, 2.8, 15.0):
        S, I, R, peak = run(R0)
        print("  R0=%4.1f -> peak infectious %5.0f, final susceptible %5.0f, herd threshold %4.0f %%" % (
            R0, peak, S, 100 * (1 - 1 / R0)))
    S, I, R, peak = run(2.8)
    assert peak > 100, peak
    assert S < 150, S
    assert abs((1 - 1 / 15.0) - 0.93333) < 1e-4
    _, _, _, peak_measles = run(15.0)
    assert peak_measles > 700
    print("OK: %s ran the SIR epidemic" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_plaque_assay(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def pfu_per_ml(plaques, dilution, volume_ml):
    return plaques / (dilution * volume_ml)
def main():
    cases = [(45, 1e-6, 0.1), (32, 1e-5, 0.2), (87, 1e-7, 0.1)]
    for plaques, dil, vol in cases:
        print("  %d plaques, 10^%d dilution, %.1f mL -> %.3g PFU/mL" % (
            plaques, round(math.log10(dil)), vol, pfu_per_ml(plaques, dil, vol)))
    assert abs(pfu_per_ml(45, 1e-6, 0.1) / 4.5e8 - 1) < 1e-9
    assert abs(pfu_per_ml(32, 1e-5, 0.2) / 1.6e7 - 1) < 1e-9
    assert abs(pfu_per_ml(87, 1e-7, 0.1) / 8.7e9 - 1) < 1e-9
    print("gold-standard titration: one plaque = one infectious particle")
    print("OK: %s titrated virus by plaque assay" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_vector_capacity(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
VECTORS = {"AAV": 4.7, "lentivirus": 8.0, "adenovirus": 7.5}   # kb cargo capacity
def fits(vector, gene_kb):
    return gene_kb <= VECTORS[vector]
def main():
    genes = [("SMN1 (spinal muscular atrophy)", 0.9), ("factor VIII (hemophilia A)", 7.0),
             ("dystrophin (Duchenne)", 11.0)]
    for gname, kb in genes:
        ok = [v for v in VECTORS if fits(v, kb)]
        print("  %-34s %4.1f kb -> fits: %s" % (gname, kb, ", ".join(ok) if ok else "NONE"))
    assert fits("AAV", 0.9) and not fits("AAV", 7.0)
    assert fits("lentivirus", 7.0) and not fits("lentivirus", 11.0)
    assert not any(fits(v, 11.0) for v in VECTORS)
    print("OK: %s packed genes into viral vectors" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_giant_compare(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    genomes = {"influenza A": 13500, "mimivirus": 1180000, "pandoravirus": 2500000}
    print("genome sizes (letters):")
    for vname, L in genomes.items():
        print("  %-14s %8d" % (vname, L))
    ratio = genomes["pandoravirus"] / genomes["influenza A"]
    print("pandoravirus / influenza genome ratio: %.1f x" % ratio)
    assert abs(ratio - 185.19) < 0.5
    assert genomes["mimivirus"] > 80 * genomes["influenza A"]
    # size: pandoravirus ~1000 nm vs light-microscope limit ~200 nm -> visible
    print("pandoravirus (~1000 nm) exceeds the 200 nm light limit: visible under light microscope")
    assert 1000.0 > 200.0
    print("OK: %s sized the giants" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_erv_genome(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    human_bp = 3.2e9
    erv_frac = 0.08
    erv_bp = human_bp * erv_frac
    print("human genome %.1f Gb x %.0f %% ERV = %.3g bp of viral fossils" % (
        human_bp / 1e9, erv_frac * 100, erv_bp))
    assert erv_bp == 2.56e8
    # find an LTR-like motif (TG...CA) in a synthetic locus
    locus = "ATCG" * 50 + "TG" + "A" * 300 + "CA" + "GCTA" * 50
    i = locus.find("TG")
    j = locus.find("CA", i)
    print("synthetic provirus locus: LTR-like TG at %d, CA at %d, span %d bp" % (i, j, j - i))
    assert i == 200 and j == 502 and (j - i) == 302
    print("syncytin: a domesticated retroviral envelope building every human placenta")
    print("OK: %s read the viral fossils" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_kmer_count(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def kmers(seq, k):
    return [seq[i:i + k] for i in range(len(seq) - k + 1)]
def main():
    reads = ["ATGCGATCGA", "GATCGATCGA", "ATGCGATCGA", "TTATGCGATC"]
    k = 4
    counts = {}
    for r in reads:
        for km in kmers(r, k):
            counts[km] = counts.get(km, 0) + 1
    top = max(counts, key=counts.get)
    print("%d reads -> %d distinct %d-mers; most common: %s (x%d)" % (
        len(reads), len(counts), k, top, counts[top]))
    assert top == "GATC"
    assert counts["GATC"] == 5
    assert counts["CGAT"] == 4
    print("assemblers chain overlapping k-mers into contigs; classifiers match them to databases")
    print("OK: %s counted k-mers like a metagenomics pipeline" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_surveillance_metrics(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def doubling_time(c0, c1, days):
    return days * math.log(2) / math.log(c1 / c0)
def cfr(deaths, cases):
    return deaths / cases
def main():
    dt = doubling_time(100, 400, 4.0)
    print("cases 100 -> 400 in 4 days: doubling time %.1f days" % dt)
    assert abs(dt - 2.0) < 1e-9
    print("case fatality ratio: 12 deaths / 800 cases = %.2f %%" % (100 * cfr(12, 800)))
    assert abs(cfr(12, 800) - 0.015) < 1e-9
    # variant growth advantage from sequence proportions
    p0, p1, weeks = 0.05, 0.50, 4.0
    adv = math.log((p1 / (1 - p1)) / (p0 / (1 - p0))) / (weeks * 7)
    print("variant 5%% -> 50%% of sequences in 4 weeks: logistic growth advantage %.3f/day" % adv)
    assert adv > 0.1
    print("OK: %s read the surveillance dashboard" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "virus_scale": demo_virus_scale, "capsid_geometry": demo_capsid_geometry,
    "size_filter": demo_size_filter, "genome_stats": demo_genome_stats,
    "baltimore_lookup": demo_baltimore_lookup, "microscope_resolution": demo_microscope_resolution,
    "taxonomy_tree": demo_taxonomy_tree, "binding_affinity": demo_binding_affinity,
    "transmission_routes": demo_transmission_routes, "lytic_burst": demo_lytic_burst,
    "lysogeny_switch": demo_lysogeny_switch, "entry_kinetics": demo_entry_kinetics,
    "replication_playbook": demo_replication_playbook, "revtranscribe": demo_revtranscribe,
    "rdrp_errors": demo_rdrp_errors, "assembly_kinetics": demo_assembly_kinetics,
    "phage_moi": demo_phage_moi, "tmv_packing": demo_tmv_packing,
    "host_matrix": demo_host_matrix, "r0_compare": demo_r0_compare,
    "spillover_score": demo_spillover_score, "quasispecies_sim": demo_quasispecies_sim,
    "latency_markov": demo_latency_markov, "onco_table": demo_onco_table,
    "pcr_amplification": demo_pcr_amplification, "vaccine_efficacy": demo_vaccine_efficacy,
    "antiviral_dose_response": demo_antiviral_dose_response, "sir_model": demo_sir_model,
    "plaque_assay": demo_plaque_assay, "vector_capacity": demo_vector_capacity,
    "giant_compare": demo_giant_compare, "erv_genome": demo_erv_genome,
    "kmer_count": demo_kmer_count, "surveillance_metrics": demo_surveillance_metrics,
}

# ---------------------------------------------------------------- records

def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_virology.py).
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
    for slug in ("virology", "virology-signature"):
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
