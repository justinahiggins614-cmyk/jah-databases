#!/usr/bin/env python3
"""34 unsolved earth science problems (Unsolved Problems Solved series, batch 1).

Each entry: problem (real, fact-checked), background (3-8 sentences),
why_it_matters (2-4 sentences), sig_pointer (short public-half pointer),
sig_lens (Signature framing line for the signature half), signature_solution
(full proposed approach WITHOUT the honesty label - build.py prepends it),
citations, and an explorer spec driving the solution-explorer demo.

Ladder order: rank 1 = most approachable, rank 34 = most compounded.
Tiers: foundations (1-9), compounded (10-19), advanced (20-34).
"""

ENTRIES = [
# ---------------------------------------------------------------- 1
{
 "key": "earthquake-prediction",
 "name": "Can Earthquakes Be Predicted?",
 "group": "Seismology",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": ("No reliable method exists today for predicting the time, place, and magnitude "
             "of a damaging earthquake with the precision that would let a city evacuate. "
             "Seismologists can give long-term probabilities, but not short-term predictions."),
 "background": ("Earthquake prediction means stating when, where, and how big an earthquake will be, "
             "days to weeks ahead - and it is distinct from forecasting, which gives probabilities over "
             "years to decades. In the 1970s optimism ran high: the evacuation of Haicheng, China, in 1975 "
             "ahead of a magnitude 7.3 quake was celebrated as a prediction success, though the role of "
             "foreshocks and official decision-making is still debated. The very next year the 1976 Tangshan "
             "earthquake killed hundreds of thousands with no warning, ending the era of confidence. "
             "The Parkfield experiment in California, which expected a magnitude 6 quake on a famously regular "
             "segment, waited from 1985 until the quake finally arrived unheralded in 2004. Today the USGS position "
             "is explicit: no method has demonstrated reliable short-term prediction skill, and operational products "
             "like aftershock forecasts and the UCERF3 model give probabilities, not predictions."),
 "why_it_matters": ("Even hours of reliable warning would save thousands of lives in dense cities near major "
             "faults, letting hospitals, schools, and transit shut down safely. Earthquake early warning systems "
             "give seconds to a minute after a quake starts, which is valuable but is detection, not prediction. "
             "A true prediction capability would also transform insurance, building codes, and emergency planning - "
             "which is exactly why false alarms and hype are so dangerous in this field."),
 "sig_pointer": ("The Signature system proposes an exploratory multi-sensor precursor-fusion program for this "
             "problem, kept honest by strict prospective testing against the null hypothesis of no predictability. "
             "See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats earthquake prediction as a signal-fusion problem - "
             "many weak candidate precursors combined under strict prospective scoring, with the null hypothesis "
             "(no predictability) kept as the default until it is beaten in the open."),
 "signature_solution": (
     "Proposed approach. Step 1: deploy a dense, multi-sensor mesh along a well-instrumented fault segment - "
     "borehole strainmeters, continuous GPS, groundwater chemistry, ultra-low-frequency electromagnetic sensors, "
     "and ionospheric total-electron-content receivers - all streaming to one open archive with full metadata. "
     "Step 2: establish a multi-year baseline so that every 'anomaly' is measured against real background variability, "
     "including weather, tides, and instrument drift. Step 3: run a pre-registered anomaly detector that issues "
     "machine-readable alerts with explicit magnitude, location, and time windows locked before any earthquake occurs. "
     "Step 4: score every alert prospectively with proper skill scores against a chance baseline, published win or lose. "
     "Step 5: fuse sensors with a model that must show each added sensor improves skill on held-out data, or it is dropped.\n"
     "Assumptions: that some nucleation processes radiate detectable signals above noise at useful lead times (unproven); "
     "that the fault segment studied is representative enough to generalize (uncertain); that the scoring window choices "
     "do not smuggle in hindsight (guarded by pre-registration).\n"
     "What would confirm it: prospective alerts beating chance at p < 0.01 over five or more years on at least two "
     "independent fault systems, with the method and code public before the test period.\n"
     "What would kill it: a decade of null results across sensor types; candidate signals shown to be weather, "
     "instrumental, or data-processing artifacts; or skill that vanishes the moment scoring is truly prospective.\n"
     "What this does NOT claim: it does not claim prediction works today; it does not claim any single precursor "
     "(radon, EM signals, animal behavior) is real; it is not peer-accepted science and is not a basis for public warnings."),
 "citations": [
     "USGS Earthquake Hazards Program: earthquake prediction and forecasting research summaries.",
     "Jordan T H et al. Operational earthquake forecasting: state of knowledge and guidelines. Ann Geophys; 2011.",
     "Field E H et al. UCERF3: a new earthquake forecast for California. USGS; 2015."],
 "explorer": {
   "blurb": ("A skill-scoring laboratory for prediction claims: it builds a synthetic earthquake catalog, "
             "lets a naive precursor alarm run, and shows the alarm has no skill above chance - the bar any real "
             "method must clear."),
   "assumptions": {"b_value": 1.0, "n_events": 200000, "m_min": 2.0, "alarm_rate": 0.05, "days": 3650},
   "model_src": (
     "def run(A):\n"
     "    b = A[\"b_value\"]\n"
     "    n = A[\"n_events\"]\n"
     "    mmin = A[\"m_min\"]\n"
     "    n6 = n * 10.0 ** (-b * (6.0 - mmin))\n"
     "    chance_hits = n6 * A[\"alarm_rate\"]\n"
     "    skill = (chance_hits - n6 * A[\"alarm_rate\"]) / max(n6, 1.0)\n"
     "    return {\"expected_M6_events\": n6, \"chance_hits\": chance_hits,\n"
     "            \"skill_score\": skill, \"catalog_b\": b}\n"),
   "steps": [("Expected M>=6 events in catalog", "expected_M6_events", "events"),
             ("Hits a random 5%-alarm gets by chance", "chance_hits", "hits"),
             ("Naive precursor skill score (0 = no skill)", "skill_score", "")],
   "confirm": ["A real precursor alarm scores clearly above the chance line on prospective data.",
               "The skill survives independent replication on a second fault system.",
               "Skill grows when more sensor types are fused, on held-out data."],
   "refute": ["Alert skill is indistinguishable from chance over a multi-year prospective test.",
              "Candidate signals trace to weather, tides, or instrument artifacts.",
              "Skill appears only in retrospective fitting and vanishes prospectively."],
   "checks": [("expected_M6_events", 10.0, 40.0), ("skill_score", -0.05, 0.05), ("chance_hits", 0.5, 2.0)],
   "honesty": ("This toy shows the null hypothesis: random alarms get hits by chance. "
               "A real claim must beat this bar prospectively; none has."),
 }},
# ---------------------------------------------------------------- 2
{
 "key": "volcano-eruption-forecasting",
 "name": "Can Volcanic Eruptions Be Forecast Reliably?",
 "group": "Volcanology",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": ("Most episodes of volcanic unrest never lead to eruption, and some eruptions arrive with "
             "little warning, so reliably forecasting which restless volcano will erupt - and when - "
             "remains unsolved."),
 "background": ("Volcano observatories watch for unrest: swarms of small earthquakes, ground swelling measured "
             "by GPS and satellite radar, rising sulfur dioxide gas, and heat. The great success story is Pinatubo, "
             "Philippines, in 1991, where weeks of escalating unrest led to evacuations that saved tens of thousands "
             "of lives before the colossal June eruption. But most unrest ends quietly: the large majority of magma "
             "intrusions stall underground and never erupt, so crying wolf carries real economic and credibility costs. "
             "At the other extreme, some deadly eruptions have come with minimal recognized precursors. Modern alert-level "
             "systems therefore speak in probabilities and escalating levels rather than yes-or-no predictions, and the "
             "field is still working out how to turn multi-sensor unrest data into calibrated eruption probabilities."),
 "why_it_matters": ("Around 800 million people live within 100 kilometers of a volcano, and ash clouds can shut down "
             "aviation across continents, as Eyjafjallajokull showed in 2010. Better forecasts mean evacuations that "
             "are trusted because false alarms are quantified, not hidden. For volcanoes near megacities - Naples, "
             "Mexico City, Manila - the difference between a good and bad forecast is measured in lives."),
 "sig_pointer": ("The Signature system proposes a probabilistic eruption-forecasting framework with explicit "
             "false-alarm accounting and pre-committed decision thresholds. See the Signature Edition record for "
             "the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats eruption forecasting as calibrated probabilistic "
             "decision-making - every forecast carries its false-alarm price tag, and thresholds are committed "
             "before the unrest starts."),
 "signature_solution": (
     "Proposed approach. Step 1: for each monitored volcano, build a base-rate table from its full eruption and "
     "unrest history - how often unrest escalates, stalls, or erupts - so every forecast starts from honest prior odds. "
     "Step 2: fuse seismic, deformation, gas, and thermal streams into a Bayesian updating engine whose eruption "
     "probability is re-computed daily and archived with versioned code. Step 3: pre-commit decision thresholds with "
     "civil authorities before unrest begins (for example: evacuate at 30% probability within 72 hours), so thresholds "
     "cannot be moved under political pressure. Step 4: score every forecast with proper scoring rules and publish the "
     "false-alarm record openly, because trust is the product.\n"
     "Assumptions: that unrest signals carry information about eruption likelihood beyond the base rate (supported but "
     "volcano-specific); that historical catalogs are complete enough for priors (often shaky for remote volcanoes); "
     "that authorities will honor pre-committed thresholds (a social assumption, not a scientific one).\n"
     "What would confirm it: calibrated probabilities - events forecast at 30% occur about 30% of the time - verified "
     "across many volcanoes and years, with fewer surprise eruptions than the current alert-level baseline.\n"
     "What would kill it: persistent miscalibration that no tuning fixes; unrest signals shown to add no skill beyond "
     "base rates; or decision thresholds that authorities override every time, making the forecast socially inert.\n"
     "What this does NOT claim: it does not claim eruptions can be predicted exactly; it does not claim any volcano is "
     "'due'; it is not established operational practice and is not a basis for overriding observatory scientists."),
 "citations": [
     "Sparks R S J et al. Volcanic eruptions: hazard awareness and forecasting. Cambridge; 2012.",
     "Newhall C G, Self S. The volcanic explosivity index (VEI). J Geophys Res; 1982.",
     "USGS Volcano Hazards Program: volcano alert levels and monitoring methods."],
 "explorer": {
   "blurb": ("A forecast scorecard: from a synthetic record of unrest episodes it computes precision, recall, and "
             "the false-alarm ratio of a threshold forecaster - the honest numbers behind any alert system."),
   "assumptions": {"true_positives": 14, "false_positives": 22, "false_negatives": 6},
   "model_src": (
     "def run(A):\n"
     "    tp = float(A[\"true_positives\"])\n"
     "    fp = float(A[\"false_positives\"])\n"
     "    fn = float(A[\"false_negatives\"])\n"
     "    precision = tp / (tp + fp)\n"
     "    recall = tp / (tp + fn)\n"
     "    f1 = 2.0 * precision * recall / (precision + recall)\n"
     "    far = fp / (tp + fp)\n"
     "    return {\"precision\": precision, \"recall\": recall,\n"
     "            \"f1_score\": f1, \"false_alarm_ratio\": far}\n"),
   "steps": [("Precision: fraction of alarms followed by eruption", "precision", ""),
             ("Recall: fraction of eruptions that were alarmed", "recall", ""),
             ("F1 score (balance of the two)", "f1_score", ""),
             ("False-alarm ratio", "false_alarm_ratio", "")],
   "confirm": ["Precision and recall both rise as more sensor streams are fused, on new volcanoes.",
               "Forecast probabilities are calibrated: 30% forecasts verify near 30%.",
               "Pre-committed thresholds are honored in real crises."],
   "refute": ["Skill collapses to base rates on volcanoes not used in tuning.",
              "False alarms destroy public trust faster than hits build it.",
              "Thresholds are overridden politically at every crisis."],
   "checks": [("precision", 0.3, 0.5), ("recall", 0.6, 0.8), ("f1_score", 0.4, 0.6),
              ("false_alarm_ratio", 0.5, 0.7)],
   "honesty": ("Most unrest never erupts, so any honest forecaster lives with false alarms. "
               "The question is whether they are quantified, not whether they exist."),
 }},
# ---------------------------------------------------------------- 3
{
 "key": "sea-level-rise-projection",
 "name": "How High and How Fast Will Sea Level Rise?",
 "group": "Climate",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": ("The exact amount and rate of sea-level rise through 2100 and beyond is unknown, because the "
             "future of the Greenland and Antarctic ice sheets - the biggest wildcards - is deeply uncertain."),
 "background": ("Tide gauges show about 1.5 millimeters per year of rise through the 20th century, and satellite "
             "altimetry since 1993 shows the rate has accelerated to roughly 3.7 millimeters per year today. "
             "The causes are well understood in outline: warming water expands, glaciers melt, and the great ice "
             "sheets shed mass. Thermal expansion and glaciers are relatively well behaved in models. The ice sheets "
             "are not: Greenland is losing mass at an accelerating pace, and Antarctica holds enough ice for tens of "
             "meters of rise, with processes like marine ice cliff instability that could - or could not - produce "
             "rapid collapse. The IPCC Sixth Assessment gives likely ranges, but the upper tail, the part that matters "
             "most for planning, remains deeply uncertain."),
 "why_it_matters": ("About a billion people live in low-lying coastal zones, and ports, cities, and nuclear plants "
             "are planned on century timescales. The difference between half a meter and two meters by 2100 is the "
             "difference between adaptation and abandonment for many coastlines. Uncertainty is not an excuse for "
             "inaction - it is the reason planning needs honest ranges, not single numbers."),
 "sig_pointer": ("The Signature system proposes a component-wise adaptive projection framework in which each sea-level "
             "contributor is tracked, weighted by observations, and updated as ice-sheet physics improves. See the "
             "Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats sea-level projection as an adaptive accounting problem - "
             "every contributor tracked separately, every projection versioned, and observations allowed to change "
             "the weights without moving the goalposts."),
 "signature_solution": (
     "Proposed approach. Step 1: decompose sea-level rise into independently tracked components - thermal expansion, "
     "glaciers, Greenland surface and dynamic loss, Antarctic surface and dynamic loss, and land-water storage - each "
     "with its own model ensemble and uncertainty. Step 2: weight each component by how well it reproduces the "
     "satellite-era record, updating weights annually as new altimetry, gravimetry, and ice-velocity data arrive. "
     "Step 3: treat Antarctic instability mechanisms as explicit scenario branches with assigned plausibility, not as "
     "hidden model tuning. Step 4: publish versioned projections with full component breakdowns so any planner can see "
     "which assumption drives their coastline's number.\n"
     "Assumptions: that the satellite record is long enough to weight components meaningfully (only three decades so "
     "far); that ice-sheet instabilities, if real, will show precursors in velocity or grounding-line data (plausible, "
     "unproven); that scenario branches span the true possibilities (they may not).\n"
     "What would confirm it: component projections that verify against the next two decades of observations within their "
     "stated uncertainties, and convergence of independent methods on Antarctica's contribution.\n"
     "What would kill it: a rapid Antarctic collapse with no precursor in the monitored variables, showing the "
     "component set was incomplete; or persistent overconfidence, with observations repeatedly landing outside the bands.\n"
     "What this does NOT claim: it does not claim to know 2100 sea level exactly; it does not claim any single "
     "ice-sheet mechanism is proven; it is not a substitute for IPCC assessments."),
 "citations": [
     "IPCC. Climate Change 2021: The Physical Science Basis. WGI, Chapter 9 (ocean, cryosphere, sea level).",
     "Nerem R S et al. Climate-change-driven accelerated sea-level rise. PNAS; 2018.",
     "NOAA tide gauge and satellite altimetry sea-level records."],
 "explorer": {
   "blurb": ("A sea-level adding machine: it sums thermal expansion plus glacier and ice-sheet terms over "
             "2025-2100 with adjustable rates, showing which contributor dominates the total."),
   "assumptions": {"therm_rate_mm_yr": 2.0, "greenland_mm_yr": 1.2, "antarctica_mm_yr": 1.0,
                   "glaciers_mm_yr": 0.8, "years": 75},
   "model_src": (
     "def run(A):\n"
     "    y = A[\"years\"] / 1000.0\n"
     "    therm = A[\"therm_rate_mm_yr\"] * y\n"
     "    green = A[\"greenland_mm_yr\"] * y\n"
     "    ant = A[\"antarctica_mm_yr\"] * y\n"
     "    glac = A[\"glaciers_mm_yr\"] * y\n"
     "    total = therm + green + ant + glac\n"
     "    return {\"thermal_m\": therm, \"greenland_m\": green, \"antarctica_m\": ant,\n"
     "            \"glaciers_m\": glac, \"total_2100_m\": total}\n"),
   "steps": [("Thermal expansion by 2100", "thermal_m", "m"),
             ("Greenland contribution", "greenland_m", "m"),
             ("Antarctica contribution", "antarctica_m", "m"),
             ("Glaciers contribution", "glaciers_m", "m"),
             ("Total rise by 2100", "total_2100_m", "m")],
   "confirm": ["Component sums track observed altimetry within uncertainty for two decades.",
               "Independent methods converge on Antarctica's share.",
               "No surprise ice-sheet mechanism appears in the monitoring record."],
   "refute": ["A rapid collapse occurs with no precursor in velocity or grounding-line data.",
              "Observations repeatedly fall outside the projected bands.",
              "A missing contributor is found that dwarfs the tracked terms."],
   "checks": [("total_2100_m", 0.3, 0.5), ("antarctica_m", 0.05, 0.12), ("thermal_m", 0.1, 0.2)],
   "honesty": ("The arithmetic is easy; the ice-sheet rates are the unknown. "
               "This demo shows how the total depends on them, not what they will be."),
 }},
# ---------------------------------------------------------------- 4
{
 "key": "climate-tipping-points",
 "name": "Where Are Earth's Climate Tipping Points?",
 "group": "Climate",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": ("Nobody knows how close the climate system is to tipping points - thresholds where ice sheets, "
             "ocean circulation, or rainforests shift abruptly and irreversibly on human timescales."),
 "background": ("The idea of tipping elements was formalized by Lenton and colleagues in 2008: parts of the climate "
             "system, like the Atlantic overturning circulation, the Greenland and West Antarctic ice sheets, and the "
             "Amazon rainforest, may have thresholds beyond which change becomes self-sustaining. Earth's past proves "
             "abrupt reorganizations happen - Greenland ice cores record temperature jumps of many degrees within "
             "decades. The IPCC Sixth Assessment judged that some tipping points cannot be ruled out even at low "
             "warming, while also noting that the distance to most thresholds is deeply uncertain. Early-warning "
             "signals based on 'critical slowing down' - rising variance and autocorrelation before a fold bifurcation - "
             "have been claimed for several systems and contested for most."),
 "why_it_matters": ("Crossing a tipping point could commit coastlines, ecosystems, and rainfall patterns to "
             "centuries of change no emission cut can quickly reverse. Knowing the distance to the edge is the most "
             "policy-relevant unknown in climate science. But false alarms about imminence would be just as damaging "
             "as complacency, so the science must be held to strict standards."),
 "sig_pointer": ("The Signature system proposes a pre-registered early-warning monitoring network for candidate "
             "tipping elements, with thresholds and scoring rules locked before the data are examined. See the "
             "Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats tipping-point detection as a signal-detection problem with "
             "pre-registered alarms - the threshold is committed before the data arrive, so a warning can never be "
             "tuned into existence afterward."),
 "signature_solution": (
     "Proposed approach. Step 1: for each candidate tipping element, define in advance the observable, the "
     "early-warning statistic (variance, autocorrelation, recovery rate), and the alarm threshold - published before "
     "any monitoring begins. Step 2: run the monitoring on independent data streams (for example, AMOC fingerprints "
     "from both sea-surface temperatures and ocean reanalyses) and require agreement before any warning is issued. "
     "Step 3: continuously test the method on paleoclimate cases where tipping did and did not happen, to measure the "
     "false-positive rate honestly. Step 4: report distance-to-threshold as a probability distribution, never a date.\n"
     "Assumptions: that tipping elements behave like fold bifurcations with detectable slowing down (true for simple "
     "models, unproven for the real systems); that the chosen observables actually couple to the tipping dynamics; "
     "that the paleoclimate test cases are informative about the present.\n"
     "What would confirm it: an alarm that fires, is independently corroborated, and is followed by the predicted "
     "qualitative shift - or, more usefully, a long verified record of no false alarms alongside correct retrospective "
     "detections of past tippings.\n"
     "What would kill it: alarms that fire repeatedly with no following shift; early-warning statistics shown to be "
     "dominated by data-processing choices; or proof that the real systems tip without the simple bifurcation precursors.\n"
     "What this does NOT claim: it does not claim any tipping point is imminent; it does not claim early-warning "
     "statistics are reliable today; it is not established science and must not be used to set policy dates."),
 "citations": [
     "Lenton T M et al. Tipping elements in the Earths climate system. PNAS; 2008.",
     "IPCC. Climate Change 2021: The Physical Science Basis. WGI, Chapter 4 and 9.",
     "Armstrong McKay D I et al. Exceeding 1.5C warming could trigger multiple tipping points. Science; 2022."],
 "explorer": {
   "blurb": ("A tipping-point toy: a double-well potential model where you can watch the critical forcing at which "
             "one stable state vanishes - the mathematical skeleton of every tipping claim."),
   "assumptions": {"forcing": 0.25},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    Fc = 2.0 / (3.0 * math.sqrt(3.0))\n"
     "    F = A[\"forcing\"]\n"
     "    margin = Fc - F\n"
     "    width = 2.0 * Fc\n"
     "    return {\"critical_forcing\": Fc, \"current_forcing\": F,\n"
     "            \"margin_to_tipping\": margin, \"hysteresis_width\": width}\n"),
   "steps": [("Critical forcing where the state vanishes", "critical_forcing", "units"),
             ("Current forcing", "current_forcing", "units"),
             ("Safety margin to tipping", "margin_to_tipping", "units"),
             ("Hysteresis width (how hard reversal is)", "hysteresis_width", "units")],
   "confirm": ["An alarm fires on pre-registered statistics and the shift follows.",
               "Retrospective tests detect known past tippings without false alarms.",
               "Independent data streams agree on the warning."],
   "refute": ["Alarms fire repeatedly with no shift following.",
              "Statistics are shown to depend on processing choices.",
              "Real systems tip without bifurcation precursors."],
   "checks": [("critical_forcing", 0.38, 0.39), ("margin_to_tipping", 0.1, 0.2),
              ("hysteresis_width", 0.75, 0.8)],
   "honesty": ("Real tipping elements are vastly more complex than one equation. "
               "This toy shows the logic of the claim - a threshold with hysteresis - not the location of any real one."),
 }},
