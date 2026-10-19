#!/usr/bin/env python3
"""34 ladder-ordered unsolved oceanography problem entries (Unsolved Problems
Solved series, batch 1; Manon 2026-10-17 16:15 EDT).

Each entry: key, name, group, ladder_rank/tier, problem, background,
why_it_matters, sig_pointer (public half), sig_lens, signature_solution
(full Signature proposal, honesty-labeled), citations, explorer (demo spec).

Ranks 1-12 foundations, 13-23 compounded, 24-34 advanced.
Titles are distinct from the unsolved-earth-science and unsolved-climate-science
siblings (dedupe gate enforced at build).
"""

ENTRIES = [
# ---------------------------------------------------------------- 1
{
 "key": "rogue-wave-prediction",
 "name": "Can Rogue Waves Be Predicted?",
 "group": "Waves and Extremes",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": ("Rogue waves - single crests more than twice the surrounding significant wave height - "
             "rise out of ordinary seas and have damaged or sunk ships for centuries, yet no operational "
             "system forecasts them the way weather services forecast storms."),
 "background": ("Sailors told stories of walls of water for centuries, and scientists dismissed them until "
             "New Year Day 1995, when the Draupner platform in the North Sea measured a 25.6-meter crest in a "
             "sea of 12-meter waves - the first instrument-confirmed rogue wave. The European Space Agency MaxWave "
             "project then found, from satellite radar, that such waves occur far more often than Gaussian wave "
             "statistics predict. Competing mechanisms are on the table: nonlinear focusing through the "
             "Benjamin-Feir instability, where a uniform wave train breaks into groups and one crest steals energy "
             "from its neighbors; wave-current interaction, as in the Agulhas Current off South Africa; and "
             "dispersive or directional focusing of crossing seas. Each mechanism is real in the laboratory and in "
             "models, but which one dominates in the open ocean, and with what warning time, remains unsettled."),
 "why_it_matters": ("Offshore platforms and ships are engineered against statistical wave extremes - getting the "
             "tail of the distribution wrong means structures designed for a 10,000-year wave can meet it next "
             "decade. A reliable rogue-wave warning, even hours ahead for a shipping lane, would save lives and "
             "cargo. The problem is also a pure physics puzzle: the ocean is the largest nonlinear wave laboratory "
             "on Earth, and cracking it would sharpen forecasting of every extreme driven by wave dynamics."),
 "sig_pointer": ("The Signature system proposes treating rogue-wave risk as a sea-state classification problem: "
             "compute the Benjamin-Feir instability index and crossing-sea geometry from spectral wave models in "
             "real time, and issue probabilistic warnings when the index crosses pre-registered thresholds. See "
             "the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats rogue waves as predictable instability of the wave "
             "field itself - forecast the sea state instability, not the individual wave."),
 "signature_solution": (
     "Proposed approach. Step 1: run the instability calculation inside operational spectral wave models - for "
     "every forecast grid cell, compute the Benjamin-Feir index from modeled steepness and spectral bandwidth, "
     "plus a crossing-sea angle metric, turning today's wave forecast into a rogue-risk map. Step 2: pre-register "
     "risk thresholds against buoy and platform laser-altimeter records, so warnings are calibrated on data rather "
     "than tuned after the fact. Step 3: test the thresholds in the Agulhas and other current-opposed regions where "
     "wave-current focusing dominates, because a single mechanism will not cover the whole ocean. Step 4: deliver "
     "the output as probability of a 2x-significant-height crest within a 3-hour window - honest about uncertainty, "
     "never a deterministic wave-by-wave prediction.\n"
     "Assumptions: that spectral wave models resolve steepness and bandwidth well enough for the index to carry "
     "signal (unproven at global resolution); that buoy records are long enough to calibrate rare-event "
     "probabilities (marginally true); that shipping will act on probabilistic warnings (a human-factors "
     "assumption).\n"
     "What would confirm it: calibrated warnings verifying against independent buoy networks - predicted high-risk "
     "windows containing measurably more rogue crests than low-risk windows, across basins.\n"
     "What would kill it: the instability index showing no skill over climatology on independent data; rogue crests "
     "proving to be dominated by mechanisms the index cannot see, such as fine-scale current shear.\n"
     "What this does NOT claim: it does not claim individual rogue waves can be predicted; it does not endorse any "
     "existing commercial warning product; it is not established oceanography."),
 "citations": [
     "Haver S. A possible freak wave event measured at the Draupner jacket January 1 1995. Rogue Waves 2004.",
     "Rosenthal W, Lehner S. Rogue waves: results of the MaxWave project. J Offshore Mech Arct Eng; 2008.",
     "Benjamin T B, Feir J E. The disintegration of wave trains on deep water. J Fluid Mech; 1967."],
 "explorer": {
   "blurb": ("A Benjamin-Feir instability sketch: it computes the instability index from wave steepness and "
             "spectral bandwidth, converts it to a rogue-crest probability, and shows how the risk climbs as the "
             "sea state narrows and steepens."),
   "assumptions": {"steepness": 0.10, "bandwidth": 0.15, "crossing_angle_deg": 30.0},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    bfi = A[\"steepness\"] * math.sqrt(2.0) / A[\"bandwidth\"]\n"
     "    p = 0.002 * math.exp(2.0 * (bfi - 1.0))\n"
     "    crest = 1.0 + 0.9 * bfi\n"
     "    cross = 1.0 + 0.3 * math.sin(math.radians(A[\"crossing_angle_deg\"]))\n"
     "    return {\"BFI\": bfi, \"rogue_per_1000\": 1000.0 * p * cross,\n"
     "            \"max_crest_factor\": crest, \"risk_index\": bfi * cross}\n"),
   "steps": [("Benjamin-Feir instability index", "BFI", ""),
             ("Expected rogue crests per 1000 waves", "rogue_per_1000", ""),
             ("Maximum crest amplification factor", "max_crest_factor", "x"),
             ("Combined risk index", "risk_index", "")],
   "confirm": ["High-risk windows contain measurably more rogue crests on independent buoys.",
               "The index keeps its skill across basins, not just the North Sea.",
               "Warnings verify better than climatology at 3-hour lead times."],
   "refute": ["The index shows no skill over climatology on independent data.",
              "Rogue crests are dominated by current-shear mechanisms the index cannot see.",
              "Calibration records prove too short for stable rare-event probabilities."],
   "checks": [("BFI", 0.8, 1.1), ("rogue_per_1000", 1.0, 10.0), ("max_crest_factor", 1.5, 2.2)],
   "honesty": ("The Benjamin-Feir index is one lens on a multi-mechanism phenomenon. Skill on buoys is the only "
               "verdict that matters, and it has not been demonstrated yet."),
 }},
# ---------------------------------------------------------------- 2
{
 "key": "missing-ocean-plastic",
 "name": "Where Has All the Ocean Plastic Gone?",
 "group": "Pollution",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": ("Humanity pours millions of tons of plastic into the ocean every year, yet surveys find only a "
             "small fraction floating at the surface. The rest - the missing plastic - has never been accounted "
             "for, and without that budget no cleanup or policy can be aimed at the right reservoir."),
 "background": ("Jambeck and colleagues estimated in 2015 that 4.8 to 12.7 million tons of plastic entered the "
             "ocean in 2010 alone, rising since. Yet Cozar and colleagues reported in 2014 that surface trawls "
             "find on the order of tens of thousands of tons - roughly one percent of what should be there, "
             "with a striking deficit of the smallest fragments. Eriksen and colleagues estimated 269,000 tons "
             "afloat, still two orders of magnitude short. Candidate sinks compete: beaching on coastlines, "
             "sinking after biofouling makes fragments heavy, fragmentation down to nanoplastics that nets cannot "
             "catch, ingestion by organisms, and burial in sediments. Each has some evidence; none has a closed "
             "global budget, and the nanoplastic fraction is essentially unmeasured in the open ocean."),
 "why_it_matters": ("You cannot manage what you cannot find. If most plastic beaches and stays near coasts, "
             "cleanup belongs on shorelines; if it sinks to the deep seafloor, surface cleanup fleets are "
             "theater; if it fragments to nanoplastics, the toxicology question changes completely. The missing "
             "plastic is the central uncertainty in every treaty, cleanup claim, and risk assessment about ocean "
             "plastic."),
 "sig_pointer": ("The Signature system proposes a closed-budget observing campaign: paired surface, water-column, "
             "sediment, and shoreline surveys on the same transects, plus standardized nanoplastic detection, so "
             "every reservoir is measured in comparable units. See the Signature Edition record for the full "
             "labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats missing plastic as an accounting problem - measure "
             "every reservoir on the same transects, in the same units, until the budget closes."),
 "signature_solution": (
     "Proposed approach. Step 1: run coordinated transects from river mouth to open ocean to abyssal sediment, "
     "sampling surface, water column, seafloor, and adjacent shoreline with intercalibrated methods - one region "
     "at a time, starting with the best-studied inputs of Southeast Asia. Step 2: make nanoplastic detection "
     "routine rather than exotic, because the size fraction the nets miss may be the largest reservoir. Step 3: "
     "track beaching and resuspension with marked debris releases, closing the coastal loop that models currently "
     "guess at. Step 4: publish the budget as a living ledger - inputs, floating stock, beached, sunk, fragmented "
     "- updated as surveys land, with uncertainties shown, not hidden.\n"
     "Assumptions: that intercalibration across methods is achievable (hard but precedented); that nanoplastic "
     "detection can be standardized within years (optimistic); that one region's budget generalizes usefully "
     "(unproven).\n"
     "What would confirm it: regional budgets that close within stated uncertainties, replicated in a second "
     "region with a different input regime.\n"
     "What would kill it: persistent non-closure - the ledger refusing to balance - implying an unmeasured "
     "reservoir or a fundamentally wrong input estimate.\n"
     "What this does NOT claim: it does not claim cleanup technologies are effective or useless; it does not "
     "settle nanoplastic toxicology; it is not established marine science."),
 "citations": [
     "Jambeck J R et al. Plastic waste inputs from land into the ocean. Science; 2015.",
     "Cozar A et al. Plastic debris in the open ocean. Proc Natl Acad Sci; 2014.",
     "Eriksen M et al. Plastic pollution in the world oceans. PLoS ONE; 2014."],
 "explorer": {
   "blurb": ("A plastic-budget ledger: it takes annual inputs, routes them through floating, beached, sunk, and "
             "fragmented reservoirs, and shows how large the unaccounted missing fraction remains under different "
             "sink assumptions."),
   "assumptions": {"annual_input_Mt": 8.0, "years": 20.0, "float_frac": 0.02, "beach_frac": 0.25,
                   "sink_frac": 0.35, "nano_frac": 0.30},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    total = A[\"annual_input_Mt\"] * A[\"years\"]\n"
     "    accounted = total * (A[\"float_frac\"] + A[\"beach_frac\"] + A[\"sink_frac\"] + A[\"nano_frac\"])\n"
     "    missing = total - accounted\n"
     "    return {\"cumulative_input_Mt\": total, \"accounted_Mt\": accounted,\n"
     "            \"missing_Mt\": missing, \"missing_fraction\": missing / total}\n"),
   "steps": [("Cumulative plastic input", "cumulative_input_Mt", "Mt"),
             ("Accounted across reservoirs", "accounted_Mt", "Mt"),
             ("Unaccounted missing plastic", "missing_Mt", "Mt"),
             ("Missing fraction of input", "missing_fraction", "")],
   "confirm": ["Regional ledgers close within stated uncertainties.",
               "Independent methods converge on the same reservoir sizes.",
               "A second region with different inputs reproduces the pattern."],
   "refute": ["The ledger persistently refuses to close, implying wrong inputs or an unknown reservoir.",
              "Nanoplastic detection never standardizes, leaving the largest term unmeasured."],
   "checks": [("cumulative_input_Mt", 100.0, 220.0), ("missing_fraction", 0.0, 0.25)],
   "honesty": ("This ledger balances by construction - the fractions are assumptions, not measurements. Its only "
               "honest use is to show which reservoir must be measured next to close the real budget."),
 }},
# ---------------------------------------------------------------- 3
{
 "key": "deep-sea-species-census",
 "name": "How Many Species Live in the Deep Sea?",
 "group": "Life and Ecosystems",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": ("The deep sea is the largest habitat on Earth, yet estimates of how many species it holds range "
             "from hundreds of thousands to ten million. The true number - the most basic fact about life in "
             "two-thirds of the planet - is unknown."),
 "background": ("The Census of Marine Life, a decade-long program ending in 2010, described more than 6,000 "
             "potentially new species and showed that deep-sea sampling had barely begun - a single trawl can "
             "still return mostly undescribed animals. Published estimates of total marine species span an order "
             "of magnitude: Bouchet argued for under a million, Mora and colleagues for 2.2 million, and "
             "Grassle and Maciolek extrapolated deep-sea samples to 10 million. The dispute is methodological: "
             "how to extrapolate from postage-stamp samples to abyssal plains, how to count microbes and "
             "meiofauna, and whether DNA barcodes split or lump species. Meanwhile taxonomy - the science that "
             "actually describes species - remains underfunded, describing roughly 2,000 marine species a year "
             "against an unknown remainder."),
 "why_it_matters": ("Every conservation decision in the deep sea - mining licenses, marine protected areas, "
             "fisheries limits - is made in ignorance of what lives there. You cannot protect, or even price, "
             "biodiversity you have not counted. The census question also decides how the largest ecosystem on "
             "Earth functions: a million rare species implies a very different food web than a hundred thousand "
             "common ones."),
 "sig_pointer": ("The Signature system proposes a standardized, DNA-barcoded sampling grid across depth zones "
             "and basins, with discovery curves published live so the total estimate updates as sampling grows. "
             "See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the species count as a sampling problem - sample on "
             "a grid, barcode everything, and let the discovery curve converge on the total."),
 "signature_solution": (
     "Proposed approach. Step 1: establish a stratified random sampling grid spanning depths, latitudes, and "
     "substrates, with every specimen DNA-barcoded and vouchered - ending the era of incompatible one-off "
     "expeditions. Step 2: publish live discovery curves per stratum so the estimated total is a moving, "
     "falsifiable number rather than a dueling-opinions debate. Step 3: prioritize the strata where the curve "
     "is steepest - the least-sampled habitats - because that is where each sample buys the most knowledge. "
     "Step 4: fold in environmental DNA from water and sediment, calibrated against the vouchered specimens, to "
     "extend coverage cheaply.\n"
     "Assumptions: that barcode clusters map usefully onto species (contested for some groups); that funding for "
     "systematic sampling materializes (historically the binding constraint); that discovery curves extrapolate "
     "across unsampled strata (risky).\n"
     "What would confirm it: discovery curves flattening toward a stable total in multiple strata, with eDNA and "
     "voucher estimates converging.\n"
     "What would kill it: curves that refuse to flatten after massive sampling, or barcode and morphology "
     "estimates diverging irreconcilably.\n"
     "What this does NOT claim: it does not claim barcodes replace taxonomy; it does not promise a final number "
     "on any schedule; it is not established marine biology."),
 "citations": [
     "Census of Marine Life. First Census of Marine Life 2010: Highlights of a Decade of Discovery.",
     "Mora C et al. How many species are there on Earth and in the ocean? PLoS Biol; 2011.",
     "Grassle J F, Maciolek N J. Deep-sea species richness. Am Nat; 1992."],
 "explorer": {
   "blurb": ("A species-discovery curve: it fits new-species accumulation against sampling effort, extrapolates "
             "the asymptote - the estimated total - and shows how many centuries of taxonomy remain at current "
             "description rates."),
   "assumptions": {"described_species": 240000.0, "estimated_total": 2200000.0, "new_per_year": 2000.0,
                   "curve_steepness": 0.6},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    frac = A[\"described_species\"] / A[\"estimated_total\"]\n"
     "    remaining = A[\"estimated_total\"] - A[\"described_species\"]\n"
     "    years = remaining / A[\"new_per_year\"]\n"
     "    disc_rate = A[\"curve_steepness\"] * (1.0 - frac)\n"
     "    return {\"fraction_described\": frac, \"species_remaining\": remaining,\n"
     "            \"years_at_current_rate\": years, \"discovery_rate_index\": disc_rate}\n"),
   "steps": [("Fraction of species described", "fraction_described", ""),
             ("Species remaining to describe", "species_remaining", ""),
             ("Years needed at current rate", "years_at_current_rate", "yr"),
             ("Discovery-rate index", "discovery_rate_index", "")],
   "confirm": ["Discovery curves flatten toward a stable total in multiple depth strata.",
               "eDNA and voucher-based estimates converge on the same totals.",
               "Independent statistical estimators agree within a factor of two."],
   "refute": ["Curves refuse to flatten after massive systematic sampling.",
              "Barcode clusters and morphological species diverge irreconcilably."],
   "checks": [("fraction_described", 0.05, 0.25), ("years_at_current_rate", 500.0, 2000.0)],
   "honesty": ("The asymptote is only as good as the extrapolation. Every historical estimate has moved as "
               "sampling moved - this one will too."),
 }},
# ---------------------------------------------------------------- 4
{
 "key": "ocean-microbial-dark-matter",
 "name": "What Is the Microbial Dark Matter of the Ocean?",
 "group": "Microbes and Viruses",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": ("A liter of seawater holds a million microbes, and the vast majority belong to lineages never "
             "grown in a laboratory, many never even seen as complete genomes. This microbial dark matter runs "
             "the ocean's chemistry, and most of it is functionally uncharacterized."),
 "background": ("Sogin and colleagues revealed in 2006 that the rare biosphere - thousands of microbial types "
             "present at tiny abundances - dwarfs the familiar players in diversity. The Tara Oceans expedition "
             "then catalogued tens of millions of genes from plankton, most without known function. Single-cell "
             "genomics has since sketched genomes for uncultured lineages like SAR11 subclades and the "
             "enigmatic CPR bacteria, yet cultivation - the route to physiology - succeeds for perhaps one "
             "percent of marine microbes. The result is an ocean whose dominant organisms are known mainly as "
             "DNA sequences: their metabolisms inferred, their ecological roles guessed, their responses to a "
             "changing ocean unmeasured."),
 "why_it_matters": ("Microbes drive the ocean's carbon, nitrogen, sulfur, and iron cycles - every climate model "
             "that includes ocean biology is parameterizing organisms it has never grown. If the dark matter "
             "harbors major unrecognized metabolisms, our picture of ocean chemistry is wrong at its foundation. "
             "It is also a biotechnology reservoir: novel enzymes and compounds from lineages with no cultured "
             "representatives."),
 "sig_pointer": ("The Signature system proposes a function-first campaign: pair single-cell genomes with "
             "in-situ activity measurements and targeted cultivation, prioritizing the lineages that dominate "
             "gene counts in each biome. See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats microbial dark matter as a function gap, not a "
             "naming gap - genomes first, then measured activity, then cultivation of what matters most."),
 "signature_solution": (
     "Proposed approach. Step 1: complete single-cell genome sketches for the hundred most abundant uncultured "
     "lineages in each ocean biome, ranked by gene abundance in Tara-style metagenomes. Step 2: measure what "
     "they actually do in place - substrate uptake with isotope tracers and single-cell activity assays - "
     "because a genome is a parts list, not a physiology. Step 3: aim cultivation at the lineages whose measured "
     "activity dominates regional fluxes, using high-throughput dilution-to-extinction informed by the genomic "
     "parts lists. Step 4: encode the results as functional types for ecosystem models, replacing today's "
     "parameterizations with measured metabolisms.\n"
     "Assumptions: that abundance in metagenomes tracks ecological importance (usually but not always); that "
     "in-situ activity assays scale to the uncultured majority (technically demanding); that functional types "
     "capture enough of microbial diversity for models (an open simplification).\n"
     "What would confirm it: cultivated representatives whose measured physiology matches the in-situ activity, "
     "and model functional types that reproduce observed biogeochemical fluxes.\n"
     "What would kill it: systematic mismatch between genomic predictions and measured activity - the parts list "
     "refusing to predict the physiology.\n"
     "What this does NOT claim: it does not claim every microbe can or should be cultured; it does not promise "
     "biotech products; it is not established microbiology."),
 "citations": [
     "Sogin M L et al. Microbial diversity in the deep sea and the underexplored rare biosphere. Proc Natl Acad Sci; 2006.",
     "Sunagawa S et al. Structure and function of the global ocean microbiome. Science; 2015.",
     "Rappe M S, Giovannoni S J. The uncultured microbial majority. Annu Rev Microbiol; 2003."],
 "explorer": {
   "blurb": ("A rarefaction sketch: it models how observed microbial diversity climbs with sequencing effort, "
             "estimates the fraction of the community still unseen, and shows how cultivation success lags far "
             "behind detection."),
   "assumptions": {"true_types": 100000.0, "seq_effort": 20000.0, "half_saturation": 15000.0,
                   "cultured_frac": 0.01},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    obs = A[\"true_types\"] * A[\"seq_effort\"] / (A[\"seq_effort\"] + A[\"half_saturation\"])\n"
     "    return {\"types_observed\": obs, \"fraction_seen\": obs / A[\"true_types\"],\n"
     "            \"types_cultured\": A[\"true_types\"] * A[\"cultured_frac\"],\n"
     "            \"dark_fraction\": 1.0 - A[\"cultured_frac\"]}\n"),
   "steps": [("Microbial types detected by sequencing", "types_observed", ""),
             ("Fraction of true diversity seen", "fraction_seen", ""),
             ("Types with cultured representatives", "types_cultured", ""),
             ("Dark fraction (never cultured)", "dark_fraction", "")],
   "confirm": ["In-situ activity matches genomic predictions for top uncultured lineages.",
               "New functional types measurably improve model flux predictions.",
               "Cultivation guided by genomes succeeds where blind cultivation failed."],
   "refute": ["Genomic parts lists systematically fail to predict measured physiology.",
              "Activity assays prove unscalable to the uncultured majority."],
   "checks": [("fraction_seen", 0.3, 0.8), ("dark_fraction", 0.95, 1.0)],
   "honesty": ("Rarefaction curves describe sampling, not ecology. The dark matter is real; our map of what it "
               "does is mostly inference."),
 }},
