#!/usr/bin/env python3
"""Solution-explorer walkthrough demos, ranks 10-17."""


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + "import math\n" + body.replace(
        "NAME", __import__("json").dumps(name))


def demo_wood_wide_web(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: The question is quantitative: transfer as fraction of budget.")
    tf = P["transfer_fraction"]; thr = P["budget_threshold"]; n = P["plots"]
    print("  measured transfer: %.3f of receiver budget (n=%d plots)" % (tf, n))
    print("  meaningful-sharing bar: %.2f" % thr)
    print("Step 2: Seedling pots cannot settle an adult-forest question.")
    assert tf < thr
    print("  current field number sits BELOW the meaningful bar.")
    print("Step 3: Run isotope labeling on mature trees, severed-network controls.")
    print("CONFIRM (sharing) if: transfers exceed a few percent of receiver")
    print("  budgets, concentrated toward shaded kin seedlings.")
    print("REFUTE (sharing) if: transfers stay below a tenth of a percent in")
    print("  every mature-forest test - networks serve fungus-to-host nutrition.")
    print("OK: %s explored the wood wide web audit" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_plant_cognition(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Separate abilities (testable) from labels (philosophical).")
    tests = P["tests"]; bar = P["pass_bar"]; sp = P["species"]
    print("  battery: %d tests, pass bar %d, %d species, double-blind" % (tests, bar, sp))
    passed = 4
    print("Step 2: Suppose plants pass %d of %d pre-registered tests." % (passed, tests))
    assert passed < bar
    print("  below the bar: strong cognition claim not supported here.")
    print("Step 3: Criteria are pre-registered so results are interpreted, not renegotiated.")
    print("CONFIRM (cognitive-level) if: plants pass pre-registered tests that")
    print("  current physiological models cannot produce.")
    print("REFUTE (strong claim) if: every behavior decomposes into known")
    print("  signal-response pathways with no residual flexibility.")
    print("OK: %s explored the cognition test battery" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ascent_of_sap(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: A %.0f m tree holds water at %.1f MPa tension." % (P["height_m"], P["tension_mpa"]))
    emb = P["embolism_pct"]
    print("  drought embolism: %.0f%% of vessels air-filled" % emb)
    assert 10.0 < emb < 30.0
    print("Step 2: Refilling under tension is impossible by bulk flow -")
    print("  so repair must be local and cellular.")
    print("Step 3: Micro-CT imaging pairs refilling vessels with osmotic signatures.")
    print("CONFIRM if: refilling vessels consistently pair with local osmotic")
    print("  activity in neighboring parenchyma.")
    print("REFUTE if: refilling occurs with no local cellular signature, or")
    print("  species survive without ever refilling - tolerance is avoidance.")
    print("OK: %s explored the embolism-repair question" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_hormone_crosstalk(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: %d hormones, hypothesize %d integrator hubs." % (P["hormones"], P["hubs"]))
    triples = P["triples_tested"]
    print("Step 2: Fit the directed network on pairs; predict unseen triples.")
    print("  triple perturbations tested: %d" % triples)
    hits = 34
    acc = hits / triples
    print("  predicted correctly: %d/%d = %.2f" % (hits, triples, acc))
    assert 0.8 < acc < 0.9
    print("Step 3: Hubs like DELLA and MYC2 should dominate the wiring.")
    print("CONFIRM if: triple-hormone responses are accurately predicted across")
    print("  tissues from the hub model.")
    print("REFUTE if: interactions rewire unpredictably with every new condition -")
    print("  no stable mappable network exists.")
    print("OK: %s explored the hormone crosstalk map" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_plant_immunity(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: %d NLR detectors per genome; most targets unknown." % P["nlr_genes"])
    pyr = P["pyramid"]; seasons = P["seasons"]
    print("Step 2: Pyramid %d conserved-target detectors; challenge %d seasons." % (pyr, seasons))
    escape_single = 0.6
    escape_pyramid = escape_single ** pyr
    print("  escape prob single: %.2f -> pyramid: %.4f" % (escape_single, escape_pyramid))
    assert escape_pyramid < 0.14
    print("Step 3: Durability = aiming at targets the pathogen cannot change.")
    print("CONFIRM if: pyramided lines hold resistance for many pathogen")
    print("  generations while single-detector lines fall.")
    print("REFUTE if: pathogens escape even conserved-target detectors rapidly -")
    print("  durability needs a different principle.")
    print("OK: %s explored durable plant immunity" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_root_microbiome(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: %d taxa in the rhizosphere; hunt the keystone core." % P["taxa"])
    core = P["core_size"]; plots = P["field_plots"]
    print("Step 2: Dropout synthesis: remove functional groups one at a time.")
    print("  candidate core: %d strains, field plots: %d" % (core, plots))
    full, minimal = 1.00, 0.93
    print("  full community effect: %.2f, minimal core: %.2f" % (full, minimal))
    assert minimal > 0.9 * full
    print("Step 3: The core must reproduce the effect in REAL field soil.")
    print("CONFIRM if: a small defined consortium matches whole-microbiome")
    print("  performance in the field.")
    print("REFUTE if: effects vanish whenever any of hundreds of taxa are")
    print("  removed - irreducible whole-community function.")
    print("OK: %s explored the root microbiome core" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mycorrhizal_functions(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Treat the symbiosis as a biological market.")
    rate = P["exchange_rate"]; partners = P["partners"]; sanc = P["sanction"]
    print("  baseline exchange rate %.1f across %d fungal partners" % (rate, partners))
    print("Step 2: Manipulate supply ratios; signals should encode prices.")
    shocked = rate * (1.0 - sanc)
    print("  cheater sanction cuts exchange to %.2f" % shocked)
    assert 0.45 < shocked < 0.55
    print("Step 3: Signal levels must predict exchange-rate adjustments.")
    print("CONFIRM if: signals quantitatively track exchange rates and shift with")
    print("  supply ratios.")
    print("REFUTE if: fixed exchange ratios regardless of signals - the")
    print("  conversation is ceremonial, not regulatory.")
    print("OK: %s explored the mycorrhizal market" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_drought_genetics(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: %d QTLs -> compress into %d functional modules." % (P["qtls"], P["modules"]))
    combos = P["combos"]
    print("Step 2: Build %d module-combination lines in a common background." % combos)
    pred_acc = 0.88
    print("  modular model predicts untested combos at accuracy %.2f" % pred_acc)
    assert 0.8 < pred_acc < 0.95
    print("Step 3: Phenotype under managed field drought WITH heat.")
    print("CONFIRM if: new combinations are accurately predicted from module")
    print("  parameters.")
    print("REFUTE if: pervasive cross-module epistasis defeats every modular")
    print("  prediction - irreducible whole-genome context.")
    print("OK: %s explored the drought architecture" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS_B = {
    "wood-wide-web": demo_wood_wide_web,
    "plant-cognition": demo_plant_cognition,
    "ascent-of-sap": demo_ascent_of_sap,
    "hormone-crosstalk": demo_hormone_crosstalk,
    "plant-immunity": demo_plant_immunity,
    "root-microbiome": demo_root_microbiome,
    "mycorrhizal-functions": demo_mycorrhizal_functions,
    "drought-genetics": demo_drought_genetics,
}