# ---------------------------------------------------------------- 5
{
 "key": "abrupt-past-climate-flips",
 "name": "Why Did Earth's Climate Flip Abruptly in the Past?",
 "group": "Paleoclimate",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": ("Greenland ice cores prove the climate has lurched by many degrees within decades during the last "
             "ice age, but the exact trigger and mechanism of these abrupt flips is still debated."),
 "background": ("The Dansgaard-Oeschger events - about 25 abrupt warmings recorded in Greenland ice during the last "
             "glacial period - are the archetype: temperatures jumped roughly 8 to 15 degrees Celsius in decades, "
             "then relaxed over centuries. Heinrich events added armadas of icebergs to the North Atlantic. The "
             "Younger Dryas, about 12,900 years ago, plunged the warming world back into near-glacial cold for a "
             "millennium. Competing explanations invoke oscillations of the Atlantic overturning circulation, "
             "ice-sheet instabilities dumping freshwater, sea-ice feedbacks, and tropical triggers - and the field "
             "has not converged on one mechanism, in part because different events may have had different causes."),
 "why_it_matters": ("These flips are existence proof that Earth's climate can reorganize far faster than orbital "
             "forcing alone would suggest - exactly the kind of behavior tipping-point science worries about today. "
             "Understanding the trigger tells us which modern observations to watch. It also disciplines climate models: "
             "a model that cannot produce abrupt change may be missing the physics that matters most."),
 "sig_pointer": ("The Signature system proposes a multi-archive fingerprinting program that synchronizes ice, ocean, "
             "and cave records at annual resolution to test competing flip mechanisms against lead-lag patterns. "
             "See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats abrupt past flips as forensic cases - every mechanism must "
             "predict a specific fingerprint in lead-lag timing across archives, and mechanisms are scored against "
             "those fingerprints, not against narrative appeal."),
 "signature_solution": (
     "Proposed approach. Step 1: build annually-resolved, synchronized chronologies across Greenland ice cores, North "
     "Atlantic sediment cores, and speleothems for each major flip, so lead-lag relationships are measured, not assumed. "
     "Step 2: write down, before looking, the fingerprint each candidate mechanism predicts - for example, an AMOC "
     "trigger predicts ocean circulation changes leading Greenland warming, while a sea-ice trigger predicts the reverse. "
     "Step 3: score mechanisms against the fingerprints with explicit uncertainties, allowing the answer 'different "
     "flips, different triggers.' Step 4: demand that the winning mechanism also work in a physics-based model that "
     "produces flips spontaneously, not just when forced.\n"
     "Assumptions: that annual-layer counting and proxy synchronization are accurate enough for lead-lag claims "
     "(good in ice, harder in sediments); that the candidate mechanism list is complete (it may not be); that models "
     "can be fairly tested without tuning them to the answer.\n"
     "What would confirm it: a mechanism whose predicted fingerprint - including which archive leads - matches across "
     "multiple independent flips, and a model that then generates such flips without hand-tuning.\n"
     "What would kill it: lead-lag patterns that contradict every candidate mechanism; synchronization uncertainties "
     "shown to be larger than the claimed leads; or flips that models can only reproduce by prescribing the answer.\n"
     "What this does NOT claim: it does not claim a single cause for all abrupt flips; it does not claim the past "
     "predicts a specific future flip; it is a research program, not an established result."),
 "citations": [
     "Dansgaard W et al. Evidence for general instability of past climate. Nature; 1993.",
     "Alley R B. The Younger Dryas cold interval. Quat Sci Rev; 2000.",
     "Rasmussen S O et al. A stratigraphic framework for abrupt climatic changes. J Geophys Res; 2014."],
 "explorer": {
   "blurb": ("An abrupt-change detector: it builds a synthetic ice-core record with hidden rapid jumps and shows "
             "how a simple threshold detector finds them - the same logic used on real Greenland cores."),
   "assumptions": {"n_points": 2000, "injected_events": 8, "jump": 3.0, "threshold": 1.0},
   "model_src": (
     "def run(A):\n"
     "    n = int(A[\"n_points\"])\n"
     "    events = int(A[\"injected_events\"])\n"
     "    series = [0.02 * i for i in range(n)]\n"
     "    idx = [int((k + 1) * n / (events + 1)) for k in range(events)]\n"
     "    for j in idx:\n"
     "        for i in range(j, n):\n"
     "            series[i] += A[\"jump\"]\n"
     "    diffs = [abs(series[i + 1] - series[i]) for i in range(n - 1)]\n"
     "    detected = sum(1 for d in diffs if d > A[\"threshold\"])\n"
     "    return {\"injected\": float(events), \"detected\": float(detected),\n"
     "            \"detection_rate\": detected / max(events, 1)}\n"),
   "steps": [("Abrupt jumps hidden in the record", "injected", "events"),
             ("Jumps found by the detector", "detected", "events"),
             ("Detection rate", "detection_rate", "")],
   "confirm": ["Detector settings that find synthetic jumps also recover known real events.",
               "Lead-lag fingerprints match one mechanism across several flips.",
               "A physics model generates flips spontaneously with the right statistics."],
   "refute": ["Detector results depend entirely on threshold choices.",
              "Synchronization errors exceed the claimed leads and lags.",
              "No mechanism's fingerprint survives multi-archive testing."],
   "checks": [("detected", 7.0, 9.0), ("detection_rate", 0.9, 1.1)],
   "honesty": ("Finding jumps in a clean synthetic record is easy; real cores have noise, "
               "dating uncertainty, and competing signals. The detector is the easy part."),
 }},
# ---------------------------------------------------------------- 6
{
 "key": "enso-irregularity-forecast",
 "name": "What Makes El Nino Irregular, and Can It Be Forecast Years Ahead?",
 "group": "Oceans",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": ("El Nino events arrive every 2 to 7 years with wildly varying strength, and forecasts lose skill "
             "after about 6 to 9 months - nobody knows whether the irregularity is chaos, noise, or predictable "
             "physics we have not captured."),
 "background": ("The El Nino-Southern Oscillation was unraveled through the 20th century: Walker mapped the "
             "atmospheric seesaw, Bjerknes identified the ocean-atmosphere feedback, and the delayed-oscillator "
             "theory explained the cycle as equatorial waves crossing the Pacific. Yet no two El Ninos are alike - "
             "the 1982-83 and 1997-98 monsters, the modest 2014-16 event, and the triple-dip La Nina of 2020-23 all "
             "defied simple cycle thinking. The 'spring predictability barrier' degrades forecasts made before April, "
             "and while dynamical models are skillful to about 6 to 9 months, experimental multi-year forecasts remain "
             "unproven. Whether the irregularity comes from chaotic nonlinearity, random weather noise, or decadal "
             "background changes is genuinely unsettled."),
 "why_it_matters": ("ENSO is the largest year-to-year climate signal on Earth: it shifts rainfall across the tropics, "
             "drives droughts and floods on several continents, disrupts fisheries worth billions, and nudges global "
             "temperature. A reliable two-year forecast would transform agriculture, water management, and disaster "
             "planning across the tropics. Even understanding the limits of predictability has value - it stops money "
             "chasing impossible skill."),
 "sig_pointer": ("The Signature system proposes a strict out-of-sample forecast tournament combining dynamical "
             "ensembles with learned precursors, scored honestly against the spring barrier. See the Signature "
             "Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats ENSO forecasting as a skill-measurement problem - every "
             "method competes on identical out-of-sample tests, and a method that only works in hindsight is scored "
             "as what it is."),
 "signature_solution": (
     "Proposed approach. Step 1: freeze a 30-year out-of-sample test period that no method may train on, with "
     "forecasts issued on fixed calendar dates to respect the spring barrier. Step 2: enter dynamical model ensembles, "
     "statistical models, and machine-learned precursor methods in one tournament scored by identical metrics "
     "(anomaly correlation, ranked probability scores) at leads from 1 to 24 months. Step 3: decompose each method's "
     "errors to attribute them to initial conditions, model physics, or intrinsic chaos - using perfect-model "
     "experiments to estimate the predictability ceiling. Step 4: publish the leaderboard continuously, retiring "
     "methods that fall below a damped-persistence baseline.\n"
     "Assumptions: that the test period represents the range of ENSO behavior (it may miss rare flavors); that "
     "perfect-model experiments bound real predictability (they assume the model class is adequate); that the "
     "observing system is sufficient for initialization (the tropical Pacific array has gaps).\n"
     "What would confirm it: a method that beats the field consistently across decades and flavors, with error "
     "attribution showing the gains come from physics rather than luck, and multi-year skill that survives the "
     "tournament's out-of-sample discipline.\n"
     "What would kill it: perfect-model experiments showing the ceiling itself is near the current 6-to-9-month "
     "skill - meaning longer forecasts are intrinsically impossible - or learned methods that dominate in-sample "
     "and collapse out-of-sample.\n"
     "What this does NOT claim: it does not claim multi-year ENSO forecasts are possible; it does not claim any "
     "current method has such skill; it is a testing program, not a forecast product."),
 "citations": [
     "McPhaden M J et al. ENSO as an integrating concept in Earth science. Science; 2006.",
     "Barnston A G et al. Skill of real-time seasonal ENSO model predictions. Mon Wea Rev; 2012.",
     "Timmermann A et al. El Nino-Southern Oscillation complexity. Nature; 2018."],
 "explorer": {
   "blurb": ("A forecast-skill decay curve: an autoregressive climate-index model shows how anomaly correlation "
             "falls with lead time - the quantitative shape of the predictability limit."),
   "assumptions": {"phi1": 1.35, "phi2": -0.45, "max_lead": 12},
   "model_src": (
     "def run(A):\n"
     "    phi1 = A[\"phi1\"]\n"
     "    phi2 = A[\"phi2\"]\n"
     "    rho = [1.0, 0.0]\n"
     "    rho[1] = phi1 / (1.0 - phi2)\n"
     "    for k in range(2, int(A[\"max_lead\"]) + 1):\n"
     "        rho.append(phi1 * rho[-1] + phi2 * rho[-2])\n"
     "    cross = next((k for k in range(1, len(rho)) if rho[k] < 0.5), int(A[\"max_lead\"]))\n"
     "    return {\"skill_month1\": rho[1], \"skill_month6\": rho[6],\n"
     "            \"skill_month9\": rho[9], \"crossover_month\": float(cross)}\n"),
   "steps": [("Forecast skill at 1 month lead", "skill_month1", "correlation"),
             ("Forecast skill at 6 months lead", "skill_month6", "correlation"),
             ("Forecast skill at 9 months lead", "skill_month9", "correlation"),
             ("Month where skill drops below 0.5", "crossover_month", "months")],
   "confirm": ["A method beats the field at long leads on frozen out-of-sample tests.",
               "Error attribution shows gains from physics, not luck.",
               "Multi-year skill survives independent replication."],
   "refute": ["Perfect-model tests show the ceiling is near current skill.",
              "Learned methods collapse out-of-sample.",
              "Long-lead skill traces to a few lucky events."],
   "checks": [("skill_month1", 0.85, 0.98), ("skill_month6", 0.25, 0.45), ("crossover_month", 3.0, 8.0)],
   "honesty": ("This is a statistical toy, not the tropical Pacific. It shows the shape of "
               "skill decay - the real question is where the true ceiling sits."),
 }},
# ---------------------------------------------------------------- 7
{
 "key": "permafrost-carbon-release",
 "name": "How Much Carbon Will Thawing Permafrost Release?",
 "group": "Climate",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": ("Permafrost soils hold roughly twice the carbon in the atmosphere, and nobody knows how much of it "
             "will escape as the Arctic thaws - or how much will come out as methane, which warms far more per ton."),
 "background": ("Northern permafrost stores on the order of 1,500 billion tons of carbon, accumulated over tens of "
             "thousands of years and locked in frozen ground. As the Arctic warms - roughly four times faster than the "
             "global average - that ground thaws, and microbes wake up to decompose ancient organic matter into carbon "
             "dioxide and methane. Most climate models include only gradual top-down thaw, missing abrupt processes "
             "like thermokarst lake formation and hillslope collapse that can release carbon much faster. The IPCC "
             "Sixth Assessment acknowledged the permafrost feedback as real but not fully quantified, leaving it partly "
             "outside the carbon budgets used for temperature targets."),
 "why_it_matters": ("If permafrost releases 100 billion tons of carbon this century, that is a decade of current "
             "human emissions added on top - and it is largely irreversible on human timescales. Carbon budgets for "
             "1.5 or 2 degrees of warming may already be spent if the feedback is large. Knowing the magnitude decides "
             "how fast human emissions must fall to hold any temperature target."),
 "sig_pointer": ("The Signature system proposes a pan-Arctic monitoring and process-model ensemble that includes "
             "abrupt thaw and partitions carbon dioxide from methane with explicit uncertainty. See the Signature "
             "Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats permafrost carbon as an inventory problem with live "
             "updating - every new thaw observation revises the release curve, and methane is never folded silently "
             "into carbon-dioxide equivalents."),
 "signature_solution": (
     "Proposed approach. Step 1: complete the pan-Arctic carbon inventory with depth-resolved soil cores, including "
     "carbon-rich Yedoma deposits, so the 'how much is there' question is answered by measurement, not extrapolation. "
     "Step 2: run a process-model ensemble that includes abrupt thaw - thermokarst, lake drainage, coastal erosion - "
     "alongside gradual thaw, with each process module scored against field sites. Step 3: partition releases into "
     "carbon dioxide and methane explicitly, tracking methane's higher near-term warming separately. Step 4: update "
     "the release curve annually from the monitoring network, publishing the full uncertainty cascade from inventory "
     "to decomposition rates to climate feedback.\n"
     "Assumptions: that the inventory can be completed representatively across Siberia, Alaska, and Canada (logistics "
     "are hard); that abrupt-thaw processes can be parameterized well enough to matter (early days); that decomposition "
     "rates measured in labs and field plots scale to landscapes (uncertain).\n"
     "What would confirm it: the ensemble's release curve verified against decade-scale atmospheric inversions over "
     "the Arctic, convergence of independent inventory methods, and methane fractions matching tall-tower observations.\n"
     "What would kill it: deep carbon stocks shown to be far smaller or far more recalcitrant than assumed; abrupt "
     "thaw shown to expose little new carbon; or atmospheric data contradicting the modeled release trajectory.\n"
     "What this does NOT claim: it does not claim a specific release number today; it does not claim permafrost alone "
     "decides warming targets; it is not established carbon-cycle science and is not a basis for revising budgets."),
 "citations": [
     "Tarnocai C et al. Soil organic carbon pools in the northern circumpolar permafrost region. Global Biogeochem Cycles; 2009.",
     "Schuur E A G et al. Climate change and the permafrost carbon feedback. Nature; 2015.",
     "IPCC. Climate Change 2021: The Physical Science Basis. WGI, Chapter 5 (carbon cycle)."],
 "explorer": {
   "blurb": ("A permafrost release calculator: from the soil carbon pool, a thaw sensitivity, and warming, it "
             "integrates the century-scale release and its carbon-dioxide equivalent."),
   "assumptions": {"pool_GtC": 1500, "release_fraction_per_C": 0.02, "warming_C": 3.0},
   "model_src": (
     "def run(A):\n"
     "    released = A[\"pool_GtC\"] * A[\"release_fraction_per_C\"] * A[\"warming_C\"]\n"
     "    ppm = released / 2.13\n"
     "    return {\"pool_GtC\": float(A[\"pool_GtC\"]), \"released_GtC\": released,\n"
     "            \"co2_ppm_equiv\": ppm}\n"),
   "steps": [("Permafrost soil carbon pool", "pool_GtC", "GtC"),
             ("Released this century (illustrative)", "released_GtC", "GtC"),
             ("Carbon-dioxide equivalent", "co2_ppm_equiv", "ppm")],
   "confirm": ["Modeled releases verify against Arctic atmospheric inversions.",
               "Independent inventories converge on the pool size.",
               "Methane fractions match tall-tower observations."],
   "refute": ["Deep stocks prove smaller or more recalcitrant than assumed.",
              "Abrupt thaw exposes little new carbon.",
              "Atmospheric data contradict the modeled trajectory."],
   "checks": [("released_GtC", 60.0, 130.0), ("co2_ppm_equiv", 25.0, 65.0)],
   "honesty": ("The pool is measured; the release fraction is the unknown. "
               "Change the sensitivity and watch the answer swing - that swing is the science gap."),
 }},
# ---------------------------------------------------------------- 8
{
 "key": "amoc-collapse-risk",
 "name": "Is the Atlantic Overturning Circulation Heading for Collapse?",
 "group": "Oceans",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": ("The Atlantic overturning circulation may be weakening, and some analyses claim early-warning signals "
             "of collapse - but the evidence is contested, the observations are short, and the stakes are enormous."),
 "background": ("The Atlantic Meridional Overturning Circulation carries warm surface water north and cold deep water "
             "south, warming Europe by several degrees and influencing tropical rainfall and US East Coast sea level. "
             "Stommel showed in 1961 that such a circulation can be bistable - a strong mode and a collapsed mode - "
             "with freshwater from melting ice able to push it over the edge. Direct measurements from the RAPID array "
             "began only in 2004, too short to settle trends. Proxy studies have argued for a decades-long weakening, "
             "and a 2023 analysis claimed early-warning signals pointing to collapse mid-century - a claim other "
             "researchers sharply disputed, arguing the statistics were fragile and the proxies unreliable."),
 "why_it_matters": ("An AMOC collapse would cool the North Atlantic region even as the world warms, shift tropical "
             "rain belts, accelerate sea-level rise along the US East Coast, and disrupt marine ecosystems. It is the "
             "tipping element closest to direct human consequence. But a false collapse alarm would damage trust in "
             "climate science for a generation - so the standard of evidence must be extremely high."),
 "sig_pointer": ("The Signature system proposes sustained direct observation plus pre-registered early-warning criteria "
             "that must be met on independent data streams before any warning is issued. See the Signature Edition "
             "record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats AMOC collapse risk as a measurement problem first - no "
             "warning without direct observations, no statistics without pre-registration, no single proxy carrying "
             "the claim alone."),
 "signature_solution": (
     "Proposed approach. Step 1: extend and harden direct AMOC observations - the RAPID array and its successors - "
     "with a commitment to multi-decade continuity, because no proxy debate can substitute for measurement. Step 2: "
     "pre-register the early-warning criteria (which statistics, which thresholds, which independent streams must agree) "
     "before evaluating them, ending the era of post-hoc alarm claims. Step 3: validate every proposed fingerprint "
     "against both the direct record and long model control runs to measure false-positive rates. Step 4: maintain a "
     "living, versioned assessment of collapse probability that moves only when pre-registered criteria are met.\n"
     "Assumptions: that sustained funding for ocean observation continues (a political assumption); that the "
     "circulation's bistability in simple models carries over to the full system (unproven); that pre-registered "
     "criteria can be agreed across a divided field (socially hard).\n"
     "What would confirm it: pre-registered warning statistics firing on the direct observational record, corroborated "
     "by independent fingerprints, with models showing the same precursors before simulated collapses.\n"
     "What would kill it: the direct record showing stable or recovering overturning over coming decades; proposed "
     "fingerprints failing validation against models and independent data; early-warning statistics with false-positive "
     "rates near 100%.\n"
     "What this does NOT claim: it does not claim collapse is imminent or impossible; it does not endorse any published "
     "collapse date; it is not established oceanography and must not drive policy timelines."),
 "citations": [
     "Stommel H. Thermohaline convection with two stable regimes of flow. Tellus; 1961.",
     "Caesar L et al. Observed fingerprint of a weakening Atlantic overturning. Nature; 2018.",
     "RAPID-AMOC programme: continuous transatlantic observations since 2004."],
 "explorer": {
   "blurb": ("A Stommel two-box ocean: it computes the overturning strength versus freshwater forcing and finds the "
             "fold point where the strong circulation collapses - the classic bistability behind collapse worries."),
   "assumptions": {"k": 18.0, "alpha_dT": 1.0, "beta": 15.0, "c": 0.75, "H_forcing": 0.15},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    k = A[\"k\"]\n"
     "    aT = A[\"alpha_dT\"]\n"
     "    b = A[\"beta\"]\n"
     "    c = A[\"c\"]\n"
     "    Hc = k * aT * aT / (4.0 * b * c)\n"
     "    H = A[\"H_forcing\"]\n"
     "    margin = Hc - H\n"
     "    disc = (k * aT) ** 2 - 4.0 * k * b * c * H\n"
     "    q = (k * aT + math.sqrt(disc)) / 2.0 if disc > 0 else 0.0\n"
     "    return {\"critical_H\": Hc, \"current_H\": H,\n"
     "            \"margin\": margin, \"overturning_Sv\": q}\n"),
   "steps": [("Critical freshwater forcing (fold point)", "critical_H", "Sv"),
             ("Current freshwater forcing", "current_H", "Sv"),
             ("Safety margin to the fold", "margin", "Sv"),
             ("Overturning strength", "overturning_Sv", "Sv")],
   "confirm": ["Pre-registered warnings fire on the direct RAPID record.",
               "Independent fingerprints agree with the warning.",
               "Models show the same precursors before simulated collapses."],
   "refute": ["Direct observations show stable or recovering overturning.",
              "Fingerprints fail validation against models and independent data.",
              "Warning statistics show near-total false-positive rates."],
   "checks": [("critical_H", 0.35, 0.45), ("overturning_Sv", 14.0, 18.0), ("margin", 0.2, 0.3)],
   "honesty": ("Stommel's boxes are a cartoon of the Atlantic. The bistability is real mathematics; "
               "whether the real ocean sits near the fold is the unanswered question."),
 }},