# ---------------------------------------------------------------- 5
{
 "key": "sargassum-great-belt",
 "name": "What Drives the Great Atlantic Sargassum Belt?",
 "group": "Life and Ecosystems",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": ("Since 2011, floating Sargassum seaweed has exploded into a belt stretching across the tropical "
             "Atlantic, inundating Caribbean and West African beaches with millions of tons. What flipped the "
             "system from the historically stable Sargasso Sea to this recurring mega-bloom is still debated."),
 "background": ("Sargassum natans and fluitans have floated in the Sargasso Sea for centuries, but Wang and "
             "colleagues showed in 2019 that a new Great Atlantic Sargassum Belt now spans the equatorial "
             "Atlantic, peaking above 20 million tons in 2018. Competing explanations invoke increased nutrient "
             "discharge from the Amazon and Congo rivers, Saharan dust supplying iron, warming surface waters "
             "extending the growing season, and shifts in Atlantic circulation trapping the weed in a new "
             "recurrent pattern - with the 2010-2011 North Atlantic Oscillation anomaly as a possible trigger. "
             "Satellites now track the belt routinely, but attribution among the drivers, and therefore any "
             "forecast of next year bloom severity, remains contested."),
 "why_it_matters": ("The blooms devastate tourism economies, smother turtle nesting beaches and coral, and "
             "rot into hydrogen sulfide that sends residents to clinics - a recurring natural disaster for the "
             "Caribbean. Sargassum also sequesters carbon when it sinks, so its boom changes Atlantic carbon "
             "budgets. Forecasting bloom severity a season ahead would let islands prepare instead of react."),
 "sig_pointer": ("The Signature system proposes a driver-attribution experiment: coupled physical-biological "
             "hindcasts that switch each hypothesized driver on and off, scored against the satellite bloom "
             "record year by year. See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the Sargassum belt as an attribution problem - "
             "switch each driver off in the model and see which removal kills the bloom."),
 "signature_solution": (
     "Proposed approach. Step 1: build a basin-scale Sargassum drift-and-growth model forced by observed "
     "currents, temperature, and nutrient fields for 2010 to present. Step 2: run factorial experiments - "
     "remove the Amazon nutrient pulse, remove the dust iron, remove the warming trend, remove the circulation "
     "shift - one at a time and in combination, scoring each run against satellite bloom area. Step 3: use the "
     "winning driver combination to issue pre-season severity forecasts, published before each bloom season "
     "with the scorecard public. Step 4: test interventions only in the model - harvesting scenarios, "
     "nutrient-source scenarios - before anyone proposes them for the real Atlantic.\n"
     "Assumptions: that satellite-derived bloom area is a reliable ground truth (reasonable); that growth "
     "parameters measured in labs transfer to the open Atlantic (uncertain); that drivers combine separably "
     "enough for factorial attribution (may fail if interactions dominate).\n"
     "What would confirm it: one driver combination reproducing the year-to-year bloom record - timing, extent, "
     "and the 2011 onset - and then forecasting an out-of-sample season correctly.\n"
     "What would kill it: no combination reproducing the record, or the bloom proving driven by initial "
     "conditions and chaos rather than identifiable forcing.\n"
     "What this does NOT claim: it does not blame any single nation river; it does not endorse harvesting or "
     "sinking schemes; it is not established marine ecology."),
 "citations": [
     "Wang M et al. The great Atlantic Sargassum belt. Science; 2019.",
     "Smetacek V, Zingone A. Green and golden seaweed tides on the rise. Nature; 2013.",
     "Djakour et al. Sargassum proliferation analyses. Remote Sens; 2017."],
 "explorer": {
   "blurb": ("A bloom-growth sketch: it grows Sargassum biomass logistically under nutrient, temperature, and "
             "current-retention drivers, and shows how turning each driver off changes the peak bloom - the "
             "factorial attribution experiment in miniature."),
   "assumptions": {"nutrient": 1.0, "temperature": 1.0, "retention": 1.0, "growth_rate": 0.08,
                   "carrying_Mt": 22.0},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    driver = (A[\"nutrient\"] * 0.4 + A[\"temperature\"] * 0.3 + A[\"retention\"] * 0.3)\n"
     "    r = A[\"growth_rate\"] * driver\n"
     "    peak = A[\"carrying_Mt\"] * driver / (1.0 + math.exp(-r * 120.0) * 9.0)\n"
     "    no_nutrient = A[\"carrying_Mt\"] * (0.0 * 0.4 + A[\"temperature\"] * 0.3 + A[\"retention\"] * 0.3)\n"
     "    return {\"driver_index\": driver, \"peak_bloom_Mt\": peak,\n"
     "            \"no_nutrient_Mt\": no_nutrient * 0.9, \"sensitivity\": peak - no_nutrient * 0.9}\n"),
   "steps": [("Combined driver index", "driver_index", ""),
             ("Peak bloom biomass", "peak_bloom_Mt", "Mt"),
             ("Peak with nutrients removed", "no_nutrient_Mt", "Mt"),
             ("Nutrient attribution", "sensitivity", "Mt")],
   "confirm": ["One driver combination reproduces the satellite bloom record year by year.",
               "The model forecasts an out-of-sample bloom season correctly.",
               "Independent nutrient and current records corroborate the winning drivers."],
   "refute": ["No driver combination reproduces the 2011 onset and recurrence.",
              "The bloom proves chaos-dominated, with no identifiable forcing winning."],
   "checks": [("driver_index", 0.8, 1.2), ("peak_bloom_Mt", 10.0, 25.0)],
   "honesty": ("The driver weights are educated guesses. Real attribution needs the full coupled hindcast, not "
               "this sketch - but the factorial logic is exactly the experiment to run."),
 }},
# ---------------------------------------------------------------- 6
{
 "key": "marine-heatwave-origins",
 "name": "Why Do Marine Heatwaves Form, and Can They Be Forecast?",
 "group": "Waves and Extremes",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": ("Marine heatwaves - weeks to months of extreme ocean warmth like the 2013-2016 Pacific Blob - "
             "kill kelp forests, bleach corals, and collapse fisheries, yet their triggers differ from event "
             "to event and no system forecasts them reliably beyond days."),
 "background": ("Hobday and colleagues formalized the marine heatwave definition in 2016, and the catalog since "
             "has grown alarming: the Blob warmed the northeast Pacific by several degrees for over two years, "
             "the 2016 event bleached two-thirds of the northern Great Barrier Reef, and Tasman Sea heatwaves "
             "have wiped out kelp forests. Proposed triggers form a menu rather than a theory: persistent "
             "atmospheric high-pressure systems cutting wind and cloud, reduced ocean mixing shoaling the mixed "
             "layer, anomalous currents advecting warm water, and preconditioning by background warming. Because "
             "each event mixes these differently, predictability - the practical question for fisheries and "
             "reef managers - remains event-by-event detective work."),
 "why_it_matters": ("Marine heatwaves are the ocean extreme with the fastest-growing damages: collapsed "
             "fisheries, dead kelp and coral, toxic algal blooms, and seabird die-offs. A seasonal forecast with "
             "real skill would let managers close fisheries early, shade reefs, or move aquaculture - adaptation "
             "instead of triage. The events are also sentinels: how their frequency scales with background "
             "warming tests our whole understanding of ocean-atmosphere coupling."),
 "sig_pointer": ("The Signature system proposes a trigger-classified forecast system: label every historical "
             "heatwave by its dominant trigger from reanalysis, then train the forecast per trigger class "
             "rather than one-size-fits-all. See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats marine heatwaves as several distinct phenomena "
             "wearing one name - classify by trigger first, then forecast each class."),
 "signature_solution": (
     "Proposed approach. Step 1: build the trigger-labeled atlas - for every documented marine heatwave, use "
     "reanalysis to partition the warming among reduced mixing, anomalous advection, air-sea flux anomalies, "
     "and preconditioning. Step 2: develop per-class forecast models, because an atmosphere-driven event and a "
     "current-driven event have different predictability horizons. Step 3: issue seasonal outlooks per class "
     "with published hit rates, so managers learn which warnings to trust. Step 4: maintain the atlas as new "
     "events occur, letting the trigger taxonomy itself be falsified and revised.\n"
     "Assumptions: that reanalysis partitions triggers faithfully (model-dependent); that trigger classes are "
     "stable enough to forecast by (unproven); that managers will use probabilistic outlooks (mixed evidence).\n"
     "What would confirm it: per-class forecasts beating persistence and climatology at seasonal lead times, "
     "with the trigger labels predicting which events are forecastable.\n"
     "What would kill it: triggers proving inseparable in practice, or per-class models showing no skill gain "
     "over a single generic model.\n"
     "What this does NOT claim: it does not claim heatwaves are purely natural or purely anthropogenic per "
     "event; it does not promise skill where none exists; it is not established oceanography."),
 "citations": [
     "Hobday A J et al. A hierarchical approach to defining marine heatwaves. Prog Oceanogr; 2016.",
     "Bond N A et al. Causes and impacts of the 2014 warm anomaly in the NE Pacific (the Blob). Geophys Res Lett; 2015.",
     "Oliver E C J et al. Longer and more frequent marine heatwaves over the past century. Nat Commun; 2018."],
 "explorer": {
   "blurb": ("A mixed-layer heat budget: it warms a slab of ocean with anomalous air-sea heat flux, shoals the "
             "mixed layer, and computes how fast a heatwave-grade anomaly builds - the core physics behind "
             "atmosphere-triggered events."),
   "assumptions": {"heat_flux_Wm2": 40.0, "mixed_layer_m": 25.0, "days": 60.0, "threshold_C": 2.0},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    rho_cp = 1025.0 * 4000.0\n"
     "    dTdt = A[\"heat_flux_Wm2\"] / (rho_cp * A[\"mixed_layer_m\"])\n"
     "    warming = dTdt * A[\"days\"] * 86400.0\n"
     "    return {\"warming_rate_C_per_day\": dTdt * 86400.0, \"total_warming_C\": warming,\n"
     "            \"heatwave_reached\": 1.0 if warming > A[\"threshold_C\"] else 0.0,\n"
     "            \"days_to_threshold\": A[\"threshold_C\"] / (dTdt * 86400.0)}\n"),
   "steps": [("Warming rate", "warming_rate_C_per_day", "C/day"),
             ("Total warming over event", "total_warming_C", "C"),
             ("Heatwave threshold reached", "heatwave_reached", ""),
             ("Days to reach threshold", "days_to_threshold", "days")],
   "confirm": ["Per-class forecasts beat persistence at seasonal leads on independent events.",
               "Trigger labels predict which events are forecastable.",
               "Managers act on outlooks and avoid the worst losses."],
   "refute": ["Triggers prove inseparable; per-class models gain no skill.",
              "No forecast beats climatology beyond two weeks."],
   "checks": [("total_warming_C", 1.0, 6.0), ("days_to_threshold", 10.0, 120.0)],
   "honesty": ("A slab model ignores advection and entrainment - the two terms that often decide real events. "
               "It shows the trigger logic, not a forecast."),
 }},
# ---------------------------------------------------------------- 7
{
 "key": "kuroshio-large-meander",
 "name": "What Triggers Large Meanders of the Kuroshio?",
 "group": "Circulation",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": ("The Kuroshio, the Pacific counterpart of the Gulf Stream, usually flows straight past Japan - "
             "but every decade or so it swings into a giant offshore loop, the large meander, that persists "
             "for years and reshuffles regional climate and fisheries. No one can predict the flip."),
 "background": ("Since systematic observation began, the Kuroshio south of Japan has alternated between a "
             "straight path and a large-meander path looping far offshore, with meander episodes lasting from "
             "under a year to over a decade - the 2017 meander persisted for years. Theories compete: wind "
             "stress curl over the North Pacific priming the system, eddies arriving from the east kicking it "
             "offshore, interaction with the Izu-Ogasawara Ridge topography, and intrinsic nonlinear dynamics "
             "of the current itself. High-resolution models reproduce meander-like behavior, but the trigger in "
             "any given year - the forecast problem - remains out of reach, and the meander reshapes winter "
             "storm tracks, coastal sea level, and fish distributions while it lasts."),
 "why_it_matters": ("The Kuroshio feeds Japan: its path sets coastal water temperatures, the nutrient supply "
             "to fishing grounds, and sea level along the coast by tens of centimeters. A predicted meander "
             "would let fisheries and coastal managers plan years ahead instead of reacting. Scientifically, "
             "the meander is the cleanest natural experiment in western boundary current dynamics - cracking "
             "its trigger would illuminate the Gulf Stream and every current like it."),
 "sig_pointer": ("The Signature system proposes a meander-watch index combining upstream eddy energy, wind "
             "stress curl, and transport - with the flip forecast as a threshold crossing, calibrated on the "
             "historical meander record. See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the large meander as a threshold crossing - find "
             "the combined index that always crosses before a flip, and forecast the crossing."),
 "signature_solution": (
     "Proposed approach. Step 1: assemble the full historical record of Kuroshio path states with coincident "
     "upstream eddy kinetic energy, basin wind stress curl, and transport estimates. Step 2: search for a "
     "combined precursor index - not one variable but their joint state - that separates pre-meander years "
     "from straight-path years in the historical record. Step 3: test the index out of sample on the 2017 "
     "meander and in high-resolution model ensembles, where many synthetic flips can be examined. Step 4: run "
     "it operationally as a published meander outlook, scored openly year by year.\n"
     "Assumptions: that the historical record is long enough to define a threshold (only a handful of meanders "
     "exist - the binding weakness); that models generate realistic flips (partially true); that a single index "
     "captures a multi-cause trigger (may fail).\n"
     "What would confirm it: the index crossing before a future meander with no false alarms over a decade of "
     "operational use.\n"
     "What would kill it: a meander arriving with no precursor crossing, or repeated false alarms showing the "
     "threshold was overfit to a tiny sample.\n"
     "What this does NOT claim: it does not claim wind alone drives the meander; it does not promise "
     "deterministic timing; it is not established physical oceanography."),
 "citations": [
     "Kawabe M. Variations of the Kuroshio in the southern region of Japan. J Oceanogr; 1995.",
     "Qiu B, Chen S. Eddy-induced heat transport in the subtropical North Pacific. J Phys Oceanogr; 2005.",
     "Usui N et al. Long-term variability of the Kuroshio path. J Oceanogr; 2013."],
 "explorer": {
   "blurb": ("A threshold-crossing sketch: it combines eddy energy, wind forcing, and transport into one "
             "meander index, and shows how close the current system sits to the historical flip threshold."),
   "assumptions": {"eddy_energy": 0.7, "wind_curl": 0.6, "transport": 0.5, "threshold": 0.75},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    index = 0.45 * A[\"eddy_energy\"] + 0.35 * A[\"wind_curl\"] + 0.20 * A[\"transport\"]\n"
     "    margin = A[\"threshold\"] - index\n"
     "    p = 1.0 / (1.0 + math.exp(-12.0 * (index - A[\"threshold\"])))\n"
     "    return {\"meander_index\": index, \"threshold_margin\": margin,\n"
     "            \"flip_probability\": p, \"status\": 1.0 if index > A[\"threshold\"] else 0.0}\n"),
   "steps": [("Combined meander index", "meander_index", ""),
             ("Margin to flip threshold", "threshold_margin", ""),
             ("Flip probability this year", "flip_probability", ""),
             ("Meander state", "status", "")],
   "confirm": ["The index crosses before a future meander with no false alarms over a decade.",
               "Model ensembles reproduce the same threshold behavior.",
               "The precursor holds in the historical record without overfitting."],
   "refute": ["A meander arrives with no precursor crossing.",
              "Repeated false alarms reveal overfitting to a handful of events."],
   "checks": [("meander_index", 0.4, 0.9), ("flip_probability", 0.0, 1.0)],
   "honesty": ("With only a handful of historical meanders, any threshold is fragile. This sketch shows the "
               "forecast logic; the data to validate it do not yet exist."),
 }},
# ---------------------------------------------------------------- 8
{
 "key": "ocean-biological-geography",
 "name": "What Sets the Biological Geography of the Ocean?",
 "group": "Life and Ecosystems",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": ("Satellites show the ocean painted in biological provinces - green blooms at high latitudes, vast "
             "blue deserts in the subtropics - but why the boundaries fall where they do, and how they will "
             "move as the climate warms, is not settled."),
 "background": ("Longhurst divided the ocean into biogeochemical provinces in 1998, and satellite chlorophyll "
             "maps made the geography visible to everyone: productive upwelling zones and spring blooms versus "
             "the oligotrophic gyres covering much of the subtropics. John Martin iron hypothesis of 1990 - "
             "that iron shortage, not nitrogen, limits vast high-nutrient low-chlorophyll regions - was "
             "confirmed by the IronEx experiments, yet the full province map resists simple explanation: "
             "light, temperature, stratification, grazing, and micronutrients interact, and province boundaries "
             "are already observed shifting poleward. Models reproduce the broad pattern but disagree on the "
             "mechanisms setting the boundaries - which matters because the geography determines where the "
             "ocean food web, and the carbon pump, actually operate."),
 "why_it_matters": ("Fisheries, carbon uptake, and biodiversity all follow the biological geography. If the "
             "subtropical deserts expand with warming - as some analyses suggest - the productive ocean "
             "shrinks, with consequences for food security and the carbon cycle. Understanding the boundary "
             "physics is the difference between projecting that shift and being surprised by it."),
 "sig_pointer": ("The Signature system proposes boundary-tracking from space: define province edges from "
             "chlorophyll gradients, regress their movement against stratification, iron supply, and light, "
             "and let the data rank the drivers. See the Signature Edition record for the full labeled "
             "proposal."),
 "sig_lens": ("Signature lens: the Signature system treats biological provinces as moving boundaries - track "
             "the edges from satellites and let their motion reveal the controlling physics."),
 "signature_solution": (
     "Proposed approach. Step 1: define province boundaries objectively from multi-decadal satellite "
     "chlorophyll gradients, producing a moving-boundary dataset rather than static Longhurst polygons. "
     "Step 2: regress boundary motion against candidate drivers - mixed-layer depth, stratification, dust "
     "iron deposition, upwelling indices - in a framework that lets drivers compete rather than assuming one. "
     "Step 3: test the winning driver set by predicting boundary positions in years held out of the fit, and "
     "in ocean models run with altered iron or stratification. Step 4: project boundary positions under "
     "warming scenarios only through the validated driver relationships, with the uncertainty carried along.\n"
     "Assumptions: that chlorophyll gradients mark ecologically real boundaries (mostly true); that the "
     "satellite record is long enough to separate trend from variability (marginally); that drivers act "
     "smoothly enough for regression (may fail at sharp fronts).\n"
     "What would confirm it: out-of-sample boundary predictions verifying, and models with the validated "
     "drivers reproducing the observed province geography.\n"
     "What would kill it: boundaries proving set by food-web structure or history rather than physics, with "
     "no driver combination predicting their motion.\n"
     "What this does NOT claim: it does not claim iron explains everything; it does not fix fisheries "
     "quotas; it is not established biological oceanography."),
 "citations": [
     "Longhurst A. Ecological Geography of the Sea. Academic Press; 1998.",
     "Martin J H et al. Testing the iron hypothesis in ecosystems of the equatorial Pacific Ocean. Nature; 1994.",
     "Polovina J J et al. Ocean's least productive waters are expanding. Geophys Res Lett; 2008."],
 "explorer": {
   "blurb": ("A nutrient-light growth sketch: it grows phytoplankton under Monod nutrient limitation and light "
             "limitation, and shows which factor caps growth across a gradient from upwelling zone to "
             "subtropical gyre."),
   "assumptions": {"nitrate": 5.0, "iron": 0.3, "light": 0.8, "grazing": 0.4},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    n_lim = A[\"nitrate\"] / (A[\"nitrate\"] + 1.0)\n"
     "    fe_lim = A[\"iron\"] / (A[\"iron\"] + 0.2)\n"
     "    light_lim = A[\"light\"] / (A[\"light\"] + 0.3)\n"
     "    growth = 1.5 * min(n_lim, fe_lim) * light_lim\n"
     "    biomass = growth / (0.2 + A[\"grazing\"])\n"
     "    return {\"growth_rate\": growth, \"chlorophyll_index\": biomass,\n"
     "            \"limiting_factor\": 1.0 if fe_lim < n_lim else 0.0,\n"
     "            \"desert_index\": 1.0 - biomass / 3.0}\n"),
   "steps": [("Phytoplankton growth rate", "growth_rate", "/day"),
             ("Chlorophyll index", "chlorophyll_index", ""),
             ("Iron-limited (1) vs nitrogen-limited (0)", "limiting_factor", ""),
             ("Ocean-desert index", "desert_index", "")],
   "confirm": ["Boundary motion predictions verify out of sample.",
               "Models with validated drivers reproduce province geography.",
               "Independent iron and stratification records corroborate the ranking."],
   "refute": ["No driver combination predicts boundary motion - biology sets its own geography.",
              "Boundaries prove historically contingent rather than physically controlled."],
   "checks": [("growth_rate", 0.1, 1.5), ("chlorophyll_index", 0.2, 3.0)],
   "honesty": ("Monod curves are cartoons of real physiology, and grazing is crudely parameterized. The sketch "
               "shows the limitation logic that province boundaries must obey."),
 }},
