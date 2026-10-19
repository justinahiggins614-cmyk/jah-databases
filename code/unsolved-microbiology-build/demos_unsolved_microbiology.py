#!/usr/bin/env python3
"""Demo programs for the Unsolved Microbiology databases (Manon's 16:15 orders, batch).

Every demo is a solution-explorer walkthrough: real, runnable, stdlib-only Python that
walks through the Signature solution approach with adjustable assumptions, prints real
computed values, runs a confirm/refute panel, asserts tight bounds (never float
exact-equality), and ends with the OK marker. All 68 are machine-executed by build.py.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_usm_plate_count_anomaly(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the plate count anomaly as a signaling failure.
    # ADJUSTABLE ASSUMPTIONS: base culturable fraction and signal-conditioned boost.
    cells_per_ml = 1.0e6
    base_frac = 0.008        # under one percent on standard plates
    colonies = cells_per_ml * base_frac
    cond_frac = 0.060        # conversation-conditioned medium
    cond_colonies = cells_per_ml * cond_frac
    improvement = cond_colonies / colonies
    print("step 1 - the anomaly: %.0f cells/ml under the microscope, %.0f colonies on plates" % (cells_per_ml, colonies))
    print("step 2 - add the chemical conversation: %.0f colonies in conditioned medium" % cond_colonies)
    print("step 3 - the gap is permission, not death: %.1f-fold more growth with signals" % improvement)
    assert 7900.0 < colonies < 8100.0, colonies
    assert 59000.0 < cond_colonies < 61000.0, cond_colonies
    assert 7.4 < improvement < 7.6, improvement
    print("CONFIRM panel: sequence the signal molecules in conditioned media; show they raise culturability across lineages.")
    print("REFUTE panel: conditioned media work with no detectable signals, or cells prove dead/dormant.")
    print("OK: %s counted the uncultured" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_viruses_alive(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the virion as dormant spore, the virocell as the living phase.
    # ADJUSTABLE ASSUMPTIONS: hours spent dormant vs active in one infection cycle.
    dormant_h = 72.0    # virion waiting in the environment
    active_h = 8.0      # virocell factory running inside the host
    total = dormant_h + active_h
    living_frac = active_h / total
    print("step 1 - the particle phase: %.0f h dormant, metabolism zero" % dormant_h)
    print("step 2 - the factory phase: %.0f h of regulated viral metabolism" % active_h)
    print("step 3 - living fraction of the cycle: %.3f - ask about the phase, not the particle" % living_frac)
    assert 0.09 < living_frac < 0.11, living_frac
    assert total == 80.0
    print("CONFIRM panel: virocells show virus-regulated metabolism across families; virocell biology predicts outcomes.")
    print("REFUTE panel: replication with no active factory phase, or metabolism fully host-run.")
    print("OK: %s phased the question" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_bacterial_species(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: dual-axis species definition - core genome AND ecological niche.
    # ADJUSTABLE ASSUMPTIONS: axis weights and the species threshold.
    ani = 0.990                       # core-genome identity
    genomic = (ani - 0.90) / 0.10     # normalized genomic score
    niche_overlap = 0.88              # ecological distinctness score
    species_score = 0.5 * genomic + 0.5 * niche_overlap
    threshold = 0.85
    print("step 1 - genomic axis: ANI %.3f -> score %.3f" % (ani, genomic))
    print("step 2 - ecological axis: niche score %.2f" % niche_overlap)
    print("step 3 - dual score %.3f vs threshold %.2f -> %s" % (species_score, threshold, "SPECIES" if species_score > threshold else "NOT"))
    assert 0.89 < genomic < 0.91, genomic
    assert 0.88 < species_score < 0.90, species_score
    assert species_score > threshold
    print("CONFIRM panel: dual criterion resolves disputed taxa and predicts phenotype better than either axis alone.")
    print("REFUTE panel: populations tight on both axes behaving as multiple species.")
    print("OK: %s drew the line twice" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_gut_unculturable(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: community-first cultivation - grow the minimal city, not the isolate.
    # ADJUSTABLE ASSUMPTIONS: per-dependency success probability and dependency count.
    p_dep = 0.15          # chance one dependency is met by luck in isolation
    k = 3                 # dependencies on neighbors/host
    p_isolate = p_dep ** k
    p_consortium = 0.85   # minimal city provides all services
    gain = p_consortium / p_isolate
    print("step 1 - isolate odds with %d dependencies: %.5f" % (k, p_isolate))
    print("step 2 - minimal-consortium odds: %.2f" % p_consortium)
    print("step 3 - community-first gain: %.1f-fold" % gain)
    assert 0.0033 < p_isolate < 0.0035, p_isolate
    assert 251.0 < gain < 253.0, gain
    print("CONFIRM panel: minimal consortia grow species never grown alone; dependency maps predict indispensable members.")
    print("REFUTE panel: species grow alone once one nutrient is found, or complete maps still fail.")
    print("OK: %s built the minimal city" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_vbnc_state(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: single-cell VBNC observatory - watch individuals, not crowds.
    # ADJUSTABLE ASSUMPTIONS: array size, true VBNC fraction, wake-signal efficacy.
    n_cells = 20000
    vbnc_frac = 0.60
    wake_eff = 0.12
    expected_revivals = n_cells * vbnc_frac * wake_eff
    contaminant_rate = 1.0e-6
    expected_fakes = n_cells * contaminant_rate
    print("step 1 - tracked cells: %d, VBNC fraction %.2f" % (n_cells, vbnc_frac))
    print("step 2 - expected true revivals at efficacy %.2f: %.0f" % (wake_eff, expected_revivals))
    print("step 3 - expected contaminant fakes: %.3f - single-cell tracking beats the crowd" % expected_fakes)
    assert 1430.0 < expected_revivals < 1450.0, expected_revivals
    assert expected_fakes < 1.0
    assert expected_revivals > 1000 * expected_fakes
    print("CONFIRM panel: reproducible single-cell revival with defined signals; wake-signal receptors identified.")
    print("REFUTE panel: zero revivals across exhaustive screens, or all revivals trace to contaminants.")
    print("OK: %s watched individuals" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_microbiome_causation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: the four-rung causation ladder - prediction, transplant, mechanism, reversibility.
    # ADJUSTABLE ASSUMPTIONS: rung scores for two candidate conditions.
    c_diff = [1, 1, 1, 1]      # C. difficile: all four rungs
    obesity = [1, 1, 0, 0]     # obesity: stuck at rung two (mouse transplant)
    s_cdiff = sum(c_diff)
    s_obesity = sum(obesity)
    print("step 1 - C. difficile ladder score: %d/4 (causal claim allowed)" % s_cdiff)
    print("step 2 - obesity ladder score: %d/4 (correlation only)" % s_obesity)
    print("step 3 - the ladder sorts the field: %d conditions cleared, %d still climbing" % (s_cdiff // 4, 1 - s_obesity // 4))
    assert s_cdiff == 4
    assert s_obesity == 2
    assert s_cdiff > s_obesity
    print("CONFIRM panel: ladder sorts known cases correctly; new rung-four successes yield real therapies.")
    print("REFUTE panel: full-ladder cases failing in humans, or causation without identifiable mechanism.")
    print("OK: %s climbed the ladder" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_healthy_microbiome(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: functional health judged against personal baselines, not population averages.
    # ADJUSTABLE ASSUMPTIONS: personal butyrate baseline and measurement noise.
    personal_mean = 15.0    # mmol/day, this person's history
    personal_sd = 1.5
    measured = 14.2
    z_personal = (measured - personal_mean) / personal_sd
    pop_mean, pop_sd = 12.0, 6.0
    z_pop = (measured - pop_mean) / pop_sd
    print("step 1 - personal z-score: %.2f (healthy if |z| < 2)" % z_personal)
    print("step 2 - population z-score: %.2f - the roster misleads, the function judges" % z_pop)
    print("step 3 - verdict: %s" % ("HEALTHY" if abs(z_personal) < 2.0 else "DEVIATED"))
    assert -0.55 < z_personal < -0.52, z_personal
    assert abs(z_personal) < 2.0
    assert 0.36 < z_pop < 0.38, z_pop
    print("CONFIRM panel: functional profiles predict disease onset across diets and geographies.")
    print("REFUTE panel: healthy people with stably broken functional profiles by every measure.")
    print("OK: %s judged the work" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_antibiotic_ecology(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: antibiotics as dose-dependent signals - words at low dose, weapons at high.
    # ADJUSTABLE ASSUMPTIONS: signaling EC50 and killing MIC for a model soil antibiotic.
    ec50_signal = 0.05   # ug/mL: half-max behavioral effect
    mic_kill = 8.0       # ug/mL: minimum inhibitory concentration
    regime_ratio = mic_kill / ec50_signal
    print("step 1 - signaling EC50: %.2f ug/mL" % ec50_signal)
    print("step 2 - killing MIC: %.1f ug/mL" % mic_kill)
    print("step 3 - regime separation: %.0f-fold - two jobs, one molecule" % regime_ratio)
    assert 159.0 < regime_ratio < 161.0, regime_ratio
    assert regime_ratio > 100.0
    print("CONFIRM panel: wild-type resistance genes tune signaling; lexicon maps predict community responses.")
    print("REFUTE panel: natural niches routinely reach killing doses, or no sub-lethal behavioral effects exist.")
    print("OK: %s read the lexicon" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_persister_cells(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: forced wake-up - open the bunker, then strike.
    # ADJUSTABLE ASSUMPTIONS: persister fraction, wake probability, antibiotic kill rate.
    total = 1.0e9
    pers_frac = 1.0e-3
    persisters = total * pers_frac
    wake_p = 0.70
    awakened = persisters * wake_p
    kill_rate = 0.999
    survivors = awakened * (1.0 - kill_rate) + persisters * (1.0 - wake_p)
    print("step 1 - persisters hiding: %.0f" % persisters)
    print("step 2 - forced awake: %.0f" % awakened)
    print("step 3 - survivors after two-step strike: %.0f (vs %.0f with drug alone)" % (survivors, persisters))
    assert 990000.0 < persisters < 1010000.0, persisters
    assert 699000.0 < awakened < 701000.0, awakened
    assert 300000.0 < survivors < 302000.0, survivors
    assert survivors < persisters
    print("CONFIRM panel: wake-key plus antibiotic sterilizes chronic models where drugs alone fail.")
    print("REFUTE panel: persisters survive full metabolic reactivation, or wake keys fuel the infection.")
    print("OK: %s opened the bunker" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_resistance_spread(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: fight the market, not the mint - block transfer at hub environments.
    # ADJUSTABLE ASSUMPTIONS: hub share of gene flow and blocker efficacy.
    hub_share = 0.80        # fraction of inter-species flow via hubs
    blocker_eff = 0.90      # flow reduction at treated hubs
    residual = (1.0 - hub_share) + hub_share * (1.0 - blocker_eff)
    reduction = 1.0 - residual
    print("step 1 - hubs carry %.0f%% of gene flow" % (hub_share * 100))
    print("step 2 - residual flow after blocking: %.2f" % residual)
    print("step 3 - market slowed by %.0f%% without killing a single cell" % (reduction * 100))
    assert 0.27 < residual < 0.29, residual
    assert 0.71 < reduction < 0.73, reduction
    print("CONFIRM panel: gene flow drops at treated hubs; fewer new resistant strains downstream.")
    print("REFUTE panel: transfer too diffuse for hubs, or rapid evolution around blockers.")
    print("OK: %s closed the market" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_antibiotic_void(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: wake the silent factories - ecological triggers for cryptic gene clusters.
    # ADJUSTABLE ASSUMPTIONS: clusters per genome, silent fraction, trigger hit rate, strains screened.
    clusters = 25
    silent_frac = 0.88
    silent = clusters * silent_frac
    hit_rate = 0.15
    awakened_per_strain = silent * hit_rate
    strains = 200
    pipeline_yield = awakened_per_strain * strains
    print("step 1 - silent clusters per genome: %.1f of %d" % (silent, clusters))
    print("step 2 - awakened per strain at hit rate %.2f: %.2f" % (hit_rate, awakened_per_strain))
    print("step 3 - pipeline yield over %d strains: %.0f awakened clusters" % (strains, pipeline_yield))
    assert 21.9 < silent < 22.1, silent
    assert 3.29 < awakened_per_strain < 3.31, awakened_per_strain
    assert 659.0 < pipeline_yield < 661.0, pipeline_yield
    print("CONFIRM panel: pipeline yields novel scaffolds yearly, including from uncultured taxa.")
    print("REFUTE panel: awakened clusters yield only known-scaffold variants.")
    print("OK: %s switched the factories on" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_fmt_mechanism(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: fractionate the toolbox - find the active agents in donor stool.
    # ADJUSTABLE ASSUMPTIONS: activity share per fraction (sums to full effect).
    fractions = {"bacteria": 0.55, "metabolites": 0.30, "viruses": 0.10, "other": 0.05}
    total = sum(fractions.values())
    minimal = fractions["bacteria"] + fractions["metabolites"]
    print("step 1 - fraction activities: " + ", ".join("%s %.2f" % kv for kv in fractions.items()))
    print("step 2 - total accounted activity: %.2f" % total)
    print("step 3 - minimal reconstitution captures %.2f of the effect" % minimal)
    assert 0.99 < total < 1.01, total
    assert 0.84 < minimal < 0.86, minimal
    print("CONFIRM panel: defined consortium matches whole-stool cure rates with dose-response.")
    print("REFUTE panel: activity vanishes on every fractionation; whole community required.")
    print("OK: %s inventoried the toolbox" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_gut_brain_axis(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: postal tracking - trace each microbial letter to its brain receptor.
    # ADJUSTABLE ASSUMPTIONS: effect share per route (vagus, blood, immune).
    routes = {"vagus_nerve": 0.35, "blood_metabolites": 0.25, "immune_signaling": 0.20}
    explained = sum(routes.values())
    unexplained = 1.0 - explained
    print("step 1 - route effects: " + ", ".join("%s %.2f" % kv for kv in routes.items()))
    print("step 2 - behavior explained by traced routes: %.2f" % explained)
    print("step 3 - blockade test: cutting vagus removes %.2f, leaving %.2f" % (routes["vagus_nerve"], explained - routes["vagus_nerve"]))
    assert 0.79 < explained < 0.81, explained
    assert 0.19 < unexplained < 0.21, unexplained
    assert explained - routes["vagus_nerve"] > 0.4
    print("CONFIRM panel: traced routes survive blockade and replicate in humans; druggable targets emerge.")
    print("REFUTE panel: effects vanish under every blockade - no traceable wires exist.")
    print("OK: %s tracked the post" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_obesity_microbes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: diet-clamped causation - hold the room's heat constant, watch the thermostat.
    # ADJUSTABLE ASSUMPTIONS: extra harvest kcal/day and trial length.
    extra_kcal_day = 120.0
    days = 30.0
    kcal_per_kg_fat = 7700.0
    extra_kcal = extra_kcal_day * days
    fat_kg = extra_kcal / kcal_per_kg_fat
    print("step 1 - extra harvest with diet fixed: %.0f kcal/day" % extra_kcal_day)
    print("step 2 - over %d days: %.0f kcal" % (days, extra_kcal))
    print("step 3 - predicted fat gain: %.3f kg - microbes move the scale or they do not" % fat_kg)
    assert 3590.0 < extra_kcal < 3610.0, extra_kcal
    assert 0.46 < fat_kg < 0.48, fat_kg
    print("CONFIRM panel: diet-fixed weight differences via microbial intervention with identified mechanism.")
    print("REFUTE panel: zero effect under strict diet control - microbes are passengers.")
    print("OK: %s clamped the diet" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_microbial_census(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: calibrate the extrapolation - measure the species-volume curve, then scale.
    # ADJUSTABLE ASSUMPTIONS: fitted curve S = c * V^z from nested-volume saturation censuses.
    c, z = 2000.0, 0.12
    ocean_L = 1.4e21
    s_ocean = c * (ocean_L ** z)
    s_1L = c * (1.0 ** z)
    print("step 1 - measured curve: S = %.0f * V^%.2f (V in liters)" % (c, z))
    print("step 2 - one liter to saturation: %.0f species" % s_1L)
    print("step 3 - scaled to the ocean: %.0f species - with honest uncertainty bars" % s_ocean)
    assert 1999.0 < s_1L < 2001.0, s_1L
    assert 6.8e5 < s_ocean < 7.0e5, s_ocean
    print("CONFIRM panel: measured curves converge on consistent global estimates with quantified uncertainty.")
    print("REFUTE panel: diversity rises without limit at every scale, or rare species collapse into artifacts.")
    print("OK: %s mapped the shoreline" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_candidate_phyla(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: host-first discovery - find the landlords, then co-culture the pair.
    # ADJUSTABLE ASSUMPTIONS: lineages surveyed, host-mapped, and co-cultured.
    lineages = 100
    host_mapped = 62
    co_cultured = 18
    map_frac = host_mapped / lineages
    culture_frac = co_cultured / host_mapped
    print("step 1 - lineages imaged in situ: %d" % lineages)
    print("step 2 - host partners identified: %d (%.0f%%)" % (host_mapped, map_frac * 100))
    print("step 3 - pairs co-cultured: %d (%.1f%% of mapped)" % (co_cultured, culture_frac * 100))
    assert 0.61 < map_frac < 0.63, map_frac
    assert 0.29 < culture_frac < 0.30, culture_frac
    print("CONFIRM panel: reproducible partnerships with metabolic exchange; dark-matter lineages finally grown.")
    print("REFUTE panel: CPR cells fully independent after all, or partners unculturable by any method.")
    print("OK: %s found the landlords" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_viral_dark_matter(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: host-first virology - a letter without an address is uninterpretable.
    # ADJUSTABLE ASSUMPTIONS: viral populations surveyed and host-assignment rate.
    populations = 5000
    assigned = 3400
    assign_frac = assigned / populations
    orphans = populations - assigned
    print("step 1 - viral populations assembled: %d" % populations)
    print("step 2 - hosts assigned via CRISPR/single-cell: %d (%.0f%%)" % (assigned, assign_frac * 100))
    print("step 3 - remaining orphans: %d - the shrinking unknown" % orphans)
    assert 0.67 < assign_frac < 0.69, assign_frac
    assert orphans == 1600
    print("CONFIRM panel: host assignments for most abundant populations; ecological roles validated.")
    print("REFUTE panel: true orphans dominate despite exhaustive methods.")
    print("OK: %s addressed the letters" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_giant_viruses(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: function-first giant virology - map the rooms, the architecture follows.
    # ADJUSTABLE ASSUMPTIONS: ORFans screened and functions assigned.
    orfans = 2000
    characterized = 350
    frac = characterized / orfans
    cellular_like = 120   # of characterized, with cellular-like physiology functions
    print("step 1 - ORFans in the screening pipeline: %d" % orfans)
    print("step 2 - functions assigned: %d (%.1f%%)" % (characterized, frac * 100))
    print("step 3 - cellular-like vs viral-process functions: %d vs %d" % (cellular_like, characterized - cellular_like))
    assert 0.17 < frac < 0.18, frac
    assert characterized - cellular_like == 230
    print("CONFIRM panel: functional patterns decisively favor one origin story - or reveal a novel biology.")
    print("REFUTE panel: ORFans uncharacterizable at scale in every assay.")
    print("OK: %s mapped the rooms" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_virus_origins(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: polyphyletic origins - different doors for different viral families.
    # ADJUSTABLE ASSUMPTIONS: per-realm winning hypothesis and its support score.
    realms = {
        "realm_A": ("virus-first", 0.72),
        "realm_B": ("escape", 0.68),
        "realm_C": ("reduction", 0.61),
        "realm_D": ("virus-first", 0.66),
    }
    scores = [s for _, s in realms.values()]
    mean_support = sum(scores) / len(scores)
    doors = len(set(h for h, _ in realms.values()))
    print("step 1 - realms reconstructed: %d" % len(realms))
    for r, (h, s) in realms.items():
        print("  %s -> %s (support %.2f)" % (r, h, s))
    print("step 2 - distinct origin doors used: %d; mean support %.3f" % (doors, mean_support))
    assert doors == 3
    assert 0.66 < mean_support < 0.68, mean_support
    assert all(0.5 < s < 1.0 for s in scores)
    print("CONFIRM panel: realms sort into distinct origin stories with dated fossil support.")
    print("REFUTE panel: all realms converge on one origin, or deep signal erased beyond recovery.")
    print("OK: %s opened every door" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_phage_decision(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: election-rule mapping - read the ballots to forecast the vote.
    # ADJUSTABLE ASSUMPTIONS: signal weights in the lysis-probability logistic model.
    a_sig, b_health, c0 = 1.5, 2.0, -0.5
    signal, health = 2.0, -1.0     # strong arbitrium signal, poor host health
    z = a_sig * signal + b_health * health + c0
    p_lysis = 1.0 / (1.0 + math.exp(-z))
    print("step 1 - signal landscape: arbitrium %.1f, host health %.1f" % (signal, health))
    print("step 2 - decision variable z = %.2f" % z)
    print("step 3 - predicted lysis probability: %.3f" % p_lysis)
    assert 0.49 < z < 0.51, z
    assert 0.62 < p_lysis < 0.63, p_lysis
    print("CONFIRM panel: signal landscapes predict community lysis-lysogeny ratios; synthetic signals steer as predicted.")
    print("REFUTE panel: decisions dominated by unmeasurable noise; signals predict nothing.")
    print("OK: %s read the ballots" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_ancient_resistome(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: paleo-functional reconstruction - read the toolbox's original manual.
    # ADJUSTABLE ASSUMPTIONS: low-dose regulatory EC50 vs high-dose shield MIC of a resurrected gene.
    ec50_tune = 0.02    # ug/mL: dose where signaling-tuning appears
    mic_shield = 16.0   # ug/mL: dose where killing is blocked
    separation = mic_shield / ec50_tune
    print("step 1 - ancient gene tunes signaling at EC50 %.2f ug/mL" % ec50_tune)
    print("step 2 - same gene shields at MIC %.1f ug/mL" % mic_shield)
    print("step 3 - separation %.0f-fold -> verdict: TUNER DRAFTED AS SHIELD" % separation)
    assert 799.0 < separation < 801.0, separation
    assert separation > 100.0
    print("CONFIRM panel: ancient genes show low-dose regulatory functions distinct from modern clinical alleles.")
    print("REFUTE panel: ancient genes identical to modern ones at all doses - always shields.")
    print("OK: %s read the old manual" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_reverse_resistance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: ratchet-mapping - find each lock, then jam its teeth.
    # ADJUSTABLE ASSUMPTIONS: fitness cost before/after compensatory mutation, generations.
    gens = 100
    w_raw = 0.92          # resistant fitness without compensation
    w_comp = 0.995        # with compensatory mutation
    freq_raw = w_raw ** gens
    freq_comp = w_comp ** gens
    print("step 1 - uncompensated resistance after %d generations: frequency %.5f (ratchet slips back)" % (gens, freq_raw))
    print("step 2 - compensated resistance after %d generations: frequency %.3f (ratchet locked)" % (gens, freq_comp))
    print("step 3 - the lock is the compensation: break it and susceptibility returns")
    assert 0.0002 < freq_raw < 0.0003, freq_raw
    assert 0.60 < freq_comp < 0.62, freq_comp
    assert freq_comp > 1000 * freq_raw
    print("CONFIRM panel: targeted interventions restore susceptibility where blanket bans failed.")
    print("REFUTE panel: every targeted reversal fails despite correct lock identification.")
    print("OK: %s jammed the ratchet" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_eukaryote_origin(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: contract-order reconstruction - eliminate scenarios experimentally.
    # ADJUSTABLE ASSUMPTIONS: viability scores per scenario after Asgard proxy tests.
    scenarios = {"syntrophy-first": 0.78, "phagocytosis-first": 0.41, "mito-early": 0.66}
    cutoff = 0.50
    survivors = {k: v for k, v in scenarios.items() if v >= cutoff}
    print("step 1 - scenario viability scores: " + ", ".join("%s %.2f" % kv for kv in scenarios.items()))
    print("step 2 - survivors above cutoff %.2f: %s" % (cutoff, ", ".join(survivors)))
    print("step 3 - %d of %d scenarios eliminated by experiment, not argument" % (len(scenarios) - len(survivors), len(scenarios)))
    assert len(survivors) == 2
    assert "phagocytosis-first" not in survivors
    assert 0.77 < survivors["syntrophy-first"] < 0.79
    print("CONFIRM panel: one scenario survives all eliminations with positive step-order evidence.")
    print("REFUTE panel: Asgard archaea incapable of any host role; all scenarios fail energetics.")
    print("OK: %s reconstructed the merger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_mito_first(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: energy-budget tribunal - audit the energy before arguing the order.
    # ADJUSTABLE ASSUMPTIONS: host ATP budget and per-feature costs (arbitrary energy units).
    budget = 1.00
    costs = {"nucleus-like": 0.50, "cytoskeleton": 0.40, "endomembranes": 0.30}
    total_cost = sum(costs.values())
    deficit = total_cost - budget
    print("step 1 - Asgard-grade host budget: %.2f units" % budget)
    print("step 2 - pre-mitochondrial complexity cost: %.2f units" % total_cost)
    print("step 3 - deficit %.2f -> verdict: %s" % (deficit, "MITOCHONDRIA-EARLY FAVORED" if deficit > 0 else "LATE VIEW SURVIVES"))
    assert 1.19 < total_cost < 1.21, total_cost
    assert 0.19 < deficit < 0.21, deficit
    assert deficit > 0
    print("CONFIRM panel: budget and gene trees converge on one order with quantified confidence.")
    print("REFUTE panel: uncertainties leave both orders feasible.")
    print("OK: %s audited the energy" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_eukaryotic_gap(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: test the jump - are synthetic halfway states viable or doomed?
    # ADJUSTABLE ASSUMPTIONS: relative growth rate of synthetic intermediates vs parent.
    parent_rate = 1.00
    halfway_rate = 0.85
    viability = halfway_rate / parent_rate
    generations = 500
    print("step 1 - synthetic halfway state grows at %.0f%% of the parent" % (viability * 100))
    print("step 2 - competition over %d generations: %s" % (generations, "PERSISTS" if viability > 0.8 else "COLLAPSES"))
    print("step 3 - viable halfway states favor extinction-over-leap; collapse favors the singular jump")
    assert 0.84 < viability < 0.86, viability
    assert viability > 0.8
    print("CONFIRM panel: genuine intermediate found alive, or synthetic halfway states proving inviable.")
    print("REFUTE panel: surveys never saturate while intermediates are merely mediocre.")
    print("OK: %s tested the jump" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_membrane_divide(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: plank-by-plank ship rebuilding - find the viable lipid transition path.
    # ADJUSTABLE ASSUMPTIONS: per-step membrane viability during stepwise remodeling.
    steps = ["backbone flip", "ester linkages", "fatty-acid chains", "full bacterial-type"]
    viabilities = [0.92, 0.85, 0.78, 0.88]
    path_viable = all(v > 0.70 for v in viabilities)
    weakest = min(viabilities)
    print("step 1 - remodeling steps: " + ", ".join(steps))
    print("step 2 - per-step viabilities: " + ", ".join("%.2f" % v for v in viabilities))
    print("step 3 - weakest plank %.2f -> path %s" % (weakest, "VIABLE" if path_viable else "BLOCKED"))
    assert 0.77 < weakest < 0.79, weakest
    assert path_viable
    print("CONFIRM panel: complete viable stepwise path from archaeal to bacterial-type membranes.")
    print("REFUTE panel: every intermediate collapses - no viable path exists.")
    print("OK: %s rebuilt the ship" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_deep_biosphere_energy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: audit the vault - every income traced, every penny accounted.
    # ADJUSTABLE ASSUMPTIONS: energy income streams vs metered community demand (energy units).
    income = {"radiolytic_H2": 40.0, "ancient_organics": 35.0, "redox_interfaces": 15.0}
    total_income = sum(income.values())
    demand = 82.0
    balance = total_income - demand
    margin = balance / demand
    print("step 1 - incomes: " + ", ".join("%s %.0f" % kv for kv in income.items()))
    print("step 2 - total income %.0f vs metered demand %.0f" % (total_income, demand))
    print("step 3 - balance %+.0f (margin %+.1f%%) -> books %s" % (balance, margin * 100, "BALANCE" if abs(margin) < 0.15 else "OPEN"))
    assert 89.0 < total_income < 91.0, total_income
    assert 0.09 < margin < 0.10, margin
    assert abs(margin) < 0.15
    print("CONFIRM panel: balanced books at multiple sites with identified dominant incomes.")
    print("REFUTE panel: persistent imbalance despite exhaustive measurement.")
    print("OK: %s audited the vault" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_microbial_carbon_pump(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: meter the refinery - track carbon from uptake to recalcitrant output.
    # ADJUSTABLE ASSUMPTIONS: labeled carbon input, recalcitrant fraction, warming response.
    labeled = 1000.0
    recalc_frac = 0.18
    recalcitrant = labeled * recalc_frac
    warming_delta = 0.03    # extra recalcitrant fraction per +2C in this regime
    warmed_frac = recalc_frac + warming_delta
    print("step 1 - labeled carbon in: %.0f units" % labeled)
    print("step 2 - recalcitrant out: %.0f units (fraction %.2f)" % (recalcitrant, recalc_frac))
    print("step 3 - at +2C: fraction %.2f - the pump %s with warming here" % (warmed_frac, "STRENGTHENS" if warmed_frac > recalc_frac else "WEAKENS"))
    assert 179.0 < recalcitrant < 181.0, recalcitrant
    assert 0.20 < warmed_frac < 0.22, warmed_frac
    print("CONFIRM panel: consistent production functions; pump-inclusive models beat pump-free ones.")
    print("REFUTE panel: recalcitrant production indistinguishable from background.")
    print("OK: %s metered the refinery" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_methane_budget(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: audit both bookkeepers together - paired guild measurement.
    # ADJUSTABLE ASSUMPTIONS: methanogenesis vs methane oxidation at a matched wetland site.
    production = 500.0    # Tg-scale arbitrary flux units
    oxidation = 380.0
    net = production - oxidation
    sink_frac = oxidation / production
    print("step 1 - methanogen checks written: %.0f" % production)
    print("step 2 - methanotroph checks cashed: %.0f (%.0f%% intercepted)" % (oxidation, sink_frac * 100))
    print("step 3 - net flux to atmosphere: %.0f - observed, not subtracted" % net)
    assert 119.0 < net < 121.0, net
    assert 0.75 < sink_frac < 0.77, sink_frac
    print("CONFIRM panel: budget closes within uncertainty; surges attributed to specific guild responses.")
    print("REFUTE panel: paired measurements still too uncertain; fingerprints cannot resolve sources.")
    print("OK: %s balanced the ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_permafrost_carbon(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: watch each thaw shift clock in - gradual vs abrupt, guild by guild.
    # ADJUSTABLE ASSUMPTIONS: 21st-century emissions from gradual vs abrupt thaw (PgC).
    gradual = 2.1
    abrupt = 1.4
    total = gradual + abrupt
    abrupt_share = abrupt / total
    print("step 1 - gradual thaw emissions: %.1f PgC" % gradual)
    print("step 2 - abrupt thaw emissions: %.1f PgC" % abrupt)
    print("step 3 - total %.1f PgC; abrupt share %.0f%% - the unmodeled shift matters" % (total, abrupt_share * 100))
    assert 3.49 < total < 3.51, total
    assert 0.39 < abrupt_share < 0.41, abrupt_share
    print("CONFIRM panel: microbial-process models predict new-site emissions better than pool-decay models.")
    print("REFUTE panel: guild activity unpredictable from thaw state at every site.")
    print("OK: %s clocked the shifts" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_nitrogen_budget(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: meters on every workstation - assemble the budget from measured flows.
    # ADJUSTABLE ASSUMPTIONS: nitrogen input vs summed measured outputs (Tg N / yr).
    inputs = 200.0
    outputs = {"denitrification": 110.0, "anammox": 45.0, "n2o_leak": 18.0, "burial": 22.0}
    total_out = sum(outputs.values())
    gap = inputs - total_out
    gap_frac = gap / inputs
    print("step 1 - measured outputs: " + ", ".join("%s %.0f" % kv for kv in outputs.items()))
    print("step 2 - outputs %.0f vs inputs %.0f" % (total_out, inputs))
    print("step 3 - gap %.0f (%.1f%%) -> budget %s" % (gap, gap_frac * 100, "CLOSED" if gap_frac < 0.05 else "OPEN"))
    assert 194.0 < total_out < 196.0, total_out
    assert 0.02 < gap_frac < 0.03, gap_frac
    assert gap_frac < 0.05
    print("CONFIRM panel: flow-based budget closes; N2O rise attributed to specific processes.")
    print("REFUTE panel: flows too heterogeneous to generalize beyond individual fields.")
    print("OK: %s metered the workstations" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_luca_nature(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: edit-aware restoration - separate original text from scribal edits.
    # ADJUSTABLE ASSUMPTIONS: candidate genes, transfer-flagged genes, retained core.
    candidates = 500
    transfer_flagged = 145
    retained = candidates - transfer_flagged
    retention = retained / candidates
    print("step 1 - candidate LUCA genes: %d" % candidates)
    print("step 2 - flagged as later transfers: %d" % transfer_flagged)
    print("step 3 - cleaned ancestral core: %d genes (retention %.0f%%)" % (retained, retention * 100))
    assert retained == 355
    assert 0.70 < retention < 0.72, retention
    print("CONFIRM panel: cleaned gene set yields a coherent, experimentally viable organism model.")
    print("REFUTE panel: cleaning leaves too few genes for any coherent metabolism.")
    print("OK: %s restored the manuscript" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_open_pangenome(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: learn the library's rules - track gene circulation in real time.
    # ADJUSTABLE ASSUMPTIONS: discovery curve S(n) = base + k * n^alpha (power-law openness).
    base, k, alpha = 3000.0, 800.0, 0.35
    n1, n2 = 100, 1000
    s1 = base + k * (n1 ** alpha)
    s2 = base + k * (n2 ** alpha)
    growth = s2 - s1
    print("step 1 - pan-genome at %d genomes: %.0f gene families" % (n1, s1))
    print("step 2 - at %d genomes: %.0f gene families" % (n2, s2))
    print("step 3 - still growing by %.0f families - the library %s" % (growth, "STAYS OPEN" if growth > 1000 else "CLOSES"))
    assert 7000.0 < s1 < 7020.0, s1
    assert 11970.0 < s2 < 11985.0, s2
    assert growth > 4000.0
    print("CONFIRM panel: circulation rules predict persistence; curves flatten or hold under unbiased sampling.")
    print("REFUTE panel: curves always reflect sampling effort - openness is artifact.")
    print("OK: %s learned the library rules" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usm_tree_or_web(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SOLUTION EXPLORER: frequency decomposition - measure the tree-signal vs transfer-signal spectrum.
    # ADJUSTABLE ASSUMPTIONS: tree-congruence scores per gene class.
    congruence = {"informational": 0.82, "operational": 0.45, "mobile": 0.12}
    tree_like = congruence["informational"]
    web_like = 1.0 - congruence["mobile"]
    spread = max(congruence.values()) - min(congruence.values())
    print("step 1 - congruence by class: " + ", ".join("%s %.2f" % kv for kv in congruence.items()))
    print("step 2 - tree-signal %.2f in informational genes; web-signal %.2f in mobile genes" % (tree_like, web_like))
    print("step 3 - spectrum spread %.2f - neither pure tree nor pure web" % spread)
    assert 0.69 < spread < 0.71, spread
    assert tree_like > 0.8
    assert congruence["mobile"] < 0.2
    print("CONFIRM panel: stable reproducible spectrum showing where tree vs web thinking applies.")
    print("REFUTE panel: congruence proves method-dependent; every metric disagrees.")
    print("OK: %s decomposed the signal" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
 "plate-count-anomaly": demo_usm_plate_count_anomaly,
 "viruses-alive": demo_usm_viruses_alive,
 "bacterial-species": demo_usm_bacterial_species,
 "gut-unculturable": demo_usm_gut_unculturable,
 "vbnc-state": demo_usm_vbnc_state,
 "microbiome-causation": demo_usm_microbiome_causation,
 "healthy-microbiome": demo_usm_healthy_microbiome,
 "antibiotic-ecology": demo_usm_antibiotic_ecology,
 "persister-cells": demo_usm_persister_cells,
 "resistance-spread": demo_usm_resistance_spread,
 "antibiotic-void": demo_usm_antibiotic_void,
 "fmt-mechanism": demo_usm_fmt_mechanism,
 "gut-brain-axis": demo_usm_gut_brain_axis,
 "obesity-microbes": demo_usm_obesity_microbes,
 "microbial-census": demo_usm_microbial_census,
 "candidate-phyla": demo_usm_candidate_phyla,
 "viral-dark-matter": demo_usm_viral_dark_matter,
 "giant-viruses": demo_usm_giant_viruses,
 "virus-origins": demo_usm_virus_origins,
 "phage-decision": demo_usm_phage_decision,
 "ancient-resistome": demo_usm_ancient_resistome,
 "reverse-resistance": demo_usm_reverse_resistance,
 "eukaryote-origin": demo_usm_eukaryote_origin,
 "mito-first": demo_usm_mito_first,
 "eukaryotic-gap": demo_usm_eukaryotic_gap,
 "membrane-divide": demo_usm_membrane_divide,
 "deep-biosphere-energy": demo_usm_deep_biosphere_energy,
 "microbial-carbon-pump": demo_usm_microbial_carbon_pump,
 "methane-budget": demo_usm_methane_budget,
 "permafrost-carbon": demo_usm_permafrost_carbon,
 "nitrogen-budget": demo_usm_nitrogen_budget,
 "luca-nature": demo_usm_luca_nature,
 "open-pangenome": demo_usm_open_pangenome,
 "tree-or-web": demo_usm_tree_or_web,
}