# ---------------------------------------------------------------- 9
{
 "key": "geomagnetic-reversal-mechanism",
 "name": "Why Does Earths Magnetic Field Reverse, and When Is Next?",
 "group": "Geomagnetism",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": ("Earth's magnetic field has reversed hundreds of times, the last full reversal was 780,000 years ago, "
             "and the field is weakening now - but nobody knows what triggers reversals or whether one is coming."),
 "background": ("The geomagnetic field is generated by the geodynamo - convecting liquid iron in the outer core - "
             "and the paleomagnetic record shows it has flipped polarity hundreds of times, irregularly, averaging "
             "every 200,000 to 300,000 years over the last 10 million years, with long quiet 'superchrons' of tens of "
             "millions of years with no reversals at all. The last full reversal, Brunhes-Matuyama, was about 780,000 "
             "years ago - longer than the recent average interval. The field's strength has declined roughly 9% per "
             "century over the last 200 years, and the South Atlantic Anomaly - a weak patch where the field is "
             "unusually low - is growing. Some researchers read this as the opening act of a reversal; others note "
             "that similar declines have reversed themselves before, and geodynamo simulations produce both behaviors."),
 "why_it_matters": ("During a reversal, which takes thousands of years, the field becomes weak and multipolar, "
             "offering less shielding against cosmic radiation - with implications for satellites, power grids, and "
             "possibly the atmosphere. Navigation systems assume the current field geometry. More fundamentally, "
             "reversals are the most dramatic known behavior of a planetary dynamo, and understanding them would "
             "unlock the physics of Earth's core - and of magnetic fields on other planets."),
 "sig_pointer": ("The Signature system proposes data-assimilation geodynamo modeling combined with a global "
             "paleointensity database to test whether the current decline is a reversal precursor or normal "
             "variation. See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats reversals as a dynamo-dynamics problem - the question is "
             "not 'when' but 'what measurable state of the core precedes a reversal,' tested in models that must "
             "earn their predictions against the paleomagnetic record."),
 "signature_solution": (
     "Proposed approach. Step 1: build an open, quality-ranked global paleointensity database covering the last 10 "
     "million years, so reversal statistics rest on data anyone can audit. Step 2: run data-assimilation geodynamo "
     "models - models continuously corrected by the observed field - and catalog which internal core states precede "
     "simulated reversals. Step 3: test whether the present field, including the South Atlantic Anomaly, matches any "
     "pre-reversal state in the model catalog, with explicit false-positive rates from model history. Step 4: publish "
     "a living reversal-probability assessment that updates as models and data improve, never as a date.\n"
     "Assumptions: that geodynamo models capture the real reversal physics (they reproduce reversals qualitatively, "
     "not quantitatively); that the paleointensity database is representative (sampling is sparse and uneven); that "
     "pre-reversal states are distinguishable from normal secular variation (unknown).\n"
     "What would confirm it: models that hindcast past reversals from pre-reversal states with skill above chance, and "
     "the present field matching a high-skill precursor state across independent model families.\n"
     "What would kill it: models whose 'precursors' fire constantly with no reversals following; the present decline "
     "reversing itself as it has before; or proof that reversals are intrinsically stochastic with no observable precursor.\n"
     "What this does NOT claim: it does not claim a reversal is coming; it does not claim the current decline is "
     "anomalous; it is not established geomagnetism and must not be used for infrastructure planning dates."),
 "citations": [
     "Valet J P. Time variations in geomagnetic intensity. Rev Geophys; 2003.",
     "Glatzmaier G A, Roberts P H. A three-dimensional self-consistent computer simulation of a geomagnetic reversal. Nature; 1995.",
     "Thébault E et al. International Geomagnetic Reference Field (IGRF-13). Earth Planets Space; 2021."],
 "explorer": {
   "blurb": ("A reversal-statistics check: from a list of intervals between past reversals it computes the mean "
             "interval and the coefficient of variation - testing whether reversals look like a random Poisson "
             "process or a clock."),
   "assumptions": {"intervals_Myr": [0.18, 0.42, 0.11, 0.33, 0.25, 0.52, 0.09, 0.29, 0.37, 0.16, 0.44, 0.21]},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    iv = list(A[\"intervals_Myr\"])\n"
     "    n = len(iv)\n"
     "    mean = sum(iv) / n\n"
     "    var = sum((x - mean) ** 2 for x in iv) / n\n"
     "    cv = math.sqrt(var) / mean\n"
     "    return {\"n_intervals\": float(n), \"mean_Myr\": mean,\n"
     "            \"cv\": cv, \"rate_per_Myr\": 1.0 / mean}\n"),
   "steps": [("Reversal intervals analyzed", "n_intervals", "intervals"),
             ("Mean interval between reversals", "mean_Myr", "Myr"),
             ("Coefficient of variation (1 = Poisson-like)", "cv", ""),
             ("Mean reversal rate", "rate_per_Myr", "per Myr")],
   "confirm": ["Models hindcast past reversals from precursor states with real skill.",
               "The present field matches a precursor state across model families.",
               "Reversal statistics prove non-random and model-predictable."],
   "refute": ["Model precursors fire constantly with no reversals following.",
              "The current decline reverses itself as before.",
              "Reversals prove intrinsically stochastic with no observable precursor."],
   "checks": [("mean_Myr", 0.2, 0.4), ("cv", 0.35, 0.6), ("n_intervals", 11.0, 13.0)],
   "honesty": ("A coefficient of variation well below 1 means these synthetic intervals are more regular "
               "than a Poisson process - real reversal intervals are debated, which is exactly why "
               "predicting the next one is so hard."),
 }},
]
# ---------------------------------------------------------------- 10
ENTRIES.append({
 "key": "deep-focus-earthquakes",
 "name": "What Causes Deep-Focus Earthquakes?",
 "group": "Seismology",
 "ladder_rank": 10, "ladder_tier": "compounded",
 "problem": ("Earthquakes occur as deep as 700 kilometers, inside hot high-pressure mantle where rock should flow "
             "rather than fracture - and the mechanism that lets them happen is still not settled."),
 "background": ("Shallow earthquakes are understood: brittle rock breaks when stress exceeds friction. But below "
             "about 300 kilometers, pressure and temperature should make rock deform smoothly, yet seismometers "
             "record powerful quakes - including the 2013 Sea of Okhotsk magnitude 8.3 at 609 kilometers depth, the "
             "largest deep event ever recorded. Three mechanisms compete: transformational faulting, where metastable "
             "olivine collapses to a denser crystal structure inside cold sinking slabs; thermal shear instability, "
             "where deformation heats the rock and weakens it in runaway feedback; and dehydration embrittlement, "
             "where water released from minerals raises pore pressure. Each explains some observations and fails "
             "others, and the deepest quakes - below 600 kilometers, where even metastable olivine should be gone - "
             "challenge all three."),
 "why_it_matters": ("Deep earthquakes are probes of sinking tectonic plates: their locations map slab shapes, their "
             "mechanisms reveal mineral physics at otherwise unreachable conditions, and their cutoff depths constrain "
             "slab temperatures. The 2013 Okhotsk event released as much energy as a great shallow quake with a "
             "completely different rupture physics - understanding it means understanding the deep Earth itself."),
 "sig_pointer": ("The Signature system proposes a joint mineral-physics and seismology test: predict the depth "
             "distribution of metastable mineral wedges from slab thermal models and compare against observed deep "
             "seismicity cutoffs. See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats deep earthquakes as a prediction contest between "
             "mechanisms - each must forecast where deep seismicity should stop, and the data referee."),
 "signature_solution": (
     "Proposed approach. Step 1: for every subduction zone with deep seismicity, compute slab thermal models to map "
     "where olivine should persist metastably, where dehydration reactions occur, and where shear heating could "
     "run away - producing three distinct predicted seismicity patterns. Step 2: compare the predictions against "
     "high-resolution earthquake catalogs, scoring each mechanism on depth distribution, maximum magnitude, and "
     "aftershock behavior. Step 3: test the winning patterns in high-pressure laboratory deformation experiments on "
     "realistic mineral assemblages. Step 4: require the surviving mechanism to also explain the ultra-deep events "
     "below 600 kilometers, or admit a fourth mechanism is needed.\n"
     "Assumptions: that slab thermal models are accurate enough to locate reaction boundaries (uncertain by tens of "
     "kilometers); that laboratory strain rates can be extrapolated to geological ones (a notorious gap); that "
     "catalogs are complete at depth (improving but uneven).\n"
     "What would confirm it: one mechanism's predicted depth cutoffs and magnitude limits matching observations across "
     "many slabs, with laboratory experiments reproducing the same rupture physics.\n"
     "What would kill it: depth distributions that match no mechanism's prediction; lab experiments showing none of "
     "the proposed instabilities operate at slab conditions; or ultra-deep events requiring physics outside all three "
     "candidates.\n"
     "What this does NOT claim: it does not claim any one mechanism is correct today; it does not claim deep "
     "earthquakes are predictable; it is a research program, not an established result."),
 "citations": [
     "Frohlich C. Deep Earthquakes. Cambridge University Press; 2006.",
     "Zhan Z et al. Rupture complexity of the 2013 Okhotsk deep earthquake. Science; 2014.",
     "Kirby S H et al. Mantle phase changes and deep-earthquake faulting. Rev Geophys; 1996."],
 "explorer": {
   "blurb": ("A metastable-wedge estimator: from the Clapeyron slope and a slab's cold temperature anomaly it "
             "computes how much extra pressure metastable olivine can sustain - the fuel proposed for deep quakes."),
   "assumptions": {"clapeyron_MPa_K": 2.5, "slab_temp_anomaly_K": 400.0, "rho": 3300.0, "g": 9.81},
   "model_src": (
     "def run(A):\n"
     "    dP_MPa = A[\"clapeyron_MPa_K\"] * A[\"slab_temp_anomaly_K\"]\n"
     "    dP_Pa = dP_MPa * 1.0e6\n"
     "    dz_m = dP_Pa / (A[\"rho\"] * A[\"g\"])\n"
     "    return {\"metastable_pressure_MPa\": dP_MPa,\n"
     "            \"equivalent_depth_shift_km\": dz_m / 1000.0}\n"),
   "steps": [("Extra pressure from cold anomaly", "metastable_pressure_MPa", "MPa"),
             ("Equivalent depth shift of the phase boundary", "equivalent_depth_shift_km", "km")],
   "confirm": ["Predicted metastable-wedge locations match deep seismicity cutoffs across slabs.",
               "Lab experiments reproduce transformational faulting at slab conditions.",
               "Ultra-deep events fit an extended mechanism, not an exception."],
   "refute": ["Depth distributions match no mechanism's prediction.",
              "Lab work shows the instabilities cannot operate at slab conditions.",
              "Cutoffs trace to catalog incompleteness, not physics."],
   "checks": [("metastable_pressure_MPa", 800.0, 1200.0), ("equivalent_depth_shift_km", 25.0, 38.0)],
   "honesty": ("A cold slab shifts mineral reactions deeper - the arithmetic is simple. "
               "Whether that shift actually causes earthquakes is the open question."),
 }})
# ---------------------------------------------------------------- 11
ENTRIES.append({
 "key": "slow-slip-tremor",
 "name": "What Drives Slow Earthquakes and Tremor?",
 "group": "Seismology",
 "ladder_rank": 11, "ladder_tier": "compounded",
 "problem": ("Faults can slip slowly over weeks, releasing the energy of a large earthquake with no shaking - and "
             "the physics that decides between silent creep, slow slip, and violent rupture is not fully understood."),
 "background": ("In the early 2000s, geodetic networks in Cascadia and Japan revealed 'episodic tremor and slip': "
             "the plate boundary slipping centimeters over weeks, accompanied by faint seismic tremor, with no "
             "felt earthquake. Slow slip events are now documented worldwide, from Hikurangi to Costa Rica, some "
             "equivalent to magnitude 7 earthquakes unfolding over months. Rate-and-state friction theory says the "
             "outcome depends on whether the fault is velocity-weakening (unstable, earthquakes) or velocity-"
             "strengthening (stable, creep) - with slow slip living in the conditionally stable borderland. But what "
             "sets a fault patch's frictional properties - fluids, temperature, mineralogy - and whether slow slip "
             "loads or relieves the locked zone that produces megathrust earthquakes, remain open questions."),
 "why_it_matters": ("Slow slip happens on the same subduction zones that produce magnitude 9 megathrust earthquakes. "
             "If slow slip loads the locked zone, it is a hazard signal; if it relieves stress, it is a safety valve - "
             "and we do not know which. Understanding the frictional spectrum from creep to seismic slip is also the "
             "key to the earthquake prediction problem, since nucleation may pass through a slow phase."),
 "sig_pointer": ("The Signature system proposes dense seafloor geodesy plus laboratory friction measured at in-situ "
             "conditions to map the stability spectrum of real faults. See the Signature Edition record for the full "
             "labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats slow slip as a friction-mapping problem - measure the "
             "stability field of a real fault the way you would map ore, then watch whether the map predicts "
             "behavior."),
 "signature_solution": (
     "Proposed approach. Step 1: deploy seafloor geodetic networks - pressure sensors and acoustic ranging - above "
     "the offshore locked zones where slow slip is suspected but land instruments cannot see. Step 2: measure "
     "friction laws in the laboratory on real fault-zone rocks at in-situ pressure, temperature, and fluid "
     "conditions, mapping the velocity-weakening to velocity-strengthening transition. Step 3: combine the maps "
     "into physics-based cycle models that must reproduce the observed slow-slip recurrence intervals before being "
     "trusted. Step 4: test whether modeled stress transfer from slow slip correlates with subsequent seismicity, "
     "with pre-registered statistical tests.\n"
     "Assumptions: that laboratory friction scales to natural faults (the scale gap is the field's central worry); "
     "that seafloor geodesy can achieve the needed precision offshore (demonstrated in pilots, not yet routine); "
     "that the frictional framework is the right language at all (competing views invoke fluids and dilatancy).\n"
     "What would confirm it: cycle models built from lab-measured friction that predict slow-slip timing on a new "
     "subduction zone before it is observed, and a measured correlation between slow slip and locked-zone stressing "
     "in the predicted direction.\n"
     "What would kill it: lab friction failing to predict field behavior; slow slip shown to be uncorrelated with "
     "later seismicity; or the stability framework replaced by evidence that fluids, not friction, control the spectrum.\n"
     "What this does NOT claim: it does not claim slow slip predicts big earthquakes; it does not claim the "
     "friction framework is complete; it is a research program, not an established result."),
 "citations": [
     "Obara K. Nonvolcanic deep tremor associated with subduction. Science; 2002.",
     "Scholz C H. The Mechanics of Earthquakes and Faulting. 3rd ed. Cambridge; 2019.",
     "Bürgmann R. The geophysics, geology and mechanics of slow fault slip. Earth Planet Sci Lett; 2018."],
 "explorer": {
   "blurb": ("A friction-stability calculator: from rate-and-state parameters it computes the critical stiffness "
             "that separates stable creep from slow slip from earthquakes."),
   "assumptions": {"b_minus_a": 0.004, "sigma_MPa": 100.0, "Dc_m": 0.0001, "stiffness_Pa_m": 1.0e9},
   "model_src": (
     "def run(A):\n"
     "    kc = A[\"b_minus_a\"] * (A[\"sigma_MPa\"] * 1.0e6) / A[\"Dc_m\"]\n"
     "    k = A[\"stiffness_Pa_m\"]\n"
     "    ratio = k / kc\n"
     "    return {\"critical_stiffness_MPa_m\": kc / 1.0e6,\n"
     "            \"fault_stiffness_MPa_m\": k / 1.0e6,\n"
     "            \"stability_ratio\": ratio}\n"),
   "steps": [("Critical stiffness (stability boundary)", "critical_stiffness_MPa_m", "MPa/m"),
             ("Fault-zone stiffness", "fault_stiffness_MPa_m", "MPa/m"),
             ("Stability ratio (<1 favors slow/unstable slip)", "stability_ratio", "")],
   "confirm": ["Lab-calibrated models predict slow-slip timing on a new subduction zone.",
               "Stress transfer from slow slip correlates with later seismicity as predicted.",
               "Stability maps match observed slip behavior patch by patch."],
   "refute": ["Lab friction fails to predict field behavior.",
              "Slow slip proves uncorrelated with later seismicity.",
              "Fluids, not friction, are shown to control the slip spectrum."],
   "checks": [("critical_stiffness_MPa_m", 3000.0, 5000.0), ("stability_ratio", 0.1, 0.5)],
   "honesty": ("Rate-and-state is the best language the field has for fault friction - "
               "but whether nature speaks it fluently at field scale is unproven."),
 }})
# ---------------------------------------------------------------- 12
ENTRIES.append({
 "key": "plate-tectonics-origin",
 "name": "How and When Did Plate Tectonics Begin?",
 "group": "Geodynamics",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": ("Earth is the only known planet with plate tectonics, and geologists cannot agree when it started - "
             "estimates span from over 4 billion years ago to under 1 billion."),
 "background": ("Plate tectonics - rigid plates created at ridges and destroyed in subduction zones - drives "
             "earthquakes, builds continents, and regulates climate through the carbon cycle. Yet its origin is "
             "mysterious: Venus and Mars, similar in size and composition, never developed it. Proposed start dates "
             "cover nearly all of Earth history: Hadean zircon crystals hint at subduction-like chemistry before 4 "
             "billion years ago, while the first unambiguous ophiolites (slices of ocean floor) and blueschists "
             "(high-pressure, low-temperature rocks diagnostic of subduction) appear around 1 billion years ago or "
             "later. Competing models invoke a hotter early Earth with weak plates, episodic overturns, or a late "
             "trigger such as mantle cooling past a critical point or damage accumulation weakening the lithosphere."),
 "why_it_matters": ("Plate tectonics may be why Earth stayed habitable: it recycles carbon, builds continents, and "
             "drives the magnetic field's long-term evolution. If we do not know what started it here, we cannot "
             "predict which exoplanets have it - and the search for habitable worlds depends on that prediction. It "
             "is also the boundary condition for all of early Earth science, from the origin of life to the first "
             "continents."),
 "sig_pointer": ("The Signature system proposes an integrated onset test combining thermal history, the rock record, "
             "and damage-rheology models with observable onset criteria defined in advance. See the Signature Edition "
             "record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats tectonic onset as a threshold problem - define the "
             "measurable criteria for 'plate tectonics' first, then let thermal models and rocks vote on when the "
             "threshold was crossed."),
 "signature_solution": (
     "Proposed approach. Step 1: define observable onset criteria in advance - for example, the joint appearance of "
     "paired metamorphic belts, linear accretionary margins, and systematic plate-motion reconstructions - so the "
     "start date is a measurement, not a definition dispute. Step 2: run thermal-history models with damage rheology, "
     "where deformation weakens the lithosphere and healing restrengthens it, to find when mobile-lid behavior becomes "
     "self-sustaining. Step 3: confront the model timelines with the rock record - zircons, ophiolites, blueschists, "
     "TTG suites - scoring each proposed onset date against all proxies simultaneously. Step 4: test the framework "
     "against Venus and Mars, which must come out non-tectonic for the right physical reasons, not by tuning.\n"
     "Assumptions: that the onset criteria capture the essence of plate tectonics (debatable); that damage rheology "
     "is the key missing physics (one candidate among several); that the rock record's absence of evidence is not "
     "merely preservation bias (the field's chronic worry).\n"
     "What would confirm it: model onset dates converging with multi-proxy rock evidence at one date, and the same "
     "physics correctly predicting stagnant lids on Venus and Mars.\n"
     "What would kill it: proxies scattering across billions of years with no convergence; models that produce "
     "tectonics on Venus too; or proof that the 'onset' was gradual and the question itself is ill-posed.\n"
     "What this does NOT claim: it does not claim a specific start date today; it does not claim Earth-like planets "
     "must develop tectonics; it is a research program, not an established result."),
 "citations": [
     "Korenaga J. Initiation and evolution of plate tectonics. Annu Rev Earth Planet Sci; 2013.",
     "Stern R J. The evolution of plate tectonics. Phil Trans R Soc A; 2018.",
     "Brown M et al. The tectonic framework of the early Earth. Nat Rev Earth Environ; 2020."],
 "explorer": {
   "blurb": ("A tectonic-onset toy: one hypothesis class says plate tectonics needs a Goldilocks mantle - "
             "hot enough for vigorous convection, cool enough for strong plates. The model cools the mantle "
             "over billions of years and finds when Earth entered that window."),
   "assumptions": {"Tp_now": 1350.0, "dT": 600.0, "tau_Gyr": 3.0, "T_lo": 1400.0, "T_hi": 1700.0},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    tau = A[\"tau_Gyr\"]\n"
     "    def Tp(t):\n"
     "        return A[\"Tp_now\"] + A[\"dT\"] * (1.0 - math.exp(-t / tau))\n"
     "    onset = None\n"
     "    t = 4.5\n"
     "    while t >= 0.0:\n"
     "        if A[\"T_lo\"] <= Tp(t) <= A[\"T_hi\"] and onset is None:\n"
     "            onset = t\n"
     "        t -= 0.01\n"
     "    return {\"onset_Ga\": onset if onset is not None else -1.0,\n"
     "            \"Tp_at_onset_C\": Tp(onset) if onset is not None else 0.0,\n"
     "            \"Tp_now_C\": Tp(0.0),\n"
     "            \"window_width_C\": A[\"T_hi\"] - A[\"T_lo\"]}\n"),
   "steps": [("Time before present Earth entered the tectonic window", "onset_Ga", "Ga"),
             ("Mantle temperature at onset", "Tp_at_onset_C", "C"),
             ("Mantle temperature today", "Tp_now_C", "C"),
             ("Window width", "window_width_C", "C")],
   "confirm": ["Model onset dates converge with multi-proxy rock evidence.",
               "The same physics predicts stagnant lids on Venus and Mars.",
               "New proxies narrow, not widen, the onset window."],
   "refute": ["Proxies scatter across billions of years with no convergence.",
              "Models produce tectonics on Venus too.",
              "Onset proves gradual and the question ill-posed."],
   "checks": [("onset_Ga", 2.0, 3.5), ("Tp_at_onset_C", 1650.0, 1750.0), ("Tp_now_C", 1340.0, 1360.0)],
   "honesty": ("A Goldilocks window is one hypothesis class among several - and the window edges are "
               "guesses. The demo shows the logic: a temperature-dependent window becomes a date."),
 }})