# ---------------------------------------------------------------- 9
{
 "key": "deep-ocean-sounds",
 "name": "What Makes the Unexplained Sounds of the Deep Ocean?",
 "group": "Observing the Ocean",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": ("Hydrophone arrays hear powerful, structured sounds rising from the deep ocean - some identified "
             "as icequakes and volcanoes, others, like the seasonal Upsweep, still without a confirmed source "
             "after decades of listening."),
 "background": ("NOAA Pacific Marine Environmental Laboratory has recorded the deep sound channel since the "
             "1990s, cataloguing a bestiary: the Bloop, a powerful ultra-low-frequency signal eventually "
             "attributed in 2005 to ice calving and icequakes in Antarctica; the Slow Down, likely sea ice; "
             "the Julia, probably a large iceberg grounding; and the Upsweep - a repeating, seasonal, "
             "upsweeping whistle heard across the Pacific since 1991 with no confirmed source, hypothesized as "
             "undersea volcanic activity but never pinned down. The deep sound channel lets low-frequency "
             "sound travel thousands of kilometers, so one array hears a whole basin - which makes localization "
             "hard and every unexplained signal a genuine mystery rather than an artifact."),
 "why_it_matters": ("Unexplained basin-scale sounds may be undiscovered geological processes - new volcanic "
             "systems, ice dynamics - or unknown animal choruses, each a discovery in its own right. The "
             "listening arrays also monitor nuclear tests, earthquakes, and increasingly ocean noise pollution "
             "from shipping, so understanding the natural soundscape is the baseline for everything else the "
             "arrays are asked to detect."),
 "sig_pointer": ("The Signature system proposes targeted source localization: deploy temporary arrays around "
             "the Upsweep bearing, correlate detections with volcanic and ice catalogs, and publish the "
             "localization openly. See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats unexplained ocean sounds as localization problems "
             "- triangulate first, hypothesize second."),
 "signature_solution": (
     "Proposed approach. Step 1: run a dedicated localization campaign for the Upsweep using temporary "
     "hydrophone arrays positioned along its known bearing, achieving kilometer-scale fixes instead of "
     "basin-scale guesses. Step 2: correlate every localized detection against volcanic eruption catalogs, "
     "iceberg tracking, and seismic records in a pre-registered analysis - no post-hoc story fitting. Step 3: "
     "if volcanic, deploy seafloor instruments at the source for direct confirmation; if biological, record "
             "with directional arrays to characterize the call structure. Step 4: publish the full detection "
     "archive openly so the next unexplained sound starts from data, not legend.\n"
     "Assumptions: that the Upsweep source is stationary enough to localize (unknown); that temporary arrays "
     "can be funded and deployed (logistically hard); that correlation catalogs are complete enough "
     "(volcanic catalogs have gaps).\n"
     "What would confirm it: repeated kilometer-scale localizations coinciding with an observed volcanic or "
     "ice process, confirmed by independent seafloor instruments.\n"
     "What would kill it: localizations scattering across the basin with no repeatability, suggesting a "
     "propagation artifact rather than a real source.\n"
     "What this does NOT claim: it does not claim sea monsters or secret installations; it does not promise "
     "the source is interesting - only that it is localizable; it is not established marine science."),
 "citations": [
     "NOAA Pacific Marine Environmental Laboratory. Unexplained and unusual ocean sounds monitoring program.",
     "Dziak R P et al. Long-term ocean sound monitoring. Oceanography; 2011.",
     "Fox C G et al. Acoustic detection of seafloor volcanism. Geophys Res Lett; 2001."],
 "explorer": {
   "blurb": ("A sound-channel sketch: it computes how far a deep-ocean sound of given source level travels in "
             "the SOFAR channel before fading into noise - showing why one array hears a whole basin and why "
             "localization is so hard."),
   "assumptions": {"source_level_dB": 180.0, "noise_level_dB": 70.0, "frequency_Hz": 20.0},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    tl_allowed = A[\"source_level_dB\"] - A[\"noise_level_dB\"]\n"
     "    R_km = 10.0 ** (tl_allowed / 15.0) / 1000.0\n"
     "    R_km = min(R_km, 15000.0)\n"
     "    basin_fraction = R_km / 20000.0\n"
     "    return {\"detection_range_km\": R_km, \"basin_fraction_heard\": basin_fraction,\n"
     "            \"localization_km\": R_km * 0.05, \"tl_budget_dB\": tl_allowed}\n"),
   "steps": [("Detection range in the sound channel", "detection_range_km", "km"),
             ("Fraction of a basin heard", "basin_fraction_heard", ""),
             ("Typical localization uncertainty", "localization_km", "km"),
             ("Transmission-loss budget", "tl_budget_dB", "dB")],
   "confirm": ["Kilometer-scale localizations repeat at the same source.",
               "Detections correlate with an observed volcanic or ice process.",
               "Independent seafloor instruments confirm the source."],
   "refute": ["Localizations scatter irreproducibly across the basin.",
              "The signal proves to be a propagation artifact, not a source."],
   "checks": [("detection_range_km", 1000.0, 20000.0), ("tl_budget_dB", 90.0, 130.0)],
   "honesty": ("Spherical spreading is a crude propagation model - real channels focus and shadow sound. The "
               "sketch shows why basin-scale hearing makes localization the whole problem."),
 }},
# ---------------------------------------------------------------- 10
{
 "key": "tidal-energy-dissipation",
 "name": "Where Does All the Tidal Energy Go?",
 "group": "Circulation",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": ("The moon and sun pump about 3.7 terawatts of tidal energy into the ocean, and roughly a third "
             "of it must dissipate in the deep sea to sustain the abyssal circulation - yet the exact "
             "pathways from tides to turbulence to mixing are still being mapped."),
 "background": ("Munk and Wunsch showed in 1998 that maintaining the deep stratification against upwelling "
             "requires about 2 terawatts of mechanical mixing energy, launching the hunt for where tidal "
             "energy actually dissipates. Satellite altimetry revealed that internal tides - underwater waves "
             "at tidal frequencies - radiate from rough topography like the Hawaiian Ridge, carrying roughly "
             "1 terawatt. Microstructure measurements and the Brazil Basin experiment showed intense mixing "
             "over rough topography, but also that most internal-tide energy travels far before breaking, "
             "dissipating in ways - parametric subharmonic instability, scattering at continental slopes - "
             "that are observed in pieces but never closed into a global budget. The geography of dissipation "
             "determines the geography of deep upwelling, so the missing map matters for the whole "
             "circulation."),
 "why_it_matters": ("The deep overturning circulation ventilates the abyss, stores heat and carbon, and sets "
             "sea level patterns - and it is ultimately powered by this tidal dissipation. Climate models "
             "parameterize mixing with crude geography; getting the real dissipation map would tighten "
             "projections of deep-ocean heat uptake and carbon storage. It is also the largest energy "
             "cascade in the ocean, and we cannot fully account for it."),
 "sig_pointer": ("The Signature system proposes a dissipation census: combine altimetry-derived internal-tide "
             "fluxes with targeted microstructure transects along the energy propagation paths, closing the "
             "budget basin by basin. See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats tidal dissipation as an energy audit - follow each "
             "terawatt from generation to turbulence until the ledger balances."),
 "signature_solution": (
     "Proposed approach. Step 1: map internal-tide generation globally from altimetry and models, fixing the "
     "source term of the budget. Step 2: deploy microstructure and moored transects along the propagation "
     "paths - not just at generation sites - to measure where the energy actually breaks into turbulence. "
     "Step 3: test each proposed dissipation mechanism (parametric instability, slope scattering, wave-wave "
     "interaction) against the along-path decay, keeping only those that close the budget. Step 4: encode "
     "the resulting dissipation geography into climate-model mixing schemes and verify that deep stratification "
     "and ventilation improve.\n"
     "Assumptions: that altimetry captures the dominant low-mode internal tides (true for modes 1-2); that "
     "sparse microstructure transects represent their regions (the perennial sampling gamble); that the "
     "budget closes at the terawatt scale rather than leaking to unmeasured high modes (unproven).\n"
     "What would confirm it: basin budgets that close within uncertainties, and models with the new mixing "
     "geography reproducing observed deep stratification and tracer ages.\n"
     "What would kill it: persistent non-closure - measured dissipation far below the required 2 terawatts - "
     "implying a missing energy pathway or a wrong requirement.\n"
     "What this does NOT claim: it does not claim tides alone drive the circulation (winds matter); it does "
     "not promise a complete map on any schedule; it is not established physical oceanography."),
 "citations": [
     "Munk W, Wunsch C. Abyssal recipes II. Deep Sea Res I; 1998.",
     "Egbert G D, Ray R D. Significant dissipation of tidal energy in the deep ocean. Nature; 2000.",
     "Waterhouse A F et al. Global patterns of diapycnal mixing from measurements. J Phys Oceanogr; 2014."],
 "explorer": {
   "blurb": ("A tidal-energy ledger: it partitions the 3.7 terawatt input among shallow friction, internal-tide "
             "generation, and deep dissipation, and checks whether the deep pathways supply the mixing energy "
             "the abyssal circulation requires."),
   "assumptions": {"total_TW": 3.7, "shallow_frac": 0.68, "internal_tide_frac": 0.27, "required_deep_TW": 2.0},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    shallow = A[\"total_TW\"] * A[\"shallow_frac\"]\n"
     "    itide = A[\"total_TW\"] * A[\"internal_tide_frac\"]\n"
     "    deep = A[\"total_TW\"] - shallow\n"
     "    return {\"shallow_dissipation_TW\": shallow, \"internal_tide_TW\": itide,\n"
     "            \"deep_dissipation_TW\": deep, \"budget_gap_TW\": deep - A[\"required_deep_TW\"]}\n"),
   "steps": [("Dissipated in shallow seas", "shallow_dissipation_TW", "TW"),
             ("Radiated as internal tides", "internal_tide_TW", "TW"),
             ("Dissipated in the deep ocean", "deep_dissipation_TW", "TW"),
             ("Gap vs mixing requirement", "budget_gap_TW", "TW")],
   "confirm": ["Basin budgets close within stated uncertainties.",
               "Models with the new mixing geography reproduce deep tracer ages.",
               "Along-path measurements confirm the proposed decay mechanisms."],
   "refute": ["Measured dissipation stays far below the required 2 terawatts.",
              "The requirement itself proves wrong under better stratification data."],
   "checks": [("deep_dissipation_TW", 0.8, 1.6), ("internal_tide_TW", 0.7, 1.3)],
   "honesty": ("The fractions are literature values with real error bars, and the ledger omits wind-driven "
               "mixing entirely. It frames the audit; closing it needs the field campaign."),
 }},
# ---------------------------------------------------------------- 11
{
 "key": "ocean-cloud-seeding",
 "name": "How Does the Ocean Seed Clouds?",
 "group": "Ocean and Atmosphere",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": ("The ocean constantly seeds the atmosphere with particles - sea spray and the sulfur gas DMS - "
             "that become cloud droplets, yet how much of marine cloud cover the ocean itself controls, "
             "through the famous CLAW feedback loop, remains one of climate science longest-running arguments."),
 "background": ("Charlson, Lovelock, Andreae, and Warren proposed in 1987 the CLAW hypothesis: phytoplankton "
             "emit dimethyl sulfide, which oxidizes to particles that seed clouds, which cool the ocean - a "
             "planetary thermostat. Decades of testing have left it wounded but alive: DMS correlates with "
             "cloud condensation nuclei in remote regions, yet the full loop - biology responding to climate "
             "in the required direction - has never been demonstrated, and critics led by Quinn and Bates "
             "showed sea spray, not DMS, often dominates particle numbers. Newer work adds organic-rich sea "
             "spray from bursting bubbles as a major source. The question matters because marine low clouds "
             "are the largest uncertainty in climate sensitivity, and the ocean supplies their seeds."),
 "why_it_matters": ("If the ocean regulates its own cloud cover, climate sensitivity is lower and more stable "
             "than models assume - and deliberate marine cloud brightening proposals rest on the same physics. "
             "If it does not, the thermostat is a comforting story obscuring real vulnerability. Either way, "
             "the particle-to-cloud pathway is the lever by which ocean biology touches the planetary energy "
             "budget, and it is poorly quantified."),
 "sig_pointer": ("The Signature system proposes a loop-closure experiment: measure DMS flux, particle "
             "formation, cloud droplet number, and sunlight together on long ocean transects, testing each "
             "link of the CLAW chain in the same air mass. See the Signature Edition record for the full "
             "labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the CLAW loop as a chain of measurable links - "
             "test every link in the same air mass, and the loop stands or falls as a whole."),
 "signature_solution": (
     "Proposed approach. Step 1: run ship-and-aircraft transects across DMS-rich and DMS-poor regimes, "
     "measuring sea-to-air DMS flux, new particle formation, cloud condensation nuclei, droplet number, and "
     "cloud albedo in the same advected air mass. Step 2: test the feedback direction - does warming-driven "
     "stratification change DMS emission in the sign the thermostat requires - using multi-year records at "
     "fixed ocean stations. Step 3: separate the sea-spray and DMS contributions with size-resolved "
     "composition, ending the attribution argument with data. Step 4: encode only the validated links into "
     "climate models, labeled as validated or assumed.\n"
     "Assumptions: that Lagrangian air-mass tracking works over the needed days (feasible with modern "
     "trajectories); that fixed stations capture the feedback sign (they sample one regime); that the loop "
     "acts fast enough to observe (the weakest assumption - the thermostat may operate on long timescales).\n"
     "What would confirm it: the full chain - flux to particles to droplets to albedo - observed coherently "
     "in the same air mass, with the feedback sign confirmed at fixed stations.\n"
     "What would kill it: broken links - DMS flux failing to predict particle numbers, or the feedback sign "
     "reversing - reducing CLAW to disconnected true statements.\n"
     "What this does NOT claim: it does not endorse marine cloud brightening; it does not claim the ocean "
     "thermostat is real; it is not established atmospheric science."),
 "citations": [
     "Charlson R J et al. Oceanic phytoplankton, atmospheric sulphur, cloud albedo and climate. Nature; 1987.",
     "Quinn P K, Bates T S. The case against climate regulation via oceanic phytoplankton sulphur emissions. Nature; 2011.",
     "Ayers G P, Cainey J M. The CLAW hypothesis: a review. Environ Chem; 2007."],
 "explorer": {
   "blurb": ("A CLAW-chain sketch: it converts a DMS sea-to-air flux into particle numbers, then cloud droplet "
             "numbers, then a cloud-albedo change - showing how strong each link must be for the thermostat to "
             "matter."),
   "assumptions": {"dms_flux": 5.0, "yield": 0.3, "background_ccn": 100.0, "updraft": 0.5},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    ccn = A[\"background_ccn\"] + A[\"dms_flux\"] * A[\"yield\"] * 40.0\n"
     "    droplets = ccn * (0.5 + 0.2 * math.log10(max(ccn, 1.0)))\n"
     "    albedo_change = 0.05 * math.log(droplets / A[\"background_ccn\"]) / math.log(2.0)\n"
     "    return {\"ccn_per_cm3\": ccn, \"droplet_number\": droplets,\n"
     "            \"albedo_change\": albedo_change, \"chain_gain\": droplets / A[\"background_ccn\"]}\n"),
   "steps": [("Cloud condensation nuclei", "ccn_per_cm3", "/cm3"),
             ("Cloud droplet number", "droplet_number", "/cm3"),
             ("Cloud albedo change", "albedo_change", ""),
             ("Chain gain over background", "chain_gain", "x")],
   "confirm": ["The full chain observed coherently in the same air mass.",
               "Fixed stations confirm the feedback sign over years.",
               "Size-resolved data settle the spray-versus-DMS attribution."],
   "refute": ["DMS flux fails to predict particle numbers downwind.",
              "The feedback sign reverses or vanishes in long records."],
   "checks": [("ccn_per_cm3", 100.0, 400.0), ("albedo_change", 0.0, 0.15)],
   "honesty": ("Every conversion factor here is a placeholder for contested science. The sketch shows what "
               "must be measured, not what is known."),
 }},
# ---------------------------------------------------------------- 12
{
 "key": "ice-free-arctic-ocean",
 "name": "What Will an Ice-Free Arctic Ocean Look Like?",
 "group": "Ice and Coasts",
 "ladder_rank": 12, "ladder_tier": "foundations",
 "problem": ("Arctic sea ice is retreating toward seasonally ice-free conditions, likely within decades - "
             "but what the Arctic Ocean becomes afterward, ecologically and physically, is largely "
             "extrapolation rather than knowledge."),
 "background": ("September Arctic sea ice extent has fallen about 13 percent per decade since 1979, and "
             "CMIP6 models project the first ice-free September - under 1 million square kilometers - in the "
             "2040s to 2050s under high emissions, possibly sooner. Yet the transition is not just less ice: "
             "an open Arctic absorbs far more sunlight, mixes deeper in autumn storms, may ventilate heat "
             "upward from Atlantic water, and opens new light regimes for phytoplankton while destroying the "
             "ice-algae habitat that underpins the food web. Paleo analogs are imperfect - the last ice-free "
             "Arctic was millions of years ago under different geography - and models disagree on whether "
             "productivity booms or stratification starves the surface."),
 "why_it_matters": ("The Arctic transition rearranges Northern Hemisphere weather, opens shipping routes and "
             "resource disputes, and transforms Indigenous livelihoods built around ice. Ecologically it is a "
             "whole-ocean regime shift happening within a human lifetime - the closest thing to a controlled "
             "experiment in planetary-scale change, and we are running it without a clear prediction of the "
             "outcome."),
 "sig_pointer": ("The Signature system proposes a transition watch: sustained year-round observations of the "
             "Arctic water column, light, and food web through the ice-free transition, designed to catch the "
             "regime shift as it happens. See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the ice-free Arctic as a regime shift to be caught "
             "in the act - instrument the transition, not just the endpoints."),
 "signature_solution": (
     "Proposed approach. Step 1: maintain year-round Arctic observing - ice-tethered profilers successors, "
     "under-ice floats, moorings - through the transition decades, because the shift will be observed or "
     "missed in the autumn freeze-up and spring bloom windows. Step 2: track the candidate tipping "
     "mechanisms directly: Atlantic water heat reaching the surface, stratification versus storm mixing, "
     "ice-algae versus pelagic production. Step 3: run high-resolution Arctic models with the observed "
     "transition as a test - models must reproduce the change as it happens, not just hindcast it later. "
     "Step 4: publish an annual Arctic transition report card with the regime indicators, so the shift is "
     "documented as a time series, not reconstructed from memory.\n"
     "Assumptions: that observing infrastructure survives the geopolitics of the Arctic (fragile); that "
     "decades of continuity can be funded (historically hard); that the transition is gradual enough to "
     "observe rather than abrupt (likely but unproven).\n"
     "What would confirm it: the observing system capturing the mechanism sequence - which tipping "
     "processes fire in which order - as the ice disappears.\n"
     "What would kill it: the transition arriving as a single abrupt flip with the observing system blind "
     "at the critical moment, or geopolitics closing the Arctic to science.\n"
     "What this does NOT claim: it does not set the date of the first ice-free September; it does not "
     "adjudicate shipping or resource disputes; it is not established polar science."),
 "citations": [
     "Stroeve J, Notz D. Changing state of Arctic sea ice across all seasons. Environ Res Lett; 2018.",
     "Polyakov I V et al. Arctic Ocean warming. Science; 2017.",
     "IPCC AR6 WGI, Chapter 9: Ocean, Cryosphere and Sea Level Change; 2021."],
 "explorer": {
   "blurb": ("An ice-albedo sketch: it projects September ice extent from the observed trend, accelerates the "
             "loss with the albedo feedback as open water grows, and estimates the first ice-free year under "
             "different feedback strengths."),
   "assumptions": {"extent_2020_Mkm2": 3.9, "trend_Mkm2_per_dec": 0.8, "albedo_feedback": 0.3},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    trend = A[\"trend_Mkm2_per_dec\"] * (1.0 + A[\"albedo_feedback\"])\n"
     "    years = (A[\"extent_2020_Mkm2\"] - 1.0) / (trend / 10.0)\n"
     "    ice_free_year = 2020.0 + years\n"
     "    return {\"effective_trend\": trend, \"years_to_ice_free\": years,\n"
     "            \"ice_free_year\": ice_free_year, \"feedback_gain\": 1.0 + A[\"albedo_feedback\"]}\n"),
   "steps": [("Effective loss trend", "effective_trend", "Mkm2/decade"),
             ("Years to ice-free September", "years_to_ice_free", "yr"),
             ("Projected first ice-free year", "ice_free_year", ""),
             ("Albedo feedback gain", "feedback_gain", "x")],
   "confirm": ["The observing system captures the mechanism sequence of the transition.",
               "Models reproduce the change as it happens, not just in hindcast.",
               "Annual report cards document a coherent regime shift."],
   "refute": ["The transition arrives as an unobserved abrupt flip.",
              "Geopolitics or funding gaps blind the critical years."],
   "checks": [("ice_free_year", 2030.0, 2080.0), ("years_to_ice_free", 10.0, 60.0)],
   "honesty": ("Linear trends with a feedback fudge factor are not a prediction. The real date depends on "
               "emissions and variability this sketch ignores - the value is in the watch, not the year."),
 }},
# ---------------------------------------------------------------- 13
{
 "key": "seabed-2030-mapping",
 "name": "Can We Map the Entire Seafloor by 2030?",
 "group": "Observing the Ocean",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": ("Seabed 2030 - the Nippon Foundation-GEBCO project - aims to map the entire ocean floor by "
             "2030, yet only about a quarter is mapped at useful resolution, and the current pace may not "
             "close the gap without a radical change in how mapping is done."),
 "background": ("Humanity has better maps of the Moon and Mars than of its own seafloor: as of the mid-2020s "
             "roughly 25 percent of the ocean floor is mapped with modern multibeam sonar, the rest known "
             "only through coarse satellite-altimetry gravity estimates that miss features smaller than "
             "several kilometers - including most seamounts and all habitat-scale structure. Seabed 2030 "
             "coordinates the global effort, but ship time is expensive and the unmapped ocean is vast and "
             "remote, concentrated in the Southern Ocean and deep Pacific. New tools - autonomous surface "
             "vessels, opportunistic transit data from commercial ships, machine-learning interpolation - "
             "promise acceleration, but whether they can quadruple effective coverage in a few years is "
             "unproven, and the deep-sea ecosystems that need maps most urgently are the least mapped."),
 "why_it_matters": ("Every tsunami model, submarine cable route, fisheries habitat map, and deep-sea mining "
             "claim depends on knowing what is down there. Unmapped seamounts are unprotected biodiversity "
             "hotspots; unmapped trenches hide earthquake hazards. A complete map is the base layer for all "
             "deep-ocean science and stewardship - and the 2030 deadline is the forcing function making it "
             "happen."),
 "sig_pointer": ("The Signature system proposes a coverage triage: rank unmapped regions by hazard and "
             "biodiversity value, aim autonomous fleets at the highest-value gaps, and publish a live "
             "completion meter. See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats seafloor mapping as a triage problem - map the "
             "highest-value gaps first, and let a public completion meter drive the effort."),
 "signature_solution": (
     "Proposed approach. Step 1: publish the live value-weighted gap map - unmapped area scored by tsunami "
     "hazard, cable routes, seamount likelihood, and mining-claim overlap - so every ship day goes where it "
     "matters most. Step 2: scale autonomous surface vessels on the highest-value remote gaps, where crewed "
     "ships are prohibitively expensive, with data standards identical to ship surveys. Step 3: mandate "
     "transit-data sharing from commercial and research vessels - the ocean is crossed daily by ships whose "
     "echo sounders record but discard data. Step 4: hold the 2030 target honest with the public completion "
     "meter, and if the pace falls short, say so early enough to change strategy.\n"
     "Assumptions: that autonomous vessels achieve survey-grade data (approaching true); that commercial "
     "fleets will share data (needs incentives or mandates); that value-weighting is politically acceptable "
     "(some regions will object to being deprioritized).\n"
     "What would confirm it: the completion meter accelerating toward 100 percent with autonomous and "
     "transit data carrying the remote gaps, verified by independent quality audits.\n"
     "What would kill it: the meter stalling below 50 percent as easy areas finish and hard areas resist "
     "automation, or data-quality audits failing the new sources.\n"
     "What this does NOT claim: it does not claim satellite gravity can substitute for sonar; it does not "
     "promise 2030 will be met; it is not established marine geophysics."),
 "citations": [
     "Mayer L et al. The Nippon Foundation-GEBCO Seabed 2030 Project. Oceanography; 2018.",
     "Sandwell D T et al. New global marine gravity model from CryoSat-2 and Jason-1. Science; 2014.",
     "Wessel P et al. The Generic Mapping Tools and seafloor mapping. Oceanography; 2018."],
 "explorer": {
   "blurb": ("A mapping-race model: it projects seafloor coverage from ship, autonomous, and transit-data "
             "rates, and shows which combination reaches 100 percent by 2030 - and what happens if the new "
             "sources underperform."),
   "assumptions": {"mapped_frac": 0.25, "ship_rate": 0.02, "auto_rate": 0.03, "transit_rate": 0.02,
                   "deadline": 2030.0, "now": 2026.0},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    years = A[\"deadline\"] - A[\"now\"]\n"
     "    rate = A[\"ship_rate\"] + A[\"auto_rate\"] + A[\"transit_rate\"]\n"
     "    projected = A[\"mapped_frac\"] + rate * years\n"
     "    ship_only = A[\"mapped_frac\"] + A[\"ship_rate\"] * years\n"
     "    return {\"combined_rate_per_yr\": rate, \"projected_2030\": projected,\n"
     "            \"ship_only_2030\": ship_only, \"gap_to_target\": 1.0 - projected}\n"),
   "steps": [("Combined mapping rate", "combined_rate_per_yr", "/yr"),
             ("Projected 2030 coverage", "projected_2030", ""),
             ("Ships-alone 2030 coverage", "ship_only_2030", ""),
             ("Gap to full coverage", "gap_to_target", "")],
   "confirm": ["The completion meter accelerates with autonomous and transit data verified by audits.",
               "High-value gaps close first under the triage map.",
               "2030 arrives with the map essentially complete."],
   "refute": ["Coverage stalls below half as hard areas resist automation.",
              "Quality audits fail the new data sources."],
   "checks": [("projected_2030", 0.3, 1.2), ("combined_rate_per_yr", 0.03, 0.12)],
   "honesty": ("Constant rates are optimistic - the easy ocean maps first and rates decay. The sketch shows "
               "the arithmetic the 2030 target must satisfy, not a forecast that it will."),
 }},
