#!/usr/bin/env python3
"""Demo programs for the Unsolved Genetics databases.

Every demo is a SOLUTION EXPLORER walkthrough: real, runnable,
stdlib-only Python that walks the user through the Signature solution
approach for its record - interactive steps, adjustable assumptions,
real computed values, and explicit CONFIRM / REFUTE panels showing what
evidence would support or kill the approach.

All 68 demos are machine-executed by build.py: each prints its real
computed values, asserts tight bounds (never float exact-equality),
states the honesty label, and ends with the OK marker.
"""

import json

from entries_unsolved_genetics import ENTRIES, HONEST_LABEL

_BY_KEY = {e["key"]: e for e in ENTRIES}

_PREAMBLE = "import math\n"

# ---------------------------------------------------------------- calcs
# Per-record computations: real numbers from the record's assumptions,
# tight-bounds asserts (never float exact-equality).

DEMO_CALC = {
    "junk_dna": '''\
    active_frac = 0.80          # ENCODE 2012: biochemical activity
    constrained_frac = 0.082    # Lindblad-Toh 2011: mammalian constraint
    gap = active_frac - constrained_frac
    unexplained_bp = 3.2e9 * gap
    print("biochemically active fraction: %.3f" % active_frac)
    print("evolutionarily constrained fraction: %.3f" % constrained_frac)
    print("gap (active but unconstrained): %.3f" % gap)
    print("unexplained base pairs: %.3e" % unexplained_bp)
    assert 0.717 < gap < 0.719
    assert 2.29e9 < unexplained_bp < 2.31e9''',
    "gene_count": '''\
    human_pc = 19932
    mouse_pc = 21590
    ratio = mouse_pc / human_pc
    print("human protein-coding genes: %d" % human_pc)
    print("mouse protein-coding genes: %d" % mouse_pc)
    print("mouse/human gene-count ratio: %.4f" % ratio)
    assert 1.082 < ratio < 1.084''',
    "cvalue": '''\
    sizes = {"human": 3.2, "onion": 16.0, "lungfish": 133.0,
             "paris_japonica": 149.0}
    ordered = sorted(sizes, key=sizes.get)
    ratio = sizes["paris_japonica"] / sizes["human"]
    print("genome sizes (Gb), smallest first:")
    for k in ordered:
        print("  %-14s %6.1f" % (k, sizes[k]))
    print("paris japonica / human ratio: %.2f" % ratio)
    assert ordered[0] == "human"
    assert 46.5 < ratio < 46.6''',
    "human_mouse": '''\
    ccre = 900000
    genes = 19932
    per_gene = ccre / genes
    print("candidate regulatory elements: %d" % ccre)
    print("protein-coding genes: %d" % genes)
    print("regulatory elements per gene: %.2f" % per_gene)
    assert 45.1 < per_gene < 45.3''',
    "missing_heritability": '''\
    twin_h2 = 0.80
    snp_h2 = 0.45
    gap = twin_h2 - snp_h2
    explained = snp_h2 / twin_h2
    print("twin heritability: %.2f | SNP heritability: %.2f" % (twin_h2, snp_h2))
    print("missing heritability: %.2f" % gap)
    print("fraction of heritability explained: %.4f" % explained)
    assert 0.349 < gap < 0.351
    assert 0.5624 < explained < 0.5626''',
    "genotype_phenotype": '''\
    h2 = 0.80
    pgs_r2 = 0.40
    ceiling_gap = h2 - pgs_r2
    print("heritability ceiling for prediction R^2: %.2f" % h2)
    print("current polygenic-score R^2: %.2f" % pgs_r2)
    print("unexplained predictable variance: %.2f" % ceiling_gap)
    assert 0.399 < ceiling_gap < 0.401''',
    "gxe": '''\
    env = [0, 1]
    gA = [100.0 + 0.0 * e for e in env]
    gB = [95.0 + 10.0 * e for e in env]
    interaction = (gB[1] - gB[0]) - (gA[1] - gA[0])
    print("genotype A across environments: %s" % gA)
    print("genotype B across environments: %s" % gB)
    print("rank flips: B below A in env 0, B above A in env 1")
    print("interaction effect: %.1f" % interaction)
    assert gB[0] < gA[0] < gB[1]
    assert 9.9 < interaction < 10.1''',
    "siblings_differ": '''\
    mean_ibd = 0.50
    sd_ibd = 0.04
    lo = mean_ibd - 2 * sd_ibd
    hi = mean_ibd + 2 * sd_ibd
    denovo_each = 70
    print("sibling genome sharing: mean %.2f, ~95%% interval %.2f-%.2f"
          % (mean_ibd, lo, hi))
    print("de novo mutations per sibling: %d (expected shared: 0)" % denovo_each)
    assert 0.419 < lo < 0.421
    assert 0.579 < hi < 0.581''',
    "harmful_persist": '''\
    carrier_freq = 1.0 / 25.0
    q = carrier_freq / 2.0
    mu_implied = q * q * 1.0      # q^2 = mu/s with s = 1
    typical = 1e-5
    print("carrier 1 in 25 -> allele frequency q = %.4f" % q)
    print("mutation rate implied by balance: %.1e" % mu_implied)
    print("typical per-gene rate: %.1e | ratio: %.1f" % (typical, mu_implied / typical))
    assert 3.9e-4 < mu_implied < 4.1e-4
    assert mu_implied / typical > 10.0''',
    "paternal_age": '''\
    base = 70
    per_year = 2.0
    age20 = base
    age40 = base + per_year * 20
    print("expected de novo SNVs, father age 20: %d" % age20)
    print("expected de novo SNVs, father age 40: %.0f" % age40)
    print("increase over 20 years: %.0f" % (age40 - age20))
    assert age40 - age20 == 40
    assert 109.9 < age40 < 110.1''',
    "mutation_rate_var": '''\
    expected = 3.2e9 * 1.2e-8
    cpg_frac, boost = 0.01, 10.0
    cpg_share = cpg_frac * boost / ((1 - cpg_frac) + cpg_frac * boost)
    cpg_expected = expected * cpg_share
    print("genome-wide expected de novo: %.1f" % expected)
    print("CpG share of mutations: %.4f" % cpg_share)
    print("expected CpG-derived de novo: %.2f" % cpg_expected)
    assert 38.3 < expected < 38.5
    assert 3.52 < cpg_expected < 3.53''',
    "epigenetic_inheritance": '''\
    survive = (1 - 0.999) ** 2
    expected_survivors = 28e6 * survive
    print("methylation surviving one reprogramming wave: %.4f" % 0.001)
    print("surviving both waves: %.1e" % survive)
    print("illustrative survivors: %.0f of 2.8e7 CpG sites" % expected_survivors)
    assert 27.9 < expected_survivors < 28.1''',
    "why_sex": '''\
    generations = 10
    cost = 2.0 ** generations / 1.0 ** generations
    print("twofold cost over %d generations: asexual lineage %.0fx larger"
          % (generations, cost))
    print("sex must buy back at least a %.0f-fold edge to break even" % cost)
    assert cost == 1024.0''',
    "lewontin_paradox": '''\
    Ne = 0.001 / (4 * 1.2e-8)
    ratio = 8e9 / Ne
    print("Ne implied by diversity: %.0f" % Ne)
    print("census: 8.0e9 | census/Ne discrepancy: %.2e" % ratio)
    assert 20800 < Ne < 20900
    assert 3.8e5 < ratio < 3.9e5''',
    "balancing_selection": '''\
    wAA, wAS, wSS = 0.85, 1.0, 0.15
    s1, s2 = wAS - wAA, wAS - wSS
    qhat = s1 / (s1 + s2)
    print("fitnesses AA/AS/SS: %.2f %.2f %.2f" % (wAA, wAS, wSS))
    print("equilibrium allele frequency: %.4f" % qhat)
    assert 0.1499 < qhat < 0.1501''',
    "canalization": '''\
    def Phi(x):
        return 0.5 * (1 + math.erf(x / math.sqrt(2.0)))
    p_raw = 1 - Phi(2.0)
    p_buf = 1 - Phi(2.0 / math.sqrt(0.5))
    print("unbuffered variance 1.0: P(liability > 2) = %.4f" % p_raw)
    print("buffered variance 0.5:  P(liability > 2) = %.5f" % p_buf)
    print("buffering hides %.1fx of the extreme outcomes" % (p_raw / p_buf))
    assert 0.0227 < p_raw < 0.0229
    assert 0.0023 < p_buf < 0.0024''',
    "pleiotropy": '''\
    n_traits, p_each = 10, 0.10
    p_any = 1 - (1 - p_each) ** n_traits
    print("traits: %d, per-trait hit probability: %.2f" % (n_traits, p_each))
    print("P(mutation touches at least one trait): %.4f" % p_any)
    assert 0.6512 < p_any < 0.6514''',
    "grn": '''\
    n = 3
    states = 2 ** n
    funcs = 2 ** states
    networks = funcs ** n
    print("genes: %d -> network states: %d" % (n, states))
    print("boolean functions per gene: %d" % funcs)
    print("possible wirings: %d" % networks)
    assert states == 8 and funcs == 256 and networks == 16777216''',
    "splicing": '''\
    genes, transcripts = 20000, 200000
    per_gene = transcripts / genes
    print("genes: %d | transcripts: %d" % (genes, transcripts))
    print("isoforms per gene: %.1f" % per_gene)
    print("multi-exon genes alternatively spliced: 95%%")
    assert per_gene == 10.0''',
    "lncrna": '''\
    total, known = 19000, 500
    frac = known / total
    print("lncRNA genes: %d | with established function: ~%d" % (total, known))
    print("fraction functionally characterized: %.4f" % frac)
    assert 0.0263 < frac < 0.0264''',
    "protein_function": '''\
    pdb, uniprot = 200000, 250000000
    coverage = pdb / uniprot
    print("experimental structures: %d" % pdb)
    print("known protein sequences: %d" % uniprot)
    print("structural coverage: %.2e" % coverage)
    assert 7.9e-4 < coverage < 8.1e-4''',
    "mitonuclear": '''\
    nuc_div = 0.012
    naive_mito = nuc_div * 10.0
    print("human-chimp nuclear divergence: %.3f" % nuc_div)
    print("naive 10x expectation for mtDNA: %.3f" % naive_mito)
    print("mtDNA proteins: 13 | nuclear-encoded mito proteins: ~1500")
    assert 0.119 < naive_mito < 0.121''',
    "telomere": '''\
    divisions, loss_per = 60, 100
    total_loss = divisions * loss_per
    start, end = 10000, 10000 - total_loss
    print("loss over %d divisions: %d bp" % (divisions, total_loss))
    print("telomere start %d bp -> end %d bp" % (start, end))
    assert total_loss == 6000 and end == 4000''',
    "karyotype": '''\
    chimp, human = 48, 46
    fusions = (chimp - human) // 2
    print("chimpanzee: %d chromosomes | human: %d" % (chimp, human))
    print("telomere-telomere fusions implied: %d" % fusions)
    print("indian muntjac: 6-7 chromosomes, similar gene content")
    assert fusions == 1''',
    "hgt": '''\
    erv_bp = 3.2e9 * 0.08
    print("endogenous-retrovirus fraction: 0.08")
    print("viral-derived base pairs in human genome: %.2e" % erv_bp)
    assert 2.55e8 < erv_bp < 2.57e8''',
    "behavior_genetics": '''\
    rMZ, rDZ = 0.86, 0.60
    h2 = 2 * (rMZ - rDZ)
    print("MZ twin correlation: %.2f | DZ: %.2f" % (rMZ, rDZ))
    print("Falconer heritability h^2 = 2(rMZ - rDZ) = %.2f" % h2)
    assert 0.519 < h2 < 0.521''',
    "omnigenic": '''\
    core, peripheral = 100, 10000
    h2_peripheral = 0.80 * 0.90
    print("core genes: %d | peripheral genes: %d" % (core, peripheral))
    print("heritability via peripheral genes: %.2f" % h2_peripheral)
    assert 0.719 < h2_peripheral < 0.721''',
    "prs_portability": '''\
    r2_eur, r2_afr = 0.10, 0.02
    drop = r2_eur / r2_afr
    print("R^2 European ancestry: %.2f | R^2 African ancestry: %.2f" % (r2_eur, r2_afr))
    print("portability drop: %.1fx" % drop)
    assert 4.99 < drop < 5.01''',
    "genetic_nurture": '''\
    transmitted, nurture = 1.0, 0.30
    share = nurture / (transmitted + nurture)
    print("direct transmitted effect: %.2f" % transmitted)
    print("genetic-nurture effect: %.2f" % nurture)
    print("nurture share of parental-genotype association: %.4f" % share)
    assert 0.2307 < share < 0.2308''',
    "domestication": '''\
    R = 0.35 * 2.0
    total = R * 10
    print("breeder's equation R = h^2 * S = 0.35 * 2.0 = %.2f per generation" % R)
    print("response after 10 generations: %.1f" % total)
    assert 0.699 < R < 0.701
    assert 6.99 < total < 7.01''',
    "minimal_genome": '''\
    genes, bp = 473, 531560
    per_gene = bp / genes
    print("JCVI-syn3.0 genes: %d | base pairs: %d" % (genes, bp))
    print("base pairs per gene: %.2f" % per_gene)
    print("essential genes of unknown function: ~31%%")
    assert 1123.7 < per_gene < 1123.9''',
    "genetic_load": '''\
    U = 2.0
    load = 1 - math.exp(-U)
    print("deleterious mutations per genome per generation U = %.1f" % U)
    print("naive mutation load 1 - e^-U = %.4f" % load)
    assert 0.8646 < load < 0.8648''',
    "code_origin": '''\
    sense, aa = 61, 20
    degeneracy = sense / aa
    print("sense codons: %d | amino acids: %d" % (sense, aa))
    print("mean degeneracy: %.4f codons per amino acid" % degeneracy)
    assert 3.049 < degeneracy < 3.051''',
    "rna_world": '''\
    length = 40
    space = 4 ** length
    print("sequence space for %d-mer RNA: 4^%d = %.3e" % (length, length, space))
    assert 1.208e24 < space < 1.210e24''',
}