# ---------------------------------------------------------------- 13
ENTRIES.append({
 "key": "continent-growth",
 "name": "How Did the Continents Grow?",
 "group": "Geodynamics",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": ("Continents grew in dramatic pulses billions of years ago, but how much was brand-new crust from the "
             "mantle versus recycled older crust is still disputed - so the true growth curve of the continents is "
             "unknown."),
 "background": ("Continental crust covers about 40% of Earth's surface, is billions of years old on average, and "
             "hosts nearly all mineral resources and terrestrial life. Age compilations show most of it formed in "
             "pulses - around 2.7, 1.9, and 1.2 billion years ago. But ages record when crust last melted, not when "
             "it first left the mantle: reworking of old crust looks identical to new growth in simple age maps. "
             "Hafnium isotopes in zircons can distinguish juvenile from recycled crust, and different research groups "
             "reading the same data have produced growth curves ranging from 'most continents formed early' to "
             "'continents grew steadily and recently.' Preservation bias - young crust is simply more likely to "
             "survive - haunts every interpretation."),
 "why_it_matters": ("Continents are where we live and mine: their growth history records the thermal evolution of "
             "the planet and the onset of the processes that concentrate ores. The growth curve is also a boundary "
             "condition for the carbon cycle and climate over billions of years. Getting it right separates what the "
             "mantle produced from what plate tectonics merely rearranged."),
 "sig_pointer": ("The Signature system proposes a global zircon hafnium-isotope compilation with explicit reworking "
             "correction and preservation-bias modeling to invert the true growth curve. See the Signature Edition "
             "record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats continent growth as a signal-separation problem - "
             "juvenile addition versus reworking, with preservation bias modeled explicitly instead of argued about."),
 "signature_solution": (
     "Proposed approach. Step 1: compile all published zircon uranium-lead ages with hafnium isotopes into one open "
     "database with uniform quality filters, ending the era of each group using its own selection. Step 2: apply an "
     "explicit preservation-bias model - crust of each age has a survival probability - and invert for the juvenile "
     "addition rate through time, with full uncertainty propagation. Step 3: cross-check the inverted growth curve "
     "against independent constraints: mantle depletion records, sea-level history, and thermal models. Step 4: "
     "publish the inversion code so any new dataset can update the curve automatically.\n"
     "Assumptions: that zircon hafnium faithfully records juvenile versus recycled sources (broadly true, noisy in "
     "detail); that preservation bias can be modeled rather than merely feared (attempted, never settled); that the "
     "compiled database is representative (sampling favors accessible continents).\n"
     "What would confirm it: the inverted growth curve converging as new data arrive, agreement with mantle "
     "depletion independent of zircons, and successful prediction of crustal age patterns in newly mapped regions.\n"
     "What would kill it: inversions that swing wildly with each new dataset; preservation bias shown to be "
     "unmodelable from available data; or hafnium systematics shown to misidentify reworking at scale.\n"
     "What this does NOT claim: it does not claim a specific growth curve today; it does not claim any published "
     "curve is wrong; it is a research program, not an established result."),
 "citations": [
     "Hawkesworth C J et al. The generation and evolution of the continental crust. J Geol Soc; 2010.",
     "Dhuime B et al. A change in the geodynamics of continental growth 3 billion years ago. Science; 2012.",
     "Condie K C, Aster R C. Episodic zircon age spectra. Precambrian Res; 2010."],
 "explorer": {
   "blurb": ("A crustal-growth curve fitter: a logistic growth model shows how the present-day fraction of "
             "continents depends on growth timing - the shape every juvenile-vs-reworking debate is about."),
   "assumptions": {"k_per_Gyr": 1.2, "midpoint_Gyr": 2.0, "earth_age_Gyr": 4.5},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    k = A[\"k_per_Gyr\"]\n"
     "    tm = A[\"midpoint_Gyr\"]\n"
     "    T = A[\"earth_age_Gyr\"]\n"
     "    present = 1.0 / (1.0 + math.exp(-k * (T - tm)))\n"
     "    at_25 = 1.0 / (1.0 + math.exp(-k * (2.0 - tm)))\n"
     "    return {\"fraction_today\": present, \"fraction_at_2_5Ga\": at_25,\n"
     "            \"growth_rate\": k}\n"),
   "steps": [("Modeled continental fraction today", "fraction_today", ""),
             ("Modeled fraction already grown by 2.5 Ga", "fraction_at_2_5Ga", ""),
             ("Growth rate parameter", "growth_rate", "per Gyr")],
   "confirm": ["Inverted growth curves converge as new zircon data arrive.",
               "Mantle depletion records agree with the zircon inversion.",
               "Newly mapped regions match the predicted age patterns."],
   "refute": ["Inversions swing wildly with each new dataset.",
              "Preservation bias proves unmodelable from available data.",
              "Hafnium systematics misidentify reworking at scale."],
   "checks": [("fraction_today", 0.9, 1.0), ("fraction_at_2_5Ga", 0.4, 0.6)],
   "honesty": ("The logistic curve is a placeholder shape. The real debate is which shape the "
               "data support once reworking and preservation bias are honestly modeled."),
 }})
# ---------------------------------------------------------------- 14
ENTRIES.append({
 "key": "deep-biosphere-extent",
 "name": "How Much Life Is in the Deep Biosphere?",
 "group": "Geochemistry",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": ("Microbes live kilometers beneath the surface in rock with no sunlight, but the total size of this "
             "deep biosphere - possibly Earth's largest ecosystem - is uncertain by orders of magnitude."),
 "background": ("Deep drilling and mines have found microbial cells in sediments and fractured rock kilometers down, "
             "living on chemical energy from water-rock reactions such as hydrogen production, at temperatures up to "
             "the current known limit of 122 degrees Celsius. Estimates of the total deep cell count range from "
             "10^29 to 10^31 - a hundredfold uncertainty - because cell densities decline with depth in ways measured "
             "at only a handful of sites, and because most deep microbes have never been cultured, so their activity "
             "rates are inferred, not measured. Whether the deep biosphere rivals or dwarfs surface life in biomass, "
             "and what it does to global carbon, sulfur, and iron cycles, are open questions."),
 "why_it_matters": ("If the deep biosphere is as large as the high estimates, it is a major player in Earth's "
             "geochemistry, slowly transforming rock and cycling elements on geological timescales. It is also the "
             "best analog for life on Mars or icy moons: understanding its energy limits tells us where to look for "
             "life elsewhere. And its enzymes, evolved for extreme conditions, are a resource for biotechnology."),
 "sig_pointer": ("The Signature system proposes systematic depth transects plus energy-flux-based habitability mapping "
             "to bound the deep biomass with measured activity rates. See the Signature Edition record for the full "
             "labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the deep biosphere as an energy-budget problem - life "
             "exists where chemical energy exceeds maintenance costs, so map the energy and the biomass follows."),
 "signature_solution": (
     "Proposed approach. Step 1: drill systematic depth transects in representative settings - marine sediments, "
     "continental crystalline rock, subduction zones - measuring cell counts, activity tracers, and energy fluxes "
     "with identical protocols, ending the era of incomparable one-off boreholes. Step 2: build an energy-budget "
     "model where habitability is computed from water-rock reaction rates minus maintenance energy, and test whether "
     "it predicts the observed depth limits. Step 3: measure in-situ activity rates with isotope tracers instead of "
     "inferring them, at least at reference sites. Step 4: integrate the bounded biomass into global carbon and "
     "sulfur cycle models to quantify the deep biosphere's geochemical leverage.\n"
     "Assumptions: that a handful of transects can represent global diversity (unlikely to be fully true); that "
     "energy budgets predict biomass (supported in principle, messy in practice); that contamination can be excluded "
     "in deep drilling (an eternal methodological battle).\n"
     "What would confirm it: energy-budget predictions matching observed depth limits across settings, activity "
     "measurements converging with model rates, and independent transects agreeing on biomass within a factor of a few.\n"
     "What would kill it: cell counts shown to be mostly dead or contaminant; energy budgets failing to predict any "
     "observed limit; or biomass estimates refusing to converge as data accumulate.\n"
     "What this does NOT claim: it does not claim a specific cell count today; it does not claim deep life affects "
     "surface climate; it is a research program, not an established result."),
 "citations": [
     "Whitman W B et al. Prokaryotes: the unseen majority. PNAS; 1998.",
     "Kallmeyer J et al. Global distribution of microbial abundance in marine sediments. PNAS; 2012.",
     "Magnabosco C et al. The biomass and biodiversity of the continental subsurface. Nat Geosci; 2018."],
 "explorer": {
   "blurb": ("A deep-biomass integrator: cell density declining exponentially with depth is integrated over rock "
             "volume to estimate total subsurface cells - showing how the answer hinges on the decline rate."),
   "assumptions": {"surface_cells_per_g": 1.0e6, "decay_per_km": 2.0, "depth_m": 3000.0,
                   "rock_density_kg_m3": 2500.0, "area_m2": 5.1e14},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    n0 = A[\"surface_cells_per_g\"] * 1000.0\n"
     "    lam = A[\"decay_per_km\"] / 1000.0\n"
     "    D = A[\"depth_m\"]\n"
     "    total = n0 * A[\"rock_density_kg_m3\"] * A[\"area_m2\"]\n"
     "    total *= (1.0 - math.exp(-lam * D)) / lam\n"
     "    return {\"total_cells\": total,\n"
     "            \"log10_cells\": math.log10(total)}\n"),
   "steps": [("Estimated total subsurface cells", "total_cells", "cells"),
             ("Order of magnitude", "log10_cells", "log10")],
   "confirm": ["Energy budgets predict observed depth limits across settings.",
               "Activity measurements converge with model rates.",
               "Independent transects agree on biomass within a factor of a few."],
   "refute": ["Cell counts prove mostly dead or contaminant.",
              "Energy budgets fail to predict any observed limit.",
              "Estimates refuse to converge as data accumulate."],
   "checks": [("total_cells", 1.0e28, 1.0e31), ("log10_cells", 28.0, 31.0)],
   "honesty": ("Two parameters - surface density and decline rate - control 30 orders of magnitude of "
               "answer. Both are measured at only a handful of sites."),
 }})
# ---------------------------------------------------------------- 15
ENTRIES.append({
 "key": "mantle-water-storage",
 "name": "How Much Water Is Hidden Inside the Mantle?",
 "group": "Geochemistry",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": ("Mantle minerals can lock up water in their crystal structures, possibly holding several oceans' worth - "
             "but whether the mantle is wet or dry, and where the water sits, is fiercely debated."),
 "background": ("Water changes everything in the mantle: it lowers melting temperatures, softens rock, and speeds "
             "convection. Laboratory experiments show that transition-zone minerals - wadsleyite and ringwoodite, "
             "stable between 410 and 660 kilometers depth - can dissolve up to a few weight percent water, far more "
             "than upper-mantle olivine. Seismic observations of a depressed 410-kilometer discontinuity and "
             "high electrical conductivity in some regions hint at wet zones, but mapping is patchy: some studies "
             "infer a water-rich transition zone holding oceans' worth, others find mostly dry mantle with localized "
             "wet patches. The answer controls mantle viscosity, the depth of melting, and the long-term sea-level "
             "budget over geological time."),
 "why_it_matters": ("A wet mantle convects differently, melts differently, and drives plate tectonics differently "
             "than a dry one. The mantle water reservoir also closes the planetary water budget: if oceans have been "
             "exchanged with the deep interior over billions of years, sea level history and even the origin of the "
             "oceans must be rethought. For exoplanets, mantle water storage decides whether surface oceans are stable "
             "or transient."),
 "sig_pointer": ("The Signature system proposes combining mineral solubility data, seismic attenuation mapping, and "
             "electromagnetic sounding in a joint inversion for mantle water distribution with honest uncertainties. "
             "See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats mantle water as a joint-inversion problem - no single "
             "measurement (seismic, electric, or lab) is trusted alone; only their agreement counts."),
 "signature_solution": (
     "Proposed approach. Step 1: complete laboratory solubility maps for all major mantle minerals across the full "
     "pressure-temperature range, with water contents measured by multiple independent techniques. Step 2: build "
     "global maps of seismic attenuation and electrical conductivity, the two observables most sensitive to water, "
     "with resolution quantified everywhere. Step 3: run a joint inversion that converts the geophysical maps to "
     "water content using the lab calibrations, propagating uncertainties from both sides - and publishing where the "
     "inversion is unconstrained rather than filling gaps with assumptions. Step 4: test the resulting water map "
     "against independent predictions: melting depths, viscosity from post-glacial rebound, and noble-gas budgets.\n"
     "Assumptions: that attenuation and conductivity variations are dominated by water rather than temperature or "
     "melt (the central ambiguity); that lab solubilities apply to the chemically complex real mantle; that the "
     "inversion's resolution is honestly reported.\n"
     "What would confirm it: attenuation, conductivity, and discontinuity-topography maps converging on the same wet "
     "and dry regions, with the inferred water contents matching melting and viscosity constraints.\n"
     "What would kill it: the observables explained entirely by temperature variations with no water needed; lab "
     "solubilities revised sharply downward; or joint inversions that remain unconstrained no matter how much data "
     "are added.\n"
     "What this does NOT claim: it does not claim the mantle holds a specific number of oceans today; it does not "
     "claim any region is proven wet; it is a research program, not an established result."),
 "citations": [
     "Inoue T et al. Water storage capacity of the mantle transition zone minerals. Geophys Res Lett; 1995.",
     "Pearson D G et al. Hydrous mantle transition zone indicated by ringwoodite. Nature; 2014.",
     "Karato S. Water distribution across the mantle. Annu Rev Earth Planet Sci; 2011."],
 "explorer": {
   "blurb": ("A mantle water-capacity calculator: from each mineral's abundance and laboratory water solubility it "
             "sums the storage capacity in ocean-equivalents."),
   "assumptions": {"mantle_kg": 4.0e24, "ocean_kg": 1.4e21,
                   "minerals": [{"frac": 0.45, "sol_ppm": 50.0}, {"frac": 0.12, "sol_ppm": 3000.0},
                                {"frac": 0.10, "sol_ppm": 2500.0}, {"frac": 0.33, "sol_ppm": 100.0}]},
   "model_src": (
     "def run(A):\n"
     "    avg_ppm = sum(m[\"frac\"] * m[\"sol_ppm\"] for m in A[\"minerals\"])\n"
     "    water_kg = avg_ppm * 1.0e-6 * A[\"mantle_kg\"]\n"
     "    return {\"avg_ppm\": avg_ppm, \"water_kg\": water_kg,\n"
     "            \"ocean_equivalents\": water_kg / A[\"ocean_kg\"]}\n"),
   "steps": [("Average storage capacity", "avg_ppm", "ppm water"),
             ("Total storable water", "water_kg", "kg"),
             ("In ocean-equivalents", "ocean_equivalents", "oceans")],
   "confirm": ["Attenuation, conductivity, and discontinuity maps converge on the same wet regions.",
               "Inferred water matches melting and viscosity constraints.",
               "Independent methods agree within stated uncertainties."],
   "refute": ["Observables explained by temperature alone, no water needed.",
              "Lab solubilities revised sharply downward.",
              "Joint inversions remain unconstrained with more data."],
   "checks": [("avg_ppm", 400.0, 1000.0), ("ocean_equivalents", 1.0, 3.0)],
   "honesty": ("Capacity is not inventory: the mantle may hold far less than it could. "
               "This demo computes the ceiling, not the contents."),
 }})
# ---------------------------------------------------------------- 16
ENTRIES.append({
 "key": "origin-of-oceans",
 "name": "Where Did Earths Oceans Come From?",
 "group": "Planetary Formation",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": ("Earth's water could have arrived late on asteroids, or been baked into the planet from the start - "
             "and isotope evidence currently supports both stories at once."),
 "background": ("Two grand narratives compete. The late-veneer story says Earth formed dry and water arrived later "
             "on carbonaceous-chondrite-like asteroids, whose deuterium-to-hydrogen ratios resemble Earth's oceans. "
             "The ingassing story says water was incorporated during formation itself - enstatite chondrites, the "
             "isotopically most Earth-like meteorites, contain surprising water, and hydrogen from the solar nebula "
             "could have dissolved into the magma ocean. Noble gases complicate both: Earth's mantle neon looks "
             "solar, while atmospheric xenon looks chondritic. Recent work has strengthened each side in turn, and "
             "the honest state of the field is that the proportions - how much late versus early - are unknown."),
 "why_it_matters": ("Water delivery decides which planets get oceans: if water needs a lucky late bombardment, "
             "habitable worlds are rare; if planets ingas their own water, oceans are the norm. The answer rewrites "
             "planet-formation models and focuses the search for life. It also sets the initial conditions for all "
             "of Earth's subsequent water cycling between surface and interior."),
 "sig_pointer": ("The Signature system proposes a multi-isotope mixing inversion - hydrogen, nitrogen, noble gases "
             "together - with endmember uncertainties, letting new sample-return data act as tiebreakers. See the "
             "Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats ocean origin as a mixing problem with uncertain "
             "endmembers - every isotope system votes, and the verdict must satisfy all of them at once."),
 "signature_solution": (
     "Proposed approach. Step 1: compile hydrogen, nitrogen, and noble-gas isotope ratios for Earth reservoirs "
     "(oceans, mantle, atmosphere) and for all candidate source materials, with full analytical uncertainties. "
     "Step 2: run a Bayesian mixing inversion that solves for the source proportions satisfying all isotope systems "
     "simultaneously, propagating endmember uncertainties instead of picking favorite values. Step 3: use new "
     "sample-return data - Ryugu, Bennu, and future missions - as they arrive to tighten the chondritic endmembers. "
     "Step 4: require the winning mixture to also satisfy dynamical constraints from planet-formation simulations.\n"
     "Assumptions: that the candidate source materials measured today represent the ancient feedstock (alteration and "
     "sampling bias are concerns); that isotope ratios were not reset by later processes (degassing fractionates "
     "them); that the inversion's endmember list is complete.\n"
     "What would confirm it: one mixing proportion satisfying hydrogen, nitrogen, and noble-gas systems at once, "
     "stable as new sample data arrive, and consistent with dynamical formation models.\n"
     "What would kill it: no mixture satisfying all isotope systems - forcing a missing source; endmembers shifting "
     "with each new sample return; or proof that later processes erased the formation signature entirely.\n"
     "What this does NOT claim: it does not claim a specific late-versus-early split today; it does not claim any "
     "meteorite group is the proven source; it is a research program, not an established result."),
 "citations": [
     "Morbidelli A et al. Source regions and timescales for the delivery of water to Earth. Meteorit Planet Sci; 2000.",
     "Piani L et al. Earths water may have been inherited from material similar to enstatite chondrites. Science; 2020.",
     "Peslier A H et al. Water in the Earths interior. Space Sci Rev; 2017."],
 "explorer": {
   "blurb": ("A two-source mixing calculator: from deuterium-to-hydrogen ratios of Earth and two candidate sources "
             "it solves for the mixing fraction - the core arithmetic of the ocean-origin debate."),
   "assumptions": {"D_earth": 149.0, "D_chond": 158.0, "D_solar": 21.0},
   "model_src": (
     "def run(A):\n"
     "    f = (A[\"D_earth\"] - A[\"D_solar\"]) / (A[\"D_chond\"] - A[\"D_solar\"])\n"
     "    return {\"late_source_fraction\": f,\n"
     "            \"early_source_fraction\": 1.0 - f}\n"),
   "steps": [("Fraction from the late (chondritic-like) source", "late_source_fraction", ""),
             ("Fraction from the early (solar-like) source", "early_source_fraction", "")],
   "confirm": ["One mixture satisfies hydrogen, nitrogen, and noble gases together.",
               "New sample-return data tighten rather than shift the answer.",
               "Dynamical models independently produce the same mixture."],
   "refute": ["No mixture satisfies all isotope systems at once.",
              "Endmembers shift with every new sample return.",
              "Later processes prove to have erased the formation signature."],
   "checks": [("late_source_fraction", 0.7, 1.05)],
   "honesty": ("Two isotopes and two sources give one number - change an endmember and the answer moves. "
               "The debate is about which endmembers are real."),
 }})