# ---------------------------------------------------------------- 14
{
 "key": "vent-origin-of-life",
 "name": "Did Life Begin at Deep-Sea Vents?",
 "group": "Deep Ocean",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": ("One of the leading theories for the origin of life places it at alkaline deep-sea vents, where "
             "natural proton gradients could have powered the first metabolism - but the leap from vent "
             "chemistry to living cells remains unbridged."),
 "background": ("Russell and colleagues proposed in the 1990s that alkaline hydrothermal vents - like the "
             "Lost City field discovered by Kelley in 2000, venting warm pH-11 fluid into acidic early oceans - "
             "provided exactly what life needed: mineral compartments concentrating reactants, and a natural "
             "proton gradient across thin mineral walls, the same gradient all cells use to make ATP today. "
             "Martin and Russell formalized the chemistry in 2003-2007, and laboratory experiments have since "
             "shown vent-like conditions synthesizing organics and even driving protometabolic reactions. "
             "Competing theories - Darwin warm little pond, hydrothermal pools, delivery by meteorites - each "
             "have strengths, and the vent theory fairest criticism is that no experiment has crossed from "
             "chemistry to anything that replicates, evolves, or deserves the name alive."),
 "why_it_matters": ("The origin of life is the deepest question in science, and the vent theory is its most "
             "geologically grounded answer: if life began at vents, then life should be common wherever rocky "
             "planets have oceans - Europa, Enceladus, exoplanets. If vents cannot bridge the gap, the search "
             "for life elsewhere must look to different environments. The theory also frames what to look for "
             "in ancient rocks and on other worlds."),
 "sig_pointer": ("The Signature system proposes a bridge-or-break program: staged vent-simulator experiments "
             "that must each clear a pre-registered chemical milestone toward replication, with failures "
             "published as loudly as successes. See the Signature Edition record for the full labeled "
             "proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the vent origin as a milestone ladder - define the "
             "chemical steps to replication, and require each to be demonstrated, not assumed."),
 "signature_solution": (
     "Proposed approach. Step 1: define the milestone ladder explicitly - gradient-driven CO2 reduction, "
     "sustained protometabolic cycles, template-directed polymerization, compartment replication - with "
     "measurable pass criteria for each. Step 2: run vent-simulator flow reactors against the ladder, "
     "pre-registering each milestone before the experiment, so near-misses cannot be relabeled as successes. "
     "Step 3: require the failures to be published and mined - the conditions that do not work constrain the "
     "theory as much as the ones that do. Step 4: compare against the competing theories on the same "
     "milestone ladder, so the field converges on which environment clears the most rungs.\n"
     "Assumptions: that laboratory simulators capture the essential vent physics (they simplify drastically); "
     "that the milestone ladder is the right decomposition (philosophically loaded); that negative results "
     "get published and funded (culturally hard).\n"
     "What would confirm it: a vent simulator clearing successive milestones up to template-directed "
     "polymerization under pre-registered criteria, with independent replication.\n"
     "What would kill it: persistent failure at an early rung despite exhaustive conditions - or a competing "
     "environment clearing rungs the vents cannot.\n"
     "What this does NOT claim: it does not claim life did begin at vents; it does not claim the ladder "
     "captures everything about life; it is not established geobiology."),
 "citations": [
     "Martin W, Russell M J. On the origins of cells. Philos Trans R Soc B; 2003.",
     "Kelley D S et al. A serpentinite-hosted ecosystem: the Lost City hydrothermal field. Science; 2005.",
     "Sojo V et al. The origin of life in alkaline hydrothermal vents. Astrobiology; 2016."],
 "explorer": {
   "blurb": ("A vent-energetics sketch: it computes the proton-motive force available across a vent mineral "
             "wall from the pH gradient, converts it to free energy per mole of protons, and compares it to "
             "the energy cost of making ATP - the quantitative core of the vent-origin argument."),
   "assumptions": {"ph_inside": 11.0, "ph_outside": 5.5, "temperature_C": 70.0, "atp_cost_kJ": 50.0},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    T = A[\"temperature_C\"] + 273.15\n"
     "    dph = A[\"ph_inside\"] - A[\"ph_outside\"]\n"
     "    pmf_V = 2.303 * 8.314 * T / 96485.0 * dph\n"
     "    dG_kJ = -96485.0 * pmf_V / 1000.0\n"
     "    return {\"proton_motive_force_V\": pmf_V, \"free_energy_kJ_per_mol\": -dG_kJ,\n"
     "            \"atp_equivalents\": -dG_kJ / A[\"atp_cost_kJ\"], \"gradient_pH_units\": dph}\n"),
   "steps": [("Proton-motive force across wall", "proton_motive_force_V", "V"),
             ("Free energy per mole of protons", "free_energy_kJ_per_mol", "kJ/mol"),
             ("ATP equivalents per proton", "atp_equivalents", ""),
             ("pH gradient", "gradient_pH_units", "units")],
   "confirm": ["Vent simulators clear successive pre-registered milestones toward replication.",
               "Independent labs replicate the milestone crossings.",
               "Competing environments clear fewer rungs on the same ladder."],
   "refute": ["Persistent failure at an early rung under exhaustive conditions.",
              "A competing environment demonstrably clears rungs the vents cannot."],
   "checks": [("proton_motive_force_V", 0.2, 0.5), ("atp_equivalents", 0.3, 1.0)],
   "honesty": ("Free energy is necessary, not sufficient - having the energy says nothing about the mechanism "
               "that would harness it. The sketch quantifies the theory best argument, not its proof."),
 }},
# ---------------------------------------------------------------- 15
{
 "key": "carbon-pump-efficiency",
 "name": "How Efficient Is the Biological Carbon Pump of the Ocean?",
 "group": "Carbon and Climate",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": ("The biological carbon pump carries roughly 5 to 12 billion tons of carbon into the deep ocean "
             "each year - but what fraction survives the gauntlet of hungry microbes to stay sequestered, and "
             "how that efficiency varies across the ocean, is poorly constrained."),
 "background": ("Martin and colleagues VERTEX program in 1987 gave the field its working curve: sinking "
             "particle flux attenuates with depth as a power law, the Martin curve, with most surface export "
             "remineralized in the upper kilometer. Buesseler and others have since shown the transfer "
             "efficiency to 1000 meters varies enormously - high-latitude blooms export efficiently, "
             "subtropical systems barely at all - depending on plankton community, ballast minerals, and "
             "zooplankton repackaging. Yet global estimates still lean on a handful of sediment-trap sites "
             "and satellite proxies, the twilight-zone transformations are observed in fragments, and models "
             "disagree on whether pump efficiency will strengthen or weaken as the ocean warms - a first-order "
             "uncertainty in the future carbon sink."),
 "why_it_matters": ("The biological pump is one of the largest carbon fluxes on the planet, comparable to "
             "human emissions, and its efficiency sets how much carbon the ocean locks away for centuries. "
             "Proposals to fertilize the ocean with iron to draw down CO2 stand or fall on transfer "
             "efficiency: carbon remineralized at 200 meters returns to the air in years; carbon reaching "
             "2000 meters stays for centuries. Without the efficiency map, neither climate projections nor "
             "geoengineering claims can be trusted."),
 "sig_pointer": ("The Signature system proposes an efficiency atlas: standardized particle-flux profiles from "
             "autonomous floats and traps across all biomes, with transfer efficiency mapped like a weather "
             "variable. See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats pump efficiency as a mappable field - measure the "
             "transfer profile in every biome until the map, not the average, is known."),
 "signature_solution": (
     "Proposed approach. Step 1: deploy a global array of profiling floats with optical sediment-trap proxies "
     "and neutrally buoyant traps, measuring flux attenuation profiles in every major biome with one "
     "intercalibrated method. Step 2: pair the profiles with plankton community and particle-size data, so "
     "efficiency can be predicted from observable ecosystem state rather than fitted per region. Step 3: "
     "test the predictions against independent deep-trap records and thorium-234 budgets. Step 4: maintain "
     "the efficiency atlas as a living product - the baseline against which any fertilization experiment "
     "must be judged, and an input to carbon-cycle models that currently guess.\n"
     "Assumptions: that optical proxies can be intercalibrated to real flux (the key technical bet); that "
     "biome-scale efficiency is stable enough to map (seasonality is strong); that community composition "
     "predicts efficiency causally rather than coincidentally (unproven).\n"
     "What would confirm it: the atlas predicting independent trap and thorium measurements, and models "
     "using it reproducing deep-ocean carbon storage patterns.\n"
     "What would kill it: efficiency proving dominated by episodic events the array misses, or proxies "
     "failing intercalibration so the map is noise.\n"
     "What this does NOT claim: it does not endorse iron fertilization; it does not fix the pump strength; "
     "it is not established biogeochemistry."),
 "citations": [
     "Martin J H et al. VERTEX: carbon cycling in the northeast Pacific. Deep Sea Res; 1987.",
     "Buesseler K O et al. Revisiting carbon flux through the ocean twilight zone. Science; 2007.",
     "Henson S A et al. Global patterns in efficiency of particulate organic carbon export. Global Biogeochem Cycles; 2012."],
 "explorer": {
   "blurb": ("A Martin-curve sketch: it attenuates surface export down the water column with the power-law "
             "exponent, computes transfer efficiency to 1000 and 2000 meters, and shows how a small change in "
             "the exponent transforms sequestration."),
   "assumptions": {"export_100m": 10.0, "martin_b": 0.86, "depth_m": 1000.0},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    z = A[\"depth_m\"] / 100.0\n"
     "    flux = A[\"export_100m\"] * z ** (-A[\"martin_b\"])\n"
     "    te = flux / A[\"export_100m\"]\n"
     "    flux2k = A[\"export_100m\"] * 20.0 ** (-A[\"martin_b\"])\n"
     "    return {\"flux_at_depth\": flux, \"transfer_efficiency\": te,\n"
     "            \"flux_at_2000m\": flux2k, \"sequestered_fraction\": flux2k / A[\"export_100m\"]}\n"),
   "steps": [("Particle flux at target depth", "flux_at_depth", "units"),
             ("Transfer efficiency to target depth", "transfer_efficiency", ""),
             ("Flux reaching 2000 m", "flux_at_2000m", "units"),
             ("Centuries-scale sequestered fraction", "sequestered_fraction", "")],
   "confirm": ["The atlas predicts independent trap and thorium-234 budgets.",
               "Models using the atlas reproduce deep carbon storage patterns.",
               "Community composition predicts efficiency causally."],
   "refute": ["Efficiency proves event-dominated and unmappable by arrays.",
              "Optical proxies fail intercalibration; the map is noise."],
   "checks": [("transfer_efficiency", 0.05, 0.3), ("sequestered_fraction", 0.02, 0.15)],
   "honesty": ("The Martin curve is an empirical fit, not a mechanism - and the exponent varies more than "
               "the textbooks admit. The sketch shows why that variation is the whole game."),
 }},
# ---------------------------------------------------------------- 16
{
 "key": "twilight-zone-biomass",
 "name": "How Much Life Hides in the Twilight Zone?",
 "group": "Life and Ecosystems",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": ("The mesopelagic - the ocean twilight zone from 200 to 1000 meters - may hold ten billion tons "
             "of fish, an order of magnitude more than previously thought, yet the estimate rests on acoustic "
             "echoes that could be off by a factor of ten either way."),
 "background": ("Irigoien and colleagues reported in 2014 that acoustic backscatter implied mesopelagic fish "
             "biomass around 10 billion tons - ten times the previous estimate and more than all current "
             "fisheries catches combined. The claim electrified biologists and industry alike, but acoustics "
             "measure echoes, not fish: converting backscatter to biomass requires knowing the species mix, "
             "their swim bladders, sizes, and orientations - all poorly sampled because trawls avoid or miss "
             "the agile inhabitants. The twilight zone also drives the carbon pump through the largest animal "
             "migration on Earth, the nightly vertical migration, so its biomass sets the scale of active "
             "carbon transport - another quantity hanging on the same uncertain number."),
 "why_it_matters": ("Ten billion tons of fish would be the largest fishery on Earth and a protein source of "
             "last resort - but harvesting the twilight zone without knowing its biomass or its role in "
             "carbon transport risks repeating the collapses of surface fisheries at planetary scale. The "
             "number also anchors the active carbon flux: get the biomass wrong and the biological pump "
             "budget is wrong with it."),
 "sig_pointer": ("The Signature system proposes a biomass reconciliation: coordinated acoustic surveys "
             "calibrated by in-situ imaging, genetics, and targeted trawls on the same transects, until the "
             "echo-to-fish conversion is measured, not assumed. See the Signature Edition record for the "
             "full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats twilight-zone biomass as a calibration problem - "
             "measure the echo and the fish together until the conversion is data, not assumption."),
 "signature_solution": (
     "Proposed approach. Step 1: run co-located surveys - multi-frequency acoustics, towed imaging, "
     "environmental DNA, and carefully designed trawls - on the same transects across biomes, so every echo "
     "has a ground-truth counterpart. Step 2: build the open echo-to-biomass library by species and size "
     "class, replacing the single conversion factor with measured distributions. Step 3: reprocess the "
     "global acoustic archive through the library, producing a biomass estimate with honest, propagated "
     "uncertainty. Step 4: establish the monitoring baseline before any commercial harvest begins, so the "
     "fishery - if it ever comes - starts from knowledge rather than hope.\n"
     "Assumptions: that trawls and imaging sample representatively despite avoidance (the central "
     "difficulty); that eDNA quantifies abundance usefully (semi-quantitative at best); that a global "
     "reprocessing is funded before harvest pressure forces hasty numbers (politically uncertain).\n"
     "What would confirm it: independent methods - acoustics, imaging, eDNA - converging on the same "
     "biomass within a factor of two across biomes.\n"
     "What would kill it: persistent order-of-magnitude disagreement between methods, implying the "
     "conversion is fundamentally underdetermined.\n"
     "What this does NOT claim: it does not endorse harvesting the twilight zone; it does not fix the 10 "
     "billion ton number; it is not established fisheries science."),
 "citations": [
     "Irigoien X et al. Large mesopelagic fishes biomass and trophic efficiency. Nat Commun; 2014.",
     "Davison P C et al. Carbon export mediated by mesopelagic fishes. Limnol Oceanogr; 2013.",
     "St John M A et al. A dark hole in our understanding of marine ecosystems. ICES J Mar Sci; 2016."],
 "explorer": {
   "blurb": ("An echo-to-biomass sketch: it converts acoustic backscatter to fish biomass under different "
             "target-strength assumptions, showing how the ten-billion-ton headline slides by an order of "
             "magnitude with the conversion factor."),
   "assumptions": {"backscatter": 1.0, "target_strength": -60.0, "mean_weight_g": 10.0, "area_Mkm2": 200.0},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    sigma = 10.0 ** (A[\"target_strength\"] / 10.0)\n"
     "    density_per_m2 = A[\"backscatter\"] * 1e-6 / sigma\n"
     "    biomass_t = density_per_m2 * A[\"mean_weight_g\"] / 1e6 * A[\"area_Mkm2\"] * 1e12\n"
     "    Gt = biomass_t / 1e9\n"
     "    return {\"biomass_Gt\": Gt, \"density_per_m2\": density_per_m2,\n"
     "            \"vs_fisheries_catch\": Gt / 0.1, \"target_sigma\": sigma}\n"),
   "steps": [("Estimated mesopelagic biomass", "biomass_Gt", "Gt"),
             ("Fish density", "density_per_m2", "/m2"),
             ("Multiple of global fisheries catch", "vs_fisheries_catch", "x"),
             ("Acoustic cross-section", "target_sigma", "m2")],
   "confirm": ["Acoustics, imaging, and eDNA converge within a factor of two across biomes.",
               "The echo library predicts independent trawl catches.",
               "A monitoring baseline exists before any harvest."],
   "refute": ["Methods disagree by an order of magnitude persistently.",
              "Avoidance proves uncorrectable; the conversion stays underdetermined."],
   "checks": [("biomass_Gt", 1.0, 30.0), ("vs_fisheries_catch", 10.0, 300.0)],
   "honesty": ("The target strength is the whole argument compressed into one number - change it by 10 dB "
               "and the headline moves tenfold. That sensitivity is the point of the sketch."),
 }},
# ---------------------------------------------------------------- 17
{
 "key": "oxygen-minimum-expansion",
 "name": "Why Are Ocean Oxygen Minimum Zones Expanding?",
 "group": "Ocean Chemistry",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": ("Oxygen minimum zones - vast mid-water regions where oxygen falls too low for most animals - "
             "have been growing for decades, compressing habitat and rewiring nitrogen chemistry, but how "
             "much is warming, how much is circulation, and where it ends is unresolved."),
 "background": ("Stramma and colleagues documented in 2008 that tropical oxygen minimum zones were expanding "
             "and intensifying, a trend since confirmed across the Pacific and Atlantic. Two mechanisms "
             "share the blame: warming water holds less dissolved oxygen and stratifies more strongly, "
             "reducing ventilation; and changes in circulation and productivity alter the respiration demand. "
             "Their relative weight matters because they imply different futures - solubility decline is "
             "thermodynamic and certain, circulation change is dynamical and uncertain. Expanding low-oxygen "
             "water also expands denitrification, which removes bioavailable nitrogen and emits nitrous "
             "oxide, a potent greenhouse gas - a feedback loop whose strength is essentially unmeasured."),
 "why_it_matters": ("Oxygen minimum zones already compress the habitable water column for tunas, billfish, and "
             "squid, pushing predators into thinner surface layers where fisheries find them - an "
             "easier catch masking a shrinking habitat. The nitrogen feedback touches the planetary nutrient "
             "budget and the greenhouse balance. Understanding the expansion is understanding how much "
             "habitable ocean the future holds."),
 "sig_pointer": ("The Signature system proposes an oxygen attribution budget: separate solubility, "
             "ventilation, and respiration trends with sustained oxygen sensor arrays and transient tracers. "
             "See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats OMZ expansion as a budget to be partitioned - "
             "solubility, ventilation, and respiration each get their own measured trend."),
 "signature_solution": (
     "Proposed approach. Step 1: expand sustained oxygen observations - Biogeochemical-Argo floats with "
     "oxygen sensors plus repeat hydrography - until the OMZ boundaries are tracked as routinely as sea "
     "surface temperature. Step 2: partition each region oxygen trend into the solubility component "
     "(computed from temperature), the ventilation component (from transient tracers like CFCs and SF6), "
     "and the residual respiration component. Step 3: measure the denitrification and nitrous oxide "
     "response at expanding OMZ edges, closing the feedback loop observationally. Step 4: require models "
     "to reproduce the partitioned trends - not just total oxygen - before trusting their OMZ projections.\n"
     "Assumptions: that oxygen sensors stay calibrated over multi-year float missions (improving but "
     "imperfect); that transient tracers resolve ventilation on the right timescales (decadal, roughly "
     "right); that partitioning is additive enough to be meaningful (interactions exist).\n"
     "What would confirm it: partitioned budgets that sum to the observed trends across basins, and models "
     "that reproduce each component passing the projection test.\n"
     "What would kill it: the residual respiration term dominating irreproducibly, or sensor drift "
     "corrupting the long records the whole attribution rests on.\n"
     "What this does NOT claim: it does not claim OMZs will keep expanding linearly; it does not set "
     "fisheries policy; it is not established chemical oceanography."),
 "citations": [
     "Stramma L et al. Expanding oxygen-minimum zones in the tropical oceans. Science; 2008.",
     "Schmidtko S et al. Decline in global oceanic oxygen content during the past five decades. Nature; 2017.",
     "Breitburg D et al. Declining oxygen in the global ocean and coastal waters. Science; 2018."],
 "explorer": {
   "blurb": ("An oxygen-budget sketch: it declines oxygen from solubility loss as water warms and from "
             "weakening ventilation, and shows which term dominates the expansion under different "
             "assumptions - the attribution problem in miniature."),
   "assumptions": {"warming_C": 0.5, "ventilation_decline": 0.2, "oxygen_uM": 150.0, "years": 50.0},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    solubility_loss = A[\"oxygen_uM\"] * 0.02 * A[\"warming_C\"]\n"
     "    vent_loss = A[\"oxygen_uM\"] * A[\"ventilation_decline\"] * 0.5\n"
     "    total_loss = solubility_loss + vent_loss\n"
     "    return {\"solubility_loss_uM\": solubility_loss, \"ventilation_loss_uM\": vent_loss,\n"
     "            \"total_loss_uM\": total_loss, \"solubility_share\": solubility_loss / total_loss}\n"),
   "steps": [("Oxygen loss from solubility", "solubility_loss_uM", "uM"),
             ("Oxygen loss from ventilation decline", "ventilation_loss_uM", "uM"),
             ("Total oxygen loss", "total_loss_uM", "uM"),
             ("Solubility share of loss", "solubility_share", "")],
   "confirm": ["Partitioned budgets sum to observed trends across basins.",
               "Models reproduce each component and pass projection tests.",
               "The N2O feedback is measured at expanding edges."],
   "refute": ["The respiration residual dominates irreproducibly.",
              "Sensor drift corrupts the long records the attribution needs."],
   "checks": [("total_loss_uM", 5.0, 40.0), ("solubility_share", 0.05, 0.6)],
   "honesty": ("The 2-percent-per-degree solubility rule and the ventilation scaling are simplifications - "
               "real OMZs are shaped by currents this sketch ignores. It shows the attribution logic only."),
 }},
