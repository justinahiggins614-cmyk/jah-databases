#!/usr/bin/env python3
"""Solution-explorer walkthrough demos, ranks 27-34."""


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + "import math\n" + body.replace(
        "NAME", __import__("json").dumps(name))


def demo_c4_rice(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: %d candidate traits; %d installed so far." % (P["traits"], P["installed"]))
    gain = P["gain_pct"]
    print("Step 2: Current stack gain: +%.0f%%; rank next traits by flux gain per cost." % gain)
    assert gain > 0
    marginal = [4.0, 2.5, 1.2, 0.4, 0.1]
    print("Step 3: Marginal gains of next traits: %s" % marginal)
    assert marginal == sorted(marginal, reverse=True)
    print("  stop adding complexity when marginal gains vanish.")
    print("CONFIRM if: a defined minimal stack produces measurable C4-like carbon")
    print("  concentration and yield gain.")
    print("REFUTE if: gains require nearly the full natural complexity - no")
    print("  shortcut exists.")
    print("OK: %s explored the minimal C4 stack" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_longevity_genome(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Conifer genome %.0f Gb; require %d independent signatures." % (P["genome_gb"], P["signatures"]))
    cand = P["candidates"]
    print("Step 2: Intersection of expansion + expression + low mutation: %d candidates." % cand)
    assert cand > 0
    print("Step 3: Test top candidates by overexpression in fast-cycling models.")
    print("CONFIRM if: candidates pass all three genomic signatures and show")
    print("  protective phenotypes in models.")
    print("REFUTE if: no enrichment of maintenance genes in the longest-lived")
    print("  lineages - longevity is mostly ecological.")
    print("OK: %s explored the longevity genome triangulation" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_land_plant_origins(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Land invasion ~%.0f Mya; %d key innovations to order." % (P["mya"], P["innovations"]))
    pre = P["preadapted"]
    print("Step 2: %d of %d innovations have algal precursors (pre-adapted)." % (pre, P["innovations"]))
    assert pre > P["innovations"] / 2
    print("Step 3: Express ancestral-state genes in modern algae under desiccation.")
    print("CONFIRM (pre-adaptation) if: algal genes confer land-like stress")
    print("  tolerance when tested.")
    print("REFUTE if: key innovations require novel genes with no algal")
    print("  precursors - true invention on land.")
    print("OK: %s explored the land invasion reconstruction" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_endosymbiosis(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: %d genes retained in chloroplast; %d moved to nucleus." % (P["retained"], P["transferred"]))
    core = P["redox_core"]
    frac = core / P["retained"]
    print("  redox-regulatory core: %d (%.0f%% of retained)" % (core, frac * 100))
    assert 0.5 < frac < 0.75
    print("Step 2: Relocate a retained gene to the nucleus with proper targeting.")
    print("Step 3: Test under fluctuating light - the redox stress test.")
    print("CONFIRM if: relocated redox genes fail under fluctuating light while")
    print("  non-redox relocations succeed.")
    print("REFUTE if: clean relocation of the entire retained set with no")
    print("  regulatory cost - retention is historical accident.")
    print("OK: %s explored the endosymbiosis retention test" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_synthetic_chloroplast(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Candidate part list: %d parts, of which %d are repair." % (P["parts"], P["repair_parts"]))
    stages = P["stages"]
    print("Step 2: Build in %d stages: electron flow -> carbon fixation -> repair." % stages)
    assert stages == 3
    print("Step 3: Each stage must PERSIST before the next is added.")
    print("  a photosystem without repair dies within hours in light.")
    print("CONFIRM if: a staged system reaches persistent light-driven carbon")
    print("  fixation.")
    print("REFUTE if: repair machinery proves irreducibly complex, with no")
    print("  stable intermediate stages.")
    print("OK: %s explored the synthetic chloroplast staging" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_photosynthesis_optimization(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: %d pipeline steps; optimize %d trait knobs jointly." % (P["steps"], P["traits"]))
    yrs = P["ensemble_years"]
    print("Step 2: Optimize over %d-year weather ensembles per region." % yrs)
    plateau = [1.00, 0.99, 0.985, 0.97]
    print("  near-optimum designs: %s (broad plateau = engineerable)" % plateau)
    assert plateau[0] - plateau[-1] < 0.05
    print("Step 3: Build top-ranked trait stacks; measure in the field.")
    print("CONFIRM if: stacked lines match model-predicted gains across weather")
    print("  years.")
    print("REFUTE if: persistent prediction failures imply unmodeled interactions")
    print("  dominate.")
    print("OK: %s explored the photosynthesis joint optimum" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_denovo_photosynthesizer(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: %d genes in the model cyanobacterium; %d essential in constant light." % (P["genes"], P["essential"]))
    frac = P["essential"] / P["genes"]
    print("  essential fraction: %.1f%%" % (frac * 100))
    assert 0.15 < frac < 0.22
    print("Step 2: Essentiality is condition-specific: state the environment.")
    print("Step 3: Synthesize the reduced genome and boot it up.")
    assert P["booted"] == 1
    print("CONFIRM if: a booted minimal strain grows photosynthetically with a")
    print("  fully annotated gene list.")
    print("REFUTE if: essentiality is so condition-dependent that no stable")
    print("  minimal set exists.")
    print("OK: %s explored the minimal photosynthesizer" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_plant_consciousness(hdr, name, rid, group, P):
    pinject = "P = %s\n" % __import__("json").dumps(P)
    return _wrap(hdr, name, rid, group, pinject + '''\
def main():
    print("SOLUTION EXPLORER: " + NAME)
    print("Step 1: Replace 'consciousness' with a %d-rung capacity ladder." % P["rungs"])
    cleared = P["cleared"]
    print("Step 2: Plants clear rung %d of %d (double-blind: %s)." % (cleared, P["rungs"], bool(P["blinded"])))
    assert 0 < cleared < P["rungs"]
    print("Step 3: Philosophers state IN ADVANCE which rung changes their verdict.")
    print("Step 4: Publish behavioral results and verdicts together.")
    print("CONFIRM (progress) if: plants clear rungs the skeptics said they could")
    print("  not, with criteria agreed in advance.")
    print("REFUTE (strong claim) if: plants stall at integration with no flexible")
    print("  self-modeling under any paradigm.")
    print("OK: %s explored the consciousness capacity ladder" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS_D = {
    "c4-rice": demo_c4_rice,
    "longevity-genome": demo_longevity_genome,
    "land-plant-origins": demo_land_plant_origins,
    "endosymbiosis": demo_endosymbiosis,
    "synthetic-chloroplast": demo_synthetic_chloroplast,
    "photosynthesis-optimization": demo_photosynthesis_optimization,
    "denovo-photosynthesizer": demo_denovo_photosynthesizer,
    "plant-consciousness": demo_plant_consciousness,
}