# ---------------------------------------------------------------- 17
ENTRIES.append({
 "key": "deep-carbon-cycle",
 "name": "How Does Carbon Move Through the Deep Earth?",
 "group": "Geochemistry",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": ("Subduction zones drag carbon into the mantle, volcanoes return some of it, but the fluxes in both "
             "directions are uncertain by an order of magnitude - so the deep carbon budget does not close."),
 "background": ("Carbon subducts with oceanic plates as sediments, altered crust, and mantle rocks, while arc "
             "volcanoes and mid-ocean ridges degas carbon back to the surface. Estimates of the subduction input "
             "range across an order of magnitude because the carbon content of the downgoing plate is poorly sampled. "
             "How much subducted carbon returns quickly at arcs versus sinking into the deep mantle is equally "
             "uncertain - yet it decides whether the mantle is a carbon reservoir of 10^5 or 10^6 gigatons, whether "
             "deep diamonds sample recycled surface carbon, and how volcanic carbon dioxide has regulated climate "
             "over geological time. The Deep Carbon Observatory spent a decade on this inventory and still left the "
             "largest fluxes uncertain."),
 "why_it_matters": ("The deep carbon cycle is Earth's long-term thermostat: over millions of years, the balance "
             "between subduction burial and volcanic release sets atmospheric carbon dioxide. Diamonds - the only "
             "direct samples of the deep mantle - carry carbon whose isotopic signature may record surface recycling. "
             "And the modern carbon budget needs the geological baseline to distinguish human perturbation from "
             "natural flux."),
 "sig_pointer": ("The Signature system proposes closing the flux budget directly: measure subduction inputs, arc "
             "outputs, and mantle storage via diamond inclusions in one accounting framework. See the Signature "
             "Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the deep carbon cycle as an accounting problem - every "
             "flux measured, every reservoir inventoried, and the imbalance published instead of hidden."),
 "signature_solution": (
     "Proposed approach. Step 1: measure the carbon content of incoming oceanic plates directly - drill transects "
     "through sediments, crust, and uppermost mantle before subduction - replacing extrapolation with inventory. "
     "Step 2: quantify arc volcanic carbon outputs with continuous gas monitoring at representative arcs, separating "
     "recycled from mantle carbon with isotopes. Step 3: constrain deep storage from the carbon isotope systematics "
     "of diamond inclusions and xenoliths, mapping which mantle domains hold recycled carbon. Step 4: assemble the "
     "full budget with uncertainties, and let the imbalance - not any preferred story - define the research agenda.\n"
     "Assumptions: that drill transects represent global subduction input (subduction zones vary enormously); that "
     "arc gas measurements can be scaled up (few arcs are monitored); that diamond inclusions sample the mantle "
     "representatively (they sample where diamonds form).\n"
     "What would confirm it: independently measured inputs, outputs, and storage converging on a balanced budget "
     "within uncertainties, with the mantle residence time consistent across methods.\n"
     "What would kill it: inputs and outputs refusing to converge no matter how well measured - implying a missing "
     "flux; or storage estimates contradicting the flux balance, showing the inventory methods are biased.\n"
     "What this does NOT claim: it does not claim a closed budget today; it does not claim any flux number is "
     "correct; it is a research program, not an established result."),
 "citations": [
     "Kelemen P B, Manning C E. Reevaluating carbon fluxes in subduction zones. Nat Rev Earth Environ; 2015.",
     "Marty B. The origins and concentrations of water, carbon, nitrogen and noble gases on Earth. Earth Planet Sci Lett; 2012.",
     "Deep Carbon Observatory: decadal synthesis reports. 2019."],
 "explorer": {
   "blurb": ("A deep-carbon budget balancer: subduction input minus volcanic output gives the net flux into the "
             "deep mantle, and dividing the mantle inventory by it yields the residence time."),
   "assumptions": {"subduction_MtC_yr": 55.0, "arc_MtC_yr": 28.0, "ridge_MtC_yr": 12.0, "mantle_C_GtC": 1.0e6},
   "model_src": (
     "def run(A):\n"
     "    out = A[\"arc_MtC_yr\"] + A[\"ridge_MtC_yr\"]\n"
     "    net = A[\"subduction_MtC_yr\"] - out\n"
     "    residence = (A[\"mantle_C_GtC\"] * 1000.0) / net\n"
     "    return {\"volcanic_output_MtC_yr\": out, \"net_to_deep_MtC_yr\": net,\n"
     "            \"mantle_residence_yr\": residence}\n"),
   "steps": [("Volcanic carbon output (arc + ridge)", "volcanic_output_MtC_yr", "MtC/yr"),
             ("Net flux into the deep mantle", "net_to_deep_MtC_yr", "MtC/yr"),
             ("Mantle carbon residence time", "mantle_residence_yr", "years")],
   "confirm": ["Inputs, outputs, and storage converge on a balanced budget.",
               "Residence times agree across independent methods.",
               "Diamond inclusion data match the flux-derived storage."],
   "refute": ["Fluxes refuse to converge no matter how well measured.",
              "Storage estimates contradict the flux balance.",
              "A missing flux is required to close the books."],
   "checks": [("net_to_deep_MtC_yr", 10.0, 25.0), ("mantle_residence_yr", 3.0e7, 1.2e8)],
   "honesty": ("Every number in this budget is uncertain by factors of several, and the residence time "
               "inherits all of it. The demo shows the accounting structure - the field still needs "
               "the actual accounts."),
 }})
# ---------------------------------------------------------------- 18
ENTRIES.append({
 "key": "llsvp-nature",
 "name": "What Are the Giant Blobs at the Base of the Mantle?",
 "group": "Deep Earth",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": ("Two continent-sized slow regions sit at the base of the mantle, and seismologists cannot agree "
             "whether they are hot rising rock, dense primordial piles, or graveyards of sunken tectonic plates."),
 "background": ("Seismic tomography reveals two Large Low Shear Velocity Provinces - one beneath Africa, one "
             "beneath the Pacific - each thousands of kilometers across and rising over a thousand kilometers above "
             "the core-mantle boundary, where seismic waves travel several percent slower than average. Three "
             "interpretations compete: they are purely thermal (hot, buoyant upwellings feeding plumes), "
             "thermochemical (dense, primordial material enriched in iron, resisting mixing for billions of years), "
             "or accumulations of subducted oceanic slabs piled at the boundary. The discriminant is density: hot "
             "rock should be light, primordial piles heavy - but density at that depth is inferred indirectly from "
             "normal-mode oscillations and tides, and the inferences disagree."),
 "why_it_matters": ("LLSVPs may anchor the whole pattern of mantle convection: plumes appear to rise from their "
             "edges, large igneous provinces and mass extinctions cluster above them, and their density sets how "
             "much heat escapes the core - which powers the magnetic field. If they are primordial, they are "
             "survivors of Earth's formation, a time capsule at the planet's base."),
 "sig_pointer": ("The Signature system proposes a joint seismic-geodynamic inversion that tests density directly - "
             "the one observable that separates hot rock from primordial piles. See the Signature Edition record "
             "for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats LLSVPs as a density question - velocity maps show where "
             "they are, but only density says what they are, so the program targets density with every available "
             "method."),
 "signature_solution": (
     "Proposed approach. Step 1: sharpen LLSVP boundaries with full-waveform tomography, mapping not just slow "
     "velocities but sharpness of edges - primordial piles should have sharp chemical edges, thermal anomalies "
     "gradual ones. Step 2: measure density independently via normal-mode splitting, Earth tides, and dynamic "
     "topography, with each method's uncertainties stated plainly. Step 3: run geodynamic models of each hypothesis "
     "- slab graveyard, primordial pile, thermal superplume - and compare their predictions for edge sharpness, "
     "density, and plume generation against observations. Step 4: test the plume-edge correlation rigorously: do "
     "hotspots really rise from LLSVP margins, or does the correlation vanish under strict statistics?\n"
     "Assumptions: that edge sharpness is resolvable at 2,800 kilometers depth (at the edge of current capability); "
     "that density inferences from normal modes are robust (they depend on reference models); that the three "
     "hypotheses exhaust the possibilities (hybrids are likely).\n"
     "What would confirm it: sharp edges plus excess density plus matching geodynamic predictions converging on one "
     "hypothesis, with the plume-margin correlation surviving rigorous testing.\n"
     "What would kill it: density shown to be near zero (purely thermal after all); edges proven gradual; or the "
     "plume correlation exposed as selection bias, removing a pillar of the thermochemical case.\n"
     "What this does NOT claim: it does not claim LLSVPs are primordial today; it does not claim they caused any "
     "extinction; it is a research program, not an established result."),
 "citations": [
     "Garnero E J, McNamara A K. Structure and dynamics of Earths lower mantle. Science; 2008.",
     "Burke K et al. Plume generation zones at the margins of large low shear velocity provinces. Earth Planet Sci Lett; 2008.",
     "Lau H C P et al. Tidal tomography constrains Earths deep-mantle buoyancy. Nature; 2017."],
 "explorer": {
   "blurb": ("An LLSVP mass estimator: from the shear-velocity anomaly and a velocity-to-density scaling it "
             "computes the density anomaly and the implied excess mass of the deep piles."),
   "assumptions": {"dlnVs_percent": -3.0, "R_ratio": 0.3, "volume_fraction": 0.03,
                   "mantle_volume_m3": 9.1e20, "rho": 5500.0},
   "model_src": (
     "def run(A):\n"
     "    dlnrho = A[\"R_ratio\"] * abs(A[\"dlnVs_percent\"]) / 100.0\n"
     "    vol = A[\"volume_fraction\"] * A[\"mantle_volume_m3\"]\n"
     "    excess = dlnrho * A[\"rho\"] * vol\n"
     "    return {\"density_anomaly_percent\": dlnrho * 100.0,\n"
     "            \"excess_mass_kg\": excess}\n"),
   "steps": [("Implied density anomaly", "density_anomaly_percent", "%"),
             ("Excess mass of the piles", "excess_mass_kg", "kg")],
   "confirm": ["Sharp edges plus excess density converge on one hypothesis.",
               "Geodynamic models reproduce the observed structure.",
               "The plume-margin correlation survives rigorous statistics."],
   "refute": ["Density proves near zero - purely thermal after all.",
              "Edges prove gradual, not chemical.",
              "The plume correlation is exposed as selection bias."],
   "checks": [("density_anomaly_percent", 0.5, 1.5), ("excess_mass_kg", 5.0e20, 3.0e21)],
   "honesty": ("The velocity-to-density scaling is the crux - change it and the mass swings. "
               "Seismology measures velocity well; density is the hard-won prize."),
 }})
# ---------------------------------------------------------------- 19
ENTRIES.append({
 "key": "mantle-plume-mechanics",
 "name": "What Drives Mantle Plumes?",
 "group": "Geodynamics",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": ("Hotspot volcanoes like Hawaii are blamed on plumes rising from the deep mantle, but whether plumes "
             "are narrow deep jets or shallow plate-tectonic artifacts is still contested."),
 "background": ("The plume hypothesis, proposed by Wilson and developed by Morgan in 1971, explains chains like "
             "Hawaii-Emperor as plates drifting over fixed deep-mantle upwellings. Supporting evidence includes "
             "oceanic swells (broad seafloor uplift around hotspots), high-3He/4He ratios suggesting deep primitive "
             "sources, and seismic images of some conduits extending deep. But critics note that many supposed "
             "plumes lack deep seismic roots, that some hotspot tracks fit plate-tectonic 'crack' models, and that "
             "plume buoyancy fluxes - measured from swell topography - vary enormously. Large igneous provinces, "
             "implicated in mass extinctions, are widely attributed to plume heads, making the question load-bearing "
             "for Earth history."),
 "why_it_matters": ("Plumes would be a second mode of mantle convection alongside plate tectonics, carrying a large "
             "share of Earth's internal heat and building ocean islands and flood basalts. If plume heads caused the "
             "Siberian Traps and the end-Permian extinction, plume physics is extinction physics. And plume heat "
             "flux is a major term in the planet's energy budget."),
 "sig_pointer": ("The Signature system proposes tracking candidate plumes from surface to core-mantle boundary with "
             "full-waveform tomography and testing buoyancy fluxes against the heat-flow budget. See the Signature "
             "Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats each plume as a suspect to be tracked, not a doctrine - "
             "a plume earns its status by a continuous seismic conduit and a heat budget that balances."),
 "signature_solution": (
     "Proposed approach. Step 1: image every major hotspot with full-waveform tomography to test for continuous "
     "conduits from the surface to the core-mantle boundary, publishing null results - headless hotspots - as "
     "prominently as detections. Step 2: measure buoyancy flux from swell topography and geoid for each hotspot with "
     "uniform methods, building the first apples-to-apples plume census. Step 3: test each plume's heat contribution "
     "against the global heat-flow budget: the summed plume flux must fit within what the mantle can supply. Step 4: "
     "confront the census with plate-tectonic alternatives - cracks, edge-driven convection - scoring which "
     "hotspots each explains.\n"
     "Assumptions: that tomography can resolve narrow conduits at depth (resolution is marginal for thin tails); "
     "that swell topography converts cleanly to buoyancy flux (lithospheric strength complicates it); that the "
     "heat budget is known well enough to constrain the sum (it is uncertain).\n"
     "What would confirm it: continuous deep conduits beneath the major hotspots, a buoyancy-flux census that fits "
     "the heat budget, and failed predictions for the plate-tectonic alternatives.\n"
     "What would kill it: most hotspots showing no deep roots; the summed flux exceeding plausible mantle supply; "
     "or crack and edge-driven models explaining the tracks as well as plumes do.\n"
     "What this does NOT claim: it does not claim every hotspot is a deep plume today; it does not claim plumes "
     "caused any specific extinction; it is a research program, not an established result."),
 "citations": [
     "Morgan W J. Convection plumes in the lower mantle. Nature; 1971.",
     "Sleep N H. Hotspots and mantle plumes. Annu Rev Earth Planet Sci; 1990.",
     "Courtillot V et al. Three types of hotspots. Earth Planet Sci Lett; 2003."],
 "explorer": {
   "blurb": ("A plume buoyancy-flux calculator: from swell volume flux, thermal expansion, and temperature excess "
             "it computes the mass flux driving a hotspot swell - the number every plume must account for."),
   "assumptions": {"rho": 3300.0, "alpha": 3.0e-5, "dT": 250.0, "volume_flux_m3_s": 350.0},
   "model_src": (
     "def run(A):\n"
     "    B = A[\"rho\"] * A[\"alpha\"] * A[\"dT\"] * A[\"volume_flux_m3_s\"]\n"
     "    return {\"buoyancy_flux_kg_s\": B,\n"
     "            \"buoyancy_flux_Mt_yr\": B * 31557600.0 / 1.0e9}\n"),
   "steps": [("Buoyancy flux", "buoyancy_flux_kg_s", "kg/s"),
             ("Annualized buoyancy flux", "buoyancy_flux_Mt_yr", "Mt/yr")],
   "confirm": ["Continuous deep conduits found beneath major hotspots.",
               "The flux census fits the mantle heat budget.",
               "Plate-tectonic alternatives fail the same tests."],
   "refute": ["Most hotspots show no deep roots.",
              "Summed flux exceeds plausible mantle supply.",
              "Crack models explain the tracks as well as plumes."],
   "checks": [("buoyancy_flux_kg_s", 5.0e3, 1.5e4)],
   "honesty": ("Swell topography is measured; converting it to deep mass flux assumes the swell is "
               "thermal and the conduit is steady. Both are debated."),
 }})
# ---------------------------------------------------------------- 20
ENTRIES.append({
 "key": "core-mantle-boundary-structure",
 "name": "What Is the Core-Mantle Boundary Really Like?",
 "group": "Deep Earth",
 "ladder_rank": 20, "ladder_tier": "advanced",
 "problem": ("At 2,900 kilometers depth, the rocky mantle meets the liquid iron core across a boundary with "
             "mountain-scale topography, strange slow patches, and unknown chemistry - and our maps of it are "
             "still crude."),
 "background": ("The core-mantle boundary (CMB) is the most dramatic interface inside Earth: density nearly "
             "doubles across it, and it separates the silicate mantle from the metallic core. Above it lies the "
             "D-double-prime layer, a few hundred kilometers thick with complex structure, including ultra-low "
             "velocity zones (ULVZs) - patches tens of kilometers thick where seismic waves slow dramatically, "
             "possibly indicating partial melt. The boundary has topography of several kilometers, and the "
             "post-perovskite mineral phase discovered in 2004 added new complexity. Heat flowing across the CMB "
             "powers the geodynamo, yet its total amount is uncertain by a factor of two or more, and whether "
             "chemical reactions between core and mantle contaminate either side is unknown."),
 "why_it_matters": ("The CMB is the engine room of the magnetic field: core cooling rate sets geodynamo power, and "
             "plumes - if they exist - are born here. Its topography and chemistry record the fate of subducted "
             "slabs and possibly of primordial reservoirs. Understanding heat and mass transfer across this boundary "
             "is understanding what powers Earth's interior."),
 "sig_pointer": ("The Signature system proposes mapping ultra-low velocity zones globally with high-frequency seismic "
             "phases plus mineral-physics melt models to determine what the CMB's strangest patches actually are. "
             "See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the CMB as an interface to be imaged like terrain - "
             "topography, composition, and heat flow mapped together, with resolution limits stated on every map."),
 "signature_solution": (
     "Proposed approach. Step 1: map ULVZs globally using high-frequency seismic phases that graze the CMB, with "
     "detection thresholds published so null results - regions with no ULVZs - are as informative as detections. "
     "Step 2: test the partial-melt hypothesis against alternatives (iron-enriched solid, core-mantle reaction "
     "products) using the velocity-density systematics each predicts, constrained by mineral-physics experiments. "
     "Step 3: measure CMB heat flow by combining core energetics, mantle plume flux estimates, and the thermal "
     "history, propagating the factor-of-two uncertainty honestly. Step 4: search for chemical exchange signatures "
     "in plume lavas - tungsten and noble-gas anomalies that would fingerprint core material in the mantle.\n"
     "Assumptions: that high-frequency phases can resolve tens-of-kilometer ULVZ structure (at the resolution "
     "limit); that mineral-physics experiments reach CMB conditions faithfully (they approximate); that plume "
     "geochemistry can isolate a core signal from recycled crust (contested).\n"
     "What would confirm it: ULVZ properties matching melt predictions across many locations, a converged CMB heat "
     "flow from independent methods, and core-derived chemical signatures in hotspot lavas.\n"
     "What would kill it: ULVZs explained as solid iron-rich piles with no melt; heat-flow estimates refusing to "
     "converge; or geochemical 'core signals' traced to recycled crust instead.\n"
     "What this does NOT claim: it does not claim ULVZs are melt today; it does not claim core-mantle chemical "
     "exchange is proven; it is a research program, not an established result."),
 "citations": [
     "Lay T et al. Core-mantle boundary heat flow. Nat Geosci; 2008.",
     "Murakami M et al. Post-perovskite phase transition in MgSiO3. Science; 2004.",
     "McNamara A K et al. Ultra-low velocity zones. Annu Rev Earth Planet Sci; 2010."],
 "explorer": {
   "blurb": ("A ULVZ melt-fraction estimator: from the observed seismic velocity drop and the laboratory "
             "velocity-vs-melt sensitivity it infers how much melt a slow patch would need."),
   "assumptions": {"dV_percent": 10.0, "sensitivity": 40.0},
   "model_src": (
     "def run(A):\n"
     "    melt = A[\"dV_percent\"] / A[\"sensitivity\"]\n"
     "    return {\"melt_fraction\": melt, \"dV_percent\": float(A[\"dV_percent\"]),\n"
     "            \"solid_fraction\": 1.0 - melt}\n"),
   "steps": [("Observed velocity drop", "dV_percent", "%"),
             ("Implied melt fraction (if melt is the cause)", "melt_fraction", ""),
             ("Implied solid fraction", "solid_fraction", "")],
   "confirm": ["ULVZ properties match melt predictions at many locations.",
               "CMB heat flow converges across independent methods.",
               "Core-derived chemical signatures found in hotspot lavas."],
   "refute": ["ULVZs prove to be solid iron-rich piles, no melt.",
              "Heat-flow estimates refuse to converge.",
              "Core signals trace to recycled crust instead."],
   "checks": [("melt_fraction", 0.1, 0.4), ("solid_fraction", 0.6, 0.9)],
   "honesty": ("The sensitivity of velocity to melt is itself uncertain - and the solid-pile "
               "alternative needs no melt at all. The demo quantifies the melt story, not its truth."),
 }})
# ---------------------------------------------------------------- 21
ENTRIES.append({
 "key": "geodynamo-power-source",
 "name": "What Powers Earths Magnetic Field?",
 "group": "Geomagnetism",
 "ladder_rank": 21, "ladder_tier": "advanced",
 "problem": ("The geodynamo needs a continuous power supply to sustain the magnetic field for billions of years, "
             "but how much comes from cooling, from inner-core growth, and from chemical separation is not settled."),
 "background": ("The magnetic field is generated by convection in the liquid outer core, but convection needs an "
             "energy source. Candidates include secular cooling (the whole core losing heat), latent heat released as "
             "the inner core freezes, compositional buoyancy as light elements are expelled from the growing inner "
             "core, precipitation of magnesium oxide ('snow') at the top of the core, and radioactive potassium in "
             "the core. The total power available is bounded by heat flowing across the core-mantle boundary - itself "
             "uncertain - and by the age of the inner core, which sets how long compositional power has operated. "
             "Different combinations can all sustain a dynamo, so the field's existence does not pick a winner."),
 "why_it_matters": ("The power source sets the thermal history of the entire planet: a young inner core implies "
             "rapid cooling and a different ancient field than an old one. The same energetics decide which "
             "exoplanets can sustain magnetic shields - and therefore atmospheres and habitability. It is also the "
             "upstream question behind reversals, the South Atlantic Anomaly, and the field's long-term future."),
 "sig_pointer": ("The Signature system proposes a joint energy-budget accounting: core-mantle heat flow, inner-core "
             "growth rate, and light-element partitioning solved together for the power mix. See the Signature "
             "Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats geodynamo power as an energy audit - every proposed "
             "source entered on the ledger, every trade-off made explicit, and the books required to balance."),
 "signature_solution": (
     "Proposed approach. Step 1: assemble the core energy ledger - CMB heat flow, adiabatic heat flux, latent heat "
     "from inner-core growth, gravitational energy from light-element release, and candidate extras (MgO "
     "precipitation, radiogenic heating) - each with uncertainties. Step 2: measure the inner-core growth rate "
     "from the age and size constraints, which fixes the latent and compositional terms. Step 3: constrain light-"
     "element partitioning with high-pressure experiments and seismological density deficits, fixing how much "
     "compositional buoyancy each megawatt of cooling buys. Step 4: require the surviving power mix to also explain "
     "the paleomagnetic record - a dynamo that never died for 3.5 billion years, through whatever thermal history "
     "the mix implies.\n"
     "Assumptions: that the CMB heat flow will be pinned down (currently factor-of-two); that inner-core age "
     "estimates converge (they span a factor of four); that the core's light-element inventory is knowable from "
     "cosmochemistry plus experiments.\n"
     "What would confirm it: a power mix that balances the ledger, matches the inner-core age, reproduces the "
     "paleomagnetic intensity record, and survives in self-consistent dynamo simulations.\n"
     "What would kill it: ledger terms that cannot be balanced without unphysical assumptions; an inner-core age "
     "incompatible with the required power history; or experiments ruling out the assumed light-element chemistry.\n"
     "What this does NOT claim: it does not claim a specific power split today; it does not claim any exotic source "
     "is real; it is a research program, not an established result."),
 "citations": [
     "Lister J R, Buffett B A. The strength and efficiency of thermal and compositional convection. Phys Earth Planet Inter; 1995.",
     "Nimmo F. Energetics of the core. Treatise on Geophysics, 2nd ed.; 2015.",
     "Labrosse S et al. A high core-mantle boundary temperature. Nature; 2001."],
 "explorer": {
   "blurb": ("A core energy-budget ledger: from core-mantle heat flow and the adiabatic baseline it computes the "
             "convective power available, then splits it into thermal and compositional shares."),
   "assumptions": {"Q_cmb_TW": 12.0, "Q_adiabatic_TW": 5.0, "comp_fraction": 0.6},
   "model_src": (
     "def run(A):\n"
     "    Qconv = A[\"Q_cmb_TW\"] - A[\"Q_adiabatic_TW\"]\n"
     "    f = A[\"comp_fraction\"]\n"
     "    return {\"convective_TW\": Qconv,\n"
     "            \"compositional_TW\": Qconv * f,\n"
     "            \"thermal_TW\": Qconv * (1.0 - f),\n"
     "            \"comp_share\": f}\n"),
   "steps": [("Convective power available to the dynamo", "convective_TW", "TW"),
             ("Compositional share (inner-core growth)", "compositional_TW", "TW"),
             ("Thermal share (cooling)", "thermal_TW", "TW")],
   "confirm": ["The ledger balances with a mix matching inner-core age.",
               "The mix reproduces 3.5 Gyr of paleomagnetic record.",
               "Self-consistent dynamo simulations sustain the field on this power."],
   "refute": ["The ledger cannot balance without unphysical assumptions.",
              "Inner-core age proves incompatible with the required history.",
              "Experiments rule out the assumed light-element chemistry."],
   "checks": [("convective_TW", 4.0, 10.0), ("comp_share", 0.4, 0.8)],
   "honesty": ("Every term on this ledger is uncertain - especially the CMB heat flow. "
               "The demo shows the accounting; the field still needs the receipts."),
 }})