# ---------------------------------------------------------------- 18
{
 "key": "abyssal-mixing-recipes",
 "name": "What Mixes the Deep Ocean?",
 "group": "Deep Ocean",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": ("Walter Munk famous 1966 abyssal recipes calculated that the deep ocean must be mixed far more "
             "vigorously than measurements showed - the missing mixing problem - and six decades later the "
             "geography of that mixing is still being filled in."),
 "background": ("Munk 1966 balanced deep upwelling against downward diffusion and found the abyss requires a "
             "diffusivity around 10^-4 square meters per second - ten times what microstructure profilers "
             "typically measure in the open ocean. The resolution came in pieces: internal tides breaking "
             "over rough topography, boundary mixing along continental slopes and mid-ocean ridges, and "
             "turbulence in narrow passages like the Romanche Fracture Zone, where Polzin and others measured "
             "mixing hundreds of times the background. Yet the global integral remains an assembly of "
             "extrapolations: direct measurements cover a minute fraction of the seafloor, the Southern "
             "Ocean contribution is contested, and whether the canonical Munk number even applies uniformly "
             "is debated - some argue the circulation is better described without it."),
 "why_it_matters": ("Abyssal mixing sets the deep stratification, the residence time of deep water, and the "
             "rate at which the ocean takes up heat and carbon - the slow heartbeat of the climate system. "
             "Climate models that misplace the mixing misplace the deep circulation and its response to "
             "warming. The missing-mixing problem is also a standing invitation: the largest turbulent "
             "cascade in the ocean is still only partially mapped."),
 "sig_pointer": ("The Signature system proposes a mixing census: systematic microstructure surveys "
             "stratified by topography - ridges, slopes, plains, passages - until the global integral is "
             "measured rather than extrapolated. See the Signature Edition record for the full labeled "
             "proposal."),
 "sig_lens": ("Signature lens: the Signature system treats abyssal mixing as a census problem - sample every "
             "topographic class, weight by area, and sum the planet."),
 "signature_solution": (
     "Proposed approach. Step 1: design the stratified survey - microstructure sections across each "
     "topographic class in every basin, with enough repeats to capture the intermittency that dominates "
     "turbulence statistics. Step 2: measure the energy sources in parallel - internal-tide fluxes from "
     "moorings - so mixing is tied to its driver, not just described. Step 3: integrate by class and area "
     "to produce the first measured global mixing budget, with uncertainties propagated honestly. Step 4: "
     "confront the theories - uniform Munk mixing versus boundary-concentrated mixing - with the measured "
     "geography, and update model parameterizations to the winner.\n"
     "Assumptions: that topographic classes capture the mixing geography (largely true); that sparse "
     "sections represent their class (the intermittency gamble); that the survey can be funded as a "
     "coordinated program rather than scattered PI projects (organizationally hard).\n"
     "What would confirm it: the class-weighted integral matching the Munk requirement within uncertainties, "
     "with the geography pointing clearly to boundary versus interior dominance.\n"
     "What would kill it: the integral falling far short even after the full census - implying missing "
     "physics - or intermittency defeating every attempt at representative sampling.\n"
     "What this does NOT claim: it does not claim Munk number is universal; it does not settle the "
     "Southern Ocean role alone; it is not established physical oceanography."),
 "citations": [
     "Munk W H. Abyssal recipes. Deep Sea Res; 1966.",
     "Polzin K L et al. Spatial variability of turbulent mixing in the abyssal ocean. Science; 1997.",
     "Ledwell J R et al. Evidence for enhanced mixing over rough topography. Nature; 2000."],
 "explorer": {
   "blurb": ("A Munk-balance sketch: it computes the upwelling rate implied by a given diffusivity over the "
             "abyssal depth scale, and shows how the required mixing - the famous 10^-4 - emerges from the "
             "advective-diffusive balance."),
   "assumptions": {"kappa": 1e-4, "depth_scale_m": 1000.0, "area_Mkm2": 300.0},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    w = A[\"kappa\"] / A[\"depth_scale_m\"]\n"
     "    w_Sv = w * A[\"area_Mkm2\"] * 1e12 / 1e6\n"
     "    w_m_per_yr = w * 86400.0 * 365.0\n"
     "    return {\"upwelling_m_per_s\": w, \"upwelling_Sv\": w_Sv,\n"
     "            \"upwelling_m_per_yr\": w_m_per_yr, \"kappa_cm2_per_s\": A[\"kappa\"] * 1e4}\n"),
   "steps": [("Implied upwelling velocity", "upwelling_m_per_s", "m/s"),
             ("Implied deep upwelling transport", "upwelling_Sv", "Sv"),
             ("Upwelling per year", "upwelling_m_per_yr", "m/yr"),
             ("Diffusivity", "kappa_cm2_per_s", "cm2/s")],
   "confirm": ["The class-weighted integral matches the Munk requirement within uncertainties.",
               "The geography clearly favors boundary or interior dominance.",
               "Models updated to the measured geography improve deep ventilation."],
   "refute": ["The integral falls far short after the full census - missing physics.",
              "Intermittency defeats representative sampling entirely."],
   "checks": [("upwelling_Sv", 10.0, 60.0), ("upwelling_m_per_yr", 1.0, 8.0)],
   "honesty": ("The one-dimensional balance is Munk own simplification - real upwelling is concentrated at "
               "boundaries. The sketch shows where the famous number comes from, nothing more."),
 }},
# ---------------------------------------------------------------- 19
{
 "key": "antarctic-bottom-water",
 "name": "Is Antarctic Bottom Water Slowing Down?",
 "group": "Circulation",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": ("Antarctic Bottom Water - the densest water in the ocean, filling the abyss of every basin - "
             "has been freshening, warming, and contracting for decades, but whether its formation is "
             "slowing, and what that means for the deep circulation, is not settled."),
 "background": ("Purkey and Johnson showed in 2010-2013 from repeat hydrography that Antarctic Bottom Water "
             "is warming and its volume contracting - the abyssal ocean losing its coldest water. The "
             "formation regions are small and violent: winter polynyas off the Adélie Coast, in the Ross "
             "Sea, and the Weddell Sea, where sea ice formation rejects brine and the dense water cascades "
             "down the continental slope. Freshening from melting ice shelves and increased precipitation "
             "may be capping the density needed for formation, but direct measurements of the formation rate "
             "are sparse - a few moorings at the slope - and models disagree on whether the system is "
             "weakening gradually or approaching a threshold."),
 "why_it_matters": ("Antarctic Bottom Water ventilates the deepest ocean, carrying oxygen and storing carbon "
             "and heat on millennial timescales. A slowdown would stagnate the abyss - deoxygenation, "
             "reduced carbon storage, and a fundamental reorganization of the deep circulation. It is the "
             "Southern Hemisphere counterpart to the much-debated Atlantic overturning, observed far less "
             "and understood far worse."),
 "sig_pointer": ("The Signature system proposes a formation watch: sustained moorings at the key sills and "
             "polynyas plus tracer budgets, turning AABW formation from an inferred quantity into a measured "
             "time series. See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats bottom-water formation as a quantity to be "
             "measured at the source - moor the sills, watch the polynyas, and stop inferring."),
 "signature_solution": (
     "Proposed approach. Step 1: instrument the formation choke points - moored arrays across the Adélie "
     "and Ross sills and in the Weddell outflow - measuring dense-water transport continuously rather than "
     "in ship snapshots. Step 2: close the polynya salt budget with satellite ice-production estimates and "
     "ocean profiles, testing whether freshening is actually capping formation. Step 3: run tracer "
     "inventories (CFCs, SF6) to date the abyssal ventilation independently of the moorings. Step 4: "
     "confront models with the measured formation time series - models must reproduce the trend before "
     "their projections of abyssal stagnation are trusted.\n"
     "Assumptions: that a handful of sills capture most of the formation (largely true but incomplete); "
     "that moorings survive iceberg country (historically the operational risk); that tracer ages resolve "
     "decadal formation changes (marginally).\n"
     "What would confirm it: moored transports and tracer ages agreeing on a formation trend, with the "
     "polynya salt budget explaining it mechanistically.\n"
     "What would kill it: moorings showing stable formation while the abyss keeps warming - implying the "
     "signal is redistribution, not slowdown - or icebergs repeatedly destroying the arrays.\n"
     "What this does NOT claim: it does not claim a collapse threshold exists; it does not duplicate the "
     "Atlantic overturning debate; it is not established physical oceanography."),
 "citations": [
     "Purkey S G, Johnson G C. Warming of global abyssal and deep Southern Ocean waters. J Clim; 2010.",
     "Purkey S G, Johnson G C. Antarctic Bottom Water warming and freshening. J Clim; 2013.",
     "Rintoul S R. Rapid freshening of Antarctic Bottom Water. Nature; 2007."],
 "explorer": {
   "blurb": ("A bottom-water budget sketch: it declines dense-water formation with freshening, propagates "
             "the change into abyssal volume and ventilation age, and shows how a formation slowdown "
             "translates into abyssal warming."),
   "assumptions": {"formation_Sv": 8.0, "freshening": 0.3, "abyssal_volume_Mkm3": 250.0},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    formation = A[\"formation_Sv\"] * (1.0 - A[\"freshening\"] * 0.5)\n"
     "    vol_m3 = A[\"abyssal_volume_Mkm3\"] * 1e15\n"
     "    residence_yr = vol_m3 / (formation * 1e6) / (86400.0 * 365.0)\n"
     "    warming = A[\"freshening\"] * 0.4\n"
     "    return {\"formation_Sv\": formation, \"slowdown_frac\": 1.0 - formation / A[\"formation_Sv\"],\n"
     "            \"residence_years\": residence_yr, \"abyssal_warming_signal\": warming}\n"),
   "steps": [("Dense-water formation rate", "formation_Sv", "Sv"),
             ("Fractional slowdown", "slowdown_frac", ""),
             ("Abyssal residence time", "residence_years", "yr"),
             ("Abyssal warming signal", "abyssal_warming_signal", "C")],
   "confirm": ["Moored transports and tracer ages agree on a formation trend.",
               "The polynya salt budget explains the trend mechanistically.",
               "Models reproduce the measured series before projecting."],
   "refute": ["Moorings show stable formation while the abyss warms - redistribution, not slowdown.",
              "Icebergs make sustained sill measurements impossible."],
   "checks": [("formation_Sv", 5.0, 9.0), ("residence_years", 500.0, 1500.0)],
   "honesty": ("A single-box abyss with one formation number is a cartoon - real ventilation has pathways "
               "and ages. The sketch shows the slowdown logic that the moorings must test."),
 }},
# ---------------------------------------------------------------- 20
{
 "key": "decadal-ocean-memory",
 "name": "How Does the Ocean Remember a Decade?",
 "group": "Carbon and Climate",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": ("The ocean carries the memory that makes decadal climate prediction possible - heat buried in "
             "one decade resurfacing in the next - but which memory mechanisms actually operate, in the "
             "Atlantic multidecadal variability and the Pacific decadal oscillation, is fiercely debated."),
 "background": ("Hasselmann 1976 gave the null hypothesis: the ocean integrates weather noise into red, "
             "decadal variability with no dynamics at all. Against it stand dynamical theories - the Atlantic "
             "Multidecadal Variability as an overturning oscillation (Delworth, Zhang), the Pacific Decadal "
             "Oscillation as gyre and Kuroshio dynamics or just noise (Newman), and the Interdecadal Pacific "
             "Oscillation spanning basins. The practical stakes are decadal prediction systems, initialized "
             "with ocean observations, which show real but modest skill - yet skill without agreed mechanism "
             "is fragile, and recent work argues much Atlantic multidecadal variability is externally forced "
             "by aerosols and volcanoes rather than internal ocean memory at all."),
 "why_it_matters": ("Decadal prediction is the timescale of infrastructure, water planning, and fisheries "
             "management - the decisions a mayor or a minister actually makes. If the ocean memory is "
             "dynamical and predictable, skill can be built; if it is noise plus forcing, the enterprise "
             "needs redesigning. The debate also decides how much of observed multidecadal change is "
             "human-caused versus natural - the attribution question underlying every regional climate "
             "projection."),
 "sig_pointer": ("The Signature system proposes mechanism-separating prediction experiments: initialized "
             "forecasts with each hypothesized memory process switched off, scored against the real "
             "initialized record. See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats ocean memory as competing hypotheses to be "
             "switched off one at a time inside the prediction system itself."),
 "signature_solution": (
     "Proposed approach. Step 1: run the initialized decadal prediction system in mechanism-denial mode - "
     "suppress overturning variability, suppress gyre memory, suppress aerosol forcing - one at a time, "
     "measuring which denial destroys the observed skill. Step 2: confront each mechanism with its "
     "independent observable: overturning arrays for the AMV-overturning theory, subsurface heat content "
     "for gyre memory, forcing reconstructions for the external account. Step 3: publish the skill "
     "attribution openly, so the prediction enterprise knows which memory it is actually exploiting. "
     "Step 4: redesign initialization around the winning mechanisms - observe what matters, stop "
     "over-investing in what does not.\n"
     "Assumptions: that models can cleanly suppress one mechanism without breaking others (partially true); "
     "that the short initialized record is enough to score denials (the binding statistical weakness); "
     "that mechanisms are separable rather than entangled (may fail).\n"
     "What would confirm it: one denial experiment consistently destroying skill across systems, with the "
     "independent observable corroborating the mechanism.\n"
     "What would kill it: all denials leaving skill intact - implying the skill comes from forcing or "
     "initialization shock, not ocean memory - or skill itself proving illusory.\n"
     "What this does NOT claim: it does not claim decadal prediction is solved; it does not take sides in "
     "the AMV debate a priori; it is not established climate science."),
 "citations": [
     "Hasselmann K. Stochastic climate models. Tellus; 1976.",
     "Zhang R et al. Impact of Atlantic multidecadal variability. Rev Geophys; 2019.",
     "Yeager S G et al. Predicting near-term changes in the Earth system. Bull Amer Meteor Soc; 2018."],
 "explorer": {
   "blurb": ("A Hasselmann memory sketch: it integrates white weather noise through an ocean with a given "
             "damping time, and shows how the decorrelation time - the memory - emerges, plus how much "
             "decadal variance that memory explains."),
   "assumptions": {"damping_years": 8.0, "noise": 1.0, "years": 100.0},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    tau = A[\"damping_years\"]\n"
     "    var = A[\"noise\"] ** 2 * tau / 2.0\n"
     "    memory_10yr = math.exp(-10.0 / tau)\n"
     "    return {\"ocean_variance\": var, \"memory_after_10yr\": memory_10yr,\n"
     "            \"decorrelation_years\": tau, \"decadal_signal\": math.sqrt(var) * memory_10yr}\n"),
   "steps": [("Ocean temperature variance", "ocean_variance", ""),
             ("Memory remaining after 10 years", "memory_after_10yr", ""),
             ("Decorrelation timescale", "decorrelation_years", "yr"),
             ("Decadal signal amplitude", "decadal_signal", "")],
   "confirm": ["One denial experiment consistently destroys skill across systems.",
               "Independent observables corroborate the winning mechanism.",
               "Initialization redesign measurably improves skill."],
   "refute": ["All denials leave skill intact - the memory is not what was thought.",
              "Skill proves to be initialization shock, not ocean physics."],
   "checks": [("memory_after_10yr", 0.1, 0.6), ("decorrelation_years", 3.0, 20.0)],
   "honesty": ("Red noise is the null hypothesis, not an explanation - it produces decadal wiggles with "
               "zero dynamics. The sketch shows what memory looks like; the denial experiments must show "
               "what it is."),
 }},
# ---------------------------------------------------------------- 21
{
 "key": "submarine-groundwater",
 "name": "How Much Fresh Water Leaks Into the Ocean From Below?",
 "group": "Ice and Coasts",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": ("Submarine groundwater discharge - fresh and brackish water seeping from coastal aquifers into "
             "the sea - may rival rivers in delivering nutrients and carbon to the coastal ocean, yet its "
             "global volume is uncertain by an order of magnitude."),
 "background": ("Moore showed in the 1990s-2000s, using radium isotopes as tracers, that groundwater "
             "discharge to the Atlantic could approach river fluxes in some regions - a hidden hydrological "
             "cycle invisible to river gauges. The discharge carries nutrients, carbon, metals, and "
             "pollutants from land, fueling coastal productivity and, in places, harmful algal blooms. But "
             "measuring it is brutally hard: seepage meters sample square meters, tracers integrate "
             "kilometers with model-dependent assumptions, and the global extrapolation rests on a few dozen "
             "studied coastlines. Climate change - sea-level rise pushing saltwater into aquifers, changing "
             "recharge - is altering the flux while it remains unmeasured."),
 "why_it_matters": ("Coastal water quality, algal blooms, and nearshore fisheries all depend on nutrient "
             "inputs, and groundwater may be the largest unbudgeted term. Contaminants - nitrates, PFAS, "
             "wastewater - ride the same hidden pathway to the sea. Without the global number, coastal "
             "management plans and ocean nutrient budgets are built on an incomplete ledger."),
 "sig_pointer": ("The Signature system proposes a coastline census: standardized radium-tracer and seepage "
             "surveys stratified by geology, scaled with a global aquifer model, until the hidden flux is "
             "budgeted. See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats groundwater discharge as a hidden-river census - "
             "survey every coastline type, then scale with geology, not hope."),
 "signature_solution": (
     "Proposed approach. Step 1: run standardized discharge surveys - radium and radon tracers plus seepage "
     "meters - across a stratified sample of coastlines: karst, volcanic, deltaic, fractured rock, permafrost. "
     "Step 2: build the scaling model from coastal geology, recharge, and topography, calibrated on the "
     "surveyed strata. Step 3: validate the global extrapolation against independent constraints - ocean "
     "radium budgets and coastal nutrient anomalies the discharge must explain. Step 4: monitor sentinel "
     "coastlines for the climate-driven change - saltwater intrusion and recharge shifts - so the flux "
     "becomes a watched variable, not a one-time estimate.\n"
     "Assumptions: that coastline strata capture the discharge variability (reasonable); that tracers "
     "integrate discharge faithfully (model-dependent); that the scaling model transfers to unsurveyed "
     "coasts (the extrapolation gamble).\n"
     "What would confirm it: independent radium budgets and nutrient anomalies agreeing with the scaled "
     "global flux within a factor of two.\n"
     "What would kill it: tracer and seepage methods disagreeing irreconcilably, or the flux proving so "
     "locally variable that no stratification tames it.\n"
     "What this does NOT claim: it does not claim groundwater exceeds rivers globally; it does not map "
     "pollution sources; it is not established hydrology."),
 "citations": [
     "Moore W S. Large groundwater inputs to coastal waters. Nature; 1996.",
     "Moore W S. The effect of submarine groundwater discharge on the ocean. Ann Rev Mar Sci; 2010.",
     "Burnett W C et al. Quantifying submarine groundwater discharge. Biogeochemistry; 2006."],
 "explorer": {
   "blurb": ("A Darcy-flux sketch: it estimates groundwater discharge from aquifer permeability, hydraulic "
             "gradient, and coastline length, and compares the hidden flux to the river discharge it may "
             "rival."),
   "assumptions": {"permeability_m2": 1e-10, "gradient": 0.01, "aquifer_m": 50.0, "coast_km": 1000.0,
                   "river_Sv": 0.001},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    q = A[\"permeability_m2\"] * 1000.0 * 9.81 / 0.001 * A[\"gradient\"]\n"
     "    discharge = q * A[\"aquifer_m\"] * A[\"coast_km\"] * 1000.0\n"
     "    return {\"darcy_velocity_m_per_s\": q, \"discharge_m3_per_s\": discharge,\n"
     "            \"discharge_Sv\": discharge / 1e6, \"vs_river\": discharge / 1e6 / A[\"river_Sv\"]}\n"),
   "steps": [("Darcy velocity", "darcy_velocity_m_per_s", "m/s"),
             ("Groundwater discharge", "discharge_m3_per_s", "m3/s"),
             ("Discharge in Sverdrups", "discharge_Sv", "Sv"),
             ("Ratio to river discharge", "vs_river", "x")],
   "confirm": ["Radium budgets and nutrient anomalies agree with the scaled flux.",
               "Stratified surveys converge on stable per-type discharge rates.",
               "Sentinel coasts show the expected climate-driven changes."],
   "refute": ["Tracer and seepage methods disagree irreconcilably.",
              "Local variability defeats every stratification scheme."],
   "checks": [("discharge_Sv", 0.0001, 0.05), ("vs_river", 0.05, 5.0)],
   "honesty": ("Darcy law with one permeability is a cartoon of real aquifers - fractured rock laughs at "
               "it. The sketch shows the scaling logic; the tracers must supply the truth."),
 }},
