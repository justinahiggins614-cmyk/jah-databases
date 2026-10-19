#!/usr/bin/env python3
"""Solution-explorer walkthrough demos, ranks 18-26."""


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + "import math\n" + body.replace(
        "NAME", __import__("json").dumps(name))


def demo_c4_convergence(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: %d independent C4 origins; test for a shared waystation order." % P["origins"])
    ws = P["waystations"]; shared = P["shared"]
    print("  waystations: %d, shared-order fraction: %.2f" % (ws, shared))
    assert shared > 0.7
    print("Step 2: Intermediates should cluster at the same waystations.")
    print("Step 3: Preconditioned non-C4 lineages must miss a predicted step.")
    print("CONFIRM if: a single dominant waystation sequence is shared across")
    print("  most origins.")
    print("REFUTE if: origins reach C4 by scrambled, lineage-specific routes")
    print("  with no shared order.")
    print("OK: %s explored the C4 convergence map" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_photorespiration(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Photorespiration wastes ~%.0f%% of photosynthetic energy." % (P["waste_fraction"] * 100))
    gain = P["bypass_gain"]; stresses = P["stresses"]
    print("Step 2: Synthetic bypasses recovered +%.0f%% biomass in field trials." % (gain * 100))
    net = gain * (1.0 - 0.1 * stresses / 4.0)
    print("  net gain after %d-stress penalty screen: %.3f" % (stresses, net))
    assert net > 0.10
    print("Step 3: Screen every bypass for loss of protective functions.")
    print("CONFIRM if: a bypass raises yield under all tested stresses with no")
    print("  protective-function penalty.")
    print("REFUTE if: every bypass shows hidden costs under some stress - the")
    print("  native pathway's inefficiency is load-bearing.")
    print("OK: %s explored the photorespiration bypass screen" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_nitrogen_fixation_cereals(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Cereal N need: %.0f kg/ha; associative fixation now: %.0f kg/ha." % (P["n_need_kg_ha"], P["fixed_kg_ha"]))
    share = P["fixed_kg_ha"] / P["n_need_kg_ha"]
    print("  current share of need: %.1f%%" % (share * 100))
    assert 0.15 < share < 0.18
    print("Step 2: Oxygen limit factor %.1f caps nitrogenase activity." % P["oxygen_limit"])
    print("Step 3: Breed exudate chemistry + engineer oxygen protection.")
    print("CONFIRM if: isotope-proven fixation supplies a substantial fraction of")
    print("  crop nitrogen across seasons.")
    print("REFUTE if: fixed nitrogen stays at a few percent regardless of")
    print("  engineering - a hard energetic ceiling.")
    print("OK: %s explored the cereal nitrogen path" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_photoprotection(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Quenching relaxes slowly: lag %.0f min wastes flicker light." % P["lag_minutes"])
    gain = P["flicker_gain"]; dmg = P["damage_index"]
    print("Step 2: Faster relaxation gained +%.0f%% biomass; damage index %.1f." % (gain * 100, dmg))
    assert 0.9 < dmg < 1.1
    print("  damage unchanged: the safety margin had headroom.")
    print("Step 3: Tune knobs per climate; verify under combined stresses.")
    print("CONFIRM if: tuned lines gain yield with damage markers indistinguishable")
    print("  from controls across stresses.")
    print("REFUTE if: yield gains always come with elevated damage under some")
    print("  stress - the margin is already optimal.")
    print("OK: %s explored photoprotection tuning" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_epigenetic_memory(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Embryonic reset erases %.0f%% of marks per generation." % (P["reset_rate"] * 100))
    gens = P["generations"]; maternal = P["maternal_share"]
    surviving = (1.0 - P["reset_rate"]) ** gens
    print("  marks surviving %d unstressed generations: %.4f" % (gens, surviving))
    assert surviving < 0.001
    print("Step 2: Maternal provisioning explains ~%.0f%% of claimed memories." % (maternal * 100))
    print("Step 3: Only embryo-rescue survivors count as true inheritance.")
    print("CONFIRM if: marks and phenotypes persist three unstressed generations")
    print("  after embryo rescue.")
    print("REFUTE if: the effect vanishes after controlling for seed provisioning.")
    print("OK: %s explored the epigenetic memory filter" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_plant_electricity(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Record electrical signatures for %d stress types." % P["signal_types"])
    acc = P["classifier_acc"]; speed = P["speed_cm_min"]
    print("  classifier accuracy: %.2f, wave speed: %.0f cm/min" % (acc, speed))
    assert acc > 0.8
    print("Step 2: The plant's own gene response must match the classifier.")
    print("Step 3: Distinct signatures = vocabulary; one alarm = broadcast.")
    print("CONFIRM if: classifiers identify the stressor from the signal alone,")
    print("  with plant responses matching.")
    print("REFUTE if: all stresses produce one indistinguishable alarm with")
    print("  specificity added later by local chemistry.")
    print("OK: %s explored the plant electrical vocabulary" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_field_efficiency_gap(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Theoretical max %.1f%%; field reality %.1f%%." % (P["theoretical"], P["field"]))
    gap = P["theoretical"] - P["field"]
    rec = P["recoverable"]
    print("  gap: %.1f%%, modeled recoverable: %.1f%%" % (gap, rec))
    assert 3.4 < gap < 3.6
    print("Step 2: Rank losses by JOINT recoverability, not alone.")
    print("Step 3: Validate top combinations with targeted field experiments.")
    print("CONFIRM if: model predictions match measured gains when combinations")
    print("  are actually built.")
    print("REFUTE if: persistent mismatch implies unknown loss terms or")
    print("  interactions dominate.")
    print("OK: %s explored the efficiency gap audit" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_rubisco_engineering(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Natural Rubisco: turnover %.1f/s, specificity %.0f." % (P["turnover"], P["specificity"]))
    gap = P["frontier_gap"]
    print("Step 2: The tradeoff frontier is the hypothesis under test.")
    print("  engineered best sits %.2f beyond the natural frontier." % gap)
    assert -0.01 < gap < 0.01
    print("  still ON the frontier: the tradeoff holds so far.")
    print("Step 3: Winners must work inside living chloroplasts, not test tubes.")
    print("CONFIRM (breakable) if: engineered variants sit clearly beyond the")
    print("  natural frontier and work in planta.")
    print("REFUTE (engineering dream) if: every functional variant lands on the")
    print("  frontier after exhaustive search - near-perfect optimization.")
    print("OK: %s explored the Rubisco frontier test" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_yield_ceilings(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Potential %.1f t/ha; best farm %.1f; global avg %.1f." % (P["potential_t_ha"], P["best_farm"], P["global_avg"]))
    farm_gap = P["potential_t_ha"] - P["best_farm"]
    print("  best-farm gap: %.1f t/ha (%.0f%% of potential)" % (farm_gap, 100 * farm_gap / P["potential_t_ha"]))
    assert 2.5 < farm_gap < 3.1
    print("Step 2: Ceilings must be distributions over weather years, not points.")
    print("Step 3: Decompose observed yields into gap components per region.")
    print("CONFIRM if: farm data track the predicted distributions and gap")
    print("  decomposition across regions.")
    print("REFUTE if: systematic divergence between modeled ceilings and the")
    print("  best real farms - missing physiology.")
    print("OK: %s explored the yield ceiling framework" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS_C = {
    "c4-convergence": demo_c4_convergence,
    "photorespiration": demo_photorespiration,
    "nitrogen-fixation-cereals": demo_nitrogen_fixation_cereals,
    "photoprotection": demo_photoprotection,
    "epigenetic-memory": demo_epigenetic_memory,
    "plant-electricity": demo_plant_electricity,
    "field-efficiency-gap": demo_field_efficiency_gap,
    "rubisco-engineering": demo_rubisco_engineering,
    "yield-ceilings": demo_yield_ceilings,
}