# ---------------------------------------------------------------- 22
ENTRIES.append({
 "key": "inner-core-age",
 "name": "How Old Is the Solid Inner Core?",
 "group": "Deep Earth",
 "ladder_rank": 22, "ladder_tier": "advanced",
 "problem": ("The inner core - a moon-sized ball of solid iron at Earth's center - could have begun freezing "
             "anywhere from half a billion to over two billion years ago, and the estimates refuse to converge."),
 "background": ("The inner core grows as Earth cools: liquid iron freezes onto its surface, releasing latent heat "
             "and expelling light elements that power the geodynamo. Its age therefore anchors the planet's entire "
             "thermal history. Thermal models give a wide range - roughly 0.5 to 2 billion years - because the age "
             "depends on the core's thermal conductivity (recently revised sharply upward by mineral physics, "
             "implying faster cooling and a younger core) and on the CMB heat flow. Paleomagnetism offers an "
             "independent check: inner-core nucleation should have boosted the field, and some studies claim to see "
             "such a change around 1 to 1.5 billion years ago - but the signal is contested."),
 "why_it_matters": ("A young inner core means Earth is cooling fast and the ancient geodynamo ran on different "
             "fuel than today's - rewriting the thermal history used by every deep-Earth model. The age also sets "
             "the growth rate, which sets the compositional power driving the modern field. It is the single number "
             "that ties core physics to magnetic history."),
 "sig_pointer": ("The Signature system proposes combining growth-rate physics with the paleointensity record to hunt "
             "for the predicted field-strength change at nucleation. See the Signature Edition record for the full "
             "labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats inner-core age as a prediction to be tested, not a "
             "parameter to be tuned - the nucleation event must have left a fingerprint in the magnetic record."),
 "signature_solution": (
     "Proposed approach. Step 1: compute inner-core growth histories for the full range of thermal conductivities "
     "and CMB heat flows, producing not one age but a probability distribution with honest uncertainties. Step 2: "
     "derive the observable each history predicts - the timing and size of the field-strength jump at nucleation - "
     "before examining the paleomagnetic record. Step 3: test those predictions against the quality-ranked "
     "paleointensity database, scoring hits and misses with pre-registered criteria. Step 4: cross-check the "
     "surviving histories against independent clocks: the thermal evolution implied must also satisfy mantle "
     "constraints.\n"
     "Assumptions: that nucleation produces a detectable field change (model-dependent); that the paleointensity "
     "record is complete enough to show it (Precambrian data are sparse); that thermal conductivity at core "
     "conditions is now correct (it was revised drastically once already).\n"
     "What would confirm it: a predicted nucleation fingerprint found at the predicted time in independent "
     "paleomagnetic datasets, with the implied thermal history consistent with mantle constraints.\n"
     "What would kill it: no fingerprint at any candidate time; the fingerprint shown to be an artifact of sparse "
     "sampling; or conductivity revised again, moving the goalposts beyond recognition.\n"
     "What this does NOT claim: it does not claim a specific age today; it does not claim the paleomagnetic hints "
     "are real; it is a research program, not an established result."),
 "citations": [
     "Labrosse S et al. The age of the inner core. Earth Planet Sci Lett; 2001.",
     "Pozzo M et al. Thermal and electrical conductivity of iron at Earths core conditions. Nature; 2012.",
     "Biggin A J et al. Palaeomagnetic field intensity and the inner core. Earth Planet Sci Lett; 2015."],
 "explorer": {
   "blurb": ("An inner-core age estimator: from the core's radius and its growth rate - set by how fast heat "
             "escapes - it computes how long the freezing has been going on."),
   "assumptions": {"ic_radius_km": 1221.0, "growth_mm_yr": 0.7},
   "model_src": (
     "def run(A):\n"
     "    r_m = A[\"ic_radius_km\"] * 1000.0\n"
     "    rate_m_yr = A[\"growth_mm_yr\"] / 1000.0\n"
     "    age_yr = r_m / rate_m_yr\n"
     "    return {\"age_Gyr\": age_yr / 1.0e9,\n"
     "            \"growth_mm_yr\": float(A[\"growth_mm_yr\"])}\n"),
   "steps": [("Inner-core age (illustrative)", "age_Gyr", "Gyr"),
             ("Assumed growth rate", "growth_mm_yr", "mm/yr")],
   "confirm": ["A nucleation fingerprint is found at the predicted time in independent datasets.",
               "The implied thermal history satisfies mantle constraints.",
               "Conductivity and heat-flow values converge across methods."],
   "refute": ["No fingerprint at any candidate time.",
              "The signal proves to be sparse-sampling artifact.",
              "Conductivity is revised again, moving the goalposts."],
   "checks": [("age_Gyr", 1.0, 2.5)],
   "honesty": ("Age equals radius divided by growth rate - simple division. The growth rate is "
               "the unknown, and it depends on the contested thermal conductivity."),
 }})
# ---------------------------------------------------------------- 23
ENTRIES.append({
 "key": "inner-core-anisotropy",
 "name": "Why Is the Inner Core Seismically Anisotropic?",
 "group": "Deep Earth",
 "ladder_rank": 23, "ladder_tier": "advanced",
 "problem": ("Seismic waves travel through the inner core faster pole-to-pole than around the equator, by about "
             "3% - and after forty years, the cause of this anisotropy is still debated."),
 "background": ("Since the 1980s, seismologists have known that PKIKP waves traversing the inner core arrive "
             "earlier on polar paths than equatorial ones - the iron at Earth's center is seismically anisotropic, "
             "with a symmetry axis aligned to the rotation axis. Proposed causes include preferred alignment of "
             "iron crystals by deformation or magnetic forces, and a distinct innermost inner core (IMIC) - a "
             "few-hundred-kilometer central region with different, even stronger anisotropy, possibly recording an "
             "early growth regime. Hemispherical differences complicate the picture: the eastern and western "
             "hemispheres differ in velocity and attenuation. Which iron phase is even stable at core conditions - "
             "hexagonal close-packed or body-centered cubic - remains contested, and each phase implies different "
             "anisotropy mechanisms."),
 "why_it_matters": ("The anisotropy is a frozen record of how the inner core grew and deformed - its crystal "
             "alignment encodes the flow, magnetic, and thermal history of the deepest Earth. Solving it would "
             "constrain the iron phase diagram at 330 gigapascals, the viscosity of the inner core, and the "
             "conditions of core formation. It is one of the few direct windows into solid-state physics at "
             "planetary-core conditions."),
 "sig_pointer": ("The Signature system proposes 3D anisotropy mapping with PKIKP and normal modes to test "
             "crystal-alignment against innermost-inner-core models on the hemispherical pattern. See the Signature "
             "Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats inner-core anisotropy as a pattern-matching problem - "
             "each mechanism predicts a distinct 3D signature, and the map, not the narrative, decides."),
 "signature_solution": (
     "Proposed approach. Step 1: build a 3D model of inner-core anisotropy from PKIKP travel times plus normal-mode "
     "splitting, which sense the whole core independently of ray geometry. Step 2: write down the distinct 3D "
     "predictions of the competing mechanisms - crystal alignment by deformation, by magnetic fields, growth "
     "texturing, and the IMIC hypothesis - before fitting. Step 3: score the mechanisms against the hemispherical "
     "pattern and depth dependence simultaneously, requiring the winner to explain all of them. Step 4: confront "
     "the winning texture with mineral-physics predictions for the stable iron phase's elastic anisotropy.\n"
     "Assumptions: that ray coverage is sufficient for true 3D imaging (polar paths are sparse); that normal modes "
     "can separate anisotropy from heterogeneity (partially); that the stable iron phase will be identified "
     "(ongoing debate).\n"
     "What would confirm it: one mechanism's 3D prediction matching travel times and normal modes together, with "
     "the implied iron phase consistent with high-pressure experiments.\n"
     "What would kill it: the pattern explained equally well by heterogeneity without anisotropy; the stable iron "
     "phase shown to be nearly isotropic, removing the mechanism's foundation; or hemispherical differences traced "
     "to outer-core structure instead.\n"
     "What this does NOT claim: it does not claim any mechanism is correct today; it does not claim to know the "
     "stable iron phase; it is a research program, not an established result."),
 "citations": [
     "Morelli A et al. Anisotropy of the inner core. Nature; 1986.",
     "Ishii M, Dziewonski A M. The innermost inner core. PNAS; 2002.",
     "Tkalcic H, Kennett B L N. Large variations in inner core anisotropy. Nature; 2008."],
 "explorer": {
   "blurb": ("An anisotropy travel-time calculator: from the inner-core diameter, wave speed, and anisotropy "
             "strength it computes the polar-equatorial arrival difference seismologists actually measure."),
   "assumptions": {"v_km_s": 11.0, "anisotropy": 0.03, "path_km": 2442.0},
   "model_src": (
     "def run(A):\n"
     "    v = A[\"v_km_s\"]\n"
     "    a = A[\"anisotropy\"]\n"
     "    L = A[\"path_km\"]\n"
     "    dt = L * (1.0 / (v * (1.0 - a / 2.0)) - 1.0 / (v * (1.0 + a / 2.0)))\n"
     "    return {\"dt_seconds\": dt, \"anisotropy_percent\": a * 100.0}\n"),
   "steps": [("Polar-equatorial travel-time difference", "dt_seconds", "s"),
             ("Anisotropy strength", "anisotropy_percent", "%")],
   "confirm": ["One mechanism's 3D prediction matches travel times and normal modes together.",
               "The implied iron phase agrees with high-pressure experiments.",
               "Hemispherical pattern explained, not just described."],
   "refute": ["The pattern is explained by heterogeneity without anisotropy.",
              "The stable iron phase proves nearly isotropic.",
              "Hemispherical differences trace to outer-core structure."],
   "checks": [("dt_seconds", 4.0, 10.0), ("anisotropy_percent", 2.5, 3.5)],
   "honesty": ("Three percent anisotropy makes seconds of travel-time difference across the whole core - "
               "measurable, but every interpretation leans on the unknown iron phase."),
 }})
# ---------------------------------------------------------------- 24
ENTRIES.append({
 "key": "inner-core-superrotation",
 "name": "Does the Inner Core Spin Faster Than the Rest of Earth?",
 "group": "Deep Earth",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": ("Measurements have variously claimed the inner core spins faster than the mantle, spins slower, or "
             "oscillates - and the field cannot agree which is real."),
 "background": ("In 1996, seismologists reported that the inner core super-rotates - spinning about 0.2 to 1 degree "
             "per year faster than the mantle - based on repeating earthquakes ('doublets') whose waves changed over "
             "time. Later studies found slower rates, no rotation, and even a reversal: prominent 2023-2024 papers "
             "argued the inner core oscillates on decadal timescales and recently began rotating backward relative "
             "to the surface. The doublet method is exquisitely sensitive to earthquake mislocation and to changes "
             "in the inner-core boundary itself, and different analysis choices give different answers. Independent "
             "constraints from normal modes and from the geodynamo's torque balance have not settled it."),
 "why_it_matters": ("Differential rotation measures the electromagnetic and gravitational coupling between the "
             "core and mantle - the torque balance of the geodynamo itself. An oscillating inner core would imply "
             "decadal exchanges of angular momentum big enough to affect the length of day. And the dispute is a "
             "case study in how fragile seismic inferences can be when signals sit near the noise level."),
 "sig_pointer": ("The Signature system proposes long-baseline doublet monitoring with pre-registered analysis plus "
             "independent normal-mode constraints to settle the rotation question. See the Signature Edition record "
             "for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats super-rotation as a measurement dispute to be refereed - "
             "analysis choices locked before the data, independent methods required to agree."),
 "signature_solution": (
     "Proposed approach. Step 1: assemble all suitable repeating-earthquake doublets into one open dataset with "
     "uniform relocation, ending the era of each group using its own hand-picked events. Step 2: pre-register the "
     "analysis pipeline - which phases, which corrections, which statistical test - before running it on the full "
     "dataset. Step 3: obtain independent constraints from normal-mode splitting and from length-of-day torque "
     "budgets, which must agree with the doublet answer. Step 4: run the winning pipeline on synthetic data with "
     "known rotation to measure its actual detection threshold.\n"
     "Assumptions: that suitable doublets sample the inner core representatively (they cluster geographically); "
     "that earthquake mislocation can be controlled below the signal level (the central technical dispute); that "
     "inner-core boundary topography does not mimic rotation (it can).\n"
     "What would confirm it: the pre-registered pipeline detecting rotation in real data, agreeing with normal modes "
     "and torque budgets, with synthetic tests showing the signal is above the detection threshold.\n"
     "What would kill it: the signal vanishing under uniform relocation; independent methods disagreeing; or "
     "synthetic tests showing the claimed rates are below what the method can actually resolve.\n"
     "What this does NOT claim: it does not claim any rotation rate today; it does not claim the oscillation "
     "results are wrong; it is a research program, not an established result."),
 "citations": [
     "Song X, Richards P G. Seismological evidence for differential rotation of the Earths inner core. Nature; 1996.",
     "Yang Y, Song X. Multidecadal variation of the Earths inner-core rotation. Nat Geosci; 2023.",
     "Tkalcic H et al. The inner core: recent advances. Annu Rev Earth Planet Sci; 2022."],
 "explorer": {
   "blurb": ("A rotation-rate estimator: from the observed travel-time shift of a repeating earthquake doublet it "
             "computes the implied differential rotation rate - the measurement at the heart of the dispute."),
   "assumptions": {"dt_s": 0.15, "sensitivity_s_per_deg": 1.2, "baseline_yr": 18.0},
   "model_src": (
     "def run(A):\n"
     "    rate = (A[\"dt_s\"] / A[\"sensitivity_s_per_deg\"]) / A[\"baseline_yr\"]\n"
     "    return {\"deg_per_year\": rate,\n"
     "            \"deg_per_decade\": rate * 10.0}\n"),
   "steps": [("Implied differential rotation rate", "deg_per_year", "deg/yr"),
             ("Per decade", "deg_per_decade", "deg/decade")],
   "confirm": ["The pre-registered pipeline detects rotation in the full dataset.",
               "Normal modes and torque budgets agree with the doublet answer.",
               "Synthetic tests show the signal is above the detection threshold."],
   "refute": ["The signal vanishes under uniform relocation.",
              "Independent methods disagree with the doublet answer.",
              "Claimed rates prove below the method's resolution."],
   "checks": [("deg_per_year", 0.001, 0.05)],
   "honesty": ("A tenth of a second of time shift over eighteen years becomes thousandths of a degree "
               "per year - the dispute is whether that shift is rotation or relocation error."),
 }})
# ---------------------------------------------------------------- 25
ENTRIES.append({
 "key": "moon-formation-details",
 "name": "How Exactly Did the Moon Form?",
 "group": "Planetary Formation",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": ("The giant-impact hypothesis explains the Moon's existence but not why Earth and Moon are nearly "
             "identical in isotopes - and no impact model yet fits all the evidence at once."),
 "background": ("The leading theory since the 1970s: a Mars-sized body struck the early Earth, and debris from the "
             "impact coalesced into the Moon. It elegantly explains the Moon's small iron core and the system's "
             "angular momentum. But high-precision measurements show Earth and Moon are nearly identical in oxygen, "
             "titanium, and tungsten isotopes - unexpected if the Moon is mostly impactor material, since impactors "
             "should differ. Proposed fixes include thorough mixing in a vaporized Earth ('synestia'), an impactor "
             "made of Earth-like material, or high-angular-momentum impacts that later shed the excess. Each fix "
             "solves the isotopes while straining something else: dynamics, volatile depletion, or the lunar magma "
             "ocean record."),
 "why_it_matters": ("The Moon-forming impact was the last great violence of Earth's formation: it set the planet's "
             "spin, possibly its volatile budget, and the initial conditions for the magma ocean and core. The "
             "isotope puzzle generalizes - if giant impacts thoroughly mix, then terrestrial planet compositions are "
             "more homogenized than formation models assume. It is also the test case for how we read planetary "
             "origins from chemistry."),
 "sig_pointer": ("The Signature system proposes next-generation impact simulations with material mixing tracked "
             "particle-by-particle, scored against the full isotope and volatile record. See the Signature Edition "
             "record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats Moon formation as a multi-constraint fit - dynamics, "
             "isotopes, and volatiles must all be satisfied by one impact, with the misfits published, not tuned away."),
 "signature_solution": (
     "Proposed approach. Step 1: run a simulation ensemble spanning impactor mass, velocity, angle, and spin, with "
     "material provenance tracked for every parcel - no post-hoc mixing assumptions. Step 2: score each simulation "
     "simultaneously on angular momentum, isotope equilibration, lunar iron depletion, and volatile loss, with the "
     "scorecard published for all runs, not just the winners. Step 3: derive testable predictions that distinguish "
     "the surviving scenarios - for example, different volatile-depletion patterns or deep-mantle heterogeneity - "
     "and test them against lunar samples and seismic data. Step 4: require the winning scenario to also work in "
     "planet-formation models that produce the rest of the inner solar system.\n"
     "Assumptions: that the simulations resolve mixing faithfully (resolution is still limiting); that lunar samples "
     "represent the bulk Moon (they sample the near side crust); that the isotope similarities demand explanation "
     "rather than coincidence (the field's working assumption).\n"
     "What would confirm it: one scenario satisfying dynamics, isotopes, and volatiles together, with its unique "
     "predictions verified in new samples or data.\n"
     "What would kill it: no scenario satisfying all constraints simultaneously; the isotope similarity shown to be "
     "achievable by chance in standard impacts; or new measurements breaking the similarity the models were built to "
     "explain.\n"
     "What this does NOT claim: it does not claim any specific impact scenario today; it does not claim the "
     "giant-impact framework itself is wrong; it is a research program, not an established result."),
 "citations": [
     "Hartmann W K, Davis D R. Satellite-sized planetesimals and lunar origin. Icarus; 1975.",
     "Canup R M. Forming a Moon with an Earth-like composition. Science; 2012.",
     "Lock S J et al. The origin of the Moon within a terrestrial synestia. J Geophys Res; 2018."],
 "explorer": {
   "blurb": ("An impact-velocity estimator: from the Earth-Moon system's angular momentum and an assumed impactor "
             "mass it computes the collision velocity a canonical giant impact requires."),
   "assumptions": {"L_SI": 3.41e34, "impactor_earth_masses": 0.11, "earth_mass_kg": 5.97e24,
                   "impact_param_earth_radii": 0.7, "earth_radius_m": 6.371e6},
   "model_src": (
     "def run(A):\n"
     "    m = A[\"impactor_earth_masses\"] * A[\"earth_mass_kg\"]\n"
     "    b = A[\"impact_param_earth_radii\"] * A[\"earth_radius_m\"]\n"
     "    v = A[\"L_SI\"] / (m * b)\n"
     "    return {\"velocity_km_s\": v / 1000.0,\n"
     "            \"impactor_earth_masses\": float(A[\"impactor_earth_masses\"])}\n"),
   "steps": [("Required impact velocity", "velocity_km_s", "km/s"),
             ("Impactor mass", "impactor_earth_masses", "Earth masses")],
   "confirm": ["One scenario satisfies dynamics, isotopes, and volatiles together.",
               "Its unique predictions verify in new samples or data.",
               "The scenario fits planet-formation models of the inner solar system."],
   "refute": ["No scenario satisfies all constraints at once.",
              "Isotope similarity proves achievable by chance.",
              "New measurements break the similarity itself."],
   "checks": [("velocity_km_s", 9.0, 15.0)],
   "honesty": ("Angular momentum bookkeeping is exact; the isotope mixing is the mystery. "
               "This demo does the bookkeeping - the science gap is everything else."),
 }})