# ---------------------------------------------------------------- 22
{
 "key": "hadal-trench-life",
 "name": "What Lives in the Deepest Ocean Trenches?",
 "group": "Deep Ocean",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": ("Hadal trenches - deeper than 6000 meters - hold nearly half the ocean depth range in a tiny "
             "fraction of its area, and their ecosystems, connectivity, and role in carbon burial are "
             "barely explored."),
 "background": ("Jamieson and colleagues have shown over the past two decades that trenches are not the "
             "azoic deserts once imagined: snailfish thrive below 8000 meters, amphipods swarm in the "
             "thousands, and microbial communities adapt to crushing pressure. Yet only a handful of the "
             "27 hadal trenches have been biologically surveyed, the connectivity between them - stepping "
             "stones or isolated islands - is unknown, and the trench role as carbon traps, funneling "
             "surface production down their steep walls, is inferred from a few sediment cores. Pressure "
             "adaptation itself is partly mysterious: piezolytes like trimethylamine oxide stabilize "
             "proteins, but the depth limit of fish - around 8400 meters, with no fish below - hints at a "
             "biochemical wall no one fully understands."),
 "why_it_matters": ("Trenches are the least-explored ecosystems on Earth and the final sink for much of "
             "what the ocean buries - including pollutants and microplastics, which Jamieson found even in "
             "Mariana amphipods. Their isolation makes them natural laboratories for evolution under "
             "extremes, and their carbon burial may matter globally. We are contemplating exploiting the "
             "deep sea while its deepest habitats remain essentially unsurveyed."),
 "sig_pointer": ("The Signature system proposes a trench transect program: standardized lander surveys down "
             "the axis of every major trench, with connectivity genetics and carbon-burial measurements "
             "built in. See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats trenches as an archipelago to be surveyed "
             "systematically - same landers, same protocols, every trench, until the deep map is filled."),
 "signature_solution": (
     "Proposed approach. Step 1: deploy standardized baited-lander and imaging transects down the axis of "
     "each major trench, from rim to hadal floor, with identical protocols so trenches can be compared. "
     "Step 2: sequence the inhabitants for connectivity - are trench populations isolated endemics or a "
     "connected hadal network. Step 3: measure carbon burial directly with sediment traps and cores along "
     "the axis, testing the trench-as-carbon-trap hypothesis quantitatively. Step 4: probe the fish depth "
     "limit with comparative biochemistry of the deepest snailfish versus their shallower relatives, "
     "attacking the 8400-meter wall mechanistically.\n"
     "Assumptions: that landers sample representatively despite bait bias (known limitation); that a "
     "global trench program can be coordinated and funded (ambitious); that the fish limit is biochemical "
     "rather than ecological (the hypothesis under test).\n"
     "What would confirm it: comparable surveys revealing the rules - which trenches are rich, which "
     "isolated, how much carbon they bury - and biochemistry explaining the fish limit.\n"
     "What would kill it: bait bias proving to dominate every comparison, or the program stalling after "
     "two trenches for lack of ships and funding.\n"
     "What this does NOT claim: it does not claim trenches are pristine (pollutants reach them); it does "
     "not promise new species of any utility; it is not established deep-sea biology."),
 "citations": [
     "Jamieson A J. The Hadal Zone: Life in the Deepest Oceans. Cambridge Univ Press; 2015.",
     "Jamieson A J et al. Bioaccumulation of persistent organic pollutants in the deepest ocean. Nat Ecol Evol; 2017.",
     "Yancey P H et al. Unusual organic osmolytes in deep-sea animals. J Exp Zool; 2002."],
 "explorer": {
   "blurb": ("A trench-pressure sketch: it computes hydrostatic pressure down to Challenger Deep, estimates "
             "the piezolyte concentration needed to stabilize proteins, and shows where the biochemical "
             "cost may wall off fish."),
   "assumptions": {"depth_m": 10900.0, "fish_limit_m": 8400.0, "tmao_rate": 0.035},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    pressure_MPa = 1025.0 * 9.81 * A[\"depth_m\"] / 1e6\n"
     "    tmao_needed = A[\"tmao_rate\"] * A[\"depth_m\"] / 1000.0\n"
     "    limit_pressure = 1025.0 * 9.81 * A[\"fish_limit_m\"] / 1e6\n"
     "    return {\"pressure_MPa\": pressure_MPa, \"pressure_atm\": pressure_MPa * 9.87,\n"
     "            \"tmao_mmol_per_kg\": tmao_needed * 1000.0, \"fish_limit_pressure_MPa\": limit_pressure}\n"),
   "steps": [("Pressure at trench floor", "pressure_MPa", "MPa"),
             ("Pressure in atmospheres", "pressure_atm", "atm"),
             ("Piezolyte needed for proteins", "tmao_mmol_per_kg", "mmol/kg"),
             ("Pressure at the fish limit", "fish_limit_pressure_MPa", "MPa")],
   "confirm": ["Standardized surveys reveal comparable rules across trenches.",
               "Connectivity genetics map the hadal network.",
               "Biochemistry explains the 8400-meter fish wall."],
   "refute": ["Bait bias dominates every comparison; no rules emerge.",
              "The program stalls for lack of ships after two trenches."],
   "checks": [("pressure_MPa", 90.0, 120.0), ("fish_limit_pressure_MPa", 70.0, 95.0)],
   "honesty": ("The piezolyte scaling is a rough empirical trend, not a law - and pressure is only one of "
               "the trench stresses. The sketch quantifies the extreme; the landers must map the life."),
 }},
# ---------------------------------------------------------------- 23
{
 "key": "ice-shelf-melt-coupling",
 "name": "How Fast Will the Ocean Melt the Ice Shelves From Below?",
 "group": "Ice and Coasts",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": ("Warm ocean water is melting Antarctic ice shelves from below, unbuttressing the glaciers "
             "behind them - but melt rates under the shelves are measured in a few places, modeled crudely "
             "everywhere, and the difference decides meters of sea level."),
 "background": ("Ice shelves float, but they hold back the grounded ice streams behind them; when shelves "
             "thin from below, glaciers accelerate - the dynamic behind the Amundsen Sea collapse observed "
             "since the 1990s. Warm Circumpolar Deep Water intrudes onto the continental shelf through "
             "troughs, reaching cavity openings at temperatures degrees above freezing - enormous heat by "
             "polar standards. Direct observations under shelves are rare: a handful of boreholes, "
             "autonomous submersibles like Boaty McBoatface, and seal-tag profiles. Models parameterize "
             "basal melt with simple functions of ocean temperature, but the cavity circulation - tides, "
             "topography, the ice pump - makes melt rates vary by orders of magnitude over kilometers, "
             "and Thwaites Glacier future hinges on getting this right."),
 "why_it_matters": ("The West Antarctic Ice Sheet holds over 3 meters of sea-level equivalent, and its "
             "fate is largely an ocean problem: warm water at the grounding line. Sea-level projections for "
             "2100 differ by a meter largely because of ice-shelf melt uncertainty. Coastal planning for "
             "centuries is being written now, from physics measured in a handful of boreholes."),
 "sig_pointer": ("The Signature system proposes a cavity watch: sustained ocean observations at the "
             "grounding zones of the critical glaciers, with melt parameterizations tested against measured "
             "melt, not tuned to it. See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats ice-shelf melt as a boundary layer to be "
             "measured - instrument the cavities, test the formulas, and stop tuning."),
 "signature_solution": (
     "Proposed approach. Step 1: maintain continuous ocean observations at the cavity openings and "
     "grounding zones of Thwaites, Pine Island, and the Totten - moorings, seal tags, and autonomous "
     "submersibles, year-round. Step 2: measure basal melt directly where possible - borehole phase-"
     "sensitive radar and ApRES - so parameterizations are tested against data rather than tuned to "
     "match ice-sheet behavior. Step 3: run cavity-resolving ocean models for the critical shelves, "
     "validating the circulation against the moorings before trusting melt projections. Step 4: carry "
     "only validated melt laws into ice-sheet models, with the uncertainty propagated into sea-level "
     "projections honestly.\n"
     "Assumptions: that instruments survive under ice shelves for years (improving); that a few "
     "calibration sites represent their regions (risky given kilometer-scale variability); that "
     "validated laws transfer to unmeasured shelves (the extrapolation step).\n"
     "What would confirm it: measured melt matching cavity-model predictions at multiple sites, and "
     "ice-sheet models with validated laws reproducing observed glacier acceleration.\n"
     "What would kill it: melt proving dominated by sub-kilometer processes no observing system or "
     "model can resolve, leaving projections irreducibly uncertain.\n"
     "What this does NOT claim: it does not set the date of any collapse; it does not claim all "
     "shelves behave like Thwaites; it is not established glaciology."),
 "citations": [
     "Rignot E et al. Ice-shelf melting around Antarctica. Science; 2013.",
     "Jenkins A et al. West Antarctic Ice Sheet retreat driven by ocean. Nat Geosci; 2018.",
     "Holland P R et al. Oceanic and atmospheric forcing of Larsen C. Geophys Res Lett; 2015."],
 "explorer": {
   "blurb": ("A basal-melt sketch: it applies the standard thermal-forcing melt law to warm water intruding "
             "under an ice shelf, and shows how melt - and the resulting sea-level commitment - scales with "
             "ocean temperature above freezing."),
   "assumptions": {"ocean_temp_C": 1.0, "freezing_C": -2.0, "gamma": 8.0, "shelf_area_Mkm2": 0.5},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    dT = A[\"ocean_temp_C\"] - A[\"freezing_C\"]\n"
     "    melt = A[\"gamma\"] * dT\n"
     "    mass_Gt = melt * A[\"shelf_area_Mkm2\"] * 1e12 / 1e3 * 0.917\n"
     "    return {\"thermal_forcing_C\": dT, \"melt_rate_m_per_yr\": melt,\n"
     "            \"mass_loss_Gt_per_yr\": mass_Gt, \"doubling_per_C\": 2.0 ** 1.0}\n"),
   "steps": [("Ocean thermal forcing", "thermal_forcing_C", "C"),
             ("Basal melt rate", "melt_rate_m_per_yr", "m/yr"),
             ("Shelf mass loss", "mass_loss_Gt_per_yr", "Gt/yr"),
             ("Melt doubling per degree", "doubling_per_C", "x")],
   "confirm": ["Measured melt matches cavity-model predictions at multiple sites.",
               "Validated melt laws let ice-sheet models reproduce observed acceleration.",
               "Projections carry honest, propagated uncertainty."],
   "refute": ["Melt proves sub-kilometer dominated and unresolvable.",
              "Instruments cannot survive the cavities long enough to calibrate."],
   "checks": [("melt_rate_m_per_yr", 1.0, 30.0), ("thermal_forcing_C", 1.0, 6.0)],
   "honesty": ("Gamma is the whole parameterization compressed into one tunable number - this sketch uses "
               "it, the science must earn it. Real cavities have tides, topography, and plumes this "
               "ignores."),
 }},
# ---------------------------------------------------------------- 24
{
 "key": "viral-shunt-carbon",
 "name": "Do Ocean Viruses Control the Carbon Cycle?",
 "group": "Microbes and Viruses",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": ("Ocean viruses kill an estimated 20 percent of marine biomass every day, shunting carbon away "
             "from grazers into dissolved matter - the viral shunt - but whether this planetary-scale lysis "
             "strengthens or weakens carbon sequestration is unresolved."),
 "background": ("Suttle 2007 established viruses as the ocean most numerous biological entities - ten "
             "million per milliliter - and the agents of massive daily mortality. Wilhelm and Suttle "
             "formalized the viral shunt: lysis converts particulate carbon that grazers would package "
             "into sinking fecal pellets into dissolved organic matter that microbes mostly respire near "
             "the surface. The logic suggests viruses weaken the biological pump - but the shunt also "
             "releases nutrients that fuel new production, and some argue viral lysis aggregates particles "
             "and enhances sinking. The net sign of viral activity on carbon export, and how it responds "
             "to warming and acidification, rests on models with barely any field validation."),
 "why_it_matters": ("If viruses are the master switch of the carbon pump, then the largest carbon flux in "
             "the ocean is controlled by entities barely included in climate models. Viral ecology would "
             "move from curiosity to a first-order climate variable - and viral responses to ocean change "
             "would become a feedback to quantify, not a footnote to ignore."),
 "sig_pointer": ("The Signature system proposes a shunt-measurement campaign: simultaneous lysis rates, "
             "particle export, and DOM production on process cruises, closing the viral carbon budget "
             "observationally. See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the viral shunt as a budget to be closed - "
             "measure lysis, export, and respiration together until the sign of the viral effect is data."),
 "signature_solution": (
     "Proposed approach. Step 1: run process cruises measuring the full viral loop in the same water - "
     "viral production and lysis rates, grazer packaging, particle export by traps, DOM release and "
     "respiration - so the shunt is budgeted, not inferred. Step 2: manipulate viral pressure "
     "experimentally in mesocosms across biomes, watching export respond - the causal test the field "
     "lacks. Step 3: track viral community and lysis across warming and acidification gradients, "
     "parameterizing the climate response from observation. Step 4: encode the validated shunt into "
     "ecosystem models as a dynamic process, and test whether it changes projected carbon export.\n"
     "Assumptions: that lysis rates can be measured representatively (method-dependent); that mesocosm "
     "manipulations scale to the ocean (the perennial enclosure question); that viral effects are "
     "separable from the bacterial processes they drive (partially true).\n"
     "What would confirm it: closed viral carbon budgets across biomes with a consistent sign, and "
     "models whose export projections shift when the shunt is included.\n"
     "What would kill it: budgets that refuse to close, or mesocosms showing export insensitive to "
     "viral pressure - the shunt real but climatically irrelevant.\n"
     "What this does NOT claim: it does not claim viruses can be managed for carbon; it does not fix "
     "the 20-percent number; it is not established marine microbiology."),
 "citations": [
     "Suttle C A. Marine viruses - major players in the global ecosystem. Nat Rev Microbiol; 2007.",
     "Wilhelm S W, Suttle C A. Viruses and nutrient cycles in the sea. Bioscience; 1999.",
     "Fuhrman J A. Marine viruses and their biogeochemical and ecological effects. Nature; 1999."],
 "explorer": {
   "blurb": ("A viral-shunt budget: it partitions primary production among grazing, viral lysis, and "
             "respiration, routes the lysed carbon through the microbial loop, and computes how the pump "
             "efficiency shifts as viral pressure changes."),
   "assumptions": {"production": 50.0, "lysis_frac": 0.2, "grazing_frac": 0.4, "loop_efficiency": 0.3},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    lysed = A[\"production\"] * A[\"lysis_frac\"]\n"
     "    grazed = A[\"production\"] * A[\"grazing_frac\"]\n"
     "    looped = lysed * A[\"loop_efficiency\"]\n"
     "    export = grazed * 0.3 + looped * 0.1\n"
     "    pump_eff = export / A[\"production\"]\n"
     "    return {\"lysed_carbon\": lysed, \"export\": export, \"pump_efficiency\": pump_eff,\n"
     "            \"shunt_diversion\": lysed / (lysed + grazed)}\n"),
   "steps": [("Carbon lysed by viruses", "lysed_carbon", "units"),
             ("Carbon exported downward", "export", "units"),
             ("Biological pump efficiency", "pump_efficiency", ""),
             ("Shunt share of mortality", "shunt_diversion", "")],
   "confirm": ["Closed viral carbon budgets across biomes with a consistent sign.",
               "Export responds to viral manipulation in mesocosms.",
               "Models shift projections when the shunt is included."],
   "refute": ["Budgets refuse to close; export proves insensitive to viral pressure.",
              "The shunt is real but climatically irrelevant."],
   "checks": [("pump_efficiency", 0.05, 0.25), ("shunt_diversion", 0.2, 0.5)],
   "honesty": ("The routing fractions are placeholders for the measurements that do not yet exist - this "
               "sketch is the budget template, and the field campaign is the work."),
 }},
# ---------------------------------------------------------------- 25
{
 "key": "deep-water-return-path",
 "name": "How Does Deep Water Get Back to the Surface?",
 "group": "Circulation",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": ("Deep water sinks in the North Atlantic and around Antarctica - but the return journey, the "
             "upwelling that closes the global overturning circulation, is split between competing theories "
             "that imply very different oceans."),
 "background": ("The textbook conveyor shows deep water rising diffusively everywhere, per Munk abyssal "
             "recipes - but Toggweiler and Samuels argued in the 1990s that Southern Ocean winds do the "
             "lifting, pulling deep water up along sloping density surfaces, with eddies partly "
             "compensating. Marshall and Speer formalized the residual circulation: what matters is the "
             "sum of wind-driven and eddy-driven transports. Observations support both stories in part: "
             "Southern Ocean upwelling is real and wind-sensitive, yet abyssal mixing maps show intense "
             "boundary upwelling too. The split matters because the two closures respond differently to "
             "changing winds and stratification - one predicts a circulation slave to the westerlies, the "
             "other a circulation paced by interior mixing."),
 "why_it_matters": ("The return path sets the timescale of the whole overturning - centuries or millennia - "
             "and therefore how fast the deep ocean takes up heat and carbon, and how fast it would release "
             "them. It decides whether the circulation has a wind-driven vulnerability to shifting storm "
             "tracks or a mixing-driven inertia. Every long-term climate projection carries one of these "
             "closures implicitly; none has been proven."),
 "sig_pointer": ("The Signature system proposes a closure discrimination experiment: measure the residual "
             "upwelling directly with tracer budgets and eddy-resolving observations, and require models to "
             "reproduce the measured split. See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the return path as a fork to be resolved - "
             "measure the residual upwelling and let the wind-versus-mixing split be data."),
 "signature_solution": (
     "Proposed approach. Step 1: measure the Southern Ocean residual circulation directly - combining "
     "moored transport arrays, float-derived eddy fluxes, and tracer budgets - to fix the wind-driven "
     "upwelling term observationally. Step 2: measure abyssal boundary upwelling with the mixing census "
     "from the companion program, fixing the diffusive term. Step 3: require ocean models to reproduce "
     "both terms simultaneously; models that get the total right with the wrong split are flagged, not "
     "trusted. Step 4: test the response - how each closure reacts to wind shifts in models - so the "
     "vulnerability question is answered per mechanism.\n"
     "Assumptions: that the residual circulation is measurable with current arrays (at the edge of "
     "feasible); that models can be diagnosed finely enough to expose the split (largely true); that "
     "the two closures are separable rather than one continuum (debatable).\n"
     "What would confirm it: observations fixing the wind-versus-mixing split within uncertainties, with "
     "models reproducing the split and its wind sensitivity.\n"
     "What would kill it: the split proving unmeasurable - eddy compensation defeating every observing "
     "strategy - or models reproducing observations with mutually exclusive closures.\n"
     "What this does NOT claim: it does not claim the conveyor metaphor is accurate; it does not predict "
     "circulation collapse; it is not established physical oceanography."),
 "citations": [
     "Toggweiler J R, Samuels B. Effect of Drake Passage on the global thermohaline circulation. Deep Sea Res; 1995.",
     "Marshall J, Speer K. Closure of the meridional overturning circulation. Nat Geosci; 2012.",
     "Lumpkin R, Speer K. Global ocean meridional overturning. J Phys Oceanogr; 2007."],
 "explorer": {
   "blurb": ("A residual-circulation sketch: it combines wind-driven upwelling with eddy compensation and "
             "diffusive upwelling, and shows how the total return flow - and its wind sensitivity - depends "
             "on which closure dominates."),
   "assumptions": {"wind_upwelling_Sv": 20.0, "eddy_compensation": 0.6, "diffusive_Sv": 10.0},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    residual = A[\"wind_upwelling_Sv\"] * (1.0 - A[\"eddy_compensation\"])\n"
     "    total = residual + A[\"diffusive_Sv\"]\n"
     "    wind_share = residual / total\n"
     "    sensitivity = wind_share * 1.0\n"
     "    return {\"residual_Sv\": residual, \"total_return_Sv\": total,\n"
     "            \"wind_share\": wind_share, \"wind_sensitivity\": sensitivity}\n"),
   "steps": [("Residual wind-driven upwelling", "residual_Sv", "Sv"),
             ("Total deep-water return", "total_return_Sv", "Sv"),
             ("Wind-driven share", "wind_share", ""),
             ("Sensitivity to wind shifts", "wind_sensitivity", "")],
   "confirm": ["Observations fix the wind-versus-mixing split within uncertainties.",
               "Models reproduce the split and its wind sensitivity.",
               "Tracer budgets corroborate the measured return."],
   "refute": ["Eddy compensation defeats every attempt to measure the residual.",
              "Models match observations with mutually exclusive closures."],
   "checks": [("total_return_Sv", 12.0, 28.0), ("wind_share", 0.2, 0.7)],
   "honesty": ("One compensation fraction stands in for the hardest measurement in physical oceanography. "
               "The sketch shows the fork; the arrays must walk it."),
 }},