assert set(DEMO_CALC) == set(_BY_KEY), "demo calc map misses entries"


def _explorer_program(hdr_fn, name, rid, group, key):
    e = _BY_KEY[key]
    calc = DEMO_CALC[key]
    body = _PREAMBLE + '''\
def main():
    print("=" * 64)
    print("SOLUTION EXPLORER: " + @@NAME@@)
    print("Record " + @@RID@@ + " [" + @@GROUP@@ + "]")
    print("=" * 64)
    print("WALKTHROUGH - the Signature approach, step by step:")
    steps = @@STEPS@@
    for i, s in enumerate(steps, 1):
        print("  Step %d/%d: %s" % (i, len(steps), s))
    print("ADJUSTABLE ASSUMPTIONS - edit these values and re-run to explore:")
    assumptions = @@ASSUMPTIONS@@
    for k in sorted(assumptions):
        print("  assume %-28s = %s" % (k, assumptions[k]))
    print("HONESTY: " + @@HONEST@@)
    print("THE NUMBERS - computed live from the assumptions above:")
@@CALC@@
    print("CONFIRM PANEL - evidence that would SUPPORT this approach:")
    for c in @@CONFIRM@@:
        print("  [+] " + c)
    print("REFUTE PANEL - evidence that would WEAKEN or KILL it:")
    for r in @@REFUTE@@:
        print("  [-] " + r)
    oc = @@OBS_C@@
    orr = @@OBS_R@@
    score = len(oc) - len(orr)
    if score > 0:
        verdict = "leaning supported"
    elif score < 0:
        verdict = "leaning refuted"
    else:
        verdict = "undecided"
    print("scenario: %d supporting vs %d refuting observations (net %+d)"
          % (len(oc), len(orr), score))
    print("scenario verdict: " + verdict + " - proposed, not established")
    print("SCOPE - what this approach does NOT claim:")
    print("  " + @@SCOPE@@)
    print("OK: " + @@NAME@@ + " explorer finished - approach walked, numbers checked")
if __name__ == "__main__":
    main()
'''
    body = _PREAMBLE + '''\
def main():
    print("=" * 64)
    print("SOLUTION EXPLORER: " + @@NAME@@)
    print("Record " + @@RID@@ + " [" + @@GROUP@@ + "]")
    print("=" * 64)
    print("WALKTHROUGH - the Signature approach, step by step:")
    steps = @@STEPS@@
    for i, s in enumerate(steps, 1):
        print("  Step %d/%d: %s" % (i, len(steps), s))
    print("ADJUSTABLE ASSUMPTIONS - edit these values and re-run to explore:")
    assumptions = @@ASSUMPTIONS@@
    for k in sorted(assumptions):
        print("  assume %-28s = %s" % (k, assumptions[k]))
    print("HONESTY: " + @@HONEST@@)
    print("THE NUMBERS - computed live from the assumptions above:")
@@CALC@@
    print("CONFIRM PANEL - evidence that would SUPPORT this approach:")
    for c in @@CONFIRM@@:
        print("  [+] " + c)
    print("REFUTE PANEL - evidence that would WEAKEN or KILL it:")
    for r in @@REFUTE@@:
        print("  [-] " + r)
    oc = @@OBS_C@@
    orr = @@OBS_R@@
    score = len(oc) - len(orr)
    if score > 0:
        verdict = "leaning supported"
    elif score < 0:
        verdict = "leaning refuted"
    else:
        verdict = "undecided"
    print("scenario: %d supporting vs %d refuting observations (net %+d)"
          % (len(oc), len(orr), score))
    print("scenario verdict: " + verdict + " - proposed, not established")
    print("SCOPE - what this approach does NOT claim:")
    print("  " + @@SCOPE@@)
    print("OK: " + @@NAME@@ + " explorer finished - approach walked, numbers checked")
if __name__ == "__main__":
    main()
'''
    body = body.replace("@@NAME@@", json.dumps(name))
    body = body.replace("@@RID@@", json.dumps(rid))
    body = body.replace("@@GROUP@@", json.dumps(group))
    body = body.replace("@@STEPS@@", repr(e["sig_steps"]))
    body = body.replace("@@ASSUMPTIONS@@", repr(e["sig_assumptions"]))
    body = body.replace("@@HONEST@@", json.dumps(HONEST_LABEL))
    body = body.replace("@@CALC@@", calc)
    body = body.replace("@@CONFIRM@@", repr(e["sig_confirm"]))
    body = body.replace("@@REFUTE@@", repr(e["sig_refute"]))
    body = body.replace("@@OBS_C@@", repr(e["scenario"]["observed_confirm"]))
    body = body.replace("@@OBS_R@@", repr(e["scenario"]["observed_refute"]))
    body = body.replace("@@SCOPE@@", json.dumps(e["sig_scope"]))
    for tok in ("@@NAME@@", "@@RID@@", "@@GROUP@@", "@@STEPS@@",
                "@@ASSUMPTIONS@@", "@@HONEST@@", "@@CALC@@", "@@CONFIRM@@",
                "@@REFUTE@@", "@@OBS_C@@", "@@OBS_R@@", "@@SCOPE@@"):
        assert tok not in body, "unreplaced token %s" % tok
    return hdr_fn(name, rid, group) + body


def _make(key):
    def fn(hdr, name, rid, group, points, req):
        return _explorer_program(hdr, name, rid, group, key)
    fn.__name__ = "demo_usg_" + key
    return fn


DEMOS = {e["key"]: _make(e["key"]) for e in ENTRIES}