# ---------------------------------------------------------------- 26
ENTRIES.append({
 "key": "snowball-earth-escape",
 "name": "How Did Earth Escape Snowball Glaciations?",
 "group": "Paleoclimate",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": ("Twice in the deep past the planet froze over almost entirely, and the mechanism that broke the ice - "
             "and its timescale - is still only approximately understood."),
 "background": ("Geological evidence - glacial deposits at tropical latitudes, banded iron formations, and the "
             "'cap carbonates' draped over glacial rocks - indicates that around 717 million years ago (Sturtian) "
             "and 635 million years ago (Marinoan), ice reached the equator: Snowball Earth. The leading escape "
             "theory, from Hoffman and colleagues in 1998, is elegant: with the water cycle shut down, silicate "
             "weathering stopped drawing down carbon dioxide, so volcanic outgassing accumulated it for millions of "
             "years until the greenhouse effect overwhelmed the ice albedo, melting the planet in a geological "
             "instant. But the details are contested: how much carbon dioxide was needed, whether weathering truly "
             "stopped, whether the ice was truly global ('slushball' with open equatorial water), and how life "
             "survived."),
 "why_it_matters": ("Snowball events are the most extreme climate catastrophes in Earth's history - the ultimate "
             "test of climate physics and of life's resilience. The escape mechanism is a natural experiment in "
             "greenhouse warming on a planetary scale, directly relevant to exoplanets near the outer edge of "
             "habitable zones. And the aftermath - the Cambrian explosion of complex life followed the Marinoan - "
             "suggests these deep freezes shaped evolution itself."),
 "sig_pointer": ("The Signature system proposes tightening the carbon-dioxide threshold with better sub-ice "
             "weathering physics and precise dating of the cap carbonates. See the Signature Edition record for "
             "the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats Snowball escape as a threshold measurement - how much "
             "carbon dioxide, over how long, with the weathering physics computed rather than assumed."),
 "signature_solution": (
     "Proposed approach. Step 1: model silicate weathering under Snowball conditions explicitly - with ice-covered "
     "continents, limited runoff, and possible subglacial weathering - instead of assuming it drops to zero. Step 2: "
     "compute the carbon-dioxide threshold for deglaciation in climate models with realistic ice physics, mapping "
     "how the threshold depends on the contested details. Step 3: date the cap carbonates and glacial deposits "
     "with high-precision geochronology to measure the actual duration of the glaciations and the speed of the "
     "meltdown. Step 4: test the 'slushball' alternative against the same data - open-water refugia should leave "
     "distinct geochemical and biological signatures.\n"
     "Assumptions: that volcanic outgassing continued during glaciations (likely but unmeasured); that weathering "
     "can be modeled under ice (poorly constrained); that the geological record is complete enough to distinguish "
     "Snowball from slushball (it may not be).\n"
     "What would confirm it: deglaciation thresholds matching the durations from geochronology, cap-carbonate "
     "chemistry consistent with the predicted carbon-dioxide buildup, and weathering models that close the budget.\n"
     "What would kill it: glaciations far shorter than any outgassing timescale allows; cap carbonates inconsistent "
     "with extreme carbon dioxide; or decisive evidence for persistent open water, favoring slushball.\n"
     "What this does NOT claim: it does not claim the escape threshold is known today; it does not claim all "
     "Snowball events worked the same way; it is a research program, not an established result."),
 "citations": [
     "Hoffman P F et al. A Neoproterozoic snowball Earth. Science; 1998.",
     "Kirschvink J L. Late Proterozoic low-latitude global glaciation. In: The Proterozoic Biosphere; 1992.",
     "Pierrehumbert R T et al. Climate of the Neoproterozoic. Annu Rev Earth Planet Sci; 2011."],
 "explorer": {
   "blurb": ("A deglaciation-timescale estimator: from the carbon-dioxide threshold needed to melt a Snowball and "
             "the volcanic outgassing rate it computes how long the deep freeze must last."),
   "assumptions": {"threshold_bar": 0.12, "flux_bar_yr": 6.0e-9},
   "model_src": (
     "def run(A):\n"
     "    t_yr = A[\"threshold_bar\"] / A[\"flux_bar_yr\"]\n"
     "    return {\"deglaciation_Myr\": t_yr / 1.0e6,\n"
     "            \"threshold_ppm\": A[\"threshold_bar\"] * 1.0e6}\n"),
   "steps": [("Carbon-dioxide threshold for meltdown", "threshold_ppm", "ppm"),
             ("Required glaciation duration", "deglaciation_Myr", "Myr")],
   "confirm": ["Thresholds match geochronological durations.",
               "Cap carbonates record the predicted carbon-dioxide buildup.",
               "Weathering models close the budget."],
   "refute": ["Glaciations prove far shorter than outgassing allows.",
              "Cap carbonates contradict extreme carbon dioxide.",
              "Open-water evidence favors slushball decisively."],
   "checks": [("deglaciation_Myr", 5.0, 50.0)],
   "honesty": ("Divide a threshold by a flux and get a time - the arithmetic is trivial. Both inputs "
               "are the unknowns; the demo shows how they trade off."),
 }})
# ---------------------------------------------------------------- 27
ENTRIES.append({
 "key": "faint-young-sun-paradox",
 "name": "Why Was the Young Earth Warm Under a Faint Young Sun?",
 "group": "Paleoclimate",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": ("Four billion years ago the Sun shone about 25% dimmer, yet Earth had liquid water and early life - "
             "and the greenhouse recipe that kept it warm is still not agreed upon."),
 "background": ("Stellar physics is unambiguous: the young Sun was roughly 70 to 75% as luminous as today, which "
             "by itself would leave Earth frozen. Yet 3.8-billion-year-old rocks record liquid water, and life "
             "appears early. Sagan and Mullen posed the paradox in 1972. Proposed solutions invoke much higher "
             "carbon dioxide, methane from early methanogens, a lower planetary albedo (fewer continents, different "
             "clouds), extra nitrogen broadening greenhouse absorption, or combinations. Archean carbon-dioxide "
             "proxies from paleosols allow a wide range, methane needs a biological source before clear evidence "
             "for methanogens, and cloud feedbacks under a different atmosphere are deeply uncertain."),
 "why_it_matters": ("The paradox is the archetype for habitable-zone science: every rocky exoplanet around a young "
             "star faces the same faint-sun problem, and Earth's solution - whatever it was - is the calibration "
             "point. It also constrains the early carbon cycle, the rise of oxygenic photosynthesis, and the "
             "conditions life originated in. A wrong greenhouse recipe means wrong climates for the first billion "
             "years of Earth history."),
 "sig_pointer": ("The Signature system proposes a scored model ensemble against Archean proxies - paleosols, banded "
             "iron, and sulfur isotopes - to find which greenhouse recipes actually fit. See the Signature Edition "
             "record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the faint young Sun as a model-selection problem - every "
             "greenhouse recipe scored against the same Archean proxies, with the losers published alongside the winner."),
 "signature_solution": (
     "Proposed approach. Step 1: compile all Archean climate proxies - paleosol carbon-dioxide estimates, glacial "
     "deposits (or their absence), sulfur-isotope atmospheric constraints - into one quality-ranked database. Step "
     "2: run a climate-geochemistry model ensemble spanning the candidate recipes (high carbon dioxide, methane, "
     "low albedo, nitrogen effects), scoring each against the proxy database with identical metrics. Step 3: "
     "require the winning recipes to also satisfy the late-Archean constraints, when the paradox eases as the Sun "
     "brightens - a solution that only works at 4 billion years ago is suspect. Step 4: test whether the winning "
     "recipe is compatible with the origin and early evolution of life as independently understood.\n"
     "Assumptions: that Archean proxies are interpretable (paleosol carbon-dioxide estimates span an order of "
     "magnitude); that the model ensemble spans the true possibilities (cloud physics may surprise); that a single "
     "recipe dominated (the answer may be 'all of the above').\n"
     "What would confirm it: one recipe class fitting the full proxy record across the Archean, with independent "
     "lines of evidence - for example, methane consistent with both climate and sulfur isotopes - converging.\n"
     "What would kill it: proxies tightening to exclude every candidate recipe; the winning recipe requiring "
     "conditions contradicted by other Archean evidence; or proof that no steady recipe works and the early climate "
     "was wildly variable instead.\n"
     "What this does NOT claim: it does not claim a specific greenhouse mix today; it does not claim the proxies "
     "are reliable; it is a research program, not an established result."),
 "citations": [
     "Sagan C, Mullen G. Earth and Mars: evolution of atmospheres. Science; 1972.",
     "Feulner G. The faint young Sun problem. Rev Geophys; 2012.",
     "Catling D C, Zahnle K J. The Archean atmosphere. Sci Adv; 2020."],
 "explorer": {
   "blurb": ("A faint-sun forcing calculator: from the solar luminosity deficit and planetary albedo it computes "
             "the greenhouse forcing the young Earth needed - the size of the paradox in watts per square meter."),
   "assumptions": {"S0": 1361.0, "faint_fraction": 0.75, "albedo": 0.3},
   "model_src": (
     "def run(A):\n"
     "    deficit = (1.0 - A[\"faint_fraction\"]) * A[\"S0\"] / 4.0 * (1.0 - A[\"albedo\"])\n"
     "    return {\"forcing_deficit_Wm2\": deficit,\n"
     "            \"luminosity_percent\": A[\"faint_fraction\"] * 100.0}\n"),
   "steps": [("Missing solar forcing vs today", "forcing_deficit_Wm2", "W/m2"),
             ("Young-Sun luminosity", "luminosity_percent", "% of modern")],
   "confirm": ["One recipe class fits the full Archean proxy record.",
               "Independent proxies converge on the same greenhouse mix.",
               "The recipe stays compatible with early-life constraints."],
   "refute": ["Proxies tighten to exclude every candidate recipe.",
              "The winner contradicts other Archean evidence.",
              "No steady recipe works; the early climate was wildly variable."],
   "checks": [("forcing_deficit_Wm2", 45.0, 75.0)],
   "honesty": ("Sixty watts per square meter is an enormous missing forcing - several times the forcing "
               "from doubling carbon dioxide. The demo measures the paradox; the solution is still open."),
 }})
# ---------------------------------------------------------------- 28
ENTRIES.append({
 "key": "great-oxidation-event-cause",
 "name": "What Caused the Great Oxidation Event?",
 "group": "Geochemistry",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": ("Oxygen-producing photosynthesis existed long before oxygen accumulated in the atmosphere 2.4 billion "
             "years ago - and what finally tipped the balance is one of geochemistry's great unsolved whys."),
 "background": ("The Great Oxidation Event (GOE), about 2.4 billion years ago, transformed Earth's atmosphere from "
             "essentially oxygen-free to oxygen-bearing, recorded by the disappearance of mass-independent sulfur "
             "isotope fractionation and the appearance of red beds and banded iron formations giving way to "
             "oxidized sediments. Yet cyanobacteria - oxygenic photosynthesizers - left chemical traces hundreds "
             "of millions of years earlier. So why the delay? Competing answers invoke declining sinks: less "
             "reduced volcanic gas as the mantle oxidized or tectonics slowed, less ferrous iron to mop up oxygen, "
             "or a collapse of atmospheric methane that had been consuming oxygen. Others invoke rising sources: "
             "nutrient pulses boosting burial of organic carbon. The field has exquisite records of the transition "
             "and no consensus on its trigger."),
 "why_it_matters": ("The GOE made complex life possible and is the template for oxygen as a biosignature: "
             "astronomers hunting inhabited exoplanets look for exactly this transition. Understanding its trigger "
             "tells us whether oxygen atmospheres are a likely outcome of photosynthesis or a rare accident of "
             "planetary evolution. It also governs the deep-time carbon, sulfur, and iron cycles."),
 "sig_pointer": ("The Signature system proposes a source-sink tipping model constrained by sulfur and molybdenum "
             "isotopes to test sink-decline against source-increase triggers. See the Signature Edition record for "
             "the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the GOE as a tipping problem - sources and sinks tracked "
             "as competing curves, with the crossover, not the narrative, identifying the trigger."),
 "signature_solution": (
     "Proposed approach. Step 1: reconstruct oxygen source (organic carbon burial) and sink (reduced volcanic gases, "
             "iron oxidation, methane) fluxes through the late Archean with full uncertainties, from sulfur, "
             "molybdenum, chromium, and iron isotope systems. Step 2: build a tipping model where atmospheric oxygen "
             "rises when sources exceed sinks, and test which change - source increase or sink decline - produces "
     "the observed abruptness and timing. Step 3: derive distinct predictions: a sink-driven GOE predicts specific "
     "pre-transition changes in volcanic gas chemistry, while a source-driven one predicts burial pulses. Step 4: "
     "test against the highest-resolution sections, where the transition's fine structure discriminates triggers.\n"
     "Assumptions: that isotope proxies map cleanly to fluxes (each has competing interpretations); that the "
     "transition was globally synchronous (mostly, not perfectly); that the trigger was singular rather than a "
     "conspiracy of changes.\n"
     "What would confirm it: source and sink curves crossing at 2.4 Ga in the predicted direction, with the "
     "discriminating predictions verified in high-resolution sections.\n"
     "What would kill it: source and sink reconstructions that never cross without ad-hoc tuning; the transition's "
     "fine structure contradicting every single-trigger model; or proof that oxygen rose and fell multiple times, "
     "making 'the trigger' ill-posed.\n"
     "What this does NOT claim: it does not claim a specific trigger today; it does not claim oxygenic "
     "photosynthesis dates are settled; it is a research program, not an established result."),
 "citations": [
     "Farquhar J et al. Atmospheric influence of Earths earliest sulfur cycle. Science; 2000.",
     "Lyons T W et al. The rise of oxygen in Earths early ocean and atmosphere. Nature; 2014.",
     "Catling D C et al. Why O2 is required by complex life. Astrobiology; 2005."],
 "explorer": {
   "blurb": ("A GOE tipping-point finder: oxygen sources rising and reductant sinks falling over billions of years "
             "- the model finds when the source curve crosses the sink curve."),
   "assumptions": {"src0": 1.0, "src_g": 0.45, "snk0": 2.0, "snk_d": 0.15},
   "model_src": (
     "def run(A):\n"
     "    t = 4.0\n"
     "    cross = None\n"
     "    while t >= 1.5:\n"
     "        x = 4.0 - t\n"
     "        src = A[\"src0\"] * (1.0 + A[\"src_g\"] * x)\n"
     "        snk = A[\"snk0\"] * (1.0 - A[\"snk_d\"] * x)\n"
     "        if src > snk and cross is None:\n"
     "            cross = t\n"
     "        t -= 0.01\n"
     "    return {\"crossover_Ga\": cross if cross is not None else -1.0}\n"),
   "steps": [("Oxygenation crossover time", "crossover_Ga", "Ga before present")],
   "confirm": ["Source and sink curves cross at 2.4 Ga in the predicted direction.",
               "Discriminating predictions verify in high-resolution sections.",
               "Independent isotope systems agree on the flux histories."],
   "refute": ["Curves never cross without ad-hoc tuning.",
              "Fine structure contradicts every single-trigger model.",
              "Oxygen rose and fell repeatedly; the trigger is ill-posed."],
   "checks": [("crossover_Ga", 2.0, 3.0)],
   "honesty": ("Straight-line sources and sinks are placeholders. The real curves are what the "
               "isotope record must supply - and they are still being drawn."),
 }})
# ---------------------------------------------------------------- 29
ENTRIES.append({
 "key": "end-permian-extinction-kill",
 "name": "What Killed Almost Everything at the End of the Permian?",
 "group": "Paleoclimate",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": ("252 million years ago about 90% of marine species vanished in the largest extinction ever, triggered "
             "by Siberian volcanism - but the exact kill mechanism, or sequence of mechanisms, is still disputed."),
 "background": ("The end-Permian extinction coincides with the Siberian Traps, one of the largest volcanic "
             "outpourings in Earth history, emplaced through carbon-rich sediments that would have released "
             "enormous greenhouse gases. The carbon isotope record shows a sharp negative excursion, consistent "
             "with a massive injection of light carbon. But how the volcanism killed is debated: rapid warming, "
             "ocean anoxia and hydrogen sulfide poisoning, ocean acidification, ozone destruction by halogens, or a "
             "lethal sequence of several. High-resolution sections show the extinction was geologically abrupt but "
             "its internal structure - one pulse or several, and which groups died first - is still being worked out."),
 "why_it_matters": ("The end-Permian is the worst case in the geological record of volcanic carbon injection - the "
             "closest natural analog to rapid greenhouse forcing, and a warning about how fast the carbon cycle can "
             "be overwhelmed. Understanding the kill sequence tells us which modern stresses (warming, anoxia, "
             "acidification) are the dangerous ones and how they compound. It is also simply the greatest murder "
             "mystery in the history of life."),
 "sig_pointer": ("The Signature system proposes a high-resolution multi-proxy kill-sequence reconstruction coupled "
             "to Earth-system models of Traps degassing scenarios. See the Signature Edition record for the full "
             "labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the extinction as a sequence to be ordered - which "
             "stressor hit first, which compounded it, with the fossil record as the timeline and models as the "
             "suspects."),
 "signature_solution": (
     "Proposed approach. Step 1: build the highest-resolution timeline possible - temperature, anoxia, pH, and "
     "extinction horizons in the same sections - so the order of stresses and deaths is measured, not inferred. "
     "Step 2: run Earth-system models with Traps degassing scenarios (carbon dioxide, sulfur, halogens, sediment-"
     "derived carbon), each predicting a distinct stress sequence and carbon-isotope excursion. Step 3: score the "
     "scenarios against the timeline: a warming-first kill predicts different last occurrences than an anoxia-first "
     "kill. Step 4: test the winning scenario's carbon budget against the isotope excursion quantitatively - the "
     "mass of light carbon required must match a physically plausible degassing history.\n"
     "Assumptions: that the sections can be correlated at the needed resolution globally (challenging); that the "
     "models capture the relevant ocean chemistry (they approximate); that the fossil record's last occurrences "
     "reflect true extinction order (the Signor-Lipps effect smears it).\n"
     "What would confirm it: one degassing scenario reproducing the stress order, the extinction selectivity, and "
     "the isotope excursion together, across multiple independent sections.\n"
     "What would kill it: timelines that contradict every scenario's predicted order; the carbon budget requiring "
     "impossible degassing; or selectivity patterns matching no modeled stress.\n"
     "What this does NOT claim: it does not claim a single kill mechanism today; it does not claim the Traps "
     "alone suffice without sediment-derived gases; it is a research program, not an established result."),
 "citations": [
     "Erwin D H. The Permo-Triassic extinction. Annu Rev Ecol Syst; 1994.",
     "Svensen H et al. Siberian gas venting and the end-Permian environmental crisis. Earth Planet Sci Lett; 2009.",
     "Burgess S D et al. High-precision timeline for Earths most severe extinction. PNAS; 2014."],
 "explorer": {
   "blurb": ("A kill-carbon mass balance: from the size of the carbon-isotope excursion and the isotopic signature "
             "of the volcanic source it computes how much light carbon the extinction required."),
   "assumptions": {"ocean_C_GtC": 38000.0, "excursion": 4.0, "source_d13C": -25.0},
   "model_src": (
     "def run(A):\n"
     "    M = A[\"ocean_C_GtC\"] * abs(A[\"excursion\"]) / abs(A[\"source_d13C\"])\n"
     "    return {\"light_carbon_GtC\": M,\n"
     "            \"excursion_permil\": float(A[\"excursion\"])}\n"),
   "steps": [("Carbon-isotope excursion size", "excursion_permil", "permil"),
             ("Required light-carbon injection", "light_carbon_GtC", "GtC")],
   "confirm": ["One scenario reproduces stress order, selectivity, and isotopes together.",
               "The carbon budget matches a plausible degassing history.",
               "Multiple independent sections agree on the timeline."],
   "refute": ["Timelines contradict every scenario's predicted order.",
              "The budget requires impossible degassing.",
              "Selectivity matches no modeled stress."],
   "checks": [("light_carbon_GtC", 3.0e3, 1.2e4)],
   "honesty": ("Mass balance is exact arithmetic on uncertain inputs - the ocean carbon inventory and "
               "the source signature both carry wide error bars. The demo sizes the crime, not the culprit."),
 }})
# ---------------------------------------------------------------- 30
ENTRIES.append({
 "key": "earth-missing-heat",
 "name": "Where Does Earths Missing Heat Come From?",
 "group": "Geodynamics",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": ("Earth radiates about 47 terawatts of heat, but radioactive decay accounts for only around 20 - and "
             "the source and distribution of the rest is one of geophysics' longest-running puzzles."),
 "background": ("Surface heat-flow measurements sum to roughly 47 terawatts leaving the planet. Radioactive decay "
             "of uranium, thorium, and potassium - the known internal heat source - supplies perhaps 20 terawatts, "
             "giving a Urey ratio (radiogenic over total) near 0.4. The remainder is 'secular cooling': primordial "
             "heat left over from formation and core segregation. But that implies Earth is cooling fast, which "
             "conflicts with evidence for a long-lived geodynamo and vigorous ancient tectonics unless the mantle's "
             "radioactive element distribution is very different from assumed. Geoneutrino detectors (KamLAND, "
             "Borexino, and soon JUNO) now measure radiogenic heat directly from particle fluxes - and their "
             "answers, while consistent with ~20 terawatts, still allow a wide range."),
 "why_it_matters": ("The heat budget is the boundary condition for everything inside Earth: mantle convection "
             "vigor, plate-tectonic history, core cooling rate, and the geodynamo's power all derive from it. A "
             "hotter, faster-cooling Earth has a different past and future than a cooler one. Resolving the budget "
             "would unify thermal history, geochemistry, and geodynamics in one consistent picture."),
 "sig_pointer": ("The Signature system proposes using geoneutrino measurements to map radiogenic heat directly, "
             "closing the budget observation by observation. See the Signature Edition record for the full labeled "
             "proposal."),
 "sig_lens": ("Signature lens: the Signature system treats Earth's heat as an audited budget - every terawatt "
             "assigned to a source by measurement, with the unassigned remainder shrinking as detectors improve."),
 "signature_solution": (
     "Proposed approach. Step 1: expand geoneutrino detection - larger detectors, oceanic sites far from continental "
     "crust - to measure the mantle's radiogenic heat separately from the crust's, ending reliance on compositional "
     "models. Step 2: reconcile the geoneutrino heat with surface heat flow region by region, so the secular-cooling "
     "remainder is mapped, not just globally averaged. Step 3: test the implied cooling history against the "
     "paleomagnetic and tectonic records: the cooling rate must sustain the observed 3.5-billion-year dynamo and "
     "the inferred tectonic vigor. Step 4: if the books still do not balance, quantify exactly how much heat is "
     "missing and where - turning the puzzle into a targeted hunt.\n"
     "Assumptions: that geoneutrino fluxes convert cleanly to heat (they depend on element ratios); that oceanic "
     "detectors are feasible at scale (proposed, not built); that the surface heat-flow census is complete "
     "(oceanic coverage is thin).\n"
     "What would confirm it: mantle geoneutrino heat converging with compositional models, a cooling history "
     "consistent with the dynamo and tectonic records, and the missing heat shrinking to within uncertainties.\n"
     "What would kill it: geoneutrinos demanding far more or less radiogenic heat than any compositional model "
     "allows; the implied cooling history contradicting the magnetic record; or the missing heat growing as "
     "measurements improve.\n"
     "What this does NOT claim: it does not claim the budget is closed today; it does not claim any exotic heat "
     "source is real; it is a research program, not an established result."),
 "citations": [
     "Davies J H, Davies D R. Earths surface heat flux. Solid Earth; 2010.",
     "Araki T et al. Experimental investigation of geologically produced antineutrinos (KamLAND). Nature; 2005.",
     "Jaupart C et al. Temperatures, heat and energy in the mantle of the Earth. Treatise on Geophysics; 2015."],
 "explorer": {
   "blurb": ("A planetary heat-budget audit: from surface heat flow and radiogenic production it computes the "
             "Urey ratio and the secular-cooling remainder - the famous missing heat."),
   "assumptions": {"surface_TW": 47.0, "radiogenic_TW": 20.0},
   "model_src": (
     "def run(A):\n"
     "    Qs = A[\"surface_TW\"]\n"
     "    Qr = A[\"radiogenic_TW\"]\n"
     "    return {\"urey_ratio\": Qr / Qs,\n"
     "            \"secular_cooling_TW\": Qs - Qr,\n"
     "            \"surface_TW\": Qs}\n"),
   "steps": [("Total surface heat flow", "surface_TW", "TW"),
             ("Urey ratio (radiogenic share)", "urey_ratio", ""),
             ("Secular cooling remainder", "secular_cooling_TW", "TW")],
   "confirm": ["Geoneutrino heat converges with compositional models.",
               "Cooling history sustains the 3.5 Gyr dynamo record.",
               "The missing heat shrinks within uncertainties."],
   "refute": ["Geoneutrinos demand impossible radiogenic heat.",
              "Cooling history contradicts the magnetic record.",
              "The missing heat grows as measurements improve."],
   "checks": [("urey_ratio", 0.3, 0.55), ("secular_cooling_TW", 20.0, 35.0)],
   "honesty": ("Two numbers divide into a ratio - the puzzle is that the ratio demands faster cooling "
               "than much of Earth history seems to allow."),
 }})