# ---------------------------------------------------------------- 26
{
 "key": "southern-ocean-sink-future",
 "name": "Will the Southern Ocean Keep Absorbing Carbon?",
 "group": "Carbon and Climate",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": ("The Southern Ocean absorbs a disproportionate share of human CO2 - but its uptake stalled in "
             "the 1990s, reinvigorated in the 2000s, and theory says it must eventually saturate. Which "
             "future is real is the largest single uncertainty in the ocean carbon sink."),
 "background": ("Le Quere and colleagues reported in 2007 that the Southern Ocean sink had weakened, "
             "attributing it to intensifying westerly winds driving more carbon-rich deep water to the "
             "surface - the first observed saturation of an ocean sink. Landschutzer and colleagues then "
             "showed in 2015 that the sink had reinvigorated, likely from natural variability, reopening "
             "the question. Beneath the variability sits the inexorable chemistry: as the ocean absorbs "
             "CO2, the Revelle factor rises and each additional ton is taken up less efficiently - "
             "saturation written into the carbonate system. Models project the sink growing for decades "
             "then flattening, but the timing depends on winds, eddies, and biology that models resolve "
             "poorly, and the Southern Ocean remains the least-observed major basin."),
 "why_it_matters": ("The Southern Ocean takes up roughly 40 percent of the ocean anthropogenic CO2 despite "
             "covering far less area - it is the workhorse of the natural carbon sink buying time against "
             "emissions. If it saturates early, atmospheric CO2 rises faster than carbon budgets assume, "
             "and every net-zero timeline tightens. The sink future is the sink question."),
 "sig_pointer": ("The Signature system proposes a saturation watch: sustained Southern Ocean carbon "
             "observations - floats, ships, moorings - with the Revelle-driven decline separated from "
             "wind-driven variability in a published attribution. See the Signature Edition record for the "
             "full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the sink future as two signals to separate - "
             "the inevitable chemistry and the variable winds - measured until they disentangle."),
 "signature_solution": (
     "Proposed approach. Step 1: sustain and densify Southern Ocean carbon observations - "
     "biogeochemical floats with pH sensors, repeat hydrography, air-sea flux moorings - until the basin "
     "is no longer the least-observed. Step 2: publish the running attribution - Revelle-factor-driven "
     "efficiency decline versus wind-driven ventilation variability - updated annually, so saturation "
     "and variability are never again confused. Step 3: confront models with the attributed record; "
     "models must reproduce both the 1990s stall and the 2000s reinvigoration before their saturation "
     "timing is trusted. Step 4: carry only validated saturation curves into carbon budgets, with the "
     "uncertainty shown as a range, not a line.\n"
     "Assumptions: that float pH sensors achieve climate-quality accuracy (approaching true); that the "
     "attribution can separate chemistry from winds (largely, on decadal scales); that Southern Ocean "
     "logistics sustain the array (the perennial funding risk).\n"
     "What would confirm it: the attribution cleanly separating a steady chemical decline from "
     "wind-driven swings, with models reproducing both.\n"
     "What would kill it: variability proving to dominate so completely that the chemical trend is "
     "undetectable for decades - or the observing system collapsing in the harshest ocean.\n"
     "What this does NOT claim: it does not claim the sink will collapse; it does not set carbon-budget "
     "policy; it is not established carbon-cycle science."),
 "citations": [
     "Le Quere C et al. Saturation of the Southern Ocean CO2 sink. Science; 2007.",
     "Landschutzer P et al. The reinvigoration of the Southern Ocean carbon sink. Science; 2015.",
     "Gruber N et al. The oceanic sink for anthropogenic CO2. Science; 2019."],
 "explorer": {
   "blurb": ("A sink-saturation sketch: it grows the Revelle factor as dissolved carbon accumulates, "
             "declines the uptake efficiency accordingly, and layers wind-driven variability on top - "
             "showing the two signals the observing system must separate."),
   "assumptions": {"dic_increase": 50.0, "revelle_0": 10.0, "wind_variability": 0.3, "base_uptake_Pg": 1.0},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    revelle = A[\"revelle_0\"] * (1.0 + A[\"dic_increase\"] / 2000.0 * 0.5)\n"
     "    efficiency = A[\"revelle_0\"] / revelle\n"
     "    uptake = A[\"base_uptake_Pg\"] * efficiency\n"
     "    return {\"revelle_factor\": revelle, \"uptake_efficiency\": efficiency,\n"
     "            \"sink_Pg_per_yr\": uptake, \"wind_noise\": A[\"wind_variability\"] * uptake}\n"),
   "steps": [("Revelle factor", "revelle_factor", ""),
             ("Uptake efficiency vs preindustrial", "uptake_efficiency", ""),
             ("Southern Ocean sink", "sink_Pg_per_yr", "Pg/yr"),
             ("Wind-driven variability", "wind_noise", "Pg/yr")],
   "confirm": ["Attribution separates chemical decline from wind swings cleanly.",
               "Models reproduce both the stall and the reinvigoration.",
               "Validated saturation curves enter carbon budgets with ranges."],
   "refute": ["Variability dominates so completely the trend stays undetectable for decades.",
              "The observing array cannot be sustained in the Southern Ocean."],
   "checks": [("uptake_efficiency", 0.8, 1.0), ("sink_Pg_per_yr", 0.6, 1.4)],
   "honesty": ("The Revelle scaling is real chemistry but the wind noise is parameterized - the sketch "
               "shows exactly the separation problem the floats must solve."),
 }},
# ---------------------------------------------------------------- 27
{
 "key": "deep-sea-mining-recovery",
 "name": "How Long Would the Deep Seafloor Take to Recover From Mining?",
 "group": "Life and Ecosystems",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": ("Deep-sea mining for polymetallic nodules would strip abyssal habitat that took millions of "
             "years to form - and the only long-term disturbance experiment suggests recovery takes "
             "decades at minimum, centuries more likely, with no one able to say for sure."),
 "background": ("The 1989 DISCOL experiment ploughed the Peru Basin seafloor to simulate nodule mining; "
             "decades later, the tracks remain visible and the fauna has not recovered - the longest "
             "deep-sea recovery experiment ever run, and it says: not in a human lifetime. Nodules "
             "themselves grow millimeters per million years, so the habitat substrate is effectively "
             "non-renewable. The International Seabed Authority is writing exploitation regulations while "
             "the science of recovery rests on DISCOL, a few smaller experiments, and natural disturbance "
             "analogs - against industry timelines measured in years. Proponents argue mining footprints "
             "are small relative to the abyss; opponents note the nodule fields are the habitat, not "
             "interchangeable mud."),
 "why_it_matters": ("The decision to mine the deep sea is being made now, and recovery time is the central "
             "scientific input: decades versus millennia changes the moral and economic calculus "
             "completely. The metals - cobalt, nickel, copper - feed the energy transition, so the "
             "trade-off is real: green technology built on ecosystems that may not recover before "
             "civilizations fall."),
 "sig_pointer": ("The Signature system proposes a recovery-measurement program: long-term monitoring of "
             "all disturbance experiments with standardized recolonization metrics, plus nodule-regrowth "
             "physics, until recovery curves are data. See the Signature Edition record for the full "
             "labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats mining recovery as a measured curve, not a "
             "modeled hope - monitor every disturbance for decades and let the recolonization data speak."),
 "signature_solution": (
     "Proposed approach. Step 1: standardize long-term monitoring of DISCOL and all newer disturbance "
     "experiments with identical recolonization metrics - species, function, nodule-associated fauna - "
     "revisited on a fixed schedule for decades. Step 2: run new controlled disturbances across nodule "
     "provinces before commercial mining, so baselines exist where the machines will go. Step 3: measure "
     "the actual recolonization mechanisms - larval supply, growth rates, succession - because recovery "
     "time without mechanism is just curve-fitting. Step 4: publish the recovery curves with full "
     "uncertainty and require them in every environmental impact assessment, so no license is granted on "
     "assumed resilience.\n"
     "Assumptions: that monitoring survives funding cycles for decades (historically the failure point); "
     "that experimental disturbances represent commercial ones (scale differs hugely); that recolonization "
     "mechanisms are measurable in the abyss (technically demanding).\n"
     "What would confirm it: converging recovery curves across sites showing consistent timescales, with "
     "mechanisms explaining the rates.\n"
     "What would kill it: monitoring lapsing after a decade as usual, or commercial-scale disturbance "
     "proving qualitatively different from experiments - the curves not transferring.\n"
     "What this does NOT claim: it does not claim mining should or should not proceed; it does not value "
     "the metals against the ecosystems; it is not established deep-sea ecology."),
 "citations": [
     "Thiel H, Schriever G. DISCOL project: long-term large-scale disturbance experiment. Deep Sea Res; 1989.",
     "Jones D O B et al. Biological responses to disturbance from simulated deep-sea mining. Sci Adv; 2017.",
     "Van Dover C L. Mining seafloor massive sulphides. Mar Policy; 2011."],
 "explorer": {
   "blurb": ("A recolonization sketch: it grows disturbed seafloor fauna back logistically with the "
             "abyss slow growth rates, and shows how recovery time stretches from decades to millennia as "
             "the growth rate falls - the quantitative core of the mining debate."),
   "assumptions": {"growth_rate": 0.05, "carrying": 1.0, "disturbed_frac": 0.95, "years": 200.0},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    N0 = A[\"carrying\"] * (1.0 - A[\"disturbed_frac\"])\n"
     "    r = A[\"growth_rate\"]\n"
     "    t50 = math.log((A[\"carrying\"] - N0) / N0) / r\n"
     "    N200 = A[\"carrying\"] / (1.0 + (A[\"carrying\"] - N0) / N0 * math.exp(-r * A[\"years\"]))\n"
     "    return {\"half_recovery_years\": t50, \"recovered_by_200yr\": N200 / A[\"carrying\"],\n"
     "            \"initial_survivors\": N0, \"century_recovery\": 1.0 / (1.0 + 19.0 * math.exp(-r * 100.0))}\n"),
   "steps": [("Years to half recovery", "half_recovery_years", "yr"),
             ("Fraction recovered after 200 years", "recovered_by_200yr", ""),
             ("Surviving fauna fraction", "initial_survivors", ""),
             ("Fraction recovered after a century", "century_recovery", "")],
   "confirm": ["Recovery curves converge across sites with explained mechanisms.",
               "Pre-mining baselines exist where machines will go.",
               "Impact assessments use measured curves, not assumed resilience."],
   "refute": ["Monitoring lapses after a decade as usual.",
              "Commercial-scale disturbance proves qualitatively different from experiments."],
   "checks": [("half_recovery_years", 20.0, 500.0), ("recovered_by_200yr", 0.3, 1.0)],
   "honesty": ("Logistic regrowth with one rate is the simplest possible ecology - real succession has "
               "stages, species, and surprises. The sketch shows why slow growth means long recovery, "
               "which is the robust part."),
 }},
# ---------------------------------------------------------------- 28
{
 "key": "subseafloor-biosphere",
 "name": "How Deep Does Life Go Beneath the Seafloor?",
 "group": "Deep Ocean",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": ("Life has been found in sediments hundreds of meters below the seafloor and in fractured "
             "oceanic crust - but the true lower limit of the deep biosphere, set by temperature, energy, "
             "and pore space, has never been reached by drilling."),
 "background": ("The known temperature limit of life is 122 C, set by the archaeon Methanopyrus jannaschii, "
             "and geothermal gradients of 20-60 C per kilometer imply a hard thermal ceiling a few "
             "kilometers down - but energy, not temperature, may bite first. D Hondt and colleagues showed "
             "that microbes persist in South Pacific Gyre sediments millions of years old on vanishingly "
             "small energy fluxes, dividing on century timescales. Kallmeyer census work suggests the deep "
             "biosphere may hold a substantial fraction of Earth biomass - or far less, depending on whose "
             "extrapolation you trust. Scientific ocean drilling has sampled the shallow fringe; the "
             "deepest, hottest, most energy-starved realms - and the crustal aquifer where water circulates "
             "through basalt - remain largely unsampled, and the limit of life is still a theoretical "
             "line, not a measured one."),
 "why_it_matters": ("The deep biosphere may be the largest ecosystem on Earth by volume, a slow-motion "
             "bioreactor altering ocean chemistry over geological time. Its limits define the habitable "
             "zone of our own planet subsurface - and by extension the search for life in the Martian "
             "subsurface and icy ocean worlds. If life thrives kilometers down on milliwatts, our "
             "definition of habitability is far too narrow."),
 "sig_pointer": ("The Signature system proposes a limit-drilling program: scientific drilling transects "
             "aimed at the thermal and energy limits, with contamination controls that make negative "
             "results trustworthy. See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the limit of life as a depth to be drilled to "
             "- aim at the thermal ceiling with clean methods, and let the last living sample mark the "
             "line."),
 "signature_solution": (
     "Proposed approach. Step 1: select drilling transects spanning the gradient range - cold old crust "
     "where energy limits first, hot young crust where temperature limits first - so the two candidate "
     "ceilings are tested separately. Step 2: drill to and through the predicted limits with contamination "
     "controls rigorous enough that a sterile sample is publishable evidence, not an inconclusive one. "
     "Step 3: measure in-situ energy fluxes and metabolic rates at each depth, testing whether life "
     "fades at the predicted energy floor. Step 4: encode the measured limits into habitability models "
     "for Earth subsurface and ocean worlds, replacing theoretical lines with drilled ones.\n"
     "Assumptions: that drilling technology can reach the thermal limit cleanly (at the edge of current "
     "capability); that contamination control can make negatives trustworthy (the field perennial "
     "challenge); that gradients are stable enough for predictions (largely true).\n"
     "What would confirm it: life found exactly to the predicted thermal or energy line and not beyond, "
     "replicated across transects.\n"
     "What would kill it: life persisting far beyond predictions - implying unknown energy sources - or "
     "contamination defeating every deep sample.\n"
     "What this does NOT claim: it does not claim the deep biosphere dwarfs surface life; it does not "
     "promise astrobiology answers; it is not established geomicrobiology."),
 "citations": [
     "D Hondt S et al. Subseafloor sedimentary life in the South Pacific Gyre. Proc Natl Acad Sci; 2009.",
     "Kallmeyer J et al. Global distribution of microbial abundance and biomass in subseafloor sediment. Proc Natl Acad Sci; 2012.",
     "Edwards K J et al. Under the sea: microbial life in the oceanic crust. Nat Rev Microbiol; 2012."],
 "explorer": {
   "blurb": ("A habitability-depth sketch: it projects temperature with depth from the geothermal gradient, "
             "finds where the 122 C life limit is crossed, and compares the thermal ceiling against the "
             "energy-starvation floor - showing which limit bites first."),
   "assumptions": {"gradient_C_per_km": 30.0, "surface_C": 2.0, "life_limit_C": 122.0,
                   "energy_floor_km": 2.5},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    thermal_km = (A[\"life_limit_C\"] - A[\"surface_C\"]) / A[\"gradient_C_per_km\"]\n"
     "    limiting = min(thermal_km, A[\"energy_floor_km\"])\n"
     "    which = 1.0 if thermal_km < A[\"energy_floor_km\"] else 0.0\n"
     "    return {\"thermal_limit_km\": thermal_km, \"energy_limit_km\": A[\"energy_floor_km\"],\n"
     "            \"habitable_depth_km\": limiting, \"temperature_limited\": which}\n"),
   "steps": [("Thermal limit depth", "thermal_limit_km", "km"),
             ("Energy-starvation limit depth", "energy_limit_km", "km"),
             ("Habitable subseafloor depth", "habitable_depth_km", "km"),
             ("Temperature-limited (1) vs energy-limited (0)", "temperature_limited", "")],
   "confirm": ["Life found to the predicted line and not beyond, across transects.",
               "In-situ energy fluxes match the predicted floor.",
               "Habitability models adopt the drilled limits."],
   "refute": ["Life persists far beyond predictions - unknown energy sources.",
              "Contamination defeats every deep sample."],
   "checks": [("thermal_limit_km", 2.0, 8.0), ("habitable_depth_km", 1.0, 5.0)],
   "honesty": ("The energy floor is the least-constrained number in deep biosphere science - this sketch "
               "treats it as an input, but the drilling must measure it."),
 }},
# ---------------------------------------------------------------- 29
{
 "key": "internal-wave-solitons",
 "name": "Can We Predict Giant Internal Ocean Waves?",
 "group": "Waves and Extremes",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": ("In the South China Sea, underwater waves 100 meters tall - solitons - race from the Luzon "
             "Strait, strong enough to endanger submarines and mix the ocean, yet their generation and "
             "arrival remain only crudely predictable."),
 "background": ("Internal tides generated at the Luzon Strait ridges steepen into rank-ordered packets of "
             "solitary waves as they cross the South China Sea, with amplitudes exceeding 100 meters and "
             "currents over 2 meters per second - among the largest waves in the world ocean, invisible "
             "from the surface except in sun-glint satellite images. The IWISE program mapped their "
             "generation and transformation, showing a sensitive dependence on the Kuroshio position, "
             "stratification, and the spring-neap tidal cycle. But prediction - when a packet will arrive "
             "at a drilling rig or submarine operating area, with what amplitude - requires forecasting "
             "the nonlinear steepening across hundreds of kilometers of varying stratification, a problem "
             "no operational system solves."),
 "why_it_matters": ("Solitons are a hazard: their currents have damaged drilling operations and they are "
             "a first-order concern for submarine navigation in the region. They are also a major mixing "
             "agent, dissipating tidal energy on the continental slope and lifting nutrients - so their "
             "unpredictability is a gap in both safety and the ocean energy budget."),
 "sig_pointer": ("The Signature system proposes a soliton forecast testbed: a high-resolution model of the "
             "Luzon-to-slope system scored daily against moorings and satellite glint, until arrival "
             "predictions verify. See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats solitons as a forecast-verification problem - "
             "run the nonlinear model daily, score every packet, and let the hit rate be the verdict."),
 "signature_solution": (
     "Proposed approach. Step 1: maintain the moored sentinel line from Luzon Strait across the basin to "
     "the slope, measuring generation, steepening, and arrival continuously. Step 2: run a "
     "nonhydrostatic forecast model daily, initialized with observed stratification and tides, "
     "predicting packet arrivals 3-5 days out. Step 3: score every forecast against the moorings and "
     "satellite detections with published skill metrics - no selective reporting. Step 4: diagnose the "
     "misses - Kuroshio intrusion, mesoscale eddies, stratification errors - and feed the error "
     "attribution back into model development.\n"
     "Assumptions: that moorings survive the currents they measure (engineering challenge); that "
     "stratification initialization is adequate (marginally); that nonhydrostatic models are affordable "
     "operationally (computationally heavy).\n"
     "What would confirm it: arrival predictions verifying within hours and amplitude within tens of "
     "percent over a full spring-neap cycle and Kuroshio states.\n"
     "What would kill it: chaotic steepening defeating every forecast beyond a day, or the moored line "
     "proving unsustainable.\n"
     "What this does NOT claim: it does not claim solitons can be suppressed or steered; it does not "
     "promise operational status; it is not established physical oceanography."),
 "citations": [
     "Alford M H et al. The formation and fate of internal waves in the South China Sea. Nature; 2015.",
     "Ramp S R et al. Internal solitons in the northeastern South China Sea. IEEE J Oceanic Eng; 2004.",
     "Lien R-C et al. Modulation of internal waves by the Kuroshio. J Phys Oceanogr; 2014."],
 "explorer": {
   "blurb": ("A KdV soliton sketch: it computes solitary-wave speed and width from amplitude and "
             "stratification, estimates travel time across the basin, and shows how arrival prediction "
             "depends on getting the amplitude right."),
   "assumptions": {"amplitude_m": 100.0, "phase_speed": 2.5, "nonlinearity": 0.02, "distance_km": 400.0},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    c = A[\"phase_speed\"] * (1.0 + A[\"nonlinearity\"] * A[\"amplitude_m\"] / 2.0)\n"
     "    width_km = 2.0 * math.sqrt(A[\"phase_speed\"] / (A[\"nonlinearity\"] * A[\"amplitude_m\"]))\n"
     "    travel_h = A[\"distance_km\"] * 1000.0 / c / 3600.0\n"
     "    return {\"soliton_speed_m_per_s\": c, \"soliton_width_km\": width_km,\n"
     "            \"travel_time_hours\": travel_h, \"current_m_per_s\": c * 0.6}\n"),
   "steps": [("Soliton propagation speed", "soliton_speed_m_per_s", "m/s"),
             ("Soliton width", "soliton_width_km", "km"),
             ("Basin crossing time", "travel_time_hours", "hr"),
             ("Peak orbital current", "current_m_per_s", "m/s")],
   "confirm": ["Arrival predictions verify within hours over full tidal and Kuroshio cycles.",
               "Amplitude errors stay within tens of percent.",
               "Error attribution improves the model year on year."],
   "refute": ["Chaotic steepening defeats forecasts beyond a day.",
              "The moored sentinel line proves unsustainable."],
   "checks": [("soliton_speed_m_per_s", 2.0, 6.0), ("travel_time_hours", 20.0, 60.0)],
   "honesty": ("KdV theory is weakly nonlinear - real South China Sea solitons push its limits. The sketch "
               "shows the prediction quantities; the moorings must supply the verdict."),
 }},
# ---------------------------------------------------------------- 30
{
 "key": "deep-argo-heat",
 "name": "How Much Heat Is the Deep Ocean Hiding?",
 "group": "Observing the Ocean",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": ("The Argo array revolutionized ocean observation - but only down to 2000 meters. Below that, "
             "half the ocean volume, heat content is estimated from sparse ship sections, and the deep "
             "contribution to sea-level rise and warming is the largest observational gap in the energy "
             "budget."),
 "background": ("Since 2007 Argo 4000 profiling floats have measured the upper 2000 meters superbly, "
             "pinning down upper-ocean heat uptake - but Purkey and Johnson showed from repeat hydrography "
             "that the abyss below is also warming, contributing measurably to thermosteric sea-level "
             "rise. The estimates rest on ship sections repeated roughly decadally: exquisite accuracy, "
             "terrible sampling. Deep Argo - floats rated to 6000 meters pioneered by Johnson and "
             "colleagues - promises to close the gap, but the array is young, sparse, and expensive, and "
             "the deep heat content trend remains the least-constrained term in Earth energy imbalance "
             "accounting."),
 "why_it_matters": ("Earth energy imbalance - the watts per square meter the planet is gaining - is the "
             "single most important number in climate science, and the deep ocean is its largest "
             "uncertain reservoir. Sea-level budgets cannot close without the deep thermosteric term. "
             "The gap is not academic: it is the difference between knowing the planet energy gain to "
             "0.1 W/m2 or not."),
 "sig_pointer": ("The Signature system proposes completing Deep Argo as the top ocean-observing priority, "
             "with the deep heat-content time series published as a climate indicator alongside surface "
             "temperature. See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats deep heat as the missing climate indicator - "
             "finish the array, publish the time series, and close the energy budget."),
 "signature_solution": (
     "Proposed approach. Step 1: complete the Deep Argo array to its design density - roughly 1200 floats "
     "- prioritizing the abyssal warming hotspots identified by repeat hydrography. Step 2: maintain the "
     "repeat ship sections as calibration anchors, intercomparing float and ship data continuously. "
     "Step 3: publish the deep (below 2000 m) heat-content time series as an official climate indicator, "
     "with uncertainties, updated annually. Step 4: close the Earth energy imbalance budget with the deep "
     "term included, and require climate models to reproduce the observed deep warming pattern.\n"
     "Assumptions: that Deep Argo floats achieve multi-year lifespans at 6000 meters (demonstrated but "
     "costly); that funding prioritizes completion over new initiatives (politically uncertain); that "
     "the array density resolves the warming pattern (design studies say yes).\n"
     "What would confirm it: a continuous deep heat-content record with uncertainties small enough to "
     "close the energy budget, corroborated by independent ship sections.\n"
     "What would kill it: float lifespans or costs preventing array completion, leaving the deep term "
     "permanently estimated from sparse sections.\n"
     "What this does NOT claim: it does not claim the deep ocean dominates the energy budget; it does "
     "not fix sea-level projections alone; it is not established climate science."),
 "citations": [
     "Johnson G C et al. Deep Argo ocean heat content data. J Atmos Oceanic Technol; 2019.",
     "Purkey S G, Johnson G C. Warming of global abyssal and deep Southern Ocean waters. J Clim; 2010.",
     "von Schuckmann K et al. Heat stored in the Earth system. Earth Syst Sci Data; 2020."],
 "explorer": {
   "blurb": ("A deep heat-content sketch: it converts a deep-ocean warming rate over the below-2000-meter "
             "volume into zettajoules and watts per square meter - showing how a tiny temperature trend in "
             "a huge volume becomes a first-order climate term."),
   "assumptions": {"warming_C_per_dec": 0.01, "deep_volume_Mkm3": 700.0, "years": 20.0},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    vol = A[\"deep_volume_Mkm3\"] * 1e15\n"
     "    dT = A[\"warming_C_per_dec\"] / 10.0 * A[\"years\"]\n"
     "    heat_J = 1025.0 * 4000.0 * vol * dT\n"
     "    slr_mm = dT * 1.5e-4 * vol / 3.61e14 * 1000.0\n"
     "    return {\"deep_warming_C\": dT, \"heat_uptake_ZJ\": heat_J / 1e21,\n"
     "            \"imbalance_W_per_m2\": heat_J / (A[\"years\"] * 3.15e7) / 5.1e14,\n"
     "            \"sea_level_mm\": slr_mm}\n"),
   "steps": [("Deep-ocean warming", "deep_warming_C", "C"),
             ("Heat uptake", "heat_uptake_ZJ", "ZJ"),
             ("Earth energy imbalance share", "imbalance_W_per_m2", "W/m2"),
             ("Thermosteric sea-level rise", "sea_level_mm", "mm")],
   "confirm": ["A continuous deep heat record closes the energy budget within uncertainties.",
               "Ship sections corroborate the float record.",
               "Models reproduce the observed deep warming pattern."],
   "refute": ["Float lifespans or costs prevent array completion.",
              "The deep term stays estimated from sparse sections indefinitely."],
   "checks": [("heat_uptake_ZJ", 5.0, 60.0), ("imbalance_W_per_m2", 0.02, 0.25)],
   "honesty": ("The warming rate is the uncertain input dressed as an assumption - this sketch shows what "
               "rides on it, which is exactly why the array must measure it."),
 }},
