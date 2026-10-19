#!/usr/bin/env python3
"""Entries 10-19 (compounded tier) for the Unsolved Geology databases."""

ENTRIES_10_19 = [
# ---------------------------------------------------------------- 10
{
 "key": "onset-tectonics",
 "name": "Which Rocks Mark the Start of Plate Tectonics?",
 "group": "Tectonics",
 "ladder_rank": 10, "ladder_tier": "compounded",
 "problem": ("Plate tectonics runs Earth today, but the rock record disagrees about "
             "when it started: estimates range from over 4 billion to under 1 "
             "billion years ago. Geologists read the same ancient rocks and reach "
             "opposite conclusions."),
 "background": ("The evidence is indirect. Ophiolites - slices of ancient ocean "
             "floor thrust onto continents - appear as far back as 2 billion years "
             "and arguably 3.8 billion, suggesting seafloor spreading. Blueschists, "
             "which need cold, deep subduction, are rare before about 800 million "
             "years ago, suggesting modern-style subduction is young. Zircon trace "
             "elements hint at subduction-like magmas 4 billion years ago, while "
             "thermal models argue the hot early mantle could not sustain rigid "
             "plates and Earth ran a stagnant lid instead. The dispute is partly "
             "definitional: a planet can recycle crust without modern plates, so "
             "the question is really which rock assemblage counts as proof - and "
             "no definition commands consensus."),
 "why_it_matters": ("The onset of plate tectonics is the onset of the modern Earth "
             "system: stable continents, the carbon cycle, and the climate "
             "thermostat all depend on it. Dating it decides whether early life "
             "evolved on a stagnant-lid world or a plate-tectonic one - two "
             "completely different planets."),
 "sig_pointer": ("The Signature system proposes a proof-standard program: define "
             "in advance which rock assemblages count as tectonic proof, then date "
             "their first appearance without moving the goalposts. See the "
             "Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the onset debate as a "
             "standards problem - and proposes fixing the definition of proof "
             "before arguing about the date."),
 "signature_solution": (
     "Proposed approach. Step 1: convene the competing camps to pre-register a "
     "proof standard - the exact assemblage (for example ophiolite plus sheeted "
     "dikes plus paired metamorphic belt) that counts as plate-tectonic evidence, "
     "with the standard locked before any dating. Step 2: apply the standard "
     "blind to the global Precambrian rock catalog: independent teams score each "
     "candidate terrane pass or fail without knowing its age. Step 3: date only "
     "the terranes that pass, and plot first appearance against the thermal "
     "evolution models that predict when plates became possible. Step 4: publish "
     "the disagreements - terranes where teams split - as the honest uncertainty "
     "map.\n"
     "Assumptions: that a proof standard can be agreed in advance (the hardest "
     "step - careers are built on the current ambiguity); that ancient "
     "assemblages are not so deformed that scoring is meaningless; that thermal "
     "models bound the possible rather than dictating it.\n"
     "What would confirm it: blind scoring converging on a first-appearance date "
     "that survives the disagreement map, with thermal models consistent rather "
     "than contradictory.\n"
     "What would kill it: blind teams splitting on nearly every terrane - proof "
     "the rocks cannot bear the question - or the agreed standard excluding "
     "evidence everyone privately trusts.\n"
     "What this does NOT claim: it does not claim a single global start date "
     "exists; it does not claim stagnant-lid Earth was lifeless; it is not "
     "established science."),
 "citations": [
     "Stern R J. The evolution of plate tectonics. Phil Trans R Soc A; 2018.",
     "Korenaga J. Initiation and evolution of plate tectonics on Earth. Annu Rev Earth Planet Sci; 2013.",
     "Palin R M, Santosh M. Plate tectonics: what, where, why, and when? Gondwana Res; 2021."],
 "explorer": {
   "blurb": ("An onset-estimate visualizer: it plots the rival start dates "
             "against mantle temperature curves, showing how much of the "
             "disagreement is definitional."),
   "assumptions": {"oldest_claim_Ga": 4.0, "youngest_claim_Ga": 0.8,
                   "mantle_cooling_C_per_Ga": 100.0, "plate_threshold_C": 150.0},
   "model_src": (
     "def run(A):\n"
     "    span_Ga = A[\"oldest_claim_Ga\"] - A[\"youngest_claim_Ga\"]\n"
     "    temp_drop = span_Ga * A[\"mantle_cooling_C_per_Ga\"]\n"
     "    midpoint_Ga = (A[\"oldest_claim_Ga\"] + A[\"youngest_claim_Ga\"]) / 2.0\n"
     "    return {\"disagreement_span_Ga\": span_Ga,\n"
     "            \"mantle_cooling_over_span_C\": temp_drop,\n"
     "            \"midpoint_estimate_Ga\": midpoint_Ga}\n"),
   "steps": [("Span of rival onset estimates", "disagreement_span_Ga", "Ga"),
             ("Mantle cooling across that span", "mantle_cooling_over_span_C", "C"),
             ("Midpoint of the rival claims", "midpoint_estimate_Ga", "Ga")],
   "confirm": ["Blind scoring converges on a first-appearance date surviving the disagreement map.",
               "Thermal models are consistent with the converged date."],
   "refute": ["Blind teams split on nearly every terrane, or the agreed standard excludes trusted evidence."],
   "checks": [("disagreement_span_Ga", 2.0, 4.0),
              ("mantle_cooling_over_span_C", 200.0, 400.0),
              ("midpoint_estimate_Ga", 1.5, 3.0)],
   "honesty": ("We do not know when plate tectonics started; this explorer only "
               "measures how wide the disagreement is, in billions of years and "
               "in degrees of mantle cooling.")}
},
# ---------------------------------------------------------------- 11
{
 "key": "great-unconformity",
 "name": "What Caused the Great Unconformity?",
 "group": "Stratigraphy",
 "ladder_rank": 11, "ladder_tier": "compounded",
 "problem": ("Across North America and on other continents, half-billion-year-old "
             "sediments sit directly on billion-year-old basement - a gap of up to "
             "a billion years with the rock record simply missing. Powell named it "
             "the Great Unconformity in 1869, and its cause is still contested."),
 "background": ("An unconformity is a buried erosion surface, and the Great "
             "Unconformity is the largest: in the Grand Canyon, the 525-million-"
             "year-old Tapeats Sandstone rests on 1.7-billion-year-old Vishnu "
             "basement, and similar gaps appear from the Ozarks to Scandinavia. "
             "Two rival explanations dominate. The Snowball Earth hypothesis says "
             "global glaciations around 700 million years ago scoured continents "
             "bare with kilometers of ice. The supercontinent-breakup hypothesis "
             "says the rifting of Rodinia uplifted continents, and rivers and "
             "weathering stripped them. Thermochronology shows the basement cooled "
             "- was exhumed - roughly in the right window for both, and each "
             "hypothesis explains some localities better than others."),
 "why_it_matters": ("The gap erases the record of the most interesting billion "
             "years in Earth history - the run-up to complex life. Whatever "
             "stripped the continents also reset landscapes, delivered nutrients "
             "to the oceans, and may have helped trigger the Cambrian explosion. "
             "It is erosion on a planetary scale, and we do not know what drove "
             "it."),
 "sig_pointer": ("The Signature system proposes an exhumation-timing survey: date "
             "the cooling of basement beneath the unconformity on every continent "
             "and test whether it was synchronous (glaciation) or diachronous "
             "(rifting). See the Signature Edition record for the full labeled "
             "proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the missing billion "
             "years as a timing question - and proposes that synchrony versus "
             "sequence is the test that separates the rival causes."),
 "signature_solution": (
     "Proposed approach. Step 1: compile thermochronology (apatite and zircon "
     "helium ages) from basement directly beneath the Great Unconformity on all "
     "continents where it is exposed, with uniform lab protocols. Step 2: build "
     "an exhumation timeline per continent - when did each basement cool through "
     "each temperature? Step 3: test synchrony - the Snowball hypothesis "
     "predicts globally synchronous exhumation around 700 to 650 million years; "
     "the rifting hypothesis predicts exhumation sweeping with Rodinias breakup "
     "over 200 million years. Step 4: check the sediment sink - the eroded "
     "billion years of rock went somewhere, so the predicted sediment volumes "
     "must appear in Neoproterozoic basins.\n"
     "Assumptions: that helium ages record exhumation rather than later "
     "reheating (a chronic ambiguity); that the unconformity on different "
     "continents is the same event and not several; that sediment volumes can be "
     "reconstructed from surviving basins.\n"
     "What would confirm it: exhumation synchronous within dating error on "
     "multiple continents (glaciation wins), or a clear time-transgressive sweep "
     "(rifting wins), plus matching sediment volumes.\n"
     "What would kill it: exhumation ages scattering with no pattern, or "
     "sediment budgets an order of magnitude short of the eroded volume.\n"
     "What this does NOT claim: it does not claim the two hypotheses are "
     "mutually exclusive; it does not date Snowball Earth from the unconformity "
     "alone; it is not established science."),
 "citations": [
     "Keller C B et al. Neoproterozoic glacial origin of the Great Unconformity. PNAS; 2019.",
     "Flowers R M et al. Diachronous Great Unconformity exhumation. Geology; 2020.",
     "Powell J W. Exploration of the Colorado River of the West. Smithsonian; 1875."],
 "explorer": {
   "blurb": ("An erosion-volume calculator: from the missing time and continental "
             "area it estimates how much rock vanished, and what ice versus rivers "
             "would have to remove."),
   "assumptions": {"gap_Ma": 1000.0, "area_km2": 5000000.0,
                   "mean_erosion_mm_yr_glacial": 1.0, "mean_erosion_mm_yr_fluvial": 0.05},
   "model_src": (
     "def run(A):\n"
     "    gap_yr = A[\"gap_Ma\"] * 1e6\n"
     "    glacial_m = A[\"mean_erosion_mm_yr_glacial\"] / 1000.0 * gap_yr\n"
     "    fluvial_m = A[\"mean_erosion_mm_yr_fluvial\"] / 1000.0 * gap_yr\n"
     "    volume_km3 = A[\"area_km2\"] * glacial_m / 1000.0\n"
     "    return {\"glacial_erosion_m\": glacial_m, \"fluvial_erosion_m\": fluvial_m,\n"
     "            \"glacial_volume_km3\": volume_km3}\n"),
   "steps": [("Rock removed by glacial rates over 1 Gyr", "glacial_erosion_m", "m"),
             ("Rock removed by fluvial rates over 1 Gyr", "fluvial_erosion_m", "m"),
             ("Implied sediment volume (glacial case)", "glacial_volume_km3", "km3")],
   "confirm": ["Exhumation is synchronous across continents (glaciation) or a clean time-transgressive sweep (rifting).",
               "Neoproterozoic basins hold the predicted sediment volumes."],
   "refute": ["Exhumation ages scatter with no pattern, or sediment budgets fall an order of magnitude short."],
   "checks": [("glacial_erosion_m", 500000.0, 2000000.0),
              ("fluvial_erosion_m", 20000.0, 100000.0),
              ("glacial_volume_km3", 1e9, 1e10)],
   "honesty": ("We do not know what stripped the continents; this explorer only "
               "converts the missing time into missing rock volumes, which any "
               "cause must be able to move.")}
},
# ---------------------------------------------------------------- 12
{
 "key": "supercontinent-mechanics",
 "name": "Why Do Supercontinents Assemble and Break Apart?",
 "group": "Geodynamics",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": ("Earths continents have gathered into supercontinents - Rodinia, "
             "Pannotia, Pangea - and broken apart again, several times. Whether "
             "the cycle is driven by the mantle below or the plates themselves, "
             "and why it repeats, is unresolved."),
 "background": ("Pangea assembled about 335 million years ago and began rifting "
             "200 million years ago; Rodinia assembled around 1 billion years ago "
             "and broke up around 750 million years ago. Two end-member engines "
             "compete. In the top-down view, subduction zones ring a "
             "supercontinent, slab pull tears it apart from the edges, and new "
             "oceans open by extroversion. In the bottom-up view, a supercontinent "
             "insulates the mantle like a blanket, heat builds beneath it, and "
             "the resulting upwelling cracks it from below. Numerical models can "
             "produce both behaviors by tuning parameters, which means the models "
             "do not yet discriminate - the geological record must, and so far it "
             "supports pieces of each."),
 "why_it_matters": ("The supercontinent cycle is the longest-period rhythm in "
             "Earth history: it drives sea level, climate, ocean chemistry, and "
             "mass extinctions. Understanding its engine is understanding what sets "
             "the tempo of the whole planet - and whether the cycle is truly "
             "cyclic or just episodic."),
 "sig_pointer": ("The Signature system proposes an engine-discrimination program: "
             "list the distinct predictions of top-down versus bottom-up models "
             "and test them against the breakup record of two supercontinents. "
             "See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the cycle as a machine "
             "with two candidate motors - and proposes the measurements that "
             "would show which motor is actually running."),
 "signature_solution": (
     "Proposed approach. Step 1: write down the discriminating predictions in "
     "advance - bottom-up predicts breakup starting over mantle upwellings with "
     "massive volcanism first; top-down predicts breakup starting at old "
     "subduction margins with rifting first and volcanism later. Step 2: "
     "reconstruct the breakup sequences of Pangea and Rodinia at 10-million-"
     "year resolution - where did rifting start, where did the first large "
     "igneous provinces erupt, in what order? Step 3: score each supercontinent "
     "against both prediction sets blind. Step 4: run the test on the assembly "
     "phase too - do collisions close oceans by introversion (top-down) or "
     "extroversion?\n"
     "Assumptions: that breakup sequences can be reconstructed at the needed "
     "resolution (Rodinia is the weak link); that large igneous provinces mark "
     "mantle upwellings rather than plate-tectonic melting; that the two engines "
     "are separable and not always coupled.\n"
     "What would confirm it: both supercontinents matching one prediction set "
     "on breakup and assembly, with the other set failing the same tests.\n"
     "What would kill it: Pangea and Rodinia matching opposite engines - "
     "suggesting no single engine - or breakup sequences too poorly resolved to "
     "score.\n"
     "What this does NOT claim: it does not claim the cycle is periodic; it "
     "does not claim mantle plumes exist as textbook cartoons; it is not "
     "established science."),
 "citations": [
     "Nance R D et al. The supercontinent cycle. Sci Am; 2014.",
     "Yoshida M, Santosh M. Supercontinents, mantle dynamics and plate tectonics. Gondwana Res; 2011.",
     "Gurnis M. Large-scale mantle convection and the aggregation and dispersal of supercontinents. Nature; 1988."],
 "explorer": {
   "blurb": ("A cycle-tempo calculator: from assembly and breakup dates it "
             "measures supercontinent lifespans and tests whether the rhythm "
             "looks periodic."),
   "assumptions": {"pangea_assembled_Ma": 335.0, "pangea_broke_Ma": 200.0,
                   "rodinia_assembled_Ma": 1000.0, "rodinia_broke_Ma": 750.0},
   "model_src": (
     "def run(A):\n"
     "    pangea_life = A[\"pangea_assembled_Ma\"] - A[\"pangea_broke_Ma\"]\n"
     "    rodinia_life = A[\"rodinia_assembled_Ma\"] - A[\"rodinia_broke_Ma\"]\n"
     "    cycle_gap = A[\"rodinia_broke_Ma\"] - A[\"pangea_assembled_Ma\"]\n"
     "    mean_life = (pangea_life + rodinia_life) / 2.0\n"
     "    return {\"pangea_lifespan_Ma\": pangea_life,\n"
     "            \"rodinia_lifespan_Ma\": rodinia_life,\n"
     "            \"assembly_gap_Ma\": cycle_gap,\n"
     "            \"mean_lifespan_Ma\": mean_life}\n"),
   "steps": [("Pangeas assembled lifespan", "pangea_lifespan_Ma", "Ma"),
             ("Rodinias assembled lifespan", "rodinia_lifespan_Ma", "Ma"),
             ("Gap between Rodinia breakup and Pangea assembly", "assembly_gap_Ma", "Ma"),
             ("Mean supercontinent lifespan", "mean_lifespan_Ma", "Ma")],
   "confirm": ["Both supercontinents match one engine prediction set on breakup and assembly.",
               "The other prediction set fails the same tests."],
   "refute": ["Pangea and Rodinia match opposite engines, or breakup sequences are too poorly resolved to score."],
   "checks": [("pangea_lifespan_Ma", 100.0, 200.0),
              ("rodinia_lifespan_Ma", 150.0, 350.0),
              ("mean_lifespan_Ma", 100.0, 300.0)],
   "honesty": ("We do not know the engine; this explorer only measures the "
               "lifespans and gaps, which are the raw facts any engine theory "
               "must reproduce.")}
},
# ---------------------------------------------------------------- 13
{
 "key": "future-supercontinent",
 "name": "Will a New Supercontinent Form, and Where?",
 "group": "Geodynamics",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": ("If the supercontinent cycle continues, Earths continents will gather "
             "again in 200 to 300 million years - but models predict three "
             "completely different supercontinents: Amasia, Pangea Proxima, and "
             "Aurica. They cannot all be right."),
 "background": ("The Atlantic is widening and the Pacific is shrinking: subduction "
             "zones ring the Pacific and consume its floor, so the simplest "
             "extrapolation closes the Pacific and piles the continents around the "
             "Arctic - Amasia. But the Atlantic has its own young subduction zones "
             "in the Caribbean and Scotia arcs; if those grow and the Atlantic "
             "starts closing, the continents reassemble roughly where Pangea was - "
             "Pangea Proxima. A third model notes both oceans have subduction "
             "zones, so both may close and a new ocean - the Pan-Asian - opens "
             "instead: Aurica, centered on the equator. Each scenario follows from "
             "a defensible reading of present plate motions, and the choice hinges "
             "on which young subduction zones survive - something no model can yet "
             "predict."),
 "why_it_matters": ("The next supercontinent decides the far-future geography "
             "that will govern climate, sea level, and evolution for hundreds of "
             "millions of years. It is also the ultimate test of plate-tectonic "
             "forecasting: if we cannot predict 250 million years ahead from "
             "todays motions, the limits of geodynamic prediction are exposed."),
 "sig_pointer": ("The Signature system proposes a subduction-survival watch: "
             "identify the young subduction zones whose fate decides between the "
             "three scenarios, and monitor the observables that discriminate them. "
             "See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the three "
             "supercontinents as a three-way bet - and proposes naming the exact "
             "observations that would settle the bet."),
 "signature_solution": (
     "Proposed approach. Step 1: formalize each scenario as a set of falsifiable "
     "predictions for the next 50 million years - which oceans shrink fastest, "
     "which subduction zones lengthen or die. Step 2: identify the decision "
     "points - the Caribbean, Scotia, and western Pacific subduction zones - and "
     "define measurable criteria for subduction initiation versus death "
     "(seismicity depth, slab imaging, forearc geology). Step 3: run all three "
     "scenarios forward in mantle-convection models with identical physics but "
     "different initial subduction geometries, and report which outcomes are "
     "robust and which are knife-edge. Step 4: publish a living scoreboard - as "
     "new seismic images arrive, each scenarios probability updates in the open.\n"
     "Assumptions: that present plate motions extrapolate meaningfully for tens "
     "of millions of years (true until a reorganization hits); that subduction "
     "initiation physics is understood well enough to model (it is not, fully); "
     "that mantle convection models capture the real force balance.\n"
     "What would confirm it: one scenario accumulating passed predictions while "
     "the others fail theirs, with models agreeing the winner is robust.\n"
     "What would kill it: a plate reorganization within the watch period that "
     "scrambles all three scenarios - the honest result that prediction has "
     "limits.\n"
     "What this does NOT claim: it does not claim any scenario is favored today; "
     "it does not predict the far future; it is not established science."),
 "citations": [
     "Mitchell R N et al. Plate tectonics before 2.0 Ga. Nature; 2021.",
     "Duarte J C et al. Invading the Atlantic: the Atlantic-Mediterranean subduction zones. Geology; 2013.",
     "Yoshida M. Formation of a future supercontinent. Terra Nova; 2016."],
 "explorer": {
   "blurb": ("A scenario comparator: from ocean widths and spreading rates it "
             "estimates closure times for the Atlantic and Pacific under each "
             "supercontinent scenario."),
   "assumptions": {"atlantic_width_km": 5000.0, "pacific_width_km": 15000.0,
                   "atlantic_spread_cm_yr": 2.5, "pacific_subduct_cm_yr": 8.0},
   "model_src": (
     "def run(A):\n"
     "    atl_growth_Ma = (A[\"atlantic_width_km\"] * 1e5) / A[\"atlantic_spread_cm_yr\"] / 1e6\n"
     "    pac_close_Ma = (A[\"pacific_width_km\"] * 1e5) / A[\"pacific_subduct_cm_yr\"] / 1e6\n"
     "    ratio = pac_close_Ma / atl_growth_Ma\n"
     "    return {\"atlantic_double_Ma\": atl_growth_Ma,\n"
     "            \"pacific_close_Ma\": pac_close_Ma,\n"
     "            \"pacific_vs_atlantic\": ratio}\n"),
   "steps": [("Time to double the Atlantic at 2.5 cm/yr", "atlantic_double_Ma", "Ma"),
             ("Time to close the Pacific at 8 cm/yr", "pacific_close_Ma", "Ma"),
             ("Pacific closure versus Atlantic doubling", "pacific_vs_atlantic", "x")],
   "confirm": ["One scenario accumulates passed predictions while the others fail theirs.",
               "Models agree the winning outcome is robust, not knife-edge."],
   "refute": ["A plate reorganization scrambles all three scenarios within the watch period."],
   "checks": [("atlantic_double_Ma", 100.0, 300.0),
              ("pacific_close_Ma", 100.0, 300.0),
              ("pacific_vs_atlantic", 0.5, 2.0)],
   "honesty": ("We do not know which supercontinent comes next; this explorer "
               "only converts present rates into closure times so the scenarios "
               "can be compared quantitatively.")}
},
# ---------------------------------------------------------------- 14
{
 "key": "banded-iron",
 "name": "How Did Banded Iron Formations Form?",
 "group": "Geochemistry",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": ("Banded iron formations - striped iron-silica rocks - hold almost all "
             "the worlds iron ore and formed almost entirely between 2.7 and 2.4 "
             "billion years ago. The chemistry that precipitated trillions of "
             "tonnes of iron from the oceans is still argued."),
 "background": ("BIFs are alternating bands of iron oxide and chert, sometimes "
             "hundreds of meters thick and stretching for hundreds of kilometers "
             "- the Hamersley Basin of Australia alone holds deposits mined for a "
             "century. They demand an ocean rich in dissolved iron, which requires "
             "anoxic deep water, plus an oxidant to precipitate it. The classic "
             "model invokes oxygen from early cyanobacteria; rivals invoke "
             "anoxygenic photoferrotrophs - bacteria that oxidize iron using "
             "sunlight without making oxygen - or even ultraviolet photo-oxidation "
             "with no biology at all. BIFs vanish after the Great Oxidation Event "
             "about 2.4 billion years ago, which both supports the oxygen story "
             "and is equally consistent with the alternatives, since all three "
             "mechanisms shut down when the ocean oxygenated."),
 "why_it_matters": ("BIFs are the raw material of the steel age - the Hamersley, "
             "the Quadrilatero, Krivoy Rog - and their formation records the "
             "oxygenation of Earths oceans, the prerequisite for complex life. "
             "Settling the mechanism dates the rise of oxygenic photosynthesis, "
             "one of the most consequential metabolisms ever."),
 "sig_pointer": ("The Signature system proposes a BIF mechanism bake-off: "
             "measure iron-isotope and rare-earth fingerprints that differ "
             "between biological and abiotic oxidation, across the great BIF "
             "basins. See the Signature Edition record for the full labeled "
             "proposal."),
 "sig_lens": ("Signature lens: the Signature system treats each BIF basin as an "
             "experiment in ancient ocean chemistry - and proposes the "
             "fingerprints that would show which oxidant ran the experiment."),
 "signature_solution": (
     "Proposed approach. Step 1: define the discriminating fingerprints in "
     "advance - oxygenic photosynthesis predicts iron-isotope fractionations "
     "tied to free O2, photoferrotrophy predicts distinct organic biomarkers "
     "and iron-isotope patterns, UV oxidation predicts no biological "
     "fractionation at all. Step 2: measure all three fingerprint suites on the "
     "same samples from Hamersley, Transvaal, and Krivoy Rog with one protocol. "
     "Step 3: run laboratory precipitation experiments under Archean ocean "
     "conditions for each mechanism and compare the synthetic fingerprints with "
     "the rocks. Step 4: score mechanisms per basin - the honest outcome may be "
     "different winners in different basins.\n"
     "Assumptions: that 2.5-billion-year metamorphism has not erased the primary "
     "fingerprints (the perennial worry); that lab conditions approximate "
     "Archean seawater; that the sampled basins represent global BIF "
     "formation.\n"
     "What would confirm it: one mechanism matching fingerprints in all basins, "
     "with lab synthetics reproducing the rock patterns.\n"
     "What would kill it: fingerprints scrambled beyond recognition by "
     "metamorphism, or lab experiments showing all three mechanisms make "
     "indistinguishable rocks.\n"
     "What this does NOT claim: it does not claim BIFs prove oxygenic "
     "photosynthesis dates; it does not claim all BIFs formed one way; it is "
     "not established science."),
 "citations": [
     "Klein C. Some Precambrian banded iron-formations (BIFs) from around the world. Econ Geol; 2005.",
     "Konhauser K O et al. Ocean chemistry and the deposition of banded iron formation. Nature; 2017.",
     "Bekker A et al. Iron formation: the sedimentary product of a complex interplay. Econ Geol; 2010."],
 "explorer": {
   "blurb": ("An iron-budget calculator: from BIF tonnages it estimates the "
             "dissolved iron the ancient ocean must have held, and the oxidant "
             "flux needed to precipitate it."),
   "assumptions": {"bif_iron_Gt": 100000.0, "interval_Ma": 300.0,
                   "ocean_mass_kg": 1.4e21, "fe_ppm_needed": 50.0},
   "model_src": (
     "def run(A):\n"
     "    rate_Gt_Ma = A[\"bif_iron_Gt\"] / A[\"interval_Ma\"]\n"
     "    ocean_fe_Gt = A[\"ocean_mass_kg\"] * A[\"fe_ppm_needed\"] / 1e6 / 1e12\n"
     "    turnovers = A[\"bif_iron_Gt\"] / ocean_fe_Gt\n"
     "    return {\"deposition_rate_Gt_Ma\": rate_Gt_Ma,\n"
     "            \"ocean_iron_inventory_Gt\": ocean_fe_Gt,\n"
     "            \"ocean_iron_turnovers\": turnovers}\n"),
   "steps": [("Mean iron deposition rate", "deposition_rate_Gt_Ma", "Gt/Ma"),
             ("Dissolved iron in a 50 ppm ocean", "ocean_iron_inventory_Gt", "Gt"),
             ("Times the ocean iron inventory was precipitated", "ocean_iron_turnovers", "x")],
   "confirm": ["One mechanism matches fingerprints in all basins, with lab synthetics reproducing the rocks.",
               "Different basins may honestly show different winners."],
   "refute": ["Fingerprints are scrambled by metamorphism, or all mechanisms make indistinguishable rocks in the lab."],
   "checks": [("deposition_rate_Gt_Ma", 100.0, 1000.0),
              ("ocean_iron_inventory_Gt", 10000.0, 200000.0),
              ("ocean_iron_turnovers", 0.5, 5.0)],
   "honesty": ("We do not know the oxidant; this explorer only quantifies the "
               "iron throughput, which any mechanism must be able to supply.")}
},
# ---------------------------------------------------------------- 15
{
 "key": "devonian-extinction",
 "name": "What Killed the Seas in the Late Devonian?",
 "group": "Paleontology",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": ("About 372 million years ago, the oceans lost up to 70 percent of "
             "marine species in the Kellwasser crisis - one of the big five mass "
             "extinctions - with no asteroid impact in sight. The killer was "
             "something slower, and it is still unidentified."),
 "background": ("The Late Devonian extinction was actually a drawn-out crisis: "
             "the Kellwasser event at 372 million years and the Hangenberg event "
             "at 359 million years, spanning 15 million years of reef collapse, "
             "anoxia, and black shale deposition. Unlike the end-Cretaceous, "
             "there is no iridium layer, no crater, no shocked quartz. Leading "
             "suspects include the spread of land plants - roots accelerating "
             "weathering, nutrients fertilizing the oceans, and the resulting "
             "anoxia suffocating reefs - plus sea-level swings and possible "
             "volcanism. The plant hypothesis is elegant but struggles with "
             "timing: forests spread tens of millions of years before the worst "
             "killing. Each new geochemical study shifts the weight without "
             "closing the case."),
 "why_it_matters": ("The Devonian crisis destroyed the greatest reef systems Earth "
             "had built and reset vertebrate evolution just as tetrapods were "
             "emerging - our own lineage. It is the premier example of a mass "
             "extinction driven from within the Earth-life system rather than "
             "from space, and the closest ancient analogue to modern "
             "human-driven ocean stress."),
 "sig_pointer": ("The Signature system proposes a kill-sequence reconstruction: "
             "high-resolution timelines of anoxia, sea level, and plant spread "
             "across the crisis interval to find what leads and what follows. "
             "See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the Devonian crisis "
             "as a murder with no smoking gun - and proposes reconstructing the "
             "sequence of events precisely enough to convict or acquit each "
             "suspect."),
 "signature_solution": (
     "Proposed approach. Step 1: build a million-year-resolution timeline for "
     "the 375 to 355 million year interval - uranium-isotope anoxia proxies, "
     "sea-level curves, mercury volcanic proxies, and plant-fossil first "
     "appearances - from sections on at least three paleocontinents. Step 2: "
     "for each suspect, state the predicted lead-lag signature in advance: "
     "plants-first predicts weathering and nutrient proxies rising before "
     "anoxia; volcanism-first predicts mercury spikes leading the carbon "
     "excursions. Step 3: test for geographic pattern - a plant-driven kill "
     "should track the spread of forests, a volcanic kill should be global and "
     "synchronous. Step 4: run Earth-system models of each scenario and require "
     "the winner to reproduce both the selectivity (reefs died, fish suffered "
     "less) and the duration.\n"
     "Assumptions: that uranium isotopes record global anoxia rather than local "
     "basin restriction; that mercury anomalies are volcanic and not diagenetic; "
     "that the fossil timeline is resolved enough for lead-lag tests.\n"
     "What would confirm it: one suspects proxies consistently leading the "
     "killing horizons across continents, with models reproducing the "
     "selectivity.\n"
     "What would kill it: all proxies moving together within dating error, or "
     "different continents telling contradictory sequences.\n"
     "What this does NOT claim: it does not claim plants are guilty; it does "
     "not rule out a hidden impact; it is not established science."),
 "citations": [
     "McGhee G R. The Late Devonian Mass Extinction. Columbia Univ Press; 1996.",
     "Algeo T J et al. Terrestrial-marine teleconnections in the Devonian. Palaeogeogr Palaeoclimatol Palaeoecol; 2001.",
     "Racki G. The Alvarez impact theory and the Late Devonian mass extinction. Geol Soc Am Spec Pap; 2020."],
 "explorer": {
   "blurb": ("A kill-rate calculator: from species-loss estimates and interval "
             "length it computes the Devonian extinction tempo and compares it "
             "with the sudden end-Cretaceous kill."),
   "assumptions": {"species_loss_pct": 70.0, "interval_Ma": 15.0,
                   "kpg_loss_pct": 75.0, "kpg_duration_yr": 10000.0},
   "model_src": (
     "def run(A):\n"
     "    devonian_rate = A[\"species_loss_pct\"] / (A[\"interval_Ma\"] * 1e6)\n"
     "    kpg_rate = A[\"kpg_loss_pct\"] / A[\"kpg_duration_yr\"]\n"
     "    tempo_ratio = kpg_rate / devonian_rate\n"
     "    return {\"devonian_loss_per_yr\": devonian_rate,\n"
     "            \"kpg_loss_per_yr\": kpg_rate,\n"
     "            \"kpg_faster_by\": tempo_ratio}\n"),
   "steps": [("Devonian species loss per year", "devonian_loss_per_yr", "pct/yr"),
             ("End-Cretaceous loss per year", "kpg_loss_per_yr", "pct/yr"),
             ("How many times faster the impact kill was", "kpg_faster_by", "x")],
   "confirm": ["One suspects proxies consistently lead the killing horizons across continents.",
               "Models reproduce both the selectivity and the duration."],
   "refute": ["All proxies move together within dating error, or continents tell contradictory sequences."],
   "checks": [("devonian_loss_per_yr", 1e-06, 1e-04),
              ("kpg_loss_per_yr", 0.001, 0.05),
              ("kpg_faster_by", 100.0, 100000.0)],
   "honesty": ("We do not know the killer; this explorer only contrasts the "
               "Devonian slow crisis with an impact-fast kill, which is the "
               "tempo any suspect must match.")}
},
# ---------------------------------------------------------------- 16
{
 "key": "triassic-extinction",
 "name": "Was the End-Triassic Extinction Volcanic?",
 "group": "Volcanology",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": ("201 million years ago, the Central Atlantic Magmatic Province erupted "
             "and half of marine genera vanished - the extinction that cleared the "
             "way for the dinosaurs. The eruptions and the dying coincide, but "
             "coincidence is not causation, and the kill mechanism is debated."),
 "background": ("CAMP - the Central Atlantic Magmatic Province - poured out some "
             "2 to 3 million cubic kilometers of basalt as Pangea began rifting, "
             "with the main pulse dated to within tens of thousands of years of "
             "the extinction horizon. Mercury anomalies in end-Triassic sediments "
             "worldwide fingerprint massive volcanism, and the carbon-isotope "
             "record shows sharp negative excursions consistent with volcanic CO2 "
             "or methane release. Yet the killing was selective in puzzling ways - "
             "reef builders and large amphibians died while dinosaurs and mammals "
             "sailed through - and some sections show the extinction beginning "
             "before the largest eruptions. Rivals argue the volcanism merely "
             "stressed an already vulnerable biosphere, or that the true killer "
             "was ocean acidification, anoxia, or heat acting with lags the "
             "volcanic record cannot resolve."),
 "why_it_matters": ("The end-Triassic is the cleanest test case for whether "
             "flood-basalt volcanism alone can cause a mass extinction - the "
             "same question asked about the end-Permian Siberian Traps and the "
             "Deccan Traps at the end-Cretaceous. It also handed the planet to "
             "the dinosaurs, shaping 135 million years of evolution."),
 "sig_pointer": ("The Signature system proposes an eruption-kill synchrony test: "
             "date individual CAMP lava flows against the extinction horizons bed "
             "by bed, and require the kill mechanism to match the selectivity. "
             "See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats CAMP as the prime "
             "suspect with a strong alibi problem - and proposes the bed-by-bed "
             "timeline that would convict or acquit it."),
 "signature_solution": (
     "Proposed approach. Step 1: date the CAMP eruptive stratigraphy flow by "
     "flow with high-precision U-Pb on zircons from interbedded ashes, building "
     "an eruption timeline at 20-thousand-year resolution. Step 2: build a "
     "matching-resolution extinction timeline from multiple boundary sections - "
     "which groups vanish in which beds, in what order? Step 3: test the "
     "candidate kill mechanisms against the selectivity: CO2 warming predicts "
     "tropical reef collapse first; acidification predicts calcifiers first; "
     "anoxia predicts deep-water dysoxia proxies leading. Step 4: run "
     "carbon-cycle models forced by the dated eruption timeline and require the "
     "winner to reproduce the isotope excursions quantitatively, not just "
     "qualitatively.\n"
     "Assumptions: that U-Pb zircon dates record eruption and not inheritance; "
     "that mercury anomalies are volcanic; that the boundary sections are "
     "complete and not condensed.\n"
     "What would confirm it: eruption pulses leading extinction pulses bed by "
     "bed, with one mechanism reproducing both selectivity and isotopes.\n"
     "What would kill it: extinction horizons consistently preceding the dated "
     "eruptions, or no mechanism reproducing the selectivity pattern.\n"
     "What this does NOT claim: it does not claim volcanism cannot kill; it "
     "does not claim the dating is already good enough; it is not established "
     "science."),
 "citations": [
     "Blackburn T J et al. Zircon U-Pb geochronology links the end-Triassic extinction with CAMP. Science; 2013.",
     "Lindstrom S et al. Volcanic mercury and the end-Triassic extinction. Sci Rep; 2019.",
     "Wignall P B. Large igneous provinces and mass extinctions. Annu Rev Earth Planet Sci; 2001."],
 "explorer": {
   "blurb": ("An eruption-scale calculator: from CAMP volume and duration it "
             "computes eruption rates and the CO2 pulse, comparing them with "
             "modern anthropogenic emissions."),
   "assumptions": {"camp_volume_km3": 2500000.0, "duration_yr": 600000.0,
                   "co2_per_km3_Gt": 5.0, "modern_co2_Gt_yr": 40.0},
   "model_src": (
     "def run(A):\n"
     "    rate_km3_yr = A[\"camp_volume_km3\"] / A[\"duration_yr\"]\n"
     "    co2_Gt_yr = rate_km3_yr * A[\"co2_per_km3_Gt\"]\n"
     "    vs_modern = co2_Gt_yr / A[\"modern_co2_Gt_yr\"]\n"
     "    total_co2_Gt = A[\"camp_volume_km3\"] * A[\"co2_per_km3_Gt\"]\n"
     "    return {\"eruption_rate_km3_yr\": rate_km3_yr,\n"
     "            \"co2_rate_Gt_yr\": co2_Gt_yr,\n"
     "            \"vs_modern_emissions\": vs_modern,\n"
     "            \"total_co2_Gt\": total_co2_Gt}\n"),
   "steps": [("Mean CAMP eruption rate", "eruption_rate_km3_yr", "km3/yr"),
             ("Implied CO2 release rate", "co2_rate_Gt_yr", "Gt/yr"),
             ("Versus modern human emissions", "vs_modern_emissions", "x"),
             ("Total CO2 released", "total_co2_Gt", "Gt")],
   "confirm": ["Eruption pulses lead extinction pulses bed by bed, with one mechanism reproducing selectivity and isotopes.",
               "Carbon-cycle models match the excursions quantitatively."],
   "refute": ["Extinction horizons consistently precede the dated eruptions, or no mechanism reproduces the selectivity."],
   "checks": [("eruption_rate_km3_yr", 1.0, 20.0),
              ("co2_rate_Gt_yr", 5.0, 100.0),
              ("vs_modern_emissions", 0.1, 3.0),
              ("total_co2_Gt", 5000000.0, 30000000.0)],
   "honesty": ("We do not know the kill mechanism; this explorer only scales "
               "the eruption against modern emissions, which is the comparison "
               "every volcanic-kill theory must survive.")}
},
# ---------------------------------------------------------------- 17
{
 "key": "deep-water-flux",
 "name": "How Much Ocean Water Gets Recycled Into the Deep Mantle?",
 "group": "Geochemistry",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": ("Subduction zones drag waterlogged ocean crust into the mantle, and "
             "volcanoes return water to the surface - but whether Earth is "
             "currently gaining or losing surface water, and by how much, is "
             "unsettled by an order of magnitude."),
 "background": ("Water enters subduction zones in sediments, in the altered "
             "basaltic crust, and in serpentinized mantle beneath it - perhaps "
             "several ocean masses worth over Earth history. Most is squeezed "
             "out shallow and returns via arc volcanoes, but seismic images of "
             "slow anomalies in slabs suggest some water descends past 400 "
             "kilometers into the transition zone, where the mineral ringwoodite "
             "can hold weight-percent water. Estimates of the deep flux range "
             "from a tenth to a full ocean per billion years, while volcanic "
             "outgassing estimates are equally uncertain. The net - regassing "
             "minus degassing - could be positive, negative, or zero, and the "
             "sign decides whether sea level is falling on billion-year "
             "timescales."),
 "why_it_matters": ("The deep water cycle is the long-term control on ocean "
             "volume: if subduction wins, the oceans are slowly draining into "
             "the mantle; if volcanism wins, they are filling. It also decides "
             "how much water the mantle holds today - the reservoir that "
             "lubricates plate tectonics itself."),
 "sig_pointer": ("The Signature system proposes a water-budget closure program: "
             "measure the water in, the water out, and the deep reservoir "
             "independently, and require the three to balance. See the Signature "
             "Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the deep water cycle "
             "as a bank account - deposits at trenches, withdrawals at volcanoes "
             "- and proposes auditing all three ledgers until they balance."),
 "signature_solution": (
     "Proposed approach. Step 1: measure water input at a representative set of "
     "trenches - sediment thickness, crustal alteration depth from seismic "
     "velocity, and serpentinization extent - with uniform methods. Step 2: "
     "measure the shallow return via arc-volcano volatile budgets (melt "
     "inclusions, gas plumes) and the deep leak via transition-zone water "
     "estimates from receiver functions and mineral physics. Step 3: close the "
     "budget - input minus shallow return minus deep storage must equal the "
     "observed sea-level trend over millions of years from stratigraphy. Step "
     "4: test time-dependence - was the Archean cycle wetter, and did that "
     "change the onset of plate tectonics?\n"
     "Assumptions: that the sampled trenches represent global subduction; that "
     "melt inclusions record primary water contents; that transition-zone water "
     "estimates from seismology are not artifacts of temperature or "
     "composition.\n"
     "What would confirm it: the three ledgers balancing within a factor of "
     "two, with the net flux matching the stratigraphic sea-level trend.\n"
     "What would kill it: ledgers disagreeing by an order of magnitude with no "
     "convergence as methods improve - the sign of the net flux genuinely "
     "unknowable with current tools.\n"
     "What this does NOT claim: it does not claim the oceans are draining; it "
     "does not claim ringwoodite water estimates are correct; it is not "
     "established science."),
 "citations": [
     "van Keken P E et al. Subduction factory water fluxes. J Geophys Res; 2011.",
     "Pearson D G et al. Hydrous mantle transition zone indicated by ringwoodite. Nature; 2014.",
     "Hirschmann M M. Water, melting, and the deep Earth water cycle. Annu Rev Earth Planet Sci; 2006."],
 "explorer": {
   "blurb": ("A water-budget calculator: from subduction input and volcanic "
             "output estimates it computes the net flux and the time to drain "
             "or fill an ocean."),
   "assumptions": {"subduction_in_Sv": 1.0, "volcanic_out_Sv": 0.99,
                   "ocean_mass_kg": 1.4e21, "Sv_kg_yr": 3.15e16},
   "model_src": (
     "def run(A):\n"
     "    net_Sv = A[\"subduction_in_Sv\"] - A[\"volcanic_out_Sv\"]\n"
     "    net_kg_yr = net_Sv * A[\"Sv_kg_yr\"]\n"
     "    ocean_lifetime_yr = A[\"ocean_mass_kg\"] / abs(net_kg_yr)\n"
     "    pct_per_Ga = abs(net_kg_yr) * 1e9 / A[\"ocean_mass_kg\"] * 100.0\n"
     "    return {\"net_flux_Sv\": net_Sv, \"net_flux_kg_yr\": net_kg_yr,\n"
     "            \"ocean_turnover_yr\": ocean_lifetime_yr,\n"
     "            \"ocean_change_pct_per_Ga\": pct_per_Ga}\n"),
   "steps": [("Net deep flux (positive = into mantle)", "net_flux_Sv", "Sv"),
             ("Net flux in kg per year", "net_flux_kg_yr", "kg/yr"),
             ("Time to move one ocean at this rate", "ocean_turnover_yr", "yr"),
             ("Ocean volume change per billion years", "ocean_change_pct_per_Ga", "pct/Ga")],
   "confirm": ["Input, return, and storage ledgers balance within a factor of two.",
               "The net flux matches the stratigraphic sea-level trend."],
   "refute": ["Ledgers disagree by an order of magnitude with no convergence as methods improve."],
   "checks": [("net_flux_Sv", 0.001, 0.05),
              ("ocean_turnover_yr", 1e6, 1e8),
              ("ocean_change_pct_per_Ga", 1e3, 1e6)],
   "honesty": ("We do not know the sign of the net flux; this explorer only "
               "converts published estimates into ocean lifetimes so the "
               "disagreement is visible in concrete terms.")}
},
# ---------------------------------------------------------------- 18
{
 "key": "water-tectonics",
 "name": "Did Water Make Plate Tectonics Possible?",
 "group": "Geodynamics",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": ("Venus is Earths twin in size and composition but has no plate "
             "tectonics - and no surface water. Many geodynamicists suspect the "
             "two facts are one fact: that water is what lets plates slide. "
             "Proving it has resisted every attempt."),
 "background": ("Water weakens rocks dramatically: a trace of water in olivine "
             "drops mantle viscosity by orders of magnitude, and water in fault "
             "zones enables the stable sliding that subduction requires. "
             "Laboratory deformation experiments confirm the weakening, and "
             "numerical models of mantle convection produce plate-like behavior "
             "only when a weak, water-lubricated layer is included. Venus, "
             "baked dry by a runaway greenhouse, instead resurfaces in "
             "catastrophic overturns. The counterargument is timing: Earth may "
             "have had plate tectonics before the oceans condensed, and some "
             "models generate plates with damage mechanics and no water at all. "
             "The correlation is striking; the causation is unproven."),
 "why_it_matters": ("If water is the switch for plate tectonics, then the "
             "habitability recipe changes: a rocky planet needs not just water "
             "but water delivered early enough and kept long enough to start "
             "the conveyor. It links ocean formation, tectonics, and climate "
             "into one coupled origin story - or breaks the link entirely."),
 "sig_pointer": ("The Signature system proposes a water-switch test program: "
             "find the geological moment when each weakening mechanism could "
             "first have operated, and test whether tectonics follows water in "
             "time. See the Signature Edition record for the full labeled "
             "proposal."),
 "sig_lens": ("Signature lens: the Signature system treats Venus as the control "
             "experiment Earth never ran - and proposes the measurements on "
             "Earth that would show whether water flipped the tectonic switch."),
 "signature_solution": (
     "Proposed approach. Step 1: date the three water arrivals independently - "
     "the first oceans (zircon oxygen isotopes), the first hydrated mantle "
     "(water in the oldest arc magmas), and the first weak faults (the oldest "
     "blueschists, which need water-rich subduction). Step 2: date the first "
     "plate-tectonic evidence with the pre-registered proof standard from the "
     "onset program. Step 3: test ordering across cratons - does tectonic "
     "evidence always follow hydration, or does it ever precede it? Step 4: "
     "confront the models - run convection simulations with and without water "
     "weakening at Archean mantle temperatures and report which produce "
     "Earth-like plates, with the failures published too.\n"
     "Assumptions: that zircon oxygen isotopes date oceans and not later "
     "alteration; that blueschists require water (they do) and mark subduction "
     "(usually); that lab weakening laws extrapolate to planetary scales.\n"
     "What would confirm it: hydration consistently preceding tectonic evidence "
     "on every craton, with dry models failing to make plates.\n"
     "What would kill it: tectonic evidence predating hydration anywhere "
     "robust, or dry damage-mechanics models making convincing plates.\n"
     "What this does NOT claim: it does not claim Venus proves the case; it "
     "does not claim water is sufficient alone; it is not established science."),
 "citations": [
     "Mei S, Kohlstedt D L. Influence of water on plastic deformation of olivine. J Geophys Res; 2000.",
     "Korenaga J. Thermal cracking and the deep hydration of oceanic lithosphere. Earth Planet Sci Lett; 2007.",
     "Lenardic A, Kaula W M. More thoughts on convergent crustal growth. J Geophys Res; 1995."],
 "explorer": {
   "blurb": ("A weakening calculator: from laboratory flow laws it shows how "
             "much water drops mantle viscosity, and what that does to "
             "convective stress."),
   "assumptions": {"dry_viscosity_Pas": 1e21, "water_ppm": 1000.0,
                   "weakening_exponent": 1.2, "reference_ppm": 100.0},
   "model_src": (
     "def run(A):\n"
     "    factor = (A[\"water_ppm\"] / A[\"reference_ppm\"]) ** A[\"weakening_exponent\"]\n"
     "    wet_viscosity = A[\"dry_viscosity_Pas\"] / factor\n"
     "    stress_drop = factor\n"
     "    return {\"viscosity_reduction_factor\": factor,\n"
     "            \"wet_viscosity_Pas\": wet_viscosity,\n"
     "            \"convective_stress_drop\": stress_drop}\n"),
   "steps": [("Viscosity reduction from water", "viscosity_reduction_factor", "x"),
             ("Wet mantle viscosity", "wet_viscosity_Pas", "Pa s"),
             ("Convective stress drop", "convective_stress_drop", "x")],
   "confirm": ["Hydration consistently precedes tectonic evidence on every craton.",
               "Dry models fail to make Earth-like plates."],
   "refute": ["Tectonic evidence predates hydration anywhere robust, or dry models make convincing plates."],
   "checks": [("viscosity_reduction_factor", 5.0, 50.0),
              ("wet_viscosity_Pas", 1e19, 5e20)],
   "honesty": ("We do not know if water is the switch; this explorer only "
               "quantifies how strong the weakening is, which is the physical "
               "fact the hypothesis stands on.")}
},
# ---------------------------------------------------------------- 19
{
 "key": "messinian-crisis",
 "name": "What Triggered the Messinian Salinity Crisis?",
 "group": "Stratigraphy",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": ("5.96 million years ago the Mediterranean began drying up, leaving "
             "salt layers kilometers thick - then the crisis ended as "
             "mysteriously as it began. What closed the Atlantic gateway, and "
             "what reopened it, is still debated."),
 "background": ("The Messinian Salinity Crisis ran from 5.96 to 5.33 million "
             "years ago: the Strait of Gibraltar region closed, evaporation "
             "outpaced inflow, and the Mediterranean deposited evaporites - "
             "gypsum then halite - in places over 2 kilometers thick, with "
             "deep basins possibly desiccating entirely. The leading trigger is "
             "tectonic: the Africa-Eurasia collision choked the Rif and Betic "
             "corridors. But the timing also matches global sea-level falls, and "
             "some models need both - tectonics narrowing the gateway, then a "
             "glacioeustatic dip finishing the closure. The end is equally "
             "puzzling: the Zanclean flood refilled the basin, but whether the "
             "breach was gradual erosion or a catastrophic megaflood is its own "
             "open question."),
 "why_it_matters": ("The crisis is the largest known salt giant and a natural "
             "experiment in what happens when an ocean basin is cut off - with "
             "lessons for evaporite oil seals, deep-biosphere survival in "
             "hypersaline brines, and how fast sea level can change when "
             "gateways move."),
 "sig_pointer": ("The Signature system proposes a gateway-timing program: date "
             "the closure of each Atlantic corridor independently and test "
             "whether tectonics alone closed them before sea level fell. See "
             "the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the crisis as a "
             "plumbing problem - and proposes dating each pipe closure to find "
             "which one shut the sea off."),
 "signature_solution": (
     "Proposed approach. Step 1: date the marine-to-evaporite transition in the "
     "Rif corridor, the Betic corridor, and the western Mediterranean with "
     "astrochronology tied to the same timescale. Step 2: reconstruct gateway "
     "depths through time from benthic foraminifera - when did each corridor "
     "shallow below the critical sill depth? Step 3: compare the closure "
     "timeline with the global sea-level curve: did the last corridor close "
     "during a tectonic uplift pulse or a sea-level lowstand? Step 4: model the "
     "basin hydrology - which closure sequence reproduces the observed "
     "gypsum-then-halite stacking?\n"
     "Assumptions: that astrochronology tuning is correct through the "
     "Messinian (well established); that foraminifera faithfully record sill "
     "depths; that the corridors dated are the ones that mattered.\n"
     "What would confirm it: corridors closing in a tectonic sequence that "
     "precedes the sea-level fall, with hydrology models matching the "
     "evaporite stacking.\n"
     "What would kill it: the final closure coinciding exactly with a "
     "sea-level lowstand while tectonics was quiescent - or corridors that "
     "never fully closed in the reconstructions.\n"
     "What this does NOT claim: it does not claim the Mediterranean fully "
     "desiccated; it does not claim tectonics acted alone; it is not "
     "established science."),
 "citations": [
     "Hsue K J et al. History of the Mediterranean salinity crisis. Nature; 1977.",
     "Krijgsman W et al. Chronology, causes and progression of the Messinian salinity crisis. Nature; 1999.",
     "Roveri M et al. The Messinian Salinity Crisis. Earth Sci Rev; 2014."],
 "explorer": {
   "blurb": ("A desiccation calculator: from basin volume and evaporation rates "
             "it estimates how fast the Mediterranean could dry, and how much "
             "salt that leaves behind."),
   "assumptions": {"basin_volume_km3": 3750000.0, "evap_m_yr": 1.5,
                   "basin_area_km2": 2500000.0, "seawater_salt_kg_m3": 35.0},
   "model_src": (
     "def run(A):\n"
     "    area_m2 = A[\"basin_area_km2\"] * 1e6\n"
     "    loss_km3_yr = A[\"evap_m_yr\"] * area_m2 / 1e9\n"
     "    dry_years = A[\"basin_volume_km3\"] / loss_km3_yr\n"
     "    salt_Gt = A[\"basin_volume_km3\"] * 1e9 * A[\"seawater_salt_kg_m3\"] / 1e12\n"
     "    return {\"evaporative_loss_km3_yr\": loss_km3_yr,\n"
     "            \"desiccation_years\": dry_years,\n"
     "            \"salt_deposited_Gt\": salt_Gt}\n"),
   "steps": [("Water lost to evaporation per year", "evaporative_loss_km3_yr", "km3/yr"),
             ("Years to evaporate the basin with no inflow", "desiccation_years", "yr"),
             ("Salt left behind by one full desiccation", "salt_deposited_Gt", "Gt")],
   "confirm": ["Corridors close in a tectonic sequence preceding the sea-level fall.",
               "Hydrology models match the gypsum-then-halite stacking."],
   "refute": ["Final closure coincides with a sea-level lowstand during tectonic quiescence."],
   "checks": [("evaporative_loss_km3_yr", 2000.0, 6000.0),
              ("desiccation_years", 500.0, 2000.0),
              ("salt_deposited_Gt", 100000.0, 200000.0)],
   "honesty": ("We do not know the trigger; this explorer only shows how fast "
               "an isolated Mediterranean dries, which sets the timescale any "
               "trigger theory must work within.")}
},
]