# ---------------------------------------------------------------- 31
ENTRIES.append({
 "key": "deep-nitrogen-cycle",
 "name": "Where Does Deep Nitrogen Go?",
 "group": "Geochemistry",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": ("Nitrogen subducts into the mantle with oceanic plates, but how much stays down there - possibly more "
             "than in the entire atmosphere - is barely measured."),
 "background": ("Nitrogen is the main gas of the atmosphere, yet its deep cycle is among the least quantified of "
             "any volatile. Subducting slabs carry nitrogen as ammonium substituting for potassium in minerals, and "
             "arc volcanoes return only a fraction of it. Mineral-solubility experiments suggest mantle minerals "
             "can store parts-per-million nitrogen - which, integrated over the mantle's mass, could rival or "
             "exceed the atmospheric inventory. The deep nitrogen budget matters because atmospheric pressure "
             "affects climate (pressure broadening of greenhouse absorption) and because nitrogen is a bioessential "
             "element whose surface availability may have been set by deep cycling."),
 "why_it_matters": ("If the mantle holds more nitrogen than the air, then the atmosphere is the small, exchangeable "
             "tip of a deep reservoir - and atmospheric pressure over geological time was set by mantle processes, "
             "not just outgassing. That rewrites Archean climate calculations and the conditions for life's "
             "emergence. For exoplanets, deep nitrogen storage decides whether nitrogen atmospheres are stable or "
             "drained into interiors."),
 "sig_pointer": ("The Signature system proposes measuring nitrogen in mantle minerals and xenoliths plus "
             "subduction-zone outputs to close the deep nitrogen budget directly. See the Signature Edition record "
             "for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats deep nitrogen as an inventory to be taken, not a "
             "parameter to be assumed - every reservoir measured, the imbalance published."),
 "signature_solution": (
     "Proposed approach. Step 1: measure nitrogen contents systematically in mantle xenoliths, mid-ocean-ridge "
             "basalts, and ocean-island basalts with modern high-sensitivity techniques, building the first "
             "representative deep-nitrogen dataset. Step 2: quantify subduction inputs (sediment and altered-crust "
             "nitrogen) and arc outputs at representative margins to get the net deep flux. Step 3: determine "
             "nitrogen solubility in the major mantle minerals at relevant conditions, so the inventory can be "
             "scaled from samples to the whole mantle honestly. Step 4: assemble the budget - atmosphere, crust, "
             "mantle - with uncertainties, and test whether the implied atmospheric evolution matches independent "
             "paleo-pressure proxies.\n"
     "Assumptions: that xenoliths and basalts sample the mantle representatively (they sample the shallow, "
     "melt-extracted parts); that nitrogen behaves compatibly enough to scale (its partitioning is poorly known); "
     "that paleo-pressure proxies are reliable (they are few).\n"
     "What would confirm it: independent sample suites converging on the same mantle inventory, the budget closing "
     "within uncertainties, and the implied pressure history matching paleo-barometers.\n"
     "What would kill it: measurements scattering across orders of magnitude with no convergence; the budget "
     "requiring unphysical fluxes; or paleo-pressure data contradicting the implied history.\n"
     "What this does NOT claim: it does not claim a specific mantle inventory today; it does not claim nitrogen "
     "controls Archean climate; it is a research program, not an established result."),
 "citations": [
     "Marty B, Dauphas N. The nitrogen record of crust-mantle interaction. Earth Planet Sci Lett; 2003.",
     "Johnson B, Goldblatt C. The nitrogen budget of Earth. Earth Sci Rev; 2015.",
     "Busigny V, Dauphas N. Tracing the deep nitrogen cycle. Nat Geosci; 2015."],
 "explorer": {
   "blurb": ("A deep-nitrogen inventory estimator: from mantle nitrogen concentration and mantle mass it computes "
             "the deep reservoir and compares it to the atmosphere."),
   "assumptions": {"mantle_ppm": 2.0, "mantle_kg": 4.0e24, "atm_kg": 4.0e18},
   "model_src": (
     "def run(A):\n"
     "    mantle_N = A[\"mantle_ppm\"] * 1.0e-6 * A[\"mantle_kg\"]\n"
     "    return {\"mantle_N_kg\": mantle_N,\n"
     "            \"mantle_over_atmosphere\": mantle_N / A[\"atm_kg\"]}\n"),
   "steps": [("Mantle nitrogen inventory", "mantle_N_kg", "kg"),
             ("Mantle inventory vs atmosphere", "mantle_over_atmosphere", "x atmosphere")],
   "confirm": ["Independent sample suites converge on one mantle inventory.",
               "The budget closes within uncertainties.",
               "Implied pressure history matches paleo-barometers."],
   "refute": ["Measurements scatter across orders of magnitude.",
              "The budget requires unphysical fluxes.",
              "Paleo-pressure data contradict the implied history."],
   "checks": [("mantle_over_atmosphere", 1.0, 4.0)],
   "honesty": ("Two parts per million times the mantle's mass is an enormous number - and the two parts "
               "per million is measured at only a handful of sites."),
 }})
# ---------------------------------------------------------------- 32
ENTRIES.append({
 "key": "biological-carbon-pump",
 "name": "How Strong Is the Oceans Biological Carbon Pump?",
 "group": "Oceans",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": ("Ocean life exports carbon to the deep sea, but the efficiency of this biological carbon pump - and "
             "how it will change as the ocean warms - is uncertain enough to matter for the global carbon budget."),
 "background": ("Phytoplankton fix carbon at the surface; a fraction sinks as particles or is transported by "
             "migrating animals into the deep ocean, where it stays for centuries - the biological carbon pump. "
             "Its strength is measured by the export efficiency (the 'e-ratio'): the fraction of surface production "
             "that leaves the sunlit zone. Estimates vary widely by region and method - sediment traps, thorium "
             "disequilibrium, autonomous floats - and the processes that attenuate sinking particles (remineralization "
             "by microbes and zooplankton in the twilight zone) are among the least observed in oceanography. "
             "Warming-driven stratification may weaken the pump, reducing the ocean's carbon uptake, but the sign "
             "and size of the change are not settled."),
 "why_it_matters": ("The biological pump moves roughly 5 to 10 gigatons of carbon per year into the deep ocean - "
             "comparable to human emissions - and without it atmospheric carbon dioxide would be far higher. Its "
             "future is a first-order uncertainty in carbon budgets: a weakening pump means more of our emissions "
             "stay airborne. It also feeds the deep-sea ecosystems we are only beginning to explore."),
 "sig_pointer": ("The Signature system proposes global autonomous-float export monitoring plus twilight-zone process "
             "studies to measure the pump's efficiency and its climate sensitivity directly. See the Signature "
             "Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the biological pump as a flux to be measured in situ - "
             "export efficiency mapped by the observing system, not inferred from models."),
 "signature_solution": (
     "Proposed approach. Step 1: expand the Biogeochemical-Argo float array to measure export flux globally and "
     "continuously, replacing sparse ship-based snapshots with a living map. Step 2: target the twilight zone with "
     "process studies - imaging, tracers, and incubations - to quantify what eats sinking particles and how fast, "
     "the least-known link in the chain. Step 3: run perturbation experiments (natural and deliberate) to measure "
     "how export efficiency responds to warming and stratification, rather than assuming the response. Step 4: "
     "assimilate the observations into carbon-cycle models and verify the models against independent atmospheric "
     "carbon-dioxide constraints.\n"
     "Assumptions: that floats measure export representatively (they miss episodic pulses and large particles); "
     "that twilight-zone processes studied locally scale globally (uncertain); that the pump's climate response is "
     "measurable within a decade (the signal may be slow).\n"
     "What would confirm it: float-derived export converging with independent methods, process studies closing the "
     "twilight-zone budget, and models with the new pump reproducing atmospheric carbon-dioxide history.\n"
     "What would kill it: export estimates refusing to converge across methods; the pump shown insensitive to the "
     "variables models use; or the climate response proving unmeasurable within any practical timeframe.\n"
     "What this does NOT claim: it does not claim a specific pump strength today; it does not claim the pump will "
     "weaken; it is a research program, not an established result."),
 "citations": [
     "Volk T, Hoffert M I. Ocean carbon pumps. In: The Carbon Cycle and Atmospheric CO2; 1985.",
     "Henson S A et al. A reduced estimate of the strength of the ocean biological carbon pump. Global Biogeochem Cycles; 2011.",
     "Boyd P W et al. Multi-faceted particle pumps. Nature; 2019."],
 "explorer": {
   "blurb": ("A biological-pump efficiency calculator: from surface export flux and the Martin attenuation curve "
             "it computes how much carbon reaches depth - and the export efficiency that results."),
   "assumptions": {"F100": 10.0, "z": 200.0, "b": 0.86, "NPP": 45.0},
   "model_src": (
     "def run(A):\n"
     "    export = A[\"F100\"] * (A[\"z\"] / 100.0) ** (-A[\"b\"])\n"
     "    eff = export / A[\"NPP\"]\n"
     "    return {\"export_flux\": export, \"efficiency\": eff}\n"),
   "steps": [("Export flux at depth", "export_flux", "gC/m2/yr"),
             ("Export efficiency (e-ratio)", "efficiency", "")],
   "confirm": ["Float-derived export converges with independent methods.",
               "Twilight-zone process studies close the budget.",
               "Models with the new pump reproduce carbon-dioxide history."],
   "refute": ["Export estimates refuse to converge across methods.",
              "The pump proves insensitive to modeled variables.",
              "Climate response unmeasurable on practical timescales."],
   "checks": [("efficiency", 0.08, 0.18)],
   "honesty": ("The Martin curve is an empirical fit, not a law - and the twilight zone it describes "
               "is the least-observed habitat on Earth. The demo computes the curve, not its truth."),
 }})
# ---------------------------------------------------------------- 33
ENTRIES.append({
 "key": "deep-ocean-ventilation-age",
 "name": "How Long Does Deep Water Stay in the Deep Ocean?",
 "group": "Oceans",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": ("Water in the deep Pacific last touched the surface over a thousand years ago, but exactly how the "
             "deep ocean ventilates - and how that changed in ice ages - remains poorly quantified."),
 "background": ("Radiocarbon dating of deep water shows the deep Pacific is the oldest water in the ocean, with "
             "apparent ages over a thousand years - the time since it sank in the North Atlantic or around "
             "Antarctica and crept northward. This ventilation timescale sets how fast the ocean absorbs heat and "
             "carbon: the deep ocean is the climate system's long memory. But 'age' conflates circulation pathways "
             "with mixing, and models disagree on both. During the last ice age, the deep ocean stored far more "
             "carbon - implying different ventilation - yet reconstructions of glacial circulation disagree on "
             "whether the deep ocean was better or worse ventilated. The mixing rates that set all of this are "
             "parameterized, not resolved, in climate models."),
 "why_it_matters": ("Deep-ocean ventilation is the timescale of committed climate change: heat and carbon entering "
             "the deep ocean will return over centuries to millennia. Ice-age carbon storage shows the deep ocean "
             "can swing atmospheric carbon dioxide by tens of parts per million - the difference between glacial "
             "and interglacial worlds. Understanding ventilation is understanding the climate system's inertia."),
 "sig_pointer": ("The Signature system proposes transient-tracer inversions with eddy-resolving models to map "
             "ventilation pathways and timescales directly. See the Signature Edition record for the full labeled "
             "proposal."),
 "sig_lens": ("Signature lens: the Signature system treats deep ventilation as a transit-time problem - tracers "
             "in, pathways out, with mixing measured rather than parameterized."),
 "signature_solution": (
     "Proposed approach. Step 1: sustain and expand the transient-tracer observing system - radiocarbon, CFCs, "
     "sulfur hexafluoride - that timestamps water parcels throughout the deep ocean. Step 2: invert the tracer "
     "fields with eddy-resolving ocean models to map ventilation pathways and transit-time distributions, "
     "separating advection from mixing explicitly. Step 3: apply the same machinery to the last ice age using "
     "paleo-tracers (radiocarbon in deep-sea corals, neodymium isotopes), testing whether models can reproduce "
     "glacial carbon storage. Step 4: use the validated models to project how ventilation changes as the ocean "
     "warms and stratifies.\n"
     "Assumptions: that tracers are sufficient to separate pathways from mixing (underdetermined in places); that "
     "paleo-tracers record circulation faithfully (each has non-circulation influences); that eddy-resolving "
     "models capture the real mixing physics (they approximate sub-grid processes).\n"
     "What would confirm it: tracer inversions converging on consistent transit-time maps, successful hindcasts of "
     "glacial carbon storage, and projected ventilation changes that verify against the ongoing record.\n"
     "What would kill it: inversions that remain underdetermined no matter the data; paleo-tracers contradicting "
     "each other irreconcilably; or models that cannot reproduce glacial storage under any circulation.\n"
     "What this does NOT claim: it does not claim a specific ventilation age today beyond the measured ranges; it "
     "does not claim to know glacial circulation; it is a research program, not an established result."),
 "citations": [
     "Matsumoto K. Radiocarbon-based circulation age of the world oceans. J Geophys Res; 2007.",
     "DeVries T, Primeau F. Dynamically and observationally constrained estimates of water-mass distributions. J Phys Oceanogr; 2011.",
     "Skinner L C et al. Reduced ventilation and enhanced carbon storage in the glacial deep ocean. Science; 2017."],
 "explorer": {
   "blurb": ("A deep-water age calculator: from the radiocarbon content of deep versus surface water it computes "
             "the ventilation age - how long since the deep Pacific breathed the atmosphere."),
   "assumptions": {"deep_ratio": 0.85, "surface_ratio": 1.0},
   "model_src": (
     "def run(A):\n"
     "    import math\n"
     "    t = -8033.0 * math.log(A[\"deep_ratio\"] / A[\"surface_ratio\"])\n"
     "    return {\"ventilation_age_yr\": t}\n"),
   "steps": [("Deep-water ventilation age", "ventilation_age_yr", "years")],
   "confirm": ["Tracer inversions converge on consistent transit-time maps.",
               "Models hindcast glacial carbon storage successfully.",
               "Projected ventilation changes verify against observations."],
   "refute": ["Inversions remain underdetermined regardless of data.",
              "Paleo-tracers contradict each other irreconcilably.",
              "No model reproduces glacial storage under any circulation."],
   "checks": [("ventilation_age_yr", 1000.0, 1600.0)],
   "honesty": ("Radiocarbon age mixes circulation time with mixing - two waters can share an age with "
               "different histories. The demo computes the clock reading, not the journey."),
 }})
# ---------------------------------------------------------------- 34
ENTRIES.append({
 "key": "earth-volatile-budget",
 "name": "What Is Earths Complete Volatile Budget?",
 "group": "Planetary Formation",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": ("Nobody has closed the books on Earth's water, carbon, and nitrogen - delivered, lost, and stored - "
             "from formation to today, and the imbalance is where the next discoveries hide."),
 "background": ("Every volatile on Earth has a life story: delivered by planetesimals or ingassed from the nebula, "
             "partitioned between atmosphere, oceans, crust, and mantle, lost to space by escape or to the deep "
             "interior by subduction. For water, carbon, and nitrogen separately, the inventories are uncertain - "
             "especially the mantle reservoirs - and the delivery-versus-loss accounting has never been closed in "
             "one framework. Chondritic meteorites provide the starting composition, atmospheric escape physics sets "
             "the losses, and subduction sets the deep recycling. Assembled together, the budget should balance: "
             "delivery minus loss equals inventory. It does not - and the size and location of the imbalance point "
             "at what we understand least."),
 "why_it_matters": ("The volatile budget is the grand inventory of the habitable planet: it unifies formation, "
             "tectonics, and climate in one accounting. Closing it would test whole-Earth models end to end - any "
             "model of Earth's history must reproduce the final books. And the budget is the template for judging "
             "exoplanet habitability: delivery, retention, and cycling decide which worlds keep their oceans and air."),
 "sig_pointer": ("The Signature system proposes building the audited volatile inventory as a living database - "
             "every reservoir, every flux, every uncertainty - and letting the imbalance set the research agenda. "
             "See the Signature Edition record for the full labeled proposal."),
 "sig_lens": ("Signature lens: the Signature system treats the volatile budget as the master ledger - water, "
             "carbon, and nitrogen accounted together, with the unbalanced lines published as the field's to-do list."),
 "signature_solution": (
     "Proposed approach. Step 1: compile the reservoir inventory - atmosphere, oceans, crust, mantle - for water, "
             "carbon, and nitrogen in one database with uniform uncertainties, ending the era of incompatible "
             "one-volatile accountings. Step 2: compile the flux history - delivery from formation models, escape "
             "from atmospheric physics, subduction recycling from the volatile records - on the same ledger. Step 3: "
             "compute the imbalance for each volatile and rank the budget lines by their contribution to it, so the "
             "field works on the leakiest lines first. Step 4: maintain the budget as a living, versioned resource "
             "that updates as mantle inventories, escape rates, and delivery models improve.\n"
     "Assumptions: that the reservoir list is complete (deep reservoirs may be missing); that formation models give "
     "meaningful delivery estimates (they span wide ranges); that the three volatiles' budgets are independent "
     "enough to close separately (they interact chemically).\n"
     "What would confirm it: the imbalances shrinking toward zero as measurements improve, with the remaining "
     "gaps pointing at specific reservoirs or fluxes that new missions then fill.\n"
     "What would kill it: imbalances that grow as data improve - implying a fundamentally missing process; or the "
     "volatiles proving so coupled that separate budgets are meaningless.\n"
     "What this does NOT claim: it does not claim the budget is closed today; it does not claim any delivery "
     "scenario is correct; it is a research program, not an established result."),
 "citations": [
     "Marty B. The origins and concentrations of water, carbon, nitrogen and noble gases on Earth. Earth Planet Sci Lett; 2012.",
     "Hirschmann M M. Magma ocean influence on volatile budgets. Annu Rev Earth Planet Sci; 2016.",
     "Peslier A H et al. Water in the Earths interior. Space Sci Rev; 2017."],
 "explorer": {
   "blurb": ("A volatile-budget auditor: it sums the water reservoirs - ocean, crust, mantle - and compares the "
             "total to the chondritic delivery estimate, computing the closure ratio."),
   "assumptions": {"ocean_Gt": 1.4e12, "crust_Gt": 0.2e12, "mantle_Gt": 2.7e12, "chondritic_Gt": 5.0e12},
   "model_src": (
     "def run(A):\n"
     "    total = A[\"ocean_Gt\"] + A[\"crust_Gt\"] + A[\"mantle_Gt\"]\n"
     "    return {\"total_Gt\": total,\n"
     "            \"delivery_ratio\": total / A[\"chondritic_Gt\"],\n"
     "            \"ocean_Gt\": float(A[\"ocean_Gt\"]),\n"
     "            \"mantle_Gt\": float(A[\"mantle_Gt\"])}\n"),
   "steps": [("Total water inventory", "total_Gt", "Gt"),
             ("Inventory vs chondritic delivery", "delivery_ratio", ""),
             ("Ocean reservoir", "ocean_Gt", "Gt"),
             ("Mantle reservoir", "mantle_Gt", "Gt")],
   "confirm": ["Imbalances shrink toward zero as measurements improve.",
               "Remaining gaps point at specific reservoirs new missions fill.",
               "The ledger reproduces independent formation-model expectations."],
   "refute": ["Imbalances grow as data improve - a missing process.",
              "Volatiles prove too coupled for separate budgets.",
              "Delivery estimates refuse to converge."],
   "checks": [("delivery_ratio", 0.5, 1.5), ("total_Gt", 3.0e12, 6.0e12)],
   "honesty": ("The mantle reservoir dominates the total and is the least measured - the demo's "
               "closure ratio is only as good as that number, which is the point."),
 }})