# ---------------------------------------------------------------- 31
{
 "key": "bioluminescent-networks",
 "name": "Why Does So Much of the Deep Sea Glow?",
 "group": "Life and Ecosystems",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": ("Three-quarters of deep-sea animals can make light, in an environment where sunlight never "
             "reaches - yet for most of them, what the flashes mean, who they are for, and how the light "
             "ecology works remain unknown."),
 "background": ("Martini and Haddock 2017 found that 76 percent of observed deep-sea animals are "
             "bioluminescent - the rule, not the exception. Known functions cover only the basics: "
             "counterillumination camouflage in midwater fish and squid, the burglar-alarm flash that "
             "startles predators, lures like the anglerfish esca. But most emissions - the dinoflagellate "
             "milky seas spanning thousands of square kilometers, the siphonophore light shows, the "
             "specific flash patterns of copepods and ostracods - have no confirmed ecological role. "
             "Whether flashes are private communication channels, species recognition signals, or mostly "
             "byproducts remains untested, because observing behavior in the deep sea at the relevant "
             "scales has only recently become possible with low-light cameras."),
 "why_it_matters": ("If most deep-sea animals communicate by light, the largest ecosystem on Earth runs on "
             "an optical network we cannot read - and artificial light from submersibles, mining, and "
             "fishing may be scrambling it. Understanding the light ecology is prerequisite to assessing "
             "human impact on the deep sea, and it is one of the great unopened chapters of animal "
             "behavior."),
 "sig_pointer": ("The Signature system proposes a deep-sea light observatory: long-duration low-light "
             "camera stations recording flash behavior in situ, with stimulus-response experiments to "
             "decode the signals. See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats deep-sea light as a language to be recorded - "
             "watch long enough, in the dark, and let the grammar emerge from the data."),
 "signature_solution": (
     "Proposed approach. Step 1: deploy long-duration low-light observatories - cameras that see "
     "bioluminescence without blasting white light - at representative midwater and benthic sites, "
     "recording for months. Step 2: build the flash ethogram - catalog flash patterns by species, "
     "context, and outcome, the way bird song was cataloged. Step 3: run stimulus-response experiments "
     "with programmable light lures, testing whether specific patterns elicit specific behaviors - "
     "the decoding step. Step 4: assess the artificial-light impact - measure how submersible and "
     "industrial light alters the recorded behavior, informing deep-sea lighting standards.\n"
     "Assumptions: that low-light cameras capture ecologically relevant behavior (new but promising); "
     "that flash patterns are species-specific enough to catalog (likely); that months of observation "
     "suffice to see rare behaviors (uncertain).\n"
     "What would confirm it: repeatable flash-response grammars - specific patterns predicting specific "
     "behaviors across individuals and sites.\n"
     "What would kill it: flashes proving mostly physiological byproducts with no communicative "
     "structure, or observation bias defeating every cataloging attempt.\n"
     "What this does NOT claim: it does not claim to decode animal language; it does not promise "
     "biotech applications; it is not established marine biology."),
 "citations": [
     "Martini S, Haddock S H D. Quantification of bioluminescence. Sci Rep; 2017.",
     "Haddock S H D et al. Bioluminescence in the sea. Ann Rev Mar Sci; 2010.",
     "Widder E A. Bioluminescence in the ocean. Science; 2010."],
 "explorer": {
   "blurb": ("A light-ecology sketch: it computes how far a bioluminescent flash of given intensity "
             "travels in clear deep water before fading below detection, estimating the communication "
             "range that structures the deep-sea light network."),
   "assumptions": {"intensity": 1e10, "threshold": 1e4, "attenuation_per_m": 0.05},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    R = math.log(A[\"intensity\"] / A[\"threshold\"]) / A[\"attenuation_per_m\"]\n"
     "    R = R / 2.0\n"
     "    return {\"detection_range_m\": R, \"network_spacing_m\": R * 2.0,\n"
     "            \"dynamic_range\": math.log10(A[\"intensity\"] / A[\"threshold\"]),\n"
     "            \"volume_liters\": 4.0 / 3.0 * math.pi * R ** 3 * 1000.0}\n"),
   "steps": [("Flash detection range", "detection_range_m", "m"),
             ("Typical network spacing", "network_spacing_m", "m"),
             ("Intensity dynamic range", "dynamic_range", "orders"),
             ("Monitored water volume", "volume_liters", "liters")],
   "confirm": ["Repeatable flash-response grammars emerge across sites.",
               "Stimulus experiments decode specific pattern meanings.",
               "Artificial-light impacts are measured and standardized."],
   "refute": ["Flashes prove to be physiological byproducts without communicative structure.",
              "Observation bias defeats every cataloging attempt."],
   "checks": [("detection_range_m", 50.0, 200.0), ("dynamic_range", 4.0, 8.0)],
   "honesty": ("Exponential attenuation with one coefficient is a crude ocean - scattering and "
               "background complicate everything. The sketch sizes the communication problem; the "
               "cameras must read the messages."),
 }},
# ---------------------------------------------------------------- 32
{
 "key": "ocean-eddies-climate",
 "name": "Do Ocean Eddies Set the Climate?",
 "group": "Circulation",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": ("Mesoscale eddies - ocean storms 100 kilometers wide - hold most of the ocean kinetic "
             "energy and transport enormous heat, yet climate models cannot resolve them and parameterize "
             "their effects crudely. How much of the climate the eddies secretly control is unknown."),
 "background": ("Satellite altimetry revealed an ocean seething with eddies, the weather of the sea, "
             "carrying heat, salt, and carbon across basins - the Agulhas leakage alone injects warm "
             "Indian Ocean water into the Atlantic, potentially stabilizing the overturning. Gent and "
             "McWilliams 1990 gave models their standard eddy parameterization, flattening density "
             "surfaces as eddies do, but it is an approximation tuned, not derived, and eddy-resolving "
             "models show the parameterized ocean can differ qualitatively - in Southern Ocean heat "
             "uptake, in western boundary current separation, in carbon transport. Whether eddies merely "
             "stir or actively set stratification, overturning strength, and climate sensitivity remains "
             "the central uncertainty of ocean modeling."),
 "why_it_matters": ("Every century-scale climate projection runs on parameterized eddies. If the "
             "parameterization misrepresents heat uptake or the overturning response to winds, the "
             "projections are biased in ways no ensemble spread captures. Eddy-resolving climate models "
             "are coming but will remain too expensive for large ensembles for decades - so the "
             "parameterization question decides the credibility of the projections we actually use."),
 "sig_pointer": ("The Signature system proposes an eddy-truth campaign: compare parameterized and "
             "eddy-resolving models against the same observations - altimetry, Argo, moorings - and score "
             "which climate-relevant quantities the parameterization gets right. See the Signature "
             "Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats eddy parameterization as a scored contest - "
             "same observations, both model classes, and the climate-relevant errors decide."),
 "signature_solution": (
     "Proposed approach. Step 1: define the climate-relevant scorecard - Southern Ocean heat uptake, "
     "overturning strength and sensitivity, western boundary current paths, carbon transport - the "
     "quantities projections actually depend on. Step 2: run coordinated experiments with parameterized "
     "and eddy-resolving versions of the same models, scored against altimetry, Argo, and mooring "
     "arrays. Step 3: develop next-generation parameterizations - including machine-learned closures - "
     "trained on the eddy-resolving truth and tested out of sample. Step 4: require new climate models "
     "to publish their eddy scorecard, so users see which projections rest on solid representation and "
     "which on hope.\n"
     "Assumptions: that eddy-resolving models are truth enough to train on (they have their own "
     "biases); that learned closures generalize across climates (unproven); that the scorecard "
     "captures what matters (a judgment call).\n"
     "What would confirm it: next-generation parameterizations matching eddy-resolving results on the "
     "scorecard across model families, with published error bars.\n"
     "What would kill it: eddy effects proving irreducibly resolution-dependent - no parameterization "
     "capturing the climate-relevant quantities - forcing the field to wait for exascale.\n"
     "What this does NOT claim: it does not claim current projections are wrong; it does not promise "
     "cheap eddy-resolving climate models; it is not established ocean modeling."),
 "citations": [
     "Gent P R, McWilliams J C. Isopycnal mixing in ocean circulation models. J Phys Oceanogr; 1990.",
     "Chelton D B et al. Global observations of nonlinear mesoscale eddies. Prog Oceanogr; 2011.",
     "Griffies S M et al. Impacts on ocean heat uptake of eddy-resolving models. J Clim; 2015."],
 "explorer": {
   "blurb": ("An eddy-transport sketch: it estimates eddy heat transport from a Gent-McWilliams diffusivity "
             "acting on the meridional temperature gradient, and compares it to the total ocean heat "
             "transport - sizing the parameterized unknown."),
   "assumptions": {"kappa_GM": 1000.0, "slope": 0.001, "delta_T": 5.0, "depth_m": 1000.0,
                   "length_m": 1e7, "total_PW": 1.5},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    v_star = A[\"kappa_GM\"] * A[\"slope\"] / A[\"depth_m\"]\n"
     "    transport_W = 1025.0 * 4000.0 * v_star * A[\"delta_T\"] * A[\"depth_m\"] * A[\"length_m\"]\n"
     "    transport_PW = transport_W / 1e15\n"
     "    return {\"eddy_velocity_mm_per_s\": v_star * 1000.0, \"eddy_transport_PW\": transport_PW,\n"
     "            \"eddy_share\": transport_PW / A[\"total_PW\"], \"kappa_m2_per_s\": A[\"kappa_GM\"]}\n"),
   "steps": [("Eddy-induced velocity", "eddy_velocity_mm_per_s", "mm/s"),
             ("Eddy heat transport", "eddy_transport_PW", "PW"),
             ("Eddy share of total transport", "eddy_share", ""),
             ("GM diffusivity", "kappa_m2_per_s", "m2/s")],
   "confirm": ["New parameterizations match eddy-resolving results on the scorecard.",
               "Climate models publish eddy scorecards with error bars.",
               "Out-of-sample tests validate learned closures."],
   "refute": ["Eddy effects prove irreducibly resolution-dependent.",
              "No parameterization captures the climate-relevant quantities."],
   "checks": [("eddy_transport_PW", 0.1, 1.2), ("eddy_share", 0.05, 0.8)],
   "honesty": ("One diffusivity times one gradient is the parameterization in miniature - the real ocean "
               "has eddies within eddies. The sketch sizes the unknown; the model contest must shrink it."),
 }},
# ---------------------------------------------------------------- 33
{
 "key": "ocean-carbon-geoengineering",
 "name": "Can the Ocean Be Engineered to Draw Down Carbon Safely?",
 "group": "Carbon and Climate",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": ("Ocean carbon dioxide removal - alkalinity enhancement, iron fertilization, artificial "
             "upwelling - promises gigaton-scale drawdown, but efficacy, side effects, and verification "
             "are all unproven at climate-relevant scales."),
 "background": ("John Martin 1990 half-joking proposal - give me half a tanker of iron and I will give "
             "you an ice age - launched a dozen iron fertilization experiments (IronEx, SOFeX, EIFEX) that "
             "proved blooms but ambiguous export: carbon sank, then much of it was remineralized shallow. "
             "Ocean alkalinity enhancement - adding crushed minerals to shift carbonate chemistry - is "
             "chemically sound in the lab but untested in the open ocean, with unknown ecological effects "
             "of the particles and the altered chemistry. Artificial upwelling and seaweed sinking face "
             "similar verification gaps. The field runs ahead of the science: startups sell credits while "
             "researchers debate whether any method sequesters carbon durably, and governance - who "
             "permits, who monitors, who is liable - barely exists."),
 "why_it_matters": ("If any ocean method works safely at gigaton scale, it changes the net-zero equation; "
             "if none does, capital and attention are being diverted from emissions cuts to expensive "
             "theater. Worse, large-scale deployment without understanding could damage ocean ecosystems "
             "or backfire on the carbon cycle. The efficacy question is the most consequential applied "
             "question in oceanography."),
 "sig_pointer": ("The Signature system proposes a verification-first research program: field trials at "
             "meaningful scale with pre-registered efficacy criteria, full ecosystem monitoring, and no "
             "credit sales until durability is demonstrated. See the Signature Edition record for the "
             "full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats ocean carbon removal as guilty until proven "
             "durable - pre-registered criteria, full monitoring, and no credits before proof."),
 "signature_solution": (
     "Proposed approach. Step 1: define the efficacy bar precisely - tons of CO2 removed from the "
     "atmosphere for centuries, additional to baseline, verifiable by measurement - and require every "
     "method to clear it in pre-registered field trials. Step 2: run the trials at scales where the "
     "carbon and ecosystem signals exceed detection limits, with independent monitoring of export, "
     "remineralization, and ecological side effects. Step 3: build the verification toolkit - tracers, "
     "autonomous monitoring, carbon accounting protocols - as public infrastructure, not proprietary "
     "secrets. Step 4: establish the governance before deployment - permitting, liability, and a ban "
     "on credit sales until durability is demonstrated, so the market cannot outrun the science.\n"
     "Assumptions: that field trials at meaningful scale can be permitted (politically contested); "
     "that durability is measurable on policy-relevant timescales (centuries cannot be observed "
     "directly); that governance can precede commercial pressure (historically doubtful).\n"
     "What would confirm it: a method clearing the pre-registered bar - measured, additional, durable "
     "removal - replicated independently.\n"
     "What would kill it: trials showing export gains erased by remineralization, or ecological side "
     "effects outweighing carbon benefits, across methods.\n"
     "What this does NOT claim: it does not endorse any method or company; it does not claim the ocean "
     "should be engineered; it is not established climate policy science."),
 "citations": [
     "Martin J H. Glacial-interglacial CO2 change: the iron hypothesis. Paleoceanography; 1990.",
     "Boyd P W et al. Mesoscale iron enrichment experiments. Science; 2007.",
     "National Academies. A Research Strategy for Ocean-based Carbon Dioxide Removal. 2022."],
 "explorer": {
   "blurb": ("An alkalinity-enhancement sketch: it adds alkalinity to surface seawater, computes the "
             "additional CO2 uptake from carbonate chemistry, discounts for incomplete air-sea "
             "equilibration, and prices the carbon per ton of mineral."),
   "assumptions": {"alkalinity_mol": 1e9, "uptake_ratio": 0.8, "equilibration": 0.7, "mineral_t_per_mol": 0.0001},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    co2_mol = A[\"alkalinity_mol\"] * A[\"uptake_ratio\"] * A[\"equilibration\"]\n"
     "    co2_tons = co2_mol * 44.0 / 1e6\n"
     "    mineral_tons = A[\"alkalinity_mol\"] * A[\"mineral_t_per_mol\"]\n"
     "    return {\"co2_removed_tons\": co2_tons, \"mineral_required_tons\": mineral_tons,\n"
     "            \"tons_co2_per_ton_mineral\": co2_tons / mineral_tons,\n"
     "            \"gross_uptake_ratio\": A[\"uptake_ratio\"] * A[\"equilibration\"]}\n"),
   "steps": [("CO2 removed", "co2_removed_tons", "tons"),
             ("Mineral required", "mineral_required_tons", "tons"),
             ("Removal efficiency", "tons_co2_per_ton_mineral", "t CO2/t mineral"),
             ("Net uptake ratio", "gross_uptake_ratio", "mol/mol")],
   "confirm": ["A method clears the pre-registered durability bar, replicated independently.",
               "Verification toolkits become public infrastructure.",
               "Governance precedes any deployment."],
   "refute": ["Export gains prove erased by remineralization across methods.",
              "Side effects outweigh carbon benefits; the market outruns the science anyway."],
   "checks": [("co2_removed_tons", 20000.0, 40000.0), ("tons_co2_per_ton_mineral", 0.2, 0.6)],
   "honesty": ("The uptake ratio and equilibration are the contested science compressed into inputs - "
               "and the sketch ignores mining, grinding, and transport emissions entirely. Efficacy "
               "claims must survive the full life cycle, not this sketch."),
 }},
# ---------------------------------------------------------------- 34
{
 "key": "ocean-turbulence-closure",
 "name": "Can Climate Models Ever Resolve Ocean Turbulence?",
 "group": "Carbon and Climate",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": ("Ocean turbulence spans from basin gyres to millimeter dissipation - ten orders of magnitude "
             "no model will ever resolve - so climate models must parameterize what they cannot see. "
             "Whether that closure can ever be trustworthy, or the ocean will always surprise its models, "
             "is the deepest methodological question in the field."),
 "background": ("The closure problem is as old as turbulence theory: Reynolds averaging leaves unknown "
             "correlations that must be modeled, and every ocean parameterization - Gent-McWilliams for "
             "eddies, KPP for the boundary layer, tidal mixing schemes - is a closure assumption with "
             "tunable constants. As resolution increases, the gray zone shifts but never vanishes: "
             "resolve the mesoscale and the submesoscale needs closure; resolve that and boundary-layer "
             "turbulence needs it. Machine learning now offers data-driven closures trained on "
             "high-resolution simulations, but they inherit the training data biases and may fail in "
             "climates unlike the present. The philosophical edge: the ocean is a chaotic, multi-scale "
             "system, and it is not proven that any closure hierarchy converges to the right climate."),
 "why_it_matters": ("This is the credibility foundation of all ocean-containing climate projections. If "
             "closures can be made trustworthy - validated across regimes, with quantified uncertainty - "
             "then projections rest on physics. If the ocean chaotic multi-scale nature defeats closure, "
             "then long-term ocean projections carry irreducible uncertainty that must be admitted, not "
             "hidden in ensemble spreads. Either answer reshapes how science advises policy."),
 "sig_pointer": ("The Signature system proposes a closure-verification hierarchy: every parameterization "
             "tested across regimes - present, paleo, idealized - with out-of-sample climates as the "
             "exam, until trust is earned or limits admitted. See the Signature Edition record for the "
             "full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats turbulence closure as trust to be earned - "
             "test every parameterization outside its training climate, and publish where it breaks."),
 "signature_solution": (
     "Proposed approach. Step 1: build the closure test suite - a hierarchy from idealized turbulence "
     "through eddy-resolving basins to paleoclimate states - that every parameterization must pass, "
     "with out-of-sample climates weighted hardest. Step 2: require uncertainty quantification with "
     "every closure: not a best value but a distribution, propagated into projections. Step 3: run "
     "the adversarial program - deliberately search for climates and regimes where each closure fails, "
     "and publish the failure modes as prominently as the successes. Step 4: where closures fail "
     "irreducibly, say so: mark those projection quantities as unresolvable-at-current-resolution "
     "rather than letting tuned constants masquerade as physics.\n"
     "Assumptions: that test hierarchies capture the relevant failure modes (an article of faith); "
     "that uncertainty quantification is computationally affordable (barely); that the field will "
     "publish failures as readily as successes (culturally hard).\n"
     "What would confirm it: closures passing out-of-sample climate tests with quantified, shrinking "
     "uncertainty - trust earned across regimes.\n"
     "What would kill it: systematic failure outside training climates, with uncertainty refusing to "
     "shrink - the irreducible-uncertainty verdict.\n"
     "What this does NOT claim: it does not claim current models are untrustworthy; it does not promise "
     "closure is achievable; it is not established fluid dynamics - it is a proposal about how the "
     "field should judge itself."),
 "citations": [
     "Gent P R et al. Parameterizing eddy-induced tracer transports. J Phys Oceanogr; 1995.",
     "Fox-Kemper B et al. Parameterization of mixed layer eddies. J Phys Oceanogr; 2011.",
     "Zanna L, Bolton T. Data-driven equation discovery of ocean mesoscale closures. Geophys Res Lett; 2020."],
 "explorer": {
   "blurb": ("A resolution-cost sketch: it computes the grid needed to resolve the Rossby radius at a "
             "given latitude, the cost scaling of a global eddy-resolving model, and the closure burden "
             "that remains at each resolution - showing why the problem never disappears."),
   "assumptions": {"rossby_km": 30.0, "points_per_radius": 4.0, "earth_ocean_Mkm2": 361.0,
                   "cost_exponent": 4.0},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    dx_km = A[\"rossby_km\"] / A[\"points_per_radius\"]\n"
     "    cells = A[\"earth_ocean_Mkm2\"] * 1e6 / dx_km ** 2\n"
     "    cost = (100.0 / dx_km) ** A[\"cost_exponent\"]\n"
     "    return {\"grid_spacing_km\": dx_km, \"surface_cells_millions\": cells / 1e6,\n"
     "            \"relative_cost\": cost, \"closure_burden\": 1.0 / A[\"points_per_radius\"]}\n"),
   "steps": [("Required grid spacing", "grid_spacing_km", "km"),
             ("Surface grid cells", "surface_cells_millions", "millions"),
             ("Relative compute cost", "relative_cost", "x"),
             ("Remaining closure burden", "closure_burden", "")],
   "confirm": ["Closures pass out-of-sample climate tests with shrinking uncertainty.",
               "Failure modes are published as prominently as successes.",
               "Projections carry honest resolution-limit labels."],
   "refute": ["Systematic failure outside training climates; uncertainty refuses to shrink.",
              "The field keeps tuning constants and calling it physics."],
   "checks": [("grid_spacing_km", 5.0, 12.0), ("surface_cells_millions", 3.0, 12.0)],
   "honesty": ("The cost exponent is approximate and the real bill includes time steps and ensembles - "
               "but the scaling argument is robust: resolving smaller scales always costs more than "
               "linear, and something always remains unresolved."),
 }},
]
